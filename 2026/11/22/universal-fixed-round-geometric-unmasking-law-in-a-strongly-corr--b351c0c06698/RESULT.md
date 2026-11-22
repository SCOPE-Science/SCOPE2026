# Universal fixed-round geometric unmasking law in a strongly correlated Ising chain

## Finding
For every **fixed integer** \(m\ge2\), the globally minimum per-site path-relative-entropy cost of independent parallel unmasking of a nearly ordered fair binary Markov chain has the exact leading asymptotics
\[
\inf_{\mathbf p}B_m(f;\mathbf p)\sim m(\log2)^{1/m}f^{(m-1)/m},\qquad f\downarrow0.
\]
Every global minimizer, not just one constructed schedule, obeys
\[
p_j\sim(f/\log2)^{(m-j)/m}\quad(1\le j<m).
\]
Equivalently, at correlation length \(\xi=-1/\log(1-2f)\), the optimum is asymptotic to \(m(\log2)^{1/m}(2\xi)^{-(m-1)/m}\). The number of rounds is fixed before the low-switch-density limit. This is a theorem about **path** relative entropy, not about final-output relative entropy.

## Assumptions and scope
Let \((X_i)_{i\in\mathbb Z}\) be the symmetric two-state stationary Markov chain with \(\mathbb P(X_{i+1}\ne X_i)=f\), \(0<f<1/2\). Put \(\lambda=1-2f\in(0,1)\). At round \(j\) a still-unrevealed site is chosen with probability \(q_j\), independently across sites, and the chosen spins are sampled **independently conditional on the previously revealed spins**, using exact marginal conditionals. The comparison joint sampler samples the same selected block from its exact conditional joint distribution. Its path-level relative entropy relative to the factorized sampler, averaged over reveals, is the sum of roundwise conditional total correlations, denoted by \(B_m\) after division by system length and the infinite-length limit. This is the exact error functional studied by Baule [1], Eq. (22); no many-round smooth-schedule approximation is used.

Take \(p_0=0\), \(p_m=1\) and arbitrary nondecreasing \(0\le p_1\le\cdots\le p_{m-1}\le1\), where \(q_j=(p_j-p_{j-1})/(1-p_{j-1})\) and \(q_m=1\) if \(p_{m-1}<1\). Empty rounds are allowed; the final theorem shows that none is optimal for sufficiently small \(f\). The order of limits is first chain length \(L\to\infty\) at fixed parameters, then \(f\downarrow0\).

## Proof
**1. Exact positive entropy series.** The mutual information between spins \(d\) edges apart is
\[
I_f(d)=\frac12[(1+\lambda^d)\log(1+\lambda^d)+(1-\lambda^d)\log(1-\lambda^d)]
=\sum_{k\ge1}c_k\lambda^{2kd},\quad c_k=\frac1{2k(2k-1)}.
\]
In particular, \(\sum_{k\ge1}c_k=\log2\). From the exact gap-averaged four-point information identity [1, Eqs. (22), (31)], the error per site for one reveal stage, preceded by revealed fraction \(p\), with conditional reveal probability \(q\), is
\[
e_f(p,q)=p^2q^2\sum_{\ell,d,r\ge1}(1-p)^{\ell+d+r-1}(1-q)^{d-1}\big[I_f(d)-I_f(d+\ell)-I_f(d+r)+I_f(d+\ell+r)\big].\tag{1}
\]
All terms are nonnegative. Substitution of the information series and three geometric sums gives the **exact** positive expression
\[
e_f(p,q)=q^2(1-p)^2\sum_{k\ge1}\frac{\lambda^{2k}}{2k(2k-1)[1-(1-p)(1-q)\lambda^{2k}]}\left(\frac{1-\lambda^{2k}}{1-(1-p)\lambda^{2k}}\right)^2.\tag{2}
\]
Formula (2), unlike (1), is continuous at \(p=0\), where it simplifies to \(q^2\sum c_k\lambda^{2k}/[1-(1-q)\lambda^{2k}]\). Consequently
\[
B_m(f;\mathbf p)=\sum_{j=1}^m e_f(p_{j-1},q_j).\tag{3}
\]
The sum is continuous on the compact simplex of cumulative reveal fractions, including empty rounds, so a global minimizer exists.

