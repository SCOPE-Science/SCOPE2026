# Sharp collective-mean boundary layers for a telegraph-driven harmonic gas

## Finding

For a stationary gas of \(N\) independent thermal particles confined by one harmonically driven, telegraph-switching trap center, the collective sample mean develops a universal, parameter-sensitive boundary layer outside the compact support of its large-\(N\) limit. The exact finite-\(N\) conditional-Gaussian representation below, already implicit in the cited stationary law, is input rather than a new claim. The contribution is the sharp boundary-layer, selection, and exterior-tail classification derived from it.

Put \(B=v_0/\mu\), \(\sigma=\sqrt{D/\mu}\), \(\nu=\gamma/\mu\), \(c_\nu=[(2B)^\nu\mathrm{B}(\nu,\nu)]^{-1}\), and let \(\overline\Phi\) be the survival function of a standard normal. Define
\[
 J_\nu(\xi;\sigma)=\int_0^\infty w^{\nu-1}\overline\Phi((\xi+w)/\sigma)\,dw.
\]
For every fixed real \(\xi\), as \(N\to\infty\),
\[
 \Pr\{C_N>B+\xi/\sqrt N\}\sim c_\nu N^{-\nu/2}J_\nu(\xi;\sigma),
\]
with convergence of the normalized probabilities uniform over compact intervals of \(\xi\). At the limiting support edge, the prefactor is explicit:
\[
 \Pr(C_N>B)\sim
 \frac{\sigma^\nu 2^{\nu/2-1}\Gamma((\nu+1)/2)}{\nu\sqrt\pi\,(2B)^\nu\mathrm{B}(\nu,\nu)}N^{-\nu/2}.
\]
Thus the collective overshoot exponent is the tunable ratio \(\gamma/(2\mu)\), although every individual particle has unbounded Gaussian thermal fluctuations.

There is also a conditional endpoint-selection law. On \(\{C_N>B\}\), the hidden common center approaches the maximal deterministic drive with \(\sqrt N\)-scaled gap \(W_N=\sqrt N(B-U)\); its conditional distribution converges to the probability density
\[
 f_{\rm edge}(w)=\frac{w^{\nu-1}\overline\Phi(w/\sigma)}{J_\nu(0;\sigma)},\qquad w>0.
\]
For each \(\xi\ge0\), the conditional overshoot has the nondegenerate limiting survival function
\[
 \lim_{N\to\infty}\Pr\{\sqrt N(C_N-B)>\xi\mid C_N>B\}
 =\frac{J_\nu(\xi;\sigma)}{J_\nu(0;\sigma)}.
\]

Outside the boundary layer there is a different, exponentially small regime. For each bounded positive sequence \(\delta_N\) such that \(\sqrt N\,\delta_N\to\infty\),
\[
 \Pr\{C_N>B+\delta_N\}\sim
 \frac{\Gamma(2\nu)}{\Gamma(\nu)}
 \frac{\sigma^{2\nu+1}}{\sqrt{2\pi}(2B)^\nu\delta_N^{\nu+1}}
 N^{-\nu-1/2}\exp\!\left[-\frac{N\delta_N^2}{2\sigma^2}\right].
\]
All these statements have exact lower-edge analogues by reflection.

## Assumptions and scope

Fix \(\mu,D,v_0,\gamma>0\), and any integer \(N\ge1\). The particles obey the overdamped stochastic differential equations
\[
 dX_i(t)=-\mu[X_i(t)-z(t)]\,dt+\sqrt{2D}\,dW_i(t),
 \qquad z(t)=\frac{v_0}{\mu}S(t),
\]
where \(S(t)\in\{-1,+1\}\) is an independent symmetric telegraph process switching sign at rate \(\gamma\), and \(W_i\) are independent standard Wiener processes. All probabilities refer to their unique stationary joint law; the number \(N\) of particles tends to infinity with the physical parameters fixed. The observable is the empirical particle center \(C_N=N^{-1}\sum_{i=1}^N X_i\), **not** the instantaneous trap center \(z(t)\). The auxiliary variable \(U\) is the exponentially filtered common center, which differs from \(z(t)\).

