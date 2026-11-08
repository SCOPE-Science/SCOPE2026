# An infinite third-versus-fourth specialization separation for four-spine caterpillars

## Finding

For each integer \(h\geq0\), let
\[
 A_h=C_{(h+2,h+1,h+3,3)},\qquad
 B_h=C_{(h+3,h+1,h+2,3)}.
\]
These are nonisomorphic trees on \(3h+9\) vertices. Define, for \(k\geq2\),
\[
 P_k(G;q,t)=\sum_{\substack{\kappa:V(G)\to\{0,\ldots,k-1\}\\
 \kappa\text{ proper}}}
 q^{\sum_{v\in V(G)}\kappa(v)}t^{|\kappa(V(G))|}.
\]
Then, as polynomials in two independent variables,
\[
 \boxed{P_3(A_h;q,t)=P_3(B_h;q,t)\quad\text{for every }h\geq0.}
\]
Nevertheless the ordinary fourth principal specializations are distinct, with an exact low-degree separating coefficient:
\[
 \boxed{[q^8]\big(P_4(A_h;q,1)-P_4(B_h;q,1)\big)
 =\begin{cases}14,&h=0,\\4,&h=1,\\2,&h\geq2.\end{cases}}
\]
In particular, \(P_4(A_h;q,t)\ne P_4(B_h;q,t)\) for every \(h\geq0\). The \(h=0\) equality at three colors is the example reported in the motivating paper; the uniform infinite family and separating four-color coefficients are the findings here.

## Assumptions and scope

For a positive composition \((a,b,c,d)\) with \(a,d\geq2\), the caterpillar \(C_{(a,b,c,d)}\) has a path of four spine vertices in order; the respective spine vertices are adjacent to \(a-1,b-1,c-1,d-1\) distinct pendant vertices. Its order is \(a+b+c+d\). Colors are \(0,1,\ldots,k-1\); adjacent vertices have different colors, and \(t\) records the number of distinct colors actually used, without surjectivity requirements. The coefficient \([q^8]\) is a formal polynomial coefficient, not evaluation at a numerical value of \(q\). All assertions hold for every integer \(h\geq0\), including the boundary composition with second part one.

## Proof

**The third specialization.** For colors \(i\in\{0,1,2\}\), put
\[
 w_i=q^i,\qquad
 L_0=q+q^2,\quad L_1=1+q^2,\quad L_2=1+q.
\]
If a spine vertex of color \(i\) has \(e\) pendant neighbors, summing the weights of their proper colorings gives \(w_i L_i^e\). Thus, with \(a=b+1,c=b+2,d=3\) and \(b=h+1\), the three-color specialization at \(t=1\) is the complete sum
\[
 F(a,b,c,d)=\sum_{\substack{i\ne j,\ j\ne k,\ k\ne l\\i,j,k,l\in\{0,1,2\}}}
  w_iL_i^{a-1}\,w_jL_j^{b-1}\,w_kL_k^{c-1}\,w_lL_l^{d-1}.
\]
Here and below the simultaneous conditions merely restrict adjacent spine colors, not nonadjacent colors. Define \(D_i=w_iL_i^2\). In the difference \(F(a,b,c,3)-F(c,b,a,3)\), contributions with the first and third spine colors equal cancel. Fixing the second spine color \(j\), and writing \(\{p,r\}=\{0,1,2\}\setminus\{j\}\), the two remaining ordered assignments of those first and third colors combine to
\[
 \Delta=q^3(L_0L_1L_2)^{b-1}
 \sum_{j=0}^2 L_pL_r(L_r-L_p)(D_p-D_r).
\]
The order of \(p,r\) is immaterial because both differences change sign upon swapping them. The following two polynomial identities are exact:
\[
 D_0=(q+q^2)^2=q^2(1+q)^2=D_2,
\]
\[
 L_0L_1(L_1-L_0)=L_1L_2(L_2-L_1)=q(1-q)(1+q)(1+q^2).
\]
The \(j=1\) summand vanishes since \(D_0=D_2\); the \(j=0\) and \(j=2\) summands cancel by the second identity. Hence \(\Delta=0\) for every \(b\geq1\), proving equality of the ordinary third specializations.

Because every proper coloring of a nontrivial connected bipartite graph with three available colors uses exactly two or three colors, it suffices to identify the \(t^2\) term. The two parts of the bipartition for either caterpillar have cardinalities
\[
 U=b+d=h+4,\qquad V=a+c=2h+5.
\]
For each pair of available colors \(i<j\), its two surjective proper colorings contribute \(q^{iU+jV}+q^{jU+iV}\), so
\[
 [t^2]P_3(A_h;q,t)=[t^2]P_3(B_h;q,t)
 =\sum_{0\leq i<j\leq2}(q^{iU+jV}+q^{jU+iV}).
\]
Subtracting this common coefficient from the common ordinary polynomial proves equality of the \(t^3\) coefficients. Thus the complete \(t\)-refined third specializations agree.

