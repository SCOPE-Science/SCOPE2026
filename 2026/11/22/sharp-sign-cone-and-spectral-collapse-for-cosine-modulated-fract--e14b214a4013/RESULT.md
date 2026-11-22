# Sharp sign cone and spectral collapse for cosine-modulated fractional circle kernels

## Finding

Let \(t>0\), let \(k\ge1\) be an integer, and let \(\alpha>0\). On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), define the absolutely and uniformly convergent series
\[
H_{t,\alpha}(\theta)=\sum_{n\in\mathbb Z}e^{-t|n|^\alpha}e^{in\theta},
\qquad
K_{t,\alpha,k,b}(x,y)=H_{t,\alpha}(x-y)\bigl(1+b\cos(k(x-y))\bigr),
\]
for real \(b\). Positive semidefiniteness means that every finite Gram matrix of \(K\) is positive semidefinite. Then the **exact** positivity region is \(b\ge b_*(t,\alpha,k)\), where
\[
\boxed{
 b_*(t,\alpha,k)=
 \begin{cases}
 -\dfrac{2e^{-tk^\alpha}}{1+e^{-t(2k)^\alpha}},&0<\alpha\le1,\\[6pt]
 0,&\alpha>1.
 \end{cases}}
\]
The boundary has three sharply different types:

- If \(0<\alpha<1\) and \(b=b_*\), exactly the Fourier coefficients with indices \(n=\pm k\) vanish. Every other coefficient is positive, and \(K\) is strictly positive definite on *every* finite set of pairwise distinct circle points.
- If \(\alpha=1\) and \(b=b_*=-\operatorname{sech}(tk)\), precisely the indices \(|n|\ge k\) vanish. The kernel has Fourier rank \(2k-1\); its Gram matrix is positive definite at every set of at most \(2k-1\) distinct points and singular at every set of at least \(2k\) points.
- If \(\alpha>1\), the boundary is \(b_*=0\), and all Fourier coefficients are strictly positive even at the boundary. Every \(b<0\) creates negative Fourier coefficients at arbitrarily high frequencies.

In particular the admissible lower endpoint jumps from \(-\operatorname{sech}(tk)\) at \(\alpha=1\) to \(0\) immediately above \(1\). The classification applies to every harmonic index \(k\), not only to the first cosine harmonic.

## Assumptions and scope

The base spectral kernel is normalized by Fourier coefficients \(u_n=e^{-t|n|^\alpha}\) with \(u_0=1\); there is no factor \(1/(2\pi)\) in the series. It is absolutely convergent for each fixed \(t>0\) and \(\alpha>0\). The angular frequency \(k\) is a fixed *positive integer* and \(b\) is real. The claim is about positive definiteness of stationary kernels, not pointwise nonnegativity of the kernels. For \(0<\alpha\le2\) the unmodulated kernel is the spectral kernel of a stable/fractional heat semigroup; for \(\alpha>2\), the formula remains a positive-definite spectral covariance but need not be a positivity-preserving Markov heat kernel.

For Fourier coefficients \(c_n\) of \(K_{t,\alpha,k,b}\), direct multiplication gives
\[
c_n=u_n+\frac b2\bigl(u_{n-k}+u_{n+k}\bigr),\qquad
u_n=e^{-t|n|^\alpha}.
\]
Here the displayed \(u_j\) uses the absolute value for negative indices. The coefficients are real and even. Herglotz's characterization on \(\mathbb T\) states that the stationary kernel is positive semidefinite if and only if \(c_n\ge0\) for every integer \(n\).

## Proof

**1. Reduction to a single ratio maximum.** For \(n\ge0\) define
\[
D_n=\frac{u_{|n-k|}+u_{n+k}}{u_n}
=e^{t(n^\alpha-|n-k|^\alpha)}+e^{t(n^\alpha-(n+k)^\alpha)}.
\]
All \(u_n\) are positive. If \(b<0\), the spectral inequalities \(c_n\ge0\) are exactly \(-b\le 2/D_n\), or equivalently \(b\ge-2/(\sup_{n\ge0}D_n)\). If \(b\ge0\), every coefficient is strictly positive.

**2. Concave-power case.** Suppose \(0<\alpha<1\), and put \(f(s)=s^\alpha\) for \(s\ge0\). On \(0\le n\le k\), the first summand \(e^{t(f(n)-f(k-n))}\) in \(D_n\) is strictly increasing with \(n\). The second summand \(e^{-t(f(n+k)-f(n))}\) is increasing as well, because increments of a concave function decrease under translation. Thus \(D_0<D_1<\cdots<D_k\).

On integers \(n\ge k\) put \(a_n=f(n)-f(n-k)\). The sequence \((a_n)_{n\ge k}\) is positive, decreasing, and **convex**: indeed, for real \(s>k\),
\[
a(s)=\int_0^k f'(s-v)\,dv,
\]
and \(f'\) is positive, decreasing and strictly convex since \(f'''(s)=\alpha(\alpha-1)(\alpha-2)s^{\alpha-3}>0\) for \(s>0\). Convexity extends to the endpoint by continuity. In particular, with \(\delta_n=a_n-a_{n+1}>0\), one has \(\delta_n\ge\delta_{n+k}\). Now
\[
D_n=e^{ta_n}+e^{-ta_{n+k}},
\]
and therefore
\[
\begin{aligned}
D_n-D_{n+1}
&=(e^{ta_n}-e^{ta_{n+1}})
 -(e^{-ta_{n+k+1}}-e^{-ta_{n+k}})\\
&>t\delta_n-t\delta_{n+k}\ge0.
\end{aligned}
\]
The strict inequality uses \(a_n>0\): the derivative of \(e^{tx}\) is greater than \(t\) on positive arguments, whereas the magnitude of the derivative of \(e^{-tx}\) is less than \(t\). Consequently \(D_k>D_{k+1}>D_{k+2}>\cdots\). The unique global maximum is
\[
D_k=\frac{1+e^{-t(2k)^\alpha}}{e^{-tk^\alpha}},
\]
which gives the asserted sharp bound. At equality,
\[
c_n=u_n\left(1-\frac{D_{|n|}}{D_k}\right)
\]
is zero only for \(n=\pm k\). All other coefficients are strictly positive. If a finite Gram form vanishes, the positive Fourier coefficients for the infinitely many consecutive integers \(n\ge k+1\) force the coefficients of its point masses to vanish by a square Vandermonde system, proving strict positive definiteness for distinct sites.

