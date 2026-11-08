# A unique endpoint transition in two-source continuous-time path contagion

## Finding

For the irreversible continuous-time SI process on an undirected path \(P_n\) with \(n\ge 2\), let every infected-to-susceptible edge transmit at rate \(\lambda>0\), independently. Choose exactly two distinct vertices \(1\le x<y\le n\) to be infected at time zero. For any fixed deadline \(t>0\), write \(s=\lambda t\), \(L=x-1\), \(M=y-x-1\), \(R=n-y\), and
\[
 Q_j(u)=\Pr\{\operatorname{Poisson}(u)\ge j\}
 =1-e^{-u}\sum_{a=0}^{j-1}\frac{u^a}{a!},\qquad Q_0(u)=1.
\]
Then the exact probability of full infection by time \(t\) is
\[
 \boxed{\Pr_{x,y}\{\tau_{\rm full}\le t\}=Q_L(s)Q_R(s)Q_M(2s).}
\]
Every globally maximizing pair is obtained by allocating \(n-2\) units among three strictly decreasing marginal sequences
\[
 \ell_j(s),\quad\ell_j(2s),\quad\ell_j(s),\qquad
 \ell_j(u)=\log\frac{Q_j(u)}{Q_{j-1}(u)},\quad j\ge1,
\]
choosing the \(n-2\) largest marginal values with allowable ties. An exact three-way merge uses \(O(n)\) marginal comparisons and yields a globally optimal seed pair.

The endpoint pair \(\{1,n\}\) is uniquely optimal at every positive deadline when \(2\le n\le4\). For every \(n\ge5\), there is exactly one \(s_n\in(0,\infty)\) satisfying
\[
 \boxed{Q_{n-2}(2s_n)=Q_{n-3}(2s_n)(1-e^{-s_n}).}
\]
The endpoint pair is **not optimal** for \(0<s<s_n\), is **uniquely optimal** for \(s>s_n\), and at \(s=s_n\) the complete set of optimizing pairs is precisely \(\{1,n\}\), \(\{2,n\}\), and \(\{1,n-1\}\). In particular, the five-vertex critical time is \(s_5=2.728771444704983\ldots\), with optimum seeds \(\{2,5\}\) and \(\{1,4\}\) at \(s=1\), but endpoints \(\{1,5\}\) at \(s=4\).

## Assumptions and scope

The path is finite and connected. Seeds are placed simultaneously and are permanently infected. Each infected-susceptible edge triggers infection at constant rate \(\lambda\) while exposed; events from distinct edges are independent Poisson processes. Infection is irreversible, with no outside introductions, recovery, or depletion of the transmission rate. Completion means **all** vertices have become infected by the fixed deadline. The result optimizes this full-coverage probability, not the expected number infected by that deadline, and not the expected completion time.

## Proof

**1. Three independent front processes.** The left exterior segment consists of \(L\) susceptible vertices and one infection front, so its time to completion has an Erlang distribution of shape \(L\) and rate \(\lambda\). Similarly the right exterior has shape \(R\) and rate \(\lambda\). Between the two seeds, if \(M>0\) susceptible vertices remain, there are always exactly two exposed infected-susceptible edges until no susceptible vertex remains. By memorylessness, successive interior infections occur after independent exponential holding times of rate \(2\lambda\), giving an Erlang distribution of shape \(M\) and rate \(2\lambda\). For a zero gap the corresponding completion time is zero. The disjoint-edge Poisson clocks yield independence between the three segment-completion times. Thus their maximum is the global completion time, and the Erlang/Poisson-tail identity proves the displayed product formula.

**2. Strictly decreasing gap increments.** For \(u>0\), put \(w_j=e^{-u}u^j/j!\). The conditional failure hazard in the upper tail is
\[
 \frac{w_j}{Q_j(u)}=
 \left[\sum_{r=0}^{\infty}
 \frac{u^r}{(j+1)(j+2)\cdots(j+r)}\right]^{-1},
\]
where the empty product is one. Every nonconstant summand in brackets decreases strictly with \(j\); consequently \(w_j/Q_j(u)\) increases strictly with \(j\). Since \(Q_{j+1}(u)/Q_j(u)=1-w_j/Q_j(u)\), the consecutive log differences \(\ell_j(u)\) are strictly decreasing with \(j\). Decomposing \(\log\Pr\{\tau_{\rm full}\le t\}\) into the first \(L\), \(M\), and \(R\) increments in the three sequences, with \(L+M+R=n-2\), makes selection of the largest \(n-2\) values necessary and sufficient. Each selected set is a prefix because its sequence is strictly decreasing. Ties across different sequences give all possible maximizers; a three-pointer merge is globally optimal.

