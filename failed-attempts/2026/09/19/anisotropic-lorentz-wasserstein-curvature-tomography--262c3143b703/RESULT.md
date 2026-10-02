# Anisotropic Lorentz–Wasserstein probes recover timelike sectional curvature and the full curvature tensor

## Statement

Let \((M,g)\) be a globally hyperbolic Lorentzian manifold of dimension \(n+1\), with signature \((+,-,\ldots,-)\). Fix \(x\in M\), a future-directed unit timelike vector \(v\in T_xM\), and the unit-speed timelike geodesic
\[
\gamma(t)=\exp_x(tv).
\]
Put \(h_0=-g|_{v^\perp}\). Choose an \(h_0\)-orthonormal basis \(e_1,\ldots,e_n\) of \(v^\perp\), parallel translate it along \(\gamma\), and let \(A_v\) be the symmetric endomorphism of \(v^\perp\) whose matrix \(a=(a_{ij})\) is the quadratic coefficient in the Fermi expansion
\[
g_{00}(t,w)=1-a_{ij}(t)w^iw^j+O(|w|_{h_0}^3),\qquad a_{ij}(0)=a_{ij}.
\]
With the curvature convention of Braun--Li, \(a(u,u)\) is the timelike sectional curvature of \(\operatorname{span}\{v,u\}\) for every \(h_0\)-unit \(u\in v^\perp\), and \(\operatorname{tr}_{h_0}A_v=\operatorname{Ric}(v,v)\).

Let \(\mu\) be any Borel probability measure supported in the unit ball of \((v^\perp,h_0)\), and define the matched anisotropic slice measures
\[
\nu_{0}^{\varepsilon,\mu}
 :=(\exp_x\circ(\varepsilon\,\mathrm{Id}))_\#\mu,
\qquad
\nu_{\delta}^{\varepsilon,\mu}
 :=\bigl(\exp_{\gamma(\delta)}\circ /\!\!/_{\delta}\circ(\varepsilon\,\mathrm{Id})\bigr)_\#\mu,
\]
where \(/\!\!/_{\delta}:v^\perp\to\dot\gamma(\delta)^\perp\) is parallel transport along \(\gamma\). Write
\[
M_\mu^{ij}=\int u^iu^j\,d\mu(u)
\]
for the raw second-moment matrix of \(\mu\).

Then, as \(\delta,\varepsilon\to0\) with \(\varepsilon=o(\delta^{5/2})\),
\[
\boxed{
\ell_1\bigl(\nu_{0}^{\varepsilon,\mu},\nu_{\delta}^{\varepsilon,\mu}\bigr)
=
\delta\left[
1-\frac{\varepsilon^2}{2}\,\operatorname{tr}(A_vM_\mu)
+O(\varepsilon^3)+O(\delta\varepsilon^2)
\right].
}
\]
The remainder constants can be chosen uniformly over all such probability measures \(\mu\).

Equivalently, if
\[
\kappa_{\varepsilon,\delta}^{\mu}(v)
:=1-\frac{\ell_1(\nu_{0}^{\varepsilon,\mu},\nu_{\delta}^{\varepsilon,\mu})}{\delta},
\]
then
\[
\boxed{
\lim_{\substack{\delta,\varepsilon\to0\\ \varepsilon=o(\delta^{5/2})}}
\frac{2}{\varepsilon^2}\,\kappa_{\varepsilon,\delta}^{\mu}(v)
=\operatorname{tr}(A_vM_\mu).
}
\]
Thus the leading Lorentz--Wasserstein correction does not intrinsically collapse curvature to Ricci: Ricci appears for isotropic probes because their second moment is a scalar multiple of the identity.

### Rank-one probes recover timelike sectional curvature

For any \(h_0\)-unit vector \(u\in v^\perp\), take
\[
\mu_u=\tfrac12(\delta_u+\delta_{-u}).
\]
Then \(M_{\mu_u}=u\otimes u\), so
\[
\boxed{
\lim \frac{2}{\varepsilon^2}\,\kappa_{\varepsilon,\delta}^{\mu_u}(v)
=a(u,u)=\varkappa(u,v).
}
\]
Hence a two-point transverse probability law extracts a single timelike sectional curvature from the same codimension-one Lorentz--Wasserstein observable whose isotropic version extracts \(\operatorname{Ric}(v,v)\).

### Finite tomography of the tidal operator

