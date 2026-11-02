# Exact quadratic isosceles-orthogonality profile of the regular octagonal plane
## Finding
Let \(X_8=(\mathbb R^2,N)\) with
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For \(0\le \alpha<1\), let Yang--Li's quadratic isosceles-orthogonality constant be
\[
\Omega_{X_8}(\alpha)=\sup_{x\perp_I y,\,(x,y)\ne(0,0)}
\frac{N(\alpha x+y)^2+N(x+\alpha y)^2}{N(x+y)^2}.
\]
Put
\[
\alpha_0=3-2\sqrt2,\qquad \alpha_1=\frac{2\sqrt2-1}{7}.
\]
Then
\[
\Omega_{X_8}(\alpha)=
\begin{cases}
4-2\sqrt2,&0\le \alpha\le \alpha_0,\\[3pt]
\dfrac{\alpha^2+2(\sqrt2-1)\alpha+5-2\sqrt2}{2},&\alpha_0\le \alpha\le \alpha_1,\\[7pt]
1+2(\sqrt2-1)\alpha+(3-2\sqrt2)\alpha^2,&\alpha_1\le \alpha<1.
\end{cases}
\]
Thus the profile has a nontrivial plateau near \(\alpha=0\), followed by two algebraic branches. The corresponding maximizing unit-vector geometry changes at \(\alpha_1\); a separate support change inside the adjacent-vertex branch occurs at \(\alpha_0\).

Equivalently, for Yang--Li's auxiliary function
\[
\gamma_{X_8}(t)=\sup_{x,y\in S_{X_8}}
\frac{N(x+ty)^2+N(x-ty)^2}{2},\qquad 0\le t\le1,
\]
one has
\[
\gamma_{X_8}(t)=
\begin{cases}
\bigl(1+(\sqrt2-1)t\bigr)^2,&0\le t\le2-\sqrt2,\\[3pt]
1+(2-\sqrt2)(t+t^2),&2-\sqrt2\le t\le1/\sqrt2,\\[3pt]
(2-\sqrt2)(1+t)^2,&1/\sqrt2\le t\le1.
\end{cases}
\]

## Assumptions and scope
The scalar field is real. The norm above is a standard realization of the regular octagonal Banach plane. Isosceles orthogonality means \(x\perp_I y\) when \(N(x+y)=N(x-y)\). The parameter range is the one used in the defining Yang--Li constant, \(0\le\alpha<1\).

The proof uses Yang--Li's published identity
\[
\Omega_X(\alpha)=\frac{(1+\alpha)^2}{2}\,
\gamma_X\!\left(\frac{1-\alpha}{1+\alpha}\right),
\]
so the substantive new calculation is the complete exact \(\gamma_{X_8}\)-profile.

## Proof
Write \(r=\sqrt2-1\). The octagonal unit ball has vertices
\[
v_0=(1,r),\ v_1=(r,1),\ v_2=(-r,1),\ v_3=(-1,r),
\]
together with their negatives. For fixed \(t\), the objective defining \(\gamma_{X_8}(t)\) is convex in each of \(x\) and \(y\) separately on the unit ball. Maximizing first in one variable and then the other therefore reduces the ball maximum to vertex pairs. Since vertices belong to the unit sphere, this ball maximum equals the sphere supremum. Dihedral symmetry fixes the first vertex as \(v_0\), leaving separations \(k=0,1,2,3,4\).

For \(k=0,4\), direct evaluation gives
\[
F_0(t)=1+t^2.
\]
For the two-edge pair \((v_0,v_2)\), both deformed vectors have norm \(1+rt\), hence
\[
F_2(t)=(1+rt)^2.
\]
For an adjacent pair \((v_0,v_1)\), the active support of one deformed vector changes at \(t=1/\sqrt2\). Exact support evaluation gives
\[
F_1(t)=
\begin{cases}
1+(2-\sqrt2)(t+t^2),&0\le t\le1/\sqrt2,\\[3pt]
(2-\sqrt2)(1+t)^2,&1/\sqrt2\le t\le1.
\end{cases}
\]
The three-edge pair gives the same values by symmetry.

