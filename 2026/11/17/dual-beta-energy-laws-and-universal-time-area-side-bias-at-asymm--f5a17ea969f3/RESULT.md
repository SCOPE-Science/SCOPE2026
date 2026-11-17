# Dual beta energy laws and universal time–area side bias at asymmetric piecewise-potential centers

## Finding

For small periodic energy levels of a planar mechanical oscillator with two possibly different analytic restoring potentials joined at a switching axis, original physical-time sampling and uniform enclosed-area sampling have **different universal limiting laws** for the fraction of energy stored as potential energy. On each side with leading potential order \(k\), those laws are respectively \(\operatorname{Beta}(1/k,1/2)\) and \(\operatorname{Beta}(1/k,3/2)\), both in total variation with quantified local error. Their first nonzero analytic correction has an explicit centered, universal profile.

A further conclusion concerns *which half-plane is seen*. If the positive and negative potentials have distinct leading orders \(n<m\), the side of order \(n\) occupies a vanishing proportion of both the physical period and the enclosed area as energy \(h\downarrow0\). However, the **ratio** of those two vanishing proportions converges to the coefficient-independent number
\[
\lim_{h\downarrow0}\frac{T_n(h)/T(h)}{\mathcal A_n(h)/\mathcal A(h)}=\frac{m(n+2)}{n(m+2)}>1.
\]
Thus physical-time sampling systematically overweights the less-flat side relative to planar area sampling. This is a statement about two different sampling procedures, not merely a period-function asymptotic.

## Assumptions and scope

