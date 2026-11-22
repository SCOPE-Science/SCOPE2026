# Eight singularities and a Milnor census for a normal Jacobian decic

## Finding
Let \(C\) be the smooth genus-two curve \(y^2=x^5+1\) over \(\mathbb C\), and let \(A=\operatorname{Jac}(C)\). Use the five smooth \((1,1)\)-branch curves on \(\mathbb P^1\times\mathbb P^1\) constructed by Chen–Lazarsfeld–Moretti (Theorem 2.2). Choose a general projection center outside this branch divisor to obtain a reduced union \(B=V(F_{10})\) of five plane conics, and a general line \(Q=0\) avoiding all singular points of \(B\) and meeting its smooth locus transversely. Define
\[
S=V\bigl(W^5Q(X,Y,Z)^5-F_{10}(X,Y,Z)\bigr)\subset\mathbb P^3_{\mathbb C}.
\]
This is the normal degree-ten model of \(A\) supplied by their cyclic-cover construction. Its **entire reduced singular locus** consists of exactly eight points, with the following local geometry and Milnor numbers:

| Location | Number | Proven local description | Milnor number per point |
|---|---:|---|---:|
| \(W=0\), images of triple branch contacts | 5 | Analytically \(z^5=u(v^2-u^4)\) | 24 |
| \(W=0\), contracted ruling images | 2 | Multiplicity-five hypersurface germ with smooth plane-quintic tangent cone | 64 |
| \([W:X:Y:Z]=[1:0:0:0]\) | 1 | Semi-quasihomogeneous of weights \((1,1,2)\), degree \(10\), with isolated principal part \(z^5-f_{10}(u,v)\) for a square-free binary decic \(f_{10}\) | 324 |

Hence the **total Milnor number is**
\[
\sum_{p\in\operatorname{Sing}(S)}\mu_p=5\cdot24+2\cdot64+324=572.
\]

## Assumptions and scope
The ground field is \(\mathbb C\). The five original branch components and their incidence configuration are those of Chen–Lazarsfeld–Moretti, not arbitrary five \((1,1)\)-curves. The projection center on \(\mathbb P^1\times\mathbb P^1\) is chosen generally: it lies off the branch divisor, neither contracted ruling contains a branch singularity, and its intersection points with the five components are pairwise distinct on each ruling. The chosen line \(Q=0\) in the target plane avoids the seven branch singular points and has ten distinct transverse intersections with the reduced degree-ten divisor. Such choices exist by avoidance of finitely many proper closed conditions. The theorem addresses this general family of projective models, not every special projection or every special choice of \(Q\). The Milnor number is the complex dimension of the local Jacobian algebra at each isolated hypersurface singularity.

## Proof
**1. The five branch contacts on the quadric.** In §2.4–2.6 of Chen–Lazarsfeld–Moretti, the resolution of the cyclic quotient contains curves \(E_i,F_i,\Gamma_i\), with indices modulo five. First contracting the five disjoint \(\Gamma_i\) produces a surface on which each \((-1)\)-curve \(F_i\) meets \(E_{i-1}\) and \(E_{i+1}\) at one common point, while it meets \(E_i\) at a distinct point. The two curves \(E_{i-1}\) and \(E_{i+1}\) meet transversely at that common point. These statements follow directly from the three distinct intersections of \(\Gamma_i\) with \(E_{i-1},E_{i+1},F_i\) on the previous surface and the distinct original intersection \(E_i\cap F_i\). Blowing down \(F_i\) sends these three curves to three smooth branches through one point: the first two become tangent with intersection multiplicity two and the third is transverse to both. The five contracted \(F_i\) are disjoint, so their images give five distinct points of this type on the quadric \(\mathbb P^1\times\mathbb P^1\).