Fix an \(h_0\)-orthonormal basis \(e_1,\ldots,e_n\) of \(v^\perp\). Use the \(n\) probes \(\mu_{e_i}\) and the \(\binom n2\) probes
\[
\mu_{ij}
=
\tfrac12\left(
\delta_{(e_i+e_j)/\sqrt2}
+
\delta_{-(e_i+e_j)/\sqrt2}
\right),\qquad i<j.
\]
Let \(Q_i\) and \(Q_{ij}\) be the corresponding normalized limits. Then
\[
Q_i=a_{ii},\qquad
Q_{ij}=\frac{a_{ii}+2a_{ij}+a_{jj}}2,
\]
so
\[
\boxed{
a_{ij}=Q_{ij}-\frac{Q_i+Q_j}{2}.}
\]
Therefore exactly \(n(n+1)/2\) explicitly specified scalar probes recover the entire symmetric tidal/Fermi curvature operator \(A_v\). This count is linearly minimal within the class of second-moment measurements \(A\mapsto\operatorname{tr}(AM)\), because \(\dim\operatorname{Sym}(n)=n(n+1)/2\).

### Finite tomography of the full Riemann tensor

Let \(m=n+1\). Vary \(v\) over future-directed unit timelike vectors and \(u\) over unit spacelike vectors orthogonal to \(v\). The rank-one probe limit gives the linear functional
\[
R\longmapsto R(u,v,v,u)
\]
up to the fixed sign convention encoded by \(a(u,u)\). These functionals separate algebraic curvature tensors. Indeed, if an algebraic curvature tensor \(S\) has \(S(u,v,v,u)=0\) for every such orthogonal timelike-spacelike pair, then for each timelike \(v\) and arbitrary \(z\), writing \(z=\alpha v+u\) with \(u\perp v\) gives
\[
S(z,v,v,z)=S(u,v,v,u)=0.
\]
For fixed \(z\), the left-hand side is a polynomial in \(v\), and it vanishes on the open timelike cone; hence it vanishes for all \(v\). Thus all sectional quadratic forms of \(S\) vanish, and the standard polarization identity for algebraic curvature tensors yields \(S=0\).

The vector space of algebraic curvature tensors in dimension \(m\) has dimension
\[
D_m=\frac{m^2(m^2-1)}{12}.
\]
Since the above family of scalar probe functionals separates this \(D_m\)-dimensional space, a finite subfamily of exactly \(D_m\) such probes can be chosen to form a basis of its dual. Consequently,
\[
\boxed{
D_m=\frac{m^2(m^2-1)}{12}
}
\]
suitably chosen anisotropic Lorentz--Wasserstein probe limits determine the complete algebraic Riemann curvature tensor at a point. In \(3+1\) dimensions this gives \(D_4=20\). The count is linearly minimal among scalar linear curvature measurements.

## Proof of the anisotropic expansion

