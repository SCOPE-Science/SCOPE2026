# Exact coextinction-rank covariance and a degree-invisible fourfold robustness-variance gap

## Finding

A secondary species in the standard binary knockout-extinction model disappears when its final primary-species neighbor is removed. The random extinction *rank* of two secondary species has an exact covariance controlled by their degrees and neighborhood intersection, and this covariance can have either sign. Consequently, the variability of the area under a single random-extinction survival curve is not determined by either guild's degree sequence, although its expectation is.

**Covariance theorem.** Fix integers \(n\ge1\) and nonempty sets \(A,B\subseteq\{1,\ldots,n\}\). Define \(a=|A|\), \(b=|B|\), \(c=|A\cap B|\), and \(u=a+b-c\). In a uniform random permutation of the primary vertices, let \(T_A\) and \(T_B\) be the positions at which the last elements of \(A\) and \(B\), respectively, are removed. Then

\[
\boxed{\operatorname{Cov}(T_A,T_B)=\frac{n+1}{(a+1)(b+1)}\left(\frac{c(n-u)}{u+2}-\frac{(a-c)(b-c)}{u+1}\right).}
\]

The sign is strictly negative if the neighborhoods are disjoint; for incomparable overlapping sets, the sign is precisely that of
\[
 c(n-u)(u+1)-(a-c)(b-c)(u+2).
\]
Equality and boundary cases are included. For example, when \(a=b=2\) and \(c=1\), the covariance is \(-1/36\) at \(n=4\) but \(1/10\) at \(n=5\), despite no change to the two local neighborhoods. For a single neighborhood, the formula gives
\[
\operatorname{Var}(T_A)=\frac{a(n-a)(n+1)}{(a+1)^2(a+2)}.
\]

**Robustness-variance consequence.** For \(m\ge1\) secondary species having nonempty neighborhoods \(A_1,\ldots,A_m\), define a realization-specific robustness statistic by averaging the surviving secondary fraction over each of the \(n+1\) stages, including the initial and final stages. Equivalently,
\[
 R_\pi=\frac1{m(n+1)}\sum_{i=1}^{m}T_{A_i}.
\]
The exact mean is the previously known degree-only identity
\[
\mathbb E[R_\pi]=\frac1m\sum_{i=1}^{m}\frac{|A_i|}{|A_i|+1},
\]
whereas the variance is
\[
 \operatorname{Var}(R_\pi)=\frac1{m^2(n+1)^2}\sum_{i=1}^{m}\sum_{j=1}^{m}\operatorname{Cov}(T_{A_i},T_{A_j}),
\]
with every summand explicitly evaluated by the covariance theorem.

For \(n=m=4\), compare two simple bipartite graphs, specified by the secondary-neighborhood lists

\[
\begin{aligned}
G_{\rm cycle}: &\quad \{1,2\},\{2,3\},\{3,4\},\{4,1\},\\
G_{\rm pairs}: &\quad \{1,2\},\{1,2\},\{3,4\},\{3,4\}.
\end{aligned}
\]

Every primary and secondary degree equals two in both graphs. The first is a single eight-cycle; the second comprises two disjoint four-cycles. Their robustness means are both \(2/3\), yet
\[
\operatorname{Var}(R_\pi;G_{\rm cycle})=\frac1{1800},\qquad
\operatorname{Var}(R_\pi;G_{\rm pairs})=\frac1{450}.
\]
The entire exact four-primary permutation distributions are
\[
\begin{array}{c|cc}
&\text{Robustness value}&\text{Number of permutations}\\\hline
G_{\rm cycle}&13/20&16\\
&7/10&8\\\hline
G_{\rm pairs}&3/5&8\\
&7/10&16
\end{array}
\]
(out of \(4!=24\) equally probable permutations). Their variance ratio is exactly four; no empirical data or numerical approximation enters this example.

## Assumptions and scope

