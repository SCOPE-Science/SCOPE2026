# Two sharp tail thresholds for transport restored by local resetting on a random comb

## Finding

A biased walker on a random comb with *unbiased*, finite reflecting teeth and tooth-local Poisson returns exhibits two distinct sharp tail-exponent boundaries. The first, at \(\alpha=1\), separates a zero-velocity unreset phase from a positive-velocity one; the second, at \(\alpha=3\), separates an infinite from a finite **right derivative of stationary drift with respect to the return rate**. The complete weak-return law has five regimes and explicit constants.

Let \(p>q>0\) be backbone jump rates, \(a>0\) the tooth-entry rate, and \(r\ge0\) the rate of returns to the local junction from every positive-depth tooth site. Let the independent tooth lengths \(L_i\ge1\) satisfy
\[
\Pr(L_i\ge n)\sim c n^{-\alpha}\quad(n\to\infty),\qquad c>0,\quad\alpha>0.
\]
The limiting stationary unwrapped backbone drift \(v(r)\) is defined by first taking stationarity on a periodic ring with \(N\) junctions, then \(N\to\infty\) along a typical infinite iid sequence of teeth, and finally varying \(r\). Put \(\mu=\mathbb E L\), potentially infinite, and for \(1<\alpha\) put
\[
v_0=\frac{p-q}{1+a\mu},\qquad K=\frac{(p-q)a}{(1+a\mu)^2}.
\]
Define convergent positive integrals
\[
I_{\alpha}=\int_0^\infty x^{-\alpha}\operatorname{sech}^2x\,dx\quad(0<\alpha<1),\qquad
J_{\alpha}=\int_0^\infty x^{-\alpha}\tanh^2x\,dx\quad(1<\alpha<3).
\]
Then all limits below are exact asymptotic equivalents as \(r\downarrow0\):

