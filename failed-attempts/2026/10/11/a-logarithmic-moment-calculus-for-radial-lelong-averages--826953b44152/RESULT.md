# A logarithmic-moment calculus for radial Lelong averages

## Finding

Let \(u\) be plurisubharmonic in a neighborhood of
\[
0\in\mathbb C^n
\]
and not identically equal to \(-\infty\). Write
\[
S(u,r)
=
\frac{1}{\sigma(\partial B(r))}
\int_{\partial B(r)}u\,d\sigma.
\]

Let \(\beta\) be a probability measure on
\[
(0,1]
\]
with finite logarithmic radius moment
\[
L(\beta)
=
\int_{(0,1]}-\log t\,d\beta(t)
<
\infty.
\]
Define
\[
A_\beta(u,r)
=
\int_{(0,1]}
S(u,tr)\,d\beta(t).
\]

Then for any two such probability measures \(\beta\) and \(\gamma\),
\[
\lim_{r\downarrow0}
\left(
A_\beta(u,r)-A_\gamma(u,r)
\right)
=
\nu(u,0)
\left(
L(\gamma)-L(\beta)
\right).
\]

In particular,
\[
\lim_{r\downarrow0}
\left(
S(u,r)-A_\beta(u,r)
\right)
=
L(\beta)\nu(u,0).
\]

This gives an exact additive recovery formula for every smooth radial regularization. If
\[
\rho\in C_c^\infty(B(1))
\]
is nonnegative and radial, with
\[
\int_{B(1)}\rho\,dV=1,
\]
set
\[
u_{\rho,r}(0)
=
\int_{\mathbb C^n}
u(-rw)\rho(w)\,dV(w)
\]
and
\[
L_\rho
=
\int_{B(1)}
-\log|w|\,\rho(w)\,dV(w).
\]
Then
\[
0<L_\rho<\infty
\]
and
\[
\lim_{r\downarrow0}
\left(
S(u,r)-u_{\rho,r}(0)
\right)
=
L_\rho\nu(u,0).
\]
Therefore
\[
\nu(u,0)
=
\frac{1}{L_\rho}
\lim_{r\downarrow0}
\left(
S(u,r)-u_{\rho,r}(0)
\right).
\]

The recent spherical-solid identity is the uniform-ball member of this family.

## Assumptions and scope

The Lelong number and spherical mean are normalized as in arXiv:2609.30999v1.

The radial probability measure \(\beta\) is allowed to be arbitrary on \((0,1]\), subject only to
\[
\int_{(0,1]}-\log t\,d\beta(t)<\infty.
\]
This condition is exactly what is needed for the dominated-convergence argument.

For the mollifier corollary, the kernel is smooth, nonnegative, radial, compactly supported in the open unit ball, and has total mass one.

The result concerns radial averages centered at the singular point. It does not assert an analogous formula for nonradial kernels.

## Proof

Put
\[
\phi(x)
=
S(u,e^x).
\]
The classical radial theory recalled in the recent source gives that \(\phi\) is increasing and convex, and
\[
\lim_{x\to-\infty}
\frac{\phi(x)}x
=
\nu(u,0).
\]

Fix
\[
s\ge0.
\]
For a convex function with asymptotic slope \(\nu(u,0)\) at \(-\infty\),
\[
\phi(x)-\phi(x-s)
\longrightarrow
\nu(u,0)s
\qquad
(x\to-\infty).
\]

We also need a bound uniform in \(s\). Choose \(x_0\) in the interval of definition. By convexity, every secant slope on an interval contained in
\[
(-\infty,x_0]
\]
is bounded above by a finite one-sided slope at \(x_0\). Hence there is
\[
C<\infty
\]
such that for all sufficiently negative \(x\) and every
\[
s\ge0,
\]
\[
0
\le
\phi(x)-\phi(x-s)
\le
Cs.
\]

Now take
\[
x=\log r
\]
and
\[
s=-\log t.
\]
For every fixed
\[
t\in(0,1],
\]
\[
S(u,r)-S(u,tr)
\longrightarrow
-\nu(u,0)\log t.
\]
The preceding bound gives
\[
0
\le
S(u,r)-S(u,tr)
\le
C(-\log t).
\]
Since
\[
L(\beta)<\infty,
\]
dominated convergence yields
\[
\begin{aligned}
\lim_{r\downarrow0}
\left(
S(u,r)-A_\beta(u,r)
\right)
&=
\int_{(0,1]}
\lim_{r\downarrow0}
\left(
S(u,r)-S(u,tr)
\right)
d\beta(t)
\\
&=
\nu(u,0)
\int_{(0,1]}
-\log t\,d\beta(t)
\\
&=
L(\beta)\nu(u,0).
\end{aligned}
\]

