# Functional diversity limit for finite-state Markov stick breaking

## Finding

Consider a stationary, irreducible, aperiodic Markov chain \((Z_j)_{j\geq1}\) on a finite state space \(E\), with transition matrix \(P\), invariant law \(\pi\), and break function \(v:E\to(0,1)\). Put \(V_j=v(Z_j)\) and
\[
 w_j=V_j\prod_{i<j}(1-V_i),\qquad j\geq1.
\]
Given the chain, sample \(X_1,X_2,\ldots\) conditionally iid with \(\Pr(X_i=j\mid(Z_k))=w_j\). Let \(K_m=|\{X_1,\ldots,X_m\}|\) count distinct sampled labels. Define
\[
 Y_j=-\log(1-V_j),\quad \mu=\mathbb E_\pi Y_1>0,\quad
 s^2=\operatorname{Var}_\pi(Y_1)+2\sum_{h\geq1}\operatorname{Cov}_\pi(Y_1,Y_{h+1}).
\]
The sum converges absolutely. As \(n\to\infty\), in the Skorokhod \(J_1\) topology on \(D[0,1]\),
\[
 \boxed{\left(\frac{K_{\lfloor n^t\rfloor}-t(\log n)/\mu}{\sqrt{\log n}}\right)_{0\leq t\leq1}
 \ \Longrightarrow\ \left(\frac{s}{\mu^{3/2}}B(t)\right)_{0\leq t\leq1},}
\]
where \(B\) is standard Brownian motion; the limiting process is identically zero when \(s^2=0\). Moreover \(K_n/\log n\to1/\mu\) almost surely.

For two states, suppose \(0<u<v<1\), \(v(0)=u\), \(v(1)=v\), and
\[
 P=\begin{pmatrix}1-p&p\\q&1-q\end{pmatrix},\quad 0<p,q<1.
\]
Write \(a=-\log(1-u)\), \(b=-\log(1-v)\), \(\lambda=1-p-q\). Then
\[
 \pi_0=\frac q{p+q},\quad\pi_1=\frac p{p+q},\quad
 \mu=\pi_0 a+\pi_1 b,\quad
 \boxed{s^2=\pi_0\pi_1(b-a)^2\frac{1+\lambda}{1-\lambda}.}
\]
Thus, at fixed break values and fixed stationary proportions, Markov persistence changes the Gaussian fluctuation magnitude while leaving the almost-sure diversity growth coefficient fixed. For symmetric proportions \(\pi_0=\pi_1=1/2\), choosing \(p=q=(1-\lambda)/2\) permits any \(-1<\lambda<1\): the fluctuation coefficient ranges over the positive reals, tending to zero as \(\lambda\downarrow-1\) and to infinity as \(\lambda\uparrow1\).

For the concrete choice \(u=1-e^{-1}\), \(v=1-e^{-2}\), \(p=1/4\), \(q=1/3\), the deterministic constants are \(\mu=10/7\) and \(s^2/\mu^3=51/250\).

## Assumptions and scope

All asymptotics are as \(n\to\infty\) through positive integers. The chain is **stationary** from the first break onward, finite-state, irreducible and aperiodic; the function \(v\) takes values strictly between zero and one. These conditions imply deterministic \(\delta>0\) such that \(\delta\leq V_j\leq1-\delta\) for every state and time. The base atom locations, if the weights define a random discrete measure, are independently drawn from a diffuse law, so distinct occupied labels equal distinct observed species. No independence between consecutive break lengths is imposed. The index \(\lfloor n^t\rfloor\) makes the process right-continuous with left limits and equals one at \(t=0\). Using \(\lceil n^t\rceil\) changes every path by at most one before normalization, but those paths need not be right-continuous. For general finite-state chains \(s^2\) may vanish and no nondegenerate Gaussian claim is made in that case.

## Proof

**1. Properness and a renewal coordinate.** Set \(S_0=0\) and \(S_j=Y_1+\cdots+Y_j\). Let \(d=\min_{z\in E}[-\log(1-v(z))]>0\) and \(D=\max_{z\in E}[-\log(1-v(z))]<\infty\). Since \(S_j\geq jd\), the residual mass after the first \(j\) sticks is \(e^{-S_j}\to0\). Thus \(\sum_jw_j=1\). Each weight satisfies \(\delta e^{-S_{j-1}}\leq w_j\leq e^{-S_{j-1}}\). Define the right-continuous counting function
\[
 M(x)=\#\{j\geq1:S_{j-1}\leq x\}\quad(x\geq0),\qquad M(x)=0\quad(x<0).
\]
Any interval of length \(r\geq0\) contains at most \(1+r/d\) of the points \(S_{j-1}\).

