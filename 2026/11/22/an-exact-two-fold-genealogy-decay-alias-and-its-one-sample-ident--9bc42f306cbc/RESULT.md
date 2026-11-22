# An exact two-fold genealogy-decay alias and its one-sample identification repair

## Finding

In the conditional three-event offspring likelihood of the finite-depth genealogical-reinforcement model, full rank of the observed relative-count vectors does **not** guarantee global identification of the baseline, reinforcement strength, and genealogical decay rate. A simultaneously realizable binary genealogy with truncation depth \(D=3\) has the count rows (for living relatives at distances \(2,4,6\))

\[
C=\begin{pmatrix}0&0&1\\1&0&3\\1&1&1\end{pmatrix},\qquad \det C=1.
\]

Write \(t=e^{-2\theta}\in(0,1)\), where \(\theta>0\). For **every** \(t\in(0,1/2)\) except \(t_c=(\sqrt6-2)/2\), there are exactly two distinct admissible parameter triples giving the same three offspring distributions. The second decay base is

\[
s=\frac{1-2t}{2(1+t)}.
\]

At \(t=t_c\), the two branches coalesce and the three-event Fisher information is singular. For \(t\in[1/2,1)\), the triple is globally identifiable conditional on this design. A fourth individual, with the simultaneously realizable count row \((1,0,0)\), restores global structural identifiability for **every** \(t\in(0,1)\), including the singular point. Here identification always refers to the exact family of conditional offspring probability distributions given the observed pre-branching genealogy, not recovery from one noisy realization or identification of the law of an unobserved complete population history.

## Assumptions and scope

Fix a generation of a rooted genealogical tree whose vertices have at most two children. Each living vertex produces \(\xi(v)\sim\operatorname{Binomial}(2,p_v)\), conditionally independently given the current tree, where

\[
\operatorname{logit}(p_v)=\beta_0+\beta_1\sum_{\substack{u\ne v\text{ living}\\d(u,v)\le 6}}e^{-\theta d(u,v)},\quad \beta_0\in\mathbb R,\ \beta_1>0,\ \theta>0.
\]

All living vertices are at the same generation, so relevant distances are \(2,4,6\). The observed sample comprises three named living individuals and their subsequent offspring counts; a fourth named vertex is available for the repair. Their local count vectors are treated as known design data. Structural identifiability means injectivity of the map from \((\beta_0,\beta_1,\theta)\) to the corresponding conditional Binomial probability laws. It is not a claim about unconstrained model trajectories, unobserved ancestor probabilities, or finite-sample estimator uniqueness.

An explicit feasible genealogy has living individuals represented by the following depth-five binary paths from a common root (each character is one edge to a left or right child):

```
00000 00100
01000 01001 01100 01101 01110
10000 10001 10010 10100
11000 11001
```

The three sampled individuals are `00000`, `01000`, `10000`; the fourth is `11000`. All other depth-five leaves are living but need not have their next branching events observed. Every prefix has at most two distinct child prefixes. Relatives from different depth-two prefix families have genealogical distance at least eight, so contribute nothing at \(D=3\). The four count rows are, in order, \((0,0,1),(1,0,3),(1,1,1),(1,0,0)\). This finite tree has positive probability under any finite admissible parameter triple because all individual offspring probabilities lie strictly between zero and one.

## Proof

**1. Reduction to a one-dimensional shape curve.** Set \(t=e^{-2\theta}\) and write \(\eta_i=\operatorname{logit}(p_i)\). For the first three rows, the genealogy-weighted totals are

\[
g_1=t^3,\qquad g_2=t+3t^3,\qquad g_3=t+t^2+t^3.
\]

Thus \(\eta_i=\beta_0+\beta_1g_i(t)\). Since \(\beta_1>0\), the difference \(\eta_2-\eta_1=\beta_1t(1+2t^2)\) is strictly positive. Eliminating the offset and scale by a ratio gives the observable invariant

\[
R(t)=\frac{\eta_3-\eta_1}{\eta_2-\eta_1}=\frac{1+t}{1+2t^2}.
\]

For \(s,t\in(0,1)\), direct cross multiplication gives

\[
R(s)=R(t)\quad\Longleftrightarrow\quad (s-t)[1-2(t+s+st)]=0.
\]

Hence every alternative to \(s=t\) must equal \(F(t)=(1-2t)/(2(1+t))\); it is admissible precisely for \(0<t<1/2\). The two roots coincide only if \(2t^2+4t-1=0\), or \(t=t_c=(\sqrt6-2)/2\). Therefore the first-three-event map is two-to-one exactly for \(t\in(0,1/2)\setminus\{t_c\}\), and one-to-one at the remaining individual parameters. This is a classification of the fiber at each parameter, not a statement that the map is globally injective over the whole parameter domain.

**2. Reconstruction of both admissible triples.** Given \(s=F(t)\), define

\[
\beta_1'=\beta_1\frac{t(1+2t^2)}{s(1+2s^2)}>0,\qquad
\beta_0'=\beta_0+\beta_1t^3-\beta_1's^3.
\]

