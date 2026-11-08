# Mixed atomic–diffuse quorum clocks: exact limit laws and deterministic time atoms

## Finding

Let a coupon collection have \(N\) uniformly sampled types with positive quorum weights summing to one. A fixed finite number of types retain positive limiting weights, while every remaining weight vanishes. The normalized time to exceed any fixed quorum threshold converges to the first crossing of a deterministic exponential-growth component plus independent finite jumps. This limiting law has an explicit survival function, a **complete classification of its deterministic-time atoms**, and convergence of every positive moment. Although every finite continuous-time law is atomless, its limit may have as many as \(2^r\) distinct positive-mass atoms when there are \(r\) macroscopic types; this upper bound is attained.

Here is a precise statement. Fix \(r\ge 1\), \(0<\theta<1\), and \(\lambda>0\). For each \(N>r\), let \(w_{1,N},\ldots,w_{N,N}>0\) sum to one. Assume
\[
w_{i,N}\longrightarrow a_i>0\quad (1\le i\le r),\qquad
b_N:=\max_{j>r}w_{j,N}\longrightarrow0,\qquad
d:=1-\sum_{i=1}^r a_i>0.
\]
Let \(\tau_N\) be the first time the discovered weight exceeds \(\theta\) under independent coupon clocks of rates \(\lambda/N\). Let \(K_N\) be the number of draws needed to exceed the same threshold in independent uniform discrete sampling. If \(E_1,\ldots,E_r\) are independent unit exponentials, set
\[
X(t)=d(1-e^{-t})+\sum_{i=1}^r a_i\mathbf1_{\{E_i\le t\}},\qquad
T=\inf\{t\ge0:X(t)>\theta\}.
\]
Then
\[
\frac{\lambda\tau_N}{N}\Rightarrow T,\qquad
\frac{K_N}{N}\Rightarrow T,
\]
and, for every real \(q>0\), the \(q\)-th moments of both normalized collection times converge to \(\mathbb E T^q\). The full limiting survival function is
\[
\Pr(T>t)=\sum_{A\subseteq[r]}
\mathbf1_{\{a_A+d(1-e^{-t})<\theta\}}
(1-e^{-t})^{|A|}e^{-t(r-|A|)},\qquad t\ge0,
\]
where \(a_A=\sum_{i\in A}a_i\). **The strict inequality is essential** at deterministic crossing times: the infimum of times with mass strictly greater than \(\theta\) can equal a time at which \(X(t)=\theta\), because the diffuse part increases immediately afterward.

For each subset \(A\subseteq[r]\) satisfying \(0<\theta-a_A<d\), define
\[
t_A=-\log\!\left(1-\frac{\theta-a_A}{d}\right).
\]
The deterministic atoms are **exactly** the distinct values among these \(t_A\), with probability at \(t\) equal to
\[
\Pr(T=t)=\sum_{A:t_A=t}(1-e^{-t})^{|A|}e^{-t(r-|A|)}.
\]
There are at most \(2^r\) such locations, and this is sharp: take \(a_i=2^{i-1}/[4(2^r-1)]\), \(d=3/4\), and \(\theta=1/2\). All \(2^r\) subsets have distinct qualifying crossing times.

Let \(\mathcal A\) denote the finite set of deterministic atom locations. For each \(N\), \(\lambda\tau_N/N\) is atomless, and hence
\[
\left\|\mathcal L(\lambda\tau_N/N)-\mathcal L(T)\right\|_{\mathrm{TV}}
\ge \Pr(T\in\mathcal A).
\]
In particular, whenever the limit has a deterministic atom, weak convergence and convergence of all moments **do not strengthen to total-variation convergence**.

A concrete one-heavy-type example takes \(a_1=2/5\), \(d=3/5\), and \(\theta=1/2\). Then
\[
T\stackrel d=\min\!\left(\log6,\max(E_1,\log(6/5))\right).
\]
It has atoms of mass \(1/6\) at each of \(\log(6/5)\) and \(\log6\), continuous mass \(2/3\) between them, and
\[
\mathbb ET=\log(6/5)+2/3.
\]

