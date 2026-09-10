"""Bundles an assignment repository into a single .txt file for submission.

Run this from the ROOT of your project repository:

    python3 munger.py

It asks for your student ID, your name, and which submission this is, then
writes <ID>_<Name>_takehome_bundle.txt or <ID>_<Name>_inclass_bundle.txt
containing your git commit history, your project tree, and the contents of
every source/test/config/design file it finds.

The take-home and in-class submissions go to DIFFERENT Google Forms. Upload
each bundle through the form for that submission.

DO NOT MODIFY THIS FILE. Every bundle records the SHA-256 of the script that
produced it, and that digest is checked against the published one when your
submission is graded. A modified munger is treated as a submission integrity
problem, not a clever workaround.

It is still your responsibility to open the bundle and confirm your work is
in it before you upload. If this script misses something your project needs
included, email the instructor - do not edit the script.
"""

import hashlib
import os
import re
import subprocess

# Configure what to include/exclude
ALLOWED_EXTENSIONS = {
    # C / C++
    '.h', '.hpp', '.hh', '.c', '.cpp', '.cc', '.cxx',
    # JVM
    '.java', '.kt', '.kts', '.gradle',
    # Python
    '.py', '.toml', '.cfg',
    # JavaScript / TypeScript
    '.js', '.mjs', '.cjs', '.ts',
    # .NET
    '.cs', '.csproj',
    # Swift
    '.swift',
    # docs, design, config
    '.md', '.txt', '.json', '.xml', '.yml', '.yaml',
    '.mmd', '.puml', '.uml', '.dot', '.pseudo',
}

IGNORE_DIRS = {
    '.git', '.idea', '.vscode', 'bin', 'obj', 'out', 'build', 'node_modules',
    '__pycache__', 'target', '.gradle', 'cmake-build-debug', 'cmake-build-release',
    '.pytest_cache', '.mypy_cache', '.ruff_cache', 'venv', '.venv', 'env',
    'dist', '_build', 'coverage', '.tox', 'Debug', 'Release',
}

# Generated documentation. Listed in the tree with a file count, so the grader
# can see the docs were actually generated, but not dumped into the bundle -
# a Doxygen HTML tree would bury your actual work under megabytes of markup.
DOC_DIRS = {'doc', 'docs', 'javadoc', 'apidocs'}


def clean_string(text):
    """Removes special characters to create a safe filename."""
    return re.sub(r'[^a-zA-Z0-9]', '_', text.strip())


def is_bundle(filename):
    """True for any bundle this script has produced.

    Matches previous runs as well as the current one, so that the in-class
    bundle does not end up containing the whole take-home bundle.

    @param filename a bare filename, not a path
    @return whether the file is a munger bundle
    """
    return filename.endswith('_bundle.txt')


def generate_tree(dir_path, prefix=""):
    """Recursively builds a string representation of the directory structure."""
    tree_str = ""
    try:
        items = sorted(os.listdir(dir_path))
    except PermissionError:
        return ""

    # Filter out hidden files, ignored directories, and any bundle files
    items = [i for i in items if not i.startswith('.') and not is_bundle(i) and not (os.path.isdir(os.path.join(dir_path, i)) and i in IGNORE_DIRS)]

    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "

        if os.path.isdir(path) and item in DOC_DIRS:
            tree_str += f"{prefix}{connector}{item}/  [{count_files(path)} generated files, not bundled]\n"
            continue

        tree_str += f"{prefix}{connector}{item}\n"

        if os.path.isdir(path):
            extension = "    " if is_last else "│   "
            tree_str += generate_tree(path, prefix + extension)
    return tree_str


def count_files(dir_path):
    """Counts every file beneath a directory, for the generated-docs summary."""
    total = 0
    for _, _, files in os.walk(dir_path):
        total += len(files)
    return total


