# Unique bounded-variation minimax rule among positive symmetric cubic-exact three-node quadratures

## Finding
Let \(\operatorname{Var}(f)\) be the Jordan total variation of a real pointwise function \(f:[0,1]\to\mathbb R\). Among all positive symmetric quadrature rules with at most three nodes that integrate each polynomial of degree at most three exactly, there is a **unique rule** minimizing
\[
\mathcal E(Q)=\sup_{\operatorname{Var}(f)\le1}\left|Q(f)-\int_0^1f(x)\,dx\right|.
\]
Let \(d_*\) denote the unique root in \([1/\sqrt{12},1/2]\) of
\[
12d^2(1-d)=1,\qquad d_*=0.361175862232188\ldots.
\]
The minimizing rule is
\[
Q_*(f)=\frac{1-d_*}{2}\left[f\left(\frac12-d_*\right)+f\left(\frac12+d_*\right)\right]+d_*f\left(\frac12\right),
\]
with sharp error coefficient
\[
\boxed{\mathcal E(Q_*)=\frac{d_*}{2}=0.180587931116094\ldots.}
\]
Both distinct upper-step signals \(f=\mathbf 1_{[1/2,1]}\) and \(f=\mathbf 1_{(1/2-d_*,1]}\) attain equality. Within the same symmetric cubic-exact family, three-point Gauss–Legendre quadrature has coefficient \(2/9\), and Simpson's rule has coefficient \(1/3\). Thus the optimal robust rule sacrifices fifth-degree exactness in exchange for an approximately \(18.7\%\) smaller worst-case error than three-point Gaussian quadrature on variation-one integrands.

## Assumptions and scope
A *pointwise Jordan-BV function* is a real function on the closed interval \([0,1]\) with finite variation
\[
\operatorname{Var}(f)=\sup_{0=t_0<\cdots<t_m=1}\sum_{j=1}^m|f(t_j)-f(t_{j-1})|.
\]
Its Riemann integral exists, and its values at quadrature nodes are taken as specified, including at discontinuities. The result does not identify functions only up to Lebesgue-almost-everywhere equivalence, because point evaluation on such equivalence classes is undefined.

A symmetric rule with at most three nodes and nonnegative weights has the form
\[
Q_{d,b}(f)=b f(\tfrac12-d)+(1-2b)f(\tfrac12)+b f(\tfrac12+d),
\quad 0<d\le\tfrac12,\quad 0\le b\le\tfrac12.
\]
Requiring degree-three exactness is equivalent to
\[
2bd^2=\frac1{12},\qquad \frac1{\sqrt{12}}\le d\le\frac12,\qquad b=\frac1{24d^2}.
\]
The limiting case \(b=1/2\), where the centre has zero weight, is included. Symmetry guarantees exactness of the first and third moments once constants and the centred quadratic moment are exact.

## Proof
**Step 1: exact variation error from discrepancies.** For any probability measure \(\nu\) supported on finitely many nodes in \([0,1]\), write \(Q_\nu(f)=\int f\,d\nu\). Define the two one-sided distribution discrepancies
\[
D(\nu)=\sup_{0\le t\le1}\max\{|\nu([0,t])-t|,|\nu([0,t))-t|\}.
\]
Then
\[
\sup_{\operatorname{Var}(f)\le1}\left|Q_\nu(f)-\int_0^1f(x)\,dx\right|=D(\nu).
\]
Indeed, the two upper-step functions \(\mathbf1_{(t,1]}\) and \(\mathbf1_{[t,1]}\), both of variation one when \(0<t<1\), have quadrature errors respectively \(t-\nu([0,t])\) and \(t-\nu([0,t))\). The endpoint cases follow by limits. Conversely, a real nondecreasing function is a positive superposition of such upper-step functions by its layer-cake representation; hence its error is bounded by \(D(\nu)\) times its endpoint increase. Every finite-Jordan-variation real function is a difference of two nondecreasing functions whose total increases sum to its variation (Jordan decomposition). This proves the upper bound for every pointwise BV function and the matching supremum.

**Step 2: evaluate the three-node discrepancy.** Set \(a=1/2-d\) and \(b=1/(24d^2)\). Immediately before and after each of the three atoms, the absolute discrepancy is among
\[
a,\qquad |b-a|,\qquad \frac12-b.
\]
Moreover \(b>2a\) throughout the admissible interval. To see this, note
\[
24d^2(b-2a)=1-24d^2(1-2d)\ge\frac19>0,
\]
because the maximum of \(24d^2(1-2d)\) on \([0,1/2]\) is \(8/9\), attained at \(d=1/3\). Thus \(b-a>a\ge0\), and the exact sharp coefficient of every admissible rule is
\[
\boxed{\mathcal E(Q_{d,b})=\max\left\{\frac1{24d^2}+d-\frac12,\;\frac12-\frac1{24d^2}\right\}.}
\]
For every admissible \(d\), upper-step indicators yield equality at an appropriate atom, so no smoothness assumption or finite enumeration enters sharpness.

