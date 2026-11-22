# Eleven Frobenius zeta functions of the \(27\)-line boundary on six-point cubic surfaces

## Finding
Let \(k=\mathbb F_q\), with \(\operatorname{char}(k)\ge5\). Let \(Z\subset\mathbb P^2_k\) be a reduced Frobenius-stable six-point geometric subscheme in general position (no three collinear and not all six on a conic). Put \(S=\operatorname{Bl}_{Z}\mathbb P^2\), and assume additionally that the anticanonically embedded smooth cubic surface \(S\) has **no Eckardt points**. Let \(D\subset S\) be the *reduced union of all twenty-seven geometric exceptional curves*. Frobenius permutes the six points of \(Z(\bar k)\) with one of the eleven partitions \(\lambda\vdash6\).

For each \(\lambda\), the orbit data in `27_line_frobenius.csv` give the complete Hasse--Weil zeta function of \(D\), every extension-field point count, and the cardinality of its connected Picard torus. There are **eleven distinct** zeta functions among these eleven Frobenius types. Precisely the two types \((3,3)\) and \((6)\) have \(D(k)=\varnothing\). In type \((2,2,2)\), six \(k\)-rational nodes do not lie on any \(k\)-rational geometric component; in type \((2,4)\), there is exactly one such node.

Define \(v_d,e_d,b_d\) to be the numbers of length-\(d\) Frobenius orbits on, respectively, the twenty-seven lines, the 135 geometric nodes, and the 270 branches over those nodes. Let \(p_d\) and \(n_d\) count node orbits of length \(d\) whose two branches return after \(d\) iterations without exchange or with exchange, respectively. All quantities are nonnegative integers, and the table gives them for every \(\lambda\). Then
\[
\boxed{Z(D,t)=\frac{\prod_{d\ge1}(1-t^d)^{b_d-e_d-v_d}}{\prod_{d\ge1}(1-q^dt^d)^{v_d}}},
\qquad
\boxed{\#D(k)=(q+1)v_1+e_1-b_1}.
\]
For every positive integer \(r\), replace Frobenius by its \(r\)-th power in the second formula to obtain \(\#D(\mathbb F_{q^r})\). The connected Picard scheme \(T=\operatorname{Pic}^0(D)\) is a torus of dimension \(109\), with *exact*, not just isogeny-theoretic, point count
\[
\boxed{\#T(k)=(q-1)\frac{\prod_{d\ge1}(q^d-1)^{p_d}(q^d+1)^{n_d}}{\prod_{d\ge1}(q^d-1)^{v_d}}}.
\]
This is an integer because it is the determinant of Frobenius on an integral character lattice. In particular, the two point-free types have
\[
\begin{aligned}
Z(D_{(3,3)},t)&=\frac{(1-t^3)^{36}}{(1-q^3t^3)^9},\\
Z(D_{(6)},t)&=\frac{(1-t^6)^{19}}{(1-t^3)^2(1-q^3t^3)(1-q^6t^6)^4},\\
\#T_{(6)}(k)&=(q-1)(q^3+1)^2(q^6-1)^{17}.
\end{aligned}
\]
No claim is made that all eleven Frobenius types are realized over every finite field; each assertion applies to any configuration satisfying its stated hypotheses.

### Complete eleven-type table

| Six-point type | \(v_d\) | \(a_d\) | \(\#D(k)\) | Nonsplit rational nodes |
|---|---|---|---:|---:|
| \(1,1,1,1,1,1\) | `1^27` | `1^108` | \(27q-108\) | 0 |
| \(1,1,1,1,2\) | `1^15, 2^6` | `1^30, 2^39` | \(15q-30\) | 0 |
| \(1,1,2,2\) | `1^7, 2^10` | `2^54` | \(7q\) | 2 |
| \(1,1,1,3\) | `1^9, 3^6` | `1^9, 3^33` | \(9q-9\) | 0 |
| \(2,2,2\) | `1^3, 2^12` | `1^−6, 2^57` | \(3q+6\) | 6 |
| \(1,2,3\) | `1^3, 2^3, 3^4, 6^1` | `1^−3, 2^6, 3^11, 6^11` | \(3q+3\) | 0 |
| \(1,1,4\) | `1^5, 2^1, 4^5` | `4^27` | \(5q\) | 1 |
| \(3,3\) | `3^9` | `3^36` | \(0\) | 0 |
| \(2,4\) | `1^1, 2^3, 4^5` | `1^−2, 2^1, 4^27` | \(q+2\) | 1 |
| \(1,5\) | `1^2, 5^5` | `1^−2, 5^22` | \(2q+2\) | 0 |
| \(6\) | `3^1, 6^4` | `3^−2, 6^19` | \(0\) | 0 |

In the table, entries such as `1:3,2:4` denote three orbits of length one and four of length two; zero exponents are omitted. The column headed \(a_d\) records \(a_d=b_d-e_d-v_d\). The full lists of node and branch orbits, plus positive and negative node signs, are in the accompanying CSV.

## Assumptions and scope
All twenty-seven exceptional curves are considered geometrically, including curves not individually defined over \(k\). The no-Eckardt hypothesis is essential: without it, three exceptional curves may meet in one geometric point, invalidating the 135-node normalization. The six blowup points form a finite étale reduced six-point scheme; general position ensures a smooth cubic surface, and the extra hypothesis ensures that each geometric intersection is an ordinary node. Statements about \(\#D(k)\) concern the **geometrically reduced union**, not just the union of the \(k\)-defined lines. Frobenius acts within the subgroup \(S_6\subset W(E_6)\) specified by this six-point blowdown; no classification of the other Weyl-group forms is asserted.

## Proof
**1. Geometric graph from the blowup.** Fix geometric labels \(1,\dots,6\), a plane hyperplane class \(H\), and exceptional classes \(E_i\). The twenty-seven line classes are
\[
E_i,\qquad L_{ij}=H-E_i-E_j\ (1\le i<j\le6),\qquad Q_i=2H-\sum_{j\ne i}E_j.
\]
The intersection form is \(H^2=1\), \(H E_i=0\), and \(E_i E_j=-\delta_{ij}\). Two distinct line classes have intersection number either zero or one. Every line meets ten others, so the simple intersection graph has 27 vertices and 135 edges. The graph is connected (already the incidence of exceptional and pair lines connects it). Because there are no Eckardt points, all 135 pair intersections are distinct ordinary nodes. The normalization is the disjoint union of twenty-seven copies of \(\mathbb P^1\) over \(\bar k\), with exactly 270 geometric preimages of the nodes; the arithmetic genus is \(135-27+1=109\).

**2. Frobenius and the three finite schemes.** The six-point Frobenius permutation acts by relabeling \(E_i,L_{ij},Q_i\), hence on the 27 geometric lines, 135 unordered adjacent line pairs, and 270 *ordered endpoint flags*. A fixed unordered adjacent pair is a rational node whether or not its two component branches are fixed. If Frobenius swaps its two branches, the node is rational but neither preimage in the normalization is rational. These are the nonsplit rational nodes, measured by \(n_1\).

**3. The zeta function.** For each extension \(k_r=\mathbb F_{q^r}\), let \(V_r,N_r,B_r\) denote fixed geometric points on the three finite Frobenius sets (components, nodes, and normalization branches). The normalization is a disjoint union of projective lines over their fields of definition, so its rational-point count is \((q^r+1)V_r\). Identifying exactly the branches over each node gives the exact equality
\[
\#D(k_r)=(q^r+1)V_r+N_r-B_r.
\]
A length-\(d\) orbit contributes \(d\) fixed points to the \(r\)-th Frobenius power exactly when \(d\mid r\). Exponentiation of \(\sum_{r\ge1}\#D(k_r)t^r/r\) gives the claimed zeta product. Because the orbit data are functions solely of the conjugacy class in \(S_6\), the table is universal for each allowed Frobenius type. It distinguishes all eleven zeta functions.

**4. Integral torus point counts.** For a connected nodal curve with rational geometric components, the connected Picard scheme is a torus with integral character lattice the graph cycle lattice \(H_1(\Gamma,\mathbb Z)\), of rank 109. Choose an orientation of each of the 135 geometric graph edges. In the exact equivariant sequence
\[
0\longrightarrow H_1(\Gamma,\mathbb Z)\longrightarrow\mathbb Z^{135}\overset{\partial}{\longrightarrow}\mathbb Z^{27}\longrightarrow\mathbb Z\longrightarrow0,
\]
Frobenius acts on the edge summand as a signed permutation. A positive signed orbit of length \(d\) contributes the characteristic factor \(x^d-1\), while a negative signed orbit contributes \(x^d+1\). A vertex orbit contributes \(x^d-1\). Taking determinants of \(q-\mathrm{Frob}\) in the exact sequence yields the displayed formula for \(\#T(k)=|\det(q-\mathrm{Frob}\mid H_1)|\). This identity is integral and does not assume a decomposition of the torus into Weil restrictions.

**5. Evaluation for all types.** Enumerate the eleven partitions of six and relabel the geometric curves, edges, and branches. This determines \(v_d,e_d,b_d,p_d,n_d\) exactly. For \((3,3)\), every line and every node lies in a Frobenius orbit of length three. For \((6)\), every line has length three or six, and every node has length three or six. Consequently neither divisor has rational points. For \((2,2,2)\), nine nodes are rational, but only six branches are fixed; exactly six rational nodes have exchanged branches and lie on no individually rational component. The other entries follow by the same finite orbit procedure; the complete reproducible enumeration and explicit eleven-row output are supplied.

## Verification
Run `python3 verify_boundary.py` alongside `27_line_frobenius.csv`, using Python 3 and only the standard library. The verifier reconstructs the 27 divisor classes and 135 edges by intersection numbers and *independently* by direct geometric incidence rules; checks connectedness and degrees; enumerates all 720 permutations, grouping them into eleven partitions; checks all orbit counts against a fixed eleven-type reference table; verifies the negative-orbit/branch relation; compares the zeta logarithmic coefficients with direct fixed-point counts for twelve extension degrees and two formal field sizes; and confirms that the torus determinant quotient is integral in those cases. It prints `CUBIC_27_LINE_BOUNDARY_S6_ZETA_OK` on success. This finite verification certifies the stated finite conjugacy-class census, not the general normalization theorem, which is proved above.

## Relationship to prior work
The twenty-seven line classes and tritangent/incidence configurations are classical. Buckley--Košir (2006) treat sixers and double-sixes; Polo-Blanco--Top (2008) explicitly describe all line classes and involutive real forms. In particular, their fixed-line counts for real involutions are **already known**; these are not a claimed contribution. Hirschfeld's 1981 discussion, accessible here through the detailed publisher summary, gives the rational-line/split boundary point count \(27(q-4)\) when there are no Eckardt points; this is precisely the \((1^6)\) row, so that row is also **prior art**. Sottile--Yahl describe splitting types of lines under Frobenius, not the nodal boundary's full signed-branch arithmetic. A published arithmetic computation for the Clebsch cubic concerns a special surface with ten Eckardt points, hence it is not an instance of the nodal theorem. A published eleven-type Igusa boundary formula concerns an entirely different fifteen-line, triple-point curve, with different Galois sets and torus rank. The assessed contribution is the **evaluated complete eleven-type 27-line nodal boundary spectrum**, its two point-free types, the nonsplit rational-node data, and the resulting explicit integral Picard-torus order formula. The latter is not claimed to determine the complete torus isomorphism class. Historical priority remains subject to checking older specialist literature.

## Limitations
The no-Eckardt hypothesis cannot be omitted. The classification does not cover full \(W(E_6)\)-twists, wild or singular cubic surfaces, or the integral isomorphism type of the torus (only its complete rational point order for each type). The results are conditional on the existence of the specified six-point configuration over a given field; no existence cutoff is established. The earlier split-row formula and rational-line splitting information are not new. The complete text of Hirschfeld's chapter was not accessible, so comparison with it is limited to the available detailed summary; this is a residual historical-priority risk. There is no independent audit.

## References
1. A. Buckley and T. Košir, *Determinantal representations of smooth cubic surfaces*, arXiv:math/0606098, first posted 2006-06-05, https://arxiv.org/abs/math/0606098.
2. I. Polo-Blanco and J. Top, *Explicit Real Cubic Surfaces*, Canadian Mathematical Bulletin **51** (2008), 125--133, doi:10.4153/CMB-2008-014-5; accessible transcription at https://www.academia.edu/16013345/Explicit_Real_Cubic_Surfaces.
3. J. W. P. Hirschfeld, *Cubic surfaces whose points all lie on their 27 lines*, in *Finite Geometries and Designs* (1981); publisher summary https://www.cambridge.org/core/books/abs/finite-geometries-and-designs/cubic-surfaces-whose-points-all-lie-on-their-27-lines/6AD025008D32D2A6330A2E4ECC48277F.
4. F. Sottile and T. Yahl, *Splitting types of the 27 lines on cubic surfaces*, https://franksottile.github.io/research/stories/27_Frobenius/index.html.
5. *Arithmetic incidence and zeta function of the Clebsch cubic's line complement*, published research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-arithmetic-incidence-and-zeta-function-of-the-clebsch-cubic-s-li--9b45ce52c311.
6. *Finite-field twists and integral Picard tori of the fifteen-line Igusa boundary*, published research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-finite-field-twists-and-integral-picard-tori-of-the-fifteen-line--71e0231fbb0b.
