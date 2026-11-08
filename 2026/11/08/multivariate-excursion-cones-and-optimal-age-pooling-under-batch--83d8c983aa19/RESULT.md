# Multivariate excursion cones and optimal age pooling under batch resetting

## Finding

Fix integers \(N\ge4\), \(2\le m\le N-2\), and \(3\le k\le N-m+1\), together with \(D,r>0\). Let \(N\) independent one-dimensional Brownian particles have diffusion generator \(D\partial_{xx}\). At the events of one independent rate-\(r\) Poisson clock, choose uniformly one subset of precisely \(m\) labels and instantaneously return its positions to zero. Observe the unique stationary law and select \(k\) distinct labels.

For every positive vector \(\boldsymbol a=(a_1,\ldots,a_k)\), the simultaneous *one-sided* far-tail rate exists:

\[
I(\boldsymbol a)=\lim_{R\to\infty}-\frac{1}{R}\log
\Pr\{X_1>a_1R,\ldots,X_k>a_kR\}.
\]

Sort the thresholds as \(a_{(1)}\ge\cdots\ge a_{(k)}>0\), and define

\[
d_j=\frac{\binom{N-j}{m-1}}{\binom Nm}>0\quad(1\le j\le k),\qquad
p_j=\sum_{i=1}^j d_i=1-\frac{\binom{N-j}{m}}{\binom Nm}.
\]

Apply decreasing, weighted pool-adjacent-violators (PAV) to the ordered sequence \(a_{(j)}^2/d_j\) with weights \(d_j\): whenever adjacent fitted block means increase, merge the two blocks and replace them by their weighted mean, repeating until the block means are nonincreasing. For the resulting consecutive blocks \(\mathcal B\), set \(S_B=\sum_{j\in B}a_{(j)}^2\) and \(d_B=\sum_{j\in B}d_j\). The exact multivariate logarithmic tail is

\[
\boxed{I(\boldsymbol a)=\sqrt{\frac rD}\sum_{B\in\mathcal B}\sqrt{d_B S_B}.}
\]

The optimal rescaled backward reset ages are unique. Labels within one block share the limiting age \(u_B=\sqrt{S_B/(4Drd_B)}\), and these block ages are nonincreasing in descending threshold order. In fact, conditionally on all the specified excursions, each backward reset age divided by \(R\) converges in probability to its corresponding \(u_B\).

In particular, for \(a_1=\cdots=a_k=a>0\), all ages asymptotically pool and

\[
\boxed{I(a,\ldots,a)=a\sqrt{\frac{kr}{D}\left(1-\frac{\binom{N-k}{m}}{\binom Nm}\right)}.}
\]

This is a genuinely \(k\)-tagged rate (the claimed range starts at \(k=3\)); it is not determined by applying a two-particle tail event separately to each pair.

For the minimal illustrative four-regime example \((N,m,k)=(5,2,3)\), the increments are \((d_1,d_2,d_3)=(2/5,3/10,1/5)\). Four *distinct* age-clustering geometries occur as the positive thresholds vary: three singletons at \((3,2,1)\); the first two pooled at \((1.6,1.4,1)\); the last two pooled at \((2,1.2,1)\); and all three pooled at \((1,1,1)\). The rate is continuously differentiable on the positive orthant but, in general, not twice differentiable across these pooling boundaries. For example, with \(a_{(2)}=2\), \(a_{(3)}=1/10\) and variable \(a_{(1)}\), the second derivative with respect to \(a_{(1)}\) jumps at \(a_{(1)}=4/\sqrt3\), from the positive value

\[
\sqrt{\frac rD}\,\frac{4\sqrt{7/10}}{(28/3)^{3/2}}
\]

on the pooled side to zero on the separated side.

## Assumptions and scope

The batch sizes, particle count and number of observed labels are fixed as \(R\to\infty\). The subset selection is uniform, independent between Poisson events and independent of the Brownian motions. Coordinates diffuse independently between events; the process has no direct particle interactions, drift, confinement, or resetting-time cost. Each threshold is positive, and only one-sided simultaneous positive excursions are claimed (sign changes follow by spatial symmetry). The strict condition \(k\le N-m+1\) guarantees that a reset event can act on one specified tag while sparing any prescribed collection of the other \(k-1\) tags; it is essential to the full age-vector local lower bound used here.

The weights in PAV are the *increments of the probability that a size-\(m\) batch intersects a growing set of tags*. They are not independent resetting probabilities and cannot be replaced by the individual thinning rate \(m/N\).

## Proof

**1. Stationary ages and conditional displacements.** Extend the marked Poisson process to the entire real time axis. Every label is reset at positive rate \(rm/N\), giving an almost surely finite backward age \(A_i\). Coupling all initial states at the first reset of each label gives the unique stationary law. Conditional on these ages, Brownian increments after the respective last resets are independent; thus

