# Optimal multi-offer cover walks: exact bipartite parity and start-side dominance

## Finding

**Theorem.** Fix integers \(a\ge b\ge1\) and \(d\ge2\). Consider the complete bipartite graph \(K_{a,b}\). At each step a controller receives \(d\) independently and uniformly sampled neighbors of the walker's current vertex, with replacement, and must move to one of them. The objective is to visit every vertex as early as possible. Let \(C_A\), respectively \(C_B\), be the cover time from a prescribed vertex in the part of size \(a\), respectively \(b\), when an optimal policy is used.

The policy that selects an unvisited offered neighbor whenever one exists minimizes the cover time in first-order stochastic order **simultaneously at every integer deadline**, among all adaptive randomized policies. Let \(U_n\) denote the time to see all \(n\) labels in the following \(d\)-offer collector beginning with one label already seen: on each round sample \(d\) independent uniform labels and accept a new label whenever offered. Set \(F_n(k)=\Pr(U_n\le k)\), with \(F_n(k)=0\) for \(k<0\) and \(U_1=0\). Then, for every integer \(k\ge0\),

\[
\Pr(C_A\le2k+1)=\Pr(C_B\le2k+1)=F_a(k)F_b(k),
\]
\[
\Pr(C_A\le2k)=F_a(k)F_b(k-1),\qquad
\Pr(C_B\le2k)=F_a(k-1)F_b(k).
\]

If \(a>b\), the latter CDF difference is **strictly positive exactly for \(k\ge a-1\)** and zero for smaller \(k\), while the odd-time CDF difference is always zero. In particular, \(C_A\) is strictly smaller than \(C_B\) in first-order stochastic order, despite infinitely many parity times at which their CDFs agree. With independently sampled \(U_a,U_b\),

\[
\mathbb E[C_B]-\mathbb E[C_A]
=\Pr(U_a>U_b)-\Pr(U_a<U_b)\in(0,1].
\]

Equality to \(1\) occurs exactly when \(b=1<a\); if \(a=b\), both starting-side laws coincide. The structural input is the additional assertion \(U_a\ge_{\mathrm{lr}}U_b\) for \(a>b\): the single-part completion times are ordered in **likelihood-ratio order**, a stronger property than first-order stochastic dominance.

For the two-offer walk on \(K_{3,2}\), the even-time probabilities at four steps are \(10/27\) versus \(0\), and the expected cover-time advantage is exactly \(23/28\) step.

## Assumptions and scope

The graph is simple and unweighted; every offered neighbor is sampled independently with replacement, with the same integer \(d\ge2\) at every step. The controller knows visited vertices and all offers and may use history and randomization. Cover time includes the starting vertex at time zero and counts traversed edges. The designation of parts does not restrict the controller. The likelihood-ratio order \(X\ge_{\mathrm{lr}}Y\) for nonnegative integer variables means that the mass-function ratios \(\Pr(X=k)/\Pr(Y=k)\) are nondecreasing where defined, equivalently \(\Pr(X=j)\Pr(Y=i)\ge\Pr(X=i)\Pr(Y=j)\) whenever \(i<j\). Empty support is interpreted by this cross-product criterion.

Write \(\operatorname{Geom}(p)\) for the positive-integer geometric distribution with mass \(p(1-p)^{t-1}\), \(t\ge1\). All waiting times below use this normalization. For \(n\ge2\),

\[
U_n\stackrel{\mathrm d}=\sum_{r=1}^{n-1}G_{n,r},\qquad
G_{n,r}\text{ independent},\quad
G_{n,r}\sim\operatorname{Geom}\!\left(1-\left(1-\frac r n\right)^d\right).
\]

No independence between the actual walk's successive vertex labels is assumed beyond independent offers; independence between the two partwise collector processes follows from the alternating bipartite structure and disjoint offer randomness.

## Proof

**1. An optimal all-deadline rule.** Every step necessarily switches the bipartition class. When there are \(j\) previously visited vertices in the target class of order \(n\), the chance that every offer is previously visited equals \((j/n)^d\), regardless of which particular vertices were visited or of the walker's current position. Hence no rule can increase the visited count at the next step with probability exceeding \(1-(j/n)^d\). Selecting an offered new vertex attains that bound. The birth-chain transition \(j\mapsto j+1\) with this probability is monotone in the initial count: if two counts differ, a one-step jump of at most one cannot invert their order; at equal counts a greedy transition dominates the alternative. Coupling these count chains at all successive visits to each part proves that the greedy rule maximizes both visited counts jointly at every time. Because the classes are alternated deterministically, this maximizes the probability of complete coverage by **every** deadline. Thus it is stochastically optimal, not merely mean-optimal.

