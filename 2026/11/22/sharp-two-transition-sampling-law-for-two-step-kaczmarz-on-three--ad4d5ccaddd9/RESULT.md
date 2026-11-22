# Sharp two-transition sampling law for two-step Kaczmarz on three planar rows

## Finding
For each real \(0<u<1\), consider the three normalized row vectors
\[
a_0=(1,0),\qquad a_+=(\sqrt u,\sqrt{1-u}),\qquad a_-=(\sqrt u,-\sqrt{1-u}).
\]
For the consistent system \(a_i^\mathsf T x=b_i\), perform exactly two ordinary (unrelaxed) Kaczmarz row projections. The ordered row pair \((I,J)\) has any fixed joint distribution on \(\{0,+,-\}^2\) chosen before the initial error, and it is independent of that error. Define the worst-direction mean-square retention
\[
\rho(p)=\sup_{\|e\|_2=1}\mathbb E_p\|P_JP_Ie\|_2^2,\qquad P_i=I_2-a_i a_i^\mathsf T.
\]
The exact minimum over **all nine ordered-pair probabilities**, including repeats, is
\[
\rho_*(u)=\begin{cases}
\dfrac{u}{2},&0<u\le\dfrac14,\\[5pt]
\dfrac{u(1-u)(2u-1)^2}{u+(2u-1)^2(1-2u)},&\dfrac14<u<\dfrac12,\\[5pt]
u(2u-1)^2,&\dfrac12\le u<1.
\end{cases}
\]
The formulas agree at both boundaries. Put \(q(u)=\min\{u,(2u-1)^2\}\). For \(u<1/2\), every optimum has first-row probabilities
\[
\Pr(I=0)=t_*(u):=\frac{q(u)(1-2u)}{u+q(u)(1-2u)},\qquad
\Pr(I=+)=\Pr(I=-)=\frac{1-t_*(u)}2.
\]
If the first row is \(0\), the second row can be either leaf \(+\) or \(-\), arbitrarily. If the first row is a leaf, its unique optimal second row is \(0\) for \(u<1/4\) and the opposite leaf for \(1/4<u<1/2\); at \(u=1/4\) either of those second rows can be used. For \(u>1/2\), every optimum selects the first leaf uniformly from \(\{+,-\}\) and then the opposite leaf, never choosing the center row. At \(u=1/2\), every optimum chooses either leaf first with arbitrary mixture and then the opposite leaf; all such schedules solve the system exactly after two projections. Every optimum has zero probability of repeating a row.

The two thresholds mark distinct phenomena: at \(u=1/4\) the preferred successor of each leaf switches, and at \(u=1/2\) the center disappears from the first-step support. For example, at \(u=3/8\) the optimizer uses the center first with probability \(1/25\) even though a leaf-to-opposite-leaf pair is individually less correlated; its sharp retention \(3/80\) is strictly below the best deterministic pair's \(1/16\). At \(u=3/4\) the optimal retention is \(3/16\), versus \(11/18\) for two independent uniform row draws.

## Assumptions and scope
The row vectors above have unit norm and span \(\mathbb R^2\). The same consistent right-hand side \(b_i=a_i^\mathsf T x_*\) is used for each projection. The initial error \(e=x_0-x_*\) is otherwise unrestricted and deterministic. The pair distribution is fixed before \(e\) is chosen and may correlate the first and second labels, but may not use the current residual or initial error to adapt the row choices. The performance criterion is a **single two-update batch**, not the asymptotic rate of repeated batches, nor a noise floor or computation time. A fixed pair uses two projections whether or not a row repeats. The theorem concerns only this symmetric planar three-row family, and does not claim optimality for general matrices.

## Proof
**Projection reduction.** Each \(P_i\) is a rank-one orthogonal projector onto a line perpendicular to \(a_i\). For any two planar unit row normals,
\[
(P_jP_i)^\mathsf T(P_jP_i)=P_iP_jP_i=(a_i^\mathsf Ta_j)^2P_i.
\]
Consequently the positive-semidefinite mean-square matrix is
\[
M(p)=\sum_{i,j}p_{ij}(a_i^\mathsf Ta_j)^2P_i,
\qquad \rho(p)=\lambda_{\max}(M(p)).
\]
The three distinct pairwise squared inner products are \(u,u,(2u-1)^2\); repetition has squared inner product \(1\). Because \(0<u<1\), any repeated step is strictly dominated for its first row by choosing another row. The least possible conditional second-step squared overlap is \(q_0=u\) after the center and \(q_+=q_-=q(u)\) after a leaf.