Write \(T\sim\operatorname{Beta}(\nu,\nu)\), and let \(Z\) be independent standard normal. The exact known stationary decomposition is
\[
 C_N\stackrel d=U+\frac\sigma{\sqrt N}Z,
 \qquad U=B(2T-1),\qquad -B<U<B.
\]
The density of \(Y=B-U\) on \((0,2B)\) is
\[
 g(y)=c_\nu y^{\nu-1}\left(1-\frac{y}{2B}\right)^{\nu-1}.
\]
The beta function \(\mathrm B(\nu,\nu)=\Gamma(\nu)^2/\Gamma(2\nu)\). The strict positive-temperature condition \(D>0\) is essential to the outside-support leakage.

## Proof

**1. Exact reduction.** Solve the linear particle equation back from stationarity. The drive-dependent term is the same for all particles and equals the filtered telegraph process \(U\) satisfying \(\dot U=-\mu U+v_0 S(t)\); the independent stochastic-convolution terms are centered stationary Gaussians with variance \(D/\mu=\sigma^2\). Hence their mean is exactly Gaussian of variance \(\sigma^2/N\) and independent of \(U\). The stationary telegraph-filter density is the beta density above, as in the source paper. Therefore, for every threshold offset \(a\in\mathbb R\),
\[
 P_N(a):=\Pr(C_N>B+a)=\int_0^{2B}c_\nu y^{\nu-1}
 \left(1-\frac{y}{2B}\right)^{\nu-1}
 \overline\Phi\left(\frac{\sqrt N(a+y)}\sigma\right)dy.\tag{1}
\]
This identity is exact at every finite \(N\).

**2. Sharp \(N^{-1/2}\) boundary layer.** Put \(a=\xi/\sqrt N\) and \(w=\sqrt Ny\) in (1). Factoring out \(c_\nu N^{-\nu/2}\) leaves
\[
 \int_0^{2B\sqrt N}w^{\nu-1}
 \left(1-\frac{w}{2B\sqrt N}\right)^{\nu-1}
 \overline\Phi((\xi+w)/\sigma)\,dw.\tag{2}
\]
On each bounded \(w\)-interval, the middle factor converges uniformly to one, and the integrand is integrable at zero because \(\nu>0\). For \(w\ge R\) with \(w\le B\sqrt N\), a Gaussian survival bound dominates uniformly for \(\xi\) in a compact set. The remaining portion \(B\sqrt N\le w\le2B\sqrt N\) is exponentially small, even when \(\nu<1\), since its beta density is integrable. Dominated convergence with these explicit bounds proves (2) tends to \(J_\nu(\xi;\sigma)\) uniformly on compact \(\xi\)-sets. At zero, Tonelli's theorem gives \(J_\nu(0;\sigma)=\mathbb E[(\sigma Z)_+^\nu]/\nu\). The positive normal moment equals \(\sigma^\nu 2^{\nu/2-1}\Gamma((\nu+1)/2)/\sqrt\pi\), proving the edge coefficient.

**3. Selected hidden-center and overshoot laws.** Before integrating (2), its measure is exactly the joint unnormalized distribution of \(W_N=\sqrt N(B-U)\) and the event \(\{C_N>B\}\). Divide by the edge probability and apply the same integrable convergence argument to obtain \(f_{\rm edge}\). Since \(\{C_N>B+\xi/\sqrt N\}\subset\{C_N>B\}\) for \(\xi\ge0\), dividing the two boundary-layer asymptotics yields the stated conditional overshoot survival ratio.

