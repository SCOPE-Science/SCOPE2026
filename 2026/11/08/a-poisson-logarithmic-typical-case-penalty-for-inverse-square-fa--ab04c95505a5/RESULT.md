# A Poisson logarithmic typical-case penalty for inverse-square facility omission

## Finding

In one-dimensional facility location with one fewer facility than agents, the Inverse-Square omission mechanism of Chan, Lin and Wang has an unbounded approximation ratio even on independent uniform locations, although its worst-case guarantee on arbitrary metrics is of square-root order. Its *typical* scale is logarithmic and has a nonconstant Poisson limit.

Specifically, let \(n\ge3\) agent locations be independent uniform random variables on \([0,1]\), and let \(R_n\) be the ratio of the conditional expected total connection cost of Inverse-Square to the optimal cost of placing \(n-1\) facilities. Let \(0<T_1<T_2<\cdots\) be the arrival times of a rate-one Poisson process on \((0,\infty)\). Define \(S_2=\sum_{j=1}^{\infty}T_j^{-2}\). Then

\[
\frac{R_n}{\log n}\ \xrightarrow{d}\ Z:=\frac{1}{T_1S_2}.
\]

The random variable \(Z\) is strictly positive, finite and nondegenerate, with \(Z\le T_1\) almost surely. In particular, \(R_n\to\infty\) in probability. The conditional law of \(S_2\), which completely specifies the limit, satisfies for \(t,s>0\)

\[
\mathbb E[\exp(-sS_2)\mid T_1=t]
=\exp\left(-\frac{s}{t^2}-\int_t^\infty(1-e^{-s/u^2})\,du\right).
\]

This is a statement about the conditional expected social cost *given a sampled report profile*, not a realized randomized omission and not a claim about convergence of expected approximation ratios.

## Assumptions and scope

The metric is absolute distance on the real line; all reported locations are truthful, almost surely distinct, and sampled independently from the uniform distribution on \([0,1]\). Exactly \(n-1\) facilities may be placed anywhere on the line, with linear social cost equal to the sum of each agent's distance to its nearest facility. The Inverse-Square rule omits a report with probability proportional to the inverse square of that report's nearest-neighbor distance, and places facilities at every other report. The optimal cost is the smallest pairwise distance, equal to the smallest *consecutive* gap in sorted locations.

All asymptotics hold as the number of agents tends to infinity, with the number of facilities always exactly one less. The Poisson process is an auxiliary limit process, not a replacement for the finite uniform sampling model.

## Proof

**Step 1: An exact deterministic cost formula.** Sort the sampled locations as \(X_{(1)}<\cdots<X_{(n)}\), and write \(G_i=X_{(i+1)}-X_{(i)}\), \(1\le i\le n-1\). If report \(i\) is omitted, its cost is \(\delta_i\), the distance to its closest other report; all other agents pay zero. Thus \(\delta_1=G_1\), \(\delta_n=G_{n-1}\), and \(\delta_i=\min(G_{i-1},G_i)\) for interior indices. Writing \(g_*:=\min_iG_i\), the ratio is exactly

\[
R_n=\frac{\sum_{i=1}^n\delta_i^{-1}}
{g_*\sum_{i=1}^n\delta_i^{-2}}.
\tag{1}
\]

For optimality of \(g_*\), any allocation of \(n\) agents to \(n-1\) facilities assigns two distinct agents to the same facility. Their combined distance to it is at least their separation, which is at least \(g_*\). Conversely, omitting one endpoint of a closest pair and opening facilities at every other report incurs cost \(g_*\).

**Step 2: Exponential spacings.** Let \(E_0,E_1,\ldots,E_n\) be independent mean-one exponential random variables and \(H=\sum_{j=0}^nE_j\). The joint law of the sorted uniform spacings, including the two boundary spacings, is that of \((E_0/H,\ldots,E_n/H)\). In particular, \((G_1,\ldots,G_{n-1})\) has the distribution of \((E_1/H,\ldots,E_{n-1}/H)\). Define \(m_1=E_1\), \(m_n=E_{n-1}\), and \(m_i=\min(E_{i-1},E_i)\) for interior indices. Let \(e_*:=\min_{1\le j\le n-1}E_j\), \(A_n=\sum_{i=1}^nm_i^{-1}\), \(B_n=\sum_{i=1}^nm_i^{-2}\). The common factor \(H\) cancels from (1), leaving the distributional identity

\[
R_n\ \stackrel d=\ \frac{A_n}{e_*B_n}.
\tag{2}
\]

For either \(p=1\) or \(p=2\), the identity \(\min(a,b)^{-p}=a^{-p}+b^{-p}-\max(a,b)^{-p}\) gives

\[
\sum_{i=1}^n m_i^{-p}
=2\sum_{j=1}^{n-1}E_j^{-p}
-\sum_{j=1}^{n-2}\max(E_j,E_{j+1})^{-p}.
\tag{3}
\]

**Step 3: A logarithmic numerator.** For \(X=E_1^{-1}\), \(\Pr(X>u)=1-e^{-1/u}\sim u^{-1}\). Take \(b_n=n\log n\) and \(X^{(n)}=\min(X,b_n)\). Direct tail integration yields \(\mathbb E X^{(n)}=\log b_n+O(1)\) and \(\mathbb E[(X^{(n)})^2]\le2b_n\). Therefore Chebyshev's inequality gives

