# Exact minimum coordinate controllability on the dodecahedral graph

## Finding

For the unweighted dodecahedral graph \(D=GP(10,2)\), the minimum number of independently actuated vertices in the continuous-time Laplacian system \(\dot x=-L(D)x+B_Su\) is exactly five. A five-element set \(S\) is controlling if and only if it contains one vertex from each of five distinct antipodal pairs and the five chosen pairs, viewed as vertices of the Petersen quotient, induce one of \(C_5\), \(P_5\), or \(P_4\sqcup K_1\). There are exactly \(4224\) labelled optimal input sets.

## Assumptions and scope

The graph has vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), indices modulo ten. Its adjacency matrix is \(A\), and \(L=3I-A\). Inputs are independent coordinate inputs: \(B_S\) consists of the columns \(e_s\) for \(s\in S\). Controllability means the ordinary linear-system Kalman rank condition over the reals, or equivalently the PBH condition. The antipodal involution \(\tau\) sends \(u_i\mapsto u_{i+5}\) and \(v_i\mapsto v_{i+5}\). The quotient consists of ten classes \(U_j=\{u_j,u_{j+5}\}\) and \(V_j=\{v_j,v_{j+5}\}\) for \(j\in\mathbb Z/5\mathbb Z\); its edges give the Petersen graph \(GP(5,2)\). A labelled placement counts actual vertices, without quotienting by graph automorphisms.

## Proof

**Lower bound and antipodal restriction.** Five independent vectors in the adjacency eigenspace for eigenvalue one are, for \(j\in\mathbb Z/5\mathbb Z\),
\[
 w^{(j)}(u_i)=\mathbf1_{i\equiv j}-\mathbf1_{i+2\equiv j}-\mathbf1_{i+3\equiv j},\qquad
 w^{(j)}(v_i)=\mathbf1_{i\equiv j},
\]
where each congruence is modulo five. Direct substitution in the three-neighbour adjacency relations yields \(Aw^{(j)}=w^{(j)}\); the restrictions to \(v_0,\ldots,v_4\) form the identity matrix. Hence an input set of fewer than five vertices cannot observe this five-dimensional eigenspace. Moreover, each \(w^{(j)}\) takes the same value on opposite vertices. Thus a controlling set with five coordinates must use five distinct antipodal classes, because two observations from the same class have equal restrictions on this eigenspace.

**Independence of antipodal lift.** With \(I\) the identity, the exact integer matrix identity
\[
 6\tau=A^5-2A^4-7A^3+10A^2+10A-6I
\]
holds (verified by finite integer multiplication in the accompanying certificate). Therefore each eigenspace of the real symmetric matrix \(A\) belongs entirely to one \(\tau\)-parity, with \(\tau\) acting as either \(+I\) or \(-I\). For any eigenvector in a fixed eigenspace, evaluating at an antipodal partner changes its selected coordinate by the same fixed scalar sign. Thus replacing any selected vertex by its antipode preserves all PBH observation ranks. Each eligible quotient five-set represents exactly \(2^5\) real placements of identical control status.

**Eight exhaustive quotient classes.** Number quotient vertices \(0,\ldots,9\), with \(0,\ldots,4\) the outer quotient vertices and \(5,\ldots,9\) the inner ones. The permutations \(\rho(u_i)=u_{i+1}\), \(\rho(v_i)=v_{i+1}\), \(\sigma(u_i)=u_{-i}\), \(\sigma(v_i)=v_{-i}\), together with the displayed 20-entry permutation in `verify.py`, preserve all thirty edges and generate a 120-element automorphism group. Their induced action on the Petersen quotient has order sixty. The standard-library certificate constructs the entire finite group and partitions all \(\binom{10}{5}=252\) five-subsets into precisely the eight orbits in the following table. A representative \(j<5\) is lifted to \(u_j\), and \(5+j\) to \(v_j\).

