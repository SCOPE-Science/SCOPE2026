# Observable-dependent variance cost of periodic Poisson-window sampling

## Finding

Consider a one-dimensional point-process sampler whose arrival intensity is periodically modulated but whose one-unit sliding-window count remains Poisson-distributed at every observation time. **Uniform arrival intensity minimizes the asymptotic variance of the continuous-time average of every square-integrable observable of the count.** Equality for a genuinely nonuniform periodic intensity occurs exactly for affine observables. In particular, the linear count average is completely insensitive to the modulation, while every nonlinear observable incurs a strictly positive variance penalty.

For the natural second-factorial-moment observable \(h(n)=n(n-1)\), the penalty admits the explicit exact Fourier formula

\[
\mathcal V_h(\eta)=4\lambda^3+\frac43\lambda^2+\frac{2\lambda^2}{\pi^2}\sum_{k\in\mathbb Z\setminus\{0\}}\frac{|\widehat\eta_k|^2}{k^2},
\qquad
\widehat\eta_k=\int_0^1\eta(t)e^{-2\pi i kt}\,dt.
\]

Thus a single sinusoidal perturbation \(\eta(t)=1+\varepsilon\cos(2\pi\ell t)\), with integer \(\ell\ge1\) and \(|\varepsilon|<1\), causes an exact extra variance \(\lambda^2\varepsilon^2/(\pi^2\ell^2)\). The corresponding extra variance for the linear count observable is zero.

## Assumptions and scope

Fix \(\lambda>0\). Let \(\eta:\mathbb R\to(0,\infty)\) be measurable, one-periodic, bounded above and bounded away from zero, with \(\int_0^1\eta(t)\,dt=1\). Let \(N\) be the two-sided nonhomogeneous Poisson point process of deterministic intensity \(\lambda\eta(t)\,dt\), and let

\[
S(t)=N((t-1,t]),\qquad t\in\mathbb R.
\]

For any \(h:\mathbb Z_{\ge0}\to\mathbb R\) with \(\mathbb E[h(P)^2]<\infty\) for \(P\sim\operatorname{Poisson}(\lambda)\), put \(\mu_h=\mathbb E h(P)\) and \(\widehat\mu_{h,T}=T^{-1}\int_0^T h(S(t))\,dt\). This observable uses **physical time**, not event index or an operational-clock average. Define \(\mathcal V_h(\eta)=\lim_{T\to\infty}T\operatorname{Var}(\widehat\mu_{h,T})\).

Use the monic Poisson–Charlier polynomials

\[
C_r(n;\lambda)=\sum_{j=0}^r {r\choose j}(-\lambda)^{r-j}(n)_j,
\quad (n)_j=n(n-1)\cdots(n-j+1),
\]

with \((n)_0=1\), and the unique expansion in \(L^2(\operatorname{Poisson}(\lambda))\):

\[
h(n)-\mu_h=\sum_{r\ge1}c_r C_r(n;\lambda),
\qquad \sum_{r\ge1}c_r^2r!\lambda^r<\infty.
\]

For \(0\le v\le1\) set \(J_v(t)=\int_{t+v-1}^t\eta(s)\,ds\), with \(0\le J_v(t)\le1\). Then the full variance formula is

\[
\boxed{\mathcal V_h(\eta)=2\sum_{r\ge1}c_r^2r!\lambda^r
\int_0^1\!\int_0^1 J_v(t)^r\,dt\,dv.}
\]

Moreover, \(\sqrt T(\widehat\mu_{h,T}-\mu_h)\) converges in law to a centered Gaussian of variance \(\mathcal V_h(\eta)\). For \(\eta\equiv1\), this variance is \(\sum_{r\ge1}2c_r^2r!\lambda^r/(r+1)\). For arbitrary admissible \(\eta\), it is no smaller. If \(\eta\) is not almost everywhere constant, equality holds if and only if \(h(n)=a+bn\) for all nonnegative integers \(n\).

