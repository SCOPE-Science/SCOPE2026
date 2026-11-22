# Excited zero-temperature traps and field-resonant stability spikes on an Ising icosahedron

## Finding
For the uniform antiferromagnetic Ising model on the 12-vertex icosahedral graph, there are exactly three field intervals with strictly single-spin-stable states *above* the ground energy. Those excited traps occur in three geometrically distinct, completely classified families of sizes **20, 15, and 6**, respectively. The exact numbers of weakly stable states at the two internal transition fields are **407** and **191**, compared with **92, 45, 26** in the adjacent open intervals. At saturation, the weakly stable configurations coincide with the ground states.

Let \(M=\sum_i s_i\) and \(B=\sum_{\{i,j\}\in E}s_i s_j\), where \(s_i\in\{-1,+1\}\). For \(0<h<J\), all strict local minima have \((M,B)=(0,-10)\) with multiplicity 72 or \((0,-6)\) with multiplicity 20. For \(J<h<3J\) they have \((4,-6)\), multiplicity 30, or \((4,-2)\), multiplicity 15. For \(3J<h<5J\) they have \((6,0)\), multiplicity 20, or \((8,10)\), multiplicity 6. Above \(5J\), only the all-plus state is strictly stable.

Each excited family has a canonical geometric form: the 20 zero-field-plateau traps split the vertices into two induced hexagons; the 15 intermediate-field traps have four negative spins spanning exactly two disjoint edges; the six high-field traps place their two negative spins at antipodal vertices. The excited energy excess is \(4J\), \(4J\), and \(10J-2h\), respectively. At the exact fields \(h=J,3J,5J\), weak stability permits zero-energy flips and is not asserted to imply dynamical absorption.

## Assumptions and scope
The graph is the simple icosahedron \(I\), with twelve vertices and thirty edges. The Hamiltonian is
\[
\mathcal H_h(s)=J\sum_{\{i,j\}\in E(I)}s_i s_j-h\sum_i s_i,\qquad J>0,\quad h\ge0.
\]
A configuration is *weakly one-spin stable* if flipping any one spin does not decrease \(\mathcal H_h\); it is *strictly one-spin stable* if every single flip increases energy. For positive-temperature single-spin dynamics these configurations need not be absorbing; the strict classification applies to zero-temperature dynamics permitting no uphill flips, and weakly stable states at critical fields need not be absorbing if neutral flips are permitted. Results are exact for this finite graph, not limits of growing lattices. Negative fields follow by global spin reversal.

A reproducible labeling uses vertex 0 as the north pole, 11 as the south pole, upper pentagon \(1,\ldots,5\), and lower pentagon \(6,\ldots,10\). For indices \(r\) modulo 5, the edges are \(\{0,1+r\}\), \(\{11,6+r\}\), \(\{1+r,1+(r+1)\}\), \(\{6+r,6+(r+1)\}\), \(\{1+r,6+r\}\), and \(\{1+r,6+(r-1)\}\). Every vertex has degree five.

## Proof
For any state, flipping spin \(i\) changes the energy by exactly
\[
\Delta_i\mathcal H_h=2s_i\left(h-J\sum_{j\sim i}s_j\right).
\]
Because each vertex has five neighbors, \(\sum_{j\sim i}s_j\in\{-5,-3,-1,1,3,5\}\). Thus, for nonnegative \(h\), membership in the weak/strict one-spin-stable sets can change only at \(h/J=1,3,5\). It is therefore sufficient to examine representative points of the four open intervals and the three boundary values; \(h=0\) shares the first open-interval classification because all neighbor sums are odd.

For an independently verifiable finite certificate, enumerate all \(2^{12}=4096\) subsets \(D\subseteq V(I)\) of down spins. Writing \(d_D(v)=|N(v)\cap D|\), the exact local inequalities are
\[
\begin{aligned}
 v\notin D &: \quad h/J\ge 5-2d_D(v),\\
 v\in D &: \quad h/J\le 5-2d_D(v).
\end{aligned}
\]
Strict stability means strict inequalities. The magnetization is \(M=12-2|D|\), and the exchange-energy coefficient is \(B=30-2|\partial D|\). Both relations involve integers only. The two included, independently implemented complete enumerators each traverse every subset and verify the following complete stable-state decomposition. Each cell lists \((M,B):\text{multiplicity}\).

