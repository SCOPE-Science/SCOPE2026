# An optimal logarithmic path coupling for the Pelikan map and its critical-window occupation law

## Finding
Let \(X_0\) be uniformly distributed on \((0,1)\). Independently at each step, apply \(x\mapsto 2x\pmod 1\) with probability \(p\in(0,1)\), and \(x\mapsto x/2\) otherwise. Put \(M_k=\lfloor-\log_2 X_k\rfloor\). There is a coupling, using the very same map choices, with the reflected nearest-neighbor walk \(W_0=M_0\), \(W_{k+1}=\max\{0,W_k+\xi_{k+1}\}\), where \(\xi=+1\) on contraction and \(\xi=-1\) on doubling, such that for every integer \(N,d\ge1\),
\[
0\le M_k-W_k\quad(0\le k\le N),\qquad
\Pr\!\left\{\max_{0\le k\le N}(M_k-W_k)\ge d\right\}\le Np\,2^{-d}.
\]
The logarithmic size of this uniform error cannot be improved for a fixed expanding-branch probability \(p>1/2\):
\[
\lim_{N\to\infty}\frac{\max_{0\le k\le N}(M_k-W_k)}{\log_2 N}=1\quad\text{almost surely}.
\]
The same coupling works across the critical window. Fix \(\beta\in\mathbb R\), and for each observation horizon \(N\) choose \(p_N=1/2+\beta/\sqrt N\) (for sufficiently large \(N\)). In the Skorokhod \(J_1\) topology,
\[
\left(\frac{-\log_2 X_{\lfloor Nt\rfloor}}{\sqrt N}\right)_{0\le t\le1}
\ \Rightarrow\ (R_\beta(t))_{0\le t\le1},\quad
R_\beta(t)=B_t-2\beta t-\min\left\{0,\inf_{0\le s\le t}(B_s-2\beta s)\right\},
\]
where \(B\) is standard Brownian motion. At the exactly critical parameter \(p=1/2\), \(R_0\) has the law of reflected Brownian motion \((|B_t|)\). For every fixed \(a>0\), the fraction of steps in a population shell exponentially deep on the \(\sqrt N\) scale obeys
\[
\frac1N\sum_{k=1}^{N}{\bf1}\{X_k\le2^{-a\sqrt N}\}
\ \Rightarrow\ \int_0^1{\bf1}\{|B_t|\ge a\}\,dt,
\]
with explicit limiting expectation
\[
2(1+a^2)\overline\Phi(a)-2a\varphi(a),
\]
where \(\overline\Phi=1-\Phi\) and \(\varphi\) are the standard normal tail and density. The occupation limit is nondegenerate.

## Assumptions and scope
All initial positions are independent of map choices, with the uniform law on \((0,1)\). The countable set of eventually dyadic rational starting positions has probability zero and is ignored, ensuring \(X_k>0\) always. In the critical-window assertion, each horizon \(N\) defines a new experiment with independent choices of the same probability \(p_N\), not a changing probability within one trajectory. \(\log_2\) is base-two logarithm. In all statements the probability refers to the joint law of initial position and branch selections. The reflected walk starts at the same random nonnegative integer \(M_0\), which has \(\Pr(M_0=j)=2^{-j-1}\) for \(j\ge0\). No stationary law at criticality is assumed.

## Proof
**1. Exact conditional shell uniformity.** Let \(I_j=[2^{-j-1},2^{-j})\) for \(j\ge0\). Under the initial law, conditional on \(M_0=j\), the coordinate is uniform on \(I_j\). This remains true conditional on the entire observed shell-index history and branch-selection history: contraction maps \(I_j\) affinely onto \(I_{j+1}\); doubling maps \(I_j\), \(j\ge1\), affinely onto \(I_{j-1}\); doubling maps \(I_0\) onto \([0,1)\), whose conditional law within any new shell is uniform. Thus the exact shell transitions are \(j\mapsto j+1\) with probability \(1-p\), \(j\mapsto j-1\) with probability \(p\) when \(j\ge1\), and from \(j=0\), a contraction goes to 1 while a doubling goes to a fresh \(G\) with \(\Pr(G=r)=2^{-r-1}\), \(r\ge0\). Successive fresh values can be constructed independently of each other and of all branch choices.

**2. Uniform coupling and its nonasymptotic tail.** Drive both \(M\) and \(W\) with the same independent signs \(\xi\). Initialize \(M_0=W_0\). If \(M_k\ge1\), its next transition is \(M_k+\xi\), whereas the reflected update \(w\mapsto\max(0,w+\xi)\) is monotone and one-Lipschitz on nonnegative integers. Hence the nonnegative difference cannot increase. If \(M_k=0\), necessarily \(W_k=0\); contraction keeps the difference zero, while doubling makes \((M_{k+1},W_{k+1})=(G,0)\). It follows deterministically that \(0\le M_k-W_k\le\max\{G_1,\ldots,G_{K_N}\}\) for every \(k\le N\), where \(K_N\) is the number of doubling choices made at shell zero by time \(N\). At each such choice, the conditional tail is \(\Pr(G\ge d)=2^{-d}\). A union bound over the at most \(N\) possible choices gives \(\Pr(\max_{k\le N}(M_k-W_k)\ge d)\le Np2^{-d}\), including the dependence of \(K_N\) on previous overshoots.

