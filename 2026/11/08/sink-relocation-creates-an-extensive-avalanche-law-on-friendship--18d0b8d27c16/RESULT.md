# Sink relocation creates an extensive-avalanche law on friendship graphs

## Finding
Let \(F_k\), for each integer \(k\ge2\), be the *friendship graph* obtained by identifying one vertex \(c\) in each of \(k\) disjoint triangles. Write the outer vertices of the triangles as \(a_i,b_i\), for \(1\le i\le k\). Thus the edges are \(ca_i,cb_i,a_ib_i\), and there are \(2k+1\) vertices. Consider the ordinary finite Abelian sandpile with exactly one designated sink: a nonsink vertex topples on reaching its degree, sends one grain along each incident edge, and grains entering the sink disappear.

For a fixed sink \(s\), define the *joint principal-avalanche polynomial*
\[
A_{k,s}(z,y)=\sum_{\eta\in\mathcal R_s}\ \sum_{v\ne s}z^{T(\eta,v)}y^{L(\eta,v)},
\]
where \(\mathcal R_s\) is the set of recurrent stable configurations, \(T\) is the total number of individual vertex topplings in stabilizing \(\eta+\mathbf1_v\), and \(L\) is the number of grains delivered to the sink. Terms with no toppling are included. Both sink conventions have exactly \(3^k\) recurrent configurations and the same sandpile group \((\mathbb Z/3\mathbb Z)^k\), but have radically different avalanche polynomials.

With the central sink \(s=c\),
\[
\boxed{A_{k,c}(z,y)=2k3^{k-1}(1+zy+z^2y^2).}
\]
With a peripheral sink \(s=a_1\),
\[
\boxed{\begin{aligned}
A_{k,a_1}(z,y)={}&3^{k-1}\bigl(2k+zy+z^{2k-1}y+2z^{2k}y^2\bigr)\\
&+2(k-1)3^{k-2}\bigl(z+z^{2k}y+z^{2k+1}y\\
&\hspace{46mm}+z^{2k+1}y^2+z^{2k+2}y^2+z^{4k+1}y^3\bigr).
\end{aligned}}
\]

Choose a recurrent configuration uniformly and, independently, an addition site uniformly from the \(2k\) nonsink vertices. If \(T_k\) denotes the resulting number of topplings with the peripheral sink, then
\[
\Pr(T_k\ge 2k-1)=\frac{10k-1}{18k},\qquad
\Pr(T_k=4k+1)=\frac{k-1}{9k},
\]
whereas with the central sink every avalanche has at most two topplings. In fact,
\[
\frac{T_k}{k}\ \Longrightarrow\ \frac49\delta_0+\frac49\delta_2+\frac19\delta_4.
\]
Here the \(\delta_t\) denote point masses, and the arrow denotes convergence in distribution. Thus changing only the sink, with the graph and its critical group fixed, creates a nonvanishing probability of extensive avalanches. In the peripheral-sink model, the probability of a positive-toppling avalanche with *zero* sink loss is \((k-1)/(9k)\).

## Assumptions and scope
The graph is finite, simple, undirected and unweighted. The model has integer grains, deterministic degree-threshold topplings, exactly one absorbing sink, and single-grain additions at nonsink vertices. A recurrent configuration is a stable sandpile in the recurrent class of the addition dynamics, equivalently one satisfying Dhar's burning criterion. The probabilities use the uniform recurrent-state measure and the uniform nonsink addition-site measure; no claims are made about other sampling conventions, stochastic toppling, infinite-volume sandpile limits, or arbitrary cactus graphs. The index range is \(k\ge2\) for both formulas and probability statements.

## Proof
**1. Recurrent states and the critical group.** For the central sink, every outer triangle becomes a two-site subsystem. Its reduced Laplacian block is \(\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)\), with determinant three, so the product over all triangles has critical group \((\mathbb Z/3\mathbb Z)^k\). By burning, the allowed stable height pairs are exactly \((1,0),(0,1),(1,1)\), independently for each triangle; there are \(3^k\) choices.