This theorem is specific to the Poisson target, a common deterministic window length, positive deterministic periodic intensities, square-integrable test functions, and physical-time averaging. It does not assert a comparable optimization for interacting multivariate samplers, non-Poisson targets, or event-indexed efficiency.

## Proof

**1. The fixed one-time target.** One-periodicity and normalization imply \(\int_{t-1}^t\eta(s)\,ds=1\). Hence \(S(t)\sim\operatorname{Poisson}(\lambda)\) for every \(t\). The point process is a particular independent-coordinate, deterministic-service-time sampler with periodically modulated base intensity.

**2. Exact two-window covariance.** For \(0\le v\le1\), the overlap between \((t-1,t]\) and \((t+v-1,t+v]\) contains a Poisson count of mean \(\lambda J_v(t)\), and the two disjoint remainders have independent Poisson counts. The exponential generating function of the Charlier polynomials is

\[
 e^{-\lambda z}(1+z)^n=\sum_{r\ge0}C_r(n;\lambda)\frac{z^r}{r!}.
\]

Taking the expectation of the product of the generating functions for the two window counts gives exactly \(\exp(\lambda J_v(t)zu)\). Coefficient comparison yields

\[
\mathbb E[C_r(S(t);\lambda)C_s(S(t+v);\lambda)]
=\mathbf1_{\{r=s\}}\,r!\lambda^r J_v(t)^r.
\]

The Charlier polynomials form a complete orthogonal family in Poisson \(L^2\), with squared norms \(r!\lambda^r\). Expansion and \(L^2\)-convergence therefore give

\[
\operatorname{Cov}(h(S(t)),h(S(t+v)))
=\sum_{r\ge1}c_r^2r!\lambda^rJ_v(t)^r.
\]

The covariance is zero for \(|v|\ge1\), since nonoverlapping Poisson increments are independent. Its nonnegative terms are bounded in sum by \(\operatorname{Var}(h(P))\). Periodic averaging of the finite-range covariance over the physical interval \([0,T]\) now proves the boxed variance formula, including existence and finiteness.

**3. Sharp optimality and equality.** Fubini and periodicity give \(\int_0^1J_v(t)\,dt=1-v\). Jensen's inequality implies \(\int_0^1J_v(t)^r\,dt\ge(1-v)^r\) for every integer \(r\ge1\). Equality always holds for \(r=1\). For any \(r\ge2\), equality requires \(J_v\) to be constant almost everywhere in \(t\). If \(\eta\) has any nonzero Fourier mode \(\widehat\eta_k\) with \(k\ne0\), the corresponding Fourier mode of \(J_v\) is proportional to \(\widehat\eta_k(1-e^{2\pi ikv})/(2\pi ik)\), nonzero for almost every \(v\). Therefore Jensen's inequality is strict on a set of positive \(v\)-measure. Thus nonconstant \(\eta\) has strictly larger variance if any \(c_r\ne0\) for \(r\ge2\); equality means that \(h\) is affine. Since a Poisson law with positive parameter charges every nonnegative integer, this equality is pointwise on the count state space.

**4. Exact second-factorial-moment penalty.** For \(h(n)=(n)_2\),

\[
h(n)-\lambda^2=C_2(n;\lambda)+2\lambda C_1(n;\lambda).
\]

The covariance therefore equals \(4\lambda^3J_v(t)+2\lambda^2J_v(t)^2\). Parseval applied to the Fourier coefficients of the interval integral \(J_v\) gives

\[
\int_0^1J_v(t)^2\,dt
=(1-v)^2+\sum_{k\ne0}|\widehat\eta_k|^2
\frac{|1-e^{2\pi ikv}|^2}{4\pi^2k^2}.
\]

Since \(\int_0^1|1-e^{2\pi ikv}|^2\,dv=2\) for nonzero integer \(k\), integrating in \(v\) yields

\[
\int_0^1\int_0^1J_v(t)^2\,dt\,dv
=\frac13+\frac1{2\pi^2}\sum_{k\ne0}\frac{|\widehat\eta_k|^2}{k^2}.
\]