Braun--Li prove two pointwise Fermi-coordinate estimates that are uniform for \(w,w'\) in the transverse \(\varepsilon\)-ball. Their lower estimate states that whenever \(|w-w'|_{h_0}=O(\delta\varepsilon^2)\),
\[
l\bigl(\exp_x w,\exp_{\gamma(\delta)}(/\!\!/_{\delta}w')\bigr)
\ge
\delta-\frac\delta2a_{ij}w^iw^j
+O(\delta\varepsilon^3)+O(\delta^2\varepsilon^2).
\]
Their upper estimate, under \(\varepsilon=o(\delta^{5/2})\), is uniform in arbitrary \(w,w'\) in the ball and gives
\[
l\bigl(\exp_x w,\exp_{\gamma(\delta)}(/\!\!/_{\delta}w')\bigr)
\le
\delta-\frac1{2\delta}|w-w'|_{h_0}^2
-\frac\delta2a_{ij}w^iw^j
+O(\delta\varepsilon^3)+O(\delta^2\varepsilon^2).
\]
Dropping the nonpositive displacement term yields an upper bound depending only on the first marginal.

For the lower bound on \(\ell_1\), couple the two matched laws by the identity in transverse coordinates, so \(w'=w=\varepsilon u\). This is a chronological coupling for sufficiently small parameters and has zero transverse displacement. Integrating the lower estimate gives
\[
\ell_1
\ge
\delta-
\frac{\delta\varepsilon^2}{2}
\int a_{ij}u^iu^j\,d\mu(u)
+O(\delta\varepsilon^3)+O(\delta^2\varepsilon^2).
\]

For the upper bound, every coupling is chronological once the two sufficiently small slices are uniformly timelike separated. Integrate the upper pointwise estimate against an arbitrary coupling. Its curvature term depends only on the first marginal, hence equals the same second-moment contraction
\[
\varepsilon^2a_{ij}\int u^iu^j\,d\mu(u).
\]
Taking the supremum over chronological couplings yields the matching upper estimate. Dividing by \(\delta\) proves the formula.

The proof uses neither absolute continuity nor symmetry of \(\mu\). Atomic probes are therefore allowed. Isotropy is needed only if one wants the contraction to reduce to a trace.

## Consistency checks

1. **Braun--Li isotropic slice.** For normalized Lebesgue measure on the unit ball,
\[
M_\mu=\frac1{n+2}I,
\]
so the formula becomes
\[
\ell_1
=
\delta\left[
1-\frac{\varepsilon^2}{2(n+2)}\operatorname{Ric}(v,v)
+O(\varepsilon^3)+O(\delta\varepsilon^2)
\right],
\]
exactly their unweighted reconstruction formula.

2. **Flat spacetime.** If \(A_v=0\), the second-order correction vanishes for every anisotropic law, as expected.

3. **Constant timelike sectional curvature.** If \(A_v=K I\), the correction is \(-\frac12\varepsilon^2K\,\mathbb E_\mu|u|^2\). For the unit-ball law, \(\mathbb E|u|^2=n/(n+2)\), recovering \(\operatorname{Ric}(v,v)=nK\).

4. **Off-diagonal reconstruction.** For \(u=(e_i+e_j)/\sqrt2\), the measured quadratic form is \((a_{ii}+2a_{ij}+a_{jj})/2\), giving the stated polarization formula.

## Context and originality

Braun--Li (arXiv:2609.18664, submitted 16 September 2026) introduce codimension-one timelike Ollivier--Ricci curvature and prove the isotropic reconstruction of \(\operatorname{Ric}(v,v)\). Their proof explicitly identifies the Fermi curvature quadratic form \(a_{ij}w^iw^j\) before averaging it over a Euclidean ball, and their upper estimate is uniform over arbitrary endpoint pairs. The present result retains that quadratic form instead of tracing it out: arbitrary matched transverse laws convert it into the contraction \(\operatorname{tr}(A_vM_\mu)\), rank-one laws recover timelike sectional curvature, and finite collections recover first the full tidal operator and then the entire algebraic curvature tensor.

Barton--Borza--Roehrig (arXiv:2606.04910) independently develop Lorentzian Ollivier--Ricci curvature from causal-diamond measures and recover timelike Ricci curvature. Their time-separation analysis also displays the unaveraged curvature quadratic form before a symmetric-domain average, but their transport curvature and continuum theorem use isotropic causal-diamond measures and report the Ricci contraction.

Ketterer--Mondino (arXiv:1610.03339; Adv. Math. 329 (2018), 781--818) characterize sectional and intermediate Ricci curvature bounds in the Riemannian setting through entropy convexity along Wasserstein geodesics. This is distinct from the local Ollivier/Lorentz--Wasserstein endpoint observable considered here.

Targeted searches for combinations of “Lorentz--Wasserstein”, “anisotropic”, “second moment”, “sectional curvature”, “Jacobi operator”, “tidal curvature”, “Riemann tensor”, “Ollivier--Ricci”, and “curvature tomography” did not locate an earlier statement of the matched-law second-moment formula, the explicit finite tidal-operator reconstruction, or the finite full-curvature tomography consequence. Searches of the current SCOPE archive by timelike, Lorentz--Wasserstein, Ollivier--Ricci, sectional-curvature, Jacobi/tidal, and curvature-tensor terminology found no overlap. Originality is asserted only to the best of our knowledge.

## Limitations

The result is a smooth local asymptotic theorem and inherits the scale regime \(\varepsilon=o(\delta^{5/2})\) from the available uniform upper bound. It does not by itself define an anisotropic curvature notion on discrete causal sets, prove convergence of a discrete estimator, or give stability/error bounds for reconstructing curvature from noisy finite data. The full-tensor statement is an algebraic identifiability theorem: it proves existence of a linearly minimal finite family of scalar probes but does not optimize conditioning or provide a canonical universal choice of the \(D_m\) directions. The individual rank-one limit is closely tied to the classical fact that timelike sectional curvature appears in the second variation of time separation; the new content is the matched-law Lorentz--Wasserstein second-moment law and its finite transport-tomography consequences.

## References

1. M. Braun and X.-M. Li, *Timelike Ollivier--Ricci curvature*, arXiv:2609.18664 (2026). https://arxiv.org/abs/2609.18664
2. J. Barton, S. Borza and J. Roehrig, *Ollivier--Ricci curvature for causal sets*, arXiv:2606.04910 (2026). https://arxiv.org/abs/2606.04910
3. C. Ketterer and A. Mondino, *Sectional and intermediate Ricci curvature lower bounds via optimal transport*, Adv. Math. 329 (2018), 781--818; arXiv:1610.03339. https://arxiv.org/abs/1610.03339
