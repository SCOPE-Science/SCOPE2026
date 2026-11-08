# Integral Weil–Cartier divisor defect of the weight-12 motivic toric base
## Finding
Let \(k\) be an algebraically closed field of characteristic zero. Consider the projective toric threefold \(Y\subset\mathbb P^6_k\) defined by
\[
 af=b^2,\qquad be=c^2,\qquad bg=cd,\qquad cg=de
\]
in homogeneous coordinates \([a:b:c:d:e:f:g]\). This is the reduced three-dimensional weight-12 toric base of Burmester–Charlton–Kidambi–Lotter–Preiß, Example 3.8. The integral divisor groups are
\[
\boxed{\operatorname{Cl}(Y)\cong\mathbb Z^3,\quad
\operatorname{Pic}(Y)=\mathbb Z[\mathcal O_Y(1)],\quad
\operatorname{Cl}(Y)/\operatorname{Pic}(Y)\cong\mathbb Z^2\oplus\mathbb Z/2\mathbb Z.}
\]
In particular \(\mathcal O_Y(1)\) is primitive among Cartier classes but twice a non-Cartier Weil class. The free rank-two Weil–Cartier defect detects the failure of \(\mathbb Q\)-factoriality; the additional order-two element records an integral failure invisible to rational divisor ranks.

## Assumptions and scope
All divisor groups are those of the normal projective variety \(Y\), not of its affine cone or of the full weight-12 relation variety. The variety is normal by the cited source's normality theorem. \(\operatorname{Cl}\) denotes Weil divisor classes modulo principal divisors and \(\operatorname{Pic}\) denotes line bundles/Cartier classes. Calculations use the saturated torus character lattice; there are no assumptions about smoothness or \(\mathbb Q\)-factoriality.

## Proof
**1. Recover the integral polytope.** The four relations show the seven degree-one characters may be represented in \(\mathbb Z^4\) by
\[
\begin{array}{c|rrrrrrr}
& a&b&c&d&e&f&g\\ \hline
& (1,0,0,0)&(0,1,0,0)&(0,0,1,0)&(0,0,0,1)&(0,-1,2,0)&(-1,2,0,0)&(0,-1,1,1)
\end{array}
\]
where each column has coordinate sum one. The first four characters form an integral basis, so the quotient character lattice by the common grading is saturated of rank three. Subtract the exponent of \(d\), then use its first three coordinates. The resulting lattice points, in the order \(a,b,c,d,e,f,g\), are
\[
(1,0,0),\ (0,1,0),\ (0,0,1),\ (0,0,0),\ (0,-1,2),\ (-1,2,0),\ (0,-1,1).
\]
Their convex hull \(P\) has five vertices \(a,d,e,f,g\); \(b\) and \(c\) are nonvertices on boundary edges. In the convention \(P=\{x:Rx\le h\}\), the primitive outward facet normals and integral support numbers are
\[
R=\begin{pmatrix}
1&1&1\\0&0&-1\\-3&-1&0\\-2&-1&-1\\1&-1&0\\0&-1&-1
\end{pmatrix},\qquad
h=\begin{pmatrix}1\\0\\1\\0\\1\\0\end{pmatrix}.
\]
Direct substitution verifies all seven points satisfy these inequalities. The six facet triples of polytope vertices are \(\{a,e,f\}\), \(\{a,d,f\}\), \(\{e,f,g\}\), \(\{d,f,g\}\), \(\{a,e,g\}\), and \(\{a,d,g\}\). Each bound is tight at the corresponding triple. Their half-spaces have no other vertices, by intersecting triples of supporting hyperplanes. Thus these six are precisely the facets, and the toric normal fan has precisely six rays with primitive generators the rows of \(R\).

**2. Integral Weil classes.** The standard toric divisor sequence is
\[
0\longrightarrow M\cong\mathbb Z^3\xrightarrow{R}\mathbb Z^6
\longrightarrow\operatorname{Cl}(Y)\longrightarrow0.
\]
The integer matrix \(R\) has rank three and the greatest common divisor of its \(3\times3\) minors equals one. Hence its Smith invariants are \((1,1,1)\). It follows that \(\operatorname{Cl}(Y)\cong\mathbb Z^3\), with no torsion.

