# Perfect Roman domination on the Heawood graph: a 133-configuration Fano-plane census

## Finding
Let \(H\) be the fourteen-vertex point–line incidence (Heawood) graph of the Fano plane. A *perfect Roman dominating function* (PRDF) is \(f:V(H)\to\{0,1,2\}\) such that every vertex labeled zero has **exactly one** neighbor labeled two. Its weight is \(w(f)=\sum_{v\in V(H)}f(v)\). Write \(P_H(z)=\sum_{f\ \mathrm{PRDF}}z^{w(f)}\), with distinct vertex labelings counted separately.

Then the complete weight polynomial is
\[
\begin{aligned}
P_H(z)={}&133z^{10}+1064z^{11}+4578z^{12}+12530z^{13}
 +23913z^{14}+34664z^{15}\\
&+40803z^{16}+40138z^{17}+33607z^{18}+24360z^{19}
 +15813z^{20}+9312z^{21}\\
&+4977z^{22}+2422z^{23}+1043z^{24}+364z^{25}
 +91z^{26}+14z^{27}+z^{28}.
\end{aligned}
\]
In particular, \(\gamma_R^p(H)=10\), and there are exactly \(133\) minimum-weight functions.

Every minimum function is determined by its set \(T=f^{-1}(2)\), which comprises some points \(P\) and lines \(L\) with **no incidences between any selected point and selected line**. Its sizes \((|P|,|L|)\) are precisely \((1,1)\), \((2,1)\), \((1,2)\), or \((2,2)\), with respectively \(28\), \(42\), \(42\), and \(21\) possibilities. Given one of these sets \(T\), all unselected vertices with exactly one neighbor in \(T\) have label zero, and all other unselected vertices have label one. Thus the four families classify every optimum without any unlisted exceptions.

## Assumptions and scope
We use the labelled Fano plane on point indices \(0,\ldots,6\), whose lines are
\[
\ell_j=\{j,j+1,j+3\}\pmod7,\qquad 0\le j<7.
\]
The graph has vertices \(p_i\) and \(\ell_j\), with \(p_i\ell_j\) an edge exactly when \(i\in\ell_j\). It is cubic, bipartite, and has fourteen vertices. The graph is fixed and all labels are regarded as distinct; no quotient by automorphisms is taken. No condition is imposed on the neighbors of vertices labeled one or two.

## Proof
**1. An exact defender-set identity.** For any \(T\subseteq V(H)\), put
\[
U(T)=\{v\in V(H)\setminus T:|N(v)\cap T|=1\}.
\]
A PRDF with \(f^{-1}(2)=T\) must label every vertex outside \(T\cup U(T)\) by one, while each vertex of \(U(T)\) can independently be labeled zero or one. Consequently
\[
P_H(z)=\sum_{T\subseteq V(H)}z^{14+|T|-|U(T)|}(1+z)^{|U(T)|}.\tag{1}
\]
The least weight for fixed \(T\) is \(14+|T|-|U(T)|\), uniquely achieved by giving every vertex of \(U(T)\) label zero. Identity (1) counts each PRDF once because its two-labelled set is unique.

**2. Fano incidence geometry.** Let \(P\) and \(L\) be the selected points and selected lines, with sizes \(p\) and \(\ell\). For a point set \(P\), let \(a(P)\) count lines incident with exactly one point of \(P\); define \(a(L)\) dually. For set sizes zero through five, Fano-plane incidence gives
\[
\begin{array}{c|cccccc}
|P|&0&1&2&3&4&5\\\hline
a(P)&0&3&4&3\text{ or }6&0\text{ or }3&1
\end{array}
\]
The larger value at size three corresponds to a collinear triple; the zero value at size four corresponds to the four-point complement of a line. These facts follow by counting incidences and using that any two distinct points determine one line, and dually. Let \(d_1(P,L)\) be the number of selected vertices having exactly one selected neighbor in the induced bipartite graph on \(P\cup L\). Then
\[
|U(P\cup L)|=a(P)+a(L)-d_1(P,L).\tag{2}
\]
Indeed the first two terms count all uniquely incident lines and points; the final term removes those vertices already selected as defenders.

For \(p+\ell\le5\), (2) and the Fano-plane incidences give the following exhaustive small-size table. Interchanging points and lines gives the reversed pairs.

| \((\min(p,\ell),\max(p,\ell))\) | Maximum \(|U(T)|\) | Number of supports attaining that maximum |
|---|---:|---:|
| \((0,0)\) | 0 | 1 |
| \((0,1)\) | 3 | 7 |
| \((0,2)\) | 4 | 21 |
| \((1,1)\) | 6 | 28 |
| \((0,3)\) | 6 | 7 |
| \((1,2)\) | 7 | 42 |
| \((0,4)\) | 3 | 28 |
| \((1,3)\) | 7 | 42 |
| \((2,2)\) | 8 | 21 |
| \((0,5)\) | 1 | 21 |
| \((1,4)\) | 4 | 168 |
| \((2,3)\) | 8 | 21 |

