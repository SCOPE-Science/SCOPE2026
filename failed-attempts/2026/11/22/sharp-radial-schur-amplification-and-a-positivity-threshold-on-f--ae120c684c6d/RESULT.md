# Sharp radial Schur amplification and a positivity threshold on finite and infinite stars

## Finding

Let \(K_{1,n}\) be the star with a central vertex and \(n\geq1\) leaves. For real \(t\), let \(\mathcal S_{n,t}\) be the Schur multiplier on complex \((n+1)\)-by-\((n+1)\) matrices whose radial symbol is \(m(0)=1\), \(m(1)=t\), and \(m(2)=0\), where the argument is graph distance. Write \(T=|t|\). Then the ordinary operator-to-operator norm and completely bounded norm coincide, with **exact sharp value**

\[
\|\mathcal S_{n,t}\|_{B\to B}=\|\mathcal S_{n,t}\|_{\mathrm{cb}}=
\begin{cases}
1,&0\leq T\leq1/\sqrt n,\\[2mm]
1+\dfrac{2(nT^2-1)}{2nT+n+1},&T>1/\sqrt n.
\end{cases}
\]

The multiplier is contractive if and only if it is completely positive, which occurs exactly for \(nT^2\leq1\). For each finite \(n\), its norm is continuous but not differentiable at \(T=1/\sqrt n\): the right slope is \(4\sqrt n/(1+\sqrt n)^2\) and the left slope vanishes.

For the countably infinite star (one center and countably many leaves), the same radial symbol defines a bounded Schur multiplier on \(B(\ell^2)\) with

\[
\|\mathcal S_{\infty,t}\|_{B\to B}=\|\mathcal S_{\infty,t}\|_{\mathrm{cb}}
=1+\frac{2T^2}{2T+1}.
\]

Thus on the infinite star, contractivity is possible exactly for \(t=0\). The \(t=1\) case is a previously known radius-one star projection norm, not a new subclaim.

## Assumptions and scope

All entries and operators are complex, although the radial parameter \(t\) is real. The operator norm is induced by the Hilbert-space operator norm, and the completely bounded norm is the supremum over spatial matrix amplifications. Both diagonal and leaf-diagonal entries receive multiplier \(1\). Only hub-to-leaf entries receive \(t\); all off-diagonal entries between different leaves are discarded. For \(n=1\), there is no distance-two pair. The infinite-star multiplier is understood as a normal map on \(B(\ell^2(\{0\}\cup\mathbb N))\), not as a finite-matrix limit alone. No claim is made for complex radial \(t\), arbitrary trees, or intermediate Schatten exponents.

## Proof

**Reduction to \(t\geq0\).** Replacing the central coordinate by its negative conjugates the symbol with parameter \(T\) to that with parameter \(-T\). More explicitly, if \(U=\operatorname{diag}(-1,1,\ldots)\), then \(\mathcal S_{n,-T}(X)=U\mathcal S_{n,T}(X)U^*\). Both norms are therefore invariant under the sign of \(t\), in finite and infinite dimensions.

**Contractive branch.** The real symmetric symbol matrix \(M\) has eigenvalue \(1\) on the \((n-1)\)-dimensional leaf-difference space, while its restriction to the plane spanned by the hub and normalized leaf-average vector is

\[
\begin{pmatrix}1&\sqrt nT\\\sqrt nT&1\end{pmatrix}.
\]

Consequently \(M\succeq0\) precisely when \(nT^2\leq1\). A Schur multiplier with positive semidefinite symbol is completely positive; its completely bounded norm is the maximum diagonal symbol entry, here \(1\). Evaluation on the identity matrix gives the reverse operator-norm inequality. This proves the first branch and characterizes complete positivity.

**Finite-star upper bound beyond the threshold.** Suppose \(nT^2>1\) and set

\[
D=2nT+n+1,\qquad d=\frac{2(nT^2-1)}D>0,\qquad s=1+d.
\]

