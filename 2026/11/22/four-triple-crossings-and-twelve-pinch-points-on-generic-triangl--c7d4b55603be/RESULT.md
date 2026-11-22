# Four triple crossings and twelve pinch points on generic triangle Lissajous sextics

## Finding

Let \(c\in\mathbb C\setminus\{0,1,-1\}\) and choose \(\lambda\in\mathbb C^\times\) with \(\lambda+\lambda^{-1}=2c\). Set
\[
T_\lambda=\{(a,b,d)\in(\mathbb C^\times)^3:abd=\lambda\}\simeq(\mathbb C^\times)^2,
\qquad \nu(a,b,d)=\tfrac12(a+a^{-1},b+b^{-1},d+d^{-1}).
\]
The image \(S_c\subset\mathbb A^3_{\mathbb C}\) is an integral sextic, and \(\nu:T_\lambda\to S_c\) is its finite birational normalization. Writing the coordinates as \(x_1,x_2,x_3\), its **complete reduced singular locus** consists of six distinct affine lines
\[
\ell_{ij}^{\epsilon}=\{x_j=\epsilon x_i,\ x_k=\epsilon c\},
\quad 1\le i<j\le3,\quad\{i,j,k\}=\{1,2,3\},\quad\epsilon\in\{1,-1\}.
\]
The line arrangement has precisely four intersection points,
\[
P_s=(s_1c,s_2c,s_3c),\qquad s_i\in\{1,-1\},\quad s_1s_2s_3=1.
\]
Each is an ordinary three-sheet transverse crossing, lies on exactly three of the lines, and has three normalization preimages. Each of the six lines also carries exactly two distinct Whitney pinch points, given by \(x_i=1\) or \(x_i=-1\) on that line; these twelve points have one normalization preimage apiece. Apart from those sixteen distinguished points, all singular points are ordinary double normal crossings. The complement is smooth. The compactly supported topological Euler characteristic is
\[\chi_c(S_c(\mathbb C))=10.\]

## Assumptions and scope

All statements concern reduced affine varieties over \(\mathbb C\), not the singularities at infinity of projective closures. The phase parameter \(c\) ranges over **every** complex value other than \(0,\pm1\); no unmentioned genericity condition is imposed. Different roots \(\lambda\) of \(\lambda^2-2c\lambda+1\) yield the same surface via simultaneous coordinate inversion. The special members \(c=0\) and \(c=\pm1\) are excluded from the asserted sixteen-point stratification. “Ordinary double crossing” means analytic type \(UV=0\) in a smooth threefold; “pinch” means analytic type \(U^2=VW^2\); and “ordinary triple crossing” means three smooth local sheets with linearly independent tangent-plane normals, equivalently \(UVW=0\).

## Proof

**1. Equation and normalization.** Put \(x=x_1,y=x_2,z=x_3\), and \(w=(ab+(ab)^{-1})/2\). The trace identities give
\[
w^2-2xyw+x^2+y^2-1=0,\qquad
w^2-2czw+z^2+c^2-1=0.
\]
With \(A=z^2+c^2-x^2-y^2\) and \(B=2(xy-cz)\), subtraction gives \(A+Bw=0\). Eliminating \(w\) gives
\[
F_c=A^2+2xyAB+(x^2+y^2-1)B^2=0.
\]
For generic fixed \((y,z)\), the two choices each of \(b\) and \(d\) yield four distinct traces of \(a=\lambda/(bd)\), because \(\lambda^2\ne1\). Thus the image has degree four in \(x\). Since \(F_c\) is monic of degree four in \(x\), it generates the prime ideal of the image. Its total degree is six: its highest-degree term is \(4x^2y^2z^2\). Every \(a,b,d\) solves a monic quadratic over \(\mathbb C[x,y,z]\), so \(\nu\) is finite. The generic fiber is a singleton by the same four-trace argument, so \(\nu\) is birational. The source \(T_\lambda\simeq(\mathbb C^\times)^2\) is smooth and normal, and hence is the normalization.

**2. Exhaustive fiber and rank analysis.** Two preimages with equal coordinate traces differ by replacing any subset of \(a,b,d\) with inverses. Replacing all three preserves the product only when \(\lambda^2=1\), which is excluded. Replacing precisely \(a_i,a_j\) preserves the product exactly when \((a_i a_j)^2=1\). Writing \(a_i a_j=\epsilon\) gives \(x_j=\epsilon x_i\) and \(a_k=\epsilon\lambda\), hence \(x_k=\epsilon c\), exactly the six stated lines. Replacing a single coordinate does not produce a distinct preimage unless that coordinate is \(\pm1\), in which case the replacement is trivial. On \(T_\lambda\), the differential of each trace is a nonzero multiple of \(\mathrm d\log a_i\) unless \(a_i=\pm1\). Restricted to \(\sum_i\mathrm d\log a_i=0\), the Jacobian has rank below two exactly when at least two of \(a,b,d\) equal \(\pm1\). These rank-drop points lie on the six displayed lines. Outside the six lines there is a single preimage at which \(\nu\) is immersive; the finite local embedding/analytic inverse-function argument gives a smooth image. This excludes all further singularities. Conversely a generic point of every line has two distinct smooth source preimages with different tangent planes, hence is singular, and the singular locus is closed.