**2. Three uniform estimates needed for the singular limit.** First, if \(q\downarrow0\) and \(f/q\to0\), then
\[
e_f(0,q)=q\log2\,(1+o(1)).\tag{4}
\]
Indeed, after division by \(q\), each summand is \(c_kq\lambda^{2k}/[1-(1-q)\lambda^{2k}]\le c_k\), tends to \(c_k\) for each fixed \(k\), and dominated convergence applies.

Second, if \(p\downarrow0\), \(f/p\to0\), \(q/p\to\infty\), and \(0<q\le1\), then
\[
e_f(p,q)=\frac{fq}{p}\,(1+o(1)).\tag{5}
\]
To verify the coefficient, split (2) into the ranges \(k\ll p/f\), \(k\asymp p/f\), and \(k\gg p/f\). Uniformly on the middle range, putting \(t=4fk/p\) and using \(c_k\sim(4k^2)^{-1}\), \(1-\lambda^{2k}\sim4fk\), and \(1-(1-p)(1-q)\lambda^{2k}\sim q\), the sum is the Riemann integral
\[
\frac{fq}{p}\int_0^\infty\frac{dt}{(1+t)^2}=\frac{fq}{p}.
\]
A rigorous tail bound comes from \(1-\lambda^{2k}\le C\min(fk,1)\), \(1-(1-p)\lambda^{2k}\ge c\min(p+fk,1)\), and \(c_k\le Ck^{-2}\). On \(k\ge\varepsilon/f\), the contribution is \(O(fq)=o(fq/p)\); on \(k\le\varepsilon p/f\) it is \(O(\varepsilon fq/p)\); on \(k\ge Mp/f\) it is \(O(fq/(Mp))\), uniformly after letting \(\varepsilon\downarrow0\), \(M\uparrow\infty\). The denominator containing \(q\) is uniformly \(q(1+o(1))\) over the range that contributes, because \(q/p\to\infty\).

Third, there exists a constant \(c>0\) such that for all sufficiently small \(f\), all \(0\le p\le1/2\), and all \(0\le q\le1\),
\[
e_f(p,q)\ge c\frac{fq^2}{(p+f)(p+q+f)}.\tag{6}
\]
For a direct proof in (2), restrict to integers \(K\le k\le2K\) with \(K=\max\{1,\lceil(p+f)/(4f)\rceil\}\). In that block \(1-\lambda^{2k}\asymp p+f\), \(\lambda^{2k}\ge c\), and \(\sum_{k=K}^{2K}c_k\ge c/K\asymp f/(p+f)\). Also \(1-(1-p)\lambda^{2k}\le C(p+f)\) and \(1-(1-p)(1-q)\lambda^{2k}\le C(p+q+f)\), while \((1-p)^2\ge1/4\). These comparisons yield (6) with universal constants.

**3. Candidate upper bound and forced scale separation of every global minimizer.** Let \(s=f^{1/m}\) and choose trial fractions
\[
p_j=(f/\log2)^{(m-j)/m}\quad(1\le j<m).\tag{7}
\]
Equations (4)–(5), applied to the first stage and the remaining stages respectively, show that each of the \(m\) stage errors is \((\log2)^{1/m}f^{(m-1)/m}(1+o(1))\). Thus the global minimum is \(O(f^{(m-1)/m})\).

Let \(\mathbf p^*\) be any minimizing fractions and set \(t_j=(p_j^*+f)/(p_{j-1}^*+f)\ge1\). Suppose \(j\) is the first round at which \(p_j^*\ge1/2\). Then all preceding \(p_{i-1}^*<1/2\) and (6), with \(q_i=(p_i^*-p_{i-1}^*)/(1-p_{i-1}^*)\), entails
\[
e_f(p_{i-1}^*,q_i)\ge cf\frac{(t_i-1)^2}{t_i}.
\]
Since the total error is \(O(f^{(m-1)/m})\), this forces \(t_i\le C f^{-1/m}\) until the first crossing. But their product up to the first crossing is at least \((1/2+f)/f\asymp f^{-1}\), which is impossible in fewer than \(m\) rounds. The first crossing therefore occurs in the last round. For all \(m\) ratios, \(\prod_{i=1}^m t_i=(1+f)/f\), while the individual upper bounds are \(Cf^{-1/m}\); hence each ratio satisfies \(c'f^{-1/m}\le t_i\le C'f^{-1/m}\). It follows that, **uniformly over all minimizers**,
\[
p_j^*=\Theta(f^{(m-j)/m})\quad(1\le j<m),
\]
and the conditions of (4)–(5) apply to every stage, including the final round with \(q_m=1\).

