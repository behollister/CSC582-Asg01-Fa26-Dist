# Walk-through: setting up, and testing your submission before submission day

Do this **on day one**, not the night before. The point is to prove the whole pipeline works —
repository, style tool, tests, docs, bundle — while it's still cheap to discover that something
doesn't. Budget half an hour.

Nothing here depends on which language you picked. Commands are shown for Linux/macOS; on Windows
use PowerShell or WSL and adjust paths.

---

## Step 0 — Verify your copy of the munger

`munger.py` is what turns your project into the single file you submit, and **it must not be
modified** (§10 of the handout). Check that your copy is the one that was distributed:

```
sha256sum munger.py
```

macOS:

```
shasum -a 256 munger.py
```

Compare the output against the digest in `CHECKSUMS.txt` and in §10 of the assignment PDF. They
must match exactly. If they don't, re-download the starter package — don't try to fix it by hand.

To check the whole package at once, from the package directory:

```
sha256sum -c CHECKSUMS.txt        # Linux
shasum -a 256 -c CHECKSUMS.txt    # macOS
```

Every line should say `OK`. Do this against a fresh copy of the package — once you start working,
your own files will differ from the distributed ones, which is the point.

## Step 1 — Make your project directory a git repository

Copy the starter package contents into a working directory of your own, then:

```
cd ~/csc582-adder        # wherever you're working
git init
git add .
git commit -m "Initial commit: starter package"
```

That's your first of at least fifteen commits (rubric item 2). A local repository is all you
need — no GitHub account, no remote.

## Step 2 — Do a dry run of the munger, right now

Before you've written a single line of your own code, run the bundler on the starter package as
it stands:

```
python3 munger.py
```

It asks three things: your student ID, your name, and **which submission this is**. Answer `1`
(take-home) for this rehearsal. It then writes `<ID>_<Name>_takehome_bundle.txt` into the current
directory.

There are two submissions this term, and they produce two differently-named files that go to two
different Google Forms:

| Answer | Bundle filename | Form | Due |
|---|---|---|---|
| `1` take-home | `<ID>_<Name>_takehome_bundle.txt` | [https://forms.gle/8BxR4VmePRjMWs5s9](https://forms.gle/8BxR4VmePRjMWs5s9) | start of class |
| `2` in-class | `<ID>_<Name>_inclass_bundle.txt` | given out during the session | before the session ends |

Because the names differ, running it a second time on session day won't overwrite your take-home
bundle, and a leftover bundle never gets swept into a later one.

This is a rehearsal — the output isn't worth submitting yet, but running it now tells you whether
Python works on your machine, whether you're in the right directory, and what the bundle actually
looks like.

## Step 3 — Read the bundle you just produced

Open the `.txt` file in an editor. You should see four sections in order:

```
STUDENT NAME: ...
STUDENT ID: ...
SUBMISSION: take-home ...              <- which submission this bundle is for
MUNGER SHA-256: 953efe8d...            <- must match Step 0
========================================

GIT COMMIT HISTORY:                     <- your commits, newest first
c0ffee1  2026-09-10  Your Name  Initial commit: starter package

(1 commits)
========================================

PROJECT STRUCTURE:                      <- your directory tree
├── README.md
├── design
│   └── README.md
├── munger.py
└── starter
    └── ...
========================================

SOURCE FILES:                           <- the contents of each file, in full

--- START FILE: starter/source/FourBitAdder/intern/AbstractGate.pseudo ---
...
--- END FILE: starter/source/FourBitAdder/intern/AbstractGate.pseudo ---
```

**Check these four things**, because they're the same four things that matter on submission day:

1. **The commit history is there.** If it says no `.git` directory was found, you ran the script
   from the wrong directory — run it from your repository root.
2. **Your files are actually in the `SOURCE FILES` section**, not just listed in the tree. The
   tree lists everything; only recognized file types get their contents bundled.
3. **The digest at the top matches Step 0.**
4. **Nothing enormous got swept in.** Build directories, `node_modules/`, and virtual environments
   are skipped automatically. Generated documentation directories (`doc/`, `docs/`) appear in the
   tree with a file count instead of being dumped — that's intentional, and it's how the grader
   sees you generated docs without the bundle filling up with HTML.

Delete the dry-run bundle when you're done looking at it. Re-running the script overwrites it
anyway.

## Step 4 — Set up your language's toolchain, and prove each piece works

Pick your language (§3 of the handout) and get all four of these running before you build
anything real. For each one, the test is that you ran it and saw output — not that you installed
it.

| Piece | Prove it by |
|---|---|
| Build/run | Compiling or running a trivial "hello" in your project layout |
| Unit tests | Translating `starter/tests/TestLogicGates.pseudo` and watching it pass |
| Docs generator | Generating docs into `doc/` and opening the result in a browser |
| Style tool | Running it over your source and seeing it reformat or report clean |

Translate `AbstractGate.pseudo` and `LogicGates.pseudo` first — they're provided in full, so
nothing is left to your judgment except the translation itself. When `TestLogicGates` passes for
real in your framework, your toolchain is proven end to end, and everything after that is design
work rather than setup.

Commit at that point. It's a natural, honest commit boundary, and it's the one that proves you
started early.

## Step 5 — Now build the system

Work up the hierarchy — `AbstractDevice` → `Xor2` → `HalfAdder` → `FullAdder` → `FourBitAdder` —
writing each class's tests as you go rather than at the end. Run your style tool before each
commit. Keep `AI_USAGE.md` current as you work (§8 of the handout). Draft your diagrams alongside
the code (§7).

## Step 6 — Submission day

```
git add -A
git commit -m "..."          # your last commit before submitting
python3 munger.py            # answer 1 for take-home
```

Open the bundle one more time and re-check the things from Step 3, plus one more: that the
`SUBMISSION:` line says take-home. Then upload `<ID>_<Name>_takehome_bundle.txt` to the take-home
form:

https://forms.gle/8BxR4VmePRjMWs5s9

That's the whole submission — nothing else to hand in, nothing to push anywhere.

## Step 7 — Session day

After the in-class extension, commit again and re-run `munger.py`, this time answering `2`. That
writes `<ID>_<Name>_inclass_bundle.txt`, which goes to a **separate in-class form** handed out
during the session, before time is called. Your take-home bundle still stands for rubric items 1–8; the in-class one is graded for
item 10.

---

## If something goes wrong

**"No .git directory found here"** — you're not in your repository root. `cd` to the directory
containing `.git` and re-run.

**You uploaded the wrong file to a form** — tell me as soon as you notice. The filenames make this
easy to spot: `takehome` in the name belongs to the take-home form, `inclass` to the in-class one.

**Bundled 0 files** — you're either in the wrong directory or your files use extensions the
script doesn't recognize. Check the tree section: if your files aren't listed there either, it's
the directory. If they're in the tree but not bundled, email me — **do not edit the script**, it
is checksummed.

**Your language needs a file type that isn't bundled** — email me before submission day. This is
a two-minute fix on my end and an integrity problem if you patch it yourself.

**Your bundle is enormous** — expect roughly 30–150 KB depending on your language. Much past
500 KB means something generated got swept in: check the tree for a directory that shouldn't be
there, and tell me what it is; the exclusion list may need one more entry.
