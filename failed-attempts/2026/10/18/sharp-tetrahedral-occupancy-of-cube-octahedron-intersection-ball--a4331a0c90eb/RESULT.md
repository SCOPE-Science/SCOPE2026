# Sharp tetrahedral occupancy of cube–octahedron intersection balls

## Finding
For every real parameter \(1\le c\le3\), let
\[
 K_c=[-1,1]^3\cap\{(x_1,x_2,x_3)\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le c\}.
\]
Among **all** nondegenerate or degenerate tetrahedra contained in \(K_c\), the exact maximum Euclidean volume is
\[
 \boxed{M(c)=\frac16\begin{cases}
 4c^2-6c+4,&1\le c\le\frac32,\\
 8(c-1),&\frac32\le c\le2,\\
 8\bigl(1+(c-2)^2\bigr),&2\le c\le3.
 \end{cases}}
\]
Thus the optimal configuration changes type at \(c=3/2\) and \(c=2\). In the respective open intervals \((1,3/2)\), \((3/2,2)\), and \((2,3)\), exactly \(24\), \(6\), and \(12\) **vertex-supported** tetrahedra maximize volume. At \(c=3/2\), exactly \(30\) vertex-supported tetrahedra maximize volume. For \(c=1,2,3\), the corresponding counts, using distinct geometric vertices, are \(12,6,2\).

Moreover,
\[
 \boxed{\frac{M(c)}{\operatorname{vol}_3(K_c)}\ge\frac16}
\]
for every \(1\le c\le3\), with equality **if and only if** \(c=3/2\), the regular truncated-octahedron parameter. This determines the unique least favorable member of the entire cube-to-octahedron family for optimal contained-tetrahedron volume fraction.

## Assumptions and scope
The containing body is the closed, full-dimensional, centrally symmetric polytope \(K_c\); its geometry is fixed, without any normalization by inradius or edge length. Contained tetrahedra may have arbitrary vertices, positions, and orientations. \(M(c)\) denotes their unrestricted maximum, not a minimum or a vertex-only optimization. Vertex-supported maximizing counts do **not** purport to classify all possible continuous equality configurations.

For \(1<c<2\), the vertices of \(K_c\) are the \(24\) distinct signed permutations of \((1,c-1,0)\). For \(2<c<3\), they are the \(24\) distinct signed permutations of \((1,1,c-2)\). At the endpoints \(c=1,2,3\), there are \(6,12,8\) distinct vertices respectively. The piecewise volume of \(K_c\) itself is
\[
 \operatorname{vol}_3(K_c)=\frac43\left[c^3-3(c-1)^3+3\max\{c-2,0\}^3\right],\quad1\le c\le3.
\]
This formula follows from the inclusion–exclusion formula for the part of \([0,1]^3\) below the plane \(x_1+x_2+x_3=c\), multiplied by eight for the orthants.

## Proof
**1. Reduction to vertices.** Fix three vertices of a candidate tetrahedron and vary its fourth point within the convex polytope. The signed determinant is affine in that point, so its absolute value is convex and attains its maximum at a polytope vertex. Replace the fourth point accordingly without decreasing volume, and repeat for the other three points. Thus a maximum-volume tetrahedron exists among four distinct vertices of \(K_c\), and its volume is one sixth of the largest absolute four-point determinant. This does not assert that all maximizing tetrahedra are vertex-supported.

**2. Exhaustive symbolic candidate families.** On \(1<c<2\), set \(u=c-1\), so \(0<u<1\), and generate all signed coordinate permutations of \((1,u,0)\). On \(2<c<3\), set \(v=c-2\), and generate all signed permutations of \((1,1,v)\). In each open interval there are exactly \(24\) vertices and \(\binom{24}{4}=10626\) unordered four-vertex candidates. Express the determinant of each candidate as an integer polynomial of degree at most three in the appropriate parameter. Up to global sign there are exactly \(54\) nonzero polynomial forms in the first family and \(48\) in the second. The numbers of nonzero-determinant polynomials counted with candidate multiplicity are \(9924\) and \(9846\). The complete reconstruction and finite exact proof certificate are in `verify.py`.

The three proposed upper-bound polynomials are
\[
 A(u)=2+2u+4u^2,\quad B(u)=8u,\quad C(v)=8+8v^2.
\]
For **every** enumerated signed determinant polynomial \(p\), both differences between the applicable bound and the signed choices \(p\) and \(-p\) have nonnegative cubic Bernstein coefficients on the intervals
\[
 (u,\text{bound},\text{interval})=(u,A,[0,1/2]),\ (u,B,[1/2,1]),\ (v,C,[0,1]).
\]
For clarity, if \(q\) has degree at most three, its Bernstein representation on \([a,b]\) is
\[
 q(a+(b-a)t)=\sum_{j=0}^3 \beta_j\binom3j t^j(1-t)^{3-j},\qquad 0\le t\le1.
\]
Writing \(q(a+(b-a)t)=\sum_{k=0}^3d_kt^k\), the exact coefficients are \(\beta_j=\sum_{k=0}^j d_k\binom jk/\binom3k\). All four Bernstein basis functions are nonnegative on \([0,1]\); hence the computed coefficient-sign certificates prove the upper bounds **for every real parameter in each entire interval**, not just at sampled parameters.

