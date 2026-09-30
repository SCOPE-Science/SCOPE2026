# Independent Audit — 2026/09/14/024

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `48e3aaf387010791bc3c14e6a52b72e7ff05598c`
- Disposition: **FAILED**

## Correctness

**PASS** — Independent exhaustive enumeration of all 2^22 bond configurations on the stated 5-by-3 vertex grid reproduces exactly 1,550,368 left-right crossing configurations, hence probability 1,550,368/4,194,304 = 48,449/131,072 about 0.3696365356. The advertised 0.25 to 0.45 window therefore holds with wide exact margin.

## Originality

**FAIL** — The computation is a direct evaluation of a small two-terminal reliability/crossing probability by exhaustive enumeration. Exact finite-lattice percolation polynomials and finite-size crossing computations are established techniques, including substantially larger lattices. Even if this exact reduced fraction was not previously printed, obtaining it by enumerating 4,194,304 subsets is not a research-level new method or structural theorem.

## Scientific value

**FAIL** — The exact number is a sound benchmark for code validation, but it concerns one 22-edge graph at one probability and yields no finite-size scaling law, reliability polynomial, asymptotic correction, or reusable theorem. Its value is primarily as a regression test rather than as an independent scientific finding.

## Sources

- Effective boundary extrapolation length to account for finite-size effects in the percolation crossing function (Robert M. Ziff): https://doi.org/10.1103/PhysRevE.54.2547 — Prior finite-size crossing-probability work on much larger rectangular bond-percolation lattices.
- Exact percolation probabilities for a square lattice: Site percolation on a plane, cylinder, and torus (Renat K. Akhunzhanov; Andrei V. Eserkepov; Yuri Yu. Tarasevich): https://arxiv.org/abs/2204.01517 — Demonstrates exact finite-lattice percolation probability computation via systematic enumeration/dynamic programming.

## Limitations

- The audit independently reproduced the exact count but did not assess whether the same fraction occurs in an obscure unpublished reliability table.
- Failure is based on originality/scientific value, not on correctness.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
