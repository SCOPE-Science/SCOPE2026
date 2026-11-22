# Exact cyclic switch classes: uniform shattering, trace multiplicities, and logarithmic adaptive growth

## Finding
For integers \(n\ge3\) and even \(k\) with \(0\le k\le n\), let \(\mathcal C_{n,k}\) be the family of binary labelings of the vertices of a labeled cycle of length \(n\) with exactly \(k\) edges whose endpoint labels differ. Coordinate membership is the binary query: what is the label at a specified vertex? Define
\[
r=\min\{k+1,n-k+1\}.
\]
A set of vertices is shattered by \(\mathcal C_{n,k}\) **if and only if its cardinality is at most \(r\)**. The entire shattering complex is therefore the independence complex of the uniform matroid \(U_{r,n}\), with complete face polynomial
\[
\Phi_{n,k}(z)=\sum_{j=0}^{r}\binom nj z^j,
\qquad \operatorname{VCdim}(\mathcal C_{n,k})=r.
\]
More precisely, for any nonempty support \(S=\{p_1,\ldots,p_s\}\) listed cyclically and any assigned bits \(y_1,\ldots,y_s\), let \(g_i\ge1\) be the number of cycle edges from \(p_i\) to \(p_{i+1}\), where indices are cyclic and \(g_1=n\) for a singleton. Put \(\delta_i=y_i\oplus y_{i+1}\) and
\[
P_g^\epsilon(z)=\sum_{\substack{0\le j\le g\\j\equiv\epsilon\pmod2}}\binom gjz^j
=\frac{(1+z)^g+(-1)^\epsilon(1-z)^g}{2}.
\]
The **exact number** of class members realizing the prescribed support labels is
\[
N_{n,k}(S,y)=[z^k]\prod_{i=1}^{s}P_{g_i}^{\delta_i}(z).
\]
For the empty support this multiplicity is \(2\binom nk\).

If \(1\le r<n\), the complex is pure and shellable, with homotopy type \(\bigvee^{\binom{n-1}{r}}S^{r-1}\). In particular its top integral homology is free of rank \(\binom{n-1}{r}\), and its other reduced integral homology vanishes.

For even \(2\le k\le n-1\), the online learning dimension satisfies
\[
k\left\lfloor\log_2\left\lfloor\frac{n-1}{k}\right\rfloor\right\rfloor
\le\operatorname{Ldim}(\mathcal C_{n,k})
\le\left\lfloor\log_2\left(2\binom nk\right)\right\rfloor,
\]
with the convention that the lower bound equals zero when \(n-1<k\). Consequently for every fixed positive even \(k\), \(\operatorname{Ldim}(\mathcal C_{n,k})=k\log_2 n+O_k(1)\), whereas eventually \(\operatorname{VCdim}(\mathcal C_{n,k})=k+1\). For \(k=0\), and also for \(k=n\) when \(n\) is even, the online dimension equals one. The first strict static/online gap at \(k=2\) occurs for \(n=5\): the dimensions are three and four, respectively; an explicit complete depth-four query tree is provided.

## Assumptions and scope
Vertices are distinguishable and indexed cyclically; the edge between the last and first vertex counts toward the transition total. The query labels are the actual vertex bits, not pairwise separation indicators or window observations. Both global bit complements are included. Exactly \(k\), not at most \(k\), switch edges are required. Feasibility forces \(k\) even; all allowed even values from zero to the maximum even value not exceeding \(n\) are included. Every statement about all \(n,k\) is proved combinatorially; finite checks are supplementary.

## Proof
**Local completion and exact enumeration.** A gap containing \(g\) cycle edges between selected vertices of prescribed endpoint bits admits exactly \(\binom gj\) switch-edge subsets of size \(j\) if \(j\equiv\delta\pmod 2\), and none otherwise. Indeed the starting endpoint bit and the chosen switch-edge set uniquely determine all intermediate bits; consistency at the far endpoint is exactly the parity condition. Distinct cyclic gaps have disjoint edge sets. Multiplication of their generating polynomials and extraction of the coefficient of \(z^k\) gives the displayed exact trace multiplicity formula. With no selected vertex, the switch-edge set can be any \(k\)-subset of the \(n\) edges and the starting bit has two possibilities, yielding \(2\binom nk\).

