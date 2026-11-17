# The icosahedral majority landscape: isolated caps and seven oscillation symmetries

## Finding

Let \(I\) be the ordinary icosahedral graph (12 vertices, 30 edges, each of degree 5). For synchronous binary neighbor-majority \(F:\{0,1\}^{12}\to\{0,1\}^{12}\), a vertex adopts opinion 1 exactly when at least three of its five neighbors have opinion 1. States are labelled by vertices; spatial graph automorphisms are not identified unless explicitly stated.

The **complete finite dynamical census** is as follows.

1. Exactly 14 states are fixed: the two unanimous states and the 12 distinct closed-neighborhood indicator states \(\mathbf1_{N[v]}\), one for each vertex. Each nonunanimous fixed state has an attraction basin consisting of itself alone (its only predecessor is itself). The two unanimous fixed states each have exactly 1,586 initial configurations in their attraction basins.
2. Exactly 156 unordered primitive temporal two-cycles exist, containing 312 recurrent states. Their cycle basin sizes are distributed as follows: 16 cycles have basin size 2, 60 have size 4, 60 have size 6, and 20 have size 14. The 156 cycles split into exactly 7 orbits under the full 120-element graph automorphism group, with orbit sizes \(6,10,20,30,30,30,30\). Temporal phases within a cycle are identified; opinion complementation is not an additional symmetry quotient.
3. All 4,096 initial configurations satisfy \(F^7(x)=F^5(x)\). The first periodic entry time has exact histogram \((326,986,984,1080,480,240)\) at times \(0,1,2,3,4,5\), respectively. Thus five updates is a sharp global first-entry bound.
4. The numbers of cycles whose two phase states have population sizes \((5,5)\), \((6,6)\), and \((7,7)\) are respectively \(30,96,30\). For initial configurations with \(k=0,1,\ldots,12\) opinions equal to 1, the exact numbers eventually entering a fixed point versus a primitive two-cycle are

\[
(1,0),(12,0),(66,0),(220,0),(495,0),(732,60),(132,792),
(732,60),(495,0),(220,0),(66,0),(12,0),(1,0).
\]

In particular, among uniformly sampled initial configurations, the exact probabilities of eventual unanimity, eventual arrival at a nonunanimous fixed point, and eventual two-periodic oscillation are respectively \(793/1024\), \(3/1024\), and \(57/256\).

## Assumptions and scope

The simple undirected graph \(I\) is specified without ambiguity by two poles and two pentagonal rings. Use vertices \(0,1,\dots,11\), with top pole \(0\), first ring \(A_i=1+i\), second ring \(B_i=6+i\) for \(i\in\mathbb Z/5\mathbb Z\), and bottom pole \(11\). Edges are the five spokes \(0A_i\), five spokes \(11B_i\), two ring cycles \(A_iA_{i+1}\), \(B_iB_{i+1}\), and ten staggered rungs \(A_iB_i\), \(A_iB_{i-1}\). This is isomorphic to the standard icosahedral graph, independently checked by a graph-isomorphism routine. All index operations in the ring construction are modulo five.

For any initial configuration \(x\), its **first periodic entry time** is the least \(t\ge0\) such that \(F^t(x)\) belongs to an orbit with least temporal period one or two. A cycle's **basin** contains every labelled initial configuration eventually entering that cycle, including its periodic states. A primitive temporal two-cycle is an unordered pair \(\{x,F(x)\}\) with \(F^2(x)=x\ne F(x)\). Geometric cycle classes are defined by the action of \(\operatorname{Aut}(I)\) on these unordered pairs.

## Proof

This is a **finite exhaustive proof**, with the entire domain explicitly bounded and independently reproduced, not an extrapolation or a general infinite-graph claim. The critical exhaustive certificate is supplied as executable source plus an 82-row orbit-quotient table.

1. For \(x\in\{0,1\}^{12}\), encode \(x\) as an integer from 0 to 4095. Let \(M_v=\sum_{u\in N(v)}2^u\), with bitwise AND denoted by \(\mathbin{\&}\), and let \(w(z)\) be the population count of an integer bit mask. Then the exact update is

\[
F(x)=\sum_{v=0}^{11}2^v\mathbf 1_{\{w(M_v\mathbin{\&}x)\ge3\}}.
\]

No ties are possible because every degree is five. The code `check_finite.py` independently constructs the 30-edge pole-and-ring graph, verifies the degrees, calculates \(F(x)\) for all 4096 integers, and explicitly checks \(F^7(x)=F^5(x)\) for all 4096 inputs. Because \(F^7=F^5\), all images at time five are periodic with period dividing two.

2. The exact sets \(\{x:F(x)=x\}\) and \(\{x:F^2(x)=x\}\), found using full enumeration, have sizes 14 and 326. Every primitive pair is counted once by normalizing it as the sorted pair of its two integer states, hence the number of primitive two-cycles is \((326-14)/2=156\). The fixed set equals \(\{\mathbf0,\mathbf1\}\cup\{\mathbf1_{N[v]}:v\in V(I)\}\), with 12 distinct caps. These equalities and all 4096 membership decisions are checked by executable assertions; the 82-row quotient table `state_orbits.csv` gives a compact independent organization of all state orbits under geometric symmetry.

The cap indicator is visibly fixed: the near pole has five agreeing neighbors, each near-ring vertex has three agreeing neighbors, each far-ring vertex has three agreeing neighbors, and the opposite pole has five agreeing neighbors.

**Symbolic non-nucleation proof for the cap equilibria.** Fix a target cap consisting of a pole and its adjacent pentagonal ring. Use the pole-and-ring graph from the scope section. For an arbitrary putative predecessor \(x\), let \(t,d\in\{0,1\}\) be its two pole values, \(a_i,b_i\in\{0,1\}\) its ring values, and \(A=\sum_i a_i\), \(B=\sum_i b_i\). The five target-one ring vertices must each see at least three input ones, while the five target-zero opposite-ring vertices must each see at most two. Summing their neighborhood counts gives

