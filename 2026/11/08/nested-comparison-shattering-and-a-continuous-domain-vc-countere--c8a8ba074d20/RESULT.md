# Nested comparison shattering and a continuous-domain VC counterexample for single-peaked preferences

## Finding
For every integer \(n\ge 1\), consider all strict preference orders on the known axis \([n]=\{1,\ldots,n\}\) that are single-peaked on that axis. A query \(q_{ab}\), with \(a<b\), is answered one if and only if \(a\) is preferred to \(b\). Write \(\mathcal P_n\) for their binary comparison vectors.

**Theorem (one unified classification and its learning consequences).** A set \(S\) of pair queries is VC-shattered by \(\mathcal P_n\) if and only if it has the form
\[
S=\{q_{a_i b_i}:1\le i\le k\},\qquad a_1<\cdots<a_k<b_k<\cdots<b_1.
\]
The empty set is admitted. Every shattered support is also **strongly shattered**: there exists a family of \(2^k\) distinct concepts whose vectors agree outside \(S\) and realize all \(2^k\) assignments on \(S\). Consequently the entire shattering polynomial, static dimension, and online dimension are
\[
\Phi_n(z)=\sum_{k=0}^{\lfloor n/2\rfloor}\binom n{2k}z^k,\qquad
\operatorname{VCdim}(\mathcal P_n)=\left\lfloor\frac n2\right\rfloor,
\qquad \operatorname{Ldim}(\mathcal P_n)=n-1.
\]
The equality \(\Phi_n(1)=2^{n-1}=|\mathcal P_n|\) exhibits shattering-extremality. The exact adaptive-static gap is \(\lceil n/2\rceil-1\). For \(n\ge4\), the shattering complex is nonpure: \(\{q_{1,2}\}\) is an inclusion-maximal face while other maximal faces have size \(\lfloor n/2\rfloor\).

**Continuous consequence.** Let \(\mathcal P_{\mathbb R}\) be all binary-choice preferences of the form \(x\succ y\iff u(x)>u(y)\), where \(u:\mathbb R\to\mathbb R\) is continuous, strictly increasing to one peak and strictly decreasing thereafter. Then
\[
\operatorname{VCdim}(\mathcal P_{\mathbb R})=\infty.
\]
Indeed, every positive integer \(k\) admits a shattered support of \(k\) pair questions, and every labeling can be attained with the *same predetermined peak location*. This is incompatible with the illustrative finite-VC statement for this unrestricted utility class in Basu–Echenique (2020, §2.2, pp. 1285–1286). The present claim makes no assertion about the paper's separate expected-utility, Choquet-utility, or max-min utility models.

## Assumptions and scope
For \(n\ge1\), single-peakedness means that each upper contour set is an interval of the fixed alternative axis. Equivalently, the worst remaining alternative is always the left or right endpoint of the remaining interval, and every sequence of deleting a current endpoint from worst to best yields exactly one admissible strict order. There are precisely \(2^{n-1}\) such orders, since all but the final deletion have two choices. No distance symmetry, monotone slope bound, fixed cardinal representation, voter aggregation, or uncertainty about the axis is imposed. All query pairs are distinct and use a fixed answer convention. The continuous assertion concerns unrestricted continuous, strictly unimodal real utilities; it does not claim the same conclusion for parametric distance-utility families.

A support is **VC-shattered** if every binary answer vector occurs as the restriction of an admissible preference. It is **strongly shattered** if the concepts can be chosen with a common answer vector on all queries outside that support. Littlestone dimension is the maximum depth of a complete binary adaptive query tree each of whose paths is consistent with a concept.

## Proof
**1. A forbidden pair of queries.** Consider two distinct queries \(q_{ab}\) and \(q_{cd}\) with \(a<b\), \(c<d\), \(a\le c\), and \(b\le d\). Every single-peaked order satisfies
\[
 a\succ b\quad\Longrightarrow\quad c\succ d.
\]
To see this, on any ordered triple \(x<y<z\), the middle alternative \(y\) cannot be ranked last. Because \(a\succ b\) for \(a<b\), the peak must be strictly to the left of \(b\): otherwise both endpoints would lie on the increasing side of the peak and \(b\succ a\). If \(c\ge b\), both \(c\) and \(d\) lie on the decreasing side, so \(c\succ d\). If \(a\le c<b\), the no-valley condition on \(a<c<b\), or the tautology for \(a=c\), forces \(c\succ b\). When \(d=b\), this is precisely \(c\succ d\); when \(d>b\), both \(b\) and \(d\) lie to the right of the peak, giving \(b\succ d\), and transitivity yields \(c\succ d\). This covers shared endpoints without assuming a strict self-comparison. Thus the labeling \(q_{ab}=1\), \(q_{cd}=0\) is impossible, and no such two-query set can be shattered.

