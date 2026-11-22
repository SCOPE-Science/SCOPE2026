# Scientific review: Jordan-rank rigidity for Taft-compatible skew derivations

## Correctness

**PASS.** Fix the scaling \(\sigma(x)=\zeta x\). The skew Leibniz identity fixes every value \(D(x^i)\) from \(D(x)\). The relation \(D\sigma=\zeta\sigma D\) forces \(D(x)\) into the \(m\)-fold-degree invariant subalgebra, and descent through \(x^N\) forces the constant term to vanish precisely when \(m\nmid N\). These conditions are necessary and sufficient. The \(m\)-th power vanishes because each product of \(m\) consecutive quantum integers includes a factor \([am]_{\zeta}=0\). For a nonzero parameter with least degree \(ms\), distinct surviving input monomials have distinct least output degrees after taking powers, proving the exact ranks and all Jordan multiplicities. The finite-field enumeration follows from independent leading-coefficient and trailing-coefficient choices. A standalone checker exhaustively tested 6,581 permitted coefficient assignments in 55 prime-field parameter settings, with direct multiplication and modular matrix-rank checks.

## Originality

**PASS relative to inspected statements, with explicit priority limits.** Montgomery--Schneider (2001), Lemma 2.1 and Theorem 2.2, already cover a special case where the polynomial algebra dimension equals the root order; this is credited, not restated as new. Centrone--Yasumura (2020), Theorem 8, provides a more general framework for Hopf-module algebra actions via skew derivations, but its relevant displayed theorems do not give all-truncation power-rank multiplicities for the specified local algebra. The present new comparison target is the full \(N\)-dependent Jordan-profile law and its exact finite-field frequencies. Published records on square-zero derivations and Taft Hopf operators have different operators or structural constraints. The main residual risk is a possible equivalent treatment of cyclotomic \(q\)-derivatives in classical quantum-calculus literature, or a stronger statement elsewhere in the 2001/2020 sources not found in the inspected relevant sections. This is not an independent priority determination.

## Mathematical value

**PASS.** The linear representation of the skew-primitive generator is a natural invariant of a Taft-module algebra. Over an unbounded family of local truncations, one integer (its rank) reconstructs *every* Jordan block, and the formulas exhibit how the truncation residue and the vanishing order of the generator image control successive nilpotence thresholds. Exact finite-field multiplicities give a complete distribution of the resulting module-theoretic profiles. This is a structural all-parameter classification beyond the known single-truncation boundary, not a one-off small-field count. The formulas do not classify arbitrary Taft automorphism actions or isomorphism classes.

## Sources and remaining risks

Primary motivation: L. Centrone and F. Yasumura, J. Algebra 560 (2020), 725–744, DOI 10.1016/j.jalgebra.2020.06.007, public June 10, 2020. Closest same-object boundary: S. Montgomery and H.-J. Schneider, Tsukuba J. Math. 25 (2001), 337–358, DOI 10.21099/tkbjm/1496164292. Related but different source objects: Z. Cline (2018), arXiv:1805.10340; S. Crawford, J. Gaddis and R. Won (2024), arXiv:2409.17890. Novelty is qualified by the possibility of unindexed or differently formulated \(q\)-differential-module results. All claimed identities and counts are valid only under the fixed-scaling hypotheses stated in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
