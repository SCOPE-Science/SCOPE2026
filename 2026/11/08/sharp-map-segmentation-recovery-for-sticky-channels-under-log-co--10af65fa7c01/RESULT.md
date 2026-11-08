# Sharp MAP segmentation recovery for sticky channels under log-convex and log-concave dwell laws

## Finding

Let a known source word \(s=(s_1,\ldots,s_m)\), \(m\ge1\), have \(c\) maximal constant-symbol runs of lengths \(r_1,\ldots,r_c\). Independently repeat every source symbol a random positive integer number of times, with a common strictly positive probability mass function \(a=(a_k)_{k\ge1}\), \(\sum_{k\ge1}a_k=1\); observe the complete replicated word \(Z\) noiselessly, including its length. The estimation target is the entire *source-indexed duration vector*, with the source word supplied to the decoder. Denote the optimum (possibly randomized) exact-recovery probability by \(P^*(s;a)\), averaged over the random output.

**Exact general formula and universal sharp bound.** For every such duration law,

\[
\boxed{P^*(s;a)=\prod_{j=1}^{c}U_{r_j}(a),\qquad
 U_r(a)=\sum_{L=r}^{\infty}\ \max_{\substack{k_i\ge1\\\sum_{i=1}^rk_i=L}}\prod_{i=1}^{r}a_{k_i}.}
\]

In particular, for every word and every strictly positive duration law,

\[
\boxed{P^*(s;a)\ge a_1^{m-c}.}
\]

The bound is *best possible simultaneously for every source word* among all strictly positive laws with the same value \(a_1\): the positive geometric distribution \(a_k=a_1(1-a_1)^{k-1}\) attains it. More generally, **every log-convex positive dwell law** (nondecreasing ratios \(a_{k+1}/a_k\)) attains equality for all source words, regardless of the rest of its tail:

\[
\boxed{P^*(s;a)=a_1^{m-c}\quad\text{for every log-convex positive dwell law}.}
\]

**Contrasting log-concave formula.** If the ratios \(a_{k+1}/a_k\) are nonincreasing, the conditional posterior mode within an observed constant-output run is a *balanced* positive composition, not an extreme one. In this case,

\[
\boxed{U_r(a)=\sum_{u=1}^{\infty}\sum_{v=0}^{r-1}a_u^{\,r-v}a_{u+1}^{\,v},\qquad r\ge1.}
\]

For a strictly log-concave law, meaning \(a_2^2>a_1a_3\), one has \(U_r(a)>a_1^{r-1}\) whenever \(r\ge2\), hence the sharp log-convex value is strictly exceeded as soon as the source contains adjacent equal symbols.

**Source averages and downstream noise.** If \(s\) is instead drawn from a finite-state Markov source with row-vector initial distribution \(\pi\) and transition matrix \(Q\), independent of the durations, then for any log-convex dwell law,

\[
\boxed{\mathbb E_S P^*(S;a)=\pi M^{m-1}{\bf1},\qquad M_{ab}=Q_{ab}a_1^{\mathbf1\{a=b\}}.}
\]

For independent uniform \(q\)-ary symbols, this reduces to \(((q-1+a_1)/q)^{m-1}\). If an observation \(Y\) is obtained from \(Z\) through *any* further stochastic kernel satisfying \(K\to Z\to Y\) conditional on \(s\), the optimal probability from \(Y\) never exceeds \(P^*(s;a)\), with equality attainable in the noiseless case. For log-convex dwell laws, this is a universal sharp noise-independent upper bound of \(a_1^{m-c}\). The lower bound for noiseless observation is **not** asserted for noisy observations.

## Assumptions and scope

The source states are exactly distinguishable in \(Z\); source word and input length are known. Each of the \(m\) source-indexed positive durations is independent with the *same* strictly positive distribution \(a\) on all positive integers. We do not allow deletions or zero-length durations. A maximal run is defined by consecutive equal source symbols, even when the same symbol appears again in a nonadjacent run. When the source has no adjacent equal symbols, every duration is directly observable and exact recovery succeeds with probability one. The conditional law for a particular observed \(Z\) is not generally uniform; uniformity holds for geometric duration laws. A noisy channel may erase additional information but must not leak extra duration-specific side information bypassing \(Z\). All probabilities refer to average zero-one loss for identifying the *full labeled duration vector* and not to decoding an unknown source or estimating its entropy.