\[
\frac{\sum_{j=1}^{n-1} X_j^{(n)}}{n\log n}\ \xrightarrow{p}\ 1.
\]

Also \(\Pr(\max_{j\le n-1}X_j>b_n)\le n/b_n=1/\log n\), so the same convergence holds without truncation. The correction in (3) is negligible because \(\max(E_j,E_{j+1})^{-1}\) has finite expectation \(2\log2\) (the maximum of two independent exponentials has density \(2(e^{-u}-e^{-2u})\)). By Markov's inequality,

\[
\frac{A_n}{2n\log n}\ \xrightarrow{p}\ 1.
\tag{4}
\]

**Step 4: The quadratic extreme sum.** Put \(W_j=\max(E_j,E_{j+1})^{-2}\). For \(u>0\),

\[
\Pr(W_j>u)=(1-e^{-u^{-1/2}})^2\le\min(1,u^{-1}).
\]

It follows that \(\Pr(\max_{j\le n-2}W_j>n^2)\le1/n\), while \(\mathbb E[\min(W_j,n^2)]\le1+2\log n\). Hence \(n^{-2}\sum_{j=1}^{n-2}W_j\to0\) in probability, and (3) gives

\[
\frac{B_n}{2n^2}-\sum_{j=1}^{n-1}(nE_j)^{-2}\ \xrightarrow{p}\0.
\tag{5}
\]

**Step 5: Joint Poisson convergence.** The point process \(\Pi_n=\sum_{j=1}^{n-1}\delta_{nE_j}\) converges on compact subsets of \((0,\infty)\) to a rate-one Poisson process: counts of independent exponentials in disjoint bounded rescaled intervals converge jointly to independent Poisson counts by the multinomial rare-events limit. To pass from compactly supported functions to the singular sum, fix \(\varepsilon>0\) and \(M>0\). The probability that any rescaled exponential is below \(\varepsilon\) is at most \(\varepsilon\). For the tail,

\[
\mathbb E\sum_{j=1}^{n-1}(nE_j)^{-2}\mathbf1_{\{nE_j>M\}}
=\frac{n-1}{n}\int_M^\infty u^{-2}e^{-u/n}\,du
\le\frac1M.
\]

The corresponding Poisson tail has expectation \(1/M\), and its probability of any point below \(\varepsilon\) is at most \(\varepsilon\). Truncation and the continuous mapping theorem therefore establish the joint distributional convergence

\[
\left(ne_*,\ \sum_{j=1}^{n-1}(nE_j)^{-2}\right)
\xrightarrow{d}(T_1,S_2).
\tag{6}
\]

There is almost surely a strictly positive first Poisson arrival, so \(S_2\ge T_1^{-2}>0\); Poisson tail integrability gives \(S_2<\infty\) almost surely. Combining (2), (4), (5) and (6) by Slutsky's theorem proves the announced limit. Conditional on \(T_1=t\), the remaining points are an independent unit-rate Poisson process on \((t,\infty)\); its Laplace functional yields the stated conditional transform, and its random contribution to \(S_2\) proves nondegeneracy. Since \(Z>0\) almost surely, for any fixed \(M>0\), \(\Pr(R_n\le M)\to0\) by convergence in distribution and positivity of the limit.

## Verification

The standalone `checker.py` reproduces (1) and (3) as exact rational identities on \(3,223\) distinct rational-location profiles of sizes \(3\) through \(7\). It separately checks distance-scale invariance and the deterministic bound \(R_n\ge1\) on \(125\) seeded exponential-spacing samples. Run `python3 checker.py` using the Python standard library. These finite checks do not replace the infinite-limit proof above.

## Relationship to prior work

Chan, Lin and Wang (2026) introduce the Inverse-Square rule and prove strategyproofness and a tight worst-case approximation ratio of \((1+\sqrt{n/2})/2\) in arbitrary metric spaces, but their mechanism and approximation sections do not determine this distributional typical-case law under uniform sampling. Fotakis and Tzamos (2013) prove a worst-case factor of \(2\) on the line for their *different* Pick the Loser mechanism, so the present divergence does not contradict the existence of a constant-approximation mechanism on the line. Exponential-spacing and Poisson-extremes arguments are standard probabilistic tools; the new assertion is the mechanism-specific logarithmic ratio limit.

## Limitations

The distributional result is restricted to independent uniform points on one interval, linear total distance cost, exactly one omitted report, and the named Inverse-Square mechanism. It does not establish convergence of expected ratios, nor extend to general location densities, multiple omitted reports, or independent realizations of the mechanism's random omission. The law has received a self-review, but no independent scientific validation; prior-work priority can be affected by unindexed or subsequently appearing research.

## References

1. Hau Chan, Jianan Lin, and Chenhao Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484, publicly available August 23, 2026; Inverse-Square rule and its worst-case analysis in Section 4. https://arxiv.org/abs/2608.22484 .
2. Dimitris Fotakis and Christos Tzamos, *Strategyproof Facility Location for Concave Cost Functions*, arXiv:1305.3333, publicly available May 15, 2013; Pick the Loser in Section 6. https://arxiv.org/abs/1305.3333 .
