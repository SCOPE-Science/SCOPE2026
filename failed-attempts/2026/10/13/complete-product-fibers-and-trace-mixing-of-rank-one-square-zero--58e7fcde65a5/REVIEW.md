# Independent mathematical audit

## correctness

PASS

The complete fiber law, survival probability, TV normalization and exact support statements in RESULT.md lines 3–41 and 43–78 check. Independent proof: put P=D/(q−1) and h=(H−1)/(q−1). A factor has an incident image line/kernel hyperplane (P h choices) and one of q−1 nonzero scales. Given its image line L and a proposed next image L′, exactly J=q^{n−2} hyperplanes through L exclude L′ if L≠L′, and zero if equal. The survival fraction per transition is therefore J(P−1)/(Ph)=λ/C. Conditional on all transitions surviving the initial image line is uniform, and the successive image lines take uniform steps to distinct lines (transition (ones−I)/(P−1)); the last kernel is uniform among the h hyperplanes through the last line, and the scalar of the product is uniform among q−1 choices since one uniformly random factor scale already suffices. This gives per-target conditional probability [h/P + (−1/(P−1))^{r−1}(1_{tr B=0}−h/P)]/[Ph(q−1)]. Multiplying by C λ^{r−1} gives both nonzero rank-one formulas including r=1. No rank≥2 is possible, and subtraction gives the zero count. The conditional signed deviation from uniform scales by (−1/(P−1))^{r−1} from r=1; at r=1 its TV is 1−h/P because the law is uniform on the trace-zero stratum. This yields the stated TV and alternating sign. At r=2 the trace-zero count H(J−1) vanishes exactly for n=2; each class is positive by r=3 and stays so because the transition has positive off-diagonal entries and a positive lower-right entry. Independent replay python /workspace/branches/independent_reproduction.py 4 checked all targets that can occur and exact conditional TV at each length 1–4 for n=2,3 over F2; the general proof uses finite projective counts and is not limited to prime fields. The supplied verifier was inspected, not executed.

## originality

FAIL

A distinct catalogue entry explicitly gives the same complete rank/trace fibers, conditional mixing and support boundary for k≥2, with the omitted length one following from the factor definition. Its later catalogue date establishes equivalent coverage in this review, not earlier precedence or attribution. Earlier factorization existence results are not treated as exact frequency results.

## value

FAIL

The target multiplicity and sharp dimension-two obstruction are worthwhile objects; the exact survival-conditioned TV also has real quantitative content. But all that content is already present in the exact counterpart at every substantive length. Adding the length-one tautology or replacing a projective walk by a two-state recurrence does not leave a distinct unknown fact or a demonstrated new use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
