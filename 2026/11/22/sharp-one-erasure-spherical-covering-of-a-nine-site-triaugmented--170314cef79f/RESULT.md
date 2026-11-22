# Sharp one-erasure spherical covering of a nine-site triaugmented prism

## Finding

A nine-point configuration on the unit two-sphere can be tested for *one-erasure covering robustness*: after an adversary removes any one point, how large must equal spherical caps centered at the eight survivors be to cover the entire sphere? For the complete symmetric triaugmented-triangular-prism family in its fixed simplicial combinatorial chamber, the answer is exact and undergoes a sharp change of worst deleted orbit.

For \(1/2<r<1\), set \(h=\sqrt{1-r^2}\) and let the nine unit sites \(V_r\) be the three equatorial vertices and six upper/lower vertices specified below. If \(\rho(S)=\max_{u\in\mathbb S^2}\min_{v\in S}\arccos(u\cdot v)\) and \(V_r\setminus\{v\}\) denotes a deletion, then, for any equatorial site \(a\) and any upper/lower prism site \(b\),
\[
\boxed{\begin{aligned}
\cos\rho(V_r\setminus\{a\})&=\min\{r/2,\sqrt{1-r^2}\},\\
\cos\rho(V_r\setminus\{b\})&=\sqrt{\frac{1-r}{5-3r}}.
\end{aligned}}
\]
In particular, the worst-erasure covering radius \(R(r)=\max_{v\in V_r}\rho(V_r\setminus\{v\})\) obeys
\[
\boxed{\cos R(r)=\begin{cases}
\dfrac r2,&1/2<r\le2/3,\\[2mm]
\sqrt{\dfrac{1-r}{5-3r}},&2/3\le r<1.
\end{cases}}
\]
The unique family-wide minimizer of \(R\) is \(r=2/3\), with \(R(2/3)=\arccos(1/3)\). For \(r<2/3\), deleting an equatorial site is worst; for \(r>2/3\), deleting a prism-ring site is worst; at the transition both types tie. The nine-vertex *volume*-maximizer has the distinct parameter \(r_*=\sqrt3-1>2/3\), so its worst erasure is a prism-ring vertex and its covering radius is strictly larger than \(\arccos(1/3)\).

## Assumptions and scope

Let \(u_j=(\cos(2\pi j/3),\sin(2\pi j/3))\) and \(w_j=(\cos((2j+1)\pi/3),\sin((2j+1)\pi/3))\) for \(j=0,1,2\). Define
\[
a_j=(u_j,0),\qquad x_j=(r w_j,h),\qquad y_j=(r w_j,-h),\qquad
V_r=\{a_0,a_1,a_2,x_0,x_1,x_2,y_0,y_1,y_2\}.
\]
All distances and facet normals are Euclidean in \(\mathbb R^3\); \(\arccos\) gives angular distance in radians on \(\mathbb S^2\). The restriction \(1/2<r<1\) is the complete open chamber in which the *intact* nine-vertex triaugmented prism has fourteen triangular facets. The statement does not optimize over all nine-point spherical configurations or all polyhedra. By threefold rotation and reflection across the equatorial plane, single deletions have exactly two symmetry types, represented by \(a_0\) and \(x_0\).

For reproducibility index the vertices in the order \(0=a_0,1=a_1,2=a_2,3=x_0,4=x_1,5=x_2,6=y_0,7=y_1,8=y_2\). For a finite spherical set \(S\) with the origin in the interior of its Euclidean convex hull \(Q\),
\[
\cos\rho(S)=\min_{u\in\mathbb S^2}\max_{v\in S}u\cdot v
=\min_{\text{facet }F\text{ of }Q}\operatorname{dist}(0,\operatorname{aff}F).
\]
The first equality uses monotonicity of cosine; the second uses the origin-centered inradius, since the minimum of the support function over unit normals is the smallest facet-plane distance.

## Proof

