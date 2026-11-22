# A unique turnover optimum for multistage traversal of ephemeral habitat bridges

## Finding
For a temporary habitat bridge with independent exponential opening and closure, a colonist must complete \(n\geq1\) successive exponential migration stages before the bridge next closes; closure erases partial progress. If the opening and closure rates are \(\alpha\lambda\) and \(\beta\lambda\), with fixed \(\alpha,\beta>0\), then the mean time \(M_n(\lambda)\) to reach the destination **starting with the bridge closed** is
\[
M_n(\lambda)=\frac{1}{\alpha\lambda}+\frac{\alpha+\beta}{\alpha\beta\lambda}\left[\prod_{i=1}^n\left(1+\frac{\beta\lambda}{\mu_i}\right)-1\right],\qquad\lambda>0,
\]
where each within-bridge stage has independent completion rate \(\mu_i>0\). This exact formula has three sharp implications.

1. For \(n=1\), \(M_1\) decreases strictly with \(\lambda\); there is no finite optimal turnover. For every \(n\geq2\), \(M_n\) is strictly convex and has exactly one finite global minimizer \(\lambda_n^*>0\).
2. Appending **any** additional independent positive-rate stage strictly decreases the optimum: \(\lambda_{n+1}^*<\lambda_n^*\) for every \(n\geq2\), without assuming equal stage rates.
3. When every stage rate equals \(\mu>0\), the optimum is \(\lambda_n^*=(\mu/\beta)x_n\), where \(x_n\) is the unique solution in \((0,1/(n-1))\) of
\[
(1-(n-1)x_n)(1+x_n)^{n-1}=\frac{\alpha}{\alpha+\beta}.
\]
As \(n\to\infty\),
\[
n\,\frac{\beta\lambda_n^*}{\mu}\longrightarrow c_p=1+W_0(-p/e),\qquad p=\frac{\alpha}{\alpha+\beta},
\]
where \(W_0\) is the principal real Lambert branch and \(c_p\in(0,1)\). In particular, optimal habitat-turnover speed decays as the reciprocal of the number of required stages at fixed stage rate and habitat availability.

## Assumptions and scope
The source habitat stays occupied and the target stays viable and empty until first colonization. The single connecting habitat bridge is alternately unavailable and available, beginning **unavailable**. The bridge becomes available after an exponential wait with rate \(\alpha\lambda\), and remains available for an independent exponential duration with rate \(\beta\lambda\); all open and closed periods are independent. During each available period the colonist completes \(n\) ordered independent exponential crossing stages with positive rates \(\mu_1,\ldots,\mu_n\). Any closure discards all partial progress, and each reopening starts a fresh independent attempt. Completing the final stage immediately and irreversibly colonizes the destination. All stochastic clocks are independent. The common multiplier \(\lambda>0\) changes turnover frequency **without changing** the stationary bridge availability \(p=\alpha/(\alpha+\beta)\). No claims are made about mortality, density dependence, memory across closures, or finite-time colonization probabilities.

## Proof
Let \(W\) be the unconstrained time to complete all \(n\) stages in one available interval, and let \(L\) be an independent exponential closure time of rate \(\beta\lambda\). The probability that a fresh available interval succeeds is the Laplace transform
\[
q(\lambda)=\Pr(W<L)=\mathbb E e^{-\beta\lambda W}=\prod_{i=1}^n\frac{\mu_i}{\mu_i+\beta\lambda}.
\]
An attempted interval consumes \(\min(W,L)\) time, with expectation \((1-q)/(\beta\lambda)\); the preceding closed interval contributes mean \(1/(\alpha\lambda)\). At failure the process restarts from exactly the original state. Conditioning on the first trial therefore gives
\[
M_n=\frac{1}{\alpha\lambda}+\frac{1-q}{\beta\lambda}+(1-q)M_n.
\]
Solving and substituting the product for \(q\) proves the claimed exact formula. Finiteness follows from \(q>0\) for every fixed positive rate choice.

