# Distinct optimal-reset exponents at the hub and leaves of a star

## Finding
For the observed discrete-time random walk with stochastic resetting on a star with \(m\ge 2\) leaves, let \(h_{c,m}(p)\) and \(h_{\ell,m}(p)\) be the stationary Shannon entropy rates when the reset node is, respectively, the center or a fixed leaf. The reset probability is \(p\in[0,1]\); entropy is measured in natural units per transition. Then
\[
h_{c,m}(p)>h_{\ell,m}(p)\qquad(0<p<1).
\]
The center-rooted rate has the **unique** global maximizer
\[
p_{c,m}=\frac{2}{1+\sqrt{1+4m}},\qquad
\max_p h_{c,m}(p)=\log\frac{1+\sqrt{1+4m}}2.
\]
For every choice \(p_{\ell,m}\) of a global maximizer of the leaf-rooted entropy rate, as \(m\to\infty\),
\[
m^{3/4}p_{\ell,m}\longrightarrow1,\qquad
m^{3/4}\left[\max_p h_{\ell,m}(p)-\frac12\log m\right]\longrightarrow1.
\]
The corresponding center-rooted optimizer and entropy gain obey
\[
\sqrt m\,p_{c,m}\longrightarrow1,\qquad
\sqrt m\left[\max_p h_{c,m}(p)-\frac12\log m\right]\longrightarrow\frac12.
\]
Thus the two symmetry-distinct root locations have different optimal-reset exponents, \(1/2\) and \(3/4\), and the ratio of their maximal entropy gains is asymptotic to \(m^{1/4}/2\).

## Assumptions and scope
The graph is the undirected loopless star \(K_{1,m}\), with center \(c\) and leaves \(\ell_1,\ldots,\ell_m\), \(m\in\{2,3,\ldots\}\). At each integer time, with probability \(p\), the current node is replaced by the fixed reset node \(r\); otherwise the walker chooses a uniformly random neighbor of its current node. The observed trajectory records the visited vertices, **not** a hidden indicator of whether a reset occurred. Consequently if a reset and a regular hop have the same destination, their probabilities must be combined before computing path entropy. Let \(P^{(r)}(p)\) be the resulting transition matrix and \(\pi^{(r)}(p)\) its stationary distribution. Define
\[
h_{r,m}(p)=-\sum_i\pi_i^{(r)}(p)\sum_jP^{(r)}_{ij}(p)\log P^{(r)}_{ij}(p),
\]
where \(0\log0=0\). At \(p=0\) the star walk is periodic but irreducible and has a unique stationary probability; the entropy-rate formula is still valid. At \(p=1\), the reset node is absorbing and the rate is zero. For both reset locations the no-reset benchmark is exactly \(\frac12\log m\).

## Proof
**1. Exact transition entropies and stationary center mass.** Put \(H(p)=-p\log p-(1-p)\log(1-p)\), with continuous endpoint extensions. When resetting to the center, a leaf always goes to the center, while the center stays there with probability \(p\) and chooses each leaf with probability \((1-p)/m\). Stationarity gives \(\pi_c=1/(2-p)\), and hence
\[
h_{c,m}(p)=\frac{H(p)+(1-p)\log m}{2-p}.\tag{1}
\]
When resetting to a particular leaf, the center is occupied with stationary probability \(\pi_c=(1-p)/(2-p)\). Each leaf has a two-destination transition (to the center with probability \(1-p\), to the reset leaf with probability \(p\)); the center jumps to the reset leaf with probability \(a=p+(1-p)/m\) and to each other leaf with probability \(b=(1-p)/m\). Therefore, writing
\[
F_m(p)=-a\log a-(m-1)b\log b,
\]
one obtains
\[
h_{\ell,m}(p)=\frac{H(p)+(1-p)F_m(p)}{2-p}.\tag{2}
\]
For \(0<p<1\), the center's leaf-destination distribution \((a,b,\ldots,b)\) is nonuniform; hence \(F_m(p)<\log m\). Equations (1)--(2) give strict center dominance for the whole open parameter interval.