**1. The two eight-site facet lists.** For each deletion, we exhibit all its facets, together with squared distances from their planes to the origin. In the following table each parenthesized tuple denotes one triangular facet, except for the specified four-vertex quadrilaterals. The symbols \(A,B,C,D,E,F\) denote the positive rational functions of \(r\):
\[
\begin{aligned}
A&=\frac{1-r}{5-3r},&B&=\frac{1-r^2}{5-4r},&
C&=\frac{4(1-r^2)}{8-4r-3r^2},\\
D&=\frac{3r^2}{4(1-r+r^2)},&E&=1-r^2,&F&=\frac{r^2}{4}.
\end{aligned}
\]

For **deletion of \(a_0\)**, the full facet list, grouped by squared plane distance, is

| Squared distance | Facets, by vertex indices |
|---|---|
| \(F\) | quadrilateral \((3,5,6,8)\) |
| \(E\) | \((3,4,5)\), \((6,7,8)\) |
| \(C\) | \((1,3,4)\), \((1,6,7)\), \((2,4,5)\), \((2,7,8)\) |
| \(D\) | \((1,3,6)\), \((1,4,7)\), \((2,4,7)\), \((2,5,8)\) |

For **deletion of \(x_0\)** the full list is

| Squared distance | Facets, by vertex indices |
|---|---|
| \(A\) | quadrilateral \((0,1,4,5)\) |
| \(B\) | \((0,1,6)\) |
| \(C\) | \((0,6,8)\), \((1,6,7)\), \((2,4,5)\), \((2,7,8)\) |
| \(D\) | \((0,5,8)\), \((1,4,7)\), \((2,4,7)\), \((2,5,8)\) |
| \(E\) | \((6,7,8)\) |

Here is a direct exact check of each facet list. For three listed vertices \(p,q,s\), let \(n=(q-p)\times(s-p)\). For every other surviving vertex \(z\), the determinant \((z-p)\cdot n\) has constant nonzero sign throughout \(1/2<r<1\); the origin also lies strictly on that same side. Indeed, after removal of its common positive factor \(\sqrt3 h\), every determinant is a signed positive numerical multiple of one of
\[
1,\quad r,\quad r^2,\quad r+1,\quad 2r-1,\quad
2-r,\quad r(r+1),\quad r(2-r),\quad r(r+4).
\]
Direct substitution verifies coplanarity of the four vertices of each listed quadrilateral. Their squared plane distances, calculated as \(((p\cdot n)^2)/(n\cdot n)\), simplify to the table entries using \(h^2=1-r^2\). The bundled exact symbolic verifier checks **every** required determinant sign, origin interior-side test and squared-distance identity over the full open parameter interval.

Each erased hull has eight vertices and the exhibited list comprises eleven distinct facets, ten triangles and one quadrilateral. For a three-polytope with \(v=8\) vertices and at least one quadrilateral facet, Euler's identity and \(2e\ge3f+1\) imply \(f\le2v-5=11\). Therefore these eleven supporting facets are exhaustive. They also show that the origin is interior, so the spherical covering formula in the preceding section applies.

**2. The equatorial-erasure minimum.** Its candidate squared distances are \(C,D,E,F\). First \(D-F=r^2(2-r)(r+1)/(4(1-r+r^2))>0\). If \(1/2<r\le2/3\), direct rational simplification yields \(C\ge F\); if \(2/3\le r<1\), it yields \(C\ge E\). Consequently \(\min\{C,D,E,F\}=\min\{E,F\}\), giving the first displayed formula. The equal-contribution threshold inside this expression is \(r=2/\sqrt5\), but it does not control the *worst-erasure* switch.

