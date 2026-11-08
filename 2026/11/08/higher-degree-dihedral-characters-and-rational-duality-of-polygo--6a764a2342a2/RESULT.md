# Higher-degree dihedral characters and rational duality of polygonal moment-angle quotients

## Finding
For every integer \(n\ge 6\), let \(C_n\) be the simplicial cycle with vertices \(\mathbb Z/n\mathbb Z\), and let \(Z_n=(D^2,S^1)^{C_n}\). The dihedral group \(D_n=\langle r,s\rangle\) acts by coordinate permutations \(r(i)=i+1\) and \(s_a(i)=a-i\pmod n\). The following gives **all previously unaddressed higher-degree rational characters** \(\chi_{n,k}(g)=\operatorname{tr}(g\mid H^{k+1}(Z_n;\mathbb Q))\), for \(4\le k\le n-2\), and the top-degree character.

The identity trace is
\[
\chi_{n,k}(1)=(k-1)\binom nk-n\binom{n-2}{k-2}.
\]
For a nonidentity rotation \(r^a\) of order \(d=n/\gcd(n,a)\),
\[
\chi_{n,k}(r^a)=\begin{cases}
-(-1)^{(d-1)k/d}\binom{n/d}{k/d},&d\mid k,\\
0,&d\nmid k.
\end{cases}
\]
For reflections, write \(\chi_{n,k}(s_a)=[x^k]F_{n,a}(x)\), with
\[
F_{n,a}(x)=\begin{cases}
-(1-x^2)^{(n-3)/2}(1+x^3),&n\text{ odd},\\
-(1-x^2)^{n/2},&n\text{ even and }a\text{ even},\\
-(1-x^2)^{n/2-1}(1+x^2),&n\text{ even and }a\text{ odd}.
\end{cases}
\]
Thus the rational Betti numbers \(b_{k+1}(Z_n/D_n)\), in every degree \(5\le k+1\le n-1\), are explicit integers:
\[
 b_{k+1}(Z_n/D_n)=\frac{1}{2n}\left[\chi_{n,k}(1)-\sum_{\substack{d\mid\gcd(n,k)\\d>1}}\varphi(d)(-1)^{(d-1)k/d}\binom{n/d}{k/d}+R_{n,k}\right],
\]
where \(R_{n,k}=n[x^k]F_{n,0}(x)\) for odd \(n\), and \(R_{n,k}=\frac n2[x^k](F_{n,0}(x)+F_{n,1}(x))\) for even \(n\). Here \(\varphi\) is Euler's totient function, and \([x^k]\) denotes coefficient extraction.

In top degree, the one-dimensional representation on \(H^{n+2}(Z_n;\mathbb Q)\) is
\[
\omega_n(g)=\operatorname{sgn}(g\mid\mathbb Z/n\mathbb Z)\cdot\deg(g\mid |C_n|),
\]
where rotations have degree \(+1\) on the polygon and reflections have degree \(-1\). Consequently,
\[
 b_{n+2}(Z_n/D_n)=\begin{cases}1,&n\equiv3\pmod4,\\0,&\text{otherwise}.\end{cases}
\]
The rational cohomology ring of \(Z_n/D_n\) is a Poincaré-duality algebra of formal dimension \(n+2\) **if and only if** \(n\equiv3\pmod4\).

## Assumptions and scope
The vertices of \(C_n\) are labeled cyclically; edges join consecutive residues. All characters and quotient Betti numbers use rational coefficients. The quotient is the ordinary topological quotient by coordinate permutations, not a quotient by a subtorus, not the Borel construction, and not the real moment-angle space. The new character classification concerns \(n\ge6\), \(4\le k\le n-2\), plus degree \(n+2\). The lower-degree characters (degrees three and four) and ordinary Betti numbers are not asserted as new. The other cohomology groups of \(Z_n\), besides degrees zero, three through \(n-1\), and \(n+2\), vanish by the ordinary polygon calculation.

