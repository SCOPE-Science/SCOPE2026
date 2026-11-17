# Three primitive systolic directions in the thirteen-vertex Paley torus

## Finding
Let \(P_{13}\) be the Paley graph with vertex set \(\mathbb Z/13\mathbb Z\) and edge differences \(\{\pm1,\pm3,\pm4\}\). Let \(K\) be its clique complex, endowed with unit edge lengths. This is the flag triangulated torus also denoted \(T_{13,1,3}\).

**The complete simple homology one-systolic shell of \(K\) consists of exactly 39 distinct unoriented four-edge cycles.** They represent exactly three primitive homology directions, with 13 cycles in each. More precisely, every shortest essential simple cycle is a cyclic translate of exactly one of
\[
(0,1,2,3),\qquad (0,3,6,9),\qquad (0,4,8,12),
\]
with the final vertex joined back to the first. All 39 form a *single orbit* under the 78-element affine automorphism group \(\mathbb F_{13}\rtimes(\mathbb F_{13}^{\times})^2\). Of the 78 simple four-edge cycles in the graph, precisely the other 39 are contractible in \(K\).

There is also an exact marked combinatorial length formula. Identify \(H_1(K;\mathbb Z)\) with the lattice
\[
L=\{(u,v)\in\mathbb Z^2:u+3v\equiv0\pmod {13}\},
\]
with basis \(a=(3,-1)\) and \(b=(4,3)\). For **every** integer pair \((m,n)\), the minimum number of graph edges in a closed walk in homology class \(ma+nb\) is
\[
\ell(m,n)=\max\{|3m+4n|,\,|-m+3n|,\,|4m+n|\}.
\]
The shortest nonzero classes are exactly \(\pm a\), \(\pm b\), and \(\pm(b-a)\), all of length four. The marked formula is for closed walks; a shortest representative of a nonprimitive class need not be simple.

## Assumptions and scope
The graph is undirected and each edge has length one. A simple cycle is considered without a chosen starting vertex or orientation. An essential cycle means one representing a nonzero element of \(H_1(K;\mathbb Z)\); on a torus this is equivalent to noncontractibility. The length of a class is minimized over closed edge walks, not merely embedded simple cycles. Three *unoriented primitive directions* means the six signed primitive classes pair into three inverse pairs; the statement does not identify them as the same homology class.

## Proof
**1. The precise torus and its cover.** The two triangle families are
\[
\{i,i+1,i+4\},\qquad \{i,i+3,i+4\},\quad i\in\mathbb Z/13\mathbb Z.
\]
The graph has 13 vertices, 39 edges and exactly these 26 triangular cliques; it has no four-clique. To see the clique assertion, choose the edge differences among \(\{\pm1,\pm3,\pm4\}\). Any three steps summing to zero modulo 13 have integer sum zero because their absolute sum is at most 12. The only resulting nondegenerate triple relation is \(1+3=4\), up to signs and ordering. The six neighbours of a vertex induce a six-cycle, so the 26 triangles constitute a closed orientable connected surface with Euler characteristic \(13-39+26=0\).

An explicit cover is the plane triangulation with vertices \(\mathbb Z^2\), edges in the six directions
\[
\pm e_1,\qquad\pm e_2,\qquad\pm(e_1+e_2),
\]
and triangles \(\{z,z+e_1,z+e_1+e_2\}\), \(\{z,z+e_2,z+e_1+e_2\}\). The map \((u,v)\mapsto u+3v\pmod{13}\) takes its quotient by deck lattice \(L\) exactly to \(K\). The plane triangulation is contractible, so \(\pi_1(K)\cong H_1(K;\mathbb Z)\cong L\). The displayed vectors \(a,b\) have determinant \(13\), the index of \(L\), hence form its integral basis.

**2. Every marked length.** For the six allowed lattice steps, the graph word metric from the origin is exactly
\[
N(u,v)=\max\{|u|,|v|,|u-v|\}.
\]
Each step changes each displayed linear form in absolute value by at most one, proving the lower bound. If \(uv\ge0\), use \(\min(|u|,|v|)\) common-sign diagonal steps and remaining axial steps to achieve \(\max(|u|,|v|)\); if \(uv<0\), use the two opposing axial directions to achieve \(|u|+|v|=|u-v|\). Thus the lower bound is sharp. Any closed edge walk lifts to a path between two vertices displaced by a member of \(L\), and conversely any lattice path to such a displacement projects to a closed edge walk. Substituting \((u,v)=ma+nb=(3m+4n,-m+3n)\) gives the formula for \(\ell(m,n)\) for every class, with no finite-experiment inference.

**3. Complete shortest shell.** If \(N(u,v)\le3\) and \((u,v)\in L\), then \(|u+3v|\le4N(u,v)\le12<13\), so \(u+3v=0\). Hence \(N(u,v)\ge|u-v|=4|v|\), forcing \(u=v=0\). At \(N(u,v)=4\), the only nonzero lattice vectors are
\[
\pm(3,-1),\qquad\pm(4,3),\qquad\pm(1,4).
\]
For completeness, either \(u+3v=0\), whose shortest nonzero solutions are \(\pm(3,-1)\), or \(u+3v=\pm13\), whose norm-four solutions are \(\pm(4,3)\) and \(\pm(1,4)\); the bound \(|u+3v|\le16\) excludes all other multiples of 13. These three representatives are \(a,b,b-a\), respectively; each is primitive because its coordinates in the basis \(a,b\) are coprime.