## Proof

**Step 1: Exact posterior-maximum mass.** Write the successive maximal input runs as lengths \(r_j\) and their visibly corresponding output runs as lengths \(L_j\). Since every duration is positive and each adjacent input run has a distinct symbol, observing \(Z\) is exactly equivalent, given \(s\), to observing the vector of totals \((L_1,\ldots,L_c)\). Durations for distinct maximal runs are independent. Within an input run with \(r\) source positions and observed total length \(L\), the compatible vectors are exactly the ordered positive compositions \((k_1,\ldots,k_r)\) of \(L\). The *unconditional* mass of a candidate vector is \(\prod_i a_{k_i}\), so the conditional MAP mass times the probability of observing \(L\) is the maximum such product. Summing this identity over every \(L\ge r\) yields \(U_r(a)\), and independence across maximal runs yields the product formula for \(P^*(s;a)\). Since any MAP contribution is bounded by the total mass at that \(L\), each \(U_r\le1\), so the infinite sum converges absolutely.

**Step 2: Universal lower bound and its equality.** Among the positive compositions of \(L\) into \(r\) parts is \((L-r+1,1,\ldots,1)\). Therefore

\[
U_r(a)\ge\sum_{L=r}^{\infty}a_{L-r+1}a_1^{r-1}=a_1^{r-1}.
\]

Multiplying over runs gives \(P^*(s;a)\ge a_1^{\sum_j(r_j-1)}=a_1^{m-c}\). To show equality for log-convex \(a\), suppose two parts of a positive composition have sizes \(2\le i\le j\). The nondecreasing ratio assumption implies

\[
a_i a_j\le a_{i-1}a_{j+1},
\]

because \(a_i/a_{i-1}\le a_{j+1}/a_j\). Iteratively transferring units from any part at least two into another part never reduces the product, and terminates at the extreme composition \((L-r+1,1,\ldots,1)\) up to permutation. Thus the maximum at total \(L\) equals \(a_{L-r+1}a_1^{r-1}\), giving exact equality above. For any specified \(a_1\in(0,1)\), the geometric law \(a_k=a_1(1-a_1)^{k-1}\) is strictly positive, normalized and log-convex (indeed both log-convex and log-concave), establishing the asserted simultaneous sharpness.

**Step 3: Log-concave mode balancing.** If ratios are nonincreasing and two parts satisfy \(i+2\le j\), then

\[
a_i a_j\le a_{i+1}a_{j-1},
\]

because \(a_{i+1}/a_i\ge a_j/a_{j-1}\). Repeated balancing does not reduce a composition's probability and terminates when all parts differ by at most one. For \(L=ur+v\) with integers \(u\ge1\) and \(0\le v<r\), exactly \(v\) parts have size \(u+1\) and the others have size \(u\). Hence the maximum product equals \(a_u^{r-v}a_{u+1}^v\), proving the double-series formula by summing over the disjoint pairs \((u,v)\). If \(r\ge2\) and \(a_2^2>a_1a_3\), compare the balanced composition \((2,2,1,\ldots,1)\) at total \(L=r+2\) with the extreme \((3,1,\ldots,1)\). The former has strictly greater mass, while at every other \(L\) the maximum is at least the extreme mass. Summing gives strict inequality \(U_r>a_1^{r-1}\). All products and sums are finite per observed total, so ties do not affect the argument.

**Step 4: Source law and degradation.** For a log-convex dwell distribution, the fixed-source success equals

\[
a_1^{m-c(s)}=\prod_{i=1}^{m-1}a_1^{\mathbf1\{s_i=s_{i+1}\}}.
\]