Construct a symmetric matrix \(H\) with every diagonal entry \(s\), every hub–leaf entry \(T-d\), and every distinct-leaf entry \(d\). We claim \(H+M\succeq0\) and \(H-M\succeq0\). On the leaf-difference subspace their eigenvalues are respectively \(2\) and \(0\). On the hub/leaf-average plane they have representations

\[
H+M:\ \begin{pmatrix}d+2&\sqrt n(2T-d)\\\sqrt n(2T-d)&nd+2\end{pmatrix},
\qquad
H-M:\ \begin{pmatrix}d&-\sqrt n d\\-\sqrt n d&nd\end{pmatrix}.
\]

Every diagonal entry is nonnegative; the two determinants vanish because

\[
(d+2)(nd+2)=n(2T-d)^2,\qquad d(nd)=n d^2.
\]

The first identity follows by substituting the displayed rational formula for \(d\), and the second is immediate. Both matrices are therefore positive semidefinite. Let \(Q_\pm=(H\pm M)/2\). Their Schur maps are completely positive and have completely bounded norms equal to their constant diagonal entries \((s\pm1)/2\). Since \(M=Q_+-Q_-\), the completely bounded norm of its Schur map is at most \((s+1)/2+(s-1)/2=s\).

**Matching finite-star lower bound.** Put

\[
q=\frac{nT+1}{D},\qquad r=\frac{T+1}{D},\qquad q+nr=1,
\]

and let \(u=(\sqrt q,\sqrt r,\ldots,\sqrt r)\), a unit vector. Define \(B=\operatorname{diag}(u)M\operatorname{diag}(u)\). On the leaf-difference space, \(B\) has eigenvalue \(r\) of multiplicity \(n-1\). On the hub/leaf-average plane, it is

\[
\begin{pmatrix}q&T\sqrt{nqr}\\T\sqrt{nqr}&r\end{pmatrix}.
\]

The identity \((q-r)^2+4nT^2qr=T^2\) gives the two remaining eigenvalues \((q+r+T)/2\) and \((q+r-T)/2\). The latter is exactly \(-(nT^2-1)/D<0\). Hence the trace norm equals

\[
\|B\|_{S_1}=(n-1)r+T=1+d=s.
\]

Choose the self-adjoint contraction \(X=\operatorname{sgn}(B)\), assigning sign zero to a null eigenvalue. Because \(M\) is real symmetric,

\[
\langle\mathcal S_{n,T}(X)u,u\rangle
=\operatorname{Tr}(BX)=\|B\|_{S_1}=s.
\]

Thus the ordinary operator norm is at least \(s\), matching the completely bounded upper bound and proving the exact finite-star formula. This proof also covers \(n=1\).

**Countably infinite star.** For \(T>0\) define \(d_\infty=2T^2/(2T+1)\), \(s_\infty=1+d_\infty\), and a bounded symmetric kernel \(H\) with diagonals \(s_\infty\), hub–leaf entries \(T-d_\infty\), and distinct-leaf entries \(d_\infty\). Let \(w=(1,-1,-1,\ldots)\) and \(v=(\sqrt{d_\infty+2},\sqrt{d_\infty},\sqrt{d_\infty},\ldots)\). As kernels (not necessarily rank-one bounded operators),

\[
H-M=d_\infty ww^*,\qquad
H+M=vv^*+2\operatorname{diag}(0,1,1,\ldots).
\]

The second identity uses \((2T-d_\infty)^2=d_\infty(d_\infty+2)\) with \(2T-d_\infty>0\). These kernels generate normal completely positive Schur maps through bounded diagonal multipliers and diagonal expectation, with completely bounded norms determined by their diagonal entries. Consequently \(\|\mathcal S_{\infty,T}\|_{\mathrm{cb}}\leq s_\infty\). Restriction to the first \(n\) leaves has norm given by the finite-star formula, converging to \(s_\infty\) as \(n\to\infty\), and therefore supplies the matching ordinary operator-norm lower bound. The case \(T=0\) is the diagonal conditional expectation and has norm one.