**2. Center optimum.** Direct differentiation of (1) yields
\[
h'_{c,m}(p)=\frac{\log[(1-p)/(mp^2)]}{(2-p)^2}.\tag{3}
\]
Its sign changes exactly once, when \(1-p=mp^2\). Solving yields the displayed unique center maximizer. Substituting \(m=(1-p)/p^2\) into (1) gives \(h_{c,m}(p_{c,m})=-\log p_{c,m}\). Expanding the positive root gives \(p_{c,m}=m^{-1/2}+O(m^{-1})\) and \(\max h_{c,m}=\frac12\log m+\frac12m^{-1/2}+O(m^{-1})\).

**3. Exact collision-entropy decomposition at the peripheral root.** The center-to-reset-leaf destination can arise from either hopping or resetting. The entropy lost by forgetting which event occurred is
\[
G_m(p)=a H(p/a)=p\log(1+b/p)+b\log(1+p/b)\ge0,
\]
so that \(F_m(p)=H(p)+(1-p)\log m-G_m(p)\). Thus (2) is equivalently
\[
h_{\ell,m}(p)=H(p)+\frac{(1-p)^2}{2-p}\log m-\frac{1-p}{2-p}G_m(p).\tag{4}
\]
For \(0<p<1\), using \(\log(1+x)\le x\),
\[
0\le G_m(p)\le b\big[1+\log(1+p/b)\big].\tag{5}
\]
At fixed \(m\), \(F_m(p)=\log m+O(p^2)\) as \(p\downarrow0\). Equation (2) then gives \(h_{\ell,m}(p)=\frac12\log m+\frac12p\log(1/p)+O(p)\). Thus every \(m\ge2\) has a global leaf maximizer in \((0,1)\), although no finite-\(m\) uniqueness assertion is needed.

**4. Uniform localization of all leaf optimizers.** Set \(g(p)=\frac12-\frac{(1-p)^2}{2-p}=p(3-2p)/[2(2-p)]\). The entropy gain above no resetting is exactly
\[
\Delta_m(p)=H(p)-g(p)\log m-\frac{1-p}{2-p}G_m(p).\tag{6}
\]
For the trial point \(p_0=m^{-3/4}\), (5) gives \(G_m(p_0)=O((\log m)/m)\). The expansions \(H(p)=p(\log(1/p)+1)+O(p^2)\) and \(g(p)=3p/4+O(p^2)\) therefore yield
\[
\Delta_m(p_0)=m^{-3/4}(1+o(1))>0.\tag{7}
\]
For \(0<p\le m^{-4/5}\), (6) and \(H(p)\le p\log(e/p)\) give
\[
\Delta_m(p)\le m^{-4/5}\big(1+(4/5)\log m\big)=o(m^{-3/4}).\tag{8}
\]
For \(m^{-7/10}\le p\le 1/10\), since \(g(p)/p=(3-2p)/[2(2-p)]\ge14/19>7/10\), (6) gives \(\Delta_m(p)\le p[1-(14/19-7/10)\log m]<0\) for sufficiently large \(m\). For \(p\ge1/10\), \(H(p)\le\log2\) and \(g(p)\ge g(1/10)>0\), so again \(\Delta_m(p)<0\) eventually. Therefore **every** global leaf maximizer lies in
\[
m^{-4/5}<p_{\ell,m}<m^{-7/10}\tag{9}
\]
for all sufficiently large \(m\).

