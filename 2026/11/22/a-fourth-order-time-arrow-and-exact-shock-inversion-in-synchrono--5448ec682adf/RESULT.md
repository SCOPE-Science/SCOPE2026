# A fourth-order time arrow and exact shock inversion in synchronously reset harmonic diffusion

## Finding

Two independently Brownian-driven harmonic coordinates, coupled only through a common Poisson clock that multiplies both coordinates by the same factor, have *zero positional cross-covariance at every lag* but strictly positive mixed squared-position covariance. If the two trap strengths differ, the squared-position cross-covariance is time-directional, with an exact rate-ratio law and one nonzero optimal asymmetry lag. Moreover, the joint stationary squared-position statistics and just one positive-lag energy cross-covariance identify both the Poisson shock rate and shock contraction factor when the two trap strengths are known, without knowledge of the two diffusivities.

Let \(i\neq j\) denote two coordinates, and set
\[
 u=1-q^2,\qquad \delta=ru,\qquad
 L_i=2a_i+\delta,\quad L_j=2a_j+\delta,\quad
 B=L_i+L_j-\delta u.
\]
Writing \(m_h=\mathbb E X_h^2=2D_h/L_h\) and \(C_0=\operatorname{Cov}(X_i^2,X_j^2)\) in the stationary law, the exact identity is
\[
 C_0=\frac{4D_iD_j\delta u}{L_iL_jB}>0,\qquad
 \operatorname{Cov}(X_i(0)^2,X_j(t)^2)=C_0e^{-L_jt},\quad t\ge0.
\]
In the reverse ordering the decay is \(C_0e^{-L_it}\), and therefore
\[
 \frac{\operatorname{Cov}(X_i(0)^2,X_j(t)^2)}
 {\operatorname{Cov}(X_j(0)^2,X_i(t)^2)}
 =e^{2(a_i-a_j)t}.
\]
When \(a_i\ne a_j\), the absolute difference of these two cross-covariances has precisely one maximum on \((0,\infty)\), at
\[
 t_*=\frac{\log(L_i/L_j)}{L_i-L_j}.
\]
Finally, let \(H=C_0/(m_im_j)\). Observing the forward exponential decay rate \(L_j\) and the stationary moments \(m_i,m_j,C_0\), with known \(a_i,a_j\), gives
\[
 \delta=L_j-2a_j,\qquad
 u=\frac{H(L_i+L_j)}{\delta(1+H)},\qquad
 q=\sqrt{1-u},\qquad r=\frac{\delta}{u},
 \quad L_i=L_j+2(a_i-a_j).
\]
Thus these shock parameters are uniquely identified on the stated domain.

## Assumptions and scope

Fix \(a_i,a_j,D_i,D_j,r>0\) and \(0\le q<1\). Between shocks, the two real coordinates satisfy the Itô equations \(dX_h=-a_hX_h\,dt+\sqrt{2D_h}\,dW_h\), with mutually independent standard Brownian motions. A single independent homogeneous Poisson clock of rate \(r\) simultaneously maps \((X_i,X_j)\mapsto(qX_i,qX_j)\) at each jump. Initial conditions are drawn from the unique stationary law. All expectations are with respect to that law and the independent future noises, and all lag assertions hold for every real \(t\ge0\). Distinct trap strengths are required only for a *nonzero* time arrow and its unique peak. Their equality does not invalidate the positive cross-energy covariance or parameter inversion.

## Proof

**Existence, integrability, and conditional decorrelation.** Coupling two solutions to the same Brownian paths and clock makes their differences at most \(e^{-a_ht}\) times their initial differences (each shock only contracts). Extending the stochastic convolution to the infinite past therefore gives the unique stationary distribution. Conditionally on the entire past Poisson clock, each coordinate is centered Gaussian, with variance
\[
 V_h=2D_h\int_0^\infty e^{-2a_hs}q^{2N(-s,0]}\,ds\le D_h/a_h.
\]
The two centered coordinates are conditionally independent because their Brownian drivers are independent. This yields \(\mathbb E[X_i(0)X_j(t)]=0\) for all real \(t\) (also at unequal times), while all needed fourth moments exist by the variance bound.

