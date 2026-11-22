# Squared-corruption stationary bias and a sharp largest-gap relaxation law for residual-weighted Kaczmarz

## Finding
For generalized weighted randomized Kaczmarz (GWRK) with a **fixed** exponentially decreasing residual weight, the exact scalar corrupted-measurement model has a reversible, finite-state transition law. As weighting becomes arbitrarily aggressive, its stationary probability of each measurement value approaches the **square of that value's row multiplicity**, normalized by the sum of all squared multiplicities. Thus stronger downweighting can make the first wrong projection exponentially rare without removing stationary corruption error. Moreover, when the distinct measurement values have a unique largest consecutive separation, the slowest relaxation rate is exponentially controlled by that largest separation, with an exact prefactor that depends on both neighboring multiplicities and the squared masses of the two sides.

## Assumptions and scope
Fix an integer \(s\ge2\), distinct real values \(v_1<\cdots<v_s\), positive integer multiplicities \(n_1,\ldots,n_s\), and a fixed parameter \(\eta>0\). All rows of the linear system equal the scalar \(1\); the right-hand side has exactly \(n_i\) rows of value \(v_i\). At state \(x\), independently select a row with probability proportional to \(f_\eta(|x-v_i|)=\exp(-\eta|x-v_i|)\), then perform the ordinary exact unit-row Kaczmarz projection \(x^+=v_i\). The weight parameter is fixed across time, and probabilities are recomputed after every projection. This is a specialization of the generalized residual-weighted sampling rule of Chen et al. [1], **not** their median- or MAD-adaptive exponential scale and not a quantile-accepted method.

Every iterate after the first lies in the finite state set \(\{v_1,\ldots,v_s\}\), regardless of initial real \(x\). Define
\[
K_{ij}=e^{-\eta|v_i-v_j|},\quad Z_i=\sum_{j=1}^s n_jK_{ij},\quad S=\sum_{i=1}^s n_i Z_i.
\]
For corruption statements only, suppose exactly one level is \(0\), with \(g\ge1\) clean rows; the remaining levels contain \(k\ge1\) corrupted rows in total (optionally \(k<g\) in the sparse-majority setting). Squared error always refers to error relative to the clean solution \(0\). All limiting assertions in this result keep the finite set of levels and multiplicities fixed as \(\eta\to\infty\).

## Proof
**Exact chain and stationarity.** From state \(v_i\), each of the \(n_j\) rows at level \(v_j\) receives identical weight \(K_{ij}\); normalization gives
\[
P_{ij}=\frac{n_jK_{ij}}{Z_i}.
\]
All entries are positive, hence the chain is irreducible and aperiodic. The probability vector
\[
\boxed{\pi_i=\frac{n_iZ_i}{S}}
\]
sums to one and satisfies detailed balance because
\[
\pi_iP_{ij}=\frac{n_in_jK_{ij}}{S}=\pi_jP_{ji}.
\]
It is therefore the unique stationary distribution. More generally, this reversible-kernel calculation holds for **any** strictly positive, fixed residual weight depending symmetrically on the absolute difference of measurement values; it is a standard weighted-graph identity rather than a claim of a new reversibility principle.

**Squared-multiplicity corruption and exact first-escape horizon.** Since the levels are distinct, \(K_{ij}\to\mathbf 1_{i=j}\); therefore \(Z_i\to n_i\) and \(S\to\sum_j n_j^2\). It follows that
\[
\boxed{\pi_i\longrightarrow\frac{n_i^2}{\sum_j n_j^2}.}
\]
If \(k\) bad rows form levels of multiplicities \(k_1,\ldots,k_r\), the limiting stationary corruption probability is
\[
B_\infty=\frac{\sum_{j=1}^{r}k_j^2}{g^2+\sum_{j=1}^{r}k_j^2},
\qquad \boxed{\frac{k}{g^2+k}\le B_\infty\le\frac{k^2}{g^2+k^2}.}
\]
The bounds are attained, respectively, when all bad measurements are at distinct nonzero levels (each multiplicity one) and when all bad rows share one nonzero level; the inequalities use \(k\le\sum_j k_j^2\le k^2\). Consequently the stationary mean squared error tends to \(\sum_j n_j^2 v_j^2/\sum_jn_j^2\), which is strictly positive if any bad level is present.

