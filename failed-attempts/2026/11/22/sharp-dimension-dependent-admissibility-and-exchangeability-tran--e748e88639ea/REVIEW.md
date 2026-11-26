# Independent mathematical audit

## correctness

PASS

For α>-1, split the rational CDF into the product of u/(1+αu) and α times the product of u²/(1+αu), with the common prefactor (1+α)^(n-1); differentiate the factors to get the stated mixed density. Uniform margins and grounding follow by substitution. For -1<α<0, u(2+αu) increases from 0 to 2+α, so the density is nonnegative everywhere iff 1+α(2+α)^n>=0. A strict violation at the corner persists inside the cube; at equality the density merely vanishes at the corner. At α=-1 the interior expression is zero and cannot extend with uniform margins. For α<-1 there is a nonremovable pole with generic other coordinates. On 0<s<1, s(2-s)^n increases up to 2/(n+1) and decreases to 1 at s=1, giving exactly the stated admissible root and dimension cutoff. With t=2^(-n), the root obeys t<s_n<2t for large n; expanding s_n=t(1-s_n/2)^(-n) first gives s_n=t+O(nt²), and substituting this back yields the stated second term with O(n²t³). The two normalized factors are CDFs for α>=0 and the claimed mixing weights give uniform margins. The bivariate difference from independence is α times a product of strictly positive interior functions. Its integral gives strictly negative covariance for admissible α<0, impossible for an infinite exchangeable sequence by the variance of a sum. No claim about maximal dimension of alternative finite extensions follows. Replay: python3 /workspace/branches/independent_checks.py 4, four exact rational near-corner box volumes, including the sign change from n=3 to n=4 at s=1/8. Frozen checker and its 51-check log were inspected, not rerun.

## originality

FAIL

The sharp condition is a direct sign corollary of the full separable density for this exact family, which the frozen record itself attributes to Chesneau's Proposition 6. One bounds every factor by its attained endpoint value 2+α; evaluating that same density at the all-one corner gives immediate necessity. The originally reported sufficient interval need not have stated the sharp condition verbatim. The remaining phase claims are immediate from the two normalized product terms and the sign of the known bivariate difference. This is a verdict about demonstrated mathematical implication, not a claim that a source printed every endpoint, or a failure due to inaccessible papers.

## value

FAIL

Knowing the admissible domain is a natural goal, but here the proposed invariant reduces mechanically to the endpoint sign of the already available same-family density. Root inversion and expansion do not create a new constrained-extension result; the positive phase just normalizes the two existing product terms, and the negative phase specializes the routine pair-covariance obstruction. An exact finite-extension limit for alternative exchangeable constructions could be substantive, but is explicitly outside the finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
