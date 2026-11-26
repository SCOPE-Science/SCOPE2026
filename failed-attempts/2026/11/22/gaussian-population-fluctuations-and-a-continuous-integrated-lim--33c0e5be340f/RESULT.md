# Gaussian population fluctuations and a continuous integrated limit for singular Brownian-excursion births

## Finding

Consider the singular birth–death model of independent Itô Brownian excursions. The precise claim is a *joint, two-scale limit theorem for population counts*, with a continuous functional limit for integrated counts despite an almost surely dense set of times with infinitely many live particles.

Fix an excursion immigration intensity \(\rho>0\), and put
\[
\kappa=2\rho\sqrt{2/\pi},\qquad
K(s,t)=\kappa\left(\sqrt{\max(s,t)}-\sqrt{|t-s|}\right),\quad s,t\ge0.
\]
Let \(N_t\) be the number of live particles at the deterministic time \(t\). For every \(T>0\), define \(G_T(t)=T^{-1/4}(N_{Tt}-\kappa\sqrt{Tt})\) at each deterministic time, and define the continuous random function
\[
H_T(t)=T^{-5/4}\int_0^{Tt}\bigl(N_u-\kappa\sqrt u\bigr)\,du.
\]
Then the following statements hold simultaneously.

1. As \(T\to\infty\), the finite-dimensional distributions of \(G_T\) converge to those of the centered Gaussian process \(G\) with covariance \(\mathbb E[G(s)G(t)]=K(s,t)\). The Gaussian process admits a continuous version and is self-similar with exponent \(1/4\), but its increments are **not** stationary.
2. For every finite \(L>0\), \(H_T\Rightarrow H\) in \(C([0,L])\) with its uniform topology, where \(H(t)=\int_0^tG(v)\,dv\). For \(0\le s\le t\),
\[
\mathbb E[H(s)H(t)]=\kappa\left(\frac{2st^{3/2}}3-\frac{2s^{5/2}}{15}-\frac{4t^{5/2}}{15}+\frac{4(t-s)^{5/2}}{15}\right),
\qquad \operatorname{Var}H(t)=\frac{4\kappa}{15}t^{5/2}.
\]
3. At every \(t_0>0\), the local Gaussian tangent is a fractional Brownian motion with Hurst exponent \(1/4\): as \(\varepsilon\downarrow0\),
\[
\bigl(\varepsilon^{-1/4}[G(t_0+\varepsilon u)-G(t_0)]\bigr)_{u\ge0}
\xrightarrow{\mathrm{f.d.d.}}
\bigl(\sqrt{2\kappa}\,B_{1/4}(u)\bigr)_{u\ge0},
\]
where \(B_{1/4}\) is standard fractional Brownian motion. At the origin, self-similarity instead gives the non-fractional-Brownian process \(G\) itself.

The exact finite-time count mean and covariance, used as input for this theorem, are \(\mathbb E N_t=\kappa\sqrt t\) and \(\operatorname{Cov}(N_s,N_t)=K(s,t)\). These formulas follow from the existing excursion-Poisson construction and are not, on their own, claimed as a new contribution.

## Assumptions and scope

Let \(\Theta\) be a Poisson random measure on \([0,\infty)\times\mathcal E\) with intensity \(\rho\,db\otimes\mathbf n(de)\), where \(\mathcal E\) is the space of one-dimensional Brownian excursions away from zero, with both signs permitted, and \(\mathbf n\) is the Itô excursion measure normalized by the entrance density
\[
\mathbf n_u(dx)=\frac{|x|}{\sqrt{2\pi u^3}}e^{-x^2/(2u)}\,dx.
\]
An atom \((b,e)\) is alive at \(t\) when \(b\le t<b+\xi(e)\), with \(\xi(e)\) its excursion lifetime. This choice of strict right endpoint is immaterial at each deterministic time and for time integration. Integrating the entrance law gives
\[
\mathbf n\{\xi>v\}=\sqrt{2/\pi}\,v^{-1/2},\qquad
\mathbf n(\xi\in dv)=(2\pi)^{-1/2}v^{-3/2}\,dv.
\]
Thus \(N_t=\int\mathbf1_{\{b\le t<b+\xi\}}\,\Theta(db,de)\) is a finite Poisson variable for each deterministic \(t\). The integrated process exists almost surely for every compact time interval because \(\mathbb E\int_0^L N_u\,du=(2\kappa/3)L^{3/2}<\infty\).

The assertion about \(G_T\) is **only finite-dimensional convergence**, not convergence of its raw trajectories in \(D([0,L])\) or \(C([0,L])\). The cited construction has an almost surely dense exceptional set of infinite-particle times. The \(C\)-valued assertion is made for the *integrated* process \(H_T\), not for the instantaneous count.

## Proof

