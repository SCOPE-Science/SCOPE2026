# A logarithmic acute-triangle law and conditional shape limit for thin ellipses

## Finding
Let \(E_\varepsilon=\{(x,y):x^2+y^2/\varepsilon^2=1\}\), where \(0<\varepsilon<1\). Independently choose three points with **normalized Euclidean arclength** on \(E_\varepsilon\); let \(A_\varepsilon\) be the event that their Euclidean triangle has all three angles strictly acute. Then
\[
\boxed{\Pr(A_\varepsilon)\sim 2\varepsilon^2\log(1/\varepsilon)}\qquad (\varepsilon\downarrow0).
\]
There is also a joint limit for the rare acute triangles. Sort their three first coordinates as \(X_1<X_2<X_3\), write \(s=X_2-X_1\), \(t=X_3-X_2\), and let \(\sigma_i\in\{-1,1\}\) be the sign of the second coordinate of the point having first coordinate \(X_i\). Define
\[
\Lambda_\varepsilon=\frac{\log s}{\log\varepsilon},\qquad
U_\varepsilon=\frac{st}{4\varepsilon^2(1-X_2^2)}.
\]
Conditionally on \(A_\varepsilon\), the tuple \((X_2,\Lambda_\varepsilon,U_\varepsilon,\sigma_1,\sigma_2,\sigma_3)\) converges in distribution to \((X,\Lambda,U,\Sigma,-\Sigma,\Sigma)\), where the four variables on the right are mutually independent, \(X\) has density \(\tfrac34(1-x^2)\) on \((-1,1)\), \(\Lambda\) is uniform on \((0,2)\), \(U\) is uniform on \((0,1)\), and \(\Sigma\) is fair on \(\{-1,1\}\). Thus two opposite-branch endpoints accompany the middle-branch point with asymptotic probability one, and the logarithmic allocation between the two horizontal gaps is uniform.

## Assumptions and scope
The ellipse has horizontal semiaxis one and vertical semiaxis \(\varepsilon\). Arclength means one-dimensional Euclidean Hausdorff measure normalized by the entire perimeter, **not** uniform eccentric anomaly or affine arclength. The sampling is independent. Strictly right and coincident configurations have probability zero. Limits are taken with \(\varepsilon\to0^+\); no uniform finite-\(\varepsilon\) error constant is asserted.

## Proof
**1. Coordinates and a comparison measure.** Write \(f(x)=\sqrt{1-x^2}\). A point of the ellipse has coordinates \((x,\varepsilon\sigma f(x))\) with sign \(\sigma=\pm1\). Under arclength sampling, \(\sigma\) is fair and independent of \(x\), whose density is
\[
q_\varepsilon(x)=\frac{w_\varepsilon(x)}{I_\varepsilon},\quad
w_\varepsilon(x)=\sqrt{1+\frac{\varepsilon^2 x^2}{1-x^2}},\quad
I_\varepsilon=\int_{-1}^1 w_\varepsilon(x)\,dx.
\]
The bound \(0\le\sqrt{1+u}-1\le\min(u/2,\sqrt u)\), split at \(1-|x|=\varepsilon^2\), gives \(I_\varepsilon-2=O(\varepsilon^2\log(1/\varepsilon))\). Consequently
\[
q_\varepsilon=(1-\alpha_\varepsilon)q_0+\alpha_\varepsilon h_\varepsilon,\qquad
q_0=\tfrac12,\quad
\alpha_\varepsilon=\frac{I_\varepsilon-2}{I_\varepsilon}=O(\varepsilon^2\log(1/\varepsilon)),
\]
where \(h_\varepsilon=(w_\varepsilon-1)/(I_\varepsilon-2)\) is a probability density. We first prove the result with \(x\) uniform and then transfer it to arclength.

