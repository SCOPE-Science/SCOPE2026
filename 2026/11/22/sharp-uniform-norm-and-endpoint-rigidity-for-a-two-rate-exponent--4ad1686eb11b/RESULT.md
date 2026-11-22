# Sharp uniform norm and endpoint rigidity for a two-rate exponential orthoprojector

## Finding

For every pair of distinct positive real rates \(0<a<b\), let \(P_{a,b}\) be the ordinary unweighted \(L^2(0,\infty)\)-orthogonal projector onto the real two-dimensional subspace
\[E_{a,b}=\operatorname{span}\{e^{-at},e^{-bt}\}.\]
Its finite-rank integral kernel also defines a bounded operator on \(L^\infty(0,\infty)\). Put \(R=b/a>1\). The exact endpoint operator norm is
\[
\boxed{\|P_{a,b}\|_{L^\infty\to L^\infty}=
\mathcal L(R):=\frac{4(R+1)}R\,R^{-1/(R-1)}.}
\]
The kernel's \(L^1\)-row norm achieves its **unique global maximum** at output time \(t=0\). In the input variable it changes sign exactly once, at
\[s_0=\frac{\log R}{b-a}.\]
The bounded function equal to \(+1\) before \(s_0\) and \(-1\) after \(s_0\) attains this operator norm in the natural \(L^\infty\) extension (its sign may be reversed).

The norm is strictly increasing in the rate ratio, with sharp but unattained two-rate envelope
\[
\lim_{R\downarrow1}\mathcal L(R)=\frac8e,\qquad
\sup_{R>1}\mathcal L(R)=\lim_{R\to\infty}\mathcal L(R)=4.
\]
For exactly equal rates the span collapses to one dimension and the norm is \(2\). Thus the two-rate limit is discontinuous at the rank drop. At \(R=2\), the exact norm is \(3\).

## Assumptions and scope

The measure is ordinary Lebesgue measure on the nonnegative half-line. The rates are real, finite, positive and distinct. The scalar field can be real or complex: the kernel is real and the same operator norm holds for complex bounded inputs. The orthogonal projection is originally defined in \(L^2\); the stated \(L^\infty\) operator is its canonical bounded extension, defined through the two absolutely convergent exponential moments. The output representative is continuous on the closed half-line and tends to zero at infinity; its essential supremum on the open half-line equals the supremum of this continuous extension, including the boundary limit at zero. Equality of operator norms is an assertion about this specific least-squares orthoprojector, not arbitrary projections onto the same subspace. The sign input giving the \(L^\infty\) norm need not belong to \(L^2\).

Rescaling both rates by a common positive factor amounts to an isometric change of variable. It suffices to set \(a=1\) and write \(b=R\).

## Proof

**1. Kernel and reduction.** The Gram matrix of \(e^{-t}\) and \(e^{-Rt}\), and its inverse, are
\[
G=\begin{pmatrix}1/2&1/(R+1)\\1/(R+1)&1/(2R)\end{pmatrix},\qquad
G^{-1}=\frac{2(R+1)}{(R-1)^2}
\begin{pmatrix}R+1&-2R\\-2R&R(R+1)\end{pmatrix}.
\]
For an output time \(t\ge0\), set
\[u=e^{-t},\quad w=e^{-(R-1)t},\quad
D=\frac{2(R+1)}{(R-1)^2},\quad C=D(R-1)=\frac{2(R+1)}{R-1},\]
\[A=(R+1)-2Rw,\qquad B=R((R+1)w-2).\]
The reproducing kernel is
\[K(t,s)=Du\,e^{-s}(A+B e^{-(R-1)s}).\]
Hence, substituting \(z=e^{-s}\), its absolute row integral is
\[\mathcal J(w)=Du\int_0^1|A+Bz^{R-1}|\,dz,\qquad u=w^{1/(R-1)}.\]
Without the absolute value, the integral is \(A+B/R=(R-1)(1-w)\). At the endpoints of the \(z\)-interval, the signs are those of \(A\) and \(A+B=(R-1)(Rw-1)\). The function of \(z\) inside the absolute value is monotone; thus it changes sign at most once.

**2. Initial row and sharp lower bound.** At \(t=0\), the row simplifies to
\[K(0,s)=\frac{2(R+1)}{R-1}\big(R e^{-Rs}-e^{-s}\big).\]
Its unique zero is \(s_0=(\log R)/(R-1)\). Its signed integral is zero, and the positive mass before the zero is
\[\frac{2(R+1)}{R-1}\left(e^{-s_0}-e^{-Rs_0}\right).\]
Twice this positive mass is the absolute row integral
\[\mathcal J(1)=\frac{4(R+1)}R\,R^{-1/(R-1)}=\mathcal L(R).\]
Choosing bounded input equal to the sign of this kernel realizes the row norm and therefore gives the claimed lower bound for the operator norm.

**3. Early-time sign regime.** Let \(w_A=(R+1)/(2R)\). For \(w_A<w\le1\), one has \(A<0\) and \(A+B>0\). The unique zero in the \(z\) variable satisfies
\[z_0^{R-1}=\frac{2Rw-(R+1)}{R((R+1)w-2)}.\]
The right side is at most \(1/R\) because \((R-1)w\le R-1\). Consequently
\[z_0\le z_*:=R^{-1/(R-1)}.\]
Integrating the negative segment exactly gives
\[\mathcal J(w)=Cu\left[(1-w)+\frac{2}{R}(2Rw-R-1)z_0\right].\]
Since the coefficient of \(z_0\) is nonnegative, replacement by \(z_*\) yields
\[
\mathcal J(w)\le Cu\left[\frac{2(R-1)}Rz_*+(1-4z_*)(1-w)\right].
\]
The elementary logarithmic inequality \(\log R\le R-1\) implies \(z_*\ge e^{-1}>1/4\), so the second summand is nonpositive. Therefore \(\mathcal J(w)\le u\mathcal L(R)\le\mathcal L(R)\), strictly if \(t>0\). At \(w=w_A\), the formula holds by continuity.

