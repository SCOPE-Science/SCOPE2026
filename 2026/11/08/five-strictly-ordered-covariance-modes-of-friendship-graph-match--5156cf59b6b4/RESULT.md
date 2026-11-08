# Five strictly ordered covariance modes of friendship-graph matching polytopes

## Finding

For each integer \(m\ge2\), let \(F_m\) be the friendship (Dutch-windmill) graph comprising \(m\) triangles with a single common hub. Let \(P_m\subset\mathbb R^{3m}\) be the convex hull of the indicator vectors of all matchings of \(F_m\), including the empty matching. For a uniformly chosen vertex \(X\) of \(P_m\), the covariance matrix has exactly five distinct eigenvalue classes. Set \(n=m+1\). They are

\[
\lambda_{C,\pm}=\frac{m+3\pm\sqrt{m^2-2m+9}}{8n},\qquad \operatorname{mult}(\lambda_{C,\pm})=m-1,
\]
\[
\lambda_{U,\pm}=\frac{m^2+m+3\pm\sqrt{(m^2+m+3)^2-8mn}}{8n^2},\qquad \operatorname{mult}(\lambda_{U,\pm})=1,
\]
\[
q=\frac1{2n},\qquad \operatorname{mult}(q)=m.
\]

For every \(m\ge2\), their order is strict:

\[
0<\lambda_{U,-}<\lambda_{C,-}<q<\lambda_{U,+}<\lambda_{C,+}.
\]

The least-variance eigenspace is the single axial-minus line in the span of the uniform base-edge and uniform spoke-edge vectors. The greatest-variance eigenspace has dimension \(m-1\) and lies in the coupled base-edge/spoke-symmetric contrast sector. The exact spectral condition number satisfies

\[
\kappa(\operatorname{Cov}(X))=\frac{\lambda_{C,+}}{\lambda_{U,-}}\sim\frac{m^2}{2}\quad(m\to\infty).
\]

## Assumptions and scope

The graph has hub \(h\), outer vertices \(u_i,v_i\) and three edges \(a_i=u_iv_i\), \(b_i=hu_i\), \(c_i=hv_i\) for every \(1\le i\le m\). The ambient metric is ordinary edge-coordinate Euclidean distance, not an intrinsic graph distance or an ellipsoidal metric. All matching-indicator vectors are distinct vertices because a zero-one point cannot be a nontrivial convex combination of other zero-one points. The empty matching and each single-edge matching are vertices, so the polytope has full affine dimension \(3m\). The probability is uniform over those vertices, not the volume-uniform distribution on \(P_m\).

## Proof

**Matching count and moments.** Every matching has either no spoke edge (then all \(m\) base edges can be independently selected) or exactly one spoke edge (then all but its own base edge can independently be selected). Thus the exact number of matching vertices is \(2^m+2m2^{m-1}=(m+1)2^m\). Write \(A_i\) for the indicator of \(a_i\), and \(B_{i,0},B_{i,1}\) for the indicators of the two spokes in triangle \(i\). Counting gives

\[
\mathbb EA_i=\frac{m}{2n},\quad \mathbb EB_{i,\epsilon}=\frac1{2n};\quad
\mathbb EA_iA_j=\begin{cases}\frac{m}{2n},&i=j,\\\frac14-\frac1{2n},&i\ne j,\end{cases}
\]

and, for spokes, \(\mathbb EB_{i,\epsilon}B_{j,\eta}=0\) whenever the two spoke labels are distinct. In addition, \(\mathbb EA_iB_{j,\epsilon}=0\) when \(i=j\), and equals \(1/(4n)\) otherwise. All mixed expectations follow directly by choosing a unique spoke and independently choosing each unblocked base edge with probability one half.

**Covariance blocks.** Let \(I,J\) denote appropriately sized identity and all-ones matrices. Let \(H\) be the \(m\times2m\) matrix with \(H_{i,(j,\epsilon)}=1\) when \(i=j\), and zero otherwise. With all base coordinates followed by all spoke coordinates, the block covariance is

\[
\Sigma_{AA}=\frac14 I_m-\frac1{4n^2}J_m,\qquad
\Sigma_{BB}=\frac1{2n}I_{2m}-\frac1{4n^2}J_{2m},\qquad
\Sigma_{AB}=\frac1{4n^2}J_{m,2m}-\frac1{4n}H.
\]

For example, the displayed base moment formulas yield base off-diagonal covariance \(-1/(4n^2)\), and the same-triangle mixed covariance is \(-m/(4n^2)\). These verify the normalization of all entries.

**Invariant decomposition.** The spoke-pair antisymmetric vectors \(e_{b_i}-e_{c_i}\) span an \(m\)-dimensional eigenspace of eigenvalue \(q=1/(2n)\). For any base contrast vector \(v\in\mathbb R^m\) with \(\sum_i v_i=0\), pair it with the normalized symmetric spoke vector \(w\) having \(w_{b_i}=w_{c_i}=v_i/\sqrt2\). On their orthonormal two-dimensional span, \(\Sigma\) acts as the symmetric matrix

