# Exponential spell lengths in the subcritical expiring coupon collector

## Finding

Fix any \(\alpha\in(0,1)\). In the uniform \(n\)-coupon model with expiration after \(M_n=\lfloor\alpha n\log n\rfloor\) draws, condition on a **new entrance** into complete coverage in the stationary two-sided stream. If \(L_n\) is the number of consecutive complete sliding windows beginning at that entrance, then, for every \(t\ge0\),

\[
\lim_{n\to\infty}\Pr\!\left(L_n>\lfloor t n^\alpha\rfloor\mid E_0\right)=e^{-t}.
\]

Thus \(L_n/n^\alpha\) converges in law to a mean-one exponential random variable. Moreover, with \(S(j,k)\) denoting a Stirling number of the second kind, for every \(n\ge2\) and \(M\ge n\),

\[
\mathbb E[L\mid E_0]=\frac{n\,S(M,n)}{(n-1)S(M-1,n-1)},
\]

and under the stated subcritical scaling this exact mean is asymptotic to \(n^\alpha\). The distributional statement concerns the duration of one successful *spell*, not the much longer time between rare entrances.

## Assumptions and scope

Let \((X_i)_{i\in\mathbb Z}\) be independent, uniformly distributed on \(\{1,\ldots,n\}\), and put \(W_j=(X_{j-M+1},\ldots,X_j)\). A window is *complete* (or *onto*) if it contains every coupon type. Define the entry event

\[
E_0=\{W_{-1}\text{ is not onto},\;W_0\text{ is onto}\},
\]

and, conditional on this positive-probability event, define the positive-integer spell length

\[
L=\min\{j\ge1:W_j\text{ is not onto}\}.
\]

Throughout the limit theorem \(n\to\infty\), \(\alpha\in(0,1)\) is fixed, \(M=M_n\), and \(L_n=L\). For sufficiently large \(n\), \(M_n\ge n\). The normalization applies to *entry-conditioned* spells; it is not asserted for a randomly sampled complete window, which has a size-biased spell law.

## Proof

**1. Entrance-conditioned word.** Write \(a=X_0\), and let \(U=(X_{-M+1},\ldots,X_{-1})\), of length \(m=M-1\). On \(E_0\), the color \(a\) is absent from \(U\), while all \(N=n-1\) other colors occur. Conversely these two properties imply \(E_0\), independently of \(X_{-M}\): that departing symbol cannot supply the missing \(a\) except with a separate probability, which would make \(W_{-1}\) onto and suppress an entrance. More precisely, conditional on the two properties, \(E_0\) additionally requires \(X_{-M}\ne a\); this factor \((n-1)/n\) is independent of \(U\). Consequently, given \(E_0\) and \(a\), \(U\) is uniform among onto words of length \(m\) over \(N\) colors. The subsequent symbols \(X_1,X_2,\ldots\) remain independent uniform draws. This is the entry-word characterization underlying the exact flux in [1].

**2. Initial singleton losses.** Let \(H_k\) count positions among the first \(k\) positions of \(U\) whose color appears exactly once in all of \(U\). Let \(\rho_{N,m}=S(m-1,N-1)/S(m,N)\). For each fixed integer \(r\ge1\) and \(k\le m\), selecting \(r\) ordered positions, requiring that each be an entire singleton color, and freely distributing the remaining \(N-r\) colors gives the exact factorial-moment identity

\[
\mathbb E[(H_k)_r\mid E_0]=(k)_r\frac{S(m-r,N-r)}{S(m,N)}.
\tag{1}
\]

Here \((z)_r=z(z-1)\cdots(z-r+1)\), and Stirling counts are interpreted as zero outside their standard ranges. The numerator counts onto words with those singleton positions fixed but with their distinct colors freely assigned.

**3. Uniform-on-surjections singleton asymptotics.** Let \(\lambda>0\) uniquely solve

\[
\frac{\lambda}{1-e^{-\lambda}}=\frac{m}{N}.
\]

The regime \(m/N=\alpha\log n+o(1)\) gives \(\lambda=\alpha\log n+o(1)\), hence \(e^{-\lambda}=n^{-\alpha}(1+o(1))\). Let \(Z_1,\ldots,Z_N\) be independent zero-truncated Poisson variables, each with \(\Pr(Z=j)=\lambda^j/[j!(e^\lambda-1)]\), \(j\ge1\). Their sum has mean \(m\) and variance \(N\operatorname{Var}Z\sim\alpha n\log n\). Upon conditioning on \(\sum Z_i=m\), the count vector is the occupancy vector of a uniformly sampled onto word \(U\).

For each fixed \(r\), both the central sum probability \(\Pr(\sum_{i=1}^N Z_i=m)\) and the shifted one \(\Pr(\sum_{i=1}^{N-r}Z_i=m-r)\) are asymptotic to \((2\pi N\operatorname{Var}Z)^{-1/2}\). The target of the latter is displaced from its mean by \(r(m/N-1)=O(\log n)\), negligible against \(\sqrt{n\log n}\). This triangular-array lattice local limit follows by Fourier inversion: the characteristic function is \((e^{\lambda e^{it}}-1)/(e^\lambda-1)\); near zero its centered logarithm has a uniform quadratic expansion on the \((N\operatorname{Var}Z)^{-1/2}\) scale, and off a shrinking neighborhood its \(N\)-th power is negligible. The uniform local-limit argument for these same zero-truncated Poisson rows is detailed in [1, Appendix A]; the stated \(O(\log n)\) displacement obeys its same Fourier estimates.

Using the occupancy representation and the previous ratio of lattice probabilities,