There are no further intersections of the branch components. Indeed each component is a rational \((1,1)\)-curve, so the reduced union has bidegree \((5,5)\) and arithmetic genus \((5-1)(5-1)=16\). Each of the five three-branch contacts has local \(\delta\)-invariant \(2+1+1=4\). The normalization genus formula gives \(16=\sum_p\delta_p-5+1\), and the five exhibited points already contribute \(20\) to the delta sum. Alternatively, their total pairwise intersection multiplicity is \(5\cdot4=20\), exactly \(\binom52\cdot2\).

**2. Plane conics and two additional ordinary multiple points.** The birational map from the quadric to \(\mathbb P^2\), obtained by blowing up the general center and contracting the proper transforms of its two rulings, sends each \((1,1)\)-curve to a smooth plane conic. Each of the two contracted rulings meets each of the five curves once, at distinct smooth points. Its image is consequently an ordinary fivefold point of the union of conics. Away from these rulings the map is an isomorphism, so it preserves the five triple-contact singularities. Thus \(B=V(F_{10})\) has exactly seven singular points: five three-branch points with one contact-two pair, and two ordinary fivefold points. As a check, their total delta invariant is \(5\cdot4+2\binom52=40\), and \(40-5+1=36=(10-1)(10-2)/2\), the arithmetic genus of a plane decic.

**3. No other singular points of the decic surface.** Set \(\Phi=W^5Q^5-F_{10}\). The projective derivative \(\partial_W\Phi=5W^4Q^5\) implies that every singular point lies on \(W=0\) or \(Q=0\). On \(W=0\), the other derivatives reduce to \(-\nabla F_{10}\), so the singularities there correspond precisely to the seven singular points of \(B\). On \(Q=0\) with \((X,Y,Z)\ne(0,0,0)\), the same reduction and the assumption that \(Q\) avoids \(\operatorname{Sing}(B)\) imply smoothness. The remaining point \([1:0:0:0]\) is singular because the local defining equation has multiplicity five. Therefore the eight listed points exhaust the singular support. This also proves normality by the hypersurface \(S_2\) condition and regularity in codimension one.

**4. Five triple-contact Milnor numbers.** At such a branch point, let \(u=0\) be the transverse branch and write the two tangent branches as \(v=a(u)\) and \(v=b(u)\), with \(\operatorname{ord}_u(a-b)=2\). Centering \(v\) on \((a+b)/2\) and rescaling \(u\) by a convergent unit gives the exact reduced branch germ \(u(v^2-u^4)=0\), up to multiplication by a unit. Since \(Q\) is a unit there and every holomorphic unit has a fifth root, the covering germ is analytically equivalent to \(z^5=u(v^2-u^4)\). Its Jacobian algebra is
\[
\mathbb C\{u,v,z\}/(z^4,uv,v^2-5u^4).
\]
The quotient in \(u,v\) has basis \(1,u,u^2,u^3,u^4,v\), so its length is six, and the full Jacobian length is \(4\cdot6=24\).

**5. Two ordinary fivefold Milnor numbers.** At either of the two ordinary fivefold points of \(B\), the lowest homogeneous term of the cyclic covering equation is \(z^5-\prod_{i=1}^5\ell_i(u,v)\), where the five pairwise nonproportional linear forms \(\ell_i\) describe the branch tangent directions. The associated plane quintic is nonsingular: away from \(z=0\) its derivative in \(z\) is nonzero, and on \(z=0\) the binary product has simple roots. Thus the homogeneous principal part is isolated. The standard semi-quasihomogeneous Jacobian-length theorem gives the exact Milnor number \((5-1)^3=64\), regardless of the higher-order conic terms.

**6. Vertex Milnor number.** In the affine chart \(W=1\), choose linear coordinates \(u,v,z\) with \(z=Q\). Assign weights \(\operatorname{wt}(u)=\operatorname{wt}(v)=1\), \(\operatorname{wt}(z)=2\). The weight-ten principal part of \(z^5-F_{10}(u,v,z)\) is \(z^5-f_{10}(u,v)\), with \(f_{10}(u,v)=F_{10}(u,v,0)\). Because \(Q=0\) meets the branch divisor in ten distinct smooth points, \(f_{10}\) is a square-free binary form of degree ten. Hence the weighted principal part is isolated, and all omitted terms have strictly greater weight. The weighted-homogeneous Jacobian-length formula (preserved under this semi-quasihomogeneous perturbation) yields
\[
\mu_{\mathrm{vertex}}=(10/1-1)^2(10/2-1)=9^2\cdot4=324.
\]
These three calculations prove the asserted singularity count and total Milnor number.

