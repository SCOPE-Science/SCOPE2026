# Sharp endpoint laws for common-axis disk hulls

## Finding

Let \(m\ge3\). In \(\mathbb R^{m+1}\) with orthonormal basis \(e_0,\ldots,e_m\), let \(D_j\) be the centered unit disk in \(\operatorname{span}(e_0,e_j)\), \(1\le j\le m\), and put \(K_m=\operatorname{conv}(D_1\cup\cdots\cup D_m)\). For \(U\) uniform on \(S^m\), let \(W_m\) be the distance between the two support hyperplanes of \(K_m\) orthogonal to \(U\). The support reduction is
\[
W_m=2\sqrt{U_0^2+\max_{1\le j\le m}U_j^2},\qquad 2/\sqrt m\le W_m\le 2.
\]
For each fixed \(m\ge3\) and \(\varepsilon\downarrow0\), the two sharp endpoint laws are
\[
\begin{aligned}
\Pr(W_m\le 2/\sqrt m+\varepsilon)
 &=\frac{\Gamma((m+1)/2)m^{m-1/4}}{\pi^{m/2}\sqrt{m-1}\,\Gamma(m+1/2)}
   \varepsilon^{m-1/2}+O_m(\varepsilon^{m+1/2}),\\
\Pr(W_m>2-\varepsilon)&=m\varepsilon^{(m-1)/2}+O_m(\varepsilon^{m/2}).
\end{aligned}
\]
The endpoint statements concern fixed dimension. The two-disk law and the growing-dimensional Dirichlet-maximum limit below are comparison cases, not originality claims.

## Proof

The support function of \(D_j\) is \(\sqrt{u_0^2+u_j^2}\), and the support function of the hull is the maximum of these. Central symmetry doubles the support function to give the width. The minimum squared half-width is \(1/m\), by \(\max_{j\ge1}u_j^2\ge(1-u_0^2)/m\), with equality only at \(u_0=0\) and \(|u_j|=1/\sqrt m\) for all \(j\ge1\). The maximum is attained on the circles \(S^m\cap\operatorname{span}(e_0,e_j)\).

**Lower edge.** Put \(Y_j=U_j^2\). The vector \((Y_0,\ldots,Y_m)\) has a Dirichlet distribution with all parameters \(1/2\), with density \(C_m\prod_{j=0}^m y_j^{-1/2}\) in \(m\) independent simplex coordinates, where \(C_m=\Gamma((m+1)/2)/\pi^{(m+1)/2}\). Write \(\delta=w^2/4-1/m\), \(a=y_0\) and \(b=1/m+\delta-a\). The event \(W_m\le w\) is \(y_j\le b\) for all \(j\ge1\). For given \(a\), set \(z_j=b-y_j\). These variables are nonnegative and sum to \(m\delta-(m-1)a\); nonempty sections require \(0\le a\le m\delta/(m-1)\). For fixed \(m\) and small enough \(\delta>0\) the resulting full simplex of \(z_j\)'s is allowed: uniformly in it, every \(y_j\) for \(j\ge1\) is \(1/m+O_m(\delta)>0\). The coordinate volume of this simplex, using \(z_1,\ldots,z_{m-1}\), is \([m\delta-(m-1)a]^{m-1}/(m-1)!\). The coordinate Jacobian has absolute value one. Thus
\[
\begin{aligned}
\Pr(W_m\le w)
 &=\frac{C_m m^{m/2}}{(m-1)!}(1+O_m(\delta))
   \int_0^{m\delta/(m-1)} a^{-1/2}[m\delta-(m-1)a]^{m-1}\,da\\
 &=\frac{\Gamma((m+1)/2)m^{(3m-1)/2}}{\pi^{m/2}\sqrt{m-1}\,\Gamma(m+1/2)}
   \delta^{m-1/2}(1+O_m(\delta)).
\end{aligned}
\]
The second equality uses the beta integral with parameters \((1/2,m)\). Substitution of \(\delta=\varepsilon/\sqrt m+\varepsilon^2/4\) proves the lower-edge result.

**Upper edge.** Put \(\eta=1-(2-\varepsilon)^2/4\). Then \(W_m>2-\varepsilon\) is the union over \(j\ge1\) of \(E_j=\{\sum_{k\ge1,\ k\ne j}Y_k<\eta\}\). Each sum has law \(\operatorname{Beta}((m-1)/2,1)\), so \(\Pr(E_j)=\eta^{(m-1)/2}\). If two different events hold, then \(\sum_{k\ge1}Y_k<2\eta\); the latter sum has law \(\operatorname{Beta}(m/2,1/2)\) and lower-tail probability \(O_m(\eta^{m/2})\). The union bound and the first pairwise correction bound the union probability by \(m\eta^{(m-1)/2}+O_m(\eta^{m/2})\). Use \(\eta=\varepsilon-\varepsilon^2/4\).

