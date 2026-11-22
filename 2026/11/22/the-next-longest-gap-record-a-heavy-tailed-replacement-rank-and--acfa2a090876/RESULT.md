# The next longest-gap record: a heavy-tailed replacement rank and an explicit drop law

## Finding

Consider independent points sampled uniformly, one at a time, on a circle of circumference one. Let \(L_n\) be the largest of the \(n\) cyclic spacings after the first \(n\ge2\) points. Almost surely all initial spacings are distinct. Write \(G_{n,(1)}>\cdots>G_{n,(n)}\) for those **original** spacings in decreasing length order, and let
\[
W_n=\min\{r\ge1:L_{n+r}<L_n\}.
\]
At that time let \(K_n\in\{1,\ldots,n\}\) be the original length-rank of the parent spacing that contains the new longest gap: all later split fragments retain the rank of their parent spacing at time \(n\). Such a rank is almost surely unique. Put \(D_n=n(L_n-L_{n+W_n})\).

**Theorem.** As \(n\to\infty\), jointly on \(\mathbb R_+\times\mathbb N\times\mathbb R_+\),
\[
\left(\frac{\log n}{n}W_n,K_n,D_n\right)\ \Longrightarrow\ (T,K,Y).
\]
Here \(E_1,E_2,\ldots\) and \(Z_1,Z_2,\ldots\) are two independent collections of i.i.d. rate-one exponential variables, and
\[
T=E_1,\qquad K=\min\{k\ge2:E_k>E_1\},\qquad Y=\sum_{j=1}^{K-1}\frac{Z_j}{j}.
\]
The variable \(K\) is finite almost surely, but has infinite mean. More explicitly, for every integer \(k\ge2\),
\[
\Pr(K=k)=\frac1{k(k-1)},\qquad \Pr(K>k)=\frac1k,
\]
and, conditionally on \(K=k\), \(Y\) has the law of the maximum of \(k-1\) independent rate-one exponential variables. For \(y>0\),
\[
\Pr(Y\le y)=1-\frac{y}{e^y-1},\qquad
\Pr(Y>y)=\frac{y}{e^y-1},\qquad
\mathbb E Y=\frac{\pi^2}{6}.
\]
The distribution function at \(y=0\) is zero, by continuous extension. The waiting-time limit \(T\) and the replacement rank \(K\) are **not** independent: for every \(t>0\) and integer \(k\ge2\),
\[
\Pr(K=k\mid T=t)=e^{-t}(1-e^{-t})^{k-2}.
\]
The exponential gap-difference variables \((Z_j)\) are independent of the entire pair \((T,K)\). No claim about convergence of the finite-sample expectations \(\mathbb E D_n\) is needed for this theorem.

## Assumptions and scope

The sample points are i.i.d. uniform with respect to arclength on a *unit circle* and are inserted sequentially, without resampling or moving previous points. All limits are as the initial number of points \(n\) tends to infinity; there is no additional free geometric or stochastic parameter. Rank always refers to the original list of \(n\) spacings, not to the ranks after intermediate insertions. The probability measure is unconditional over both initial locations and future insertions. The theorem concerns the **first strict decrease after a specified large initial sample**, not the entire process of successive record increments.

## Proof

**1. Initial exponential representation and near-equal leading gaps.** The unordered cyclic gaps of \(n\) uniform points have the Dirichlet distribution with all parameters equal to one. Thus, if \(V_1,\ldots,V_n\) are i.i.d. rate-one exponentials, \(S_n=\sum_iV_i\), and \(V_{[1]}>\cdots>V_{[n]}\) are their decreasing order statistics, then
\[
(G_{n,(1)},\ldots,G_{n,(n)})\ \stackrel{\mathrm d}=\ (V_{[1]},\ldots,V_{[n]})/S_n.
\]
For each fixed \(m\), the law of large numbers and standard exponential maximum bounds imply
\[
S_n/n\to1,\quad V_{[j]}/\log n\to1\ (1\le j\le m)
\]
in probability. The memoryless property also gives the exact independent descending-spacing representation
\[
Z_{j,n}:=j(V_{[j]}-V_{[j+1]})\ \stackrel{\mathrm{ind}}\sim\ \operatorname{Exp}(1),
\quad 1\le j<n.
\]
Consequently the finite vector \(\big(n(G_{n,(1)}-G_{n,(k)})\big)_{2\le k\le m}\) converges to \(\big(\sum_{j<k}Z_j/j\big)_{2\le k\le m}\), and
\[
G_{n,(j)}\sim\frac{\log n}{n}\quad(1\le j\le m),\qquad
\max_{1\le i\le m}\big(G_{n,(i)}-G_{n,(m)}\big)=O_{\Pr}(1/n).
\]
The limiting \(Z_j\)'s can be chosen independent of the future insertion process.