**7. Independent Euler check.** Topologically the union of the five conics has Euler characteristic \(5\cdot2-5\cdot(3-1)-2\cdot(5-1)=-8\). A general line \(Q\) meets it in ten points. Projection \(S\setminus\{[1:0:0:0]\}\to\mathbb P^2\) has five-point fibers off \(B\cup Q\), one-point fibers on \(B\setminus Q\), empty fibers on \(Q\setminus B\), and affine-line fibers above \(B\cap Q\). Stratified Euler additivity therefore gives
\[
\chi(S)=5\,[3-(-8+2-10)]+(-8-10)+10+1=88.
\]
A smooth degree-ten hypersurface in \(\mathbb P^3\) has Euler characteristic \(10(10^2-4\cdot10+6)=660\). The isolated surface-singularity smoothing formula independently yields \(660-88=572\), agreeing with the local Jacobian calculation.

## Verification
Run the included `verify.py` using Python 3 and SymPy. It computes exact Groebner standard-monomial lengths of the three isolated principal/normal-form Jacobian algebras, checks the normalization genus equations, and independently checks the Euler characteristic. It prints: `PASS: Jacobian lengths 24/64/324; branch-genus and Euler identities; total 8 points and Milnor sum 572`. The checker does not infer genericity or prove the incidence resolution: those are established by the geometric argument and the cited primary source.

## Relationship to prior work
Chen–Lazarsfeld–Moretti, *Some normal abelian surfaces in* \(\mathbb P^3\) (arXiv:2611.09613v1), construct the genus-two Jacobian's five-component \((1,1)\) branch covering (Theorem 2.2), describe the necessary blowdowns (§2.4–2.6), and establish normal projective models (Proposition 1.6). Their results imply the birational model and supply incidence data; they do not state the eight-point singularity census or its Milnor-number basket. Artal Bartolo–Cogolludo-Agustín–Libgober previously constructed a cyclic covering whose smooth model is a genus-two Jacobian; their degree-ten covering has a different branch presentation and does not calculate the singularities of this normal decic embedding. The weighted Milnor calculation is classical; the contribution is its application to the complete, geometrically determined basket of the specific new projective model.

## Limitations
Only general choices of the projection center and of \(Q\) are addressed. Special projections can cause collisions or additional tangencies. The theorem gives the exact analytic type at the five triple contacts and the tangent-cone/weighted-principal-part characterizations at the other three points; it does **not** assert a unique analytic isomorphism type for arbitrary higher-order terms at the vertex or the two fivefold points. No complete resolution graph, Tjurina numbers, or deformation classification is claimed. Historical priority beyond the inspected literature and indexed record searches is not established; no independent mathematical audit has been performed.

## References
1. N. Chen, R. Lazarsfeld, F. Moretti, *Some normal abelian surfaces in* \(\mathbb P^3\), arXiv:2611.09613v1, submitted 2026-11-06. https://arxiv.org/html/2611.09613v1
2. E. Artal Bartolo, J. I. Cogolludo-Agustín, A. Libgober, *Albanese varieties of cyclic covers of the projective plane and orbifold pencils*, Nagoya Math. J. 227 (2017), 189–213, DOI 10.1017/nmj.2016.54. https://doi.org/10.1017/nmj.2016.54
3. M. Furuya, M. Tomari, *A characterization of semi-quasihomogeneous functions in terms of the Milnor number*, Proc. Amer. Math. Soc. 132 (2004), 1885–1890, DOI 10.1090/S0002-9939-04-07383-6. https://doi.org/10.1090/S0002-9939-04-07383-6