**3. Poisson-power endpoint.** For \(\alpha=1\), the function \(f(s)=s\) has constant increments. The same first-step argument shows \(D_n\) is strictly increasing on \(0\le n\le k\), while for every \(n\ge k\),
\[
D_n=e^{tk}+e^{-tk}=2\cosh(tk).
\]
Therefore \(b_*=-1/\cosh(tk)\), and exactly the tail \(|n|\ge k\) disappears at equality. More explicitly, putting \(r=e^{-t}\),
\[
\boxed{c_n=\frac{r^{|n|}-r^{2k-|n|}}{1+r^{2k}}>0
\quad (|n|<k),\qquad c_n=0\quad(|n|\ge k).}
\]
Thus the positive-frequency support contains the \(2k-1\) consecutive integers \(-k+1,\ldots,k-1\). The matrix of these exponentials evaluated at \(m\) distinct points has column rank \(\min(m,2k-1)\) by the usual Vandermonde determinant. The exact Gram rank and finite-site statement follow.

**4. Superlinear powers.** For every \(\alpha>1\),
\[
D_n\ge e^{t(n^\alpha-(n-k)^\alpha)}\longrightarrow\infty
\quad(n\to\infty),
\]
since the mean value theorem gives \(n^\alpha-(n-k)^\alpha\ge\alpha k(n-k)^{\alpha-1}\). Hence every \(b<0\) causes a negative coefficient, at arbitrarily large indices. For \(b\ge0\) every coefficient is strictly positive, proving both the threshold and strict positive definiteness.

**5. Cross-exponent boundary.** Continuity of the explicit fractional formula as \(\alpha\uparrow1\) gives \(-2e^{-tk}/(1+e^{-2tk})=-\operatorname{sech}(tk)\). The superlinear branch has lower endpoint \(0\) for every \(\alpha>1\), establishing the discontinuity.

## Verification

The accompanying standalone `check.py` evaluates the logarithmic Fourier-ratio profile for many exponents, scales and harmonics; it checks the monotone rise and fall around \(n=k\), the plateau for \(\alpha=1\), the sign of the predicted critical Fourier coefficients, and the superlinear negative-mode obstruction. It also verifies the Poisson endpoint formula **exactly over rational arithmetic**, for several rational \(r\), degrees and Fourier indices. The checker completed 82,183 assertions. These finite tests are not used to justify the infinite inequalities, which follow from the preceding calculus and Vandermonde arguments.

Reproduce with Python 3 (standard library only): `python check.py`. No external data or downloaded package is required.

## Relationship to prior work

The periodic fractional-Laplacian Fourier multiplier appears in the torus analysis of Cardona, Delgado and Ruzhansky (arXiv:2406.05973, Section 1.2), and fractional-heat semigroups are central to Ren and Zhang (arXiv:2111.00725). Their investigated operator bounds and evolution equations do not give the signed stationary angular-modulation cone. Buhmann and Jäger (2022, Section 5) give general strict-positive-definiteness criteria on the circle, which support the Fourier-support interpretation but do not compute the sharp all-harmonic modulation bound.

Other known circle-kernel results concern Poisson or geodesic exponential covariances, Gaussian heat coefficients, or *sum-coordinate* nonstationary modulations. The present calculation uses \(\cos(k(x-y))\), shifts the *stationary* spectral coefficients, and distinguishes concave, linear, and superlinear damping across every integer \(k\). The classical \(\alpha=1\) finite-band cancellation is elementary on its own; the nontrivial statement is the unified sharp threshold, unique fractional spectral notch, and three-way spectral-rank transition. No claim of a general new Herglotz theorem is made.

## Limitations

The finding classifies one signed cosine modulation, not arbitrary trigonometric multipliers or nonstationary kernels. It does not give sharp Gram eigenvalues for arbitrary point configurations. Inaccessibility of some thematically adjacent published records prevents exclusion of every earlier equivalent formulation; priority remains provisional. Boundary strict positive definiteness does not imply full Fourier-support universality, since critical fractional kernels omit two frequencies. The arithmetic checker tests finite parameter sets and cannot certify the universal theorem independently.

## References

1. X. Ren and C. Zhang, *Boundedness of differential transforms for heat semigroups generated by fractional Laplacian*, arXiv:2111.00725v1, first public 2021-11-01, https://arxiv.org/abs/2111.00725.
2. D. Cardona, J. Delgado and M. Ruzhansky, *Well-posedness for a class of pseudo-differential hyperbolic equations on the torus*, arXiv:2406.05973v1 (first public 2024-06-10), https://arxiv.org/abs/2406.05973; *Aequationes Mathematicae* 98 (2024), https://doi.org/10.1007/s00010-024-01093-x.
3. M. Buhmann and J. Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres*, *Journal of Fourier Analysis and Applications* 28, 40 (2022), https://doi.org/10.1007/s00041-022-09913-x.
4. Classical Herglotz theorem for positive-definite functions on compact abelian groups and the elementary Vandermonde determinant (background tools).
