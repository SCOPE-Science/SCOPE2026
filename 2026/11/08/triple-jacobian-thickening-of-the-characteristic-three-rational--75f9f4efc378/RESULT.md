# Triple Jacobian thickening of the characteristic-three rational-normal-quartic tangent surface

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). The tangent developable \(T\subset\mathbf P^4_k\) of the rational normal quartic
\[
\Gamma=\{[s^4:s^3t:s^2t^2:st^3:t^4]:[s:t]\in\mathbf P^1\}
\]
is the reduced complete intersection of
\[
Q=X_0X_4-X_1X_3,\qquad C=X_2^3+X_1^2X_4+X_0X_3^2.
\]
Let \(J\) be the scheme-theoretic singular locus defined on \(T\) by the maximal minors of the \(2\times5\) Jacobian of \((Q,C)\), together with \((Q,C)\). Then \(J_{\mathrm{red}}=\Gamma\), and the natural projection \(\pi:J\to\Gamma\cong\mathbf P^1\) identifies its sheaf of algebras with
\[
\boxed{\pi_*\mathcal O_J\cong \mathcal O_{\mathbf P^1}\oplus\mathcal O_{\mathbf P^1}(-4)\varepsilon\oplus\mathcal O_{\mathbf P^1}(-8)\varepsilon^2,\quad\varepsilon^3=0,}
\]
where multiplication is that of the truncated symmetric algebra on \(\mathcal O_{\mathbf P^1}(-4)\). Thus \(J\) is a **split curvilinear triple structure** on \(\Gamma\), not merely a multiplicity-three cycle. Its embedded hyperplane bundle is \(\mathcal O_J(1)=\pi^*\mathcal O_{\mathbf P^1}(4)\), and
\[
\boxed{\deg J=12,\qquad P_J(m)=12m-9,\qquad p_a(J)=10.}
\]
For integers \(m\ge0\), its sheaf cohomology satisfies
\[
\boxed{h^0(J,\mathcal O_J(m))=\sum_{j=0}^2\max\{4m-4j+1,0\}.}
\]
The last equality concerns global sections of the *sheaf* on \(J\), not necessarily the degree-\(m\) component of its homogeneous coordinate ring.

## Assumptions and scope

All equations and Jacobian schemes are taken over the algebraically closed field \(k\) with \(\operatorname{char}k=3\); the same equations and gluing work before algebraic closure. “Tangent developable” means the reduced scheme underlying the union of projective embedded tangent lines to the displayed Veronese image, not the scheme-theoretic image of an unspecified map. The singular scheme is the standard Fitting/Jacobian singular subscheme of the codimension-two complete intersection. Degree and arithmetic genus refer to this nonreduced projective one-dimensional singular scheme.

The complete-intersection description is included for explicit identification of the object; it is not advanced as an independently novel fact, in light of the broad tangential-variety Gorenstein and syzygy theorems in the cited work of Aprodu and collaborators. The assessed new statement is the complete **global scheme structure of \(J\)** and the resulting characteristic-three invariants.

## Proof

**1. Identify the tangent developable.** On the chart \(X_0\ne0\), put the affine Veronese parameter \(t\) and tangent parameter \(u\). In characteristic three a point on the tangent line has coordinates
\[
[1:t+u:t^2-tu:t^3:t^4+ut^3].
\]
Direct substitution gives \(Q=C=0\). Conversely, eliminate \(X_4\) by \(Q\) and introduce the triangular coordinates
\[
a=X_1/X_0,\quad z=X_2/X_0-a^2,\quad y=X_3/X_0-a^3.
\]
The second defining equation becomes exactly
\[
C|_{Q=0}=y^2+z^3.
\]
The above tangent parametrization satisfies \(z=-u^2\), \(y=-u^3\), and \(t=a-u\). Over an algebraically closed field the cusp \(y^2+z^3=0\) is the image of this parametrization, so it is precisely the tangent surface on \(X_0\ne0\). This affine hypersurface is reduced and integral.

The intersection of \(V(Q,C)\) with the hyperplane \(X_0=0\) has dimension one: \(Q\) becomes \(-X_1X_3\), while \(C\) becomes \(X_2^3+X_1^2X_4\). Hence there is no additional two-dimensional component supported in that hyperplane. The two equations form a codimension-two complete intersection and thus are Cohen–Macaulay and unmixed; generic reducedness on the dense integral chart implies reducedness throughout. The projective reduced tangent surface therefore equals \(V(Q,C)\) scheme-theoretically.

**2. Compute the singular scheme on the first chart.** Because elimination of \(Q\) gives the hypersurface equation \(f=y^2+z^3\) with free coordinate \(a\), its singular scheme is
\[
(f,\partial f/\partial y,\partial f/\partial z)=(y,z^3)
\]
in characteristic three. In particular its coordinate algebra on \(X_0\ne0\) is \(k[a,z]/(z^3)\), and the reduced subscheme there is the rational normal quartic \(y=z=0\).

