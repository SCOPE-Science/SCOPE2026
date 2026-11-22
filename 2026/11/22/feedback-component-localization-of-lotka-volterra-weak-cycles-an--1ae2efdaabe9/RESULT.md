# Feedback-component localization of Lotka–Volterra weak cycles and a sharp two-species cutoff

## Finding

**Theorem (feedback-component localization).** Let \(A\) be any real \(N\times N\) interaction matrix whose indices are partitioned into nonempty ordered blocks \(V_1,\ldots,V_m\), with \(A_{V_i,V_j}=0\) whenever \(i<j\). For each \(b\in\mathbb R^N\), form the directed weak equilibrium graph \(\mathrm{WG}(A,b)\) defined below. Then

\[
\bigl[\mathrm{WG}(A,b)\text{ is acyclic for every }b\in\mathbb R^N\bigr]
\quad\Longleftrightarrow\quad
\bigl[\mathrm{WG}(A_{V_j,V_j},c)\text{ is acyclic for every }c\in\mathbb R^{|V_j|}\text{ and every }j\bigr].
\]

Thus the property that **all growth-rate choices are free from weak cycles** is determined exactly by the diagonal feedback components; the cross-block interactions are unrestricted in sign and magnitude.

**Sharp dynamical consequence.** If the nonzero-interaction digraph of \(A\) has strongly connected components of size at most two, every \(a_{ii}<0\), and each two-vertex component \(\{i,j\}\) satisfies \(a_{ii}a_{jj}-a_{ij}a_{ji}>0\), then \(A\) is Volterra–Lyapunov stable and \(\mathrm{WG}(A,b)\) is acyclic for every real \(b\). In particular, no such system has a heteroclinic cycle of distinct nonnegative equilibria. The component-size cutoff is sharp as an unconditional graph-size restriction: a three-vertex feedback component can support a heteroclinic three-cycle even with a Volterra–Lyapunov stable matrix.

## Assumptions and scope

The system is \(\dot u_i=u_i(b_i+\sum_{j=1}^N a_{ij}u_j)\) on \(\mathbb R^N_{\ge0}\), with fixed finite \(N\ge1\). An equilibrium \(x\ge0\) satisfies \(x_i r_i(x)=0\) for each \(i\), where \(r_i(x)=b_i+\sum_j a_{ij}x_j\). Its support is \(I(x)=\{i:x_i>0\}\). For **distinct** equilibria \(x,y\), a weak edge \(x\to y\) means

\[
r_j(x)\ge0\quad(j\in I(y)\setminus I(x)),\qquad
r_i(y)\le0\quad(i\in I(x)\setminus I(y)).
\]

An edge requires neither inequality when its corresponding support difference is empty. A directed cycle consists of finitely many distinct vertices (at least two) with consecutive directed edges. The theorem concerns this weak graph and includes zero invasion rates. It is not the claim that a cycle in one diagonal block necessarily occurs for every **fixed** full vector \(b\).

The interaction digraph has an arrow \(j\to i\) when \(i\ne j\) and \(a_{ij}\ne0\). Ordering its strongly connected components by any topological order puts \(A\) into the required lower-block-triangular form. Volterra–Lyapunov stability means existence of a positive diagonal \(H\) such that \(HA+A^{\mathsf T}H\) is negative definite.

## Proof

**1. Weak edges project when earlier blocks agree.** Consider a directed cycle of full equilibria \(x^{(1)}\to\cdots\to x^{(q)}\to x^{(1)}\). The restrictions \(x^{(k)}_{V_1}\) are equilibria of the first diagonal subsystem with growth vector \(b_{V_1}\). Every full weak edge projects either to an edge of its weak graph or to equality of the projected endpoints: the invasion rates on \(V_1\) depend only on \(V_1\). Consequently the projections form a closed directed walk with possible stationary steps. If the first-block weak graph is acyclic, all these projections must coincide.

Inductively, suppose all restrictions to \(V_1,\ldots,V_{j-1}\) are constant around the cycle, with common earlier values \(\bar x_{V_\ell}\). Each projected \(x^{(k)}_{V_j}\) is then an equilibrium of one and the same subsystem with effective growth vector

\[
c_j=b_{V_j}+\sum_{\ell<j} A_{V_j,V_\ell}\bar x_{V_\ell}.
\]

Every full weak edge again projects to either a weak edge of \(\mathrm{WG}(A_{V_j,V_j},c_j)\) or equality. Acyclicity of that graph forces the \(V_j\)-restrictions to coincide. Induction through all blocks would make every full vertex equal, contradicting the distinctness of vertices on a cycle. This proves the right-to-left implication, for every \(b\).

