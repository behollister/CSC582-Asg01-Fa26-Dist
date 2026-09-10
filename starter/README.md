# Starter outline (pseudocode)

This is a **structural outline in pseudocode**. It does not compile, it does not run, and it is not written in any real language on purpose.

> ### Read this part twice
>
> **Your submission must be written in a real programming language that compiles/interprets and runs on a computer, with a real, executing test suite.** Pseudocode is not a deliverable. A repository containing translated-but-non-running code, tests that are described rather than executed, or `.pseudo` files with the logic filled in, scores zero on rubric items 1, 7, and 8 — and leaves you nothing to extend during the in-class session, which is another 25%.
>
> What you're being handed here is the *skeleton*: the class hierarchy, the file layout, the method contracts, and one worked example of each kind of test. Translating that skeleton into working, tested code in a language of your choice is the assignment.

See [`../Fa26-CSC582-Assignment1.pdf`](../Fa26-CSC582-Assignment1.pdf) for the full specification, especially §3 (choosing a language), §5 (the required class hierarchy), and §6 (project structure). [`../WALKTHROUGH.md`](../WALKTHROUGH.md) walks you through day-one setup.

## What's here

```
starter/
  source/
    FourBitAdder/
      FourBitAdder.pseudo         public entry point            (ADD YOUR CODE)
      intern/
        AbstractGate.pseudo       provided - abstract 2-in/1-out gate base
        LogicGates.pseudo         provided - AND, OR, NAND primitives
        FourBitAdder.pseudo       implementation                (ADD YOUR CODE)
  tests/
    TestLogicGates.pseudo         provided - worked example of both test kinds
    TestHalfAdder.pseudo          (ADD YOUR CODE)
    TestFullAdder.pseudo          (ADD YOUR CODE)
    TestFourBitAdder.pseudo       (ADD YOUR CODE)
```

Two files are genuinely *provided* rather than stubbed — `AbstractGate.pseudo` and `LogicGates.pseudo`. Between them they give you the abstract gate base and the three primitives (AND, OR, NAND) that the entire rest of the system must be built from. `TestLogicGates.pseudo` shows the two kinds of test you owe for every class you write: a construction test and an exhaustive truth-table test.

Everything else is yours to build.

## How to use it

1. **Pick your language** (§3 of the handout). Anything with classes, inheritance, and polymorphism. There's no bonus for picking C++.
2. **Set up a project in that language**, keeping this directory layout — `source/FourBitAdder/` with an `intern/` beneath it, `tests/`, and a `doc/` for generated documentation output. Name the test directory after your framework (`gtests/`, `junit/`, `pytest/`, `jest/`, …). See §6 of the handout.
3. **Translate `AbstractGate` and the three gates first**, then get `TestLogicGates` passing *for real* in your framework before you build anything on top of them. That's your proof the toolchain works end to end: build, test, style, docs.
4. **Then work up the hierarchy** — `AbstractDevice`, `Xor2`, `HalfAdder`, `FullAdder`, and finally `FourBitAdder` — writing the tests for each level as you go, not at the end.
5. **Delete the `.pseudo` files** once you've translated them. They're scaffolding, and leaving them in a submission just makes it harder to see what you actually built.

## Notation

The pseudocode uses `<-` for assignment, `IS` for comparison, and spells out `ABSTRACT`, `VIRTUAL`, `OVERRIDE`, `PROTECTED`, and so on. Where a construct doesn't exist in your language, use the nearest idiomatic equivalent — the intent is what's being specified, not the syntax. If your language has no abstract classes but has interfaces, use interfaces; if it has neither, you picked a language that doesn't fit this assignment (§3 of the handout).
