# Strong-resolving polynomials of rank-two Grassmann graphs over finite fields

## Finding
For each prime power \(q\) and every integer \(d\ge4\), let \(G=G_q(d,2)\) be the graph whose vertices are the \(2\)-dimensional vector subspaces of \(\mathbb F_q^d\), adjacent exactly when their intersection has dimension \(1\). A subset \(W\subseteq V(G)\) is strongly resolving **if and only if** the projective lines corresponding to \(V(G)\setminus W\) meet pairwise.

Put
\[
N=\genfrac{[}{]}{0pt}{}{d}{2}_q,\quad P=\genfrac{[}{]}{0pt}{}{d}{1}_q,\quad T=\genfrac{[}{]}{0pt}{}{d}{3}_q,\quad
r=\genfrac{[}{]}{0pt}{}{d-1}{1}_q,\quad s=q^2+q+1.
\]
The Gaussian coefficient \(\genfrac{[}{]}{0pt}{}{a}{b}_q\) counts \(b\)-dimensional subspaces of \(\mathbb F_q^a\). The complete omission polynomial \(I_{q,d}(t)=\sum_{W\text{ strongly resolving}}t^{N-|W|}\) is
\[
\boxed{I_{q,d}(t)=1+Nt+P((1+t)^r-1-rt)+T\bigl((1+t)^s-1-st-s((1+t)^{q+1}-1-(q+1)t)\bigr).}
\]
Consequently the entire strong-resolving-set polynomial is \(R_{q,d}(z)=z^NI_{q,d}(z^{-1})\), including the full set \(W=V(G)\).

Every inclusion-minimal strongly resolving set is the complement either of a full point pencil (all lines through a fixed point) or of a full plane top (all lines contained in a fixed projective plane). There are exactly \(P\) sets of size \(N-r\) and exactly \(T\) sets of size \(N-s\). These two geometric families are disjoint, even when \(d=4\) and \(r=s\). For \(d\ge5\) the strong metric dimension is \(N-r\), attained by exactly \(P\) bases; the other \(T\) inclusion-minimal sets are strictly larger and the gap is \(r-s\). For \(d=4\), the strong metric dimension is \(N-r=N-s\) and there are \(P+T\) bases.

## Assumptions and scope
All graphs are finite, simple and connected. The ground field \(\mathbb F_q\) exists because \(q\) is a prime power. Dimensions are vector-space dimensions; a projective point is a \(1\)-space, a line a \(2\)-space, and a projective plane a \(3\)-space. A vertex \(w\) *strongly resolves* distinct vertices \(u,v\) if \(u\) belongs to some shortest \(v\)-to-\(w\) path or \(v\) belongs to some shortest \(u\)-to-\(w\) path. A set is strongly resolving if it strongly resolves every unordered pair of distinct vertices.

For \(d\ge4\), the Grassmann graph has diameter exactly two: intersecting lines have distance one, and disjoint lines have a common transversal line (one joining any chosen point on each). All projective lines in any plane meet. The integer \(s\) is both the number of lines and the number of points in a projective plane over \(\mathbb F_q\); exactly \(q+1\) of its lines pass through a fixed point.

## Proof
**1. Strong-resolution/line-intersection equivalence.** Suppose that distinct omitted vertices \(u,v\) represent disjoint projective lines. Since \(d_G(u,v)=2\) equals the diameter, any vertex \(w\) strongly resolving \(u,v\) must be \(u\) or \(v\): otherwise a shortest path from one to \(w\) through the other would have length at least three. Neither lies in \(W\), contradiction.

Conversely suppose every two omitted lines meet. Pairs containing a vertex of \(W\) are strongly resolved by that selected endpoint. For distinct omitted lines \(u,v\), write \(A=u\cap v\) for their projective point and \(\Pi\) for the unique plane spanned by both lines. Choose a point \(B\) on \(v\) other than \(A\) and a line \(w\) through \(B\) not contained in \(\Pi\), possible because \(d\ge4\). The lines \(u,w\) are disjoint but \(v,w\) meet, so \(u,v,w\) form a geodesic of length two. Pairwise intersection of omitted lines forces \(w\in W\). Thus \(w\) strongly resolves \(u,v\). This proves both directions for every \(q,d\) in scope.

