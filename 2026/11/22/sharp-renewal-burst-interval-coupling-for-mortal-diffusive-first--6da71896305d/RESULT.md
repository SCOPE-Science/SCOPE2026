# Sharp renewal burst–interval coupling for mortal diffusive first passage

## Finding

Consider independent mortal diffusive searchers introduced in batches at renewal epochs, with the number of searchers in each batch allowed to depend on the **immediately preceding interarrival interval**. If every individual searcher has eventual success probability \(p\in(0,1)\), set \(a=1-p\). For iid interval–batch pairs \((W,J)\), with strictly positive bounded intervals and bounded positive integer batch sizes, the probability \(Q(t)\) that **none** of the emitted particles has reached the target by time \(t\) has the exact exponential decay rate

\[
\boxed{\lim_{t\to\infty}-\frac{1}{t}\log Q(t)=\theta,\qquad
\mathbb E\!\left[e^{\theta W}a^J\right]=1,\quad\theta>0.}
\tag{1}
\]

Among **all joint laws** of \((W,J)\) with the same two marginal laws, the largest possible rate \(\theta\) is achieved by the **comonotone** coupling (large batches after long intervals), and the smallest is achieved by the **countermonotone** coupling (large batches after short intervals). Both bounds are sharp. This is an ordering of long-time first-reaction survival exponents, not a finite-time stochastic ordering.

For a two-point example, let each interval take the values \(1,2\) with probabilities \(1/2,1/2\), let each batch size also take the values \(1,2\) with probabilities \(1/2,1/2\), and let \(a=1/2\). The three exponents for comonotone coupling, independent marks, and countermonotone coupling, respectively, are

\[
\boxed{
\theta_{\rm co}=\log2,
\qquad\theta_{\rm ind}=\log\!\left(\frac{\sqrt{201}-3}{6}\right),
\qquad\theta_{\rm anti}=\log\!\left(\frac{\sqrt{65}-1}{4}\right).
}
\tag{2}
\]

Thus \(\theta_{\rm co}/\theta_{\rm anti}=1.219319668\ldots\), a change of approximately \(21.93\%\) in the asymptotic no-reaction decay rate. All protocols have the **same interarrival distribution, burst-size distribution, average renewal rate, and average production throughput**. Equation (2) is realized by one-dimensional Brownian target search with diffusivity and degradation rate both equal to \(1\) and source distance \(\log2\).

## Assumptions and scope

Initially the system contains no searchers. Let \((W_i,J_i)_{i\ge1}\) be independent, identically distributed random pairs with any dependence *within* each pair and with deterministic bounds

\[
0<w_-\le W_i\le w_+<\infty,
\qquad 1\le J_i\le j_+<\infty.
\]

Here \(J_i\) is integer-valued and \(j_+\) is an integer. At time \(S_i=\sum_{k=1}^iW_k\), introduce exactly \(J_i\) independent searchers, each starting at \(x_0>0\) and evolving on the positive half-line with Brownian generator \(D\partial_{xx}\), absorbing target \(0\), and an independent exponential mortality clock of rate \(d>0\). All particles' motions and mortality clocks are independent of all interval–batch pairs and of one another. Put \(N(t)=\max\{i:S_i\le t\}\). The first successful target-hitting time, if any, is \(T\), and \(Q(t)=\Pr(T>t)\).

For these Brownian particles the eventual single-particle success probability is

\[
p=\Pr(\tau_0<\Delta)=\mathbb E[e^{-d\tau_0}]
  =e^{-x_0\sqrt{d/D}},\quad a=1-p\in(0,1),
\]

where \(\tau_0\) is the Brownian hitting time and \(\Delta\) the independent death time. The proof works, more generally, for independent searchers with the same defective reaction-time law whenever its eventual failure probability is \(a\in(0,1)\) and its remaining eventual-success tail is bounded above by a decaying exponential times a constant.

## Proof

**1. Exact conditional first-reaction survival.** Let \(U\in[0,\infty]\) be the target-hitting delay, with \(U=\infty\) if mortality wins. Write \(q(u)=\Pr(U>u)\). The eventual failure probability is \(a=\Pr(U=\infty)\). For Brownian searchers with independent exponential death,

\[
0\le q(u)-a=\Pr(u<\tau_0<\Delta)\le\Pr(\Delta>u)=e^{-du}.
\tag{3}
\]

Conditional on all interval–batch pairs, the probability of no target encounter by time \(t\) is exactly \(\prod_{i=1}^{N(t)}q(t-S_i)^{J_i}\), hence

