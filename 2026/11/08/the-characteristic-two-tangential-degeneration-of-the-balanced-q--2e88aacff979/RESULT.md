# The characteristic-two tangential degeneration of the balanced quartic scroll

## Finding
Let \(k\) be any field and let \(X=S(2,2)\subset\mathbb P^5_k\) be the smooth balanced rational normal quartic scroll, with its fixed monomial embedding
\[
([s:t],[u:v])\longmapsto
[u s^2:u st:u t^2:v s^2:v st:v t^2].
\]
For ambient coordinates \([A_0:A_1:A_2:B_0:B_1:B_2]\), set
\[
M_0=A_1B_2-A_2B_1,\quad
M_1=A_2B_0-A_0B_2,\quad
M_2=A_0B_1-A_1B_0.
\]
Write \(\tau(X)\) for the **reduced** projective tangential variety, namely the closure of the union of the embedded tangent planes to \(X\).

**Theorem.** If \(\operatorname{char}(k)\ne2\), then \(\tau(X)\) is the integral quartic hypersurface
\[
\tau(X)=V(M_1^2-4M_0M_2).
\]
Its standard tangent-incidence parametrization is birational, and the quartic is nonnormal: its singular locus contains the rank-one \(2\times3\) matrices, a divisor in \(\tau(X)\).

If \(\operatorname{char}(k)=2\), then \(\tau(X)\) is instead the geometrically integral **normal quadric**
\[
\tau(X)=V(Q),\qquad Q=A_0B_2-A_2B_0=-M_1.
\]
Its scheme-theoretic singular locus is the line \(V(A_0,A_2,B_0,B_2)\). The tangent-incidence parametrization is generically **purely inseparable of degree two**. In fact, over the chart \(A_2\ne0\), its function-field extension is obtained by adjoining \(z\) with \(z^2=A_0/A_2\).

Moreover the primitive integral quartic \(H=M_1^2-4M_0M_2\) defines a flat quartic hypersurface over \(\mathbb Z\), whose special fiber at two is \(V(Q^2)\), a nonreduced double quadric, not \(\tau(X_{\mathbb F_2})=V(Q)\). Thus taking the **reduced tangential variety** fails to commute with specialization at two; the normality and generic tangent-incidence degree also change.

## Assumptions and scope
The scroll is the explicit integral monomial model above, not a factorial-scaled symmetric-tensor coordinate reduction. All hypersurface equalities are scheme-theoretic for the reduced image: their ideals are respectively the principal prime ideals \((H)\) when the characteristic is not two and \((Q)\) in characteristic two. The comparison of integral and modular fibers is made in this fixed ambient projective coordinate space. "Degree two" for the incidence map means degree of the induced extension of rational function fields, not the number of distinct geometric points in a generic fiber.

