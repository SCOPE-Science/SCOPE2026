# All-degree dihedral resonances and quadratic reopening of two-equator harmonic traces

## Finding

Fix an integer \(d\ge4\) and consider complex homogeneous spherical harmonics of one exact degree \(\ell\ge0\) on \(S^{d-1}\). Let \(E_0\) and \(E_\theta\) be distinct great equators sharing a common \(S^{d-3}\), with angle \(0<\theta<\pi\) between their normal directions. Define the average squared trace-concentration operator \(T_\ell(\theta)\) as in the next section.

**Theorem.** If \(\theta/\pi\) is irrational, \(T_\ell(\theta)\) is positive definite for every \(\ell\). If \(\theta/\pi=p/q\) is in lowest terms, \(q\ge2\), its nullity is exactly
\[
N_{d,\ell}(q)=\sum_{j=1}^{\lfloor\ell/q\rfloor}\binom{\ell-jq+d-3}{d-3},\qquad
\sum_{\ell\ge0}N_{d,\ell}(q)t^\ell=\frac{t^q}{(1-t^q)(1-t)^{d-2}}.
\]
The first invisible degree is exactly \(q\), with a one-dimensional nullspace; for fixed \(d,q\), the invisible fraction approaches \(1/(2q)\) as \(\ell\) tends to infinity. At any resonant angle \(\theta_0=p\pi/q\), precisely \(N_{d,\ell}(q)\) eigenvalues of \(T_\ell(\theta)\) vanish at the *quadratic* rate \(\Theta((\theta-\theta_0)^2)\), all remaining eigenvalues stay positive, and
\[
\operatorname{ord}_{\theta=\theta_0}\det T_\ell(\theta)=2N_{d,\ell}(q).
\]
This is a finite-degree analytic assertion; the determinant is taken in any fixed orthonormal basis.

Irrational injectivity is never uniformly stable over degrees. For every integer \(L\ge2\),
\[
\min_{1\le m\le L}\lambda_{\min}(T_m(\theta))
\le\frac{\pi^2d}{2(d-1)L^2}.
\]
This last inequality also holds for rational angles, where some degrees have exact zeros.

## Assumptions and scope

Use coordinates \((x_1,x_2,y)\in\mathbb R^2\times\mathbb R^{d-2}\). In polar normal coordinates, let \(x_1+ix_2=\rho e^{i\phi}\). The great equator \(E_\psi\) consists of points with \((x_1,x_2)=s(\cos\psi,\sin\psi)\), \(-1\le s\le1\); equivalently, its defining normal is \((-\sin\psi,\cos\psi,0)\). Both equators receive their own normalized rotation-invariant probability measure. Let \(\mathcal H_{d,\ell}\) be the complex vector space of restrictions of homogeneous polynomials of degree \(\ell\) annihilated by the Euclidean Laplacian. Equip it with the normalized sphere \(L^2\) inner product. The trace \(R_\psi:\mathcal H_{d,\ell}\to L^2(E_\psi)\) is ordinary restriction; then
\[
T_\ell(\theta)=\tfrac12(R_0^*R_0+R_\theta^*R_\theta).
\]
All assertions concern continuous traces of **pure exact-degree spherical harmonics**, not discrete sampling or arbitrary mixed-degree bands. Angles are distinct modulo \(\pi\), so coinciding equators are excluded. The binomial convention is zero when the upper argument is below the lower one.

## Proof

**Reflection principle.** If a harmonic polynomial vanishes on a hyperplane, it is odd under reflection in that hyperplane. For a normal coordinate \(s\) write the polynomial \(P(s,y)=\sum_{k\ge0}s^ka_k(y)\). The Laplace equation yields \((k+2)(k+1)a_{k+2}+\Delta_y a_k=0\). Vanishing at \(s=0\) gives \(a_0=0\), hence all even coefficients vanish. The converse is immediate. Nonzero polynomial trace vanishes in \(L^2\) exactly when it vanishes everywhere on that equator.

**Dihedral condition.** If both traces vanish, the polynomial is odd under the two equatorial reflections, hence invariant under their product, rotation by \(2\theta\) in the normal two-plane. When \(\theta/\pi\) is irrational, polynomial rotational invariance extends to the full circle; it is incompatible with being odd under either reflection. Thus the trace pair is injective. When \(\theta=p\pi/q\), the relevant anti-invariant polynomials are those whose planar angular frequencies are positive integer multiples of \(q\).

**Multiplicity.** The subspace \(K_0=\ker R_0\) decomposes into the mutually independent sine Fourier angular frequencies \(m\in\{1,\ldots,\ell\}\). The homogeneous degree-\(\ell\) harmonic multiplicity of frequency \(m\) in the sine sector is exactly
\[
h_{d,\ell,m}=\binom{\ell-m+d-3}{d-3}.
\]
Indeed, before imposing harmonicity, the degree generating function is \(t^m/[(1-t^2)(1-t)^{d-2}]\): one factor \(t^m\) for the angular mode, arbitrary powers of the planar radius squared, and arbitrary transverse coordinate monomials. The equivariant Fischer decomposition removes the factor \(1/(1-t^2)\), leaving \(t^m/(1-t)^{d-2}\). The second trace vanishes on a frequency exactly when \(\sin(m\theta)=0\), giving the stated sum and generating function. Standard binomial asymptotics give \(N_{d,\ell}(q)\sim\ell^{d-2}/[q(d-2)!]\) and \(\dim\mathcal H_{d,\ell}\sim2\ell^{d-2}/(d-2)!\).

