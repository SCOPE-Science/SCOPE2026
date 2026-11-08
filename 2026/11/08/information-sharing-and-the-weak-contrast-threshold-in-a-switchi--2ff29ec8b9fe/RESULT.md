# Information sharing and the weak-contrast threshold in a switching harmonic gas

## Finding

A stationary gas of noninteracting Brownian particles in a *common*, randomly switching harmonic trap has exactly zero covariance between the positions of distinct particles, yet two large disjoint particle groups share an unbounded amount of Shannon mutual information. The following theorem gives its exact finite-population formula, the sharp large-population constant, and a continuous critical crossover as the two trap stiffnesses merge.

**Theorem.** Fix \(D>0\), \(\mu_1>\mu_2>0\), and transition rates \(r_1,r_2>0\). Put
\[
 a=\frac{r_1}{2\mu_1},\quad b=\frac{r_2}{2\mu_2},\quad c_1=\frac1{\mu_1},\quad c_2=\frac1{\mu_2},\quad
 J=c_1\mathrm B(a,b+1)+c_2\mathrm B(a+1,b),
\]
and let \(U\in(0,1)\) have density
\[
 q(u)=\frac{u^{a-1}(1-u)^{b-1}[c_1(1-u)+c_2u]}{J}.
\]
Define \(W=\log(D[c_1(1-U)+c_2U])\), and let \(Z_k=\log(\chi_k^2/k)\), independently of \(W\), for each positive integer \(k\). Here \(h\) denotes differential entropy in natural units, and \(I\) denotes Shannon mutual information. For disjoint stationary groups \(\mathbf X^{(n)}\) and \(\mathbf Y^{(m)}\) of sizes \(n,m\ge1\), define \(F_k=h(W+Z_k)-h(Z_k)\). Then
\[
 \boxed{I(\mathbf X^{(n)};\mathbf Y^{(m)})=F_n+F_m-F_{n+m}.}\tag{1}
\]
Moreover, as both \(n,m\to\infty\), with no ratio restriction,
\[
 \boxed{I(\mathbf X^{(n)};\mathbf Y^{(m)})
 =\frac12\log\frac{nm}{n+m}+h(W)-\frac12\log(4\pi e)+o(1).}\tag{2}
\]
For equal group sizes this is \(\tfrac12\log n+h(W)-\tfrac12\log(8\pi e)+o(1)\). The nonuniversal constant is an explicit one-dimensional integral:
\[
 h(W)=-\int_0^1q(u)\log\!\left(\frac{q(u)[c_1(1-u)+c_2u]}{c_2-c_1}\right)du.\tag{3}
\]
Every mutual information above is independent of the Brownian diffusivity \(D\). Meanwhile \(\operatorname{Cov}(X_i,X_j)=0\) for distinct particles, although \(\operatorname{Cov}(X_i^2,X_j^2)=\operatorname{Var}(e^W)>0\).

There is a **sharp weak-stiffness-contrast crossover**. Fix \(\mu_0,D,a,b>0\); for each \(n\), take
\[
 \mu_{2,n}=\mu_0,\qquad \mu_{1,n}=\mu_0(1+\varepsilon_n),\qquad
 r_{i,n}=2a_i\mu_{i,n},\quad(a_1,a_2)=(a,b),\qquad \varepsilon_n>0,\quad\varepsilon_n\to0.
\]
Write \(\mathcal I_n\) for the mutual information between two groups, each of size \(n\), in this \(n\)-dependent stationary system, and \(B\sim\operatorname{Beta}(a,b)\). Let \(G_1,G_2\) be independent standard normal variables independent of \(B\). Then:

