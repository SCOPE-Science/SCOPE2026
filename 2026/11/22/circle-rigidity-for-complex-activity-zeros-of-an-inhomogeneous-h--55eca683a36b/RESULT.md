# Circle rigidity for complex activity zeros of an inhomogeneous hard-core cycle

## Finding

Let \(n\ge2\). On the cyclic hard-core gas \(C_{2n}\), give each even vertex activity \(z\in\mathbb C\), and give odd vertex \(2j+1\) an arbitrary positive activity \(b_j>0\) for \(j\in\mathbb Z/n\mathbb Z\). The partition polynomial is
\[
P_n(z)=\sum_{I\subseteq V(C_{2n})\atop I\text{ independent}}z^{|I\cap E|}\prod_{2j+1\in I}b_j,\qquad E=\{0,2,\ldots,2n-2\}.
\]
**Theorem (circle rigidity).** All \(n\) complex zeros of \(P_n\), counted with multiplicity, have the same absolute value if and only if
\[
b_j=b_{j+2}\quad \text{for every }j\in\mathbb Z/n\mathbb Z.
\]
Thus odd \(n\) forces homogeneous background activity; even \(n\) admits arbitrary, possibly unequal, alternating background activities. Whenever this criterion holds, **all zeros are simple** and lie on the circle of radius
\[
R=\left(\prod_{j=0}^{n-1}(1+b_j)\right)^{1/n}.
\]

The following explicit factorizations give every zero. If \(n=2m\) and \(b_{2j}=b\), \(b_{2j+1}=c\), set \(R=\sqrt{(1+b)(1+c)}\). Then
\[
P_{2m}(z)=\prod_{k=0}^{m-1}\left[z^2+\left(2-2\sqrt{bc}\cos\frac{(2k+1)\pi}{2m}\right)z+R^2\right].
\]
If \(n=2m+1\) and every \(b_j=b\), set \(R=1+b\). Then
\[
P_{2m+1}(z)=(z+R)\prod_{k=0}^{m-1}\left[z^2+\left(2R-4b\cos^2\frac{(2k+1)\pi}{2(2m+1)}\right)z+R^2\right].
\]
In particular, for even \(n\) and unequal alternating backgrounds \(b\ne c\), neither \(R\) nor \(-R\) is a zero and the angular root arcs avoid the negative-real direction by a positive gap uniformly as \(n\to\infty\) at fixed \(b,c\).

## Assumptions and scope

The cycle \(C_{2n}\) is a simple graph, including \(C_4\) at \(n=2\). The odd-vertex activities are strictly positive and fixed independently of the common complex even-vertex activity. Indices of the positive activities are taken modulo \(n\). “All zeros on a circle” means one circle centered at the complex origin, not an arbitrary translated circle. The statements involve finite-volume partition-polynomial zeros, not a claim of a nonanalytic finite-temperature free energy.

## Proof

**1. Transfer representation and two extreme coefficients.** Put \(w_j=1+b_j\). Summing independently over odd vertices after selecting even occupied vertices gives a two-state transfer matrix:
\[
M_j(z)=\begin{pmatrix}w_j&1\\ z&z\end{pmatrix},\qquad P_n(z)=\operatorname{tr}\bigl(M_0(z)M_1(z)\cdots M_{n-1}(z)\bigr).
\]
Equivalently, selecting no even vertices leaves all odd vertices free; selecting one even vertex blocks its two adjacent odd vertices; selecting all but one even vertex blocks every odd vertex. Hence
\[
P_n(z)=z^n+nz^{n-1}+\cdots+c_1z+c_0,
\]
\[
c_0=\prod_{j=0}^{n-1}w_j=R^n,\qquad c_1=R^n\sum_{j=0}^{n-1}\frac1{w_{j-1}w_j}.
\]
The displayed \(z^{n-1}\) coefficient identity also holds for \(n=2\), when it coincides with \(c_1\).

**2. A coefficient obstruction proves necessity.** Suppose all complex roots \(\zeta_k\) satisfy \(|\zeta_k|=r\). The constant coefficient gives \(r^n=c_0=R^n\), so \(r=R\). Because the polynomial is real and monic with positive constant coefficient, its multiset of roots is invariant under \(\zeta\mapsto R^2/\zeta=\overline\zeta\). Therefore
\[
\frac{c_1}{c_0}=-\sum_{k=1}^n\frac1{\zeta_k}
=-\frac1{R^2}\sum_{k=1}^n\overline{\zeta_k}
=\frac{n}{R^2},
\]
where the last equality uses \(\sum_k\zeta_k=-n\). Consequently
\[
\frac1n\sum_{j=0}^{n-1}\frac{R^2}{w_{j-1}w_j}=1.
\]
The product of the \(n\) strictly positive summands is \(1\), since \(\prod_j(w_{j-1}w_j)=R^{2n}\). Equality in the arithmetic–geometric mean inequality forces every summand to equal \(1\): \(w_{j-1}w_j=R^2\) for all \(j\). Dividing adjacent identities gives \(w_{j+1}=w_{j-1}\), equivalently \(b_{j+2}=b_j\). This also proves a **strict obstruction**: if the activities are not two-periodic, then \(c_1>nR^{n-2}\), so root-circle equality is impossible.

