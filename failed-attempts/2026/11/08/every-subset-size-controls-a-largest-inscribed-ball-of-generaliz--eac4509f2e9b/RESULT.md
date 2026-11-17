# Every subset size controls a largest inscribed ball of generalized parking-function polytopes

## Finding
For every integer \(n\ge2\) and every positive integral parameter vector \(\mathbf b=(b_1,\ldots,b_n)\), let \(P_{\mathbf b}\subset\mathbb R^n\) be the convex hull of the positive integral vectors whose nondecreasing coordinate rearrangement \((\beta'_1,\ldots,\beta'_n)\) satisfies \(\beta'_j\le S_j:=\sum_{i=1}^j b_i\). Define
\[
R_k=\sum_{j=n-k+1}^n(S_j-1),\qquad
r_k=\frac{R_k}{k+\sqrt k},\qquad 1\le k\le n,
\]
and \(r=\min_{1\le k\le n}r_k\). The maximum radius of a Euclidean ball contained in \(P_{\mathbf b}\) is exactly \(r\), and its center is **unique**:
\[
\operatorname{inrad}_2(P_{\mathbf b})=r,\qquad
c=(1+r)\mathbf1.
\]
Every one of the \(n\) lower coordinate facets is tangent to this ball. Precisely those upper subset facets with \(|I|\in M:=\{k:r_k=r\}\) are tangent. Thus the exact number of tangent facets is
\[
 n+\sum_{k\in M}\binom nk.
\]
When \(b_1=1\), subset inequalities of size \(n-1\) are redundant, and \(n-1\notin M\); the formula still applies.

**Full phase realization.** For every \(n\ge2\) and every \(m\in\{1,\ldots,n\}\), there exists a positive integer parameter vector with \(b_1\ge2\) for which \(M=\{m\}\). Consequently every upper-facet cardinality occurs as the *unique* controlling cardinality, already including genuinely intermediate ones. For example, \(n=3\), \(\mathbf b=(34,1,16)\) has
\[
 (R_1,R_2,R_3)=(50,84,117),\qquad
 \frac{84}{2+\sqrt2}<\min\left\{25,\frac{117}{3+\sqrt3}\right\},
\]
so its maximum ball touches all three lower coordinate facets and all three upper **pair-sum** facets, but neither the upper single-coordinate facets nor the full-sum facet. Indeed, the first comparison follows from \(34^2<2\cdot25^2\), and the second follows from the exact rational bounds \(\sqrt3<1733/1000\) and \(\sqrt2>1414/1000\).

## Assumptions and scope
The metric is the ordinary Euclidean metric in the standard coordinate realization, not an arbitrary unimodularly transformed realization. Parameters are positive integers and \(n\ge2\), so the polytope is full dimensional. The result concerns *inscribed Euclidean balls*; no claim about John ellipsoids, enclosing spheres, or Ehrhart coefficients is made. The quantity \(R_k\) is the upper subset-sum bound after translating the polytope by \(-\mathbf1\), not a lattice-invariant quantity.

## Proof
**1. Facets and feasibility.** A published inequality description of generalized parking-function polytopes states that, after the translation \(z_i=x_i-1\),
\[
 z_i\ge0\quad(1\le i\le n),\qquad
 \sum_{i\in I}z_i\le R_{|I|}
 \quad(\varnothing\ne I\subseteq[n]).
\]
When \(b_1=1\), the constraints with \(|I|=n-1\) are redundant; every other displayed supporting inequality defines a facet. These facts are Theorem 2.3(c) of Bayer et al. [2]. The outward upper-facet normal is \(\mathbf1_I\), with Euclidean length \(\sqrt{|I|}\).

A ball of radius \(\rho\) centered at \(z\) lies in the translated polytope if and only if
\[
 z_i\ge\rho\quad\hbox{for all }i,\qquad
 \sum_{i\in I}z_i+\rho\sqrt{|I|}\le R_{|I|}
 \quad\hbox{for all nonempty }I.
\]
For every candidate ball, the first inequalities imply \(\sum_i z_i\ge n\rho\). Average the second inequality over all subsets of any fixed cardinality \(k\). Every coordinate appears in the same fraction \(k/n\) of these subsets. Therefore
\[
 k\rho+\rho\sqrt k\le R_k,
\]
so \(\rho\le r_k\) for each \(k\), hence \(\rho\le r\). Conversely, choosing \(z=r\mathbf1\) satisfies all displayed inequalities because \((k+\sqrt k)r\le R_k\). Thus \(r\) is attained.

**2. Rigidity and tangencies.** Let \(m\in M\) and let \(z\) be the center of any radius-\(r\) inscribed ball. Averaging its shifted upper inequalities over the size-\(m\) subsets gives
\[
 \frac mn\sum_i z_i+r\sqrt m\le R_m=r(m+\sqrt m),
\]
so \(\sum_i z_i\le nr\). But each \(z_i\ge r\); therefore every \(z_i=r\). This proves uniqueness. At this center the distance to each lower coordinate hyperplane is \(r\). The distance to any upper hyperplane indexed by \(I\) with \(|I|=k\) equals
\[
 \frac{R_k-kr}{\sqrt k},
\]
which equals \(r\) if and only if \(k\in M\). Every tangent hyperplane supports a genuine facet whenever it is nonredundant, and the tangency point is \(r\mathbf1+(r/\sqrt k)\mathbf1_I\) in shifted coordinates. When \(b_1=1\), the final increment \(S_1-1=0\) makes \(R_n=R_{n-1}\); since \(n+\sqrt n>n-1+\sqrt{n-1}\), one has \(r_n<r_{n-1}\). Thus a redundant size is never counted. Distinct facets have distinct tangency points.

**3. Every size is realized.** Fix \(n\ge2\) and a target \(m\in[n]\). Set \(g(t)=t+\sqrt t\) for \(t\ge0\). Choose a sufficiently small \(\varepsilon>0\) and prescribe a real rank profile at integer arguments by
\[
 F(k)=g(k)+\varepsilon\bigl(|k-m|-m\bigr),\quad k=0,1,\ldots,n.
\]
Then \(F(0)=0\), and for sufficiently small \(\varepsilon\) its successive increments are positive and strictly decreasing. Indeed, \(g(k)-g(k-1)=1+\sqrt k-\sqrt{k-1}\) is positive and strictly decreasing; the perturbation changes successive increments by \(-\varepsilon\) up to \(m\) and \(+\varepsilon\) after \(m\), creating only one possible upward jump of size \(2\varepsilon\), dominated by the strictly positive adjacent-slope gap of \(g\).

For \(1\le k\le m\),
\[
 \frac{F(k)}{g(k)}=1-\varepsilon\frac{k}{k+\sqrt k},
\]
which is strictly decreasing in \(k\). For \(k\ge m\),
\[
 \frac{F(k)}{g(k)}=1+\varepsilon\frac{k-2m}{k+\sqrt k},
\]
whose derivative for real \(k>0\) has the sign of \(2m+\sqrt k/2+m/\sqrt k>0\). Therefore \(m\) is the *strict unique* minimum of \(F(k)/g(k)\) among \(1\le k\le n\).

All the strict inequalities just established remain true after sufficiently close simultaneous rational approximation of \(F(1),\ldots,F(n)\), keeping \(F(0)=0\). Multiply the approximating rank values by a sufficiently large common positive denominator. Their successive increments then become strictly decreasing positive integers \(A_n>A_{n-1}>\cdots>A_1\ge1\), where \(A_{n-k+1}=F(k)-F(k-1)\) for the scaled profile. Choose \(b_1=A_1+1\) and \(b_j=A_j-A_{j-1}\) for \(j\ge2\). All \(b_j\) are positive integers, and \(S_j-1=A_j\). Thus the resulting integer parking-function polytope has rank values equal to the selected integers, with exactly \(M=\{m\}\) and \(b_1\ge2\). This completes the all-layer construction.

## Verification
The supplementary `verify.py` constructs independent full-halfspace Chebyshev linear programs for small dimensions and compares their optimal radii and centers against the exact formula. It also tests all singleton controlling cardinalities in dimensions two through seven using high-precision integer-parameter witnesses and checks random parameter vectors. It executes as `python verify.py`; the LP cross-check requires SciPy, while the exact formula and phase checks use Python's standard library. Its finite computations are corroborative only: the proof above covers every admissible dimension and parameter vector.

## Relationship to prior work
Bayer et al. [2] prove the general facet and vertex descriptions, including the precise redundancy when the first parameter equals one. Their work does not state the Euclidean inradius, the full tangent-facet stratification, or the every-cardinality realization theorem. Hill et al. [1] study lattice slicing, Ehrhart enumeration and magic positivity for the same all-parameter family; their publicly accessible abstract states no Euclidean inball theorem. A separate published inball result treats only the two-parameter subfamily \((a,b,b,\ldots,b)\), where exactly the first or last upper-facet size is controlling. The complete all-parameter phase realization, notably the intermediate pair-sum phase in dimension three, is not implied by that restricted conclusion.

## Limitations
The facet description is imported from [2], an established, fully inspected source, rather than reproved here. The claim is metric and depends on the standard coordinate realization. The all-parameter statement is mathematical, not statistical; numerical checks do not certify the universal quantifiers. Historical priority could still be affected by an unlocated general symmetric-polymatroid Chebyshev-center theorem or an inaccessible paper. There is no claim that arbitrary prescribed *sets* of simultaneous active sizes are realizable; only each single size is realized in isolation.

## References
1. Charlie Hill, Ambrose Luo, Vu Trinh, and Andrés R. Vindas-Meléndez, *Lattice slices, Ehrhart polynomials, and magic positivity of generalized parking-function polytopes*, arXiv:2607.15503, first public version 2026-07-16.
2. Margaret M. Bayer, Steffen Borgwardt, Teressa Chambers, Spencer Daugherty, Aleyah Dawkins, Danai Deligeorgaki, Hsin-Chieh Liao, Tyrrell McAllister, Angela Morrison, Garrett Nelson, and Andrés R. Vindas-Meléndez, *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, first public version 2024-03-12; *Discrete & Computational Geometry* 76 (2026), 339–377, DOI 10.1007/s00454-025-00770-1, especially Theorem 2.3(c).