Start at the clean value \(0\) and let \(\tau=\min\{t\ge1:X_t\ne0\}\). While the process remains at zero it makes fresh independent selections with the same escape probability
\[
p_\eta=\frac{\sum_{v_j\ne0}n_je^{-\eta|v_j|}}{g+\sum_{v_j\ne0}n_je^{-\eta|v_j|}}.
\]
Thus \(\Pr(\tau>T)=(1-p_\eta)^T\) for all nonnegative integers \(T\). Set \(d=\min_{v_j\ne0}|v_j|>0\) and \(k_*=\sum_{|v_j|=d}n_j\). Then \(p_\eta\sim (k_*/g)e^{-\eta d}\), so for every \(t\ge0\),
\[
\boxed{\Pr\bigl(\tau>\lfloor te^{\eta d}\rfloor\bigr)\longrightarrow e^{-tk_*/g}.}
\]
The first wrong update is therefore governed by the **nearest** bad level, even if the chain's eventual global relaxation is governed by a different, more distant gap.

**Sharp largest-gap spectral law.** Put \(d_i=v_{i+1}-v_i\) for \(1\le i<s\). Suppose the maximum \(\Delta=\max_i d_i\) is attained at a **unique** index \(a\). Let
\[
M_L=\sum_{i\le a}n_i^2,\qquad M_R=\sum_{i>a}n_i^2.
\]
Let \(\lambda_2(P_\eta)\) denote the largest eigenvalue other than the simple eigenvalue one. Detailed balance makes the eigenvalues real; the finite symmetric kernel \(e^{-\eta|v_i-v_j|}\) is positive definite for distinct ordered levels (it is the covariance of a nondegenerate stationary Ornstein–Uhlenbeck vector), so all eigenvalues of \(P_\eta\) are positive. Define the spectral gap \(\gamma_\eta=1-\lambda_2(P_\eta)>0\). Then
\[
\boxed{\lim_{\eta\to\infty}e^{\eta\Delta}\gamma_\eta
=n_an_{a+1}\left(\frac1{M_L}+\frac1{M_R}\right).}
\]
Here is a direct variational proof, including the prefactor. Reversibility gives the Rayleigh characterization
\[
\gamma_\eta=\min_{\operatorname{Var}_{\pi}(u)>0}
\frac{\mathcal E_\eta(u)}{\operatorname{Var}_{\pi}(u)},\qquad
\mathcal E_\eta(u)=\frac1S\sum_{i<j}n_in_je^{-\eta|v_i-v_j|}(u_i-u_j)^2.
\]
Test vectors constant at distinct values \(A\) and \(B\) on the two blocks \(\{1,\ldots,a\}\) and \(\{a+1,\ldots,s\}\). Among all cross-block pairs, only \((a,a+1)\) has distance \(\Delta\); all others have strictly larger distance. Since \(S\to M_L+M_R\), this test yields the displayed constant as an upper bound for \(\limsup e^{\eta\Delta}\gamma_\eta\).

For the matching lower bound, choose minimizing vectors with \(\sum_i\pi_i u_i=0\) and \(\operatorname{Var}_{\pi}(u)=1\). Each stationary coordinate weight stays bounded away from zero as \(\eta\to\infty\), so these normalized vectors are bounded and have convergent subsequences. The just-established upper bound makes their scaled energy \(e^{\eta\Delta}\mathcal E_\eta(u)\) bounded. For every consecutive edge inside either block, its length \(d_i<\Delta\); its scaled Dirichlet coefficient diverges as \(e^{\eta(\Delta-d_i)}\). Hence differences between all neighboring coordinates **within** each block tend to zero. Every subsequential limit is therefore constant, say \(A\) on the left and \(B\) on the right; the variance normalization ensures \(A\ne B\). Retaining only the cross-edge \((a,a+1)\) in the nonnegative Dirichlet sum gives
\[
\liminf e^{\eta\Delta}\gamma_\eta\ge
\frac{n_an_{a+1}(A-B)^2/(M_L+M_R)}{M_LM_R(A-B)^2/(M_L+M_R)^2}
=n_an_{a+1}\left(\frac1{M_L}+\frac1{M_R}\right).
\]
This equals the upper bound for every convergent subsequence, proving the full limit. The uniqueness of the maximal gap is necessary for this two-block prefactor; tied maximal gaps require a different reduced-chain analysis and are **not** covered by this formula.

**Two-value exact finite-time benchmark.** With levels \(0\) (multiplicity \(g\)) and \(\delta\ne0\) (multiplicity \(k\)), write \(z=e^{-\eta|\delta|}\). The clean-to-bad and bad-to-clean probabilities are \(p=kz/(g+kz)\) and \(q=gz/(k+gz)\). Their stationary bad probability and exact transient from a clean start are
\[
\pi_{\mathrm{bad}}=\frac{k(k+gz)}{g^2+k^2+2gkz},\qquad
\Pr(X_t=\delta\mid X_0=0)=\pi_{\mathrm{bad}}\bigl[1-(1-p-q)^t\bigr].
\]
In the joint limit \(\eta\to\infty\), \(t_\eta=\lfloor az^{-1}\rfloor\), this latter probability tends to
\[
\frac{k^2}{g^2+k^2}\bigl(1-e^{-a(k/g+g/k)}\bigr).
\]
This explicitly separates a long apparently accurate transient from a persistent limiting bias.

