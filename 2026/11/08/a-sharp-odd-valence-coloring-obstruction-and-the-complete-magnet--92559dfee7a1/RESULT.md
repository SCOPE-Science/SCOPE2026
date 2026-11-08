# A sharp odd-valence coloring obstruction and the complete magnetic response of the icosahedral three-state Potts antiferromagnet

## Finding

For the classical three-state Potts antiferromagnet on the regular icosahedron, the entire zero-temperature response to a uniform color-selective field is exactly resolved. With \(x=h/J\), the ground energy is

\[
\frac{E_0}{J}=\begin{cases}
10,&x\le-2,\\
4-3x,&-2\le x\le-1,\\
3-4x,&-1\le x\le1,\\
5-6x,&1\le x\le3,\\
11-8x,&3\le x\le4,\\
15-9x,&4\le x\le5,\\
30-12x,&x\ge5.
\end{cases}
\]

There are seven field-open regimes, with favored-color occupancies \(0,3,4,6,8,9,12\), and six exact coexistence fields \(-2,-1,1,3,4,5\). Their labeled ground-state multiplicities are:

| Field range for \(x\) | Occupancy of color \(0\) | Ground-state count |
|---|---:|---:|
| \(x<-2\) | \(0\) | \(72\) |
| \(x=-2\) | \(0,1,2,3\) | \(2292\) |
| \(-2<x<-1\) | \(3\) | \(360\) |
| \(x=-1\) | \(3,4\) | \(480\) |
| \(-1<x<1\) | \(4\) | \(120\) |
| \(x=1\) | \(4,5,6\) | \(600\) |
| \(1<x<3\) | \(6\) | \(120\) |
| \(x=3\) | \(6,7,8\) | \(840\) |
| \(3<x<4\) | \(8\) | \(240\) |
| \(x=4\) | \(8,9\) | \(400\) |
| \(4<x<5\) | \(9\) | \(160\) |
| \(x=5\) | \(9,10,11,12\) | \(329\) |
| \(x>5\) | \(12\) | \(1\) |

A general structural bound explains the unavoidable zero-field frustration: for every simple triangulation of a closed surface, if \(o\) vertices have odd degree, then any assignment of three colors creates at least \(\lceil o/4\rceil\) monochromatic edges. The icosahedral graph has twelve odd-degree vertices and attains the bound with exactly three frustrated bonds. It has precisely \(120\) zero-field ground configurations, all using each color four times; these configurations have twenty distinct three-edge defect supports, each compatible with exactly six assignments.

## Assumptions and scope

The spin variables are \(\sigma_v\in\{0,1,2\}\), the antiferromagnetic bond strength is \(J>0\), and the field \(h\in\mathbb R\) favors color \(0\) when positive. The Hamiltonian is

\[
H_{J,h}(\sigma)=J\sum_{uv\in E(G)}\mathbf1_{\sigma_u=\sigma_v}-h\sum_{v\in V(G)}\mathbf1_{\sigma_v=0}.
\]

An explicit graph labeling is \(V(G)=\{N,S,U_0,\ldots,U_4,V_0,\ldots,V_4\}\), with every subscript taken modulo five. Its thirty edges are \(NU_i\), \(SV_i\), \(U_iU_{i+1}\), \(V_iV_{i+1}\), \(U_iV_i\), and \(U_iV_{i-1}\), for each \(i=0,\ldots,4\). This is the standard five-regular icosahedral graph, comprising twenty triangular faces. The general odd-degree bound applies to vertex-three-colorings of a simple graph embedded as a triangular cellulation of a closed surface, with every edge in precisely two triangular faces and with cyclic vertex links.

## Proof

**Parity obstruction.** Fix an odd-degree vertex \(v\). If all edges incident to \(v\) are bichromatic, its neighbors avoid the color of \(v\) and therefore use at most two colors. If all edges of the cyclic link of \(v\) are also bichromatic, those neighbors give a proper two-coloring of an odd cycle, a contradiction. Thus every odd-degree vertex is either an endpoint of a monochromatic edge or the opposite vertex of a triangular face containing such an edge. Any monochromatic edge has just two endpoints and two opposite face vertices, so it accounts for at most four odd-degree vertices. Counting yields \(o\le4b\), or \(b\ge\lceil o/4\rceil\). This applies regardless of which three colors occur.