Write
\[
P_n(\lambda)=\prod_{i=1}^n\left(1+\frac{\beta\lambda}{\mu_i}\right)=1+\sum_{k=1}^{n}c_k\lambda^k,
\]
where **each** elementary-symmetric coefficient \(c_k\) is strictly positive. Then
\[
M_n(\lambda)=\frac{1}{\alpha\lambda}+\frac{\alpha+\beta}{\alpha\beta}\sum_{k=1}^{n}c_k\lambda^{k-1}.
\]
For \(n=1\) the second term is constant, so \(M_1'(\lambda)=-1/(\alpha\lambda^2)<0\). For \(n\geq2\),
\[
M_n''(\lambda)=\frac{2}{\alpha\lambda^3}+\frac{\alpha+\beta}{\alpha\beta}\sum_{k=3}^{n}(k-1)(k-2)c_k\lambda^{k-3}>0.
\]
Moreover \(M_n'(\lambda)\to-\infty\) as \(\lambda\downarrow0\), whereas \(M_n'(\lambda)>0\) for all sufficiently large \(\lambda\), since \(c_2>0\). Thus strict convexity gives one and only one global minimizer.

For an additional positive stage rate \(\nu\), the product gains a factor \(1+\beta\lambda/\nu\). Consequently
\[
M_{n+1}(\lambda)-M_n(\lambda)=\frac{\alpha+\beta}{\alpha\nu}P_n(\lambda).
\]
Its derivative is strictly positive because \(P_n'(\lambda)>0\). At the old minimizer \(M_n'=0\), the new derivative is strictly positive, so the unique new critical point lies to its left. This proves strict stage-extension ordering for \(n\geq2\).

For equal \(\mu_i=\mu\), differentiate the exact expression after substituting \(x=\beta\lambda/\mu\). The stationary equation becomes
\[
g_n(x)=(1-(n-1)x)(1+x)^{n-1}=p.
\]
On \((0,1/(n-1))\), \(g_n(0)=1\), \(g_n(1/(n-1))=0\), and
\[
g_n'(x)=-n(n-1)x(1+x)^{n-2}<0.
\]
This yields the asserted unique root. Put \(y_n=nx_n\). Then \(0<y_n<n/(n-1)\), and any subsequential limit \(y\in[0,1]\) satisfies \((1-y)e^y=p\). The function \((1-y)e^y\) decreases strictly from \(1\) to \(0\) on \((0,1)\), so the subsequential limit is uniquely determined, hence the entire sequence converges. Solving \((1-y)e^y=p\) by the principal real branch gives \(y=1+W_0(-p/e)\).

## Verification
The package includes `corridor_checker.py`, runnable with Python 3 using only the standard library. It constructs the exact transient Markov-chain first-step linear equations for the closed state and all available-progress states. For \(n=1,\ldots,5\), 1,984 rational instance/derivative diagnostic checks compare this independent formulation to the renewal expression; 22 further rational checks test strict stage-extension derivative ordering and explicit two- and three-stage polynomial formulas, for a total of 2,006 passing assertions. The derivative diagnostics use an explicitly bounded finite difference, **not** a proof of the infinite-domain derivative identities. The proof above establishes all quantified claims analytically.

With \(\alpha=\beta=\mu_i=1\), the exact two-stage and three-stage times are
\[
M_2(\lambda)=\lambda^{-1}+4+2\lambda,\qquad M_3(\lambda)=\lambda^{-1}+6+6\lambda+2\lambda^2.
\]
Their optima are respectively \(\lambda_2^*=1/\sqrt2\) and \(\lambda_3^*=(\sqrt3-1)/2\), illustrating the strict reduction with stage number. At \(p=1/2\), the equal-stage large-\(n\) constant is \(c_p\approx0.7680390470\).

## Relationship to prior work
Matlack and Monde (2004) investigated dynamic ecological habitat connectivity and specifically observed short-lived bridges facilitating range expansion at intermediate turnover rates. Their full Methods and Results use a finite lattice simulation, not the present closed-start continuous-time resetting crossing model or a theorem for arbitrary stages. The current result gives a mathematically exact minimal mechanism, not a solution of their lattice model.

Doering and Gadoua (1992) established resonant activation for diffusion across a Markov-switching potential barrier; it motivates caution against claiming the **existence** of a fluctuation-speed optimum as novel. The present result concerns complete restart after closure and provides a sharp one-stage versus multistage classification, an all-positive-rates stage-addition ordering, and a quantified long-corridor limit.

More generally, interrupted-service and gated-first-passage theory predate this result. Gaver (1962) treats broad service interruptions, and Scher and Reuveni (2021) derive general gated-reaction relations for position processes decoupled from gate state. Baykal-Gürsoy, Figueroa-Candia and Duan (2025) derive transforms for preemptive replace/restart service and investigate tails. These frameworks contextualize the renewal calculation, but the examined accessible text does not state the exact ecological turnover minimizer, the universal strict ordering under an appended exponential crossing stage, or its Lambert-law scaling. Generic renewal-transform coverage is acknowledged; mathematical priority for this specific combined theorem is not independently established.

## Limitations
The stationary bridge availability is fixed as turnover changes, and the bridge is initially closed. Different initial gate states, any progress retained through closure, mortality of the source population, varying stage rates tied to turnover, correlated gate and crossing clocks, multiple interacting bridges, or empirical landscape dynamics may change conclusions. The formal stage count is a model abstraction; it is not a claim that ecological distance alone determines the number of stages. The mathematical theorem is exact inside its assumptions but has not been field validated. Published generic interruption frameworks may yield related formulas by specialization; comprehensive historical uniqueness is not certified.

## References
1. G. R. Matlack and J. Monde (2004), “Consequences of low mobility in spatially and temporally heterogeneous ecosystems,” *Journal of Ecology* 92, 1025–1035. First published 2004-09-16. https://doi.org/10.1111/j.0022-0477.2004.00908.x
2. C. R. Doering and J. C. Gadoua (1992), “Resonant activation over a fluctuating barrier,” *Physical Review Letters* 69, 2318–2321. https://doi.org/10.1103/PhysRevLett.69.2318
3. D. P. Gaver Jr. (1962), “A waiting line with interrupted service, including priorities,” *Journal of the Royal Statistical Society, Series B* 24, 73–90. https://doi.org/10.1111/j.2517-6161.1962.tb00438.x
4. Y. Scher and S. Reuveni (2021), “A unified approach to gated reactions on networks,” arXiv:2101.05124. https://arxiv.org/abs/2101.05124
5. M. Baykal-Gürsoy, M. Figueroa-Candia and Z. Duan (2025), “Completion times of jobs on two-state service processes and their asymptotic behavior,” *Probability in the Engineering and Informational Sciences* 39, 188–216. https://doi.org/10.1017/S0269964824000226
