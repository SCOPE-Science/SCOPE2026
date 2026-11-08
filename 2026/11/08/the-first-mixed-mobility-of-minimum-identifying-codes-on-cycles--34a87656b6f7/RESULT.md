# The first mixed mobility of minimum identifying codes on cycles

## Finding

Let \(C_n\) have vertex set \(\mathbb Z/n\mathbb Z\), with the two usual cyclic edges, and let a radius-one *identifying code* be a set \(D\subseteq V(C_n)\) for which all signatures \(D\cap N[v]\), indexed by all vertices \(v\), are nonempty and pairwise distinct. Write \(\mathcal S_n\) for the graph of minimum-cardinality identifying codes of \(C_n\), where a move replaces one code vertex by one adjacent non-code vertex, without changing cardinality or losing the identifying property. Let \(\mathcal J_n\) allow the replaced vertex to jump to any non-code vertex instead.

**Theorem.** The eleven-cycle is the smallest identifiable cycle whose minimum identifying codes include both frozen and movable configurations under one-token sliding. Its minimum identifying-code cardinality is \(7\), it has exactly \(33\) minimum codes, and

\[
\mathcal S_{11}\cong 11K_1\sqcup C_{22}.
\]

In contrast, \(\mathcal J_{11}\) is a connected, \(4\)-regular graph on \(33\) vertices with \(66\) edges; it has radius \(4\) and diameter \(5\). The nontrivial component of \(\mathcal S_{11}\) has diameter \(11\).

This is a first-coexistence statement: on every identifiable cycle of order less than \(11\), the minimum-code token-slide graph has either no isolated vertex or no nonisolated vertex. In particular, \(C_7\) has a mobile cycle of length \(14\), while \(C_9\) has \(18\) frozen optimal codes.

## Assumptions and scope

All graphs are finite, simple, undirected, and vertex-labeled. The closed neighborhood \(N[v]\) includes \(v\). The code is required to identify **all** vertices, including code vertices (not merely vertices outside the code). Minimum means globally smallest cardinality, not inclusion-minimal. Legal token slides preserve the minimum cardinality and the identifying-code condition at every intermediate step. An isolated vertex of the token-slide graph is termed *frozen*.

For \(C_n\) only \(n\ge3\) is considered. The three-cycle is not identifiable because all closed neighborhoods coincide. Results for larger cycles, beyond the first-coexistence cutoff, are not asserted.

## Proof

**1. A local criterion for the eleven-cycle.** Write \(Z=V(C_{11})\setminus D\) for the omitted vertices. Direct comparison of signatures of adjacent vertices shows that a necessary condition is

\[
\forall i\in\mathbb Z/11\mathbb Z:\quad \{i,i+3\}\not\subseteq Z. \tag{1}
\]

Indeed, the closed neighborhoods of \(i+1\) and \(i+2\) differ exactly at \(i\) and \(i+3\). Condition (1) also separates every pair at cycle distance two: the symmetric difference of the corresponding neighborhoods contains a pair of vertices at cyclic separation three. Pairs at graph distance at least three have disjoint closed neighborhoods, and are distinguished whenever both signatures are nonempty. The latter is precisely the condition

\[
\forall i\in\mathbb Z/11\mathbb Z:\quad \{i,i+1,i+2\}\not\subseteq Z. \tag{2}
\]

Thus (1) and (2) are together necessary and sufficient for \(D\) to be identifying. This also follows from the general cycle characterization of Chen, Lu, and Miao (2009), but the stated argument supplies an independent proof in the present case.

**2. Minimum cardinality.** Condition (1) means \(Z\) is an independent set in the step-three cycle on \(\mathbb Z/11\mathbb Z\). Because \(3\) is invertible modulo \(11\), the step-three cycle is an ordinary \(11\)-cycle. Hence \(|Z|\le5\), giving \(|D|\ge6\). Every independent five-set in the step-three cycle is a cyclic translate (in the original labels) of \(\{0,1,2,6,7\}\): there are exactly \(11\) such sets, one for each translation. Each contains three consecutive omitted vertices, violating (2). Thus \(|D|\ge7\). The valid examples below attain \(7\).

**3. Complete orbit classification.** When \(|D|=7\), \(Z\) is an independent four-set in the step-three cycle. A cycle of length \(11\) has exactly

\[
\frac{11}{11-4}\binom{11-4}{4}=55
\]

independent four-sets. Because \(11\) is prime, each such four-set has an orbit of size \(11\) under vertex rotation. Thus there are exactly five orbits. Representatives, written as eleven-bit omitted-vertex indicators with the bit for vertex \(0\) first, are exhaustively listed here:

| Omitted-vertex indicator | Condition (2) | Orbit name |
| --- | --- | --- |
| `00001000111` | fails | discarded |
| `00001010101` | holds | A |
| `00001100011` | holds | B |
| `00001110001` | fails | discarded |
| `00010100011` | holds | C |

Each listed representative satisfies (1); direct inspection of the five strings confirms the displayed status under (2). The five orbits are distinct, so together they exhaust all \(55\) candidates. The three valid orbits supply exactly \(3\cdot11=33\) labeled minimum codes.

Let \(A_i,B_i,C_i\) denote the minimum codes obtained by rotating the corresponding omitted-vertex string by \(i\) places, all indices modulo \(11\). Since every permitted slide exchanges a single occupied vertex with a cyclic neighbor, checking the two possible destinations of each of seven selected vertices for the three representatives gives the complete sliding-neighbor rules:

\[
N_{\mathcal S}(A_i)=\varnothing,\qquad
N_{\mathcal S}(B_i)=\{C_i,C_{i+6}\},\qquad
N_{\mathcal S}(C_i)=\{B_i,B_{i+5}\}. \tag{3}
\]

