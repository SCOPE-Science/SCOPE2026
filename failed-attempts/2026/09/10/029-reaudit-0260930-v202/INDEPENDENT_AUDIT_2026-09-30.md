# Independent scientific audit — SCOPE-20260910-029

Audited: 2026-09-30 UTC

Disposition: **failed**

## Correctness

**PASS** — The graph-theoretic transfer is correct: every king edge has grid distance at most 2, hence every king-square edge lies in the fourth power of the grid. Applying the cited finite-component splitting at grid power 4 yields finite king-square components on each side. The Conley-Miller recoloring argument then uses chi(king)=4, removes one color class, and colors the remaining finite components with a second four-color palette sharing one color, giving seven Borel colors. The finite-component covering argument is valid because inserted independent-set vertices only connect through one finite king-square component of the complement.

## Originality

**FAIL** — Gao-Jackson-Krohne-Seward already states the general theorem chi_B(Gamma)<=2 chi(Gamma)-1 for Borel graphs admitting weakly orthogonal decompositions, and constructs the required orthogonal decomposition machinery for the free Z^n Bernoulli action. The record’s king/grid metric comparison and power inclusion are a short hypothesis-transfer application of that general theorem, so under the required implication-based bar the seven-color bound is covered as a specialized corollary rather than an independent result.

## Value

**PASS** — The king-move benchmark is a natural abelian Schreier-graph test case and a seven-color bound is mathematically meaningful. The record fails acceptance because of prior implication coverage, not because the question lacks value.

## Sources and residual risk

- https://arxiv.org/abs/2401.13866 — Primary abstract stating the general chi_B<=2chi-1 theorem and orthogonal decompositions for free Z^n Bernoulli actions. Assessment: Strong broader coverage.
- https://mathweb.ucsd.edu/~bseward/Files/borelcomb.pdf — Indexed primary-PDF excerpt for Corollary 3.2; direct PDF fetch later returned a transport error. Assessment: Confirms the decomposition constants used by the record; access failure to a fresh full render is retained as a source-access risk, but does not undo the explicit broader theorem statement already read.

Residual risks:
- A direct fresh render of the full primary PDF was unavailable at closeout; the coverage judgment rests on the primary arXiv abstract, indexed Corollary 3.2 text, and the record’s own elementary hypothesis transfer.

The detailed machine-readable audit is in `INDEPENDENT_AUDIT_2026-09-30.json`.
