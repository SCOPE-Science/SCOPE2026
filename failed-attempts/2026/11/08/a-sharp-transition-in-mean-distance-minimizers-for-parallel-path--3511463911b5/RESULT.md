# A sharp transition in mean-distance minimizers for parallel-path metric networks

## Finding
Let \(m\ge3\) be an integer, and \(L>0\). The two-pole network \(G_m(\ell_1,\ldots,\ell_m)\) has \(m\) internally disjoint metric intervals of respective positive lengths \(\ell_i\), with both endpoints identified at the same pair of distinct poles, and \(\sum_i\ell_i=L\). Give it the intrinsic shortest-path metric and normalized arclength measure, and take two independent points \(X,Y\). Then
\[
\inf_{\ell_i>0,\,\sum_i\ell_i=L}\mathbb E[d(X,Y)]
=\begin{cases}
\frac{5L}{27},&m=3,\\[3pt]
\frac{(2m-3)L}{4(m-1)^2},&m\ge4.
\end{cases}
\]
When \(m=3\), the unique minimizing length vector up to path permutation is \((L/3,L/3,L/3)\). When \(m\ge4\), no positive length vector attains its infimum. Every minimizing sequence, after reordering the paths, satisfies
\[
\ell_1\longrightarrow0,\qquad \ell_2,\ldots,\ell_m\longrightarrow\frac{L}{m-1}.
\]
The limit identifies the two poles and is the equilateral flower with \(m-1\) loops. The change from an attained symmetric optimum to a uniquely determined degenerating optimum occurs between three and four parallel paths.

## Assumptions and scope
Lengths are arbitrary positive reals. There are precisely two distinct poles and exactly \(m\) internally disjoint paths (each represented by one metric interval), with no other edge or attached tree; this is also called a pumpkin, banana, dipole, or generalized theta network. All distances use the *ambient intrinsic shortest-path metric* and are integrated against independent normalized arclength. The expression \(\mathbb E[d(X,Y)]\) counts two independent ordered points, including pairs on the same path. No Euclidean embedding is specified. All results hold for every integer \(m\ge3\) and every total length \(L>0\).

## Proof
**Exact pair integrals.** Put \(I_m=L^2\mathbb E[d(X,Y)]\), so that \(I_m\) is the ordered-pair arclength integral. Sort the path lengths and call the shortest \(a\), and the others \(x_1,\ldots,x_k\), with \(k=m-1\), \(x_i\ge a\). Define \(S=\sum_i x_i=L-a\), \(Q=\sum_i x_i^2\), \(R=\sum_i x_i^3\).

For two points on the same path of length \(u\), let \(q\) be the shortest competing path. Their metric distance is \(\min(z,u+q-z)\) when their within-edge coordinate separation is \(z\). The ordered integral is
\[
H(u,q)=2\int_0^u (u-z)\min(z,u+q-z)\,dz=
\begin{cases}u^3/3,&u\le q,\\ (3u^3+3u^2q-3uq^2+q^3)/12,&u>q.\end{cases}
\]

For different paths of lengths \(u,v\) and shortest remaining competing path \(q\), parameterize points by \(s\in[0,u]\), \(t\in[0,v]\) measured from the same pole. The four possible simple pole routes have lengths \(s+t\), \(u+v-s-t\), \(s+q+v-t\), and \(u-s+q+t\); any other walk is no shorter. Let \(u_0(s)=\min(s,u-s+q)\) and \(u_1(s)=\min(u-s,s+q)\). Then
\[
d(s,t)=\min(t+u_0(s),v-t+u_1(s)),\qquad
\int_0^v d(s,t)\,dt=\frac{v^2}{4}+\frac{v(u_0+u_1)}2-\frac{(u_0-u_1)^2}4.
\]
The crossing lies inside \([0,v]\) because \(|u_1-u_0|\le u\le v\) after interchanging the two paths if necessary. Integrating in \(s\), with breakpoints \((u-q)/2\) and \((u+q)/2\) when \(q<u\), gives
\[
J(u,v;q)=\begin{cases}
\dfrac{u(-u^2+6uv+3v^2)}{12},&q\ge u,\\[4pt]
\dfrac{2q^3-3q^2(u+v)+6quv+3uv(u+v)}{12},&q<u,
\end{cases}\quad(u\le v).
\]
In each case the formula is continuous when \(q=u\). For the shortest edge, all competing lengths are at least \(a\); for pairs of longer paths the shortest competitor is \(a\). Thus summing same-path integrals \(H\) once and distinct-path integrals \(J\) twice, and simplifying, gives the all-parameter cubic identity
\[
\boxed{I_m=\frac{(2S+a)Q-R}{4}+\frac{aS^2}{2}
+\frac{7-2m}{4}a^2 S+\frac{2m^2-7m+9}{12}a^3.}\tag{1}
\]
This identity remains valid with repeated lengths by continuity.

**Strict balancing of longer paths.** Keep \(a\) and \(S\) fixed, and write \(t=S/k\). Let \(\overline I_m(a)\) denote \(I_m\) evaluated at \(x_1=\cdots=x_k=t\). The elementary power-sum identities
\[
Q-kt^2=\frac1k\sum_{i<j}(x_i-x_j)^2,\quad
R-kt^3=\frac1k\sum_{i<j}(x_i-x_j)^2(x_i+x_j+t)
\]
turn (1) into the *exact rigidity gap*
\[
\boxed{I_m-\overline I_m(a)=\frac{1}{4k}
\sum_{i<j}(x_i-x_j)^2\bigl(2S+a-x_i-x_j-t\bigr).}\tag{2}
\]
Since \(k\ge2\), \(x_i+x_j\le S\), and \(2S+a-x_i-x_j-t\ge S(1-1/k)+a>0\), the right side is nonnegative, and is zero exactly when all longer paths are equal. This also establishes strict balancing even when some path lengths tie at the minimum.