It remains to take the envelope. On the first adjacent-support interval,
\[
F_1(t)-F_2(t)=(\sqrt2-1)t\bigl(t-(2-\sqrt2)\bigr).
\]
Also
\[
F_2(t)-F_0(t)=2(\sqrt2-1)t(1-t)\ge0.
\]
Therefore \(F_2\) is maximal up to \(t=2-\sqrt2\), and \(F_1\) is maximal thereafter on the first support interval. On \([1/\sqrt2,1]\), the difference between the second branch of \(F_1\) and \(F_2\) is already positive at \(1/\sqrt2\), and its derivative is
\[
2(\sqrt2-1)t+6-4\sqrt2>0.
\]
The difference from \(F_0\) is likewise positive there. This proves the displayed three-branch formula for \(\gamma_{X_8}\).

Finally put \(t=(1-\alpha)/(1+\alpha)\). The support-change point \(t=1/\sqrt2\) becomes
\[
\alpha_0=3-2\sqrt2,
\]
and the envelope-change point \(t=2-\sqrt2\) becomes
\[
\alpha_1=\frac{2\sqrt2-1}{7}.
\]
Substitution into Yang--Li's identity gives the three displayed branches of \(\Omega_{X_8}(\alpha)\). The formulas agree at both breakpoints and tend to \(2\) as \(\alpha\to1^-\).

## Verification
The accompanying `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt2)\) through SymPy. It checks that every listed vertex is on the unit sphere; certifies the active support on each of seven affine support intervals by endpoint inequalities; reconstructs all candidate quadratics; verifies the exact envelope factorizations and threshold order; performs the parameter change from \(t\) to \(\alpha\); and checks continuity at both breakpoints and the limiting endpoint. A successful run prints `VERIFY_OK`.

The checker is auxiliary. The infinite optimization is justified by the separate-convexity vertex reduction and the exact interval arguments above, not by finite numerical sampling.

## Relationship to prior work
Yang and Li introduced \(\Omega_X(\alpha)\), proved the identity with \(\gamma_X\), and calculated several classical examples, including \(\ell_1\), \(\ell_\infty\), \(\ell_p\) in a stated range, and two mixed two-dimensional spaces. Their full article contains no regular-octagon calculation.

The closest located exact result for this same octagonal norm is the parameterized modified von Neumann--Jordan profile
\[
C'_{\mathrm{NJ}}(\lambda,X_8)=\sup_{x,y\in S_{X_8}}
\left(N(\lambda x+(1-\lambda)y)^2+\lambda(1-\lambda)N(x-y)^2\right).
\]
That functional is not \(\gamma_{X_8}(t)\): it has a convex-combination term and a separately weighted difference term, whereas \(\gamma\) averages the two symmetric deformations \(x\pm ty\). At the symmetric endpoint there is a normalization relation, but the full parameterized statement does not imply the three-branch \(\gamma\)-profile or the resulting \(\Omega\)-profile.

Targeted searches for the regular-octagon \(\Omega_X\) profile, the exact \(\gamma_{X_8}(t)\) profile, the two breakpoints, and equivalent isosceles-orthogonality formulations did not locate a covering result. This search evidence is not treated as a proof of novelty; the main originality comparison is statement-level comparison with the defining full text and the closest exact octagonal profile.

## Limitations
The theorem is restricted to one real two-dimensional polyhedral Banach space and Yang--Li's parameter interval. It does not classify \(\Omega_X\) for arbitrary regular polygons or arbitrary Banach spaces. The bibliographic search cannot exclude every unindexed or differently phrased source, although the defining article, its concrete examples, targeted web searches, and the closest structured-result records were checked.

## References
1. Z. Yang and Y. Li, “A New Geometric Constant in Banach Spaces Related to the Isosceles Orthogonality,” Kyungpook Mathematical Journal 62 (2022), 271–287. DOI: 10.5666/KMJ.2022.62.2.271. Published online 30 June 2022.
2. MaRDI/zbMATH metadata for the preceding article, recording MSC 46B20 (Geometry and structure of normed linear spaces), MaRDI Q5093374.
3. Y. Wang et al., “Novel constants based on the generalization of Von Neumann-Jordan constant,” arXiv:2110.15741, for the distinct parameterized modified von Neumann–Jordan functional used in the closest comparison.
