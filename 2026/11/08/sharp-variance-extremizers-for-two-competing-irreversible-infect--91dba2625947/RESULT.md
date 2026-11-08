# Sharp variance extremizers for two competing irreversible infections on finite trees

## Finding
Consider two mutually exclusive irreversible infections, A and B, spreading on a finite tree from distinct seed vertices. If the path between the seeds has \(m\ge 1\) uninfected interior vertices, constant positive transmission rates \(\lambda_A\) and \(\lambda_B\) along that path, and arbitrary positive transmission rates on the off-path edges, then the final size of the A territory is a weighted binomial threshold:
\[
 Z_A=w_0+\sum_{j=1}^{X}w_j,\qquad
 X\sim\operatorname{Bin}\left(m,\frac{\lambda_A}{\lambda_A+\lambda_B}\right).
\]
Here \(w_j\) counts the vertices of the subtree attached to path vertex \(v_j\), including \(v_j\). In particular, off-path transmission rates and detailed off-path shapes do not change the final territory-size distribution once these weights are fixed.

There is also a sharp extremal theorem for **equal** path rates. Fix the seed separation \(m+1\) edges and total vertex count \(n=m+2+B\), with \(B\ge0\) off-path vertices. Over every tree with those parameters,
\[
 \boxed{\frac m4\ \le\ \operatorname{Var}(Z_A)\ \le\
 \frac m4+\frac{Bm}{2}\frac{\binom{m-1}{j_*-1}}{2^{m-1}}
   +B^2q_{j_*}(1-q_{j_*})},
 \quad q_j=2^{-m}\sum_{k=j}^{m}\binom mk,
 \quad j_*=\left\lceil\frac m2\right\rceil.
\]
For \(B>0\), the minimum is attained **exactly** when every off-path vertex belongs to a component attached to one of the two seeds. The maximum is attained **exactly** when all \(B\) off-path vertices belong to the component attached to one central interior path vertex: \(j=(m+1)/2\) when \(m\) is odd, and either \(j=m/2\) or \(j=m/2+1\) when \(m\) is even. The internal shapes of those attached components are unrestricted. For \(B=0\) both bounds coincide at \(m/4\).

For example, \(m=3\) and \(B=4\) give a variance range from \(3/4\) to \(31/4\). In a maximizing tree the A-territory sizes are \(1,2,7,8\) with respective probabilities \(1/8,3/8,3/8,1/8\).

## Assumptions and scope
Let \(T=(V,E)\) be an arbitrary finite simple undirected tree with distinct seed vertices \(v_0=a\) and \(v_{m+1}=b\), joined by the unique path \(v_0,v_1,\ldots,v_m,v_{m+1}\). Every vertex is initially susceptible except \(a\), occupied by infection A, and \(b\), occupied by infection B. For each oriented infected-to-susceptible edge, the corresponding successful transition occurs according to the continuous-time Markov jump mechanism of that infection, independently of other active edges. On every path edge the infection-specific rates are constants \(\lambda_A,\lambda_B>0\). Rates on off-path edges may be arbitrary positive numbers, depending on the edge and infection. Infection is permanent and mutually exclusive; there is no spontaneous recovery or additional seeding. All vertices are eventually assigned an infection almost surely.

Deleting the \(m+1\) seed-path edges partitions \(V\) into \(m+2\) rooted components \(C_0,\ldots,C_{m+1}\) containing their respective path vertices; let \(w_j=|C_j|\ge1\). For the extremal part only, assume \(\lambda_A=\lambda_B\). The total number of vertices is \(n=m+2+B\), and \(B\) may be any nonnegative integer. The result does not apply without a tree topology or without constant per-strain rates along the seed path.

## Proof
**1. Reduction to a single path interface.** Every off-path component \(C_j\) touches the remaining tree only at \(v_j\); hence once \(v_j\) acquires type A or B, all of \(C_j\) eventually acquires the same type. The only contested region lies on the open seed-to-seed path. At every stage before it is filled, the two occupied path prefixes each have exactly one active edge into the remaining open path segment. The two competing hazards are \(\lambda_A\) and \(\lambda_B\). The memoryless property of the independent exponential edge mechanisms, including after irrelevant off-path infections occur, gives probability \(p=\lambda_A/(\lambda_A+\lambda_B)\) for the next contested path vertex to be captured by A, independently of previous captures. There are exactly \(m\) contested captures. If \(X\) counts those made by A, then \(X\sim\operatorname{Bin}(m,p)\), and A captures precisely \(C_0,C_1,\ldots,C_X\). This proves the full distributional formula, including independence from off-path rates.

In particular, with \(q_j=\Pr(X\ge j)\) for \(1\le j\le m\), one obtains
\[
 \mathbb E Z_A=w_0+\sum_{j=1}^{m}w_jq_j,\quad
 \operatorname{Var}(Z_A)=\sum_{i,j=1}^{m}w_iw_j
 \big(q_{\max(i,j)}-q_iq_j\big).
\]

