# Parity-split quartic binding at a critical defect in alternating weighted shifts

## Finding
Fix distinct positive numbers \(a,b\) and let \(T_{m,c}\) be the unilateral weighted shift on complex \(\ell^2(\mathbb N_0)\) with weights \(a,b,a,b,\ldots\), except that the weight at edge \(m\) is \(c\). Write \(w(T)\) for numerical radius. Set
\[
E=\frac{a+b}{2},\quad D=\frac{ab}{a+b},\quad p_m=\begin{cases}a,&m\text{ even},\\b,&m\text{ odd},\end{cases}
\quad B_{\rm e}=-\frac{ab(4a+b)}{2(a+b)^2},\quad B_{\rm o}=-\frac{ab(3a+2b)}{2(a+b)^2}.
\]
For each real \(\xi\), and every sufficiently large integer \(m\), replace edge \(m\) by
\[
c_m=p_m+\frac{D}{m}+\frac{\xi}{m^2}>0.
\]
As \(m\to\infty\) separately through even and odd integers, one has the **sharp fourth-order edge-binding laws**
\[
\boxed{\displaystyle \lim_{\substack{m\to\infty\\m\ {\rm even}}}m^4\bigl(w(T_{m,c_m})-E\bigr)=\frac{(\xi-B_{\rm e})_+^2}{D},\qquad
\lim_{\substack{m\to\infty\\m\ {\rm odd}}}m^4\bigl(w(T_{m,c_m})-E\bigr)=\frac{(\xi-B_{\rm o})_+^2}{D}.}
\]
Here \(x_+=\max(x,0)\). If \(\xi\) is strictly larger than the relevant \(B_j\), there is exactly one eigenvalue of the self-adjoint part above its essential upper edge, whereas if \(\xi<B_j\) there is none for all sufficiently large indices of that parity. In particular, since \(B_{\rm e}-B_{\rm o}=-ab(a-b)/(2(a+b)^2)\ne0\), any \(\xi\) strictly between the two constants binds on exactly one parity subsequence.

A finer eigenvector statement accompanies the positive law. For \(\xi>B_j\), let \(u^{(m)}\in\ell^2(\mathbb N_0)\) be the positive, unit-norm eigenvector of \(H_{m,c_m}=(T_{m,c_m}+T_{m,c_m}^*)/2\) associated with its upper isolated eigenvalue. Along parity \(j\), define \(\gamma_j=(\xi-B_j)/D>0\). Then
\[
F_m(s)=m\,u^{(m)}_{\lfloor m^2s\rfloor}\ \longrightarrow\ \sqrt{2\gamma_j}\,e^{-\gamma_js}
\quad\text{strongly in }L^2([0,\infty)) .
\]
Thus the bound-state spatial scale is \(m^2\), rather than the \(m\) scale in the ordinary first critical window.

## Assumptions and scope
The weights \(a,b\) are held fixed and strictly positive, with \(a\ne b\); \(\xi\in\mathbb R\) is fixed. All limits are taken with \(m\ge1\) through the specified parity. The spectrum relevant to the numerical radius is that of the self-adjoint part, not the spectrum of the nonnormal shift. The eigenvector assertion applies only in the strictly supercritical cases \(\xi>B_j\); no normalized eigenvector is asserted at or below threshold. The assertion at \(\xi=B_j\) is only the zero fourth-order limit, not absence of an eigenvalue at finite depth.

## Proof
**1. Jacobi reduction and the upper-edge parametrization.** Unimodular diagonal conjugation makes the numerical range of any unilateral weighted shift a centered disk. Thus \(w(T_{m,c})=\sup\sigma(H_{m,c})\), where \(H=(T+T^*)/2\). Let \(J=2H\). Because the coefficients are eventually two-periodic, the upper edge of its essential spectrum is \(a+b\), so \(w(T_{m,c})\ge E\). An exterior eigenvalue of \(J\) can be uniquely written
\[
\lambda_J(\kappa)=\sqrt{a^2+b^2+2ab\cosh(2\kappa)}\qquad(\kappa>0),
\]
with the corresponding top eigenvalue of \(H\) equal to \(\lambda_J(\kappa)/2\). Expansion at zero gives
\[
\frac{\lambda_J(\kappa)}2-E=D\kappa^2+O(\kappa^4).
\]
The characteristic multipliers of the two-step transfer matrix at this energy are \(e^{\pm2\kappa}\).