**2. Independent first-hit clocks.** Poissonize the future point arrivals using a rate-one Poisson process on the unit circle. The ordered spatial marks of this process are i.i.d. uniform, so the first-record state agrees with the original discrete-time experiment. Conditional on the original spacings, independent thinning produces first-hit times \(\tau_{i,n}\) of original gap rank \(i\), which are independent exponentials of rates \(G_{n,(i)}\). Equivalently, with auxiliary independent rate-one exponentials \(E_i\), independent of the initial spacings,
\[
\tau_{i,n}=\frac{E_i}{G_{n,(i)}}.
\]
Until original gap rank one is hit, it stays intact and is strictly longer than every other gap or fragment, so the next strict record time is exactly \(\tau_{1,n}\). For each fixed \(m\), jointly with the initial normalized gaps,
\[
\left(\frac{\log n}{n}\tau_{i,n}\right)_{i=1}^m\ \Longrightarrow\ (E_i)_{i=1}^m.
\]
Let \(W_n\) be the number of marks up to and including this first hit. Given \(\tau_{1,n}\) and the original gaps, the non-first-gap marks form a Poisson variable with mean \((1-G_{n,(1)})\tau_{1,n}\), independent of the rank-one first hit. Hence
\[
W_n=1+\operatorname{Pois}\big((1-G_{n,(1)})\tau_{1,n}\big)
\]
conditionally in distribution. Since \(\tau_{1,n}=O_{\Pr}(n/\log n)\) and \(G_{n,(1)}=O_{\Pr}(\log n/n)\), conditional mean and variance bounds show
\[
\frac{\log n}{n}(W_n-\tau_{1,n})\to0\quad\text{in probability}.
\]
This proves the exponential waiting-time coordinate jointly with any fixed collection of first-hit indicators.

**3. Uniform elimination of damaged leading gaps.** Fix \(m\ge2\). Let \(A_{n,m}\) be the event that some original rank \(i\in\{2,\ldots,m\}\) remains untouched by time \(\tau_{1,n}\). Whenever \(A_{n,m}\) occurs, there is an intact gap of length at least \(G_{n,(m)}\). A damaged original gap ranked greater than \(m\) can never exceed this length. For a hit gap of original rank \(i\le m\), consider its **first** inserted point. Its relative position \(U_i\) is uniform on \((0,1)\), independently of the hit times and original gaps. Every resulting fragment is at most
\[
G_{n,(i)}\max\{U_i,1-U_i\}.
\]
Therefore the conditional probability that a hit gap of rank \(i\le m\) retains a fragment of length at least \(G_{n,(m)}\) is bounded by
\[
\min\left\{1,\frac{2(G_{n,(i)}-G_{n,(m)})}{G_{n,(i)}}\right\}.
\]
For fixed \(m\), this bound tends to zero in probability by step 1 and is bounded by one. Its expectation tends to zero. Summing over the finite ranks \(1,\ldots,m\) proves that, outside an event of probability \(o(1)\), whenever \(A_{n,m}\) occurs the new longest gap is precisely the intact original gap of **smallest rank** among ranks \(2,\ldots,m\) not hit by \(\tau_{1,n}\). The stronger assertion includes its exact length, not merely its parent rank.

For the limiting independent clocks, the event that all ranks \(2,\ldots,m\) have been hit before rank one has probability
\[
\int_0^\infty e^{-t}(1-e^{-t})^{m-1}\,dt=\frac1m.
\]
Thus \(\limsup_{n\to\infty}\Pr(K_n>m)\le1/m\). The rank family is tight, and the probability that it fails to equal the first untouched rank among \(2,\ldots,m\) tends to at most \(1/m\). In particular the probability of a damaged original gap being the new longest gap tends to zero. Here \(K_n\) is defined even on that exceptional event, but asymptotically it is never needed.

