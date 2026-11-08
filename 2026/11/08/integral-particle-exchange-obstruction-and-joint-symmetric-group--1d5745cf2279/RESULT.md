# Integral particle-exchange obstruction and joint symmetric-group character of two-point stars

## Finding
For every integer \(m\ge3\), let \(S_m\) be the metric star formed from \(m\) closed unit intervals joined at their zero endpoints. The ordered collision-free configuration space \(F_2(S_m)=\{(p,q):p\ne q\}\) has an equivariant strong deformation retract onto the subdivided crown graph with edges indexed by ordered pairs \((i,j)\) of distinct arms. Its integral first homology is canonically the lattice
\[
L_m=\left\{(a_{ij})_{i\ne j}\in\mathbb Z^{m(m-1)}:\sum_{j\ne i}a_{ij}=\sum_{j\ne i}a_{ji}=0\text{ for all }i\right\}.
\]
The group \(S_m\times C_2\), acting respectively by arm permutations and particle exchange \(T\), acts via \((\sigma a)_{ij}=a_{\sigma^{-1}i,\sigma^{-1}j}\) and \((Ta)_{ij}=-a_{ji}\). All higher homology vanishes, and \(\operatorname{rank}L_m=m^2-3m+1\).

Let \(L_m^+=\ker(T-1)\) and \(L_m^-=\ker(T+1)\) inside the **integral** lattice. The following exact obstruction is the principal statement:
\[
\boxed{L_m/(L_m^++L_m^-)\cong(\mathbb Z/2)^{m(m-3)/2}.}
\]
Consequently integral splitting into particle-exchange eigensublattices fails for every \(m\ge4\), despite an eigenspace decomposition over \(\mathbb Q\). More precisely, for \(m\ge4\), with \(S^\lambda\) denoting rational Specht modules and \(\varepsilon\) the nontrivial one-dimensional \(C_2\)-module,
\[
H_1(F_2(S_m);\mathbb Q)\cong
(S^{(m-2,1,1)}\boxtimes\mathbf1)\oplus
(S^{(m-2,2)}\boxtimes\varepsilon).
\]
For \(m=3\), only the one-dimensional \(S^{(1,1,1)}\boxtimes\mathbf1\) term occurs. The **full joint character** is, for any \(\sigma\in S_m\), with \(f(\sigma)\) fixed arms and \(t_2(\sigma)\) two-cycles,
\[
\chi(\sigma,1)=f(\sigma)^2-3f(\sigma)+1,\qquad
\chi(\sigma,T)=1-2t_2(\sigma).
\]

## Assumptions and scope
All particles are labeled, the configuration points are distinct, and every arm has length exactly one (the construction also works after a common positive rescaling). The group acts by genuine isometries of the metric star and by exchanging labels. Homology is singular homology with indicated integral or rational coefficients. The assertion includes \(m=3\) (where the obstruction is zero), with representation formula stated separately. The rank-zero case \(m=2\) is excluded because the crown graph is disconnected.

## Proof
**1. Equivariant graph spine.** Write \(r(p)\in[0,1]\) for the radial coordinate on the arm containing \(p\). For \((p,q)\in F_2(S_m)\), the maximum \(R=\max\{r(p),r(q)\}\) is positive. Simultaneously change each radial coordinate \(r\) to \(((1-t)+t/R)r\), for \(0\le t\le1\). Distinct points on one arm remain distinct, points on distinct arms remain distinct, and a radial coordinate zero stays zero. The maximum radius becomes one, so this is a strong deformation retraction onto the subspace \(X\) in which at least one particle occupies an arm tip. It commutes with both arm permutations and label exchange.

In \(X\), whenever the first particle is at tip \(i\) and the second is strictly inside arm \(i\), contract the second particle radially to the center; do the analogous operation with the particles exchanged. These are disjoint open hairs attached at \((\mathrm{tip}_i,\mathrm{center})\) or \((\mathrm{center},\mathrm{tip}_i)\), and their closures meet the remaining spine only at those attachment points. Contracting them simultaneously gives a continuous equivariant strong deformation retraction fixing the rest. The spine has vertices \(A_i=(\mathrm{tip}_i,0)\), \(B_j=(0,\mathrm{tip}_j)\), and for each \(i\ne j\) the unique path \(A_i\to(\mathrm{tip}_i,\mathrm{tip}_j)\to B_j\). Thus it is the crown graph \(K_{m,m}\) with its matching removed and each remaining edge subdivided. It is connected for \(m\ge3\), has \(2m\) essential vertices and \(m(m-1)\) edges, and its first-homology rank equals \(m(m-1)-2m+1\).

**2. Integral chain model.** Orient each crown edge from \(A_i\) to \(B_j\). A one-chain with coefficients \(a_{ij}\) is closed exactly when every row and every column sums to zero. Because the spine is one-dimensional, the cycle lattice equals integral first homology without further quotient; in particular it has no torsion. Permuting arms preserves all these edge orientations, while exchanging labels sends the \(A_i\)-to-\(B_j\) edge to the reverse of the \(A_j\)-to-\(B_i\) edge, giving the stated actions.

