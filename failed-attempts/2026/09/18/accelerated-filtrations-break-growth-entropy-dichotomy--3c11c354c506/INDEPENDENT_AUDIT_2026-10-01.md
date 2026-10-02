# Independent mathematical audit — SCOPE-20260918-3c11c354c506

Audit date: 2026-10-01 (UTC) UTC.

Outcome: **FAILED**.

## Final claim assessed

Accelerated filtrations break arbitrary-filtration entropy-growth implications.

## Correctness

**PASS** — For \(V_n=U^{b^n}\), \(V_nV_m\subseteq V_{n+m}\) follows from \(b^n+b^m\le b^{n+m}\), and infinite dimensionality forces every adjacent power \(U^r\subsetneq U^{r+1}\). Hence the quotient dimension across the accelerated gap is at least \(b^n-b^{n-1}\), giving entropy at least \(\log b\); for \(k[x]\) equality is immediate while the Gelfand–Kirillov dimension remains one. The one-sided comparison and the linearly controlled repair also follow from the displayed inclusions and submultiplicativity.

## Originality

**FAIL** — Two published Resultary findings dated 2026-09-19 now strictly cover and strengthen this 2026-09-18 record. “Accelerated filtrations break entropy-growth detection” gives the full \(k[x]\) prescribed-entropy spectrum and a stronger every-filtration characterization while explicitly retaining the same linear-control repair; “Universal acceleration gives divergent filtration entropy on every infinite-dimensional affine algebra” strengthens the universal finite lower bound to divergent entropy. These later published results dominate the assigned final claim.

## Value

**FAIL** — The mathematics remains useful, but as a current publishable finding its claimed gap has been superseded by stronger published results that contain the counterexample mechanism and repair. There is no remaining distinct structural contribution in this package that clears the value bar independently of that coverage.

## Source inspections

- **J. Schwarz and A. Sebandal, Growth functions of algebras and an application to Leavitt path algebras, arXiv:2609.18144v1 (2026).** Primary full text inspected. Theorem 3.14 states that positive algebraic entropy for a finite-dimensional filtration forces exponential intrinsic growth, relying on the arbitrary-filtration comparison theorem. Consequence: The accelerated \(k[x]\) filtration is a genuine counterexample to the source theorem as printed.
- **W. Bock et al., Algebraic Entropy of Path Algebras and Leavitt Path Algebras of Finite Graphs, Results in Mathematics 79 (2024), 180.** Open-access full text inspected around Section 3. It explicitly treats filtration dependence and linear reindexing, including the observation that nonzero entropy can be scaled by linear reindexing while zero remains zero for listed restricted changes. Consequence: Provides prior filtration-dependence context but not the exponential acceleration counterexample.
- **Resultary, Accelerated filtrations break entropy-growth detection (published 2026-09-19).** Published summary states that \(k[x]\) admits every prescribed filtration entropy in \([0,\infty)\), that one-filtration positive entropy does not imply exponential growth, and that linear upper control restores the implication. Consequence: Strictly covers the assigned \(k[x]\) counterexample and linear-control repair, while strengthening them.
- **Resultary, Universal acceleration gives divergent filtration entropy on every infinite-dimensional affine algebra (published 2026-09-19).** Published summary states universal existence of a finite-dimensional exhaustive filtration with divergent algebraic entropy for every infinite-dimensional affine algebra. Consequence: Strictly strengthens the assigned universal lower bound \(h_{alg}\ge\log b\).

## Residual risks

- The source theorem is genuinely false as printed, but the assigned correction is scientifically superseded by stronger published 2026-09-19 Resultary findings.
- The later covering records were compared through their published Resultary summaries; their implications are already sufficient to dominate the assigned claim.

The accompanying JSON audit records the implication comparisons and exact coverage analysis in structured form.