**Quadratic reopening and determinant order.** Parameterize all equator traces on the fixed standard equator by rotating coordinates, so their target Hilbert space does not vary with angle. On \(K_0\), the second trace has a fixed injective map \(B\), applied to the diagonal sine-frequency multiplier \(D_\theta\), with the \(m\)-block multiplied by \(\sin(m\theta)\). To see that \(B\) is injective, choose any irrational reference angle \(\alpha/\pi\): both the full two-equator trace and \(D_\alpha\) are injective, so \(B\) must be injective. In finite dimension decompose \(\mathcal H_{d,\ell}=K_0\oplus K_0^\perp\). Since \(R_0\) is injective on the complement, its trace norm controls the complementary component. Boundedness of the rotated second trace and the uniform lower bound of the fixed injective \(B\) show that, for \(\theta\) near \(\theta_0\), the energy
\[
2\langle T_\ell(\theta)(k+e),k+e\rangle
=\|R_0e\|^2+\|R_\theta e+BD_\theta k\|^2
\]
is bounded above and below by fixed positive multiples of \(\|e\|^2+\|D_\theta k\|^2\). Consequently, exactly the \(N_{d,\ell}(q)\) sine-frequency blocks with \(q\mid m\) have singular values proportional to \(\lvert\theta-\theta_0\rvert\), since their sine factors have simple zeros; every other block stays nonzero. The min–max principle gives quadratic eigenvalue reopening. The trace matrix is analytic in \(\theta\) (its entries are finite polynomial sphere moments), so the determinant has precisely twice the nullity as its order of vanishing.

**No degree-uniform stability.** The harmonic polynomial \(P_m(x)=\operatorname{Im}(x_1+ix_2)^m\) vanishes on \(E_0\), so its exact Rayleigh quotient is
\[
\frac{\langle T_m(\theta)P_m,P_m\rangle}{\|P_m\|^2}
=c_{d,m}\sin^2(m\theta),\quad
c_{d,m}=\frac{(1/2)_m(d/2)_m}{(1)_m((d-1)/2)_m}.
\]
Here \((a)_m\) is the rising factorial. The formula follows by integrating the planar harmonic over the normalized sphere and equator: their angular sine-square averages are one half, with radial even moments \((1)_m/(d/2)_m\) and \((1/2)_m/((d-1)/2)_m\), respectively. The coefficient decreases with \(m\ge1\), so \(c_{d,m}\le c_{d,1}=d/[2(d-1)]\). Dirichlet's elementary approximation lemma supplies an integer \(1\le m\le L\) with \(\operatorname{dist}(m\theta/\pi,\mathbb Z)\le1/L\). The variational bound and \(\lvert\sin(\pi u)\rvert\le\pi\operatorname{dist}(u,\mathbb Z)\) prove the claimed instability inequality.

## Verification

Two standalone ordinary-Python scripts accompany this manuscript. `verify_two_equators.py` constructs exact harmonic spaces by Laplacian nullspaces, restricts to the two equatorial hyperplanes, and compares observed rational-angle ranks to the binomial formula in 200 independent dimension/degree/angle cases. `verify_resonant_splitting.py` builds the full degree-three Gram matrix from normalized quadrature in dimension four, checks exact resonant nullities at angles \(\pi/2\) and \(\pi/3\), and confirms numerically that their disappearing eigenvalues scale quadratically with angular detuning. Both scripts were run successfully. Their finite computations corroborate, but do not replace, the all-dimensional proof.

## Relationship to prior work

The general spherical-harmonic reconstruction setting appears in Zandieh–Han–Avron (2022). Rigat–Wielonsky (2023) established an irrational/rational angular dichotomy for certain planar Fourier uniqueness pairs, a different trace operator and a distinct function class. Previously published two-equator results identify the quadratic and cubic low-degree exceptional angles, and two-meridian spherical sampling studies cover the two-sphere setting. Those cases are consistent with the present exact nullity formula, but the asserted combination of all degrees in ambient dimension at least four, explicit nullity generating series, and exact Gram-determinant vanishing order is not supplied by the inspected claims. Angular sine decompositions, Fischer decomposition, and dihedral invariant techniques are standard and are not independently claimed as new.

## Limitations

The theorem does not compute the positive eigenvalues, prove optimal angular placement, extend to curved or non-great observation hypersurfaces, or provide uniform stable inversion as the degree grows. Its determinant-order assertion holds at fixed harmonic degree; no joint high-degree/angular-limit equivalence is asserted. Related specialist papers not retrievable in full leave residual historical-priority uncertainty. Independent external verification is not claimed.

## References

1. M. Zandieh, I. Han, and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, first public version February 25, 2022, https://arxiv.org/abs/2202.12995.
2. F. Rigat and F. Wielonsky, *Boundary value problems and Heisenberg uniqueness pairs*, first public version April 5, 2023, https://arxiv.org/abs/2304.02318.
3. *Sharp two-equator frames for quadratic spherical harmonics: generic injectivity and an optimal oblique angle*, published research summary, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-equator-frames-for-quadratic-spherical-harmonics-gener--f1a2fb2e4db0.
4. *Two-equator tomography of cubic spherical harmonics: the 60- and 90-degree blind-spot law*, published research summary, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-equator-tomography-of-cubic-spherical-harmonics-the-60-and-9--02c51ea5353c.
5. *Exact angular resonances and minimal two-meridian sampling of pure spherical harmonics*, published research summary, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-angular-resonances-and-minimal-two-meridian-sampling-of-pu--f7a6d1cb41a5.