\[
\frac{S(m-r,N-r)}{S(m,N)}
=\frac{(N)_r}{(m)_r}\left(\frac{\lambda}{e^\lambda-1}\right)^r
\frac{\Pr(\sum_{i=1}^{N-r}Z_i=m-r)}{\Pr(\sum_{i=1}^{N}Z_i=m)}
\sim e^{-r\lambda}\sim n^{-\alpha r}.
\tag{2}
\]

In particular, \(\rho_{N,m}\sim n^{-\alpha}\).

**4. A Poisson first-singleton process.** Put \(k_n=\lfloor t n^\alpha\rfloor\). For fixed \(t>0\) and every fixed \(r\), (1)–(2) yield

\[
\mathbb E[(H_{k_n})_r\mid E_0]\longrightarrow t^r.
\]

By the factorial-moment method for nonnegative integer random variables, \(H_{k_n}\) converges to a Poisson variable of mean \(t\). Thus \(\Pr(H_{k_n}=0\mid E_0)\to e^{-t}\). For \(t=0\) this follows immediately from \(k_n=0\).

**5. Replacing the first singleton by the actual exit.** Let \(k<M\). If an initial singleton among the first \(k\) symbols does *not* cause a loss of complete coverage within \(k\) shifts, its coupon must be drawn again among the first \(k\) new independent symbols. A union bound conditional on \(U\) gives

\[
\Pr(L>k,\,H_k>0\mid E_0)\le\frac{k}{n}\mathbb E[H_k\mid E_0]=\frac{k^2\rho_{N,m}}{n}.
\tag{3}
\]

Conversely, if \(H_k=0\) but coverage fails by step \(k\), some initial color with at least two occurrences has *all* of them in the first \(k\) positions of \(U\). The expected number of such colors is

\[
\sum_{j=2}^{k}\binom{k}{j}\frac{S(m-j,N-1)}{S(m,N)}
\le\rho_{N,m}\sum_{j=2}^{k}\binom{k}{j}(N-1)^{1-j}
\le\frac{\rho_{N,m} k^2}{2(N-1)}e^{k/(N-1)}.
\tag{4}
\]

The first inequality follows by iterating \(S(v+1,b)\ge bS(v,b)\). Combining (3)–(4),

\[
\left|\Pr(L>k\mid E_0)-\Pr(H_k=0\mid E_0)\right|
\le\frac{\rho_{N,m}k^2}{n}
+\frac{\rho_{N,m} k^2 e^{k/(N-1)}}{2(N-1)}.
\]

At \(k=k_n\), \(k/n\to0\) and \(\rho_{N,m}\sim n^{-\alpha}\), so this bound is \(O(n^{\alpha-1})\to0\). Together with Step 4 this proves the exponential survival law and convergence in distribution.

**6. Exact mean and its normalization.** For each fixed \((n,M)\), the stationary probability of a complete window is

\[
\pi_{n,M}=\frac{n!S(M,n)}{n^M},
\]

and the entrance flux computed in [1] is

\[
\mu_{n,M}=\frac{(n-1)(n-1)!S(M-1,n-1)}{n^M}.
\]

Counting expected complete time per entrance in a finite stationary ergodic process gives \(\pi_{n,M}=\mu_{n,M}\mathbb E[L\mid E_0]\), hence the exact mean displayed above. Finally the singleton ratio \(S(M-1,n-1)/S(M,n)\sim n^{-\alpha}\) follows from Step 3 with \((m,N)=(M,n)\), so \(\pi/\mu\sim n^\alpha\), proving convergence of the explicitly computed means in this case (not merely convergence of distributions).

## Verification

The standalone Python 3 standard-library program `checker.py` enumerates conditioned onto words for small \(n\), computes singleton factorial moments using exact Stirling counts, and independently enumerates all possible future draws to test the coverage-spell probability and the rigorous finite discrepancy bound. Run `python checker.py`; its recorded output was `EXACT_CASES_PASSED 29`. These checks are finite and do not certify the infinite asymptotic theorem; that rests on Steps 1–6 and the indicated lattice local limit. The source code has no external dependencies.

## Relationship to prior work

Long [1] analyzes *waiting to enter* the set of complete sliding windows: exact stationary entrance flux, entrance-conditioned surjection, exponential rare-entry time and logarithmic estimates on waiting time. The theorem here addresses a different conditional law, namely the duration of a **contiguous spell after entry**. Its exponential normalization comes from the asymptotic placement of initially singleton coupon colors inside the entrance-conditioned word. The exact mean is a simple stationary mass-to-flux consequence of [1] and is stated as calibration rather than independent novelty. The original 2012 question [2] concerns the time to collect all types with expiration and a heuristic overall waiting scale, not this consecutive-window duration law. General hitting-time and renewal theory can motivate an exponential law but does not directly identify this specific entrance-conditioned spell normalization; see [3] as related background.

## Limitations

The theorem assumes uniform independent coupons and a fixed \(0<\alpha<1\). It does not cover the critical scale \(\alpha=1\), nonuniform coupon probabilities, the distribution from a size-biased randomly selected complete window, joint laws of successive spells, or the waiting time to first completion. The mean identity alone is already implied by the flux and stationarity in [1]; novelty is claimed only for the conditional spell-length limit and its proof. Priority beyond inspected sources and accessible search records remains subject to independent scrutiny. Numerical enumeration is not an asymptotic proof.

## References

[1] Christopher D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298v1, first posted 2026-04-29. https://arxiv.org/abs/2604.26298

[2] *Expiring coupon collector's problem*, Mathematics Stack Exchange, question and answer initiated 2012. https://math.stackexchange.com/questions/188889/expiring-coupon-collectors-problem

[3] M. Auer and R. Zweimüller, *Local limit theorems for hitting times and return times of small sets*, arXiv:2312.14581 (background on general rare-set return-time phenomena; not an asserted novelty exclusion). https://arxiv.org/abs/2312.14581
