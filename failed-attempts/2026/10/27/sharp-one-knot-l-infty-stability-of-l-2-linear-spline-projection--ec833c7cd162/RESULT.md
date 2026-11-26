# Sharp one-knot \(L^\infty\) stability of \(L^2\) linear-spline projection

## Finding
For every \(a\in(0,1)\), let \(P_a\) project orthogonally in \(L^2[0,1]\) onto the continuous functions that are affine on \([0,a]\) and \([a,1]\). With \(h=\min\{a,1-a\}\), its exact bounded-input amplification is
\[\boxed{\|P_a\|_{L^\infty\to L^\infty}=1+\frac4{3(1+h)}.}\]
The balanced knot uniquely minimizes the norm, with value \(17/9\). The supremum over interior knots is \(7/3\), approached at either boundary but never reached. At each fixed interior knot, a measurable sign-valued function attains the sharp operator norm.

For measurable inputs \(0\le f\le1\), the exact global least fitted value is
\[\boxed{\inf_{0\le f\le1}\min_{x\in[0,1]}(P_af)(x)=-\frac2{3(1+h)}.}\]
A characteristic function attains this minimum; smooth inputs taking values strictly between zero and one can still give a negative fitted value.

There is a singular stability boundary: as \(a\) tends to either endpoint, \(P_a\) converges strongly in \(L^2\) to the global-affine projector \(P_{\mathrm{aff}}\), but the sharp \(L^\infty\) norms tend to \(7/3\), whereas \(\|P_{\mathrm{aff}}\|_{\infty\to\infty}=5/3\).

## Assumptions and scope
All functions and projections are real-valued; identical constants hold for complex-valued inputs because the reproducing kernels are real and sign witnesses suffice. The interval carries Lebesgue measure. The sole interior knot obeys \(0<a<1\); no quasi-uniformity assumption is made. Let
\[S_a=\{s\in C[0,1]:s|_{[0,a]}\text{ and }s|_{[a,1]}\text{ are affine}\}.\]
The \(L^2\)-orthogonal projector is extended from \(L^2\) to \(L^\infty\) using its bounded integral kernel; output functions have continuous representatives, so point evaluation is unambiguous. The \(L^\infty\) norm is the essential supremum of the input and the ordinary supremum of the continuous output. Boundary knots \(a=0,1\) are not part of the three-dimensional family.

## Proof
**1. Reproducing kernel.** Use the nodal hat basis \(N_0,N_a,N_1\), whose nodal values are respectively the coordinate vectors at \(0,a,1\). The Gram matrix is
\[G_a=\frac16\begin{pmatrix}2a&a&0\\a&2&1-a\\0&1-a&2(1-a)\end{pmatrix}.\]
Its determinant is \(a(1-a)/36>0\). Writing \(N(x)=(N_0(x),N_a(x),N_1(x))^T\), the reproducing kernel is
\[K_a(x,y)=N(x)^TG_a^{-1}N(y),\qquad (P_af)(x)=\int_0^1K_a(x,y)f(y)\,dy.\]
Because \(1\in S_a\), its row integral equals \(1\): \(\int_0^1K_a(x,y)\,dy=1\).

**2. Reduction to three output points.** For fixed \(y\), \(K_a(x,y)\) is affine in \(x\) on each of \([0,a]\) and \([a,1]\). Thus \(x\mapsto\int_0^1|K_a(x,y)|\,dy\) is convex separately on these intervals. Its global maximum is one of the rows at \(x=0,a,1\).

**3. Exact rows.** Direct inversion of \(G_a\) gives
\[K_a(1,y)=\begin{cases}
1-3y/a,&0\le y\le a,\\
-2+\dfrac{3(2-a)}{(1-a)^2}(y-a),&a\le y\le1.
\end{cases}\]
The left piece crosses zero at \(y=a/3\). The right piece crosses zero at
\[y=a+\frac{2(1-a)^2}{3(2-a)},\]
which lies strictly between \(a\) and \(1\). Integrating absolute values exactly,
\[\int_0^a|K_a(1,y)|\,dy=\frac{5a}{6},\]
\[\int_a^1|K_a(1,y)|\,dy=1+\frac a2+\frac{4(1-a)^2}{3(2-a)}.\]
Consequently
\[\int_0^1|K_a(1,y)|\,dy=1+\frac4{3(2-a)}.\]
Reflection \(x\mapsto1-x\) yields
\[\int_0^1|K_a(0,y)|\,dy=1+\frac4{3(1+a)}.\]
At the knot,
\[K_a(a,y)=\begin{cases}-2+6y/a,&0\le y\le a,\\-2+6(1-y)/(1-a),&a\le y\le1,\end{cases}\]
so \(\int_0^1|K_a(a,y)|\,dy=5/3\). Both endpoint-row norms are strictly larger than \(5/3\). Taking their maximum and simplifying the smaller denominator gives the claimed formula.

