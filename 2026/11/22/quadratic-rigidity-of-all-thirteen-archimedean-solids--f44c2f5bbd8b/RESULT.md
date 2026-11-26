# Quadratic rigidity of octahedral rotation orbits and of the Archimedean solids

## Finding

Let \(O\) be the proper octahedral rotation group, acting by determinant-\(+1\) signed coordinate permutations. For a nonzero vector \(v=(a,b,c)\), the only real degree-at-most-two polynomials vanishing on \(Ov\) are multiples of \(\|x\|^2-\|v\|^2\) **if and only if** at least two of \(a,b,c\) are nonzero and \(|a|,|b|,|c|\) are not all equal. The only exceptional orbits, up to scale, are the coordinate-axis octahedron and the cube.

This criterion, combined with the known quadratic unisolvence of icosahedral orbits and the truncated-tetrahedron case, gives a proof of Berestovskiĭ and Nikonorov’s Conjecture 1: every one of the thirteen classical Archimedean solids is perfect. Here perfect means that the span of the circumsphere equation is the whole kernel of degree-at-most-two evaluation at the vertices. We do not claim the icosahedral orbit theorem, or the previously treated cuboctahedron and truncated tetrahedron cases, as new.

## Assumptions and scope

Polynomials are real and may have constant and linear terms. All orbits consist of distinct points on the sphere centered at the origin of radius \(R=\|v\|>0\). The polynomial restrictions to that sphere are the direct sum \(\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\) of real homogeneous harmonic degrees 0, 1, and 2, of dimensions 1, 3, and 5. The only relation from restricting a polynomial of degree at most two to the entire sphere is the sphere equation: the quadratic part splits into its trace and trace-free parts, and on the sphere the trace part is constant. Thus perfectness is equivalent to rank nine. Translation to the circumcenter and uniform scaling do not affect the rank.

The classical thirteen exclude prisms, antiprisms and the pseudorhombicuboctahedron. The proof uses the usual vertex transitivity under the proper octahedral or icosahedral rotation group for the listed solids, including the snubs; the truncated tetrahedron is treated separately.

## Proof

**Evaluation on an orbit.** Suppose a group of orthogonal transformations acts on a space of polynomials that is a direct sum of pairwise nonisomorphic real irreducibles. The kernel of evaluation on a group orbit is invariant. Complete reducibility and Schur’s lemma imply that it is the sum of precisely those summands killed by evaluation. In fact any irreducible submodule of the kernel has nonzero projection to some summand, which must be isomorphic to it; all other projections are zero. A summand is killed by orbit evaluation exactly when all its functions vanish at the generating point, because the summand is invariant.

**Proper octahedral orbits.** In addition to the constants and \(\mathcal H_1=\langle x,y,z\rangle\), the invariant blocks are
\[
E=\langle x^2-y^2,x^2+y^2-2z^2\rangle,\qquad T=\langle xy,yz,zx\rangle,
\qquad \mathcal H_2=E\oplus T.
\]
The five proper octahedral classes (identity, coordinate-axis quarter-turn, coordinate-axis half-turn, body-diagonal third-turn, edge-axis half-turn) have sizes \(1,6,3,8,6\). From the signed permutations their three nonconstant block characters are respectively
\[
\begin{aligned}
\chi_{\mathcal H_1}&=(3,1,-1,0,-1),\\
\chi_E&=(2,0,2,-1,0),\\
\chi_T&=(3,-1,-1,0,1).
\end{aligned}
\]
The class-weighted inner products divided by 24 give the identity matrix and each character has mean zero. Hence the blocks, including the constants, are irreducible and pairwise inequivalent. Constants and linears evaluate nontrivially at every \(v\ne0\). Evaluation at \(v\) kills all of \(E\) exactly when \(a^2=b^2=c^2\), and kills all of \(T\) exactly when \(ab=bc=ca=0\). These give the eight-point cube and the six-point coordinate-axis octahedron, respectively. All other nonzero orbits have rank nine by the orbit evaluation argument.

**Icosahedral input.** Every orbit of the proper icosahedral rotation group on \(S^2\) is a spherical 5-design. In particular, the orbit average of the square of a quadratic restriction equals its sphere average. If the restriction vanishes on the orbit, the square has zero integral and therefore the restriction vanishes identically on the sphere. One direct prior route to the 5-design fact is Mohammadpour–Waldron, Example 7.4: all the binary icosahedral orbits have projective design indices \((p,p)\) for \(0\le p\le5\). Under the Hopf projection to \(S^2\), given for a unit \(z\in\mathbb C^2\) by \((2\operatorname{Re}(z_1\bar z_2),2\operatorname{Im}(z_1\bar z_2),|z_1|^2-|z_2|^2)\), these indices give exact integration for real polynomials of degree at most five: a polynomial of degree \(k\) pulls back to a sum of equal-bidegree terms through \((k,k)\), and harmonic decomposition preserves that degree range. Haar surface measure projects to uniform surface measure; the equivariant orbit map has equal-sized fibers and the binary group projects to the proper rotation group.

