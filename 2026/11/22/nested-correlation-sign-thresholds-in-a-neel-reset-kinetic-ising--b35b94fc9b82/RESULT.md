# Nested correlation-sign thresholds in a Neel-reset kinetic Ising chain

## Finding

Zero-temperature ferromagnetic Glauber dynamics competes with globally synchronized resets to a perfect alternating (Néel) spin pattern. This competition has an exact **finite-size and infinite-volume classification of the stationary two-spin correlation signs**. In particular, local ferromagnetic correlations coexist with a long-range staggered component, and their sign-change distance is logarithmically larger than the ordinary coarsening length at weak resetting.

Take an even periodic chain of \(N\ge4\) spins with unit-clock Glauber dynamics, and let every rate-\(r>0\) reset replace the entire chain with one of the two Néel patterns, each with probability \(1/2\), independently of the past. Define the stationary correlation \(C_{n,N}(r)=\mathbb E[s_0s_n]\) for \(0\le n\le N\), and put
\[
\kappa=\operatorname{arcosh}(1+r/2),\qquad q=e^{-\kappa}\in(0,1).
\]
Then for every \(1\le n<N\), exactly
\[
\boxed{C_{n,N}(r)=\frac{r(-1)^n+4h_{n,N}(r)}{r+4},\qquad
h_{n,N}(r)=\frac{q^n+q^{N-n}}{1+q^N}.}
\]
All even-distance correlations are strictly positive. For **each odd** \(1\le n<N\), there is exactly one critical resetting rate \(r_{n,N}>0\), determined by \(4h_{n,N}(r_{n,N})=r_{n,N}\). The correlation is positive below this rate, zero at it, and negative above it. The thresholds are strictly decreasing with odd separation on \(1\le n\le N/2\), and symmetric under \(n\mapsto N-n\). For fixed odd \(n\), the threshold is strictly larger on every finite even ring than on the infinite chain and decreases to the latter as ring size grows.

On the infinite chain, the exact stationary correlation is
\[
\boxed{C_n(r)=\frac{r(-1)^n+4e^{-n\kappa}}{r+4},\qquad n\ge1.}
\]
For odd \(n=2m+1\), the unique critical rate \(r_n\) is algebraic:
\[
\boxed{u_n^m(u_n-1)=2,\quad u_n>1,\qquad r_n=\frac{(u_n-1)^2}{u_n}.}
\]
It follows that \(r_1=4/3\), \(r_3=1/2\), \(r_1>r_3>r_5>\cdots>0\), and
\[
\boxed{r_n\sim\frac{4W(n)^2}{n^2}\quad\text{as odd }n\to\infty,}
\]
where \(W\) is the principal Lambert function. Equivalently, at any fixed \(r>0\), odd-distance correlations are positive precisely when \(n<\ell_*(r)=\log(4/r)/\kappa\), negative precisely when \(n>\ell_*(r)\), and zero when equality occurs. For \(r\downarrow0\),
\[
\boxed{\ell_*(r)\sim\frac{\log(4/r)}{\sqrt r}.}
\]

The finite-ring static structure factor has an exact ferromagnetic diffuse component and an antiferromagnetic Bragg contribution. At the allowed wave numbers \(k=2\pi j/N\),
\[
\boxed{S_N(k)=\frac4{r+4}\frac{1-q^N}{1+q^N}\frac{1-q^2}{1-2q\cos k+q^2}
+\frac{Nr}{r+4}\mathbf1_{\{k=\pi\}},}
\]
where \(S_N(k)=\sum_{n=0}^{N-1}C_{n,N}(r)e^{-ikn}\). The stochastic reset choice makes the stationary mean of each spin zero, so this is also the covariance structure factor. The infinite-volume staggered long-range weight is \(r/(r+4)\).

## Assumptions and scope

The finite system is a periodic cycle of even length \(N\ge4\), with spins \(s_i\in\{-1,+1\}\), ferromagnetic nearest-neighbor coupling and **strictly zero temperature**. Each site flips, independently conditional on the configuration, with rate
\[
w_i(s)=\frac12\left[1-\frac12s_i(s_{i-1}+s_{i+1})\right].
\]
This rate fixes the unit of time. At independent exponential event times of total rate \(r>0\), all spins are replaced simultaneously by either \(s_i=(-1)^i\) or \(s_i=-(-1)^i\), with fresh independent fair choice at each reset. Each reset affects all sites, not one site at a time; the stochastic choice of Néel phase, unlike a fixed phase, ensures the one-spin means vanish. The same two-point formulas hold with a fixed Néel reset phase, although the one-spin means then need not vanish. No positive-temperature, odd-cycle, local-reset or time-dependent-correlation statement is asserted.