**2. A uniform high-probability coupling.** Let \(L=\log n\), \(h=4\log(L+2)\), and \(N_n(t)=\lfloor e^{Lt}\rfloor\). For every \(j\) with \(S_{j-1}\leq L\), put \(m_j=\lfloor e^{S_{j-1}+h+1}\rfloor\). Conditionally on the environment, the probability that label \(j\) is not among the first \(m_j\) observations is at most \(\exp(-\delta e^{h+1}/2)\), since \(m_j\geq e^{S_{j-1}+h+1}/2\). There are at most \(1+L/d\) such labels. For any \(t\) with \(S_{j-1}\leq Lt-h-1\), one has \(m_j\leq N_n(t)\). A union bound therefore guarantees that all labels counted by \(M(Lt-h-1)\) have appeared by observation \(N_n(t)\), simultaneously for all \(t\), except with probability \(O(L+1)\exp(-\delta e^{h+1}/2)\).

For the upper bound, take integers \(i=0,1,\ldots,\lceil L\rceil\). After the first \(M(i+h+1)\) boxes, the remaining total weight is \(e^{-S_{M(i+h+1)}}\leq e^{-(i+h+1)}\). At most \(\lfloor e^{i+1}\rfloor\) samples are observed at any \(t\) with \(i\leq Lt<i+1\). The probability that any of those samples falls beyond box \(M(i+h+1)\) is at most \(e^{-h}\). Summing over \(i\) shows that the upper bound fails with probability at most \(O(L+1)e^{-h}=O((L+2)^{-3})\). Hence, with probability tending to one,
\[
 M(Lt-h-1)\leq K_{N_n(t)}\leq M(Lt+h+1)\quad\text{for all }0\leq t\leq1.
\]
Because \(Y_j\geq d\), the two bounds differ by at most \(2+(2h+2)/d\), deterministically. Consequently
\[
 \sup_{0\leq t\leq1}|K_{\lfloor n^t\rfloor}-M(Lt)|=O_{\mathbb P}(\log(L+2))=o_{\mathbb P}(\sqrt L).
\]
The error-probability bounds are summable when \(n=\lceil e^k\rceil\), \(k\in\mathbb N\). Along this subsequence the sandwich holds eventually almost surely. The ergodic theorem gives \(M(x)/x\to1/\mu\) almost surely as \(x\to\infty\); monotonicity in sample size and the ratio of consecutive logarithmic sample sizes tending to one fill the gaps, proving the asserted strong law.

**3. Finite-state Markov functional CLT.** For \(f(z)=-\log(1-v(z))-\mu\), solve the finite-state Poisson equation \((I-P)g=f\) with \(\pi g=0\). The identity
\[
 \sum_{j=1}^{m}f(Z_j)=\sum_{j=1}^{m}\bigl(g(Z_{j+1})-(Pg)(Z_j)\bigr)+g(Z_1)-g(Z_{m+1})
\]
expresses centered partial sums as a martingale with bounded differences plus a uniformly bounded remainder. Stationarity and the ergodic theorem identify its limiting conditional quadratic variation per step. This variance equals the Green–Kubo expression for \(s^2\): the bounded remainder does not change the asymptotic variance per step, and covariance decay is geometric because the chain is finite, irreducible and aperiodic. The bounded-increment martingale functional central limit theorem gives
\[
 W_L(u):=\frac{S_{\lfloor Lu\rfloor}-\mu Lu}{\sqrt L}\ \Longrightarrow\ sB(u)
\]
on any fixed compact time interval. If the variance is zero this gives the zero process.

For \(t\in[0,1]\), \(S_{M(Lt)-1}\leq Lt<S_{M(Lt)}\leq Lt+D\). The ergodic law for \(S_m\) implies \(M(Lt)/L\to t/\mu\) uniformly almost surely: use the inverse bounds \((\mu-\epsilon)m\leq S_m\leq(\mu+\epsilon)m\) for sufficiently large \(m\) and the bounded indices below that cutoff. The index \(M(Lt)/L\) stays on a fixed compact interval by \(M(Lt)\leq1+L/d\). The overshoot bound gives, uniformly in \(t\),
\[
 \frac{M(Lt)-Lt/\mu}{\sqrt L}
 =-\frac{1}{\mu}W_L(M(Lt)/L)+O(L^{-1/2}).
\]
Since the limiting process is continuous, this random-time evaluation converges to \(-sB(t/\mu)/\mu\), which has the law of \(sB(t)/\mu^{3/2}\). Step 2 and Slutsky's theorem on \(D[0,1]\) give the asserted limit.