For a self-contained check of the quadratic conclusion, the classes of the proper icosahedral group have sizes \(1,15,20,12,12\) and angles \(0,\pi,2\pi/3,2\pi/5,4\pi/5\). The character on \(\mathcal H_j\) at angle \(\theta\) is \(1+2\sum_{k=1}^j\cos(k\theta)\). For \(\varphi=(1+\sqrt5)/2\) the characters for \(j=1,2\) are \((3,-1,0,\varphi,1-\varphi)\) and \((5,1,-1,0,0)\), of norm one, mutually orthogonal and of zero average. Each harmonic degree evaluates nontrivially at every \(v\ne0\); for degree two one can use \((v\cdot x)^2-\|v\|^2\|x\|^2/3\). The same kernel argument proves rank nine. This also follows by combining the irreducibility calculation with the spherical-design criterion of de la Harpe and Pache, Theorem 1(ii) with \(s=2\).

**Truncated tetrahedron.** For completeness its vertices can be scaled to all placements of the unsigned coordinates \((3,1,1)\) with sign product \(+1\). They are obtained by trisecting the edges between the four vertices with unsigned coordinates \((3,3,3)\) and sign product \(+1\). Every truncated vertex has squared radius 11. Write a vanishing polynomial as
\[
C+\sum_i A_i x_i^2+\sum_i B_i x_i+\sum_{i<j}D_{ij}x_ix_j.
\]
For each placement \(u=(u_1,u_2,u_3)\) of \((3,1,1)\), the four sign characters \(1,\epsilon_1,\epsilon_2,\epsilon_3\) are independent on the even sign patterns. The constant coefficient gives \(C+\sum_i A_i u_i^2=0\), so comparing placements yields \(A_1=A_2=A_3=A\) and \(C=-11A\). For each \(i\) the \(\epsilon_i\) coefficient gives \(u_i B_i+u_j u_k D_{jk}=0\) with \(\{i,j,k\}=\{1,2,3\}\). The two possibilities give \(3B_i+D_{jk}=B_i+3D_{jk}=0\), so both coefficients vanish. Only the sphere equation remains.

**All thirteen solids.** The cuboctahedron, truncated cube, truncated octahedron, rhombicuboctahedron, truncated cuboctahedron, and snub cube are octahedral rotation orbits with at least twelve vertices, so neither exceptional orbit occurs. The icosidodecahedron, truncated dodecahedron, truncated icosahedron, rhombicosidodecahedron, truncated icosidodecahedron, and snub dodecahedron are covered by the icosahedral input. Together with the truncated tetrahedron this proves the conjecture for the thirteen classical solids.

## Verification

Run `python3 verify_archimedean.py` with SymPy installed. The supplied checker tests the truncated tetrahedron’s rank and kernel, the octahedral and icosahedral character inner products, rank on representative octahedral orbits including the two exceptions, and rank on the regular icosahedron over \(\mathbb Q(\sqrt5)\). The expected success marker is `ARCHIMEDEAN_QUADRATIC_UNIQUENESS_CHECKS_PASS`. These exact finite checks supplement the proof; checking representative orbits cannot establish a universal orbit criterion. The proof uses the vertex-transitivity classification of the classical solids as input.

## Relationship to prior work and limitations

Berestovskiĭ and Nikonorov formulate the perfectness conjecture explicitly. Icosahedral unisolvence is already implied by the stronger design theorem above. Prior explicit quadratic-harmonic sampling results cover the cuboctahedron and truncated tetrahedron. The contribution here is the exact exceptional-orbit classification for the proper octahedral group and its use to complete a proof for all thirteen classical Archimedean solids, not a first proof for each constituent solid. That classification includes orbits that are not spherical 4-designs: rank concerns injectivity, not exact quadrature through degree four. This statement deals only with real quadratics and these proper rotation groups, not higher-degree interpolation, other finite rotation groups, or a priority claim over all possible treatments.

## References

1. V. N. Berestovskiĭ and Yu. G. Nikonorov, *Perfect and almost perfect homogeneous polytopes*, [arXiv:2304.12211v1](https://arxiv.org/abs/2304.12211v1), Definition 2 and Conjecture 1.
2. M. Mohammadpour and S. Waldron, *Complex spherical designs from group orbits*, [arXiv:2308.02499v3](https://arxiv.org/abs/2308.02499v3), §4 and Example 7.4.
3. P. de la Harpe and C. Pache, *Spherical designs and finite group representations (some results of E. Bannai)*, European Journal of Combinatorics **25** (2004), 213–227, [DOI:10.1016/S0195-6698(03)00101-X](https://doi.org/10.1016/S0195-6698(03)00101-X), Theorem 1(ii).
4. *The tetrahedral graphic matroid controls quadratic-harmonic sampling on the cuboctahedron*, [research record](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-the-tetrahedral-graphic-matroid-controls-quadratic-harmonic-samp--22932f55648e), full-rank case of the erasure formula.
5. *Eight optimal nine-point quadratic-harmonic samplers on the truncated tetrahedron*, [research record](https://github.com/Resultary/2026/tree/main/2026/11/16/SCOPE-eight-optimal-nine-point-quadratic-harmonic-samplers-on-the-trun--e5399224a33a), full-vertex interpolation and nine-point sampling.
