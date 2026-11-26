# Exact John and Löwner ellipsoids of Euclidean rounded orthotopes

## Finding
For every integer \(d\ge 3\), ball radius \(r>0\), and strictly positive orthotope half-lengths \(a_1,\ldots,a_d\), form the rounded orthotope
\[
K=\prod_{i=1}^d[-a_i,a_i]+rB_2^d\subset\mathbb R^d.
\]
Its unique maximum-volume contained **John ellipsoid** is
\[
J=\left\{x:\sum_{i=1}^d\frac{x_i^2}{(a_i+r)^2}\le1\right\}.
\]
There is a unique \(c>0\) satisfying
\[
\sum_{i=1}^d\left(\frac{\sqrt{a_i^2+4rc}-a_i}{2r}\right)^2=1.
\]
Define \(v_i=(\sqrt{a_i^2+4rc}-a_i)/(2r)\) and \(z_i=a_i+rv_i\). The unique minimum-volume enclosing **Löwner ellipsoid**, with no restriction on a competitor's orientation or center, is
\[
L=\left\{x:\sum_{i=1}^d\frac{x_i^2}{d z_i^2}\le1\right\}.
\]
The entire contact set \(K\cap\partial L\) consists of precisely the \(2^d\) signed points \((\varepsilon_1z_1,\ldots,\varepsilon_dz_d)\), \(\varepsilon_i\in\{-1,1\}\). In particular, \(L\) is the Löwner ellipsoid of the unique maximum-volume centered axis-aligned box contained in \(K\), whose half-lengths are \(z_i\).

Writing \(\kappa_d=\operatorname{Vol}(B_2^d)\), the two volumes and their exact quotient are
\[
\operatorname{Vol}(J)=\kappa_d\prod_i(a_i+r),\qquad
\operatorname{Vol}(L)=\kappa_d d^{d/2}\prod_i z_i,
\]
\[
\frac{\operatorname{Vol}(L)}{\operatorname{Vol}(J)}
=d^{d/2}\prod_i\frac{a_i+rv_i}{a_i+r}.
\]
For fixed positive half-lengths, this quotient tends to \(d^{d/2}\) as \(r\downarrow0\) and to \(1\) as \(r\to\infty\). No monotonicity in \(r\) is asserted.

## Assumptions and scope
Here \(B_2^d=\{x\in\mathbb R^d:\|x\|_2\le1\}\), a Minkowski sum \(A+B=\{a+b:a\in A,b\in B\}\), and an ellipsoid \(E(q,Q)\) means \(\{x:(x-q)^\top Q^{-1}(x-q)\le1\}\) with positive definite \(Q\). All radii and half-lengths are strictly positive; this is essential for the asserted finite contact-set description. Dimension is fixed but arbitrary \(d\ge3\). Orthotope edges are pairwise perpendicular. No claim is made for arbitrarily skew parallelepipeds plus a Euclidean ball.

## Proof
**1. John's ellipsoid.** For \(u\in B_2^d\), write \(((a_i+r)u_i)_i=(a_i u_i)_i+ru\). The first summand belongs to the orthotope and the second to \(rB_2^d\), hence \(J\subseteq K\). Every coordinate of a point of \(K\) has modulus at most \(a_i+r\). If an arbitrary contained ellipsoid has center \(q\) and positive definite shape \(Q\), its two extreme coordinate values imply \(|q_i|+\sqrt{Q_{ii}}\le a_i+r\). Hadamard's determinant inequality gives
\[
\det Q\le\prod_i Q_{ii}\le\prod_i(a_i+r)^2.
\]
Equality forces \(q=0\) and the diagonal shape of \(J\); this proves global optimality and uniqueness.

**2. The unique contact box.** Let \(U=\{v\in\mathbb R^d:v_i\ge0,\ \|v\|_2\le1\}\). The strictly concave function \(\Phi(v)=\sum_i\log(a_i+rv_i)\) has a unique maximizer on \(U\). Its partial derivatives are positive, so the norm constraint is active; no coordinate can vanish, since introducing a small positive coordinate increases \(\Phi\) to first order while preserving the norm by a second-order correction. Its Lagrange conditions give
\[
\frac{r}{a_i+rv_i}=2\lambda v_i,\qquad
v_i(a_i+rv_i)=c=\frac{r}{2\lambda}>0.
\]
Conversely the positive quadratic roots shown in the finding depend continuously and strictly increasingly on \(c\), start at zero, and have unbounded squared sum. Thus exactly one \(c>0\) normalizes \(\sum_i v_i^2=1\); strict concavity makes it the maximizer. A centered axis-aligned box with positive half-lengths \(t_i\) is contained in the unconditional convex body \(K\) precisely when its positive corner \((t_i)\) lies in \(K\). At a volume maximizer, that corner has the form \((a_i+rv_i)\) with \(v\in U\): one can increase each coordinate until the orthotope support and Euclidean radius are saturated. Consequently the unique largest centered box has half-lengths \(z_i=a_i+rv_i\).