**2. Exact secular relations.** Write \(c_m(\kappa)\) for the unique positive defect strength producing \(\lambda_J(\kappa)\) as an upper eigenvalue. Solving the transfer recurrence with Dirichlet boundary value \(u_{-1}=0\), matching the growing and decreasing Bloch solutions across the exceptional bond, gives, for even \(m\),
\[
\frac{c_m(\kappa)^2}{a^2}=1+\frac{b(e^{4\kappa}-1)}{a(e^{2\kappa}-e^{-2(m+1)\kappa})+b(1-e^{-2m\kappa})};
\tag{1}
\]
and, for odd \(m\),
\[
\frac{c_m(\kappa)^2}{b^2}=1+\frac{a(e^{4\kappa}-1)}{(a+be^{2\kappa})(1-e^{-2(m+1)\kappa})}.
\tag{2}
\]
For direct verification of the matching step, set \(t=e^{2\kappa}\), \(g=(a/t+b)/(at+b)\). At every ordinary two-edge cell the growing/decaying multipliers are \(t\) and \(t^{-1}\). The solution satisfying \(u_{-1}=0\) is the difference of the two Bloch modes with reflection factor \(g\); matching at the modified edge gives the algebraically equivalent expressions
\[
\frac{c_m^2}{a^2}=\frac{t(a+bt)/(at+b)-g t^{-m}}{1-g t^{-m}}\quad(m\text{ even}),\qquad
\frac{c_m^2}{b^2}=\frac{t(at+b)}{a+bt}\,\frac{1-gt^{-(m+1)}}{1-t^{-(m+1)}}\quad(m\text{ odd}),
\]
which simplify exactly to (1) and (2). These identities can independently be recovered by eliminating the left and right half-line Weyl boundary resolvents in the rank-two coupling equation \(c^2 R_L(\lambda_J)R_R(\lambda_J)=1\).

For \(\lambda_J>a+b\), both boundary resolvents are strictly positive and strictly decreasing with \(\lambda_J\). Consequently the matching equation has at most one solution above the edge; the corresponding eigenvector is strictly positive. The right-hand sides of (1) and (2) start at finite positive thresholds as \(\kappa\downarrow0\) and increase continuously to infinity. Thus a unique upper outlier exists precisely when the bond strength exceeds its threshold; otherwise the numerical radius remains \(E\).

**3. The two exact threshold expansions.** Taking the continuous limit \(\kappa\downarrow0\) in (1) and (2) gives the already known finite-depth thresholds
\[
C_{m,\rm e}=a\sqrt{1+\frac{2b}{m(a+b)+2a}},\qquad
C_{m,\rm o}=b\sqrt{1+\frac{2a}{(m+1)(a+b)}}.
\tag{3}
\]
Expanding the explicit square roots at large \(m\) yields
\[
C_{m,j}=p_m+\frac Dm+\frac{B_j}{m^2}+O(m^{-3}),
\tag{4}
\]
with the constants in the finding. These threshold formulas and the resulting existence criterion are prior work; neither is claimed as independently new.

