# Exact power-domination obstruction complex of the Heawood graph

## Finding
Let \(H\) be the fourteen-vertex point–line incidence graph of the Fano plane. A vertex set \(S\subseteq V(H)\) is a power-dominating set **if and only if** it is not contained in the closed neighborhood \(N_H[v]\) of any vertex \(v\). Thus the fourteen four-vertex closed stars are precisely the inclusion-maximal unsuccessful sensor sets, and the complete power-domination polynomial is
\[
\mathcal P_H(z)=(1+z)^{14}-(1+14z+63z^2+56z^3+14z^4).
\]
In particular, \(\gamma_P(H)=2\), exactly \(28\) two-vertex sets succeed (the nonincident point–line pairs), and every set of five or more vertices succeeds. The exchange graph of the \(28\) minimum sets, with adjacency for a single sensor replacement, is connected, six-regular, has \(84\) edges and diameter \(3\).

## Assumptions and scope
Let the Fano points be \(p_i\), and its lines \(\ell_j\), for \(i,j\in\mathbb Z/7\mathbb Z\). Define incidence by \(p_i\sim\ell_j\) exactly when \(j-i\in\{0,1,3\}\pmod 7\). There are no edges within a point shore or within a line shore. The difference-set property gives one joining line for each pair of points and one intersection point for each pair of lines. Thus \(H\) is the Heawood graph, a connected cubic graph of girth six.

For an initial selected set \(S\), the domination step observes \(N_H[S]\), and each subsequent forcing step observes any unique unobserved neighbor of an observed vertex. Iterate until no vertex can be added. A set is power dominating when the result is all fourteen vertices. A successful two-vertex set is *minimum* because no singleton is successful. Counts refer to distinct labeled subsets, not automorphism orbits. The exchange graph has vertices the minimum sets and joins two sets when their intersection has size one.

## Proof
**1. Two sufficient configurations.** A nonincident point–line pair \(\{p,\ell\}\) observes itself, the three lines through \(p\), and the three points on \(\ell\): eight distinct vertices. Each observed line through \(p\) has exactly one unobserved point neighbor, and each observed point on \(\ell\) has exactly one unobserved line neighbor. All six remaining vertices are forced in one round, proving such a pair succeeds.

Any three noncollinear Fano points also succeed. The projective linear group on \(\mathbb F_2^3\) takes any ordered noncollinear point triple to any other because the triples are ordered vector-space bases. It therefore suffices to check \(\{p_0,p_1,p_2\}\), which is noncollinear for the specified incidence. Its domination step observes the points \(\{p_0,p_1,p_2\}\) and the lines \(\{\ell_0,\ell_1,\ell_2,\ell_3,\ell_4,\ell_5\}\). Its next wave forces \(p_3,p_5,p_6\), and the following wave forces \(p_4,\ell_6\); all vertices are then observed. By point–line duality, any three nonconcurrent Fano lines likewise succeed. These assertions use the ordinary unique-unobserved-neighbor rule; the exact wave sets can be checked directly from the displayed incidence relation.

**2. Exhaustiveness.** If a selected set \(S\) contains a nonincident point–line pair or a noncollinear point triple or a nonconcurrent line triple, the monotonicity of the power-domination process makes \(S\) successful. Suppose none of the three configurations is present. If \(S\) contains only points, then every three of them are collinear. Any two distinct Fano points determine a unique line, so all selected points lie on one line, with at most three selected; hence \(S\subseteq N_H[\ell]\) for that line. The dual argument covers line-only sets. If both shores meet \(S\), every selected point is incident with every selected line. With only one selected line, all selected points lie on it, and \(S\subseteq N_H[\ell]\). With at least two selected lines, their unique intersection is the only possible selected point, so all selected lines pass through this point and \(S\subseteq N_H[p]\). This also covers the empty set. Thus every set lacking the three sufficient configurations lies in some closed star.

**3. Each closed star fails.** Fix a point \(p\). Starting from the four vertices in \(N_H[p]\), the domination step observes all seven points and exactly the three lines through \(p\). Each of the remaining four lines is unobserved. The point \(p\) has no unobserved neighbor, while each other observed point has two unobserved line neighbors. No force is possible. The argument for a line-centered closed star is dual. Since unsuccessful sets are downward closed, precisely the subsets of closed stars are unsuccessful. Distinct closed stars intersect in at most two vertices: Heawood's girth six excludes common neighborhoods of size three. All fourteen stars have size four, so they are distinct and inclusion-maximal.