* If \(n\varepsilon_n^2\to0\), then \(\mathcal I_n\to0\).
* If \(\sqrt n\,\varepsilon_n\to\tau\in(0,\infty)\), then
\[
 \boxed{\mathcal I_n\to\mathcal J_{a,b}(\tau):=I(\tau B+\sqrt2G_1;\tau B+\sqrt2G_2)>0.}\tag{4}
\]
* If \(n\varepsilon_n^2\to\infty\), then
\[
 \boxed{\mathcal I_n=\frac12\log(n\varepsilon_n^2)+h(B)-\frac12\log(8\pi e)+o(1).}\tag{5}
\]
The crossover profile has the explicit small-signal expansion
\[
 \mathcal J_{a,b}(\tau)=\frac{\operatorname{Var}(B)^2}{8}\tau^4+O(\tau^6)
 =\frac{a^2b^2}{8(a+b)^4(a+b+1)^2}\tau^4+O(\tau^6).\tag{6}
\]
It is continuous, is zero only at \(\tau=0\), and satisfies
\[
 \mathcal J_{a,b}(\tau)=\log\tau+h(B)-\tfrac12\log(8\pi e)+o(1)\qquad(\tau\to\infty).\tag{7}
\]
The entropy \(h(B)\) has the explicit standard beta-entropy formula with beta and digamma functions. Equations (4)--(7) show that the controlling parameter for information visibility is the number of particles times the **square of the relative stiffness contrast**, rather than either quantity individually.

## Assumptions and scope

The model is
\[
 dX_i(t)=-\mu_{S(t)}X_i(t)\,dt+\sqrt{2D}\,dB_i(t),
\]
where \(S(t)\in\{1,2\}\) is a single irreducible continuous-time Markov chain, with transition rate \(r_i\) from state \(i\) to the other state, shared by all particles. The Brownian motions are mutually independent and independent of \(S\). All displayed distributions refer to the unique stationary joint law; common initial conditions outside stationarity are not asserted to have the same finite-time information. The two groups are disjoint and sampled simultaneously. Natural logarithms give information in nats. The strict inequalities between positive trap stiffnesses are necessary for the nondegenerate fixed-contrast asymptotics: if \(\mu_1=\mu_2\), there is no common random variance and the mutual information is exactly zero.

## Proof

**1. Stationary Gaussian mixture.** Conditional on the complete two-sided trajectory of \(S\), each stationary particle is a centered Gaussian with the same conditional variance
\[
 V=2D\int_{-\infty}^0\exp\!\left(-2\int_s^0\mu_{S(t)}dt\right)ds.
\]
Different particles are conditionally independent. This random variance evolves between switches according to \(\dot V=2D-2\mu_iV\) in state \(i\), confined to \((D/\mu_1,D/\mu_2)\). Write \(V=D[c_1+(c_2-c_1)U]\). If \(p_i(v)\) are the stationary joint variance--state densities, their zero-total-flux equations are
\[
 (f_1p_1)'=-r_1p_1+r_2p_2,\quad (f_2p_2)'=r_1p_1-r_2p_2,\quad f_i(v)=2D-2\mu_iv,
\]
with \(f_1p_1+f_2p_2=0\). Integration yields a density proportional to
\[
 (v-D/\mu_1)^{a-1}(D/\mu_2-v)^{b-1}
 \left[\frac{v-D/\mu_1}{2\mu_2}+\frac{D/\mu_2-v}{2\mu_1}\right].
\]
Changing to \(U\) and normalizing via beta integrals gives \(q\) as stated. This is the same Gaussian-mixture object computed by Biroli, Kulkarni, Majumdar and Schehr, not a newly claimed stationary-law derivation. Since \(V\) is nondegenerate, distinct positions have zero covariance but their squares have covariance \(\operatorname{Var}(V)>0\).