The primary guild contains \(n\) distinguishable species, removed *without replacement* in one uniformly sampled complete order. The secondary guild contains \(m\) distinguishable species, each initially connected to at least one primary species. A secondary species goes extinct exactly when all its original primary neighbors are removed. Secondary loss neither triggers additional primary extinctions nor permits interaction rewiring, weighted-threshold rules, or new species. Neighborhoods may coincide. Randomness is solely the primary removal order; all moment statements are exact finite-population statements.

The area statistic here includes \(n+1\) equally weighted stages. This normalization matches the robustness convention stated in Jones, Zurell, and Wiesner (2024). Conventions omitting an endpoint rescale the variable and must be handled separately. For \(n=1\), deterministic ranks and zero variance are correctly captured.

## Proof

**Step 1: Realize the random permutation by continuous priorities.** Assign independent \(U_1,\ldots,U_n\sim\mathrm{Uniform}(0,1)\) and remove vertices in increasing priority order. With probability one all priorities are distinct. Write \(C=A\cup B\), \(u=|C|\), \(d=n-u\), \(\alpha=a-c\), and \(\beta=b-c\). Let \(J_A,J_B\) denote the positions of the last members of \(A,B\) in the *restricted order on \(C\)*; let \(M_A=\max_{i\in A}U_i\) and \(M_B=\max_{j\in B}U_j\). For each external vertex \(z\notin C\), define indicator variables \(X_z=\mathbf1\{U_z\le M_A\}\) and \(Y_z=\mathbf1\{U_z\le M_B\}\). Then exactly
\[
T_A=J_A+\sum_{z\notin C}X_z,\qquad T_B=J_B+\sum_{z\notin C}Y_z.
\]

**Step 2: Covariance within the union.** The restricted maximum positions can be written
\[
J_A=a+\sum_{y\in B\setminus A}\mathbf1\{U_y\le M_A\},\qquad
J_B=b+\sum_{x\in A\setminus B}\mathbf1\{U_x\le M_B\}.
\]
For any such pair \(x,y\), the events \(U_y>M_A\) and \(U_x>M_B\) cannot both occur, because the former implies \(U_y>U_x\) and the latter implies \(U_x>U_y\). Their individual probabilities are \(1/(a+1)\) and \(1/(b+1)\), respectively, by exchangeability among the corresponding augmented subsets. The covariance of the two complementary indicators is therefore exactly \(-1/[(a+1)(b+1)]\). Summing over all \(\alpha\beta\) ordered pairs gives
\[
C_0:=\operatorname{Cov}(J_A,J_B)=-\frac{(a-c)(b-c)}{(a+1)(b+1)}.
\]

**Step 3: Continuous-maxima moments.** On \(0\le s\le t\le1\), independence of vertex priorities gives
\[
\Pr(M_A\le s,M_B\le t)=s^a t^{b-c},
\]
and on \(0\le t\le s\le1\) the analogous joint distribution is \(s^{a-c}t^b\). Integrating the joint distribution over the two triangles and subtracting marginal products yields
\[
C_M:=\operatorname{Cov}(M_A,M_B)=\frac{c}{(a+1)(b+1)(u+2)}.
\]
The same joint distribution yields
\[
D:=\mathbb E[\min(M_A,M_B)-M_AM_B]
=\frac1{u+1}-\frac{1/(a+1)+1/(b+1)}{u+2}.
\]
Given the restricted ordering of the \(u\) union priorities, the expected value of its \(j\)-th order statistic is \(j/(u+1)\); hence
\[
\operatorname{Cov}(J_A,M_B)=\operatorname{Cov}(J_B,M_A)=\frac{C_0}{u+1}.
\]
This last equality follows from conditioning on the restricted ordering and using independence of that ordering from the ordered priority values.

**Step 4: Add outside vertices.** Conditioned on all priorities in \(C\), the \(d\) outside priority pairs of indicators are independent across outside vertices, have conditional expectations \(M_A,M_B\), and within each vertex have conditional covariance \(\min(M_A,M_B)-M_AM_B\). The law of total covariance applied to the decomposition in Step 1 gives
\[
\operatorname{Cov}(T_A,T_B)=C_0\left(1+\frac{2d}{u+1}\right)+d^2C_M+dD.
\]
Substitute the three expressions from Steps 2–3, use \(d=n-u\), and collect rational terms; the result is precisely the displayed covariance formula. No asymptotic approximation is used.