## Proof
Write \(q(z)=(z^2,z,1)\) on the dense chart \(t=1\) of the base \(\mathbb P^1\). Its derivative is \(q'(z)=(2z,1,0)\). The tangent plane at the scroll point with base coordinate \(z\) and ruling vector \([u:v]\) is spanned by the ruling vectors with rows proportional to \(q(z)\) together with the base derivative \((u,v)\otimes q'(z)\). Taking the union over \([u:v]\) shows that the tangential incidence over fixed \(z\) is the projective three-space of all matrices whose two rows belong to \(\langle q(z),q'(z)\rangle\):
\[
(A_0,A_1,A_2)=(\alpha z^2+2rz,\alpha z+r,\alpha),\qquad
(B_0,B_1,B_2)=(\beta z^2+2sz,\beta z+s,\beta).
\]
We used \(r,s\) merely as free coefficients, independently of the original homogeneous base coordinate. The closure of these three-spaces as \(z\) varies is irreducible of dimension four: on the rank-two-matrix locus the row span determines its annihilator, and a general tangent line of the conic \([z^2:z:1]\) is determined up to the inseparability described below.

For a rank-two matrix, the annihilator of its row span is \([M_0:M_1:M_2]\). The dual conic of the plane conic \([s^2:st:t^2]\) is given by the binary-quadratic discriminant \(M_1^2-4M_0M_2\). If the characteristic is not two, the tangent-line normal vector is \([1:-2z:z^2]\). This gives the quartic equation \(H=0\), and conversely every rank-two point of \(H=0\) lies in the tangent-incidence image after extending scalars to an algebraic closure. As the rank-one locus has codimension two in \(\mathbb P^5\), it creates no other hypersurface component. The quartic is generically reduced: at the rank-two matrix with rows \((0,0,1)\), \((0,1,0)\), its partial derivative with respect to \(A_0\) is \(4\), nonzero whenever \(2\) is invertible. Hence \(H\) is the reduced irreducible defining equation. On the dense open where \(M_0\ne0\), \(z=-M_1/(2M_0)\), so the incidence map is birational.

In characteristic two the derivative is \(q'(z)=(0,1,0)\), and its tangent-line normal vector is \([1:0:z^2]\). The closure of these normals is the reduced line \(M_1=0\) in the dual plane (Frobenius is dominant). Pulling this line back via the rank-two annihilator map gives \(Q=0\). This quadric is irreducible, and the rank-two locus is dense, hence its principal ideal is precisely the ideal of the reduced tangential variety. On the affine chart \(A_2=1\) of this quadric, the equation gives \(B_0=A_0B_2\), so its rational function field is \(k(A_0,A_1,B_1,B_2)\). The tangent parameter satisfies \(z^2=A_0\) and generates an extension of degree two, since the variable \(A_0\) is not a square in this rational function field (use valuation at \(A_0=0\)). The extension is purely inseparable. The same description on general \(A_2\ne0\) is \(z^2=A_0/A_2\).

Differentiating \(Q=A_0B_2-A_2B_0\) shows its gradient vanishes exactly where \(A_0=A_2=B_0=B_2=0\); the other two coordinates are free, giving a projective line. A hypersurface is Cohen–Macaulay and therefore satisfies Serre's condition \(S_2\). Since this singular line has codimension three inside the four-dimensional quadric, the quadric satisfies \(R_1\), and Serre's criterion proves normality. In characteristic different from two, every rank-one matrix has all three minors zero, so the gradient of \(H\) vanishes. The rank-one Segre locus has dimension three inside the four-dimensional quartic; failure of regularity in codimension one proves the latter is nonnormal.

Finally, \(H\) has coprime integral coefficients and is primitive, so \(\mathbb Z[A_0,A_1,A_2,B_0,B_1,B_2]/(H)\) is torsion-free over \(\mathbb Z\), hence flat. Coefficientwise reduction at two gives \(H\equiv M_1^2=Q^2\), whereas the actual reduced tangential image has equation \(Q=0\). This proves the stated discrepancy of fibers.

## Verification
Run \(\texttt{python3 VERIFY.py}\) in an environment with SymPy. The standalone verifier checks the quartic identity on the tangent parametrization, exact reduction of \(H\) to \(Q^2\), the differential structure of \(Q\), and direct rank-two point-set comparisons over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). It reports \(\texttt{ALL_CHECKS_PASSED}\). The rank-two finite-field comparisons are corroborating checks; the proof above, not finite enumeration, establishes the claims over arbitrary fields.

## Relationship to prior work
Oeding and Raicu (first preprint 2011) determine the equations of Segre–Veronese tangential varieties **in characteristic zero**, including the quartic-generator case associated with bidegree \((2,1)\). Catalisano and Oneto study secant dimensions of these tangential surfaces over \(\mathbb C\). Khadam and Vodička study their Cohen–Macaulay and Gorenstein properties over \(\mathbb C\). These results do not assert the characteristic-two reduced equation, its Frobenius incidence degree, or the comparison with the doubled integral fiber.

Van Geemen and Marrani study quartic-to-quadric tangential degenerations in characteristic two for different homogeneous varieties (including the Segre threefold and certain Grassmannians). Their discriminant mechanism is analogous, but those varieties are not the balanced quartic scroll \(S(2,2)\) considered here. The general phenomenon of anomalous characteristic-two tangency is therefore not claimed as new; the precise scroll result and its normalization/base-change consequences are the scope of this theorem.

## Limitations
No claim of uniqueness in the literature or independent validation is made. Specialized historical treatments of tangent developables of scrolls, if unlocated, could supply equivalent statements. The theorem concerns the ordinary reduced embedded tangential variety and the fixed integral hypersurface defined by \(H\), not derived or scheme-theoretic tangent stacks, nor every model of the scroll in mixed characteristic. Finite-field computations do not by themselves establish the theorem.

## References
1. L. Oeding and C. Raicu, *Tangential varieties of Segre–Veronese varieties*, arXiv:1111.6202 (initially public 2011-11-26), Sections 1–2; published in Collectanea Mathematica (2014).
2. M. V. Catalisano and A. Oneto, *Tangential varieties of Segre–Veronese surfaces are never defective*, arXiv:1805.11964 (2018), Introduction and Section 2.
3. B. van Geemen and A. Marrani, *Lagrangian Grassmannians and Spinor Varieties in Characteristic Two*, SIGMA 15 (2019), 064, Sections 6.6–6.7; arXiv:1903.01228.
4. M. A. Khadam and M. Vodička, *Cohen–Macaulay and Gorenstein tangential varieties of the Segre–Veronese varieties*, arXiv:2012.14476 (2020), Introduction and Theorem 3.10.
