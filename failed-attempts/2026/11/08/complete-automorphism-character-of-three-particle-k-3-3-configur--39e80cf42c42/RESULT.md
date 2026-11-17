# The complete \(S_3\wr C_2\)-character on three-particle \(K_{3,3}\) configuration homology

## Finding
Let \(G=K_{3,3}\), regarded as a geometric graph with left vertices \(L=\{0,1,2\}\), right vertices \(R=\{3,4,5\}\), and all nine left-right edges. Let \(B_3(G)\) be the unordered configuration space of three pairwise distinct points on the geometric realization of \(G\). Its graph-automorphism group is \(A=\operatorname{Aut}(G)\cong(S_3\times S_3)\rtimes C_2=S_3\wr C_2\), of order \(72\), where the involution interchanges the two parts.

Write \(W\) for the two-dimensional rational standard representation of \(S_3\), \(\varepsilon\) for its sign character, and \(D^-(W)\) for the representation on \(W\otimes W\): the normal subgroup \(S_3\times S_3\) acts factorwise and the part-swap acts as the **negative tensor flip**. Set \(I(\varepsilon,W)=\operatorname{Ind}_{S_3\times S_3}^{A}(\varepsilon\boxtimes W)\), a four-dimensional rational representation. The complete positive-degree rational homology representations are
\[
H_1(B_3(G);\mathbb Q)\cong D^-(W),\qquad
H_2(B_3(G);\mathbb Q)\cong D^-(W)\oplus I(\varepsilon,W),\qquad
H_i(B_3(G);\mathbb Q)=0\quad(i\ge3).
\]
In particular, the second-homology representation contains two distinct four-dimensional irreducibles; both positive-degree globally invariant subspaces vanish. Its integral homology is
\[
H_0\cong\mathbb Z,\qquad H_1\cong\mathbb Z^4\oplus\mathbb Z/2\mathbb Z,\qquad H_2\cong\mathbb Z^8,\qquad H_i=0\ (i\ge3).
\]
The underlying nonequivariant second Betti number \(8\) and first-homology groups are **previously known** and are not claimed as discoveries. The new result is the complete, graph-automorphism-equivariant rational representation classification.

For an explicit character table, write an automorphism as \((p,q,\delta)\) with \(p,q\in S_3\) and \(\delta\in\{0,1\}\). If \(\delta=0\), its action is \(i\mapsto p(i)\) on the left and \(3+j\mapsto3+q(j)\) on the right. If \(\delta=1\), it is \(i\mapsto3+p(i)\) and \(3+j\mapsto q(j)\). The nine conjugacy-class representatives, class sizes, and character values are:

| Representative \((p,q,\delta)\) | Size | \(\chi_1\) | \(\chi_2\) |
|---|---:|---:|---:|
| \((1,1,0)\) | 1 | 4 | 8 |
| \((1,(12),0)\) | 6 | 0 | -2 |
| \((1,(123),0)\) | 4 | -2 | -1 |
| \(((12),(12),0)\) | 9 | 0 | 0 |
| \(((12),(123),0)\) | 12 | 0 | 1 |
| \(((123),(123),0)\) | 4 | 1 | -1 |
| \((1,1,1)\) | 6 | -2 | -2 |
| \((1,(12),1)\) | 18 | 0 | 0 |
| \((1,(123),1)\) | 12 | 1 | 1 |

Here \(1\), \((12)\), and \((123)\) mean the identity, a transposition, and a three-cycle in \(S_3\); their exact numbered representatives are reproduced by `k33_classes.py`.

## Assumptions and scope
The configuration is unordered and consists of exactly three noncolliding points in the one-dimensional CW complex underlying \(K_{3,3}\); there are no sink collisions, order labels, or Euclidean ambient-space motions. Homology uses ordinary, unreduced integral or rational coefficients. Only the natural automorphisms of the *base graph* act; the result is not a representation of the graph braid fundamental group.

## Proof
**Finite chain model.** Use the fully reduced Świątkowski complex of the graph. Let the nine edges be formal commuting weight-one, homological-degree-zero generators. At each of the six degree-three vertices, choose a baseline incident half-edge \(h_0\), and use the two degree-one, weight-one symbols \(h_j-h_0\), \(j=1,2\). The local differential is \(\partial(h_j-h_0)=e(h_j)-e(h_0)\). Multiply by the polynomial edge monomials and apply the signed tensor-product differential with vertices in the order \(0,1,2,3,4,5\). The weight-three chain groups \(C_d\), for \(d=0,1,2,3\), have ranks \((165,540,540,160)\). This complex computes configuration-space homology by the natural comparison theorem for Świątkowski complexes.