**1. Exact overlap intensities.** Write \(\mu(db,d\ell)=\rho(2\pi)^{-1/2}\,db\,\ell^{-3/2}d\ell\), and \(I_t(b,\ell)=\mathbf1_{\{b\le t<b+\ell\}}\). The compensated Poisson isometry gives
\[
\mathbb EN_t=\int I_t\,d\mu=\rho\sqrt{2/\pi}\int_0^t(t-b)^{-1/2}db=\kappa\sqrt t.
\]
For \(0\le s\le t\), two times share a live particle exactly if its birth was at \(b\le s\) and its lifetime exceeds \(t-b\). Hence
\[
\operatorname{Cov}(N_s,N_t)=\int I_sI_t\,d\mu
=\rho\sqrt{2/\pi}\int_0^s(t-b)^{-1/2}db
=\kappa\bigl(\sqrt t-\sqrt{t-s}\bigr).
\]
Symmetry yields \(K\). In particular the count pair is the sum of a common Poisson category with mean \(K(s,t)\) and two independent exclusive categories with means \(\kappa\sqrt s-K(s,t)\) and \(\kappa\sqrt t-K(s,t)\). Every category mean is nonnegative.

**2. Gaussian finite-dimensional limit.** Fix \(m\ge1\), deterministic times \(t_1,\ldots,t_m\ge0\), and real coefficients \(a_1,\ldots,a_m\). The linear combination \(\sum_j a_jG_T(t_j)\) is the compensated Poisson integral with integrand
\[
f_T(b,\ell)=T^{-1/4}\sum_{j=1}^m a_j I_{Tt_j}(b,\ell).
\]
It obeys \(\lVert f_T\rVert_\infty\le T^{-1/4}\sum_j|a_j|\), and Brownian lifetime scaling gives, *exactly for every* \(T\),
\[
\int f_T^2\,d\mu=\sum_{i,j}a_ia_jK(t_i,t_j).
\]
The Poisson characteristic exponent is \(\int(e^{if_T}-1-if_T)d\mu\). Since \(|e^{ix}-1-ix+x^2/2|\le |x|^3/6\), the difference from the corresponding Gaussian exponent is bounded by
\[
\frac16\lVert f_T\rVert_\infty\int f_T^2\,d\mu=O(T^{-1/4}).
\]
Cramér–Wold and Lévy's theorem prove the joint Gaussian limit. The kernel \(K\) is nonnegative-definite by the indicator Gram representation. For \(s\le t\),
\[
\mathbb E|G(t)-G(s)|^2=\kappa\left(2\sqrt{t-s}+\sqrt s-\sqrt t\right)
\le2\kappa\sqrt{t-s}.
\]
Gaussian moments of order \(p>4\) and Kolmogorov's continuity criterion give a continuous version. Since \(K(as,at)=a^{1/2}K(s,t)\), this version is \(1/4\)-self-similar. Increments are not stationary: for fixed \(h>0\), their variance equals \(\kappa\sqrt h\) at origin, but approaches \(2\kappa\sqrt h\) when the starting time tends to infinity.

**3. Continuous integrated-process limit.** Define the interval-occupation kernel
\[
A_{T,t}(b,\ell)=\int_0^{Tt}I_u(b,\ell)\,du
=\left|[b,b+\ell)\cap[0,Tt]\right|.
\]
The time-integrated centered count equals \(\int A_{T,t}(\Theta-\mu)\), justified by Tonelli for the nonnegative terms and by the finite expected integrated population. For a finite linear combination of \(H_T(t_j)\), the compensated integrand is \(T^{-5/4}\sum_j a_jA_{T,t_j}\); its supremum is bounded by \(L T^{-1/4}\sum_j|a_j|\) for \(0\le t_j\le L\), while its \(L^2(\mu)\) norm is independent of \(T\) by the exact covariance scaling. The same characteristic-exponent argument proves Gaussian finite-dimensional convergence, with covariance \(\int_0^s\int_0^tK(u,v)\,dv\,du\).

Furthermore, \(K(u,v)\le\kappa\sqrt L\) on \([0,L]^2\). Consequently, uniformly over \(T>0\),
\[
\mathbb E|H_T(t)-H_T(s)|^2
=\int_s^t\int_s^tK(u,v)\,du\,dv
\le\kappa\sqrt L\,|t-s|^2.
\]
The functions \(H_T\) have continuous paths, start at zero, and satisfy the uniform second-moment increment criterion, hence are tight in \(C([0,L])\). Their finite-dimensional limit is \(H=\int_0^{\cdot}G(v)dv\). Directly integrating \(K\), for \(s\le t\), gives
\[
\int_0^s\int_0^t\sqrt{\max(u,v)}\,dvdu=\frac{2s^{5/2}}{15}+\frac{2st^{3/2}}3,
\]
\[
\int_0^s\int_0^t\sqrt{|v-u|}\,dvdu=\frac4{15}\left(s^{5/2}+t^{5/2}-(t-s)^{5/2}\right).
\]
Subtraction proves the covariance and variance in the finding.

