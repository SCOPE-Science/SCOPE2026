# The first anisotropic degree-one Walsh frame in quartic graph ice

## Finding

Let \(G=K_{2,2,2}\) be the simple octahedral graph on vertex classes \(\{0,1\},\{2,3\},\{4,5\}\), and let \(E\) be its 12 unordered edges ordered lexicographically with reference orientation from smaller to larger label. For each Eulerian orientation \(\omega\), define its edge spin vector \(s(\omega)\in\{\pm1\}^{12}\), where \(s_{(a,b)}=+1\) if the edge points from \(a\) to \(b\) and \(-1\) otherwise. Let \(\mathcal I\) be the uniform ensemble of Eulerian orientations, with two incoming and two outgoing edges at every vertex. There are exactly 38 such orientations.

Write \(B\) for the \(6\)-by-\(12\) oriented incidence matrix, with column \(e=(a,b)\) having \(+1\) at \(a\) and \(-1\) at \(b\). Let \(P_{\mathrm{cyc}}\) be the Euclidean orthogonal projection onto \(\ker B\). Define \(v\in\{\pm1\}^{12}\) by \(v_e=+1\) on edges between the first and second vertex classes, or between the second and third classes, and \(v_e=-1\) on edges between the first and third classes (relative to the fixed increasing-label orientation). Then \(Bv=0\), \(\|v\|_2^2=12\), and the exact centered degree-one Walsh Gram matrix is

\[
C:=\mathbb E_{\omega\in\mathcal I}\bigl[s(\omega)s(\omega)^{\mathsf T}\bigr]
=\frac{32}{19}P_{\mathrm{cyc}}+\frac{1}{57}vv^{\mathsf T}.
\]

Consequently its eigenvalues are \(0\) with multiplicity five, \(32/19\) with multiplicity six, and \(36/19\) with multiplicity one. The nullspace is exactly the cut space \(\operatorname{im}B^{\mathsf T}\), while the exceptional positive eigendirection is the canonical three-class circulation \(\mathbb R v\). For any real edge coefficient vector \(a\),

\[
\frac{32}{19}\|P_{\mathrm{cyc}}a\|_2^2\le
\mathbb E_{\omega}\left|\sum_{e\in E}a_es_e(\omega)\right|^2
\le\frac{36}{19}\|P_{\mathrm{cyc}}a\|_2^2.
\]

Both constants are attained, and the sampling map on the seven-dimensional identifiable quotient has sharp singular-value condition number \(\sqrt{9/8}\) (the Gram condition number is \(9/8\)). The constant Walsh character is orthogonal to all 12 edge characters by reversal symmetry, so adding it yields sampling rank eight.

This is the **first non-tight example by vertex order among connected simple four-regular graphs**: no such graph exists on fewer than five vertices; the unique five-vertex instance is \(K_5\), whose uniform Eulerian-orientation edge Gram is the tight matrix \(\frac53 P_{\mathrm{cyc},K_5}\); and the unique six-vertex instance is \(K_{2,2,2}\), with the strict gap above.

## Assumptions and scope

The graph is finite, simple, unweighted, with all Eulerian orientations equally likely. The 12 coordinates represent oriented edges, and inner products and projections are unnormalized Euclidean ones. The Walsh coordinates are the single-edge characters \(s_e=(-1)^{b_e}\) of the binary orientation encoding \(b_e\). The result is about the degree-one sampling Gram matrix, not the full Walsh convolution spectrum nor a physical finite-temperature Gibbs model.

## Proof

**1. Exact coefficient principle.** Introduce commuting indeterminates \(t_0,\ldots,t_5\), and, for any subset \(S\subseteq E\), define

\[
Z(S)=[t_0^2t_1^2\cdots t_5^2]\prod_{e=(a,b)\in E}
\bigl(t_a+(-1)^{\mathbf 1_{e\in S}}t_b\bigr).
\]

Each factor chooses which endpoint is the edge source. Extracting degree two at every vertex enforces balance; for edges in \(S\), the minus sign records the edge spin. Therefore \(Z(\varnothing)=|\mathcal I|\) and \(Z(\{e,f\})=\sum_{\omega\in\mathcal I}s_e(\omega)s_f(\omega)\) for distinct edges \(e,f\). The diagonal numerators equal \(Z(\varnothing)\). Exact multivariate coefficient recurrence (implemented in `verify_coefficient.py`) yields \(Z(\varnothing)=38\) and verifies, for all 144 ordered edge pairs, the identity

\[
Z(\{e,f\})=64(P_{\mathrm{cyc}})_{e,f}+\frac23v_ev_f
\qquad(e\ne f),
\]

with the same right side equal to 38 when \(e=f\). Thus dividing by 38 gives the displayed Gram formula. The calculation is exhaustive, uses exact integer and rational arithmetic, and truncates polynomial degrees above two without loss, since all degrees only increase. In particular no floating-point spectral guess enters the proof.

