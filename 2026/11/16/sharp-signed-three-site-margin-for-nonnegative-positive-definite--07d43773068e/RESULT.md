# Sharp signed three-site margin for nonnegative positive-definite functions

## Finding
For every dimension \(d\ge1\), normalized continuous nonnegative real positive-definite \(f\) satisfies the sharp signed three-site inequality
\[
(-1,1,1)K_f(0,x,-x)(-1,1,1)^{\mathsf T}=3-4f(x)+2f(2x)\ge\tfrac12.
\]
The constant is attained. The full equality class is characterized through Bochner spectral phase support, with an exact nonnegative deficit formula and an immediate near-equality concentration bound.

## Assumptions and scope
The function \(f:\mathbb R^d\to[0,\infty)\), \(d\in\mathbb N\), is continuous, real valued and positive definite, with \(f(0)=1\). The site \(x\in\mathbb R^d\) is arbitrary. Put \(X_0=0\), \(X_1=x\), \(X_2=-x\); \(K_{ij}=f(X_i-X_j)\). The tested vector is \(c=(-1,1,1)^{\mathsf T}\). No statement about arbitrary configurations, all coefficient vectors, or the full Loewner order is asserted.

By Bochner's theorem there is a symmetric probability measure \(\mu\) on \(\mathbb R^d\) such that \(f(y)=\int\cos\langle\xi,y\rangle\,d\mu(\xi)\). Symmetric means invariant under \(\xi\mapsto-\xi\).

## Proof
Write \(u=\cos t\). The elementary exact polynomial identity
\[
\frac54-2\cos t+\cos(2t)-\frac14\cos(3t)=\frac14(1-u)(2u-1)^2\ge0
\]
holds for every real \(t\), since \(-1\le u\le1\). Integrating at \(t=\langle\xi,x\rangle\) yields
\[
\frac54-2f(x)+f(2x)-\frac14f(3x)
=\frac14\int(1-u)(2u-1)^2\,d\mu(\xi).
\]
Here \(u=\cos\langle\xi,x\rangle\). Rearrangement, using \(f(3x)\ge0\), proves the stronger exact defect decomposition
\[
 c^{\mathsf T}Kc-\frac12
 =\frac12 f(3x)+\frac12\int(1-u)(2u-1)^2\,d\mu(\xi)\ge0.
\]
Equality forces both nonnegative summands to vanish. The integral vanishes if and only if \(u=1\) or \(u=1/2\) almost surely. On these phase classes, \(\cos(3t)\) equals \(1\) and \(-1\), respectively, so \(f(3x)=0\) is equivalent to equal class masses. The converse is immediate.

Sharpness: choose \(d=1\), \(f(t)=(1+\cos t)/2\), and \(x=\pi/3\). This is a nonnegative continuous positive-definite function, with spectral probabilities \(\mu=\frac12\delta_0+\frac14\delta_{1}+\frac14\delta_{-1}\). Its values are \(f(x)=3/4\), \(f(2x)=1/4\), and \(f(3x)=0\). Therefore \(c^{\mathsf T}Kc=1/2\) exactly.

If the defect is at most \(\varepsilon\), each nonnegative summand in the identity is at most \(\varepsilon\). Thus \(f(3x)\le2\varepsilon\), and \(\int(1-u)(2u-1)^2d\mu\le2\varepsilon\). More generally for a fixed \(\eta>0\), the spectral probability of the set where both \(|u-1|\ge\eta\) and \(|u-1/2|\ge\eta\) is at most \(2\varepsilon/m_\eta\), where \(m_\eta\) is the minimum of \((1-u)(2u-1)^2\) over that closed subset of \([-1,1]\) (if nonempty), and \(m_\eta>0\).

## Verification
The included standalone checker performs rational polynomial expansion of the trigonometric identity after substituting the Chebyshev polynomials of degrees two and three. It verifies the exact rational three-site matrix, example values, and equality of the defect. The analytical proof, not numerical sampling, establishes the result in every dimension and for every admissible measure.

## Relationship to prior work
Vybíral's 2026 counterexample to the Hinrichs–Vybíral conjecture concerns a **different**, unrestricted eight-site matrix inequality and exhibits an eight-point failure. The present result is an exact sharp *signed single-vector* lower bound on a fixed three-site arithmetic progression and does not settle full three-point Loewner positivity. The paper by Pevnyi and Sitnik (2016) proves Krein–Linnik–Gorin inequalities for general positive-definite functions, with different combinations and no exact displayed sharp nonnegative-function three-site spectral deficit in the inspected full text. An indexed published one-circle compression of the eight-point counterexample likewise does not imply this three-site lower bound. The original 2011 Hinrichs–Vybíral article and older specialty correlation inequalities are residual sources of possible equivalent formulations; this comparison is not an independence certification.

## Limitations
The result is restricted to the symmetric progression \((0,x,-x)\) and vector \((-1,1,1)\). It does not establish the previously conjectured matrix Loewner order for arbitrary samples. The spectral equality description presupposes the stated global nonnegativity of \(f\); a measure satisfying only its phase support condition need not define a globally nonnegative function. Independently established novelty is not claimed.

## References
1. J. Vybíral, *An explicit counterexample to the Hinrichs--Vybiral conjecture*, arXiv:2609.21733 (first publicly submitted September 18, 2026), https://arxiv.org/html/2609.21733v1.
2. A. Hinrichs and J. Vybíral, *On positive positive-definite functions and Bochner's theorem*, Journal of Complexity 27 (2011), 264–272.
3. A. B. Pevnyi and S. M. Sitnik, *Inequalities of M. G. Krein, Yu. V. Linnik and E. A. Gorin for positive definite functions*, arXiv:1609.01218 (2016), https://arxiv.org/abs/1609.01218.
4. *Sharp odd-base transition for a positive-definite Fourier kernel on the circle*, indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-odd-base-transition-for-a-positive-definite-fourier-kernel--6c4e2ef6b84c.