For displacement \(a=(3,-1)\), every four-step shortest lifted path consists of three \(+e_1\) steps and one \(-e_2\) step: it must increase \(u-v\) by one at every step. The projected unoriented cycles are precisely the 13 translates of \((0,1,2,3)\). For \(b=(4,3)\), the four steps are three \(e_1+e_2\) and one \(+e_1\), giving the 13 translates of \((0,4,8,12)\). For \(b-a=(1,4)\), they are three \(+e_2\) and one \(e_1+e_2\), giving the 13 translates of \((0,3,6,9)\). Every such cycle has four distinct vertices. Reversing orientations introduces no new unoriented cycles, and the three families have distinct inverse-pair homology classes. This proves the complete 39-cycle essential shell.

**4. Total census and symmetry.** The graph has parameters \((13,6,2,3)\): adjacent vertices have exactly two common neighbours and nonadjacent vertices exactly three. Thus its number of simple unoriented four-cycles is
\[
\frac12\left(39\binom22+39\binom32\right)=78,
\]
because each four-cycle has two unordered pairs of opposite vertices. The other 39 cycles have zero deck displacement and are therefore contractible.

Every affine map \(i\mapsto qi+t\), with \(q\in\{1,3,4,9,10,12\}\), preserves adjacency and hence acts on \(K\). Translations act transitively within each 13-cycle family. Multiplication by 3 takes edge difference \(+1\) to \(+3\) and then to \(-4\), cyclically permuting the three unoriented families. Thus all 39 essential cycles are in one orbit under the order-78 group. The action on deck vectors for multiplication by 3 is \((u,v)\mapsto(-v,u-v)\), which cycles \(a\), \(b-a\), and \(-b\), confirming the homology directions.

## Verification
The standalone `verify.py` reconstructs the graph from quadratic-residue differences and independently checks the 26 clique triangles, absence of larger cliques, every six-cycle vertex link, and the Euler characteristic. Breadth-first search verifies the hexagonal norm on every vector in radius eight, while exact enumeration lists all deck vectors of norm at most four. A separate complete enumeration of all ordered four-tuples of distinct vertices, canonically deduplicated under rotation and reversal, finds 78 graph four-cycles; lifted displacements classify 39 essential cycles, with exactly 13 in each primitive class. It checks the entire 78-map affine action and verifies one orbit on the essential cycles. The recorded successful six-line output is in `verification_output.txt`. These finite checks support—but are not a substitute for—the exact all-class norm proof above.

## Relationship to prior work
Delecroix, Ebbens, Lazarus and Yakovlev established general algorithms relating marked length spectra of combinatorial tori to polyhedral norms. Their generic method makes norm calculations possible but does not list the explicit 13-vertex Paley torus formula or classify its shortest carriers.

Jones and Mačaj's Example 6 identifies the same Paley graph as the \(\{3,6\}_{3,1}\) torus with 13 vertices, 39 edges, 26 triangular faces and an affine 13-by-6 symmetry group. Their classification does not address graph-edge systoles.

A published classification of the cyclic torus family establishes the distinct **\(n\ge17\)** regime, in which \(T_{n,1,3}\) has just one primitive four-systolic direction and exactly \(n\) shortest carriers. Its triangular-cover method is expressly acknowledged here. That published claim does not cover \(n=13\); the three-direction, 39-carrier phenomenon is different and is not obtained by substituting the index into the stated \(n\ge17\) theorem. A separate flag criterion identifies \(T_{13,1,3}\) as the first flag member of the cyclic family, but does not determine its systoles. The present result supplies the exact first-shell geometry and marked formula for that distinguished case.

## Limitations
This concerns the unit-edge graph metric on a specified 13-vertex torus triangulation, not the Riemannian flat-torus metric or all triangulations of the torus. The marked formula counts minimum closed walks in all homology classes; it does not claim that all those minimizers are simple. The 39-carrier census applies specifically to the *first nonzero* simple integral homology length. The norm-lattice method is classical; originality is asserted only for the particular exceptional three-direction shell, its complete carrier/orbit census and its explicit associated formula. An equivalent census under older regular-map or lattice-systole terminology remains a residual literature risk.

## References
1. V. Delecroix, M. Ebbens, F. Lazarus, and I. Yakovlev, *Algorithms for Length Spectra of Combinatorial Tori*, arXiv:2303.08036v1, 2023-03-14; SoCG 2023, DOI:10.4230/LIPIcs.SoCG.2023.26.
2. G. A. Jones and M. Mačaj, *Regular dessins with primitive automorphism groups*, arXiv:2303.11808v1, 2023-03-21, Example 6.
3. B. Datta and A. K. Upadhyay, *Degree-regular triangulations of torus and Klein bottle*, arXiv:math/0403433v1, 2004-03-25.
4. *A one-direction systolic shell in the cyclic torus family* \(T_{n,1,3}\), public research result dated 2026-10-11, identifier `2026/10/11/SCOPE-a-one-direction-systolic-shell-in-the-cyclic-torus-family-t-n-1--ceddf77f71ea`.
5. *An exact flag criterion for the cyclic weakly regular torus family*, public research result dated 2026-10-11, identifier `2026/10/11/SCOPE-an-exact-flag-criterion-for-the-cyclic-weakly-regular-torus-fami--a170495e50a8`.
