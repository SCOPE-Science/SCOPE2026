# Uniform first-detection ranks and stochastic-optimal sentinels on a cycle

## Finding

In a homogeneous susceptible–infected (SI) epidemic on a finite cycle with one uniformly chosen initial case and a prescribed number of continuously monitored sentinel vertices, placing the sentinels with **as equal cyclic spacing as the integers permit** minimizes the time to first detection in the *usual stochastic order*. Placing them consecutively maximizes this time in the same order. The result holds simultaneously at every positive observation time, for every infection rate, and for every nondecreasing loss of detection delay for which the expectation exists. These are exact optimizers, not approximations.

More precisely, let \(n\ge 3\), \(1\le k\le n\), and \(\lambda>0\). Order the \(k\) sentinel vertices cyclically and let \(\ell_1,\ldots,\ell_k\ge1\) be their successive edge distances, so \(\sum_i\ell_i=n\). Let \(T\) be the first time at which a sentinel becomes infected, allowing \(T=0\) when the uniformly selected initial case is a sentinel. Let \(R\) be the number of post-seeding infection events through and including that first detection (so \(R=0\) at immediate detection). Then, for every nonnegative integer \(m\),

\[
\Pr(R>m)=\frac1n\sum_{i=1}^{k}(\ell_i-m-1)_+.
\]

Writing \(u=2\lambda t\), for every \(t\ge0\) the complete continuous-time survival law is

\[
\boxed{\Pr(T>t)=\frac{e^{-u}}n\sum_{i=1}^{k}\sum_{m=0}^{\ell_i-2}(\ell_i-m-1)\frac{u^m}{m!}.}
\]

An inner sum with upper limit below zero is zero, and \(x_+=\max(x,0)\). In particular,

\[
\boxed{\mathbb E T=\frac1{4\lambda n}\sum_{i=1}^k\ell_i(\ell_i-1).}
\]

Write \(n=kq+r\), with integers \(q\ge1\) and \(0\le r<k\). The minimum stochastic-delay law occurs exactly for the multiset of distances consisting of \(k-r\) copies of \(q\) and \(r\) copies of \(q+1\). The maximum occurs exactly for distances \((n-k+1,1,\ldots,1)\), up to permutation. Thus, for every sentinel set \(S\), balanced set \(S_{\mathrm{bal}}\), and consecutive set \(S_{\mathrm{con}}\),

\[
T_{S_{\mathrm{bal}}}\le_{\mathrm{st}}T_S\le_{\mathrm{st}}T_{S_{\mathrm{con}}}.
\]

If the gap multisets are different, the corresponding survival-tail inequality is strict at **every** finite \(t>0\). In the degenerate cases \(k=1\) or \(k=n\), all configurations have the same gap multiset and the assertions reduce to equality. The exact mean extremes are

\[
\min\mathbb ET=\frac{(k-r)q(q-1)+rq(q+1)}{4\lambda n},\qquad
\max\mathbb ET=\frac{(n-k+1)(n-k)}{4\lambda n}.
\]

For example, with \(n=12\) and \(k=3\), equally spaced sentinels have gaps \((4,4,4)\) and mean delay \(3/(4\lambda)\), whereas three consecutive sentinels have gaps \((10,1,1)\) and mean delay \(15/(8\lambda)\). The former also has strictly smaller probability of undetected infection at every \(t>0\), not just a smaller mean.

## Assumptions and scope

The contact graph is the undirected simple cycle \(C_n\), with one individual per vertex. Initially exactly one vertex is infected, uniformly among all \(n\), independently of edge-transmission clocks. Infected individuals never recover; any directed contact across an infected–susceptible edge causes infection at rate \(\lambda\), independently across active edges, in continuous time. Monitoring is instantaneous, perfect and continuous at a fixed nonempty set \(S\) of exactly \(k\) vertices. The process is stopped at the first infected sentinel. Transmissions through different active edges leading to the same individual are independent, so their hazards add (this matters for the final susceptible vertex between two infected neighbors). The sample of initial cases includes sentinels; no transmission is needed if such a case is chosen. These conclusions do not claim robustness to heterogeneous rates, recovery, delayed monitoring, multiple independent seeds, or noncycle graphs.