## Verification
Run `python3 verification/verify.py` using only the Python standard library. The checker verifies **11,746 exact rational families** of transition normalization, detailed balance, stationarity, two-class finite-time evolution, and sharp multiplicity bounds; it also runs a high-precision, independent three-state spectral diagnostic. For levels \((0,1,4)\) with multiplicities \((4,1,2)\), the clean value is zero, the first corrupted state is typically reached at scale \(4e^\eta\), the stationary corruption probability tends to \(5/21\), and the exact spectral claim predicts
\[
\gamma_\eta\sim\frac{21}{34}e^{-3\eta}.
\]
At \(\eta=18\), the checker reports \(e^{54}\gamma_{18}\approx0.617647095607\), versus \(21/34\approx0.617647058824\). Exact finite checks and this numerical diagnostic **do not constitute proof** of the infinite-parameter statement; the Dirichlet compactness argument above supplies that proof.

## Relationship to prior work
Chen, Cheng, He, Kryshchenko, Chi, Ma and Haddock [1], Algorithm 2 and Theorem 3 with Remarks 1–3, introduce GWRK, establish one-step corruption-sensitive error bounds, and discuss how positivity of the corrupt-row weight can create a convergence horizon. The proof here specializes their row-selection rule to a fixed exponential weight and gives a global invariant law, sharp corruption-multiplicity bias, first-wrong-update clock, and unique-largest-gap spectral-relaxation prefactor, none stated in the inspected relevant sections. It does not assert that adaptive median/MAD weighting obeys these formulas.

Haddock, Ma and Rebrova [2], Algorithms 1–2 and Section V-D, consider a **different** quantile/subsampling selection mechanism. A published two-state sampled-quantile result [3] calculates exact hypergeometric corruption transitions and a rare-event clock, but its transition probabilities come from order-statistic sampling and do not imply the residual-dependent kernel above; the general idea of rare corrupted projections is prior work. The weighted sparse-Kaczmarz comparison [4] concerns increasing residual-power weights, a full-rank consistent model, and two finite steps. The two-row Markov Kaczmarz result [5] has an exogenous row-index Markov chain and fresh observation noise rather than residual-dependent endogenous selection. General reversible graph random-walk and Dirichlet variational identities are classical tools, not claimed discoveries. The new target is the **joint exact bias and sharp longest-gap metastable time scale** of this specific numerical method.

## Limitations
The entire result concerns one scalar unknown, identical unit rows, finitely many **fixed** response levels, fully recomputed row probabilities, independent sampling at every iteration, exact projections, and a fixed exponential decay parameter. It gives no general matrix-valued convergence theorem, no guarantee of practical solver quality or computational advantage, and no claim for adaptive weights, threshold methods, or nonlinear inverse problems. The two-block spectral formula assumes a unique maximal adjacent level gap and does not cover ties; levels and multiplicities remain fixed in the large-parameter limit. This is a mathematical finite-state counterexample and calibration result, not a proposed general optimizer. Independent verification and complete historical-priority certification have not been performed.

## References
1. J. Chen, Z. Cheng, Y. He, A. Kryshchenko, J. T. Chi, A. Ma, J. Haddock, *Weighted Randomized Kaczmarz for Sparsely Corrupted Linear Systems*, arXiv:2611.03889v1, first posted **2026-11-02**. https://arxiv.org/abs/2611.03889
2. J. Haddock, A. Ma, E. Rebrova, *On Subsampled Quantile Randomized Kaczmarz*, arXiv:2308.07987v1, first posted 2023-08-15. https://arxiv.org/html/2308.07987v1
3. *Exact two-state dynamics and a sharp rare-corruption horizon for small-sample quantile Kaczmarz*, published mathematical result (2026-10-25). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-two-state-dynamics-and-a-sharp-rare-corruption-horizon-for--2639ecb81dd1
4. *Two-step greed reversal in weighted sparse Kaczmarz and a two-row projection barrier*, published mathematical result (2026-10-12). https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-two-step-greed-reversal-in-weighted-sparse-kaczmarz-and-a-two-ro--f080ede8111d
5. *Sharp rate–noise Pareto frontier for two-row Markov Kaczmarz*, published mathematical result (2026-11-08). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-rate-noise-pareto-frontier-for-two-row-markov-kaczmarz--532e58979b34
