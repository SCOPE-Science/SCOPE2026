# Exact two-periodic spline projection norms and a quadratic mesh-contrast law

## Finding
Let \(m\ge2\), and let \(P_m\) be the orthogonal \(L^2\)-projection onto the real continuous periodic piecewise-linear splines with \(2m\) knots and successive positive interval lengths alternating between \(a\) and \(b\), after a common scaling to circumference one. Put
\[
s=a+b,\quad H=3a^2+8ab+3b^2,\quad
\Delta=\sqrt{H^2-4a^2b^2},\quad
q=\frac{2ab}{H+\Delta},
\]
where \(0<q<1\), and define, with indices modulo \(m\),
\[
U_k=\frac{12s}{\Delta}\frac{q^k+q^{m-k}}{1-q^m},\qquad
V_k=\frac{aU_k+bU_{k+1}}{2s},\qquad
\Phi(u,v)=\frac{u^2+v^2}{2(u+v)}\quad(u,v>0).
\]
Here the formula for \(U_k\) is given for \(0\le k\le m-1\), with \(U_m=U_0\). The exact endpoint operator norm is
\[
\boxed{\Lambda_m(a,b):=\|P_m\|_{L^\infty\to L^\infty}=
\sum_{k=0}^{m-1}\bigl[a\Phi(U_k,V_k)+b\Phi(V_k,U_{k+1})\bigr].}
\]
All and only the knots are norm-maximizing evaluation points. At each knot, the sign of its reproducing kernel is an extremizing bounded input (up to almost-everywhere agreement and a global sign). The exact sharp positivity defect is
\[
\boxed{\inf_{0\le f\le1}\min_x (P_m f)(x)=-\frac{\Lambda_m(a,b)-1}{2}.}
\]
The minimum is attained by the indicator of the negative set of the reproducing kernel at a knot. For fixed \(a,b>0\), the infinite-period-cell limit is the unexpectedly simple rational law
\[
\boxed{\lim_{m\to\infty}\Lambda_m(a,b)=
\frac{5a^2+22ab+5b^2}{3a^2+10ab+3b^2}
=2-\frac{(a-b)^2}{(3a+b)(a+3b)}.}
\]
Thus the limiting norm equals \(2\) exactly for equal spacings, is strictly less than \(2\) for every genuinely alternating mesh, and approaches \(5/3\) as the aspect ratio tends to zero or infinity. Convergence at fixed positive aspect ratio is exponentially fast in the number of cells.

## Assumptions and scope
The circle carries Lebesgue measure and periodic boundary conditions. The knot sequence consists of \(2m\) distinct points, \(m\ge2\), separated successively by intervals proportional to \(a,b,a,b,\ldots,a,b\), with \(a,b>0\). Common scaling of all interval lengths does not affect \(\Lambda_m\). The projection is the continuous \(L^2\)-orthogonal projection onto the associated real hat-function space, not interpolation or a discrete quadrature projector. Essential-supremum operator norms agree with the maximum of the continuous norm function in the evaluation coordinate. Every statement concerns the continuous circle and finite \(m\), except the displayed limit.

## Proof
**1. Signed inverse Gram matrix.** Use the cyclic nodal hats \(N_j\), \(j\in\mathbb Z/(2m)\). With unnormalized lengths \(h_{2k}=a\), \(h_{2k+1}=b\), their Gram matrix \(G\) has
\[
G_{jj}=\frac{h_{j-1}+h_j}{3}=\frac{s}{3},\qquad
G_{j,j+1}=\frac{h_j}{6};
\]
all other off-diagonals vanish, with cyclic adjacency. The diagonal sign matrix \(D_{jj}=(-1)^j\) converts \(G\) into a strictly diagonally dominant irreducible symmetric matrix with nonpositive off-diagonals. Its inverse is entrywise strictly positive. Consequently
\(\operatorname{sgn}(G^{-1}_{ij})=(-1)^{i+j}\): neighboring inverse-Gram coefficients have opposite signs and nonzero magnitudes.

**2. Explicit two-period Green function.** At the even knot indexed zero, write the even inverse-Gram magnitudes \(u_k=G^{-1}_{0,2k}\) and odd magnitudes \(v_k=-G^{-1}_{0,2k+1}\). The row equation for \(6G\) reads
\[
2s u_k-a v_k-bv_{k-1}=6\mathbf1_{k=0},\qquad
2s v_k=a u_k+b u_{k+1}.
\]
Eliminating \(v\) gives the cyclic recurrence
\[
H u_k-ab(u_{k-1}+u_{k+1})=12s\mathbf1_{k=0}.
\]
Its characteristic smaller root is \(q=(H-\Delta)/(2ab)=2ab/(H+\Delta)\). The unique solution is precisely \(u_k=U_k\), since the cyclic Green kernel is the periodization of \((12s/\Delta)q^{|k|}\). The odd coefficients satisfy \(v_k=V_k\).

