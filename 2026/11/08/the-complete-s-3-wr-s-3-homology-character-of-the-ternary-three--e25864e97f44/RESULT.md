# The complete \(S_3\wr S_3\) homology character of the ternary three-cube Rips complex

## Finding

Let \(T=\{0,1,2\}^3\) with Hamming distance \(d(u,v)=\#\{i:u_i\ne v_i\}\). Define \(X=\operatorname{VR}_{\leq2}(T)\), the abstract simplicial complex of all subsets of pairwise distance at most two. The natural coordinate-and-symbol permutation group \(G=(S_3)^3\rtimes S_3\) of order \(1296\) acts on \(X\). Its reduced rational homology is zero except in degree three, where it has dimension \(46\). The complete rational character \(\chi(g)=\operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))\) is the 22-class character displayed below. In particular,
\[
\dim\widetilde H_3(X;\mathbb Q)^G=0,
\qquad
\dim\widetilde H_3(X;\mathbb Q)^{C_3^3}=2,
\]
where \(C_3^3\) is the subgroup of three independent cyclic translations of alphabet symbols. The character has self-inner product \(7\).

For the class table, write each group element as \(g_{c;s_0,s_1,s_2}\) with \(c\in S_3\) and \(s_i\in S_3\), acting by \(g(x)_i=s_i(x_{c(i)})\). Each three-digit word denotes the images of \(0,1,2\) in order (for instance, `021` is the transposition of 1 and 2). Every row gives the class index, class size, element order, \(c\), the three \(s_i\), and character. The representatives fully identify the 22 conjugacy classes, including classes that share order or vertex-cycle type.

| Class | Size | Order | \(c\) | \(s_0/s_1/s_2\) | \(\chi\) |
|---:|---:|---:|:---:|:---:|---:|
| 0 | 216 | 6 | `120` | `012/012/021` | 0 |
| 1 | 162 | 4 | `021` | `021/012/021` | -2 |
| 2 | 144 | 9 | `120` | `012/012/120` | 1 |
| 3 | 108 | 6 | `021` | `021/012/120` | 0 |
| 4 | 108 | 12 | `021` | `120/012/021` | 0 |
| 5 | 72 | 6 | `021` | `120/012/120` | 1 |
| 6 | 72 | 3 | `120` | `012/012/012` | 4 |
| 7 | 54 | 6 | `012` | `021/021/120` | 0 |
| 8 | 54 | 4 | `021` | `012/012/021` | 0 |
| 9 | 54 | 2 | `021` | `021/012/012` | 0 |
| 10 | 36 | 6 | `012` | `012/021/120` | 0 |
| 11 | 36 | 6 | `012` | `021/120/120` | 0 |
| 12 | 36 | 6 | `021` | `012/012/120` | -2 |
| 13 | 36 | 6 | `021` | `120/012/012` | -2 |
| 14 | 27 | 2 | `012` | `012/021/021` | 6 |
| 15 | 27 | 2 | `012` | `021/021/021` | 0 |
| 16 | 18 | 2 | `021` | `012/012/012` | -14 |
| 17 | 12 | 3 | `012` | `012/120/120` | -2 |
| 18 | 9 | 2 | `012` | `012/012/021` | 0 |
| 19 | 8 | 3 | `012` | `120/120/120` | 1 |
| 20 | 6 | 3 | `012` | `012/012/120` | 4 |
| 21 | 1 | 1 | `012` | `012/012/012` | 46 |

## Assumptions and scope

The metric is discrete three-coordinate Hamming distance, not Euclidean distance and not shortest-path distance between arbitrary points of a continuous graph. The Rips convention is inclusive at scale two. Vertices are lexicographically ordered by \((a,b,c)\leftrightarrow9a+3b+c\). For homology and character assertions use rational coefficients and reduced homology; the finite mod-two homology calculation is a separate certificate. The group is the specified natural wreath-product action; no claim of an equivariant sphere-wedge splitting or integral representation-lattice classification is made.

## Proof

**Complex and homology.** A subset is a face if and only if each pair agrees in at least one coordinate; equivalently \(X=\operatorname{Ind}(K_3\times K_3\times K_3)\), where \(\times\) denotes the categorical graph product. Enumerate every nonempty clique recursively, choosing the smallest remaining vertex and intersecting remaining candidates with its graph-distance-at-most-two neighbor set. The nine face counts, from dimensions zero through eight, are
\[
(27,243,945,1728,1620,945,351,81,9).
\]
Exact bit-vector Gaussian elimination of every simplicial boundary over \(\mathbb F_2\) yields, in increasing boundary degree, the ranks
\[
(26,217,728,954,666,279,72,9).
\]
All faces and all boundaries are constructed in `verify_simplicial.py`; none are loaded from a hidden table. Thus the unreduced mod-two Betti numbers are \((1,0,0,46,0,0,0,0,0)\). Universal coefficients imply that each rational Betti number is at most the corresponding mod-two Betti number. The integer Euler characteristic computed directly from the face vector is \(-45\); hence \(b_0=1\), \(b_3=46\), and all other rational Betti numbers vanish. This conclusion does not assert torsion-freeness.

**Character via Lefschetz.** Since \(X\) is connected and its only positive-degree rational homology is in degree three, the simplicial Lefschetz formula gives
\[
\chi(g)=1-\sum_{d\ge0}(-1)^d\operatorname{tr}(g\mid C_d(X;\mathbb Q)).
\]
For each \(g\) and each invariant oriented simplex, the chain trace is the sign of the induced permutation of its vertices. `verify_simplicial.py` exhaustively computes these signs and traces for conjugacy-class representatives. The group is explicitly enumerated as the distinct \(1296\) vertex permutations arising from the prescribed action. Conjugation by eight natural generators partitions it into exactly 22 classes, of the displayed sizes, and verifies that these sizes total 1296.

**Independent orbit formula.** For a fixed \(g\), partition the 27 vertices into cycles of the permutation. An invariant face is exactly a nonempty union of vertex cycles that is still a simplex. If the union uses \(k\) cycles and \(s\) vertices, its trace contribution is \((-1)^{s-1}\cdot(-1)^{s-k}=(-1)^{k-1}\). It follows that
\[
\chi(g)=\sum_{\substack{A\text{ a collection of}\ g\text{-vertex orbits}\\\bigcup A\in X}}(-1)^{|A|},
\]
including the empty collection. `verify_orbits.py` independently evaluates this orbit-clique expression for **all 1296 elements**, agreeing with the signed-simplex character for all 22 tabulated representatives. The distribution on the entire group is 702 elements with trace 0, 246 with trace \(-2\), 224 with trace 1, 78 with trace 4, 27 with trace 6, 18 with trace \(-14\), and the identity with trace 46. The total character sum is zero, while the sum of squared character values is \(7\cdot1296\). Averaging over the full group proves the first invariant-dimension assertion.

For the subgroup of 27 translations \(x\mapsto x+t\) coordinatewise modulo three, the character values consist of the identity value 46, six values 4, eight values 1, and twelve values \(-2\). Their sum is 54; hence the translation-invariant dimension is \(54/27=2\). Both averaging arguments use Maschke's theorem over \(\mathbb Q\).

## Verification

From the unpacked package directory run `python3 verify_simplicial.py` followed by `python3 verify_orbits.py`. Both programs use only the Python standard library. The first produces `character_data.json` deterministically (also included for convenience), re-enumerates all 5,949 simplices, independently constructs every boundary, checks exact mod-two ranks, builds all 1296 group elements, closes all conjugacy classes, and calculates signed Lefschetz traces. The second independently uses only vertex-orbit admissibility to calculate all 1296 character values and checks the invariants and character norm. The recorded stdout files are `verify_simplicial_output.txt` and `verify_orbits_output.txt`.

## Relationship to prior work

Barmak's 2010 independence-complex work develops topological techniques for graph complexes but does not treat this metric-space symmetry character. Goyal–Shukla–Singh's 2019 work determines the nonequivariant independence-complex homotopy type of two-factor categorical complete-graph products. Antolín Camarena–Carnero Bravo's 2023 paper proves a three-factor result with a \(K_2\) factor and discusses broader conjectures; the present three \(K_3\) factors lie outside its proved family. A published finite computation of the exact 27-point Rips filtration gives \(X\simeq\bigvee^{46}S^3\), but no wreath-product homology character. Galetto–Montaño–Wellner's 2026 equivariant homology theorem concerns **binary** hypercubes, with symmetry groups of type \(C_2\wr S_n\), and does not determine the ternary \(S_3\wr S_3\) module. Thus the 46-sphere homotopy result and its Betti number are prior results; the **22-class symmetry character and fixed-subspace distinctions** are the contribution here. Known nonequivariant homotopy or a character for a different group action does not imply this character without further information.

## Limitations

This is one exact 27-vertex example, not a formula for arbitrary alphabet size or number of coordinates. It proves the rational representation's character, not integral torsion, an integral lattice decomposition, or an equivariant CW homotopy splitting. It does not establish full publication priority against every unindexed or inaccessible source. The finite computations are exhaustive but require standard trust in the code and its execution; they are not an independent external audit.

## References

1. J. A. Barmak, "Star clusters in independence complexes of graphs," arXiv:1007.0418v1 (first public 2010-07-02), https://arxiv.org/html/1007.0418v1.
2. S. Goyal, S. Shukla and A. Singh, "Homotopy Type of Independence Complexes of Certain Families of Graphs," arXiv:1905.06926 (first public 2019-05-16), https://arxiv.org/abs/1905.06926.
3. O. Antolín Camarena and A. Carnero Bravo, "Homotopy type of the independence complex of some categorical products of graphs," arXiv:2307.12401 (first public 2023-07-23), https://arxiv.org/abs/2307.12401.
4. F. Galetto, J. Montaño and Z. Wellner, "Homology of Vietoris-Rips complexes of hypercube graphs via group actions," arXiv:2606.20784 (first public 2026-06-18), https://arxiv.org/abs/2606.20784.
5. "Complete Vietoris–Rips persistence of the ternary three-cube," public mathematical research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-vietoris-rips-persistence-of-the-ternary-three-cube--62d7487289d8.