**2. Independent collectors and parity.** Starting in \(A\), the number of later selections into \(A\) is \(\lfloor t/2\rfloor\), and into \(B\) is \(\lceil t/2\rceil\). The initial vertex counts as one visit in \(A\). In the initially empty class, its first selection is necessarily new, so full collection there requires \(1+U_b\) selections. The two families of offers are independent; their count-transition probabilities depend only on the count, not the current label. Consequently, with independent \(U_a,U_b\),

\[
C_A\stackrel{\mathrm d}=\max\{2U_a,2U_b+1\},\qquad
C_B\stackrel{\mathrm d}=\max\{2U_b,2U_a+1\}.
\]

Taking the probability that both constraints are satisfied gives the four displayed formulas. For a coupling with the same independent \(U_a,U_b\), subtraction of the two maxima gives \(C_B-C_A=1\), \(0\), or \(-1\) according as \(U_a>U_b\), \(U_a=U_b\), or \(U_a<U_b\). Taking expectations proves the displayed identity and the absolute upper bound of one step.

**3. Likelihood-ratio lemma.** We use three elementary properties of nonnegative integer probability sequences. First, positive-integer geometric masses are log-concave; convolutions of log-concave masses are log-concave. Second, if \(X\ge_{\mathrm{lr}}Y\) and \(H\) is independent and has a log-concave mass sequence, then \(X+H\ge_{\mathrm{lr}}Y+H\). To verify this, expand the cross-product difference at indices \(k<\ell\), group terms indexed by \(i<j\), and use the nonnegative minors of \(h(t-i)\) (which follow by repeated adjacent-ratio comparison from log-concavity), together with \(g(j)f(i)-g(i)f(j)\ge0\). Third, if \(X\) is log-concave and \(H\) is an independent positive-integer variable, then \(X+H\ge_{\mathrm{lr}}X\): for every fixed positive shift \(s\), log-concavity makes \(\Pr(X=k-s)/\Pr(X=k)\) nondecreasing in \(k\); mixtures over \(s\) preserve this cross-product inequality.

**4. Likelihood-ratio ordering by class size.** For each fixed remaining count \(r\), the geometric success probability \(1-(1-r/n)^d\) strictly decreases as \(n\) increases (provided \(1\le r<n\)). Its failure probability increases; hence

\[
G_{n,r}>_{\mathrm{lr}}G_{n-1,r}\quad(1\le r\le n-2).
\]

Replace the \(n-2\) independent summands in \(U_{n-1}\) one at a time by \(G_{n,r}\). The other summands at each stage form a log-concave convolution, so the likelihood-ratio order is preserved under each replacement. Adding the extra independent positive geometric summand \(G_{n,n-1}\) preserves and enlarges this order by the third property. Thus \(U_n\ge_{\mathrm{lr}}U_{n-1}\); transitivity gives \(U_a\ge_{\mathrm{lr}}U_b\) for \(a>b\). The case \(b=1\) follows directly from \(U_1=0\).

**5. Strict even-time comparison.** Write \(f_n(k)=\Pr(U_n=k)\). Likelihood-ratio order implies, for every \(j<k\), \(f_a(k)f_b(j)\ge f_a(j)f_b(k)\). Summing over \(j<k\),

\[
F_a(k)F_b(k-1)-F_a(k-1)F_b(k)\ge0.
\]

If \(a>b\) and \(k\ge a-1\), take \(j=b-1< a-1\le k\). Then \(f_b(j)>0\) while \(f_a(j)=0\), and \(f_a(k)>0\), so the inequality is strict. When \(k<a-1\), \(F_a(k)=F_a(k-1)=0\) and the difference vanishes. Together with the parity identity this establishes the precise stochastic order.