\[
(X_1,\ldots,X_k)\mid(A_1,\ldots,A_k)
\sim\bigotimes_{i=1}^k\mathcal N(0,2DA_i).
\]

**2. Exact marked-Poisson age survival.** For any nonnegative age thresholds \(t_i\), let \(t_{[1]}\ge\cdots\ge t_{[k]}\) be their descending order, with \(t_{[k+1]}=0\). The event \(\{A_i>t_i\ \forall i\}\) requires, going backward through the intervals between ordered thresholds, the absence of batches hitting each still-constrained set of tags. A batch hits a specified set of size \(j\) with probability

\[
p_j=1-\binom{N-j}{m}/\binom Nm.
\]

Poisson independence across disjoint backward-time intervals yields the exact identity

\[
\Pr(A_i>t_i\ \forall i)
=\exp\!\left[-r\sum_{j=1}^k p_j(t_{[j]}-t_{[j+1]})\right]
=\exp\!\left[-r\sum_{j=1}^k d_jt_{[j]}\right].
\tag{1}
\]

Here \(d_j=p_j-p_{j-1}=\binom{N-j}{m-1}/\binom Nm\) (with \(p_0=0\)), positive and nonincreasing. Equation (1) is the relevant multivariate Marshall–Olkin survival structure; no claim of novelty is made for that classical shock representation.

**3. Local exponential age law, including coincident ages.** For a positive vector \(\boldsymbol u\), define

\[
J(\boldsymbol u)=r\sum_{j=1}^k d_j u_{[j]}.
\]

A small box around \(R\boldsymbol u\) has upper exponential bound \(e^{-RJ(\boldsymbol u)+o(R)}\) from (1), with an arbitrarily small perturbation in the thresholds. For distinct ordered \(u_{[1]}>\cdots>u_{[k]}\), the matching lower exponent follows by forcing one tagged reset near each prescribed backward time while forbidding all resets of the already-older tags over the necessary intervals. At the \(j\)-th time there is a positive Poisson rate \(rd_j\) of subsets containing that tag and avoiding the \(j-1\) older tags, because \(k\le N-m+1\); designated events can be confined to disjoint fixed-width windows, contributing only \(e^{o(R)}\) factors. The required no-hit intervals contribute precisely \(e^{-RJ(\boldsymbol u)+o(R)}\). Vectors with ties are approximated by arbitrarily close vectors with distinct entries, and continuity of \(J\) gives the same local lower exponent. Consequently the scaled age vector obeys the required local large-deviation bounds on the positive orthant.

**4. Gaussian tails and the Laplace principle.** Uniformly for \(u\) in compact subsets of \((0,\infty)\), the normal survival estimate gives

\[
\lim_{R\to\infty}\frac1R\log\Pr\{\mathcal N(0,2DRu)>aR\}
=-\frac{a^2}{4Du}.
\]

Using conditional independence in step 1 and the local bounds from step 3 therefore gives

\[
I(\boldsymbol a)=\inf_{\boldsymbol u>0}\left\{
J(\boldsymbol u)+\sum_{i=1}^k\frac{a_i^2}{4Du_i}
\right\}.
\tag{2}
\]

For completeness, this Laplace argument can be carried out with finite grid boxes on \([\varepsilon,M]^k\). The excluded region \(\max u_i>M\) has probability at most \(k\exp(-rpmM/N)\) from the one-tag age tails; the excluded region \(\min u_i<\varepsilon\) has a Gaussian survival factor bounded by \(\exp[-a_{\min}^2 R/(4D\varepsilon)]\). First let the mesh tend to zero, then \(M\to\infty\) and \(\varepsilon\downarrow0\). The matching lower bound takes a neighborhood of any strictly positive minimizing age vector and uses step 3. Thus (2) is an exact logarithmic limit, not merely a heuristic saddle point.

**5. Threshold ordering, strict convexity and the pooling solution.** The age cost \(J\) is symmetric. Exchanging \(u_i<u_j\) when \(a_i>a_j\) strictly decreases the Gaussian cost, so the minimizing ages have the same descending order as the thresholds. Moreover \(J\) is convex: it equals \(r\) times \(d_k\sum u_i\) plus nonnegative multiples \(d_j-d_{j+1}\) of the sums of the \(j\) largest ages. Each reciprocal term in (2) is strictly convex for positive age, so the total objective has a unique minimizer.

With descending \(a_{(j)}\), minimizing (2) is equivalent to the strictly convex, order-constrained problem

\[
\min_{u_1\ge\cdots\ge u_k>0}
\sum_{j=1}^k\left(rd_j u_j+\frac{a_{(j)}^2}{4Du_j}\right).
\tag{3}
\]

On any block \(B\) of tied ages, the first-order equation gives