**3. Integral eigenspace obstruction.** Since \(T\) acts as minus transposition, \(L_m^+\) consists of skew-symmetric zero-diagonal matrices with zero row sums, while \(L_m^-\) consists of symmetric zero-diagonal matrices with zero row sums. For any \(a\in L_m\), its rational eigenspace projections are \((a-a^t)/2\) and \((a+a^t)/2\). They are both integral exactly when \(a_{ij}\equiv a_{ji}\pmod2\) for every pair; their row and column sums automatically vanish. Therefore the cokernel is exactly the image of the parity map
\[
\delta:L_m\longrightarrow\mathbb F_2^{\binom m2},\quad
\delta(a)_{\{i,j\}}=a_{ij}-a_{ji}\bmod2.
\]
Each class has exponent two because \(2a=(a-a^t)+(a+a^t)\) lies in \(L_m^++L_m^-\). Reduction of the integral cycle lattice of the connected crown graph onto its mod-two cycle space is surjective: take integral fundamental cycles for a spanning tree. That binary cycle space has dimension \(m(m-1)-2m+1=m^2-3m+1\). Its subspace annihilated by \(\delta\) is the set of symmetric zero-diagonal mod-two matrices with even row sums, i.e. the binary cycle space of the complete graph \(K_m\), of dimension \(\binom m2-m+1=(m-1)(m-2)/2\). Thus
\[
\dim_{\mathbb F_2}\operatorname{im}(\delta)
=(m^2-3m+1)-(m-1)(m-2)/2=m(m-3)/2,
\]
which proves the **exact abstract abelian group** claimed, not merely its order.

**4. Joint rational representation.** The skew-symmetric integral zero-row-sum lattice is the integral oriented cycle space of \(K_m\); rationally it identifies with \(\bigwedge^2 A\), where \(A=\ker(\mathbb Q^m\to\mathbb Q)\) is the standard \(S_m\)-representation. This is the irreducible \(S^{(m-2,1,1)}\), and \(T\) acts as plus one. The symmetric zero-row-sum part is the rational kernel of the unsigned incidence map from the permutation representation on unordered edges of \(K_m\) to the permutation representation on vertices. For \(m\ge4\), it is irreducible \(S^{(m-2,2)}\), with \(T\) acting as minus one. For \(m=3\), this kernel is zero. The direct sum over \(\mathbb Q\) follows from semisimplicity of the involution.

For any \(\sigma\), the signed trace on the crown graph is \(2f(\sigma)\) on vertices, \(f(\sigma)(f(\sigma)-1)\) on oriented edges, and the graph has one invariant connected-component class. Hence \(\chi(\sigma,1)=1-2f+f(f-1)\). Under \(\sigma T\), no crown vertex is fixed because the bipartition classes are exchanged. Exactly \(2t_2(\sigma)\) crown edges are fixed setwise, each with reversed orientation, so the cellular trace on oriented edges is \(-2t_2(\sigma)\); therefore \(\chi(\sigma,T)=1-2t_2(\sigma)\). The formulas hold for all permutations, including the identity.

## Verification
The included standalone Python 3 program `verify.py` enumerates the ordered Abrams cubical model on a star with two edges per arm, all \(m!\) arm permutations, and both label-exchange states, for \(3\le m\le6\). Signed cellular Lefschetz traces are compared to the two character formulas for every group element (1,740 tests). The program also enumerates integral fundamental cycles of the crown graph and computes the rank of their parity images over \(\mathbb F_2\), confirming the predicted exponents \(0,2,5,9\). This is a finite consistency check; the deformation retraction, integer cokernel, and all-parameter character are established by the preceding proofs, not inferred from test cases. Run `python3 verify.py`; the expected exact standard output is in `verify_output.txt`.

## Relationship to prior work
Farley–Sabalka (arXiv:math/0410539, 2004) establish foundational graph-braid Morse methods. Doig's *Stellar Braiding* (arXiv:math/0412531, 2004) explicitly constructs a one-dimensional spine of **unordered** star-configuration spaces; our two-label crown spine is related by the natural ordered double cover, and we do not claim the nonequivariant Betti-rank computation as new. Barnett–Farber (arXiv:0903.2180, 2009) investigate ordered two-particle graph spaces generally. Wawrykow (arXiv:2401.13821, 2024) develops ordered star homology and specifically describes the particle-swap splitting for the four-arm, two-particle example; that special rational fact is prior work. The present distinction is the uniform complete **joint arm-permutation and label-exchange module** together with the **exact integral, non-splitting parity obstruction**, not the existing ranks or special label-swap cases. A natural lift of Doig's spine may make this result derivable, but the examined texts do not state the integral obstruction or the uniform joint module.

## Limitations
The graph spine and first-homology lattice are specialized to exactly two labeled particles and equally long arms; no claim is made about unequal-arm isometry groups or other particle numbers. The quotient statement is an isomorphism of abstract abelian groups, not a complete classification of its additional \(S_m\)-module structure. The rational decomposition is not an integral decomposition. No independent audit or definitive publication-priority determination has been performed. Equivalent unindexed literature remains possible.

## References
1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, first posted 2004-10-25, arXiv:math/0410539, https://arxiv.org/abs/math/0410539.
2. M. I. Doig, *Stellar Braiding*, first posted 2004-12-29, arXiv:math/0412531, https://arxiv.org/abs/math/0412531.
3. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, first posted 2009-03-12, arXiv:0903.2180, https://arxiv.org/abs/0903.2180.
4. N. Wawrykow, *Homology generators and relations for the ordered configuration space of a star graph*, first posted 2024-01-24, arXiv:2401.13821, https://arxiv.org/html/2401.13821v3.
