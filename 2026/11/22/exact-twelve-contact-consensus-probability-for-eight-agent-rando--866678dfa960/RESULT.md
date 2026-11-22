# Exact twelve-contact consensus probability for eight-agent random gossip

## Finding

**Theorem (exact shortest-horizon probability).** Let eight labelled agents have initial real opinions \(a_0,\ldots,a_7\). At each integer time choose one of the \(\binom82=28\) unordered distinct agent pairs uniformly and independently, and replace both opinions by their arithmetic mean. Assume the initial opinions are in general position: if integer coefficients \(c_i\) satisfy \(\sum_i c_i=0\) and \(\sum_i c_i a_i=0\), then all \(c_i=0\). Write \(T\) for the first time at which all opinions coincide. Then \(T\ge 12\), and

\[
\boxed{\Pr(T=12)=\frac{2,528,870,400}{28^{12}}=\frac{225}{20,661,046,784}.}
\]

Exactly \(2,528,870,400\) of the \(28^{12}\) ordered twelve-pair sequences achieve consensus at their twelfth event. In particular, the probability is approximately \(1.08900581056\times10^{-8}\). No conditional probabilities, grouped pair events or symmetry-quotient weights enter this count.

The lower bound of twelve events and existence of such shortest schedules are established in prior work. The contribution here is the exact **number and probability** of shortest schedules, together with a self-contained finite counting certificate.

## Assumptions and scope

The network is the complete graph on eight labelled nodes. Each event chooses a *single* unordered pair, uniformly from all 28 pairs, with replacement between events. The two endpoints update simultaneously to their pre-event arithmetic mean. All arithmetic is exact. The general-position condition excludes accidental earlier consensus caused by special initial opinions; it is satisfied for Lebesgue-almost-every initial real vector. The theorem concerns the probability of first exact consensus at **the minimum possible number of events**, not the full hitting-time distribution, asynchronous communication delays, noisy/weighted averaging, or approximate consensus.

Let \(M_t\) be the product of the first \(t\) symmetric doubly stochastic pair-averaging matrices, with \(M_0=I\); write \(p_i(t)\) for its \(i\)-th row. Conservation of the total mean and the general-position assumption imply that the opinions first agree exactly when \(M_t=J/8\), where \(J\) is the all-ones matrix. Thus every successful schedule is characterized independently of the numerical values of the initial opinions.

## Proof

**1. A sharp entropy bound and rigidity.** Define \(H(p)=-\sum_jp_j\log_2p_j\) for a probability row vector, with \(0\log_20=0\), and \(\mathcal H(t)=\sum_{i=0}^{7}H(p_i(t))\). Initially \(\mathcal H(0)=0\). Averaging two rows \(p,q\), producing two copies of \(r=(p+q)/2\), increases the row-entropy sum by

\[
2H(r)-H(p)-H(q)=2\,\operatorname{JS}(p,q)\le 2.
\]

Here the Jensen–Shannon divergence \(\operatorname{JS}(p,q)\le1\) because it equals the information gained about an equiprobable choice between \(p\) and \(q\) upon sampling from the resulting mixture. Equality holds if and only if the supports of \(p\) and \(q\) are disjoint. At consensus all rows are the uniform distribution on eight labels and \(\mathcal H(T)=8\log_2 8=24\). Therefore \(T\ge12\). If \(T=12\), every single update must attain equality, and the two rows averaged at every update have disjoint supports.

**2. A complete characterization of shortest schedules.** Work backward from the twelve-step consensus matrix. Its rows are uniform on the full eight-element support. If an update from disjointly supported probability rows \(p,q\) produces uniform \(r\) on a set \(S\), then \(p+q=2r\) with disjoint supports. Hence \(p\) and \(q\) are uniform on complementary equal-cardinality halves of \(S\). All untouched rows stay uniform on their own supports. Applying this argument inductively backward through the twelve equal-entropy steps proves that every row at every intermediate time is the uniform probability distribution on some support, and a pair can be used at an equality step precisely when the two supports are disjoint and have equal size.

Conversely, starting from eight singleton supports, any twelve contacts each joining two disjoint equal-sized supports, and replacing both by the union, increase \(\mathcal H\) by exactly two bits per event. After twelve events the total entropy is 24, its maximum. Since every individual row entropy is at most three, all eight must be uniform on all eight labels, giving exact consensus. Consequently the support-mask rule is necessary and sufficient for a shortest sequence; it excludes both redundant contacts and nonuniform rows.

**3. Finite exact enumeration.** Represent the support of each row by an eight-bit integer mask \(s_i\); initially \(s_i=2^i\). A state is the ordered tuple \(s=(s_0,\ldots,s_7)\). For each \(0\le i<j<8\) satisfying