**3. The second chart and the exceptional hyperplane.** On \(X_4\ne0\) eliminate \(X_0\) by \(Q\), and set
\[
b=X_3/X_4,\quad z'=X_2/X_4-b^2,\quad y'=X_1/X_4-b^3.
\]
Again \(C|_{Q=0}=y'^2+z'^3\), so the singular scheme on this chart is \(k[b,z']/(z'^3)\). If \(X_0=X_4=0\), the defining equations force \(X_2=0\) and \(X_1X_3=0\), leaving only the points \([0:1:0:0:0]\) and \([0:0:0:1:0]\). At each the gradients of \(Q\) and \(C\) are independent; both points are smooth. Thus the two affine cusp charts cover all of \(J\).

**4. Determine the global algebra, not just its cycle.** On \(J\cap\{X_0\ne0\}\), the equations \(y=0\) and \(Q=0\) give \(X_3/X_0=a^3\), \(X_4/X_0=a^4\), \(X_2/X_0=a^2+z\). In the overlap with \(X_4\ne0\), this yields exactly
\[
b=a^{-1},\qquad z'=a^{-4}z.
\]
Consequently \(z\) is a local generator of \(\mathcal O_{\mathbf P^1}(-4)\), its square generates \(\mathcal O_{\mathbf P^1}(-8)\), and \(z^3=0\) globally. There are no higher-order correction terms in the transition; this proves the asserted *split* algebra isomorphism. Since the homogeneous coordinate functions \(X_0\) and \(X_4\) on the reduced curve transform by \(X_4/X_0=a^4\), the hyperplane bundle on the finite thickening equals \(\pi^*\mathcal O_{\mathbf P^1}(4)\).

**5. Compute invariants.** Finiteness of \(\pi\), the direct-sum decomposition, and Riemann–Roch on \(\mathbf P^1\) give for every integer \(m\):
\[
\chi(J,\mathcal O_J(m))=\sum_{j=0}^2(4m-4j+1)=12m-9.
\]
Thus the degree is \(12\) and \(p_a(J)=1-\chi(\mathcal O_J)=10\). Summing \(h^0(\mathbf P^1,\mathcal O(4m-4j))\) proves the displayed global-section formula.

## Verification

The accompanying `verify.py` is a standalone Python standard-library checker. It recomputes the tangent equations, both affine cusp reductions, the nilpotent-coordinate transition, and the nonvanishing Jacobian ranks at the two exceptional points, directly over \(\mathbb F_3\). It also checks the independent degree-two and degree-three parameterized polynomial ranks (\(14\) and \(29\)), and displays the Euler characteristics and sheaf-global-section values for twists \(0\) through \(5\). `verification_output.txt` is an actual successful execution output terminating in `VERIFY_OK`.

The finite rank calculations **do not** establish the general projective assertions by themselves. The complete-intersection argument, exact chart identifications, transition functions, and sheaf Euler characteristic in the proof establish the statements for every algebraically closed field of characteristic three.

## Relationship to prior work

Chipalkatti (arXiv:math/0110224, first publicly posted 2001-10-19) and Kurmann (arXiv:1108.4532, first posted 2011-08-23) study equations and singular loci of coincident-root varieties in characteristic-zero binary-form settings. Their statements do not supply the characteristic-three Jacobian scheme of the specific *tangent developable* considered here. The binary-form coincident-root formulation should not be transferred without checking the noninvertible binomial coefficients in characteristic three.

Aprodu–Farkas–Papadima–Raicu–Weyman (arXiv:1810.11635, 2018) prove a strong general theorem: the tangential variety of a rational normal curve in characteristic different from two has a Gorenstein homogeneous coordinate ring of regularity three (Theorem 5.1), and give a jet-bundle normalization construction (Section 5.4). The degree-four complete-intersection presentation is compatible with and largely subsumed by those results. The present claim instead specifies the **Jacobian singular subscheme**, including the global nilpotent gluing and genus. Neither that exact scheme nor its characteristic-three Hilbert polynomial is supplied in the inspected relevant sections. Related published mathematical records on singular Hadamard quartics, Gibbs cubics, and Fano schemes concern different embedded objects and do not imply the claimed scheme structure.

## Limitations

This gives an explicit singular subscheme of this one tangential surface, not a general classification of singular schemes of all tangential varieties or a new syzygy theorem. The full homogeneous graded Hilbert function of the saturated Jacobian ideal is not claimed: the displayed \(h^0\) formula is for the associated sheaf. Independent external evaluation and historical-priority verification remain outstanding. Park (2022) was checked through its publicly accessible original full-text introduction, central geometry and proof sections; its stated syzygy theorems do not calculate this Jacobian singular scheme. Unlocated specialist sources could still contain an equivalent description.

## References

1. J. V. Chipalkatti, *On equations defining coincident root loci*, arXiv:math/0110224 (2001), https://arxiv.org/abs/math/0110224.
2. S. Kurmann, *Some remarks on equations defining coincident root loci*, arXiv:1108.4532 (2011), https://arxiv.org/abs/1108.4532.
3. M. Aprodu, G. Farkas, Ş. Papadima, C. Raicu, and J. Weyman, *Koszul modules and Green's conjecture*, arXiv:1810.11635 (2018), https://arxiv.org/abs/1810.11635.
4. J. Park, *Syzygies of tangent developable surfaces and K3 carpets via secant varieties*, arXiv:2212.07584 (2022), https://arxiv.org/abs/2212.07584 (relevant full-text sections inspected).