## Proof

**Step 1: two independent frontier clocks.** Condition on a seed vertex strictly inside one of the \(k\) open arcs between successive sentinels, of edge length \(\ell\). Until detection, infected vertices form a single contiguous interval inside this arc, with exactly two active boundary transmission edges. Each edge has hazard \(\lambda\), even when both edges lead to the same final susceptible vertex. Consequently, the successive event waiting times up to detection are independent \(\operatorname{Exp}(2\lambda)\) random variables. Independently, at each event the left or right frontier fires with probability \(1/2\). An infinite independent sequence of such frontier directions can be generated before the epidemic starts and truncated at detection.

**Step 2: a uniform-rank lemma.** Label the internal vertices of a fixed arc by \(j=1,\ldots,\ell-1\) from its left sentinel. Fix an arbitrary frontier-direction sequence. After \(m\) prescribed events, let \(a\) be the number of leftward events and \(m-a\) the number of rightward events. The initial case at \(j\) has survived all \(m\) events without hitting either sentinel precisely when \(a<j\) and \(m-a<\ell-j\). The number of integer positions \(j\) satisfying both inequalities is exactly \((\ell-m-1)_+\), independent of the chosen direction sequence. Since the seed is uniform among positions in that arc, this proves

\[
\Pr(R>m\mid\text{seed in arc of length }\ell)
=\frac{(\ell-m-1)_+}{\ell-1}\quad(\ell\ge2).
\]

In particular \(R\) is uniform on \(\{1,\ldots,\ell-1\}\) conditional on an internal seed, and its distribution does not depend on the frontier directions. Unconditionally the probability that the seed occupies any specific internal vertex is \(1/n\), yielding the claimed exact rank tail. The \(k\) sentinel seed locations contribute \(R=0\).

**Step 3: passage from event ranks to detection times.** Independently of the stopped direction process, sample successive waiting times \(E_j\sim\operatorname{Exp}(2\lambda)\). Then \(T=\sum_{j=1}^R E_j\). Equivalently, with an independent rate-\(2\lambda\) Poisson process \(N(t)\),

\[
\Pr(T>t)=\Pr\bigl(R>N(t)\bigr)
=e^{-2\lambda t}\sum_{m\ge0}\Pr(R>m)\frac{(2\lambda t)^m}{m!}.
\]

Only ranks through \(n-k\) contribute. Substitution gives the exact tail formula. Integrating the survival tail (or using \(\mathbb E E_j=1/(2\lambda)\)) gives

\[
\mathbb ET=\frac{\mathbb ER}{2\lambda}
=\frac1{2\lambda n}\sum_i\sum_{j=1}^{\ell_i-1}j
=\frac1{4\lambda n}\sum_i\ell_i(\ell_i-1).
\]

**Step 4: pointwise strict discrete convexity.** Set

\[
f_\ell(u)=e^{-u}\sum_{m=0}^{\ell-2}(\ell-m-1)\frac{u^m}{m!}
\quad(\ell\ge1),\qquad f_1(u)=0.
\]

A direct finite difference, with the empty-sum convention, gives for every \(\ell\ge2\)

\[
\boxed{f_{\ell+1}(u)-2f_\ell(u)+f_{\ell-1}(u)
=e^{-u}\frac{u^{\ell-1}}{(\ell-1)!}>0\quad(u>0).}
\]