**4. Joint limit and explicit marks.** For fixed \(m\), the first-hit clocks converge jointly to \((E_i)_{i\le m}\) and the normalized differences of the original gaps converge jointly to the independent \((Z_j)_{j<m}\). Ties among the limiting clocks have probability zero. Step 3 then identifies the joint limit of the waiting time, winning rank, and drop on the event that a rank \(2,\ldots,m\) is untouched. Letting \(m\to\infty\), with exceptional mass at most \(1/m\), proves the stated three-coordinate weak convergence and identifies \(K=\min\{k\ge2:E_k>E_1\}\). The minimum is finite almost surely, since the conditional survival chance of each clock beyond a fixed \(E_1=t\) is \(e^{-t}>0\).

For each \(k\ge2\), integrating the independent exponential clock densities gives
\[
\Pr(K=k)=\int_0^\infty e^{-2t}(1-e^{-t})^{k-2}\,dt
=\int_0^1u(1-u)^{k-2}\,du=\frac1{k(k-1)}.
\]
Its tail telescopes to \(1/k\), so \(\mathbb EK=\infty\). Conditional on \(K=k\), exponential-order-statistic spacings imply
\[
\Pr(Y\le y\mid K=k)=(1-e^{-y})^{k-1}\quad(y\ge0).
\]
Put \(q=1-e^{-y}\). Summing the geometric-weighted telescoping series gives
\[
\Pr(Y\le y)=\sum_{j\ge1}\frac{q^j}{j(j+1)}
=1+\frac{1-q}{q}\log(1-q)=1-\frac{y}{e^y-1}.
\]
Finally, by monotone integration and the elementary exponential series,
\[
\mathbb EY=\int_0^\infty\frac{y}{e^y-1}\,dy
=\sum_{r\ge1}\int_0^\infty ye^{-ry}\,dy
=\sum_{r\ge1}r^{-2}=\frac{\pi^2}{6}.
\]
The conditional geometric law of \(K\) given \(T=t\) follows directly from the independent-clock model. This completes the proof.

## Verification

The accompanying standalone `checker.py` executes deterministic algebraic checks of the rank probabilities, survival distribution, conditional maximum representation, and convergent-series bounds, and runs reproducible direct finite-sample circle-fragmentation experiments. These experiments are **not** proofs of limiting statements; the proof above supplies the infinite argument. The direct finite-sample algorithm explicitly verifies that the first record happens when the original largest gap is first hit and tracks all descendant fragments, thereby testing the definitions of \(W_n\), \(K_n\), and \(D_n\). The convergence of winner rank is expected to be slow because a cut point near one endpoint of the original largest gap can temporarily retain a dominant fragment with probability of order \(1/\log n\).

Reproduce using `python3 checker.py`; only Python's standard library is required. The program prints the number of successfully checked assertions and a finite-sample illustrative table.

## Relationship to prior work

Penrose (2026) studies the number and times of record decreases for maximal spacings (and more general coverage thresholds). His Theorem 2.2 establishes the aggregate record-count order of \((\log n)^2\); its proof is based on current largest holes and does not identify the parent-gap **rank of the next record leader** or the **size of that particular next drop**. The present theorem concerns the marked *first next* record and gives a joint law, including a new heavy-tailed discrete mark and a non-Gumbel drop distribution.

Holst (1980) supplies classical exact representations and extremes for ranked uniform spacings, including their exponential order-statistic construction, and studies a different waiting time: time until **all gaps** are shorter than a deterministic shrinking threshold. Those classical ingredients are credited in the proof above. The coupled next-record waiting/rank/drop law is not an assertion of either cited work. Other work on fixed-sample Greenwood statistics and longest gaps concerns static dependence, not subsequent dynamic fragmentation. A published or unindexed mathematically equivalent theorem cannot be excluded categorically.

## Limitations

Only one-dimensional uniform circular samples are covered. The result does not establish the joint process of successive future record drops, rates of convergence, or convergence of finite-sample drop moments. Finite-sample convergence can be slow, especially the probability that a just-cut fragment remains the maximum. The identified first-record marked limit is an asymptotic theorem, not an exact finite-\(n\) distribution. Historical priority outside the inspected literature remains open to independent verification.

## References

1. M. D. Penrose, *Record times for coverage thresholds and maximal spacings* (first public version 2026-08-19), arXiv:2608.19104, https://arxiv.org/abs/2608.19104 . Relevant material: Introduction, Theorem 2.2, proofs of record-count results, Section 8.
2. L. Holst, *On the lengths of the pieces of a stick broken at random*, Journal of Applied Probability 17 (1980), 623–634, DOI:10.2307/3212956. Open full text: https://imprs-gw-lectures.aei.mpg.de/wp-content/uploads/2023/12/Holst_StickBreakingDistributions.pdf . Relevant material: Sections 2, 3, 6.