**Separation at four colors.** Let
\[
 d(h)=[q^8]\big(P_4(A_h;q,1)-P_4(B_h;q,1)\big).
\]
For \(h\geq8\), a four-coloring contributing to degree at most eight cannot color any of the first three spine vertices zero. Indeed, if the first spine color is zero its \(h+1\) leaves alone contribute degree at least \(h+1\geq9\); if the third is zero its \(h+2\) leaves contribute at least ten; and if the second is zero its \(h\) leaves together with its two necessarily positive spine neighbors contribute at least \(h+2\geq10\). Therefore all three of these spine colors belong to \(\{1,2,3\}\).

For a positive spine color \(i\), the available leaf-color polynomial is \(1+R_i(q)\) with \(R_i(0)=0\). For each fixed proper spine-color assignment without zero among the first three positions, its contribution to \([q^8]\) is a product of factors of the form \((1+R_i(q))^{h+s_i}\) times an \(h\)-independent polynomial. By the binomial theorem, the coefficient of degree at most eight of each such factor is polynomial in \(h\), of degree at most eight; in a product the degrees in \(h\) sum to at most the total \(q\)-degree. Consequently \(d(h)\), restricted to integers \(h\geq8\), is the value of a single rational polynomial in \(h\) of degree at most eight.

A finite, exact coefficient calculation using the displayed spine-color sum with four colors gives
\[
 d(0)=14,\quad d(1)=4,\quad d(h)=2\quad(2\leq h\leq16).
\]
The complete reproducible integer-polynomial calculation is in `artifacts/verify.py`. Since a polynomial of degree at most eight taking the value two at the nine distinct integers \(8,9,\ldots,16\) is identically two, this establishes \(d(h)=2\) for every \(h\geq8\); the same calculation explicitly covers \(0\leq h\leq7\). This is a finite exact certificate plus a polynomial-degree argument, not extrapolation from finitely many graph instances. Nonzero \(d(h)\) proves distinct ordinary fourth specializations; setting \(t=1\) then proves distinct \(t\)-refined fourth specializations.

**Nonisomorphism.** A caterpillar with four spine vertices and both endpoint parts at least two has a unique central four-vertex path after all leaves are removed. Graph isomorphisms therefore identify its composition only up to reversal. The compositions for \(A_h\) and \(B_h\) are neither equal nor reversals: the first entries differ, while equality with the reversal would require simultaneously \(h+2=3\) and \(3=h+3\), impossible. Thus the trees are nonisomorphic, and their orders \(3h+9\) are unbounded.

## Verification

Run `python3 artifacts/verify.py`. The standalone Python program uses only standard-library exact integer arithmetic. It independently checks the two nontrivial three-color polynomial cancellation identities, directly enumerates actual proper vertex colorings (including the number of used colors) at \(h=0,1,2\), and checks the full three-color spine polynomials at \(h=0,\ldots,12\). For the fourth-color step it constructs the entire degree-eight truncation of the coloring sum and verifies \(d(0),\ldots,d(16)\) exactly; this is the finite input to the degree-eight interpolation proof. Additional checks at \(h=19,25,40\) are corroboration, not needed for the theorem. The proof's infinite steps are the formal cancellation and the polynomial-degree bound.

## Relationship to prior work

Bingham, Celano, Commins, Orellana, Pan and Simone introduced the \(t\)-chromatic symmetric function, determined second-specialization classes, and proved third-specialization reconstruction for caterpillars with three spine vertices (arXiv:2610.31785v1, October 22, 2026). Their Introduction explicitly gives \(C_{(2,1,3,3)}\) and \(C_{(3,1,2,3)}\) as one pair of four-spine caterpillars not distinguished by the third \(t\)-refined specialization. This is exactly the \(h=0\) case here and is not claimed as new. The present claim explains an unbounded family extending that example and establishes an exact, positive coefficient distinguishing it at the fourth specialization.

The separate ordinary-specialization family \((5,j,j,4,3)\), \((4,j,j,5,3)\) discussed in Remark 3.11 of that paper concerns five spine vertices and unequal second ordinary specializations; it does not imply the present four-spine \(t\)-refined equalities and fourth-color separation. An independently available subsequent account of that five-spine question and a finite unrelated uniqueness counterexample were also compared; neither provides the stated four-spine family or its fourth-color coefficient.

## Limitations

The theorem concerns exactly this one-parameter family of four-spine caterpillars and principal specializations with three and four available colors. It does not classify all third-specialization collisions or establish fourth-specialization injectivity on all trees. The coefficient calculation is exact, but the general fourth-color separation relies on its independently stated degree-bound argument. Priority remains provisional: other unindexed or unpublished equivalent infinite families cannot be excluded, and no independent mathematical audit has been performed.

## References

1. A. Bingham, K. Celano, P. Commins, R. Orellana, J. Pan and M. C. Simone, *Principal specializations of the \(t\)-chromatic symmetric function*, arXiv:2610.31785v1, first posted 2026-10-22. https://arxiv.org/html/2610.31785v1
2. *Equal third and unequal second principal specializations for a caterpillar family*, an independently available account of the five-spine ordinary-specialization question. https://www.trureturing.org/research/bingham-2026-caterpillar-principal-specialization-family/
3. *The exhaustive-pairs question for caterpillar principal specializations*, an independently available account of a finite ordinary-specialization uniqueness counterexample. https://www.trureturing.org/research/bingham-2026-caterpillar-principal-specialization-uniqueness/
