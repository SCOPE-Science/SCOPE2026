# A three-regime optimal-period law for displaced Gaussian reset cycles

## Finding
Consider a periodically restarted one-dimensional Ornstein–Uhlenbeck diffusion. Each cycle begins from a Gaussian law with mean \(\mu\) and variance \(qD\tau\), while the confining equilibrium is centered with variance \(D\tau\). Define the cycle reward to be the *symmetric endpoint Kullback–Leibler divergence*, divided by the cycle length. Write the dimensionless squared displacement \(c=\mu^2/(D\tau)\) and the dimensionless cycle duration \(z=2t/\tau\). For fixed \(c\ge0\), let \(z_q\) be **any** global maximizer of this rate for \(0<q<1\).

As the reset width \(q\downarrow0\), there are exactly three scaling regimes:
\[
\boxed{z_q\sim 2\sqrt{q/(2-c)}}\quad (0\le c<2),\qquad
\boxed{z_q\sim(6q)^{1/3}}\quad(c=2),
\]
\[
\boxed{z_q\longrightarrow z_c>0}\quad(c>2).
\]
For \(c>2\), \(z_c\) is the unique positive maximizer of
\[
H_c(z)=\frac{1-e^{-z}+c(1-e^{-z/2})^2}{z}.
\]
It is characterized by \(z_c N_c'(z_c)=N_c(z_c)\), where \(N_c(z)=1-e^{-z}+c(1-e^{-z/2})^2\). This establishes a sharp displacement threshold \(c=2\): the optimal cycle length shrinks with a square-root law below threshold, a cube-root law exactly at threshold, and tends to a finite fraction of the trap relaxation time above threshold.

## Assumptions and scope
Let \(D,\tau>0\), \(0<q<1\), and \(\mu\in\mathbb R\). Between resets the process solves \(dX_t=-X_t\,dt/\tau+\sqrt{2D}\,dB_t\). At every deterministic time interval \(t>0\), the state is *newly sampled* from \(\mathcal N(\mu,qD\tau)\), independently of preceding cycles. The endpoint divergence \(J\) is \(D_{\rm KL}(P_0\|P_t)+D_{\rm KL}(P_t\|P_0)\); the optimized objective is \(J/t\). This is an observable information-geometric endpoint cost, **not a claim about the complete physical entropy production** of the resetting apparatus.

## Proof
Set \(z=2t/\tau\), \(y=1-e^{-z}\), \(a=1-e^{-z/2}\), and \(u=q+(1-q)y\). The Gaussian Ornstein–Uhlenbeck semigroup gives the final mean \(\mu e^{-z/2}\) and variance \(D\tau u\). The exact symmetric Gaussian divergence is
\[
J(z)=\frac{(u-q)^2}{2qu}+\frac{c a^2}{2}\left(\frac1q+\frac1u\right).
\]
Thus maximizing \(J/t\) is equivalent, for each fixed \(q\), to maximizing
\[
P_{q,c}(z)=\frac{2qJ(z)}z=\frac1z\left\{\frac{(u-q)^2}{u}+c a^2\left(1+\frac qu\right)\right\}.
\]
For every \(q\in(0,1)\) and fixed \(c\ge0\), this positive continuous function tends to zero both as \(z\downarrow0\) and as \(z\to\infty\), so a nonempty compact set of positive finite maximizers exists.

For fixed \(z>0\), as \(q\downarrow0\), \(P_{q,c}(z)\to H_c(z)=N_c(z)/z\) locally uniformly. Writing \(s=e^{-z/2}\), the exact comparison with the boundary value \(H_c(0+)=1\) is
\[
z-N_c(z)=\bigl[z-3+4e^{-z/2}-e^{-z}\bigr]+(2-c)(1-e^{-z/2})^2.
\]
The first bracket is strictly positive for \(z>0\): its derivative is \((1-e^{-z/2})^2>0\), and its value at zero is zero. Therefore \(H_c(z)<1\) at every positive \(z\) when \(c\le2\). If \(c>2\), the expansion \(H_c(z)=1+(c/4-1/2)z+O(z^2)\) gives \(H_c(z)>1\) for sufficiently small positive \(z\).

For \(c>2\), \(N_c''(z)=e^{-z/2}[(c-1)e^{-z/2}-c/2]\), which changes sign exactly once from positive to negative. Since \(d[zN_c'(z)-N_c(z)]/dz=zN_c''(z)\), the derivative numerator of \(H_c\) increases from zero then strictly decreases to \(-(1+c)\). It has exactly one positive root \(z_c\), the unique strict global maximizer. The exact objective has \(\limsup_{q\to0,\ z\to0}P_{q,c}(z)\le1\), while \(P_{q,c}(z_c)\to H_c(z_c)>1\); moreover \(P_{q,c}(z)\to0\) uniformly as \(z\to\infty\) for small \(q\), after rescaling as above. Compactness and local uniform convergence imply that every maximizer tends to \(z_c\).

For \(c\le2\), the same compactness argument using \(H_c(z)<1\), the competitor \(z=q^{1/3}\) (or another shrinking scale with \(q/z\to0\)), and the elementary bound \(\limsup_{q\to0,z\to0}P_{q,c}(z)\le1\), implies every maximizer tends to zero. The precise boundary-layer expansion, valid uniformly for \(q/z\to0\), \(z\to0\), is
\[
P_{q,c}(z)=1-\frac{2-c}{4}z+\left(\frac16-\frac c8\right)z^2-\frac qz
+O\left(z^3+q+\frac{q^2}{z^2}\right).
\]
Indeed it follows by expanding the exact rational-Gaussian expression; the leading \(-q/z\) term is the finite-width correction. A direct comparison with the candidate scales shows that all maximizing sequences satisfy \(q/z\to0\), and the strictly positive losses \(q/z\) and \(z\) (if \(c<2\)), or \(q/z\) and \(z^2\) (if \(c=2\)), prevent a maximizing sequence from escaping either end of the corresponding rescaled compact intervals.

For \(c<2\), substitute \(z=s\sqrt q\) and divide \(1-P_{q,c}(z)\) by \(\sqrt q\). Uniformly on each compact interval in \(s>0\), the limit is \(1/s+(2-c)s/4\), with unique minimizer \(s=2/\sqrt{2-c}\). The localization just established forces all global maximizers to have this limit. At \(c=2\), substitute \(z=sq^{1/3}\): the limiting loss divided by \(q^{2/3}\) is \(1/s+s^2/12\), whose unique minimizer is \(s=6^{1/3}\). This proves all three cases.

## Verification
Run `python verification/check.py` using Python 3 standard libraries. It independently recomputes both Gaussian KL terms, searches the positive time axis, tests near-optimality across displacement and width values, and tests the three limits. These numerical checks corroborate but do not replace the global analytic argument. All limits are for fixed \(c\), not a joint varying-\(c\) crossover window.

## Relationship to prior work
Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, first public 2026-05-27, arXiv:2605.28445v1, derives endpoint KL costs for centered harmonic resetting, giving leading approximations for narrow localization and discussing periodic and Poisson reset clocks. The present result changes the reset law to a Gaussian with a fixed nonzero mean and proves an **offset-triggered singular three-regime optimizer classification** not implied by centered narrow-width formulas. The older general thermodynamics of resetting of Fuchs, Goldt and Seifert (2016) does not supply this displaced-Gaussian endpoint optimization. A separate existing calculation concerns centered Gaussian resets with a *Poisson* clock; it does not imply this deterministic-clock, displaced-mean threshold. The Gaussian divergence formula itself and OU variance evolution are standard and are not claimed as new.

## Limitations
The reset event is an imposed Gaussian resampling, without an implementation-specific work or entropy model. Only the optimized symmetric *endpoint* divergence is classified. There is no claim of uniqueness of the finite-width optimum for arbitrary \(q\), no result for arbitrary reset-time distributions, and no uniform expansion as \(c\to2\) together with \(q\to0\). Independent novelty and correctness assessment remains outstanding, especially for other Gaussian-control literature not accessible in full.

## References
1. O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, arXiv:2605.28445v1 (first submitted 2026-05-27), https://arxiv.org/html/2605.28445v1.
2. J. Fuchs, S. Goldt, U. Seifert, *Stochastic thermodynamics of resetting*, Europhys. Lett. 113, 60009 (2016), arXiv:1603.01141, https://arxiv.org/abs/1603.01141.
3. M. R. Evans, S. N. Majumdar, G. Schehr, *Stochastic resetting and applications*, J. Phys. A 53, 193001 (2020), https://doi.org/10.1088/1751-8121/ab7cfe.