## Assumptions and scope

All limits send \(N\to\infty\) with \(r\), \(\theta\), and \(\lambda\) fixed. The macroscopic weights \(a_i\) are strictly positive, and their sum is strictly less than one. No ordering, equality, or regularity is required of the remaining weights beyond positivity, vanishing maximum, and total mass. Coupon draws and first-discovery clocks are independent in the usual thinning coupling. The threshold convention is strictly **greater than** \(\theta\), not greater than or equal. This result concerns homogeneous sampling *rates* with heterogeneous quorum *weights*, not aligned activity-weight Zipf clocks.

## Proof

**1. Coupling and the diffuse empirical-process estimate.** Rescale continuous time by \(t=\lambda u/N\). Every discovery clock then becomes a unit exponential. Couple the \(r\) heavy clocks to fixed \(E_i\), and write the remaining independently sampled clocks as \(E_{j,N}\). Define \(d_N=\sum_{j>r}w_{j,N}\to d\), and \(F(t)=1-e^{-t}\). The weighted dust process is
\[
D_N(t)=\sum_{j>r}w_{j,N}\mathbf1_{\{E_{j,N}\le t\}}.
\]
Symmetrization with independent copies and Rademacher signs, followed by sorting the clock observations and applying the \(L^2\) martingale maximal inequality to the resulting signed partial sums, gives
\[
\mathbb E\sup_{t\ge0}|D_N(t)-d_NF(t)|
\le4\left(\sum_{j>r}w_{j,N}^2\right)^{1/2}
\le4\sqrt{d_Nb_N}\longrightarrow0.
\]
The first inequality follows because the symmetrized process has supremum bounded in expectation by twice the Rademacher maximal supremum, which in turn is at most twice its terminal \(L^2\) norm. Consequently, for the entire discovered-mass process \(X_N\),
\[
\mathbb E\sup_{t\ge0}|X_N(t)-X(t)|
\le\sum_{i=1}^r|w_{i,N}-a_i|+|d_N-d|+4\sqrt{d_Nb_N}\to0.
\]
This inequality is the uniform-in-time premise used below. It requires no concentration assumption beyond \(b_N\to0\).

**2. Stability of the strict-threshold passage.** Almost surely the \(E_i\) are distinct, and no jump lands **exactly** on the threshold: condition on every clock except \(E_i\), and use the continuous density of \(E_i\) together with the strictly increasing function \(dF(t)\). Therefore the crossing \(T\) is either a strict jump overshoot or a continuous crossing between two jumps. In either case, for every sufficiently small \(\varepsilon>0\),
\[
X(T-\varepsilon)<\theta<X(T+\varepsilon).
\]
Uniform-in-time convergence in probability of \(X_N\) then brackets \(\lambda\tau_N/N\) between \(T-\varepsilon\) and \(T+\varepsilon\) with probability tending to one. Thus the continuous-time weak limit holds. The limit is finite because \(X(t)\uparrow1>\theta\).

**3. Exact survival law, atoms, and sharpness.** At fixed \(t\), the indicators \(\mathbf1_{\{E_i\le t\}}\) are independent Bernoulli variables with success probability \(F(t)\). Since \(d>0\), the trajectory increases strictly immediately to the right of every time, even between jumps; hence \(T>t\) precisely when \(X(t)<\theta\), explaining the strict sign in the survival formula. Conditioning on the active subset gives the stated finite sum. A nonjump passage can only occur at a deterministic solution of \(a_A+dF(t)=\theta\), namely one of the qualifying \(t_A\). On the event that the active subset at \(t_A\) is exactly \(A\), the process is below threshold at every earlier time and crosses continuously at \(t_A\); this event has probability \(F(t_A)^{|A|}(1-F(t_A))^{r-|A|}\). A passage occurring at a jump time \(E_i\) has no fixed-time atom. Summing disjoint active-subset events proves that the displayed set and weights are complete. The binary choice of \(a_i\) produces \(2^r\) distinct subset sums and therefore distinct crossing times, proving sharpness. Finite continuous-time completion always happens at one of finitely many exponentially distributed discovery times, so its law charges no fixed point; the total-variation bound follows by testing the set \(\mathcal A\).

