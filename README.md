# CSC 582 — Assignment #1: The Four-Bit Adder and Extensions (Fall 2026)

Build a virtual four-bit adder out of nothing but AND, OR, and NAND gates, in an object-oriented language of your choice.

**Start here:** [`Fa26-CSC582-Assignment1.pdf`](Fa26-CSC582-Assignment1.pdf) — the assignment itself: rubric, specification, policies, and submission instructions. Read all of it before writing any code; several requirements (the primitives-only rule, the exhaustive-test requirement, the in-class session) are easy to design yourself into a corner on.

Then do [`WALKTHROUGH.md`](WALKTHROUGH.md) on day one. It takes half an hour and proves your whole pipeline works while it's still cheap to find out it doesn't.

## What's in this package

| | |
|---|---|
| [`Fa26-CSC582-Assignment1.pdf`](Fa26-CSC582-Assignment1.pdf) | The assignment. Rubric first, then specification, policies, and how to submit. |
| [`WALKTHROUGH.md`](WALKTHROUGH.md) | Day-one setup: verify the munger, make your repo, dry-run a bundle, prove your toolchain works. |
| [`starter/`](starter/) | Pseudocode outline of the system, plus [`ARCHITECTURE.md`](starter/ARCHITECTURE.md) diagramming the hierarchy. **Not a submission; translate it into a real language.** |
| [`design/`](design/) | Where your UML class diagram and sequence diagrams go (rubric item 5). Must be plain text — Mermaid, PlantUML, or Graphviz. |
| [`AI_USAGE.template.md`](AI_USAGE.template.md) | Rename to `AI_USAGE.md` in your repo and keep it current (rubric item 3). |
| [`munger.py`](munger.py) | Run from your repo root to bundle your project into the single file you submit. Asks which submission it is. **Do not modify it.** |
| [`CHECKSUMS.txt`](CHECKSUMS.txt) | SHA-256 of every file in this package, so you can confirm your copy is unmodified. |

## Verifying this package

Every file here is checksummed. From this directory:

```
sha256sum -c CHECKSUMS.txt        # Linux
shasum -a 256 -c CHECKSUMS.txt    # macOS
```

Every line should report `OK`. On Windows PowerShell, check a single file with
`Get-FileHash munger.py -Algorithm SHA256` and compare against the entry in `CHECKSUMS.txt`.

Two different reasons to run this:

- **`munger.py` must never change.** Its digest is recorded in every bundle you produce and is
  checked when your submission is graded. If it doesn't match, re-download the package — don't
  patch it. If the bundler doesn't handle something your project needs, email the instructor.
- **The rest is a sanity check** that you have an unmodified copy of the package. It is expected
  and fine that your *own working files* diverge from these as you do the assignment — you'll be
  translating the `.pseudo` files, renaming `AI_USAGE.template.md`, and so on. Check against a
  fresh copy of the package, not against your work in progress.

## The short version

- **Individual work.** No teams this term.
- **Any OO language**, as long as it actually builds, runs, and has an executing test suite. The starter is pseudocode precisely so no language is privileged — but pseudocode itself is not a deliverable.
- **AI coding agents are allowed** during the week, and must be disclosed in `AI_USAGE.md`.
- **The assignment culminates in an in-class session**: questions about what you submitted, then a one-hour extension task built on your own code, with AI assistance off. Together they're 25% of the grade.
- **Submit by running `munger.py`** and uploading the resulting `.txt` through the matching Google Form. No GitHub account or hosted repo is required; a local git repo is (its history rides along in the bundle).
- **Two submissions, two filenames, two forms:**

  | | Bundle filename | Form | Due |
  |---|---|---|---|
  | Take-home | `<ID>_<Name>_takehome_bundle.txt` | [submit here](https://forms.gle/8BxR4VmePRjMWs5s9) | start of class |
  | In-class Part B | `<ID>_<Name>_inclass_bundle.txt` | given out during the session | before the session ends |

  `munger.py` asks which one you're making and names the file accordingly, so the two never overwrite each other. Check the filename against the form before uploading.

## Getting started

1. Read the assignment PDF — the rubric is on page 1.
2. Work through [`WALKTHROUGH.md`](WALKTHROUGH.md).
3. Pick your language and set up a project with the required layout, plus a test framework, a docs generator, and a style tool.
4. Translate `starter/source/FourBitAdder/intern/AbstractGate.pseudo` and `LogicGates.pseudo`, then get `starter/tests/TestLogicGates.pseudo` running as real tests. Commit before building anything on top of it.
5. Work up the hierarchy: `AbstractDevice` → `Xor2` → `HalfAdder` → `FullAdder` → `FourBitAdder`, testing each level as you go.
6. Draw your diagrams alongside the code, not after it.
7. Run `python3 munger.py`, choose the take-home option, and upload that bundle to the [take-home form](https://forms.gle/8BxR4VmePRjMWs5s9).