Multiplying this factor into the probability of each Markov source path replaces each self-transition \(Q_{aa}\) by \(a_1Q_{aa}\) and leaves every other transition unchanged; summing paths yields \(\pi M^{m-1}{\bf1}\). With iid uniform symbols each row of \(M\) sums to \((q-1+a_1)/q\), yielding its power. Finally, if a decoder observes \(Y\), a decoder given \(Z\) can simulate \(Y\) from its conditional kernel and copy the proposed guess; thus \(Y\) cannot have greater optimal success than \(Z\). No finite-field assumption or asymptotic approximation is needed.

## Verification

The included exact-rational `checker.py` verifies the geometric boundary case by enumerating duration vectors over finite boxes, grouping outputs and checking the maximum probability at each output against the finite-box closed form, along with Markov-path matrix identities. It also checks the universal lower envelope and extremal-composition optimality for a strictly positive log-convex two-geometric mixture and checks the balanced-composition modes for a log-concave positive (factorial-tail) law over finite observed totals. All tests are finite corroboration; the pairwise-transfer and infinite-series proof above establishes the unbounded claims. Execute with `python3 checker.py`.

## Relationship to prior work

McBain and Viterbo, *Information Rate Decomposition for Noisy Nanopore Channels with Geometric Duplication* (arXiv:2606.06808, first public June 5, 2026), give the geometric replication channel and analyze its soft-alignment penalty and **Shannon information rate**, including a noiseless bound. Their full accessible Sections III–VI do not state an all-coordinate exact MAP alignment-recovery law or the log-curvature phase distinction for general dwell distributions. Deriving an entropy penalty is not equivalent to evaluating the maximum posterior **single-vector** probability: conditional expectation of \(-\log P\) and the sum of posterior maxima are different functionals. The formulas here address a known source and a different zero-one estimation objective.

Mitzenmacher, *Capacity Bounds for Sticky Channels* (2008), analyzes sticky/run-length channel capacity for general replication distributions; the inspected full paper does not supply an exact known-source segment-duration MAP probability or the log-convex sharp envelope. Cheraghchi and Ribeiro, *Sharp Analytical Capacity Upper Bounds for Sticky and Related Channels* (arXiv:1806.06218), focuses on capacity. Bouette and collaborators, *Capacity of Additive-Noise Sticky Channels* (arXiv:2608.01433, first public August 2, 2026), focuses on coding capacity; only its abstract was accessible, leaving residual priority risk. Standard pairwise balancing facts for log-convex/log-concave sequences underlie the proof but do not themselves imply the channel-specific posterior factorization, optimal success functional or noise converse without the run-boundary argument.

## Limitations

The source must be supplied to the alignment decoder; the finding is not a source-decoding theorem and does not give an achievable code rate. Independent identically distributed positive dwell durations are essential to the formulas, and strictly positive infinite support is assumed to state the log-curvature dichotomy without support-endpoint complications. Noise is permitted only downstream of the replicated symbol string, not as a timing side channel. No claim is made about exact MAP performance at a specified nonzero noise level or about non-iid dwell times. The possible existence of an equivalent in unindexed papers remains a priority risk; independent mathematical audit is not yet performed.

## References

1. B. McBain and E. Viterbo, *Information Rate Decomposition for Noisy Nanopore Channels with Geometric Duplication*, arXiv:2606.06808, submitted June 5, 2026. https://arxiv.org/abs/2606.06808
2. M. Mitzenmacher, *Capacity Bounds for Sticky Channels*, IEEE Transactions on Information Theory 54 (2008), 72–77. https://www.eecs.harvard.edu/~michaelm/postscripts/stickytemp.pdf
3. M. Cheraghchi and J. Ribeiro, *Sharp Analytical Capacity Upper Bounds for Sticky and Related Channels*, arXiv:1806.06218. https://arxiv.org/abs/1806.06218
4. C. Bouette et al., *Capacity of Additive-Noise Sticky Channels*, arXiv:2608.01433, submitted August 2, 2026. https://arxiv.org/abs/2608.01433