Sort any nonempty support by its left endpoints. If two have the same left endpoint, or if successive right endpoints do not strictly decrease, they give the above forbidden configuration. Therefore a shattered support necessarily has strictly increasing left endpoints and strictly decreasing right endpoints. The ordered-pair inequalities \(a_i<b_i\) then imply \(a_1<\cdots<a_k<b_k<\cdots<b_1\), as required. (An identical query is not repeated in a set.)

**2. Construction of a whole coordinate cube.** Conversely take any strictly nested support. Construct strict orders by deleting alternatives from worst to best. First delete, in fixed order, the unpaired extreme alternatives outside the outermost selected pair. The two members \(a_1,b_1\) are then the current endpoints. Delete them consecutively in either order. Remove the next unpaired extreme alternatives in a fixed order, and repeat for \(a_2,b_2\); proceed until every selected pair is deleted and finish any remaining alternatives in a fixed endpoint-deletion order. All steps delete a current extreme, hence each resulting ranking is single-peaked. The \(k\) choices of the within-pair deletion order are independent. In the final complete ranking, members of each selected pair are adjacent to one another and all pair blocks and singleton blocks occur in one common fixed order. Therefore varying the \(i\)-th choice changes **only** the comparison between \(a_i\) and \(b_i\), not any other pair comparison. We obtain a \(k\)-dimensional subcube of comparison vectors, proving strong shattering and the if direction.

**3. Coefficientwise count, extremality, and nonpurity.** Selecting a nested \(k\)-matching is equivalent to choosing any \(2k\) axis elements, pairing the least with the greatest, the second least with the second greatest, and so forth. There are exactly \(\binom n{2k}\) such supports. Their sum is \(\sum_{k\ge0}\binom n{2k}=2^{n-1}\), which equals the number of concepts from the endpoint deletion coding; this is the sandwich-bound equality. Maximum possible \(k\) is \(\lfloor n/2\rfloor\). The pair \(q_{1,2}\) cannot coexist in a shattered support with any other query, since it is not strictly nested with any other query. It is nonetheless individually shattered. This shows nonpurity for \(n\ge4\).

**4. Exact adaptive dimension.** In a current interval \([\ell,r]\), query which of its two endpoints is preferred. The less preferred endpoint must be the worst remaining alternative by single-peakedness. Delete that endpoint and continue. For every sequence of \(n-1\) binary outcomes, this procedure gives one valid endpoint-deletion sequence and therefore one distinct preference realizing that root-to-leaf path. Thus a complete Littlestone tree of depth \(n-1\) exists. Conversely a depth-\(d\) complete Littlestone tree needs at least \(2^d\) distinct concepts, whereas \(|\mathcal P_n|=2^{n-1}\). Hence \(d\le n-1\), proving equality, including \(n=1\).

**5. A common-peak real-line construction.** Fix \(k\ge1\), query the \(k\) pairs \((i,2k+1-i)\), for \(i=1,\ldots,k\), on the ordered real sample points \(1,\ldots,2k\). Choose a peak at \(c=k+\tfrac12\), the same location for all labels. Given any binary labeling \(\lambda_i\), set \(\epsilon_i=1\) if \(\lambda_i=1\) and \(\epsilon_i=-1\) otherwise, and prescribe
\[
 u(i)=8i+\epsilon_i,\qquad
 u(2k+1-i)=8i-\epsilon_i\quad(1\le i\le k),\qquad
 u(c)=8(k+1).
\]
These values increase strictly from the left toward \(c\), and decrease strictly from \(c\) toward the right. Piecewise-linear interpolation through the prescribed points, followed by strictly monotone linear extensions to both infinities, produces a continuous utility that is strictly increasing on \(( -\infty,c)\) and strictly decreasing on \((c,\infty)\). The difference between the two queried utilities is \(2\epsilon_i\), so each prescribed answer is realized independently. Since \(k\) is arbitrary, the continuous concept class shatters supports of every finite size and has infinite VC dimension. In particular, at \(k=2\), the crossing choices asserted unavailable in the cited example already occur on the nested pairs \((1,4)\) and \((2,3)\), e.g. \(u(1)>u(4)\) while \(u(2)<u(3)\).

