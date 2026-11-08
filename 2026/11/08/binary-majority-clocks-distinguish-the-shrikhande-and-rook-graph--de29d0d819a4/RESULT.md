# Binary majority clocks distinguish the Shrikhande and rook graphs

## Finding

Let \(R\) denote the \(4\times4\) rook graph and \(S\) the Shrikhande graph. They are the two nonisomorphic strongly regular graphs with parameters \((16,6,2,2)\), hence have identical adjacency spectra. Apply **synchronous binary majority dynamics with tie retention** to every labelled binary configuration. Define \(\tau(x)\) as the first time at which the trajectory becomes periodic, and \(p(x)\) as its least eventual period.

The complete counts of initial configurations by first entrance time and least eventual period are:

| Graph | \(p\) | \(\tau=0\) | \(\tau=1\) | \(\tau=2\) | \(\tau=3\) | \(\tau=4\) | \(\tau=5\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rook \(R\) | 1 | 302 | 10,104 | 29,984 | 18,720 | 0 | 0 |
| Rook \(R\) | 2 | 2,394 | 4,032 | 0 | 0 | 0 | 0 |
| Shrikhande \(S\) | 1 | 142 | 7,576 | 26,240 | 18,496 | 9,024 | 960 |
| Shrikhande \(S\) | 2 | 1,370 | 1,728 | 0 | 0 | 0 | 0 |

Each graph row-pair sums to \(2^{16}=65,536\). In particular, \(R\) has **302 fixed configurations and 1,197 primitive two-cycle orbits**, whereas \(S\) has **142 fixed configurations and 685 primitive two-cycle orbits**. Every initial condition enters its eventual periodic orbit by time three for \(R\), but the sharp maximum for \(S\) is five. In both graphs, any initial condition eventually reaching a primitive two-cycle does so by time one.

The contrast can already be witnessed without computation: \(R\) has exactly eight fixed configurations with four occupied vertices, and \(S\) has none. Thus the **complete temporal majority census, including its fixed-point count, oscillatory orbit count and sharp transient depth, is not determined by the strongly regular parameters or adjacency spectrum**.

## Assumptions and scope

Use the common labelled vertex set \(V=(\mathbb Z/4\mathbb Z)^2\). Distinct vertices \((a,b)\) and \((c,d)\) are adjacent in \(R\) if \(a=c\) or \(b=d\). In \(S\), vertices are adjacent if their difference modulo four is one of \(\pm(1,0)\), \(\pm(0,1)\), or \(\pm(1,1)\). Reversing the second coordinate gives the equally standard convention with \(\pm(1,-1)\). Neither graph has self-loops.

For \(x\in\{0,1\}^{V}\), write \(F_G(x)(v)\) for the simultaneous update. Since all degrees equal six, \(F_G(x)(v)=1\) when at least four neighbors of \(v\) have state one, \(F_G(x)(v)=0\) when at most two do, and \(F_G(x)(v)=x(v)\) when exactly three do. Define
\[
\tau_G(x)=\min\{t\geq0:\ F_G^{t+1}(x)=F_G^t(x)\ \text{or}\ F_G^{t+2}(x)=F_G^t(x)\},
\]
with \(p_G(x)=1\) in the first case and \(p_G(x)=2\) otherwise. The finite exhaustive argument below establishes that this minimum exists for all states here, without assuming a numerical stabilization cutoff in advance. States and cycles are counted **with labelled vertices**, with opposite points of the same primitive two-cycle counted as one orbit only in the orbit totals.

## Proof

**Graph and spectral identity.** Both explicit neighbor constructions give degree six. Every two distinct vertices in either graph have exactly two common neighbors: for \(R\), this follows from the row/column intersection construction; for \(S\), it follows by checking the fifteen nonzero differences of the six Cayley generators (reproduced in `code/check_structure.py`). Hence each adjacency matrix \(A\) satisfies \(A^2=4I+2J\). On the all-ones vector its eigenvalue is six; on the orthogonal complement the eigenvalues are \(\pm2\). Trace zero and total dimension sixteen give multiplicities six and nine, respectively. Both spectra are therefore \(6^1,2^6,(-2)^9\).

**An analytic fixed-point separation.** Suppose precisely four vertices have state one. A one-vertex must have at least three one-neighbors to remain one, so those four vertices must form a \(K_4\). In \(R\), exactly the four rows and four columns are \(K_4\)'s, and each outside vertex has exactly one neighbor in the selected row or column. Each is therefore a fixed configuration. In \(S\), the neighbors of any vertex induce a six-cycle, which contains no triangle; a \(K_4\) is impossible. Thus the respective four-one fixed populations are eight and zero. The full computation also finds these exact values independently of this argument.

**Exhaustive finite certificate.** Give \((a,b)\) the bit index \(4a+b\), and enumerate every integer \(x\) from \(0\) through \(65,535\). `code/census_bitmask.py` explicitly constructs all six neighbor masks, checks regularity, symmetry and every pairwise common-neighbor count, and computes the update at every bit. It then traces the complete functional graph of \(65,536\) states, recognizing a cycle only when a state repeats within the current path, and propagates the exact first-entry time and period backwards. The exhaustive traversal visits every state, detects only cycles of lengths one and two, and returns the table in the finding. In particular, each row-pair sums to the entire state space; no states are left unclassified. The number of primitive two-cycle **orbits** is the number of two-periodic **configurations at entrance time zero**, divided by two.

`code/verify_direct.py` is a second computation: it creates each graph directly as coordinate-neighbor lists, evaluates each local majority as a sum of signed opinions rather than a bit count, and for every input directly tests successive iterates for the **first** equality after one or two updates. It does not use functional-graph path tracing. Its independently computed entire \((\tau,p)\) table, fixed-point weight distribution and primitive two-periodic weight distribution agree exactly with the first computation. Its explicit maximum-depth witnesses are the bit masks \(359\) on \(R\) and \(1901\) on \(S\), with entrance times three and five respectively. `code/check_structure.py` separately checks \(A^2=4I+2J\), the eight versus zero four-clique counts, and the eight versus zero weight-four fixed configurations.

The two independently structured exhaustive classifications, the analytic graph properties and the explicit witnesses together establish all asserted finite counts and sharp maxima. No finite experiment is extrapolated to a family of larger graphs.

## Verification

Run the three standalone Python 3 standard-library programs from the root of the extracted package:

```
python3 code/census_bitmask.py
python3 code/verify_direct.py
python3 code/check_structure.py
```

Their exact outputs are provided as `outputs/census_bitmask.json`, `outputs/verify_direct.json`, and `outputs/check_structure.txt`. The full labelled transition tables from the bit-mask calculation have SHA-256 digests `0a1ee0d258a2e3c59745c35817bb6c2756ace942cc59ea6306fdc7dbc69e21bf` for \(R\) and `d7cf391ec7f6adab7f3a2480eed69eca627686c17f9095801c2a49b7823f8c81` for \(S\), obtained by serializing every successor as a two-byte little-endian integer in input order. The two independent programs were run directly, and their common census fields were compared exactly; the structural check also passed.

## Relationship to prior work

Goles and Olivos established eventual period at most two for symmetric finite-graph threshold dynamics; that general period restriction is not new. Benjamini, Chan, O'Donnell, Tamuz and Tan study majority convergence and disagreement, including infinite unimodular and random graphs, but not the exact temporal census of these two labelled sixteen-vertex graphs. Fountoulakis, Kang and Makai prove rapid unanimity in dense random graphs, which does not determine the exceptional finite-graph counts or sharp worst-case entrance times here. Benjamini, Zakharov and Zhukovskii study sharp transients on finite trees, a disjoint graph class. Cameron's description of the two strongly regular graph mates supplies the graph-theoretic comparison but no binary-majority dynamics census.

Linear-algebraic parity automata, homology invariants, and three-state excitable automata on the same graphs evolve under different transition maps. Their periodic counts do not imply the nonlinear, binary majority update counts here. The novelty claim is restricted to the explicit majority-dynamics table, the resulting separation of its three temporal invariants, and the fixed-weight structural witness, not to the existence or spectral description of the two graphs.

## Limitations

The theorem concerns these two specific graphs with one precisely specified tie rule; it does not assert a general formula over all strongly regular graphs or other vote thresholds. The full numerical census is proved by finite exhaustive algorithms rather than a closed-form hand enumeration. The analytic four-clique argument supports one particular census component independently. A published or unindexed earlier equivalent census cannot be ruled out by finite literature searches. Computational replication was done with two independent algorithms, not by an independent external evaluator.

## References

1. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486v1 (first submitted 2014-05-11). https://arxiv.org/abs/1405.2486
3. N. Fountoulakis, M. Kang and T. Makai, “Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs,” *Random Structures & Algorithms* 57 (2020), 1134–1156. https://doi.org/10.1002/rsa.20970
4. I. Benjamini, G. Zakharov and M. Zhukovskii, “Majority Dynamics on Finite Trees,” *Random Structures & Algorithms* 69 (2026), e70092. https://doi.org/10.1002/rsa.70092
5. P. J. Cameron, “The Shrikhande graph,” 2025-04-07, https://cameroncounts.wordpress.com/2025/04/07/the-shrikhande-graph-2/
