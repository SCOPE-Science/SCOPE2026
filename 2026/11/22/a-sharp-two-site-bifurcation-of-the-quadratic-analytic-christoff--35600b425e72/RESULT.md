# A sharp two-site bifurcation of the quadratic analytic Christoffel kernel on weighted ellipses

## Finding
Consider the three-dimensional analytic-polynomial subspace of degree at most two, with the probability-weighted area inner product on the interior of a noncircular ellipse. The diagonal Christoffel–Darboux kernel has its unique global minimum at the center for sufficiently round ellipses, but for sufficiently thin ellipses it instead has **exactly two** global minimizers, a symmetric pair strictly inside the major axis. This is a complete phase classification for every admissible weight exponent.

Let \(a>b>0\), \(\alpha>-1\), \(s=\alpha+2>1\), \(c^2=a^2-b^2\) and \(R=(a^2+b^2)/(a^2-b^2)>1\). Set
\[
D=2sR^2-1,\qquad P=2sR^2-2(s+1)R-1.
\]
The critical aspect ratio is
\[
\rho_*(\alpha)=\sqrt{\frac{R_*(s)-1}{R_*(s)+1}},\quad
R_*(s)=\frac{s+1+\sqrt{(s+1)^2+2s}}{2s}.
\]
Writing \(\rho=b/a\), the exact classification is:

* If \(\rho\ge\rho_*(\alpha)\), the origin is the unique global minimizer. At equality, the major-axis quadratic term vanishes and the first positive major-axis term is quartic.
* If \(0<\rho<\rho_*(\alpha)\), the two and only two global minimizers are \(z=\pm x_*\), where
\[
 x_*^2=\frac{-c^2P}{4s(s+1)R}>0.
\]
They lie strictly inside the ellipse, and the center is not a local minimum.

In both regimes the exact sharp minimum is
\[
\boxed{\min_{z\in E_{a,b}}K_2(z,z)
=1+\frac{s+1}{D}-\frac{(\max\{-P,0\})^2}{4(s+1)R^2D}.}
\]
Equivalently, the reciprocal Christoffel function \(\lambda_2(z)=1/K_2(z,z)\) has exactly the same maximizer sites. For the uniform-area ellipse \(\alpha=0\), the sharp transition is at
\[
R_*=(3+\sqrt{13})/4,\qquad \rho_*=0.4956592188330808\ldots.
\]
At the rationally parameterized critical example \(\alpha=2/3\), the transition occurs exactly at \(\rho=1/\sqrt5\).

## Assumptions and scope
The ellipse is \(E_{a,b}=\{x+iy:x^2/a^2+y^2/b^2<1\}\). Equip it with the probability measure
\[
 d\mu_\alpha(z)=\frac{\alpha+1}{\pi ab}
 \left(1-\frac{x^2}{a^2}-\frac{y^2}{b^2}\right)^\alpha dx\,dy.
\]
The analytic polynomial space is \(\mathcal P_2=\operatorname{span}_{\mathbb C}\{1,z,z^2\}\), and its kernel is \(K_2(z,w)=\sum_{j=0}^2p_j(z)\overline{p_j(w)}\) for any orthonormal basis. The optimization is over the open ellipse, but every claimed minimizer belongs to the interior; the sharp minimum and equality classification remain valid on the closure. The case \(a=b\) follows by a continuous limit and has the center as its unique minimum, but is not required for the noncircular formula. All assertions are pointwise, exact, and uniform in the stated parameters; they make no assertion for degree at least three, real bivariate polynomial spaces, or the infinite Bergman kernel.

## Proof
**Step 1: exact orthogonal basis.** Under \(z=au+ibv\), the induced law on the unit disk is radially symmetric with density \((\alpha+1)(1-u^2-v^2)^\alpha/\pi\). Beta integration yields
\[
 \mathbb E(u^2)=\mathbb E(v^2)=\frac1{2s},\quad
 \mathbb E(u^4)=\mathbb E(v^4)=\frac3{4s(s+1)},\quad
 \mathbb E(u^2v^2)=\frac1{4s(s+1)}.
\]
Consequently
\[
 m=\mathbb E z^2=\frac{c^2}{2s},\quad
 v_1=\mathbb E|z|^2=\frac{c^2R}{2s},\quad
 v_2=\mathbb E|z^2-m|^2=\frac{c^4D}{4s^2(s+1)}.
\]
Central symmetry gives orthogonality of \(z\) to both \(1\) and \(z^2-m\); the choice of \(m\) gives orthogonality of the latter to \(1\). Thus \(1,z/\sqrt{v_1},(z^2-m)/\sqrt{v_2}\) is an orthonormal basis, with all three squared norms positive because \(s>1\) and \(R>1\).

