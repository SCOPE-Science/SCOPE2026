# A sharp radial Riesz-kernel refinement of the Schatten circular-mean inequality
## Finding
For every complex Hilbert space \(H\), every \(0<p\le 2\), every \(A,B\in S_p(H)\), and every \(t>0\), define
\[
M_p(A,B;t)=\frac{1}{2\pi}\int_0^{2\pi}\|A+t e^{i\theta}B\|_p^p\,d\theta,
\]
and put \(a=\|A\|_{\mathrm{op}}\), \(b=\|B\|_{\mathrm{op}}\). Then
\[
M_p(A,B;t)-\|A\|_p^p
\ge
p^2\|B\|_2^2
\int_0^t s(a+bs)^{p-2}\log\!\frac{t}{s}\,ds.
\]
When \(a=0\), the integrand is understood by its integrable value on \((0,t]\).

If \(0<p<2\) and \(B\ne0\), this is strictly stronger than the radius-frozen estimate
\[
\frac{p^2}{4}t^2\|B\|_2^2(a+bt)^{p-2},
\]
because \(p-2<0\) and
\[
\int_0^t s\log\!\frac{t}{s}\,ds=\frac{t^2}{4}.
\]
At \(p=2\), the new bound is the exact identity
\[
M_2(A,B;t)-\|A\|_2^2=t^2\|B\|_2^2.
\]
If \(A=0\) and \(B\) has rank one, the new lower bound is also an equality for every \(0<p\le2\) and every \(t>0\). Thus its coefficient and radial kernel cannot be uniformly increased.

## Assumptions and scope
The result concerns complex Schatten classes on an arbitrary Hilbert space. No self-adjointness, positivity, finite-rank hypothesis, or invertibility is assumed. The only exponent restriction is \(0<p\le2\). The statement is a circular-mean inequality along the affine complex line \(A+zB\); it does not classify Schatten embeddings and does not assert an upper bound for the circular mean.

The recent input is the regularized complex-Hessian estimate of Xu, Zhang, and Liu for
\[
F_\varepsilon(X)=\operatorname{Tr}(X^*X+\varepsilon I)^{p/2}.
\]
For \(r=p/2\), their Proposition 2.2 gives
\[
\partial_z\partial_{\bar z}F_\varepsilon(X+zB)\big|_{z=0}
\ge
r^2(\|X\|_{\mathrm{op}}^2+\varepsilon)^{r-1}\|B\|_2^2.
\]

## Proof
First suppose \(H\) is finite-dimensional. Apply the quoted Hessian estimate at each point \(w\) of the scalar disk to the pencil
\[
z\longmapsto A+wB+zB.
\]
Since \(r-1\le0\) and
\[
\|A+wB\|_{\mathrm{op}}\le a+|w|b,
\]
we obtain
\[
\partial_w\partial_{\bar w}F_\varepsilon(A+wB)
\ge
\frac{p^2}{4}
\bigl((a+|w|b)^2+\varepsilon\bigr)^{p/2-1}
\|B\|_2^2.
\]

For a smooth subharmonic function on the disk, the Poisson--Jensen/Green identity gives
\[
\frac{1}{2\pi}\int_0^{2\pi}F_\varepsilon(A+t e^{i\theta}B)\,d\theta
-F_\varepsilon(A)
=
\frac{2}{\pi}
\int_{|w|<t}
\log\!\frac{t}{|w|}
\,\partial_w\partial_{\bar w}F_\varepsilon(A+wB)\,dA(w).
\]
Insert the radial lower bound and pass to polar coordinates. The constants combine exactly to give
\[
\frac{1}{2\pi}\int_0^{2\pi}F_\varepsilon(A+t e^{i\theta}B)\,d\theta
-F_\varepsilon(A)
\ge
p^2\|B\|_2^2
\int_0^t
s\bigl((a+bs)^2+\varepsilon\bigr)^{p/2-1}
\log\!\frac{t}{s}\,ds.
\]
As \(\varepsilon\downarrow0\), the function values converge to the Schatten \(p\)-powers, while the right-hand integrand increases pointwise to
\[
s(a+bs)^{p-2}\log\!\frac{t}{s}.
\]
Monotone convergence therefore yields the stated finite-dimensional inequality.