\[
Q(t)=\mathbb E\left[\prod_{i=1}^{N(t)}q(t-S_i)^{J_i}\right].
\tag{4}
\]

Define the easier permanent-failure quantity

\[
F(t)=\mathbb E\left[a^{\sum_{i=1}^{N(t)}J_i}\right].
\]

As \(q(u)\ge a\) and \(\log(q(u)/a)\le(q(u)-a)/a\), equation (3) gives the pathwise uniform bound

\[
1\le\prod_{i=1}^{N(t)}\left(\frac{q(t-S_i)}a\right)^{J_i}
\le\exp\!\left[\frac{j_+}{a}\sum_{i=1}^{N(t)}e^{-d(t-S_i)}\right]
\le\exp\!\left[\frac{j_+}{a(1-e^{-dw_-})}\right]=C.
\]

The last inequality follows because successive renewal epochs are separated by at least \(w_-\). Thus, for all \(t\ge0\),

\[
F(t)\le Q(t)\le C F(t).
\tag{5}
\]

**2. Exponential root and finite-time bounds.** Since \(0<a<1\) and \(J\ge1\), the function \(H(s)=\mathbb E[e^{sW}a^J]\) satisfies \(H(0)<1\), is continuous and strictly increasing for \(s\ge0\), and tends to infinity. It therefore has a unique positive root \(H(\theta)=1\). Set \(M_n=e^{\theta S_n}a^{\sum_{i=1}^nJ_i}\), with \(M_0=1\). The iid pair assumption and the root identity make \((M_n)\) a mean-one martingale. For fixed \(t\), the first index \(K=N(t)+1\) for which \(S_K>t\) is a bounded stopping time (since \(W_i\ge w_-\)), so \(\mathbb E M_K=1\).

Since \(t<S_K\le t+w_+\) and \(a^{j_+}\le a^{J_K}\le1\),

\[
a^{j_+}e^{\theta t}a^{\sum_{i=1}^{N(t)}J_i}
\le M_K\le e^{\theta(t+w_+)}a^{\sum_{i=1}^{N(t)}J_i}.
\]

Taking expectations and using the unit expectation of \(M_K\) yields the explicit *all-time* envelope

\[
\boxed{e^{-\theta(t+w_+)}\le F(t)\le a^{-j_+}e^{-\theta t}}.
\tag{6}
\]

Combining (5) and (6) proves (1), without a renewal theorem, lattice restriction, or inference from finite-time simulation.

**3. Sharp fixed-marginal coupling order.** Fix any two marginal laws for \(W\) and \(J\) satisfying the stated bounds. For each fixed \(s>0\), the function \(w\mapsto e^{sw}\) is strictly increasing, whereas \(j\mapsto a^j\) is strictly decreasing. For \(w_1<w_2\) and \(j_1<j_2\), the two matchings differ by

\[
(e^{sw_1}a^{j_1}+e^{sw_2}a^{j_2})
-(e^{sw_1}a^{j_2}+e^{sw_2}a^{j_1})
=(e^{sw_2}-e^{sw_1})(a^{j_2}-a^{j_1})<0.
\]

Successive exchanges (or discrete quantile approximations followed by bounded convergence) give the rearrangement bounds

\[
H_{\rm co}(s)\le H_{\rm arbitrary}(s)\le H_{\rm anti}(s),\qquad s>0.
\]

The endpoints are realized by \((W,J)=(F_W^{-1}(V),F_J^{-1}(V))\) and \((W,J)=(F_W^{-1}(V),F_J^{-1}(1-V))\), respectively, for uniform \(V\) on \((0,1)\), with generalized quantile functions. Because all three \(H\)'s are strictly increasing and equal to \(1\) at their corresponding roots, one obtains

\[
\boxed{\theta_{\rm co}\ge\theta_{\rm arbitrary}\ge\theta_{\rm anti}}.
\tag{7}
\]

This proves the *global*, sharp fixed-marginal interval/cargo coupling envelope, with no assumption of independence between a batch size and its preceding interval.

Each extremum determines a unique joint law, even for atomic marginals. To see this, fix \(s>0\), set \(X=e^{sW}\), \(Y=a^J\), and express \(\mathbb E[XY]\) as the integral of \(\Pr(X>x,Y>y)\) over \(x,y>0\). The common and reversed quantile matchings of \(X,Y\) attain the pointwise upper and lower Fréchet bounds on this joint tail. For equality in the integral, the joint tail must equal its corresponding pointwise bound almost everywhere; right-continuity, taking sequences of thresholds from above, then gives equality everywhere. The transformations from \(W,J\) are injective, so this identifies their joint law. Equality of two rates at either endpoint gives equality in the transform at that endpoint's root \(s=\theta>0\), and hence the same uniqueness. If a marginal is degenerate, the two extrema coincide because there is only one joint law.

