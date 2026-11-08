# Sharp kurtosis envelope and refresh-clock calibration for Brownian diffusion with random resetting intensity

## Finding

Consider stationary one-dimensional Brownian diffusion of generator \(D\partial_{xx}\), \(D>0\), reset to the origin at its current stochastic intensity \(\Lambda_t\). The intensity is an autonomous piecewise-constant process: at independent Poisson times of rate \(\mu>0\), it is redrawn from a fixed law \(\nu\), while particle-reset events leave it unchanged. Suppose \(\nu\) is supported on finite nonnegative intensities and \(\nu((0,\infty))>0\). Let \(X_\mu\) be the stationary position and put
\[
U_\mu=(\mu+\Lambda)^{-1},\qquad a_j(\mu)=\mathbb E[U_\mu^j],\quad\Lambda\sim\nu.
\]
The stationary excess kurtosis (relative to Gaussian kurtosis three) is exactly
\[
K(\mu)=\frac{\mathbb E[X_\mu^4]}{(\mathbb E[X_\mu^2])^2}-3
=6\frac{a_2(\mu)}{a_1(\mu)^2}-3
=3+6\frac{\operatorname{Var}(U_\mu)}{a_1(\mu)^2}.
\]
For every non-point-mass \(\nu\), \(K(\mu)>3\) is **strictly decreasing and strictly convex** on \((0,\infty)\), with \(K(\mu)\downarrow3\) as \(\mu\to\infty\). Consequently, for a known nondegenerate intensity law, every admissible kurtosis greater than three identifies a unique refresh rate. These strict conclusions hold even when the intensity has an atom at zero or lacks a finite mean.

If \(\nu\) is supported on a known interval \([a,b]\), \(0\le a<b<\infty\), the sharp distribution-free envelope at every fixed refresh rate is
\[
3\le K(\mu)\le 3+\frac{3(b-a)^2}{2(\mu+a)(\mu+b)}.
\]
The lower equality holds exactly for a point-mass intensity law. The upper equality holds exactly for the endpoint law assigning probability \((\mu+a)/(2\mu+a+b)\) to intensity \(a\) and the remaining probability to intensity \(b\). In particular, for a fixed binary intensity law with \(\Pr(\Lambda=a)=p\in(0,1)\) and \(\Pr(\Lambda=b)=1-p\), the exact calibration relation is
\[
K(\mu)=3+\frac{6p(1-p)(b-a)^2}{[\mu+pb+(1-p)a]^2},
\quad
\mu=\sqrt{\frac{6p(1-p)(b-a)^2}{K-3}}-[pb+(1-p)a],
\]
where the inverse is restricted to the stated physical range \(\mu>0\).

## Assumptions and scope

The rate environment is refreshed independently of Brownian motion and of the conditional particle-reset clock. After each redraw, conditional on the current intensity, particle resets have Poisson hazard \(\Lambda_t\); a particle reset does not redraw the intensity. Redraws of the same intensity are allowed. The environment law \(\nu\) is otherwise arbitrary, with \(\Lambda<\infty\) almost surely and positive mass on \((0,\infty)\). In the nondegenerate theorem, it is not a point mass. The stationary even moments in the formulas refer to the stationary joint process of position and intensity, not to a renewal protocol that redraws the intensity at every particle reset. No smoothness or density of \(\nu\) is assumed. The supported-interval envelope requires no constraint on the mean of \(\Lambda\).

## Proof

**Existence and moment finiteness.** Start the rate environment in its invariant redraw law \(\nu\). Let \(S(t)\) be the probability of no particle reset in a time interval of length \(t\), averaged over this stationary environment. Conditioning on the first intensity redraw gives the nonnegative renewal equation
\[
S(t)=e^{-\mu t}\mathbb E[e^{-\Lambda t}]
+\int_0^t\mu e^{-\mu s}\mathbb E[e^{-\Lambda s}]S(t-s)\,ds.
\]
For \(A(z)=\mathbb E[(z+\Lambda)^{-1}]\), its Laplace transform satisfies
\[
\widetilde S(q)=\frac{A(\mu+q)}{1-\mu A(\mu+q)}.
\]
Because \(\mu A(\mu)=\mathbb E[\mu/(\mu+\Lambda)]<1\), continuity permits some sufficiently small \(\epsilon>0\) for which \(\widetilde S(-\epsilon)<\infty\). Hence the reset-free age has an exponentially decaying tail. The two-sided stationary environment and a conditional reset clock consequently define a unique stationary position via Brownian increments since the last reset; every positional moment is finite.

**Exact moments, independently from the generator.** Write \(s=Dk^2\) and let \(\Phi(s)=\mathbb E[e^{ikX_\mu}]\). For the stationary rate-position joint law, test the generator with \(e^{ikx}g(\lambda)\). The resulting Fourier-measure equation is
\[
(\lambda+\mu+s)H_s(d\lambda)
=[\lambda+\mu\Phi(s)]\nu(d\lambda).
\]
Integrating yields the previously known stationary Fourier transform
\[
\Phi(s)=\frac{1-(\mu+s)A(\mu+s)}{1-\mu A(\mu+s)}
=1-\frac{sA(\mu+s)}{1-\mu A(\mu+s)}.
\]
Set \(a_j=\mathbb E[(\mu+\Lambda)^{-j}]\), and \(B=1-\mu a_1>0\). Differentiation at \(s=0\) gives the exact second and fourth moments
\[
\mathbb E[X_\mu^2]=\frac{2Da_1}{B},
\qquad
\mathbb E[X_\mu^4]=\frac{24D^2a_2}{B^2}.
\]
They can also be recovered without Fourier differentiation: the conditional stationary second-moment measure is \([2D+\mu\mathbb E X_\mu^2](\mu+\lambda)^{-1}\nu(d\lambda)\), and the conditional fourth-moment measure obeys the analogous equation with source \(12D\) times the conditional second-moment measure. Solving those two linear equations yields the same formulas. Their ratio proves the kurtosis identity and removes \(D\) entirely.

