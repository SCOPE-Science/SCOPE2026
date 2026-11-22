# A unique seven-seed orbit separates threshold-four contagion on two cospectral graphs

## Finding

Let \(S\) be the Shrikhande graph and let \(R=K_4\square K_4\) be the four-by-four rook graph. Both are six-regular, nonisomorphic strongly regular graphs with parameters \((16,6,2,2)\). For synchronous **four-neighbor bootstrap percolation**, a contagious set is *inclusion-minimal* if deleting any one of its initial seeds makes it noncontagious. The complete inclusion-minimal cardinality-and-completion-time censuses are:

| Initial size | Completion rounds | Shrikhande | Rook |
| ---: | ---: | ---: | ---: |
| 6 | 3 | 96 | 288 |
| 6 | 4 | 336 | 0 |
| 6 | 5 | 1,152 | 576 |
| 6 | 6 | 576 | 0 |
| 7 | 3 | 64 | 0 |

Both graphs have minimum contagious-set cardinality \(6\). The Shrikhande graph has exactly \(2,224\) inclusion-minimal contagious sets, including \(64\) of size seven; the rook graph has exactly \(864\), all of size six. In particular, the largest size of an inclusion-minimal contagious set is seven for \(S\) but six for \(R\).

The \(64\) exceptional seven-seed sets in \(S\) form a single orbit under explicit affine graph symmetries. They are **exactly** the seven-vertex subsets whose induced degrees, in nondecreasing order, are \((2,2,2,3,3,3,3)\). They all finish in three synchronous rounds. No seven-vertex subset of \(R\) has this degree signature.

## Assumptions and scope

All graphs are finite, simple and undirected. The vertex set is \(\mathbb Z_4^2\), labeled \(v=4a+b\) for \(0\le a,b\le3\). In \(S\), two distinct vertices are adjacent when their difference lies in \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\); in \(R\), they are adjacent when their first or second coordinates agree. Only the fixed threshold \(r=4\) and these two graphs are asserted here.

For any initial seed set \(A_0\), define \(A_{t+1}=A_t\cup\{v:|N(v)\cap A_t|\ge4\}\). The set percolates when \(A_t=V\) for some \(t\). The completion time is the least such \(t\), with \(t=0\) for \(A_0=V\). Inclusion-minimal means no proper subset percolates, not merely minimum cardinality.

## Proof

**Peeling lemma.** In any six-regular graph, put \(W_t=V\setminus A_t\). For \(v\in W_t\), the number of active neighbors is \(6-\deg_{G[W_t]}(v)\). Consequently
\[
W_{t+1}=W_t\setminus\{v\in W_t:\deg_{G[W_t]}(v)\le2\}.
\]
Thus percolation occurs if and only if the initial inactive induced subgraph has empty three-core, equivalently is two-degenerate. The number of parallel peeling rounds is exactly the infection completion time. No stochastic or infinite-size assumption enters this equivalence.

**Finite certification of the census.** The file `check_direct.cpp` constructs both adjacency matrices from the preceding coordinates and directly applies the simultaneous infection rule to each of the \(2^{16}=65,536\) initial subsets. It stores whether each subset percolates and its exact completion time. Monotonicity of infection implies that a successful set is inclusion-minimal precisely when removing each of its selected vertices makes it unsuccessful: a smaller successful subset would force some one-vertex deletion to succeed as well. The program therefore counts *all* inclusion-minimal sets, not a sample or an isomorphism-reduced subset. Its executable assertions reproduce every cell of the table and the complete successful-set cardinality distributions.

Independently, `check_core.py` constructs the adjacencies via modular-coordinate relations and enumerates the same \(65,536\) masks by **parallel residual three-core peeling**, not forward infection. It independently checks the complete distributions and every table entry. Both checkers verify degree six and pairwise common-neighbor counts two; they do not depend on a graph library or an outside graph file. Their agreement on all tabulated values, together with the transparent exhaustive loops and the peeling lemma, supplies a finite exhaustive proof.