**2. Exact information identity.** Given \(V\), each block is an independent centered Gaussian sample. Its sum of squares \(T_k=\sum_{j=1}^kX_j^2\) is sufficient for the unknown variance: the conditional angular law does not depend on \(V\). Moreover,
\[
 \log(T_k/k)=W+Z_k.
\]
Consequently \(I(V;\mathbf X^{(k)})=I(W;W+Z_k)=F_k\). Conditional independence of the two blocks gives the chain-rule identity
\[
 I(\mathbf X^{(n)};\mathbf Y^{(m)})=I(V;\mathbf X^{(n)})+I(V;\mathbf Y^{(m)})-I(V;\mathbf X^{(n)},\mathbf Y^{(m)}).
\]
The combined block is another sample of size \(n+m\), proving (1). If \(k/2=s\), the density of \(Z_k\) is
\[
 g_k(z)=\frac{s^s}{\Gamma(s)}\exp(sz-se^z),
\]
and direct gamma entropy calculation gives
\[
 h(Z_k)=s+\log\Gamma(s)-s\psi(s)=\tfrac12\log(4\pi e/k)+o(1).\tag{8}
\]
These formulas permit direct one-dimensional numerical evaluation for every finite \(k\) without computing a high-dimensional joint density.

**3. Entropic small-noise lemma.** We record the regularity needed to pass from weak convergence to entropy convergence. If probability densities \(p_j\) on a uniformly compact interval converge in \(L^1\) to \(p\), are uniformly bounded in some \(L^q\) with \(q>1\), and independent noise densities form an approximate identity with uniformly exponentially controlled far tails, then the entropy of their convolution tends to \(h(p)\). The same statement holds when the noise has a nondegenerate smooth limiting density, replacing \(p\) by its convolution with that limiting density, provided the resulting densities have uniformly controlled tails. To see this, apply Young's inequality to preserve uniform \(L^q\) bounds; use \(L^1\) convergence and uniform integrability of \(t\log t\) on compact spatial intervals; and bound the remaining entropy tails by the exponentially controlled convolution tails. The result applies to the log-chi-square noises below: their scaled densities follow from the displayed \(g_k\), with uniform exponential far-tail bounds and local Gaussian approximation. The bounded-support density of \(W\) is an affine-change and then smooth log-change of \(q\), whose endpoints behave as positive-power beta densities. In particular it belongs to \(L^q\) for at least one \(q>1\), even when either shape parameter is below one.

**4. Fixed nonzero contrast.** The variables \(Z_k\) converge in probability to zero and satisfy the preceding entropic lemma. Hence \(h(W+Z_k)\to h(W)\). Combining with (8) in (1) proves (2), while changing variables \(u\mapsto\log(D[c_1+(c_2-c_1)u])\) proves (3). Shifting \(W\) by \(\log D\) cannot change any of the mutual informations, proving diffusivity independence.

**5. The weak-contrast window.** Under the varying-parameter assumptions, the exact variance mixture has density
\[
 q_n(u)\ \propto\ u^{a-1}(1-u)^{b-1}
 \left[\frac{1-u}{1+\varepsilon_n}+u\right]
\]
and therefore converges in \(L^1\), indeed in a suitable \(L^q\), to the \(\operatorname{Beta}(a,b)\) density. Relative to the lower endpoint variance \(D/\mu_{1,n}\), the log variance is \(\log(1+\varepsilon_n U_n)\). The log sample variance of a block of \(k\) particles adds the independent \(Z_k\). Since
\[
 \sqrt k\,Z_k\ \Rightarrow\ N(0,2)
\]
with local density and entropy convergence, taking \(k=n,2n\) and \(\sqrt n\varepsilon_n\to\tau\) in (1) gives
\[
 2\{h(\tau B+\sqrt2G)-h(\sqrt2G)\}
 -\{h(\sqrt2\tau B+\sqrt2G)-h(\sqrt2G)\}.
\]
An orthogonal sum/difference transformation of two conditionally independent Gaussian observations identifies this expression with (4). At \(\tau=0\), both observations are independent Gaussians. For \(\tau>0\), their covariance equals \(\tau^2\operatorname{Var}(B)>0\), so their mutual information is positive.