**Strict shape in the refresh parameter.** Differentiation is justified for every \(\mu>0\) by boundedness of \((\mu+\Lambda)^{-j}\), and \(a_j'(\mu)=-j a_{j+1}(\mu)\). Let \(U,V\) be independent copies of \(U_\mu\). Then
\[
K'(\mu)=\frac{12(a_2^2-a_1a_3)}{a_1^3}
=-\frac{6\mathbb E[UV(U-V)^2]}{a_1^3}<0,
\]
when \(\nu\) is nondegenerate. A second exact differentiation gives
\[
K''(\mu)=\frac{36(a_1^2a_4-2a_1a_2a_3+a_2^3)}{a_1^4}
=\frac{36\mathbb E\{U^2[U-a_2/a_1]^2\}}{a_1^2}>0.
\]
The strict inequalities follow because the map \(\lambda\mapsto(\mu+\lambda)^{-1}\) is injective and the weights are positive. As \(\mu\to\infty\), \(\mu U_\mu\to1\) almost surely and is bounded by one; dominated convergence gives \(\mu a_1\to1\) and \(\mu^2a_2\to1\). Therefore \(K\to3\). By continuity and strict decrease, the map from positive refresh rates onto \((3,K(0+))\), where the endpoint may be infinite, is one-to-one and onto.

**Sharp support envelope.** When \(\Lambda\in[a,b]\), write \(L=(\mu+b)^{-1}\), \(H=(\mu+a)^{-1}\); then \(L\le U\le H\). The pointwise inequality \((U-L)(H-U)\ge0\) gives \(\mathbb E U^2\le (L+H)m-LH\), where \(m=\mathbb E U\). Maximizing \([(L+H)m-LH]/m^2\) for \(m\in[L,H]\) gives \((L+H)^2/(4LH)\), attained only at \(m=2LH/(L+H)\) with an endpoint-supported \(U\). Its probability of \(U=H\) is \(L/(L+H)=(\mu+a)/(2\mu+a+b)\). Substitution produces the asserted sharp upper bound. Cauchy–Schwarz gives the lower bound and its equality condition. For a two-point intensity law, direct computation yields
\[
\frac{\operatorname{Var}(U)}{(\mathbb E U)^2}
=\frac{p(1-p)(b-a)^2}{[\mu+pb+(1-p)a]^2},
\]
which proves the binary formula and its physical inverse.

## Verification

Run `python verify.py` using the standard Python library. The checker evaluates exact rational moment identities for 2- and 3-rate environments; independently verifies the conditional stationary-generator balances; checks the exact negative-square first derivative and positive-square second derivative; tests the sharp support bound including its equality cases; and compares the two-rate closed form and strictly decreasing grid. The supplied run completed **228 exact-arithmetic parameter evaluations** and the stated structural identities. The finite tests are diagnostic only: the proof above, not testing, covers arbitrary intensity distributions.

For example, with \(a=1\), \(b=4\), \(p=2/5\), \(\mu=D=1\), the exact values are \(\mathbb E X^2=16/17\), \(\mathbb E X^4=1860/289\), and \(K=273/64\).

## Relationship to prior work

Arutkin and Reuveni (2025), Section 4, Eq. (23), derive the general stationary Fourier transform for independently refreshed reset rates; that transform and the known fixed-rate Laplace distribution are **prior results**. They imply the raw moment formulas by differentiation. The contribution claimed here is the cross-refresh **strict decreasing-convex law of normalized excess kurtosis**, the sharp support-dependent envelope with equality classification, and the rate-calibration consequence; these are not presented in the inspected primary article. A previously obtained localization-order result for the same protocol compares unnormalized radial tails and power moments; such ordering by itself does not order their normalized fourth-to-second-moment ratio. The search for equivalent fourth-moment and rate-calibration statements found no direct match but is not a proof of global priority.

Olsen and Löwen (2024) study partial resets with refractory periods, not persistent independently redrawn reset intensity. Santra and Das (2026) study a viscoelastic bath with a fixed reset rate and persistent bath memory; its kurtosis regime is different. These are relevant contrasts, not claimed as equivalent formulations.

## Limitations

These results address the stationary one-time position distribution, not first-passage search performance, time-dependent relaxation, energetic cost, or an environment whose rate is redrawn when the particle resets. The two-point inverse assumes the rate values and mixing weight are independently known. In an experimental setting, finite-sample fourth moments may be noisy, especially when refresh is very slow. The general shape theorem follows from the previously established Fourier transform together with new moment inequalities; claims of priority over all possible unpublished or unindexed analyses cannot be made. Independent audit has not been performed.

## References

- M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting*, arXiv:2509.25365 (first public version September 29, 2025), especially Section 4, Eq. (23). https://arxiv.org/abs/2509.25365
- M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, Physical Review Letters 106, 160601 (2011); arXiv:1102.2704. https://arxiv.org/abs/1102.2704
- K. Stølevik Olsen and H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039 (2024). https://arxiv.org/abs/2406.10039
- I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, New Journal of Physics 28, 074601 (2026). https://doi.org/10.1088/1367-2630/ae868c