**Universal lower bound and symmetry.** Let \(p_i=\Pr(I=i)\). Since every summand \(P_i\) is positive semidefinite,
\[
M(p)\succeq up_0P_0+q(u)(p_+P_++p_-P_-)=:M_0(p).
\]
Reflection across the first coordinate swaps \(+\) and \(-\). Averaging \(M_0(p)\) with its reflected conjugate and using convexity and reflection-invariance of the top eigenvalue gives
\[
\rho(p)\ge\max\{q(1-u)(1-t),\ ut+qu(1-t)\},\qquad t=p_0\in[0,1].
\]
The two scalar terms correspond to the horizontal and vertical entries, respectively, of the averaged matrix. The first term decreases strictly with \(t\); the second increases strictly, since \(u(1-q)>0\). When \(u<1/2\), the first term is larger at \(t=0\) and smaller at \(t=1\); their unique crossing is
\[
t_*=\frac{q(1-2u)}{u+q(1-2u)},\qquad
\rho_*=\frac{qu(1-u)}{u+q(1-2u)}.
\]
When \(u\ge1/2\), the vertical term is already the larger one at \(t=0\), so the unique minimizing first-center probability is \(t=0\), giving \(\rho_*=qu\). At \(u=1/2\) the latter is zero.

**Attainment and all equality cases.** Take the stated first-row probabilities, conditionally select a second row with squared overlap \(q_i\), and split the first-leaf probabilities equally. Then the mean-square matrix is diagonal and attains the lower bound. For \(u<1/2\), at the unique minimizing \(t\) its two diagonal entries coincide, so the matrix is exactly \(\rho_*I_2\). Any unequal first-leaf probabilities produce a nonzero off-diagonal entry and strictly increase the top eigenvalue. Any nonminimum conditional second-row choice adds a nonzero positive-semidefinite contribution and likewise increases the top eigenvalue. The center has two equally optimal leaf successors. If \(u>1/2\), the vertical quadratic form alone is at least \(u[q+(1-q)p_0]\), forcing \(p_0=0\) and minimum-overlap successors; the off-diagonal entry then forces equal first-leaf probabilities. If \(u=1/2\), zero contraction forces a first leaf followed by its orthogonal opposite leaf, but their first-step mixture can be arbitrary. Finally
\[
(2u-1)^2\le u \quad\Longleftrightarrow\quad u\in[1/4,1],
\]
which gives the two polynomial branches, the successor change, and the listed boundary ties. This proves the complete assertion for all \(0<u<1\).

## Verification
Run `python verify_three_line_kaczmarz.py` in an environment with NumPy and SciPy. The included checker recomputes the actual two-projection matrices for nine rational values of \(u\), compares their largest expected-error eigenvalues against the exact formulas, and independently solves nine linear programs with 360 initial-error directions each. It also tests the exact rational instances \(u=1/4,3/8,3/4\) and the uniform-IID comparison. The recorded outcome is `PASS 22 standalone exact/numeric checks; finite directional LP grid has 360 test angles`.

The finite angular grids supply sanity checks, not a proof for untested directions, parameters, or all joint laws. Those universal quantifiers are established by the positive-semidefinite reduction and one-dimensional lower bound above.

## Relationship to prior work
Randomized Kaczmarz, its exact mean-square analysis and optimized *independent* row probabilities are established topics. Haddock and Ma's **Greed Works** (arXiv:1912.03544; first public 2019-12-07) studies sampled residual-greedy Kaczmarz--Motzkin algorithms, convergence bounds and data-dependent selection rules, not minimization over arbitrary fixed joint ordered two-update laws on this three-line family. Sun, Gu and Tang (2020) sample candidate rows uniformly before a residual-greedy update and analyze convergence and computing cost, again a distinct optimization variable. Agaskar, Wang and Lu (2014) study exact MSE and row-probability optimization for standard randomized Kaczmarz; that paper is a relevant earlier risk, but its accessible abstract describes independent row sampling rather than arbitrary fixed two-row coupling.

Closely related publicly indexed results concern planar *independent-row asymptotic* optimal sampling, two-row *relaxed* projection coupling with prescribed marginals, and three-row sampling-greedy subset sizes. Their stated domains do not imply the complete arbitrary-joint-law two-step classification above. This is a comparison of mathematical assumptions and conclusions, not a proof of global publication priority.

## Limitations
No extension is claimed to more than two updates, nonplanar or nonsymmetric frames, error-adaptive row selection, or practical runtime advantage. The exact result does not assert that the optimal two-step law is optimal when blocks repeat. Earlier literature could contain an equivalent special-case derivation under different language; in particular a complete copy of the 2014 Agaskar--Wang--Lu work was not available for detailed comparison. Independent proof and historical-priority review have not been performed.

## References
1. J. Haddock and A. Ma, *Greed Works: An Improved Analysis of Sampling Kaczmarz--Motzkin*, arXiv:1912.03544 (first version 2019-12-07), https://arxiv.org/abs/1912.03544.
2. M.-L. Sun, C.-Q. Gu and P.-F. Tang, *On Randomized Sampling Kaczmarz Method with Application in Compressed Sensing*, Mathematical Problems in Engineering (2020), doi:10.1155/2020/7464212, https://onlinelibrary.wiley.com/doi/10.1155/2020/7464212.
3. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, GlobalSIP (2014), doi:10.1109/GlobalSIP.2014.7032145, https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b.
4. Z.-Z. Bai and W.-T. Wu, *On convergence rate of the randomized Kaczmarz method*, Linear Algebra and its Applications 553 (2018), 252–269, doi:10.1016/j.laa.2018.05.009.