If instead \(\sqrt n\varepsilon_n\to\infty\) with \(\varepsilon_n\to0\), divide the log-variance signal and the \(Z_n\) noise by \(\varepsilon_n\). The former converges in density and entropy to \(B\) while the noise is an entropically negligible approximate identity because its scale is \((n\varepsilon_n^2)^{-1/2}\). Thus
\[
 h(\log(1+\varepsilon_n U_n)+Z_n)=\log\varepsilon_n+h(B)+o(1),
\]
and likewise at sample size \(2n\). Using (8) in the exact identity proves (5). Repeating this argument directly for the Gaussian channel as \(\tau\to\infty\) proves (7).

Finally, for \(\tau\to0\), expand the marginal and joint Gaussian mixture densities around independent Gaussian noise. The first dependence term in the likelihood ratio is \(\tau^2\operatorname{Var}(B)z_1z_2/4\), for noise coordinates of variance two. Its half squared \(L^2\)-norm under the independent Gaussian reference is \(\tau^4\operatorname{Var}(B)^2/8\). Boundedness of \(B\) makes the expansion analytic, and symmetry under simultaneous reflection of the observations eliminates odd powers, giving (6). This completes the theorem.

## Verification

The standalone script `verify.py` uses NumPy and SciPy. Run `python verify.py` in a directory containing that file. It independently checks normalization of the mixing density, its agreement with stationary variance generator equations, exact log-gamma entropy, numerical equality of the three-entropy formula with a direct two-dimensional integration of the joint sufficient-statistic density, fixed-contrast asymptotic constants, and the weak-contrast Gaussian crossover. Finite diagnostics do not establish the infinite-population assertions; those are provided by the analytical steps above.

For \(\mu_1=2,\mu_2=1,D=1,r_1=4,r_2=2\), the computed \(h(W)=-0.442927373385\ldots\) and the equal-block asymptotic constant is \(-2.555013087150\ldots\), so the leading mutual information is \(\tfrac12\log n-2.555013087150\ldots\) nats. For \(a=b=1\) in the crossover window, \(\mathcal J_{1,1}(2)\approx0.010413607250\) nats.

## Relationship to prior work

Biroli, Kulkarni, Majumdar and Schehr (arXiv:2312.02570v1, 2023) derive the conditional Gaussian joint law and its beta-type mixing density, and analyze spatial cumulants, extreme and gap statistics, and full counting statistics. Equations (1)--(7) concern mutual information between macroscopic particle blocks, its exact finite-size reduction, and the weak-contrast scale. Those claims were not identified in the inspected relevant sections and material of that paper. The conditional-mixture law is acknowledged as prior art.

Clarke and Barron (1990) prove general information-theoretic asymptotics of Bayesian mixtures; their theory predicts the \(\tfrac12\log n\) information growth for a regular one-parameter model. We do **not** claim this generic logarithmic law independently. The application-specific explicit constant, the exact finite-population gamma-entropy representation, and the controlled singular weak-contrast crossover are the claimed combination; the classical theorem alone does not supply those model-specific formulas. Frydel (arXiv:2407.12213) treats a related fluctuating trap, including the off-state case, mainly at the level of one-particle stationary laws and dissipation.

## Limitations

Information concerns simultaneous stationary snapshots of groups of particles subject to the same trap history, not trajectories or separate independently driven traps. Large-population asymptotics use natural logs and require every group size to diverge; the critical crossover concerns two equal blocks with specified rate scaling. Fixed-contrast asymptotics are not uniform as the stiffnesses merge, which is precisely why the weak-contrast regime requires its own theorem. No assertion is made about quantum mutual information, statistical estimation from finitely many repeated experiments, or physical interactions between particles. Earlier general asymptotic information theory covers part of the leading-order mechanism; a more specialized, unindexed result could cover aspects of the exact or moving-parameter claims, so independent publication-priority review remains appropriate.

## References

1. M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570v1 (first public 2023-12-05), https://arxiv.org/abs/2312.02570 .
2. B. S. Clarke and A. R. Barron, *Information-theoretic asymptotics of Bayes methods*, IEEE Trans. Inf. Theory **36** (1990), 453–471, https://doi.org/10.1109/18.54897 .
3. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213 (first posted 2024-07-17), https://arxiv.org/abs/2407.12213 .