**4. Sharp constants by compact variational reduction.** Write \(p_j^*=\theta_j(f) f^{(m-j)/m}\), with \(\theta_m=1\). Step 3 keeps all \(\theta_j\) in a fixed compact subset of \((0,\infty)\). Along every convergent subsequence, (3)–(5) give the asymptotic objective
\[
\frac{B_m(f;\mathbf p^*)}{f^{(m-1)/m}}
=\log2\,\theta_1+\sum_{j=2}^m\frac{\theta_j}{\theta_{j-1}}+o(1).
\]
The product of the \(m\) positive terms on the right equals \(\log2\); hence AM–GM gives the sharp lower bound \(m(\log2)^{1/m}\), and equality holds only when **all \(m\) terms are equal**. This fixes \(\theta_j=(\log2)^{-(m-j)/m}\). Every convergent subsequence has this same limit, so the whole sequence of global minimizers does too. Matching the trial upper bound in Step 3 completes the proof.

## Verification
Formula (2) is obtained from (1) by summing a positive series, not by a truncation argument. The included `checker.py` independently compares (2) against the original three-gap sum for several moderate parameters, validates the unscreened first-stage limit, and checks the predicted leading terms at low switch densities for two, three and four rounds. Computation is a consistency test; the infinite-volume and all-round statements rest on the analytic bounds and variational argument above. To reproduce: run `python checker.py` with Python 3, NumPy and SciPy (no external data).

## Relationship to prior work
Baule [1] gives an **exact** finite-round gap formula, while its smooth geodesic metric and optimal-schedule discussion use a separate many-round approximation. The present theorem applies directly to the exact screened error at **each fixed** round count in the singular \(f\downarrow0\) regime and proves a sharp constant and limiting global minimizers. The existing three-round cubic-root result [2] follows as the \(m=3\) case, but does not itself imply arbitrary fixed \(m\). General information-profile and schedule-optimization works [3–5] establish broad representations, bounds, recursive stationarity conditions and smooth/simultaneous-size limits, without identifying this sharp fixed-\(m\) Ising low-switch-density law in the inspected material.

## Limitations
The theorem makes no statement uniform in the number \(m\) of rounds, and does not interchange the thermodynamic limit with the rare-switching limit. It is restricted to the symmetric nearest-neighbor two-state Markov law, ideal denoisers, independent Bernoulli site reveals and **path** relative entropy. It does not estimate terminal-output KL, generative perplexity, runtime, or performance for language data or interacting non-Markov fields. The evidence does not constitute independent scientific verification or exhaust unindexed mathematical literature.

## References
[1] A. Baule, *Masked diffusion as random sequential adsorption: an exactly solvable model for parallel decoding*, arXiv:2611.07845v1 (first submitted 5 November 2026), https://arxiv.org/abs/2611.07845. In particular Eqs. (17), (21), (22), (30)–(32).

[2] *A cubic-root optimal three-stage unmasking law*, previously recorded research finding, ID `20c36fe8-a19f-45e0-bed6-9358ab7d149d`.

[3] H. Lavenant and G. Zanella, *Error Bounds and Optimal Schedules for Masked Diffusions with Factorized Approximations*, arXiv:2510.25544v1 (2025), https://arxiv.org/abs/2510.25544.

[4] M. J. Wainwright, *The data geometry of masking diffusion: Certified-optimal schedules via unmasking growth complexity*, arXiv:2608.13520v1 (2026), https://arxiv.org/abs/2608.13520.

[5] C. Secchi and G. Zanella, *Schedule optimization for tau-leaping in masked discrete diffusion*, arXiv:2609.21960v1 (2026), https://arxiv.org/abs/2609.21960.
