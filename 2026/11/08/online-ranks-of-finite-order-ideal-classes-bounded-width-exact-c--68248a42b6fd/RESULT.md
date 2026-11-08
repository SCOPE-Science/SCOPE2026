# Online ranks of finite order-ideal classes: bounded-width exact computation and dyadic saturation

## Finding
Let \(P\) be a finite poset with \(n\) elements and width at most \(w\). Let \(\mathcal J(P)\) denote all lower order ideals, including the empty ideal, considered as binary classifiers on \(P\) under membership queries. Its Littlestone dimension can be calculated exactly with at most
\[
 n\left(\sum_{j=0}^{w}\binom{n}{j}\right)^2
\]
query transitions among pairs of order ideals, and polynomial additional work per transition. In particular, for each fixed \(w\), this is a polynomial-time exact algorithm, with \(O(n^{2w+1})\) transitions. This is an XP, not a parameterized fixed-parameter-tractability, assertion.

For the two-row product-order grid \(P_n=[2]\times[n]\), with \(n\ge2\), the same class has \(\operatorname{VCdim}(\mathcal J(P_n))=2\). Nevertheless, at every integer \(k\ge1\) and \(n=2^{k+1}-2\), it attains its information-theoretic online upper bound exactly:
\[
\boxed{\operatorname{Ldim}(\mathcal J([2]\times[2^{k+1}-2]))=2k.}
\]
Thus a natural width-two family has unbounded adaptive rank despite a fixed VC dimension, with an infinite, explicit sequence of exact ranks. For all \(n\ge2\), the more general bounds
\[
\max_{0\le t\le n}\left(\lfloor\log_2(t+1)\rfloor+\lfloor\log_2(n-t+1)\rfloor\right)
\le \operatorname{Ldim}(\mathcal J(P_n))
\le \left\lfloor\log_2\binom{n+2}{2}\right\rfloor
\]
show that its online dimension grows as \(2\log_2 n+O(1)\).

## Assumptions and scope
A lower ideal \(I\) of \(P\) is a subset closed downwards under \(\le_P\). A complete binary membership-query mistake tree of depth \(d\) is shattered if every sequence of \(d\) branch labels is realized by some \(I\in\mathcal J(P)\) on the queries along that branch. A class with one hypothesis has Littlestone dimension zero. All posets in the algorithmic assertion are given explicitly by their order relation; \(w\) bounds their actual maximum antichain size. A transition counts one evaluation of the recurrence at a candidate query; bitset operations or transitive-closure preprocessing are accounted for separately.

The grid \([2]\times[n]\) uses the product order: \((i,j)\le(i',j')\) exactly when both coordinates are no larger. In a lower ideal its first row has \(a\) cells and its second row has \(b\) cells, with \(0\le b\le a\le n\); conversely every such pair specifies an ideal. A query in the first row at column \(r\) tests \(a\ge r\), and a query in the second row tests \(b\ge r\). The dyadic statement includes all positive integers \(k\), with no additional parity or boundary assumptions.

## Proof
**1. Closure under conditional queries.** For two ideals \(L\subseteq U\), write \([L,U]\) for the hypothesis class of all ideals \(I\) with \(L\subseteq I\subseteq U\). This is precisely an interval of the distributive ideal lattice. For any query \(x\in U\setminus L\), both labels occur: \(L\) excludes \(x\), while \(U\) includes it. The positive branch consists of \([L\cup\downarrow x,U]\), and the negative branch consists of \([L,U\setminus\uparrow x]\). Here the principal downset and upset are taken in \(P\). Both new endpoints are ideals; both intervals are nonempty and have a strictly smaller free set \(U\setminus L\). Thus, if \(R(L,U)\) is the Littlestone rank of this residual class, then
\[
R(L,L)=0,\qquad
R(L,U)=1+\max_{x\in U\setminus L}
\min\{R(L\cup\downarrow x,U),R(L,U\setminus\uparrow x)\}
\]
when \(L\subsetneq U\). This is exact by induction on \(|U\setminus L|\): the root of any complete tree must query some free element, and any eligible root can be followed by optimal complete trees of the smaller branch dimension. The initial answer is \(R(\varnothing,P)\).

**2. State bound.** Every ideal is uniquely determined by its antichain of maximal elements; this antichain has at most \(w\) elements. Hence \(|\mathcal J(P)|\le\sum_{j=0}^{w}\binom{n}{j}\). Memoization therefore encounters at most \(|\mathcal J(P)|^2\) ordered ideal-endpoint pairs, and there are at most \(n\) candidate queries per state. Precomputing the order's transitive closure and representing ideals by bitsets makes each transition explicit, with polynomial overhead. The claimed transition and time bounds follow. In particular, there is no enumeration of exponential-size mistake trees.