For the infinite chain, construct Glauber dynamics via its standard bounded-rate graphical spin-update process and superimpose common global Poisson resets to either infinite alternating configuration. Observables supported on finitely many sites are well defined. Shared reset events couple any two initial configurations after their first reset, giving uniqueness of the stationary law for \(r>0\). Infinite-volume statements refer to fixed finite separations before the stated large-distance limits.

## Proof

**1. Closed correlation equation and reset source.** Under the zero-temperature flip generator, changing either end of a pair gives, for each \(n\ge1\), the standard Glauber two-spin evolution
\[
\frac{d}{dt}C_n=-2C_n+C_{n-1}+C_{n+1},\qquad C_0=1.
\]
On a finite ring also \(C_N=1\). These equations hold even for adjacent sites: the coincident-spin product gives the fixed boundary \(C_0=1\). Translation invariance of correlations follows from the equally weighted two Néel phases. A reset sets the pair product to \((-1)^n\) irrespective of the chosen phase. The stationary generator equation therefore is
\[
(r+2)C_{n,N}-C_{n-1,N}-C_{n+1,N}=r(-1)^n,
\quad 1\le n<N,\quad C_{0,N}=C_{N,N}=1.
\]
The particular bounded solution is \(p(-1)^n\), \(p=r/(r+4)\). The homogeneous characteristic equation is \(z+z^{-1}=r+2\) with roots \(q=e^{-\kappa}\) and \(q^{-1}\). The unique solution matching both boundary values is \(p(-1)^n+(1-p)(q^n+q^{N-n})/(1+q^N)\). Strict uniqueness follows either from the invertible diagonally dominant tridiagonal system (since \(r>0\)) or from resetting coupling. On \(\mathbb Z\), boundedness rules out the growing characteristic mode and the boundary \(C_0=1\) selects \(C_n=p(-1)^n+(1-p)q^n\).

**2. Unique and nested finite-size sign thresholds.** If \(n\) is even, both terms are positive. If \(n\) is odd, the sign is that of \(4h_{n,N}(r)-r\). Writing
\[
h_{n,N}(r)=\frac{\cosh((N/2-n)\kappa)}{\cosh(N\kappa/2)},
\]
one sees that this function strictly decreases with \(\kappa>0\), hence with \(r\), because \(a\tanh(a\kappa)<b\tanh(b\kappa)\) whenever \(0\le a<b\), with \(a=|N/2-n|\) and \(b=N/2\). Moreover \(h_{n,N}\to1\) as \(r\downarrow0\) and \(h_{n,N}\to0\) as \(r\to\infty\). Thus \(4h-r\) crosses zero exactly once. On the half-ring, \(h_{n,N}\) is strictly decreasing with \(n\in(0,N/2)\), so thresholds decrease with odd separation. Since
\[
h_{n,N}=q^n+\frac{q^{N-n}(1-q^{2n})}{1+q^N}>q^n,
\]
every finite-ring critical rate exceeds the infinite-chain rate. For fixed \(q,n\), the correction decreases strictly as even \(N\) increases, establishing monotone convergence of the thresholds.

**3. Infinite threshold algebra and scale.** For odd \(n\), the critical equation is \(4e^{-n\kappa}=r\). Since \(r=4\sinh^2(\kappa/2)\), it is equivalent to \(e^{-n\kappa/2}=\sinh(\kappa/2)\). The left side strictly decreases and the right side strictly increases, proving uniqueness independently. Set \(u=e^{\kappa}>1\); for \(n=2m+1\) this identity reduces to \(u^m(u-1)=2\) and gives \(r=(u-1)^2/u\). Increasing odd \(n\) lowers \(q^n\) at fixed \(r\), hence strictly lowers the unique root. The cases \(m=0,1\) give the stated exact first two rates.

For odd \(n\to\infty\), put \(t_n=\kappa_n/2\). Then \(e^{-nt_n}=\sinh t_n\), so \(t_n\downarrow0\) and, with \(y_n=nt_n\), \(y_ne^{y_n}=n[t_n/\sinh t_n]\sim n\). Strict monotonicity of the inverse of \(y\mapsto ye^y\) gives \(y_n\sim W(n)\), whence \(r_n=4\sinh^2t_n\sim4W(n)^2/n^2\). At fixed \(r\), the odd correlation sign is exactly that of \(4e^{-n\kappa}-r\); taking logarithms gives the stated \(\ell_*(r)\). Finally \(\kappa=\operatorname{arcosh}(1+r/2)\sim\sqrt r\) as \(r\downarrow0\), proving the logarithmically enhanced length.