## Proof
**1. Equivariant squarefree Koszul model.** The standard cellular moment-angle cochain model is the squarefree part of the differential algebra with degree-one anticommuting generators \(u_i\), degree-two commuting generators \(v_i\), differential \(du_i=v_i\), and relations \(v_i^2=u_iv_i=0\) and \(v_iv_j=0\) for nonedges of the cycle. A coordinate permutation permutes generators, with the Koszul sign from reordering the \(u\)'s. It preserves the multigrading by supports \(I\subseteq\mathbb Z/n\mathbb Z\).

For a proper nonempty support \(I\) of size \(k\), the support block has three consecutive cochain groups: one generator \(u_I\) in degree \(k\); the \(k\) generators \(v_i u_{I\setminus\{i\}}\) in degree \(k+1\); and one generator \(v_iv_j u_{I\setminus\{i,j\}}\) for each edge \(\{i,j\}\) of the induced graph \(C_n[I]\) in degree \(k+2\). Its differential is the augmented simplicial cochain differential of the induced graph, twisted by the determinant line of the support. Since every proper induced subgraph of a cycle is a forest, its reduced first cohomology vanishes and the reduced zeroth cohomology has dimension \(c(I)-1\), where \(c(I)\) is the number of connected components. In particular, the first differential is injective, the second is surjective, and all cohomology of the support block occurs in degree \(k+1\).

**2. A signed fixed-support trace.** Suppose \(g(I)=I\). Write \(\delta_I(g)=\operatorname{sgn}(g\mid I)\), and let \(f_I(g)\) be the number of pointwise fixed vertices of \(I\). For each edge \(e\) of \(C_n[I]\) preserved setwise by \(g\), let \(\epsilon_e(g)=+1\) when both endpoints are fixed and \(-1\) when they are swapped. Taking the alternating trace of the exact-ended three-term block gives
\[
 \operatorname{tr}(g\mid H^{k+1}_I)=\delta_I(g)\left(f_I(g)-1-\sum_{\substack{e\in E(C_n[I])\\g(e)=e}}\epsilon_e(g)\right).
\]
Nonstable supports contribute no trace. The formula holds over \(\mathbb Z\) at the chain level; rationality is needed only for quotient transfer.

**3. Rotations.** A nonidentity rotation \(r^a\) of order \(d\) has \(m=n/d\) vertex orbits, each of length \(d\). No vertex or edge is fixed setwise (for \(n\ge4\)). A stable support comprises \(j\) full orbits, so \(k=dj\), there are \(\binom mj\) of them, and the determinant sign is \((-1)^{j(d-1)}\). The fixed-support trace from step 2 is minus that sign. Summing proves the rotation formula. For the identity, summing \(c(I)-1=k-1-|E(C_n[I])|\) over all supports yields the displayed binomial formula, because each cycle edge belongs to \(\binom{n-2}{k-2}\) supports.

**4. Reflections.** For a reflection with \(f\) fixed vertices and \(h\) transposed vertex pairs, the determinant-weighted generating polynomial of stable supports is \(P(x)=(1+x)^f(1-x^2)^h\). The contributions in step 2 are the weighted fixed-vertex count minus \(P(x)\), minus the weighted fixed-edge count. If \(n\) is odd, then \(f=1\), \(h=(n-1)/2\), and exactly one edge is exchanged endpointwise. The three contributions simplify to \(-(1-x^2)^{(n-3)/2}(1+x^3)\). When \(n\) is even, a vertex-axis reflection has two fixed vertices and no setwise fixed edge, giving \(-(1-x^2)^{n/2}\). An edge-axis reflection has no fixed vertex and two endpoint-swapped edges, giving \(-(1-x^2)^{n/2-1}(1+x^2)\). Coefficients of degree \(k\), with \(2\le k\le n-2\), are precisely the fixed-support traces. This proves the stated higher-degree formulas.

