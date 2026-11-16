# Review of the parity-dependent Hartogs vertex polynomial root law

## Correctness
**PASS.** The assertion is for all integer degrees \(N\ge2\) and \(0<\alpha\le1\). The main algebraic identity \((1-z)^3 Q=A+z^N B\) and its elimination derivative are verified exactly. The coefficient expansions at \(z=-1-y\) and strictly decreasing ratios \(V_j/U_j\) bound the number of relevant real roots by one for even \(N\) and two for odd \(N\). Endpoint signs and an explicit positive ratio \(R_N(x)\) establish actual counts, uniqueness, multiplicities and the odd-degree asymptotic \(\alpha_N\to 1/2\). The cited vertex-section convergence is treated as a prior theorem, not newly proved. The included checker supplies finite symbolic and exact-rational corroboration but is not a substitute for this infinite proof.

## Originality
**PASS against inspected sources, with residual priority risk.** Edholm–Mathew (arXiv:2505.20489) studies rational generalized-Hartogs Bergman numerators, not this all-degree root count. Deng–Fu (arXiv:2611.07480) proves unit-circle positivity of a different palindromic polynomial. Most importantly, Fu (arXiv:2611.15406v1) already supplies exactly this vertex polynomial, its locally uniform convergence and the strong lemma allowing at most one double negative root, including the degree-three threshold. This review does not rebrand those statements as new. The remaining new statement is the all-integer parity split, sharp uniquely attained threshold at each odd degree, and its limiting value. Inspection of the full relevant source did not find those stronger claims. There remains a risk that a different earlier treatment of truncated power sums gives an equivalent count.

## Value
**PASS.** The count identifies when vertex-limit zeros relevant to the generalized Hartogs kernel lie on the negative real axis, versus occur only in conjugate pairs. It adds an explicit transition diagram across every natural degree and a uniform asymptotic threshold, rather than an isolated example or a routine normalization. The result is finite-polynomial mathematics but determines a meaningful missing parameter invariant of a natural analytic kernel family. It does not claim a solution of the entire Hartogs zero-set problem.

## Evidence and limitations
The complete algebraic identities, coefficient signs, critical-parameter construction and quantitative limitations appear in `RESULT.md`; the standalone `checker.py` can be run with SymPy. The most material comparison is Fu, Section 2 and Lemmas 3.1–3.2. This review is an internal self-review, not external expert validation.

Self-review: passed. Independent audit: not yet performed.