| Quotient representative | Orbit size | Induced subgraph | Control status |
|---|---:|---|---|
| (0,1,2,3,4) | 6 | \(C_5\) | controlling |
| (0,1,2,3,5) | 60 | \(P_5\) | controlling |
| (0,1,2,3,6) | 60 | degree-three tree | not controlling |
| (0,1,2,3,9) | 30 | \(P_4\sqcup K_1\) | controlling |
| (0,1,2,5,7) | 6 | \(C_5\) | controlling |
| (0,1,2,5,9) | 30 | \(P_4\sqcup K_1\) | controlling |
| (0,1,2,8,9) | 30 | \(P_3\sqcup 2K_1\) | not controlling |
| (0,1,3,7,8) | 30 | \(2K_2\sqcup K_1\) | not controlling |

For each of the five controlling representative rows, the integer controllability matrix \([B,AB,\ldots,A^{19}B]\) has rank twenty modulo the prime eleven. A full-rank minor over \(\mathbb F_{11}\) gives a nonzero integer minor and hence full rank over \(\mathbb Q\) and \(\mathbb R\). For the three noncontrolling rows, the certificate displays a nonzero integer adjacency eigenvector with eigenvalues one, one, and zero, respectively, vanishing at all five selected coordinates; the identities are checked exactly. Automorphism invariance and antipodal-lift invariance transfer these results to all five-element subsets. An independent cross-check constructs all eigenspaces over \(\mathbb F_{11}\) and verifies the PBH condition on every one of the 252 quotient five-subsets. The eigenvalues modulo eleven are \(3,1,0,9,4,7\), with respective eigenspace dimensions \(1,5,4,4,3,3\), adding to twenty.

**Count.** Exactly \(6+60+30+6+30=132\) quotient five-subsets are controlling, hence the number of labelled controlling minimum placements is \(132\cdot2^5=4224\). The lower bound of five is attained, proving optimality.

## Verification

From a directory containing `verify.py`, run `python3 verify.py`. The program requires only Python 3 and its standard library. It verifies the exact lower-bound eigenvectors, the antipodal polynomial identity, the graph automorphism generators and their 120-element closure, the 8-orbit decomposition of 252 quotient five-subsets, full-rank witnesses modulo eleven, three exact obstruction eigenvectors, and a separate 252-subset finite-field PBH classification. It asserts the final count \(4224\). These are exhaustive finite checks for the specific 20-vertex graph, not extrapolations from random or partial samples. The structural arguments above explain why these certificates prove the real-number controllability statement.

## Relationship to prior work

The conventional PBH/Kalman test and the general results of Zhang, Camlibel and Cao on distance-regular and general graph coupling give control-theoretic foundations and generic bounds, but not the eight-orbit, minimum-size dodecahedral placement classification. Monshizadeh, Zhang and Camlibel's zero-forcing framework concerns strong structural controllability over graph-defined matrix families, rather than the exact fixed unweighted Laplacian considered here. A separate previously published calculation of optimal Petersen-graph coordinate inputs gives 162 quotient patterns; this theorem identifies precisely why only 132 survive lifting to the dodecahedral graph and proves the count on the twenty-vertex cover. Known dodecahedral Laplacian spectra alone do not distinguish the three forbidden placement types.

## Limitations

The theorem concerns one fixed unweighted twenty-vertex graph and fully independent coordinate inputs. It does not classify weighted perturbations, general linear combinations of inputs, zero-forcing optima, or larger generalized Petersen graphs. Mathematical reproducibility is provided by the included finite exact certificate; external independent validation and an exhaustive publication-priority guarantee are not claimed. Inaccessible specialist treatments may bear on priority.

## References

- H. Zhang, M. K. Camlibel and M. Cao, *Controllability of Diffusively-Coupled Multi-Agent Systems with General and Distance Regular Coupling Topologies*, 50th IEEE CDC/ECC (2011), https://skoge.folk.ntnu.no/prost/proceedings/cdc-ecc-2011/data/papers/0872.pdf .
- N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, initial arXiv posting 2014-03-19, https://arxiv.org/abs/1403.4868 .
- E. W. Weisstein, *Dodecahedral Graph*, MathWorld, https://mathworld.wolfram.com/DodecahedralGraph.html .
