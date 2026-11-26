# Sharp confluent-node amplification for minimal quadratic midpoint splines

## Finding

For the unique quadratic, continuously differentiable spline interpolating four data values at sites \(0,\varepsilon,\varepsilon+L,\varepsilon+L+R\), with its only interior knot at \(\varepsilon+L/2\), fix \(L,R>0\) and let \(\varepsilon\downarrow0\). The sharp data-to-spline operator norm obeys

\[
\Lambda_{\varepsilon,L,R}=\frac{L}{2\varepsilon}\max\!\left\{\frac{2+3r}{3+4r},\frac{r^2}{2+3r}\right\}+O_{L,R}(1),\qquad r=R/L.
\]

The leading amplification occurs in the left interval for \(r<1+\sqrt3\), in the right interval for \(r>1+\sqrt3\), and at both extremal locations for \(r=1+\sqrt3\). This threshold is the unique positive solution of the exact balance equation. For \(L=R=1\), \(\Lambda_{\varepsilon,1,1}=5/(14\varepsilon)+O(1)\). The leading term is attained by data with the first two observations of opposite signs.

## Assumptions and scope

Let \(L>0\), \(R>0\) be fixed real lengths and \(0<\varepsilon<L/2\). Set \(t_1=0\), \(t_2=\varepsilon\), \(t_3=\varepsilon+L\), \(t_4=\varepsilon+L+R\), and \(k_\varepsilon=\varepsilon+L/2\). Given any \(y\in\mathbb R^4\), let \(I_{\varepsilon,L,R}y\) be quadratic on each of \([0,k_\varepsilon]\) and \([k_\varepsilon,t_4]\), continuously differentiable at \(k_\varepsilon\), and equal to \(y_i\) at \(t_i\). The vector norm is \(\|y\|_{\ell_\infty}=\max_i|y_i|\), the function norm is the supremum norm on \([0,t_4]\), and \(\Lambda_{\varepsilon,L,R}=\sup_{\|y\|_{\ell_\infty}\le1}\|I_{\varepsilon,L,R}y\|_\infty\). The \(O_{L,R}(1)\) remainder is uniform over such data, with \(L,R\) held fixed. No mesh-uniform bound is asserted when the other lengths vary with \(\varepsilon\).

## Proof

**1. Well-posedness.** Write the left and right polynomial pieces as \(a_0+a_1x+a_2x^2\) and \(b_0+b_1x+b_2x^2\), respectively. The four node values and the two matching conditions at \(k_\varepsilon\) form a six-by-six linear system. With rows ordered as left value at \(0\), left value at \(\varepsilon\), right values at \(\varepsilon+L\) and \(\varepsilon+L+R\), and then matched value and first derivative, its determinant is

\[
\frac{\varepsilon LR}{4}\bigl(3\varepsilon L+4\varepsilon R+2L^2+3LR\bigr)>0.
\]

Hence there is exactly one interpolant for every admissible positive \(\varepsilon\).

**2. Limit after rescaling.** Put \(p_\varepsilon=\varepsilon I_{\varepsilon,L,R}y\). Its interpolation equations become \(p_\varepsilon(0)=\varepsilon y_1\), \(p_\varepsilon(\varepsilon)=\varepsilon y_2\), \(p_\varepsilon(\varepsilon+L)=\varepsilon y_3\), and \(p_\varepsilon(\varepsilon+L+R)=\varepsilon y_4\). Replace the second equation by its divided difference, so that

\[
\frac{p_\varepsilon(\varepsilon)-p_\varepsilon(0)}{\varepsilon}=y_2-y_1.
\]

