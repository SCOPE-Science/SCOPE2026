# Sharp brightness extrema and exact orientation moments of the regular rhombic triacontahedron

## Finding
Let \(\varphi=(1+\sqrt5)/2\), and let the six vectors \(v_1,\ldots,v_6\) be the ordered list
\[
(0,1,\varphi),\quad (0,-1,\varphi),\quad
(1,\varphi,0),\quad (-1,\varphi,0),\quad
(\varphi,0,1),\quad (\varphi,0,-1).
\]
Define the centrally symmetric zonotope
\[
Z=\sum_{i=1}^6[-v_i/2,v_i/2]\subset\mathbb R^3.
\]
It is a regular rhombic triacontahedron; its 30 faces are congruent golden rhombi, and the present edge length is \(\sqrt{2+\varphi}\). For each unit vector \(u\in S^2\), let \(B(u)\) be the Euclidean area of the orthogonal projection of \(Z\) onto \(u^\perp\).

**Sharp endpoints with complete equality:**
\[
\boxed{\sqrt{250+110\sqrt5}\ \le B(u)\le\sqrt{306+134\sqrt5}.}
\]
The lower equality occurs precisely at the 12 directions \(u=\pm v_i/\sqrt{2+\varphi}\), for \(1\le i\le6\). The upper equality occurs at precisely 120 directed unit vectors. They admit the following finite, unambiguous description: order the 15 vectors \(w_{ij}=v_i\times v_j\) lexicographically by \((i,j)\), with \(1\le i<j\le6\). For every \(\varepsilon\in\{-1,1\}^{15}\), set \(s_{\varepsilon}=\sum_{i<j}\varepsilon_{ij}w_{ij}\). Exactly 120 signs satisfy
\[
\|s_{\varepsilon}\|^2=306+134\sqrt5,
\]
and the full upper equality set is the collection of their 120 distinct normalized vectors \(s_{\varepsilon}/\|s_{\varepsilon}\|\). One such unnormalized vector is \((2+4\varphi,-4-8\varphi,6+6\varphi)\). The sharp maximum/minimum ratio is \(\sqrt{7/5-2\sqrt5/25}\).

For a uniformly distributed \(U\in S^2\), the exact first two moments are
\[
\boxed{\mathbb E B(U)=15\varphi},
\]
\[
\boxed{\mathbb E B(U)^2
=\varphi^2\left(\frac{76}{3}+32\varphi\right)
+\frac{160\varphi^2}{\pi}\left(\sin\frac\pi5+\sin\frac{2\pi}5+\frac{\sqrt3+1}{2}\right).}
\]
Consequently \(\operatorname{Var}(B(U))\approx0.141612642020\) in this normalization.

## Assumptions and scope
All areas use the fixed Euclidean coordinates above, not unit edge length. The viewing normal is any directed unit vector, including all special directions, and uniform viewing means normalized rotation-invariant area measure on the sphere. Opposite unit normals give the same projected polygon but are counted as two directions. The result concerns ordinary orthographic planar projection, not central hyperplane sections or perspective images. The field \(\mathbb Z[\varphi]\) uses \(\varphi^2=\varphi+1\).

## Proof
**Zonotope normalization and area identity.** Every generator has squared length \(2+\varphi\). For distinct generators, their dot product is \(\pm\varphi\), so each pair determines a golden rhombus with equal edge lengths and acute cosine \(1/\sqrt5\). Every determinant of three distinct generators is nonzero. Thus the three-dimensional zonotope has two exposed rhombic facets for each of the 15 generator pairs, hence 30 congruent golden rhombi. Its edge directions are exactly the six generators, the classical six-zone construction. Orthogonal projection commutes with Minkowski addition. The area of a planar zonotope is the sum of the absolute determinants of its generator pairs; hence, for every unit \(u\),
\[
B(u)=\sum_{1\le i<j\le6}|(v_i\times v_j)\cdot u|=\sum_{k=1}^{15}|w_k\cdot u|. \tag{1}
\]
All \(\|w_k\|=2\varphi\).

**Global maximum and equality.** The identity \(\sum_k|w_k\cdot u|=\max_{\varepsilon\in\{\pm1\}^{15}}u\cdot s_{\varepsilon}\), combined with maximization over \(\|u\|=1\), gives the exact dual identity
\[
\max_{\|u\|=1}B(u)=\max_{\varepsilon\in\{\pm1\}^{15}}\|s_{\varepsilon}\|.
\]
Exhaustive exact arithmetic in \(\mathbb Z[\varphi]\) over all \(2^{15}=32768\) signed sums gives maximum squared norm \(172+268\varphi=306+134\sqrt5\). Exactly 120 sign vectors attain this value. For every one of them, all 15 scalar products \(w_k\cdot s_{\varepsilon}\) have strictly the prescribed signs. Their normalized sums are pairwise distinct by exact cross-product tests. Conversely every maximizer of \(B\) must arise in this finite equality set. This establishes the bound and every maximizing direction.