**3. Static dimension.** For any poset, a shattered support cannot contain two comparable distinct elements: the labeling setting the upper one to one and the lower one to zero is impossible in a lower ideal. Conversely an antichain is shattered, because for any chosen positive subcollection its downward closure intersects the antichain in exactly that chosen subcollection. Therefore \(\operatorname{VCdim}(\mathcal J(P))\) equals the poset width. The grid \([2]\times[n]\) has width two when \(n\ge2\).

**4. Dyadic exact ranks.** A nested chain of exactly \(2^k\) distinct threshold concepts on an ordered parameter has Littlestone dimension \(k\). Its upper bound is the number-of-hypotheses bound; the lower bound comes from binary-halving the parameter interval recursively \(k\) times.

Fix \(k\ge1\) and put \(t=2^k-1\), \(n=2t\). Restrict \(\mathcal J(P_n)\) to the concepts parametrized by \(t\le a\le2t\) and \(0\le b\le t\). The condition \(b\le a\) is then automatic, so there are exactly \(2^k\) independent possible values for each of \(a\) and \(b\). Using first-row queries to shatter a binary tree of depth \(k\) over \(a\), then second-row queries to shatter a depth-\(k\) tree over \(b\) below each leaf, produces a complete tree of depth \(2k\). Hence \(\operatorname{Ldim}\ge2k\).

The entire class has exactly \(\binom{n+2}{2}\) ideals, since its parameter pairs satisfy \(0\le b\le a\le n\). For the chosen \(n\), this number is \((2^{k+1}-1)2^k=2^{2k+1}-2^k\), which lies in \([2^{2k},2^{2k+1})\). Every shattered complete depth-\(d\) tree requires \(2^d\) distinct hypotheses, so the upper bound is \(d\le2k\). Thus equality holds.

**5. General two-row bounds.** For an arbitrary \(0\le t\le n\), the subfamily with \(t\le a\le n\) and \(0\le b\le t\) is the independent product of threshold chains of lengths \(n-t+1\) and \(t+1\). Concatenating their complete mistake trees yields the displayed lower bound. The class size gives the upper bound. Taking \(t\) closest to half of \(n\) shows that both bounds are \(2\log_2 n+O(1)\). No exact formula for every \(n\) is claimed.

## Verification
The accompanying Python 3 standard-library checker `verify.py` implements the four-boundary recurrence \(R(a_{\min},a_{\max},b_{\min},b_{\max})\) for \([2]\times[n]\), and separately implements the hypothesis-subset definition of Littlestone rank. It checks their equality for all \(1\le n\le6\), computes exact two-row ranks through \(n=30\), and verifies the four dyadic cases \(n=2,6,14,30\). An independent ideal-enumeration implementation checks the general interval-state recurrence against hypothesis-subset recursion for all 242 labeled reflexive transitive antisymmetric relations on sets with \(1\le|P|\le4\). Successful output is `ORDER_IDEAL_ONLINE_PASS 242 posets 6 direct grid crosschecks 30 grid ranks 4 dyadic equalities`.

The rank list for \(n=1,\ldots,30\) is `1,2,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7,7,8,8,8,8,8,8`. These tests corroborate the recurrence and the parameterization; the all-parameter mathematical proof is independent of finite enumeration.

## Relationship to prior work
The notion of Littlestone dimension and its role in online learning are standard. Guingona, Kolesnikov, Nierwinski and Soucy (2021) determine dimensions of zero-set classes of linear combinations, not lower ideals of bounded-width posets. Ghazi, Golowich, Kumar and Manurangsi (2021) prove general Boolean closure bounds, not the exact rank recurrence for order ideals or its fixed-width state count. Earlier ideal-lattice algorithms such as Squire's recurrence, as discussed in the 2013 paper on Gray-code enumeration, concern generating ideals rather than evaluating complete adversarial mistake trees.

The novel scope asserted here is the *explicit bounded-width online-rank algorithm together with the exact infinite dyadic sequence*, not the definitions, the VC dimension of order ideals, the binary-search fact for threshold chains, or the generic finite-class entropy bound. Prior finite computations on particular trees or chain interleavings do not by themselves imply these uniform statements.

## Limitations
The algorithm has polynomial degree depending on width; it is not shown to be fixed-parameter tractable. No closed form for all two-row widths is established. The exact rank on the dyadic subsequence does not assert that every class of width two saturates its information bound, nor that every two-row size does so. Novelty was checked against identified literature and accessible records, not proved by absence from searches; alternative terminology may contain prior results. Self-review is not independent mathematical validation.

## References
1. V. Guingona, A. Kolesnikov, J. Nierwinski, and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1, first submitted 2021-09-10, https://arxiv.org/abs/2109.04805.
2. B. Ghazi, N. Golowich, R. Kumar, and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, Proceedings of Machine Learning Research 132 (2021), pp. 686–696, https://proceedings.mlr.press/v132/ghazi21a.html.
3. *Efficient generation of the ideals of a poset in gray code order, part II*, Theoretical Computer Science 502 (2013), pp. 30–45, https://doi.org/10.1016/j.tcs.2012.02.008.
