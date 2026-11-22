# A covariance law reversing invasion thresholds under Fickian and Fokker–Planck epidemic dispersal

## Finding

Two cognitive-dispersal SIS epidemic laws can have opposite disease-invasion verdicts even though they share exactly the same spatial transmission rate, recovery rate, and dispersal coefficient. Their difference has a universal local covariance expansion near a spatially homogeneous environment.

Let \(\mathcal R_F(\varepsilon)\) and \(\mathcal R_P(\varepsilon)\) denote the basic reproduction numbers for Fickian and Fokker–Planck-type infective dispersal, respectively, with the same coefficient \(g(\gamma_\varepsilon)\). Put \(\nu_0=\gamma_0/\beta_0\), \(g_0=g(\gamma_0)\), \(g_1=g'(\gamma_0)\), and \(q=\nu_0 b-r\). With spatially centered first-order rate perturbations \(b,r\),

\[
\boxed{\mathcal R_P(\varepsilon)-\mathcal R_F(\varepsilon)
=-\frac{\beta_0g_1}{g_0\gamma_0^2}\langle r q\rangle\varepsilon^2+O(\varepsilon^3).}
\]

Here \(\langle\cdot\rangle\) denotes the normalized spatial integral. The second-order comparison is therefore independent of the domain geometry and Laplace spectrum, even though the individual second-order reproduction-number corrections generally depend on both. The formula also accommodates arbitrary, shared second-order perturbations of transmission and recovery rates.

For a single fixed decreasing dispersal response \(g(s)=1/(1+s)\), two explicit families on \(\Omega=(0,\pi)\) attain opposite strict threshold decisions for every sufficiently small positive \(\varepsilon\):

\[
\begin{array}{c|c|c}
\beta_\varepsilon(x)&\mathcal R_F(\varepsilon)&\mathcal R_P(\varepsilon)\\\hline
1+2\varepsilon\cos x-\tfrac98\varepsilon^2&1-\tfrac18\varepsilon^2+O(\varepsilon^3)&1+\tfrac18\varepsilon^2+O(\varepsilon^3)\\
1-\tfrac78\varepsilon^2&1+\tfrac18\varepsilon^2+O(\varepsilon^3)&1-\tfrac18\varepsilon^2+O(\varepsilon^3)
\end{array}
\]

In both cases \(\gamma_\varepsilon(x)=1+\varepsilon\cos x\). Thus neither diffusion mechanism universally dominates the other even arbitrarily close to a homogeneous, exactly critical epidemic environment.

## Assumptions and scope

Let \(\Omega\subset\mathbb R^d\) be a bounded connected smooth domain, with homogeneous zero-flux Neumann boundary conditions. Let \(\beta_0,\gamma_0>0\). Fix smooth real-valued spatial profiles \(b,r,d,h\) on \(\overline\Omega\), with \(\langle b\rangle=\langle r\rangle=0\), and define

\[
\beta_\varepsilon(x)=\beta_0+\varepsilon b(x)+\varepsilon^2d(x),\qquad
\gamma_\varepsilon(x)=\gamma_0+\varepsilon r(x)+\varepsilon^2h(x).
\]

Assume \(g\) is positive and \(C^3\) on a neighborhood of \(\gamma_0\). Only sufficiently small real \(\varepsilon\) such that all rate and dispersal coefficients remain positive are considered. The infected-component linearizations at the disease-free equilibrium are

\[
\partial_t I=\nabla\cdot(g(\gamma_\varepsilon)\nabla I)+(\beta_\varepsilon-\gamma_\varepsilon)I\quad\text{(Fickian)},
\]
\[
\partial_t I=\Delta(g(\gamma_\varepsilon)I)+(\beta_\varepsilon-\gamma_\varepsilon)I\quad\text{(Fokker--Planck)}.
\]

The corresponding basic reproduction numbers are the inverses of the smallest positive generalized eigenvalues \(\nu_F\) and \(\nu_P\) of

\[
-\nabla\cdot(g(\gamma_\varepsilon)\nabla u)+\gamma_\varepsilon u=\nu_F\beta_\varepsilon u,
\qquad\partial_nu=0,
\]
\[
-g(\gamma_\varepsilon)\Delta v+\gamma_\varepsilon v=\nu_P\beta_\varepsilon v,
\qquad\partial_nv=0.
\]

In the second equation \(v=g(\gamma_\varepsilon)I\) is the positive transformed eigenfunction; its natural Neumann condition corresponds exactly to zero Fokker–Planck flux. These eigenvalue problems agree with the threshold definitions in Liu, Wang and Zhang (2026), equations (3.7) and (3.12). The result treats the local onset threshold, not finite-population outbreak probabilities or endemic equilibrium shapes.

## Proof

**1. Smooth branches and common first variation.** At \(\varepsilon=0\), both operators reduce to the Neumann Laplacian with a positive constant coefficient and have simple smallest generalized eigenvalue \(\nu_0=\gamma_0/\beta_0\), with eigenfunction \(1\). Standard simple-eigenvalue elliptic perturbation theory permits \(C^3\) local branches. Normalize both positive eigenfunctions by spatial mean \(1\) and write

\[
\nu_\bullet=\nu_0+\varepsilon\nu_1^\bullet+\varepsilon^2\nu_2^\bullet+O(\varepsilon^3),\qquad
w_\bullet=1+\varepsilon u_1^\bullet+\varepsilon^2u_2^\bullet+O(\varepsilon^3).
\]

Here \(\bullet\in\{F,P\}\), \(\nu_\bullet\) denotes the eigenvalue, and \(w_\bullet\) denotes the eigenfunction. Integration of the first-order equations and spatial centering yields \(\nu_1^F=\nu_1^P=0\). Both first-order eigenfunctions coincide with the unique mean-zero Neumann solution \(u\) of

\[
-g_0\Delta u=q:=\nu_0 b-r,\qquad\partial_nu=0,\qquad\langle u\rangle=0.
\]

**2. Fickian second variation.** In the divergence operator, the first-order diffusivity perturbation multiplies \(\nabla1=0\); the integral of the second-order divergence is zero. Matching second-order terms and integrating yields

\[
\boxed{\beta_0\nu_2^F=\langle h-\nu_0d\rangle-\langle qu\rangle.}
\]

**3. Fokker–Planck second variation.** The transformed equation is \(-g(\gamma_\varepsilon)\Delta w_P+\gamma_\varepsilon w_P=\nu_P\beta_\varepsilon w_P\). Its second-order expansion includes an additional term \(-g_1r\Delta u\). Integration gives

\[
\beta_0\nu_2^P=\langle h-\nu_0d\rangle-\langle qu\rangle-g_1\langle r\Delta u\rangle.
\]

Since \(\Delta u=-q/g_0\),

\[
\boxed{\nu_2^P-\nu_2^F=\frac{g_1}{g_0\beta_0}\langle rq\rangle.}
\]

Taking reciprocals \(\mathcal R_\bullet=1/\nu_\bullet\), using the vanishing first derivatives and \(\nu_0=\gamma_0/\beta_0\), establishes the claimed coefficient. The shared second-order fields \(d,h\) cancel, as does the geometry-dependent quantity \(\langle qu\rangle\). If \(g_1\langle rq\rangle=0\), the theorem makes no assertion about the next nonzero comparison term.

**4. Exact threshold-reversal witnesses.** Let \(\Omega=(0,\pi)\), \(\beta_0=\gamma_0=1\), \(g(s)=1/(1+s)\), \(r(x)=\cos x\), \(b(x)=B\cos x\), \(h=0\), and \(d=-C\), for constant \(B,C\). Then \(g_0=1/2\), \(g_1=-1/4\), \(q=(B-1)\cos x\). The mean-zero Neumann solution is \(u=2(B-1)\cos x\), so \(\langle qu\rangle=(B-1)^2\) and \(\langle rq\rangle=(B-1)/2\). Consequently,

\[
\mathcal R_F=1+\big((B-1)^2-C\big)\varepsilon^2+O(\varepsilon^3),
\]
\[
\mathcal R_P=1+\big((B-1)^2+(B-1)/4-C\big)\varepsilon^2+O(\varepsilon^3).
\]

Choosing \((B,C)=(2,9/8)\) produces the strict signs \(\mathcal R_F<1<\mathcal R_P\). Choosing \((B,C)=(0,7/8)\) produces \(\mathcal R_P<1<\mathcal R_F\), for all sufficiently small \(\varepsilon>0\). Positivity and all Neumann conditions hold for sufficiently small amplitudes. Strictly nonzero quadratic coefficients justify these inequalities despite the unquantified cubic remainders.

## Verification

The accompanying `check.py` independently assembles the Fickian and transformed Fokker–Planck Neumann cosine-Galerkin generalized eigenvalue matrices on \((0,\pi)\). It verifies the rational quadratic coefficients and both threshold-ordering examples at \(\varepsilon=0.05,0.02,0.01\), with 15 cosine modes and 96-point Gaussian quadrature. The numerical eigenvalues approach the independently derived second-order expansions and straddle one in the prescribed opposite orders. Execute `python check.py` using Python with NumPy and SciPy. These finite calculations corroborate the witnesses but do not prove the infinite-dimensional asymptotic theorem, which follows from the preceding perturbation argument.

## Relationship to prior work

Liu, Wang and Zhang (2026) formulate the exact Fickian and Fokker–Planck-type SIS infected linearizations and their variational reproduction-number characterizations in equations (3.7) and (3.12). In the concluding discussion of Section 3, they observe that the general comparison is difficult and explicitly identify equality for spatially constant recovery rates. The covariance formula proves a local general comparison and constructs both strict signs with heterogeneous recovery.

Wang, Wang and Kim (2022) derive variational reproduction numbers for both mobility laws in an earlier spatial epidemic model; their analysis gives diffusion-parameter trends and numerical examples of differing threshold values. The present result uses that established spectral setting but obtains a dimension-independent second-order *difference law* and both opposite invasion verdicts at the same parameters, neither supplied by those source statements. Liu, Wang and Zhang (2023) consider a nonlinear-incidence variant and report spatial segregation and persistence; no competing covariance formula was identified in the accessible sections. Andreucci, Cirillo, Colangeli and Gabrielli (2018) analyze the microscopic origins of the two transport laws, without the SIS reaction threshold considered here.

## Limitations

The comparison is an asymptotic statement for a connected fixed smooth domain and smooth small heterogeneities near constant coefficients. It is not a global ordering for arbitrary heterogeneity, and a vanishing covariance coefficient requires a separate higher-order investigation. The two constructed invasion reversals are strict for sufficiently small positive amplitudes but no universal numerical amplitude bound is claimed. The mathematical result describes deterministic epidemic invasion and disease-free equilibrium thresholds; no claim is made about nonlinear endemic-size ordering or actual epidemiological interventions. Independent scientific verification and comprehensive historical priority certification have not occurred. The earlier 2023 Wiley work was accessible in selected indexed sections but not in a fully retrievable contiguous manuscript, leaving a limited historical-overlap risk.

## References

1. G. Liu, H. Wang and X. Zhang, *Cognitive diffusion of susceptibles driven by new infection cases in SIS epidemic models: frequency-dependent incidence*, European Journal of Applied Mathematics (published online 2026-06-10), DOI: https://doi.org/10.1017/S0956792526100448. Open-access publisher HTML: https://multimediafluids.uam.elogim.com/core/journals/european-journal-of-applied-mathematics/article/cognitive-diffusion-of-susceptibles-driven-by-new-infection-cases-in-sis-epidemic-models-frequencydependent-incidence/34A012BE7C3525264AC698C62B7A8522.
2. H. Wang, K. Wang and Y.-J. Kim, *Spatial segregation in reaction-diffusion epidemic models*, SIAM Journal on Applied Mathematics 82 (2022), 1680–1709, DOI: https://doi.org/10.1137/22M1485814. Author-hosted manuscript: https://www.math.ualberta.ca/~hwang/SpatialSegregation.pdf.
3. G. Liu, H. Wang and X. Zhang, *Epidemic dynamics and spatial segregation driven by cognitive diffusion and nonlinear incidence*, Studies in Applied Mathematics 151 (2023), 643–675, DOI: https://doi.org/10.1111/sapm.12606.
4. D. Andreucci, E. N. M. Cirillo, M. Colangeli and D. Gabrielli, *Fick and Fokker–Planck diffusion law in inhomogeneous media*, Journal of Statistical Physics 174 (2019), 469–493, arXiv:1807.05167, https://arxiv.org/abs/1807.05167.
