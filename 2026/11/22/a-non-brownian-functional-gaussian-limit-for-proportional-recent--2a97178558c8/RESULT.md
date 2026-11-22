# A non-Brownian functional Gaussian limit for proportional recent-memory elephant walks

## Finding

Fix a memory fraction \(c\in(0,1)\) and a repetition probability \(p\) satisfying \(0<p<p_c=(3+\sqrt{1-c})/4\). For the symmetric-start elephant walk that samples uniformly from its last \(m_n=\max\{\lfloor cn\rfloor,1\}\) increments and repeats the sampled increment with probability \(p\), define \(S_0=0\) and \(S_n=\sum_{j=1}^n X_j\). Let \(Z_N\) be the piecewise-linear interpolation of \(N^{-1/2}S_{\lfloor Nt\rfloor}\).

Write \(a=2p-1\), \(L=-\log(1-c)\), and let the continuous fundamental solution \(w:[0,\infty)\to\mathbb R\) satisfy
\[
w(0)=1,\quad w(v)=0\ (v<0),\qquad
w'(v)=\frac ac\bigl(w(v)-w(v-L)\bigr)\quad(v>0).
\]
For every finite \(T>0\), **the path-level limit** is
\[
Z_N\ \Longrightarrow\ Z\quad\text{in }C([0,T]),\qquad
Z(t)=\int_0^t w\!\left(\log\frac tu\right)\,dB(u),\quad Z(0)=0,
\]
where \(B\) is standard Brownian motion and the stochastic integral is the deterministic Itô integral. The centered continuous Gaussian limit has covariance
\[
K(s,t)=\int_0^{\min(s,t)}
w\!\left(\log\frac su\right)w\!\left(\log\frac tu\right)\,du,
\]
variance \(K(t,t)=t\sigma^2\), with \(\sigma^2=\int_0^\infty e^{-v}w(v)^2\,dv\), and is self-similar of order \(1/2\).

For every \(s>0\), the one-sided derivative of the off-diagonal covariance obeys the **memory signature**
\[
\left.\frac{\partial}{\partial t}K(s,t)\right|_{t=s+}
=\frac{\sigma^2-1}{2}.
\]
This quantity is strictly positive for \(p>1/2\), strictly negative for \(p<1/2\), and zero for \(p=1/2\). Consequently, \(Z\) is Brownian motion precisely when \(p=1/2\); otherwise its increments are not stationary, notwithstanding its Brownian scaling exponent.

## Assumptions and scope

The first increment \(X_1\) is uniform on \(\{-1,1\}\). For each integer \(n\ge2\), conditionally on past increments, a uniformly selected index in \(\{n-m_n,\ldots,n-1\}\) is repeated or reversed with probabilities \(p\) and \(1-p\). All selections and repetition decisions are independently generated conditionally on the past. The strict range \(0<p<p_c\) is essential to this proof; neither the critical normalization nor the superdiffusive regime is addressed. The result is for each fixed \(c,p,T\), not for parameters varying with \(N\).

## Proof

**1. Innovation expansion.** Define \(\mathcal F_j=\sigma(X_1,\ldots,X_j)\), \(\varepsilon_1=X_1\), and, for \(j\ge2\),
\[
\varepsilon_j=X_j-\frac{a}{m_j}\sum_{r=j-m_j}^{j-1}X_r.
\]
Then \(\varepsilon_j\) are martingale differences, \(|\varepsilon_j|\le2\), and \(\mathbb E(\varepsilon_j^2\mid\mathcal F_{j-1})=1-a^2(m_j^{-1}\sum_{r=j-m_j}^{j-1}X_r)^2\). Deterministic coefficients \(q_{j,k}\), defined by \(q_{j,k}=0\) when \(k>j\), \(q_{k,k}=1\), and
\[
q_{j,k}=q_{j-1,k}+\frac a{m_j}(q_{j-1,k}-q_{j-m_j-1,k}),\quad j>k,
\]
satisfy the **exact** identity \(S_j=\sum_{k=1}^j q_{j,k}\varepsilon_k\), by induction. This expansion and the compact-log-time coefficient limit are from Hu--Xue [1, Lemmas 2.1, 3.6]; the recurrence above also verifies the expansion directly.

