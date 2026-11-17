# All optimal coordinate-actuator placements on the triangular graphs \(J(n,2)\)

## Finding

Consider the triangular graph \(J(n,2)=L(K_n)\), whose vertices are unordered pairs of distinct elements of \([n]\), adjacent when they share one element. Let \(L_n\) be its unweighted combinatorial Laplacian. Each selected vertex receives an **independent** coordinate input in \(\dot x=-L_nx+B_Su\). Denote the least cardinality of a controllable selection by \(\kappa_n\). Then
\[
\kappa_2=1,\qquad \kappa_3=2,\qquad \kappa_4=3,\qquad
\kappa_n=\binom n2-n=\frac{n(n-3)}2\quad(n\ge5).
\]

Every minimum-size selection can also be classified. When \(n=4\), the selected pairs form a triangle or a three-edge star in \(K_4\), giving exactly eight labelled placements. When \(n=3\), any two of the three available vertices work; for \(n=2\), the single vertex works.

For each \(n\ge5\), let \(T=E(K_n)\setminus S\) be the **unactuated** pairs, so \(|T|=n\) at minimum input cardinality. The following conditions are necessary and sufficient:

1. Every connected component of the spanning graph \(([n],T)\) has exactly one cycle, and this cycle has odd length.
2. If \(n=6\), the graph \(([6],T)\) is **not** the disjoint union of two triangles.

These conditions classify all optimal placements, not merely one construction. An explicit optimal choice for every \(n\ge5\) is to leave unactuated the edges of a triangle with all remaining vertices attached by pendant edges to one triangle vertex.

Write \(R(z)=\sum_{j\ge1}j^{j-1}z^j/j!\), the exponential generating function for labelled rooted trees, and set
\[
U_{\mathrm{odd}}(z)=\frac14\log\!\left(\frac{1+R(z)}{1-R(z)}\right)-\frac12R(z).
\]
The exact number \(a_n\) of labelled optimal actuator placements for \(n\ge5\) is
\[
a_n=n!\,[z^n]\exp(U_{\mathrm{odd}}(z))-10\mathbf1_{\{n=6\}}.
\]
The initial values \(a_5=162\), \(a_6=2520\), \(a_7=45615\), and \(a_8=937440\) follow directly from this formal series.

## Assumptions and scope

The underlying simple graph is precisely the unit-weight triangular graph; it is not a graph with arbitrary adjustable edge conductances. Control inputs are independent coordinate columns \(B_S=[e_v]_{v\in S}\), not a single input broadcast to all selected vertices. Controllability means Kalman controllability over the real numbers for the complete, ungrounded Laplacian state space, including the consensus eigenmode. Graph vertices are labelled by unordered pairs, so the counting formula is for labelled configurations, not orbits under graph automorphisms.

A connected graph is **odd-unicyclic** if its number of edges equals its number of vertices and its unique cycle is odd. A spanning disjoint union of odd-unicyclic components has no isolated vertices.

## Proof

**1. Eigenspaces and the PBH test.** Let \(N=\binom n2\), and form the \(n\times N\) unsigned incidence matrix \(B\) of \(K_n\). Each column has exactly two ones. With \(A\) the adjacency of \(J(n,2)\),
\[
A=B^\top B-2I_N,\qquad BB^\top=(n-2)I_n+\mathbf1\mathbf1^\top.
\]
For \(n\ge3\), \(B\) has rank \(n\), and the three pairwise distinct Laplacian eigenlevels are
\[
\begin{array}{c|c|c}
\text{eigenvalue}&\text{eigenspace}&\text{dimension}\\\hline
0&\operatorname{span}(\mathbf1_N)&1\\
n&\{B^\top v:\mathbf1_n^\top v=0\}&n-1\\
2n-2&\ker B&N-n.
\end{array}
\]
The final zero-dimensional space is absent when \(n=3\). The Popov–Belevitch–Hautus condition for symmetric \(L_n\) says that a selection \(S\) controls exactly when no nonzero vector in any of these eigenspaces vanishes on all coordinates in \(S\).

**2. Minimum cardinality and the unsigned-incidence criterion.** The largest eigenspace dimension gives \(|S|\ge\max\{n-1,N-n\}\) for \(n\ge3\). For \(n\ge5\), this lower bound is \(N-n\). Equality makes the unactuated set \(T\) have exactly \(n\) edges. A vector of \(\ker B\) vanishes on all coordinates in \(S\) if and only if its support is contained in \(T\); equivalently, the columns of the submatrix \(B_T\) are linearly dependent. Therefore the \(2n-2\) eigenlevel is controllable exactly when \(B_T\) is an invertible square matrix.

For any finite simple graph \(F\), the unsigned incidence matrix has a one-dimensional left nullspace for each bipartite connected component and zero-dimensional left nullspace for each nonbipartite component. Indeed a left-null vector has \(v_i+v_j=0\) on every edge, forcing alternating signs along paths, and an odd cycle forces the coefficient to vanish. Thus when \(F=([n],T)\) has \(n\) edges on \(n\) vertices, invertibility of \(B_T\) is equivalent to every component being nonbipartite; equality of total row/column dimensions then forces every component to have as many edges as vertices, and hence exactly one cycle, necessarily odd. Conversely each odd-unicyclic component has nonsingular unsigned incidence, proving the equivalence.

**3. The intermediate eigenspace and the only exceptional obstruction.** An \(n\)-eigenvector \(B^\top v\) has zero coordinates on all selected pairs \(S\) exactly when \(v_i+v_j=0\) for every edge \(ij\) in \(F_S=([n],S)\), with \(\sum_i v_i=0\).

