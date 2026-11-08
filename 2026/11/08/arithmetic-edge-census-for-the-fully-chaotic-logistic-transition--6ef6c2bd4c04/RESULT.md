# Arithmetic edge census for the fully chaotic logistic transition graph

## Finding

Let \(F:[0,1]\to[0,1]\) be \(F(x)=4x(1-x)\). For an arbitrary integer \(m\ge2\), partition the unit interval into the \(m\) equal cells \(I_j=[j/m,(j+1)/m]\), \(0\le j<m\). Define the directed transition graph \(G_m\) to have an edge \(j\to k\), including possible loops, exactly when
\[
\operatorname{Leb}\bigl(\operatorname{int}(I_j)\cap F^{-1}(\operatorname{int}(I_k))\bigr)>0.
\]
Thus an isolated endpoint-to-endpoint contact does **not** create an edge. Let \(E_m\) count the distinct directed edges, let \(g_m=\gcd(m,4)\), and put \(q_m=m/g_m\). Write the prime factorization \(q_m=\prod_p p^{e_p}\), allowing the empty product when \(q_m=1\), and define
\[
R_m=\prod_p p^{\lceil e_p/2\rceil}.
\]
Then, for **every** \(m\ge2\),
\[
\boxed{E_m=3m-\frac{m}{R_m}-(m\bmod2).}
\]
In particular, the mean in-degree and out-degree both equal \(3-1/R_m-(m\bmod2)/m\). The exact global bound
\[
0<3m-E_m\le2\sqrt m+1
\]
is sharp at square resolutions: for every integer \(k\ge1\),
\[
E_{4k^2}=12k^2-4k,
\qquad 3(4k^2)-E_{4k^2}=2\sqrt{4k^2}.
\]
Consequently \(E_m/m\to3\) but its finite-resolution deficit has genuine arithmetic fluctuations of optimal order \(\sqrt m\).

If the initial state is distributed according to the invariant arcsine probability measure with density \(1/[\pi\sqrt{x(1-x)}]\), then with probability one **every** edge of \(G_m\) appears infinitely often in the successive-bin itinerary, and no nonedge appears (apart from a null set of initial states whose orbit meets a partition boundary). In fact, this statement holds simultaneously for all integer resolutions \(m\ge2\) on one set of initial conditions of full arcsine measure.

## Assumptions and scope

The logistic parameter is exactly \(4\). The grid is an equal-width **amplitude** grid in the original \(x\) coordinate, rather than a uniform grid in its doubling-map conjugate coordinate. The graph counts positive-measure transitions of the deterministic continuum map, not edges in a finite sample, not discrete floating-point states, and not target-bin touches arising solely at endpoints. Cells may be assigned any consistent endpoint convention because the defining condition uses their interiors and positive measure. Loops are included. The mean degree is the directed edge count divided by the number of vertices.

## Proof

**1. Grid-alignment lemma.** Put \(y_j=F(j/m)=4j(m-j)/m^2\). For each source boundary \(1\le j\le m-1\), its image lies at a target-cell boundary if and only if \(m y_j\) is an integer. Since
\[
m y_j=\frac{4j(m-j)}m,
\]
this condition is equivalent to \(m\mid4j^2\), hence to \(q_m\mid j^2\). Indeed, writing \(m=g_m q_m\), the prime divisibilities in \(m\mid4j^2\) are precisely those in \(q_m\mid j^2\), because \(m/\gcd(m,4)\mid j^2\) is the standard cancellation criterion for \(m\mid4j^2\). Prime by prime, \(q_m\mid j^2\) is equivalent to \(p^{\lceil e_p/2\rceil}\mid j\) for every \(p\), or simply \(R_m\mid j\). In particular, \(R_m\mid m\).

**2. Counting a monotone sweep.** Suppose consecutive source cells lie on one strictly monotone branch of \(F\), and their images together sweep an interval meeting every target cell in positive length. Counting one target-cell hit for each target cell gives \(m\) hits. At each interior boundary between source cells, one additional hit is counted if the boundary image lies in the interior of a target cell: both adjacent source cells then meet that cell in positive length. If the boundary image lies exactly on a target boundary, there is no additional positive-measure hit. This counts **ordered source-cell/target-cell pairs** exactly, hence directed edges; edges from different sources are distinct.

**3. Even resolutions.** Let \(m=2h\). The first \(h\) cells sweep \([0,1]\) monotonically upward and the last \(h\) cells sweep it downward. The alignment lemma applies to interior boundaries \(j=1,\ldots,h-1\) on the rising half. The integer \(R_m\) divides \(h\): if the \(2\)-adic valuation of \(m\) is one then \(q_m\) is odd and \(R_m\mid h\); otherwise \(q_m=m/4\) and the \(2\)-adic exponent of \(R_m\) is at most that of \(m/2\), while every odd prime divisor is already handled. Therefore exactly \(h/R_m-1\) of the \(h-1\) interior boundaries are aligned. The rising half has
\[
m+(h-1)-(h/R_m-1)=m+h-h/R_m
\]
edges. The descending half contributes the same number by the symmetry \(F(1-x)=F(x)\), so \(E_m=3m-m/R_m\).

