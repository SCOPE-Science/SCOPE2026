# A universal cyclic-overlap optimum for capacity-limited mutualist survival

## Finding

Let \(d\ge3\) be an integer. Consider three plants \(A,B,C\) and exactly \(m=3d-3\) distinct active pollinator-service units. The potential-interaction graph is simple and bipartite; each plant has exactly \(d\) pollinator partners, and every pollinator has at least one plant partner. Independently, each pollinator survives with probability \(1-q\), where \(0<q<1\). After these losses the system is **fully served** if the surviving interaction graph contains a matching covering all three plants: each plant receives one distinct surviving pollinator and no pollinator is assigned twice.

Among every such fixed network, full-service reliability is uniquely maximized up to relabeling by the **triangle-sharing design**: one distinct pollinator is shared by each pair \(AB,AC,BC\), no pollinator is shared by all three plants, and each plant has \(d-2\) private partners. Its exact maximum is

\[
R_\triangle(q,d)=1-3q^d+3q^{2d-2}(2q-1)-q^{3d-5}(3-9q+7q^2).
\]

The optimal incidence structure is independent of \(q\) throughout \((0,1)\). At the excluded deterministic endpoints \(q=0\) and \(q=1\), every design in the specified class has reliability one and zero, respectively; strict uniqueness is therefore not asserted there.

## Assumptions and scope

All units have equal independent survival probability, each plant has the same fixed potential degree, and no unlinked pollinator units are counted toward \(m\). A surviving unit can supply at most one plant. Potential links remain fixed; matching is an idealized post-loss allocation decision, not a model of population dynamics, seasonal partner discovery, or actual service levels. The theorem does not cover unequal failure rates, unequal plant degrees, multiple-unit demands, or unconstrained pollinator service capacities.

## Proof

**1. Exhaustive overlap types.** For each pollinator let its incidence degree be the number of plants it can serve. The total degree of the pollinators is \(3d\), while there are \(3d-3\) nonisolated pollinators. Hence

\[
\sum_{v\text{ pollinator}}(\deg(v)-1)=3.
\]

Since a pollinator degree lies in \(\{1,2,3\}\), either exactly three pollinators have degree two and the rest degree one, or one pollinator has degree three and one has degree two. Up to permuting the three plant labels, the possible incidences shared by more than one plant are precisely: \(T=(AB,AC,BC)\); \(D=(AB,AB,AB)\); \(S=(AB,AB,AC)\); and \(H=(ABC,AB)\). In each case the private pollinators are uniquely determined by the degree \(d\). All four are feasible for every \(d\ge3\), and there are no other incidence types.

**2. Exact Hall counting.** For each nonempty set \(U\subseteq\{A,B,C\}\), let \(n_U\) be the number of pollinators adjacent to exactly the plants in \(U\). In a random surviving set, let \(K_U\) count the surviving pollinators of this type. The \(K_U\) are independent with \(K_U\sim\operatorname{Binomial}(n_U,1-q)\). Hall's condition says that a full matching exists if and only if, for every nonempty plant subset \(S_0\),

\[
\sum_{U:\,U\cap S_0\ne\varnothing}K_U\ge |S_0|.
\]

This is a finite, exhaustive condition covering all seven nonempty plant subsets. It gives an exact coefficient-extraction formula: form

\[
F(\mathbf x)=\prod_{\varnothing\ne U\subseteq\{A,B,C\}}\bigl(q+(1-q)x_U\bigr)^{n_U},
\]

and sum only coefficients of monomials \(\prod_U x_U^{k_U}\) whose exponent vector meets the seven Hall inequalities. Thus no independence assumption beyond the specified pollinator losses enters the matching calculation.

For explicit evaluation, write \(n=d-3\) and \(z=q^n\). Once the two or three shared pollinators are fixed as alive or dead, the remaining private survivor counts have sizes \(n+a\), with \(a\in\{0,1,2,3\}\). Hall's condition depends on each such count only through \(0,1,2,\ge3\), whose probabilities are respectively

\[
q^{n+a},\quad (n+a)(1-q)q^{n+a-1},\quad \binom{n+a}{2}(1-q)^2q^{n+a-2},\quad 1-\text{the preceding three}.
\]