**4. Uniform near-threshold dispersion and quartic limit.** Differentiate (1) and (2) at \(\kappa=0\), after cancellation of the removable zeros. One finds
\[
\left.\frac{d}{d\kappa}c_m(\kappa)^2\right|_{0,\rm e}
=\frac{2a^2b(m+2)}{m(a+b)+2a},
\]
\[
\left.\frac{d}{d\kappa}c_m(\kappa)^2\right|_{0,\rm o}
=\frac{2ab^2\bigl(m(a+b)+3a+b\bigr)}{(m+1)(a+b)^2}.
\]
In both parities \(c_m'(0)=D+O(m^{-1})\). Uniform Taylor expansion of the exponentials in (1) and (2), after dividing numerator and denominator by \(\kappa\), gives, for every fixed \(M>0\), uniformly for \(0\le\kappa\le M/m^2\),
\[
c_m(\kappa)=C_{m,j}+D\kappa+O\bigl(m^{-1}\kappa+m\kappa^2\bigr).
\tag{5}
\]
Indeed the regularized denominators are positive and bounded below by positive multiples of \(m\), while their Taylor derivatives of order \(r\) are \(O(m^{r+1})\) for fixed \(a,b\); the quotient and square root yield (5). Now prescribe \(c_m=p_m+D/m+\xi/m^2\). Equations (4)–(5), strict monotonicity and a bracketing argument show that when \(\xi>B_j\),
\[
m^2\kappa_m\longrightarrow\frac{\xi-B_j}{D}=: \gamma_j.
\tag{6}
\]
When \(\xi<B_j\) there is no outlier for large \(m\); at equality, monotonicity and (4)–(5) imply that any positive \(\kappa_m\) is \(o(m^{-2})\). Substitute (6) into the dispersion law of Step 1: the fourth-order limit is \(D\gamma_j^2=(\xi-B_j)^2/D\) on the supercritical side and zero otherwise. Since \(B_{\rm e}\ne B_{\rm o}\), the parity selection follows.

**5. Normalized bound-state limit.** In the regime \(\xi>B_j\), the right half-line Bloch solution consists of alternating cell amplitudes \(A_m e^{-2k\kappa_m}\) and \(A_m r_m e^{-(2k+1)\kappa_m}\), where \(r_m\to1\) as \(\kappa_m\to0\); its two-site multiplier is \(e^{-2\kappa_m}\). On the finite left segment, the positive Dirichlet solution is a combination of the two Bloch modes. For \(m\kappa_m\to0\), the transfer formula from Step 2 bounds all of its entries by a constant times \(|A_m|\), uniformly in \(0\le i\le m\). Hence left squared mass is \(O(m|A_m|^2)\), while the geometric right squared mass is \(\sim |A_m|^2/(2\kappa_m)\). Their ratio is \(O(m\kappa_m)=O(m^{-1})\to0\). Normalization therefore gives \(mA_m\to\sqrt{2\gamma_j}\). At each positive \(s\), \(m\,u^{(m)}_{\lfloor m^2s\rfloor}\to\sqrt{2\gamma_j}e^{-\gamma_js}\). The same geometric bound is uniformly dominated by a fixed integrable exponential on \([\varepsilon,\infty)\) for each \(\varepsilon>0\), while the total mass in the shrinking initial region \([0,\varepsilon]\) is controlled by the limiting exponential integral and the vanishing left mass. This proves strong \(L^2\) convergence and finishes the claim.

## Verification
All parity thresholds, derivatives, secular equations and limit constants are exact symbolic identities. A standalone diagnostic evaluates them for both parities, multiple positive distinct weight pairs and several defect depths and compares the quartic-limit predictions with high-precision numerical roots. The tests are corroborative only, not proofs of the infinite-dimensional assertions. The full proof is analytic and given above.

## Relationship to prior work
Ghosh–Birbonshi–Ojha (2026, arXiv:2608.17486) study another family of nonconstant weighted shifts and numerical-radius determinantal methods. Existing finite-determinantal methods of Chakraborty–Ojha–Birbonshi (2022) treat finite perturbations. Earlier exact results for a **uniform** half-line with one moving defect include a quadratic critical scaling and \(m\)-scale eigenvector profile; these do not establish the alternating parity-resolved fourth-order limit. A previous two-periodic remote-defect theorem finds exact asymptotic radii for **fixed** defect strengths and explicitly does not give uniform near-threshold estimates. Marionnet's November 16, 2026 study computes the exact **finite-depth threshold** (3), which is credited, not claimed as new. The claimed new result is the sharp **fourth-order eigenvalue gap and strongly convergent \(m^2\)-scale eigenmode in the joint varying-depth/varying-coupling window**, with two distinct parity constants.

## Limitations
This treats one strictly positive edge perturbation of a real two-periodic positive unilateral weighted shift, with fixed unequal bulk weights. The formula is pointwise in \(a,b,\xi\), not claimed uniform as \(a\to b\) or \(\xi\to B_j\). At exact threshold \(\xi=B_j\), the theorem identifies only the vanishing fourth-order coefficient and does not classify higher-order binding. The exact thresholds and their parity distinction are prior work; so is the homogeneous first critical window. A more general older Jacobi point-interaction/band-edge theorem may imply the quartic scaling, and no independent mathematical audit has occurred.

## References
1. A. Ghosh, R. Birbonshi and S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486v1, publicly submitted 2026-08-18, https://arxiv.org/abs/2608.17486.
2. S. Marionnet, *Numerical range of finite perturbations of a 2-periodic weighted shift*, arXiv:2611.21280v1, publicly submitted 2026-11-16, Proposition 3.3, https://arxiv.org/html/2611.21280v1.
3. B. Chakraborty, S. Ojha and R. Birbonshi, *Numerical radii of weighted shift operators using determinantal polynomials*, *Operators and Matrices* 16 (2022), 1155–1174, https://files.ele-math.com/articles/oam-16-75.pdf.
4. B. Undrakh, H. Nakazato, A. Vandanjav and M.-T. Chien, *The Numerical Radius of a Weighted Shift Operator*, *Electronic Journal of Linear Algebra* 30 (2015), 944–963, https://journals.uwyo.edu/index.php/ela/article/download/1617/1617/.
