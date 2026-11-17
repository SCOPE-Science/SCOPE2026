# A temporal-correlation density resonance in the Markov-switched Pelikan map

## Finding

The expanding and contracting maps of the Pelikan random system admit a **complete stationary law within the dyadic-uniform density class** when the choice of map is driven by a persistent two-state Markov environment rather than independent draws. The law exhibits a sharp three-way density regularity transition—bounded, logarithmically unbounded, power-law unbounded—**while the fraction of expanding steps and the Lyapunov exponent can be held fixed**.

Let the mode be \(J_n\in\{E,C\}\) with transition matrix (in the order \(E,C\))
\[
P=\begin{pmatrix}1-u&u\\v&1-v\end{pmatrix},\qquad 0<u,v<1.
\]
First sample \(J_{n+1}\) using \(P\), then apply \(X_{n+1}=T_{J_{n+1}}(X_n)\), where \(T_E(x)=2x\pmod1\) and \(T_C(x)=x/2\). Let \(I_k=[2^{-(k+1)},2^{-k})\) and let \(m_k\) be the invariant mass of \(I_k\), summed over the two modes.

There exists exactly one stationary probability in the class of joint densities constant on each \(I_k\) separately for each mode **if and only if** \(v>u\). Put
\[
r=\frac{1-v}{1-u},\qquad e_0=\frac{v-u}{2(1-u)(u+v)},\qquad a=\frac{u(2-u-v)}{1-u}.
\]
Its exact probability generating function is
\[
\boxed{M(z)=\sum_{k\ge0}m_kz^k=\frac{v-u}{u+v}\frac{1+(u+v-1)z}{(2-z)[1-u-(1-v)z]}.}
\]
The coefficients are positive and equal to
\[
\boxed{m_k=e_0\left[2^{-k}+a\sum_{j=0}^{k-1}2^{-(k-1-j)}r^j\right],\qquad k\ge0,}
\]
with the empty sum equal to zero. Accordingly, the invariant density is exactly \(f(x)=2^{k+1}m_k\) on \(I_k\). Its sharp classification as \(x\downarrow0\) is:

1. \(r<1/2\): \(f\) is bounded, with \(f|_{I_k}\to 2e_0[1+a/(1/2-r)]\).
2. \(r=1/2\): \(v=(1+u)/2\) and
   \[
   \boxed{m_k=\frac{1+3uk}{2(1+3u)}2^{-k},\qquad f|_{I_k}=\frac{1+3uk}{1+3u},}
   \]
   giving an exact logarithmic divergence.
3. \(r>1/2\): \(f|_{I_k}\sim[2e_0a/(r-1/2)](2r)^k\). Thus the shell density has a power-law singularity with exponent \(\log_2(2r)\in(0,1)\).

For a fixed mode frequency \(p\in(1/2,1)\), write \(u=(1-p)s\) and \(v=ps\), where \(0<s<1/p\). The mode's stationary expanding fraction is always \(p\), and its time-averaged Lyapunov exponent is \((2p-1)\log2>0\). Nevertheless the density switches from power-law to logarithmic to bounded as \(s\) passes the **interior threshold**
\[
\boxed{s_*(p)=\frac{1}{3p-1}.}
\]
The transition therefore cannot be inferred from the average expansion rate alone.

## Assumptions and scope

All statements concern the two-state environment with \(0<u,v<1\), the post-transition mode application described above, and stationary joint densities uniform on each dyadic shell for each mode. The state space is \(x\in(0,1)\); endpoint atoms, including the absorbing fixed point at zero, are excluded from the asserted uniqueness. This is a complete classification **within the specified invariant subspace**, not a claim of global uniqueness among all Borel invariant measures. Exact dyadic endpoints form a measure-zero exceptional set for the densities at issue.

## Proof

**1. Closed transfer dynamics.** Write \(e_k\) and \(c_k\) for the stationary masses in \(I_k\) jointly with the modes \(E\) and \(C\). Contraction moves \(I_k\) onto \(I_{k+1}\) and never lands in \(I_0\). Expansion moves \(I_{k+1}\) onto \(I_k\) for all \(k\ge0\). Expansion from \(I_0\) maps uniform area onto uniform area on the full unit interval, distributing mass as \(h_k=2^{-(k+1)}\). Consequently the stationary equations are, for all \(k\ge0\),
\[
 c_0=0,\qquad c_{k+1}=ue_k+(1-v)c_k,
\]
\[
 e_k=(1-u)e_{k+1}+vc_{k+1}+(1-u)e_0 2^{-(k+1)}.
\]
All shell-uniform joint densities map to shell-uniform densities, so these equations are necessary and sufficient for stationarity in the stated class.

