# Independent compartment noise breaks transmission-noise equivalence on bounded SIR domains
## Finding
For the stochastic SIR model of Parkinson and Roy with stochastically independent Wiener drivers, the choice \(\sigma_S=-\sigma_I=g=\sqrt{0.02}(1-\alpha)SI\) is not equivalent to perturbing the transmission rate by one Itô white noise. Independence makes the sign of either scalar diffusion coefficient distributionally irrelevant: the printed covariance is \(g^2 I_2\), whereas a single noisy transmission rate has rank-one covariance \(g^2\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\) and cancels exactly from \(S+I\). Accordingly, for the printed system \(d\langle S+I\rangle_t=2g^2dt=0.04(1-\alpha)^2S^2I^2dt\). Moreover, for every constant admissible \(\alpha<1\), no finite axis-aligned rectangle with a positive upper face can be positively invariant for this diffusion: from interior points approaching an upper face the nonzero normal Brownian term gives a strictly positive short-time exit probability. Hence the zero-flux Fokker--Planck problem on \([0,1]^2\) used in the simulations is a confined boundary-value evolution, not the law of the unrestricted printed SDE on that rectangle.

The distinction appears already at the generator level. With independent Wiener components, changing \\(g\\) to \\(-g\\) in one coordinate does not create anticorrelation. The covariance matrix of the printed diffusion is \\(g^2I_2\\). A genuine stochastic perturbation of the transmission coefficient uses the same Brownian increment in the susceptible and infected equations with opposite signs, giving covariance
\[
g^2\begin{pmatrix}1&-1\\\\-1&1\end{pmatrix}.
\]
Thus the two constructions have different laws whenever \\(g\\ne0\\).

## Assumptions and scope
The statement concerns the two-dimensional stochastic SIR system printed in Parkinson and Roy, with stochastically independent Wiener processes \\(W_1,W_2\\), and the simulation diffusion
\[
g(S,I,\\alpha)=\\sqrt{0.02}(1-\\alpha)SI,\qquad \\sigma_S=g,\qquad \\sigma_I=-g.
\]
The source constrains \\(0\\le\\alpha\\le0.85\\), so \\(g\\) is nonzero at every point with \\(S>0\\) and \\(I>0\\). The bounded-domain statement is about finite axis-aligned rectangles, including the simulated square \\([0,1]^2\\). It does not say that the nonnegative quadrant is violated at its lower faces; there the multiplicative factor \\(SI\\) vanishes.

## Proof
Let \\(e=(1,1)^T\\). For the printed system the diffusion matrix is diagonal, \\(G_{\\mathrm{ind}}=\\operatorname{diag}(g,-g)\\), because \\(W_1\\) and \\(W_2\\) are independent. Hence
\[
G_{\\mathrm{ind}}G_{\\mathrm{ind}}^T=g^2I_2,
\qquad
e^TG_{\\mathrm{ind}}G_{\\mathrm{ind}}^Te=2g^2.
\]
Equivalently, the stochastic part of \\(d(S+I)\\) is \\(g\,dW_1-g\,dW_2=\\sqrt2g\,dB\\) for a Brownian motion \\(B\\), so
\[
d\\langle S+I\\rangle_t=2g^2dt=0.04(1-\\alpha)^2S^2I^2dt.
\]

If instead uncertainty is introduced by one noisy transmission rate, the same Brownian motion must enter the two incidence terms with opposite signs. The diffusion column is \\(G_{\\beta}=g(-1,1)^T\\), up to an irrelevant simultaneous sign. Therefore
\[
G_{\\beta}G_{\\beta}^T=g^2\begin{pmatrix}1&-1\\\\-1&1\end{pmatrix},
\qquad
e^TG_{\\beta}=0.
\]
The transmission noise cancels from \\(S+I\\), and the corresponding Fokker--Planck operator contains the mixed covariance term absent from the printed diagonal-diffusion equation. This proves non-equivalence in law.