**4. Nonnegative-kernel regime.** For \(1/R\le w\le w_A\), both endpoint signs are nonnegative, and hence the entire kernel row is nonnegative. Thus
\[\mathcal J(w)=Cu(1-w)=Cw^{1/(R-1)}(1-w).\]
The last expression is maximized for \(w=1/R\), giving precisely \(\mathcal L(R)/2\), strictly less than the initial row norm.

**5. Late-time sign regime.** For \(0<w<1/R\), one has \(A>0\), \(A+B<0\), and a single zero
\[z_0=\left(\frac{A}{-B}\right)^{1/(R-1)}\le1.\]
Integrating above this zero gives
\[\mathcal J(w)=Cu\left[\frac{2A}{R}z_0-(1-w)\right]
\le C w^{1/(R-1)}\left(\frac{R+2}{R}-3w\right).\]
Put \(p=1/(R-1)\). The upper-bound function \(w^p((R+2)/R-3w)\) has its maximum on \([0,1/R]\) at \(w_0=(R+2)/(3R^2)\). Dividing this maximum by \(\mathcal L(R)\) gives
\[Q(R)=\frac{R+2}{2R}\left(\frac{R+2}{3R}\right)^{1/(R-1)}.\]
Set \(x=2(R-1)/(3R)\), so that \((R+2)/(3R)=1-x\). From \(\log(1-x)\le-x\),
\[\log Q(R)\le\log\frac{R+2}{2R}-\frac{2}{3R}.\]
The expression on the right equals \(\log(3/2)-2/3<0\) at \(R=1\), and its derivative is
\[\frac{4(1-R)}{3R^2(R+2)}<0\qquad(R>1).\]
Consequently \(Q(R)<1\), proving strict domination in the late-time regime as well. At \(w=1/R\), continuity connects to the preceding regime. At \(w=0\) the row norm tends to zero.

Steps 3–5 prove that every positive evaluation time has strictly smaller row norm than the initial time. The lower bound from Step 2 is thus the exact global \(L^\infty\) norm, and \(t=0\) is the unique norming evaluation point.

**6. Dependence on rate ratio.** Direct differentiation shows
\[
\frac{d}{dR}\log\mathcal L(R)
=\frac{\log R-2(R-1)/(R+1)}{(R-1)^2}>0.
\]
Indeed the numerator vanishes at \(R=1\) and has derivative \((R-1)^2/[R(R+1)^2]>0\) for \(R>1\). The two limits follow from \(\log R/(R-1)\to1\) as \(R\downarrow1\) and \(\log R/(R-1)\to0\) as \(R\to\infty\). When \(a=b\), the rank-one kernel is \(2a e^{-a(t+s)}\), with uniform norm \(2\).

## Verification

A standalone reproducibility script `check.py` reconstructs the Gram inverse and two key sign identities symbolically, independently evaluates the row integrals by high-precision quadrature after splitting at the exact zero, and compares them with the three closed-form branches and the global bound for eight rate ratios and nine evaluation times per ratio. The performed run reported 72 high-precision row comparisons passing, alongside the symbolic identities and numerical limiting cases. These checks are supplementary: Steps 1–6 above prove the continuum statement for every permissible rate ratio and time.

## Relationship to prior work

The motivating half-line exponential-polynomial literature studies sharp derivative inequalities and real-exponent Chebyshev systems, rather than the precise amplification of an \(L^2\) orthoprojector on \(L^\infty\) [1]. Polynomial-frame least-squares stability [2] concerns discrete samples and regularized polynomial fits over finite intervals. Earlier exponential \(L\)-spline projections [3] involve piecewise splines, knot partitions and different differential operators; their mesh-independent bounds do not yield the present two-pure-decay kernel formula.

The general methods of Gram inversion and kernel-row integration are standard. The contribution claimed here is the exact **global**, rate-dependent expression, proof of endpoint rigidity for every rate ratio, strict monotonicity, and sharp uniform envelope \(4\) for the specified half-line orthoprojector. Other special exponential projection norms, including the coalescent two-mode limit and finite-interval exponential fits, do not by themselves imply this entire two-real-rate formula.

## Limitations

The theorem concerns exactly two distinct positive real decay rates and unweighted continuous half-line least squares. It does not address finite intervals, nonpositive/complex decay rates, higher-dimensional exponential systems, weighted input measures, or minimization of norm over all projections. A finite coefficient Gram matrix becomes ill-conditioned as the two rates coalesce; the exact norm is a property of the projected *function*, not a bound on numerical coefficient recovery. The bounded norming sign input is generally not square integrable. Earlier specialized approximation literature may have obtained equivalent formulas; historical novelty is not a theorem of the present proof. Independent validation has not been performed.

## References

[1] V. Yu. Protasov, *Generalized Markov-Bernstein inequalities and stability of dynamical systems*, arXiv:2209.12250, first public preprint September 25, 2022. https://arxiv.org/abs/2209.12250

[2] B. Adcock and A. Shadrin, *Fast and stable approximation of analytic functions from equispaced samples via polynomial frames*, arXiv:2110.03755, first public preprint October 7, 2021. https://arxiv.org/abs/2110.03755

[3] A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first public preprint August 30, 2004. https://arxiv.org/abs/math/0408418