**4. The local fractional-Brownian tangent.** For \(t_0>0\), \(u,v\ge0\) and small \(\varepsilon>0\), expand the covariance of centered increments of \(G\) via \(K\). The sole non-smooth term gives
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-1/2}
\operatorname{Cov}\bigl(G(t_0+\varepsilon u)-G(t_0),G(t_0+\varepsilon v)-G(t_0)\bigr)
=\kappa\left(\sqrt u+\sqrt v-\sqrt{|u-v|}\right).
\]
The omitted square-root terms are smooth at \(t_0>0\) and contribute only \(O(\varepsilon)\) before division by \(\sqrt\varepsilon\). The right-hand side is \(2\kappa\) times the covariance of standard fractional Brownian motion with Hurst index \(1/4\). Because all processes here are Gaussian, covariance convergence proves finite-dimensional convergence. At \(t_0=0\), the exact \(1/4\)-self-similarity of \(G\) gives a different tangent, as already noted.

## Verification

Running \(\texttt{python3 checker.py}\) from the directory containing this file performs 1,017 finite numerical and structural consistency checks. They include the exact overlap decomposition, numerical double integration of the covariance kernel, self-similarity, nonstationary increments, local tangent covariance convergence, positive-semidefiniteness tests, and a reproducible bivariate-Poisson simulation. The script uses only the Python standard library. The printed outcome is **PASS: 1017 finite numerical and structural consistency checks**.

These checks cannot certify infinite-time convergence. The actual proof of the Gaussian limits is the bounded-integrand Poisson characteristic-exponent argument above; the continuous limit additionally uses the explicit uniform second-moment tightness estimate. The exceptional-time obstruction is respected rather than suppressed.

## Relationship to prior work

Kou (2026) constructs the singular Brownian-excursion birth–death model and proves the dense exceptional-time phenomenon. Proposition 2.5 identifies fixed-time spatial Poisson laws, and Theorem 1.5 proves a one-time central limit theorem for spatial power sums with exponents strictly between zero and one. Section 4 studies two-time transforms of those power sums. The present exact count covariance is a straightforward implication of the same Poisson setup; it is used as a lemma, not advertised as independently new. The distinct asserted claim is the explicit *multitime* Gaussian population limit, its nonstationary global law versus local fractional-Brownian tangent, and the *continuous functional limit* for integrated counts, including its exact covariance.

Pang and Taqqu (2019) establish functional limits for nonstationary, power-law, finite-rate Poisson shot-noise models whose response is a deterministic integrated kernel multiplied by centered marks and whose scaled variance has prescribed power laws. Their Gaussian covariance is given by a different weighted convolution. Their hypotheses do not directly describe a sigma-finite infinite-rate family of Brownian-excursion lifetime intervals with finite deterministic-time occupancy and dense infinite-count times, so their quoted theorem does not directly imply the present specific functional claim. This does not establish that no more general Poisson-integral limit principle could be specialized to do so.

Marynych and Verovkin (2017) analyze renewal immigration with finite numbers of arrivals before finite time and heavy-tailed interarrival epochs, obtaining inverse-stable-subordinator limits. That setting differs from infinitely active excursion immigration. Seppäläinen (2005) exhibits a \(1/4\)-scale Gaussian particle-current fluctuation and a fractional-Brownian limit in an equilibrium independent-random-walk growth model; its object is not Brownian-excursion population occupancy. These relationships are analogies, not claims of the first appearance of Hurst index \(1/4\) or Gaussian shot-noise limits.

## Limitations

The instantaneous count is infinite at a dense random set of times; a path-level convergence claim for \(G_T\) in the usual finite-valued Skorokhod or continuous space would be false. Only its finite-dimensional laws are claimed. Tightness and convergence are proved for the integrated process. The fractional-Brownian tangent concerns the *Gaussian limit*, not a uniform two-parameter statement jointly taking \(T\to\infty\) and \(\varepsilon\downarrow0\). The Poisson normalization fixes the Brownian variance and both excursion signs; changing these conventions changes \(\kappa\).

Prior-art assessment is based on the inspected accessible sources. Broader general Poisson random-measure central-limit or queueing results could entail parts of the theorem after nontrivial specialization; an exhaustive historical priority assertion is not made. Independent verification has not been performed.

## References

1. Ruibo Kou, *Singular Birth-Death model*, arXiv:2611.19362v1 (first public posting 2026-11-14), https://arxiv.org/html/2611.19362v1 ; https://arxiv.org/abs/2611.19362 . Especially Definition 1.1, Theorem 1.2, Proposition 2.5, Theorem 1.5 and Section 4.
2. Guodong Pang and Murad S. Taqqu, *Nonstationary self-similar Gaussian processes as scaling limits of power-law shot noise processes and generalizations of fractional Brownian motion*, *High Frequency* 2 (2019), 95–112, https://doi.org/10.1002/hf2.10028 .
3. Alexander Marynych and Glib Verovkin, *A functional limit theorem for random processes with immigration in the case of heavy tails*, *Modern Stochastics: Theory and Applications* (2017), https://doi.org/10.15559/17-VMSTA76 .
4. Timo Seppäläinen, *Second-order fluctuations and current across characteristic for a one-dimensional growth model of independent random walks*, *Annals of Probability* 33 (2005), 759–797, https://arxiv.org/abs/math/0310044 .
