# Exact Hilbert-space fragmentation of face-resonating dimers on truncated prisms

## Finding
For each integer \(n\geq3\), truncate every vertex of the cubic prism \(C_n\square K_2\) into a triangle and retain the resulting \(n+2\) polygonal faces as the *only* allowed quantum-dimer resonance plaquettes. The resulting \(6n\)-vertex truncated prism has exactly \(2^{n+1}\) perfect-matchings (close-packed dimer coverings). Its face-flip graph has the following **complete component classification**:

1. One distinguished component is the graph obtained by identifying the empty-independent-set vertex of the Lucas cube \(\Lambda_n\) with one vertex of a four-cycle \(C_4\). Its order is \(L_n+3\), where \(L_n=F_{n-1}+F_{n+1}\) is the Lucas number, and \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\).
2. Exactly \(2^n-2\) configurations are isolated in one parity sector.
3. For every nonempty proper subset \(B\subsetneq\mathbb Z/n\mathbb Z\) in which every \(i\in B\) has at least one cyclic neighbor in \(B\), there is exactly one further component, the independent-set toggle graph of the subgraph induced on \(F_B=(\mathbb Z/n\mathbb Z)\setminus N[B]\). Its number of vertices is \(I(C_n[F_B];1)\), the number of independent vertex subsets of the indicated induced graph. Every component is exhausted by these cases.

Let \(b_n\) count the cyclic binary words of length \(n\) with no isolated \(1\) (equivalently, no cyclic occurrence of \(010\)). Then \(b_3=5\), \(b_4=10\), \(b_5=17\), and \(b_n=2b_{n-1}-b_{n-2}+b_{n-3}\) for \(n\geq6\). The exact number of dynamically disconnected components is
\[
\boxed{K_n=2^n+b_n-3.}
\]
The number of completely frozen dimer coverings (zero face flips) is
\[
\boxed{Z_n=2^n-3+\begin{cases}L_n,&n\text{ odd},\\L_{n/2}^{\,2},&n\text{ even}.\end{cases}}
\]
In the equal-positive-amplitude Rokhsar--Kivelson Hamiltonian \(H_{t,v}\) specified below, \(\dim\ker H_{t,t}=K_n\), while for \(v>t>0\) the zero-energy ground-state degeneracy is \(Z_n\); for \(v<t\), the ground energy is strictly negative. Both \(K_n/2^{n+1}\) and \(Z_n/2^{n+1}\) tend to \(1/2\) as \(n\to\infty\). At \(n=4\), the ordinary truncated cube has 32 coverings, exactly 23 connected sectors, 22 frozen coverings, and a ten-state resonance component consisting of three four-cycles meeting at one common vertex.

## Assumptions and scope
The prism \(P_n=C_n\square K_2\) has vertices \(u_i,w_i\) for \(i\in\mathbb Z/n\mathbb Z\), with top rim edges \(u_iu_{i+1}\), lower rim edges \(w_iw_{i+1}\), and rungs \(u_iw_i\). Replace every original cubic vertex by a triangle: the new graph has one vertex for every oriented edge \((x,y)\) of \(P_n\), joins the three oriented edges with common origin in an internal triangle, and joins \((x,y)\) to \((y,x)\) along each original edge. This is a simple planar graph with \(6n\) vertices, \(9n\) edges, \(2n\) triangular faces, \(n\) octagonal faces, and two \(2n\)-gonal faces. The faces under consideration are precisely the \(n\) octagons and the two \(2n\)-gons; triangular faces cannot support an alternating perfect-matching flip.