**Stationary moments.** The exact jump-diffusion generator acting on a twice differentiable polynomial is
\[
 \mathcal Lf=\sum_{h=i,j}\bigl(-a_hx_h\partial_hf+D_h\partial_h^2f\bigr)
 +r\,[f(qx_i,qx_j)-f(x_i,x_j)].
\]
It gives \(\mathcal L(x_h^2)=2D_h-L_hx_h^2\) and
\[
 \mathcal L(x_i^2x_j^2)=2D_ix_j^2+2D_jx_i^2-Bx_i^2x_j^2.
\]
Stationarity implies \(m_h=2D_h/L_h\) and
\[
 \mathbb E[X_i^2X_j^2]=\frac{2D_im_j+2D_jm_i}{B}
 =\frac{4D_iD_j(L_i+L_j)}{L_iL_jB}.
\]
Subtracting \(m_im_j\), and using \(L_i+L_j-B=r(1-q^2)^2=\delta u\), gives the asserted positive \(C_0\).

**Two-time covariances and the arrow.** Because \(\mathcal L(x_j^2-m_j)=-L_j(x_j^2-m_j)\), the Markov semigroup yields
\(\mathbb E[X_j(t)^2-m_j\mid\mathcal F_0]=e^{-L_jt}(X_j(0)^2-m_j)\).
Multiplication by \(X_i(0)^2-m_i\) and expectation establishes the forward exponential; reversing the indices establishes the reverse exponential. Their ratio cancels the common amplitude and the common resetting correction \(\delta\), giving \(e^{2(a_i-a_j)t}\). The derivative of \(e^{-L_jt}-e^{-L_it}\) has exactly one zero for \(L_i\ne L_j\), the displayed \(t_*\); the absolute difference is zero at both ends and strictly positive between, proving its unique maximum.

**Exact inversion.** From the amplitude equation, \(H=\delta u/(L_i+L_j-\delta u)\). The measured exponential slope determines \(L_j\), hence \(\delta\), and therefore \(L_i\). Solving for \(u\) gives the displayed formula, which has a unique solution in the physical interval \(0<u\le1\). The remaining formulas recover \(q\) and \(r\). No diffusivity appears in \(H\).

## Verification

The accompanying standalone `verify.py` independently checks the stationary polynomial generator identities for three parameter combinations, including full resetting; checks both cross-lag expressions and the inverse formulas; confirms the unique-lag maximizer; and samples the stationary common backward-Poisson clock directly to compare the conditional-Gaussian variance covariance against the analytic formula. Run `python verify.py` with Python 3 and NumPy. In a sample test with \((a_i,a_j,D_i,D_j,r,q)=(1.7,0.9,0.6,1.4,3.2,0.45)\), the analytic connected squared-position covariance is \(0.031926947\) and the fixed-seed independent clock simulation returns approximately \(0.031832\). The Monte Carlo check is diagnostic only; the equalities and all-parameter quantifiers follow from the analytic proof.

## Relationship to prior work

Galla (2026), especially the multi-particle section and supplemental S2.2, introduced the common-shock conditional-independence picture and computed the equal-time squared-position correlations in a weak-reset *diffusion approximation* for identical linear coordinates. The present result treats the original finite-amplitude Poisson jump system exactly, permits unequal harmonic strengths, obtains two-direction time-lag formulas and a quantitative inverse identification theorem. Tal-Friedman, Roichman and Reuveni (2022) developed partial-reset stationary and transient laws for one Brownian coordinate; Di Bello et al. (2023) provided one-process partial-reset transition kernels. Neither is asserted to establish a multi-coordinate fourth-order time arrow or the shock-parameter inversion. The generic Markov generator method is standard and not claimed as a new technique.

## Limitations

The theorem assumes independent thermal Brownian drivers, shared deterministic contraction, strictly positive harmonic relaxations and stationary sampling. It does not treat random contraction amplitudes, colored baths, partial synchronization, finite-sample statistical efficiency or measurement errors. The time arrow is a sufficient witness of irreversibility when the traps differ, not a characterization of reversibility when they agree. Novelty is relative to inspected sources and indexed comparisons; unpublished or differently expressed equivalent results may exist. No independent audit has been performed.

## References

1. T. Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1 (first public date 2026-02-25), https://arxiv.org/html/2602.21635.
2. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with partial resetting*, Phys. Rev. E **106**, 054116 (2022), https://doi.org/10.1103/PhysRevE.106.054116.
3. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, New J. Phys. **25**, 082002 (2023), https://doi.org/10.1088/1367-2630/aced1d.