**3. The prism-erasure minimum.** Its squared distances are \(A,B,C,D,E\). Elementary factorizations prove
\[
\begin{aligned}
B-A&=\frac{3r(2-r)(1-r)}{(5-3r)(5-4r)}>0,\\
C-A&=\frac{3(2-r)(1-r)(3r+2)}{(5-3r)(8-4r-3r^2)}>0,\\
D-A&=\frac{(2-r)(r+1)(5r-2)}{4(5-3r)(1-r+r^2)}>0,
\end{aligned}
\]
where the last uses \(r>1/2\). Also \(A<E\) on this interval (equivalently \((1+r)(5-3r)>1\)). Hence the smallest squared facet distance is exactly \(A\), proving the second formula.

**4. Sharp one-erasure optimum.** On \((1/2,2/3]\), \(F\le E\), and
\[
A-F=\frac{(2-r)(r+1)(2-3r)}{4(5-3r)}\ge0.
\]
Therefore the worst deletion is equatorial and \(\cos R(r)=r/2\). For \(2/3\le r<1\), \(A\le F\) from the same identity and \(A<E\) from step 3, so the worst deletion is a prism-ring vertex and \(\cos R(r)=\sqrt A\). The first branch increases strictly with \(r\), whereas
\[
\frac{dA}{dr}=-\frac{2}{(5-3r)^2}<0.
\]
They meet at \(r=2/3\), where both squared controlling distances are \(1/9\). This proves the unique global minimax parameter and sharp radius. Finally \(r_*=\sqrt3-1>2/3\) is the known, different nine-site volume-maximizer, so its worst-erasure radius is strictly larger.

## Verification

Run `python3 verify.py` with Python 3 and SymPy installed. It uses exact rational polynomial root counts and algebraic identities—no sampled-parameter assumption—to verify every facet supporting sign and origin containment throughout \(1/2<r<1\), the eleven-facet completeness certificate, every squared plane distance and every inequality used above. A successful run prints `VERIFY_OK`. Euler's identity and the support-function/inradius relation are proved in the text; the checker is a reproducible algebraic certificate, not a substitute for these geometric arguments.

## Relationship to prior work

Hoehner and Ledford, *The maximum volume polytope with nine vertices inscribed in the sphere* (arXiv:2608.04392v1, first public August 5, 2026), determine the global volume maximizing nine-vertex configuration and its parameter \(r_*=\sqrt3-1\). That theorem supplies motivation and coordinates but does not evaluate **any** eight-site covering radius after vertex loss. The related exact inball and John–Löwner ellipsoid analyses of the intact symmetric nine-vertex family (links below) compute different, intact-body quantities; neither their minimizing parameters nor their full-body facet-distance formulas imply the newly exposed quadrilateral facets and adversarial-deletion transition. Classical spherical-covering tables concern the best codes without a specified deletion from this nine-site family, and do not directly supply the two orbit-resolved formulas here.

## Limitations

The optimum is restricted to the symmetric one-parameter family with \(1/2<r<1\) and adversarial deletion of exactly one existing site. It does not establish a globally optimal one-erasure-tolerant nine-point spherical code. Independent literature may contain an equivalent erasure calculation not identified by the present search. No external mathematical audit is asserted.

## References

1. S. Hoehner and J. Ledford, *The maximum volume polytope with nine vertices inscribed in the sphere*, arXiv:2608.04392v1 (first public 2026-08-05), https://arxiv.org/abs/2608.04392. Primary manuscript inspected in its open-access revision.
2. *An eight-facet insphere transition in symmetric triaugmented triangular prisms*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-an-eight-facet-insphere-transition-in-symmetric-triaugmented-tri--b6fd090ad2f5.
3. *Exact John–Löwner ellipsoids and three distinct optima in a nine-vertex spherical prism family*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-john-l-wner-ellipsoids-and-three-distinct-optima-in-a-nine--66811e2b55c7.
4. R. H. Hardin, N. J. A. Sloane, and W. D. Smith, *Spherical Coverings*, https://neilsloane.com/coverings/index.html (general spherical-covering data; not an erasure theorem).