## Comparisons and prior work

Finch's centered example [1] is \(m=2\) and gives the same body and support computation, including its mean width. For this case, \(W_2\le w\) is \(\{|U_1|\ge s,|U_2|\ge s\}\) with \(s=\sqrt{1-w^2/4}\). This consists of four congruent spherical lenses, each the intersection of two equal caps with angular radius \(\arccos s\) whose axes are separated by \(\pi/2\). In Mazonka's cap-intersection formula [2, §4.3, Eq. (45)], each segment uses bisector angle \(\pi/4\), giving lens area \(4[\arccos(1/\sqrt{2(1-s^2)})-s\arccos(s/\sqrt{1-s^2})]\). Dividing by \(\pi\) for the four lenses gives the CDF on \([\sqrt2,2]\); its first inverse cosine equals \(\arctan\sqrt{1-2s^2}\). The density and two-disk edges follow from this CDF. The formulas above also extend to \(m=2\) as a consistency check. Neither this specialization nor its derived moments are claimed as new.

For comparison, a growing-dimensional width limit follows from the Dirichlet-maximum theorem of Bose, Dasgupta and Maulik [3, Corollary 3.1, Eqs. (36)–(37)]. Let \(a_m=2\log m-\log\log m-\log\pi\) and \(M_m=\max_{1\le j\le m}Y_j\). With transverse and extra shape parameters both \(1/2\), the cited corollary gives \((m+1)M_m/2-a_m/2\Rightarrow G\), a standard Gumbel limit. The normalized transverse vector is Dirichlet with parameters \(1/2\) and independent of \(Y_0\) by the independent-gamma representation, so \(M'_m=M_m/(1-Y_0)\) is independent of \(Y_0\). Also \(mY_0\Rightarrow Z^2\) for a standard normal \(Z\), by the Gaussian-sphere representation. Thus \(M'_m=o_{\Pr}(1)\), \(mY_0M'_m=o_{\Pr}(1)\), and \(mM'_m/2-a_m/2\Rightarrow G\). Joint convergence using independence gives
\[
\frac{mW_m^2/4-a_m}{2}\Longrightarrow G+Z^2/2,
\]
with independent terms. This is a separate limiting regime from the endpoint results.

The higher-dimensional coordinate-hyperdisk hull [4] uses disks of codimension one rather than two-dimensional disks sharing one diameter. Its extremal coordinate is the **minimum** of all squared coordinates, unlike the distinguished square plus transverse **maximum** here. Its endpoint laws therefore do not specialize to the two fixed-dimensional laws above. Setting the separation to zero in the two-disk crossover studies [5] also gives the narrow-edge coefficient for the comparison case \(m=2\), not for the retained \(m\ge3\) family. More general spherical or Dirichlet order-statistic formulas may give other representations; no claim of historical priority is made beyond the distinctions supported by these comparisons.

## Reproducibility and scope

The analytic proof supplies the exact coefficients and error estimates. The accompanying `verify_width.py` (Python 3, NumPy, SciPy) is a numerical diagnostic, including transformed-simplex checks in \(m=2,3,4\) and checks of the comparison laws. It does not prove the infinite claims. The result assumes equal disks, a single common diameter and mutually orthogonal transverse directions; it does not give an elementary CDF in every dimension.

## References

1. S. R. Finch, *Convex Hull of Two Orthogonal Disks*, arXiv:1211.4514, first posted 2012-11-19, §§1–1.2, https://arxiv.org/pdf/1211.4514.
2. O. Mazonka, *Solid Angle of Conical Surfaces, Polyhedral Cones, and Intersecting Spherical Caps*, arXiv:1205.1396, 2012, §4.3, Eq. (45), https://arxiv.org/pdf/1205.1396.
3. A. Bose, A. Dasgupta and K. Maulik, *Maxima of Dirichlet and triangular arrays of gamma variables*, arXiv:0803.3518, §3, especially Corollary 3.1, https://arxiv.org/pdf/0803.3518.
4. *Exact random widths of the orthogonal three-disk hull and sharp hyperdisk endpoint laws* (2026-11-08), record d1df18476a61.
5. *A singular crossover in near-minimal random widths of two orthogonal disks*, record a276467e90bf, and *Singular near-minimum width crossover for two separated orthogonal disks*, record 478c8834f500 (both 2026-11-22).