All six equations depend continuously and analytically on \(\varepsilon\) at zero. Their limiting constraints specify a quadratic \(p_0^-\) with \(p_0^-(0)=0\) and \((p_0^-)'(0)=y_2-y_1\), a quadratic \(p_0^+\) with \(p_0^+(L)=p_0^+(L+R)=0\), and value/derivative matching at \(L/2\). The homogeneous limiting system is nonsingular: a homogeneous candidate has \(p_0^-(x)=Ax^2\) and \(p_0^+(x)=B(x-L)(x-L-R)\). Matching gives \(AL=B(L+2R)\) and \(AL=-B(L+R)\); since \(2L+3R>0\), both coefficients vanish. Therefore the coefficient solution is analytic at zero, and the scaled spline converges uniformly, with coefficient error \(O_{L,R}(\varepsilon\|y\|_{\ell_\infty})\), to

\[
(y_2-y_1)\Phi_{L,R}(x),\qquad
\Phi_{L,R}(x)=\begin{cases}
 x-\dfrac{3L+4R}{L(2L+3R)}x^2,&0\le x\le L/2,\\[5pt]
 \dfrac{(x-L)(x-L-R)}{2L+3R},&L/2\le x\le L+R.
\end{cases}
\]

Moving the interior knot by \(\varepsilon\) changes the uniform norm only by \(O_{L,R}(\varepsilon\|y\|_{\ell_\infty})\), because both polynomial branches and their first derivatives remain uniformly bounded and agree continuously at the knot. Likewise the right endpoint moves only by \(\varepsilon\). Consequently

\[
\varepsilon\Lambda_{\varepsilon,L,R}=2\|\Phi_{L,R}\|_\infty+O_{L,R}(\varepsilon).
\]

The factor two is exact: \(\sup_{\|y\|_{\ell_\infty}\le1}|y_2-y_1|=2\), attained at \((y_1,y_2)=(-1,1)\), with the remaining entries arbitrary in \([-1,1]\).

**3. Exact extrema and phase transition.** The left parabola has its unique positive maximum at \(x=L(2L+3R)/[2(3L+4R)]\), of value

\[
M_-=\frac{L(2L+3R)}{4(3L+4R)}.
\]

The right polynomial is positive on \([L/2,L]\), attaining its positive maximum at the knot; this is smaller than \(M_-\) by exactly \(L(L+R)^2/[4(2L+3R)(3L+4R)]\). It becomes negative on \((L,L+R)\) and has a negative minimum at \(x=L+R/2\) with absolute size

\[
M_+=\frac{R^2}{4(2L+3R)}.
\]

Thus \(\|\Phi_{L,R}\|_\infty=\max\{M_-,M_+\}\). Writing \(r=R/L\), the sign of \(M_--M_+\) equals the sign of

\[
(2+3r)^2-r^2(3+4r)=-2(2r+1)(r^2-2r-2).
\]

It changes exactly at \(r=1+\sqrt3\). Substitution into the norm relation proves the stated sharp formula, all regimes, and the equal-length constant.

## Verification

The bundled executable `check_spline.py` independently rebuilds the six-by-six interpolation system using exact symbolic arithmetic. It checks the determinant identity, the limiting Hermite spline, the extrema and crossover polynomial, thirty exact-rational interpolation cases, and monotonic coefficient convergence in four separated mesh-ratio families. Run `python check_spline.py` with Python 3 and SymPy installed. These finite and symbolic checks supplement, but do not replace, the proof of the asymptotic operator norm for every real \(L,R>0\).

## Relationship to prior work

A. Greene (arXiv:2610.32044v1, 2026) proves well-posedness and a mesh-ratio-independent \(C^3\) interpolation error of order \(h^3\) for this midpoint-knot construction. Greene's introduction identifies the non-uniform boundedness of the arbitrary-data interpolation operator from M. J. D. Powell's 1981 treatment. Powell's chapter 21.2 gives general unboundedness examples and distinguishes the opposite construction, in which interpolation sites are midpoints of fixed knot intervals. The theorem here computes the exact leading operator norm for the first nontrivial four-site collision and identifies the unique competing-extremum transition. It is consistent with smooth-function approximation estimates, because independently perturbed nodal data need not come from a single \(C^3\) function with bounded third derivative.

A historical priority limitation remains: C. de Boor's 1976 paper *Quadratic spline interpolation and the sharpness of Lebesgue's inequality* could be identified bibliographically but its relevant full text was not accessible for a decisive implication check. The result does not assert an exhaustive novelty guarantee against that work or uninspected specialized spline literature.

## Limitations

Only four sampling sites, one interior midpoint knot, fixed positive lengths \(L,R\), and the coalescence \(\varepsilon\downarrow0\) are covered. The formula is an asymptotic law with a bounded remainder, not an exact finite-\(\varepsilon\) norm. It is a worst-case independent-data sensitivity result, not a lower bound for interpolation of uniformly smooth data. The right-hand length ratio transition need not persist for more nodes or different knot conventions. Independent mathematical validation has not been performed.

## References

1. A. Greene, *Optimal Convergence of Quadratic Not-a-Knot Spline Interpolation on Arbitrary Partitions*, arXiv:2610.32044v1 (first public 2026-10-23), https://arxiv.org/html/2610.32044v1.
2. M. J. D. Powell, *Approximation Theory and Methods*, Cambridge University Press (1981), sections 18.40 and 21.2.
3. C. de Boor, *Quadratic spline interpolation and the sharpness of Lebesgue's inequality*, Journal of Approximation Theory (1976), https://doi.org/10.1016/0021-9045(76)90079-4 (bibliographic comparison only; full text not inspected).
4. *Quadratic interpolatory splines*, Numerische Mathematik (1974), https://doi.org/10.1007/BF01406966 (bibliographic comparison only).
