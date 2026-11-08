# A universal logarithmic law for persistent incompatible contacts in adaptive bounded-confidence networks

## Finding

Consider a finite network in which each edge has a positive sampling weight, and edges are drawn sequentially with probability proportional to their current weights. Fix a nonempty set of **receptive** edges, of size \(g\ge1\), and a (possibly empty) set of **unreceptive** edges, of size \(b\). When drawn, a receptive edge has its weight updated by \(z\mapsto z+\gamma(1-z)\), and an unreceptive edge by \(z\mapsto\delta z\), with all unselected weights unchanged. The categories are fixed. The following sharp asymptotic laws hold almost surely.

For every \(0<\delta<1\) and every unreceptive edge \(e\), its number \(N_e(t)\) of draws during the first \(t\) steps satisfies

\[
\lim_{t\to\infty}\frac{N_e(t)}{\log t}=\frac1{\log(1/\delta)},\qquad
\lim_{t\to\infty}\frac{\log z_e(t)}{\log t}=-1.
\]

In particular, the **total number of wasted (unreceptive) draws** is

\[
\sum_{e\in B}N_e(t)\sim\frac{b\log t}{\log(1/\delta)}
\]

when \(b>0\), while each receptive edge has frequency \(N_e(t)/t\to1/g\). Thus every unreceptive edge is selected infinitely often, but the frequency of all such selections is zero, with an explicit universal leading constant independent of network topology, initial weights, or \(\gamma\).

The two endpoints of the downweighting parameter are different: at \(\delta=0\), each unreceptive edge is drawn exactly once almost surely and then never again; at \(\delta=1\), it is drawn a positive linear fraction of time. The same logarithmic laws hold after a finite, possibly random, time when the receptive/unreceptive classifications become permanently fixed and at least one receptive edge survives.

A two-edge realization gives an exact *finite-time* clock. In the path \(1-2-3\) with initial opinions \((0,0,1)\) and confidence bound \(c\in(0,1]\), edge \(12\) is always receptive and edge \(23\) always unreceptive. Set its initial weights to \(z_{12}(0)=1\) and \(z_{23}(0)=\beta\in(0,1]\). Let \(\tau_n\) be the time of the \(n\)-th draw of edge \(23\). For \(0<\delta<1\),

\[
\begin{aligned}
\mathbb E\tau_n&=n+\beta^{-1}\sum_{k=0}^{n-1}\delta^{-k}
=n+\frac{\delta^{1-n}-\delta}{\beta(1-\delta)},\\
\operatorname{Var}(\tau_n)&=\beta^{-2}\sum_{k=0}^{n-1}\delta^{-2k}
+\beta^{-1}\sum_{k=0}^{n-1}\delta^{-k}.
\end{aligned}
\]

This gives explicit expected clock time, rather than just a contact-count threshold, for suppressing an incompatible tie.

## Assumptions and scope

The edge set \(E\) is finite, with \(m=|E|\ge1\). At time \(t=0,1,\dots\), all weights \(z_e(t)\) lie in \((0,1]\) initially. Exactly one edge is selected per integer step, with conditional probability

\[
\mathbb P(e\text{ selected at step }t\mid\mathcal F_t)=\frac{z_e(t)}{Z_t},\qquad Z_t=\sum_{f\in E}z_f(t).
\]

Every edge is permanently in either \(G\) (receptive) or \(B\) (unreceptive). There is at least one edge in \(G\), so \(g=|G|\ge1\). Upon selecting \(e\in G\), set \(z_e(t+1)=z_e(t)+\gamma(1-z_e(t))\), for \(0<\gamma\le1\); upon selecting \(e\in B\), set \(z_e(t+1)=\delta z_e(t)\), for \(0\le\delta\le1\). All other weights are unchanged. Let \(N_e(t)\) count draws among steps \(0,\ldots,t-1\).

The opinion-dynamics interpretation follows the adaptive-edge Deffuant--Weisbuch model of Thompsky, Wu, Porter, and Luo [1]. It is not assumed that an arbitrary opinion process starts with fixed edge classifications. Instead, the assertion extends to trajectories whose classifications become fixed after a finite time, as explained in the proof. The original paper proves eventual effective-graph stabilization when no limiting neighbor opinion gap equals the confidence bound [1, Theorem 3]. The existence of an eventual receptive edge is an additional hypothesis for the rate law.