**4. Two-state exact variance.** For the centered state observable \(Y_j-\mu\), the two-state transition matrix has nonconstant eigenvalue \(\lambda=1-p-q\). Thus, for every \(h\geq0\),
\[
 \operatorname{Cov}(Y_1,Y_{1+h})=\pi_0\pi_1(b-a)^2\lambda^h.
\]
Since \(|\lambda|<1\), the Green–Kubo sum is \(\pi_0\pi_1(b-a)^2(1+\lambda)/(1-\lambda)\). The symmetric stationary case permits \(p=q\in(0,1)\), proving the claimed tunability. In the numerical-symbolic example, \(\pi=(4/7,3/7)\), \(\lambda=5/12\), \(\mu=10/7\), \(s^2=204/343\), and \(s^2/\mu^3=51/250\).

## Verification

The accompanying `verify.py` uses exact rational arithmetic to test the stationary weights, two-state eigenvalue and explicit asymptotic variance, checks covariance sums against finite-state transition calculations across multiple lags, and enumerates finite Markov trajectories to verify partial-sum variance identities. Its finite checks are diagnostics, not a proof of the infinite functional limit. The analytical coupling and the martingale/inversion argument above are the decisive evidence. Execute `python3 verify.py` using the standard library.

## Relationship to prior work

Gil-Leyva, Lijoi, Mena and Prünster [1] introduced general Markov-dependent stick-breaking lengths and developed properness, size-biased ordering and posterior constructions. Their section on the number of clusters develops finite-sample and computational comparisons. The present theorem concerns a finite-state stationary subclass and addresses its logarithmic nested-sample fluctuation process.

Gnedin, Iksanov and Marynych [2] proved occupied-box limit laws for the Bernoulli sieve with **iid** residual factors. Those results include the one-dimensional iid central-limit normalization but do not directly cover dependent stationary Markov factors. Taking a Markov chain with independent rows recovers the classical one-time case, which is not claimed as new.

Alsmeyer, Iksanov and Marynych [3], and the more general random-environment transfer results of Gnedin and Iksanov [5], concern processes that vary an occupancy threshold across boxes while holding the number of draws fixed. Their deterministic-frequency approximation techniques are closely related. The process here instead counts all occupied boxes while varying the size of a nested sample, and its proof uses a simultaneous sample-size coupling and Markov additive-process fluctuations.

De Blasi, Mena and Prünster [4] study distinct-value growth for geometric stick breaking with one random success probability shared by all breaks, not the stationary irreducible finite-state sequence with nonidentical breaks considered here. General finite-state Markov additive-process FCLTs are classical and are used as a tool rather than claimed as new.

## Limitations

The finite-state interior break hypothesis keeps breaks away from zero and one, as used in the uniform logarithmic coupling. The result does not treat Markov breaks approaching the endpoints, null-recurrent modulating chains, nonstationary environments with changing parameters, or posterior distributions. It asserts a functional weak limit and a strong-law coefficient, not convergence of the finite-sample variance divided by \(\log n\), a Berry–Esseen rate, or a local limit theorem. Historical priority is provisional; a broader Markov-modulated or nested-sampling theorem could subsume the result.

## References

1. M. F. Gil-Leyva, A. Lijoi, R. H. Mena and I. Prünster, *Markov stick-breaking processes*, arXiv:2601.16561v1 (January 23, 2026), https://arxiv.org/html/2601.16561v1.
2. A. Gnedin, A. Iksanov and A. Marynych, *Limit theorems for the number of occupied boxes in the Bernoulli sieve*, arXiv:1001.4920v1 (January 27, 2010), https://arxiv.org/html/1001.4920v1.
3. G. Alsmeyer, A. Iksanov and A. Marynych, *Functional limit theorems for the number of occupied boxes in the Bernoulli sieve*, arXiv:1601.04274v1 (2016), https://arxiv.org/pdf/1601.04274v1.
4. P. De Blasi, R. H. Mena and I. Prünster, *Asymptotic behavior of the number of distinct values in a sample from the geometric stick-breaking process*, Ann. Inst. Stat. Math. 74 (2022), 143–165, https://doi.org/10.1007/s10463-021-00791-6.
5. A. Gnedin and A. Iksanov, *On nested infinite occupancy scheme in random environment*, arXiv:1808.00538v1 (2018), https://arxiv.org/pdf/1808.00538v1.
