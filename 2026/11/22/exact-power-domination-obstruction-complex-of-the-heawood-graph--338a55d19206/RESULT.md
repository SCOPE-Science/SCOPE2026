# The power-domination obstruction complex of the Heawood graph

## Finding

Let \(H\) be the fourteen-vertex point–line incidence graph of the Fano plane. A vertex set \(S\subseteq V(H)\) power dominates \(H\) if and only if it is not contained in any closed neighborhood \(N_H[v]\). The fourteen closed neighborhoods are therefore exactly the maximal unsuccessful sets. The complete power-domination polynomial is
\[
\mathcal P_H(z)=(1+z)^{14}-(1+14z+63z^2+56z^3+14z^4).
\]
In particular, every set of five or more vertices succeeds. The distinct contribution is the classification at all cardinalities and its polynomial, not the classification or reconfiguration of minimum pairs.

## Assumptions and scope

Write the Fano points as \(p_i\) and the lines as \(\ell_j\), with indices in \(\mathbb Z/7\mathbb Z\). In \(H\), \(p_i\sim\ell_j\) exactly when \(j-i\in\{0,1,3\}\). Each pair of distinct points determines a unique line, and each pair of distinct lines has a unique intersection point. The ordinary power-domination rule first observes \(N_H[S]\), then repeatedly lets any observed vertex with exactly one unobserved neighbor observe that neighbor. Success means that all vertices are eventually observed. The coefficient of \(z^m\) in \(\mathcal P_H\) counts successful labelled sets of size \(m\).

## Proof

**Sufficient configurations.** A nonincident point–line pair \(\{p,\ell\}\) initially observes itself, the three lines through \(p\), and the three points on \(\ell\). Each observed line through \(p\) has exactly one unobserved point neighbor, and the resulting three forces observe distinct points because two lines through \(p\) have no other common point. Dually, the three points on \(\ell\) observe the three remaining lines. Thus the pair succeeds.

Three noncollinear points also succeed. In the model over \(\mathbb F_2\), such triples are ordered bases after choosing their order, so the projective linear group takes any noncollinear triple to \(\{p_0,p_1,p_2\}\). This triple initially observes itself and \(\ell_0,\ldots,\ell_5\). The lines \(\ell_1,\ell_2,\ell_3\) force \(p_5,p_6,p_3\), respectively. Then \(\ell_4\) forces \(p_4\), and \(p_3\) forces \(\ell_6\). By point–line duality any three nonconcurrent lines also succeed.

**Exhaustion.** If a set lacks all three sufficient configurations, it is contained in a closed neighborhood. For a set on one shore, this follows because any two distinct selected points determine a line that must contain every further selected point, or dually for lines; a set with at most one selected vertex is immediate. For a mixed set, all its selected points are incident with all its selected lines. If just one line is selected, its closed neighborhood contains the set. If at least two lines are selected, their common point must be the only selected point and all selected lines must contain it. The closed neighborhood of that point then contains the set.

**Failure and counting.** With initial sensors \(N_H[p]\), for a point \(p\), the first observation step sees all seven points and the three lines through \(p\). Four lines remain unobserved, and every point other than \(p\) has two unobserved line neighbors. No force is possible. The line-centered case is dual. Power domination is monotone under adding sensors: one can follow an earlier sequence of forces, skipping any target already observed, since every not-yet-observed target will still be the unique unobserved neighbor of its forcing vertex. Thus every subset of a closed neighborhood fails, whereas a set containing one of the sufficient configurations succeeds. This proves the classification. The closed neighborhoods have size four and are distinct. Closed neighborhoods of opposite shores can overlap only in the two centers and only when adjacent; two same-shore centers share only their unique common neighbor. Thus no triple is in two closed neighborhoods. The failed pairs are the 21 incident point–line pairs and the 42 same-shore pairs. The failed triples number \(14\binom43=56\); the failed quadruples are the fourteen closed neighborhoods. Counting the empty set and the fourteen singletons gives the stated polynomial by subtraction from \((1+z)^{14}\).

## Verification

The supplied `verify_geometry.py` and `verify_bitmask.cpp` use set-based and bitmask implementations, respectively, of the observation rule. Both enumerate all \(16{,}384\) subsets and compare failure with closed-neighborhood containment. The Python program additionally checks the known minimum-pair and exchange-graph counts. These computations concern this finite graph only; the proof above derives the classification directly.

## Relationship to prior work

Haynes et al. introduced graph power domination, Dorbec et al. study generalized power domination on regular graphs, and Brimkov et al. introduce the power-domination polynomial. The related record *Antiflag mobility and the two-sensor boundary in projective-plane incidence networks* establishes that exactly the 28 nonincident point–line pairs are minimum in the Fano plane and gives their token-jump reconfiguration graph, including degree six and diameter three. It also determines the two-sensor boundary for projective planes of all orders. The two records are dated the same day; this comparison does not infer precedence. The present classification instead specifies exactly which sets of every cardinality fail, including the maximal unsuccessful four-sets. The minimum-pair result alone does not decide whether a set containing no successful pair is successful; for example, it cannot distinguish collinear and noncollinear point triples.

## Limitations

The classification applies specifically to the Fano incidence graph with the ordinary closed-neighborhood power-domination convention. It does not assert corresponding obstruction complexes for other projective planes or different propagation rules. This comparison does not establish historical priority.

## References

1. T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi and M. A. Henning, *Domination in Graphs Applied to Electric Power Networks*, SIAM J. Discrete Math. **15** (2002), 519–529, https://doi.org/10.1137/S0895480100375831.
2. P. Dorbec, M. A. Henning, C. Löwenstein, M. Montassier and A. Raspaud, *Generalized Power Domination in Regular Graphs*, SIAM J. Discrete Math. **27** (2013), 1559–1574, https://doi.org/10.1137/120891356.
3. B. Brimkov, R. Patel, V. Suriyanarayana and A. Teich, *Power Domination Polynomials of Graphs*, https://arxiv.org/abs/1805.10984.
4. *Antiflag mobility and the two-sensor boundary in projective-plane incidence networks*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-antiflag-mobility-and-the-two-sensor-boundary-in-projective-plan--cd43734a0963/RESULT.md.