\[
C_m=\begin{pmatrix}\tfrac14&-\tfrac{\sqrt2}{4n}\\-\tfrac{\sqrt2}{4n}&\tfrac1{2n}\end{pmatrix}.
\]

This yields the two contrast eigenvalues, each \(m-1\) times, from its trace and determinant. The remaining two-dimensional subspace spanned by the normalized uniform base vector \(\mathbf1_m/\sqrt m\) and normalized uniform spoke vector \(\mathbf1_{2m}/\sqrt{2m}\) has matrix

\[
U_m=\frac1{4n^2}\begin{pmatrix}m^2+m+1&-\sqrt2\\-\sqrt2&2\end{pmatrix}.
\]

Its eigenvalues are exactly \(\lambda_{U,\pm}\). The subspace dimensions sum to \(m+2(m-1)+2=3m\), so the list is exhaustive.

**Strict hierarchy and asymptotics.** Both \(C_m\) and \(U_m\) have positive determinants: \(\det C_m=m/(8n^2)\) and \(\det U_m=m/(8n^3)\). Since \(C_m\) has a nonzero off-diagonal entry and a diagonal entry \(q\), strict interlacing of its two eigenvalues with that entry gives \(\lambda_{C,-}<q<\lambda_{C,+}\). The upper eigenvalue of \(U_m\) exceeds its first diagonal entry \((m^2+m+1)/(4n^2)\), which exceeds \(q\) for \(m\ge2\), because \(m^2-m-1>0\). Conversely \(\tfrac14 I_2-U_m\) is positive definite: its first diagonal entry equals \(m/(4n^2)>0\), and its determinant is \([m(n^2-2)-2]/(16n^4)>0\) for \(m\ge2\). Hence \(\lambda_{U,+}<1/4<\lambda_{C,+}\).

For the lower eigenvalues, \(\lambda_{U,-}<U_{22}=1/(2n^2)\), while positivity of \(C_m\) gives \(\lambda_{C,-}\ge\det C_m/\operatorname{tr}C_m=m/[2n(m+3)]\). The latter lower bound exceeds \(1/(2n^2)\) precisely when \(m^2>3\), true for \(m\ge2\). This proves all strict inequalities. Finally \(\lambda_{C,+}\to1/4\) and \(\lambda_{U,+}\to1/4\); the exact product \(\lambda_{U,-}\lambda_{U,+}=m/(8n^3)\) yields \(\lambda_{U,-}\sim1/(2m^2)\) and hence the announced condition-number asymptotic.

## Verification

The accompanying `verify.py` enumerates the complete matching vertex sets for \(2\le m\le8\) and checks all \(1,827\) covariance entries using rational arithmetic. Across these seven cases it inspects \(4,092\) matching vertices. It also checks the spectral ordering for \(2\le m\le500\) and checks both block characteristic-polynomial identities exactly for \(2\le m\le1000\). The infinite-family theorem rests on the preceding proof, not on finite enumeration.

Run `python verify.py` using Python 3; the checker needs only the Python standard library.

## Relationship to prior work

Abreu, Costa, Nascimento and Patuzzi (2019) define graph matching polytopes and determine skeleton-degree properties of general matching polytopes, including special conditions involving triangles. The examined complete article does not determine vertex-uniform covariance or its eigenvalues. Classical monomer-dimer results provide partition-function and correlation formalisms, but a general partition-function derivative identity alone does not specify the five strict eigenvalue classes for this non-edge-transitive windmill family. Related published work on symmetric-edge polytopes of clique windmills concerns a different polytope and different metric invariant. The finding concerns the explicit Euclidean second-moment geometry of these matching polytopes, not their graph adjacency spectrum, face enumeration or minimum-volume ellipsoids.

## Limitations

The spectral hierarchy is asserted only for \(m\ge2\); the single-triangle case has additional degeneracy. The result does not identify John or Löwner ellipsoids, volume-uniform covariance, strong optimization complexity or spectra for arbitrary windmills of larger cliques. Mathematical priority against all historical monomer-dimer formulations remains subject to independent literature review. All proofs and tests are presented without claiming independent validation.

## References

1. N. M. M. de Abreu, L. M. G. C. da Costa, C. H. P. Nascimento, and L. Patuzzi, “A Note on the Matching Polytope of a Graph,” *Trends in Computational and Applied Mathematics* **20** (2019), 189–196, DOI: 10.5540/tema.2019.020.01.0189; https://tema.sbmac.org.br/tema/article/download/1239/881/6725 (published 2019-05-20).
2. A. Giuliani, I. Jauslin, and E. H. Lieb, “A Pfaffian formula for monomer-dimer partition functions,” *J. Stat. Phys.* **163** (2016), 211–238; arXiv:1510.05027. Its planar-graph partition-function setting is background, not a claimed anticipation of the computed spectrum.
3. E. W. Weisstein, “Dutch Windmill Graph,” *MathWorld*, https://mathworld.wolfram.com/DutchWindmillGraph.html (terminology and graph construction).
