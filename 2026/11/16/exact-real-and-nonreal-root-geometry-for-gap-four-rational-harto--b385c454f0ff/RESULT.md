# Exact real and nonreal root geometry for gap-four rational Hartogs kernels

## Finding
For every odd positive integer \(n\), set \(m=n+4\). Let \(Q_{m,n}\) be the standard degree-eight reciprocal polynomial obtained by restricting the Bergman-kernel numerator of the rational Hartogs triangle \(\mathbb H_{m/n}\) to the oblique product-coordinate slice. **Every \(Q_{n+4,n}\) has eight simple, nonzero roots: exactly four negative real roots and four nonreal roots.** Precisely four lie in the open unit disk. Among these interior roots, exactly two are negative real, one in each of the intervals
\[
\left(-1,-\frac{3-\sqrt5}{2}\right),\qquad
\left(-\frac{3-\sqrt5}{2},0\right),
\]
and the other two form a nonreal complex-conjugate pair. There are no roots on the unit circle. This **complete finite-parameter classification** includes every coprime numerator gap four, with no large-denominator restriction.

Equivalently, writing \(Q_{m,n}(z)=z^4F_n(z+z^{-1})\), the degree-four polynomial \(F_n\) has exactly two distinct real zeros, one in \(( -\infty,-3)\), the other in \((-3,-2)\), and exactly two conjugate nonreal zeros. Thus the two negative real interior Bergman-kernel zero-product levels are uniformly separated by the golden-ratio-related point \(-(3-\sqrt5)/2\).

## Assumptions and scope
Let \(\mathbb D\) denote the open complex unit disk. The rational Hartogs triangle is
\[
\mathbb H_{m/n}=\{(z_1,z_2)\in\mathbb C^2: |z_1|^m<|z_2|^n<1\},\qquad m=n+4,\quad n\ge1\text{ odd}.
\]
This pair is coprime because \(\gcd(n,n+4)=\gcd(n,4)=1\). For two points \(z,w\in\mathbb H_{m/n}\), let \(s=z_1\overline{w_1}\) and \(t=z_2\overline{w_2}\). The standard Bergman-kernel formula is
\[
K_{m/n}(z,w)=\frac{P_{m,n}(s,t)}{m\pi^2(1-t)^2(t^n-s^m)^2},\quad
Q_{m,n}(\zeta)=\zeta^{1-2n}P_{m,n}(\zeta,\zeta).
\]
Every \(0<|\zeta|<1\) arises from \(s=t=\zeta\) for a pair of points in the domain, and the displayed kernel denominator does not vanish there. Accordingly, every interior root of \(Q_{m,n}\) is a genuine zero-product level for the Bergman kernel on this oblique slice. This **does not** classify arbitrary off-slice zeros, and \(s=t\) is **not** the Hermitian diagonal \(z=w\).

For an integer \(a\), define the triangular weight \(W_m(a)=\max\{m-|a|,0\}\). The exact, previously established centered formula is
\[
Q_{m,n}(\zeta)=\sum_{A,B\in\mathbb Z}W_m(A)W_m(nA+mB)\zeta^{4+A+B}.
\]
The sum is finite and reciprocal, with positive leading and constant coefficients.

## Proof
**Step 1: exact gap-four coefficient identities.** Put \(c_j=[\zeta^j]Q_{n+4,n}(\zeta)\). Re-indexing by \(t=A+B\), and using \(n=m-4\), yields the finite expression
\[
c_{4+t}=\sum_{A\in\mathbb Z}W_m(A)W_m(mt-4A),\qquad -4\le t\le4.
\]
Evenness of \(W_m\) gives \(c_{4+t}=c_{4-t}\). Consequently the polynomial has the form
\[
Q_{m,n}(\zeta)=a(1+\zeta^8)+b(\zeta+\zeta^7)+c(\zeta^2+\zeta^6)+d(\zeta^3+\zeta^5)+e\zeta^4.
\]
Write \(n=4h+r\), with \(h\) a nonnegative integer and \(r\in\{1,3\}\). Direct summation of the quadratic triangular products gives the following **exact identities for all** \(h\ge0\):