\[
\operatorname{popcount}(s_i)=\operatorname{popcount}(s_j),
\qquad s_i\mathbin{\&}s_j=0,
\]

form \(F_{ij}(s)\) by replacing both masks by their bitwise union. Let \(C_0((1,2,4,8,16,32,64,128))=1\) and zero otherwise. Define exactly, for \(t=0,\ldots,11\),

\[
C_{t+1}(u)=\sum_{s}\,C_t(s)\sum_{0\le i<j<8}
\mathbf1\big[\text{the mask rule holds at }(s,i,j),\ F_{ij}(s)=u\big].
\]

All sums range over finite ordered 8-tuples of masks; the recurrence performs exact nonnegative integer arithmetic. Thus each ordered contact sequence contributes exactly one count, without a hidden factor of \(2\), \(8!\), or a choice among equivalent states. At depth 12 there is precisely one reachable state, the all-full-mask state \((255,\ldots,255)\), with multiplicity \(2,528,870,400\). Dividing by the \(28^{12}\) equally probable contact sequences proves the theorem.

The complete state-count and path-count profile appears in the verification section; the executable exact recurrence is given in `verify.py`.

## Verification

Running `python3 verify.py` requires only the Python 3 standard library. It uses (i) forward integer path-count propagation over all reachable ordered support-mask states, (ii) a separate memoized suffix-count recursion over the same mathematically proved transition graph, and (iii) exhaustive direct rational-matrix simulation of all \(6^4=1296\) unrestricted four-agent four-contact words as a small independent model check. The forward and suffix recurrences independently return \(2,528,870,400\), and the four-agent brute-force baseline returns 24 successful words (probability \(1/54\)), matching the published value.

| Contacts \(t\) | Reachable mask states | Valid prefixes |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 28 | 28 |
| 2 | 210 | 420 |
| 3 | 1260 | 4200 |
| 4 | 5215 | 44520 |
| 5 | 13020 | 312480 |
| 6 | 18690 | 1683360 |
| 7 | 44520 | 9636480 |
| 8 | 94115 | 51408000 |
| 9 | 45920 | 190955520 |
| 10 | 44100 | 776724480 |
| 11 | 560 | 2528870400 |
| 12 | 1 | 2528870400 |

The finite algorithm is exhaustive because the entropy-rigidity argument proves that **every** shortest solution corresponds to exactly one path through the transition graph. The implementation is a reproducibility aid; the mathematical justification that no other paths exist is the entropy/support proof above, not an extrapolation from computation.

## Relationship to prior work

Shi, Li, Johansson and Johansson (arXiv:1206.0992, first posted 2012-06-05) establish the power-of-two criterion and the sharp \(n\log_2n\) node-update minimum for symmetric gossip. The conference version at MTNS 2014 gives the same network problem and explicitly assigns operations-research network classification 90B10. These sources cover **minimum length**, not the number of uniformly random shortest contact words for eight agents. The present proof accepts the classical minimum as background but also independently reproves its eight-agent specialization via entropy.

Krapivsky and Plakhov (arXiv:2509.01024, first posted 2025-08-31) study this same independent, uniform, unordered-pair compromise process. Their Section IV identifies the minimal-horizon hitting probability \(\mu_k\) as a natural problem, states that \(\mu_k\) was known only through \(k=2\), and computes \(\mu_2=1/54\) for four agents. Here the eight-agent result supplies the next case \(\mu_3\). No statement about the complete eight-agent hitting-time distribution follows.

## Limitations

The result is an exact finite case for eight agents, not an all-size closed formula. It assumes ideal arithmetic and general-position initial opinions; degenerate inputs can reach equality earlier. The tiny probability quantifies a rare fastest sequence, not a typical convergence time or an accuracy guarantee. Algorithmic enumeration is tractable for eight agents but the method is not claimed efficient at sixteen agents. A non-exhaustive literature and index search cannot prove publication priority; an unindexed equivalent enumeration could exist.

## References

1. G. Shi, B. Li, M. Johansson and K. H. Johansson, *Finite-time Convergent Gossiping*, arXiv:1206.0992, first public version 2012-06-05; https://arxiv.org/abs/1206.0992 .
2. G. Shi, B. Li, M. Johansson and K. H. Johansson, *When Do Gossip Algorithms Converge in Finite Time?*, MTNS 2014; https://people.kth.se/~kallej/papers/multiagent_mtns14.pdf .
3. P. L. Krapivsky and A. Yu. Plakhov, *Finite-time consensus in a compromise process*, arXiv:2509.01024, first public version 2025-08-31, especially Section IV; https://arxiv.org/abs/2509.01024 .
