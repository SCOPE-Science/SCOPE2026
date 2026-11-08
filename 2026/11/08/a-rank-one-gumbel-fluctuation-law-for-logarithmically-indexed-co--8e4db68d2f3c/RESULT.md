# A rank-one Gumbel fluctuation law for logarithmically indexed coupon siblings

## Finding

Let \(N\ge2\) coupon types be drawn independently and uniformly. Stop at the first draw \(T_N\) when all \(N\) types have appeared, and let \(K_{N,i}\) count occurrences of type \(i\) at that stopping time. In the sibling-collector interpretation, the number of empty album spaces at index \(j\ge2\) is
\[
U_{N,j}=\sum_{i=1}^{N}{\bf1}\{K_{N,i}<j\}.
\]
Set \(L_N=\log N\), and for \(x\in\mathbb R\) put
\[
j_N(x)=\lfloor L_N+x\sqrt{L_N}\rfloor,\qquad
b_N(x)=\Pr\{\operatorname{Poi}(L_N)<j_N(x)\},\qquad
\phi(x)=(2\pi)^{-1/2}e^{-x^2/2}.
\]
These definitions are used for all sufficiently large \(N\) so that \(j_N(x)\ge2\) on each compact interval under consideration. Define
\[
\tau_N=\frac{T_N}{N}-L_N,\qquad
Y_N(x)=\sqrt{L_N}\left(\frac{U_{N,j_N(x)}}N-b_N(x)\right).
\]

**Theorem (uniform rank-one approximation and joint weak limit).** For every fixed \(R>0\),
\[
\lim_{N\to\infty}\mathbb E\left[\sup_{|x|\le R}
\left|Y_N(x)+\phi(x)\tau_N\right|^2\right]=0.
\]
Consequently, with the supremum norm on \(\ell^\infty([-R,R])\),
\[
(\tau_N,Y_N)\ \Longrightarrow\
\bigl(G,\,x\mapsto-\phi(x)G\bigr),
\quad \Pr\{G\le u\}=\exp(-e^{-u}).
\]
Also, uniformly for \(|x|\le R\), \(U_{N,j_N(x)}/N-\Phi(x)\to0\) in probability, where \(\Phi\) is the standard normal distribution function. For every fixed pair \(x,y\),
\[
\lim_{N\to\infty}\mathbb E Y_N(x)=-\gamma\phi(x),\qquad
\lim_{N\to\infty}\operatorname{Cov}(Y_N(x),Y_N(y))
=\frac{\pi^2}{6}\phi(x)\phi(y),
\]
where \(\gamma\) is Euler's constant. Thus the whole growing-index profile has a single, non-Gaussian Gumbel fluctuation amplitude after deterministic Poisson-centering.

## Assumptions and scope

The coupon distribution is exactly uniform for each \(N\); successive draws are independent and sampling is with replacement. The stopping time refers to **first completion of the main album**, not completion of any higher-index album. The index window is \(j_N(x)=\lfloor\log N+x\sqrt{\log N}\rfloor\) for fixed \(x\) on a fixed compact set. In particular, this theorem does not address nonuniform coupon arrays, windows growing with \(N\), or the extreme-index tails outside the central-limit window. The notation \(\operatorname{Poi}(t)\) denotes a Poisson random variable of mean \(t\).

## Proof

**1. Coupled Poissonization and the random completion time.** Take independent rate-one Poisson processes \(\{N_i(t):t\ge0\}\), \(1\le i\le N\). The superposition has rate \(N\) and its successive labels are independent uniform coupon types. Write \(E_i\) for the first jump time of process \(i\), and define
\[
C_N=\max_{1\le i\le N}E_i,\qquad
Z_N(t,j)=\frac1N\sum_{i=1}^N {\bf1}\{N_i(t)<j\}.
\]
Under this coupling, the original discrete stopped counts are exactly \(N_i(C_N)\), so \(U_{N,j}/N=Z_N(C_N,j)\). The \(E_i\) are independent \(\operatorname{Exp}(1)\) variables, giving
\[
\Pr\{C_N-L_N\le u\}=\left(1-\frac{e^{-u}}N\right)^N
\longrightarrow\exp(-e^{-u}),
\]
for each fixed \(u\). The exponential-order-statistic spacing identity gives the distributional representation
\[
C_N\stackrel d=\sum_{k=1}^N\frac{\xi_k}{k},
\]
where the \(\xi_k\) are independent unit-rate exponentials. Therefore \(\mathbb E C_N=H_N\), \(\operatorname{Var}(C_N)=\sum_{k=1}^N k^{-2}\), and \(\sup_N\mathbb E|C_N-L_N|^4<\infty\). The last bound follows from independence, the uniformly bounded fourth centered moment of the sum, and boundedness of \(H_N-L_N\). Hence \(\mathbb E(C_N-L_N)\to\gamma\) and \(\operatorname{Var}(C_N-L_N)\to\pi^2/6\).

