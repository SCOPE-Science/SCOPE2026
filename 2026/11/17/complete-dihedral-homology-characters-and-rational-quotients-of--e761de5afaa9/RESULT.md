# Complete dihedral homology characters of cyclic noncover complexes

## Finding
For every integer \(n\ge4\), write \(C_n\) for the simple cycle with vertex set \(V_n=\mathbb Z/n\), and \(X_n=\Theta(C_n)\) for its theta (noncover) simplicial complex. The dihedral symmetry \(D_n=\langle r,s:r^n=s^2=1,\;srs=r^{-1}\rangle\) acts through \(r(i)=i+1\) and \(s(i)=-i\). All reduced integral homology of \(X_n\) is torsion-free and concentrated in one degree, with the following rational character:

\[
\begin{array}{c|c|c|c|c}
n&d_n&\operatorname{rank}\widetilde H_{d_n}(X_n;\mathbb Z)&\chi(r^a)&\chi(r^as)\\\hline
3k&2k-2&2&2\ (3\mid a),\;-1\ (3\nmid a)&0\\
3k+1&2k-1&1&1&(-1)^k\\
3k+2&2k-1&1&1&(-1)^k
\end{array}
\]

For \(n=3k\), this is the inflation along \(D_{3k}\to D_3\) of the standard two-dimensional rational representation of \(D_3\). For \(n=3k+1\) or \(n=3k+2\), it is a one-dimensional integral sign character. The cohomology ring of the ordinary dihedral orbit space is

\[
H^*(|X_n|/D_n;\mathbb Q)\cong
\begin{cases}
H^*(S^{d_n};\mathbb Q),&n\equiv1,2\pmod6,\\
\mathbb Q\text{ concentrated in degree zero},&\text{otherwise}.
\end{cases}
\]

## Assumptions and scope
A face \(S\subseteq V_n\) lies in \(X_n\) if and only if \(V_n\setminus S\) contains an edge of \(C_n\). Thus \(X_n\) is the combinatorial Alexander dual of the ordinary independence complex \(K_n=\operatorname{Ind}(C_n)\). The group action is simplicial; all quotient spaces mean ordinary topological quotients, not Borel quotients. The statements include all integers \(n\ge4\); \(k=\lfloor n/3\rfloor\). Reduced homology includes the standard augmentation in degree \(-1\) when applying the Lefschetz trace formula; it is zero in all degrees other than the degree displayed above.

## Proof
**1. Degrees and torsion.** The classical cycle recurrence \(\operatorname{Ind}(C_n)\simeq\Sigma\operatorname{Ind}(C_{n-3})\), together with base lengths \(3,4,5\), gives \(\operatorname{Ind}(C_{3k})\simeq S^{k-1}\vee S^{k-1}\), \(\operatorname{Ind}(C_{3k+1})\simeq S^{k-1}\) and \(\operatorname{Ind}(C_{3k+2})\simeq S^k\). These are nonequivariant, previously known facts. Combinatorial Alexander duality, with its universal coefficient interpretation over \(\mathbb Z\), gives \(\widetilde H_j(X_n;\mathbb Z)\cong\widetilde H^{n-j-3}(K_n;\mathbb Z)\). Thus all the claimed integral homology ranks and degrees follow; this step makes no new claim of a homotopy-equivalent sphere wedge for \(X_n\).

**2. Equivariant sign.** If \(g\in D_n\) permutes the ordered vertices, the natural Alexander-duality pairing reverses orientation according to the ambient permutation sign \(\varepsilon_V(g)\). Therefore on rational characters,

\[
\chi_{X_n}(g)=\varepsilon_V(g)\chi_{K_n}(g),
\]

where the two characters refer to their respective unique nonzero reduced homology degrees. Let \(q_n\) be the latter degree for \(K_n\), equal to \(k-1\) for residues zero or one and \(k\) for residue two. Write \(F(g)\) for the independent-set orbit graph: its vertices are the orbits of \(g\) containing no adjacent pair, with two orbits joined if an original cycle edge meets them. A \(g\)-fixed independent set is exactly a union of some pairwise nonadjacent valid orbits. Its signed contribution to the augmented Lefschetz number is \((-1)^{t-1}\) for \(t\) selected orbits, including \(-1\) for the empty selection, because the induced permutation on each selected orbit has sign \((-1)^{|O|-1}\). Thus

\[
\widetilde L(g;K_n)=-I(F(g);-1),\qquad
\chi_{X_n}(g)=\varepsilon_V(g)(-1)^{q_n+1}I(F(g);-1),
\]