| Field \(h/J\) | Weakly stable state decomposition | Total weak | Total strict |
|---|---|---:|---:|
| \(0\le h/J<1\) | \((0,-10):72;\ (0,-6):20\) | 92 | 92 |
| \(1\) | \((0,-10):72;\ (0,-6):50;\ (2,-8):120;\ (2,-4):120;\ (4,-6):30;\ (4,-2):15\) | 407 | 0 |
| \(1<h/J<3\) | \((4,-6):30;\ (4,-2):15\) | 45 | 45 |
| \(3\) | \((4,-6):30;\ (4,-2):75;\ (6,0):20;\ (6,4):60;\ (8,10):6\) | 191 | 0 |
| \(3<h/J<5\) | \((6,0):20;\ (8,10):6\) | 26 | 26 |
| \(5\) | \((6,0):20;\ (8,10):36;\ (10,20):12;\ (12,30):1\) | 69 | 0 |
| \(h/J>5\) | \((12,30):1\) | 1 | 1 |

The same exhaustive integer certificate independently computes the complete energy minimum \(\min_s(B-(h/J)M)\) at each representative field. It confirms ground-state counts \(72,222,30,50,20,69,1\) in successive rows, so in each open interval exactly one additional energy family consists of genuinely excited strict local minima. The up/down induced-degree signatures of these additional families are checked on every member: six down-spin vertices all with induced degree two, four all with induced degree one, or two both with induced degree zero and all other sites adjacent to one of them, respectively. The latter case is the antipodal-pair arrangement. The energy differences follow by subtraction from the ground-sector energy formulas.

This exhaustive finite enumeration is a proof for the twelve-vertex graph: the displayed loops cover all twelve-bit masks (alternatively all binomial subsets) without sampling, truncation, or numerical tolerance. The continuous-field classification follows from the degree-five threshold argument, not from finite sampling of field values.

## Verification
Run `python3 verify_finite.py` and `python3 verify_independent.py` using Python 3 standard library. The first uses a spin-bit representation and evaluates all single-spin energy differences. The second independently uses down-spin subsets, cut-edge counts and exact neighborhood inequalities. Both traverse every state and agree on the seven field classes, weak-state counts, and ground-state counts; the first also verifies all open-interval excited-family degree signatures. The checks were executed successfully from the listed package files. No external datasets or numerical solvers are needed.

## Relationship to prior work
Strečka, Karlová and Madaras (2015) derived the equilibrium ground-state field plateaux and exact degeneracies for Ising Platonic solids, including this icosahedron. Their icosahedral ground multiplicities \(72,30,20\), and boundary counts \(222,50,69\), are **prior results** and are not claimed here. The new claim is the **complete one-spin stability landscape**, particularly all excited strict traps, their induced-subgraph geometry, and exact marginal-field spikes. Wacław and Burda (2008) count metastable states for random Gaussian Ising interactions on generic graphs; their coupling ensemble and thermodynamic/asymptotic questions do not imply the deterministic finite icosahedral table. General zero-temperature freezing literature motivates distinguishing local traps from equilibrium minima; no universal uniqueness follows from these comparisons.

## Limitations
Only one-spin energy changes and a uniform field are classified. No claim is made about multi-spin escape, metastable lifetimes at positive temperature, neutral-move recurrent classes at the three special fields, or larger icosahedral networks. The historical-priority comparison is bounded: a previously unlocated equivalent enumeration would supersede the originality claim. The finite certificate is exhaustive, but not an independent external audit.

## References
- J. Strečka, K. Karlová, and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449 (first public version 2015-02-16), https://arxiv.org/abs/1502.04449 .
- B. Wacław and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, arXiv:0801.1224 (2008-01-08), https://arxiv.org/abs/0801.1224 .
- S. Masui, B. W. Southern, and A. E. Jacobs, *Metastable states of Ising spin glasses and random ferromagnets*, Phys. Rev. B 39, 6925 (1989), https://doi.org/10.1103/PhysRevB.39.6925 .
- V. Spirin, P. L. Krapivsky, and S. Redner, *Freezing in Ising Ferromagnets*, arXiv:cond-mat/0105037 (2001), https://arxiv.org/abs/cond-mat/0105037 .