Here are the critical equality arguments. At sizes \((1,1)\) and \((1,2)\), the maximal values \(6\) and \(7\) in (2) require the absence of incidences. At size \((2,2)\), the maximum \(8\) likewise requires \(d_1(P,L)=0\). Any nonempty incidence pattern between two points and two lines has a selected vertex of incidence degree one: a four-cycle would require two distinct lines through the same pair of points, which is impossible. Hence equality here also means zero incidences. For size \((1,3)\), a nonconcurrent triple of lines has \(a(L)=3\), while three concurrent lines cover all seven points, so their positive incidences force \(d_1\ge2\); thus \(|U|\le7\). For size \((2,3)\), in the concurrent case each of the two chosen points outside the common center has degree one among the three selected lines, while selecting the center produces at least two degree-one selected lines. Hence \(d_1\ge2\) and \(|U|\le8\); in the nonconcurrent case \(a(L)=3\) and \(|U|\le7\). The remaining table cases follow from the displayed values of \(a\), the same point-line duality, and counting the selected incidences. All entries, including their exact attaining counts, are re-derived by the exhaustive 16,384-support certificate described below.

**3. Optimality and complete minimum classification.** For \(|T|\ge6\), every PRDF has weight at least \(2|T|\ge12\). For \(|T|\le5\), insert the preceding table into \(14+|T|-|U(T)|\). The least possible weight is exactly ten; equality occurs only at \((p,\ell)=(1,1),(1,2),(2,1),(2,2)\), each with no selected incidences. Conversely these supports attain the respective eligible-zero counts \(6,7,7,8\), giving weight ten. The number of nonincident choices is respectively \(7\cdot4=28\), \(7\binom42=42\), \(7\binom42=42\), and \(\binom72=21\) (two selected lines omit exactly two points). This proves the \(133\) minimum count and all four geometric classes.

**4. Every polynomial coefficient.** Apply (1) to the \(2^{14}=16{,}384\) subsets \(T\), using the explicit seven Fano lines. For each support, compute \(|U(T)|\) from the fourteen adjacency lists and expand its contribution by the binomial coefficients \(\binom{|U(T)|}{j}\), for \(0\le j\le|U(T)|\). This is a finite exact sum, not an extrapolation. The provided standalone Python implementation evaluates (1) with integer arithmetic, yielding the polynomial shown. Independently, a C++ program loops over all \(3^{14}=4{,}782{,}969\) ternary vertex labelings, applies the original exactly-one-neighbor definition directly, and gets the same coefficients. Both codes exhaust their stated finite domains and assert the complete expected coefficient list.

## Verification
Run `python3 verify_support.py` and compile/run `verify_direct.cpp` with any conforming C++17 compiler, for example `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct`. The expected completion markers are `PRD_SUPPORT_EXACT_OK` and `PRD_DIRECT_EXHAUSTIVE_OK`. The total number of PRDFs is \(P_H(1)=249{,}827\). The first program checks the Fano pair-uniqueness axiom and the four optimal-support families; the second checks every labeling directly and the same optimum-type counts. Both use exact integers and have no third-party runtime dependencies.

## Relationship to prior work
Henning and Klostermeyer (2018) proved the universal cubic-graph upper bound \(\gamma_R^p(G)\le3|V(G)|/4\). At fourteen vertices its integral consequence is at most ten, which our lower bound attains. Their theorem supplies neither the matching lower bound for the Heawood graph nor the complete enumerator or the four Fano-geometric optimal families. Fernau and Mann (2023) studied algorithms for enumerating perfect Roman functions and their computational complexity; the inspected sections do not classify the Heawood graph. Ordinary Roman domination, total perfect Roman domination, and unique-response Roman domination impose different constraints and do not imply this census. The exact matching claims were not found in the checked accessible literature or mathematical research index; publication priority remains subject to independent checking.

## Limitations
This is an exact result for the fixed fourteen-vertex Heawood graph, not a universal formula for arbitrary finite projective planes, cubic graphs, or Levi graphs. The polynomial is for **all** perfect Roman dominating functions, not only pointwise-minimal functions. The independent audit has not been performed. Unindexed historical computations may already contain part of the finite census.

## References
1. M. A. Henning and W. F. Klostermeyer, *Perfect Roman Domination in Regular Graphs*, Applicable Analysis and Discrete Mathematics 12 (2018), 143–152. https://doi.org/10.2298/AADM1801143H
2. H. Fernau and K. Mann, *Perfect Roman Domination and Unique Response Roman Domination*, arXiv:2309.07018, first posted 2023-09-13. https://arxiv.org/abs/2309.07018
