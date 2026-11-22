# Exact sixth-distance local rigidity of the regular hexagon

## Finding
Let \(Q\subset\mathbb R^2\) be a positively oriented convex hexagon with six labeled vertices and all interior angles less than \(\pi\), and define
\[
\Phi(Q)=\frac{1}{\operatorname{area}(Q)^5}\int_Q\int_Q\|x-y\|^6\,dx\,dy.
\]
For every such \(Q\) sufficiently close, up to a direct Euclidean similarity and compatible cyclic labeling, to a regular hexagon \(H\),
\[
\Phi(Q)\ge\Phi(H)=\frac{191\sqrt3}{2835},
\]
with equality exactly when \(Q\) is itself a regular hexagon (equivalently, similar to \(H\)).

In the triangular-lattice vertex coordinates specified below, the Hessian of \(\log\Phi\) at \(H\) has precisely four zero eigenvalues, corresponding exactly to translations, rotation, and scale, and eight strictly positive eigenvalues. Its characteristic polynomial factors over the rationals into four explicit quadratics and a fourth power of the variable. This supplies an exact, non-numerical certification of *full local* sixth-distance-energy minimality, rather than global minimality.

## Assumptions and scope
The area and double integral are ordinary Euclidean Lebesgue integrals. The labeling remains cyclic and the hexagon remains a convex six-vertex polygon with all interior angles less than \(\pi\) in a neighborhood of the regular one; these conditions are open. Translation, rotation, and positive scaling preserve \(\Phi\), because the numerator scales by the tenth power of length and the denominator does likewise.

Choose oblique coordinates \((u,v)\) with Euclidean realization
\[
T(u,v)=(u+v/2,\sqrt3\,v/2),\qquad
q(u,v)=u^2+uv+v^2=\|T(u,v)\|^2.
\]
The regular hexagon \(H=T(P_0)\) has circumradius one, where the ordered vertices of \(P_0\) are
\[
(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1).
\]
For an arbitrary nearby oblique-coordinate polygon \(P\), write \(A(P)\) for its coordinate area, and
\[
E(P)=\int_P\int_P q(x-y)^3\,dx\,dy,\quad f(P)=E(P)/A(P)^5.
\]
Since \(\det T=\sqrt3/2\), \(\Phi(T(P))=(2/\sqrt3)^3 f(P)\). Consequently \(f\) and \(\Phi\) have identical local stationary and Hessian-sign properties in vertex coordinates.

## Proof
**1. Exact polygon moments.** For integers \(p,q\ge0\), set \(M_{pq}(P)=\int_P u^pv^q\,du\,dv\). In the neighborhood considered, the origin lies inside the hexagon and \(P\) is the union of the six oriented triangles \(\operatorname{conv}(0,w_i,w_{i+1})\), with cyclic indices. For any such triangle with \(w_i=(a,b)\), \(w_{i+1}=(c,d)\), the affine simplex change of variables and the beta integral yield
\[
\begin{aligned}
\int_{\operatorname{conv}(0,(a,b),(c,d))}u^pv^q\,du\,dv
={ad-bc\over(p+q+2)!}
\sum_{r=0}^p\sum_{s=0}^q
&\binom pr\binom qs(r+s)!(p+q-r-s)!\\
&\quad\cdot a^rb^sc^{p-r}d^{q-s}.
\end{aligned}
\]
Summing these six polynomial expressions gives every \(M_{pq}\) as an exact polynomial in the twelve vertex coordinates. Differentiation through second order is therefore algebraically legitimate throughout this neighborhood.

**2. Sixth-distance energy.** Expand the polynomial
\[
((u-U)^2+(u-U)(v-V)+(v-V)^2)^3
=\sum c_{pqrs}u^pv^qU^rV^s.
\]
The coefficients \(c_{pqrs}\) are integers and \(p+q+r+s=6\). Consequently
\[
E(P)=\sum c_{pqrs}M_{pq}(P)M_{rs}(P).
\]
Applying the preceding exact moment formula and its first and second derivatives to \(P_0\) gives
\[
A(P_0)=3,\qquad E(P_0)=5157/280,\qquad
\nabla E(P_0)={5E(P_0)\over A(P_0)}\nabla A(P_0).
\]
Thus \(\nabla\log f(P_0)=0\). The stated Euclidean value follows from \(f(P_0)=5157/(280\cdot3^5)\) and the Jacobian factor \((2/\sqrt3)^3\).