**4. Extremizers, knot balance and range defect.** For a row maximizing the absolute integral, choose \(f(y)=\operatorname{sgn}K_a(x_*,y)\); equality in the operator norm follows. Since \(\int K_a(x,y)\,dy=1\), the least possible value of \(\int K_a(x,y)f(y)\,dy\) for \(0\le f\le1\) equals \((1-\int|K_a(x,y)|\,dy)/2\). Choosing \(f=\boldsymbol1_{\{K_a(x_*,\cdot)<0\}}\) establishes the sharp negativity constant. Approximation in \(L^1\) by smooth functions with \(\epsilon\le f\le1-\epsilon\), taking sufficiently small \(\epsilon>0\), preserves a negative fitted value because the kernel is bounded for fixed \(a\). The quantity \(h\) is largest precisely at \(a=1/2\) and approaches zero only at the endpoints; the minimum, unattained uniform supremum, and all claimed endpoint values follow.

**5. Strong \(L^2\) convergence but discontinuous \(L^\infty\) constants.** Denote the global affine subspace by \(E\). When \(a\to0\), \(S_a=E+\operatorname{span}\{v_a\}\), where \(v_a(y)=(a-y)_+\). The normalized component of \(v_a\) perpendicular to \(E\) has norm \(1\). Since \(\|v_a\|_2=a^{3/2}/\sqrt3\) and \(\|P_Ev_a\|_2=O(a^2)\), that normalized component is asymptotic in \(L^2\) to \(v_a/\|v_a\|_2\). The latter converges weakly to zero, being supported on shrinking intervals. The difference \(P_a-P_E\) is the rank-one projector onto this normalized component, and hence \(P_af\to P_Ef\) in \(L^2\) for each fixed \(f\in L^2\). Reflection treats \(a\to1\). Independently, \(P_E\) has kernel \(1+12(x-1/2)(y-1/2)\), with sharp maximum row integral \(5/3\) at either endpoint. The exact one-knot formula tends to \(7/3\), giving a sharp gap \(2/3\) in the limiting stability constants.

## Verification
The accompanying standalone `CHECKER.py` symbolically reconstructs the Gram matrix and its inverse, verifies all three row-kernel identities for arbitrary symbolic knot parameter, checks the zero crossings and their absolute integrals, and independently evaluates exact rational row norms for interior knots and test points. It passes \(1485\) exact-rational row comparisons plus the symbolic identities. This finite supplementary check is not used as a proof for all real knots; the integral identities and convexity argument establish the universal formula.

## Relationship to prior work
Shadrin's theorem provides a mesh-independent \(L^\infty\) estimate for general spline orthoprojectors and records the sharp uniform order-two constant \(3\) when arbitrary finite knot sequences are allowed. It does not determine the exact one-interior-knot parameter profile. Passenbrunner and Shadrin subsequently give kernel decay and almost-everywhere convergence for arbitrary knots, also without the single-knot sharp norm and singular boundary profile. De Boor's earlier mesh-ratio estimates establish a general stability framework but not this exact three-dimensional classification. The one-knot result is a proper finite-interval special setting and should not be interpreted as sharpening the global uniform \(3\) theorem. Searches for equivalent one-breakpoint and three-node reproducing-kernel formulations did not identify an identical result. The older Ciesielski--Kamont paper on projections onto piecewise linear functions could not be inspected in full, so historical priority is provisional.

## Limitations
The theorem concerns unweighted continuous \(L^2\) orthogonal projection with exactly one genuine interior knot; it does not give the sharp constant for arbitrary multiple knots, weighted measures, nonorthogonal interpolation, discrete least squares or nonlinear convex regression. The source comparison is a literature check, not a mathematical proof of novelty. No independent audit has been performed.

## References
- A. Yu. Shadrin, *The \(L^\infty\)-norm of the \(L^2\)-spline projector is bounded independently of the knot sequence: A proof of de Boor's conjecture*, Acta Mathematica 187 (2001), 59--137. Public full text: https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/spn0.pdf .
- M. Passenbrunner and A. Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, arXiv:1308.4824, first posted 2013-08-22, https://arxiv.org/abs/1308.4824 .
- C. de Boor, *A bound on the \(L^\infty\)-norm of \(L^2\)-approximation by splines in terms of a global mesh ratio*, Mathematics of Computation 30 (1976), 765--771. DOI: 10.1090/S0025-5718-1976-0425432-1.
- Z. Ciesielski and A. Kamont, *Projections onto piecewise linear functions*, Functiones et Approximatio Commentarii Mathematici 25 (1997), 129--143 (full text not accessed).
