# Spectral zero ladders identify source asymmetry and mortality in burst-fed two-target diffusion

## Finding

Consider a source at a fixed interior point of a finite one-dimensional diffusion interval, producing independent diffusing particles in Poisson-timed random bursts. Each particle is absorbed at its first contact with either endpoint, or undergoes independent exponential degradation. Write \(N_0\) and \(N_L\) for the stationary counting measures of particles reacting at the two endpoint targets. Although their real-time cross-covariance density is nonnegative at **every** lag, their real cross-spectrum distinguishes exact source symmetry from asymmetry:

- At the midpoint, the real cross-spectrum is strictly positive at every finite frequency.
- At any other interior point, it has infinitely many positive simple zeros and alternating positive and negative high-frequency bands. If \(\omega_n\) denotes the unique sufficiently high-frequency zero associated with the phase \((n+\tfrac12)\pi\), then
  \[
  \omega_n=\frac{2D\pi^2}{(L-2x)^2}(n+\tfrac12)^2+\mu+O(n^{-2}).
  \]

In particular, when \(D\) and \(L\) are known, the asymptotic zero ladder determines the source's distance from the midpoint and the independent molecular-degradation rate, up to the unavoidable spatial reflection ambiguity. The sign pattern does not depend on burst intensity or burst-size distribution once a burst of at least two particles has positive probability. When every burst has size zero or one, the two target streams are independent Poisson processes and their cross-spectrum vanishes.

## Assumptions and scope

Let \(L,D,b>0\), \(\mu\geq0\), and \(x\in(0,L)\). Bursts occur at the points of a stationary Poisson process on the whole real time line with intensity \(b\). Burst sizes are independent copies of a nonnegative integer-valued variable \(K\), with \(\mathbb E K^2<\infty\). Each burst releases \(K\) independent particles simultaneously at \(x\). Each particle evolves with infinitesimal generator \(D\partial_{yy}\) on \((0,L)\), is absorbed at its first hit of either boundary, and, independently, is destroyed at exponential rate \(\mu\) before either hit. Destruction yields no target event. A single particle can produce at most one target event.

Write \(N_0\) and \(N_L\) for the point measures of hits at \(0\) and \(L\). The cross-spectrum \(S_{0L}(\omega)\) is the Fourier transform \(\int_{\mathbb R}e^{-i\omega t}C_{0L}(t)\,dt\), where \(C_{0L}(t)\,dt\,ds\) is the stationary covariance of target-\(L\) counts in \(ds\) and target-0 counts in \(ds+dt\). This convention yields one particular conjugate orientation; the real part, zeros, and conclusions are invariant under the other convention.

Put \(m_2=\mathbb E[K(K-1)]\), and, for real \(\omega\), let \(q(\omega)=\sqrt{(\mu+i\omega)/D}\), with the square-root branch of nonnegative real part. Values at \(\mu=\omega=0\) are interpreted by continuous extension.

## Proof

**1. Individual absorption transforms.** For \(\operatorname{Re}s\geq0\), the Laplace transforms of the defective first-hit densities \(f_0\) and \(f_L\) are given by
\[
F_0(s)=\frac{\sinh((L-x)\sqrt{(\mu+s)/D})}{\sinh(L\sqrt{(\mu+s)/D})},\qquad
F_L(s)=\frac{\sinh(x\sqrt{(\mu+s)/D})}{\sinh(L\sqrt{(\mu+s)/D})}.
\]
Indeed, the backward equation \(Du''=(\mu+s)u\), with boundary data \((1,0)\) or \((0,1)\), has these unique solutions. It includes the probability of escaping degradation. The interval is bounded, so the defective densities have integrable exponential tails.

**2. Cross-target cluster covariance.** Distinct Poisson source bursts are independent; their off-diagonal covariance contributions cancel against the product of the means. A single particle never hits both endpoints, so within a burst only *ordered distinct particle pairs* contribute. Conditional on burst size \(K\), there are \(K(K-1)\) such pairs, with independent event times and target marks. Consequently, for \(t\in\mathbb R\),
\[
C_{0L}(t)=b m_2\int_{\max(0,-t)}^\infty f_L(u)f_0(u+t)\,du\geq0.
\]
Taking Fourier transforms (or interchanging the two endpoint labels if an opposite lag convention is chosen) gives the exact complex cross-spectrum
\[
S_{0L}(\omega)=b m_2 F_0(i\omega)\overline{F_L(i\omega)}.
\]
It is continuous for all real \(\omega\). If \(m_2=0\), the nonnegative integer \(K\) is at most one almost surely. Poisson marking and displacement then make the two streams independent homogeneous Poisson processes. If \(m_2>0\), the factor \(b m_2\) is strictly positive and cannot affect the signs or zeros.

**3. The exact midpoint exception.** If \(x=L/2\), then \(F_0=F_L\), hence \(\operatorname{Re}S_{0L}(\omega)=b m_2|F_0(i\omega)|^2>0\) at every finite real frequency. The numerator and denominator of \(F_0\) have no nonzero zeros on the relevant complex square-root ray; at the origin of that ray the limiting transform equals \(1/2\). Thus this is strict positivity, not merely nonnegativity.