## Proof

**1. Uniform denominator and per-draw bounds.** Choose a permanently receptive edge \(f\) and let \(a=z_f(0)>0\). Its weight never decreases, so for every \(t\),

\[
a\le Z_t\le m.
\]

For a fixed unreceptive edge \(e\), after exactly \(k\) of its own selections its weight is \(z_e(0)\delta^k\). During the waiting period until its next selection, the conditional hazard at each step therefore obeys

\[
 c_e\delta^k\le\mathbb P(e\text{ selected next}\mid\mathcal F_t)\le C_e\delta^k,
\qquad c_e=\frac{z_e(0)}m>0,\quad C_e=\frac{z_e(0)}a.
\]

These bounds remain true irrespective of the draws and weight changes of other edges.

**2. Logarithmic clock for \(0<\delta<1\).** At every finite \(k\), the positive lower hazard implies that the next selection occurs almost surely, so all the successive waiting times are finite. Let \(W_k\) be the number of steps elapsed between the \(k\)-th and \((k+1)\)-st selections of \(e\), counting the successful step; \(W_0\) starts at time zero. Conditional on the history when a waiting period starts, the bounds above give, for all sufficiently large \(k\),

\[
\mathbb P\left(W_k<\frac{\delta^{-k}}{k^2}\right)\le\frac{C_e}{k^2},
\qquad
\mathbb P\left(W_k>k^2\delta^{-k}\right)\le\exp(-c_e k^2/2).
\]

For the first inequality, use the union bound over the indicated number of trials; for the second, iterated conditional survival probabilities and a floor/ceiling adjustment yield the displayed harmless factor \(1/2\). Both upper bounds are summable. By the first Borel--Cantelli lemma, almost surely eventually

\[
\frac{\delta^{-k}}{k^2}\le W_k\le k^2\delta^{-k}.
\]

The time \(\tau_n=\sum_{k=0}^{n-1}W_k\) of the \(n\)-th selection therefore satisfies

\[
\lim_{n\to\infty}\frac{\log\tau_n}{n}=\log(1/\delta),
\]

because the final summand gives the lower logarithmic bound and the sum of the first \(n\) upper bounds gives the matching bound up to \(O(\log n)\). Inverting this increasing selection-time sequence proves

\[
\lim_{t\to\infty}\frac{N_e(t)}{\log t}=\frac1{\log(1/\delta)}.
\]

The weight identity \(z_e(t)=z_e(0)\delta^{N_e(t)}\) gives the logarithmic weight limit. Finiteness of \(B\) permits summation over all unreceptive edges.

**3. Receptive-edge frequencies.** Every receptive edge \(f\) is drawn infinitely often because its conditional selection probability is always at least \(z_f(0)/m>0\). Consequently

\[
z_f(t)=1-(1-z_f(0))(1-\gamma)^{N_f(t)}\longrightarrow1.
\]

By step 2, each unreceptive weight tends to zero when \(0<\delta<1\). Hence \(Z_t\to g\) and the conditional sampling probability of each receptive edge tends to \(1/g\). Writing the realized draw indicator as its conditional mean plus a bounded martingale difference, Azuma's inequality and Borel--Cantelli (or the bounded martingale strong law) imply that the empirical selection frequency tends to the limit of those means, namely \(1/g\).

**4. Endpoint regimes.** When \(\delta=0\), each unreceptive edge retains a strictly positive constant weight until it is first drawn. Since its conditional selection probability is then bounded below by \(z_e(0)/m\), it is eventually drawn almost surely; on this first draw its weight becomes zero, ruling out all later draws. When \(\delta=1\), every unreceptive edge keeps its initial weight. Every receptive edge tends to weight one by the previous infinite-draw argument. Write \(H=\sum_{e\in B}z_e(0)\). Conditional selection probabilities converge to \(z_e(0)/(g+H)\) for unreceptive edges and to \(1/(g+H)\) for receptive edges; the martingale strong law gives the same limits for frequencies. Thus the three regimes are genuinely distinct.