**2. Classification of pairwise-intersecting line families.** Consider a family \(\mathcal F\) of at least two distinct projective lines meeting pairwise. Choose two lines meeting in a point \(A\) and spanning a plane \(\Pi\). If all lines contain \(A\), the family lies in the point pencil at \(A\). Otherwise choose a third line not through \(A\). To intersect both original lines at different points, the third line lies in \(\Pi\). Every further line outside \(\Pi\) that meets both originals must pass through \(A\), and then cannot meet the chosen third line. Hence all lines of \(\mathcal F\) lie in \(\Pi\). These are the familiar point-pencil and plane-top maximal cliques; their classical classification is not claimed as new here.

**3. Exact enumeration without overlap.** The empty family contributes \(1\), and singleton families contribute \(Nt\). Any pairwise-intersecting family of at least two lines concurrent at one point has a *unique* concurrency point (the intersection of any two lines), so all such families contribute \(P((1+t)^r-1-rt)\). Every remaining family has at least three lines, is nonconcurrent, and spans a *unique* projective plane. In any specified plane, all \(s\) lines are pairwise intersecting. After deleting its empty and singleton subsets, remove all concurrent subfamilies of size at least two: there are \(s\) possible concurrency points, with \(q+1\) lines available at each; the points are uniquely determined by any two chosen lines, so no multiple counting occurs in this subtraction. The remaining plane contribution is \((1+t)^s-1-st-s((1+t)^{q+1}-1-(q+1)t)\). Multiplying by the number \(T\) of planes proves the boxed formula coefficientwise, with no overlap between the global concurrent and nonconcurrent terms.

**4. Minimal sets and boundary.** A strongly resolving set is inclusion-minimal precisely when its omitted family is inclusion-maximal under pairwise intersection. The only maximal such families are full pencils and full plane tops by step 2; neither is properly contained in another of the two types. Their respective cardinalities are \(r\) and \(s\), and the number of pencils and tops is \(P\) and \(T\). Since \(r=s\) for \(d=4\), and \(r>s\) for \(d\ge5\), the minimum sizes and multiplicities follow. The gap \(r-s=q^3+\cdots+q^{d-2}\) is positive when \(d\ge5\).

## Verification
Run `python3 verify_grassmann_strong.py` (standard-library Python 3; no optional packages). The standalone program enumerates the projective points and lines for \((q,d)=(2,4),(3,4),(2,5)\), directly checks the defining graph's diameter-two maximally-distant behavior, enumerates every maximal line-intersection clique via an independent clique search, and tallies all their subsets against every coefficient of the formula. It reports, respectively, \(3216\), \(648651\), and \(1029728\) pairwise-intersecting families, along with pencil/top classifications. These finite checks are corroboration only; the proof above covers all stated prime powers and dimensions.

## Relationship to prior work
Bailey and Meagher study *ordinary* metric dimension of Grassmann graphs, not the strong all-set enumerator. Oellermann and Peters-Fransen established the general strong-metric/vertex-cover connection, and Rodríguez-Velázquez, Yero, Kuziak and Oellermann extend strong metric methods for graph products. Brouwer and Van Maldeghem, Section 3.5.1, explicitly give the **known** two-type maximal-clique classification of the same Grassmann graphs and their sizes. That antecedent directly supplies the maximal configurations and readily yields the minimum-set classification in conjunction with strong-metric theory; neither those ingredients nor the class sizes are independently new. The specific claim here is the closed **complete size-distribution polynomial** and its all-set incidence interpretation, including the correction of pencil/top overlap and the two boundary regimes.

## Limitations
No claim is made about ordinary metric resolving-set polynomials, higher-rank Grassmann graphs, non-prime-power parameter sets, or an independently performed audit. The maximal-clique classification is established literature; the enumeration is derived from it and elementary finite-geometric counting. Published or unindexed clique/independence polynomials could duplicate this identity, and independent priority review remains warranted. Computational examples are not a proof of the unbounded parameter family.

## References
1. R. F. Bailey and K. Meagher, *On the metric dimension of Grassmann graphs*, arXiv:1010.4495 (first public version 2010-10-21), https://arxiv.org/abs/1010.4495.
2. O. R. Oellermann and J. Peters-Fransen, *The strong metric dimension of graphs and digraphs*, Discrete Applied Mathematics 155 (2007), 356–364; DOI:10.1016/j.dam.2006.06.009.
3. J. A. Rodríguez-Velázquez, I. G. Yero, D. Kuziak and O. R. Oellermann, *On the strong metric dimension of Cartesian and direct products of graphs*, arXiv:1307.4722 (2013), https://arxiv.org/abs/1307.4722.
4. A. E. Brouwer and H. Van Maldeghem, *Strongly Regular Graphs* (2021), §3.5.1, p. 104, https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf.
