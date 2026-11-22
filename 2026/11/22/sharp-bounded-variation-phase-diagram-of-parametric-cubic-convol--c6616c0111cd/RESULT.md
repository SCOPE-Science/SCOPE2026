# Sharp bounded-variation phase diagram of parametric cubic convolution interpolation

## Finding

Let \(\lambda\in\mathbb R\). The exact total-variation amplification of the classical one-parameter, four-tap cardinal cubic convolution interpolator is
\[
\boxed{\|C_\lambda\|_{\mathrm{TV}_d\to\mathrm{TV}}=\frac{16|\lambda|}{27}+J(\lambda)}
\]
with
\[
J(\lambda)=\begin{cases}
-1+\frac23(3-\lambda)\sqrt{\frac{3-\lambda}{3(1-\lambda)}},&\lambda<0,\\
1,&0\le\lambda\le3,\\
1+\frac23(\lambda-3)\sqrt{\frac{\lambda-3}{3(\lambda-1)}},&\lambda>3.
\end{cases}
\]
Every parameter has an exact single-jump extremizer. The middle-cell derivative is nonnegative throughout precisely for \(0\le\lambda\le3\); at \(\lambda=3\) it first acquires a double zero. Beyond this threshold the additional variation over the affine branch is the explicit fractional-power cusp
\[
\frac{2(\lambda-3)^{3/2}}{3\sqrt{3(\lambda-1)}},\qquad \lambda>3.
\]
At the standard cubic-convolution parameter \(\lambda=1/2\), the gain is \(35/27\). Among all real parameters the unique nonexpansive member is \(\lambda=0\), which loses affine reproduction.

## Assumptions and scope