**Exact finite-sector calculation.** Define \(k(\sigma)=\#\{v:\sigma_v=0\}\) and \(b(\sigma)=\#\{uv\in E(G):\sigma_u=\sigma_v\}\). Let \(b_k=\min_{\sigma:k(\sigma)=k}b(\sigma)\) and let \(a_k\) count the configurations attaining this minimum. The complete exact integer sector certificate is:

| \(k\) | \(b_k\) | \(a_k\) |
|---:|---:|---:|
| 0 | 10 | 72 |
| 1 | 8 | 600 |
| 2 | 6 | 1260 |
| 3 | 4 | 360 |
| 4 | 3 | 120 |
| 5 | 4 | 360 |
| 6 | 5 | 120 |
| 7 | 8 | 480 |
| 8 | 11 | 240 |
| 9 | 15 | 160 |
| 10 | 20 | 144 |
| 11 | 25 | 24 |
| 12 | 30 | 1 |

This is an exhaustive integer proof, not a sample: the included `verify_exhaustive.cpp` explicitly visits every integer from zero to \(3^{12}-1=531440\), decodes a unique base-three spin assignment, counts all thirty bonds, and updates exactly the minimum and multiplicity for each of the thirteen sectors. Independently, `verify_transfer.py` contracts the two pentagonal rings column by column, treating each column as a pair of spins and conditioning on both pole colors. Each column has nine states. The intra-column contribution for \(s_i=(u_i,v_i)\), poles \((a,c)\), is

\[
B_i=\mathbf1_{u_i=a}+\mathbf1_{v_i=c}+\mathbf1_{u_i=v_i},
\]

while the three bonds between consecutive columns contribute

\[
C(s_{i-1},s_i)=\mathbf1_{u_{i-1}=u_i}+\mathbf1_{v_{i-1}=v_i}+\mathbf1_{u_i=v_{i-1}}.
\]

The transfer calculation fixes the first column, sums exactly over columns one through four, and closes the last-to-first bonds. It tallies every one of \(3^2\cdot9^5=3^{12}\) spin assignments exactly once, with integer-valued \((k,b)\) counts. Both independently specified algorithms reproduce the same table above.

**Lower convex envelope.** At fixed \(k\), the least energy is \(J(b_k-xk)\). The lower convex hull of the thirteen points \((k,b_k)\) has vertices \((0,10),(3,4),(4,3),(6,5),(8,11),(9,15),(12,30)\) with successive slopes \(-2,-1,1,3,4,5\). For every sector between consecutive hull vertices, its \(b_k\) is at least the corresponding interpolated ordinate; the attached exhaustive checker tests these finite integer inequalities. Hence the seven displayed linear functions are exactly the global minimum for every real field, including boundaries. At each crossing, sum the \(a_k\) over all collinear sectors; this yields the six coexistence counts and the field-open counts in the table.

At zero field the minimum of the \(b_k\) is exactly three and occurs only at \(k=4\). Since permutations of the three spin labels preserve the bond energy, all three colors occur four times in every zero-field minimizer. The exhaustive verifier additionally groups all configurations with three monochromatic edges by their labeled defect-edge set: exactly twenty supports occur, each with six colorings. The parity bound is therefore attained exactly on the icosahedron.

## Verification

Two complete standalone integer checks are embedded: `verify_exhaustive.cpp` (C++17) and `verify_transfer.py` (Python standard library). To reproduce them, run `c++ -std=c++17 -O2 verify_exhaustive.cpp -o check && ./check` and `python3 verify_transfer.py`. The exhaustive checker reports `EXHAUSTIVE_OK`, independently certifies all sector minima and counts, the twenty defect supports, the six critical degeneracies, and the lower convex-hull inequalities. The ring transfer reports `TRANSFER_EXACT_OK` and the identical thirteen-sector table. Their finite enumeration exhausts the entire finite sample space; no unproved extrapolation in system size is claimed.

## Relationship to prior work

Konstantinidis (2005, arXiv:cond-mat/0503658) studied quantum Heisenberg antiferromagnets on the same Platonic graph and the dodecahedron, demonstrating that icosahedral geometry supports physically consequential frustration, but did not study the classical three-state Potts Hamiltonian above. Kotecký, Salas and Sokal (2008, arXiv:0802.2270) studied a three-state Potts antiferromagnet on an infinite diced lattice rather than this finite icosahedral cluster. Chang and Shrock (2009, arXiv:0907.0925) established general external-field Potts partition-function representations and explicit strip-lattice transfer matrices: these are recognized as established tools; no new general Potts formalism is claimed. Nakamoto, Ota and Watanabe (2005, *Ars Combinatoria* 75, 157–162) studied the maximum number of trichromatic faces in plane triangulations, not the odd-vertex monochromatic-edge bound or this magnetic response. No numerical icosahedral three-color field diagram or twenty-support classification was located in the examined sources.

## Limitations

This is an exact finite-cluster zero-temperature result, not evidence of a finite-temperature thermodynamic phase transition. The graph has twelve labeled sites; the stated degeneracies count labeled configurations, not symmetry orbits. The infinite-family parity obstruction is elementary and may have antecedents in defective-coloring theory. Generic arbitrary-graph partition-function expressions and exact algorithms were known previously; their existence is not disputed. Unindexed older Potts, vertex-coloring, or Tutte-related tables may contain an equivalent icosahedral evaluation, so historical priority is not independently established. No claims about quantum dynamics, nonzero-temperature behavior, or larger icosahedral clusters are made.

## References

- N. P. Konstantinidis, *The Antiferromagnetic Heisenberg Model on Clusters with Icosahedral Symmetry*, arXiv:cond-mat/0503658, first submitted 2005-03-29. https://arxiv.org/abs/cond-mat/0503658
- A. Nakamoto, K. Ota and M. Watanabe, *On 3-coloring of plane triangulations*, *Ars Combinatoria* 75 (2005), 157–162. https://combinatorialpress.com/article/ars/Volume%20075/volume-75-paper-13.pdf
- R. Kotecký, J. Salas and A. D. Sokal, *Phase transition in the 3-state Potts antiferromagnet on the diced lattice*, arXiv:0802.2270, first submitted 2008-02-15. https://arxiv.org/abs/0802.2270
- S.-C. Chang and R. Shrock, *Structure of the Partition Function and Transfer Matrices for the Potts Model in a Magnetic Field on Lattice Strips*, arXiv:0907.0925, first submitted 2009-07-06. https://arxiv.org/abs/0907.0925
