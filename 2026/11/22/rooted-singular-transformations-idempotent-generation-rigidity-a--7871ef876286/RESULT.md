# Rooted singular transformations: idempotent generation, rigidity, and tournament enumeration

## Finding

Let \(X=\{0,1,\dots,n-1\}\) with \(n\ge 2\), let \(Y=X\setminus\{0\}\) and \(m=n-1\), and put
\[
P_n=\{f:X\to X:f(0)=0\},\qquad S_n=\{f\in P_n:|f(X)|<n\}.
\]
Compose on the right, so \(x(fg)=(xf)g\). For distinct \(a,b\in X\), the elementary collapse \(e_{a\to b}\) maps \(a\) to \(b\) and fixes every other point; it belongs to \(S_n\) precisely when \(a\ne0\).

For a set \(A\) of idempotents in \(S_n\), let \(D_A\) be the directed graph on \(Y\) with an arc \(a\to b\) when \(e_{a\to b}\in A\). Then \(A\) generates \(S_n\) if and only if it contains every \(e_{a\to0}\) for \(a\in Y\) and the arcs of \(D_A\), interpreted as elementary collapses on \(Y\), generate the singular transformation semigroup on \(Y\). For \(m\ge3\), the second condition is equivalent to strong connectivity and containment of a tournament. For \(m=2\) it requires both opposing arcs; for \(m=1\) there is no nonroot condition.

The ordinary rank and idempotent rank are
\[
\begin{array}{c|ccc}
& n=2 & n=3 & n\ge4\\\hline
\operatorname{rank}(S_n) & 1&3&\binom{n}{2}\\
\operatorname{idrank}(S_n) & 1&4&\binom{n}{2}.
\end{array}
\]
For \(n\ge4\), the minimum idempotent generating sets are exactly the unions of all \(n-1\) arrows into \(0\) with the arcs of one strongly connected tournament on \(Y\). The minimum idempotent generating set is unique for \(n=2\) or \(3\). For \(n\ge4\) their number is \(s_{n-1}\), where \(s_m\) counts labelled strong tournaments and satisfies
\[
s_1=1,\qquad s_m=2^{\binom{m}{2}}-\sum_{k=1}^{m-1}\binom{m}{k}s_k 2^{\binom{m-k}{2}} \quad (m\ge2).
\]
In particular \(s_2=0,\ s_3=2,\ s_4=24,\ s_5=544\).

## Assumptions and scope

Ranks refer to the minimum size of a generating set (arbitrary or idempotent) using nonempty products inside the finite singular ideal \(S_n\). Neither the units nor the rank of the full pointed monoid \(P_n\) are at issue. In a tournament, each pair of distinct vertices supports exactly one directed arc; strong connectivity requires a directed path between every ordered pair. The unpointed arc criterion used below is the classical theorem of Howie, as recalled by East, Gadouleau and Mitchell and by Cameron et al.

## Proof

**Kernels and corank-one factors.** The image size of a product is at most that of any factor. For a rank-\((n-1)\) product in \(S_n\) all factors have rank \(n-1\), and the first factor has the same kernel partition as the product: the first kernel refines the final one and both have just one doubleton as their only nonsingleton block. Every unordered pair occurs as that doubleton, since an elementary collapse with nonroot source can be chosen for it. Therefore any generating set requires at least \(\binom n2\) generators. A rank-\((n-1)\) idempotent fixes its image, so it must be an elementary collapse. The sole idempotent with kernel doubleton \(\{0,a\}\) is \(e_{a\to0}\); all such arrows are thus compulsory for idempotent generation.

**The nonroot condition is necessary.** Take a rank-\((m-1)\) transformation of \(Y\) and extend it to fix \(0\) on \(X\). Its rank is \(n-1\) and its preimage of \(0\) is \(\{0\}\). Consider a generating word in the corank-one idempotents. For a root-arrow factor \(e_{a\to0}\), if the image immediately before the factor contains \(a\), some nonroot input is sent to \(0\) and remains there under all later factors, an impossibility. Otherwise that root arrow is the identity on the preceding image and can be deleted without changing the value of the word. The initial preceding map is understood to be the identity for this argument. Removing all such ineffective factors leaves a nonempty word of nonroot arrows. Hence the nonroot arrows generate all rank-\((m-1)\) maps on \(Y\), which generate its full singular semigroup: below the top singular rank, split one point out of a nonsingleton fiber to an unused image value and then collapse that value back, inducting on rank deficit. This last argument is needed only when there are ranks below \(m-1\); for \(m=1\) no nonroot maps are needed.

**Sufficiency and the pointed reduction.** Suppose all root arrows are available and the nonroot arcs generate the singular maps on \(Y\). For a rank-\((n-1)\) map \(f\in S_n\), if its kernel doubleton lies in \(Y\), it sends no point of \(Y\) to \(0\), and its restriction to \(Y\) is singular. A word of the nonroot arcs therefore realizes \(f\). Otherwise its doubleton is \(\{0,a\}\). For \(m\ge2\) choose \(b\in Y\setminus\{a\}\) and take \(g:Y\to Y\) with \(g(x)=f(x)\) for \(x\ne a\) and \(g(a)=f(b)\). Then \(g\) is singular on \(Y\), and after extension by the fixed point \(0\) we have \(f=e_{a\to0}g\). When \(n=2\) the only singular pointed map is \(e_{1\to0}\). Finally, if \(f\) has rank \(r\le n-2\), take a nonroot point \(a\) in a nonsingleton fiber and an unused image value \(y\in Y\). Replacing \(f(a)\) by \(y\) produces a pointed map \(g\) of rank \(r+1\), with \(f=g e_{y\to f(a)}\). The second factor has rank \(n-1\) and has already been generated. Induction starting at rank \(n-1\) gives every lower rank. This proves the full criterion together with Howie's unpointed result, or the direct check that the two singular maps on a two-point set are constants and both are needed.