**4. Discrete coupon count and moments.** In the marked Poisson coupling let \(P_\lambda(u)\) count arrivals of the pooled rate-\(\lambda\) process. Then \(K_N=P_\lambda(\tau_N)\). The compensated Poisson martingale and optional stopping yield
\[
\mathbb E\left|\frac{K_N}{N}-\frac{\lambda\tau_N}{N}\right|^2
=\frac{\lambda\mathbb E\tau_N}{N^2}.
\]
For every \(t\ge0\), undiscovered expected weight equals \(e^{-t}\) at rescaled time \(t\). Markov's inequality therefore gives, uniformly in \(N\),
\[
\Pr(\lambda\tau_N/N>t)\le\frac{e^{-t}}{1-\theta}.
\]
Thus \(\lambda\mathbb E\tau_N/N\le1/(1-\theta)\), making the preceding squared difference at most \(1/[N(1-\theta)]\), which proves the discrete weak limit. Independently, after \(k\) discrete draws the expected undiscovered weight is \((1-1/N)^k\); hence
\[
\Pr(K_N>k)\le\frac{(1-1/N)^k}{1-\theta}.
\]
These uniform exponential tails give uniform integrability of every positive power of both normalized variables and hence convergence of all positive moments.

## Verification

The included standalone `verify.py` uses only the Python standard library. It compares finite uniform-draw subset-chain recursions against independent exhaustive word enumeration, checks rational exponential-clock subset probabilities by complementary missing-set enumeration, verifies the one-heavy-type exact binomial specialization and its two point masses, and checks the sharp \(2^r\)-atom construction through \(r=8\). A local replay passed **2,063 exact-rational and finite diagnostic assertions**. All infinite-limit statements are supplied by the analytic argument above, not by computational extrapolation. To replay: `python verify.py`.

## Relationship to prior work

Müller and Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1 (July 9, 2026), establish the homogeneous-clock limit under the stronger condition that **every** quorum weight vanishes (Theorem 4.1). Their separate atomic Zipf analysis (Section 7) has **aligned nonuniform rates and weights** and produces a countably atomic pure-jump process. The present statement treats the unaddressed intermediate case with finitely many persistent weights and a positive diffuse remainder under uniform discovery rates, determining the entire limit law and its discrete-time atoms. The source's finite subset probability identity is acknowledged as a background starting point, not claimed as new. Chang and Ross (2007) treat general multiple-subset stopping rules and finite moments; this supplies a related abstract finite-state framework, not a verified statement of the present limiting law.

## Limitations

The theorem requires a **positive diffuse residual mass**. It does not classify the pure-atomic boundary \(d=0\), infinite collections of macroscopic atoms, heterogeneous clock rates, or moving thresholds. All results are mathematical statements about the specified idealized models; they are not independent validations of an empirical system. A literature-priority uncertainty remains because the full text of Chang and Ross (2007) was not accessible in the available reading session, and broader weighted empirical-process results may imply related special cases. The result does not assert a universal convergence rate for the hitting time itself near jump or threshold coincidences.

## References

1. S. Müller and S. Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1 (first publicly posted July 9, 2026), https://arxiv.org/html/2607.08551.
2. K.-C. Chang and S. M. Ross, *The Multiple Subset Coupon Collecting Problem*, *Probability in the Engineering and Informational Sciences* **21** (2007), 435–440, https://doi.org/10.1017/S026996480700006X.
3. E. Anceaume, Y. Busnel and B. Sericola, *New Results on a Generalized Coupon Collector Problem Using Markov Chains*, arXiv:1402.5245 (2014), https://arxiv.org/abs/1402.5245.
