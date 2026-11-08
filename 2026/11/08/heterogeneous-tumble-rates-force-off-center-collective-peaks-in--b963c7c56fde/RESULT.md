# Heterogeneous tumble rates force off-center collective peaks in a repulsive harmonic pair

## Finding
Consider two oppositely repelling run-and-tumble particles in one dimension, harmonically confined at strength \(\mu>0\), propelled at the same speed \(v>0\), and independently reversing direction at rates \(\gamma_1,\gamma_2>0\). The repulsion has logarithmic strength \(g>0\). Set \(a=\gamma_1/\mu\), \(b=\gamma_2/\mu\), and let \(Z=\mu(X_1+X_2)/(2v)\) denote the stationary dimensionless center of mass. Its law is independent of \(g\).

**Sharp strong-total-tumbling dichotomy.** For every \(a,b>0\) with \(a+b>3\), its density \(p_{a,b}\) is even, supported on \([-1,1]\), positive inside and zero at both endpoints. More precisely:

- If \(\min(a,b)<1\), necessarily \(\max(a,b)>2\); then \(Z=0\) is a *strict local minimum*, and at least one positive and one negative off-center local maximum exist. Assuming \(a<1<b\), its exact central curvature is
  \[
  p_{a,b}''(0)=\frac{16K_aK_b(b-1)(1-a)}{a+b-3}\,B\left(\tfrac12,a+b-2\right)>0,
  \qquad K_t=\frac{\Gamma(t+1/2)}{\sqrt\pi\Gamma(t)}.
  \]
- If \(\min(a,b)\ge1\), the density is strictly decreasing on \((0,1)\) and has a unique global maximum at zero. If one rate equals \(\mu\), the central maximum can have zero second derivative.

Thus within the full, natural twice-differentiable regime \(a+b>3\), crossing the *smaller individual* tumble rate through \(\mu\) switches the center between a genuine minimum and the unique global maximum, even if the *sum* of rates stays large. No claim is made that the off-center maxima in the first case are the only local maxima.

The common endpoint decay is
\[
 p_{a,b}(z)\sim 4^{a+b-1}K_aK_bB(a,b)(1-z)^{a+b-1},\qquad z\uparrow1.
\]

## Assumptions and scope
For any \(\mu,v,g,\gamma_1,\gamma_2>0\), in the ordered region \(X_1>X_2\), let independent stationary telegraph processes \(\sigma_i(t)\in\{-1,+1\}\) flip at rate \(\gamma_i\), and consider the piecewise deterministic system
\[
 \dot X_1=-\mu X_1+v\sigma_1+\frac{g}{X_1-X_2},\qquad
 \dot X_2=-\mu X_2+v\sigma_2+\frac{g}{X_2-X_1}.
\]
For \(X_2>X_1\) the particle labels are interchanged; the same center law holds. There is no translational Brownian noise and no orientation coupling. The sharp dichotomy asserts the property for **all** \(a,b\) with \(a+b>3\), not for unexamined lower total rates. The non-Markovian effective three-valued collective forcing when \(\gamma_1\ne\gamma_2\) is part of the model, not replaced by a Markov three-state approximation.

## Proof
**1. Stationarity and force cancellation.** The ordered gap \(d=X_1-X_2>0\) obeys \(\dot d=-\mu d+v(\sigma_1-\sigma_2)+2g/d\). Since the last term dominates as \(d\downarrow0\), the ordered region is invariant; confinement bounds large gaps. The gradient of \(\mu(X_1^2+X_2^2)/2-g\log d\) is strongly monotone with modulus \(\mu\), so solutions driven by the same telegraph history contract exponentially. This yields a stationary pullback solution and uniqueness within an ordering sector. Summing the particle equations removes the equal-and-opposite repulsion exactly:
\[
 \dot M=-\mu M+\frac v2(\sigma_1+\sigma_2),\qquad M=(X_1+X_2)/2.
\]
Consequently \(Z=(U_a+U_b)/2\), where independent stationary variables are \(U_a=\mu\int_0^\infty e^{-\mu s}\sigma_1(-s)\,ds\), and similarly \(U_b\).