**3. Sufficiency for even \(n\).** Write \(n=2m\) and alternate \(b,c\). The product \(K(z)=M_b(z)M_c(z)\) satisfies
\[
\operatorname{tr}K=z^2+2z+R^2,\qquad \det K=bc\,z^2.
\]
Since \(P_{2m}=\operatorname{tr}(K^m)\), the identity expressing a two-eigenvalue power sum as a product over the \(m\) angles \((2k+1)\pi/(2m)\) gives the displayed quadratic factorization. For each angle its real linear coefficient \(a_k=2-2\sqrt{bc}\cos\theta_k\) obeys
\[
-2R<a_k<2R,
\]
because \(R=\sqrt{(1+b)(1+c)}\ge1+\sqrt{bc}\) and \(-1<\cos\theta_k<1\). Thus each quadratic has a nonreal conjugate root pair of modulus \(R\). Their coefficients \(a_k\) are pairwise distinct because the cosines are distinct, so different quadratics have disjoint root sets. All \(n\) roots are therefore simple on \(|z|=R\).

**4. Sufficiency for odd \(n\).** Two-periodicity with odd \(n=2m+1\) forces all backgrounds equal to \(b\). Here \(P_n=\operatorname{tr}(M_b^n)\), \(\operatorname{tr}M_b=z+R\), and \(\det M_b=bz\). The analogous power-sum factorization gives the displayed factor \(z+R\) and \(m\) quadratics. For every listed angle \(0<\theta_k<\pi/2\), the quadratic coefficient obeys \(-2R<2R-4b\cos^2\theta_k<2R\), because \(R=1+b>b\) and \(\cos^2\theta_k<1\). Their roots are nonreal conjugates of modulus \(R\), and distinct angles give distinct factors. The sole real root is \(-R\), also simple.

**5. A genuine alternating-background zero gap.** In the even case, writing roots \(z=Re^{\pm i\varphi}\) gives
\[
\cos\varphi=\frac{\sqrt{bc}\cos\theta_k-1}{R}.
\]
For fixed unequal \(b,c>0\), \(R>1+\sqrt{bc}\), so the cosine is uniformly strictly between \(-1\) and \(1\) for all \(k,m\); hence finite-volume roots avoid both real radial endpoints uniformly in circumference. This supplies a persistent angular gap not present at homogeneous background activity \(b=c\), where the limiting arc reaches \(-R\).

## Verification

The standalone script `verify_circle.py` (Python standard library only) independently computes the complete independent-set polynomial by configuration enumeration on small cycles and compares it to the transfer product exactly. It also checks the extreme coefficients, complex factor-root residuals and modulus, and the strict coefficient obstruction over thousands of inhomogeneous integer background samples. The checked script reports `VERIFIED 9965 exact transfer/coefficient, root-modulus, and rigidity-witness cases`. These finite checks corroborate, but do not replace, the preceding all-\(n\) algebraic proof.

To reproduce, in the same directory run `python3 verify_circle.py`.

## Relationship to prior work

Heilmann–Lieb real-negative-zero results apply to the monomer–dimer matching polynomial, and later claw-free results concern a single activity shared by **all** vertices. The present polynomial instead varies the complex activity only on one bipartite shore, while allowing arbitrary fixed positive fugacities on the other shore; even a homogeneous background yields complex conjugate root pairs rather than the usual all-negative-real statement.

Lebowitz, Ruelle and Speer (2012) study Lee–Yang zero locations in Ising systems and certain hard-object limits; their located results give zero-free/real-root properties, not an iff characterization for arbitrary inhomogeneous backgrounds on even hard-core cycles. Jerrum and Patel (2026), Section 5.1, explicitly analyze the alternating two-activity cycle via a two-state transfer matrix and provide related zero-free-region constructions. Their identical-activity-on-each-shore setting already supplies the transfer basis for the homogeneous-background special case; the claim here is the **converse rigidity over every positive background activity vector**, the precise allowance of nonuniform alternating backgrounds, and the complete simple-root factorizations in both parities. No new general transfer-matrix formalism is claimed.

## Limitations

No external independent audit has been performed. Although relevant source passages and directly comparable published results were inspected, an unindexed earlier statement of the same sharp rigidity characterization cannot be categorically excluded. The field variable is constrained to be common on one shore, while the other shore remains strictly positive; arbitrary signed or complex background activities, general bipartite graphs, and translated root circles are not covered. No general thermodynamic phase-transition theorem is asserted.

## References

- J. L. Lebowitz, D. Ruelle and E. R. Speer, “Location of the Lee–Yang zeros and absence of phase transitions in some Ising spin systems,” arXiv:1204.0558 (first public version 2 April 2012), https://arxiv.org/abs/1204.0558 .
- M. Jerrum and V. Patel, “Zero-free regions for the independence polynomial on restricted graph classes,” *Journal of the London Mathematical Society* 113 (2026), e70458, Section 5.1, https://doi.org/10.1112/jlms.70458 .
- O. J. Heilmann and E. H. Lieb, “Theory of monomer-dimer systems,” *Communications in Mathematical Physics* 25 (1972), 190–232, cited for historical context and not for the present inhomogeneous rigidity theorem.
