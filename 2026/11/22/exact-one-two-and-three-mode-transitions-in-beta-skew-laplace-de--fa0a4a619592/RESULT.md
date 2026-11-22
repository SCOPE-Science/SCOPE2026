# Exact one-, two-, and three-mode transitions in beta-skew-Laplace densities

## Finding
Consider the beta-skew-Laplace family introduced by Tovar-Falón and Martínez-Flórez (2022), with density
\[
f_\beta(x)=\frac{e^{-|x|}\bigl[(1-\beta x^3)^2+1\bigr]}{4(1+360\beta^2)},\qquad x\in\mathbb R,\quad \beta\in\mathbb R.
\]
A *mode* here is a distinct strict local maximum of the density, including the possible cusp at the origin. Write \(b=|\beta|\). Let \(z_R\) be the unique root of \(z^3-8z+4=0\) in \((5/2,13/5)\), and \(z_L\) the unique root of \(z^3-8z-4=0\) in \((3,31/10)\). Define the exact positive thresholds
\[
b_R=\left[\frac{z_R^2-2z_R+2}{6z_R^{2/3}(z_R-1)}\right]^3
=0.00753040309491222\ldots,
\qquad
b_L=\left[\frac{z_L^2+2z_L+2}{6z_L^{2/3}(z_L+1)}\right]^3
=0.03948356784410642\ldots.
\]
They satisfy \(0<b_R<b_L\). The **complete sharp local-modality diagram** is
\[
\begin{array}{c|c}
\text{tilt magnitude}&\text{number of strict local modes}\\\hline
0\le b\le b_R&1\\
b_R<b\le b_L&2\\
b>b_L&3
\end{array}.
\]
For positive \(\beta\), a right-hand outer mode is born at \(b_R\), and a left-hand outer mode is born at \(b_L\); for negative \(\beta\), the sides interchange. The cusp at zero is always a strict local mode at every finite parameter. Exactly at either positive threshold the emerging outer critical point is stationary but **not** a local mode, so the inequalities at the thresholds are part of the claim. The same classification holds for any location-scale transform \(\mu+\sigma X\) with \(\sigma>0\), with all mode locations transformed accordingly.

There is a singular limiting transition: as \(|\beta|\to\infty\), the densities converge in total variation to
\[
f_\infty(x)=\frac{x^6e^{-|x|}}{1440},
\]
which has **exactly two modes**, at \(x=-6\) and \(x=6\). Thus the central local mode survives at every finite large tilt while disappearing in the limiting law.

## Assumptions and scope
The entire real parameter domain \(\beta\in\mathbb R\) is included; \(\beta=0\) is the ordinary Laplace distribution. The density is continuous at zero and smooth separately on its two open half-lines. A stationary point with no change from increasing to decreasing behavior is not counted as a local maximum. Only the standard beta-skew-Laplace family is classified; no analogous complete diagram is claimed for the two-parameter exponentiated extension of the original article.

## Proof
**Normalization, origin, and reflection.** Pair the positive and negative halves and put \(t=|x|\): the unnormalized integrand sums to \(e^{-t}(4+2\beta^2t^6)\). Hence its total integral is \(4+2(6!)\beta^2=4(1+360\beta^2)\). Also \(f_{-\beta}(x)=f_\beta(-x)\), so it is enough to study \(\beta=b>0\). At the origin the right derivative is strictly negative and the left derivative strictly positive, since the polynomial factor equals \(2+O(|x|^3)\) and the Laplace factor is \(1-|x|+O(x^2)\). Thus zero is a strict local maximum for every finite \(b\), including \(b=0\).