Consider \(\dot x=y\), \(\dot y=-V'(x)\), with \(V(x)=U_+(x)\) for \(x\ge0\) and \(V(x)=U_-(-x)\) for \(x<0\). Assume the one-sided functions \(U_s(r)\), for \(s\in\{+,-\}\), are real analytic for sufficiently small nonnegative \(r\), and have expansions
\[
U_s(r)=a_s r^{k_s}\bigl(1+b_s r+O(r^2)\bigr),\qquad a_s>0,\quad k_s\in\{2,3,4,\ldots\}.
\]
The remainder is analytic (with its differentiated estimates), and \(a_s,b_s,k_s\) are fixed. Shrinking the neighborhood ensures \(U'_s(r)>0\) for \(0<r<r_0\). Set \(H=y^2/2+V(x)\). Every sufficiently small level \(h>0\) is a regular closed orbit enclosing \(\Omega_h=\{H\le h\}\) near the origin. Its physical period is \(T(h)\), and its enclosed Euclidean area is \(\mathcal A(h)\). Define \(T_s(h)\) as the total time on the side \(sx>0\) during a complete cycle and \(\mathcal A_s(h)=\operatorname{area}(\Omega_h\cap\{sx>0\})\). In subscripts, \(s=+\) means \(x>0\), and \(s=-\) means \(x<0\).

Two sampling methods are considered independently. Under **time sampling**, choose a uniformly random time in a complete orbit; under **area sampling**, choose a uniformly random point of \(\Omega_h\). Conditioned on either side \(s\), define the dimensionless potential-energy share \(Q=U_s(|x|)/h\in[0,1]\). Both conditional laws are absolutely continuous. The claimed total-variation distance is \(\sup_B|\mu(B)-\nu(B)|=\tfrac12\int|f-g|\).

Let \(\alpha_s=1/k_s\), \(B\) be the Euler beta function, and \(g_{\alpha,\gamma}(q)=q^{\alpha-1}(1-q)^{\gamma-1}/B(\alpha,\gamma)\), for \(0<q<1\).

## Proof

**1. The exact quadratures.** Write \(R_s(u)=U_s^{-1}(u)\), which exists for small \(u\ge0\). A full orbit traverses the allowed interval on each side once in each direction, at speed \(|y|=\sqrt{2(h-U_s(r))}\). Consequently
\[
T_s(h)=\sqrt2\int_0^h R'_s(u)(h-u)^{-1/2}\,du,\qquad
\mathcal A_s(h)=2\sqrt2\int_0^h R'_s(u)(h-u)^{1/2}\,du.
\]
The second formula integrates the vertical chord length \(2\sqrt{2(h-U_s(r))}\) over the appropriate horizontal interval. In particular, \(\mathcal A_s'(h)=T_s(h)\) at every sufficiently small positive \(h\). These are exact identities, not asymptotic formulas.

**2. Uniform analytic inversion.** Analytic inversion after the substitution \(v=u^{\alpha_s}\) yields, with \(A_s=a_s^{-\alpha_s}\),
\[
R_s(u)=A_s u^{\alpha_s}-\alpha_s b_s A_s^2 u^{2\alpha_s}+O(u^{3\alpha_s}),
\]
\[
R_s'(u)=\alpha_s A_s u^{\alpha_s-1}\bigl[1-2\alpha_s b_s A_s u^{\alpha_s}+O(u^{2\alpha_s})\bigr].
\]
After substituting \(u=hq\), the remainder is bounded uniformly on \(0\le q\le1\) relative to the leading term, and is integrable against either beta weight \(g_{\alpha_s,1/2}\) or \(g_{\alpha_s,3/2}\). Therefore
\[
T_s(h)=\sqrt2\,a_s^{-1/k_s}J_{k_s}
 h^{1/k_s-1/2}[1+O(h^{1/k_s})],
\]
\[
\mathcal A_s(h)=2\sqrt2\,a_s^{-1/k_s}K_{k_s}
 h^{1/k_s+1/2}[1+O(h^{1/k_s})],
\]
where \(J_k=B(1/k,1/2)/k\) and \(K_k=B(1/k,3/2)/k\). The beta recurrence gives \(K_k/J_k=k/(k+2)\).

**3. Conditional beta laws and their sharp first corrections.** The exact time-sampling density of \(Q\), conditioned on side \(s\), is proportional to \(R'_s(hq)(1-q)^{-1/2}\). The area-sampling density is proportional to \(R'_s(hq)(1-q)^{1/2}\). Define \(c_s=2 b_s a_s^{-1/k_s}/k_s\), \(\alpha=1/k_s\), \(\gamma\in\{1/2,3/2\}\), and \(M_{\alpha,\gamma}=B(2\alpha,\gamma)/B(\alpha,\gamma)\). The inverse expansion and normalization show that, in weighted \(L^1(0,1)\),
\[
f_{s,\gamma,h}(q)=g_{\alpha,\gamma}(q)
\Bigl[1-c_s h^{\alpha}\bigl(q^{\alpha}-M_{\alpha,\gamma}\bigr)+O(h^{2\alpha})\Bigr].
\]
The remainder has integrated absolute value \(O(h^{2\alpha})\), uniformly over \(q\in(0,1)\). Hence both beta convergences hold in total variation with \(O(h^{1/k_s})\) error. If \(b_s\ne0\), this rate is sharp, since
\[
\|f_{s,\gamma,h}-g_{\alpha,\gamma}\|_{\mathrm{TV}}
=\frac{|c_s|h^{\alpha}}2
\int_0^1g_{\alpha,\gamma}(q)
\bigl|q^{\alpha}-M_{\alpha,\gamma}\bigr|\,dq
+O(h^{2\alpha}),
\]
and the integral is strictly positive. For exactly monomial potentials the conditional beta laws hold **at every admissible positive energy**, with zero error. The limiting mean potential-energy shares are \(2/(k_s+2)\) under time and \(2/(3k_s+2)\) under area sampling.

**4. Side selection and universal amplification.** If \(k_+=k_-=m\), both methods choose side \(s\) with limiting probability \(a_s^{-1/m}/(a_+^{-1/m}+a_-^{-1/m})\). If the exponents differ, let \(m\) be the larger order and \(n\) the smaller; label the corresponding sides \(\mathrm{slow}\) and \(\mathrm{fast}\). The exact asymptotics from step 2 imply, with \(\delta=1/n-1/m>0\),
\[
\frac{T_{\mathrm{fast}}(h)}{T(h)}\sim
\frac{a_{\mathrm{fast}}^{-1/n}J_n}{a_{\mathrm{slow}}^{-1/m}J_m}h^{\delta},
\qquad
\frac{\mathcal A_{\mathrm{fast}}(h)}{\mathcal A(h)}\sim
\frac{a_{\mathrm{fast}}^{-1/n}K_n}{a_{\mathrm{slow}}^{-1/m}K_m}h^{\delta}.
\]
Dividing cancels both stiffness parameters, and \(K_k/J_k=k/(k+2)\) yields the claimed coefficient \(m(n+2)/(n(m+2))\). The flat side carries asymptotically all of both sampling measures. There are no claims about larger energies or multiple wells.

**5. A transparent exact example.** Take \(U_+(r)=r^2/2\), \(U_-(r)=r^4/4\). For all \(h>0\), exact integration yields
\[
T_+(h)=\pi,\quad \mathcal A_+(h)=\pi h,\quad
T_-(h)=\tfrac12B(1/4,1/2)h^{-1/4},\quad
\mathcal A_-(h)=B(1/4,3/2)h^{3/4}.
\]
The less-flat positive half-plane has a vanishing time share and area share, but their ratio tends to \(4/3\). Conditional time and area potential-energy fractions have beta parameters \((1/2,1/2)\), \((1/2,3/2)\) on the positive side, and \((1/4,1/2)\), \((1/4,3/2)\) on the negative side, exactly at every energy.

## Verification

The companion standard-library checker `checks/dual_beta_check.py` verifies all displayed beta recurrences for a collection of orders, the exact harmonic/quartic formulas and their area-action derivative, the predicted rare-side ratio, and the coefficient in the first inverse-derivative correction. It prints `DUAL_BETA_TIME_AREA_SWITCHING_CENTER_CHECK_OK` on success. The rigorous argument is the analytic inversion and uniformly dominated beta-integral expansion in steps 1–4; finite computational checks are not proofs for all analytic potentials.

## Relationship to prior work

Bakhshalizadeh, Liu and Rezende (arXiv:2311.10020, first public November 16, 2023), Section 3 and Theorem B, study non-isochronicity and derive the small-energy period behavior of degenerate piecewise-potential centers. Their period decomposition and monomial scaling are acknowledged, not claimed as new. Chen and Dong (arXiv:2401.07332) treat non-isochronicity for nondegenerate piecewise Hamiltonian centers with homogeneous nonlinearities. Giordano and collaborators (DOI:10.1002/andp.202300294) relate canonical statistical and deterministic oscillator frequencies; their Gibbs-ensemble comparison is different from the two *fixed-energy* conditional sampling laws here. The novel proposed distinction is the **two full conditional beta probability laws with sharp anharmonic correction and the asymptotically universal rare-side time–area amplification**, neither asserted by the inspected sources. General one-dimensional quadrature and beta-function identities are standard prerequisites, not new contributions.

## Limitations

This is a local small-energy statement for two strictly increasing analytic one-sided potentials with leading orders at least two. The proof does not address arbitrary nonsmooth potentials, nonmonotone wells, non-Hamiltonian switching or large-energy behavior. The leading beta densities for homogeneous oscillators are elementary, and the time–area ratio follows after separately establishing the two side measures; its novelty is specific to their joint, asymmetric, sharp and perturbatively stable formulation. Unindexed equivalent treatments and older pieces of oscillator literature remain possible priority risks. No independent mathematical audit has been performed.

## References

1. A. Bakhshalizadeh, C. Liu and A. C. Rezende, *On the non-existence of isochronous centers in planar discontinuous differential systems*, arXiv:2311.10020 (first public 2023-11-16), especially Section 3, Theorem B and Eq. (10). https://arxiv.org/abs/2311.10020
2. X. Chen and G. Dong, *Non-isochronicity on piecewise Hamiltonian differential systems with homogeneous nonlinearities*, arXiv:2401.07332 (first public 2024-01-14). https://arxiv.org/abs/2401.07332
3. S. Giordano et al., *On the One-Dimensional Transition State Theory and the Relation between Statistical and Deterministic Oscillation Frequencies of Anharmonic Energy Wells*, Annalen der Physik (2023), DOI:10.1002/andp.202300294; fixed-temperature statistical-frequency comparison rather than fixed-energy side-conditioned beta laws.
4. Euler beta-function identities \(B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)\); used as standard formulas, not as novelty claims.
