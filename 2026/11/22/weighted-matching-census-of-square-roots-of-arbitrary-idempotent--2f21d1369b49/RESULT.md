# Weighted matching census of square roots of arbitrary idempotent transformations

## Finding

For every nonempty finite labeled set \(X\) and every idempotent \(f\in\mathcal T_X\), the number of solutions to \(g^2=f\) is a weighted matching sum determined by the sizes of the fibers of \(f\). Fixed fibers and exchanged pairs of fibers have different weights.

Let \(S=f(X)=\{s_1,\ldots,s_r\}\) and let \(a_i=|f^{-1}(s_i)|\). Define
\[
F(a)=\sum_{j=0}^{a-1}\binom{a-1}{j}j^{a-1-j},\qquad
V(a,b)=\sum_{j=0}^{a-1}\sum_{k=0}^{b-1}\binom{a-1}{j}\binom{b-1}{k} k^{a-1-j}j^{b-1-k}.
\]
Then
\[
\#\{g\in\mathcal T_X:g^2=f\}=
\sum_{\substack{\pi\in S_r\\\pi^2=1}}
\prod_{\pi(i)=i}F(a_i)
\prod_{\{i,j\}\in\operatorname{Cyc}_2(\pi)}V(a_i,a_j),
\]
where \(\operatorname{Cyc}_2(\pi)\) is the set of unordered pairs in the two-cycles of \(\pi\).

For comparison with the enumeration of all maps whose square is idempotent, let \(P_n(u)=\sum_{g\in\mathcal T_n,\,g^4=g^2}u^{|\operatorname{im}g^2|}\), with \(P_0(u)=1\). Marking the cycle vertices in the known bounded-height functional-digraph enumeration gives the companion identity
\[
\sum_{n\ge0}P_n(u)\frac{z^n}{n!}=\exp\left(uR(z)+\frac{u^2R(z)^2}{2}\right),\qquad R(z)=z\exp(ze^z).
\]
This is a direct rank marking of the cycle construction underlying OEIS A060908, which gives \(P_n(1)\). The marked series is included for comparison and is not asserted as a separate originality claim.

## Assumptions and scope

\(\mathcal T_X\) is the monoid of all total self-maps of a finite labeled set, with composition \((hg)(x)=h(g(x))\); \(\mathcal T_n=\mathcal T_{\{1,\ldots,n\}}\). The target is idempotent, so all members of \(S\) are fixed by \(f\), and every \(a_i\ge1\). The convention \(0^0=1\) represents the unique empty assignment, and empty products are one. The series are formal exponential generating functions; \(n=0\) is used only in the series convention.

## Proof

**1. Restriction to the image.** If \(g^2=f\), then \(gf=g^3=fg\). For any \(s\in S\), \(f(g(s))=g(s)\), so \(g(S)\subseteq S\). The restriction of \(g\) to \(S\) squares to the identity and is therefore an involutive permutation \(\pi\) of the distinguished points, with \(g(s_i)=s_{\pi(i)}\). For every \(x\in f^{-1}(s_i)\), \(f(g(x))=g(f(x))=s_{\pi(i)}\). Thus \(g\) sends the \(i\)-th fiber into the \(\pi(i)\)-th fiber. Distinct cycles of \(\pi\) cannot interact.

**2. Fixed fibers.** Suppose \(\pi(i)=i\). Let \(A_i\) be the subset of the \(a_i-1\) nondistinguished points mapped directly to \(s_i\) by \(g\). If \(|A_i|=j\), each of the remaining \(a_i-1-j\) points must map into \(A_i\): its second image must be \(s_i\), but mapping directly to \(s_i\) would put the point in \(A_i\). Conversely every such assignment gives the prescribed square on the fiber. Choosing \(A_i\) and making these assignments gives \(\binom{a_i-1}j j^{a_i-1-j}\) possibilities. Summing over \(j\) gives \(F(a_i)\).

**3. Exchanged fibers.** Suppose \(\pi(i)=j\) and \(\pi(j)=i\). The roots satisfy \(g(s_i)=s_j\), \(g(s_j)=s_i\). Choose \(A_i\) of size \(p\) from the nondistinguished points of the \(i\)-fiber to map directly to \(s_j\), and \(A_j\) of size \(q\) from those of the \(j\)-fiber to map directly to \(s_i\). Each remaining point of the \(i\)-fiber must map into \(A_j\), and each remaining point of the \(j\)-fiber into \(A_i\). These conditions are sufficient as well as necessary for \(g^2=f\) on the two fibers. At fixed \(p,q\) the count is \(\binom{a_i-1}p\binom{a_j-1}q q^{a_i-1-p}p^{a_j-1-q}\), giving \(V(a_i,a_j)\) on summation.

