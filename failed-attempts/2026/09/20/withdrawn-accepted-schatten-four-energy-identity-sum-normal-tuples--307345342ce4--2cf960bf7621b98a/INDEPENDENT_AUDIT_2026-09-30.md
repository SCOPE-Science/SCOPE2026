# Independent audit — 2026-09-30

**Record:** `2026/09/20/schatten-four-energy-identity-sum-normal-tuples--307345342ce4`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `62676a4c73453791b8d0af80ec97aefa8aae68ca`  
**Disposition:** **FAILED**

## Correctness — PASS

The quartic trace argument is valid for commuting S4 operators: Schatten Hölder makes every quartic word trace class, and direct expansion gives Tr([A*,A][B*,B]) = ||[A*,B]||_2^2. The Gram and summed-energy identities follow, as do the sum-normal and Hilbert–Schmidt sum-hyponormal consequences.

## Originality — FAIL

A repository record dated 2026-09-18 already proves the same S4 summed energy identity, the doubly-commuting consequence for sum-normal tuples, and the S2 sum-hyponormal consequence. Its d=2 case implies the assigned pair identity by expanding ||C_A+C_B||_2^2 and subtracting the diagonal terms, after which the assigned Gram formula is immediate. The assigned package is therefore a refinement/repackaging of prior SCOPE work rather than an original finding.

## Scientific value — FAIL

The pairwise/Gram presentation is clean, but as a standalone research record its scientific payload is already contained in the earlier 2026-09-18 theorem package, which also includes a finite-tracial-algebra extension. It does not clear the repository's originality/value bar as an independent finding.

## Evidence and literature

- Earlier SCOPE record: A quartic trace identity rigidifies Schatten sum-normal tuples: https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/18/quartic-trace-rigidity-schatten-sum-normal-tuples--0e05327e8eba
- Chavan–Reza–Sequeira, Sum of self-commutators of commuting operators: https://arxiv.org/abs/2609.19287

## Limitations

- The scientific rejection is based on repository priority, not a mathematical error.
- The S4 threshold is sufficient, not shown sharp.

The record is scientifically rejected for repository-priority/originality reasons and should be relocated atomically with its complete source package; no claim is made that its mathematics is false.
