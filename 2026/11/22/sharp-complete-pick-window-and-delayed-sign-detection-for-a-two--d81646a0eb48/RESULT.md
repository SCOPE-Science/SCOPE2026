# Sharp complete-Pick window and delayed sign detection for a two-defect Hardy shift

## Finding

**Theorem.** For arbitrary real parameters \(a,b>0\), let \(\mathcal H_{a,b}\) be the Hilbert space of analytic functions \(f(z)=\sum_{n\ge0}f_nz^n\) on the unit disc, with
\[
\|f\|_{a,b}^2=|f_0|^2+a|f_1|^2+ab\sum_{n\ge2}|f_n|^2.
\]
The forward multiplier \(M_z\) is the unilateral weighted shift with squared weights \(a,b,1,1,\ldots\). Then the **complete Nevanlinna–Pick property** holds if and only if
\[
\boxed{a\ge1,\qquad \frac{4a}{(a+1)^2}\le b\le a.}
\]
In particular, when \(a>1\), the interval \(4a/(a+1)^2\le b<1\) consists of not expansive (hence nonconcave) complete-Pick shifts. For example, \(a=2,b=9/10\) lies in this region, whereas \(a=2,b=4/5\) fails the complete-Pick property.

**Sharp finite-test delay.** Fix \(a>1\), set \(b_*=4a/(a+1)^2\), and let \(0<b<b_*\). Define
\[
A=1-\frac1a,\quad B=\frac{b-1}{ab},\quad q=\sqrt{-B},\quad
\theta=\arccos\!\left(\frac{A}{2q}\right),\quad
u=\frac{(a-b)/(abq)-\cos\theta}{\sin\theta},\quad
\phi=\arctan\!\left(\frac1\nu\right).
\]
All these expressions are real, with \(0<\theta<\pi/2\) and \(\nu>0\). Write \(1-1/K_{a,b}(t)=\sum_{n\ge1}c_nt^n\) about the origin. Its first negative coefficient has the **exact index**
\[
\boxed{n_-(a,b):=\min\{n\ge1:c_n<0\}
=\left\lfloor\frac{\pi-\phi}{\theta}\right\rfloor+2.}
\]
As \(b\uparrow b_*\) with \(a>1\) fixed,
\[
\boxed{\lim_{b\uparrow b_*} n_-(a,b)\sqrt{b_*-b}
=\frac{2\pi\sqrt a\,(a-1)}{(a+1)^2}.}
\]
Thus arbitrarily long finite initial coefficient tests accept parameters just outside the exact complete-Pick region; the detection length diverges at order \((b_*-b)^{-1/2}\).

## Assumptions and scope

The space and the kernel are over the **open unit disc** with complex scalar functions and positive real \(a,b\); evaluation at each point is bounded. Monomials are orthogonal and polynomials dense. The kernel is normalized by \(K_{a,b}(z,0)=1\). Complete Pick means solvability of the normalized interpolation problem for matrices of **all finite sizes**; the standard McCullough–Quiggin criterion says a normalized nonvanishing kernel is complete Pick precisely if \(1-1/K\) is positive semidefinite. For radial analytic kernels, positivity is equivalent to nonnegativity of each Taylor coefficient. This last assertion follows by the positive rank-one monomial expansion in one direction and positivity of derivative evaluation forms at the origin in the other. The initial sign-delay statement is restricted to \(a>1\) and \(0<b<b_*\); no limit uniform in \(a\) is claimed.

## Proof

**1. Kernel and coefficients.** Orthogonality gives, writing \(t=z\overline w\),
\[
K_{a,b}(t)=1+\frac{t}{a}+\frac{t^2}{ab(1-t)}
=\frac{1-At-Bt^2}{1-t},\qquad A=1-\frac1a,\quad B=\frac{b-1}{ab}.
\]
Thus \(F(t)=1-1/K(t)=\sum_{n\ge1}c_nt^n\) satisfies
\[
c_1=\frac1a,\qquad c_2=\frac{a-b}{a^2b},\qquad
c_n=A c_{n-1}+B c_{n-2}\quad(n\ge3).
\]
The coefficient criterion is necessary even if a kernel has a zero: complete Pick would imply a nonvanishing kernel and a positive \(F\) near the origin.

**2. Excluded parameters.** For \(b>a\), \(c_2<0\). For \(0<a<1\) and \(b\le a\), the numbers \(A<0\), \(B<0\), \(c_2\ge0\) imply \(c_3<0\). For \(a=1\), if \(b<1\) then \(c_3=Bc_1<0\), while \(b>1\) was excluded by \(c_2\). Therefore the only possible range has \(a\ge1\) and \(b\le a\), with the case \(a=1,b=1\) giving the ordinary Hardy kernel.