Suppose \(n\ge5\) and \(|T|=n\). If \(F_S\) is disconnected and has a component of size \(a\) with \(2\le a\le n-2\), every cross-pair lies in \(T\), forcing \(|T|\ge a(n-a)\ge2(n-2)>n\), contradiction. Consequently a disconnected \(F_S\) has precisely one isolated vertex and a connected remaining component; then \(T\) consists of the full star incident with that isolated vertex and one extra edge. Therefore \(F_S\) is the complete graph on the other \(n-1\) vertices minus one edge, which contains an odd cycle because \(n-1\ge4\). The nullspace of \(B_S^\top\) consists only of vectors supported at the isolated vertex, none nonzero and orthogonal to \(\mathbf1_n\). This case presents no obstruction.

If \(F_S\) is connected, the only nonzero solutions of \(B_S^\top v=0\) occur when \(F_S\) is bipartite, with \(v\) constant \(c\) on one side and \(-c\) on the other. The additional constraint \(\sum_i v_i=0\) then fails exactly for a **balanced** bipartition. If \(n=2r\), all intra-part pairs lie in \(T\), so \(|T|\ge2\binom r2=r(r-1)\). For \(n=2r\ge6\) this is at most \(n=2r\) only when \(r\le3\). Hence the sole possibility is \(n=6\), \(r=3\), with \(T\) exactly two disjoint triangles. It indeed satisfies the odd-unicyclic condition but has \(F_S=K_{3,3}\), whose balanced sign vector is a nonzero \(n\)-eigenvector vanishing on \(S\). No further exceptions occur.

The consensus eigenspace is always observed for nonempty \(S\). The explicit construction in the Finding meets both requirements, so the multiplicity lower bound is attained for every \(n\ge5\).

**4. Small orders.** For \(n=3\), \(J(3,2)=K_3\), and every two-coordinate set is controlling by the two-dimensional nonconstant eigenspace. For \(n=4\), the larger eigenspace has dimension three, so \(|S|\ge3\). With three selected pairs, their three unselected counterparts form a forest or a triangle, and are linearly independent as columns of the unsigned incidence matrix (an even cycle needs at least four edges). The remaining \(n\)-eigenspace is controlled exactly when \(([4],S)\) is a three-edge star or triangle: these are respectively connected unbalanced bipartite and nonbipartite-plus-isolate cases. A three-edge path has a balanced bipartition and fails. There are four stars and four triangles. For \(n=2\), the graph has one vertex.

**5. Enumeration.** A connected odd-unicyclic labelled graph consists of an undirected odd cycle of length \(\ell\ge3\) and a rooted labelled tree attached to each cycle vertex. Its exponential generating function is \(R(z)^\ell/(2\ell)\). Summing odd \(\ell\) gives \(U_{\mathrm{odd}}\); taking unordered sets of components gives \(\exp(U_{\mathrm{odd}})\). This enumerates all \(n\)-edge complements meeting the incidence criterion. For \(n=6\), there are \(\binom63/2=10\) excluded two-triangle complements. Taking complements is a bijection to actuator sets, so the stated formula follows.

## Verification

The accompanying standalone program `verify.py` performs exact finite-field rank tests of the incidence and zero-sum observation matrices over a fixed large prime for **all** minimum-size labelled selections for \(3\le n\le7\). It compares the rank outcomes to the stated odd-unicyclic criterion and special cases. It additionally checks the integer adjacency/incidence identities and the first labelled enumerations from formal power series with exact fractions. No floating point is needed. These are bounded finite checks supporting the proof; they do not certify higher orders independently of the general argument.

## Relationship to prior work

Yuan et al. (2013) established the maximum-geometric-multiplicity framework for the minimum number of unconstrained independent inputs to a network; that framework provides the spectral lower bound used here, but not the all-position classification or enumeration. Dai (2022) gives general perfect-critical-set machinery and examples for two tree families, not this triangular graph family. Godsil (2010) studies controllable graph subsets with a single characteristic-vector input, which is distinct from independent coordinate inputs here. Trefois and Delvenne (2014) investigate strong structural controllability and zero forcing for variable matrix patterns, rather than the fixed unit-weight Laplacian in this result. Existing work on Johnson-graph eigenspaces supplies broader spectral context but not the proved combinatorial input-placement criterion identified in the inspected materials.

## Limitations

This result is for exact, unweighted, labelled triangular graphs and independent coordinate actuators. The formula does not cover arbitrary edge weighting, graph edits, ground-state removal, broadcast control, or robust strong structural controllability. The eigenvalue-multiplicity lower bound is established prior theory, not a new contribution. The novelty assessment is based on named inspections and searches, not a guarantee that all specialized literature has been indexed or made accessible. Independent verification by another party has not occurred.

## References

- Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, “Exact controllability of complex networks,” *Nature Communications* 4, 2447 (first public 12 September 2013). https://doi.org/10.1038/ncomms3447 ; open full-text preprint: https://arxiv.org/abs/1310.5806
- C. Godsil, “Controllable subsets in graphs,” first posted 15 October 2010, https://arxiv.org/abs/1010.3231 (distinct single-broadcast-input notion).
- L. Dai, “Minimum leader selection for controllability of undirected graphs with leader–follower framework,” *IET Control Theory & Applications* 17 (2023), first online 29 October 2022. https://doi.org/10.1049/cth2.12385
- A. Farrugia and I. Sciriha, “Controllability of undirected graphs,” *Linear Algebra and its Applications* 454 (2014), pp. 138–157. https://www.um.edu.mt/library/oar/handle/123456789/28166 (abstract accessible; full repository copy restricted).
- M. Trefois and J.-C. Delvenne, “Zero forcing number, constrained matchings and strong structural controllability,” 2014. https://arxiv.org/abs/1405.6222