**Threshold cusp.** On the strict supercritical branch, differentiating \(2(nT^2-1)/(2nT+n+1)\) at its positive endpoint \(T=n^{-1/2}\) gives right derivative \(4\sqrt n/(1+\sqrt n)^2\). The subcritical branch is constant, proving the claimed nondifferentiability.

## Verification

The standalone exact-arithmetic script `checks/weighted_star_check.py` verifies the two upper-certificate determinants, witness discriminant, negative eigenvalue, trace-norm identity, and the known \(T=1\) specialization on 2,560 prescribed rational cases and 7,000 seeded rational cases. It also verifies the infinite-kernel factorization identity on 999 positive rational parameter values. The output is `WEIGHTED_STAR_EXACT_IDENTITIES_OK 10559`. Finite arithmetic assertions are supplementary; the universal proof, including all real parameters and the infinite star, is given above.

## Relationship to prior work

González-Pérez, Parcet, Pérez García and Wang (first public version 2026-10-11) study radial Schur multipliers on trees primarily for intermediate Schatten exponents and their relationship to Fourier multipliers. Arhancet (first public version 2026-10-22) develops further Fourier–Schur comparison and the distinction between ordinary and completely bounded radial multiplier norms. Neither of these inspected accounts states this exact weighted finite/infinite-star endpoint phase diagram.

The published result *Exact endpoint Schur norms of radius-one balls on stars of arbitrary degree* determines the special case \(T=1\) as \((5n-1)/(3n+1)\), and its infinite-star value as \(5/3\). Substituting \(T=1\) here recovers exactly those known values, but that case alone does not determine the variable-\(T\) threshold, nonlinear supercritical branch or countable-star parameter law. In particular, affine interpolation between the known \(T=0\) and \(T=1\) symbols gives at most an upper estimate for intermediate parameters; it cannot imply the sharp zero-growth plateau followed by a rational growth branch.

Christensen (2025) supplies a general dual characterization of norms of self-adjoint Schur multipliers. The upper-positive-kernel and lower-trace-norm techniques used here belong to established Schur multiplier theory; the contribution is the matching parameter-dependent certificates and exact norm evaluation for this particular natural radial family. Levene (2014) computed the three-vertex projection value \(9/7\), recovered when \(n=2\), \(T=1\).

## Limitations

The sharp formula is proved for real radial multipliers supported at distances zero and one on stars, not for complex parameters, arbitrary trees or all intermediate Schatten classes. It does not assert priority for \(T=1\) or for the general positive-Schur decomposition and dual trace-norm principles. General factorization methods and older indexed or unindexed graph-pattern literature may encode an equivalent variable-parameter formula; bibliographic priority has not been independently certified. The supplied arithmetic checks do not replace the all-parameter proof, and no independent mathematical audit has been performed.

## References

1. A. González-Pérez, J. Parcet, J. Pérez García, S. Wang, *Radial Schur multipliers on trees and the failure of Fourier–Schur transference*, arXiv:2610.15881v1, first public 2026-10-11, https://arxiv.org/abs/2610.15881.
2. C. Arhancet, *Radial Schur multipliers on trees and quantitative Fourier–Schur separation*, arXiv:2610.30832v1, first public 2026-10-22, https://arxiv.org/abs/2610.30832.
3. *Exact endpoint Schur norms of radius-one balls on stars of arbitrary degree*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-endpoint-schur-norms-of-radius-one-balls-on-stars-of-arbit--708bab8a17cc.
4. E. Christensen, *The Schur multiplier norm and its dual norm*, arXiv:2505.24670v1 (2025), https://arxiv.org/abs/2505.24670.
5. R. H. Levene, *Norms of idempotent Schur multipliers*, New York Journal of Mathematics 20 (2014), 325–352, https://nyjm.albany.edu/j/2014/20-19.html.
