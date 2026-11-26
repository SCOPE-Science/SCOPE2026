# Dihedral first homology of two-particle wheel configurations

## Finding
For every integer \(n\ge4\), let \(W_n=C_n*K_1\) be the wheel with \(n\) rim vertices and one hub, and put
\[
X_n=\operatorname{UConf}_2(|W_n|).
\]
The dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) acts on \(X_n\) by rotating or reflecting the rim while fixing the hub. Let \(\varepsilon\) be its one-dimensional reflection-sign representation: \(\varepsilon(r)=1\), \(\varepsilon(s)=-1\). Let \(E_n\) be the set of the \(n\) unoriented rim edges with its natural dihedral permutation action. Then there is a (not asserted canonical) isomorphism of rational \(D_n\)-representations
\[
\boxed{H_1(X_n;\mathbb Q)\cong\varepsilon\otimes\bigl(\mathbb Q[E_n]\oplus\mathbb Q\bigr).}
\]
Moreover \(H_0(X_n;\mathbb Q)=\mathbb Q\) and \(H_i(X_n;\mathbb Q)=0\) for all \(i\ge2\).

Equivalently, writing \(\chi_n\) for the character on first homology,
\[
\chi_n(r^j)=\begin{cases}n+1,&j\equiv0\pmod n,\\1,&j\not\equiv0\pmod n,\end{cases}
\qquad
\chi_n(g)=-1-\#\{e\in E_n:g(e)=e\}
\quad(g\text{ a reflection}).
\]
For odd \(n\), every reflection has trace \(-2\). For even \(n\), the trace is \(-1\) for an axis through opposite rim vertices and \(-3\) for an axis through opposite rim edges. Consequently,
\[
\dim_{\mathbb Q}H_1(X_n/\langle r\rangle;\mathbb Q)=2,
\qquad
\widetilde H_i(X_n/D_n;\mathbb Q)=0\quad\text{for every }i\ge0.
\]
Thus rotation quotienting preserves two independent rational first-homology classes, while adding the reflections eliminates both.

## Assumptions and scope
The graph is the simple wheel with rim vertices \(0,\ldots,n-1\), hub \(h\), rim edges \(\{i,i+1\bmod n\}\), and spokes \(\{h,i\}\). Configurations consist of *two unordered, distinct points* of the geometric realization, with collisions disallowed everywhere, including vertices. The result concerns rational homology and representation isomorphism; no integral equivariant lattice isomorphism or homotopy type of the symmetry quotients is claimed. The primary subject is graph-configuration-space topology.

The unsubdivided wheel satisfies the two-particle stable discretization conditions: the shortest path between distinct essential vertices has at least one edge, and each noncontractible closed path has at least three edges. Hence the unordered Abrams cubical complex \(A_n\) is a deformation retract of \(X_n\). Its cells are unordered pairs of graph cells whose closures are disjoint. The dihedral action is cellular on \(A_n\).

## Proof
**1. Cells and connectedness.** A zero-cell is an unordered pair of distinct graph vertices, a one-cell is an edge together with a nonincident vertex, and a two-cell is an unordered pair of vertex-disjoint edges. There are no higher-dimensional cells. The cell numbers are
\[
c_0=\binom{n+1}{2},\qquad c_1=2n(n-1),\qquad
c_2=\frac{n(n-3)}2+n(n-2)=\frac{n(3n-7)}2.
\]
In the last count, two rim edges are disjoint in \(n(n-3)/2\) ways and a rim edge is disjoint from \(n-2\) spokes. Two spokes always meet at the hub. The one-skeleton is connected: the two-token graph of any connected graph is connected (move indistinguishable tokens through vacancies along a spanning tree). It follows that \(H_0(A_n;\mathbb Q)=\mathbb Q\).

**2. Injectivity of the top cellular boundary.** Orient the graph edges arbitrarily, and orient a two-cell indexed by disjoint edges \(e,f\) as their ordered product. For any integral two-chain \(z\) satisfying \(\partial_2z=0\), fix an edge \(e\) and group coefficients of all squares containing \(e\). Their contributions to one-cells of the form \((e,v)\) show that the associated one-chain on \(W_n\setminus V(e)\) has zero boundary (the ordering of the square only introduces a common sign for that fiber). If \(e\) is a spoke, the graph obtained by deleting its endpoints is a path on the remaining rim vertices; its one-cycle group is zero. Hence every coefficient of a two-cell containing a spoke vanishes. Next fix a rim edge \(e\). With all spoke-containing coefficients already zero, its fiber is supported on the path of rim edges disjoint from \(e\), again with zero one-cycle group. All remaining square coefficients therefore vanish. Thus \(\partial_2\) is injective over \(\mathbb Z\), and \(H_2(A_n;\mathbb Z)=0\). As the complex is two-dimensional, all higher homology also vanishes.

Consequently \(\chi(A_n)=c_0-c_1+c_2=-n\), and the first rational Betti number is \(1+n\).

**3. Exact signed Lefschetz traces.** Choose once and for all an orientation of each graph edge, and orient each square by a fixed ordering of its two edges. For an automorphism \(g\), the trace on cellular chains in degree zero counts unordered vertex pairs fixed as sets. The degree-one trace sums the orientation signs of fixed edge-and-vertex cells. The degree-two trace sums the products of the two edge-orientation signs and an additional minus sign if the automorphism exchanges the two edge factors. These signs are essential: fixed unoriented cells alone do not give the Lefschetz number.

