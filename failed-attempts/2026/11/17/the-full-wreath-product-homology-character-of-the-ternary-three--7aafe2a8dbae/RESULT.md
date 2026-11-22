# The full wreath-product homology character of the ternary three-cube Rips complex

## Finding
Let \(X=\{0,1,2\}^3\) carry Hamming distance and let \(K=\operatorname{VR}_{\le2}(X)\) be the *inclusive* scale-two Vietoris–Rips complex. The full Hamming-isometry group \(G=(\mathfrak S_3)^3\rtimes\mathfrak S_3=\mathfrak S_3\wr\mathfrak S_3\) acts by separate permutations of the three symbols on each axis and permutation of the three axes.

Let \(T\), \(A\), and \(V\) denote the trivial, alternating, and two-dimensional standard rational irreducible representations of the alphabet group \(\mathfrak S_3\). Write \(W_{\lambda_T,\lambda_A,\lambda_V}\) for the corresponding irreducible rational wreath-product representation indexed by three partitions whose total number of boxes is three, and write \(\varnothing\) for the empty partition. Then the **complete rational homology representation** is
\[
\begin{aligned}
\widetilde H_3(K;\mathbb Q)\cong{}&
W_{\varnothing,\varnothing,(1,1,1)}
\oplus W_{\varnothing,(1),(1,1)}
\oplus W_{\varnothing,(1,1),(1)}
\\&\oplus W_{\varnothing,(1,1,1),\varnothing}
\oplus W_{(1),\varnothing,(1,1)}
\oplus W_{(1,1),\varnothing,(1)}
\oplus W_{(1,1,1),\varnothing,\varnothing}.
\end{aligned}
\]
Their respective dimensions are \(8,12,6,1,12,6,1\), with multiplicity one for each and zero for all other irreducibles. Every other reduced rational homology group vanishes; integrally, \(K\simeq\bigvee^{46}S^3\).

Moreover, the subspace invariant under all *independent alphabet relabelings* \((\mathfrak S_3)^3\) has dimension one, and coordinate permutations act on this invariant line through their **sign character**. In particular,
\[
\widetilde H_3(K;\mathbb Q)^G=0,
\qquad
\widetilde H_i(|K|/G;\mathbb Q)=0\quad\text{for every }i\ge0.
\]
The last conclusion asserts rational acyclicity of the geometric quotient, not contractibility.

## Assumptions and scope
Everything concerns the exactly \(27\) points of the three-factor ternary Hamming space, threshold \(2\), and the complete natural wreath-product action. A subset is a simplex precisely when no two elements differ in all three coordinates. Thus \(K\) is also the independence complex of the *categorical* graph product of three triangles, \(\operatorname{Ind}(K_3\times K_3\times K_3)\); the graph product is not Cartesian. All character and quotient claims use rational coefficients. The homotopy classification is integral.

The three wreath-product labels have the following meaning. For a partition triple of total weight three, form the subgroup that preserves blocks of axes of sizes equal to the partition weights; put \(T\), \(A\), or \(V\) on the axes of its respective block, tensor the indicated Specht representation for permutations within each block, and induce to \(G\). This standard construction produces all \(22\) irreducible rational representations.

## Proof
**Finite homotopy certificate.** Represent a vertex \((a,b,c)\) by its lexicographic index and a face by its \(27\)-bit characteristic mask. Exhaustively enumerate independent sets of the graph whose edges connect points different in all coordinates. The resulting numbers of faces by vertex cardinality, including the empty face, are
\[
(1,27,243,945,1728,1620,945,351,81,9).
\]
Starting with all faces, process vertices in lexicographic order. At vertex \(v\), pair an as-yet-unmatched face \(F\) without \(v\) with \(F\cup\{v\}\) when both remain unmatched; delete both and continue. Omit the pair between the empty face and the first vertex so that one critical zero-cell remains. The explicit exhaustive certificate `verify_ternary_symmetry.py` finds \(2951\) pairs, one critical vertex and exactly \(46\) critical three-faces, with no other nonempty critical faces. Direct every codimension-one face incidence downward except pairs, which point upward. A complete topological sort checks that the resulting \(5950\)-node, \(27216\)-incidence directed Hasse graph has no cycle. The acyclic discrete-Morse theorem then gives a CW model with one zero-cell and \(46\) three-cells; their attaching maps are necessarily constant. Hence \(K\simeq\bigvee^{46}S^3\). This independently establishes that the only nonzero reduced rational homology is \(46\)-dimensional in degree three, so no assumption about missing homology is needed for the subsequent trace calculation.

**Lefschetz character.** For \(g\in G\), the reduced simplicial Lefschetz number is
\[
\widetilde L(g)=-1+\sum_{\substack{\emptyset\ne F\in K\\gF=F}}
(-1)^{|F|-1}\operatorname{sgn}(g|_F).
\]
Since reduced homology is concentrated in degree three, \(\chi_3(g)=\operatorname{tr}(g|\widetilde H_3)=-\widetilde L(g)\). Any invariant face is a union of vertex-orbits of \(g\); discard orbits that contain a forbidden pair, and form a graph whose vertices are remaining orbits and whose edges record pairs that cannot coexist in one face. A fixed face built from \(j\) selected orbits contributes \((-1)^{j+1}\) to \(\widetilde L(g)\), because the permutation orientation sign is \((-1)^{|F|-j}\). Therefore the homology trace is exactly the signed independence polynomial at \(-1\) of the orbit-conflict graph. This argument includes the empty face and handles all permutation signs; it is not a fixed-face count without orientation.