**Sharp support criterion.** Fix a nonempty support of size \(s\), its cyclic gap lengths \(g_1,\ldots,g_s\), and a labeling with adjacent-sample differences \(\delta_i\). Let \(d=\sum_i\delta_i\). Because the differences are taken around the closed cycle, \(d\) is even. Each gap permits the switch counts \(\delta_i,\delta_i+2,\ldots,g_i-e_i\), where \(e_i=1\) exactly when \(g_i\not\equiv\delta_i\pmod2\). All **even** totals between \(d\) and
\[
M=n-\sum_{i=1}^{s}e_i
\]
are achievable: sums of integer intervals with step two have no holes of that parity. Thus the labeling can be realized by exactly \(k\) switches if and only if \(d\le k\le M\).

The largest attainable \(d\) when the labels range over all \(2^s\) assignments is \(2\lfloor s/2\rfloor\), achieved by alternating around the cyclically listed support (with one equal neighboring pair when \(s\) is odd). To determine the smallest attainable \(M\), observe that the difference bits \(\delta_i\) range over all even-parity \(s\)-bit vectors. We would make every \(e_i\) equal one by choosing \(\delta_i\not\equiv g_i\pmod2\). That choice has even parity exactly when \(n-s\) is even, since \(\sum_i g_i=n\). If \(n-s\) is odd, precisely one mismatch must be surrendered, and this is attainable by flipping one difference bit. Hence, over all assignments,
\[
\min_y M=\begin{cases}n-s,&n-s\text{ even},\\n-s+1,&n-s\text{ odd},\end{cases}
=2\left\lceil\frac{n-s}{2}\right\rceil.
\]
The argument also covers \(s=1\), for which the unique difference bit is zero. A support is shattered precisely when
\[
2\lfloor s/2\rfloor\le k\le2\lceil(n-s)/2\rceil.
\]
Because \(k\) is even, these inequalities are equivalent to \(s\le k+1\) and \(s\le n-k+1\). They depend only on support cardinality. The empty support is trivially shattered because the concept family is nonempty. Thus the criterion, the uniform matroid identification, the polynomial and the exact VC dimension all follow.

**Homotopy.** A pure independence complex of a uniform matroid is shellable (for example, lexicographic ordering of its \(r\)-element bases is a shelling). Its reduced homology is concentrated in dimension \(r-1\). Counting the alternating faces yields the reduced top Euler characteristic \((-1)^{r-1}\binom{n-1}{r}\), by the elementary alternating-binomial identity. Shellability therefore gives the stated wedge of \(\binom{n-1}{r}\) spheres. This is a standard uniform-matroid consequence, not a separate originality claim.

**Online dimensions.** Every word is uniquely specified by a \(k\)-subset of the \(n\) cyclic edges together with one initial bit, and every such choice works for even \(k\). Therefore the class has \(2\binom nk\) members; a complete depth-\(d\) binary mistake tree needs at least \(2^d\) distinct members, proving the upper bound. For the lower bound with \(k\ge2\), let \(m=\lfloor(n-1)/k\rfloor\) and partition the first \(km\) edges of a fixed linear cut of the cycle into \(k\) disjoint successive blocks of \(m\) edges. Restrict to words with a fixed starting bit, exactly one variable switch edge per block, and no other switches. Since \(k\) is even, the closing edge does not switch. At any block, the bit at its first vertex is known from the parity of the preceding blocks; the bit at an internal vertex reveals whether that block's unique switch lies before the queried position. Adaptive median queries produce a complete binary tree of depth \(\lfloor\log_2m\rfloor\) within each block. Concatenating these independent trees gives the stated lower bound. For each fixed positive even \(k\) both bounds are \(k\log_2n+O_k(1)\). The two boundary families consisting of the two constant words or the two alternating words have online dimension one.