**Sharp ranks and idempotent extremizers.** A strong tournament exists for each \(m\ge3\): start with a directed three-cycle and add vertices, each with at least one entering and one leaving arc to the old tournament. The ordinary kernel lower bound is attained by combining such a tournament with the compulsory arrows; the resulting size is \(m+\binom m2=\binom n2\). Conversely, at that size an idempotent generating set has exactly one corank-one idempotent per kernel doubleton, so the nonroot digraph is a tournament and must be strong. At \(n=3\), the criterion forces the four available corank-one idempotents, but arbitrary generators need not be idempotent. In tuple notation (values at \(0,1,2\)), set
\[
a=(0,0,1),\qquad b=(0,2,0),\qquad c=(0,1,1).
\]
Their products \(ab=(0,0,2),\ ba=(0,1,0),\ cb=(0,2,2),\ a^2=(0,0,0)\) supply the four remaining maps of \(S_3\), which has \(3^2-2!=7\) maps. This attains the kernel lower bound three and proves the strict difference between the two ranks here. At \(n=2\) the unique map is idempotent and the two ranks are one.

**Counting the extremizers.** A tournament has a unique source strongly connected component: between distinct components all edges are oriented the same way, and the tournament on components is acyclic. If the source has \(k<m\) vertices, choose its labels and one of its \(s_k\) strong tournaments, attach every edge from it to the complement pointing outward, and choose any tournament on the remaining labels. This gives the stated subtraction formula for strong tournaments, applied here to count the minimum pointed idempotent generating sets. The two smaller cases follow directly from the criterion.

## Verification

`python3 verify.py` enumerates singular pointed maps and checks composition closure for all nonroot tournaments at \(n=4,5\), the cyclic tournament at \(n=6\), the small idempotent cases, and the tournament recurrence. Its recorded output is in `VERIFY_OUTPUT.txt`. `python3 verify_n3.py` separately exhausts all candidate generating subsets of the seven singular maps on three points and of their idempotents, checking the ordinary rank three, idempotent rank four, and the explicit example. The general result follows from the kernel and factorizations above and the cited unpointed theorem, not extrapolation from finite checks.

## Relationship to prior work

Howie's classical results give idempotent and arc generation, minimum size and the tournament criterion for the *unpointed* singular semigroup. Strong tournament enumeration itself is classical (Wright, as cited in East–Gadouleau–Mitchell); the recurrence is included to express the count of the pointed extremizers, not as a claim of a new tournament enumeration. Assiri and Al-bar study the point-fixing monoid (with root labelled 1) in the context of the dominion of order-decreasing maps, and explicitly treat its singular rank classes. Their printed equality of the semigroup generated by the corank-one class with the whole point-fixing monoid cannot include its units: no rank-\((n-1)\) generator product has rank \(n\). No equality of the full pointed monoid with that dominion is used here. Generation by the entire top singular rank is not itself the distinguishing claim; the criterion determines precisely which subsets of elementary idempotents suffice, with compulsory rooted arrows, tournament extremizers, and the difference between ordinary and idempotent ranks at three points.

Partition-preserving maps and partial pointed maps involve different transformation semigroups. The abstract of Xu–Gao–Lu–You uses “1-singular” for a non-singleton property and does not identify its objects as this fixed-point singular ideal; no claim about their full definition or priority is made without the complete paper. The theorem does not extend here to several distinguished fixed points or to the rank of the full pointed monoid.

## References

1. H. H. Assiri and J. A. Al-bar, *On the Dominions of Certain Semigroups of Transformations*, §2, https://arxiv.org/abs/2606.28477.
2. J. M. Howie, *The subsemigroup generated by the idempotents of a full transformation semigroup*, J. London Math. Soc. **41** (1966), 707–716.
3. J. M. Howie, *Idempotent generators in finite full transformation semigroups*, Proc. Roy. Soc. Edinburgh **81A** (1978), 317–323, https://doi.org/10.1017/S0308210500010647.
4. J. East, M. Gadouleau, and J. D. Mitchell, *Structural aspects of semigroups based on digraphs*, Introduction and reference to E. M. Wright's *The number of irreducible tournaments* (1970), https://arxiv.org/html/1704.00937v2.
5. P. J. Cameron, A. Castillo-Ramírez, M. Gadouleau, and J. D. Mitchell, *Lengths of words in transformation semigroups generated by digraphs*, J. Algebr. Comb. **45** (2017), 149–170, https://doi.org/10.1007/s10801-016-0703-9.
6. I. Dolinka, J. East, and J. D. Mitchell, *Idempotent rank in the endomorphism monoid of a non-uniform partition*, https://arxiv.org/abs/1504.02520.
7. B. Xu, R. Gao, L. Lu, and T. You, *Rank of the 1-singular transformation semigroup*, J. Shandong Univ. (Nat. Sci.) **57** (2022), no. 12, 81–85, https://doi.org/10.6040/j.issn.1671-9352.0.2022.126.