**4. Exact polynomial and optimum configurations.** Unsuccessful sets comprise the empty set (one); singletons (fourteen); pairs of adjacent vertices (twenty-one) or pairs at distance two (forty-two); triples (fourteen stars times four choices, or fifty-six); and the fourteen full stars. The triple count has no overcount because two closed stars meet in at most two vertices. There are no larger failures. Subtracting from \((1+z)^{14}\) gives the polynomial displayed in the finding. Every singleton is unsuccessful. There are \(\binom{14}{2}-63=28\) successful pairs, precisely the four nonincident lines available to each of seven points.

**5. Exchange geometry.** Let \(Q\) be the bipartite graph whose edges are the \(28\) nonincident point–line pairs. Each of its fourteen vertices has degree four. The exchange graph is the line graph \(L(Q)\), so it is six-regular on twenty-eight vertices and has \(28\cdot6/2=84\) edges. Two disjoint edges \((p,\ell)\) and \((q,m)\) of \(Q\) lie at distance two in \(L(Q)\) if either crossed pair \((p,m)\) or \((q,\ell)\) is nonincident. Otherwise, the unique joining line for \(p,q\) meets both, and there are exactly two Fano lines \(n\) that contain neither point. Thus \((p,n)\), \((q,n)\) form a length-three exchange path. Hence the diameter is at most three, and connectivity follows. For the two edges \((p_0,\ell_2)\) and \((p_1,\ell_0)\), both crossed point–line pairs are incident, so their exchange distance is three. Therefore the diameter is exactly three.

## Verification
Two independently constructed finite enumeration programs, `verify_geometry.py` and `verify_bitmask.cpp`, reconstruct the Heawood graph from the seven incidence residues and examine every one of its \(2^{14}=16{,}384\) sensor subsets with actual closure/forcing. Both independently compare the outcome against containment in one of fourteen closed neighborhoods and confirm the failure vector \((1,14,63,56,14,0,\ldots,0)\) by cardinality. The Python implementation additionally checks the exact \(28\) optimal pairs and the degree-six, diameter-three exchange graph. The C++ program uses an independent integer-bitmask forcing procedure. Commands:

```sh
python3 verify_geometry.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_bitmask.cpp -o verify_bitmask
./verify_bitmask
```

These checks cover the complete finite state space; they are supplementary to the projective-plane proof above, not evidence for any unclaimed infinite generalization.

## Relationship to prior work
The graph power-domination rule originates in Haynes, Hedetniemi, Hedetniemi and Henning (2002). Dorbec et al. (2013) establish general upper bounds for connected regular graphs, including cubic graphs; their theorem does not classify the Heawood graph's unsuccessful placements. Brimkov et al. (2018) introduce and study the power-domination polynomial and several families; their accessible full text does not present this Heawood closed-star classification. The present result is a finite exact structural and enumerative refinement for the canonical cubic girth-six graph, not a new general cubic upper bound.

## Limitations
The classification applies specifically to the fourteen-vertex Fano incidence graph with the ordinary closed-neighborhood power-domination convention, not to projective planes of arbitrary order or to different propagation rules. The comparison with published work cannot exclude an unindexed historical enumeration; no independent scholarly audit or formal proof-assistant verification is asserted. Exhaustive programs verify only this finite graph.

## References
1. T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi and M. A. Henning, *Domination in Graphs Applied to Electric Power Networks*, SIAM J. Discrete Math. **15** (2002), 519–529, DOI: https://doi.org/10.1137/S0895480100375831 (first electronically published September 10, 2002).
2. P. Dorbec, M. A. Henning, C. Löwenstein, M. Montassier and A. Raspaud, *Generalized Power Domination in Regular Graphs*, SIAM J. Discrete Math. **27** (2013), 1559–1574, DOI: https://doi.org/10.1137/120891356.
3. B. Brimkov, R. Patel, V. Suriyanarayana and A. Teich, *Power Domination Polynomials of Graphs*, arXiv:1805.10984 (2018), https://arxiv.org/abs/1805.10984.