Subtracting the corresponding formulas for \(\beta\) and \(\gamma\) gives
\[
\lim_{r\downarrow0}
\left(
A_\beta(u,r)-A_\gamma(u,r)
\right)
=
\nu(u,0)
\left(
L(\gamma)-L(\beta)
\right).
\]

For a radial mollifier, let \(\beta_\rho\) be the pushforward of
\[
\rho(w)\,dV(w)
\]
under
\[
w\longmapsto |w|.
\]
Radial symmetry gives
\[
u_{\rho,r}(0)
=
A_{\beta_\rho}(u,r)
\]
and
\[
L(\beta_\rho)
=
L_\rho.
\]
Because the support lies in the open unit ball,
\[
L_\rho>0,
\]
and smoothness makes the logarithmic singularity integrable at the origin.

Finally, the normalized volume measure on the unit ball has radial density
\[
2n\,t^{2n-1}\,dt.
\]
Its logarithmic radius moment is
\[
2n\int_0^1
(-\log t)t^{2n-1}\,dt
=
\frac1{2n}.
\]
Thus the recent exact spherical-solid formula is recovered as a special case.

## Verification

The recent primary source was inspected at its definition of radial regularization, the convexity of spherical means on the logarithmic radius scale, the classical slope characterization of the Lelong number, its exact spherical-solid theorem, and the proof of its radial-regularization zero criterion.

That proof already writes a radial regularization as a probability-weighted average of spherical means:
\[
u_{\rho,r}(0)
=
\int_0^1
S(u,tr)\,\widetilde\rho(t)\,dt.
\]
The source uses this only when the Lelong number is zero. The present proof keeps the nonzero asymptotic slope and integrates the exact fixed-shift limit.

The logarithmic-moment domination is explicit and does not use numerical approximation, finite sampling, or an unproved exchange of limits.

The earlier Biard--Wu paper was also inspected at its Lelong-number slope formulas and VMO characterization. Its full-text search contains no radial-regularization or mollifier formula of the type proved here.

## Relationship to prior work

Deng, Yang, and You prove
\[
\lim_{r\downarrow0}
\left(
S(u,r)-V(u,r)
\right)
=
\frac{1}{2n}\nu(u,0)
\]
and characterize zero Lelong number through asymptotic agreement with radial regularizations. Their proof of the regularization criterion stops after showing that the gap tends to zero when the asymptotic slope is zero.

The present result identifies the exact nonzero limit for every radial probability kernel with finite logarithmic moment. It shows that the coefficient
\[
\frac1{2n}
\]
is not isolated: it is the logarithmic radius moment of normalized ball measure.

Biard and Wu characterize zero Lelong numbers through vanishing mean oscillation and recall the classical spherical-slope description. Their work does not state an exact additive radial-kernel formula.

Standard pluripotential references provide the slope description of Lelong numbers and regularization techniques, but targeted searches did not locate the pairwise kernel formula
\[
A_\beta-A_\gamma
\longrightarrow
\nu
\left(
L(\gamma)-L(\beta)
\right).
\]

## Limitations

The theorem requires radial averaging. A nonradial kernel can interact with directional singularity data that are invisible to the spherical mean.

The finite logarithmic moment assumption is essential for the stated dominated-convergence proof.

The result determines the limiting additive gap but not a convergence rate. Such a rate would require quantitative information on how fast the logarithmic radial slope approaches the Lelong number.

## References

1. F. Deng, Y. Yang, and Z. You, *An Exact Spherical--Solid Mean Formula and Vanishing Criteria for Lelong Numbers*, arXiv:2609.30999v1, 2026.
2. S. Biard and J. Wu, *Equivalence between VMO functions and plurisubharmonic functions with zero Lelong numbers*, arXiv:2403.03568; Mathematische Zeitschrift 312 (2026), Article 60.
3. J.-P. Demailly, *Complex Analytic and Differential Geometry*, online monograph.
4. C. O. Kiselman, *Attenuating the singularities of plurisubharmonic functions*, Annales Polonici Mathematici 60 (1994), 173--197.
