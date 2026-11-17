# A mod-four reflection-orientation law for mixed-parity torus-grid Rips spheres

## Finding
For an odd integer \(m\ge5\) with \(3\nmid m\) and an integer \(b\ge2\), put \(G=C_m\square C_{2b}\), endowed with its unweighted shortest-path graph metric. Its diameter is \(D=(m-1)/2+b\). Let \(X=\operatorname{VR}_{\le D-1}(G)\) be the inclusive next-to-last Vietoris–Rips complex. Set \(q=2\lfloor m/3\rfloor+1\). Then
\[
X\simeq S^{bq-1},\qquad \widetilde H_{bq-1}(X;\mathbb Z)\cong\mathbb Z,
\]
and all other reduced integral homology groups vanish.

The **new conclusion** is the orientation character on this primitive integral homology generator under the natural factorwise \(D_m\times D_{2b}\) action. Four standard generators act as follows:
\[
\begin{array}{c|c|c}
\text{generator}&\text{vertex action}&\text{sign on }\widetilde H_{bq-1}(X;\mathbb Z)\\\hline
r&(x,y)\mapsto(x+1,y)&+1\\
s&(x,y)\mapsto(-x,y)&\epsilon_m^{b}\\
t&(x,y)\mapsto(x,y+1)&(-1)^b\\
u&(x,y)\mapsto(x,-y)&(-1)^{\lfloor b/2\rfloor}
\end{array}
\]
where \(\epsilon_m=+1\) when \(m\equiv1\pmod6\) and \(\epsilon_m=-1\) when \(m\equiv5\pmod6\). These generators determine the entire **integral** one-dimensional representation. Its restriction to the translations is already known; the reflection signs and ensuing quotient dichotomy are the contribution here.

For the geometric quotient by this specified finite group,
\[
\widetilde H_i\bigl(X/(D_m\times D_{2b});\mathbb Q\bigr)
\cong\begin{cases}
\mathbb Q,&i=bq-1\text{ and }b\equiv0\pmod4,\\
0,&\text{otherwise.}
\end{cases}
\]
Thus the rational positive-degree class survives *all* factorwise rotations and reflections exactly at widths divisible by eight (that is, when \(2b\equiv0\pmod8\)).

## Assumptions and scope
\(C_k\) is a simple cycle graph (\(k\ge3\)); \(G\) is its Cartesian graph product, not categorical graph product. The Rips simplices are the finite sets of vertices having all pairwise shortest-path distances at most \(D-1\). Homology uses its usual oriented integer simplicial chain complex. The group is the displayed factorwise dihedral subgroup of graph automorphisms; no statement is made about every possible graph automorphism or any other filtration scale. The quotient is the topological orbit space (rather than an orbit of abstract vertex subsets).

## Proof
**1. Exact forbidden graph.** Put \(a=(m-1)/2\). Graph distance is
\[d((x,y),(z,w))=\min(|x-z|,m-|x-z|)+\min(|y-w|,2b-|y-w|),\]
with coordinate differences read cyclically. Distance \(D=a+b\) occurs exactly at the pairs \((x,y),(x\pm a,y+b)\). The forbidden-pair graph splits into \(b\) connected cycles of length \(2m\), one over each opposite-column pair \(\{j,j+b\}\). Indeed, \(\gcd(a,m)=1\), and alternating the two columns runs through every first coordinate. Consequently, as simplicial complexes,
\[X=\operatorname{Ind}(\bigsqcup_{j=0}^{b-1}C_{2m})=\operatorname{Ind}(C_{2m})^{*b}.\]

**2. Integral homotopy and Koszul sign.** For \(m\equiv1,5\pmod6\), the classical independence-complex cycle theorem gives \(K=\operatorname{Ind}(C_{2m})\simeq S^{q-1}\), where \(q=2\lfloor m/3\rfloor+1\) is odd and \(q-1\) is even. The join is therefore homotopy equivalent to \(S^{bq-1}\), with primitive top homology canonically a tensor product of \(b\) rank-one factor groups. Exchanging two factors of the join contributes \((-1)^{q^2}=-1\), since \(q\) is odd.

**3. Rotation and first-coordinate reflection on one factor.** Give the canonical cycle \(C_{2m}\) a cyclic index \(z\). The original rotation \(r:x\mapsto x+1\) acts on this cycle as a shift \(z\mapsto z-2\). The only independent subsets invariant under the shift by two are the empty subset and the two parity classes (\(m\) vertices each); their signed augmented Lefschetz sum equals \(+1\). Because the only reduced homology of \(K\) is rank one in even degree, \(r\) has degree \(+1\) on that homology.