**Step 5: Area and example.** Species with last-neighbor removal at rank \(T_A\) survives exactly the stages \(0,1,\ldots,T_A-1\), hence contributes \(T_A\) unit steps to the survival-area sum. Linearity gives the mean and the pair-covariance sum gives the variance. The two eight-vertex networks have the listed neighborhood sets and hence identical degree sequences. Direct substitution gives their exact variances. Alternatively, evaluating each of the \(4!=24\) removal orders produces the two stated discrete distributions; both methods agree.

## Verification

The self-contained Python 3 standard-library program `verify.py` checks the covariance formula against direct enumeration of every primary removal permutation, for every feasible degree/overlap quadruple with \(1\le n\le7\), including equal, nested, overlapping, and disjoint neighborhoods. It separately checks the diagonal variance formula, sign boundaries, both complete four-vertex robustness distributions, and their exact means and variances using `fractions.Fraction`. On direct execution it reports `PASS 707 exact rational checks`. This exhaustive verification is limited to \(n\le7\) and does not replace the all-size proof in Steps 1–5. The general algebraic simplification was also checked independently with exact symbolic rational algebra.

## Relationship to prior work

Memmott, Waser, and Price (first published online December 6, 2004) introduce the ecological random primary-extinction and secondary-loss model. Pastor, Santamaría, Méndez, and Galeano (2012) simulate topological robustness effects and average random extinction trajectories. Bane, Pocock, and James (2018) analyze *distributions* of robustness over random extinction sequences and network models, so the existence of distributional variability is explicitly prior work. Jones, Zurell, and Wiesner (2024), Equations (10)–(12), already establish the general degree-only *expected* robustness and explicitly mention standard deviations as a possible future analytical direction. Those prior contributions are not claimed here.

The particular new mathematical target is the signed pairwise covariance for last-neighbor extinction ranks as a function of overlap and the resulting exact variance formula, with the matched-degree eight-cycle versus two-four-cycle separation. The inspected full primary texts do not state or imply these formulas from their published conclusions without a further joint-probability computation. The novelty conclusion is limited by the literature inspected; no claim of exhaustive historical uniqueness or external certification is made.

## Limitations

The result concerns one fixed unweighted bipartite network and uniformly random *full* primary removal orders. It does not address secondary feedback, species recovery, biased targeting, correlated primary risks, or alternative extinction thresholds. It quantifies randomness from the extinction order only, not ecological parameter uncertainty or stochastic population dynamics. The exact mean identity is known, and the pair-covariance computation could conceivably have appeared in historical probability or ecological-network work under different terminology. Independent audit has not been performed.

## References

- Memmott, J., Waser, N. M., and Price, M. V. (2004). *Tolerance of pollination networks to species extinctions*. Proceedings of the Royal Society B. Published online December 6, 2004. DOI: https://doi.org/10.1098/rspb.2004.2909 ; full text: https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf
- Pastor, J. M., Santamaría, S., Méndez, M., and Galeano, J. (2012). *Effects of topology on robustness in ecological bipartite networks*. Networks and Heterogeneous Media 7, 429–440. https://doi.org/10.3934/nhm.2012.7.429
- Bane, M. S., Pocock, M. J. O., and James, R. (2018). *Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness*. Ecology and Evolution 8, 10794–10804. https://doi.org/10.1002/ece3.4529 ; accessible full text: https://nora.nerc.ac.uk/id/eprint/521791/1/N521791JA.pdf
- Jones, C., Zurell, D., and Wiesner, K. (2024). *Novel analytic methods for predicting extinctions in ecological networks*. Ecological Monographs 94, e1601. https://doi.org/10.1002/ecm.1601
