# Spectral-tight Ising magnetization staircase on the Schläfli graph

## Finding
Let \(G\) be the Schläfli graph, the unique strongly regular graph with parameters \((27,16,10,8)\), equivalently the graph joining skew pairs among the \(27\) lines on a smooth cubic surface. For a subset \(T\) of \(k\) vertices, write \(b(T)\) for the number of edges between \(T\) and its complement, and put \(t=\min(k,27-k)\). **The exact cardinality-constrained maximum-cut law is**
\[
\max_{|T|=k} b(T)=16t-2\left\lceil\frac{t(t-3)}3\right\rceil,\qquad 0\le k\le27.
\]
In particular the rounded least-eigenvalue bound is attained for every cardinality, not merely at the global maximum.

Place classical spins \(\sigma_v\in\{-1,+1\}\) on the vertices with uniform antiferromagnetic coupling \(J>0\) and longitudinal field \(h\):
\[
H(\sigma)=J\sum_{\{u,v\}\in E(G)}\sigma_u\sigma_v-h\sum_v\sigma_v.
\]
For \(h>0\), the ground-state magnetization \(M=\sum_v\sigma_v\) and its multiplicity are exactly

| Field interval | Ground-state magnetization | Multiplicity |
|---|---:|---:|
| \(0<h<4J\) | \(3\) | 22968 |
| \(4J<h<8J\) | \(9\) | 8400 |
| \(8J<h<12J\) | \(15\) | 1080 |
| \(12J<h<16J\) | \(21\) | 45 |
| \(h>16J\) | \(27\) | 1 |

At the four positive critical fields \(h/J=4,8,12,16\), respectively, the ground-state multiplicities are \(630444,138000,10035,208\), with coexisting magnetizations \(\{3,5,7,9\}\), \(\{9,11,13,15\}\), \(\{15,17,19,21\}\), and \(\{21,23,25,27\}\). At zero field the energy is \(-24J\) and the ground-state multiplicity is \(1037376\): magnetizations \(\pm1\) occur \(495720\) times each and \(\pm3\) occur \(22968\) times each. Negative-field statements follow by global spin reversal.

## Assumptions and scope
The graph is simple and unweighted with \(27\) sites. The field \(h\) and coupling \(J\) are uniform and real with \(J>0\). The result describes the exact \(T=0\) classical Ising model (not the Heisenberg model and not a thermodynamic limit). The entropy-like multiplicities count labelled spin configurations, not symmetry orbits. A state with \(k\) negative spins has magnetization \(27-2k\), exchange energy \(J(216-2b(T))\), and field energy \(-h(27-2k)\).

## Proof
**Graph definition.** Label the vertices \(E_i,B_i\), for \(1\le i\le6\), and \(C_{ij}\), for \(1\le i<j\le6\). The *meeting* pairs are: \(E_iB_j\) for \(i\ne j\); \(E_iC_{jk}\) and \(B_iC_{jk}\) exactly when \(i\in\{j,k\}\); and \(C_{ij}C_{kl}\) exactly when the pairs of indices are disjoint. There are no other meeting pairs. The edges of \(G\) join distinct vertices that do **not** meet. These are the standard \(27\) line classes on a blown-up projective plane; direct inspection gives degree \(16\), and common-neighbor numbers \(10\) for adjacent and \(8\) for nonadjacent pairs. This identifies \(G\) as the Schläfli graph by uniqueness of these strongly regular parameters.

**Sharp upper bound.** Let \(A\) be the adjacency matrix of \(G\). Strong regularity gives \(A^2=2A+8I+8\mathbf 1\mathbf 1^{\mathsf T}\). Hence the eigenvalues off the constant vector are \(4\) and \(-2\), while the constant vector has eigenvalue \(16\). For the indicator vector \(x=\mathbf 1_T\) of a \(k\)-subset, decompose \(x=(k/27)\mathbf 1+y\) with \(y\perp\mathbf1\) and \(\|y\|^2=k-k^2/27\). Writing \(e(T)\) for the number of edges induced on \(T\),
\[
2e(T)=x^{\mathsf T}Ax\ge\frac{16k^2}{27}-2\left(k-\frac{k^2}{27}\right)=\frac{2k(k-3)}3.
\]
Because \(e(T)\) is an integer, \(e(T)\ge\lceil k(k-3)/3\rceil\). Since \(b(T)=16k-2e(T)\), this proves the claimed cut upper bound for \(0\le k\le13\). Taking complementary subsets proves the corresponding bound for \(14\le k\le27\).

**Sharpness certificate.** In the vertex order \(E_1,\dots,E_6,B_1,\dots,B_6,C_{12},C_{13},\dots,C_{56}\) (the last \(15\) labels in lexicographic order), bit \(i\) of a hexadecimal mask selects the vertex at zero-based index \(i\). For every \(k\in\{0,\dots,13\}\), the following masks have \(k\) set bits and achieve the upper bound. This short finite list is a witness of existence, not a sampling argument.

