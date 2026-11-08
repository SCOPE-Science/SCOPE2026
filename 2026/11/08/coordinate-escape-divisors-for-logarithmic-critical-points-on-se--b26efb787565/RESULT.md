# Coordinate-escape divisors for logarithmic critical points on Segre–Veronese toric surfaces

## Finding
For every integer \(m\geq 2\), take generic complex polynomials \(P(y)=\sum_{j=0}^m a_jy^j\) and \(Q(y)=\sum_{j=0}^m b_jy^j\), with algebraically independent coefficients, and the biform \(f(x,y)=P(y)+xQ(y)\). The exponent support is the rectangle \(A_m=\{0,1\}\times\{0,\ldots,m\}\). Its projective toric surface is \(\mathbb P^1\times\mathbb P^1\) polarized by \(\mathcal O(1,m)\), of degree \(2m\).

Over the rational function field \(K=\mathbb C(a_0,\ldots,a_m,b_0,\ldots,b_m,s,u,v)\), the critical points of the Euler integrand \(f(x,y)^s x^u y^v\) satisfy
\[
F=uP+(u+s)xQ=0,\qquad G=v(P+xQ)+sy(P'+xQ')=0.
\]
There are \(2m\) distinct critical points in \((\mathbb C^*)^2\setminus V(f)\) over an algebraic closure of \(K\), and their individual \(x\)- and \(y\)-coordinates are each pairwise distinct. Consequently, both coordinate eliminants are irreducible polynomials of degree \(2m\) over \(K\). Their primitive representatives are
\[
H_x(x)=\frac{\operatorname{Res}_y(F,G)}{s^m},\quad
H_y(y)=vPQ+(u+s)yP'Q-u yPQ'.
\]
The quotient defining \(H_x\) is a polynomial over the full coefficient ring, not merely a rational expression.