**2. The necessary product constraint.** Under the uniform-\(x\) model, sort \(x_1<x_2<x_3\) and put \(x=x_2\), \(s=x_2-x_1\), \(t=x_3-x_2\). The ordered triple has density \(3/4\) with respect to \(dx\,ds\,dt\), and its three signs are independent fair bits. At the middle point the scalar product of the two incident vectors is
\[
-st+\varepsilon^2(\sigma_1 f(x-s)-\sigma_2 f(x))(\sigma_3 f(x+t)-\sigma_2 f(x)).
\]
Acuteness forces this quantity to be positive, hence \(st<4\varepsilon^2\), regardless of signs. The Lebesgue area of \(\{(s,t)\in(0,2)^2:st<4\varepsilon^2\}\) is \(O(\varepsilon^2\log(1/\varepsilon))\). In particular, this is a bound for the acute probability *conditional on any one of the three first coordinates and its sign*, when the other two first coordinates are uniform; the three possible placements of the fixed coordinate each have a unit-Jacobian \((s,t)\) parameterization.

**3. Only one sign pattern survives logarithmically.** The function \(f\) obeys \(|f(u)-f(v)|\le\sqrt{2|u-v|}\). If exactly one neighbor has the middle sign, the positive part of the second term's coefficient is at most \(2\sqrt{2s}\), or \(2\sqrt{2t}\), respectively. The corresponding set satisfies \(t\le C\varepsilon^2/\sqrt{s}\), or its transpose, and has area \(O(\varepsilon^2)\). If all signs coincide, the coefficient is at most \(2\sqrt{st}\); the event forces \(st<4\varepsilon^4\), of area \(O(\varepsilon^4\log(1/\varepsilon))\). Thus only the two sign choices
\[
(\sigma_1,\sigma_2,\sigma_3)=(\sigma,-\sigma,\sigma)
\]
can contribute to the leading \(\varepsilon^2\log(1/\varepsilon)\) term.

**4. The logarithmic area calculation.** In these two patterns the middle-point constraint becomes
\[
st<\varepsilon^2 H(x,s,t),\qquad H(x,s,t)=(f(x-s)+f(x))(f(x+t)+f(x)).
\]
Fix \(\delta>0\) and \(h>0\) small. On \(|x|\le1-\delta\) and \(0<s,t<h\), uniformly \(H(x,s,t)=4(1-x^2)+O_\delta(h)\). For any fixed \(c>0\), the area of \(\{(s,t)\in(0,h)^2:st<c\varepsilon^2\}\) equals
\[
c\varepsilon^2\left[1+\log\frac{h^2}{c\varepsilon^2}\right]
=2c\varepsilon^2\log(1/\varepsilon)+O_{c,h}(\varepsilon^2).
\]
The parts with \(s\ge h\) or \(t\ge h\) contribute \(O_h(\varepsilon^2)\) because \(st<4\varepsilon^2\). The parts with \(|x|>1-\delta\) contribute at most \(O(\delta\varepsilon^2\log(1/\varepsilon))\), again by the universal product constraint. Finally, the **other two** vertex angles in the opposite-middle-sign patterns are acute whenever \(s,t>C_\delta\varepsilon^2\): their scalar products are bounded below by \((s+t)(s-C_\delta\varepsilon^2)\) and \((s+t)(t-C_\delta\varepsilon^2)\). Excluding \(s\) or \(t\) below this bound removes only \(O_\delta(\varepsilon^2)\) area. Let \(\varepsilon\to0\), then \(h\to0\), then \(\delta\to0\). The two valid sign choices have total probability \(2/8\), so
\[
\Pr_0(A_\varepsilon)\sim\frac34\frac28\cdot
2\varepsilon^2\log(1/\varepsilon)\int_{-1}^1 4(1-x^2)\,dx
=2\varepsilon^2\log(1/\varepsilon).
\]