Every perfect matching \(M\) is a basis ket \(\lvert M\rangle\). Two coverings \(M,M'\) are joined by a single face flip if their symmetric difference is precisely the full edge set of one specified even face (thus \(M\) alternates occupied and unoccupied edges around that face). All face flips have the same positive kinetic coefficient \(t>0\). For any real potential coefficient \(v\), define
\[
H_{t,v}=\sum_{\{M,M'\}\in E(\mathcal R_n)}\Big(v\lvert M\rangle\langle M\rvert+v\lvert M'\rangle\langle M'\rvert-t\lvert M\rangle\langle M'\rvert-t\lvert M'\rangle\langle M\rvert\Big),
\]
where \(\mathcal R_n\) is the undirected face-flip graph. Equivalently, the diagonal energy of \(M\) is \(v\) times the number of flippable faces at \(M\). No other exchanges, potentials, detunings, or hopping processes are included. The ground-state degeneracy statements concern this precisely defined finite-dimensional Hamiltonian.

The Lucas cube \(\Lambda_n\) has as vertices the independent subsets of \(C_n\), with an edge when a single vertex is added or deleted. \(I(G;1)\) denotes the number of independent vertex subsets of \(G\), including the empty set. \(N[B]\) is the closed neighborhood of \(B\) in \(C_n\). The convention \(L_2=3\) is used in the even case \(n=4\).

## Proof
**1. Dimer coverings as odd-degree edge selections.** At a triangle replacing a cubic prism vertex, a perfect matching uses either all three external incident edges, or one external edge and the internal edge pairing its two remaining triangle vertices. Hence the selected external edges form a subset of prism edges of *odd* degree at each original vertex (one or three); conversely each such subset fixes a unique perfect matching of the truncated graph. The \(2n\)-vertex prism is connected with \(3n\) edges. Its vertex-edge incidence matrix over \(\mathbb F_2\) has rank \(2n-1\). The all-ones odd-degree parity constraint is consistent because there are an even number of original vertices. The affine solution space therefore has dimension \(3n-(2n-1)=n+1\), giving \(2^{n+1}\) coverings. This odd-subgraph encoding is established in earlier truncated-cube matching literature and is used here as a starting point, not itself claimed as new.

**2. Explicit coordinates and face moves.** Write \(a_i,b_i,c_i\in\{0,1\}\) for selection of the original top, lower, and rung edge at column \(i\). At every vertex, the parity equations are
\[
a_{i-1}\oplus a_i\oplus c_i=1,\qquad b_{i-1}\oplus b_i\oplus c_i=1.
\]
Subtracting modulo two gives \(a_i\oplus b_i=d\) independent of \(i\), for some \(d\in\{0,1\}\), and the unique solution is
\[
b_i=a_i\oplus d,\qquad c_i=1\oplus a_{i-1}\oplus a_i.
\]
Thus each matching corresponds bijectively to a binary cycle word \(a=(a_0,\ldots,a_{n-1})\) and one parity bit \(d\).

A truncated face above an original base-face cycle is alternating exactly when *either all or none* of the original edges in that base face are selected: at each vertex along the base face, the third external edge is then necessarily selected by odd parity, and the internal triangle edges complete one of the two alternating patterns. An octagon above the \(i\)-th prism square has base edges \(a_i,b_i,c_i,c_{i+1}\). All are equal if and only if
\[
d=0,\qquad a_{i-1}=a_{i+1}=1.
\]
Its flip changes only \(a_i\mapsto1-a_i\), leaving \(d\) fixed. Either \(2n\)-gonal end face is flippable exactly if every \(a_i\) is equal (necessarily every \(c_i=1\)). The upper-end flip complements all bits \(a_i\) and changes \(d\mapsto1-d\); the lower-end flip changes \(d\mapsto1-d\) while leaving \(a\) unchanged. These formulas account for every face in the specified Hamiltonian.

**3. Frozen zero cores and connected components.** Within \(d=0\), define
\[
B(a)=\{i:a_i=0\ \text{and}\ (a_{i-1}=0\ \text{or}\ a_{i+1}=0)\}.
\]
Every square flip toggles only a bit with both neighbors equal to one. It cannot create or remove a pair of adjacent zeros, so \(B(a)\) is conserved. Any nonempty \(B(a)\) has no isolated vertex in its induced cyclic subgraph. Conversely take any \(B\) with this property. The zeros belonging to \(B\) are permanently immobile, every vertex in \(N[B]\setminus B\) is permanently a one, and additional zeros are precisely arbitrary independent subsets of \(F_B=V(C_n)\setminus N[B]\). The facilitated square flips are exactly the add/delete moves for these independent subsets, so this entire fixed-core component is the independent-set toggle graph on \(C_n[F_B]\). It is connected: remove each additional zero and then insert the chosen independent zeros.

When \(B=\varnothing\), all zero positions are independent in the full cycle, giving the Lucas cube \(\Lambda_n\) with \(L_n\) vertices. When \(B=V(C_n)\), the only square-flip state is the all-zero word at \(d=0\). The end-face moves exist *only* in the four states with constant \(a\) and \(d\in\{0,1\}\), and form one four-cycle. It meets the Lucas cube at the all-one word with \(d=0\), and includes the all-zero \(d=0\) state plus the two constant-word \(d=1\) states. Every nonconstant word in \(d=1\) is isolated. Hence the component classification in the finding is exhaustive, and the largest connected component has \(L_n+3\) states (all remaining components embed as proper independent-set subgraphs of \(\Lambda_n\)).

**4. Exact component and frozen counts.** The admissible cores \(B\), including the empty and the entire vertex set, are precisely cyclic binary words with no isolated \(1\), equivalently with no cyclic substring \(010\). Let \(b_n\) count them. The two admissible extremes belong to the single distinguished component, and the other \(b_n-2\) core types contribute one component each. The \(d=1\) sector supplies \(2^n-2\) isolated components; therefore \(K_n=1+(b_n-2)+(2^n-2)=2^n+b_n-3\).

For the recurrence, use a transition matrix indexed by ordered bit pairs \(00,01,10,11\), allowing a transition from \(ab\) to \(bc\) unless \(abc=010\):
\[
T=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&1&0&0\\0&0&1&1\end{pmatrix}.
\]
A closed length-\(n\) walk corresponds bijectively to a labeled cyclic admissible binary word, so \(b_n=\operatorname{tr}(T^n)\). Direct determinant calculation gives \(\det(xI-T)=x(x^3-2x^2+x-1)\); Cayley--Hamilton gives the stated order-three recurrence, with initial values \(5,10,17\) at sizes \(3,4,5\).

A word \((a,0)\) has **no square flip** precisely when no cyclic pair of its one-bits lies at distance two: \(a_{i-1}a_{i+1}\ne11\) for every \(i\). This is an independent set of the distance-two cycle graph, which has \(L_n\) possibilities for odd \(n\), or \(L_{n/2}^2\) possibilities for even \(n\) (for \(n=4\), each factor is the three independent subsets of a single edge). Exclude the all-zero word because its end-face flip is available; all other such words are frozen. In \(d=1\), exactly the \(2^n-2\) nonconstant words are frozen. Summing gives \(Z_n\).

**5. Exact quantum ground-state degeneracies and asymptotics.** Let \(A_n\) and \(D_n\) be the adjacency and degree matrices of the face-flip graph. Then \(H_{t,v}=vD_n-tA_n=t(D_n-A_n)+(v-t)D_n\). At \(v=t\), each undirected flip contributes the positive rank-one operator \(t(\lvert M\rangle-\lvert M'\rangle)(\langle M\rvert-\langle M'\rvert)\). Its kernel consists exactly of vectors constant on each connected component, giving \(\dim\ker H_{t,t}=K_n\). For \(v>t\), every nontrivial component has strictly positive energy because \(D_n\) is positive definite on that component, whereas the isolated basis states have energy zero; the ground multiplicity equals \(Z_n\). For \(v<t\), testing the uniform vector on the distinguished component gives strictly negative energy because \(v-t<0\) and the component contains an edge, so the global ground energy is negative. No general negative-side ground multiplicity is claimed.

The forbidden-substring condition implies \(b_n\leq2^n(7/8)^{\lfloor n/3\rfloor}\) by considering disjoint triples, so \(b_n/2^n\to0\). The Lucas numbers grow as \(O(\varphi^n)\), where \(\varphi=(1+\sqrt5)/2<2\), and thus the correction to \(Z_n\) is also \(o(2^n)\). This proves both limiting one-half fractions. At \(n=4\), the Lucas cube is two squares meeting at the all-one word and the end-face square adds a third, yielding the stated ten-vertex bouquet and 22 further isolated states.

## Verification
Two independent standalone standard-library Python 3 programs are embedded. `verify_prism_bits.py` constructs all \((a,d)\) words directly, builds face-flip adjacency, performs a complete component traversal, and compares every actual connected component with the corresponding invariant-core prediction for each \(3\le n\le11\). It independently checks every predicted component size as an induced-subgraph independence-set count. `verify_truncated_graph.py` does not use those bit transitions: it builds the actual \(6n\)-vertex truncated-polyhedron graph from oriented base edges, enumerates perfect matchings using vertex-covering backtracking, constructs the physical polygonal faces, tests alternating face cycles, and performs a separate flip-graph traversal for \(3\le n\le7\). Both scripts completed successfully. No finite test is used to extrapolate the theorem: all \(n\ge3\) follow from the algebraic encoding and invariant-core classification above.

| \(n\) | Coverings | Face-flip components | Largest component | Frozen states |
|---:|---:|---:|---:|---:|
| 3 | 16 | 10 | 7 | 9 |
| 4 | 32 | 23 | 10 | 22 |
| 5 | 64 | 46 | 14 | 40 |
| 6 | 128 | 90 | 21 | 77 |
| 7 | 256 | 176 | 32 | 154 |
| 8 | 512 | 343 | 50 | 302 |

## Relationship to prior work
Rokhsar and Kivelson [1] introduced the plaquette kinetic/potential quantum-dimer Hamiltonian and the general fact that at its equal-coupling point each flip component has one uniform zero-energy state. Neither that general principle nor the Lucas-cube count is claimed to be new. Røising and Zhang [2] analyze ergodicity of dimers on finite sections of planar Archimedean lattices with specified local ring exchanges; those are not the spherical truncated-prism polyhedra with both octagonal and end-face exchanges classified here. Žigert Pleteršek and Berlič [3] prove Lucas-cube resonance components for cyclic fibonacene hexagon systems, a different substrate and move set; that result does not enumerate the nonempty-core product sectors here.

The previously published truncated-cube perfect-matching-complex calculation [4] explicitly proves the 32 matching count and the odd-subgraph correspondence for the cube. This starting fact is credited, and its simplicial contractibility does not determine the *face-flip* adjacency, the 22 frozen states, the 23 ground-state sectors, or the all-\(n\) formula. A published prism/Möbius ladder square-flip result [5] obtains Lucas-cube moving components on the **untruncated** \(2n\)-vertex ladder with a different perfect-matching space; it does not imply a count of all components after vertex truncation and the additional end-face flips. The hypercube quantum-dimer flip classification [6] concerns coordinate squares of higher-dimensional binary cubes rather than truncated polyhedral faces. These comparisons are structural, not title-based. Possible unindexed equivalent treatments of the facilitated binary dynamics and the same truncated-prism application remain a priority uncertainty.

## Limitations
The exact sector count and eigenvalue-zero claims apply only to vertex-truncated cubic prism graphs, all and only their polygonal face alternations, uniform positive kinetic amplitude, and the precisely stated diagonal flippability potential. Adding longer-loop resonances, nonuniform flip amplitudes, or additional physical Hamiltonian terms can connect previously frozen sectors or move zero energies. This is a finite-network statement for each \(n\), not a thermodynamic phase transition or a proof of experimental realization. No formula for the entire positive-excitation spectrum, negative-potential ground degeneracies, or the dynamics on arbitrary truncated cubic graphs is claimed. An independent scientific audit has not been performed; a comprehensive historical uniqueness guarantee is not possible.

## References
[1] D. S. Rokhsar and S. A. Kivelson, *Superconductivity and the Quantum Hard-Core Dimer Gas*, Physical Review Letters 61, 2376--2379 (14 November 1988), DOI:10.1103/PhysRevLett.61.2376. https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.61.2376/fulltext

[2] H. S. Røising and Z. Zhang, *Ergodic Archimedean dimers*, arXiv:2303.04817, first public 8 March 2023. https://arxiv.org/abs/2303.04817

[3] P. Žigert Pleteršek and M. Berlič, *The Structure of Lucas Cubes and Maximal Resonant Sets of Cyclic Fibonacenes*, MATCH Communications in Mathematical and in Computer Chemistry 69 (2013), 707--720. https://match.pmf.kg.ac.rs/electronic_versions/Match69/n3/match69n3_707-720.pdf

[4] *Contractibility of the truncated-cube perfect-matching complex*, published 8 November 2026, result ID `2026/11/8/SCOPE-contractibility-of-the-truncated-cube-perfect-matching-complex--4d36c4fccd0e`, available at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-contractibility-of-the-truncated-cube-perfect-matching-complex--4d36c4fccd0e

[5] *Twist-parity duality for square-flip reconfiguration of ladder matchings*, published 8 November 2026, result ID `2026/11/8/SCOPE-twist-parity-duality-for-square-flip-reconfiguration-of-ladder-m--8e7090802d17`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-twist-parity-duality-for-square-flip-reconfiguration-of-ladder-m--8e7090802d17

[6] *Frozen sectors and exact square-flip connectivity in hypercube quantum-dimer configurations*, published 8 November 2026, result ID `2026/11/8/SCOPE-frozen-sectors-and-exact-square-flip-connectivity-in-hypercube-q--db180e339d90`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-frozen-sectors-and-exact-square-flip-connectivity-in-hypercube-q--db180e339d90