**2. Square-summable coefficient envelope.** We record an elementary bound sufficient for the new functional argument. There exist \(C<\infty\) and \(\gamma\in[0,1/2)\) such that for all \(j\ge k\ge1\),
\[
0\le q_{j,k}\le C(j/k)^\gamma.
\]
For \(a\le0\), the recursion is a convex combination of \(q_{j-1,k}\) and \(q_{j-m_j-1,k}\), hence \(0<q_{j,k}\le1\) and \(\gamma=0\) works. For \(a>0\), the discrete differences \(d_{j,k}=q_{j,k}-q_{j-1,k}\) are nonnegative, with \(d_{k,k}=1\) and \(d_{j,k}=a m_j^{-1}\sum_{r=j-m_j}^{j-1}d_{r,k}\) for \(j>k\). Choose \(0<\gamma<1/2\) with
\[
\frac{a}{c\gamma}\bigl(1-(1-c)^\gamma\bigr)<1.
\]
Such a choice exists exactly in the stated diffusive range: if \(a(-\log(1-c))/c\le1\), every sufficiently small positive \(\gamma\) works; otherwise take \(\gamma\) between the positive characteristic root and \(1/2\), using the root comparison in [1, Lemma 3.8]. For any fixed \(b>1/(1-c)\), the crude bound \(q_{j,k}\le\prod_{r=k+1}^j(1+a/m_r)\le C_b\) when \(j\le bk\) implies \(d_{j,k}\le C_b/k\) for \(k<j\le bk\). For \(j>bk\), the exceptional mass \(d_{k,k}\) is outside the lag interval. Compare the positive renewal recursion inductively with \(Ck^{-\gamma}j^{\gamma-1}\): uniformly as \(j\to\infty\),
\[
\frac{a}{m_j}\sum_{r=j-m_j}^{j-1}(r/j)^{\gamma-1}
\longrightarrow\frac{a}{c\gamma}\bigl(1-(1-c)^\gamma\bigr)<1.
\]
A sufficiently large comparison constant handles \(k<j\le bk\); the strict inequality propagates the envelope for \(j>bk\). Finitely many small \(k\) are absorbed by enlarging the constant. Summing \(d_{r,k}\) proves the claimed bound for \(q_{j,k}\). Thus
\[
\sum_{k=1}^j q_{j,k}^2\le C j,\qquad
\max_{1\le k\le j}q_{j,k}=O(j^\gamma)=o(\sqrt j).
\]
The coefficient limit in [1, Lemma 3.6] states \(q_{\lfloor ke^v\rfloor,k}\to w(v)\) uniformly on compact \(v\)-intervals as \(k\to\infty\). It follows also by writing the recursion on logarithmic time \(v=\log(j/k)\) and applying consistent Euler-delay approximation, since \(m_j/j\to c\).

**3. Joint finite-dimensional convergence.** For fixed \(t_1,\ldots,t_h\in(0,T]\), let \(j_i=\lfloor Nt_i\rfloor\). The deterministic Gram convergence is
\[
\frac1N\sum_{k\le\min(j_i,j_l)}q_{j_i,k}q_{j_l,k}\longrightarrow K(t_i,t_l).
\]
Indeed, on \(k/N\in[\delta,\min(t_i,t_l)]\), this follows from compact-log-time coefficient convergence and Riemann summation. The complementary range \(k\le\delta N\) has total absolute contribution at most \(C_T\int_0^\delta u^{-2\gamma}\,du\), tending to zero as \(\delta\downarrow0\). The same estimates imply finite variance and a vanishing largest martingale coefficient for every fixed linear combination of the \(S_{j_i}/\sqrt N\).

From the square-summable envelope and bounded martingale innovations, Azuma--Hoeffding gives \(\Pr(|S_j|>\varepsilon j)\le2\exp(-c_{\varepsilon}j)\) for every \(\varepsilon>0\). The Borel--Cantelli lemma therefore proves \(S_j/j\to0\) almost surely, independently of the earlier scalar theorem. Consequently, the recent-window empirical mean \(m_j^{-1}(S_{j-1}-S_{j-m_j-1})\to0\) almost surely (as \(0<c<1\)). Hence \(\mathbb E(\varepsilon_j^2\mid\mathcal F_{j-1})\to1\) almost surely. In a fixed linear combination, the deterministic coefficient squares have bounded total and vanishing maximum; splitting the conditional-variance sum into finitely many early indices and its remaining tail gives the same Gram limit. Bounded innovations give conditional Lindeberg. The scalar martingale-array CLT and Cramér--Wold therefore yield the centered Gaussian finite-dimensional law with covariance \(K\).

**4. Tightness (the extra step not furnished by a scalar CLT).** We show a uniform deterministic increment estimate
\[
\sum_{k\ge1}(q_{j,k}-q_{i,k})^2\le C(j-i),\quad 0\le i<j,
\]
where each coefficient is zero when its second index exceeds the first. For \(i<j/2\), the two individual square-sum estimates from Step 2 suffice. For \(i\ge j/2\), the recursion and the envelope yield, for \(k\le i\),
\[
|q_{j,k}-q_{i,k}|
\le \sum_{r=i+1}^{j}\frac{|a|}{m_r}
\bigl(|q_{r-1,k}|+|q_{r-m_r-1,k}|\bigr)
\le C\frac{j-i}{j}(j/k)^\gamma.
\]
The sum of their squares is at most \(C(j-i)^2/j\); the newly introduced indices \(i<k\le j\) contribute at most \(C(j-i)\), because \(j/k\le2\). The martingale Burkholder fourth-moment inequality and \(|\varepsilon_k|\le2\) now imply \(\mathbb E|S_j-S_i|^4\le C(j-i)^2\). For the polygonal interpolation, the same fourth-moment estimate gives \(\mathbb E|Z_N(t)-Z_N(s)|^4\le C_T|t-s|^2\) for all \(s,t\in[0,T]\): at sub-grid distances use its deterministic \(\sqrt N\)-Lipschitz property and otherwise split off the two fractional end steps. Kolmogorov's tightness criterion proves tightness in \(C([0,T])\). Combined with Step 3, this proves the functional convergence and the stated Wiener-integral representation.