**3. Absolute kernel integration and knot rigidity.** The reproducing kernel at a knot \(t_i\) is \(K_{t_i}(y)=\sum_j(G^{-1})_{ij}N_j(y)\). On each interval it is linear between two nonzero, opposite-sign endpoint values. Direct integration of an affine segment from \(u\) to \(-v\) over length \(h\) gives \(h\Phi(u,v)\). Summing the \(2m\) intervals at the even knot yields the exact formula for \(\Lambda_m\). Translation by two cells and reflection about an interval midpoint show all knots yield the same absolute-kernel integral. At a point strictly between neighboring knots, its kernel is a strict convex combination of the neighboring knot kernels. Since these two kernels have opposite signs in a neighborhood of one of the knots, strict triangle inequality for the integral of their absolute values shows that its norm is strictly smaller. Therefore precisely the knots are norm-maximizing evaluation points.

**4. Positivity-loss extremizers.** Reproduction of the constant function gives \(\int K_x(y)\,dy=1\). Writing \(K_x=K_x^+-K_x^-\) yields \(\int K_x^-=(\int|K_x|-1)/2\). The pointwise minimum of \(\int K_xf\) over measurable \(0\le f\le1\) equals \(-\int K_x^-\), attained by \(f=\mathbf1_{\{K_x<0\}}\). Taking the maximal norming evaluation \(x\) proves the sharp defect and its construction.

**5. Contrast law.** As \(m\to\infty\), \(U_k\) converges locally to \(Cq^{|k|}\), with \(C=12s/\Delta\). Define \(A=(a+bq)/(2s)\) and \(B=(aq+b)/(2s)\). Summing the two geometric tails of the absolute kernel gives
\[
\Lambda_\infty=\frac{C}{1-q}\bigl[a\Phi(1,A)+b\Phi(A,q)+a\Phi(q,B)+b\Phi(B,1)\bigr].
\]
The identity \(abq^2-Hq+ab=0\) simplifies this expression exactly to
\((5a^2+22ab+5b^2)/(3a^2+10ab+3b^2)\). Its difference from \(2\) equals \(-(a-b)^2/((3a+b)(a+3b))\). Geometric bounds on the periodization tails and continuity of \(\Phi\) on the positive cone give an \(O_{a,b}(q^{m/2})\) convergence estimate. No uniform-in-aspect-ratio rate is asserted.

## Verification
The standalone `CHECK.py` uses only Python 3 and SymPy. It certifies by polynomial division that the rational contrast law follows from the Green recurrence and verifies the explicit deficit identity symbolically. Independently, an exact rational Gauss–Jordan inverse of each physical hat Gram matrix checks signed coefficients, every knot evaluation, and the proposed finite formula for \(m\in\{2,3,4,5,6\}\) and five distinct rational spacing pairs. It additionally checks long-circle convergence numerically. These finite tests support, but do not replace, the analytic proof for every \(m\ge2\) and \(a,b>0\). Run `python3 CHECK.py` in a directory containing the embedded file, with SymPy installed.

## Relationship to prior work
Ciesielski and Kamont (2004) computed Franklin projection constants for two *long blocks* of distinct knot spacings on an interval, and Passenbrunner (2011) analyzed their periodic analogue, whose supremum is above \(2\). Their Gram-kernel techniques are prior art, as is the general reduction of the operator norm to absolute reproducing-kernel integrals. Passenbrunner (2016 preprint) and Passenbrunner–Shadrin (2013) establish uniform boundedness and convergence for arbitrary knots, not the present sharp alternating two-period norm. Equal spacing is a known special case; the contribution here is the full exact finite alternating formula, its positivity defect, and the strict rational mesh-contrast asymptotic, which go in the opposite direction from block-clustered meshes. Kayumov (2004) addresses stability for a broader class of second-order \(L\)-splines without the alternating exact constant.

## Limitations
The theorem does not treat endpoint/open interval splines, polynomial degrees above one, irregular (nonalternating) meshes, discretized projection, or weights other than Lebesgue measure. The limit is for fixed positive \(a,b\); the approach to the extreme aspect ratio is only a limit of the displayed rational law. The method borrows established inverse-Gram and Lebesgue-kernel principles. Related older sources on piecewise-linear projections may contain an unindexed equivalent expression; independent literature audit has not been performed.

## References
- Z. Ciesielski and A. Kamont, *The Lebesgue constants for the Franklin orthogonal system*, Studia Mathematica 164 (2004), 55–73, https://doi.org/10.4064/sm164-1-4.
- M. Passenbrunner, *The Lebesgue Constant for the Periodic Franklin System*, initial preprint 2011-03-10, https://arxiv.org/abs/1103.1950.
- M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, initial preprint 2016-08-24, https://arxiv.org/abs/1608.06720.
- M. Passenbrunner and A. Shadrin, *On almost everywhere convergence of orthogonal spline projections with arbitrary knots*, initial preprint 2013-08-22, https://arxiv.org/abs/1308.4824.
- A. Kayumov, *Least-squares approximation by second-order L-splines*, initial preprint 2004-08-30, https://arxiv.org/abs/math/0408418.
