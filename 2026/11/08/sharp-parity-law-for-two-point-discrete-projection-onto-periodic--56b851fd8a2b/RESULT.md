# Sharp parity law for two-point discrete projection onto periodic linear splines

## Finding

Fix an integer \(N\ge3\). On the circle \(\mathbb R/N\mathbb Z\), let \(S_N\) be the real vector space of continuous functions that are affine on each unit interval \([i,i+1]\), for \(i\in\mathbb Z/N\mathbb Z\). Fix \(0<t<1/2\), and let \(R_{N,t}:C(\mathbb R/N\mathbb Z)\to S_N\) be least-squares projection using the \(2N\) equally weighted observations at \(i+t\) and \(i+1-t\) for all \(i\). Write \(q=t/(1-t)\). Then the **exact, attained operator norm** is

\[
\boxed{\|R_{N,t}\|_{C\to C}=\frac{1-q^N}{(1-2t)(1-(-q)^N)}
=\begin{cases}
(1-2t)^{-1},&N\text{ even},\\[2pt]
(1-2t)^{-1}\dfrac{1-q^N}{1+q^N},&N\text{ odd}.
\end{cases}}
\]

Precisely the \(N\) knots are norm-maximizing evaluation points. At each knot, the maximizing sample data are characterized by the signs of the explicit projection coefficients in the proof. The sharp worst negativity on inputs \(0\le f\le1\) is

\[
\boxed{\inf_{0\le f\le1}\min_x(R_{N,t}f)(x)
=-\frac{\|R_{N,t}\|_{C\to C}-1}{2}.}
\]

The norm increases strictly with \(t\). As \(t\uparrow1/2\), it diverges for even \(N\), but tends to \(N\) for odd \(N\). At the coincident midpoint rule \(t=1/2\), the least-squares projector remains uniquely defined for odd \(N\), has norm exactly \(N\), and is singular for even \(N\). The degenerate knot-sampling endpoint \(t=0\) is nodal interpolation with norm one.

For two-point Gauss quadrature, \(t=(1-1/\sqrt3)/2\) and \(q=2-\sqrt3\). Consequently the exact sharp norm is \(\sqrt3\) for every even \(N\), while for odd \(N\) it equals

\[
\sqrt3\,\frac{1-(2-\sqrt3)^N}{1+(2-\sqrt3)^N}.
\]

Thus the periodic two-node Gauss sampling operator has a dimension-independent sharp \(\ell^\infty\)-to-\(L^\infty\) constant, and its odd-parity deficit is exponentially small. The two-node rule becomes arbitrarily unstable under coalescence towards cell midpoints only for even cycles; for each fixed odd cycle its limiting norm is finite.

## Assumptions and scope

The circle is parametrized by length with uniform unit cells. Its knots are \(i\pmod N\). The input is a real continuous periodic function with its ordinary uniform norm. Sampling weights on all \(2N\) points are equal and positive; multiplying them by a common constant does not change the projection. The two points within each cell are distinct for \(0<t<1/2\). The projection is the unique least-squares minimizer among periodic continuous piecewise-affine functions, not the projector defined by continuous arclength integration. The claimed endpoint norm measures the full continuous spline output, not only the sampled values. The positivity assertion permits any continuous input taking values in \([0,1]\).

## Proof

Let \(u_i=s(i)\) be the knot values of a spline. Put \(A=1-t\) and \(B=t\). On the \(i\)-th cell the two spline observations are \(Au_i+Bu_{i+1}\) and \(Bu_i+Au_{i+1}\), with subscripts modulo \(N\). Let \(T\) be the cyclic forward shift. The two sampling matrices are \(L=AI+BT\) and \(M=BI+AT\). The nodal normal matrix is

\[
G=L^{\mathsf T}L+M^{\mathsf T}M
=2(A^2+B^2)I+2AB(T+T^{-1}).
\]

For \(0<t<1/2\), \(A>B>0\); the Fourier symbol \(2(A^2+B^2+2AB\cos\theta)\) is bounded below by \(2(A-B)^2\), so \(G\) is invertible. Write \(D=A^2-B^2=1-2t\) and \(q=B/A\). The Green kernel of this cyclic matrix, obtained by periodizing the geometric fundamental solution of the bilateral recurrence, is

\[
(G^{-1})_{0k}=g_k=
\frac{(-q)^k+(-q)^{N-k}}{2D[1-(-q)^N]},
\qquad 0\le k<N.
\]

Indeed \(2(A^2+B^2)h_k+2AB(h_{k-1}+h_{k+1})\) vanishes for nonzero \(k\) when \(h_k=(-q)^{|k|}/(2D)\), and is one at zero; summing its integer translates by \(N\) gives the displayed inverse. This argument includes \(N=3\), where the two cyclic neighbors are distinct.

The coefficient of the observation at \(i+t\) in the fitted value at knot zero is \(Ag_i+Bg_{i+1}\). The coefficient of the observation at \(i+1-t\) is \(Bg_i+Ag_{i+1}\). Substitution of the Green kernel gives the **exact signed rows**

\[
c_{i,-}=\frac{(-q)^i}{2A[1-(-q)^N]},\qquad
c_{i,+}=\frac{(-q)^{N-i-1}}{2A[1-(-q)^N]}
\qquad (0\le i<N).
\]

The cancellations use \(B=Aq\). Summing the absolute values of these \(2N\) coefficients yields