For arbitrary \(H\), choose increasing finite-rank orthogonal projections \(P_N\to I\) strongly and apply the finite-dimensional result to
\[
A_N=P_NAP_N,\qquad B_N=P_NBP_N.
\]
We have \(A_N\to A\) and \(B_N\to B\) in \(S_p\), hence \(B_N\to B\) in \(S_2\), while
\[
\|A_N\|_{\mathrm{op}}\le a,\qquad \|B_N\|_{\mathrm{op}}\le b.
\]
Using the larger fixed radial envelope \(a+bs\) preserves the finite-dimensional lower bound. Passing to the limit in the circular means and in \(\|B_N\|_2\) proves the claim.

For strict improvement when \(0<p<2\) and \(B\ne0\), note that \(b>0\) and
\[
(a+bs)^{p-2}>(a+bt)^{p-2}
\]
for every \(0<s<t\). Multiplying by the positive kernel \(s\log(t/s)\) and integrating gives the strict comparison with the frozen-radius estimate.

Finally, if \(A=0\), then
\[
p^2\int_0^t s(bs)^{p-2}\log\!\frac{t}{s}\,ds
=t^p b^{p-2},
\]
because
\[
\int_0^1 u^{p-1}\log\!\frac{1}{u}\,du=\frac{1}{p^2}.
\]
For rank-one \(B\), \(\|B\|_p^p=\|B\|_2^2b^{p-2}\), so both sides equal \(t^p\|B\|_p^p\).

## Verification
The proof was checked at the three places where normalization errors are most likely. First, the complex Laplacian convention contributes the factor \(2/\pi\) in Poisson--Jensen; combined with the Hessian coefficient \(p^2/4\) and the angular integral \(2\pi\), it gives exactly the coefficient \(p^2\) in the radial integral. Second, freezing \((a+bs)^{p-2}\) at \(s=t\) recovers the published coefficient \(p^2/4\), because the logarithmic kernel has moment \(t^2/4\). Third, on a rank-one ray from the origin the integral evaluates exactly to the left-hand side, certifying sharpness without numerical approximation.

The infinite-dimensional passage uses only finite-rank compression, Schatten convergence, and operator-norm contraction under orthogonal compression. No finite experiment is used as evidence for the infinite-dimensional statement.

## Relationship to prior work
Xu, Zhang, and Liu prove the pointwise regularized Hessian estimate and then replace the operator norm on the whole disk by the outer-radius envelope \(a+tb\), obtaining their Theorem 3.1. The present result keeps the radius \(s\) inside the Green integral instead of freezing it. Their displayed circular-mean theorem therefore follows immediately from the new inequality, and is strictly weaker at every finite radius when \(0<p<2\) and \(B\ne0\).

Blower and Ransford developed the Riesz-measure/Poisson--Jensen framework for Schatten trace ideals and, for \(1\le p\le2\), proved a different local density lower bound involving the Schatten \(p\)-norm of \(A+zB\) and the coefficient \(p^2/8\). That result supplies the classical integration framework but does not contain the operator-norm/Hilbert--Schmidt radial bound above, does not cover \(0<p<1\), and is not sharp on the rank-one rays used here.

## Limitations
No converse or upper estimate is claimed. The result does not determine optimal embedding distortion in any target dimension. The sharpness statement is global in the sense that the lower bound is attained on rank-one rays from the origin; it does not classify every equality case. An older equivalent formulation could exist under Riesz-measure or PL-convexity terminology, although targeted statement-level searches and inspection of the closest classical source did not locate one.

## References
1. Ying Xu, Wenwen Zhang, Qi Liu, *Further Results on the Isometric Embeddability of \(S_q^m\) into \(S_p^n\)*, arXiv:2609.37504v1, 2026. Proposition 2.2 and Theorem 3.1.
2. Gordon Blower, Thomas Ransford, *Complex Uniform Convexity and Riesz Measures*, Canadian Journal of Mathematics 56 (2004), 225--245, DOI 10.4153/CJM-2004-011-3. Proposition 1.1 and Theorem 3.6.