Data \(y=(y_i)_{i\in\mathbb Z}\) are arbitrary real two-sided sequences with discrete total variation
\[
V_d(y)=\sum_{i\in\mathbb Z}|y_{i+1}-y_i|<\infty.
\]
Such sequences have finite limits at both ends. On every integer cell \([i,i+1]\), the interpolant \(C_\lambda y\) is the cubic Hermite polynomial with endpoint data \(y_i,y_{i+1}\) and endpoint derivatives
\[
d_i=\lambda(y_{i+1}-y_{i-1}),\qquad d_{i+1}=\lambda(y_{i+2}-y_i).
\]
This uniquely determines a globally \(C^1\) piecewise-cubic function. We measure continuous total variation by \(\operatorname{Var}(C_\lambda y)=\int_{\mathbb R}|(C_\lambda y)'(t)|\,dt\). The norm is over nonconstant data of finite discrete variation. The operator is linear and preserves constants; consequently its sharp two-input coefficient is the same number.

## Proof

**Step reduction.** Let \(s_i\) be the discrete step that vanishes at indices at most \(i\) and equals one at indices at least \(i+1\). Writing \(\Delta_i=y_{i+1}-y_i\), finite variation gives the uniformly convergent identity
\[
y=y_{-\infty}+\sum_{i\in\mathbb Z}\Delta_i s_i.
\]
The cubic reconstruction of a constant is the same constant, and translation commutes with reconstruction. If \(H_\lambda=C_\lambda s_0\), then \(H_\lambda'\) is compactly supported and
\[
(C_\lambda y)'=\sum_i\Delta_i H_\lambda'(\cdot-i)
\]
with convergence in \(L^1\). The triangle inequality gives \(\operatorname{Var}(C_\lambda y)\le\operatorname{Var}(H_\lambda)V_d(y)\). Equality holds for a unit step, so calculating this single response is sufficient and exact. In particular, finite numerical tests are not used to justify this reduction.

**Three active cells.** For the step \(s_0\), put \(t=x-i\in[0,1]\) in each cell. On the left cell \([-1,0]\), the reconstruction is \(-\lambda t^2(1-t)\); on the central cell \([0,1]\), it is
\[
p_\lambda(t)=(2\lambda-2)t^3+(3-3\lambda)t^2+\lambda t;
\]
and on the right cell \([1,2]\), it is \(1+\lambda t(1-t)^2\). Outside these cells it is constant. Each side cell has variation \(8|\lambda|/27\), since \(\max_{0\le t\le1}t^2(1-t)=4/27\). This supplies the total side contribution \(16|\lambda|/27\).

**Critical-point classification.** The central derivative is
\[
p_\lambda'(t)=\lambda+6(1-\lambda)t(1-t).
\]
For \(0\le\lambda\le3\) it is nonnegative on the whole cell, and the central variation is one. If \(\lambda<0\) or \(\lambda>3\), write
\[
q_\lambda=\sqrt{\frac{3-\lambda}{3(1-\lambda)}},\qquad a_\lambda=\frac{1-q_\lambda}2,
\]
so the two interior derivative zeros are \(a_\lambda\) and \(1-a_\lambda\). Direct substitution yields
\[
p_\lambda(a_\lambda)=\frac12+\frac{(\lambda-3)q_\lambda}6,\qquad
p_\lambda(1-a_\lambda)=1-p_\lambda(a_\lambda).
\]
For \(\lambda<0\) the first is a negative local minimum and the second is a maximum above one; the central variation is \(1-4p_\lambda(a_\lambda)= -1+\frac23(3-\lambda)q_\lambda\). For \(\lambda>3\) the first is a local maximum greater than \(1/2\) and the second a local minimum smaller than \(1/2\); the central variation is \(4p_\lambda(a_\lambda)-1=1+\frac23(\lambda-3)q_\lambda\). Adding the three cells proves the stated piecewise exact norm.

**Consequences and boundaries.** For nonzero \(\lambda\) the side contribution is positive, and the central variation is at least one, hence the norm exceeds one. For \(\lambda=0\) the piecewise cubic is the monotone smoothstep on each cell and has variation exactly \(V_d(y)\). On affine data \(y_i=ai+b\), the assigned derivative equals \(2\lambda a\); therefore affine reproduction occurs exactly at \(\lambda=1/2\), giving \(1+8/27=35/27\). At \(\lambda=3\), the derivative has one double zero at \(t=1/2\), while for larger values it has two distinct interior zeros and produces the stated \((\lambda-3)^{3/2}\) excess.

## Verification

The standalone script `verify.py` evaluates the exact critical-point formula for each Hermite cell, checks the proposed norm with explicit step extremizers for eighteen negative, positive, zero and transition-adjacent parameter values, and compares 2,160 random real finite-input examples with the rigorous bound. It also checks rational special values and the derived stationary-point identities. To reproduce, execute `python verify.py` with Python 3 (standard library only). The checker's finite sample tests supplement the preceding analytic proof and do not certify untested parameter values by enumeration.

## Relationship to prior work

Keys' 1981 paper derives the one-parameter cubic convolution family and its approximation-order properties, including the parameter \(a=-\lambda\) in the conventional kernel notation. Park and Schowengerdt (1983) study a parametric family's frequency-domain reconstruction tradeoffs. Meijering and Unser (2003) identify historical osculatory equivalences, especially the standard \(\lambda=1/2\) kernel. Those are the objects and formulas used here; the claim made here is the exact induced bounded-variation seminorm and its complete parameter threshold, not the invention of the interpolation kernel. An earlier specific-parameter calculation of \(35/27\) is already covered; its reappearance here is a consistency check, not a separate novelty claim.

## Limitations

The result is one-dimensional, cardinal, four-tap, real and bi-infinite. It does not apply automatically to finite-grid boundary closures, nonuniform knots, two-dimensional image variation or six-tap higher-order cubic convolution. The 1983 frequency-domain source was not readable in full in this investigation, so historical-priority uncertainty remains. In particular the statement is not an independent priority determination.

## References

1. R. G. Keys, *Cubic Convolution Interpolation for Digital Image Processing*, IEEE Trans. Acoust. Speech Signal Process. 29 (1981), 1153–1160. DOI: 10.1109/TASSP.1981.1163711. Publicly readable copy: https://ncorr.com/download/publications/keysbicubic.pdf
2. S. K. Park and R. A. Schowengerdt, *Image Reconstruction by Parametric Cubic Convolution*, Computer Vision, Graphics, and Image Processing 23 (1983), 258–272. DOI: 10.1016/0734-189X(83)90026-9. Bibliography and abstract: https://ntrs.nasa.gov/citations/19830065032
3. E. Meijering and M. Unser, *A Note on Cubic Convolution Interpolation*, IEEE Trans. Image Process. 12 (2003), 477–479. DOI: 10.1109/TIP.2003.811493. https://bigwww.epfl.ch/publications/meijering0301.pdf