For \(k=2\), the formula above gives VC dimensions two and three at \(n=3,4\), while the concept-count bounds \(\lfloor\log_2 6\rfloor=2\) and \(\lfloor\log_2 12\rfloor=3\) force online equality. At \(n=5\) there are 20 hypotheses, and `depth4_certificate.json` lists a complete four-level decision tree with 16 pairwise distinct consistent leaves; the counting bound \(\lfloor\log_2 20\rfloor=4\) proves sharpness.

## Verification
Run `python3 verify_cyclic_switches.py` with Python 3.9 or later. The checker enumerates all words and supports for \(3\le n\le11\) and every feasible even transition count, independently checks 23,200 support/parameter instances against the rank criterion and polynomial, and checks the exact coefficient formula on every support of size at most three and every assignment. It also calculates finite online dimensions at \(k=2\) for \(3\le n\le10\) by recursive query splitting. The actual run output is in `verification_output.txt`. The separate 16-leaf adaptive tree is given by `depth4_certificate.json`; each leaf explicitly names one consistent five-bit word. Finite verification neither proves the all-order theorem nor resolves priority.

## Relationship to prior work
The published work of Johnson, *Binary strings of finite VC dimension* (arXiv:2101.06490v1), is a primary logic/VC motivation, but studies translates of an individual word rather than a family defined by an exact cyclic number of switches. Ghazi–Golowich–Kumar–Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions* (arXiv:2007.03668v1), develops general online-dimension closure bounds, without the exact cyclic support criterion. A prior public treatment, *Endpoint-parallel shattering matroids of exact-transition binary words*, completely handles the **linear** \(n-1\)-edge model, whose shattered supports cannot contain both endpoints and whose maximum rank is \(\min\{k+1,n-k\}\). Neither this linear theorem nor its quoted bounds asserts the cyclic uniform-matroid criterion, the exact gap-polynomial trace multiplicities, or the finite five-vertex adaptive tree.

The established textbook fact that unions of a bounded number of **linear intervals** have bounded VC dimension, and its circular-arc analogue, already explains the fixed-small-\(k\) order of the VC bound. No novelty is claimed for that generic upper-bound method. The assessed contribution is the complete, **exactly** \(k\)-switch *cyclic* parameter classification including the dense-side restriction \(n-k+1\), the absence of any support-position exception, and the exact trace multiplicities. A distinct earlier public result, *Four-query static shattering and logarithmic adaptive depth in circular two-block partitions*, treats **pair-separation queries on unlabeled blocks**, not vertex-bit queries on two labeled colors.

## Limitations
This theorem is binary, labeled, cyclic, and requires an exact **even** switch count. It does not give a closed formula for the Littlestone dimension at every finite pair \((n,k)\), although it gives exact first-gap data for \(k=2\) and all-order fixed-\(k\) asymptotics. The uniform-matroid homotopy conclusion relies on established matroid topology. Equivalent results under the names cyclic change-point classifiers, alternating-run concepts, or fixed-boundary circular arcs may predate the available literature; neither a database search nor this work certifies historical priority. No independent mathematical audit has been performed.

## References
1. H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490v1, first publicly submitted January 16, 2021. https://arxiv.org/abs/2101.06490
2. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668v1, first publicly submitted July 7, 2020. https://arxiv.org/abs/2007.03668
3. *Endpoint-parallel shattering matroids of exact-transition binary words*, publicly available research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-endpoint-parallel-shattering-matroids-of-exact-transition-binary--0961bfcd9d1b
4. *Four-query static shattering and logarithmic adaptive depth in circular two-block partitions*, publicly available research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-query-static-shattering-and-logarithmic-adaptive-depth-in-c--68dbb5ccd296
5. E. Esmailian, answer on VC dimension of a finite union of intervals, March 27, 2019 (revised February 14, 2020), background on standard interval VC bounds. https://datascience.stackexchange.com/questions/48081/vc-dimension-of-hypothesis-space-of-finite-union-of-intervals/48091