Direct classification of fixed cells gives the following table. The columns \(T_q\) are the *signed* traces of \(g\) on cellular \(q\)-chains.

| Symmetry class | \(T_0\) | \(T_1\) | \(T_2\) |
| --- | ---: | ---: | ---: |
| identity | \(n(n+1)/2\) | \(2n(n-1)\) | \(n(3n-7)/2\) |
| nonidentity rotation, not a half-turn | \(0\) | \(0\) | \(0\) |
| half-turn (even \(n\)) | \(n/2\) | \(0\) | \(-n/2\) |
| reflection, odd \(n\) | \((n+1)/2\) | \(-2\) | \(-(n-1)/2\) |
| reflection through vertices, even \(n\) | \((n+4)/2\) | \(2\) | \(2-n/2\) |
| reflection through edges, even \(n\) | \(n/2\) | \(-2\) | \(2-n/2\) |

For clarity, a nonidentity rotation can fix an unordered rim-vertex pair only when it is a half-turn. In that case it also exchanges precisely \(n/2\) disjoint pairs of rim edges, each contributing \(-1\) in degree two; no spoke pair is disjoint. For an odd reflection there is one fixed spoke and one oppositely placed fixed rim edge; they form a square contributing \(-1\), and the other disjoint swapped rim-edge pairs contribute \(-(n-3)/2\). For even \(n\), a vertex-axis reflection fixes two spokes, whereas an edge-axis reflection fixes two rim edges. Counting the remaining swapped rim-edge pairs yields the last two rows. This exhausts the dihedral conjugacy types.

Since the only nonzero rational homology groups are in degrees zero and one, the Hopf trace identity reads
\[
T_0-T_1+T_2=1-\chi_n(g).
\]
Substitution gives \(\chi_n(1)=n+1\), \(\chi_n(r^j)=1\) for nontrivial rotations, and reflection traces \(-2\), \(-1\), \(-3\) in the respective cases.

**4. Identification of the module and quotient homology.** Rotations act on \(E_n\) without a fixed edge except at the identity. A reflection fixes one rim edge if \(n\) is odd; for even \(n\), it fixes no rim edge when the axis passes through opposite vertices and two rim edges when it passes through opposite edges. Therefore the character just computed equals that of \(\varepsilon\otimes(\mathbb Q[E_n]\oplus\mathbb Q)\) on every group element. Semisimplicity of rational representations of a finite group and character equality imply the claimed isomorphism.

The \(\langle r\rangle\)-invariants consist of a constant rim-edge vector and the additional one-dimensional summand, hence have dimension two. For the full dihedral group the extra line has no invariants. The rim-edge permutation module twisted by \(\varepsilon\) has none either, because the stabilizer of any rim edge contains a reflection acting by \(-1\). Finally, for an action of a finite group on a finite triangulable space, rational homology of the quotient identifies with the invariant rational homology: after equivariant barycentric subdivision the quotient chain complex is the invariant chain complex over \(\mathbb Q\). This proves the two quotient conclusions.

## Verification
The standalone program `verification/check_wheel.py` constructs all cells and both signed boundary maps for every \(4\le n\le14\), checks the integer chain identity \(\partial_1\partial_2=0\), proves the second boundary has full column rank modulo two in each tested case, checks zero-skeleton connectivity by the rank of \(\partial_1\), and computes signed cellular traces for **every** element of each \(D_n\). All agree with the theorem; its final message is `VERIFY_OK_WHEEL_TWO_POINT_DIHEDRAL`. These are independent finite consistency checks, not a substitute for the universal combinatorial proof.

Reproduction requires Python 3.10 or newer and no third-party packages. Run `python verification/check_wheel.py` from the extracted package directory.

## Relationship to prior work
Barnett–Farber establish foundational integral intersection-form and planar-graph results for two-point configuration spaces (arXiv:0903.2180, 12 March 2009); Farber–Hanbury extend that theory (arXiv:1005.2300). Prue–Scrimshaw's stable equivalence theorem (arXiv:0909.5511) justifies using the unsubdivided two-particle cubical model. Maciążek–Sawicki (DOI:10.1007/s00220-019-03583-5, section 5.3) calculate nonequivariant homology for wheel-graph configuration spaces; in particular, the already-known two-particle second-homology vanishing and homology ranks are not claimed as new. Their wheel section does not state the full dihedral rational first-homology action or the contrast between cyclic and dihedral quotient homology. The present contribution is precisely that all-parameter equivariant character and its quotient implications.

## Limitations
The representation identification is only over \(\mathbb Q\); an integral decomposition of \(H_1\) as a dihedral lattice is not asserted. The result does not identify a canonical geometric basis or the fundamental group of either quotient. No assertion of absolute bibliographic priority is made; an equivalent treatment under different terminology could exist. The computational tests cover only \(4\le n\le14\), while the proof covers every integer \(n\ge4\).

## References
1. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180, first posted 12 March 2009, https://arxiv.org/abs/0903.2180.
2. P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511, first posted 30 September 2009, https://arxiv.org/abs/0909.5511.
3. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300, first posted 13 May 2010, https://arxiv.org/abs/1005.2300.
4. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics 371 (2019), 921–973, DOI:10.1007/s00220-019-03583-5, section 5.3, https://doi.org/10.1007/s00220-019-03583-5.