| \(k\) | Mask | \(b(T)\) | \(e(T)\) |
|---:|---|---:|---:|
| 0 | `0x0000000` | 0 | 0 |
| 1 | `0x0000001` | 16 | 0 |
| 2 | `0x0000060` | 32 | 0 |
| 3 | `0x0001081` | 48 | 0 |
| 4 | `0x00000cc` | 60 | 2 |
| 5 | `0x00000dc` | 72 | 4 |
| 6 | `0x00001f8` | 84 | 6 |
| 7 | `0x00001f9` | 92 | 10 |
| 8 | `0x00003f3` | 100 | 14 |
| 9 | `0x00019db` | 108 | 18 |
| 10 | `0x00007ef` | 112 | 24 |
| 11 | `0x00007ff` | 116 | 30 |
| 12 | `0x0000fff` | 120 | 36 |
| 13 | `0x0001fff` | 120 | 44 |

Each value in the last two columns is verified independently by direct edge tests in `verify.cpp`; thus the bound is attained for every \(k\), with complement symmetry handling the other half.

**Magnetic envelope.** The integer function \(B(k)=\max_{|T|=k}b(T)\) for \(0\le k\le13\) has successive slopes \(16\) for \(k\in[0,3]\), \(12\) for \(k\in[3,6]\), \(8\) for \(k\in[6,9]\), \(4\) for \(k\in[9,12]\), and \(0\) for \(k\in[12,13]\), where slope intervals here denote segments between integer abscissae. Minimizing \(J(216-2B(k))-h(27-2k)\) is equivalent to maximizing \(B(k)-hk/J\); its supporting slopes give the four critical field ratios \(4,8,12,16\), with the stated interior magnetizations and the collinear sectors at the critical fields. For \(h>0\), a minimizing state has \(k\le13\): the complementary state has the same exchange energy and greater field alignment. Spin reversal gives \(h<0\).

**Multiplicity certificate.** The maximum cut at each cardinality has the following exhaustive integer multiplicity for \(0\le k\le13\), in increasing \(k\):
\[
(1,27,135,45,2160,6750,1080,42120,86400,8400,247860,351216,22968,495720).
\]
The exact cardinality-complement symmetry supplies the other fourteen counts. The accompanying standalone checker proves these finite values by visiting all \(2^{27}=134217728\) subsets twice: once by reflected Gray code and once by an independent binary-recursion traversal. In the recursion, adjoining vertex \(i\) to a selected set with mask \(S\) changes the cut by \(16-2|N(i)\cap S|\). The two branches are exhaustive and disjoint at every vertex, and the checker verifies that sector visitation totals are \(\binom{27}{k}\). Both algorithms agree on the exact optimum and multiplicity in every sector; direct edge-sum spot checks and all explicit witnesses are also tested. Adding optimum-sector counts at the supporting lines of the envelope gives the displayed field-degeneracy values. The spectrum claims are finite exhaustive results, not extrapolated from a bounded sample.

## Verification
Compile the self-contained `verify.cpp` with `c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify` and run `./verify`. The script checks graph order, edges, strong-regularity parameters, the eigenvalue bound's tightness using exact integer arithmetic, all \(28\) cardinality counts against two exhaustive traversals, the \(14\) written sharpness witnesses, and the five critical/zero-field degeneracy totals. Its successful output begins with `VERIFY_OK vertices=27 edges=216 subsets_per_graph=134217728 independent_enumerations=2`. `profiles.csv` records the optimum cut and its multiplicity for every cardinality, including the complements.

## Relationship to prior work
The standard graph structure and the general \(\operatorname{GQ}(2,4)\) and \(E_6\) connections are established in the finite-geometry literature; the facts that the graph has \(27\) vertices, chromatic number \(9\), and several special coclique/colouring orbits are not asserted as new. The standard spectral Hoffman method supplies the inequality used above; the assessed contribution is its **rounded sharpness at every subset cardinality**, with exact optimizer multiplicities, and the resulting complete field-dependent Ising ground-state staircase. Vinci and colleagues define longitudinal-field Ising spectral refinements for arbitrary graphs, but their examples are different finite graphs and do not imply this graph-specific exact classification. The known spectral/chromatic application of the Schläfli graph likewise does not enumerate cut optimizers or magnetization sectors.

## Limitations
This is a finite, labelled \(27\)-spin, zero-temperature result, not a phase transition in an infinite thermodynamic system. It assumes unit graph adjacency, uniform \(J>0\), and a uniform longitudinal field. It does not determine positive-temperature partition functions, quantum transverse-field spectra, or perturbations of the graph. Some low-cardinality orbit counts, especially independent triples, were known separately; the all-cardinality and field classifications are the contribution assessed here. Historical priority against unindexed older Ising tables or detailed Schläfli subset-orbit catalogues has not been independently established.

## References
1. M. Saniga, R. M. Green, P. Lévay, P. Pracna, and P. Vrana, *The Veldkamp Space of GQ(2,4)*, arXiv:0903.0715 (first posted 2009-03-04), https://arxiv.org/abs/0903.0715.
2. W. Vinci, K. Markström, S. Boixo, A. Roy, F. M. Spedalieri, P. A. Warburton, and S. Severini, *Hearing the Shape of the Ising Model with a Programmable Superconducting-Flux Annealer*, arXiv:1307.1114 (first posted 2013-07-03), https://arxiv.org/abs/1307.1114.
3. A. E. Brouwer, *Schläfli graph*, finite-geometry reference, https://jaanos.github.io/tables/graphs/Schlaefli.html.
4. M. Dutour Sikirić, D. A. Madore, P. Moustrou, and F. Vallentin, *Coloring the Voronoi tessellation of lattices*, Journal of the London Mathematical Society 104 (2021), Section 5.2.4, https://doi.org/10.1112/jlms.12456.