For \(a>b\), the mean advantage is positive because the even-time differences are strictly positive; it is at most one by Step 2. If \(b\ge2\), the independent random variable \(U_b\) has unbounded support and can exceed \(U_a\) with positive probability, making the mean gap strictly less than one. If \(b=1\), \(U_b=0\) and \(U_a>0\) almost surely, giving the equality case.

**6. Exact smallest asymmetric illustration.** For \(d=2\), \(U_2\sim\operatorname{Geom}(3/4)\), and \(U_3\) is the sum of independent \(\operatorname{Geom}(8/9)\) and \(\operatorname{Geom}(5/9)\) variables. Thus \(\Pr(U_3=2)=40/81\) and \(\Pr(U_2=1)=3/4\), giving \(\Pr(C_A\le4)=10/27\) versus \(\Pr(C_B\le4)=0\). By multiplying their geometric probability-generating functions,

\[
\mathbb E[4^{-U_3}]
=\frac{(8/9)(1/4)}{1-(1/9)(1/4)}
\frac{(5/9)(1/4)}{1-(4/9)(1/4)}=\frac1{28}.
\]

Since \(\Pr(U_2>m)=4^{-m}\) and \(\Pr(U_2\ge m)=4^{-(m-1)}\) for \(m\ge1\), independence gives \(\Pr(U_2>U_3)=1/28\) and \(\Pr(U_3>U_2)=1-4/28=6/7\). The mean gap is therefore \(23/28\).

## Verification

Run `python checker.py` using Python 3 and its standard library. The script compares the analytic product CDF against an independent labeled-vertex Markov enumeration of actual offered neighbors for \(1\le a,b\le4\), \(d\in\{2,3\}\), and all integer deadlines from zero to ten. It also checks strict even-time comparisons and numerical likelihood-ratio minors across additional part sizes and choice counts. Its exact-rational assertions passed: 704 labeled-CDF equalities, 160 odd-parity equalities, 2,564 strict even-time inequalities, and 513 likelihood-ratio minors. These are finite checks supporting, but not replacing, the all-size proof.

## Relationship to prior work

Georgakopoulos, Haslegrave, Sauerwald and Sylvester introduced and studied the two-offer choice random walk, deriving general hitting/cover-time bounds and computational complexity results (first public November 12, 2019). Their main paper provides order bounds, including a complete-graph asymptotic, but does not present the exact all-size complete-bipartite start-side laws or the likelihood-ratio comparison proved here. O'Neill's 2023 treatment of extended occupancy establishes stochastic monotonicity for single-ball, constant-fall-through models; that process has birth probabilities linear in the unseen fraction, whereas the present \(d\)-offer model has discovery probability \(1-(j/n)^d\) and couples two alternating collectors. The general likelihood-ratio convolution property is classical and is used as a proof tool, not claimed as new. Orenshtein and Shinkar's greedy edge-exploration walk is a different process, with free selection among untraversed edges rather than random limited offers.

The single-offer case \(d=1\) is excluded from the new statement: its coupon-law start-side comparison is already a simpler classical setting. The contribution is the stochastically optimal **limited-choice** policy for every positive part size and choice count, together with its sharp parity order and universal expectation gap.

## Limitations

The result requires a complete bipartite graph, uniform independent sampling with replacement, and a common offer count \(d\) on both parts. It does not establish the same order for arbitrary bipartite graphs, heterogeneous offer counts by part, weighted neighbor proposals, or policies optimizing objectives other than cover-time distributions. The originality comparison is limited to checked accessible papers, relevant records and targeted searches; it is not an independent historical-priority audit.

## References

1. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170, initial submission November 12, 2019; *Combinatorics, Probability and Computing* 31 (2022), 73–100. https://arxiv.org/abs/1911.05170
2. B. O'Neill, *Three Distributions in the Extended Occupancy Problem*, *Methodology and Computing in Applied Probability* 25, 84 (2023), published October 30, 2023. https://doi.org/10.1007/s11009-023-10053-y
3. J. G. Shanthikumar and D. D. Yao, *The preservation of likelihood ratio ordering under convolution*, *Stochastic Processes and their Applications* 23 (1986), 259–267. https://doi.org/10.1016/0304-4149(86)90039-6
4. T. Orenshtein and I. Shinkar, *Greedy Random Walk*, *Combinatorics, Probability and Computing* 23 (2014), 269–289. https://doi.org/10.1017/S0963548313000552