\[
\begin{array}{c|c}
\text{Tail range}&\text{Weak-return drift law}\\ \hline
0<\alpha<1&v(r)\sim\dfrac{p-q}{acI_{\alpha}}r^{(1-\alpha)/2}\\[5pt]
\alpha=1&v(r)\sim\dfrac{2(p-q)}{ac\log(1/r)}\\[5pt]
1<\alpha<3&v(r)-v_0\sim KcJ_{\alpha}r^{(\alpha-1)/2}\\[5pt]
\alpha=3&v(r)-v_0\sim\dfrac{Kc}{2}r\log(1/r)\\[5pt]
\alpha>3&v(r)-v_0\sim\dfrac{Kr}{6}\,\mathbb E[L(L+1)(2L+1)].
\end{array}
\]
In particular, \(v(0)=0\) exactly for \(0<\alpha\le1\), and \(v'(0+)\) is finite and strictly positive exactly for \(\alpha>3\). Throughout \(r>0\), the drift is strictly positive and strictly increasing in \(r\).

## Assumptions and scope

Take the finite periodic comb with junction vertices \((i,0)\), \(i\in\mathbb Z/N\mathbb Z\), \(N\ge3\). A tooth of length \(L_i\in\{1,2,\ldots\}\) attaches the vertices \((i,1),\ldots,(i,L_i)\). At a junction, the particle jumps to adjacent backbone junctions at right/left rates \(p,q\) and enters depth one at rate \(a\). At every positive tooth depth the particle jumps across each available vertical edge at **rate one** (the tip has one vertical edge, and the first-depth site has the edge to depth zero). Independently, each positive-depth site has a rate-\(r\) instantaneous transition to its own junction; at depth one this is an additional transition to an already adjacent destination. A putative reset at a junction does nothing. The unwrapped displacement counts only jumps on the backbone, with right and left increments \(+1\) and \(-1\); returns from teeth have zero displacement.

Each finite system is irreducible and has a unique stationary state. Write \(v_N(r)\) for its stationary expected unwrapped displacement per unit time. The iid sequence of \(L_i\) is sampled once (quenched). The statement concerns \(v(r)=\lim_{N\to\infty}v_N(r)\) almost surely at each fixed \(r\ge0\). The subsequent weak-return limit is sequential; no joint \(N,r\) scaling is asserted. The tail assumption is on the *survival probability* of the integer length, not its mass function. The exact formulas hold for positive real \(p,q,a\) and all \(r\ge0\), with the displayed tail asymptotics measured in the units where vertical jump rates equal one.

## Proof

**1. One-tooth occupation formula.** Consider the symmetric continuous-time walk on \(\{0,1,\ldots,L\}\), reflected at \(L\) and absorbed at \(0\), started at \(1\). Let \(T_L\) be its time to first hit \(0\). A rate-\(r\) local return to \(0\) truncates the excursion at an independent exponential time, with expected duration
\[
\tau_r(L)=\mathbb E\min(T_L,E_r)=\mathbb E\int_0^{T_L}e^{-rt}\,dt.
\]
For \(r>0\), the Laplace transform \(u_j=\mathbb E_j e^{-rT_L}\) satisfies \((2+r)u_j=u_{j-1}+u_{j+1}\) at interior tooth sites, \((1+r)u_L=u_{L-1}\) at the reflecting tip, and \(u_0=1\). The unique solution, setting \(\theta=\operatorname{arcosh}(1+r/2)\), is
\[
u_j=\frac{\cosh((L+\tfrac12-j)\theta)}{\cosh((L+\tfrac12)\theta)}.
\]
Thus
\[
\boxed{\tau_r(L)=\frac{1-\cosh((L-\tfrac12)\theta)/\cosh((L+\tfrac12)\theta)}{r}}\quad(r>0),
\qquad \tau_0(L)=L.
\tag{1}
\]
The last identity follows from the usual reflected Poisson equation or by letting \(r\downarrow0\). In the finite comb, the steady mass in tooth \(i\) equals the junction mass times \(a\tau_r(L_i)\): each entry is followed by the killed excursion described above, and expected occupation is its expected lifetime. This follows as well by summing the exact finite-state resolvent equations.

**2. Exact finite-ring drift and thermodynamic limit.** Summing the stationary master equations over all positive depths of each tooth eliminates vertical fluxes and returns; the remaining junction balance is
\[
p\pi_{i-1}+q\pi_{i+1}=(p+q)\pi_i,
\]
where \(\pi_i\) denotes junction probability. On a periodic ring with \(p>q\), the only solution is a constant \(\pi_i=\pi\) (by Fourier modes, or the maximum principle). Normalization gives \(\pi=[N+a\sum_i\tau_r(L_i)]^{-1}\); since only backbone jumps carry unwrapped displacement,
\[
\boxed{v_N(r)=\frac{p-q}{1+aN^{-1}\sum_{i=1}^N\tau_r(L_i)}.}\tag{2}
\]
For fixed \(r>0\), \(0\le\tau_r(L)\le 1/r\), and the strong law of large numbers yields \(v(r)=(p-q)/(1+aM(r))\), \(M(r)=\mathbb E\tau_r(L)\). For \(r=0\), \(\tau_0(L)=L\); the strong law gives the same formula if \(\mu<\infty\), while truncation plus the strong law implies \(N^{-1}\sum_i L_i\to\infty\) almost surely when \(\mu=\infty\). Hence \(v(0)=0\) in that case.

**3. Exact length increments and uniform bounds.** Subtracting (1) at lengths \(n\) and \(n-1\), and putting \(\delta_n(r)=\tau_r(n)-\tau_r(n-1)\) with \(\tau_r(0)=0\), gives
\[
\boxed{\delta_n(r)=\frac{\cosh^2(\theta/2)}{\cosh((n-\tfrac12)\theta)\cosh((n+\tfrac12)\theta)}
=\frac{1+\cosh\theta}{\cosh(2n\theta)+\cosh\theta}.}\tag{3}
\]
For \(r=0\), \(\delta_n(0)=1\). Since \(\theta/\sqrt r\to1\), for each fixed \(x>0\),
\[
\delta_{\lfloor x/\sqrt r\rfloor}(r)\to\operatorname{sech}^2 x,
\qquad 1-\delta_{\lfloor x/\sqrt r\rfloor}(r)\to\tanh^2x.
\tag{4}
\]
In addition, (3) yields, for \(0<r\le1\),
\[
0\le1-\delta_n(r)
=\frac{\cosh(2n\theta)-1}{\cosh(2n\theta)+\cosh\theta}
\le\tanh^2(n\theta)\le\min(1,rn^2),
\tag{5}
\]
and \(\delta_n(r)\le C e^{-2n\theta}\) for an absolute \(C\). At fixed \(n\), direct expansion gives \(\lim_{r\downarrow0}(1-\delta_n(r))/r=n^2\). By nonnegative sum interchange,
\[
M(r)=\sum_{n\ge1}s_n\delta_n(r),\qquad
\mu-M(r)=\sum_{n\ge1}s_n[1-\delta_n(r)]\quad(\mu<\infty),
\qquad s_n=\Pr(L\ge n).
\tag{6}
\]
These identities and (4)–(5) are the core of the singular-limit proof.

**4. The five regular-variation regimes.** Assume \(s_n\sim c n^{-\alpha}\). For \(0<\alpha<1\), split the sum (6) into \(n\sqrt r\) bounded away from zero and its two tails. The small-index contribution is bounded by \(O((\varepsilon/\sqrt r)^{1-\alpha})\); the large-index contribution decays exponentially by (3); after rescaling by \(r^{(1-\alpha)/2}\), let \(\varepsilon\downarrow0\). A Riemann sum gives
\[
M(r)\sim c r^{(\alpha-1)/2}\int_0^\infty x^{-\alpha}\operatorname{sech}^2x\,dx.
\]
For \(\alpha=1\), the terms with \(n\ll r^{-1/2}\) give the harmonic divergence \(c\log(r^{-1/2})\). The difference from the truncated harmonic sum is bounded on the scale of this logarithm using (5) at small indices and exponential decay at large ones. Hence \(M(r)\sim(c/2)\log(1/r)\).

For \(1<\alpha<3\), the second sum in (6), the bound \(1-\delta_n(r)\le\min(1,rn^2)\), and rescaled Riemann sums give
\[
\mu-M(r)\sim c r^{(\alpha-1)/2}
\int_0^\infty x^{-\alpha}\tanh^2x\,dx.
\]
Here the integral is finite at zero because \(\alpha<3\) and at infinity because \(\alpha>1\). At the borderline \(\alpha=3\), the index range \(1\ll n\ll r^{-1/2}\) instead contributes
\[
c r\sum_{n\ll r^{-1/2}}\frac1n
\sim\frac c2 r\log(1/r).
\]
The remaining indices are smaller order after a two-cutoff argument using (5), (3) and the local expansion of \(\cosh\) for \(n\theta\) small. Finally, when \(\alpha>3\), \(\sum_{n\ge1}n^2s_n<\infty\); (5) and dominated convergence yield
\[
\lim_{r\downarrow0}\frac{\mu-M(r)}r=\sum_{n\ge1}n^2s_n
=\frac16\mathbb E[L(L+1)(2L+1)].
\]
These estimates establish all five occupation laws without exchanging a divergent moment expansion with an infinite disorder average.

**5. Drift laws and sharpness.** Substitute the occupation asymptotics into \(v(r)=(p-q)/(1+aM(r))\). If \(\alpha\le1\), the denominator diverges and the first two displayed drift equivalents follow. If \(\alpha>1\), \(M(r)\to\mu\) and
\[
v(r)-v_0=\frac{(p-q)a(\mu-M(r))}{(1+aM(r))(1+a\mu)}\sim K(\mu-M(r)).
\]
This proves the three remaining equivalents, including the factor \(1/2\) at \(\alpha=3\). Since \(\mathbb E\min(T_L,E_r)\) decreases strictly with \(r\) for every finite positive \(L\), \(v(r)\) increases strictly. All stated constants are positive, so the derivative classification and both threshold endpoints follow exactly.

## Verification

The standalone standard-library script `check_comb_tail.py` solves separate finite-tooth Poisson systems using exact rational arithmetic and compares them with the closed expression (1), including the adjacent-length increments (3) and the first weak-return Taylor coefficient. It also independently assembles and solves full finite-ring stationary generators and verifies (2) exactly on heterogeneous rings. Running `python3 check_comb_tail.py` produced `PASS 90 exact recurrence / incremental / finite-ring checks`. Additional direct weighted-tail numerical evaluations for survival laws \(s_n=n^{-\alpha}\), at exponents \(0.6,1,1.5,2.5,3,3.5\), were compared to the six appropriate displayed asymptotics and were consistent with convergence of the normalized ratios as \(r\downarrow0\). Such finite computations do not prove the thermodynamic, Riemann-sum or borderline logarithmic limits; those are proved above.

## Relationship to prior work

Sarkar and Gupta, arXiv:2205.15232 (first publicly posted 2022-05-30), derive an exact stationary current for an arbitrary realization of tooth lengths and local Poisson returns in a comb with **the same nonzero bias on the backbone and the teeth**. They analyze geometric tooth lengths, power-law trapping in their outward-biased-tooth model, and a weak-reset Taylor expression under finite required expectations. Their finite-volume stationary-current method is acknowledged; it does not state the separate symmetric-tooth/heavy-tail five-regime asymptotics or the finite-susceptibility threshold at tail index three. In the current model the tooth drift is exactly zero while the backbone drift is positive, so their strict coupled-bias assumptions are not met by substitution at positive backbone bias. The relevant new ingredient is the singular rescaling of the reflected-tooth resolvent and the precise tail-response classification, not a claim to invent local resetting or general current normalization.

Elliott and Wheater, arXiv:0704.0188 (first posted 2007-04-02), treat biased walks on power-law random combs, including distinct spine and tooth biases, but with **no Poisson return mechanism**. Kotak and Barma, arXiv:2204.05357 (first posted 2022-04-11), study trapping and first-passage fluctuations in biased random combs **without local resetting**. Masó-Puigdellosas, Sandev and Méndez, *Entropy* 25 (2023) 1529, examine Markovian and non-Markovian resetting in continuum/CTRW comb-like models, focusing on mean-square displacements rather than quenched finite-tooth stationary drift and weak-rate susceptibility. Related published geometric-tail results instead have a log-periodically modulated fractional onset from outward tooth bias; they do not imply the present symmetric-tooth power-law classification by a matching parameter limit.

## Limitations

The theorem concerns a noninteracting continuous-time Markov walker, a stationary finite-ring limit taken before thermodynamic and zero-return limits, independent iid lengths with a *pure* regularly varying tail with asymptotic constant, symmetric vertical unit jump rates, independent backbone rates, and instantaneous local returns. It does not cover simultaneous size/return-rate scaling, logarithmically modulated tails, outward-biased teeth, interactions or first-passage optimization. The finite-size current formula is in the tradition of known stationary comb calculations; originality is asserted for the explicit sharp weak-return heavy-tail classification in the stated independently biased model, not for generic renewal or Tauberian principles. A general result elsewhere might imply the asymptotics without stating them; this is a publication-priority risk to be checked independently.

## References

1. J. D. Kotak and M. Barma, “Bias induced drift and trapping on random combs and the Bethe lattice: Fluctuation regime and first order phase transitions,” arXiv:2204.05357, first posted 2022-04-11, https://arxiv.org/abs/2204.05357.
2. M. Sarkar and S. Gupta, “Biased random walk on random networks in presence of stochastic resetting: Exact results,” arXiv:2205.15232, first posted 2022-05-30, https://arxiv.org/abs/2205.15232.
3. T. M. Elliott and J. F. Wheater, “Biased random walks on random combs,” arXiv:0704.0188, first posted 2007-04-02, https://arxiv.org/abs/0704.0188.
4. A. Masó-Puigdellosas, T. Sandev and V. Méndez, “Random Walks on Comb-like Structures under Stochastic Resetting,” *Entropy* 25 (2023), article 1529, https://doi.org/10.3390/e25111529.
5. Standard strong law of large numbers and dominated convergence theorem (used in the mathematical proof).