\[
\sum_{j\in B}\left(rd_j-\frac{a_{(j)}^2}{4Du_B^2}\right)=0
\quad\Longrightarrow\quad u_B^2=\frac{S_B}{4Drd_B}.
\]

The Karush–Kuhn–Tucker multipliers within the block are nonnegative exactly when each proper leading subblock has weighted ratio no greater than the whole-block ratio: \(S_{\mathrm{prefix}}/d_{\mathrm{prefix}}\le S_B/d_B\). Decreasing weighted PAV produces precisely these blocks and keeps successive block ratios nonincreasing. The block first-order equations, the internal multiplier inequalities and the between-block strict inequalities therefore satisfy every KKT condition of the strictly convex problem (3). Substituting \(u_B\) yields

\[
rd_Bu_B+\frac{S_B}{4Du_B}=\sqrt{\frac rD}\sqrt{d_BS_B},
\]

which proves the boxed expression and its unique age-clustering interpretation.

**6. Equal-level and nonsmooth angular consequences.** If all thresholds equal \(a\), then \(d_1>\cdots>d_k\) for \(m\ge2\) in the claimed domain. Therefore \(a^2/d_j\) increases, PAV produces one block, and the rate becomes \(a\sqrt{krp_k/D}\). Strict convexity of (2) and a standard exponential-gap argument show that conditional on the excursion event the scaled age vector concentrates at its unique minimizer. For \((N,m,k)=(5,2,3)\), the four displayed examples satisfy the strict PAV inequalities for their four respective partitions. At \(a_{(1)}=4/\sqrt3\), keeping \(a_{(2)}=2\) and \(a_{(3)}=1/10\), the neighboring rate formulas are

\[
\sqrt{\frac rD}\left(\sqrt{\frac7{10}(a_{(1)}^2+4)}+\sqrt{\frac1{500}}\right)
\quad\text{and}\quad
\sqrt{\frac rD}\left(\sqrt{\frac25}\,a_{(1)}+2\sqrt{\frac3{10}}+\sqrt{\frac1{500}}\right).
\]

They agree to first order at the transition, while their second derivatives differ by the positive amount displayed in the finding. The unique minimizer and the envelope theorem give continuous first derivatives throughout the positive threshold orthant, completing the assertion.

## Verification

The standalone standard-library program `verify.py` directly enumerates small batch-intersection probabilities, tests PAV/KKT conditions and exact objective identities, confirms the four three-tag age partitions, and compares the candidate optimum against many independently perturbed feasible ages. Executing `python3 verify.py` yielded 29,382 passing finite checks. A separate independent numerical minimizer was compared against the PAV solution on 1,500 randomly parameterized convex programs, and 7,500 additional feasible perturbations were checked; all passed within stated numerical tolerances. These are diagnostics, not a substitute for steps 1–6.

## Relationship to prior work

De Mauro, Majumdar and Schehr (arXiv:2601.20077, originally January 27, 2026) introduced uniform partial-batch resetting and derived exact stationary marginal Fourier recursions, ordinary correlations and their time dependence. These stationary-distribution and two-point results are prior art. The present result resolves a different observable: exact \(k\)-coordinate directional far-tail exponents for \(k\ge3\), including how the optimal backward reset ages split into consecutive pools as the excursion direction varies. The already known two-coordinate Marshall–Olkin shock picture and bivariate excursion asymptotics are not counted as new parts of the claim.

De Mauro, Biroli, Majumdar and Schehr (arXiv:2509.06658) treat fully simultaneous resetting and its exact stationary joint law under more general renewal clocks. That covers the fully shared endpoint, not the intermediate partial-batch regime with multiple competing optimal age clusters. The classical Marshall–Olkin distribution gives the marked-shock age survival form, but the Brownian Gaussian-mixture rate and PAV phase geometry require the additional large-deviation and constrained-optimization steps above.

## Limitations

Only the logarithmic probability rate and concentration of scaled backward ages are proved; no exact finite-threshold probabilities, polynomial prefactors or fluctuation laws at pooling boundaries are asserted. The age local-bound construction needs \(k\le N-m+1\); events with larger observed sets, where forced simultaneous last resets can restrict the support of the age vector, are not covered by this theorem. The source paper's arbitrary-number marginal recursion may permit other derivations; no general claim of priority over every possible unlocated theorem is made. Publication priority and proof have not undergone independent expert review.

## References

1. G. de Mauro, S. N. Majumdar and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077 (first publicly posted 2026-01-27), https://arxiv.org/abs/2601.20077 .
2. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (2025), https://arxiv.org/abs/2509.06658 .
3. A. W. Marshall and I. Olkin, *A multivariate exponential distribution*, Journal of the American Statistical Association 62 (1967), 30–44, doi:10.1080/01621459.1967.10482885 .