**3. Intersections, triple crossings, and line-wise double crossings.** The six lines meet only at the four \(P_s\), since \(c\ne0\). Each of the four lies on exactly three lines; each line contains exactly two \(P_s\). The three preimages of \(P_s\) have coordinates \(a_i=s_i\lambda^{\sigma_i}\), where exactly one \(\sigma_i=-1\) and the other two are \(+1\). This follows from the product constraint and \(\lambda^4\ne1\) (equivalent here to \(c\notin\{0,\pm1\}\)). Up to nonzero common scaling and multiplying columns by \(s_i\), the three tangent-plane normal vectors are \((-1,1,1)\), \((1,-1,1)\), and \((1,1,-1)\), whose determinant has absolute value \(4\). Thus the completed local analytic germ is three transverse smooth sheets, of ordinary triple-crossing type. At a point on just one line with \(x_i\notin\{1,-1\}\), there are exactly two preimages and two distinct tangent planes: inversion of the \(i,j\) torus coordinates changes those two normal components' signs but not the third. Since \(\lambda^2\ne1\), the third component is nonzero, so the normals are nonproportional. This is an ordinary double crossing.

**4. Whitney pinches.** On each \(\ell_{ij}^{\epsilon}\), the two points \(x_i=\pm1\) are the only rank-drop points. They lie outside the four triple crossings because \(c\ne\pm1\). At such a point choose local logarithmic source coordinates \(s,t\) with \(a_i=\rho e^s\), \(a_j=\epsilon\rho e^t\), \(a_k=\epsilon\lambda e^{-s-t}\), where \(\rho=\pm1\). Set \(u=s+t\) and \(v=(s-t)/2\). Then
\[
\rho x_i+\epsilon\rho x_j=2\cosh(u/2)\cosh(v),\qquad
\rho x_i-\epsilon\rho x_j=2\sinh(u/2)\sinh(v),
\]
while \(x_k=\epsilon\cosh(\log\lambda-u)\), whose derivative in \(u\) at zero is nonzero. It therefore provides an analytic ambient coordinate equivalent to \(U=2\sinh(u/2)\). Divide the first expression by the unit \(2\cosh(u/2)\), subtract one, and normalize the second by the analytic unit \(\cosh(v/2)\) (expressible using the first target coordinate). This transforms the germ of \(\nu\) into the standard map \((U,V)\mapsto(U,V^2,UV)\), with \(V=2\sinh(v/2)\), up to invertible scalar factors. Its image has analytic equation \(Y^2=U^2X\), a Whitney pinch. Two such points occur on each line, for twelve distinct pinches in total. The analytic coordinate transformations are valid precisely because \(\lambda\ne\pm1\).

**5. Euler characteristic.** For a finite normalization, the constructible count of preimages gives \(\chi_c(T_\lambda)=\int_{S_c}\#\nu^{-1}(p)\,\mathrm d\chi_c\). Since \(\chi_c(T_\lambda)=\chi_c((\mathbb C^\times)^2)=0\), and only double- and triple-crossing fibers have more than one point, one obtains
\[
0=\chi_c(S_c)+6\bigl(\chi_c(\mathbb A^1)-4\bigr)+4(3-1)
=\chi_c(S_c)+6(-3)+8.
\]
Here each double line has two pinch points (one preimage each) and two triple points (three preimages each), so its ordinary double-fiber stratum is a line minus four points. Hence \(\chi_c(S_c)=10\).

## Verification

The standalone script `check.py` uses exact symbolic arithmetic to verify the elimination polynomial, its leading degree, vanishing of the polynomial and all partial derivatives on each of the six lines, the incidence of four triple points (three lines through each), the twelve distinct pinch coordinates, and the degeneration at \(c=\pm1\). It also checks direct parametrization identities for several exact rational \(\lambda,a,b\). These finite computations corroborate but **do not replace** the all-parameter proof, analytic local-normal-form argument, or the global completeness argument above.

## Relationship to prior work

Mascarin–Telen introduced the triangle Lissajous surface, identified the Cayley cubic and the phase-special sextic, and proved the generic member has degree six, but did not determine the generic member's normalization, the six-line incidence, twelve Whitney pinches, or the four ordinary triple crossings. Mascarin (2026), Sections 4–5, gives general Lissajous equations and an upper/lower description of singular loci; its full explicit singular-locus result for hypersurfaces assumes at least four ambient coordinates, and its three-coordinate Example 1.2 treats a different frequency vector. The present complete local-type classification for the *phase-varying triangle family* is therefore not a restatement of that theorem. Laurent–Mascarin–Telen's graph-elliptope work determines cycle polynomials and the classical unshifted Cayley cubic, not this phase-deformed sextic basket. The previously studied phase-special member \(c=0\) (with its own normalizer and intersecting double lines) is outside this statement, and is not claimed as new. The polynomial presentation itself is a direct resultant and is **not** claimed as a novel construction.

## Limitations

This is an affine complex statement only; no singularities of projective closure at infinity, arbitrary characteristics, analytic monodromy, or independent external audit are determined. An unindexed earlier computation of these same generic-phase local singularities remains a publication-priority risk. The argument for the pinpoint local normal forms relies on characteristic-zero analytic coordinate changes; the symbolic script is a finite consistency test, not an exhaustive algebraic-closure certificate.

## References

1. F. M. Mascarin, *Intersections, Equations, and Singularities of Lissajous Varieties*, arXiv:2611.15725v1 (first posted 2026-11-11), https://arxiv.org/html/2611.15725v1, especially §§4–5.
2. F. M. Mascarin and S. Telen, *Lissajous Varieties*, arXiv:2509.06844v2 (first posted 2025-09-08), https://arxiv.org/html/2509.06844v2, especially Example 1.3 and §§2–3.
3. M. Laurent, F. M. Mascarin, and S. Telen, *The Algebraic Boundary of Graph Elliptopes*, arXiv:2605.02484v1 (first posted 2026-05-04), https://arxiv.org/html/2605.02484v1, especially Example 3.3 and §4.