For \(r=1\),
\[
\begin{aligned}
a&=(h+1)(h+2)(4h+3)/6,\\
b&=(h+1)(4h^2+11h+8),\\
c&=(h+1)(2h+3)(4h+5),\\
d&=(h+1)(12h^2+33h+22),\\
e&=(44h^3+165h^2+217h+99)/3.
\end{aligned}
\]
For \(r=3\),
\[
\begin{aligned}
a&=(h+1)(h+2)(4h+9)/6,\\
b&=(h+2)(4h^2+13h+11),\\
c&=(h+2)(2h+3)(4h+7),\\
d&=(h+2)(12h^2+39h+31),\\
e&=(44h^3+231h^2+415h+255)/3.
\end{aligned}
\]
Here is a direct way to verify the summation rather than relying on interpolation. Set \(L=h+1\), \(m=4L+r\), \(v=2L\) if \(r=1\) and \(v=2L+1\) if \(r=3\), and \(w=3L\) if \(r=1\) and \(w=3L+2\) if \(r=3\). The five coefficients are
\[
\begin{aligned}
a&=\sum_{A=w+1}^{m-1}(m-A)(4A-3m),\\
b&=\sum_{A=v+1}^{w}(m-A)(4A-2m)+\sum_{A=w+1}^{m-1}(m-A)(4m-4A),\\
c&=\sum_{A=L+1}^{v}(m-A)(4A-m)+\sum_{A=v+1}^{w}(m-A)(3m-4A),\\
d&=\sum_{A=1}^{L}(m-A)4A+\sum_{A=L+1}^{v}(m-A)(2m-4A),\\
e&=m^2+2\sum_{A=1}^{L}(m-A)(m-4A).
\end{aligned}
\]
All summands are quadratic in \(A\), and the displayed closed forms follow from \(\sum_{A=1}^N A=N(N+1)/2\) and \(\sum_{A=1}^N A^2=N(N+1)(2N+1)/6\). They are also checked as **symbolic identities in \(h\)** by the accompanying standalone checker.

**Step 2: reciprocal degree-four reduction.** With \(y=\zeta+\zeta^{-1}\), write
\[
F_n(y)=a(y^4-4y^2+2)+b(y^3-3y)+c(y^2-2)+dy+e.
\]
The elementary identities \(\zeta^j+\zeta^{-j}\) as polynomials in \(y\) prove \(Q_{n+4,n}(\zeta)=\zeta^4 F_n(y)\) for every \(\zeta\ne0\). Direct substitution into the coefficients gives
\[
F_{4h+1}(-2)=4h+5,\qquad F_{4h+3}(-2)=4h+7,
\]
and
\[
\begin{aligned}
F_{4h+1}(-3)&=-(12h^3+45h^2+85h+50)/2<0,\\
F_{4h+3}(-3)&=-(12h^3+63h^2+139h+124)/2<0.
\end{aligned}
\]
The leading coefficient \(a\) is positive. Consequently \(F_n\) has at least one real zero in \((-3,-2)\), and at least one in \((-\infty,-3)\).

**Step 3: exact upper bound of two real roots below \(-2\).** Substitute \(y=-2-u\). For \(r=1\), the coefficients of \(F_n(-2-u)\), in increasing order of powers of \(u\), are
\[
\begin{aligned}
&4h+5,\\
&-2(h+1)(8h^2+22h+27)/3,\\
&-(h+1)(8h^2+22h+39)/3,\\
&h(h+1)(4h+11)/3,\\
&(h+1)(h+2)(4h+3)/6.
\end{aligned}
\]
For \(r=3\), they are
\[
\begin{aligned}
&4h+7,\\
&-2(h+2)(8h^2+26h+33)/3,\\
&-(h+2)(8h^2+26h+45)/3,\\
&(h+2)(h+3)(4h+1)/3,\\
&(h+1)(h+2)(4h+9)/6.
\end{aligned}
\]
For every integer \(h\ge0\), the nonzero signs in either sequence are \(+,-,-,+,+\) (the fourth entry may be zero at \(h=0,r=1\)). Descartes' rule of signs therefore gives **at most two** positive roots of \(u\mapsto F_n(-2-u)\), counting multiplicity. Step 2 provides two distinct such roots, hence exactly two, both simple.

**Step 4: exclusion of all other real reduced roots.** If \(y>2\), write \(y=\zeta+\zeta^{-1}\) with \(\zeta>1\) real. Because the coefficient formulas in Step 1 are strictly positive, \(Q_{m,n}(\zeta)>0\), and hence \(F_n(y)>0\). For \(-2\le y\le2\), take \(\zeta=e^{i\theta}\) and \(y=2\cos\theta\). The known all-gap Fejér-product positivity theorem of Deng and Fu gives \(\zeta^{-4}Q_{m,n}(\zeta)>0\) for every real \(\theta\). Thus \(F_n(y)>0\) on \([-2,2]\). The two simple real reduced roots found in Step 3 are the **only** real roots of \(F_n\); the remaining two roots form a nonreal conjugate pair and are automatically simple.

