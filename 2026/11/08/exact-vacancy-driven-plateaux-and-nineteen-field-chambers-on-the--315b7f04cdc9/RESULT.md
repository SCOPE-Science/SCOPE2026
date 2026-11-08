# Exact vacancy-driven plateaux and nineteen field chambers on the spin-one icosahedron

## Finding

Let \(G\) be the simple icosahedral graph, with twelve vertices and thirty edges. Consider the antiferromagnetic spin-one Blume–Capel Hamiltonian
\[
H_{J,D,h}(\sigma)=J\sum_{uv\in E(G)}\sigma_u\sigma_v+D\sum_{v\in V(G)}\sigma_v^2-h\sum_{v\in V(G)}\sigma_v,
\qquad \sigma_v\in\{-1,0,1\},\quad J>0,
\]
with arbitrary real uniform crystal-field parameter \(D\) and longitudinal field \(h\). Put \(\delta=D/J\) and \(x=|h|/J\). The exact ground energy for every \(\delta\in\mathbb R\) and \(x\ge0\) is
\[
\frac{E_0(D,h)}{J}=\min_{(K,M,b,g)\in\mathcal P}\{b+\delta K-xM\},
\]
where \(\mathcal P\) consists of precisely the nineteen rows in the table below. Each row is the unique minimizing occupancy-magnetization sector on a nonempty open region of the half-plane \(x>0\). Here \(K\) is the number of nonzero spins, \(M\) is the absolute total magnetization in the positive-field convention, \(b\) is the minimum exchange-bond sum at that sector, and \(g\) counts minimizing assignments with that sign of magnetization.

| \(K\) | \(M\) | \(b\) | \(g\) |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 |
| 3 | 3 | 0 | 20 |
| 4 | 4 | 1 | 30 |
| 6 | 2 | -5 | 30 |
| 6 | 6 | 5 | 72 |
| 7 | 1 | -7 | 60 |
| 7 | 5 | 0 | 12 |
| 8 | 0 | -8 | 150 |
| 8 | 2 | -7 | 60 |
| 8 | 8 | 11 | 30 |
| 9 | 9 | 15 | 20 |
| 10 | 2 | -8 | 240 |
| 10 | 4 | -5 | 60 |
| 10 | 6 | 1 | 30 |
| 11 | 5 | -3 | 60 |
| 12 | 0 | -10 | 72 |
| 12 | 4 | -6 | 30 |
| 12 | 6 | 0 | 20 |
| 12 | 12 | 30 | 1 |

At zero field the full diagram reduces to a **two-stage vacancy-driven change**:
\[
\frac{E_0(D,0)}{J}=\min\{-10+12\delta,\ -8+8\delta,\ 0\}.
\]
For \(\delta<1/2\), every ground configuration has twelve occupied sites, zero total magnetization, and there are exactly \(72\) such configurations. For \(1/2<\delta<1\), every ground configuration has eight occupied sites, zero total magnetization, and there are exactly \(150\). For \(\delta>1\), only the all-zero configuration survives. At the coexistence points, the full ground degeneracies are \(462\) at \(\delta=1/2\) and \(351\) at \(\delta=1\). At \(\delta=1/2\), occupancies \(K\in\{8,10,12\}\) occur; at \(\delta=1\), occupancies \(K\in\{0,6,7,8\}\) occur. Thus an odd-occupancy sector is a **boundary-only** ground sector despite not being one of the nineteen open chambers.

## Assumptions and scope

The vertex labeling used in the certificate is \(0\) (upper pole), \(1,\ldots,5\) (upper pentagon), \(6,\ldots,10\) (lower pentagon), and \(11\) (lower pole). With indices reduced modulo five, the thirty edges are the five upper-pole spokes, five lower-pole spokes, the two pentagon rings, and the ten links from upper vertex \(1+i\) to lower vertices \(6+i\) and \(6+(i-1\bmod 5)\). The same graph is specified without ambiguity by `edges.csv`. The coupling \(J\) is uniform and strictly positive, and the single-ion field and magnetic field are uniform but unrestricted in sign. At \(h=0\) both magnetization signs are counted; at nonzero \(h\) the ground magnetization aligns with the field whenever it is nonzero. The result concerns exact zero-temperature finite-cluster energies and counting, not finite-temperature bulk phase transitions.

The exact finite table `sector_minima.csv` supplies every ground-sector minimum and its degeneracy for \(M\ge0\), including sectors present only on transition boundaries. In all cases the negative-magnetization table is obtained by global spin inversion. For arbitrary \((D,h)\), compute the minimum over the table and sum the multiplicities of **all** attaining sectors, including both signs when \(h=0\) and \(M>0\); the nineteen-row minimum alone should not be used for coexistence degeneracies.

## Proof

For an assignment \(\sigma\), set
\[
K(\sigma)=\sum_v\sigma_v^2,\qquad
M(\sigma)=\sum_v\sigma_v,\qquad
B(\sigma)=\sum_{uv\in E(G)}\sigma_u\sigma_v.
\]
Its energy in units of \(J\) is \(B+\delta K-(h/J)M\). Global inversion fixes \(K,B\) and negates \(M\), so it suffices to examine \(M\ge0\) for \(h\ge0\). The allowed sector labels are exactly \(0\le K\le12\), \(0\le M\le K\) with \(K-M\) even: there are \(49\) sectors.