**Right-hand stationary points.** For \(x=t>0\) put \(z=bt^3\), and \(Q_R(z)=(1-z)^2+1=z^2-2z+2\). Apart from a positive constant, \(f_b(t)=e^{-t}Q_R(z)\). The sign of its derivative is the sign of
\[
6b^{1/3}z^{2/3}(z-1)-Q_R(z).
\]
This is strictly negative for \(0<z\le1\). On \(z>1\) define
\[
H_R(z)=\frac{z^2-2z+2}{6z^{2/3}(z-1)}.
\]
The derivative of the density has the sign of \(b^{1/3}-H_R(z)\). Since \(H_R\) is positive and tends to infinity at both endpoints of \((1,\infty)\), it suffices to classify its minimum. Direct logarithmic differentiation gives
\[
\frac{H_R'(z)}{H_R(z)}
=\frac{z^3-8z+4}{3z(z-1)(z^2-2z+2)}.
\]
The numerator decreases until \(\sqrt{8/3}\), then increases; it is negative at \(z=1\), and has exactly one root in \((1,\infty)\). Exact rational substitutions show its root \(z_R\) lies in \((5/2,13/5)\). Therefore \(H_R\) has a unique strict minimum at \(z_R\). For \(b<b_R\) the density decreases strictly on the positive half-line; for \(b=b_R\) the derivative vanishes only at the minimum of \(H_R\) but is otherwise negative, so there is no right outer mode; for \(b>b_R\) the derivative changes sign from negative to positive at its first zero and from positive to negative at its second zero, producing exactly one right outer mode and one intervening right local minimum.

**Left-hand stationary points.** Write \(x=-t<0\), \(z=bt^3\), and \(Q_L(z)=(1+z)^2+1=z^2+2z+2\). As a function of \(t>0\), the left half-density is proportional to \(e^{-t}Q_L(z)\), with derivative sign determined by \(b^{1/3}-H_L(z)\), where
\[
H_L(z)=\frac{z^2+2z+2}{6z^{2/3}(z+1)}.
\]
Its logarithmic derivative is
\[
\frac{H_L'(z)}{H_L(z)}
=\frac{z^3-8z-4}{3z(z+1)(z^2+2z+2)}.
\]
The numerator is negative at zero, decreases until \(\sqrt{8/3}\), and then increases to infinity, so it has a unique positive zero \(z_L\), which lies in \((3,31/10)\) by exact rational evaluation. Thus \(H_L\) decreases to one strict minimum and then increases, with infinite limits at zero and infinity. The same sign analysis yields exactly one left outer mode for \(b>b_L\), and no left outer mode for \(b\le b_L\). In particular, equality at \(b=b_L\) creates a horizontal but not extremal point.

**Strict ordering of the two transitions.** For \(z>1\), subtract the two threshold functions:
\[
H_R(z)-H_L(z)=\frac{4-2z^2}{6z^{2/3}(z^2-1)}.
\]
The unique minimizer \(z_L>3>\sqrt 2\), so \(H_R(z_L)<H_L(z_L)\). Since \(z_R\) minimizes \(H_R\),
\[
b_R^{1/3}=H_R(z_R)\le H_R(z_L)<H_L(z_L)=b_L^{1/3}.
\]
Consequently the right-side mode necessarily appears before the left-side mode. Adding the permanent central mode and applying reflection establishes every regime and all boundary cases.

**Limit and singular loss of the cusp.** Divide the numerator and denominator of \(f_\beta(x)\) by \(\beta^2\): for each real \(x\), as \(|\beta|\to\infty\), it tends to \(x^6e^{-|x|}/1440\). The limit integrates to one because \(2\int_0^\infty t^6e^{-t}dt/1440=1\). By Scheffé's lemma, pointwise convergence of these normalized densities implies convergence in \(L^1\) and hence total variation. The limiting function is zero at the origin, and on each half-line has derivative sign determined by \(6-|x|\), so its only maxima are at \(\pm6\). This does not contradict the finite-parameter three-mode regime because \(f_\beta(0)=1/[2(1+360\beta^2)]\to0\).

## Verification
The self-contained file `verify.py` requires SymPy and checks the exact density normalization, both derivative-reduction identities, both cubic numerator identities, rational root brackets, the threshold-ordering difference, and normalization/modes of the limiting density. High-precision printed approximations of the algebraic thresholds are supplemental; the proof's real-root arguments, derivative signs and strict endpoint cases certify the global statement and do not rely on a finite numerical mesh. Reproduction: run `python verify.py` in the directory containing this article and checker.

## Relationship to prior work
The originating paper of Tovar-Falón and Martínez-Flórez (2022), Definition 1 and Proposition 1, establishes the family and reports that its density has at most three modes; Figure 1 illustrates sample parameter values. The paper includes the reflected-parameter identity and the limiting bimodal-Laplace density, which are acknowledged as existing distributional facts. It does not identify the two sharp parameter thresholds, count local maxima at both boundaries, or prove the one-to-two-to-three-mode phase diagram. The total-variation strengthening of the limiting statement follows from normalization and Scheffé's lemma. Sulewski and Bilski (2025) study a *different* bimodal power-Laplace model (constructed via a double-Weibull/scale-transformation mechanism), so its modal analysis does not directly imply conditions on the present cubic polynomial tilt. Related alpha-skew-Laplace variants also have different tilt polynomials. Relevant mathematical record and web searches using aliases and numerical constants found no directly covering threshold formula; this is not an exhaustive historical-priority guarantee.

## Limitations
This is a local mode-count theorem, not a classification of global-height orderings or statistically detectable mixture components. An arbitrarily low central peak remains a mathematical local mode for finite \(\beta\), even if it would be invisible in a finite histogram. The exact thresholds apply only to the stated polynomial beta-skew-Laplace model, not automatically to exponentiated or alternative skew-Laplace families. The mathematics has received a self-review only; no independent audit has been performed, and literature coverage cannot guarantee historical uniqueness.

## References
1. R. Tovar-Falón and G. Martínez-Flórez, “A New Class of Exponentiated Beta-Skew-Laplace Distribution,” *Anais da Academia Brasileira de Ciências* 94(4), e20191597 (first publicly published 24 October 2022). DOI: https://doi.org/10.1590/0001-3765202220191597. Open full text: https://www.scielo.br/j/aabc/a/vVNvTJdyMn6V4mSpdnY8RQq/?lang=en.
2. P. Sulewski and J. Bilski, “Unknown properties of bimodal power Laplace distribution,” *Wiadomości Statystyczne* 70(12), 1–34 (2025). DOI: https://doi.org/10.59139/ws.2025.12.1.
3. H. Scheffé, “A useful convergence theorem for probability distributions,” *Annals of Mathematical Statistics* 18(3), 434–438 (1947), for the standard convergence-in-density lemma.
