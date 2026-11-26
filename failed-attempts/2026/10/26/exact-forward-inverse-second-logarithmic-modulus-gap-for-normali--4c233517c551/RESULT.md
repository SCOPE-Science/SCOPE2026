# Exact forward–inverse second-logarithmic modulus gap for normalized convex maps

## Finding

Let \(\mathcal C\) denote the family of holomorphic univalent maps of the unit disk \(\mathbb D\) onto convex domains, normalized by \(f(0)=0\) and \(f'(0)=1\). Write \(f(z)=z+a_2z^2+a_3z^3+\cdots\), and use the local inverse branch \(F=f^{-1}\) at the origin. Define the direct and inverse logarithmic coefficients by
\[
\log\frac{f(z)}z=2\sum_{n\ge1}\gamma_n z^n,
\qquad
\log\frac{F(w)}w=2\sum_{n\ge1}\Gamma_n w^n.
\]
For every prescribed \(a_2\) with \(r=|a_2|^2\in[0,1]\), the **exact attainable interval** of the signed forward–inverse modulus mismatch is
\[
\left\{|\gamma_2(f)|-|\Gamma_2(f)|:
 f\in\mathcal C,\ f''(0)/2=a_2\right\}
=\left[-M(r),M(r)\right],
\qquad M(r)=\min\left\{\frac r2,\frac{1-r}{3}\right\}.
\]
Consequently,
\[
\sup_{f\in\mathcal C}\bigl||\gamma_2(f)|-|\Gamma_2(f)|\bigr|=\frac15.
\]
The maximum occurs precisely when
\[
a_2=\sqrt{\frac25}\,e^{i\theta},\qquad
\omega(z)=\frac{z\left(a_2+\lambda z\right)}{1+\overline{a_2}\lambda z},
\qquad \lambda=\pm e^{2i\theta},\qquad \theta\in\mathbb R,
\]
where \(\omega\) is defined by \(1+zf''(z)/f'(z)=(1+\omega(z))/(1-\omega(z))\). These are the *only* global extremizers. For the plus sign, \((\gamma_2,\Gamma_2)=(\frac15 e^{2i\theta},0)\); for the minus sign, the two entries interchange. Thus the two types of equality are characterized by the exact vanishing of one, but not both, second logarithmic coefficients.

## Assumptions and scope

Only the classical normalized convex class \(\mathcal C\) is asserted. No assumption that the inverse branch extends to the entire unit disk is needed. The extremal functions are explicitly and uniquely determined by the displayed rational Schwarz functions, equivalently by
\[
f'(z)=\exp\!\left(\int_0^z\frac{2\omega(\zeta)}{\zeta[1-\omega(\zeta)]}\,d\zeta\right),
\qquad f(z)=\int_0^z f'(\zeta)\,d\zeta,
\]
where the integrand is analytic at zero. The two signs and free angle give the complete global equality family. At \(r=0\) and \(r=1\), both endpoints of the conditional interval coincide at zero.

## Proof

**1. Exact coefficient coordinates.** Convexity is equivalent to \(\Re(1+zf''/f')>0\), hence there is an analytic disk self-map \(\omega\), with \(\omega(0)=0\), satisfying
\[
1+\frac{zf''(z)}{f'(z)}=\frac{1+\omega(z)}{1-\omega(z)}.
\]
Writing \(\omega(z)=uz+vz^2+O(z^3)\), Schwarz's lemma and Schwarz–Pick applied to \(\omega(z)/z\) give \(|u|\le1\), \(|v|\le1-|u|^2\). Equating the first two nonconstant Taylor coefficients gives
\[
a_2=u,\qquad a_3=u^2+\frac v3.
\]
Formal inversion through order three yields \(F(w)=w-a_2w^2+(2a_2^2-a_3)w^3+O(w^4)\). Taking the corresponding logarithms proves the exact symmetric formulae
\[
\boxed{\gamma_2=\frac{u^2}{4}+\frac v6,\qquad
\Gamma_2=\frac{u^2}{4}-\frac v6.}
\]

**2. Universal conditional upper bound.** Set \(A=u^2/4\), \(B=v/6\). Twice applying the reverse triangle inequality, once with the pairs \(A+B,A-B\) and once with \(A+B,-A+B\), gives
\[
\bigl||A+B|-|A-B|\bigr|\le2\min(|A|,|B|).
\]
Since \(|A|=r/4\) and \(|B|\le(1-r)/6\), it follows that
\[
\bigl||\gamma_2|-|\Gamma_2|\bigr|
\le 2\min\left\{\frac r4,\frac{1-r}{6}\right\}=M(r).
\]

**3. Every conditional endpoint is attainable.** For fixed \(a_2=u\) with \(0<r<1\), choose \(v\) of the phase of \(u^2\) or its opposite and magnitude \(\min\{\frac32r,1-r\}\). Then \(|v|\le1-r\) and the complex numbers \(A\) and \(B\) are collinear, giving the signed values \(\pm M(r)\). Such \((u,v)\) actually arise from analytic Schwarz functions, not merely from formal jets: let \(\lambda=v/(1-r)\), and define
\[
\omega(z)=z\frac{u+\lambda z}{1+\overline u\lambda z},
\qquad |\lambda|\le1.
\]
The second factor is a disk self-map, and its first two coefficients are precisely \(u,v\). Integrating the differential equation in the assumptions constructs the required normalized convex function. At \(r=0\), choose \(\omega(z)=vz^2\) with any \(|v|\le1\); at \(r=1\), Schwarz's lemma forces \(\omega(z)=uz\). Both give zero mismatch. As \(v\) varies continuously between the two constructed choices, the signed difference varies continuously from \(-M(r)\) to \(M(r)\). Combining this intermediate-value property with Step 2 proves the entire asserted interval.

**4. Global optimization and equality rigidity.** The two affine branches defining \(M\) intersect uniquely at \(r=2/5\), and each has strictly monotone slope on its side. Thus \(M(r)\le1/5\), with equality only at \(r=2/5\). Here \(|A|=1/10\) and \(|B|\le1/10\). Equality of the mismatch forces \(|B|=1/10\) and collinearity of \(A,B\), hence \(v=\pm(3/5)e^{2i\theta}\) for \(u=\sqrt{2/5}e^{i\theta}\). Because \(|v|=1-|u|^2\), equality in Schwarz–Pick forces the unique degree-two Blaschke form displayed in the finding. Conversely, each displayed \(\omega\) is a Schwarz function with these jets and yields a normalized convex map, with direct/inverse second coefficients \((e^{2i\theta}/5,0)\) or \((0,e^{2i\theta}/5)\). There are no other equality cases.

## Verification

The standalone script `verify_coefficients.py` checks the Carathéodory Taylor expansion, the formal inverse, both logarithmic-coefficient identities and their sum/difference using exact symbolic algebra. It also checks both signed conditional endpoints at 101 rational radii and tests 500 interior Schwarz-admissible jets. The recorded execution result is:

`VERIFY_OK symbolic_identities=6 exact_signed_conditional_extremizers=202 random_interior_tests=500`

These finite tests are corroborative only. The universal inequalities, realizability and equality classification follow from the analytic proof above, not from sampling.

## Relationship to prior work

Ali, Raza and Raza (arXiv:2610.20645v1, first posted October 11, 2026) obtain sharp *successive-index* modulus-difference bounds \(\bigl||\gamma_2|-|\gamma_1|\bigr|\) and \(\bigl||\Gamma_2|-|\Gamma_1|\bigr|\) for Ma–Minda convex classes, along with comparisons of their optimal bounds. Dhara and Ghosh (arXiv:2606.11325v1) establish related consecutive-index bounds and inverse-coefficient estimates for Janowski convex classes. Allu and Shaji (arXiv:2403.10031v1) address consecutive inverse logarithmic coefficients. Those results provide foundational coefficient formulae and context but, in the portions inspected, do not assert the *same-index, same-function* sharp mismatch interval, its fixed-coefficient transition, or its complete equality classification. The proof here is self-contained using classical Schwarz–Pick and convexity theory. Searches and comparisons cannot establish exhaustive priority over all historical literature.

## Limitations

The statement applies only to the second logarithmic coefficients and normalized convex functions. The conditional interval describes fixed second Taylor coefficient \(a_2\) but does not address higher logarithmic indices or all Ma–Minda subfamilies. Literature-priority assessment is qualified by the scope of accessible sources.

## References

1. Rashid Ali, Mohsan Raza and Umar Raza, *On the Moduli Difference of Initial Logarithmic and Inverse Logarithmic Coefficients of Ma-Minda Convex Functions*, arXiv:2610.20645v1 (2026-10-11), https://arxiv.org/html/2610.20645v1.
2. Chayani Dhara and Nirupam Ghosh, *Logarithmic Inverse Coefficients and Moduli Differences of Janowski Class*, arXiv:2606.11325v1 (2026), https://arxiv.org/abs/2606.11325.
3. Vasudevarao Allu and Amal Shaji, *Moduli difference of inverse logarithmic coefficients of univalent functions*, arXiv:2403.10031v1 (2024), https://arxiv.org/html/2403.10031v1.
4. Schwarz's lemma and Schwarz–Pick, classical standard results used in their equality forms.
