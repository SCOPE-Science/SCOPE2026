# The exact mixed-characteristic plane Hilbert scheme of the diagonal Segre cubic

## Finding
Let \(R=\mathbb Z_2\) and let \(\mathcal X\subset\mathbb P^5_R\) be the coefficientwise diagonal cubic threefold defined by
\[
\sum_{i=0}^{5}X_i=0,\qquad \sum_{i=0}^{5}X_i^3=0.
\]
Let \(H\) be the closed relative Grassmannian subscheme parametrizing **linear planes** \(\mathbb P^2\subset\mathcal X\). There is an isomorphism of finite \(R\)-schemes
\[
\boxed{H\cong\coprod_{15}\operatorname{Spec}\mathbb Z_2\;\sqcup\;\coprod_{6}\operatorname{Spec}\mathbb F_4.}
\]
The fifteen horizontal factors are the explicit perfect-matching planes, and the six vertical factors are residual-degree-two points (twelve geometric planes). Every vertical plane has no lift even to \(W_2(\mathbb F_4)\) (the unramified length-two Witt ring), while each horizontal plane lifts integrally. Thus the complete local rings of the relative plane scheme are \(\mathbb Z_2\) at the fifteen rational points and \(\mathbb F_4\) at the six degree-two points. The latter sharp first-order obstruction is the new assertion; the characteristic-two cone and its count of 27 geometric planes are previously established context, not the claimed new contribution.

## Assumptions and scope
The base is the complete discrete valuation ring \(R=\mathbb Z_2\). A plane is a linear \(\mathbb P^2\) in the given projective embedding, so \(H\subset\operatorname{Gr}_R(3,5)\) is the zero locus of the cubic restriction section. The notation \(\mathbb F_4\) means the unique quadratic extension of \(\mathbb F_2\), viewed as an \(R\)-algebra with \(2=0\). The special cubic is the **coefficientwise reduction of this specified integral diagonal model**, not the different all-characteristic GIT model of the ten-nodal Segre primal.

## Proof
**1. Integral equation and cone.** Make an integral projective coordinate change by writing \(X_i=y_i+t\) for \(0\le i\le4\), \(X_5=-5t\), subject to \(\sum_{i=0}^4y_i=0\). Put \(E_2(y)=\sum_{i<j}y_i y_j\). The identity \(\sum y_i^2=-2E_2(y)\) gives exactly
\[
\sum_{i=0}^{5}X_i^3=F_S(y)-6tE_2(y)-120t^3,\qquad F_S(y)=\sum_{i=0}^4y_i^3.
\]
Modulo two this is independent of \(t\): the special fiber is the cone with vertex \(v\) over the cubic surface \(S=V(\sum y_i,F_S(y))\subset\mathbb P^4_{\mathbb F_2}\cong\mathbb P^3_{\mathbb F_2}\). This surface is smooth: on its hyperplane, a gradient proportional to that of \(\sum y_i\) forces all five \(y_i\) equal, hence zero since five is odd.

**2. The special planes and their tangent spaces.** Every plane in the cone contains \(v\): otherwise its linear projection from \(v\) would give a plane contained in the smooth cubic surface \(S\), which is impossible. Thus planes correspond to lines on \(S\). The complete exact finite-field line enumeration attached as `verify.py` finds 27 distinct lines over \(\mathbb F_4\), of which 15 descend to \(\mathbb F_2\) and 12 form six quadratic Frobenius pairs. This is exhaustive over an algebraic closure because a smooth cubic surface has exactly 27 geometric lines. It also finds that the 15 rational lines are precisely the isotropic lines of the alternating nondegenerate pairing
\[
B(a,b)=\sum_{i=0}^{4}a_i b_i
\]
on the four-dimensional \(\mathbb F_2\)-space \(W=\{\sum_{i=0}^4y_i=0\}\), while the other 12 are nonisotropic. The five-coordinate expression is intrinsic on that hyperplane because \(B(a,a)=(\sum a_i)^2=0\).

At a special plane \(\Pi=\langle v,L\rangle\), choose coordinates \([t:u:v]\) on \(\Pi\). A first-order Grassmannian deformation consists of two normal linear forms \(\ell_1,\ell_2\); its cubic first variation is \(q_1(u,v)\ell_1+q_2(u,v)\ell_2\), where \(q_1,q_2\) are restrictions of two independent normal partial derivatives of \(F_S\). Since the ambient characteristic is two, each \(q_i\) is a square of a linear form. They have no common zero, since \(S\) is smooth along \(L\), so after coordinate changes \(q_1=u^2,q_2=v^2\). The six monomials \(u^3,u^2v,uv^2,v^3,tu^2,tv^2\) are independent. Hence the first variation map has trivial kernel. Every point of the special plane Hilbert scheme has zero relative tangent space, and the scheme is precisely the finite étale \(\mathbb F_2\)-scheme \(\coprod_{15}\operatorname{Spec}\mathbb F_2\sqcup\coprod_6\operatorname{Spec}\mathbb F_4\).