**2. Uniformly negligible empirical error.** Let
\[
b_j(t)=\Pr\{\operatorname{Poi}(t)<j\}
=e^{-t}\sum_{k=0}^{j-1}\frac{t^k}{k!}.
\]
For fixed integer \(j\), let \(S_{i,j}\) be the \(j\)th jump time of process \(i\). These variables are independent \(\Gamma(j,1)\), and \(Z_N(t,j)=N^{-1}\sum_i{\bf1}\{S_{i,j}>t\}\). The Dvoretzky–Kiefer–Wolfowitz inequality for their empirical distribution gives
\[
\Pr\left\{\sup_{t\ge0}|Z_N(t,j)-b_j(t)|>\varepsilon\right\}
\le2e^{-2N\varepsilon^2}.
\]
As \(x\) ranges over \([-R,R]\), the integer \(j_N(x)\) takes at most \(2R\sqrt{L_N}+3\) different values. A union bound and tail integration imply
\[
\mathbb E\left[\sup_{|x|\le R,t\ge0}
|Z_N(t,j_N(x))-b_{j_N(x)}(t)|^2\right]
=O_R\left(\frac{\log(2+L_N)}N\right).
\]
Multiplying by \(L_N\) yields a quantity tending to zero. This bound is valid even at the data-dependent time \(C_N\): independence between that stopping time and the empirical functions is not required.

**3. Deterministic Poisson-CDF linearization.** Direct differentiation of the finite Poisson sum yields
\[
\frac{d}{dt}b_j(t)
=-e^{-t}\frac{t^{j-1}}{(j-1)!}.
\]
Stirling's formula, uniformly for \(|x|\le R\) and \(|u|\le K\) with fixed \(K\), gives the local limit
\[
\sup_{|x|\le R,|u|\le K}
\left|\sqrt{L_N}\Pr\{\operatorname{Poi}(L_N+u)=j_N(x)-1\}
-\phi(x)\right|\longrightarrow0.
\]
The maximum of \(e^{-t}t^k/k!\) over \(t\ge0\) occurs at \(t=k\). Thus for each fixed \(R\), Stirling's formula also provides a constant \(A_R\) such that, for all sufficiently large \(N\),
\[
\sqrt{L_N}\sup_{|x|\le R,t\ge0}
\Pr\{\operatorname{Poi}(t)=j_N(x)-1\}\le A_R.
\]
Apply the integral identity
\[
\sqrt{L_N}\bigl(b_{j_N(x)}(C_N)-b_{j_N(x)}(L_N)\bigr)
=-\int_{L_N}^{C_N}\sqrt{L_N}\Pr\{\operatorname{Poi}(t)=j_N(x)-1\}\,dt.
\]
The first local-limit estimate on \(|C_N-L_N|\le K\), together with tightness of \(C_N-L_N\), proves that the difference between the right side and \(-\phi(x)(C_N-L_N)\) tends to zero uniformly in \(|x|\le R\), in probability. The displayed global bound dominates its uniform absolute value by \((A_R+\sup_{|x|\le R}\phi(x))|C_N-L_N|\); the uniform fourth-moment bound from Step 1 upgrades the convergence to \(L^2\). Together with Step 2, this proves
\[
\mathbb E\sup_{|x|\le R}
\left|Y_N(x)+\phi(x)(C_N-L_N)\right|^2\to0.
\]

**4. Returning to discrete draw time.** Write \(M(t)=\sum_iN_i(t)\). At the continuous cover time, the total number of jumps is exactly the discrete stopping count: \(M(C_N)=T_N\). The compensated process \(M(t)-Nt\) is a square-integrable martingale with predictable quadratic variation \(Nt\). Optional isometry at the integrable stopping time \(C_N\) yields
\[
\mathbb E\left|\frac{T_N}{N}-C_N\right|^2
=\frac{\mathbb E C_N}{N} =\frac{H_N}{N}\to0.
\]
One may justify optional isometry first at \(C_N\wedge m\) and then pass to the limit by \(\mathbb E C_N<\infty\). Since \(\phi\) is bounded, substitution in Step 3 proves the claimed uniform \(L^2\) approximation with \(\tau_N\). Joint weak convergence follows from Step 1 and Slutsky's theorem in the supremum-norm space; the uniform remainder also implies tightness and convergence in distribution there. The ordinary Poisson central limit theorem gives \(b_N(x)\to\Phi(x)\) uniformly on compact sets, hence the uncentered law of large numbers. Finally, the uniform \(L^2\) approximation and the exact first two moment limits in Step 1 imply the displayed expectation and covariance limits by Cauchy–Schwarz. \(\square\)

