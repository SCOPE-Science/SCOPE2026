# Independent mathematical audit

## correctness

PASS

PASS: The greedy number of 0^a1^b host blocks to embed a candidate is B(u)=Σceil(ℓ_i/c_{x_i})−number of 0→1 adjacent run transitions. Absent iff B>r; deletion changes B by at most one. For nonsingleton runs the reduction is exactly one iff ℓ_i≡1 mod capacity, and endpoint/internal singleton analysis supplies the claimed forbidden cases; therefore B=r+1 plus conditions 2–4 characterize MAS. Symbolic run weights z/(1−z), z²/(1−z) produce F_{2r+2} for both capacities>=2, 3·2^{r−1} for exactly one capacity=1, and [z^r]z(3−z+2z²)/(1−2z+z²−z³) for both=1. Independent literal subsequence/deletion enumeration for a,b in 1..4, r in 1..5 with host length <=17 reproduced all three formulas; infinite proof rests on greedy cost/series not finite tests.

## originality

FAIL

FAIL due decisive prior coverage: a separate published November 8 full-result paper proves the identical Fibonacci total F_{2r+2} for every a,b>=2. Another published November 8 full-result theorem proves the identical 3·2^{r−1} case for (0^a1)^r with a>=2; bit-complement plus reversal yields the a=1,b>=2 case. A November 2 published theorem already gives the exact identical rational total series for (01)^r AND a stronger complete length spectrum. All three count regimes are therefore known; the submitted uniform greedy-run criterion is a direct specialization of the pre-existing general Kosche–Koß–Manea–Siemer greedy-bridge characterization and does not save originality of the full claimed classification. The two November 8 titles share a published commit timestamp with the submitted record; no earlier-in-minute priority is inferred, but their independent coverage remains decisive.

## value

FAIL

FAIL as a distinct mathematical contribution: the full three-case all-parameter count is already determined in separate published results, and the remaining run-language criterion follows by routine specialization of a known general greedy embedding/minimal-absence test. Its combined uniform packaging is convenient but does not add a demonstrably new substantive invariant, boundary, or classification beyond covered components. Correctness and a reproducing checker alone cannot rescue V.

The dated certificate retains the supplied scientific assessment, sources and limitations.