**4. Completeness.** The restriction \(\pi\), the subsets \(A_i\), and the remaining images are uniquely recovered from \(g\). Conversely the choices just described define a total map with square \(f\). Multiplying over the cycles and summing over the involutions proves the matching formula.

**5. Rank marking of the global enumeration.** In a finite functional digraph, \(g^4=g^2\) means that each vertex reaches a point fixed by \(g^2\) after at most two steps. Equivalently, cycles have length one or two, and attached in-trees have height at most two. Every cycle vertex is in \(\operatorname{im}g^2\), and these are all the vertices in the image. A labeled rooted tree of height at most two is a root with an unordered set of children, each with an unordered set of leaves, giving \(R(z)=z\exp(ze^z)\). Each cycle vertex contributes a factor of \(u\): a one-cycle component contributes \(uR(z)\), and a two-cycle component contributes \((uR(z))^2/2\). Taking an unordered set of components gives the stated series, with the unmarked series precisely that of A060908.

## Verification

The standalone Python standard-library program `verify_roots.py` enumerates every self-map for \(1\le n\le7\), computes its square and checks whether the square is idempotent. It groups the roots by the actual square and checks the matching formula over every idempotent. It also checks the rank-weighted totals at \(u=1,2,3\) by exact rational series arithmetic. The unmarked total counts for \(n=1,\ldots,7\) are \(1,4,25,194,1791,19312,237637\), with the next formal coefficient \(3280524\). These finite checks are ancillary to the bijective proof.

## Relationship to prior work

Kozyra (2018, Propositions 14 and 17) counts the identity-map and constant-map cases, respectively. The identity has only singleton fibers, for which \(F(1)=V(1,1)=1\), so the count is precisely the ordinary number of involutions. The constant map has one fiber, giving \(F(|X|)\). The contribution assessed here is the explicit profile-sensitive enumeration for every idempotent, including arbitrary unequal fiber sizes and the interaction \(V(a,b)\) for exchanged fibers. General finite half-iterate algorithms, graph-based existence criteria, and fiber-size obstructions address related questions. The accessible results of Kozyra (2018) and Bhat–Gopalakrishna (2022 online) compared here do not provide this fixed-target profile formula; the body of Kozyra (2021) was not available for full comparison.

The unmarked global sequence and its exponential generating function are already tabulated in OEIS A060908, which cites Goulden–Jackson (1983). Its general cycle construction uses the component terms \(T_k^d/d\) for cycle lengths \(d\mid m\), with bounded-height tree series \(T_k\); for \(k=m=2\) those terms are \(R(z)\) and \(R(z)^2/2\). Multiplying each \(d\)-cycle term by \(u^d\) gives the companion rank series above. Neither the unmarked enumeration nor this direct marking is part of the originality claim for the weighted matching formula.

## Limitations

The result concerns idempotent target maps in finite full transformation monoids, not non-idempotent targets or extremal root counts. The global rank series counts maps \(g\) whose squares are idempotent; it does not count distinct squares. Wider historical priority for the arbitrary-idempotent matching formula is not certified.

## References

1. P. M. Kozyra, *On Half Iterates of Functions Defined on Finite Sets*, Computational Methods in Science and Technology 24(3) (2018), 187–209, DOI:10.12921/cmst.2018.0000027. Propositions 14 and 17.
2. P. M. Kozyra, *The Structure of Functional Graphs for Functions from a Finite Domain to Itself for Which a Half Iterate Exists*, Theory and Applications of Graphs 8(1) (2021), DOI:10.20429/tag.2021.080108.
3. B. V. Rajarama Bhat and C. Gopalakrishna, *Iterative square roots of functions*, Ergodic Theory and Dynamical Systems 43 (2023), 2201–2227, DOI:10.1017/etds.2022.35.
4. OEIS A060908, https://oeis.org/A060908, COMMENTS and FORMULA; the entry cites I. P. Goulden and D. M. Jackson, *Combinatorial Enumeration*, Wiley, 1983.
