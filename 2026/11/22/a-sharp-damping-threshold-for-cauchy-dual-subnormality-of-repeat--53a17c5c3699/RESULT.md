# A sharp damping threshold for Cauchy-dual subnormality of repeated-pole six-isometric shifts

## Finding

Let \(a,b,c>0\) and put
\[
P_{a,b,c}(x)=\frac{(x+a)((x+b)^2+c^2)^2}{a(b^2+c^2)^2},\qquad
W_{a,b,c}e_n=\left(\frac{P_{a,b,c}(n+1)}{P_{a,b,c}(n)}\right)^{1/2}e_{n+1}
\quad(n\geq0)
\]
on \(\ell^2(\mathbb N_0)\). The shift \(W_{a,b,c}\) is a bounded, expansive, strict \(6\)-isometry. Its Cauchy dual \(W'_{a,b,c}=W_{a,b,c}(W_{a,b,c}^*W_{a,b,c})^{-1}\) is a contractive unilateral weighted shift.

Let \(z_2\) be the unique root of \(\tan z=z\) in \((2\pi,5\pi/2)\), and let \(\rho_*\) be the unique positive solution of
\[
 e^{-\rho_*z_2}\frac{(1+\rho_*^2)z_2^2+2\rho_*z_2+2}{\sqrt{1+z_2^2}}=2.
\]
Numerically, \(z_2=7.725251836937707\ldots\) and \(\rho_*=0.1882529338801995\ldots\). Then the **exact** subnormality criterion is
\[
\boxed{\;W'_{a,b,c}\text{ is subnormal}\quad\Longleftrightarrow\quad b-a\geq \rho_*c.\;}
\]
At equality, the canonical Berger measure has a density vanishing at exactly one interior point of \((0,1)\); above threshold its density is strictly positive throughout \((0,1)\). Below threshold the unique signed representing density is negative on an open interval.

## Assumptions and scope

The parameters \(a,b,c\) are arbitrary positive real numbers. All operators act on complex \(\ell^2(\mathbb N_0)\), with \(\{e_n\}_{n\geq0}\) its canonical orthonormal basis. A unilateral shift with nonzero weights \(\{w_n\}\) is subnormal when it has a normal extension; equivalently, its squared weight products from \(e_0\) are a Stieltjes moment sequence. For a contractive shift, a Stieltjes representing measure is supported on \([0,1]\).

An operator \(T\) is \(m\)-isometric when \(\sum_{j=0}^m(-1)^{m-j}\binom mj T^{*j}T^j=0\). The designation *strict* means it is \(m\)-isometric but not \((m-1)\)-isometric. No claim is made for arbitrary quintic moments or for operator-valued weights.

## Proof

**1. Polynomial shift construction and Cauchy dual.** Since \(P_{a,b,c}(0)=1\) and \(P_{a,b,c}\) is strictly increasing on \([0,\infty)\), every squared weight is greater than \(1\). As the quotient \(P(n+1)/P(n)\to1\), the weights are bounded above and away from zero. Their products telescope:
\[
\|W_{a,b,c}^m e_k\|^2=\frac{P_{a,b,c}(k+m)}{P_{a,b,c}(k)}\qquad(k,m\geq0).
\]
Because \(P_{a,b,c}\) has degree \(5\) with positive leading coefficient, its sixth forward difference is identically zero while its fifth forward difference is nonzero. The diagonal form of \(\sum_{j=0}^{m}(-1)^{m-j}\binom mj W^{*j}W^j\) proves strict \(6\)-isometry. The Cauchy dual has weights \(\sqrt{P(n)/P(n+1)}<1\) and products
\[
\|(W'_{a,b,c})^m e_k\|^2=\frac{P_{a,b,c}(k)}{P_{a,b,c}(k+m)}.
\]
Thus subnormality is equivalent to the sequence \(\{1/P_{a,b,c}(m)\}_{m\geq0}\) being Hausdorff: necessity follows from the \(e_0\) moments and contractivity; sufficiency follows because any measure \(\mu\) with those moments gives all tail moments through the probability measures \(P(k)t^k\mu(dt)\).

**2. The unique signed density.** Define \(\rho=(b-a)/c\) and, for \(u\geq0\),
\[
g(u)=\sin u-u\cos u,\qquad
F_\rho(u)=\int_0^u e^{-\rho v}g(v)\,dv.
\]
The elementary Laplace-transform identity
\[
\mathcal L\left[\frac{e^{-bt}}{2c^3}(\sin(ct)-ct\cos(ct))\right](s)
=\frac1{((s+b)^2+c^2)^2}
\]
followed by convolution with \(e^{-at}\), yields the moment representation
\[
\frac1{P_{a,b,c}(m)}=
\int_0^1 x^m h_{a,b,c}(x)\,dx,\qquad
h_{a,b,c}(x)=\frac{a(b^2+c^2)^2}{2c^4}
 x^{a-1}F_\rho(c\log(1/x)).
\]
This density is continuous on \((0,1)\) and integrable; the integral identity holds for every integer \(m\geq0\). Uniqueness of signed finite Borel measures with prescribed moments on \([0,1]\), by polynomial density, shows that the reciprocal polynomial sequence is Hausdorff if and only if \(F_\rho(u)\geq0\) for every \(u>0\). The normalized measure is \(\mu(dx)=h_{a,b,c}(x)\,dx\) whenever it is positive.

**3. Critical-point reduction.** The positive zeros \(z_j\) of \(g(u)=0\) consist of exactly one root \(z_j\in(j\pi,(j+\tfrac12)\pi)\) for each integer \(j\geq1\). The function \(F_\rho\) increases from \(0\) to its first maximum at \(z_1\), then has successive alternating minima at \(z_2,z_4,\ldots\) and maxima at \(z_3,z_5,\ldots\), independently of \(\rho\). At a root \(z_j\), \(\sin z_j=z_j\cos z_j\) and \(\cos z_j=(-1)^j/\sqrt{1+z_j^2}\). Direct integration gives
\[
F_\rho(z_j)=\frac{2-(-1)^j Q_\rho(z_j)}{(1+\rho^2)^2},\qquad
Q_\rho(z)=e^{-\rho z}\frac{(1+\rho^2)z^2+2\rho z+2}{\sqrt{1+z^2}}>0.
\]
In particular, every positive-time local maximum of \(F_\rho\) is positive. Since
\[
\frac{\partial Q_\rho(z)}{\partial\rho}
=-e^{-\rho z}\frac{(1+\rho^2)z^3}{\sqrt{1+z^2}}<0\quad(z>0),
\]
and \(Q_0(z_2)=(z_2^2+2)/\sqrt{1+z_2^2}>2\) while \(Q_\rho(z_2)\to0\) as \(\rho\to+\infty\), there is a unique \(\rho_*>0\) with \(Q_{\rho_*}(z_2)=2\). For every \(\rho<\rho_*\), \(F_\rho(z_2)<0\), proving the *necessity* of the threshold, including negative \(\rho\).

**4. The first minimum controls every later minimum.** The threshold satisfies \(\rho_*>1/z_2\). Indeed,
\[
Q_{1/z_2}(z_2)=e^{-1}\frac{z_2^2+5}{\sqrt{1+z_2^2}}
>\frac{z_2}{e}>2,
\]
because \(z_2>2\pi>2e\) and \((z^2+5)/\sqrt{1+z^2}>z\). The derivative in the *spatial* variable is
\[
\frac{\partial Q_\rho(z)}{\partial z}
=-\frac{e^{-\rho z}z^2}{(1+z^2)^{3/2}}
\left[\rho(1+\rho^2)z^2+(\rho^2-1)z+\rho^3+3\rho\right].
\]
For \(\rho\geq\rho_*>1/z_2\) and \(z\geq z_2\), the bracket is strictly positive: its terms \(\rho z^2-z\) are nonnegative and the remaining terms \(\rho^3z^2+\rho^2z+\rho^3+3\rho\) are positive. Hence \(Q_\rho\) decreases strictly on \([z_2,\infty)\). At every even-indexed root \(z_{2j}\) we consequently have \(Q_\rho(z_{2j})\leq Q_\rho(z_2)\leq2\), so \(F_\rho(z_{2j})\geq0\); at all odd-indexed roots \(F_\rho(z_{2j-1})>0\). Monotonicity between successive stationary points, together with \(F_\rho(0)=0\), proves \(F_\rho(u)\geq0\) for every \(u\geq0\). This proves *sufficiency* and completes the equivalence.

At the threshold, strict spatial decrease of \(Q_\rho\) makes \(F_{\rho_*}(z_2)=0\) the only positive zero. Above it, all positive-time local minima are strictly positive. Replacing \(u\) by \(c\log(1/x)\) proves the assertions about the Berger density; its unique interior zero at equality is \(x=\exp(-z_2/c)\).

## Verification

The standalone `verify.py` recomputes the two scalar defining roots by bisection, tests the closed critical-point identity and a range of density signs, checks exact sixth differences and telescoping products using rational arithmetic, and compares numerical quadratures against reciprocal-polynomial moments. Its finite tests serve as reproducibility checks; the all-parameter sign classification is established by the argument above. Executing `python verify.py` requires only the Python standard library.

## Relationship to prior work

Buchała's *m-isometric weighted shifts with operator weights* (arXiv:2407.17233, first posted 24 July 2024) gives the general operator-polynomial model for \(m\)-isometric shifts, with earlier scalar structural results attributed there. Reza and Zhang's *Hausdorff moment sequences induced by rational functions* (arXiv:1903.00116, first posted 1 March 2019) develops the inversion/measure framework and classifies degree at most four; its degree-five discussion treats the equal-real-part case of one real pole and two nonreal conjugate pairs, including coincident pairs, but explicitly leaves the real-pole-dominant parameter regime outside the special classified case. Its necessary pole-dominance result excludes part of the complementary region. The new boundary \(b-a=\rho_*c\) lies **strictly within the previously unresolved positive-damping region**, and the assertion is a sharp classification for this repeated-conjugate-pair slice rather than a claim to the general rational-moment criterion. Nailwal's 2023 toral three-isometry work (arXiv:2310.04785) concerns two-variable lower-bidegree moment nets, not the present scalar degree-five denominator.

## Limitations

Only positive \(a,b,c\) and the repeated-conjugate-pair factorization stated above are covered. The method does not classify arbitrary quintic or higher-degree polynomials or arbitrary noncommuting operator-weighted shifts. The numerical value of \(\rho_*\) is approximate; its definition by an exact transcendental equation is authoritative. Numerical finite differences alone are not a certificate for all moment orders. Historical priority beyond the inspected accessible sources is not excluded; independent validation has not been conducted.

## References

1. M. Buchała, *m-isometric weighted shifts with operator weights*, arXiv:2407.17233 (2024), https://arxiv.org/abs/2407.17233.
2. Md. R. Reza and G. Zhang, *Hausdorff moment sequences induced by rational functions*, arXiv:1903.00116 (2019), https://arxiv.org/abs/1903.00116.
3. R. Nailwal, *A complete solution to the Cauchy dual subnormality problem for torally expansive toral three-isometric weighted two-shifts*, arXiv:2310.04785 (2023), https://arxiv.org/abs/2310.04785.