**3. Optimality of the logarithmic error.** Fix \(p>1/2\). The shell-index chain is irreducible and aperiodic. Its conditional mean increment at every state \(j\ge1\) is \(1-2p<0\), and the mean step at zero is finite, so the elementary Foster drift/return-time criterion (or a direct comparison to a negative-drift nearest-neighbor walk until the next visit to zero) makes the chain positive recurrent. Its unique stationary probability assigns positive mass \(\pi_0\) to zero. The ergodic theorem gives \(K_N/N\to p\pi_0>0\) almost surely. At each of these doubling-from-zero times the coupling difference is exactly the freshly sampled geometric \(G\). For \(K_N\) growing linearly, the maximum of its independent geometric marks has ratio 1 to \(\log_2 N\) almost surely: the upper deviation has probability at most \(N2^{-(1+\varepsilon)\log_2N}\), while the lower deviation has probability at most \(\exp[-cN^{\varepsilon}]\) on dyadic horizons. Borel--Cantelli and monotonicity between dyadic horizons complete the proof of the asserted almost-sure limit.

**4. Diffusive critical-window limit.** For every horizon \(N\), the reflected walk is the discrete Skorokhod reflection of \(M_0+S_k\), where \(S_k=\sum_{j=1}^{k}\xi_j\). Under \(p_N=1/2+\beta/\sqrt N\), one has \(\mathbb E\xi_j=-2\beta/\sqrt N\), \(\operatorname{Var}\xi_j\to1\). The triangular-array Donsker theorem implies \(N^{-1/2}S_{\lfloor Nt\rfloor}\Rightarrow B_t-2\beta t\) in \(D[0,1]\). The Skorokhod reflection functional is continuous at continuous paths; also \(M_0/\sqrt N\to0\) in probability. Thus \(N^{-1/2}W_{\lfloor Nt\rfloor}\Rightarrow R_\beta(t)\). Taking \(d_N=\lceil3\log_2N\rceil\) in Step 2 shows \(\max_{k\le N}|M_k-W_k|/\sqrt N\to0\) in probability, uniformly over the critical-window probabilities. Finally \(0\le-\log_2X_k-M_k<1\), proving the functional convergence of the actual real-valued population coordinate.

**5. Time occupation at criticality.** At \(\beta=0\), the reflected Brownian process has the same law as \(|B|\). Brownian motion spends zero Lebesgue time at any prescribed nonzero level \(\pm a\), almost surely. Therefore the integral of the threshold indicator is a continuous mapping at almost every limiting path, and the empirical time occupation converges in law by Step 4 and a Riemann-sum argument. It is bounded by one, so expectations converge. The reflection principle gives \(\Pr(|B_t|\ge a)=2\overline\Phi(a/\sqrt t)\); integrating over \(0<t\le1\), and integrating by parts, yields \(2(1+a^2)\overline\Phi(a)-2a\varphi(a)\). The limiting occupation is zero with positive probability (Brownian confinement in \((-a,a)\) through time one) and positive with positive probability (Brownian crossing \(a\)), hence it is nonconstant.

## Verification
The accompanying self-contained `checker.py` tests both the literal rational-coordinate dynamics and the coupled integer-state recursion across varying branch probabilities, checking the pathwise inequality and the nonasymptotic finite-horizon bounds on instances. It also samples reflected walks to compare the observed critical \(N^{-1/2}\) endpoint against the half-normal mean. These finite tests corroborate only; the all-horizon tail, almost-sure sharpness, functional limit, and occupation law follow from the preceding proofs, not from simulations.

## Relationship to prior work
Yan et al. (2023) establish invariant densities and correlation behavior of the Pelikan doubling/halving map and identify the intermittent threshold. Monthus (first public 2024) establishes the shell Markov chain, its transient propagator, and a binary-spin representation in terms of an auxiliary reflected walk and erased digits. These exact models are **prior ingredients**, not claimed as new. The claim here is the explicit **joint path coupling of the actual dyadic shell coordinate**, with a uniform-in-horizon geometric tail, its sharp almost-sure logarithmic error, and the resulting **whole-path critical-window and occupation laws**. An earlier quantitative Gaussian crossover for the *mean physical coordinate* does not imply these pathwise conclusions; results on single excursions, first-return tails, and stationary correlations likewise do not give the stated coupling error or occupation process. Standard reflected-walk invariance principles and Gaussian calculations are used openly. General coupling results or unpublished work could imply a comparable conclusion, so the scientific priority remains subject to independent literature review.

## Limitations
The coordinate-to-walk approximation uses a uniform initial coordinate and fresh independent branch choices. It is not established here for arbitrary singular initial laws or pathwise quenched statements conditional on a fixed initial binary sequence. Critical-window convergence is weak convergence over joint randomness, not almost-sure convergence of normalized coordinates. The logarithmic optimality assertion holds at each **fixed** \(p>1/2\), not uniformly as \(p\downarrow1/2\). The occupation result concerns exponentially deep shells \(2^{-a\sqrt N}\); it does not imply stationary occupation at the critical parameter. Full publication-priority certainty and independent audit are not claimed.

## References
1. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, R. Klages, *Transition to anomalous dynamics in a simple random map*, first public 18 August 2023, arXiv:2308.09269, https://arxiv.org/abs/2308.09269.
2. C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, first public 30 September 2024, arXiv:2409.19999, https://arxiv.org/abs/2409.19999.
3. *A Gaussian critical-window crossover for the mean coordinate of the Pelikan random map*, published mathematical record (2026), identifier `2026/11/1/SCOPE-a-gaussian-critical-window-crossover-for-the-mean-coordinate-of--3c956fec7465`.
4. W. Feller, *An Introduction to Probability Theory and Its Applications*, vol. II (1971), standard random-walk reflection and invariance-principle background.