**3. Global containment in the proposed Löwner ellipsoid.** Write any \(x\in K\) as \(x=b+rw\) with \(|b_i|\le a_i\) and \(\|w\|_2\le1\). Put \(u_i=|w_i|\). Then \(|x_i|\le a_i+ru_i\), \(\|u\|_2\le1\). Using \(v_i z_i=c\) and the identity \(2v\cdot(u-v)=\|u\|^2-1-\|u-v\|^2\), an exact expansion gives
\[
\sum_i\frac{(a_i+ru_i)^2}{z_i^2}-d
=\frac rc(\|u\|_2^2-1)
-\sum_i\left(\frac rc-\frac{r^2}{z_i^2}\right)(u_i-v_i)^2.
\]
Every coefficient in the final sum is strictly positive, since \(z_i^2-rc=a_i z_i>0\). Therefore \(\sum_i x_i^2/(d z_i^2)\le1\), proving \(K\subseteq L\). Equality forces \(u=v\), \(\|w\|=1\), and equality in every coordinate triangle inequality; strict positivity of \(a_i,v_i\) then gives precisely the signed corners \(x_i=\varepsilon_i z_i\). Every one of those corners lies in \(K\), by choosing the corresponding orthotope corner and the signed vector \(r v\).

**4. Optimality among all enclosing ellipsoids.** Put \(D=\operatorname{diag}(z_1,\ldots,z_d)\). If any positive-definite ellipsoid \(E(q,Q)\) contains \(K\), it contains all \(2^d\) points \(D\varepsilon\), for sign vectors \(\varepsilon\). Average their defining quadratic inequalities, using \(\mathbb E\varepsilon=0\), \(\mathbb E\varepsilon\varepsilon^\top=I_d\), to obtain
\[
\operatorname{tr}(Q^{-1}D^2)+q^\top Q^{-1}q\le1.
\]
The arithmetic–geometric mean inequality applied to the eigenvalues of \(Q^{-1/2}D^2Q^{-1/2}\) yields
\[
1\ge\operatorname{tr}(Q^{-1}D^2)\ge
 d\left(\frac{\det D^2}{\det Q}\right)^{1/d}.
\]
Hence \(\det Q\ge d^d\det D^2\), with equality only at \(q=0\), \(Q=dD^2\). This is exactly \(L\), so it is the unique unrestricted minimum-volume enclosing ellipsoid. The signed contact points become the isotropic design \(\varepsilon/\sqrt d\) under normalization by \(L\).

**5. Endpoint volume ratios.** As \(r\downarrow0\), \(0<v_i<1\) and \(z_i\to a_i\); the quotient therefore tends to \(d^{d/2}\). As \(r\to\infty\), the variational problem, after dividing the objective's arguments by \(r\), tends to maximizing \(\prod_i v_i\) on the positive unit ball. By uniqueness its maximizer approaches \((1/\sqrt d,\ldots,1/\sqrt d)\), giving \(z_i/r\to1/\sqrt d\) and ratio \(1\).

## Verification
The standalone script `VERIFY.py` independently solves the scalar equation, compares its solution with a constrained nonlinear optimizer for maximum-product contact boxes, checks the exact isotropic sign-contact identities, and tests enclosure at 30,000 independent sampled body points over 150 parameter configurations of dimensions 3, 4, 5, 8 and 12. Its deterministic run outputs `PASS`. Numerical tests are not the proof of any infinite statement; the analytical containment identity and determinant inequality are decisive. Run `python VERIFY.py` with NumPy and SciPy.

## Relationship to prior work
Todd's 2007 lecture describes general minimum-volume enclosing ellipsoids and moment-duality certificates; Henk's 2012 exposition gives John's finite contact characterization. These general criteria are used but not claimed as new. The earlier exact capsule case (a single nonzero segment direction) involves rotationally continuous contacts and is not the multiaxial positive-half-length result here. Courteaux, Ramlot, Lambert and Van Wallendael (2025) study the same *type of Minkowski sum*, with an arbitrary ellipsoid rather than necessarily a ball, and develop two-box approximations; their §§2–3 also discuss iterative minimum-volume bounds within standard outer-ellipsoid families. Their displayed statements do not give this unrestricted exact ball–orthotope ellipsoid, scalar normalizing equation, and \(2^d\)-point complete contact set. General ellipsoid-sum bounds and optimization algorithms can approximate or compute such ellipsoids numerically; that does not by itself provide this exact all-parameter classification. Historical priority outside the inspected sources remains unverified.

## Limitations
The ball is Euclidean and the box axes must be orthogonal. Strictly positive \(a_i\) ensure all contacts are isolated signed corners; with zero half-lengths other orbit structures may arise, and the assertion of exactly \(2^d\) contacts is not extended to that boundary. The result does not determine the body's volume, arbitrary anisotropic ellipsoid summands, or the monotonicity of the John–Löwner volume ratio in \(r\). The literature comparison is not a worldwide novelty certificate.

## References
1. M. J. Todd, *Minimum-Volume Ellipsoids: Applications, Duality, and Algorithms*, lecture dated 6 July 2007, Cornell University. https://people.orie.cornell.edu/~miketodd/ublndetz.pdf
2. M. Henk, *Löwner–John Ellipsoids*, Documenta Mathematica, Extra Volume ISMP (2012), pp. 95–106. https://ems.press/content/book-chapter-files/27356?nt=1
3. M. Courteaux, B. Ramlot, P. Lambert and G. Van Wallendael, *Lightweight Implicit Approximation of the Minkowski Sum of an N-Dimensional Ellipsoid and Hyperrectangle*, Mathematics **13** (2025), 1326. https://doi.org/10.3390/math13081326 ; open full text: https://imec-publications.be/bitstreams/5b3c16fd-0fc4-4c9d-adcd-0396e3638f17/download
4. A. Seeger, *Calculus rules for combinations of ellipsoids and applications*, Bulletin of the Australian Mathematical Society **47** (1993), pp. 1–12. https://doi.org/10.1017/S0004972700012211 (abstract inspected; full text not available in this comparison).