**5. Covariance signature.** Brownian change of variables gives \(K(t,t)=t\sigma^2\) and \(K(rs,rt)=rK(s,t)\). For \(s>0\), differentiating for \(t>s\) and sending \(t\downarrow s\) gives
\[
\frac1s\int_0^s w\!\left(\log\frac su\right)w'\!\left(\log\frac su\right)du
=\int_0^\infty e^{-v}w(v)w'(v)dv
=\frac12(\sigma^2-1).
\]
The integration by parts is justified by the sub-square-root growth from Step 2 and the delay equation, which gives \(e^{-v}w(v)^2\to0\). When \(a<0\), the exact discrete coefficient bounds and compact-log-time limit imply \(0\le w(v)\le1\) for all \(v\ge0\), with strict inequality \(w(v)<1\) on \(0<v<L\); when \(a>0\), they imply \(w(v)\ge1\) everywhere, with strict inequality on \(0<v<L\); hence \(\sigma^2<1\) and \(\sigma^2>1\), respectively. For \(a=0\), \(w\equiv1\), making \(Z=B\). A centered self-similar Gaussian process of index \(1/2\) with stationary increments would have covariance \(\sigma^2\min(s,t)\); the nonzero derivative excludes this whenever \(a\ne0\).

## Verification

Run `python3 check.py` using Python 3 standard library. The script constructs the exact finite innovation coefficients, enumerates every walk of length at most eight at three rational parameter pairs, calculates exact-rational finite covariances, and compares them with the exact martingale-Gram covariance. The recorded execution passed **4,196 exact-rational assertions**. These finite tests are consistency checks; Steps 2--5, not finite enumeration, prove the asymptotic and path-space statements. The independent proof of the square-summable coefficient envelope in Step 2 is included so that the key tightness premise is explicit.

## Relationship to prior work

Hu and Xue [1] introduce this exact proportional recent-memory model, the delay fundamental solution, the innovation expansion, and a **one-time** Gaussian theorem. Their one-time theorem alone does not imply joint convergence or tightness, and does not identify the full path covariance. Here the result is a functional invariance principle with a non-power-law, delay-kernel Gaussian limit and a sign-sensitive temporal dependence diagnostic.

Vázquez-Guevara and González-Navarrete [2] obtain a functional limit for a **fixed** number of recent increments. Tokumitsu [3] obtains a functional limit for a dynamic mixture whose conditional drift uses the **entire cumulative** past (times a scalar), unlike the present sliding-window drift. The amnesic models of Bertenghi and Laulin [4] and Coletti, dos Santos and Valle [5] sample from **positive weights over the entire history** rather than an abrupt relative-age cutoff. Their process-level results do not state the present delay-kernel covariance. These comparisons do not rule out all historical functional limit theorems or general martingale-transfer principles.

## Limitations

The parameter endpoints \(c=0\), \(c=1\), the phase boundary \(p=p_c\), the superdiffusive range, non-symmetric initial increments and parameter sequences depending on \(N\) are not covered. The joint Gaussian process is defined on finite compact time intervals, with consistent restrictions; no rate of weak convergence or strong pathwise coupling is proved. The principal scientific priority risk is an earlier general functional martingale-array theorem stated in a way that directly implies this kernel for sliding-window weights. The original coefficient compact-limit lemma [1] is used as a cited premise; its derivation is explained but not replaced by a new full quantitative approximation theorem.

## References

[1] Z. Hu and S. Xue, *The elephant random walk with proportionally growing recent memory*, arXiv:2611.17664v1 (first public 2026-11-13), https://arxiv.org/html/2611.17664v1 . See Lemmas 2.1, 3.1, 3.6, 3.8 and 4.1, and Theorem 1.2.

[2] V. H. Vázquez-Guevara and M. González-Navarrete, *Functional central limit theorem for dependent models with finite memory*, arXiv:2506.12145v1 (2025), https://arxiv.org/html/2506.12145v1 . See model (1.2) and Section 3.

[3] G. Tokumitsu, *Functional central limit theorems for the dynamic elephant random walk*, arXiv:2507.01708v1 (2025), https://arxiv.org/html/2507.01708 . See conditional drift (1.1) and Theorem 1.1.

[4] M. Bertenghi and L. Laulin, *A universal scaling limit for diffusive amnesic step-reinforced random walks*, arXiv:2402.09202 (2024), https://arxiv.org/abs/2402.09202 .

[5] C. F. Coletti, R. S. dos Santos and G. Valle, *Limit theorems for amnesic elephant random walks with random increment sizes*, arXiv:2609.14871 (2026), https://arxiv.org/abs/2609.14871 .