**4. Structure-factor decomposition.** The positive finite-ring kernel \(h_{n,N}\) is the normalized periodization of \(q^{|n|}\):
\[
h_{n,N}=\frac{1-q^N}{1+q^N}\sum_{a\in\mathbb Z}q^{|n+aN|}.
\]
Its discrete Fourier transform is \((1-q^N)(1-q^2)/[(1+q^N)(1-2q\cos k+q^2)]\), by summing two geometric series. The Fourier transform of \((-1)^n\) on an even ring is \(N\mathbf1_{\{k=\pi\}}\). Combining these with their coefficients proves the stated formula; the infinite antiferromagnetic plateau follows by taking \(n\to\infty\) in the exact infinite correlation.

## Verification

The standalone `check_neel_reset.py` reconstructs the entire stationary continuous-time Markov generator independently for even rings of sizes \(4,6,8\), with zero-temperature spin flips and fresh fair phase selection at global resets. It solves the stationary linear system numerically, compares all pair correlations against the closed formula at five resetting rates, checks finite and infinite threshold signs and ordering, and independently compares 144 structure-factor Fourier values to the analytic transform. The script completed **400 numeric assertion groups** successfully using Python, NumPy and SciPy. The proof above does not use numerical extrapolation to justify any infinite-chain or all-parameter assertion.

To reproduce after extraction: `python check_neel_reset.py` (Python 3, NumPy and SciPy). The exact finite-state generator uses all \(2^N\) spin configurations for each tested ring. Scientific formulas do not depend on data or scripts in another document.

## Relationship to prior work

Magoni, Majumdar and Schehr (2020) establish the global Poisson reset protocol and focus on the magnetization distribution for independent initial spins, not the alternating-reset spatial-correlation sign classification. Their conclusion specifically points to two-point correlations as a further direction. Mayer and Sollich (2003/2004) give the broad **unreset** Glauber correlation-function hierarchy and its solutions for generic initial conditions, including the closure used here; that formal background is not claimed as new. Separate work on globally reset all-plus chains reports positive stationary two-point profiles and a correlation-distribution edge transition. Its all-plus source produces a constant spatial term, while the Néel protocol here produces an alternating spatial term; neither its positive-sign conclusion nor its all-plus distribution statement supplies the nested finite-size and infinite odd-distance sign threshold classification.

The new contribution is specifically the complete geometry-dependent sign hierarchy, exact polynomial roots, finite-size ordering, logarithmically enhanced sign-front scale and coexisting staggered Bragg/diffuse response under Néel resetting. The Poisson renewal identity, classical Glauber closure, and finite-state master-equation techniques are inherited methods, not independent claims of discovery.

## Limitations

The results concern strict zero temperature, nearest-neighbor Glauber heat-bath dynamics, whole-system Poisson resets and even periodic rings or the infinite line. They do not imply any discontinuous thermodynamic phase transition as \(r\) crosses one of the *fixed-separation correlation-sign thresholds*. The latter are zeros of an observable, not transitions between distinct invariant phases. For a fixed deterministic Néel reset pattern, the two-point formula still holds, but the finite-ring structure factor includes disconnected staggered magnetization; the zero-mean covariance interpretation in the theorem requires the fresh fair-phase protocol. No claim is made for general inhomogeneous reset patterns, positive temperature, non-Poisson renewal clocks, odd rings, or microscopic temporal correlations. The finite-state checks corroborate only tested sizes and parameter values. A general published Glauber solution combined with a renewal identity may implicitly encode special cases of these formulas, and unindexed equivalent treatments remain possible; priority is not independently certified.

## References

1. M. Magoni, S. N. Majumdar and G. Schehr, *Ising model with stochastic resetting*, arXiv:2002.04867, first publicly submitted 2020-02-12; *Physical Review Research* **2**, 033182 (2020), DOI:10.1103/PhysRevResearch.2.033182.
2. P. Mayer and P. Sollich, *General Solutions for Multispin Two-Time Correlation and Response Functions in the Glauber-Ising Chain*, arXiv:cond-mat/0307214, first submitted 2003-07-09; *Journal of Physics A* **37**, 9–49 (2004), DOI:10.1088/0305-4470/37/1/002.
3. R. J. Glauber, *Time-Dependent Statistics of the Ising Model*, *Journal of Mathematical Physics* **4**, 294–307 (1963), DOI:10.1063/1.1703954.
