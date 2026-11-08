# Three entrance mechanisms and an independent exponential clock for rare deep excursions of a random interval map

## Finding

Let \(1/2<p<1\), \(q=1-p\), and \(t=p/q>1\). For the random interval dynamics \(x\mapsto 2x\bmod 1\) with probability \(p\) and \(x\mapsto x/2\) with probability \(q\), start with uniform position in \([1/2,1)\). Define the shell index \(J_n=k\) when \(2^{-k-1}\leq X_n<2^{-k}\), and the first deep-shell hitting time \(T_m=\inf\{n\geq1:J_n\geq m\}\), for integer \(m\geq2\). Every visit to shell zero begins a statistically fresh excursion. Denote the first-step type of the successful excursion by \(C\) (contracting) or \(E\) (expanding), and its first-step shell index by \(K_m\). Let \(h_m\) be the probability that a **single** excursion reaches shell \(m\) or deeper before returning to shell zero.

The exact single-excursion success probability is
\[
h_m=\frac{q(t-1)}{t^m-1}+\frac{p}{t^m-1}\sum_{k=1}^{m-1}\frac{t^k-1}{2^{k+1}}+\frac{p}{2^m}.
\]
The complete joint entrance-mark law, unnormalized by success, is
\[
\Pr(C,K_m=1,\mathrm{success})=\frac{q(t-1)}{t^m-1},\qquad
\Pr(E,K_m=k,\mathrm{success})=\begin{cases}
\dfrac{p(t^k-1)}{2^{k+1}(t^m-1)},&1\le k<m,\\[3pt]
\dfrac{p}{2^{k+1}},&k\ge m.
\end{cases}
\]
Conditional laws follow by division by \(h_m\).

There is a sharp three-way selection transition at \(p=2/3\):

1. When \(1/2<p<2/3\), put \(C_p=(t-1)[q+p/(2-t)]\). Then \(h_m\sim C_p t^{-m}\), and the successful initial mark converges on the countable space \(\{C\}\cup\{(E,k):k\ge1\}\) to
\[
\Pr(C)=\frac{q(t-1)}{C_p},\qquad
\Pr(E,k)=\frac{p(t^k-1)}{2^{k+1}C_p}.
\]
Here a positive fraction of successful excursions begin with contraction, and the initial depth remains tight.

2. When \(p=2/3\), \(h_m\sim (m/3)2^{-m}\), successful excursions begin with expansion with probability tending to one, and \(K_m/m\), conditional on success, converges to the uniform law on \([0,1]\).

3. When \(2/3<p<1\), put \(A_t=(t-2)/[2(t-1)]\). Then \(h_m\sim p(t-1)2^{-m}/(t-2)\); successful excursions begin with expansion with probability tending to one; and the integer overshoot \(D_m=K_m-m\), conditional on success, converges on \(\mathbb Z\) to the two-sided geometric mass function
\[
\Pr(D=d)=A_t2^{-d}\quad(d\ge0),\qquad
\Pr(D=-j)=A_t(2/t)^j\quad(j\ge1).
\]
This includes successful entries with \(K_m<m\), whose biased walk reaches the threshold subsequently.

In **all three regimes**, writing \(\mu_p=2p/(2p-1)\),
\[
\mathbb E[T_m]\sim\frac{\mu_p}{h_m},\qquad
\frac{T_m}{\mathbb E[T_m]}\ \Longrightarrow\ \operatorname{Exp}(1).
\]
The limiting exponential time is independent of the respective limiting successful-excursion entrance mark: the \(C/E,k\) mark in the first regime, \(K_m/m\) in the second, and \(K_m-m\) in the third. No assertion is made about pointwise sample trajectories started from an arbitrary deterministic nonrandom position.

## Assumptions and scope

The initial position is uniform in \([1/2,1)\), independent of the iid map choices, and \(p\) is fixed strictly between \(1/2\) and \(1\). The target shell depth \(m\) tends to infinity through positive integers. Visits and excursions use the **annealed** distribution (averaging over map choices and the initial position). A return at the first step is a valid unsuccessful excursion. Shell zero is \([1/2,1)\); the left endpoint \(0\), which is exceptional, has probability zero. The initial mark \(K_m\) is the first-step shell index in the final successful excursion, *not* the actual hitting location at time \(T_m\). At \(p>2/3\), it is permitted to be smaller or greater than \(m\).

## Proof

**1. Exact regenerated chain.** A position uniform on a dyadic shell remains conditionally uniform on any shell it reaches in one step. For \(j\ge1\), doubling sends shell \(j\) bijectively to shell \(j-1\), while halving sends it to \(j+1\). At shell zero, halving sends it to shell one, while doubling mod one sends it to the uniform distribution on \([0,1)\), whose shell index \(G\) satisfies \(\Pr(G=k)=2^{-k-1}\), \(k\ge0\). Conditional uniformity also holds after a return to shell zero, so successive return excursions are independent and identically distributed, with the same initial distribution. This is a fact about the interval map, not just a Markov approximation.

**2. Single-excursion gambler's ruin.** From a starting depth \(1\le k<m\), until hitting \(0\) or \(m\), the chain walks upward with probability \(q\) and downward with probability \(p\). The unique solution of \(H_0=0\), \(H_m=1\), \(H_k=qH_{k+1}+pH_{k-1}\) is
\[
H_k=\frac{t^k-1}{t^m-1}.
\]
For first-step contraction, the entry depth is exactly one; for first-step expansion, the index has the geometric \(G\) distribution. The cases \(G=0\), \(1\le G<m\), and \(G\ge m\) yield respectively failure, gambler's ruin success with probability \(H_G\), and immediate success. Their total and marked success probabilities give the exact formulas above.