The first-coordinate reflection \(s:x\mapsto-x\) becomes the reflection \(z\mapsto-z\) of \(C_{2m}\). Its orbit classes are arranged in a path \(P_{m+1}\): two singleton orbits and \(m-1\) paired orbits. Each admissible orbit chosen in an invariant independent set contributes a factor \(-1\) to the alternating signed simplicial trace (singletons: one vertex, paired orbits: vertex transposition). If \(I(P_n;z)\) is the independence polynomial, the **reduced Lefschetz number** is therefore
\[\widetilde L(s;K)=-I(P_{m+1};-1).\]
The recurrence \(I(P_n;-1)=I(P_{n-1};-1)-I(P_{n-2};-1)\) has the six-periodic sequence \(1,0,-1,-1,0,1,\ldots\), starting at \(n=0\). Thus \(I(P_{m+1};-1)=-1\) for \(m\equiv1\pmod6\) and \(+1\) for \(m\equiv5\pmod6\). Since the factor sphere dimension is even, \(s\) acts by \(\epsilon_m\). It acts simultaneously on all \(b\) factors, giving \(\epsilon_m^b\).

**4. Antipodal-column swap and even-coordinate rotation.** The involution \(h\) that exchanges opposite columns within one forbidden cycle is its antipodal half-turn \(z\mapsto z+m\). In the fixed-face Lefschetz calculation, its paired vertex orbits form the quotient cycle \(C_m\), giving \(\widetilde L(h;K)=-I(C_m;-1)=-1\): for odd \(m\) not divisible by three, \(\operatorname{Ind}(C_m)\) is an odd-dimensional sphere, so \(I(C_m;-1)=1\). Thus \(h_*=-1\) on the primitive factor generator.

The even-coordinate translation \(t:y\mapsto y+1\) cyclically permutes the \(b\) joins and crosses one antipodal half-turn at the seam. The \(b\)-cycle of the odd-degree *suspended* factors has Koszul sign \((-1)^{b-1}\), and the seam contributes \(-1\). Hence \(t_*=(-1)^b\).

**5. Even-coordinate reflection and the mod-four boundary.** Let \(u:y\mapsto-y\). It permutes opposite-column pairs indexed by \(j\pmod b\) via \(j\mapsto-j\). When \(b\) is odd there is exactly one fixed pair, \(\{0,b\}\), on which \(u\) is the identity. The other \((b-1)/2\) pairs of factors are interchanged, each with Koszul sign \(-1\). Hence \(u_*=(-1)^{(b-1)/2}\).

When \(b\) is even, the fixed pair at \(j=0\) is acted on trivially and the second fixed pair at \(j=b/2\) has its two columns exchanged, contributing \(h_*=-1\). There are \((b-2)/2\) other factor transpositions. Their combined sign is \((-1)^{1+(b-2)/2}=(-1)^{b/2}\). Both cases are \(u_*=(-1)^{\lfloor b/2\rfloor}\). This completes the four generator signs.

**6. Quotient consequence.** For a finite group acting simplicially on a finite complex, rational homology of the geometric quotient is the invariant rational homology of the cover (using the orientation-aware quotient cellular chains, or rational transfer). As \(X\) is a homotopy sphere with one-dimensional top homology, a positive-degree quotient class survives iff all four generators act with sign \(+1\). If \(b\) is odd, \(t\) acts by \(-1\); if \(b\equiv2\pmod4\), \(u\) acts by \(-1\); if \(b\equiv0\pmod4\), \(t,u,s,r\) all act trivially. The stated dichotomy follows.

## Verification
The standalone standard-library program `check_dihedral.py` constructs the metric forbidden graph from all pairwise distances and independently enumerates signed, fixed-simplex Lefschetz traces (via permutation-orbit independence polynomials) for all four generators. Seven tested parameter pairs are \((m,b)=(5,2),(5,3),(5,4),(7,2),(7,3),(7,4),(11,2)\), reaching 56 vertices. All checks passed, including the nontrivial negative reflection signs and the first width-eight survival case. These are finite corroborations; the argument above proves all specified \(m,b\).

## Relationship to prior work
Adams–Adetowubo–Barriga-Acosta–Feng–Sterling (2025) investigate the graph-metric Rips homotopy types for square torus grids; their full-text results do not state this mixed-parity factorwise reflection character. The publicly recorded result *Cyclic translation characters at the penultimate Rips scale of mixed-parity torus grids* (2026) already gives the general odd-by-even sphere-wedge formula and the complete **even-coordinate rotation** representation; those facts are prerequisites, not new contributions here. Its stated scope expressly does not address the full automorphism group. The present contribution completes the natural factorwise dihedral **integral orientation character** in the rank-one regime and derives the sharp mod-four full-symmetry quotient boundary. The cycle independence-complex theorem used in the proof is classical; no novelty is asserted for it. Equivalent unpublished or unindexed descriptions remain a priority risk.

## Limitations
No conclusion is asserted for odd \(m\) divisible by three (when factor homology has rank two), for different distance scales, or for Euclidean rather than shortest-path metrics. The quotient result is rational, not an integral homology classification of the orbit space. No independent mathematical validation has been performed.

## References
- H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng and J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134, first posted 2025-02-10, https://arxiv.org/abs/2502.07134.
- *Cyclic translation characters at the penultimate Rips scale of mixed-parity torus grids*, public published-finding corpus research record, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-cyclic-translation-characters-at-the-penultimate-rips-scale-of-m--4a3060d5f0be.
- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (2023), https://arxiv.org/abs/2307.12401.