**5. Eventually fixed classifications.** For any deterministic integer \(T\) and any fixed edge partition, start a frozen-classification copy at the weights of time \(T\), driven by the same future selection randomness. On the event that the actual process uses precisely that classification at all times after \(T\), the paths of the copy and actual process agree. The frozen proof holds for almost every random state at time \(T\). Taking the finite union over partitions and countable union over \(T\) transfers the result to any almost surely eventually fixed classification with a surviving receptive edge. Finite initial selections do not affect the normalized limits.

**6. Exact two-edge waiting time.** On the three-node path with opinions \((0,0,1)\) and \(c\in(0,1]\), selecting the receptive edge \(12\) never changes the opinions (the two endpoints agree), and selecting \(23\) also never changes them (it is always unreceptive). The former weight stays exactly one. After \(k\) draws of the latter, its weight is \(\beta\delta^k\), and until the next such draw the success probability at each step is constant,

\[
p_k=\frac{\beta\delta^k}{1+\beta\delta^k}.
\]

The successive waiting times \(W_k\) are independent geometric random variables on \(\{1,2,\ldots\}\) with parameters \(p_k\). Thus \(\mathbb E W_k=1/p_k=1+\beta^{-1}\delta^{-k}\), and \(\operatorname{Var}W_k=(1-p_k)/p_k^2=\beta^{-2}\delta^{-2k}+\beta^{-1}\delta^{-k}\). Summing independent means and variances proves the stated exact formulas.

## Verification

A standalone standard-library Python checker (`CHECKER.py`) verifies the two-edge moment formulas in 99 parameter/order combinations and performs 38 further exact rational finite-horizon Markov-chain checks (137 tests total). It confirms in particular, for \(\delta=1/2\) and \(\beta=1\), that \((\mathbb E\tau_1,\operatorname{Var}\tau_1)=(2,2)\), \((\mathbb E\tau_2,\operatorname{Var}\tau_2)=(5,8)\), and \((\mathbb E\tau_3,\operatorname{Var}\tau_3)=(10,28)\). The infinite-time almost-sure law is established by the analytic martingale and Borel--Cantelli argument above, **not** by finite tests.

## Relationship to prior work

Thompsky, Wu, Porter, and Luo [1] introduce exactly these normalized adaptive-edge updates. Their Lemma 1 already proves that all edges are sampled infinitely often, Theorem 2 proves binary limiting weights, and Theorem 3 addresses eventual effective-graph stabilization under a nonboundary hypothesis. These qualitative statements are prior art. The contribution here is a sharp \(\log t\) count of the contacts on a suppressed edge with its exact coefficient, the accompanying complementary linear receptive-edge rates, a complete \(\delta=0\), \(0<\delta<1\), \(\delta=1\) selection-frequency trichotomy, and the exact contact-time distribution structure in a realizable three-agent example. None is claimed to follow solely from the qualitative convergence statement. Other graph-reinforcement models [2,3] study different update mechanisms; they are relevant background, not evidence of an exhaustive novelty search.

## Limitations

The quantitative theorem requires positive initial weights, at least one permanently receptive edge, and the specified normalized sampling and multiplicative downweighting rule. An initially absent edge need never be sampled. When every edge is unreceptive, the denominator lacks a positive lower bound, so the logarithmic law need not hold (one such edge is drawn every step). No opinion convergence rate is asserted; the result counts attempted contacts, including those that leave opinions unchanged. For full changing-confidence dynamics, the rate law is conditional on eventual stabilization with at least one surviving receptive edge. Random or heterogeneous decrease factors, periodically changing classifications, or infinite graphs are not covered. A general-urn equivalence in unindexed prior literature is an originality risk; no independent audit has been undertaken.

## References

[1] L. Thompsky, Y. Y. Wu, M. A. Porter, and J. Luo, *A Bounded-Confidence Model of Opinion Dynamics with Adaptive Interaction Probabilities*, arXiv:2605.20418, first publicly posted 19 May 2026, https://arxiv.org/abs/2605.20418.

[2] G. Caldarelli, A. Chessa, I. Crimaldi, and F. Pammolli, *Weighted networks as randomly reinforced urn processes*, Physical Review E **87**, 020106 (2013), https://doi.org/10.1103/PhysRevE.87.020106.

[3] R. van der Hofstad, M. Holmes, A. Kuznetsov, and W. M. Ruszel, *Strongly reinforced Pólya urns with graph-based competition*, Annals of Applied Probability **26**, 2494–2539 (2016), https://doi.org/10.1214/16-AAP1153.