**Geometry of the exceptional seven-sets.** The two checkers independently enumerate the \(\binom{16}{7}=11,440\) seven-sets and find exactly \(64\) with induced degree multiset \((2,2,2,3,3,3,3)\). Each of these and no other seven-set is inclusion-minimal contagious in \(S\). In \(R\) no seven-set has that signature, and no seven-set is inclusion-minimal contagious.

For a concrete witness, the seven-set with labels \(\{1,2,4,5,7,8,12\}\) activates exactly \(\{0,6,13\}\) in round one, \(\{3,9,11\}\) in round two, and \(\{10,14,15\}\) in round three. Every one-seed deletion leaves a nonempty three-core; this is checked by both full-domain algorithms.

For an algebraic orbit certificate take the seven-set with labels \(\{1,2,4,5,7,8,12\}\). There are exactly twelve matrices \(M\in\operatorname{Mat}_{2\times2}(\mathbb Z_4)\) that map the six-element connection-difference set \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\) onto itself. Each affine map \(x\mapsto Mx+t\), where \(t\in\mathbb Z_4^2\), preserves adjacency. Enumerating these \(12\cdot16=192\) explicit maps gives an orbit of exactly \(64\) distinct seven-sets, equal to the \(64\) degree-signature sets. The Python certificate checks matrix preservation and equality of these sets directly; the argument does not assume that every graph automorphism is affine.

## Verification

From the directory containing the two supplied source files, execute:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_direct.cpp -o direct
./direct
python3 check_core.py
```

Each program terminates with a `PASS` message only after checking the complete count tables. The C++ program prints successful-set counts at every cardinality, including the absence of all percolating sets below size six. The Python program additionally verifies the affine symmetry orbit. No files, databases, third-party packages, or environment-specific paths are required.

## Relationship to prior work

The general contagious-set model and generation count are present in Coja-Oghlan, Feige, Krivelevich and Reichman (2013/2014), and the equivalence with removing a three-core in degree-six graphs is discussed in Guggiola and Semerjian (2014). The latter concerns asymptotic random regular graphs, not either of the fixed sixteen-vertex graphs. Bidgoli, Mohammadian and Tayfeh-Rezaie (2019), Theorem 2.1, already prove that the rook graph \(K_4\square K_4\) has minimum threshold-four seed size six. Accordingly the minimum size six for the rook graph is **not** claimed as new. The classification here adds the exact minimal-set counts, times, the seven-seed discrepancy, and the single-orbit induced-degree characterization. Comparable indexed results involving site percolation, majority dynamics or induced-forest complexes of the same graph pair have different state spaces or a different peeling threshold; their conclusions do not imply the present census.

## Limitations

This is an exact finite-graph theorem, not a statement about all strongly regular graphs, all thresholds, random regular graphs, or arbitrary Hamming graphs. The core equivalence is standard, not a novelty claim. The numerical part of the proof is exhaustive computation and depends on the correctness of the supplied finite implementations; no human-independent formal certification has been performed. The literature comparison found no subsuming published table, but historical priority remains subject to unindexed computations and literature not inspected in full. No physical epidemic model or probabilistic performance claim is asserted.

## References

- A. Coja-Oghlan, U. Feige, M. Krivelevich and D. Reichman, *Contagious Sets in Expanders*, arXiv:1306.2465, first posted 11 June 2013, https://arxiv.org/html/1306.2465v2 .
- A. Guggiola and G. Semerjian, *Minimal Contagious Sets in Random Regular Graphs*, arXiv:1407.7361, first posted 28 July 2014, https://arxiv.org/abs/1407.7361 .
- M. R. Bidgoli, A. Mohammadian and B. Tayfeh-Rezaie, *Percolating Sets in Bootstrap Percolation on the Hamming Graphs*, arXiv:1905.01942, first posted 6 May 2019, https://ar5iv.labs.arxiv.org/html/1905.01942 .