**3. Sharpness and winner counts.** The following explicit four-vertex witnesses have signed determinants equal in absolute value to the three bounds:
\[
\begin{array}{c|l}
 A(u)&(-1,-u,0),\ (-u,1,0),\ (u,0,-1),\ (u,0,1)\\
 B(u)&(-1,-u,0),\ (0,u,-1),\ (0,u,1),\ (1,-u,0)\\
 C(v)&(-1,-1,-v),\ (-1,1,v),\ (1,-v,1),\ (1,v,-1)
\end{array}
\]
where only the relevant parameter interval is used. Exact determinant expansion gives \(-A(u)\), \(B(u)\), and \(C(v)\), respectively. Exhaustive polynomial equality comparisons show that only the corresponding winning form occurs in each *open* chamber, with multiplicities \(24,6,12\). At \(u=1/2\), the first two forms tie and give \(30\) distinct vertex quadruples. At \(c=1,2,3\), duplicate vertex descriptions are collapsed before recomputing the counts, giving \(12,6,2\). This establishes the sharp piecewise maximum and the stated exact **vertex-supported** multiplicities.

**4. Sharp occupancy fraction.** Inclusion–exclusion gives the displayed exact polytope volume. Substitution of \(M(c)\), followed by elementary factorization, yields
\[
 M(c)-\frac{\operatorname{vol}_3(K_c)}6=\begin{cases}
 \frac{c(2c-3)^2}{9},&1\le c\le3/2,\\
 \frac{2(2c-3)(c^2-3c+3)}9,&3/2\le c\le2,\\
 \frac{2(1-3w+9w^2-w^3)}9,\quad w=c-2,&2\le c\le3.
 \end{cases}
\]
The first expression vanishes only at \(c=3/2\). The second is strictly positive for \(c>3/2\) because \(c^2-3c+3>0\). In the last expression, \(0\le w\le1\) implies \(w^3\le w^2\), so the bracket is at least \(1-3w+8w^2>0\) (negative discriminant). Thus equality occurs exactly at \(c=3/2\). This completes both assertions.

## Verification
Run `python3 verify.py` using only the Python standard library. The checker independently expands each candidate's determinant by two different formulas, one cubic-polynomial \(3\times3\) determinant and one exact rational \(4\times4\) Leibniz determinant at two rational parameter values. It tests every signed polynomial gap through its four **exact rational** Bernstein coefficients, verifies all maximizing vertex counts at rational interior points, and separately recomputes the geometric endpoint counts. It additionally checks the nonnegative occupancy-gap factorizations by exact Bernstein certificates. No floating-point tolerance or parameter sampling is used to infer the universal inequalities.

A successful run reports `VERIFY_OK` with \(54,48\) determinant-polynomial classes, \(9924,9846\) nonzero quadruple candidates and the three open-chamber winner counts \(24,6,12\). The proof of parameter-uniformity is the exact Bernstein-positivity test combined with exhaustive finite vertex enumeration.

## Relationship to prior work
Di Summa, Eisenbrand, Faenza and Moldenhauer introduced the maximum-volume simplex (MVS) formulation and developed general approximation and hardness bounds; their work does not give this closed formula for a cube intersected with a scaled octahedron. Akopyan and Glazyrin derive structural facts for maximal simplices, primarily in prisms and parallelotopes; these do not determine the current intersection family.

Deza, Hiriart-Urruty and Pournin explicitly describe this same polytope family as the polar norm balls \(\rho^*_{3,c}\), including its face geometry and **full-body** volume. Their Section 4 formula supplies a consistency check for \(\operatorname{vol}_3(K_c)\), but they do not calculate the volume of a largest **contained tetrahedron** or its phase transitions. Two related published exact records concern ordinary illumination numbers of the same family and graph distances in integer-parameter signed Johnson polytopes; neither invariant implies the present determinant envelope or the sharp occupancy ratio.

## Limitations
This result applies only to three dimensions and the exact concentric cube–octahedron intersection family. It classifies *vertex-supported* maximizing tetrahedra, not every possibly nonvertex equality tetrahedron. Its optimal ratio is a within-family statement, not a universal approximation theorem for all centrally symmetric convex bodies. The symbolic checker proves the asserted continuum inequalities by finite exact polynomial certificates but has not been independently audited. No claim of absolute bibliographic priority is made: related classical convex-polytope literature may contain an equivalent result under another formulation.

## References
1. M. Di Summa, F. Eisenbrand, Y. Faenza and C. Moldenhauer, *On largest volume simplices and sub-determinants*, arXiv:1406.3512, first posted 2014-06-13.
2. A. V. Akopyan and A. A. Glazyrin, *On maximum volume simplices in polytopes*, Periodica Mathematica Hungarica 69 (2014), 251–256, DOI:10.1007/s10998-014-0051-2; author-hosted full text.
3. A. Deza, J.-B. Hiriart-Urruty and L. Pournin, *Polytopal balls arising in optimization*, arXiv:2011.05607, first posted 2020-11-11; Contributions to Discrete Mathematics 16(3) (2021), 125–138.
4. *Exact illumination phase profile of the cube–octahedron intersection family*, publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-illumination-phase-profile-of-the-cube-octahedron-intersec--20022a556c31 .
5. *Exact shortest-path metric of the cube–cross-polytope intersection balls*, publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-shortest-path-metric-of-the-cube-cross-polytope-intersecti--55d5baa0a495 .