**2. Any blockwise weak cycle embeds for a suitable growth vector.** Suppose \(\mathrm{WG}(A_{V_j,V_j},c)\) has a directed cycle. Set \(b_{V_j}=c\), assign arbitrary growth rates on the other blocks, and extend each vertex of the block cycle by zeros on all other coordinates. Each extended vertex is an equilibrium of the full system, since the other coordinates vanish and all coordinates of the selected block have the same local growth rates. Each weak edge is preserved: all changed supports are inside \(V_j\). The extended vertices form a full weak cycle. This proves the reverse implication after universal quantification over growth vectors. No nonsingularity or stability hypothesis is needed for Steps 1–2.

**3. Two-dimensional feedback components are acyclic.** Let \(D=\begin{psmallmatrix}d_{11}&d_{12}\\d_{21}&d_{22}\end{psmallmatrix}\), with \(d_{11},d_{22}<0\) and \(\det D>0\), and let the two growth rates be arbitrary. There is at most one equilibrium for each of the four supports: empty \(0\), singleton \(P\) or \(Q\), or both species \(R\). A singleton \(P\) exists only if its corresponding intrinsic growth rate is strictly positive; thus \(P\to0\) is impossible, and similarly \(Q\to0\). If \(R\to0\), both intrinsic growth rates must be nonpositive, preventing any edge \(0\to P\) or \(0\to Q\); a simultaneous \(0\to R\) would force both growth rates zero and hence \(R=0\) by \(\det D\ne0\). Thus \(0\) lies on no directed cycle.

Write \(u=r_2(P)\) and \(v=r_1(Q)\) when the respective singletons exist. A two-cycle \(P\leftrightarrow Q\) would force \(u=v=0\); then the two distinct singleton points both solve \(Dz=-c\), contradicting invertibility. A two-cycle \(P\leftrightarrow R\) would force \(u=0\); then \(P\) and \(R\) both solve \(Dz=-c\), also impossible. The argument for \(Q\leftrightarrow R\) is identical. The only remaining directed cycles would be the two orientations on \(P,Q,R\). In \(P\to Q\to R\to P\), the first two edges force \(v\le0\) and \(v\ge0\), so \(v=0\), impossible. In \(P\to R\to Q\to P\), the first and last edges force \(u\ge0\) and \(u\le0\), so \(u=0\), impossible. Thus every two-dimensional diagonal feedback component satisfying the hypotheses is acyclic for all growth rates. The same is immediate in one dimension with negative self-interaction.

**4. Volterra–Lyapunov stability survives arbitrary feed-forward blocks.** Every one-dimensional negative diagonal block is diagonally stable. A real two-dimensional matrix with negative diagonal and positive determinant is diagonally stable: if the off-diagonal entries have opposite signs, choose positive diagonal weights cancelling the symmetric off-diagonal term; if they have the same sign, choose weights proportional to their absolute reciprocal partners, and positive determinant makes the weighted symmetric determinant positive; if one off-diagonal entry is zero, choose a sufficiently unbalanced positive diagonal weighting. In all cases the weighted symmetric part is negative definite.

If \(A=\begin{psmallmatrix}B&0\\C&D\end{psmallmatrix}\), and \(H_B,H_D\) are diagonal Lyapunov witnesses for \(B,D\), then \(H_t=\operatorname{diag}(tH_B,H_D)\) has weighted symmetric part

\[
H_tA+A^{\mathsf T}H_t
=\begin{pmatrix}tS_B&C^{\mathsf T}H_D\\H_DC&S_D\end{pmatrix},
\quad S_B\prec0,\quad S_D\prec0.
\]

The Schur complement of \(tS_B\) tends to \(S_D\prec0\) as \(t\to\infty\); hence this whole matrix is negative definite for all sufficiently large \(t\). Induction over the ordered feedback components proves full diagonal stability without a bound on \(C\). Steps 1–3 now prove acyclicity of the full weak graph. The known inclusion of the heteroclinic connection graph in the weak graph for a VL-stable matrix implies absence of heteroclinic cycles.

**5. Sharpness and separation from existing sufficient tests.** The known three-species matrix \(D_3=\begin{psmallmatrix}-1&-2&2\\2&-1&-2\\-2&2&-1\end{psmallmatrix}\), with all growth rates equal to one, has \(D_3+D_3^{\mathsf T}=-2I\) yet the three single-species equilibria \(e_1,e_2,e_3\) have the strict edges \(e_1\to e_2\to e_3\to e_1\). This is an existing rock–paper–scissors example, used only to establish optimality of the component-size threshold.