**4. Oscillatory off-center asymptotics.** Suppose \(d=|L-2x|>0\) and set \(a=\min(x,L-x)>0\). For \(\omega>0\), write \(q(\omega)=u+iv\), where \(u,v>0\). Then
\[
u^2-v^2=\mu/D,\quad \omega=2Duv,\quad u=\sqrt{v^2+\mu/D}.
\]
The exact identities
\[
F_0(i\omega)=e^{-xq}\frac{1-e^{-2(L-x)q}}{1-e^{-2Lq}},\qquad
F_L(i\omega)=e^{-(L-x)q}\frac{1-e^{-2xq}}{1-e^{-2Lq}}
\]
give, as \(v\to\infty\),
\[
\frac{\operatorname{Re}S_{0L}(\omega(v))}{b m_2e^{-Lu}}
=\cos((L-2x)v)+O(e^{-2au}).
\]
The error is also \(O(e^{-2av})\) after one derivative with respect to \(v\): it is a finite product and quotient of exponentials, with a denominator bounded away from zero for sufficiently large \(v\). The positive-frequency map \(\omega(v)=2Dv\sqrt{v^2+\mu/D}\) is strictly increasing.

The reference cosine has simple zeros \(v_n^0=(n+1/2)\pi/d\). Uniform control of both the function and derivative ensures, for every sufficiently large integer \(n\), exactly one simple true zero in a small fixed neighborhood of \(v_n^0\), with
\[
v_n=v_n^0+O(e^{-2a v_n^0}).
\]
Outside these neighborhoods the cosine remains bounded away from zero on each period, so all sufficiently high-frequency zeros are accounted for. The cosine has alternating signs between successive zeros; the exact cospectrum retains that alternation. Consequently the signed cospectrum has infinitely many high-frequency bands with negative cospectral values even though the time-lag covariance is everywhere nonnegative.

**5. Zero positions and recovery.** Substituting \(v_n\) into the strictly increasing map \(\omega(v)\), using \(\sqrt{1+z}=1+z/2-z^2/8+O(z^3)\), yields
\[
\begin{aligned}
\omega_n&=2D(v_n^0)^2+\mu-\frac{\mu^2}{4D(v_n^0)^2}+O(n^{-4})+O(n^2e^{-2a v_n^0})\\
&=\frac{2D\pi^2}{d^2}(n+\tfrac12)^2+\mu+O(n^{-2}).
\end{aligned}
\]
If \(\mu=0\), the displayed algebraic remainder is absent and the leading zero approximation has exponentially small error. Let \(A=\lim_{n\to\infty}\omega_n/(n+1/2)^2\). Then \(d=\pi\sqrt{2D/A}\) and \(\mu=\lim_{n\to\infty}[\omega_n-A(n+1/2)^2]\). The real cospectrum is invariant under \(x\leftrightarrow L-x\), so its zero positions identify only \(|L-2x|\).

## Verification

The standalone file `checks/spectral_two_wall.py` implements the exact complex hitting transforms and their cross-spectrum, independently checks these against the absorbing-heat-kernel eigenfunction expansion of boundary flux, and numerically brackets high-frequency zeros for three parameter families including zero degradation and sources on either side of the midpoint. It tests strict midpoint positivity and conjugate-frequency symmetry. It reports 106 passed comparisons on execution using NumPy and SciPy. These finite tests are diagnostic only: the infinite sign pattern and zero asymptotic follow from the exact exponential estimates in the proof, not from numerical extrapolation.

## Relationship to prior work

Boyer and Mercado-Vásquez (2026) develop stochastic synthesis/degradation with arbitrary single-particle propagators, burst production, density profiles, first-passage distributions and optimization of the first reaction time. Their burst mechanism motivates the present independent-molecule source model. The two-*target* stationary arrival cross-spectrum, its positive time-domain kernel, the strict midpoint exception, infinitely alternating high-frequency cospectral bands, and the zero-based mortality/source-distance identification are distinct questions.

Bartlett's point-process spectral framework (1963), Westcott's Poisson-cluster analysis (1973), and multivariate point-process spectral theory in Hawkes (1971) supply the general cluster/covariance machinery. The exact cluster transfer-product formula in step 2 is not claimed to be novel by itself; neither is the classical one-dimensional absorbing-interval boundary-value solution. The contribution is their physically motivated combination with a proved sharp source-symmetry dichotomy and a two-term zero-ladder law. A general published formula could implicitly imply the specialized result, so independent bibliographic confirmation is still warranted.

## Limitations

The theorem assumes Poisson-timed bursts with independent offspring, constant diffusion and killing rates, two perfectly absorbing boundaries, fixed source location, and a finite second burst-size moment. Correlated trajectories, non-Poisson production clocks, partially reactive boundaries, higher dimensions, and mobile sources are not addressed. Cross-spectrum zeros become exponentially difficult to observe at high frequency because the magnitude of the signal decays like \(e^{-L\sqrt{\omega/(2D)}}\); the result asserts mathematical identifiability from exact spectra, not stable reconstruction from finitely many noisy measurements. The underlying point-process spectrum formula is classical; only the indicated exact special-model sign and zero-ladder classification is assessed here. No claim is made about scientific publication priority or independent validation.

## References

1. D. Boyer and G. Mercado-Vásquez, *Stochastic synthesis and degradation of arbitrary diffusive processes*, arXiv:2611.04843, first submitted 2026-11-03. https://arxiv.org/abs/2611.04843
2. M. S. Bartlett, *The spectral analysis of point processes*, Journal of the Royal Statistical Society B **25** (1963), 264–281. https://doi.org/10.1111/j.2517-6161.1963.tb00508.x
3. M. Westcott, *Results in the asymptotic and equilibrium theory of Poisson cluster processes*, Journal of Applied Probability **10** (1973), 807–823. https://doi.org/10.1017/S0021900200096005
4. A. G. Hawkes, *Spectra of some self-exciting and mutually exciting point processes*, Biometrika **58** (1971), 83–90. https://doi.org/10.1093/biomet/58.1.83
5. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009, first submitted 2018-12-07. https://arxiv.org/abs/1812.03009
