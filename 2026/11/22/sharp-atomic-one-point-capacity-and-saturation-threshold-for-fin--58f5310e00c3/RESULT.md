# Sharp atomic one-point capacity and saturation threshold for finite multiorders with successors

## Finding

Fix integers \(q\ge1\) and \(m\ge0\), and let \(J\subseteq\{1,\ldots,q\}\) have size \(s\). In the signature of \(q\) named strict linear orders and the exact immediate-successor relations for the orders indexed by \(J\), the sharp maximum number of distinct atomic one-variable types realized in a single finite nonempty structure over \(m\) distinct named parameters is
\[
M(q,m,s)=m+(m+1)^q+2sm.
\]
For every prescribed family of relative orders on the parameters, this number is attained on a carrier of exactly \(M(q,m,s)\) elements. No smaller carrier can attain it. Call attaining this maximum **capacity saturation**. It does not mean realizing all types that are individually consistent across different structures.

For \(q=s=1\), mark a uniformly random \(m\)-subset of the \(N\) positions of a linear order, where \(N\ge m\ge1\). The probability of realizing \(4m+1\) types is
\[
\Pr(\text{capacity saturation})=\frac{\binom{N-3m-1}{m}}{\binom Nm},
\]
with numerator zero when \(N-3m-1<m\). If \(m=m(N)\to\infty\) and \(m/\sqrt N\to c<\infty\), the probability tends to \(e^{-3c^2}\); if \(m/\sqrt N\to\infty\), it tends to zero.

## Assumptions and scope

The orders \(<_1,\ldots,<_q\) are arbitrary strict total orders on the same finite nonempty set, with no compatibility assumed. For \(j\in J\), \(S_j(u,v)\) holds exactly when \(v\) immediately follows \(u\) in the entire order \(<_j\). An atomic one-variable type is the truth vector of equalities with the parameters \(a_1,\ldots,a_m\), order comparisons with them in both directions in each order, and successor comparisons with them in both directions for \(j\in J\). Atoms involving only the parameters are constant in the varying point \(x\), so they do not change the count in a fixed structure. No quantified types are counted.

For example, with two parameters \(a<b\) in one successor order, a possible interior type has both \(S(a,x)\) and \(S(x,b)\). A different possible interior type has neither. They cannot occur together: a double adjacency implies the gap contains only one element. Capacity saturation concerns a sharp cardinality, not the union of all individually possible types.

## Proof

**Upper bound.** The parameters each contribute an equality type. Each nonparameter \(x\) has a gap vector \((g_1(x),\ldots,g_q(x))\in\{0,\ldots,m\}^q\), where \(g_j(x)\) counts the parameters below \(x\) in order \(j\). For nonparameters not joined to any parameter by a named successor relation, this vector determines the atomic type. The other nonparameters are each the immediate predecessor or immediate successor of a named parameter in a designated order. There are \(2sm\) such oriented slots and each holds at most one element. An element may occupy multiple slots, so there are at most \(2sm\) of these elements, and at most that many additional types. Adding all three bounds gives \(M(q,m,s)\).

**Uniform attainment and minimum size.** If \(m=0\), take a one-element structure. Otherwise, place one distinct generic element for every gap vector and create a separate marker for each oriented slot. In each order, use the prescribed parameter ordering and place each generic element in its specified gap. In a designated order, place its own markers immediately next to their respective parameters, leaving the other elements inside the gaps between those markers or on the outer sides of the end markers. Place any markers from other orders in the first gap, on the outer side of the first predecessor marker if this order is designated. In an order without a named successor the other-order markers can go anywhere in the first gap. These independent arrangements give exact successors and ensure that each marker witnesses just its own named slot, while no generic element witnesses a slot. All generic type vectors differ, all marker types differ by their slots, and the equality types distinguish the parameters from both groups. Hence all \(M(q,m,s)\) elements realize distinct types. This proves sharpness and the minimum size for attaining the maximum.

**Random order.** For one order with its successor, let \(\ell_0,\ldots,\ell_m\) be the unmarked gap lengths. To attain the sum of the upper bounds there must be \(2m\) distinct slot witnesses and one generic point in every gap. An exterior gap needs one slot witness and one generic witness; an interior gap needs two distinct slot witnesses and a generic witness. These requirements are also sufficient. Thus precisely the gaps with \(\ell_0,\ell_m\ge2\) and \(\ell_i\ge3\) for \(1\le i<m\) succeed. Subtracting their minimum total \(3m+1\) from the \(N-m\) unmarked positions, the favorable gap vectors are the weak compositions of \(N-4m-1\) into \(m+1\) parts. The gap vector determines the marked subset, giving the stated numerator by stars and bars.

**Threshold.** For a positive numerator the probability is
\[
\prod_{i=0}^{m-1}\left(1-\frac{3m+1}{N-i}\right).
\]
When \(m/\sqrt N\) has a finite limit, the sum of the logarithms is \(-3m^2/N+o(1)\): the difference between the sum of the linear terms and \(-3m^2/N\) is \(O(m/N+m^3/N^2)\), and the quadratic error is \(O(m^3/N^2)\). This proves the finite-\(c\) profile. When \(m/\sqrt N\to\infty\), the probability is either zero or bounded by \(\exp[-m(3m+1)/N]\), giving the limit zero.

## Verification

`verify.py` uses only Python's standard library. It checks the attained cardinality in 70 extremizer constructions, checks the upper bound in 12,715 small configurations, and compares direct marked-subset enumeration with the binomial formula in 74 finite cases. These tests concern the number of distinct simultaneously realized types; they do not test a union of types across structures or prove the general theorem.

## Relationship to prior work

The cited work on two-variable logic with orders and successors [1–3] motivates the signatures but studies satisfiability, model bounds or certificates rather than the maximum number of atomic types over a prescribed parameter configuration. The separate order-gap and immediate-neighbor bounds are elementary; the sharp part is attaining them together by one finite structure for every prescribed ordering of the named parameters.

The one-order random calculation, once translated into gap clearance, is an instance of classical separated-set counting, not a new binomial spacing formula. For example, it can be represented as counting 3-separated \((m+1)\)-subsets on a circle of length \(N+3\) containing a fixed point: insert that point and one extra unmarked position next to it on each side of the original ordered positions. The separation requirement at the fixed point enforces the two exterior clearances; away from it, it enforces the interior clearances. See [4, Introduction] for the circular separated-set formula. The connection here is the equivalence between that spacing event and maximum atomic-type capacity.

## Limitations

No claims are made for cyclic successors as a model-theoretic signature, partial orders, extra predicates, complete types, or saturation with respect to all individually possible types. The random claim concerns only a single uniformly marked linear order. The comparisons do not establish exhaustive historical priority.

## References

1. J. Michaliszyn and P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758. https://arxiv.org/abs/2610.09758
2. A. Jeż, J. Michaliszyn and P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943. https://arxiv.org/abs/2610.19943
3. B. J. Bednarczyk, D. Kojelis and K. Szymański, *Two Variables and Two-Dimensional Structures*, arXiv:2610.20937. https://arxiv.org/abs/2610.20937
4. E. J. J. Estrugo and A. Pastine, *The number of s-separated k-sets in various circles*, Australasian Journal of Combinatorics 79(3) (2021), 424–436. https://ajc.maths.uq.edu.au/pdf/79/ajc_v79_p424.pdf