def self_digest():
    """SHA-256 of this script, so a grader can confirm it wasn't modified."""
    try:
        with open(os.path.abspath(__file__), 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception as e:
        return f"[could not hash munger.py: {e}]"


def get_git_log(root_dir):
    """Returns this repo's commit history, or a note explaining why it can't."""
    if not os.path.isdir(os.path.join(root_dir, '.git')):
        return ("[No .git directory found here. Run this script from your repository\n"
                " root. If you didn't use git, rubric item 2 cannot be credited.]\n")
    try:
        result = subprocess.run(
            ['git', 'log', '--date=short', '--pretty=format:%h  %ad  %an  %s'],
            cwd=root_dir, capture_output=True, text=True, timeout=30
        )
        log = result.stdout.strip()
        if not log:
            return "[Git repository found, but it has no commits.]\n"
        count = len(log.splitlines())
        return f"{log}\n\n({count} commits)\n"
    except Exception as e:
        return f"[Could not read git history: {e}]\n"


def ask_submission_kind():
    """Asks which of the two submissions this bundle is for.

    The take-home and in-class bundles go to DIFFERENT Google Forms and are
    graded against different rubric items, so they must be distinguishable
    from the filename alone.

    @return a (slug, description) pair, or None if the answer was unusable
    """
    print("\nWhich submission is this?")
    print("  1. Take-home  - the work you did during the week, due at the start of class")
    print("  2. In-class   - Part B, the extension you built during the session")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        return ("takehome", "take-home (due at the start of class)")
    if choice == "2":
        return ("inclass", "in-class Part B (due before the session ends)")
    return None


def main():
    print("=== CSC 582 Submission Bundler ===")
    student_id = input("Enter your Student ID: ").strip()
    student_name = input("Enter your First and Last Name: ").strip()

    if not student_id or not student_name:
        print("Error: Name and ID are required.")
        return

    kind = ask_submission_kind()
    if kind is None:
        print("Error: enter 1 for the take-home submission or 2 for the in-class one.")
        return
    slug, description = kind

    safe_id = clean_string(student_id)
    safe_name = clean_string(student_name)
    output_filename = f"{safe_id}_{safe_name}_{slug}_bundle.txt"

    root_dir = os.getcwd()

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        # 1. Write the metadata header
        outfile.write(f"STUDENT NAME: {student_name}\n")
        outfile.write(f"STUDENT ID: {student_id}\n")
        outfile.write(f"SUBMISSION: {description}\n")
        outfile.write(f"MUNGER SHA-256: {self_digest()}\n")
        outfile.write("=" * 40 + "\n\n")

        # 2. Write the commit history (evidence of incremental work)
        outfile.write("GIT COMMIT HISTORY:\n")
        outfile.write(get_git_log(root_dir))
        outfile.write("\n" + "=" * 40 + "\n\n")

        # 3. Write the directory tree
        outfile.write("PROJECT STRUCTURE:\n")
        outfile.write(generate_tree(root_dir))
        outfile.write("\n" + "=" * 40 + "\n\n")

        # 4. Write the file contents
        outfile.write("SOURCE FILES:\n\n")

        files_processed = 0
        own_files = 0
        for current_dir, dirs, files in os.walk(root_dir):
            # Modify dirs in-place to skip ignored and generated-docs directories
            dirs[:] = sorted(d for d in dirs
                             if not d.startswith('.') and d not in IGNORE_DIRS and d not in DOC_DIRS)

            for file in sorted(files):
                ext = os.path.splitext(file)[1].lower()
                if ext in ALLOWED_EXTENSIONS and not is_bundle(file):
                    filepath = os.path.join(current_dir, file)
                    rel_path = os.path.relpath(filepath, root_dir)

                    outfile.write(f"--- START FILE: {rel_path} ---\n")
                    try:
                        # errors='replace' prevents crashes on weird character encodings
                        with open(filepath, 'r', encoding='utf-8', errors='replace') as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        outfile.write(f"[Error reading file: {e}]\n")
                    outfile.write(f"\n--- END FILE: {rel_path} ---\n\n")
                    files_processed += 1
                    if os.path.abspath(filepath) != os.path.abspath(__file__):
                        own_files += 1

    print(f"\nBundled {files_processed} files, plus git history and project tree.")
    print(f"Output saved to: {output_filename}")

    if own_files == 0:
        print("\nWARNING: this bundle contains none of your work - only munger.py itself.")
        print("Are you in your project's root directory, and do your files use")
        print("extensions this script knows about? Do not submit this bundle.")
    else:
        form = "TAKE-HOME" if slug == "takehome" else "IN-CLASS"
        print("Open it, skim it, confirm your work is actually in there, then")
        print(f"upload it through the {form} submission Google Form.")
        print("The two submissions use different forms - check you have the right one.")


if __name__ == "__main__":
    main()