For a more strongly coupled acyclic example take

\[
A_4=\begin{pmatrix}-1&2&0&0\\-2&-1&0&0\\100&0&-1&2\\0&100&-2&-1\end{pmatrix},
\qquad H=\operatorname{diag}(10000,10000,1,1).
\]

After reordering coordinates, \(-\bigl(HA_4+A_4^{\mathsf T}H\bigr)\) consists of two identical positive definite blocks \(\begin{psmallmatrix}20000&-100\\-100&2\end{psmallmatrix}\), with determinant \(30000\). However the normalized absolute off-diagonal matrix has spectral radius \(2>1\), so the global generalized-dominance criterion does not apply. Nor can the weighted skew-norm criterion from the cited work apply: every allowable positive diagonal \(H'\) has \(\|G^{-1/2}KG^{-1/2}\|_2\ge(h'_1+h'_2)/\sqrt{h'_1h'_2}\ge2\), where \(G=-(H'A_4+A_4^{\mathsf T}H')\succ0\) and \(K=H'A_4-A_4^{\mathsf T}H'\); the published sufficient threshold for all four-species weak cycles is \(\tan(\pi/10)<1\). These are rigorous separations from two existing sufficient tests, not a claim that they are necessary conditions.

## Verification

The accompanying `checker.py` enumerates exact rational equilibria, signs of all weak edges, and directed cycles for 660 seeded block-triangular examples with one- and two-dimensional feedback blocks (including zero-rate and mixed-sign interactions), and passes. It also verifies the explicit four-dimensional matrix's diagonal Lyapunov certificate and the three-species strict cycle. Run: `python checker.py` with standard Python 3. All finite experiments supplement the universal projection-and-Schur-complement proof; they are not an exhaustive search over infinitely many matrices or growth vectors.

## Relationship to prior work

Bortolan–Kalita–Langa–Moura (2025) introduce the motivating VL-stable heteroclinic-cycle problem, identify the three-species rock–paper–scissors mechanism, and prove a dominance result for special cycles, but do not give the above all-growth-rate block-localization equivalence. Almaraz–Kalita–Langa–Soler-Toscano (2024) establish structural stability and interpretation of invasion graphs; their criteria concern realized community transitions, not exact localization of universal weak-graph acyclicity to arbitrary feedback blocks. Hofbauer–Schreiber (2022) develop invasion graphs for permanence rather than this localization criterion.

A later paper by Bortolan and collaborators (arXiv:2611.26473v1, **19 November 2026**) defines the same weak graph and proves all-growth-rate acyclicity under generalized dominance and under quantitative weighted-skew restrictions. Its proofs and conclusions were compared at the implication level: the four-dimensional example above violates both sufficient hypotheses yet is covered by the present feedback-component theorem. The later work's connection-to-weak-graph inclusion provides the stated dynamical consequence, not a second original general theorem here.

## Limitations

This is a theorem about weak graph cycles of nonnegative equilibria of finite-dimensional quadratic Lotka–Volterra flows, not a classification of individual heteroclinic trajectories when the matrix is arbitrary or singular. The uniform equivalence quantifies over **every** growth vector; it is not a fixed-growth-vector equivalence. The size-two cutoff is sufficient, not necessary: some larger feedback components are also cycle-free. The three-species sharpness example is known, not newly discovered. Independently established historical priority cannot be inferred from any finite search, and unindexed network-decomposition literature remains a risk.

## References

1. M. C. Bortolan, P. Kalita, J. A. Langa, R. O. Moura, *A theoretical and computational study of heteroclinic cycles in Lotka–Volterra systems*, Journal of Mathematical Biology **90**, 28 (first public 8 February 2025). https://doi.org/10.1007/s00285-025-02190-4
2. M. C. Bortolan et al., *Preventing cycles in Lotka–Volterra systems*, arXiv:2611.26473v1 (19 November 2026), §§1–4. https://arxiv.org/html/2611.26473v1
3. P. Almaraz, P. Kalita, J. A. Langa, F. Soler-Toscano, *Structural stability of invasion graphs for Lotka–Volterra systems*, Journal of Mathematical Biology **88**, 64 (17 April 2024). https://doi.org/10.1007/s00285-024-02087-8
4. J. Hofbauer, S. J. Schreiber, *Permanence via invasion graphs: incorporating community assembly into modern coexistence theory*, Journal of Mathematical Biology **85**, 54 (18 October 2022). https://doi.org/10.1007/s00285-022-01815-2