**3. Endpoint criterion.** At \(\{1,n\}\), the gaps are \((L,M,R)=(0,N,0)\) for \(N=n-2\). Because interior increments decrease strictly, the only potentially improving first exchange replaces its smallest retained increment \(\ell_N(2s)\) by one of the two unused outer increments \(\ell_1(s)\). Therefore endpoints maximize if and only if \(\ell_N(2s)\ge\ell_1(s)\), which is exactly \(Q_N(2s)\ge Q_{N-1}(2s)(1-e^{-s})\). Strict inequality makes endpoints unique. At equality, strict within-sequence decreases ensure that only the stated three allocations can tie.

**4. Exactly one positive crossing.** For \(N\ge1\), set \((N)_0=1\) and \((N)_k=N(N+1)\cdots(N+k-1)\). The sign of the endpoint comparison is the sign of
\[
 H_N(s)=\sum_{k=0}^{\infty}\frac{(2s)^k}{(N)_k}-e^s
 =\sum_{k=1}^{\infty}\frac{s^k}{k!}
 \left(\frac{2^k k!}{(N)_k}-1\right).
\]
Indeed, \(Q_{N-1}(2s)=e^{-2s}(2s)^{N-1}/(N-1)!\sum_{k\ge0}(2s)^k/(N)_k\), and direct subtraction gives the same sign. Let \(r_k=2^k k!/(N)_k\). Then \(r_0=1\) and \(r_k/r_{k-1}=2k/(N+k-1)\). For \(N=1\), all nonconstant coefficients are positive; for \(N=2\), the linear coefficient is zero and all subsequent coefficients are positive. For \(N\ge3\), \(r_1<1\), the sequence first decreases and then increases without bound, so the nonzero coefficients of \(H_N\) have **one sign change, from negative to positive**. Let \(m\) be the last index with a negative coefficient. The function \(H_N(s)/s^m\) is strictly increasing for positive \(s\): negative terms of degree less than \(m\) increase, the negative degree-\(m\) term is constant, and all positive terms have degree greater than \(m\) and increase. It starts negative and tends positive, because \(\sum_{k\ge0}(2s)^k/(N)_k=e^{2s}Q_{N-1}(2s)(N-1)!/(2s)^{N-1}\), which eventually dominates \(e^s\). Hence there is exactly one positive root for \(N\ge3\), with the asserted strict regimes. The cases \(n=2,3,4\) follow from \(N=0,1,2\) directly.

## Verification

Run `python3 verify_deadline.py` in the same folder. The standard-library script independently computes exact finite-state infection dynamics by transient continuous-time Markov-chain uniformization (for small paths), compares with the three-factor expression, exhaustively checks the global optimizer for a large finite grid, and checks the coefficient-sign lemma and the endpoint regimes. These are finite regression tests, not a replacement for the preceding arguments.

## Relationship to prior work

Fill and Pemantle's treatment of first-passage percolation and Richardson's model establishes the irreversible Poisson-edge spreading setting and its reduction to exponential passage times on the hypercube, without the inspected two-source path deadline placement classification. Kempe, Kleinberg and Tardos study optimization of *eventual* influence in cascade models, which is not the same random-time full-coverage objective; their general submodularity approximation theorems do not state the sharp endpoint transition. Van de Bovenkamp and Van Mieghem study finite-network SIS spreading times and metastability, rather than irreversible SI complete-coverage probabilities. The new content here is the exact deadline law, the all-size optimal placements, and the uniqueness of the deadline-driven endpoint crossover; the elementary idea of allocating gap units by decreasing rewards is not claimed independently novel.

## Limitations

The theorem is for homogeneous exponential clocks on paths and exactly two simultaneous seeds. It does not cover heterogeneous edge rates, reinfection, finite recovery, adaptive seeding, non-path networks, or minimizing the expectation of completion time. The historical-priority comparison is based on the inspected texts and searches, not an exhaustive proof of novelty. The first-passage literature is extensive; a previously published special-case placement result could remain undiscovered. The numerical critical value is illustrative; uniqueness and all-parameter scope follow from the analytical proof.

## References

- J. A. Fill and R. Pemantle, *Percolation, first-passage percolation, and covering times for Richardson's model on the n-cube*, arXiv:math/0404015v1 (public 2004-04-01), https://arxiv.org/abs/math/0404015 .
- D. Kempe, J. Kleinberg and É. Tardos, *Maximizing the Spread of Influence through a Social Network*, KDD 2003, DOI: 10.1145/956750.956769; expanded full-text version, *Theory of Computing* 11 (2015), DOI: 10.4086/toc.2015.v011a004, https://dokk.org/library/theoryofcomputing_v011a004 .
- R. van de Bovenkamp and P. Van Mieghem, *Time to Metastable State in SIS Epidemics on Graphs*, SITIS 2014 proceedings (2015), DOI: 10.1109/SITIS.2014.82, https://research.tudelft.nl/en/publications/time-to-metastable-state-in-sis-epidemics-on-graphs/ .