**2. Sharp lower bound.** In the equal-rate case \(p=1/2\), write \(w_j=1+b_j\), \(b_j\ge0\), and \(\sum_{j=0}^{m+1}b_j=B\). Since seed-side components are deterministic, \(Z_A\) differs by a constant from
\[
 X+\sum_{j=1}^{m}b_jI_j,\qquad I_j=\mathbf1_{\{X\ge j\}}.
\]
For every \(1\le j\le m\), the covariance
\[
 \operatorname{Cov}(X,I_j)=\frac m4\,
  \Pr\{\operatorname{Bin}(m-1,1/2)=j-1\}>0.
\]
Also, for \(i\le j\), \(\operatorname{Cov}(I_i,I_j)=q_j(1-q_i)>0\). Consequently each nonzero interior \(b_j\) strictly increases the variance above \(\operatorname{Var}(X)=m/4\). The minimum therefore occurs exactly when all extras lie in seed-attached components, establishing the lower bound and equality characterization.

**3. Concentration of off-path vertices at one interior vertex.** The covariance matrix of \((I_1,\ldots,I_m)\) is positive definite. Indeed, if \(\sum_j c_jI_j\) is constant for all \(X=0,1,\ldots,m\), successive differences at \(X=j\) force each \(c_j=0\), and all these values of \(X\) occur with positive probability. The variance is therefore a strictly convex quadratic function of \((b_1,\ldots,b_m)\). By the positivity in step 2, every maximizer uses all \(B>0\) extras on interior components. Over the simplex \(\sum_{j=1}^{m}b_j=B\), strict convexity then forces every maximum to be a vertex, so all \(B\) extras lie at a single interior position \(j\). This continuous-simplex upper bound is attained by the admissible integer allocation \(b_j=B\).

**4. Determining the maximizing position.** When all extras lie at position \(j\),
\[
 \operatorname{Var}(Z_A)=\frac m4+2B\operatorname{Cov}(X,I_j)+B^2q_j(1-q_j)
 =\frac m4+\frac{Bm}{2}\frac{\binom{m-1}{j-1}}{2^{m-1}}
 +B^2q_j(1-q_j).
\]
The binomial probabilities \(\binom{m-1}{j-1}/2^{m-1}\) increase strictly toward the central index or two central indices and decrease strictly afterward. By symmetry of \(\operatorname{Bin}(m,1/2)\), the tail probabilities \(q_j\) decrease toward and past \(1/2\), so \(q_j(1-q_j)\) has precisely those same central maximizers: one if \(m\) is odd and two if \(m\) is even. Both coefficients are strictly positive when \(B>0\), giving exactly the stated maximizers and upper formula. For \(B=0\) the variance is \(m/4\) throughout. This completes the proof for all positive integers \(m\) and all nonnegative integers \(B\).

## Verification
Run `python3 verify.py` with Python's standard library. The checker uses exact `fractions.Fraction` arithmetic to solve full finite-state transition recurrences for 75 independently specified, branching and asymmetric-rate competing processes. It compares each complete final-size distribution against the weighted binomial formula. It also checks all 4,970 rooted-component allocations for \(1\le m\le7\) and \(1\le B\le5\), testing the lower and upper bounds and their equality cases. Those finite checks support the theorem but do not replace the all-parameter proof above.

## Relationship to prior work
Gouéré (2007, arXiv:math/0607226), extending competing first-passage growth models, establishes large-scale territory/shape results on infinite spatial networks, not the finite-tree size-variance extremizers. Karrer and Newman (2011, arXiv:1105.3424, first public on 2011-05-17) analyze competing epidemics and network-level final fractions/phase diagrams, not a sharp finite-tree branching allocation theorem. Sun, Saad and Lokhov (preprint 2019, arXiv:1905.04416) obtain exact dynamic message-passing descriptions of interacting spreads on trees; their general node-marginal inference is not itself a proof of the full class-wide variance maximizer and equality classification established here. The simple path-interface binomial reduction follows from exponential memorylessness; the structural contribution is the exact maximum, minimum and equality cases over **all** finite tree shapes with fixed size and source distance.

## Limitations
Only the two-seed irreversible, mutually exclusive continuous-time spreading model is covered. The equal-rate hypothesis is needed for the stated central-position extremizer; for unequal rates the weighted-binomial law and covariance formula still hold, but the optimal allocation position may change. Cycles, recovery, heterogeneous seed-path rates and stochastic reinfection fall outside the theorem. The result is a theoretical network-design benchmark, not an empirical epidemic prediction. Earlier unindexed exact tree competition results might contain equivalent extremal statements; absence from the inspected sources is not a priority certificate. Independent validation has not been performed.

## References
- J.-B. Gouéré, "Shape of Territories in Some Competing Growth Models," *Annals of Applied Probability* 17 (2007), 1273–1305; preprint https://arxiv.org/abs/math/0607226; DOI:10.1214/105051607000000113.
- B. Karrer and M. E. J. Newman, "Competing Epidemics on Complex Networks," *Physical Review E* 84 (2011), 036106; arXiv:1105.3424, initially posted 2011-05-17; https://arxiv.org/abs/1105.3424; DOI:10.1103/PhysRevE.84.036106.
- H. Sun, D. Saad and A. Y. Lokhov, "Competition, Collaboration, and Optimization in Multiple Interacting Spreading Processes," *Physical Review X* 11 (2021), 011048; preprint https://arxiv.org/abs/1905.04416; DOI:10.1103/PhysRevX.11.011048.