Rotational symmetry makes this check exhaustive. Formula (3) immediately gives \(11\) isolated A-states and a single connected \(2\)-regular component on the \(22\) B- and C-states: the two-step walk \(B_i\to C_{i+6}\to B_{i+6}\) visits every B-state because \(6\) is coprime to \(11\). Hence that component is \(C_{22}\).

**4. Unrestricted one-token jumps.** With the same orbit notation, direct inspection of the three representatives yields

\[
\begin{aligned}
N_{\mathcal J}(A_i)&=\{A_{i+2},A_{i+9},C_{i+1},C_{i+5}\},\\
N_{\mathcal J}(B_i)&=\{B_{i+5},B_{i+6},C_i,C_{i+6}\},\\
N_{\mathcal J}(C_i)&=\{A_{i+6},A_{i+10},B_i,B_{i+5}\}.
\end{aligned} \tag{4}
\]

Thus the jumping graph is \(4\)-regular with \(33\cdot4/2=66\) edges. The A-orbit is connected by jumps of index \(\pm2\), the B-orbit by jumps of index \(\pm5\), and the C-orbit attaches to both. So the entire jumping graph is connected. Exhaustive breadth-first searches from every one of its \(33\) states give radius \(4\) and diameter \(5\). The one nontrivial sliding component is \(C_{22}\), hence has diameter \(11\).

**5. Minimality of the coexistence cutoff.** For each \(n\in\{4,5,6,7,8,9,10\}\), exhaustive enumeration of the at most \(2^{10}\) subsets, direct signature tests and legal token slides give:

| \(n\) | Minimum code size | Number of minimum codes | Slide-graph structure |
| --- | ---: | ---: | --- |
| 4 | 3 | 4 | \(C_4\) |
| 5 | 3 | 5 | \(5K_1\) |
| 6 | 3 | 2 | \(2K_1\) |
| 7 | 5 | 14 | \(C_{14}\) |
| 8 | 4 | 2 | \(2K_1\) |
| 9 | 6 | 18 | \(18K_1\) |
| 10 | 5 | 2 | \(2K_1\) |

Every graph in this table is entirely movable or entirely frozen. Together with the absence of identifying codes for \(C_3\), this establishes the asserted first coexistence at \(n=11\).

## Verification

Two standalone programs are supplied. `verify_exhaustive.py` enumerates all subsets of every cycle of order \(4\) through \(11\), tests all closed-neighborhood signatures from the definition, constructs both exchange graphs, and computes connected components and distances by breadth-first search. It independently verifies the complete cutoff table and the jumping/sliding invariants at \(n=11\).

`verify_orbits.py` instead enumerates independent four- and five-sets of the step-three graph, tests the no-three-omissions criterion, obtains the five rotation orbits, and checks the representative transition rules (3) and (4). It does not call the direct signature enumerator. The expected program outputs are embedded as `exhaustive_output.json` and `orbit_output.json`. Running each program with standard Python reproduces these files exactly (including their trailing newlines). The mathematical proof of the \(C_{22}\) component and jumping connectivity is separate from the breadth-first-search computation.

## Relationship to prior work

The concept of identifying codes and optimization on paths and cycles predates this result. Bertrand, Charon, Hudry and Lobstein (2004) study smallest identifying-code cardinalities in paths and cycles. Chen, Lu and Miao's preprint, publicly available on 19 August 2009, proves the general cycle criterion and radius-dependent minimum-size formulas; its Section 2 contains the same local pair-separation condition used here. Those **scalar minima and the local criterion are not claimed new**.

The present claim instead concerns the *configuration space of all minimum codes*, particularly the first occurrence of simultaneously frozen and mobile optima under one-token sliding, its exact \(11K_1\sqcup C_{22}\) decomposition, and the different connectivity behavior under token jumping. The inspected section of Chen–Lu–Miao does not state these transition graphs. Related published work on domination- and independent-set reconfiguration studies different permissible states or moves. This comparison does not establish absolute historical priority; independently circulated enumerations or unavailable full papers could contain overlapping results.

## Limitations

The first-coexistence assertion concerns one-token sliding among **minimum radius-one identifying codes of ordinary cycles**. It does not extend the \(C_{11}\) decomposition to other cycle orders, larger code sizes, higher identification radii, or other reconfiguration conventions. The description is an exact labeled finite classification; no extrapolation from experiments is claimed. The reported diameter and radius of the jumping graph are computer-checked finite invariants, not consequences of a separate closed-form metric theorem. Historical-priority risk and the lack of independent scholarly review remain.

## References

1. N. Bertrand, I. Charon, O. Hudry, A. Lobstein, *Identifying and locating-dominating codes on chains and cycles*, European Journal of Combinatorics 25 (2004), 969–987. DOI: `10.1016/j.ejc.2003.12.013`.
2. C. Chen, C. Lu, Z. Miao, *Identifying codes and locating-dominating sets on paths and cycles*, arXiv:`0908.2750v1`, first posted 19 August 2009; Discrete Applied Mathematics 159 (2011), 1540–1547. DOI: `10.1016/j.dam.2011.06.008`.
3. V. Junnila, T. Laihonen, *Optimal identifying codes in cycles and paths*, Graphs and Combinatorics 28 (2012), 469–481. DOI: `10.1007/s00373-011-1058-6`.
4. C. M. Mynhardt, S. Nasserasr, *Reconfiguration of colourings and dominating sets in graphs: a survey*, arXiv:`2003.05956` (2020). Distinct reconfiguration contexts are treated as background, not as a source of the present enumeration.