**5. Joint conditional limit.** On any fixed compact subinterval of \((-1,1)\), the logarithmic layer can be parameterized by
\[
s=\varepsilon^\lambda,\qquad
 t=\frac{4\varepsilon^2(1-x^2)}{s}\,u,
\quad 0<\lambda<2,\quad 0<u<1.
\]
Its Jacobian in \((s,t)\) is \(4\varepsilon^2(1-x^2)|\log\varepsilon|\). Uniform convergence of the middle-point constraint and positivity of the endpoint angles hold on every compact set with \(0<\lambda<2\). Step 4 bounds the discarded endpoint and logarithmic-edge regions, and Step 3 discards all other sign patterns. Normalizing the limiting product measure gives density \(3(1-x^2)/4\), independent uniform \(\lambda\in(0,2)\), independent uniform \(u\in(0,1)\), and a fair surviving sign. This proves the joint convergence under \(\Pr_0\).

**6. Transfer to actual arclength.** Independently draw each \(x\) from the mixture in Step 1. The event that at least two samples use the exceptional density \(h_\varepsilon\) has probability \(O(\alpha_\varepsilon^2)\). If exactly one does, the conditional product-constraint bound from Step 2 (using the two remaining uniform samples) gives acute probability \(O(\alpha_\varepsilon\varepsilon^2\log(1/\varepsilon))\). Therefore the total acute-event mass associated with any exceptional draw is
\[
O(\varepsilon^4\log^2(1/\varepsilon))=o(\varepsilon^2\log(1/\varepsilon)).
\]
The all-uniform component has weight \((1-\alpha_\varepsilon)^3=1-o(1)\). Thus the probability and conditional joint law under genuine Euclidean arclength have exactly the same limits as under uniform first-coordinate sampling.

## Verification
The standalone `check_ellipse.py` implements the acute-event test directly by three Euclidean dot products and independently samples both the uniform-projection comparison measure and the **actual arclength measure** using rejection from uniform angles with acceptance proportional to \(\sqrt{\sin^2\theta+\varepsilon^2\cos^2\theta}\). The recorded command `OPENBLAS_NUM_THREADS=1 python check_ellipse.py` completed with marker `THIN_ELLIPSE_ACUTE_LOG_LAW_CHECKS_OK`; sampled probabilities, opposite-middle sign frequencies and conditional moments are consistent with the theorem. These finite checks are neither proofs of the limit nor independent mathematical validation.

## Relationship to prior work
Random-triangle acuteness under different sampling models is a classical subject, reviewed for Gaussian and shape-theoretic models by Edelman and Strang (2015). The exact general ellipse-boundary problem was posed publicly in 2024, and a 2025 response gives a finite-eccentricity multiple-integral representation under Euclidean perimeter measure. That implicit integral does not state the explicit logarithmic degeneration or the independent conditional shape variables derived here. Equiaffine-uniform ellipse sampling is different: its acute probability has an exact dilogarithmic law, with thin-aspect coefficient \(12/\pi^2\) instead of the Euclidean-arclength coefficient \(2\). Similarly, the separate thin-rectangle boundary model has a different coefficient. Thus neither change of measure nor change of boundary shape preserves the coefficient; these distinctions are mathematical, not just terminology.

## Limitations
The asserted coefficient and conditional limit concern exactly three independent arclength-uniform vertices of an ellipse degenerating to a line segment. They do not provide a closed elementary finite-aspect-ratio probability, rates for the conditional convergence, or any claim of universality under arbitrary boundary sampling measures or arbitrary thin convex shapes. The 2025 integral answer is an especially pertinent prior expression; an earlier derivation of this explicit singular limit cannot be excluded by literature searching alone.

## References
- A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053, first posted January 9, 2015, https://arxiv.org/abs/1501.03053.
- M. Schrempp, *The limit distribution of the largest interpoint distance for distributions supported by an ellipse and generalizations*, arXiv:1505.01597, first posted May 7, 2015, https://arxiv.org/abs/1505.01597 (context on sampling from ellipses; different invariant).
- *Probability that Triangle on Ellipse is Acute*, Mathematics Stack Exchange question 5014676, posted December 22, 2024, and answer January 24, 2025, https://math.stackexchange.com/questions/5014676/probability-that-triangle-on-ellipse-is-acute (finite-eccentricity integral representation).
- T. Easingwood, *Random triangles*, Mathematical Gazette 65 (1981), 245–249, DOI:10.2307/3616588 (general background; publicly accessible abstract).
