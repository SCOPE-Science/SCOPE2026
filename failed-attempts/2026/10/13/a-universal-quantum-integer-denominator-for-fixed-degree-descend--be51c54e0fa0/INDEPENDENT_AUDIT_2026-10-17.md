# Independent mathematical audit

## correctness

PASS

Within the initiating log Calabi–Yau quantum-mirror hypotheses and fixed admissible p, published Corollary 3.9 expands each fixed-degree coefficient as a finite sum indexed by nonnegative integer k_{ell j} satisfying sum_ell ell*k_{ell j}=p_j. Its explicit rational factor contains prod_{ell,j}([ell]_q^-1)^{k_{ell j}}, times rational constants, and the refined tropical counts are Laurent-polynomial in q^1/2 by Definition 2.5 and finite rigid-count Proposition 2.6. For each ell>=2, k_{ell j}<=floor(p_j/ell); therefore D_p=prod_{ell=2}^{P}[ell]_q^{sum_j floor(p_j/ell)} clears every summand, yielding the claimed Laurent numerator after Theorem A. Every nontrivial primitive d-root is a simple zero of [ell]_q iff d divides ell, giving the stated pole-order upper envelope. Filling an integer partition with floor(p_j/ell) parts ell and remainder parts 1 attains the raw componentwise exponent. Independent enumeration for vectors (5,7), (3,4,8), (0,2,9) confirmed the maxima for every ell<=max(p); this check does not prove noncancellation or pole sharpness, which are not claimed.

## originality

FAIL

FAIL: Direct mathematical implication of prior Kennedy-Hunt–Shafi–Urundolil Kumaran, Refined curve counting with descendants and quantum mirrors, Corollary 3.9 (arxiv 2502.17236v3, journal 2026). The full published primary text expressly writes every inverse [ell]_q factor with exponent k_{ell j} and its partition constraint; taking k_{ell j}<=floor(p_j/ell) and multiplying a common denominator is a mechanically immediate specialization, not a distinct unsolved theorem. The pole bound is the generic simple-zero multiplicity of this very product; componentwise envelope is trivial for integer partitions. Difference in notation/unstated product label does not avoid prior implication. Even if the authors do not print D_p, their explicit formula fully determines and directly supplies it without any further geometric argument. No evidence of a smaller, optimal reduced denominator or genuine new pole phenomenon remains.

## value

FAIL

FAIL: The denominator is only an unreduced lcm-style clearing product produced by taking maximum multiplicity of each already displayed factor in a known finite partition expansion. It says neither which poles actually exist nor the minimal denominator after cancellations, nor a new invariant requiring novel geometric/combinatorial analysis. Routine multiplication, floor bounds and read-off pole orders are not a substantive mathematical gap, notwithstanding their possible usefulness as an elementary consistency check. The verification script merely repeats the obvious partition-count inequality. Correctness and reproducibility do not establish standalone value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