For the peripheral sink \(a_1\), the center has degree \(2k\), the vertex \(b_1\) has degree two, and all remaining outer vertices have degree two. Before the center burns, no outer vertex in triangles numbered two or higher can burn: both of its neighbors remain unburnt, and its height is at most one. The vertex \(b_1\) burns first precisely if its height is one. If it burns first, the center can subsequently burn with height at least \(2k-2\); otherwise the center must initially have height at least \(2k-1\). After the center burns, each other pair burns precisely if its heights are not \((0,0)\). Thus the recurrent states are exactly the independent products of one *gate* state
\[
G_0=(2k-2,1),\quad G_1=(2k-1,0),\quad G_2=(2k-1,1)
\]
at \((c,b_1)\), and one of \((1,0),(0,1),(1,1)\) on each of the remaining \(k-1\) pairs. This gives \(3\cdot3^{k-1}=3^k\) recurrent states. Sink independence of the critical group, or its standard spanning-tree description, establishes the same group for this sink.

**2. Central-sink avalanches.** In each independent outer pair, an addition to either vertex gives, over its three recurrent pair states, respectively zero topplings, one toppling with one grain lost, and two topplings with two grains lost. The other \(k-1\) pairs admit \(3^{k-1}\) choices. There are \(2k\) choices of addition site, proving the first polynomial.

**3. Peripheral-sink local toppling classification.** In the table below \(G_j\) is the gate state before addition. For an addition in a nonsink outer triangle other than the first, *empty* means the chosen vertex starts at height zero, *single* means the chosen vertex and its partner start at \((1,0)\), and *double* means they start at \((1,1)\). Each entry is \((T,L)\), the exact total number of topplings and grains lost.

| Addition site and local state | \(G_0\) | \(G_1\) | \(G_2\) |
|---|---|---|---|
| Center \(c\) | \((0,0)\) | \((2k-1,1)\) | \((2k,2)\) |
| First-triangle vertex \(b_1\) | \((1,1)\) | \((0,0)\) | \((2k,2)\) |
| Other triangle, empty chosen site | \((0,0)\) | \((0,0)\) | \((0,0)\) |
| Other triangle, single | \((1,0)\) | \((2k,1)\) | \((2k+1,2)\) |
| Other triangle, double | \((2k+2,2)\) | \((2k+1,1)\) | \((4k+1,3)\) |

For completeness, the nonzero toppling vectors underlying the table have the following small-coordinate description. Record coordinates in the order: center, first-triangle vertex \(b_1\), chosen outer site, its mate, and *each vertex* in any unaffected outer triangle. The cases center \(G_1,G_2\) have coordinate values \((1,0,\text{not applicable},\text{not applicable},1)\) and \((1,1,\text{not applicable},\text{not applicable},1)\); the case \(b_1,G_0\) topples only \(b_1\), while \(b_1,G_2\) topples \(c,b_1\) and each unaffected outer vertex once. The six nonzero other-triangle cases, ordered by gates \(G_0,G_1,G_2\), are:

| Source pair | \(G_0\) vector | \(G_1\) vector | \(G_2\) vector |
|---|---|---|---|
| Single | \((0,0,1,0,0)\) | \((1,0,2,1,1)\) | \((1,1,2,1,1)\) |
| Double | \((1,1,2,2,1)\) | \((1,0,2,2,1)\) | \((2,1,3,3,2)\) |

These are exact for *every* choice of states on the untouched triangles. To verify the vectors without assuming a toppling order, write the reduced graph Laplacian as \(\Delta\). At the center its action on a vector \(u\) is
\[
(\Delta u)_c=2ku_c-u_{b_1}-\sum_{i=2}^k(u_{a_i}+u_{b_i});
\]
at \(b_1\), \((\Delta u)_{b_1}=2u_{b_1}-u_c\); and on an outer pair with \(i\ge2\),
\[
(\Delta u)_{a_i}=2u_{a_i}-u_{b_i}-u_c,\qquad
(\Delta u)_{b_i}=2u_{b_i}-u_{a_i}-u_c.
\]
Substituting each vector into \(\eta'=\eta+\mathbf1_v-\Delta u\) gives a stable recurrent configuration. Every untouched outer pair returns to its original state. If the addition is in an outer triangle, its pair changes as follows: empty chosen site turns a pair with heights \((0,1)\) into \((1,1)\); a single pair \((1,0)\) becomes \((0,1)\); a double pair \((1,1)\) becomes \((1,0)\). The gate remains unchanged in the empty case; for the single case it changes \(G_0\to G_2\to G_1\to G_0\), and for the double case it changes \(G_0\to G_1\to G_2\to G_0\). Addition at the center cycles \(G_0\to G_2\to G_1\to G_0\), while addition at \(b_1\) cycles \(G_0\to G_1\to G_2\to G_0\). Thus the resulting \(\eta'\) is visibly one of the recurrent states classified in step 1.