**5. Quotient and orientation.** For a finite group acting cellularly, rational transfer identifies ordinary quotient cohomology with the invariant part of the original cohomology. Averaging the \(2n\) character values, grouping nonidentity rotations by order (there are \(\varphi(d)\) of order \(d\)), yields the quotient formula. The top Hochster summand comes from \(\widetilde H^1(C_n;\mathbb Q)\) on full support, whose action is the orientation degree of the simplicial cycle tensored with the determinant of its vertex-permutation representation. A one-step rotation acts there by \((-1)^{n-1}\). For odd \(n\), every reflection acts by \((-1)^{(n+1)/2}\). The full dihedral action is therefore trivial in top degree exactly when \(n\equiv3\pmod4\).

Finally, \(Z_n\) is a closed oriented manifold of dimension \(n+2\), and the cup-product pairing is nondegenerate. If \(\omega_n\) is trivial, averaging transfers the perfect equivariant pairing to the invariant subalgebra; hence the quotient has rational Poincaré duality. Otherwise the top invariant cohomology vanishes while degree zero persists, so it cannot be a Poincaré-duality algebra of formal dimension \(n+2\). This proves the characterization.

## Verification
The standalone `verify.py` computes the same characters by two independently constructed finite procedures: explicit induced-component permutations with determinant twists, and signed traces of the Koszul monomial cochain groups. It checks their equality with the uniform closed formulas over cycle lengths four through eleven and all dihedral elements. Separate tests validate the cellular differential's permutation equivariance, alternating Lefschetz identities, exact integer quotient character averages, and the top-degree congruence. Execute `python3 verify.py` from the package directory and compare against `verification_output.txt`. The script reports 624 character comparisons, 29,340 cochain equivariance checks, 120 Lefschetz identities, and 276 exact transfer averages. These bounded tests corroborate, but do not replace, the all-\(n\) proof.

For example, in degrees \(5,6\), the rational quotient at \(n=7\) has Betti numbers \((2,2)\) and retains its one-dimensional top class. For \(n=8\), the quotient has Betti numbers \((4,4,2)\) in degrees \(5,6,7\) and no top rational class.

## Relationship to prior work
The classical squarefree Koszul model, Hochster decomposition and ordinary polygon Betti numbers are established in Buchstaber--Panov, arXiv:math/9912199, particularly their Theorem 3.3 and Example 3.11. Their published statements do not determine the higher-degree dihedral character values or the rational Poincaré duality criterion of the coordinate-permutation quotient. Li Yu, arXiv:1406.7392, studies quotient spaces arising from vertex partitions and torus subgroups; that construction is distinct from an ordinary quotient by polygon symmetries. The lower-degree dihedral characters are excluded from the new claim. The 2022 work of Zhi Lü and Song Zhang, DOI:10.1007/s10473-022-0602-1, is potentially relevant because it treats cohomology of certain polygonal moment-angle quotients; full-text comparison was unavailable, and the scope of its special quotient class is a residual novelty risk. See the accompanying review for a careful source comparison.

## Limitations
The proof gives rational characters, quotient Betti numbers and rational Poincaré duality, not integral quotient cohomology, cup-product presentations for the quotient, integral character lattices, fixed-point isotropy classification or an equivariant homotopy decomposition. No claim of independent validation or definitive publication priority is made. The character formulas derive from known cochain models but their all-higher-degree closed evaluation and quotient-orientation classification require the explicit equivariant trace computation given here.

## References
1. V. Buchstaber and T. Panov, *Torus actions, equivariant moment-angle complexes, and coordinate subspace arrangements*, arXiv:math/9912199 (first public 1999-12-24), https://arxiv.org/html/math/9912199v1 .
2. Li Yu, *On Hochster's formula for a class of quotient spaces of moment-angle complexes*, arXiv:1406.7392 (first public 2014-06-28), https://arxiv.org/html/1406.7392v3 .
3. Zhi Lü and Song Zhang, *On the (Co)Homology of (Quotients of) Moment-Angle Manifolds Over Polygons*, Acta Math. Sci. 42 (2022), 2204--2222, https://doi.org/10.1007/s10473-022-0602-1 .
4. T. Panov, *On the cohomology of quotients of moment-angle complexes*, arXiv:1506.06875 (first public 2015-06-23), https://arxiv.org/abs/1506.06875 .