The exact leading and constant coefficients, with the standard Sylvester resultant convention, are
\[
[x^{2m}]H_x=(u+s)^m\operatorname{Res}_y(Q,yQ'),\qquad
[x^0]H_x=u^m\operatorname{Res}_y(P,yP'),
\]
\[
[y^{2m}]H_y=(v+ms)a_mb_m,\qquad
[y^0]H_y=va_0b_0.
\]
Equivalently, up to an overall nonzero sign depending only on \(m\), the first two coefficients have factor sets
\[
(u+s)^m b_0b_m\operatorname{Disc}(Q),\qquad
u^m a_0a_m\operatorname{Disc}(P).
\]
Thus, across the two ends, the precise degree-drop divisors for the \(x\)-coordinate eliminant are two resonance hyperplanes, four endpoint-coefficient hyperplanes, and the two degree-\(m\) edge discriminants; for the \(y\)-coordinate eliminant they are two resonance hyperplanes and the four endpoint-coefficient hyperplanes, with no edge discriminant. The resonance factor has multiplicity \(m\) in the \(x\) case, versus multiplicity one in the \(y\) case.

## Assumptions and scope
All formulas are over characteristic zero; the coefficient symbols and \(s,u,v\) are independent indeterminates, so no exceptional specialization is implicitly included. \(\operatorname{Res}_y(T,U)\) is the determinant of the Sylvester matrix, with its usual ordering, and \([x^j]\) denotes a coefficient. A vanishing leading or constant coefficient characterizes degree drop of the primitive eliminant; the geometric interpretation as escape of a critical coordinate applies generically on each indicated divisor, away from other collisions and excluded loci. This is NOT a claim that every parameter on an intersection of such divisors has a single, isolated escaping critical point.

## Proof
**(1) Polynomiality and closed formulas.** Put \(C=u yP'+x(u yQ'-vQ)\). Direct expansion gives \(uG=vF+sC\). Taking degree-\(m\) resultants with respect to \(y\), and working first where \(u\ne0\), yields
\[
u^m\operatorname{Res}_y(F,G)=s^m\operatorname{Res}_y(F,C).
\]
Both sides are polynomial identities in the integral coefficient ring; since \(u\) and \(s\) are relatively prime, \(s^m\) divides \(\operatorname{Res}_y(F,G)\). For the coefficient of \(x^{2m}\) in this quotient, retain the \(x\)-linear parts \((u+s)Q\) and \(vQ+syQ'\) of \(F\) and \(G\), respectively. Resultant homogeneity gives
\[
\frac{(u+s)^m\operatorname{Res}_y(Q,vQ+syQ')}{s^m}
=(u+s)^m\operatorname{Res}_y(Q,yQ').
\]
At \(x=0\), the same calculation gives \(u^m\operatorname{Res}_y(P,yP')\). The equality \(\operatorname{Res}(T,yT')=\operatorname{Res}(T,y)\operatorname{Res}(T,T')\) expresses either constant/leading coefficient as an endpoint coefficient, the leading coefficient and a discriminant, up to sign.

Eliminating \(x\) from two linear equations gives the exact identity
\[
\operatorname{Res}_x(F,G)=s\bigl(vPQ+(u+s)yP'Q-u yPQ'\bigr)=sH_y.
\]
The constant and degree-\(2m\) coefficients of this last polynomial are immediate. In particular \(H_y\) has degree exactly \(2m\).

**(2) Degree and absence of extraneous torus solutions.** For generic coefficients and every \(m\geq2\), the two equations cut out the logarithmic critical locus on the open torus. The Newton rectangle has normalized volume \(2m\), and the generic critical-point count for a nondegenerate toric support equals that volume (Goertz–Sturmfels–Telen, Theorem 1.3). Alternatively, their homogenizations are curves of bidegree \((1,m)\) on \(\mathbb P^1\times\mathbb P^1\), with intersection number \(2m\). The displayed nonzero endpoint resultants, together with nonzero \(s,u,v,u+s,v+ms\), rule out boundary intersections generically; \(f=0\) would force \(P=Q=0\), excluded by coprimality. The generic critical scheme is therefore reduced with \(2m\) points.

**(3) Both projections generically separate points.** The \(y\)-eliminant \(H_y\) is irreducible in \(K[y]\): regarded as a polynomial linear in \(v\), it has coefficient \(PQ\) and constant term \(y((u+s)P'Q-uPQ')\). These are coprime over \(\mathbb C(a,b,u,s)[y]\), because \(P\) and \(Q\) are squarefree, coprime, and have nonzero constant terms. Gauss's lemma applies. Hence its \(2m\) roots are simple in characteristic zero.

For \(x\), consider the incidence of two *distinct* critical points with the same \(x\)-coordinate. Fix \(x,y_1\ne y_2,s,u,v\) with \(xy_1y_2suv(u+s)(v+s)\ne0\). The four equations \(F(x,y_i)=G(x,y_i)=0\), for \(i=1,2\), impose four independent linear conditions on \((a_j,b_j)\). Independence is already visible on the four-dimensional subspace of linear \(P,Q\): each of \(F,G\) is then linear in \(y\); vanishing at both distinct values forces \(F=G=0\) identically, which for generic \(s,u,v,x\) forces all four coefficients to vanish. Thus the pair-incidence has generic dimension at most \(2m+4\), whereas the parameter space \((a,b,s,u,v)\) has dimension \(2m+5\). Degenerate parameter choices form proper closed subsets, and the same generic rank argument excludes a dominating component. Hence generic parameters admit no pair of critical points sharing \(x\).

The preceding rank-four calculation holds throughout this nonresonant open set, rather than only at a generic point of it; hence the pair-incidence cannot dominate the parameter space. The critical incidence itself is irreducible: on \(sfxy\ne0\), solve uniquely
\[
u=-\frac{s xQ}{f},\qquad v=-\frac{s y(P'+xQ')}{f}.
\]
It is a rational graph over the irreducible space of \((a,b,s,x,y)\). Its generically finite projection to parameter space is therefore an irreducible degree-\(2m\) cover. Because the \(x\) projection separates the generic fibre, its minimal polynomial has degree \(2m\). The displayed resultant has degree \(2m\), and its constant and leading coefficients have no common irreducible factor in the universal coefficient ring, so it has no extraneous parameter-only content. Hence \(H_x\) is the primitive irreducible eliminant. This completes the proof.

## Verification
Run `python verify.py` with Python 3 and SymPy (tested with SymPy 1.14). The script independently forms both Sylvester resultants, checks the exact coefficient identities for 20 integer specializations over all \(1\le m\le5\), and finds squarefree-specialization witnesses for both eliminants in every checked degree. It does not prove statements for arbitrary \(m\); the proof above does.

## Relationship to prior work
Goertz, Sturmfels and Telen introduce logarithmic \(A\)-discriminants and the coordinate eliminants in their Section 6. Their Example 6.9 computes leading/trailing coordinate coefficients for a triangular prism, while the paragraph after the example identifies determination of these factors for arbitrary supports as future work. Their general statements about the ambient resonance/principal-determinant factors do not determine the exact factor list or multiplicities for the entire Segre–Veronese rectangle family. The present result gives these coefficients for every integer \(m\geq2\), plus explicit primitive eliminants and generic coordinate separation. The bidegree-\((1,1)\) square is a previously computed consistency boundary, not a claimed new case. The general critical-point degree \(2m\) and the resultant construction are prior methods and are not claimed as new. Chestnov–Crisanti–Giroux study computational Landau singularity detection in general Euler-integral settings; their inspected text does not provide these biform coordinate-eliminant formulas.

## Limitations
The result is characteristic zero and generic-coefficient only; it does not classify singular fibres at simultaneous parameter degenerations, describe monodromy, or compute the full logarithmic \(A\)-discriminant hypersurface. The geometric interpretation of each leading/constant factor is generic on its divisor, not an assertion of clean escape at every intersection. Explicit extraction of the formulas from older general elimination methods may exist, so historical priority remains provisional; an independent audit has not been performed.

## References
1. M. Goertz, B. Sturmfels, S. Telen, *The Logarithmic A-Discriminant*, arXiv:2610.29204v1, first public 2026-10-21, especially Theorem 1.3 and Section 6, Example 6.9. https://arxiv.org/html/2610.29204
2. V. Chestnov, G. Crisanti, M. Giroux, *Landau's Leviathans*, arXiv:2606.29612v1, first public 2026-06-28; background on detecting escape of Euler-integral critical points. https://arxiv.org/abs/2606.29612
3. I. M. Gel'fand, M. M. Kapranov, A. V. Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants*, Birkhäuser, 1994; standard sparse discriminants and resultant identities.
