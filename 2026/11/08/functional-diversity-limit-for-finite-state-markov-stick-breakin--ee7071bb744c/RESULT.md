# Functional diversity limit for finite-state Markov stick breaking

## Finding

Consider a stationary, irreducible, aperiodic Markov chain \((Z_j)_{j\geq1}\) on a finite state space \(E\), with transition matrix \(P\), invariant law \(\pi\), and break function \(v:E\to(0,1)\). Put \(V_j=v(Z_j)\) and
\[
 w_j=V_j\prod_{i<j}(1-V_i),\qquad j\geq1.
\]
Independently, sample \(X_1,X_2,\ldots\) conditionally iid with \(\Pr(X_i=j\mid(Z_k))=w_j\). Let \(K_m=|\{X_1,\ldots,X_m\}|\) count distinct sampled labels. Define
\[
 Y_j=-\log(1-V_j),\quad \mu=\mathbb E_\pi Y_1>0,\quad
 s^2=\operatorname{Var}_\pi(Y_1)+2\sum_{h\geq1}\operatorname{Cov}_\pi(Y_1,Y_{h+1}).
\]
The sum converges absolutely. As \(n\to\infty\), in the Skorokhod space \(D[0,1]\),
\[
 \boxed{\left(\frac{K_{\lceil n^t\rceil}-t(\log n)/\mu}{\sqrt{\log n}}\right)_{0\leq t\leq1}
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
Thus, at fixed break values and fixed stationary proportions, Markov persistence changes the Gaussian fluctuation magnitude while leaving the almost-sure diversity growth coefficient fixed. For symmetric proportions \(\pi_0=\pi_1=1/2\), choosing \(p=q=(1-\lambda)/2\) permits any \(-1<\lambda<1\): the fluctuation coefficient ranges strictly from zero toward infinity as \(\lambda\) varies, with neither endpoint attained by an aperiodic two-state chain.

For the concrete choice \(u=1-e^{-1}\), \(v=1-e^{-2}\), \(p=1/4\), \(q=1/3\), the deterministic constants are \(\mu=10/7\) and \(s^2/\mu^3=51/250\).

## Assumptions and scope

All asymptotics are as \(n\to\infty\) through positive integers. The chain is **stationary** from the first break onward, finite-state, irreducible and aperiodic; the function \(v\) takes values strictly between zero and one. These conditions imply deterministic \(\delta>0\) such that \(\delta\leq V_j\leq1-\delta\) for every state and time. The base atom locations, if the weights define a random discrete measure, are independently drawn from a diffuse law, so distinct occupied labels equal distinct observed species. No independence between consecutive break lengths is imposed. The choice \(\lceil n^t\rceil\) ensures a nonzero sample at \(t=0\). For general finite-state chains \(s^2\) may vanish and no nondegenerate Gaussian claim is made in that case.

## Proof

**1. Properness and a renewal coordinate.** Set \(S_0=0\) and \(S_j=Y_1+\cdots+Y_j\). Let \(d=\min_{z\in E}[-\log(1-v(z))]>0\). Since \(S_j\geq jd\), the residual mass after the first \(j\) sticks is \(e^{-S_j}\to0\). Thus \(\sum_jw_j=1\). Each weight satisfies \(\delta e^{-S_{j-1}}\leq w_j\leq e^{-S_{j-1}}\). Define the renewal-like counting function
\[
 M(x)=\#\{j\geq1:S_{j-1}\leq x\}\quad(x\geq0),\qquad M(x)=0\quad(x<0).
\]
Any interval of length \(r\geq0\) contains at most \(1+r/d\) of the points \(S_{j-1}\), up to an irrelevant extra boundary point.

**2. A uniform high-probability coupling.** Let \(L=\log n\), \(h=4\log(L+2)\), and \(N_n(t)=\lceil e^{Lt}\rceil\). For every \(j\) with \(S_{j-1}\leq L\), the probability (conditional on the environment) that label \(j\) is not among the first \(\lceil e^{S_{j-1}+h+1}\rceil\) observations is at most \(\exp(-\delta e^{h+1})\). There are at most \(1+L/d\) such labels. Therefore, except with probability \(O(L)e^{-\delta e^{h+1}}\), simultaneously for every \(t\in[0,1]\), all labels counted by \(M(Lt-h-1)\) have appeared by observation \(N_n(t)\).

For the opposite bound, take integer grid values \(i=0,1,\ldots,\lceil L\rceil\). After the first \(M(i+h+1)\) boxes, the remaining total weight is \(e^{-S_{M(i+h+1)}}\leq e^{-(i+h+1)}\) (the strict overshoot follows from the definition of \(M\)). At most \(\lceil e^{i+1}\rceil\leq 2e^{i+1}\) samples are observed at any \(t\) with \(i\leq Lt<i+1\). A union bound shows the probability that any of those samples falls beyond box \(M(i+h+1)\) is at most \(2e^{-h}\). Summing over the grid gives probability \(O(L)e^{-h}=O(L^{-3})\) that the upper bound fails at any time. Hence, with probability tending to one,
\[
 M(Lt-h-1)\leq K_{N_n(t)}\leq M(Lt+h+1)\quad\text{for all }0\leq t\leq1.
\]
Because \(Y_j\geq d\), the two bounds differ by at most \(2+(2h+2)/d\), deterministically. Consequently
\[
 \sup_{0\leq t\leq1}|K_{\lceil n^t\rceil}-M(Lt)|=O_{\mathbb P}(\log(L+2))=o_{\mathbb P}(\sqrt L).
\]
The explicit error-probability estimates above are summable when \(n=\lceil e^k\rceil\), \(k\in\mathbb N\). Along this subsequence the sandwich holds eventually almost surely. The ergodic theorem gives \(M(k)/k\to1/\mu\) almost surely; monotonicity in sample size fills the gaps between \(\lceil e^k\rceil\) and \(\lceil e^{k+1}\rceil\), proving the asserted strong law for all integer \(n\).

**3. Finite-state Markov functional CLT.** For \(f(z)=-\log(1-v(z))-\mu\), solve the finite-state Poisson equation \((I-P)g=f\) with \(\pi g=0\). The identity
\[
 \sum_{j=1}^{m}f(Z_j)=\sum_{j=1}^{m}\bigl(g(Z_{j+1})-(Pg)(Z_j)\bigr)+g(Z_1)-g(Z_{m+1})
\]
expresses centered partial sums as a martingale with bounded differences plus a uniformly bounded remainder. Stationarity, the finite-state ergodic theorem for the conditional quadratic variation and the bounded-increment martingale functional central limit theorem give
\[
 \left(\frac{S_{\lfloor Lt\rfloor}-\mu Lt}{\sqrt L}\right)_{t\in[0,T]}
 \Longrightarrow (sB(t))_{t\in[0,T]}
\]
for each fixed \(T>0\); the martingale variance equals the absolutely summable Green--Kubo covariance expression for \(s^2\). The monotone-inverse map at the strictly increasing deterministic curve \(\mu t\) then gives
\[
 \left(\frac{M(Lt)-Lt/\mu}{\sqrt L}\right)_{0\leq t\leq1}
 \Longrightarrow\left(-\frac{s}{\mu^{3/2}}B(t)\right)_{0\leq t\leq1}.
\]
The inverse-Brownian sign does not affect the law. Step 2 and Slutsky's theorem in \(D[0,1]\) finish the functional claim.

**4. Two-state exact variance.** For the centered state observable \(Y_j-\mu\), the two-state transition matrix has nonconstant eigenvalue \(\lambda=1-p-q\). Thus, for every \(h\geq0\),
\[
 \operatorname{Cov}(Y_1,Y_{1+h})=\pi_0\pi_1(b-a)^2\lambda^h.
\]
Since \(|\lambda|<1\), the Green--Kubo sum is \(\pi_0\pi_1(b-a)^2(1+\lambda)/(1-\lambda)\). The symmetric stationary case permits \(p=q\in(0,1)\), proving the claimed tunability. In the numerical-symbolic example, \(\pi=(4/7,3/7)\), \(\lambda=5/12\), \(\mu=10/7\), \(s^2=204/343\), and \(s^2/\mu^3=51/250\).

## Verification

The accompanying `verify.py` uses exact rational arithmetic to test the stationary weights, two-state eigenvalue and explicit asymptotic variance, checks covariance sums against finite-state transition calculations across multiple lags, and independently enumerates finite Markov trajectories to verify partial-sum variance identities. Its finite checks are diagnostics, not a proof of the infinite functional limit. The analytical coupling and the martingale/inversion argument above are the decisive evidence. Execute `python3 verify.py` using the standard library.

## Relationship to prior work

Gil-Leyva, Lijoi, Mena and Prünster (arXiv:2601.16561, first posted January 23, 2026) introduced general Markov-dependent stick-breaking lengths and developed properness, size-biased ordering and posterior constructions. Their section on the number of clusters develops finite-sample and computational comparisons; no functional logarithmic cluster-count limit or explicit two-state correlation adjustment was found in the inspected main text and appendix. The present theorem concerns a finite-state stationary subclass, not all their kernels.

Gnedin, Iksanov and Marynych (arXiv:1001.4920, section 1 and theorem 1.1) proved broad occupied-box limit laws for the Bernoulli sieve with **iid** residual factors. Those results include the iid central-limit normalization but do not directly cover stationary Markov factors: their paper explicitly assumes independent copies for the residual allocation variables and for the associated renewal increments. The comparison is at the assumption and implication level; taking a Markov chain with independent rows recovers the classical case, which is not claimed as new. The new part is the Markov-environment extension with a process-level limit and a Green--Kubo covariance correction.

Alsmeyer, Iksanov and Marynych (arXiv:1601.04274v1, introduction, theorem 2.2 and section 4) prove a functional limit for the number of boxes **with between one and \(n^t\) occupants after \(n\) draws**, in the iid-factor Bernoulli sieve, and give a universal deterministic-frequency approximation for that *box-size threshold* process. This process differs from the nested-sample-size process \(K_{\lceil n^t\rceil}\) here. Their occupancy-approximation insight and iid results are acknowledged as prior work; the present statement still requires dependent Markov renewal fluctuations and a simultaneous coupling for nested sample sizes. The 2016 theory establishes substantial related structure, so the novel contribution is limited to this Markov-environment process-level statement and explicit correlation dependence.

De Blasi, Mena and Prünster (2022) investigate distinct-value growth for geometric stick-breaking with a single random success probability, a fully dependent environment. This is not an ergodic finite-state Markov sequence of nonidentical breaks; its existing one-dimensional geometric results are not claimed here. General finite-state Markov additive-process FCLTs are classical, and this proof uses them as a tool rather than claiming them as new.

## Limitations

The finite-state assumption bounds all breaks away from zero and one and is essential to the simple uniform logarithmic coupling. The result does not treat Markov breaks approaching the endpoints, null-recurrent modulating chains, nonstationary environments with changing parameters, or posterior distributions. It asserts a functional weak limit and a strong-law coefficient, not convergence of the finite-sample variance divided by \(\log n\), a Berry--Esseen rate, or a local limit theorem. Historic priority is provisional: a general preexisting Markov-modulated occupancy theorem, if located and shown to imply this statement, could subsume the contribution.

## References

1. M. F. Gil-Leyva, A. Lijoi, R. H. Mena and I. Prünster, *Markov stick-breaking processes*, arXiv:2601.16561v1 (January 23, 2026), https://arxiv.org/html/2601.16561v1.
2. A. Gnedin, A. Iksanov and A. Marynych, *Limit theorems for the number of occupied boxes in the Bernoulli sieve*, arXiv:1001.4920v1 (January 27, 2010), https://arxiv.org/html/1001.4920v1.
3. G. Alsmeyer, A. Iksanov and A. Marynych, *Functional limit theorems for the number of occupied boxes in the Bernoulli sieve*, arXiv:1601.04274v1 (2016), https://arxiv.org/html/1601.04274v1.
4. P. De Blasi, R. H. Mena and I. Prünster, *Asymptotic behavior of the number of distinct values in a sample from the geometric stick-breaking process*, Ann. Inst. Stat. Math. 74 (2022), 143--165, https://doi.org/10.1007/s10463-021-00791-6.