**4. Odd resolutions.** Let \(m=2h+1\). The central cell \(I_h\) straddles the critical point \(x=1/2\). Both of its endpoints map to \(1-1/m^2\), so its image is \([1-1/m^2,1]\), meeting only the top target cell in positive measure: it contributes exactly one edge. Each remaining monotone run has \(h\) source cells, sweeping \([0,1-1/m^2]\); this intersects **every** target cell in positive length because \(1/m^2<1/m\). There are \(h-1=(m-3)/2\) internal source boundaries per run. Because \(m\) and \(R_m\) are odd and \(R_m\ge3\), the number aligned is
\[
\left\lfloor\frac{m-3}{2R_m}\right\rfloor
=\frac{m/R_m-1}{2}.
\]
Each of the two monotone runs therefore contributes
\[
m+\frac{m-3}{2}-\frac{m/R_m-1}{2}
\]
edges. Adding the central cell yields \(E_m=3m-1-m/R_m\), proving the unified formula.

**5. Sharp finite-size bound.** By definition \(q_m\mid R_m^2\), hence \(R_m\ge\sqrt{q_m}\). With \(g_m\le4\),
\[
\frac{m}{R_m}\le \frac{m}{\sqrt{m/g_m}}
=\sqrt{g_m m}\le2\sqrt m.
\]
For \(m=4k^2\), one has \(q_m=k^2\) and \(R_m=k\), which proves equality in the even-resolution bound and the displayed exact square-family formula.

**6. Realization by typical trajectories.** Let \(h(t)=\sin^2(\pi t)\) for \(t\in\mathbb R/\mathbb Z\), and \(D(t)=2t\pmod1\). The identity \(F\circ h=h\circ D\) shows that the pushforward of Lebesgue measure under \(h\) is an ergodic \(F\)-invariant measure, namely the arcsine measure with the stated density. Each edge event \(U_{jk}=\operatorname{int}(I_j)\cap F^{-1}(\operatorname{int}(I_k))\) is an open set of positive Lebesgue, hence positive arcsine, measure. Birkhoff's ergodic theorem makes the asymptotic visit frequency of \(U_{jk}\) equal its positive measure for almost every initial state. There are finitely many edges at fixed \(m\). Nonedges are impossible except possibly at a grid boundary; the countable union of all preimages of all partition boundaries has measure zero. Finally, intersect the full-measure sets over the countably many resolutions \(m\ge2\).

## Verification

Run `python3 verify_edges.py` with a standard Python 3 interpreter. It constructs each edge by **integer** interval-overlap comparisons (both source images and target boundaries are represented over the common denominator \(m^2\)), so there is no floating-point ambiguity at grid endpoints. It independently computes the prime-factor formula and compares the two totals for all \(2\le m\le512\), then checks 100 exact square-family cases. The observed terminal line is `VERIFY_OK exact_integer_adjacency_resolutions= 511 sharp_square_family_cases=100`. Representative formula outputs include \(E_{1000}=2980\), \(E_{2000}=5960\), and \(E_{4096}=12160\). The proof above, not the finite test, establishes the arbitrary-resolution and almost-sure statements.

## Relationship to prior work

Balaji et al. (2026) build amplitude-bin transition networks of the logistic family and calculate network measures from simulated trajectories. Their publicly accompanying MATLAB program `global_measures.m` forms the one-step 2000-bin adjacency from observed transitions; the inspected code and abstract do not state an all-resolution exact edge-count theorem. Their `logmap_series_gen.m` uses a specially chosen initial state, so the typical-orbit assertion here should **not** be read as describing every trajectory in their numerical experiment. The complete paper text could not be inspected; historical novelty with respect to its uninspected material remains provisional.

Kyriakopoulos and Thurner (2007) introduced a directed graph of interval-to-interval logistic-map transitions and numerically observed a mean degree near \(3\) at parameter \(4\). They also print a four-bin adjacency matrix counting contacts at target-bin endpoints. The present positive-measure convention differs at those zero-measure contacts: for \(m=4\), the present graph has eight edges whereas their displayed endpoint-inclusive matrix has ten. Their accessible Method, Logistic Map results, and Discussion do not derive the explicit prime-divisibility correction, its exact parity term, its sharp order-\(\sqrt m\) extremal family, or the typical-orbit realization under the positive-measure convention. Earlier general work on state-transition networks supplies the construction and context, not this arithmetic census.

## Limitations

The theorem covers the single fully chaotic parameter value \(4\) and one-step directed **support** networks under uniform amplitude cells. It does not classify graph diameter, centrality, stationary Markov approximations, weighted transition probabilities, other logistic parameters, finite-precision arithmetic, or finite observation lengths. The almost-sure assertion excludes exceptional starting states; in particular the critical starting point \(1/2\) follows the exceptional orbit \(1/2\to1\to0\to0\). The full text of the 2026 motivating preprint was not accessible; an independent historical-priority check remains necessary. The proof and code have not received independent scientific audit.

## References

1. A. Balaji, S. Tandon, S. Viswesh, N. Marwan and J. Kurths, *Identifying the structure of dynamical transitions in logistic map*, arXiv:2608.20956 (first posted 2026-08-21), https://arxiv.org/abs/2608.20956.
2. A. Balaji and collaborators, accompanying MATLAB code, Zenodo 10.5281/zenodo.22114165 (2026-08-26), https://zenodo.org/records/22114165, especially `global_measures.m`, `logmap_series_gen.m`, and `README.md`.
3. F. Kyriakopoulos and S. Thurner, *Directed Network Representation of Discrete Dynamical Maps*, in *Computational Science – ICCS 2007*, LNCS 4488, 625–632 (2007), DOI:10.1007/978-3-540-72586-2_91, accessible text: https://www.researchgate.net/publication/220856161_Directed_Network_Representation_of_Discrete_Dynamical_Maps.
4. *A Novel Measure Inspired by Lyapunov Exponents for the Characterization of Dynamics in State-Transition Networks*, *Entropy* 23, 103 (2021), https://www.mdpi.com/1099-4300/23/1/103 (coarse-grained network background).