Indeed, \(f_{\ell+1}-f_\ell=e^{-u}\sum_{m=0}^{\ell-1}u^m/m!\); differencing once more proves the identity. Each \(f_\ell(u)\) is therefore a strictly convex integer sequence in \(\ell\) for \(u>0\). If two positive gaps obey \(a\ge b+2\), replacing them with \((a-1,b+1)\) strictly decreases \(f_a+f_b\). Repeated balancing must terminate exactly at the multiset \(\{q^{k-r},(q+1)^r\}\), and strictly decreases \(\sum_i f_{\ell_i}\) at every nontrivial step. Conversely, if at least two gap lengths exceed one, replacing them with \((a+b-1,1)\) strictly increases the sum (the reverse of a finite balancing sequence). Iterating ends at \((n-k+1,1,\ldots,1)\). Each prescribed positive integer gap vector is realizable by a sentinel set on the cycle. Since \(\Pr(T>t)=n^{-1}\sum_i f_{\ell_i}(2\lambda t)\), the extremizers hold simultaneously for every \(t>0\), with stated strictness. Pointwise tail inequalities are exactly the stated usual stochastic order, and imply the comparison for all increasing delay losses when their expectations exist.

## Verification

The standalone `verify.py` uses only Python's standard library; run `python3 verify.py` from the directory containing this document. It independently enumerates all frontier-direction sequences for arc lengths up to twelve, derives event-rank tails by a separate exact-fraction Markov frontier process on cycles through nine vertices, solves exact-fraction mean-passage recursions through eight vertices, checks all sentinel placements on cycles through ten vertices for pointwise rank-tail optimality, and verifies the Poisson finite-difference coefficients. It completed 50,036 exact assertions. These finite computations verify critical normalizations and boundary cases but do **not** establish the infinite family of cycle sizes; that follows from the four-step proof above.

## Relationship to prior work

Leskovec et al. (2007) formulate network outbreak detection as a sensor-selection problem and prove broad submodularity and approximation guarantees, rather than exact equal-gap stochastic optimization for homogeneous SI transmission on cycles. Christakis and Fowler (2010) study social-network sentinels empirically. Colman et al. (2019) study spatially distributed sentinels using simulated SIR outbreaks; their results support a spatial-distribution heuristic but do not give the present exact SI cycle classification. Batlle et al. (2020) formulate stochastic epidemic test allocation on contact networks, including SI-type models, and use general approximation-oriented methods; their analyzed model and statements do not provide this uniform event-rank lemma or all-time cycle extremal classification. Thus general submodularity and empirical social-sensor results do not imply the present exact strict ordering without additional cycle-specific arguments. These are statement-level comparisons based on the accessible source text; a completely exhaustive historical priority review has not been made.

## Limitations

All comparisons assume uniform initial seeding, equal per-edge infection rates, continuous perfect sensing, one infection source, no recovery, and a simple ring. An arbitrary strictly increasing loss is minimized or maximized by stochastic dominance, but expectations of unbounded losses must exist. Distinct geometric placements with identical ordered or permuted gap multisets can have identical detection laws; the uniqueness claim concerns gap multisets, not labeled positions. The full historical literature on ring-based surveillance has not been exhaustively checked, and scientific priority is provisional. 

## References

1. J. Leskovec, A. Krause, C. Guestrin, C. Faloutsos, J. VanBriesen, and N. Glance, *Cost-effective outbreak detection in networks*, Proceedings of KDD 2007, pp. 420–429, DOI: https://doi.org/10.1145/1281192.1281239. Author-hosted extended technical report (dated June 2007): https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf.
2. N. A. Christakis and J. H. Fowler, *Social Network Sensors for Early Detection of Contagious Outbreaks*, arXiv:1004.4792 (first submitted April 27, 2010), https://arxiv.org/abs/1004.4792.
3. E. Colman, P. Holme, H. Sayama, and C. Gershenson, *Efficient sentinel surveillance strategies for preventing epidemics on networks*, PLOS Computational Biology 15(11), e1007517 (2019), https://doi.org/10.1371/journal.pcbi.1007517.
4. P. Batlle, J. Bruna, C. Fernandez-Granda, and V. M. Preciado, *Adaptive Test Allocation for Outbreak Detection and Tracking in Social Contact Networks*, arXiv:2011.01998 (2020), https://arxiv.org/abs/2011.01998.