**Step 3: solve the global minimax problem.** Let
\[
F_1(d)=\frac1{24d^2}+d-\frac12,\qquad F_2(d)=\frac12-\frac1{24d^2}.
\]
Their crossing is equivalent to \(12d^2(1-d)=1\). The left-hand side is strictly increasing on \([1/\sqrt{12},1/2]\), starts below one and ends above one, so there is exactly one crossing \(d_*\). It lies below \(2/5\), since \(12(2/5)^2(3/5)>1\). On \([1/\sqrt{12},d_*]\), the derivative \(F_1'(d)=1-1/(12d^3)\) is negative, because \(d\le2/5\) implies \(12d^3<1\). On \([d_*,1/2]\), \(F_2'(d)=1/(12d^3)>0\). Therefore \(\max(F_1,F_2)\) has a unique global minimum at \(d_*\). At the crossing \(b_*=(1-d_*)/2\), and both branches have value \(d_*/2\).

**Step 4: exhibit attained equality.** At the unique optimizer, \(f_1=\mathbf1_{[1/2,1]}\) has \(Q_*(f_1)=1-b_*\) and \(\int f_1=1/2\), giving error \(1/2-b_*=d_*/2\). The second signal \(f_2=\mathbf1_{(1/2-d_*,1]}\) has \(Q_*(f_2)=1-b_*\) and integral \(1/2+d_*\), giving error \(b_*-(1/2-d_*)=d_*/2\). Both have Jordan variation one. These are different worst-case jump locations and choices of pointwise boundary value.

## Verification
A standalone Python standard-library checker (`check_quadrature.py`) performs exact rational sign checks bracketing the unique cubic root between \(0.3611758622\) and \(0.3611758623\), verifies polynomial moments through degree three at representative parameters, independently reconstructs the discrepancy from all one-sided atom limits, and verifies two equality witnesses. It also checks the Gauss and Simpson benchmarks, a grid of 20,001 admissible parameters, and 2,500 independently drawn finite-jump BV functions. The finite grid and random tests are corroborative, not substitutes for Steps 1–4 of the proof.

## Relationship to prior work
The 2011 preprint by Dragomir and Momoniat (subsequently published in 2013) provides BV bounds for three-point formulas evaluating at the *fixed interval endpoints* and one variable interior point. Its general theorem does not optimize moving symmetric outer nodes under cubic moment exactness. The 2015 work by Klaričić Bakula and collaborators treats corrected symmetric three-point Euler formulas for derivative-controlled functions, not the Jordan-variation minimax objective. Komisarski and Wąsowicz (2022) explicitly parameterize the same family of symmetric cubic-exact positive rules, but optimize quadrature inequalities for **3-convex integrands**, not worst-case error on Jordan-BV functions. The standard one-dimensional discrepancy/variation duality supplies the starting norm formula; the unique root, optimum weights/nodes and comparison with classical rules are the new synthesis here.

## Limitations
The optimization is restricted to **symmetric, nonnegative, at-most-three-node rules exact through degree three** on the uniform interval. It does not claim global optimality among nonsymmetric rules, higher node counts, signed weights or other smoothness/variation gauges. For the pointwise-Jordan-BV formulation, values at jump points are significant. A 2011 RGMIA preprint has a received date but no independently established exact first-public-posting date; the structured archival lead date is the explicitly documented online publication date of the 2015 article, not a claim that the subject began then. The literature searches and full-text comparisons do not establish absolute historical priority.

## References
1. S. S. Dragomir and E. Momoniat, *A Three Point Quadrature Rule for Functions of Bounded Variation and Applications*, RGMIA Research Report Collection 14 (2011), Article 33, full text: https://rgmia.org/papers/v14/v14a33.pdf ; journal version, *Mathematical and Computer Modelling* 57 (2013), 612–622, DOI: https://doi.org/10.1016/j.mcm.2012.07.024.
2. M. Klaričić Bakula, J. Pečarić, M. Ribičić Penava, A. Vukelić, *Some Grüss type inequalities and corrected three-point quadrature formulae of Euler type*, *Journal of Inequalities and Applications* 2015, article 76; published 3 March 2015, DOI: https://doi.org/10.1186/s13660-015-0603-x.
3. A. Komisarski and S. Wąsowicz, *On optimal inequalities between three-point quadratures*, *Aequationes Mathematicae* 96 (2022), 621–638, DOI: https://doi.org/10.1007/s00010-022-00868-4.
4. M. D. Stern, *Optimal Quadrature Formulae*, *The Computer Journal* 9 (1967), 396–403, DOI: https://doi.org/10.1093/comjnl/9.4.396 (abstract examined; concerns derivative-based minimax criteria).