**3. All nonnegative cases.** Suppose \(a>1\). When \(1\le b\le a\), \(A,B,c_1,c_2\ge0\), so the recurrence proves \(c_n\ge0\) for every \(n\). For \(0<b<1\), put \(q=\sqrt{-B}\) and \(\Delta=A^2+4B\). The characteristic roots of the recurrence are nonnegative precisely if \(\Delta\ge0\), equivalently
\[
\Delta=\frac{b(a+1)^2-4a}{a^2b}\ge0
\quad\Longleftrightarrow\quad b\ge b_*.
\]
In that case write \(r_\pm=(A\pm\sqrt\Delta)/2\). Since \(c_2/c_1=A+aq^2>A\ge r_+\ge r_-\ge0\), for distinct roots the identity
\[
c_n=c_1r_+^{n-1}+
(c_2-c_1r_+)\frac{r_+^{n-1}-r_-^{n-1}}{r_+-r_-}\quad(n\ge1)
\]
proves \(c_n\ge0\). At the double root, use its continuous limiting expression with \((n-1)r_+^{n-2}\), also nonnegative. The poles of this rational power series lie outside the unit disc: in the nonnegative-\(B\) case its positive characteristic root is below one since \(1-A-B=1/(ab)>0\); in the \(B<0,\Delta\ge0\) case both roots are at most \(A<1\). Consequently \(F\) is analytic throughout \(|t|<1\); for \(0\le r<1\), \(0\le F(r)=1-1/K(r)<1\) and nonnegative coefficients imply \(|F(t)|\le F(|t|)<1\). Hence \(K=1/(1-F)\) is everywhere nonzero and the complete-Pick criterion applies. This proves sufficiency including the boundary \(b=b_*\).

**4. Sign oscillation outside the window.** If \(a>1\) and \(0<b<b_*\), then \(\Delta<0\), and the two characteristic roots are \(qe^{\pm i\theta}\). The first two coefficients yield the exact formula
\[
c_n=c_1q^{n-1}\bigl[\cos((n-1)\theta)+\nu\sin((n-1)\theta)\bigr]
=c_1q^{n-1}\sqrt{1+\nu^2}\,\sin((n-1)\theta+\phi).
\]
Indeed \(c_2/(c_1q)=(a-b)/(abq)\), which fixes \(\nu\) as in the statement. The positivity \(\nu>0\) follows from \(c_2/c_1=A+aq^2>A/2=q\cos\theta\). Since \(0<\theta<\pi/2\) and \(0<\phi<\pi/2\), the first negative sine value occurs at the first integer \(n\) with \((n-1)\theta+\phi>\pi\), yielding the asserted floor formula. This proves necessity and the exact first-failure index.

**5. Critical delay.** As \(b\uparrow b_*\), the identity for \(\Delta\) gives
\[
-\Delta\sim\frac{(a+1)^4}{4a^3}(b_*-b),\qquad
\theta\sim\frac{(a+1)^2}{2\sqrt a\,(a-1)}\sqrt{b_*-b}.
\]
Here \(q\to(a-1)/(2a)\), \(\nu\to\infty\), and \(\phi\to0\). Therefore \(n_-=\pi/\theta+O(1)\), and multiplying by \(\sqrt{b_*-b}\) proves the limit.

## Verification

The attached standalone `verify_two_defect.py` computes coefficients by exact rational recurrence over 108 parameter pairs, including the discriminant boundary and positive/negative instances, with additional numerical checks of the first-negative-index asymptotics at twelve near-critical parameter pairs. These are consistency checks, **not** the proof for all parameters. All infinities, boundary equalities, and the limiting constant are justified analytically in the proof above. Execute using `python verify_two_defect.py` with Python's standard library.

## Relationship to prior work

Luo and Rydhe (2026) prove that concavity of the forward shift of a shift-invariant analytic reproducing kernel space implies the complete Pick property, and produce a logarithmically concave counterexample. In the present two-defect family, the ordinary concavity criterion is exactly \(a\ge1\) and \(1\le b\le2-1/a\); that prior implication therefore covers a strict subregion but not the classification or its not expansive \(b<1\) branch. Quiggin's weighted-Hardy sufficient criterion uses monotonic successive norm ratios and does not give the sharp nonmonotone parameter window. The general McCullough–Quiggin–Agler–McCarthy reciprocal-kernel criterion and the standard recurrence method are acknowledged foundations, not claimed as new. Ahmed, Das and Panja (2024) characterize complete-Pick de Branges–Rovnyak *defect* spaces from contractive multipliers; that construction is not a complete classification of our independently perturbed monomial norms. A separate published monomial-defect phase diagram for power kernels concerns kernels of the form \((1-sz^m\overline w^m)/(1-z\overline w)^\gamma\), a different coefficient family; it does not supply the sharp two-initial-weight threshold or the first-negative-index law.

## Limitations

The result concerns exactly two initial weighted-shift bonds followed by a constant tail, not arbitrary finitely supported weight perturbations or general nonradial kernels. The sign-delay estimate is for a fixed \(a>1\) from below; it does not give a universal finite coefficient cutoff for all parameter values. Previously established coefficient positivity and Pick criteria supply the framework; priority of the new **explicit phase region and sign-delay asymptotic** is supported by the cited comparisons but not by an exhaustive bibliographic proof. No independent verification is claimed.

## References

1. S. Luo and E. Rydhe, *Concave shifts and the complete Nevanlinna–Pick property*, arXiv:2611.12778v1, first submitted 9 November 2026, https://arxiv.org/html/2611.12778v1.
2. P. P. Quiggin, *Generalisations of Pick’s Theorem to Reproducing Kernel Hilbert Spaces*, PhD thesis, Lancaster University, August 1994, Chapter 2, https://eprints.lancs.ac.uk/id/eprint/61962/1/Quiggin.pdf.
3. H. Ahmed, B. K. Das and S. Panja, *de Branges–Rovnyak spaces which are complete Nevanlinna–Pick spaces*, arXiv:2403.19377v2 (2024), https://arxiv.org/html/2403.19377v2.
4. *Sharp complete-Pick phase diagram for monomial defects of power kernels*, published result record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-complete-pick-phase-diagram-for-monomial-defects-of-power--a614d1883358.
