# Sharp atomic one-point capacity and saturation threshold for finite multiorders with successors

## Finding

**Theorem.** Fix integers \(q\ge1\), \(m\ge0\) and a subset \(J\subseteq\{1,\ldots,q\}\) of size \(s\). In the signature of \(q\) named strict linear orders and the exact immediate-successor relations of just the orders indexed by \(J\), the sharp maximum number of distinct realized atomic one-variable types over \(m\) distinct named parameters, among all finite nonempty structures, is
\[
  \boxed{M(q,m,s)=m+(m+1)^q+2sm.}
\]
For every prescribed family of relative orders on those parameters, a structure of exactly \(M(q,m,s)\) elements realizes every possible atomic type. This is the smallest possible fully saturating structure.

For \(q=s=1\), mark a uniformly random \(m\)-subset of the \(N\) positions in a single linear order (\(N\ge m\ge1\)). The probability that its structure realizes the full \(4m+1\) types is exactly
\[
  \boxed{\frac{\binom{N-3m-1}{m}}{\binom Nm}},
\]
where a binomial coefficient with a top argument less than its nonnegative bottom argument is zero. If \(m=m(N)\to\infty\) and \(m/\sqrt N\to c<\infty\), this probability tends to \(e^{-3c^2}\); if \(m/\sqrt N\to\infty\), it tends to zero. Thus full atomic-type saturation has a sharp square-root-scale transition for a random marked order.

## Assumptions and scope

The carrier \(A\) is finite and nonempty, with arbitrary strict total orders \(<_1,\dots,<_q\) on the same set. Orders need not satisfy any mutual compatibility. For \(j\in J\), the interpreted relation \(S_j(u,v)\) holds exactly when \(u<_j v\) and no element is strictly between them in \(<_j\). Distinct elements \(a_1,\ldots,a_m\in A\) are fixed as parameters, so \(|A|\ge m\). When \(m=0\), the parameter tuple is empty.

The *atomic one-variable type* of \(x\in A\) is the truth vector of all atoms and their negations in one free variable relative to these parameters: equality with each \(a_i\), the two directed strict-order comparisons with each \(a_i\) for every \(j\), and the two successor relations \(S_j(x,a_i)\), \(S_j(a_i,x)\) for \(j\in J\). Parameter-only atomic formulas are constant in \(x\) and irrelevant to counting. This is not a count of complete first-order types, quantifier-rank types, or types in a language with arbitrary extra predicates.

## Proof

**Upper bound.** The \(m\) parameters have different equality types. Each remaining vertex \(x\) has a *gap vector* \((g_1(x),\dots,g_q(x))\in\{0,\dots,m\}^q\), where \(g_j(x)\) counts the parameters below \(x\) in \(<_j\). If no successor relation \(S_j\), \(j\in J\), links \(x\) directly to a parameter in either direction, every atomic assertion about \(x\) is determined by this gap vector. Thus such vertices exhibit at most \((m+1)^q\) types. A nonparameter vertex linked by a named successor relation to at least one parameter occupies one of \(2sm\) *oriented adjacency slots*: it is the immediate predecessor or immediate successor of one named parameter in one designated order. Every such slot contains at most one vertex, since the successor relation is a linear-order path. Hence there are at most \(2sm\) additional vertices, and therefore at most that many additional types. Adding the parameter types proves the bound.

**Uniform attainment and minimum size.** Prescribe any permutation of the parameters in every \(<_j\). Create distinct generic elements \(g_{\mathbf t}\), one for every vector \(\mathbf t\in\{0,\dots,m\}^q\). For each \(j\in J\), parameter \(a_i\), and sign \(\sigma\in\{-,+\}\), create a distinct special element \(b_{j,i,\sigma}\). In order \(<_j\), place each generic element \(g_{\mathbf t}\) in the gap of rank \(t_j\) among the named parameters. If \(j\in J\), insert \(b_{j,i,-}\) immediately before \(a_i\) and \(b_{j,i,+}\) immediately after \(a_i\); arrange other special elements away from all named parameters, for example in the initial gap before the first immediate-predecessor marker. Because generic and unrelated special elements can be ordered freely within each gap, no marker adjacency is accidentally created. In each order, all of its own designated specials occupy exactly their oriented slots. The generic vertices are distinct types via their gap vectors and have no marked successor adjacency. The special vertices have distinct atomic types because each witnesses a different oriented adjacency slot, and every parameter has its own equality type. Hence all \(M(q,m,s)\) types occur on exactly \(M(q,m,s)\) elements. Any fully saturating carrier has at least one element for each distinct type, proving cardinality minimality. The construction also works for \(m=0\): one generic element and no others.