where \(I(H;t)=\sum_{A\in\operatorname{Ind}(H)}t^{|A|}\). This identity is valid even when an orbit contains adjacent original vertices (such orbits are simply excluded).

**3. Rotations.** For \(g=r^a\), let \(d=\gcd(n,a)\), with \(d=n\) when \(a=0\). For \(d\ge3\), the orbit graph is \(C_d\); for \(d=2\) it is a single edge, and for \(d=1\) it has no vertices. In all cases its independence polynomial at \(-1\) equals \(2\cos(\pi d/3)\), with the conventions just described. The vertex-permutation sign is \((-1)^{n-d}\). Substituting this into the preceding display and considering \(n\) and \(d\) modulo six gives the stated rotational character.

**4. Reflections.** For a path with \(m\ge0\) vertices, define \(p_m=I(P_m;-1)\). The deletion recurrence \(p_m=p_{m-1}-p_{m-2}\), initial values \(p_0=1\), \(p_1=0\), yields the period-six list \((1,0,-1,-1,0,1)\). If \(n=2m+1\) is odd, all reflections have orbit graph \(P_m\) and vertex sign \((-1)^m\). If \(n=2m\) is even, the vertex-axis reflections have orbit graph \(P_{m+1}\) and vertex sign \((-1)^{m-1}\); the edge-axis reflections have orbit graph \(P_{m-2}\) and vertex sign \((-1)^m\). In each case the reflection trace is \(\varepsilon_V(g)(-1)^{q_n+1}p_t\) for that path length \(t\). Inserting the period-six values gives trace zero if \(3\mid n\) and \((-1)^{\lfloor n/3\rfloor}\) otherwise, for either reflection class. This proves every character value, not merely the identity trace.

**5. Quotients.** For a finite simplicial group action, barycentric subdivision makes the action cellular without inversions, and rational transfer identifies the ordinary quotient cohomology with the invariant cohomology of the original space. The two-dimensional character has no rotation-invariant vectors (a rotation has trace \(-1\)); for the one-dimensional characters, rotations fix everything and reflections fix it precisely when \((-1)^k=1\). This is equivalent to \(n\equiv1,2\pmod6\). Because a single positive reduced cohomology group survives, the asserted quotient cohomology rings follow.

## Verification
The standalone standard-library checker `checks/theta_cycle_verify.py` independently enumerates all independent sets for lengths \(4\le n\le18\), calculates the signed augmented Lefschetz trace for every one of their \(2n\) dihedral symmetries, and compares it with the closed formulas. Additionally it directly enumerates all noncover faces and recomputes signed traces for 170 symmetries at lengths 4 through 13, without invoking Alexander duality. It also computes reduced homology ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) for \(4\le n\le13\) using independent boundary-rank elimination. Its reproduced output ends `NONCOVER_CYCLE_DIHEDRAL_CHARACTER_PASS` and reports 330 symmetry checks. The exhaustive checks corroborate finite lengths only; the proof of all \(n\) is the recurrence and combinatorial signed-orbit argument above.

## Relationship to prior work
Conant and Thistlethwaite introduced theta complexes as Alexander duals of independence complexes, in a paper first posted in 2008. Kozlov's cycle-independence homotopy recurrence is explicitly recorded in Adamaszek's 2011 preprint on cycle powers. Choi, Kim and Park study non-cover complexes and prove their general collapsibility bound; their paper also treats cycle graphs for a sharpness example. These sources supply the basic objects, duality and nonequivariant homotopy information, but the inspected sections do not supply the full natural dihedral character or the ordinary orbit-space cohomology classification. Related available records concerning three-uniform tight-cycle noncovers, cycle two-independence complexes, and three-cut complexes of complementary cycles have different defining face conditions; their statements do not imply this theorem. The earliest theta-complex preprint could not be read in full and remains a substantive publication-priority risk, as does any unindexed equivalent formulation.

## Limitations
The result is a rational representation classification together with integral homology ranks and torsion-freeness. It does not determine the integral \(D_n\)-module lattice when \(3\mid n\), the integral homology of the quotient, equivariant homotopy types or quotient contractibility. The cited 2008 original preprint was accessible only through its abstract and bibliographic record in this investigation; no assertion about its entire content is made. Independent verification and definitive publication priority are not established.

## References
1. J. Conant and O. Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739 (first public version 2008-08-05), DOI:10.1016/j.topol.2010.08.016.
2. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250 (first public version 2011-06-30), DOI:10.1016/j.jcta.2012.01.009.
3. I. Choi, J. Kim and B. Park, *Collapsibility of non-cover complexes of graphs*, arXiv:1904.10320 (2019-04-23).