The exact finite enumeration certificate iterates over **all** \(3^{12}=531441\) assignments (no sampling). For each of the \(49\) sectors it records the minimum of the integer bond sum \(B\) and the number of assignments attaining that minimum. The complete table is `sector_minima.csv`; `verify_direct.py` independently regenerates the same integer data from the displayed graph definition. In particular, the zero-field minimum bond values at occupancies \(K=0,6,7,8,10,12\) are \(0,-6,-7,-8,-9,-10\), respectively, and their zero-field minimizing multiplicities are \(1,80,120,150,240,72\). Other sectors are retained in the complete table and are not silently discarded.

To obtain the compact nineteen-row energy formula **for every real** \(\delta\), `domination_certificates.json` gives for each of the thirty omitted nonnegative-magnetization sectors a convex combination of listed rows whose average occupancy equals that sector's occupancy, whose average magnetization is at least that sector's magnetization, and whose average minimum bond energy is at most that sector's minimum bond energy. All coefficients are exact nonnegative rational numbers summing to one. For \(x\ge0\), the same convex combination of row energies is no greater than the omitted sector's energy, so at least one listed row is no greater; hence the nineteen-row lower envelope is exhaustive. No assumption restricting the sign or magnitude of \(\delta\) is used.

Conversely, `open_chamber_witnesses.json` supplies a positive rational field \(x\) and rational crystal field \(\delta\) for each of the nineteen listed rows. Exact rational substitution into **all forty-nine** sector energies gives a strictly positive gap to every other sector, proving that each row is realized on an open two-dimensional region. These rational dominance and exposure checks establish the precise chamber count, rather than relying on a plotted or floating-point convex hull.

For \(h=0\), the sector table shows that only the three lines displayed above can be strictly minimal. Their crossings occur at \(\delta=1/2\) and \(\delta=1\). Summing all exactly tied sector counts gives \(72+240+150=462\) at the first crossing and \(1+80+120+150=351\) at the second. This includes the boundary-only sectors that are not exposed on any open field region.

## Verification

Run `python3 verify_direct.py` and `python3 verify_transfer.py` with Python 3 in the directory containing the bundled data. Both programs terminate with `VERIFY_OK` on the delivered data. The first checks all \(531441\) configurations, the graph's degree and triangular-face counts, the \(49\) minima, \(30\) exact rational dominance certificates, \(19\) exact rational chamber witnesses, and coexistence counts. The second contracts an upper pole and pentagon against a lower pole and pentagon by a distinct six-plus-six shell sum, reconstructing every sector minimum and multiplicity. The second implementation does not use the edge CSV to construct its bond interactions. The computations are finite and exhaustive; they do not represent an infinite-lattice proof or an independent external audit.

## Relationship to prior work

The antiferromagnetic spin-one Blume–Capel model with field and single-ion potential is a recognized statistical-mechanical setting; Kimel, Black, Carter and Wang (1987) examined its two-dimensional-lattice phase behavior by Monte Carlo. Konstantinidis (2005) computed icosahedral **quantum Heisenberg** spectra for spin-one operators, but without a tunable single-ion vacancy cost. Hucht, Sahoo, Sil and Entel (2012) studied **thirteen-site** Heisenberg clusters with radial uniaxial anisotropy, rather than this twelve-site classical axial product Hamiltonian. Suzuki, Tamura and Sugimoto (2021) studied classical vector and quantum Heisenberg interactions on an icosahedron, including longer-range couplings, not an on-site zero-spin occupancy mechanism. These models are not equivalent to the three-state axial Blume–Capel interaction.

An earlier exact three-state Potts antiferromagnet study of the icosahedron is likewise not a deduction of this claim: the Potts bond interaction is equality of neighboring colors, whereas here the exchange is the numerical product of spin components, with an additional tunable quadratic single-ion term. General exhaustive-enumeration and convex-hull methods exist; the specific nineteen-chamber and boundary-multiplicity evaluation is the claimed contribution, not either method in isolation.

## Limitations

This is an exact **finite twelve-site** result only. There are no claims about finite-temperature critical points, icosahedral quantum Heisenberg dynamics, nonuniform couplings, transverse fields, disorder, or thermodynamic limits. Open-chamber multiplicities differ from coexistence multiplicities; the complete sector table must be used on boundaries. Historical-priority risk remains for any unindexed or inaccessible calculation of the identical spin-one icosahedral axial model. Scientific novelty is assessed against the specifically inspected sources and searchable records, not asserted from absence of search hits alone.

## References

- J. D. Kimel, S. Black, P. Carter and Y.-L. Wang, “Monte Carlo study of the antiferromagnetic two-dimensional Blume-Capel model,” *Physical Review B* **35**, 3347 (1987), https://doi.org/10.1103/PhysRevB.35.3347.
- N. P. Konstantinidis, “The Antiferromagnetic Heisenberg Model on Clusters with Icosahedral Symmetry,” arXiv:cond-mat/0503658 (first submitted 2005-03-29), https://arxiv.org/abs/cond-mat/0503658.
- A. Hucht, S. Sahoo, S. Sil and P. Entel, “Effect of anisotropy on small magnetic clusters,” arXiv:1201.2088 (first submitted 2012-01-10), https://arxiv.org/abs/1201.2088.
- S. Suzuki, R. Tamura and T. Sugimoto, “Classical and Quantum Magnetic Ground States on an Icosahedral Cluster,” *Materials Transactions* **62**, 367–373 (2021), https://doi.org/10.2320/matertrans.MT-MB2020011.