\[
5t+2A+2B\ge15,\qquad 5d+2A+2B\le10.
\]

Their difference forces \(t=1,d=0\) and equality then forces \(A+B=5\). Thus each of the ten individual inequalities is an equality, giving, for each \(i\) modulo five,

\[
a_{i-1}+a_{i+1}+b_{i-1}+b_i=2,
\qquad a_i+a_{i+1}+b_{i-1}+b_{i+1}=2.
\]

Subtracting yields \(a_{i-1}+b_i=a_i+b_{i+1}\), so all five quantities \(a_i+b_{i+1}\) are equal. Their sum is \(A+B=5\), hence \(a_i+b_{i+1}=1\) for every \(i\). Substituting \(b_i=1-a_{i-1}\) into the first displayed equality gives \(a_{i+1}=a_{i-2}\). Since shifting by three generates the cyclic group of order five, all \(a_i\) are the same, and all \(b_i\) are their binary complements. The target-one top pole requires \(A\ge3\), so \(a_i=1\) and \(b_i=0\) for all \(i\). Thus the **only** predecessor of this cap is the cap itself. Vertex transitivity proves the same for all twelve caps. No noncap state can reach any cap at a later time, since a first entrance would have a noncap immediate predecessor, which is impossible. This proves the non-nucleation component without using the finite-state count.

3. For every initial state, iterate until the first periodic state (within five steps, proved in step 1). Normalize its attractor as either a one-state tuple or a sorted pair, and count the initial states with each attractor. Exhausting every possible input proves the exact basin-size distribution and entrance histogram in the finding. The 12 cap fixed points have basin size one. For a fixed point, uniqueness of the basin state implies there is no other immediate predecessor; each unanimous basin has size 1586. Grouping inputs by population count gives the thirteen displayed pairs.

4. Separately, `check_symmetry.py` uses a hard-coded 30-edge list, a vertex-by-vertex majority implementation, and a standard graph-isomorphism test against a built-in icosahedral graph. It obtains all 120 graph automorphisms, checks that the majority update commutes with every automorphism on all 4096 states, and partitions the unordered primitive two-cycles into seven disjoint automorphism orbits. Their sizes sum to \(6+10+20+4\cdot30=156\). This independently verifies the cycle count and the symmetry quotient and reproduces the basin and first-entry distributions. The 82 geometric state-orbit representatives, sizes, updates and dynamics are included in `state_orbits.csv`; their orbit sizes sum to 4096.

5. Sharpness of the five-step bound follows from the explicitly verified positive last histogram entry: 240 states first become periodic at time five. The three possible cycle population pairs are independently counted from all 156 normalized pairs. The uniform initial-state probabilities follow by dividing the fixed and period-two basin totals by 4096: unanimous mass \(2\cdot1586\), cap mass \(12\), and oscillatory mass \(16\cdot2+60\cdot4+60\cdot6+20\cdot14=912\).

## Verification

Run `python3 check_finite.py` using Python 3.8 or later (standard library only). Run `python3 check_symmetry.py` with Python 3 and NetworkX 2.8 or later, in the same directory. The second program writes `state_orbits.csv`, whose delivered contents and UTF-8 bytes are separately hashed in the package. The programs return zero only after their explicit assertions succeed. Captured successful outputs are in `check_finite.out` and `check_symmetry.out`; these logs corroborate but do not replace the complete executable proof and state-orbit table. The checked domain is exactly all 4096 binary states of this one graph; no statistical sampling is involved.

## Relationship to prior work

Agur, Fraenkel and Klein (1988) give an exact cyclic-binary-string census for self-inclusive radius-one majority; their full accessible eight-page article does not treat the icosahedral degree-five rule. Goles and Olivos (1980) prove eventual periods at most two for symmetric threshold systems, but the accessible abstract states no exact icosahedral orbit or attraction-basin enumeration. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1, first submitted 11 May 2014) study majority dynamics on infinite transitive and random graphs; the accessible 19-page primary preprint explains the finite period-two theorem but does not establish this twelve-vertex census. A separately published dodecahedral majority census concerns the dual **nonisomorphic** 20-vertex graph and is not transported by geometric duality: majority update depends on vertex neighborhoods. An existing icosahedral excitation enumeration uses three-state Greenberg–Hastings updates, a different state set and transition rule.

No indexed exact icosahedral binary-majority basin-and-orbit census was found in the searches described in `AUDIT.json`. Nonappearance in search results is not a proof of historical priority.

## Limitations

The claim concerns one natural finite graph, not a graph family or arbitrary regular graphs. Completeness is mathematical only within the explicit 4096-state domain. Computations are independently executable but no independent expert audit has been performed. The full 1980 Goles–Olivos primary article was unavailable, leaving a qualified historical-priority risk. The symmetry quotient identifies graph automorphisms and temporal phases, but not arbitrary opinion complementation as a separate quotient. The basin sizes depend on the synchronous, neighbor-only majority rule, not asynchronous updates or self-inclusive majority.

## References

- Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics **70** (1988), 295–302, DOI: 10.1016/0012-365X(88)90005-2, lawful full text: https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf.
- E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first public 2014-05-11, https://arxiv.org/abs/1405.2486.
- *Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-dodecahedral-majority-dynamics-an-exact-recurrent-basin-and-symm--095dfb0decea.
- *Icosahedral excitation: exact three-cycle, geometric-orbit, and six-step entrance census*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-icosahedral-excitation-exact-three-cycle-geometric-orbit-and-six--6295ce972482.
