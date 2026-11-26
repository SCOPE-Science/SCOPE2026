# The singular curve and transverse A-type of odd transvectant complete intersections

## Finding
For each integer \(p\ge2\), put \(r=2p+3\) and let \(V=\operatorname{Sym}^r\mathbb C^2\). Let \(C_r=\{[\ell^r]:0\ne\ell\in\mathbb C^2\}\subset\mathbb P(V)\) be the rational normal curve. Define \(X_p\subset\mathbb P(V)\) by the three coefficients of the binary quadratic \((f,f)_{r-1}\). Massri's Theorem 1.1 identifies this scheme with the quadratic hull of the \(p\)-th osculating variety and proves it is an integral complete intersection of three quadrics [1].

The reduced singular support of \(X_p\) is exactly \(C_r\). At each point of \(C_r\) the completed complex analytic germ is a product of a smooth curve and a transverse \(A_{p+1}\) singularity, with normal form
\[
\mathbb C[[u,z_1,\ldots,z_{2p-1},t]]/\bigl(z_1^2+\cdots+z_{2p-1}^2+t^{p+2}\bigr).
\]
Consequently the Jacobian singular scheme (the Fitting scheme of the cotangent module on this local complete intersection) has completed local ring \(\mathbb C[[u,t]]/(t^{p+1})\). The scheme is a curvilinear thickening of multiplicity \(p+1\) along \(C_r\), and its fundamental one-cycle has degree \((p+1)(2p+3)\).

## Assumptions and scope
The ground field is \(\mathbb C\); all statements are scheme-theoretic except where reduced support is explicitly stated. Here \((f,f)_{r-1}\) is the classical even transvectant, defined up to a nonzero scalar, and hence its zero scheme is unambiguous. The singular scheme means the maximal-minor Jacobian/Fitting ideal for the complete intersection; the multiplicity is at the generic point of \(C_r\). All integers \(p\ge2\) are covered, and only the subfamily \(r=2p+3\) is asserted.

## Proof
**1. Singular support via the moment map.** Because \(r\) is odd, the top apolar pairing
\[\omega:\operatorname{Sym}^r\mathbb C^2\times\operatorname{Sym}^r\mathbb C^2\longrightarrow\mathbb C\]
is a nondegenerate alternating \(SL_2\)-invariant form. For \(\xi\in\mathfrak{sl}_2\), define \(\langle\mu(f),\xi\rangle=\tfrac12\omega(\xi f,f)\). By the multiplicity-one Clebsch–Gordan decomposition, \(\mu\) is, up to an invertible change of three coordinates, the triple of coefficients of \((f,f)_{r-1}\). Hence the affine cone over \(X_p\) is the zero fibre of \(\mu\). Differentiation and infinitesimal symplectic invariance give
\[\langle d\mu_f(v),\xi\rangle=\omega(\xi f,v).\]
Nondegeneracy of \(\omega\) shows that \(d\mu_f\) has rank less than three precisely when some nonzero \(\xi\in\mathfrak{sl}_2\) annihilates \(f\). A nonzero semisimple \(\xi\) has no zero eigenvalue on \(\operatorname{Sym}^r\mathbb C^2\), since the weights \(r,r-2,\ldots,-r\) are all odd. A nonzero nilpotent is conjugate to \(x\partial_y\), whose kernel is the line \(\mathbb C x^r\). Thus the rank-deficiency set in projective space is precisely \(C_r\). Pure powers satisfy all the transvectants. As the three quadrics form a regular sequence by [1], the Jacobian criterion proves \(\operatorname{Sing}(X_p)_{\mathrm{red}}=C_r\).

**2. Equations in a transverse slice.** Fix \([x^r]\) and write
\[f=\sum_{i=0}^{r}\binom{r}{i}a_i x^{r-i}y^i,\qquad a_0=1.\]
The one-parameter unipotent orbit through \([x^r]\) is transverse to the slice \(a_1=0\): near the point, an analytic change of coordinates splits off the smooth orbit coordinate \(u\). Put \(k=r-1\). A nonzero normalization of the three transvectant coefficients is
\[
\begin{aligned}
q_0&=\sum_{i=0}^k(-1)^i\binom{k}{i}a_i a_{k-i},\\
q_1&=\sum_{i=0}^k(-1)^i\binom{k}{i}(a_i a_{k-i+1}+a_{i+1}a_{k-i}),\\
q_2&=\sum_{i=0}^k(-1)^i\binom{k}{i}a_{i+1}a_{k-i+1}.
\end{aligned}
\]
With \(a_0=1,a_1=0\), the first two equations have independent linear terms \(2a_{r-1}\) and \(2a_r\). Eliminate these variables by the formal implicit-function theorem. The third equation becomes a convergent polynomial hypersurface equation
\[F(a_2,a_3,\ldots,a_{r-2})=0.\]
Every monomial of \(F\) has weighted degree \(r+1\) when \(\operatorname{wt}(a_i)=i\), because every monomial of \(q_j\) has index sum \(r-1+j\) and the eliminated variable \(a_{r-1}\) is replaced by monomials of the same weight.