**3. Entrance-law phase transition.** For \(t<2\), the series \(\sum_{k\ge1}2^{-k-1}(t^k-1)=(t-1)/(2-t)\) converges, and \(2^{-m}=o(t^{-m})\). This gives \(h_m\sim C_p t^{-m}\), with summable limiting mark masses. For \(t=2\), each term \(2^{-k-1}(2^k-1)\) equals \(1/2-2^{-k-1}\), making the successful interior first-step depth asymptotically uniform on \(\{1,\ldots,m-1\}\); direct overshoot and contraction are lower-order. For \(t>2\), relabel interior depths by \(k=m-j\) and direct overshoots by \(k=m+d\). The respective weights, divided by \(p2^{-m}\), converge to \((2/t)^j/2\) and \(2^{-d}/2\); their geometric sums give \((t-1)/(t-2)\). The displayed two-sided geometric law follows. Tightness in the first and third regimes follows directly from geometric summability, hence the finite-coordinate limits are full weak limits.

**4. Rare-event clock and independence.** Let \(R\) be a first *return* time to zero from the fresh shell-zero start, and let \(L_m=\min(R,T_m)\). For \(p>1/2\), the downward-biased nearest-neighbor walk from \(k\) has mean time \(k/(p-q)\) to reach zero. Since the mean initial shell after the first step equals \(q\cdot1+p\,\mathbb EG=1\), one has
\[
\mathbb ER=1+\frac1{p-q}=\frac{2p}{2p-1}=\mu_p.
\]
Moreover, \(\mathbb ER^2<\infty\), because the biased walk's return-time second moment grows at most quadratically with the initial depth, and the initial-depth distribution has geometric tails. On a fixed excursion path, \(\{T_m<R\}\) eventually fails for all sufficiently large \(m\); therefore \(h_m\downarrow0\), \(L_m\uparrow R\) almost surely, and \(\mathbb EL_m\to\mu_p\).

By regeneration, the exact renewal identity is \(\mathbb ET_m=\mathbb EL_m/h_m\). For the joint clock and mark, write \(b_m(s)=\mathbb E[e^{-s h_m L_m/\mu_p};\mathrm{failure}]\) and \(a_m(s,B)=\mathbb E[e^{-s h_m L_m/\mu_p};\mathrm{success},\mathrm{mark}\in B]\). A geometric renewal sum gives
\[
\mathbb E[e^{-s h_m T_m/\mu_p};\mathrm{mark}\in B]=\frac{a_m(s,B)}{1-b_m(s)}.
\]
For fixed \(s\ge0\), dominated convergence and \(L_m\le R\), \(\mathbb ER^2<\infty\), give \(1-b_m(s)=h_m(1+s+o(1))\). Also \(a_m(s,B)/h_m\) differs from \(\Pr(\mathrm{mark}\in B\mid\mathrm{success})\) by at most \(s\mu_p^{-1}\mathbb E[L_m;\mathrm{success}]\to0\). Hence this joint Laplace transform converges to \(\Pr(M\in B)/(1+s)\), independently for each mark-event continuity set. The convergence of the marks proved in step 3 yields an independent unit exponential clock. Replacing \(h_m/\mu_p\) by \(1/\mathbb ET_m\) is asymptotically harmless.

## Verification

The accompanying standalone \(\texttt{checks/verify.py}\) uses exact rational arithmetic to compare the single-excursion success mass with the complete marked decomposition, to verify the gambler's ruin recurrence, and to solve finite-state hitting-time equations independently. It additionally checks the three limiting profiles at explicitly chosen large depths. It completes 1,078 stated assertions. These finite calculations support but do not replace the infinite-depth proof, which depends on the geometric-series and dominated-convergence arguments above. Execute with \(\texttt{python3 checks/verify.py}\); SymPy is used for finite rational linear systems.

## Relationship to prior work

The origin of the binary-expanding/half-contracting random interval map and its stationary density is Yan et al. (2023). Monthus (2024/2025), particularly equations (20), (31)--(43), (76), and (95)--(102), already identifies the shell Markov chain, the stationary phase boundary at \(p=2/3\), exact mean first-passage times, and an excursion/reset representation. Those results **are not claimed new here**. The present claim conditions a return excursion on the rare event of hitting an increasingly deep shell, resolves the first-step entrance mark in three distinct limiting regimes, and obtains its joint independence from the rare-event clock. Neither the published stationary density nor the published unmarked first-passage mean states these conditional mark distributions; the distinction is one of conditioned path mechanism rather than stationary mass. General renewal/exponential rare-event principles explain part of the clock limit; specificity and mathematical value reside principally in the marked three-phase classification.

## Limitations

Only uniform-on-shell-zero initial positions and iid annealed dynamics are covered. The spatial location *inside* the first deep shell and the quenched law conditioned on a particular random driving sequence are not classified. The source's stationary-density threshold \(p=2/3\) and geometric-reset chain are pre-existing; originality is limited to the conditional mark mechanism and its joint clock law. Other unindexed conditional excursion derivations could overlap. The available sources do not justify asserting a new formula for the unmarked mean first-passage time. Independent external mathematical verification and publication-priority review have not been performed.

## References

- J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269v1 (first posted 2023-08-18), subsequently *Chaos* 34, 023128 (2024). https://arxiv.org/abs/2308.09269
- C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, arXiv:2409.19999v2 (first posted 2024-09-30, revised 2025), especially Sections III--V. https://arxiv.org/html/2409.19999v2
- S. Pelikan, *Invariant densities for random maps of the interval*, *Transactions of the American Mathematical Society* 281 (1984), 813--825, doi:10.1090/S0002-9947-1984-0722776-1.