**4. Exact two-point demonstration.** Writing \(y=e^\theta\), the three defining equations are, respectively,

\[
\tfrac18(y^2+2y)=1,
\qquad\tfrac3{16}(y^2+y)=1,
\qquad\tfrac18(2y^2+y)=1.
\]

They have the three positive roots \(y=2\), \(y=(\sqrt{201}-3)/6\), and \(y=(\sqrt{65}-1)/4\), establishing (2) and their strict order exactly. With \(D=d=1\) and \(x_0=\log2\), the Brownian identity above gives \(a=1/2\), so the demonstration satisfies every physical hypothesis.

## Verification

Run `python3 verify_coupled_bursts.py` with Python's standard library. The program checks the three algebraic roots, strict ordering, equal interval and cargo marginals and average flux, exact rational renewal recursions against independently evaluated finite-horizon recursions, the finite-time martingale overshoot bounds, and convergence of numerically computed slopes toward all three predicted exponents. Its tests passed. The uniform comparison (5), optional-stopping bounds (6), and global rearrangement theorem (7) supply the **infinite-horizon proofs**; the finite checks are corroboration only.

## Relationship to prior work

Mercado-Vásquez and Boyer's 2026 stochastic synthesis–degradation studies analyze Poisson production and, in the November paper, independent random batch sizes; their first-passage analysis is not a fixed-marginal optimization of the *dependence* between each interarrival duration and its subsequent batch size. A 2026 published note, *Renewal production clocks govern the long-time survival of mortal diffusive searchers*, treats one searcher per independent renewal epoch and the effect of varying the **marginal distribution of intervals**. Its renewal-root result is a direct precursor to (1) in the single-particle case, so that special case is explicitly **not** claimed as new.

Hauke, Voits and Schwarz (2026) analyze the influence of burst and interval statistics on concentration-threshold activation in vesicle signaling, which is a different first-passage observable. Butler (published online in 2024) develops general dependent renewal–reward transforms, relevant mathematical background that may subsume the root mechanism in (1). The assessed addition is specifically the sharp, universally attained **joint-coupling envelope (7)** for the eventual target-arrival hazard of independent mortal diffusing searchers, under unchanged two marginals, together with the physical exact example (2). The tools (exponential tilting and rearrangement) are classical; no claim of their originality is made.

## Limitations

The proof assumes an initially empty system, independent particles and mortality clocks, iid interval–batch **pairs**, a uniform positive lower/upper bound on waiting times, and a uniform finite batch-size bound. It does not cover feedback from current particle population or unbounded heavy-tailed intervals or batches. For a general delayed-success law the uniform comparison in (5) uses an exponentially bounded remaining success tail. The bounds control the exponential tail rate, **not** the finite-time survival ordering, mean first-passage time, or a sharp prefactor. Classical dependent renewal–reward literature may contain alternative derivations of the root; one relevant article published online in 2024 could only be inspected at the abstract level and therefore remains an explicit novelty risk. These comparisons do not establish historical priority.

## References

- G. Mercado-Vásquez and D. Boyer, *Stochastic synthesis-degradation processes: first-passage properties and connections with resetting*, arXiv:2602.11095v1 (11 February 2026). https://arxiv.org/abs/2602.11095
- D. Boyer and G. Mercado-Vásquez, *Stochastic synthesis and degradation of arbitrary diffusive processes*, arXiv:2611.04843v1 (3 November 2026). https://arxiv.org/html/2611.04843v1
- J. Hauke, J. B. Voits and U. S. Schwarz, *Activation in Vesicle-Mediated Signaling Shaped by Batch Arrival Statistics*, arXiv:2605.06456 (first publication 7 May 2026). https://arxiv.org/abs/2605.06456
- R. W. Butler, *Distribution theory for dependent renewal–reward processes and their first-passage times using saddlepoint and residue expansions*, *Journal of Applied Probability* 62 (2025), 447–474; first online 5 December 2024. https://doi.org/10.1017/jpr.2024.99
- *Renewal production clocks govern the long-time survival of mortal diffusive searchers*, publicly indexed mathematical note (2026), distinguished above from the batch-coupling claim.