**5. The sharp peripheral exponent and gain.** On the entire interval (9), \(p\to0\), \(mp\to\infty\), \(p\log m\to0\), and the bound (5) gives \(G_m(p)=O((\log m)/m)\) uniformly. Differentiation of the exact collision formula gives
\[
G_m'(p)=\log(1+b/p)-\frac1m\log(1+p/b)=o(1)\tag{10}
\]
uniformly there. Differentiating (4), and noting \(\frac{d}{dp}[(1-p)^2/(2-p)]=-3/4+O(p)\), yields uniformly on (9)
\[
h'_{\ell,m}(p)=\log(1/p)-\frac34\log m+o(1).\tag{11}
\]
Each global optimizer is interior, so its derivative vanishes. Consequently \(\log(m^{3/4}p_{\ell,m})=o(1)\), giving \(m^{3/4}p_{\ell,m}\to1\). Substituting this fact in (6), using \(G_m=O((\log m)/m)=o(p_{\ell,m})\), shows
\[
\Delta_m(p_{\ell,m})=p_{\ell,m}\left[\log(1/p_{\ell,m})-\frac34\log m+1+o(1)\right]
=p_{\ell,m}(1+o(1)).\tag{12}
\]
This proves the asserted unit leading constant for the leaf gain. Combining it with Step 2 gives the asymptotic gain ratio \(m^{1/4}/2\).

## Verification
Run `python3 verify.py` from the same directory as this document. It forms the full \((m+1)\)-state transition matrix, solves its stationary equations by Gaussian elimination, and computes Shannon entropy independently of (1)--(2). It checks both root types, derivative identities, the center optimum and large-\(m\) scaling. The observed check summary is `CHECKS_OK` with 185 assertions. These are finite checks supporting, but not replacing, Steps 1--5, which establish every quantified statement analytically.

## Relationship to prior work
Wang and Chen (2022) give the Markov resetting rule and entropy-rate framework, and study regular random networks, finite Cayley trees and degree-heterogeneous networks, including sensitivity to the reset node. Their inspected discussion treats the finite Cayley tree numerically and does not present the star's two root-dependent asymptotic exponents or the sharp peripheral entropy gain. Burda, Duda, Luck and Waclaw (2008/2009) establish that the maximum path entropy on a fixed graph is the logarithm of the adjacency Perron eigenvalue. This classical result already explains the center's optimized rate as the Perron entropy of a star with a self-loop at the center; **that center benchmark alone is not advanced as novel**. The added statement is the quantitative \(m^{-3/4}\) peripheral-root law, together with its comparison with the center-rooted \(m^{-1/2}\) law for the same resetting protocol. Chen and Ye (2022) instead analyze time-dependent resetting and first-passage observables, not these optimized trajectory-entropy scalings.

## Limitations
The asymptotic statement concerns the number of leaves tending to infinity, not a thermodynamic limit for interacting particles. There is no assertion that the leaf entropy rate has a unique maximizing reset probability for each finite \(m\); only existence and the asymptotic behavior of **every** maximizer are proved. The results use vertex-observed entropy, not the higher entropy of a process additionally observing reset-event labels. They concern uniform nearest-neighbor hopping, a fixed single resetting node, and a homogeneous per-step reset probability. A full priority determination beyond the inspected sources, including possible equivalent results under different terminology, remains open; independent scientific validation has not been performed.

## References
1. Y. Wang and H. Chen, *Entropy rate of random walks on complex networks under stochastic resetting*, arXiv:2208.05665, first public 2022-08-11; *Phys. Rev. E* **106**, 054137 (2022). https://arxiv.org/abs/2208.05665
2. Z. Burda, J. Duda, J. M. Luck and B. Waclaw, *Localization of maximal entropy random walk*, arXiv:0810.4113, first public 2008-10-22; *Phys. Rev. Lett.* **102**, 160602 (2009). https://arxiv.org/abs/0810.4113
3. H. Chen and Y. Ye, *Random walks on complex networks under time-dependent stochastic resetting*, arXiv:2208.06212, first public 2022-08-12; *Phys. Rev. E* **106**, 044139 (2022). https://arxiv.org/abs/2208.06212