**Step 5: location and multiplicity of Bergman zeros.** Every root \(y\) of \(F_n\) yields exactly the two reciprocal roots of \(\zeta^2-y\zeta+1=0\). None has \(|\zeta|=1\), by Step 4, and none equals \(0\). Distinct simple reduced roots away from \(y=\pm2\) produce distinct simple roots of \(Q_{m,n}\). For a real reduced root \(y<-2\), both reciprocal roots are strictly negative and exactly one is in \((-1,0)\); explicitly the interior root is \((y+\sqrt{y^2-4})/2\). Since \(y\mapsto(y+\sqrt{y^2-4})/2\) is strictly decreasing on \((-\infty,-2)\), the two reduced-root intervals from Step 2 give precisely the two stated real-root intervals, separated by the image of \(y=-3\), namely \(-(3-\sqrt5)/2\). Each of the two nonreal reduced roots produces one interior and one exterior root; the two interior ones are conjugates. This accounts for all eight zeros and proves the classification.

## Verification
Run `python3 CHECK.py` with SymPy (see `requirements.txt`). The program independently constructs each polynomial from the finite tent-weight formula on a grid of admissible parameters, proves the five closed coefficient formulas by symbolic finite summation for **arbitrary nonnegative \(h\)** in both residue classes, checks the two transformed-quartic sign identities symbolically, and tests the predicted root geometry for initial members. The infinite theorem is Steps 1–5, not the finite numerical checks.

## Relationship to prior work
Edholm and Mathew's original 2025 article provides the exact rational Hartogs numerator, the reciprocal oblique-slice polynomial, and explicit formulas for numerator gaps one and two. In Section 4.3 the authors describe further unit-circle nonvanishing computations including gap four, but neither that section nor their preceding low-gap formulas provides the present full finite-denominator classification of **simple real versus nonreal roots** for gap four. Deng and Fu's November 2026 theorem establishes strict unit-circle positivity and the *number* of interior roots for all numerator gaps; that theorem is used and credited in Step 4, not claimed as new here.

Relevant published gap-three root geometry and arbitrary-fixed-gap condensation results determine roots in gap three or asymptotically as \(n\to\infty\), respectively. They do not imply the exact classification for **every** odd \(n\) in gap four, particularly the universal finite-denominator simplicity and two strict real-root brackets. An independent all-gap first-order boundary-layer law similarly concerns only sufficiently large denominators. No claim is made for new unit-circle positivity, the general polynomial formula, or the previously published asymptotic limits.

## Limitations
The theorem is about a canonical one-complex-dimensional slice of the full Bergman-kernel zero variety, not its entire two-variable zero locus. The finite gap \(m-n=4\) is fixed; no claim is made for larger arbitrary gaps. The two nonreal roots inside the disk are not individually expressed in closed radical form, though the defining quartic is completely explicit. Existing coefficient formulas allow this finite case to be studied in principle, so the contribution is the **complete all-parameter root-type, simplicity, and interval classification**, not a new representation of the Bergman kernel. Specialist work under different root-geometry terminology may still affect publication priority; no independent mathematical audit has been performed.

## References
1. L. D. Edholm and V. T. Mathew, *Arithmetic properties and zeros of the Bergman kernel on a class of quotient domains*, arXiv:2505.20489, first publicly posted May 26, 2025; *Mathematische Zeitschrift* **313** (2026), article 43, especially Proposition 4.8 and Section 4.3. https://arxiv.org/abs/2505.20489
2. G. Deng and Q. Fu, *Bergman Kernel Zeros on Rational Hartogs Triangles*, arXiv:2611.07480v1, first publicly posted November 5, 2026, especially Lemma 2.1, Lemma 3.1, and Theorem 1.1. https://arxiv.org/html/2611.07480v1
3. *Cubic-root condensation of diagonal Bergman-kernel zeros in gap-three Hartogs triangles*, mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cubic-root-condensation-of-diagonal-bergman-kernel-zeros-in-gap--78891bb4627f
4. *Universal fixed-gap condensation of rational Hartogs Bergman zeros*, mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-universal-fixed-gap-condensation-of-rational-hartogs-bergman-zer--6878ab13c2f7
5. *Arithmetic boundary layers for zeros of rational Hartogs Bergman numerators*, mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-arithmetic-boundary-layers-for-zeros-of-rational-hartogs-bergman--ecf008592e97