**3. Exact transverse Hessian.** In the coordinate order
\[
(u_0,v_0,u_1,v_1,\ldots,u_5,v_5),
\]
let \(L=D^2\log f(P_0)\). Writing gradients as columns and second derivatives as matrices, differentiation gives
\[
L={E''\over E}-{E'E'^{\!T}\over E^2}
-5{A''\over A}+5{A'A'^{\!T}\over A^2},
\]
where all quantities are evaluated at \(P_0\). The integer matrix \(25785L\) is recorded in `HESSIAN.json` and is reconstructed from independent polynomial coefficients by `verify.py`. Its characteristic polynomial is
\[
\det(zI-L)=z^4\prod_{j=1}^4\frac{F_j(z)}{\operatorname{lc}(F_j)},
\]
with
\[
\begin{aligned}
F_1(z)&=984987z^2-6040566z+4139272,\\
F_2(z)&=2954961z^2-13920462z+4139272,\\
F_3(z)&=4924935z^2-5929404z+730904,\\
F_4(z)&=24624675z^2-61299540z+8316776.
\end{aligned}
\]
For each of these four quadratic factors, its leading and constant coefficients are positive and its linear coefficient is negative. Because \(L\) is real symmetric, all roots of its characteristic polynomial are real; the two roots in each quadratic have positive sum and positive product, hence are both strictly positive. Since none of their constant coefficients vanishes, precisely four eigenvalues are zero.

The four similarity tangent vectors are independent and lie in the kernel: the two constant coordinate translations; the vector of all vertices (dilation); and the infinitesimal Euclidean rotation \((u,v)\mapsto(-u-2v,2u+v)\), a nonzero scalar multiple of the physical rotation generator in the \(T\)-coordinates. They span the whole four-dimensional nullspace.

**4. Local rigidity.** Modulo direct Euclidean similarities, a neighborhood of the regular hexagon admits a smooth eight-dimensional transverse coordinate slice. On that slice the gradient of \(\log\Phi\) vanishes and its Hessian is positive definite by the preceding calculation. Taylor's theorem implies strict local minimality. The only nearby equality configurations are on the similarity orbit of the regular hexagon, proving the claim.

## Verification
The self-contained exact-arithmetic script `verify.py` reconstructs all required moments, derivatives, the stationary relation, the integer Hessian, its characteristic polynomial, its rank, the four explicit similarity-null vectors, and the exact energy value. Run `python verify.py` from the directory containing the files. With SymPy available it prints a PASS report and regenerates `HESSIAN.json`; the delivered `HESSIAN.json` also supplies the matrix independently of a rerun.

The separate `crosscheck.py` uses a degree-exact five-by-five tensor-product Gauss rule on each triangle pair, with floating-point arithmetic, to reconstruct area and energy, and compares twelve independent directional finite-difference second derivatives to the exact Hessian. Run `python crosscheck.py` after the exact verifier. Both scripts passed on the supplied files. Floating-point checks are corroboration; the proof of positivity is the rational factorization above.

## Relationship to prior work
Bogosel, Bucur, and Fragalà, in the preprint first made public February 22, 2023, proved polygonal nonlocal isoperimetric results for the quadratic and quartic distance powers and stated a higher-power problem. Their numerical calculations report four zero and the other positive Hessian eigenvalues for regular polygons including six vertices with sixth-power interaction. Those *numerical* statements strongly anticipate the sign but do not provide the exact characteristic polynomial or a proof of the full hexagonal local theorem. The present result supplies that exact rigorous missing step for this one parameter pair.

Bonacini, Cristoferi, and Topaloglu (first posted March 11, 2021) rigorously treat nonlocal interactions for triangles and quadrilaterals, but do not imply this six-vertex sixth-power local statement. No claim of global optimality, or novelty of the numerical sign pattern, is made.

## Limitations
This theorem is local and restricted to positively labeled convex hexagons with noncollinear consecutive edges and the sixth Euclidean distance power. It does not establish a global minimum among all hexagons, any result for other polygon orders or exponents, or independent review. Priority remains subject to possible unindexed exact calculations or subsequent published certified local analyses. The rational characteristic polynomial is reconstructed by symbolic exact arithmetic, and its independent check is floating-point; no formal proof assistant or third-party independent audit was used.

## References
1. B. Bogosel, D. Bucur, I. Fragalà, *The nonlocal isoperimetric problem for polygons: Hardy-Littlewood and Riesz inequalities*, arXiv:2302.11677, first publicly posted 2023-02-22. https://arxiv.org/abs/2302.11677 . Especially Sections 2–3 and Appendix 9.3.
2. M. Bonacini, R. Cristoferi, I. Topaloglu, *Riesz-type inequalities and overdetermined problems for triangles and quadrilaterals*, arXiv:2103.06657, first publicly posted 2021-03-11. https://arxiv.org/abs/2103.06657 .