## Verification
A dependency-free finite checker is included as `verify_single_peaked.py`. It directly enumerates all endpoint-deletion orders and all candidate supports through cardinality \(\lfloor n/2
floor+1\) for each axis of size at most eight, computes their full binary traces, checks strict-nesting equivalence and the stronger fixed-complement cube property, and compares every shattering coefficient to the exact binomial formula. Larger supports need not be enumerated after one nonshattered cardinality because shattering is hereditary. The checker tested 132,154 supports over these sizes. It also tests the complete extreme-pair tree for all orders through size twelve. For the continuous construction, it independently evaluates 4,094 integral prescribed-utility patterns spanning \(1\le k\le11\), confirming both monotonicity toward a common peak and the independent query answers. These finite experiments are independent checks, not substitutions for the all-parameter proofs above.

## Relationship to prior work
The fixed-axis domain and its endpoint recursion are standard; in particular Zhan (2019) constructs the complete domain by rhombus tilings, and Zhan (2022) gives an \(n-1\)-sign representation and Bruhat operations. The number \(2^{n-1}\) of admissible orders is not claimed as new. Karpov (2023) enumerates multi-agent single-peaked profiles under varying axes rather than the Boolean supports of pair comparisons. Conitzer (2009) studies query complexity of eliciting an individual single-peaked ranking, not the complete VC-shattering complex or exact online mistake-tree depth. Johnson–Wickes (2023) use a different \(k!\)-order permutation-shattering notion; it is not the \(2^k\)-label binary-comparison notion here.

Basu and Echenique (2020), §2.2, pp. 1285–1286, explicitly describe the class of real single-peaked preferences represented by utilities increasing to some peak and decreasing thereafter as an example having finite VC dimension, and assert an obstruction to a particular pair of binary choice labels. The real-line construction above supplies every such label vector on arbitrarily many nested pairs, even at a common peak, under exactly that stated qualitative utility definition. Consequently the illustrative finite-VC assertion does not apply to their unrestricted continuous single-peaked class as written. No claim is made about any of that paper's separately established results for expected-utility or other uncertainty models. Literature priority of the specific nested-matching classification under alternate terminology remains open to broader independent review.

## Limitations
The finite dimension formulas require all strict single-peaked orders on one *known fixed axis*, not a smaller vote domain, an unknown axis, or an ensemble of voters. The continuous result allows arbitrary strictly unimodal continuous utility functions and does not transfer automatically to distance-to-peak utilities, common slope constraints, or other parametric subclasses. Only the stated VC and Littlestone quantities, support classification, and existential subcubes are proved; no statistical sample-complexity constant or computational identification complexity beyond the displayed tree is claimed. Exhaustive checks terminate at finite size and do not prove infinite statements. Historical priority needs independent review; no independent mathematical audit is represented.

## References
1. P. Zhan, *A simple construction of complete single-peaked domains by recursive tiling*, Mathematical Methods of Operations Research **90** (2019), 477–488, published online 2019-10-10. https://doi.org/10.1007/s00186-019-00685-7
2. P. Basu and F. Echenique, *On the falsifiability and learnability of decision theories*, Theoretical Economics **15** (2020), 1279–1305, §2.2, pp. 1285–1286. https://doi.org/10.3982/TE3438 ; lawful full text: https://eml.berkeley.edu/~fechenique/published/VCdimension-BasuEchenique.pdf
3. P. Zhan, *Sign representation of single-peaked preferences and Bruhat orders*, arXiv:2202.11352 (first version 2022-02-23). https://arxiv.org/abs/2202.11352
4. V. Conitzer, *Eliciting single-peaked preferences using comparison queries*, Journal of Artificial Intelligence Research **35** (2009), 161–191. https://doi.org/10.1613/JAIR.2606
5. A. Karpov, *Structure of single-peaked preferences*, Journal of Mathematical Psychology **117** (2023), 102817; public conference manuscript https://research.illc.uva.nl/COMSOC/proceedings/comsoc-2023/AlexanderKarpov.pdf
6. J. R. Johnson and B. Wickes, *Shattering \(k\)-sets with permutations*, arXiv:2112.01946 (2021). https://arxiv.org/abs/2112.01946
7. S. Kraiczy and E. Elkind, *Exact Learning of Preference Structure: Single-peaked Preferences and Beyond*, Proceedings of Machine Learning Research **162** (2022). https://proceedings.mlr.press/v162/kraiczy22a.html
