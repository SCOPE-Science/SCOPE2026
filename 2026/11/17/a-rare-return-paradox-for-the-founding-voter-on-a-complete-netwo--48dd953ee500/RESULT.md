# A rare-return paradox for the founding voter on a complete network

## Finding

Let \(n\ge2\), and run the ordinary continuous-time binary voter model on the labelled complete graph \(K_n\), with independent rate-one update clocks at every vertex. At an update a vertex copies one uniformly sampled *other* vertex. Initially a distinguished founder \(v\) alone holds opinion \(1\); all other vertices hold opinion \(0\). Stop at the almost-surely finite global-consensus time \(T_n\). Let \(N_n\) count genuine changes of opinion at \(v\) up to \(T_n\), and let \(U_n\) count changes \(0\to1\) at \(v\).

Then, for every integer \(n\ge2\),
\[
\boxed{\mathbb E N_n=\frac{2(n-1)}{n+2}},\qquad
\boxed{\mathbb E U_n=\frac{(n-1)(n-2)}{2n(n+2)}}.
\]
For every \(n\ge4\) and \(2\le k<n\),
\[
\boxed{\Pr(U_n\ge1)\le\frac1k+\frac{k-1}{2(n-k)}}.
\]
In particular, taking \(k=\lfloor\sqrt n\rfloor\),
\[
\boxed{N_n\xrightarrow[n\to\infty]{\mathsf P}1\quad\text{but}\quad
\mathbb E N_n\longrightarrow2.}
\]
Thus \((N_n)\) is not uniformly integrable. Its excess expectation comes from rare founder-return paths: as \(n\to\infty\),
\[
\boxed{\mathbb E[U_n\mid U_n\ge1]\ge(1/3+o(1))\sqrt n.}
\]
The event \(U_n\ge1\) is precisely the event that the founder, after first abandoning opinion \(1\), later readopts it. No claim is made here that its probability is asymptotic to the displayed upper bound.

## Assumptions and scope

The graph is complete, loopless, undirected and labelled. The update clocks are independent rate-one Poisson processes and copy a uniformly chosen different vertex. An update copying the current opinion is not counted as a flip. The initial condition is exactly one opinion-\(1\) vertex, and the counted vertex is that same founder. The consensus time is finite almost surely on every finite connected graph: from any nonconsensus state a finite sequence of positive-probability updates reaches consensus, and the finite-state chain has no other closed communicating class. The results concern the absorption-stopped path statistics, not the number of attempted updates or the number of updates by all vertices. The bound with \(k\) applies for \(n\ge4\) and integers \(2\le k<n\).

## Proof

**1. An exact two-site occupation calculation.** For distinct labelled vertices \(a,b\), write \(d_{ab}(t)=\Pr(\eta_t(a)\ne\eta_t(b))\). By symmetry among the nonfounders there are two disagreement probabilities: \(d_1(t)\) for a pair containing \(v\), and \(d_2(t)\) for two nonfounders. Their initial values are \(d_1(0)=1\) and \(d_2(0)=0\). Conditional on a copying event at either endpoint, replace that endpoint by the chosen neighbor; this gives, for \(n\ge3\),
\[
\begin{pmatrix}d_1'\\d_2'\end{pmatrix}
=\frac{1}{n-1}\begin{pmatrix}-n&n-2\\2&-4\end{pmatrix}
\begin{pmatrix}d_1\\d_2\end{pmatrix}.
\]
Both functions tend to zero because consensus is attained. Write \(A=\int_0^\infty d_1(t)\,dt\) and \(B=\int_0^\infty d_2(t)\,dt\). Integrating the two equations yields
\[
-nA+(n-2)B=-(n-1),\qquad 2A-4B=0,
\]
so \(B=A/2\) and \(A=2(n-1)/(n+2)\). At any instant the instantaneous genuine-flip rate of \(v\) is the fraction of its neighbors with the opposite opinion, whose expectation is \(d_1(t)\). Tonelli's theorem therefore gives \(\mathbb E N_n=A\). For \(n=2\), the two vertices disagree until the first successful copy, which occurs at total rate two, and \(v\) changes with probability one-half. The same formula gives \(1/2\).

**2. Upward changes.** Let \(D_n\) count changes \(1\to0\) at \(v\). Since the founder begins in opinion \(1\), the pathwise identity is
\[
D_n-U_n=1-\eta_{T_n}(v),\qquad N_n=D_n+U_n.
\]
The overall number of opinion-\(1\) vertices is a bounded martingale (each \(0\to1\) rate equals the \(1\to0\) rate). Consequently the probability of ultimate all-\(1\) consensus, starting with one opinion-\(1\) vertex, is \(1/n\). Taking expectations and solving gives
\[
\mathbb E U_n=\tfrac12\bigl(\mathbb E N_n-1+1/n\bigr)=\frac{(n-1)(n-2)}{2n(n+2)}.
\]