\[
\sum_{i=0}^{N-1}(|c_{i,-}|+|c_{i,+}|)
=\frac{1-q^N}{A(1-q)[1-(-q)^N]}
=\frac{1-q^N}{(1-2t)[1-(-q)^N]}.
\]

Translation symmetry gives the same evaluation norm at every knot. At a non-knot point, the fitted value is a strict convex combination of the two adjacent fitted knot values. The triangle inequality bounds its evaluation norm by the knot norm. The inequality is strict: for the sample just to the right of the second knot, the coefficients in these adjacent knot rows have opposite nonzero signs (the signed-row formula is cyclically shifted), so absolute values cannot be affine on their connecting segment. Thus precisely the knots maximize the norm.

Since \(2N\) sample sites are distinct for \(0<t<1/2\), arbitrary assigned signs at them extend to real periodic continuous functions of uniform norm one. The displayed total variation is therefore the actual attained operator norm; maximizers at each knot have sample signs equal to the signs of \(c_{i,-}\) and \(c_{i,+}\), up to one overall sign.

The projection reproduces constants, so \(\sum_i(c_{i,-}+c_{i,+})=1\). Among sample inputs in \([0,1]\), the smallest knot output is obtained by setting the samples to one exactly where their coefficients are negative, and zero elsewhere. This equals the sum of negative coefficients, \((1-\|R_{N,t}\|)/2\). Continuous interpolants attain those prescribed \(0/1\) values; the preceding strict localization proves the global positivity formula.

For even \(N\), \((-q)^N=q^N\), and the quotient cancels exactly. For odd \(N\), write \(q=e^{-2u}\), \(u>0\), so the formula becomes \(\coth(u)\tanh(Nu)\). Its logarithmic derivative in \(u\) is \(-2/\sinh(2u)+2N/\sinh(2Nu)<0\) because \(\sinh(Nx)>N\sinh(x)\) for \(N>1\) and \(x>0\). Because \(u\) decreases as \(t\) increases, the odd-case norm is strictly increasing; the even case is immediate. The odd norm tends to \(N\) as \(u\downarrow0\). At the midpoint rule, the observation equations are proportional to \(u_i+u_{i+1}\); this map has an alternating kernel precisely for even \(N\). For odd \(N\) the coincident sample coefficients combine with matching signs and yield norm \(N\). At \(t=0\), nodal sampling gives ordinary piecewise-linear interpolation of norm one. Finally substitution of the exact two-point Gauss rule proves the stated Gauss constants.

## Verification

The attached standalone Python program `checker.py` uses exact rational arithmetic, builds both sampling matrices directly, inverts their normal matrix, and tests the signed kernel coefficient formulas, row norm, reproduction of constants, positivity deficit, and adjacent-sign rigidity for each \(3\le N\le13\) at \(t=1/10,1/4,2/5\). It separately tests the odd midpoint limit and the knot-sampling endpoint. The recorded execution returned `ALL_DISCRETE_SPLINE_CHECKS_PASSED`. These finite diagnostics are not an infinite proof; the geometric inverse and analytic arguments above apply to every stated \(N\) and \(t\).

## Relationship to prior work

Grigorieff and Sloan, *Stability of discrete orthogonal projections for continuous splines* (1998), prove general \(L^p\) stability and convergence for quadrature-defined spline projections under assumptions on quadrature and meshes. Their Theorem 4.4 supplies a general boundedness framework, not the exact periodic two-site endpoint norm or the even/odd cancellation formula obtained here. Their article discusses interval rather than periodic spline spaces. Earlier work of Crouzeix and Thomée treats continuous \(L^2\)-projection stability. This result does not assert that general \(L^p\) stability or the circulant inversion method is new. It isolates sharp operator constants, all norming locations, exact positivity loss and a rank-degeneration boundary for a canonical symmetric quadrature family.

## Limitations

The theorem is for real piecewise-linear **periodic** splines, uniform cell lengths, and equal two-site quadrature weights. It does not claim the same formula for nonuniform meshes, asymmetric samples, additional spline degrees, or continuous-measure \(L^2\) projection. The historical 1998 paper has an earlier print year than its date-stamped 2009 digital publication; its exact first print dissemination day is not established here. Equivalent unindexed numerical-analysis formulas remain a priority risk. The stated results have no independent mathematical audit.

## References

1. R. D. Grigorieff and I. H. Sloan, *Stability of discrete orthogonal projections for continuous splines*, Bulletin of the Australian Mathematical Society **58** (1998), 307–332. DOI: 10.1017/S0004972700032263. Publisher's date-stamped online publication: 17 April 2009. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F7D0DC09E500F27C9A04CE850E6F18BB/S0004972700032263a.pdf/stability-of-discrete-orthogonal-projections-for-continuous-splines.pdf
2. M. Crouzeix and V. Thomée, *The stability in \(L^p\) and \(W^{1,p}\) of the \(L^2\)-projection onto finite element function spaces*, Mathematics of Computation **48** (1987), 521–532, as cited in [1].
3. M. Karkulik, C.-M. Pfeiler and D. Praetorius, *\(L^2\)-orthogonal projections onto finite elements on locally refined meshes are \(H^1\)-stable*, arXiv:1307.0917 (first version publicly posted 3 July 2013), https://arxiv.org/abs/1307.0917. This concerns a different stability norm and mesh setting.