**Step 2: the exact quartic diagonal.** Direct substitution gives
\[
 K_2(z,z)=1+\frac{2s}{c^2R}|z|^2
 +\frac{s+1}{D}\left|\frac{2sz^2}{c^2}-1\right|^2.
\]
For \(z=x+iy\), define
\[
 K_0=1+\frac{s+1}{D},\quad
 A=\frac{2sP}{c^2RD},\quad
 B=\frac{2s}{c^2}\left(\frac1R+\frac{2(s+1)}D\right),\quad
 C=\frac{4s^2(s+1)}{c^4D}.
\]
Then
\[
 K_2(x+iy,x+iy)=K_0+Ax^2+By^2+C(x^2+y^2)^2,
 \qquad B-A=\frac{8s(s+1)}{c^2D}>0,
\]
with \(B,C>0\) and \(\operatorname{sign}(A)=\operatorname{sign}(P)\).

**Step 3: unique aspect threshold.** The polynomial \(P(R)=2sR^2-2(s+1)R-1\) has \(P(1)=-3\) and the product of its two roots is negative. Hence it has exactly one positive root and is negative below this positive root. Its positive root is precisely \(R_*(s)>1\) above. Since \(R=(1+\rho^2)/(1-\rho^2)\) strictly increases with \(\rho\), \(P\ge0\) exactly when \(\rho\ge\rho_*\). (For clarity, no positivity of \(P'\) on the entire interval is needed.)

**Step 4: global minima and exact certificates.** If \(P\ge0\) then \(A\ge0\), and \(K_2-K_0=Ax^2+By^2+C(x^2+y^2)^2\ge0\), with equality only at \((x,y)=(0,0)\); when \(P=0\) the lowest nonzero term along the major axis is \(Cx^4\). If \(P<0\), set \(x_*^2=-A/(2C)=-c^2P/[4s(s+1)R]\). Completing the square gives the **global**, not merely local, identity
\[
 K_2-K_{\min}=C(x^2+y^2-x_*^2)^2+(B-A)y^2,
 \qquad K_{\min}=K_0-\frac{A^2}{4C}.
\]
Both terms vanish exactly when \(y=0\) and \(x=\pm x_*\). These sites are interior: since \(-P=2(s+1)R+1-2sR^2<2(s+1)R\),
\[
0<\frac{x_*^2}{a^2}<\frac{1}{s(R+1)}<1,
\]
using \(a^2=c^2(R+1)/2\). Inserting \(A,C\) proves the displayed sharp minimum. When \(P<0\), \(K_2-K_0\) is negative for sufficiently small nonzero real \(x\), so the center is not a local minimum. The degree-zero kernel is constant, whereas the degree-one kernel \(1+|z|^2/v_1\) has its unique minimum at zero, establishing that degree two is the first polynomial degree with this symmetry-breaking possibility.

## Verification
The accompanying stand-alone Python standard-library checker `CHECK.py` evaluates the moment identities, kernel expansion, global sum-of-squares certificates, parameter signs, and interior location using exact rational arithmetic for 84 independent triples of parameters, together with the exact critical case \((s,R)=(8/3,3/2)\). It prints `PASS: 3867 exact arithmetic and endpoint checks` when executed. These checks test the formulas only; the universal parameter quantifiers and uniqueness follow from the symbolic proof above.

## Relationship to prior work
Akemann, Nagao, Parra and Vernizzi established weighted elliptical orthogonality of planar Gegenbauer polynomials in the preprint first publicly dated 7 May 2019 and its subsequently published open-access article. Their paper supplies the general orthogonal-polynomial setting and discusses finite Christoffel–Darboux kernels, but the inspected text does not present the sharp global diagonal-minimum aspect threshold, pair of off-center minimizers, or the exact quartic-flat critical case. Beckermann, Putinar, Saff and Stylianopoulos developed the general Christoffel–Darboux kernel and leverage-score framework, particularly perturbations of measures; their work does not provide this fixed weighted-ellipse extremizer classification. The present statement is a specialized *finite analytic* kernel theorem, not a theorem about two-real-variable Christoffel functions or about zeros of the off-diagonal kernel.

## Limitations
Historical priority is best-knowledge, not an exhaustive proof that no equivalent lower-order moment calculation was previously recorded. An elementary derivation from the known degree-two orthogonal Gegenbauer basis might be available elsewhere without using the present threshold terminology. Numerical tests are not a substitute for the all-parameter analytic identity. No independent mathematical review or external validation has been performed. The domain is a noncircular ellipse, degree exactly two, and power weight \(\alpha>-1\); the phenomenon is not asserted for other domains or higher degrees.

## References
1. G. Akemann, T. Nagao, I. Parra, G. Vernizzi, *Gegenbauer and other planar orthogonal polynomials on an ellipse in the complex plane*, arXiv:1905.02397 (first version 7 May 2019), https://arxiv.org/abs/1905.02397 ; *Constructive Approximation* 53 (2021), 441–478, https://doi.org/10.1007/s00365-020-09515-0 (open access).
2. B. Beckermann, M. Putinar, E. B. Saff, N. Stylianopoulos, *Perturbations of Christoffel–Darboux kernels. I: detection of outliers*, arXiv:1812.06560 (first version 16 December 2018), https://arxiv.org/abs/1812.06560.
3. E. Pauwels, F. Bach, J.-P. Vert, *Relating Leverage Scores and Density using Regularized Christoffel Functions*, arXiv:1805.07943 (first version 21 May 2018), https://arxiv.org/abs/1805.07943 (conceptual motivation; different regularized setting).