The standard uniqueness theorem for recurrent representatives of reduced-Laplacian equivalence classes now proves that this candidate is exactly the stabilization of \(\eta+\mathbf1_v\): adding to a recurrent state stabilizes to a recurrent state in the same equivalence class, and each class has exactly one recurrent representative. Since the reduced Laplacian is invertible, the odometer vector is unique. Therefore the table contains the true toppling counts, not merely solutions of mass-balance equations. The number of grains lost is the sum of topplings at the two neighbors of the sink, namely \(u_c+u_{b_1}\), as shown in the table.

**4. Counting and limit.** For an addition at \(c\) or \(b_1\), each gate has \(3^{k-1}\) independent completions. For a chosen site in a triangle numbered at least two, each of the three gate choices and each of the three local pair choices has \(3^{k-2}\) completions, and there are \(2(k-1)\) such addition sites. Grouping the table entries gives exactly the displayed bivariate polynomial; setting \(z=y=1\) yields \(2k3^k\), accounting for all recurrent-state/addition-site pairs.

The coefficient of avalanche sizes at least \(2k-1\), for \(k\ge2\), is \(3\cdot3^{k-1}+10(k-1)3^{k-2}\). Dividing by \(2k3^k\) gives \((10k-1)/(18k)\). The unique maximum-size class has count \(2(k-1)3^{k-2}\), which yields \((k-1)/(9k)\). Exactly the same count belongs to the positive-size, zero-loss class. Finally, with probability tending to one the addition site lies in one of the triangles numbered at least two. Its nine equally likely gate/local-state types contribute four cases with size \(o(k)\), four with size \(2k+O(1)\), and one with size \(4k+1\), proving the weak limit.

## Verification
Two self-contained, separate Python programs accompany this result. `check_exhaustive.py` enumerates every stable configuration, tests recurrence by a direct burning algorithm, performs greedy single-site stabilization, and checks the full joint \((T,L)\) histogram for \(1\le k\le7\). `check_templates.py` enumerates the analytic product states, independently stabilizes by parallel waves, and checks the local toppling table for \(1\le k\le8\). Both use only the Python standard library and run with `python check_exhaustive.py` and `python check_templates.py`. The exhaustive checks cover respectively \(30{,}618\) and \(104{,}976\) additions at their largest tested sizes. These finite checks are corroboration; the all-\(k\) proof is the burning classification and reduced-Laplacian argument above.

## Relationship to prior work
Dhar's sandpile framework and burning method establish the general recurrence and critical-group principles. Austin, Chambers, Funke, García Puente and Keough (arXiv:1605.02713, first public May 9, 2016) define joint avalanche observables and derive graph-specific formulas for trees, cycles, complete graphs and wheels; they note in their Section 2.3 that avalanche distributions can depend on the sink. Their results do not imply the two evaluated friendship-graph formulas or the limiting extensive-avalanche probability by substitution, since this graph is none of their evaluated families and their general sink-dependence statement is qualitative. Gauthier (arXiv:1110.6263, first public October 28, 2011) studies first-wave avalanche clusters on growing balls of the expanded cactus; his stated theorems concern a different graph sequence, boundary prescription and observable, and do not evaluate the fixed finite friendship graph under two sink placements. A direct literature and database comparison found no exact equivalent to the joint finite-size formulas. This is not a proof of priority over every unindexed source.

## Limitations
The theorem depends on the prescribed finite friendship graph and standard single-grain Abelian dynamics. The extensive-avalanche limit arises on a sequence whose central degree grows with network size; it is not a claim of self-organized criticality, power-law decay, a thermodynamic phase transition, or universality on bounded-degree graph families. The auxiliary verification only tests finitely many instances. Independent external validation and a comprehensive historical-priority review have not been performed.

## References
1. G. Gauthier, *Avalanche dynamics of the Abelian sandpile model on the expanded cactus graph*, arXiv:1110.6263, first submitted 2011-10-28, https://arxiv.org/abs/1110.6263.
2. D. Austin, M. Chambers, R. Funke, L. D. García Puente and L. Keough, *The Avalanche Polynomial of a Graph*, arXiv:1605.02713, first submitted 2016-05-09, https://arxiv.org/abs/1605.02713.
3. D. Dhar, *Self-organized critical state of sandpile automaton models*, Physical Review Letters 64 (1990), 1613–1616, https://doi.org/10.1103/PhysRevLett.64.1613.