Terms with an impossible count are interpreted as zero. Multiplying these finite-category probabilities by the Bernoulli probabilities of the shared units, and applying the seven Hall inequalities, produces the following exact reliability for the triangle type:

\[
R_T=1-3q^3z+(-3q^4+6q^5)z^2+(-3q^4+9q^5-7q^6)z^3.
\]

For the remaining three incidence types, the same exhaustive calculation yields the more informative factorizations

\[
\begin{aligned}
R_T-R_D &=q^2z^2(1-q)^2\bigl[3(1-q^2z)+2q(1-q)\bigr],\\
R_T-R_S &=q^3z^2(1-q)^2\bigl[2-q(1+z)\bigr],\\
R_T-R_H &=2q^3z^2(1-q)^2(1-qz).
\end{aligned}
\]

**3. Strict optimality.** For \(d\ge3\), \(0<q<1\) implies \(0<z=q^{d-3}\le1\). Every displayed difference is strictly positive: in particular \(q(1+z)<2\), \(qz<1\), and \(q^2z<1\). The exhaustive four-type classification proves uniqueness up to relabeling. Substituting \(z=q^{d-3}\) into \(R_T\) gives the stated maximum formula.

## Verification

The supplied `verification/check.py` constructs all four shared-incidence types directly and independently evaluates the symbolic Hall-condition sum using truncated private-survivor counts. It verifies the optimal probability and three factorized difference identities as exact symbolic equalities. Separately, it enumerates all pollinator survival subsets for every type and each \(d\in\{3,4,5,6\}\), checking the exact reliability polynomials and coefficientwise inequalities. Finally, it examines all \(500\) distinct plant-row-unlabeled, pollinator-labeled spanning networks for the \(d=3\), six-pollinator case. All \(532\) targeted verification cases passed on the included script. To reproduce, install `requirements.txt` and run `python verification/check.py` from this package's root.

For the smallest case \(d=3\) and \(q=1/2\), the triangle reliability is \(39/64\); the respective values for the concentrated-pair, two-plus-one, and core-plus-pair types are \(28/64\), \(37/64\), and \(37/64\).

## Relationship to prior work

Kaiser-Bunbury et al. (2010) study species-removal robustness and temporal rewiring in empirical pollination networks; their stated extinction rule removes a species when it loses its partners, rather than requiring a **distinct** pollinator for every surviving plant. Dietzfelbinger and Rink (2012) optimize left-degree distributions in random bipartite graphs, not fixed spanning incidence designs exposed to independent right-vertex failures. Bane, Pocock and James (2018) examine ecological knockout and propagating-extinction robustness measures; their network outcome is not post-loss matching feasibility. All three motivate related questions, but the inspected results do not imply this four-type, all-degree, all-failure-probability optimizer classification.

Abstractly, the event is a rank-three transversal-matroid spanning event, and Hall's classical theorem supplies its exact feasibility test. That reformulation alone does not determine which degree-constrained representation maximizes the event probability.

## Limitations

This is an exact theorem for a deliberately idealized capacity-one service-allocation model, not an ecological prediction about actual pollinator species. Real pollinators may service many plant species; allowing unlimited capacity changes the event and can change which interaction structure is optimal. Historical novelty is supported only by the stated comparisons, not independently certified; specialized reliability and transversal-matroid literature may contain equivalent results. Finite enumeration was used as a reproducibility check and not as proof for unbounded \(d\).

## References

- Kaiser-Bunbury, C. N., Muff, S., Memmott, J., Müller, C. B. and Caflisch, A. (2010). *The robustness of pollination networks to the loss of species and interactions: a quantitative approach incorporating pollinator behaviour.* Ecology Letters 13, 442–452. First published 2010-03-15. https://doi.org/10.1111/j.1461-0248.2009.01437.x ; open author PDF https://www.biochem-caflisch.uzh.ch/sites/default/files/publist/pdfs/smuff10.pdf
- Dietzfelbinger, M. and Rink, M. (2012). *Towards Optimal Degree-distributions for Left-perfect Matchings in Random Bipartite Graphs.* First arXiv version 2012-03-07. https://arxiv.org/abs/1203.1506
- Bane, M. S., Pocock, M. J. O. and James, R. (2018). *Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness.* Ecology and Evolution 8, 10794–10804. https://doi.org/10.1002/ece3.4529 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6262911/