Conjugacy classes of \(G\) are indexed by cycle lengths of the axis permutation, with each axis-cycle colored by the conjugacy class of its composite alphabet permutation: `e` for identity, `t` for transposition, and `c` for a three-cycle. The exact class sizes and calculated third-homology traces are:

| Axis cycles | Alphabet cycle labels | Class size | Character |
|:--|:--|--:|--:|
| `111` | `eee` | 1 | 46 |
| `111` | `eet` | 9 | 0 |
| `111` | `eec` | 6 | 4 |
| `111` | `ett` | 27 | 6 |
| `111` | `etc` | 36 | 0 |
| `111` | `ecc` | 12 | -2 |
| `111` | `ttt` | 27 | 0 |
| `111` | `ttc` | 54 | 0 |
| `111` | `tcc` | 36 | 0 |
| `111` | `ccc` | 8 | 1 |
| `21` | `ee` | 18 | -14 |
| `21` | `et` | 54 | 0 |
| `21` | `ec` | 36 | -2 |
| `21` | `te` | 54 | 0 |
| `21` | `tt` | 162 | -2 |
| `21` | `tc` | 108 | 0 |
| `21` | `ce` | 36 | -2 |
| `21` | `ct` | 108 | 0 |
| `21` | `cc` | 72 | 1 |
| `3` | `e` | 72 | 4 |
| `3` | `t` | 216 | 0 |
| `3` | `c` | 144 | 1 |

**Irreducible decomposition.** The three irreducible characters of the base \(\mathfrak S_3\), on the identity, transposition, and three-cycle classes, are respectively \((1,1,1)\), \((1,-1,1)\), and \((2,0,-1)\). For a labeled axis-cycle, the trace in a tensor power of one base module equals the base character evaluated on the composite permutation around that axis-cycle. The standard induced-wreath character formula sums over assignments of the axis-cycles to the three base-module types, with total assigned cycle lengths prescribed by each partition's size, multiplying the corresponding symmetric-group Specht character and the base character factors. Since there are only three axes, the symmetric-group characters involved have degree at most three. The verifier generates all \(22\) irreducible characters, confirms their weighted pairwise orthogonality, and computes each multiplicity via the full class-character inner product. The seven displayed irreducibles occur once; the other fifteen occur zero times. Their dimensions sum to \(46\), independently checking the identity character.

**Invariant line and quotient.** Averaging the class character over the normal alphabet subgroup of order \(216\) gives a one-dimensional invariant subspace. Averaging over that subgroup after an axis-transposition, respectively an axis-three-cycle, gives traces \(-1\), respectively \(+1\), on the line. Hence its axis-symmetry character is the sign representation, and averaging over the entire group of order \(1296\) gives zero invariants. After barycentric subdivision, rational cellular chains on the geometric quotient identify with the group coinvariants, whose homology equals invariants in characteristic zero by averaging. The reduced rational homology of \(|K|/G\) is therefore zero in every degree.

## Verification
Run `python verify_ternary_symmetry.py` from the directory containing that file. It uses only the Python standard library and no network or external packages. The file enumerates every face, constructs and verifies the Morse matching against every Hasse incidence, evaluates the homology character in *two separately implemented ways* (signed oriented simplicial fixed-face traces and signed independent-set recursion on orbit-conflict graphs), and compares both for all \(22\) conjugacy classes. It also checks all \(1296\) group elements against their class characters, recomputes class sizes from centralizers, verifies all \(22\) irreducible characters' orthogonality, and recomputes the complete irreducible multiplicities. A transcript of the output is `verification_output.txt`. All computations are exact integer arithmetic.

## Relationship to prior work
Galetto, Montaño and Wellner (arXiv:2606.20784, first public June 18, 2026) establish irreducible symmetry decompositions for **binary** hypercubes under their hyperoctahedral groups, motivating this distinct ternary setting. Goyal, Shukla and Singh (2021, Proposition 3.4) calculate the independence-complex homotopy of categorical products of **two** complete graphs; Antolín Camarena and Carnero Bravo (2023/2024) settle certain three-factor cases with a \(K_2\) factor, not this three-\(K_3\) representation. A previously published ternary three-cube calculation determines the nonequivariant rank \(46\); the rank and wedge type are background and are independently rechecked here, **not** presented as new. The present contribution is the full \(22\)-class wreath-product homology character and seven-irreducible decomposition, including the sign action on the alphabet-fixed line. No stronger result establishing that complete representation was located by the documented searches.

## Limitations
This is one exact ternary three-axis space and one scale. The result does not determine analogous modules for arbitrary alphabet sizes, other Hamming dimensions, or other thresholds; it makes no claim of an integral irreducible splitting. The quotient is rationally acyclic, not necessarily contractible. Although relevant titles, accessible main statements and a full earlier primary article were examined, complete text of some potentially relevant recent papers was unavailable; unindexed or stronger prior work remains a literature-overlap risk. The computational argument is exhaustive only because the specified vertex and symmetry sets are finite and all have been traversed, not by extrapolation.

## References
1. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, first submitted June 18, 2026, https://arxiv.org/abs/2606.20784.
2. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, https://arxiv.org/abs/2307.12401; *Homology, Homotopy and Applications* 26 (2024), 349–373.
3. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, *Contributions to Discrete Mathematics* 16 (2021), 74–92, DOI:10.55016/ojs/cdm.v16i3.71284.
4. A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457, first submitted May 9, 2025, https://arxiv.org/abs/2505.06457.
