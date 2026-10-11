# Exact mode-capacity boundaries for generalized entangled coherent-state metrology

## Finding

Consider the generalized entangled coherent state used by Liu, Lu, Sun, and Wang,
\[
|\psi_\alpha\rangle
=
b\sum_{m=1}^d|\alpha\rangle_m+c|\alpha\rangle_0,
\]
with
\[
x=|\alpha|^2\ge1,\qquad d\ge2.
\]
The source derives unconstrained coefficients that minimize the trace of the inverse quantum Fisher information matrix, but those coefficients are usable only when they lie inside the normalization ellipse for the state.

Put
\[
t=e^{-x}.
\]
The source's normalization coefficients satisfy
\[
A=d+d(d-1)t,\qquad B=2dt,
\]
and its geometric bound
\[
|b|\le\Gamma=\frac{2}{\sqrt{4A-B^2}}
\]
simplifies exactly to
\[
\Gamma^{-2}
=
d(1-t)(1+dt).
\]

For the linear phase generators, the source's unconstrained optimum is
\[
b_L^2
=
\frac{1+x^{-1}}{d+\sqrt d}.
\]
For the nonlinear quadratic generators, write
\[
f(x)=x^3+6x^2+7x+1,
\qquad
g(x)=x(x+1)^2.
\]
The source's unconstrained optimum is
\[
b_N^2
=
\frac{f(x)}{g(x)(d+\sqrt d)}.
\]

Define, for positive \(A,B,C\),
\[
\mathcal R(A,B,C)
\]
to be the unique positive root of
\[
As^3+Bs-C=0.
\]
Equivalently,
\[
\mathcal R(A,B,C)
=
2\sqrt{\frac{B}{3A}}
\sinh\!\left[
\frac13\operatorname{arsinh}\!\left(
\frac{3C}{2B}\sqrt{\frac{3A}{B}}
\right)
\right].
\]

Then the source's linear optimum is physically normalizable exactly when
\[
\boxed{d\le R_L(x)^2},
\]
where
\[
R_L(x)
=
\mathcal R\!\left(
(x+1)t(1-t),
\,1-(x+1)t,
\,x
\right).
\]

Likewise, the nonlinear optimum is physically normalizable exactly when
\[
\boxed{d\le R_N(x)^2},
\]
where
\[
R_N(x)
=
\mathcal R\!\left(
f(x)t(1-t),
\,f(x)(1-t)-g(x),
\,g(x)
\right).
\]

Thus, for fixed coherent amplitude, the exact largest admissible integer phase counts are
\[
\left\lfloor R_L(x)^2\right\rfloor
\quad\text{and}\quad
\left\lfloor R_N(x)^2\right\rfloor,
\]
provided the respective floor is at least \(2\).

The asymptotic capacities are sharply different:
\[
R_L(x)^2\sim x^2,
\qquad
R_N(x)^2\sim\frac{x^2}{16}
\qquad
(x\to\infty).
\]
Because \(x=|\alpha|^2\), this is
\[
d_{\max,L}\sim|\alpha|^4,
\qquad
d_{\max,N}\sim\frac{|\alpha|^4}{16}.
\]
Hence, at fixed large coherent amplitude, the linear protocol can realize its formal optimum for asymptotically sixteen times as many unknown phases as the nonlinear protocol.

For the experimentally illustrative amplitude
\[
|\alpha|=4,
\]
the exact boundary brackets give
\[
255<R_L(16)^2<256
\]
and
\[
17<R_N(16)^2<18.
\]
Therefore
\[
\boxed{d_{\max,L}=255,\qquad d_{\max,N}=17}.
\]

## Assumptions and scope

The result concerns exactly the generalized entangled coherent-state family and the two local parameterizations analyzed in the source. It uses the source assumptions
\[
|\alpha|\ge1,\qquad d\ge2,
\]
with real state coefficients \(b,c\).

“Physically normalizable” means that the source normalization equation admits a real \(c\) for the displayed optimal \(b\). This is equivalent to \(|b|\le\Gamma\).

The result classifies feasibility of the source's *formal unconstrained optimum*. It does not alter the source's quantum Fisher information matrices, prove attainability of the quantum Cramér--Rao bound by a particular detector, include photon loss, or optimize over different probe-state families.

## Proof

The source normalization equation is
\[
Ab^2+Bbc+c^2=1,
\]
with
\[
A=d+d(d-1)t,\qquad B=2dt,\qquad t=e^{-x}.
\]
Viewed as a quadratic equation in \(c\), it has a real solution exactly when
\[
B^2b^2-4(Ab^2-1)\ge0.
\]
Thus
\[
b^2\le\frac{4}{4A-B^2}=\Gamma^2.
\]
A direct simplification gives
\[
\Gamma^{-2}
=
A-\frac{B^2}4
=
d(1-t)(1+dt).
\]

Let
\[
s=\sqrt d.
\]
For the linear optimum,
\[
b_L^2=\frac{x+1}{x\,s(s+1)}.
\]
The condition \(b_L^2\le\Gamma^2\) is equivalent, after multiplying by positive quantities, to
\[
(x+1)t(1-t)s^3+
\bigl[1-(x+1)t\bigr]s-x
\le0.
\]
Set
\[
A_L=(x+1)t(1-t),
\qquad
B_L=1-(x+1)t.
\]
For \(x\ge1\),
\[
A_L>0
\]
and
\[
B_L>0,
\]
because
\[
e^x>x+1.
\]
Therefore
\[
A_Ls^3+B_Ls-x
\]
is strictly increasing for \(s\ge0\), starts negative, and tends to \(+\infty\). It has exactly one positive root \(R_L(x)\), and the linear optimum is feasible exactly for
\[
s\le R_L(x),
\]
which is the stated condition.