**2. The projection is explicit.** The graph Laplacian \(BB^{\mathsf T}\) has eigenvalue zero on constants, eigenvalue four on within-pair antisymmetric vertex functions (dimension three), and eigenvalue six on the pair-constant mean-zero vertex functions (dimension two). If \(D\) denotes the orthogonal projection onto the former and \(H\) onto functions constant on each pair, then

\[
L^+=\frac14D+\frac16\left(H-\frac16\mathbf1\mathbf1^{\mathsf T}\right),
\qquad P_{\mathrm{cyc}}=I-B^{\mathsf T}L^+B.
\]

This supplies every rational entry used in the coefficient certificate. Explicitly, the first row of the unnormalized moment matrix, in lexicographic edge order starting at \((0,2)\), is \((38,-10,-14,-14,-10,6,2,2,14,14,-2,-2)\), and all other rows are checked in the independent coefficient recurrence and direct-orientation verifier.

**3. Eigenvalues and sharpness.** Since \(Bv=0\), the projection fixes \(v\). On the cut space both terms vanish. On \(\ker B\cap v^\perp\) the matrix acts by \(32/19\), while on \(\mathbb Rv\) the rank-one correction adds \(\|v\|_2^2/57=4/19\), giving \(36/19\). Connectedness implies \(\operatorname{rank}B=5\), hence these three multiplicities are five, six, and one. This proves the sharp frame bounds, the kernel statement and the condition number.

**4. First non-tight order.** A connected simple four-regular graph needs at least five vertices. On five vertices, it is necessarily \(K_5\); on six vertices, its complement is a perfect matching, hence it is uniquely \(K_{2,2,2}\) up to isomorphism. For the five-vertex case, exact counting gives 24 regular tournaments and the tight Gram \(\frac53P_{\mathrm{cyc},K_5}\); this baseline is also confirmed in `verify_direct.py` and agrees with the previously published regular-tournament tight-frame theorem. The strict inequality \(36/19>32/19\) establishes the first failure of tightness.

## Verification

The self-contained Python 3 scripts `verify_direct.py` and `verify_coefficient.py` use only the standard library. Run `python3 verify_direct.py` and `python3 verify_coefficient.py` from their directory. The first visits all \(2^{12}=4096\) orientation bitstrings, verifies vertex balance, calculates every second moment directly, and checks the projection identity with exact fractions; it also checks the \(K_5\) baseline. The second performs independent six-variable generating-polynomial coefficient extraction with degree caps and checks all 144 rational identities. Both completed with all assertions satisfied. The proof uses exhaustive finite identities, not numerical approximation or sampled experiments.

## Relationship to prior work

Lieb's 1967 square-ice work defines the balanced-arrow model and develops transfer matrices for periodic square lattices, not the exact edge covariance of the octahedral graph. Nisoli's general-graph spin-ice framework treats divergence and Laplacian Green operators and uses a Gaussian approximation for charge correlations; the exact uniform zero-charge edge-spin Gram on \(K_{2,2,2}\) is a different finite observable. A previously recorded result proves tight edge-Walsh sampling for regular tournaments on odd complete graphs, covering the \(K_5\) baseline but not this even-order complete tripartite graph. The octahedral graph is also the squared six-cycle \(C_6^2\); an existing two-winding enumerator for *odd* squared cycles does not include it, and an orientation-count enumerator alone does not yield the exact edge-covariance spectrum. This result is limited to the stated graph and the degree-one Walsh sampling operator.

## Limitations

The result does not assert a universal covariance law for four-regular graphs, an all-order theorem for squared cycles, or a conclusion for higher-order Fourier characters. The exact rational identity depends on the uniform zero-temperature Eulerian-orientation ensemble. The historical literature comparison cannot rule out unindexed exact covariance tables; independent external mathematical review has not been performed.

## References

1. E. H. Lieb, *Exact Solution of the Problem of the Entropy of Two-Dimensional Ice*, Physical Review Letters **18** (1967), 692–694, first published 1967-04-24, https://doi.org/10.1103/PhysRevLett.18.692.
2. E. H. Lieb, *Residual Entropy of Square Ice*, Physical Review **162** (1967), 162–172, https://doi.org/10.1103/PhysRev.162.162.
3. C. Nisoli, *The Concept of Spin Ice Graphs and Field Theory for their Topological Monopoles and Charges*, arXiv:2009.14433 (2020), https://arxiv.org/abs/2009.14433.
4. *Integral tight Fourier sampling and tree-complement designs for regular tournaments* (2026), publicly indexed mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-tight-fourier-sampling-and-tree-complement-designs-for--eaf6965e2c4a.
5. *Two-winding enumeration of Eulerian orientations on odd cycle squares* (2026), publicly indexed mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-winding-enumeration-of-eulerian-orientations-on-odd-cycle-sq--3a8bfe6cd8c8.
