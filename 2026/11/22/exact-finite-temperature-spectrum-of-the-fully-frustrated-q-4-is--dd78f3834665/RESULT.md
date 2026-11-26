# Exact finite-temperature spectrum of the fully frustrated \(Q_4\) Ising cell

## Finding

The classical sixteen-spin, zero-field, fully frustrated Ising model on the four-dimensional hypercube has exactly nine possible energies. In units of a positive uniform bond magnitude \(J\), the complete energy-degeneracy function is

| \(E/J\) | \(-16\) | \(-12\) | \(-8\) | \(-4\) | \(0\) | \(4\) | \(8\) | \(12\) | \(16\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Degeneracy | 16 | 1920 | 8640 | 13440 | 17504 | 13440 | 8640 | 1920 | 16 |

Consequently, for every real \(\beta\) and \(J>0\), the exact zero-field canonical partition function is

\[
Z_4(\beta J)=17504+26880\cosh(4\beta J)+17280\cosh(8\beta J)+3840\cosh(12\beta J)+32\cosh(16\beta J).
\]

In particular the first excitation above the ground energy has multiplicity \(1920\), which is \(120\) times the sixteenfold ground-state multiplicity confirmed by the census. The contribution concerns the full finite-temperature and excitation-level census, not priority for either ground-state endpoint.

## Assumptions and scope

Vertices of \(Q_4\) are \(x=(x_0,x_1,x_2,x_3)\in\{0,1\}^4\). For every coordinate \(j\) join \(x\) and \(x\oplus e_j\), with edge sign
\[
\epsilon_{x,x\oplus e_j}=(-1)^{\sum_{k<j}x_k}.
\]
The sign is independent of which endpoint labels the edge, since the exponent omits coordinate \(j\). For spins \(s_x\in\{-1,1\}\), set
\[
H(s)=-J\sum_{\{x,y\}\in E(Q_4)}\epsilon_{xy}s_xs_y.
\]
Every elementary square has the product of its four edge signs equal to \(-1\); these are fully frustrated couplings. No periodic identification of opposite vertices, no external magnetic field, and no additional interactions are present. A different signing with the same negative product around every square is gauge-equivalent and has the same zero-field density of states: its ratio to this signing has positive product around every square, hence around all cycles because commuting coordinate flips decomposes cube cycles into squares, and thus equals \(g_xg_y\) on each edge. The change of variables \(s_x\mapsto g_xs_x\) bijects spin configurations without altering energy.

## Proof

Write \(S(s)=-H(s)/J\). Let \(A\) be the symmetric signed adjacency matrix with \(A_{xy}=\epsilon_{xy}\) on edges. The signed operators corresponding to distinct coordinate flips anticommute and each squares to the identity. Therefore \(A^2=4I\) and
\[
|S(s)|=\tfrac12|s^TAs|\leq\tfrac12\|A\|\,\|s\|_2^2=16.
\]
Every spin-flip changes \(S\) by twice the negative of a sum of four signs, so by a multiple of four. The all-plus spin assignment has score \(S=8\). Consequently every score is in \(\{-16,-12,-8,-4,0,4,8,12,16\}\).

It remains to count each score exactly. Decompose \(Q_4\) into two \(Q_3\) layers, indexed by the final bit, and write their eight spins as \(a_x,b_x\) for \(x\in\{0,1\}^3\). Define the integer layer score and signed coupling
\[
Q(a)=\sum_{j=0}^{2}\ \sum_{x:x_j=0}(-1)^{\sum_{k<j}x_k}a_xa_{x\oplus e_j},\quad
B(a,b)=\sum_{x\in\{0,1\}^3}(-1)^{|x|}a_xb_x.
\]
The exact identity \(S(a,b)=Q(a)+Q(b)+B(a,b)\) holds term by term over all 32 cube edges. Thus an **exhaustive finite algebraic expression** for the signed-energy generating function is
\[
P(z)=\sum_{a\in\{-1,1\}^8}\sum_{b\in\{-1,1\}^8}z^{[Q(a)+Q(b)+B(a,b)]/4}.
\]
Evaluating the 256-by-256 sum with integer arithmetic, as specified completely in the accompanying `verify_ising_q4.py`, gives
\[
P(z)=16(z^{-4}+z^4)+1920(z^{-3}+z^3)+8640(z^{-2}+z^2)
+13440(z^{-1}+z)+17504.
\]
The checker independently evaluates every one of the \(2^{16}=65536\) complete spin assignments against all 32 signed edges and compares the resulting histogram, coefficient by coefficient, to the transfer sum and the displayed coefficients. Both procedures are finite and exhaustive; no sampling or extrapolation is used. Substituting \(z=e^{4\beta J}\) yields the displayed partition function because \(e^{-\beta H(s)}=e^{\beta JS(s)}\).

## Verification

Run `python3 verify_ising_q4.py` using Python 3.10 or later; no packages beyond the standard library are required. The direct and layer-decomposed enumerations assert all nine integer counts, all 65,536 assignments, 32 signed edges, the negative product around square faces, and \(A^2=4I\). As additional identities from the displayed coefficients, the total count is \(65536\) and the infinite-temperature moments are \(\mathbb E[S^2]=32\) and \(\mathbb E[S^4]=2432\). These moment identities are not separate tests in the checker.

## Relationship to prior work

Derrida, Pomeau, Toulouse and Vannimenus (1979) exhibit an isolated fully frustrated \(H_4\) with eight negative bonds and show that its energy saturates the lower bound (Fig. 3 and Table I, pp. 620–621; the table uses a lattice energy-per-spin normalization). Table I reports internal-field distributions for the extremal problem, not an Ising density of states. Their remark reporting sixteen ground states in dimension four (p. 624) is in the discussion of the simple-cubic lattice; it is not explicitly stated there as the isolated-cell count. Parisi and Potters (1995) use the same fully frustrated orthogonal interaction matrix and analyze large-system thermodynamics rather than the exact finite sixteen-spin density of states. Wang (2026) studies the minimum frustration index and spectral extremal configurations, not the full finite-temperature Ising partition polynomial. The nine-energy table supplies an exact finite-temperature benchmark on the isolated cell.

## Limitations

The result is exact only for a single sixteen-site, zero-field hypercube cell (not a periodic four-dimensional lattice or the infinite-dimensional model). It gives no thermodynamic-limit phase transition, no kinetic or mixing result, and no magnetic-field partition function. A dated 1979 journal issue supplies only month-level publication evidence; this does not establish a verified day of its public release. Earlier unlocated numerical tables or unpublished computations could contain equivalent coefficients; historical priority requires independent confirmation. The first-excitation ratio is an immediate consequence of the full census, not a separate independent theorem.

## References

1. B. Derrida, Y. Pomeau, G. Toulouse, J. Vannimenus, *Fully frustrated simple cubic lattices and the overblocking effect*, Journal de Physique **40**, 617–626 (June 1979), DOI: https://doi.org/10.1051/jphys:01979004006061700 ; open full text https://hal.science/jpa-00209146v1/file/ajp-jphys_1979_40_6_617_0.pdf.
2. G. Parisi, M. Potters, *Mean-Field Equations for Spin Models with Orthogonal Interaction Matrices*, arXiv:cond-mat/9503009 (first submission March 1, 1995; accessible complete v2 March 27, 1995), https://arxiv.org/html/cond-mat/9503009v2.
3. L. Wang, *The frustration index of fully frustrated hypercubes*, arXiv:2611.14906 (November 11, 2026), https://arxiv.org/html/2611.14906v1.