**Exact random saturation count for one order.** Write the \(m+1\) numbers of unmarked elements before, between and after consecutive marked elements as \(\ell_0,\ldots,\ell_m\). Every parameter supplies a distinct type automatically. To realize all \(2m\) oriented successor-slot types requires \(\ell_0,\ell_m\ge1\) and \(\ell_i\ge2\) for interior gaps. To *also* realize every generic gap type requires an unmarked element not adjacent to a parameter in each gap, i.e. \(\ell_0,\ell_m\ge2\) and \(\ell_i\ge3\) for \(1\le i<m\). These conditions are necessary and sufficient. There are \(N-m\) unmarked points; subtracting the required total \(2+2+3(m-1)=3m+1\) leaves \(N-4m-1\) units distributed into \(m+1\) nonnegative gaps. Stars and bars gives \(\binom{N-3m-1}{m}\) favorable marked subsets out of \(\binom Nm\).

**Threshold.** Whenever the numerator is positive, its ratio to the denominator equals
\[
 \prod_{i=0}^{m-1}\left(1-\frac{3m+1}{N-i}\right).
\]
If \(m/\sqrt N\to c<\infty\), then \(m/N\to0\), and the sum of the logarithms equals \(-3m^2/N+o(1)\): the first-order sum is \(-(3m+1)\sum_{i=0}^{m-1}(N-i)^{-1}=-3m^2/N+o(1)\), while the quadratic remainder is \(O(m^3/N^2)=o(1)\). Exponentiating yields \(e^{-3c^2}\). If \(m/\sqrt N\to\infty\), use \(1-t\le e^{-t}\) to bound the ratio by \(\exp(-(3m+1)m/N)\to0\), or note it is already zero when \(N<4m+1\).

## Verification

`verify.py` constructs extremizers for every \(m\in\{0,1,2,3,4\}\), every \(q\in\{1,2,3\}\), and every choice of named-successor subset (70 cases). It enumerates 12,715 small order configurations independently of the construction and verifies the upper bound; it also enumerates uniformly marked subsets and checks the exact probability numerator in 74 small cases. Run from a directory containing the file using `python verify.py`. Successful output is `VERIFY_OK constructions=70 small_order_checks=12715 random_saturation_cases=74`. The general and asymptotic statements follow from the proofs above, not from finite experiments.

## Relationship to prior work

The current study of two-variable first-order logic with linear orders, successors and constants provides a direct motivation for counting *atomic* parameter configurations. Bednarczyk, Kojelis and Szymański study finite satisfiability and complexity for such two-dimensional signatures, including two orders with one visible successor. Jeż, Michaliszyn and Witkowski study unrestricted finite satisfiability with any finite number of independent successor relations, and Michaliszyn and Witkowski study arbitrary models with invisible orders and successor star types. Their main results are decision procedures and model-size or certificate bounds; the inspected texts do not state the sharp named-parameter atomic-type capacity, minimal realization for arbitrary marked permutations, or its exact random saturation law. In contrast, the current theorem concerns the much narrower *atomic* level and makes no claim about complete types or full formula satisfiability.

Previously indexed results on complete one-types of monotone two-order homogeneous structures and quantifier-rank-two laws for random successor orders address different invariants; the former permit arbitrary quantified formulas and the latter concern sentences without these individually fixed parameters. The bound is an elementary local classification, not a consequence claimed for their full theories.

## Limitations

Only finite linear-order structures and exact immediate successors are covered. Extra predicates, cyclic successors, partial orders, quantified one-types and general formula complexity are outside the claim. The random probability uses a uniformly sampled marked subset in a *single* linear order; independence or limiting laws for multiple random orders are not asserted. Mathematical originality is assessed against identifiable accessible sources and indexed results, not against every possible older equivalent formulation; historical priority remains open to broader specialist review. No independent mathematical audit has been conducted.

## References

1. J. Michaliszyn and P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758, first posted 2026-10-07. https://arxiv.org/abs/2610.09758
2. A. Jeż, J. Michaliszyn and P. Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943, first posted 2026-10-14. https://arxiv.org/abs/2610.19943
3. B. J. Bednarczyk, D. Kojelis and K. Szymański, *Two Variables and Two-Dimensional Structures*, arXiv:2610.20937, first posted 2026-10-14. https://arxiv.org/abs/2610.20937