The first equation matches the positive logit gap between rows two and one; the second matches row one; equality of \(R\) then matches row three. The logistic function is injective, so the three sets of Binomial probabilities, hence every conditional joint offspring-count likelihood for the three sampled vertices, are identical. Conversely, equality of all three conditional Binomial laws forces equality of the logits and of \(R\), so no other alternative exists.

For an exact instance, choose \(t=1/5\), \(\beta_0=0\), \(\beta_1=1\). Then \(s=1/4\), \(\beta_0'=-1/250\), \(\beta_1'=96/125\). The decay rates are \(\theta=(\log5)/2\) and \(\theta'=\log2\), and both triples yield precisely the three logits \((1,28,31)/125\). All three probabilities are distinct despite the two-fold ambiguity.

**3. Local rank at the fold.** Let \(J=\partial(\eta_1,\eta_2,\eta_3)/\partial(\beta_0,\beta_1,\theta)\). Since \(dt/d\theta=-2t\), the explicit determinant is

\[
\det J=2\beta_1t^3(2t^2+4t-1).
\]

The conditional Fisher information is \(J^{\mathsf T}WJ\), with diagonal weights \(W_{ii}=2p_i(1-p_i)>0\). It is singular exactly when \(t=t_c\), and otherwise positive definite. Thus a full-rank count matrix alone does not even ensure nonsingular local information at every admissible parameter.

**4. A fourth, simultaneously feasible observation resolves the alias.** For count vector \((1,0,0)\), the fourth genealogical total is \(g_4=t\). Its logit gap relative to the first row yields

\[
Q(t)=\frac{\eta_4-\eta_1}{\eta_2-\eta_1}=\frac{1-t^2}{1+2t^2},\qquad Q'(t)=-\frac{6t}{(1+2t^2)^2}<0.
\]

Thus the four conditional distributions determine \(t\) uniquely over \((0,1)\), including \(t_c\). The strictly positive second-row gap then determines \(\beta_1\), and the first-row logit determines \(\beta_0\). This proves global identifiability for the augmented four-individual design. At the exact two-fold example, the fourth logits differ by \(3/250\), so the repair is substantive rather than a formally redundant observation.

## Verification

The standalone `CHECK.py` constructs the simultaneous rooted binary tree using depth-five paths, independently computes recent-common-ancestor distances, verifies all four relative-count vectors and \(\det C=1\), and checks the exact \(t=1/5\) versus \(s=1/4\) likelihood alias. It tests 49 additional rational decay bases below \(1/2\), confirms the fourth observation distinguishes the two branches, and compares its identification ratio over an ordered rational grid. Run:

```
python CHECK.py
```

The universal assertions rely on the displayed algebraic factorization and strict derivative; finite grid checks are supplementary, not substitutes for those proofs.

## Relationship to prior work

Kochocki's *Genealogical Reinforcement in Branching Processes*, arXiv:2611.08548v1 (first public November 5, 2026), introduces the truncated exponential kinship contribution and the conditional Binomial likelihood. Section 4, Theorem 1(b) asserts global structural identifiability from three linearly independent nonzero count vectors spanning three distances; Appendix A asserts nonsingular Fisher information under this condition. The present realizable design satisfies those stated counting conditions but exhibits an open-set, exact two-fold ambiguity and a singular fold. It therefore gives a precise counterexample **for the stated three-event conditional likelihood**, together with an alternative one-observation repair, rather than re-establishing the paper's general branching-process results.

General structural-identifiability literature already distinguishes local from global identifiability and uses extra observations to resolve parameter aliases. Alsammani (2026), for example, treats unrelated ODE and pharmacokinetic models with parameter exchange symmetries. The known general methodology does not directly supply the genealogically feasible count design, its exact rational alias, or the sharp added-relative repair for this Binomial branching model. No general claim of a new identifiability methodology is made.

## Limitations

This statement concerns three (or four) **selected conditional branching events**, with known genealogy, not the marginal likelihood of a complete unobserved ancestral history or the joint law from repeated full tree realizations. Observing additional branches or generations can distinguish the aliased triples. A single realized offspring count per sampled vertex is noisy, so structural identifiability with four observations does not imply accurate practical estimation. The example uses depth three and a particular feasible tree; the one-to-one / two-to-one classification applies to this design, not all binary genealogies. Unindexed equivalent nonlinear-design examples may exist. No independent validation is claimed.

## References

- A. Kochocki, *Genealogical Reinforcement in Branching Processes* (2026), arXiv:2611.08548v1, https://arxiv.org/html/2611.08548v1 ; especially equations (2), (3), (6), Section 4, and Appendix A. First publicly posted November 5, 2026.
- A. Alsammani, *A Tutorial on Symbolic Structural Identifiability Analysis of ODE Models in Julia*, *Bulletin of Mathematical Biology* **88**, article 212 (2026), https://doi.org/10.1007/s11538-026-01779-0 ; Sections 2 and 4.3 (general local/global distinction and observation design, not the present genealogy model).