**3. Bounding the probability of *any* return.** Write \(I_t\) for the number of opinion-\(1\) vertices. On states \(1\le i\le n-1\) this is a continuous-time birth-and-death chain with *equal* upward and downward rates
\[
b_i=\frac{i(n-i)}{n-1}.
\]
Fix an integer \(2\le k<n\), and let \(\tau\) be its first visit to \(0\) or \(k\), starting from \(I_0=1\). The gambler's-ruin harmonic function gives \(\Pr(I_\tau=k)=1/k\). On the interior \(0<i<k\), define the nonnegative potential
\[
g(i)=\frac{n-1}{2(n-k)}i(k-i),\qquad g(0)=g(k)=0.
\]
The generator \(\mathcal L\) of \(I_t\) satisfies
\[
(\mathcal Lg)(i)=-\frac{i(n-i)}{n-k}\le-i.
\]
Dynkin's formula (first with bounded stopping, then by monotone convergence) therefore implies
\[
\mathbb E\int_0^\tau I_t\,dt\le g(1)=\frac{(n-1)(k-1)}{2(n-k)}.
\]
Before \(\tau\), the rate at which \(v\) makes a \(0\to1\) change is at most \(I_t/(n-1)\). Markov's inequality for its counting process, followed by the possibility that \(I_t\) first reaches \(k\), proves
\[
\Pr(U_n\ge1)\le\frac{k-1}{2(n-k)}+\frac1k.
\]
This bound concerns *the entire future*, not only an arbitrary fixed time horizon, because if \(I_t\) hits zero then no upward founder change can occur later.

**4. Typical count and rare-event excess.** Because the founder starts at opinion \(1\), two or more of its genuine flips necessarily include at least one \(0\to1\) flip. Also, \(N_n=0\) implies eventual all-\(1\) consensus, an event with probability \(1/n\). Hence
\[
\Pr(N_n\ne1)\le\frac1n+\frac1k+\frac{k-1}{2(n-k)}.
\]
With \(k=\lfloor\sqrt n\rfloor\), this tends to zero, proving convergence in probability to one. But Step 1 gives the limiting mean two, so the nonnegative family cannot be uniformly integrable. Since \(U_n=0\) outside the rare-return event,
\[
\mathbb E[U_n\mid U_n\ge1]=\frac{\mathbb E U_n}{\Pr(U_n\ge1)}
\ge\frac{(n-1)(n-2)}{2n(n+2)}\left(\frac1k+\frac{k-1}{2(n-k)}\right)^{-1},
\]
which is \((1/3+o(1))\sqrt n\) or larger with that choice of \(k\). This completes the proof.

## Verification

A standalone independent labelled-state generator in `verification/check_founder.py` solves the complete transient linear system for the expected marked-vertex flip count and a separate killed-chain system for the probability of zero flips. For each \(n=2,\ldots,9\), the direct full-state flip expectation agrees numerically with the first boxed formula to better than \(10^{-10}\). An independent two-variable aggregation checks the probability of any upward founder flip for \(n=3,\ldots,17\) and confirms the proven finite-size upper bound. The zero-flip cross-check uses a separately derived Laguerre recurrence solely as an independent numerical benchmark; neither that old persistence formula nor the finite experiments are needed to prove the new theorem. The captured output is `verification/check_founder.out`; execute `python verification/check_founder.py` with NumPy and SciPy installed. The analytic argument, not finite testing, establishes every \(n\).

## Relationship to prior work

Ben-Naim, Frachebourg and Krapivsky (1995/1996) studied voter-model opinion-change distributions and mean-field persistence, including unequal initial concentrations. Their treatment of infinite-volume and time-dependent statistics does not state the absorption-stopped founder-flip mean/concentration discrepancy above. Pickering and Lim (2014/2015) obtained exact complete-graph *population-count* propagators and macrostate occupation times; those do not themselves distinguish a named initial dissenter's return changes. Sood, Antal and Redner (2007/2008) established degree-weighted fixation probabilities; the \(1/n\) winning probability used here is classical. The separately published study *Exact hub persistence on clique bouquets and its size-biased blade law* contains an exact probability that a founding hub never changes until consensus, including the complete-graph specialization: this **covers the zero-flip probability**, which is expressly not claimed as new here. It does not report the present contrast between convergence in probability of the tagged flip count to one and a limit-two expectation, or the rare-return conditional lower bound. The tools used (generator identities, gambler's ruin, and Dynkin's formula) are standard; their combination and the singular absorption-stopped founder result constitute the new claim. Priority remains qualified by the possibility of older analyses of tagged-site flips not located in the inspected literature.

## Limitations

No full distribution of \(N_n\) or exact asymptotic constant for \(\Pr(U_n\ge1)\) is proved. The \(O(n^{-1/2})\) upper bound is not asserted optimal. The finite-n mean alone cannot establish the rare-return concentration statement; both are needed. The convergence is for the single-dissenter initial state and standard equal-rate copying on the complete graph, not for generic densities, arbitrary graphs or modified update rules. Self-review is not independent mathematical validation.

## References

1. E. Ben-Naim, L. Frachebourg, P. L. Krapivsky, *Coarsening and Persistence in the Voter Model*, arXiv:cond-mat/9511040v1, public 1995-11-08; *Phys. Rev. E* 53 (1996) 3078–3087. https://arxiv.org/html/cond-mat/9511040v1
2. W. Pickering and C. Lim, *Solution of the Voter Model by Spectral Analysis*, arXiv:1408.2130, public 2014-08-09; *Phys. Rev. E* 91 (2015) 012812. https://arxiv.org/abs/1408.2130
3. V. Sood, T. Antal, S. Redner, *Voter Models on Heterogeneous Networks*, arXiv:0712.4288v1, public 2007-12-27; *Phys. Rev. E* 77 (2008) 041121. https://arxiv.org/abs/0712.4288
4. *Exact hub persistence on clique bouquets and its size-biased blade law*, published mathematical research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-hub-persistence-on-clique-bouquets-and-its-size-biased-bla--dd79e6859dc0