**2. Exact convolution.** The zero-flux stationary two-orientation equations for \(\dot U=\mu(-U+\sigma)\) give the normalized marginal density
\[
 f_t(u)=K_t(1-u^2)^{t-1}\mathbf1_{\{|u|<1\}},\qquad K_t=\frac{\Gamma(t+1/2)}{\sqrt\pi\Gamma(t)}.
\]
Indeed their sum enforces zero positional current and their difference yields \((1-u^2)f_t'(u)=-2(t-1)u f_t(u)\); normalization uses \(\int_{-1}^1(1-u^2)^{t-1}du=B(1/2,t)\). Independence then yields
\[
 p_{a,b}(z)=2\int_{\mathbb R}f_a(x)f_b(2z-x)\,dx,
 \qquad p_{a,b}(0)=2K_aK_bB\left(\tfrac12,a+b-1\right)
\]
for \(a+b>1\). This density is positive and even on \((-1,1)\). For \(z=1-\epsilon\), set \(x=1-2\epsilon t\); using dominated convergence after dividing out endpoint powers proves the claimed exact \(B(a,b)\) edge coefficient. In particular both edge limits are zero when \(a+b>3\).

**3. The rate-heterogeneous central minimum.** Suppose without loss \(0<a<1\). Since \(a+b>3\), then \(b>2\). The density \(f_b\) has an integrable second weak derivative, so \(p_{a,b}\in C^2\) and differentiation of the convolution is valid. Direct differentiation gives
\[
 f_b''(x)=K_b(b-1)\{-2(1-x^2)^{b-2}+4(b-2)x^2(1-x^2)^{b-3}\},\quad |x|<1.
\]
There are no boundary delta terms because \(f_b\) and \(f_b'\) vanish at both endpoints. Therefore
\[
 p_{a,b}''(0)=8K_aK_b(b-1)\left\{-2B\left(\tfrac12,a+b-2\right)+4(b-2)B\left(\tfrac32,a+b-3\right)\right\}.
\]
The beta identity \(B(3/2,s-3)=B(1/2,s-2)/[2(s-3)]\), with \(s=a+b>3\), reduces this to the positive formula in the finding. Symmetry gives \(p'(0)=0\), hence the origin is a strict local minimum. As \(p\) is continuous, positive inside and tends to zero at each endpoint, a maximum is attained strictly inside each half interval \((-1,0)\) and \((0,1)\).

**4. The central-maximum sector.** If \(a,b>1\), the factors \(f_a,f_b\) are symmetric, strictly log-concave densities on their intervals. Their convolution is symmetric and strictly log-concave in the interior (by the one-dimensional strict convolution form of the log-concavity theorem); it therefore strictly decreases away from zero. Alternatively this follows from the integral layer-cake representation of the convolution of symmetric strictly decreasing densities. If \(a=1\), then \(f_a\) is uniform on \((-1,1)\); as \(b>2\), differentiation of \(p_{1,b}(z)=\int_{2z-1}^{2z+1}f_b(y)dy\) gives \(p_{1,b}'(z)=-2f_b(2z-1)<0\) for \(0<z<1\). The case \(b=1\) is identical by symmetry. These cases exhaust \(a+b>3\) with \(\min(a,b)\ge1\), completing the dichotomy.

## Verification
The standalone `checker.py` numerically evaluates the original beta convolution with independent endpoint-weighted quadrature, compares the predicted central curvature to finite differences for four heterogeneous parameter pairs, checks strict central decrease for four pairs, verifies three endpoint coefficients, checks normalization for two cases, and confirms force cancellation for three interacting configurations. It passed 16 deterministic checks. These finite diagnostics are reproducibility checks, not a replacement for the all-parameter analytical proof. Run `python checker.py` with Python 3 and SciPy installed.

## Relationship to prior work
Touzo, Le Doussal and Schehr (first public February 6, 2023) study active Dyson dynamics and explicitly derive the interaction-independent center equation, but their independent particles share a single reversal rate, and their finite-particle singularity calculations concern particle-position densities. Basu and collaborators (first public October 22, 2019) exactly solve the **equal-rate**, three-state harmonic-trap model; for unequal reversal rates, the collective three-valued orientation is **not Markov**: the two microscopic states corresponding to zero total propulsion have different outgoing transition rates. The sharp heterogeneous high-rate off-center transition is therefore not implied by that three-state generator. Le Doussal, Majumdar and Schehr (2021) analyze a two-particle relative coordinate under mutual attraction; Smith and collaborators (2022) analyze two-dimensional direction-switching models with symmetric rates. None of the inspected relevant passages states this unequal-rate, interaction-invariant center-density dichotomy. A failure to find it in indexed literature is not an exhaustive novelty proof.

## Limitations
The classification concerns the sector \(a+b>3\), chosen for its genuine twice-differentiable central density, and does not classify all lower-rate regimes. In the mixed-rate sector it proves **at least two off-center local maxima**, not their uniqueness or a complete modality count. Rates and speeds are as stipulated, thermal noise is absent, and repulsion is equal and opposite. Unindexed literature on asymmetric beta-density convolutions may contain equivalent formulas or stronger modality results. Independent scientific validation has not been performed.

## References
- L. Touzo, P. Le Doussal and G. Schehr, *Interacting, running and tumbling: the active Dyson Brownian motion*, arXiv:2302.02937, first version 2023-02-06, https://arxiv.org/abs/2302.02937 . In particular, Eq. (37) and Sec. II.
- U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083, first version 2019-10-22, https://arxiv.org/abs/1910.10083 . In particular, Sec. 2 and exact stationary density.
- P. Le Doussal, S. N. Majumdar and G. Schehr, *Stationary nonequilibrium bound state of a pair of run and tumble particles*, arXiv:2105.11838, first version 2021-05-25, https://arxiv.org/abs/2105.11838 .
- N. R. Smith, P. Le Doussal, S. N. Majumdar and G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445, first version 2022-07-21, https://arxiv.org/abs/2207.10445 .