**3. Sharp modulo-four obstruction.** Reduce the exact integral equation modulo four:
\[
F_S(y)+2tE_2(y)=0\pmod4.
\]
Fix a geometric special plane \(\Pi=\langle v,a,b\rangle\) with \(a,b\) an \(\mathbb F_4\)-basis of its line. Over \(W_2(\mathbb F_4)\), any putative plane lift is, after choosing a Grassmannian chart, a deformation of its three basis vectors by twice a linear correction in \(u,v,t\). The coefficient of \(tuv\) in the cubic restriction divided by two and reduced modulo two is exactly
\[
E_2(a+b)-E_2(a)-E_2(b)=\sum_{i=0}^4a_i b_i=B(a,b).
\]
Indeed, a normal correction to \(F_S\) contributes \(\sum a_i^2\ell_i\,u^2+\sum b_i^2\ell_i\,v^2\), whose \(t\)-coefficients are combinations of \(u^2\) and \(v^2\), never \(uv\). Corrections to the term already divisible by two do not alter its reduction. Consequently, \(B(a,b)\ne0\) prevents **every** length-two Witt lift. This occurs on exactly twelve special geometric planes. For the other fifteen, the defining equations of a perfect matching of the six coordinates, \(X_i+X_j=X_k+X_l=X_m+X_n=0\), give integral plane lifts over \(R\). The fifteen matchings give fifteen pairwise distinct planes modulo two, so they exhaust the fifteen rational special planes.

**4. Determine the entire relative scheme.** The relative plane scheme \(H\) is projective over \(R\), being closed in a Grassmannian. Its special and generic fibers are finite, so \(H\to\operatorname{Spec}R\) is finite. The special fiber is finite étale by Step 2. At a point of residue degree \(d\in\{1,2\}\), its completed local ring is therefore a quotient of the unramified DVR \(W(\mathbb F_{2^d})\): the canonical unramified lift of the residue field maps into the complete local ring, and Nakayama's lemma makes this map surjective because the special local ring is the field \(\mathbb F_{2^d}\). Every ideal in that DVR is \((2^e)\) (including \(e=\infty\), the zero ideal). The fifteen integral plane sections force \(e=\infty\), so their local rings are \(\mathbb Z_2\). The modulo-four obstruction forces \(e=1\) at each of the six degree-two points, so their local rings are \(\mathbb F_4\). Since the finite closed points are pairwise disjoint in the complete Henselian base, these local descriptions yield the displayed global disjoint-union isomorphism.

## Verification
`verify.py` is a standalone Python 3 program with no third-party dependencies. It constructs \(\mathbb F_4\) exactly, enumerates all 357 lines in \(\mathbb P^3(\mathbb F_4)\), and tests the full binary-cubic restriction polynomial rather than just its rational point values. It confirms 27 surface lines, 15 Frobenius fixed lines, six two-cycles, and \(B(a,b)=0\) on exactly the 15 fixed lines. It also checks 15 lines inside \(\mathbb P^3(\mathbb F_2)\), the 15-point/15-line incidence, and basic point counts. `verify_output.txt` records its actual replay ending in `VERIFY_OK`. The universal modulo-four and local-ring conclusions follow from Steps 3–4, not finite extrapolation.

## Relationship to prior work
Collino's 2012 preprint describes the classical fifteen planes of the Segre primal and its Fano *surface of lines*. The classical 27-line theorem for smooth cubic surfaces is standard and is explicitly discussed by Debarre; the characteristic-two Clebsch surface and its 27-line arithmetic, and the special cone's 27-plane count, are already known in earlier related analyses. They are credited here as inputs. Dolgachev's all-characteristic modular Segre cubic has a different characteristic-two equation and ten nodes; it must not be conflated with this diagonal integral specialization. The present narrower contribution computes the **entire mixed-characteristic local rings**, including the sharp obstruction already over \(W_2(\mathbb F_4)\). Generic/special fiber cardinalities alone do not determine these local rings or the first infinitesimal lifting threshold.

## Limitations
This theorem concerns only planes on the explicitly specified integral diagonal cubic over \(\mathbb Z_2\), not lines, the stable modular model, other primes, or all deformations of the cubic. It does not claim that the cone structure or the 27-plane special count is new. No independent scientific audit or absolute historical-priority certification is claimed. Specialist unpublished accounts could contain an equivalent local-ring statement.

## References
1. A. Collino, *Remarks on the Topology of the Fano Surface*, arXiv:1211.2621v1 (first public submission 2012-11-12), §§2.2.1, 2.2.7–2.2.8. https://arxiv.org/abs/1211.2621
2. O. Debarre, *Around cubic hypersurfaces*, lecture notes (2015), §4.1 on 27 lines and the Clebsch cubic. https://www.math.ens.psl.eu/~debarre/Duesseldorf2014.pdf
3. I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, *Bull. Lond. Math. Soc.* 56 (2024), 1903–1919, §3, DOI 10.1112/blms.13033. https://doi.org/10.1112/blms.13033
4. P. Pokora and T. Szemberg, *A Pascal-type construction of the Segre cubic and the Cremona–Richmond configuration*, arXiv:2606.18387 (2026). Its available abstract concerns the characteristic-zero classical 15 planes; full text was not accessible in this review.