**4. Exterior and moderate-deviation region.** In (1) put \(a=\delta_N>0\). For \(\sqrt N\delta_N\to\infty\), the normal Mills expansion is uniform in \(y\ge0\):
\[
 \overline\Phi\left(\frac{\sqrt N(\delta_N+y)}\sigma\right)
 =\frac\sigma{\sqrt{2\pi N}(\delta_N+y)}
 \exp\left[-\frac{N(\delta_N+y)^2}{2\sigma^2}\right]
 (1+o(1)).
\]
Factor out \(\exp[-N\delta_N^2/(2\sigma^2)]\) and substitute \(y=\sigma^2t/(N\delta_N)\). Since \(N\delta_N^2\to\infty\), the Gaussian exponent becomes \(-t+o(1)\), and the algebraic factors tend to \(t^{\nu-1}\) times the stated global coefficient. The endpoint \(y=2B\) contributes exponentially less than the \(y=0\) region, also for \(0<\nu<1\). Dominated Laplace convergence gives \(\Gamma(\nu)\) for the remaining integral, yielding
\[
 \frac{c_\nu\Gamma(\nu)\sigma^{2\nu+1}}
 {\sqrt{2\pi}\,\delta_N^{\nu+1}}
 N^{-\nu-1/2}e^{-N\delta_N^2/(2\sigma^2)}(1+o(1)).
\]
Use \(c_\nu\Gamma(\nu)=\Gamma(2\nu)/[(2B)^\nu\Gamma(\nu)]\) to obtain the displayed result. It covers both each fixed exterior offset and exterior offsets tending to zero more slowly than \(N^{-1/2}\). Symmetry of \(U\) and \(Z\) proves the lower-edge statements.

## Verification

The standalone `check.py` reconstructs the exact beta-density integral with high-precision quadrature, independently evaluates the edge, uniform-window, exterior, and conditional-center limits, and compares the resulting expressions for several noninteger and integer values of \(\nu\). It also verifies an exact finite-\(N\) closed-form identity at \(\nu=1\). It reports 46 passing diagnostic assertions. These finite numerical diagnostics check formulas and normalization; they are **not** substituted for the analytical limit arguments.

## Relationship to prior work

Sabhapandit and Majumdar, arXiv:2404.02480v1, establish the exact Gaussian conditional independence law and the beta-distributed common center for a telegraphically driven trap. Those formulas and the source's stationary density, correlations, order/gap statistics and counting statistics are not new here. Biroli, Larralde, Majumdar and Schehr, arXiv:2307.15351v1, derive general conditional-i.i.d. sample-mean Fourier formulas and the leading macroscopic sample-mean limit. In this Gaussian specialization their integral framework already determines the full finite-\(N\) law, but it does not state the sharp outside-support \(N^{-\nu/2}\) boundary layer, the conditional endpoint-selection distribution, or the exponentially small fixed-exterior prefactor. The present result isolates these nonuniform rare-event regimes and their measurable exponent and constants. Biroli, Kulkarni, Majumdar and Schehr, arXiv:2312.02570v1, instead study a trap with a switching *stiffness* and a different variance-mixture structure; their extreme-particle analysis does not imply this mean-displacement result.

## Limitations

The asymptotic results require an infinite stationary ensemble, strictly positive thermal diffusivity, symmetric two-state telegraph modulation, and fixed positive physical parameters. They do not provide uniform error estimates if \(\nu\), \(B\), or \(\sigma\) also vary with \(N\), nor guarantees for noisy experimental estimates of the tiny exterior probabilities. The prior Gaussian-beta mixture formula already implies the exact finite-\(N\) distribution; the claimed novelty is specifically its derived sharp rare-collective-event classification, not a new stationary measure, a new conditional-i.i.d. representation, or a general unknown theory of Gaussian convolution.

## References

- S. Sabhapandit and S. N. Majumdar, *Noninteracting particles in a harmonic trap with a stochastically driven center*, arXiv:2404.02480v1 (first public version, April 3, 2024), https://arxiv.org/abs/2404.02480.
- M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351v1 (July 28, 2023), https://arxiv.org/abs/2307.15351.
- M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570v1 (December 5, 2023), https://arxiv.org/abs/2312.02570.