**Global minimum and equality.** The 15 great circles \(w_k\cdot u=0\) subdivide the unit sphere into compact spherical polygons. In any open cell of this arrangement, (1) is a positive linear functional \(L\cdot u\). Its only possible interior stationary minimum would be \(-L/\|L\|\), where the value would be negative, contradicting the strict positivity of (1). Equivalently the only positive stationary value is a strict spherical maximum. The same argument applied to arcs on each boundary great circle shows that a global minimum must occur where at least two independent great-circle boundaries meet. All 105 pairs have independent normals. For each pair \((k,\ell)\), take \(q_{k\ell}=w_k\times w_\ell\) and calculate
\[
\frac{\left(\sum_j|w_j\cdot q_{k\ell}|\right)^2}{\|q_{k\ell}\|^2}.
\]
Exact comparison of all 105 field-valued expressions gives minimum squared area \(250+110\sqrt5\), attained by 60 of the 105 pairs. Those 60 pairs generate exactly 12 distinct directed rays, each collinear with exactly one of the \(\pm v_i\). A representative minimizing ray is \(q=(0,2\varphi,2\varphi^2)\), with \(\sum_j|w_j\cdot q|=40+60\varphi\) and \(\|q\|^2=12+16\varphi\). Thus its squared area is precisely \((40+60\varphi)^2/(12+16\varphi)=250+110\sqrt5\).

**Mean and second moment.** For uniform \(U\) on \(S^2\), \(\mathbb E|a\cdot U|=\|a\|/2\). Applying this to the 15 equal-length normals in (1) yields \(15\varphi\). For arbitrary nonzero \(a,b\) and acute angle \(\theta\) between their unoriented lines, Gaussian polar decomposition gives the standard spherical identity
\[
\mathbb E\bigl[|a\cdot U|\,|b\cdot U|\bigr]
=\frac{2\|a\|\|b\|}{3\pi}
\left(\sin\theta+\left(\frac\pi2-\theta\right)\cos\theta\right). \tag{2}
\]
For the 105 unordered distinct pairs of \(w_k\), the absolute angular cosine has four exact classes: \(\varphi/2\) in 30 pairs, \((\varphi-1)/2\) in 30 pairs, \(1/2\) in 30 pairs, and \(0\) in 15 pairs. Their acute angles are respectively \(\pi/5\), \(2\pi/5\), \(\pi/3\), \(\pi/2\). The 15 diagonal terms contribute \(20\varphi^2\). Inserting the four classes into twice (2), simplifying the linear-in-angle contributions, and collecting the sine terms gives the displayed second moment. Subtracting \((15\varphi)^2\) gives the variance.

## Verification
The companion standalone script `verify_triac.py` uses integer pairs \((a,b)\) for \(a+b\varphi\) and exact sign tests via the irrationality of \(\sqrt5\). Its decisive computations are exhaustive: 32,768 signed sums for the upper extremum; 105 independent boundary intersections for the lower extremum; exact deduplication of the 120 upper and 12 lower equality directions; exact counts \(30+30+30+15\) for pair angles. It also checks 2,000 randomly selected inequalities and directly reconstructs 100 planar projected convex hulls from all 64 signed generator sums. The random tests are independent consistency checks, not substitutes for the exhaustive algebraic enumeration and the spherical arrangement proof. Run `python verify_triac.py` with Python, NumPy and SciPy installed.

## Relationship to prior work
The six-zone construction is classical: Hart describes the rhombic triacontahedron as the zonohedron generated by the six icosahedral axes. Koca, Koca and Koc construct it as a projection of a six-dimensional cube (arXiv:1403.2847, Sections 3 and the discussion of Figure 8). Zefiro and Ardigò describe its icosahedral axes, golden rhombus faces and duality. Fukuda develops general zonotope generators and hyperplane-arrangement enumeration. MathWorld tabulates its metric geometry, surface area and volume. The present contribution is the exact extrema and the complete extremal direction sets for its **two-dimensional orthographic projected area**, together with its exact first two orientation moments; these are not statements of the inspected prior material. The projection-body area identity, the spherical absolute-product identity and Cauchy's mean projection formula are standard tools, not claimed as new.

## Limitations
The theorem describes one Euclidean similarity class in one explicit scale. It gives the first two moments but not the full brightness distribution or correlations with the shadow perimeter or vertex count. The exact finite enumeration is reproducible but no independent formal or human validation has been performed. Literature comparison is based on the inspected accessible sources and may miss older equivalent statements in historical polytope tables or books; historical priority is not certified.

## References
1. M. Koca, N. Özdeş Koca and R. Koç, *Group Theoretical Analysis of Quasicrystallography from Projections of Higher Dimensional Lattices Bn*, arXiv:1403.2847, posted 12 March 2014. https://arxiv.org/abs/1403.2847 ; full text https://arxiv.org/pdf/1403.2847 .
2. George W. Hart, *Zonohedra*, https://www.georgehart.com/virtual-polyhedra/zonohedra-info.html .
3. L. Zefiro and M. R. Ardigò, *Description of the Forms Belonging to the 235 and m3 5 Icosahedral Point Groups*, https://www.mi.sanu.ac.rs/vismath/zefiro1/_icosahedral_polyhedra_2007_11_15.htm .
4. Komei Fukuda, *Zonotopes*, https://www.cs.mcgill.ca/~fukuda/760B/handouts/expoly3.pdf .
5. Eric W. Weisstein, *Rhombic Triacontahedron*, MathWorld, https://mathworld.wolfram.com/RhombicTriacontahedron.html .