**3. Cartier rank and its integral generator.** The five normal-fan maximal cones correspond to the five vertices of \(P\). At the nonsimplicial cones corresponding to \(a,f,g\), the integral Cartier support numbers \(D=(D_1,\ldots,D_6)\) satisfy, respectively,
\[
\begin{split}
D_1-D_2-D_5+2D_6&=0,\\
D_1-D_2-D_3+2D_4&=0,\\
D_3-2D_4-D_5+2D_6&=0.
\end{split}
\]
The third equality is the difference of the first two, so these are two independent rational constraints. The two other simplicial cones need no further rational constraint. Thus the rational Cartier-support space has dimension four, three of which are principal characters, so \(\operatorname{Pic}(Y)\) has rank one. (Integral Cartierness at every maximal cone also requires integer slopes; this can affect the Cartier sublattice but not its rank.) The support vector \(h\) defines the very ample bundle \(H=\mathcal O_Y(1)\), hence is Cartier. Any other Cartier class is rationally \(\lambda H\) for some \(\lambda\in\mathbb Q\). After subtracting a rational principal support function, its local linear slopes at the maximal cones equal \(\lambda\) times the corresponding vertices of \(P\). Because the slopes before subtraction are integral and the principal correction is the same at every cone, differences of these slopes are integral. In particular the vertices \(d=(0,0,0)\) and \(a=(1,0,0)\) differ by a primitive lattice vector, so \(\lambda\in\mathbb Z\). Every Cartier class is therefore an integer multiple of \(H\), proving \(\operatorname{Pic}(Y)=\mathbb Z[H]\).

**4. The integral defect.** The inclusion \(\mathbb Z[H]\hookrightarrow\operatorname{Cl}(Y)\) is induced by appending \(h\) as a fourth column to \(R\). All \(4\times4\) minors of \([R\mid h]\) have greatest common divisor \(2\); its rank is four, and the greatest common divisor of the \(3\times3\) minors is one. Its Smith invariants are therefore \((1,1,1,2)\), giving
\[
\operatorname{Cl}(Y)/\mathbb Z[H]\cong\mathbb Z^2\oplus\mathbb Z/2\mathbb Z.
\]
A concrete witness is the torus-invariant Weil divisor with coefficient vector \(D=(0,0,2,1,0,0)\): the identity \(2D=h-R(1,0,0)^{\mathsf T}\) holds in \(\mathbb Z^6\). Hence \(2[D]=[H]\), although \(D\) is not Cartier by the generation conclusion. This shows the order-two defect is genuine, not a numerical artifact.

## Verification
The standalone standard-library program `verify.py` reconstructs the exact facet inequalities and incidences, computes ranks and gcds of all relevant minors using integer arithmetic, checks the three nonsimplicial support relations and confirms the half-hyperplane witness. The checker is finite verification of the explicitly displayed integer matrices; the general toric divisor-sequence argument and integral Cartier proof are mathematical arguments, not inferred from sampling.

## Relationship to prior work
Burmester, Charlton, Kidambi, Lotter and Preiß, arXiv:2610.37351v1 (first public October 27, 2026), Example 3.8, establish the four quadrics, the three-dimensional base, and its lattice polytope; their Theorem 3.15 addresses normality. The source does not state the integral class/Picard groups or the order-two quotient. Existing local singular-stratum descriptions for the same base distinguish singularity types and the \(\mathbb Q\)-Gorenstein locus, but do not determine these global integral groups. The toric divisor exact sequence itself is standard; the specific lattice computation and nonprimitive hyperplane class are the claimed contribution.

## Limitations
This does not establish new relations among numerical multiple zeta values, does not compute the divisor class groups of the full weight-12 affine cone, and does not classify other weights. Historical priority is subject to further expert review because the result could be implicit in another source on this explicit polytope. No independent mathematical audit has been performed.

## References
1. A. Burmester, S. Charlton, A. Kidambi, F. Lotter and R. Preiß, *Toric Varieties from Multiple Zeta Values*, arXiv:2610.37351v1 (October 27, 2026), Example 3.8 and Theorem 3.15.
2. Standard toric divisor-class sequence and integral support-function description for a normal toric variety (used as established background, not claimed as a new theorem).