For bounded-domain invariance, fix a constant \\(\\alpha<1\\), a finite upper susceptible bound \\(M_S>0\\), and any \\(i>0\\) below the infected upper bound. Put \\(x_\\varepsilon=(M_S-\\varepsilon,i)\\) and choose \\(t_\\varepsilon=c\\varepsilon^2\\) with fixed \\(c>0\\). Local continuity of the SDE coefficients gives the standard short-time expansion
\[
\\frac{S(t_\\varepsilon)-S(0)}{\\sqrt{t_\\varepsilon}}
\\Longrightarrow N(0,g_0^2),
\qquad
g_0=\\sqrt{0.02}(1-\\alpha)M_Si>0,
\]
as \\(\\varepsilon\\downarrow0\\); the drift contributes only \\(O(t_\\varepsilon)=O(\\varepsilon^2)\\). Consequently
\[
\\lim_{\\varepsilon\\downarrow0}
\\Pr_{x_\\varepsilon}\\!\\left[S(t_\\varepsilon)>M_S\\right]
=1-\\Phi\\!\\left(\\frac{1}{g_0\\sqrt c}\\right)>0.
\]
For sufficiently small \\(\\varepsilon\\), an initial point strictly inside the rectangle therefore exits through the upper susceptible face with positive probability. The same argument applies to the upper infected face. No finite such rectangle can be positively invariant.

## Verification
The bundled `verify.py` checks, using exact rational arithmetic after factoring out the positive scalar \\(S^2I^2\\), that the independent covariance has sum-direction variance \\(2g^2\\), the common-transmission covariance has sum-direction variance zero, and the source's maximum intervention \\(\\alpha=0.85\\) still leaves a strictly positive diffusion coefficient at positive upper faces. It prints `VERIFY_OK` on success. The short-time exit argument is analytic and is not replaced by finite simulation.

## Relationship to prior work
Parkinson and Roy explicitly describe \\(\\sigma_I=-\\sigma_S\\propto SI\\) as equivalent to replacing the transmission coefficient by a single white-noise perturbation, but their displayed SDE subsequently declares the two Wiener components stochastically independent. Their numerical section uses \\(\\sigma_S=-\\sigma_I=\\sqrt{0.02}(1-\\alpha)SI\\), imposes zero flux, and chooses \\([0,1]^2\\) from deterministic empirical trajectories. These ingredients together trigger the covariance and invariance mismatch proved above.

Classical stochastic epidemic work distinguishes a perturbation of one epidemiological parameter from models carrying several independent Brownian perturbations. Gray et al. study stochastic perturbation of an SIS model, while Cai, Cai and Mao explicitly describe their later two-independent-Brownian model as adding a second parameter perturbation to the earlier transmission-rate perturbation. Ji, Jiang and Shi prove positivity and invariant-set results for a different stochastic SIR construction. None of the inspected statements supplies the source-specific covariance comparison and finite-rectangle obstruction above.

## Limitations
The result does not invalidate the abstract optimal-control analysis for a Fokker--Planck PDE posed as its own confined boundary-value problem. It shows that, with the displayed independent-noise SDE and simulation diffusion, that bounded zero-flux PDE cannot simultaneously be identified as the unrestricted SDE's probability law on the chosen square. The result also does not classify invariant unbounded domains, reflected SDE formulations, or alternative correlated-noise models.

## References
1. C. Parkinson and S. Roy, *A Fokker--Planck framework for control of epidemics*, Journal of Mathematical Biology 93, 47 (2026), DOI 10.1007/s00285-026-02462-7; first public as arXiv:2601.20181 on 2026-01-28.
2. A. Gray, D. Greenhalgh, L. Hu, X. Mao and J. Pan, *A Stochastic Differential Equation SIS Epidemic Model*, SIAM Journal on Applied Mathematics 71 (2011), DOI 10.1137/10081856X.
3. C. Ji, D. Jiang and N. Shi, *The Behavior of an SIR Epidemic Model with Stochastic Perturbation*, Stochastic Analysis and Applications 30 (2012), DOI 10.1080/07362994.2012.684319.
4. S. Cai, Y. Cai and X. Mao, *A stochastic differential equation SIS epidemic model with two independent Brownian motions*, Journal of Mathematical Analysis and Applications 474 (2019), DOI 10.1016/j.jmaa.2019.02.039.