**3. Transverse quadratic rank.** Let \(t=a_2\) and \(z=(a_3,\ldots,a_{r-2})\). The quadratic part of \(F\) in the variables \(z\) is, up to a nonzero overall scalar,
\[
Q(z)=\sum_{i=3}^{r-2}(-1)^{i-1}\binom{r-1}{i-1}a_i a_{r+1-i}.
\]
Its symmetric matrix is antidiagonal, all its antidiagonal entries are nonzero in characteristic zero, and its rank is \(r-4=2p-1\). The only quadratic kernel direction is \(t\), because \(2+(r-1)=r+1\) and \(a_{r-1}\) was eliminated. By the analytic Morse lemma with parameter \(t\), the reduced slice equation is analytically equivalent to \(z_1^2+\cdots+z_{r-4}^2+g(t)\), where \(g\) is the critical value obtained by the unique solution of \(\partial F/\partial z_i=0\) near the origin.

**4. Exact exponent and nonvanishing.** The weighted \(\mathbb C^*\)-action \(a_i\mapsto\lambda^i a_i\) preserves \(F\). Uniqueness of the transverse critical section forces it to be equivariant, so \(g(\lambda^2 t)=\lambda^{r+1}g(t)\). Therefore \(g(t)=c t^{(r+1)/2}=c t^{p+2}\). If \(c=0\), the split hypersurface would be singular along the entire formal \(t\)-axis in the transverse slice. But Step 1 shows that the only singular point on the slice near \([x^r]\) is \([x^r]\) itself: a pure power with \(a_0=1\) and \(a_1=0\) must equal \(x^r\). Thus \(c\ne0\). Rescaling coordinates gives the asserted \(A_{p+1}\) normal form.

**5. Jacobian thickness and globality.** The partial derivatives of the local equation force \(z_1=\cdots=z_{r-4}=t^{p+1}=0\); the equation itself then vanishes. The smooth orbit coordinate \(u\) is free, giving \(\mathbb C[[u,t]]/(t^{p+1})\). Transitivity of \(SL_2(\mathbb C)\) on \(C_r\) transports this calculation to every point. Since \(C_r\) has degree \(r\), the singular cycle has degree \(r(p+1)\).

## Verification
The dependency-free script `verify.py` reconstructs the three transvectant coefficients with exact rational arithmetic; eliminates the two pivot variables on the indicated slice; confirms weighted homogeneity and nonzero transverse quadratic determinant for \(r=5,7,9,11,13,15\); and directly verifies the critical-point equations and the nonzero critical coefficients for \(r=5,7,9\). For the first non-boundary member \(r=7\), the critical value is \(405t^4\); for \(r=9\), it is \(8960t^5\), in the script's normalization. Executing `python3 verify.py` prints `CERTIFICATE_OK`. These finite checks support, but do not replace, the all-parameter argument above.

## Relationship to prior work
Massri [1], Theorem 1.1 and Proposition 6.1, establishes the exact three-quadric complete-intersection and integrality properties for this subfamily, including a nondegenerate quadratic tangent-cone description at a highest weight point. Massri [2], Theorem 12, studies the same zero loci and observes that the pure-power rational normal curve is singular, but does not give the converse or the analytic types. The present assertion additionally identifies the *entire* singular support, the exact transverse \(A_{p+1}\) analytic class, and the multiplicity of its Jacobian scheme. Classical properties of \(SL_2\) moment maps and the analytic Morse lemma are used as standard tools rather than claimed as new. The related [3] addresses irreducibility of quadratic hulls; its full latest text could not be inspected, so some historical-priority risk remains.

## Limitations
No claim is made about non-minimal quadratic hulls \(r>2p+3\), positive characteristic, global vector-bundle structure of the Jacobian thickening, or independent validation. The completed local analytic proof is specific to the odd-degree, three-equation case. Exhaustive historical priority across all equivalent moment-map formulations has not been established.

## References
[1] C. Massri, *Quadratic hulls of osculating varieties of rational normal curves*, arXiv:2610.28499v1 (first public 2026-10-20), Theorem 1.1, Sections 2–6. https://arxiv.org/abs/2610.28499

[2] C. Massri, *Quadratic equations of projective PGL2(C)-varieties*, J. Math. Comput. Sci. 3 (2013), 808–822, arXiv:1105.0724v3. https://arxiv.org/abs/1105.0724

[3] C. Massri, *Irreducibility of quadratic hulls of osculating varieties of closed orbits*, arXiv:1202.5531 (revised 2026). https://arxiv.org/abs/1202.5531