**Optimization in the shortest length.** Necessarily \(0<a\le L/m\). Substituting \(x_i=(L-a)/(m-1)\) into (1) and differentiating yields
\[
\boxed{\overline I'_m(a)=
\frac{(ma-L)(m-2)[L(5-2m)+a(2m^2-m-4)]}{4(m-1)^2}.}\tag{3}
\]
For every \(m\ge3\), the second bracket is negative at \(a=0\) and positive at \(a=L/m\); it is strictly increasing. Before \(L/m\) the first factor is negative. Hence \(\overline I_m\) first increases and then decreases, with exactly one interior maximum and *no interior minimum*. The only candidates in the compactified interval are therefore the endpoint lengths \(a=0\) and \(a=L/m\). Direct substitution gives
\[
\overline I_m(0)=\frac{2m-3}{4(m-1)^2}L^3,\qquad
\overline I_m(L/m)=\frac{2m-1}{3m^2}L^3,
\]
and the exact comparison
\[
\boxed{\overline I_m(L/m)-\overline I_m(0)=
\frac{(m-2)(2m^2-7m+2)}{12m^2(m-1)^2}L^3.}\tag{4}
\]
At \(m=3\) the difference is negative, and at every integer \(m\ge4\) it is positive. Thus the unique minimizer for \(m=3\) is \(a=L/3\) and all equal lengths, whereas for \(m\ge4\) the minimum exists only at the excluded boundary \(a=0\). Division by \(L^2\) yields the claimed expected distances.

Finally consider any minimizing sequence. The compact length simplex admits convergent subsequences. The strict endpoint comparison in (4) forces \(a\to0\) when \(m\ge4\), and positivity in (2) forces all remaining lengths to converge to \(L/(m-1)\). Otherwise a subsequence would have a positive balancing gap or a nonminimal limiting \(a\). This proves the asserted asymptotic rigidity. For \(m=3\), the same arguments force equality of all three lengths, proving uniqueness.

## Verification
The self-contained standard-library script `parallel_paths_mean_checker.py` independently evaluates all path-pair distance integrals by exact rational planar polygon clipping of the four competing affine shortest-route functions, plus separate same-path integration. This does not use the closed cubic identity to compute the reference integral. It compares that integral against (1) on \(85\) configurations across \(m=3,4,5,6,7\) and checks balancing, endpoint values and the sharp inequality for all test cases. Output: `PARALLEL_PATHS_EXACT_INTEGRAL_AND_PHASE_TRANSITION_OK 85`. An additional exact symbolic differentiation confirms (3) and (4). These finite checks support, but do not constitute, the proof for arbitrary \(m\), which is given above.

## Relationship to prior work
Doyle and Graver (1982) introduced continuous mean distance for shapes; the 2021 work of Garijo–Márquez–Silveira reports that their three-parallel-edge examples involved constrained lengths. That 2021 paper supplies a general integration algorithm but does not give the sharp all-\(m\) constrained optimization theorem. Kennedy–Kurasov–Malenová–Mugnolo (2015) define pumpkin/banana graphs in a spectral-gap context, not an average-distance optimization.

Baptista–Kennedy–Mugnolo (2023) establish an unrestricted metric-graph mean-distance lower bound, attained on equilateral *flower* graphs with a fixed number of edges. With \(m\) edges their unrestricted bound equals \((2m-1)L/(4m^2)\), strictly below the new sharp constrained pumpkin bound for \(m\ge4\). Their equilateral flower with \(m-1\) petals is the *boundary limit* here, but the nonattainment and exact phase transition on the two-distinct-pole, positive-length parameter space do not follow from the flower statement alone. Existing three-path distance-histogram results concern \(m=3\), not the all-\(m\) phase transition proved here. The new contribution is the sharp all-\(m\) constrained optimization, exact balancing gap, and rigidity at the degenerating boundary, not the general definition, metric-graph integration method, or known flower formula.

## Limitations
The conclusion is specific to two-pole parallel-path networks. It does not optimize over all connected metric graphs, arbitrary topology, nonuniform sampling densities, or graphs with intermediate branching vertices. The infimum for \(m\ge4\) is not attained while every path length is strictly positive; it is attained only in a different limiting graph class that identifies the poles. No claim of historical priority is definitive: Doyle–Graver's full 1982 article was inaccessible, though the 2021 primary full text describes its relevant parallel-edge cases as length-constrained. The earliest verified exact day of the listed structural precursor is 2015-04-08; older 1982 works are cited without inventing a day-level date.

## References
1. J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory 6 (1982), 453–471, DOI:10.1002/jgt.3190060410. Full text unavailable during this review.
2. J. K. Doyle and J. E. Graver, *A Summary of Results on Mean Distance in Shapes*, Environment and Planning B 9 (1982), 177–179, DOI:10.1068/b090177.
3. J. B. Kennedy, P. Kurasov, G. Malenová and D. Mugnolo, *On the Spectral Gap of a Quantum Graph*, arXiv:1504.01962v1, 2015-04-08 (esp. pumpkin-graph definition).
4. D. Garijo, A. Márquez and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, arXiv:2103.11676v1 (2021), introduction and algorithmic sections.
5. L. N. Baptista, J. B. Kennedy and D. Mugnolo, *Mean Distance on Metric Graphs*, arXiv:2312.04952v1 (2023), Theorem 3.2, Example 4.3, Lemma 4.4.