## Verification

The standalone file `verification_check.py` uses only the Python standard library and is executable with `python verification_check.py`. Its 87 passing assertions combine an independent finite absorbing-chain calculation of fixed-index expectations, exact rational checks of the derivative of \(b_j\), finite local-Poisson-limit comparisons, finite differences, and a seeded Poisson-clock simulation of the first-order Gumbel random-shift approximation. The simulation's mean absolute discrepancy was approximately \(0.057100\) at \(N=2000\). The functional theorem, the uniform empirical bound, and the limiting moments follow from the analytic arguments above, **not** from the finite computations.

## Relationship to prior work

Long's 2026 paper, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, studies exactly the present sibling counts, but its Theorem 5 and Corollary 10 cover **fixed** album indices \(2,\ldots,J\). Remark 3 expressly leaves album indices growing with \(N\) outside its scope. Its fixed-index fluctuations have an exponential common amplitude and a different scale; the present logarithmically growing index window yields a compact-uniform, centered **Gumbel** profile at relative scale \((\log N)^{-1/2}\). Crucially, Ilienko's 2026 *Limit theorems in the extended coupon collector’s problem* provides an **infinite-dimensional** fixed-index theorem in \(\mathbb R^\infty\) with the **product topology**. Theorem 1 asserts coordinatewise-normalized convergence for fixed sibling ranks, and its Section 5 proof passes only finite coordinate blocks to the limit. Product-topology convergence does not control moving ranks \(j_N\asymp\log N\) or the supremum over a growing set of indices, so it does not imply the present compact-uniform central-window law. Long's companion 2026 *Radial Transform Extremality* establishes finite-alphabet transform inequalities, not this growing-index functional limit. Doumas and Papanicolaou's earlier sibling results principally concern fixed album indices and expected deficits. Mahmoud and Smythe (2012) establish multivariate Gaussian limit laws for occupancy counts with each **fixed** frequency category under deterministic sampling phases. Their Theorems 1–2 do not stop at first coupon completion or control a threshold category increasing with \(N\); in particular their Gaussian limits do not imply the Gumbel shift here. The classical coupon-collector Gumbel law, Poisson local central-limit theorem, empirical-process inequality, and exponential spacing representation used in the proof are standard ingredients, and no originality is claimed for them separately. The assertion is that their combination yields the stated nontrivial functional fluctuation at a previously untreated sibling-index scaling.

## Limitations

The result is proved for uniform coupon weights, compact index windows, and the first-cover stopping time. It is not a theorem about the \(j\)th full collection time or about a growing window of \(x\). It gives a rank-one first-order fluctuation, not a second-order Gaussian correction after subtracting the Gumbel amplitude. As for any literature-based priority assessment, inaccessible or unindexed older general occupancy theorems may independently imply the result; this has not been ruled out exhaustively. Numerical tests are finite and have no bearing on such historical priority.

## References

- Christopher D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, first publicly posted June 28, 2026, arXiv:2606.29635, especially Theorem 5 and Remark 3. https://arxiv.org/abs/2606.29635
- Andrii Ilienko, *Limit theorems in the extended coupon collector’s problem*, Modern Stochastics: Theory and Applications, published online August 11, 2026, DOI:10.15559/26-VMSTA306, especially Theorem 1, Section 5 and Section 8. https://www.vmsta.org/journal/VMSTA/article/358/read
- Christopher D. Long, *Radial Transform Extremality for the Siblings of the Coupon Collector*, first publicly posted June 30, 2026, arXiv:2606.31391. https://arxiv.org/abs/2606.31391
- A. Doumas and V. G. Papanicolaou, *The Siblings of the Coupon Collector*, arXiv:1412.4346. https://arxiv.org/abs/1412.4346
- V. G. Papanicolaou and A. Doumas, *The Coupon Collector's Brother*, arXiv:2005.05270. https://arxiv.org/abs/2005.05270
- H. M. Mahmoud and R. T. Smythe, *On the Joint Behavior of Types of Coupons in Generalized Coupon Collection*, Advances in Applied Probability 44 (2012), 429–451, DOI:10.1239/aap/1339878719. https://doi.org/10.1239/aap/1339878719
- A. Dvoretzky, J. Kiefer and J. Wolfowitz, *Asymptotic minimax character of the sample distribution function and of the classical multinomial estimator*, Annals of Mathematical Statistics 27 (1956), 642–669 (standard empirical distribution inequality; sharp constant due to Massart).