**Integral Smith calculation.** The computed differentials compose to zero. Exact integer row/column cancellation at entries \(\pm1\) gives \(164\) unit factors for \(\partial_1\) and \(160\) for \(\partial_3\), each with zero residual. For \(\partial_2\) the same procedure removes \(371\) unit factors, leaving a rank-one residual matrix all of whose nonzero entries equal \(\pm2\). Therefore the nonzero Smith factors are \(1^{164}\), \(1^{371},2\), and \(1^{160}\), respectively. Integer cancellation uses only unimodular operations; the residual rank and entries, together with the chain identities, give exactly the displayed integral homology. In particular, the \(\mathbb Z/2\mathbb Z\) summand occurs in degree one, and \(H_2\) is free.

**Equivariant computation.** All automorphisms of the bipartition are explicitly enumerated and act on the fully reduced complex by permuting edge variables and sending each half-edge difference to the corresponding difference at the image vertex (expanded relative to the chosen baseline). The action commutes *integrally* with every boundary; this is exhaustively checked. For each automorphism, compute the trace on each \(C_d\) and on each rational boundary image \(\operatorname{im}(\partial_d)\). The latter is computed by Gaussian elimination over \(\mathbb F_{10007}\). Because the integer Smith factors are exclusively \(1\) and \(2\), these image dimensions remain unchanged in that characteristic, and the trace agrees modulo \(10007\) with the rational trace. Every trace of a finite-order rational operator on a space of dimension at most \(540\) is an integer of absolute value at most \(540\), so its modular residue has a unique integral lift. The chain decomposition gives
\[
\operatorname{tr}(g\mid H_d)=\operatorname{tr}(g\mid C_d)
-\operatorname{tr}(g\mid\operatorname{im}\partial_d)
-\operatorname{tr}(g\mid\operatorname{im}\partial_{d+1}).
\]
This determines every class character. The nine rational irreducibles of the wreath product are obtained from the three irreducibles \(1,\varepsilon,W\) of \(S_3\): the six signed diagonal tensor-flip representations and the three inductions of unequal factor pairs. Exact character inner products show \(\chi_1=\chi_{D^-(W)}\) and \(\chi_2=\chi_{D^-(W)}+\chi_{I(\varepsilon,W)}\), with all other irreducible multiplicities zero. Averaging the characters over the group gives invariant dimension zero in both degrees.

## Verification
All scripts use Python 3 and the standard library. Execute, in a single directory, `python k33_compute.py`, `python k33_sym.py`, `python k33_classes.py`, `python k33_irreps.py`, and `python k33_abrams.py`. The corresponding `.out` files record successful reference runs. They independently check the integral chain relations and Smith factors, all \(72\) chain actions and image traces, the nine conjugacy classes, character orthogonality and decomposition, and a second cubical chain complex.

The independent cubical complex comes from subdividing every original edge once, yielding \(15\) vertices and \(18\) edges, sufficient for the standard Abrams deformation retraction at three particles. Its chain ranks are \((455,1404,1386,432)\); its mod-\(2\) Betti vector is \((1,5,9,0)\) and its mod-\(3\) vector is \((1,4,8,0)\), exactly as predicted by universal coefficients from the integral groups. Cubical signed Lefschetz numbers agree with the new character on every one of the \(72\) automorphisms.

## Relationship to prior work
Ko and Park's 2011 preprint, Theorem 3.16, already determines the first-homology group of three unordered particles on this nonplanar triconnected graph, including its order-two torsion. An, Drummond-Cole and Knudsen prove the general graph-configuration chain comparison theorem and discuss \(K_{3,3}\) in their first-homology analysis. The 2019 open-access paper *Non-abelian Quantum Statistics on Graphs*, Section 5.5, **explicitly computes** \(\beta_2(B_3(K_{3,3}))=8\) using twelve product cycles and their relations and studies higher particle counts. Thus the rank \(8\) and those product cycles are *not new*. The inspected treatment does not supply the nine-class automorphism character or the two four-dimensional irreducible summands. Lütgehetmann's representation-stability paper concerns a different symmetric-group action on families built by gluing summands, not the full automorphism character of the fixed unordered configuration space here. Searching for equivalent aliases and broader formulas did not reveal coverage of the equivariant result, but absence from these sources does not prove global publication priority.

## Limitations
This computes ordinary integral homology as background and rational graph-automorphism representations for this single finite graph with three unordered particles. It does not determine integral representation lattices, equivariant homotopy type, the fundamental-group representation theory, or all values of the particle count. A further unindexed or inaccessible equivalent representation computation could affect novelty. No independent mathematical audit has been performed.

## References
1. K. H. Ko and H. W. Park, *Characteristics of Graph Braid Groups*, first arXiv posting 2011-01-13, arXiv:1101.2648 (Theorem 3.16 and Section 2).
2. B. H. An, G. C. Drummond-Cole, and B. Knudsen, *Subdivisional Spaces and Graph Braid Groups*, arXiv:1708.02351, comparison theorem and Section 4.2, and Appendix C.
3. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics **371** (2019), 921–973, DOI:10.1007/s00220-019-03583-5, Section 5.5.
4. D. Lütgehetmann, *Representation Stability for Configuration Spaces of Graphs*, arXiv:1701.03490, introduction and Theorem A.