**2. Generating functions and normalization.** For \(|z|<1\), set \(E(z)=\sum e_kz^k\), \(C(z)=\sum c_kz^k\). The first recursion gives
\[
C(z)=\frac{uz}{1-(1-v)z}E(z).
\]
Substitute into the second recursion and cancel the common \(1-z\) factor to obtain the **exact rational identities**
\[
E(z)=\frac{2(1-u)e_0[1-(1-v)z]}{(2-z)[1-u-(1-v)z]},
\quad
C(z)=\frac{2(1-u)ue_0z}{(2-z)[1-u-(1-v)z]}.
\]
Hence \(M=E+C\) has the claimed rational form, with \(e_0\) fixed by \(M(1)=1\): \(e_0=(v-u)/[2(1-u)(u+v)]\).

A normalized stationary law must have \(e_0>0\): if \(e_0=0\), the nonnegative stationary equation at \(k=0\) forces \(e_1=c_1=0\); inductively every mass vanishes. If \(v<u\), the forced rational \(E(z)\) has a noncanceled pole at \(z=(1-u)/(1-v)\in(0,1)\), impossible for the generating function of a probability. If \(v=u\), the same formula diverges as \(z\uparrow1\), again impossible. This excludes finite stationary shell-uniform probabilities when \(v\le u\).

When \(v>u\), both poles of the stated rational generating functions lie outside the closed unit disk, since \(0<r<1\). Expanding the two geometric factors gives the displayed nonnegative coefficients. They sum to one, verify both recursions coefficientwise, and therefore construct a stationary probability. The recursions and normalization also force its uniqueness within the class.

**3. Exact density resonance.** From \(M(z)=e_0[1+(u+v-1)z]/[(1-z/2)(1-rz)]\), coefficient extraction yields the stated formula with \(a=u(2-u-v)/(1-u)>0\). For \(r\ne1/2\),
\[
\sum_{j=0}^{k-1}2^{-(k-1-j)}r^j=\frac{r^k-2^{-k}}{r-1/2}.
\]
This establishes the bounded/power-law cases. When \(r=1/2\), the sum is \(k2^{-(k-1)}\); substituting \(v=(1+u)/2\), \(a=3u/2\), and \(e_0=1/[2(1+3u)]\) proves the exact logarithmic formula, including \(k=0\). No numerical extrapolation is needed for any boundary.

**4. Fixed-Lyapunov crossover.** The mode chain has stationary expanding fraction \(p=v/(u+v)\). Its empirical mode frequencies converge almost surely to these stationary weights, hence the log-slope average is \((2p-1)\log2\), apart from zero-measure fold preimages. For fixed \(p\in(1/2,1)\), the admissible parameterization \(u=(1-p)s\), \(v=ps\) obeys \(0<s<1/p\). The equation \(r=1/2\) is equivalent to \(s=1/(3p-1)\). Since \(0<s_*<1/p\), all three density regimes occur at the same strictly positive Lyapunov exponent.

## Verification

A standalone Python script `check_markov_pelikan.py` uses exact rational arithmetic to verify all stationary balance equations across 36 shells for each of four rational parameter pairs (144 shells total). It independently checks the rational coefficient recurrence and the closed critical \(r=1/2\) formula. Its replay output ends with `MARKOV_PELIKAN_EXACT_RATIONAL_OK cases=4 exact_shells=144`. The infinite-step existence, necessity, and sharp classification follow from the preceding algebra, not from finite tests.

## Relationship to prior work

Yan, Majumdar, Ruffo, Sato, Beck and Klages (2023 preprint; 2024 journal) establish invariant densities, correlations and regularity transitions for the same two maps chosen **independently** at every step. Monthus (2024 preprint; 2025 journal) studies the iid Pelikan map using a Markov chain on dyadic **position shells**; that derived depth Markov chain is not the two-state **correlated switching environment** analyzed here. A previous result for this map concerns iid random-driver path couplings and a critical-window occupation law, also not this stationary joint law. General results on random switching and invariant density regularity concern other flows or provide broad existence/regularity criteria, not the explicit two-state switching shell spectrum or a fixed-Lyapunov resonance.

## Limitations

This theorem does not establish uniqueness among arbitrary singular stationary measures, convergence from arbitrary initial laws, or the existence/nonexistence of other invariant probabilities outside the dyadic-uniform class. The atom at zero is invariant in the completed interval. The sign of the Lyapunov exponent alone does not imply a precise dynamical classification outside this model. A broader matrix-geometric stationary-law treatment or an unindexed equivalent formulation remains a publication-priority risk. Independent mathematical verification has not been performed.

## References

- J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269, first posted 2023-08-18; *Chaos* 34, 023128 (2024). https://arxiv.org/abs/2308.09269
- C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, arXiv:2409.19999, first posted 2024-09-30. https://arxiv.org/abs/2409.19999
- Y. Bakhtin, T. Hurth, J. Mattingly, *Regularity of invariant densities for 1D systems with random switching*, arXiv:1406.5425 (2014), *Nonlinearity* 28 (2015). https://arxiv.org/abs/1406.5425