Insertion into the covariance integral proves the explicit variance formula and the sinusoidal example. For \(h(n)=n\), only \(c_1=1\) is nonzero, giving \(\mathcal V_h(\eta)=\lambda\) for all allowed modulation profiles.

**5. Central limit theorem.** For each integer \(j\), let \(Y_j=\int_j^{j+1}[h(S(t))-\mu_h]\,dt\). This stationary sequence is one-dependent: \(Y_j\) is measurable with respect to Poisson points in \((j-1,j+1]\), and two such blocks at index distance at least two use disjoint Poisson increments. Square integrability follows by Jensen and the bounded second moment of \(h(P)\). The standard stationary one-dependent central limit theorem gives Gaussian limits, with asymptotic variance equal to the covariance-integral limit above. The remaining fraction of a noninteger observation horizon contributes \(o_{L^2}(\sqrt T)\).

## Verification

The accompanying standalone standard-library Python program `verify.py` performs exact rational bivariate-Poisson/Charlier polynomial comparisons through degree three, independent Fourier-integral diagnostics, and physical-clock overlap-integral checks for sinusoidal modulations. It prints `PASS final total 324 algebraic and numerical diagnostics` when run with a current Python 3 interpreter. Finite tests check algebraic identities and numerical integration only; the infinite-observable theorem and central limit theorem are justified in the proof, not by test counts.

Reproduction: run `python3 verify.py` in a directory containing the file. No external packages, data, or downloads are required.

## Relationship to prior work

Stewart and Sahani (arXiv:2603.09089, first public March 10, 2026) construct sliding-window point-process samplers with a specified count distribution and explicitly ask how oscillatory base intensities affect mixing and asymptotic variance. The present result answers the asymptotic-variance question in the one-dimensional Poisson-target family with unit-period intensities and unit-width windows, for every square-integrable count observable. It does **not** claim the original sampler, the Poisson target construction, or Charlier orthogonality as new.

Classical Poisson-window and infinite-server queue covariance theory, and the integer-valued trawl-process framework of Barndorff-Nielsen, Lunde, Shephard and Veraart, supply important ingredients. Veraart (arXiv:2303.04121) studies stationary periodic-trawl processes and proves central limit theorems for their sampled means, autocovariances and estimators. Its stationary moving-average kernel setting differs from the cyclostationary nonhomogeneous-Poisson arrival construction here; neither its displayed covariance identities nor its main limit theorems imply the sharp all-observable intensity minimization and Fourier penalty without additional argument. The present optimality/equality classification and the precise second-factorial-moment penalty were not found stated in the inspected sources. A more general established result may subsume the calculation; independent priority review remains necessary.

## Limitations

The result concerns physical-time averages of the count process, not event-sampled chain effective sample sizes. All profiles have period exactly equal to the window length and integral one. The optimality conclusion is not proved for multitype coupled arrival processes, non-Poisson marginals, nonperiodic rates, or random observation schedules. A smoothness assumption is unnecessary; bounded positive measurable profiles suffice. Deterministic finite diagnostics do not certify novelty, and no independent mathematical audit has been performed.

## References

1. C. A. Stewart and M. Sahani, *Sampling on Discrete Spaces with Temporal Point Processes*, arXiv:2603.09089 (v1 March 10, 2026), especially Sections 3 and 7, https://arxiv.org/html/2603.09089.
2. O. E. Barndorff-Nielsen, A. Lunde, N. Shephard and A. E. D. Veraart, *Integer-valued trawl processes: A class of stationary infinitely divisible processes*, Scandinavian Journal of Statistics 41 (2014), 693–724, DOI:10.1111/sjos.12056; open author manuscript https://shephard.scholars.harvard.edu/sites/g/files/omnuum7741/files/GeneralTrawlPaper.pdf.
3. A. E. D. Veraart, *Periodic trawl processes: Simulation, statistical inference and applications in energy markets*, arXiv:2303.04121v2 (July 19, 2023), Sections 2, 4 and 6, https://arxiv.org/html/2303.04121v2.
4. Standard Poisson–Charlier polynomial generating-function and orthogonality identities, explicitly derived in the proof above.