For the nonlinear optimum, define
\[
f=x^3+6x^2+7x+1,
\qquad
g=x(x+1)^2.
\]
The condition
\[
\frac{f}{g\,s(s+1)}\le\Gamma^2
\]
is equivalent to
\[
f\,t(1-t)s^3+
\bigl[f(1-t)-g\bigr]s-g
\le0.
\]
The cubic coefficient is positive. For the linear coefficient, note that
\[
f-g=4x^2+6x+1.
\]
It remains to show
\[
f(1-t)-g>0.
\]
Equivalently,
\[
e^x(4x^2+6x+1)-f>0.
\]
At \(x=1\) this quantity is positive. Its derivative is
\[
e^x(4x^2+14x+7)-(3x^2+12x+7),
\]
which is positive for \(x\ge1\), since \(e^x>1\) and
\[
(4x^2+14x+7)-(3x^2+12x+7)=x^2+2x>0.
\]
Therefore the nonlinear cubic is also strictly increasing on \(s\ge0\), and it has exactly one positive root \(R_N(x)\). This proves the exact nonlinear boundary.

For the large-amplitude behavior, the linear cubic has coefficients
\[
A_L=O(xe^{-x}),
\qquad
B_L=1+O(xe^{-x}),
\]
so its positive root obeys
\[
R_L(x)=x+O(x^4e^{-x}).
\]
Hence
\[
R_L(x)^2\sim x^2.
\]

For the nonlinear cubic, first set \(t=0\). Its positive root is then
\[
\frac{g}{f-g}
=
\frac{x(x+1)^2}{4x^2+6x+1}
=
\frac1004+\frac18+O(x^{-2}).
\]
Restoring \(t=e^{-x}\) perturbs this root by
\[
O(x^4e^{-x}).
\]
Thus
\[
R_N(x)
=
\frac1004+\frac18+
O(x^{-2}+x^4e^{-x}),
\]
and therefore
\[
R_N(x)^2\sim\frac{x^2}{16}.
\]

## Verification

`verify_ecs_capacity.py` independently reconstructs \(\Gamma\), the two source optima, and both cubic feasibility conditions. It verifies their equivalence for a deterministic grid of amplitudes and phase counts.

The script also checks strict monotonicity of each cubic, the exact integer brackets at \(|\alpha|=4\), and the asymptotic capacity ratio on increasing amplitudes. It prints `VERIFY_OK`.

The finite calculations are supplementary. The all-\(x\), all-\(d\) classification follows from the monotone cubic proof above.

## Relationship to prior work

Liu, Lu, Sun, and Wang introduce the generalized entangled coherent state, derive the normalization ellipse and the bound \(|b|\le\Gamma\), and then derive separate unconstrained optimal values for the linear and nonlinear quantum Fisher information matrices.

For the linear protocol, they plot the region where the formal optimum lies inside the normalization ellipse and state qualitatively that sufficiently large coherent amplitude makes the optimum reachable. For the nonlinear protocol, they give the analogous plot and note that a larger amplitude is required; in the displayed moderate parameter regime they describe \(|\alpha|\) “larger than around \(4\)” as sufficient.

The exact cubic phase boundaries above replace those graphical regions by analytic criteria valid for every
\[
x\ge1,\qquad d\ge2.
\]
They also expose a scaling distinction that is not visible from the source's statement that the *formal optimized variances* have the same dependence on the number of parameters: the *normalization-feasible parameter capacity* is asymptotically sixteen times larger for the linear optimum.

Humphreys, Barbieri, Datta, and Walmsley establish the multiphase \(O(d)\) advantage for generalized NOON probes that motivates the coherent-state comparison. Later multiphase-metrology work continues to study probe design and loss, but targeted searches did not locate the two cubic feasibility boundaries or the factor-\(16\) capacity law for this generalized entangled coherent-state family.

## Limitations

The capacity boundary concerns normalization feasibility of the coefficient that minimizes the source's inverse-QFIM trace. It does not guarantee saturation by a specified measurement apparatus.

The result uses the source's real-coefficient generalized coherent-state ansatz and the range \(|\alpha|\ge1\). It does not optimize over arbitrary complex superposition weights or other coherent-state architectures.

The asymptotic factor \(16\) concerns the maximum phase count at fixed coherent amplitude, not a factor-\(16\) difference in estimation variance.

A residual literature risk remains because the boundary follows from algebraic elimination of the source's normalization constraint and may have appeared in unindexed notes or later work using different notation.

## References

1. J. Liu, X.-M. Lu, Z. Sun, and X. Wang, “Quantum multiparameter metrology with generalized entangled coherent state,” arXiv:1409.6167, first submitted 22 September 2014; *Journal of Physics A: Mathematical and Theoretical* 49 (2016), 115302, DOI: 10.1088/1751-8113/49/11/115302.
2. P. C. Humphreys, M. Barbieri, A. Datta, and I. A. Walmsley, “Quantum Enhanced Multiple Phase Estimation,” arXiv:1307.7653; *Physical Review Letters* 111 (2013), 070403, DOI: 10.1103/PhysRevLett.111.070403.
