# Sharp doubled-window extrapolation for symmetric three-frequency Fourier sums

## Finding

Let \(\omega>0\) and let \(a,b,c\in\mathbb C\) be not all zero. Define
\[
g(t)=a+b e^{i\omega t}+c e^{-i\omega t},\qquad
\|g\|_{\mathrm{av}}^2=\frac12\int_{-1}^1|g(t)|^2\,dt.
\]
Then the sharp, frequency-uniform **doubled-aperture** estimate is
\[
\boxed{|g(2)|^2<\frac{657}{4}\,\|g\|_{\mathrm{av}}^2.}
\]
The strict constant is the supremum over all positive gaps and all nonzero coefficient triples; it is never attained at positive gap. It is approached as \(\omega\downarrow0\) by suitably normalized sums converging to the degree-two Legendre evaluation kernel at \(t=2\). The same statement holds at \(t=-2\) by reflection and for a common frequency carrier by modulation.

At each fixed \(\omega>0\), the **exact** squared norm of evaluation is
\[
K_\omega(2)=\frac{E}{D}+\frac{O}{T},
\]
where
\[
s=\frac{\sin\omega}{\omega},\quad b_*=\frac{\sin(2\omega)}{2\omega},\quad
D=\frac{1+b_*}{2}-s^2,\quad T=1-b_*,
\]
\[
E=\frac{1+b_*}{2}-2s\cos(2\omega)+\cos^2(2\omega),
\qquad O=1-\cos(4\omega).
\]
All fixed-gap equality cases are nonzero scalar multiples of the reproducing kernel for evaluation at \(t=2\) in this three-dimensional space.

## Assumptions and scope

Only the symmetric real-frequency triple \(\{-\omega,0,\omega\}\) is considered; coefficients are arbitrary complex numbers and no lower bound on the gap is assumed. The observation norm is the **averaged** squared \(L^2\) norm on \([-1,1]\), not the unnormalized integral. The evaluation point \(2\) is the end of the adjacent exterior unit interval. No inequality for arbitrary three-frequency configurations, arbitrary exterior points, or arbitrary sparsity is claimed.

## Proof

**1. Exact reproducing kernel.** Put \(q(t)=\cos(\omega t)\) and \(r(t)=\sin(\omega t)\). The functions \(1,q,r\) span precisely the same complex space as the three exponentials. On the symmetric observation interval, \(r\) is orthogonal to both even functions. Their averaged Gram matrix is
\[
\begin{pmatrix}1&s&0\\s&(1+b_*)/2&0\\0&0&(1-b_*)/2\end{pmatrix}.
\]
It is strictly positive definite because the three functions are linearly independent when \(\omega>0\). Inverting its even block and evaluating \((1,\cos 2\omega,\sin 2\omega)\) gives exactly \(K_\omega(2)=E/D+O/T\). In particular, \(D,T>0\).

**2. Positivity problem.** Set \(C=657/4\), \(u=\omega^2\), and introduce the entire power-series functions
\[
A(u)=\sum_{j\ge0}\frac{(-1)^j u^j}{(2j+1)!},\quad
B(u)=\sum_{j\ge0}\frac{(-1)^j2^{2j}u^j}{(2j+1)!},
\]
\[
H(u)=\sum_{j\ge0}\frac{(-1)^j2^{2j}u^j}{(2j)!},\quad
J(u)=\sum_{j\ge0}\frac{(-1)^j4^{2j}u^j}{(2j)!}.
\]
Thus \(A(u)=s\), \(B(u)=b_*\), \(H(u)=\cos2\omega\), and \(J(u)=\cos4\omega\) when \(u=\omega^2\). Define
\[
D(u)=\frac{1+B(u)}2-A(u)^2,\quad T(u)=1-B(u),
\]
\[
E(u)=\frac{1+B(u)}2-2A(u)H(u)+H(u)^2,\quad O(u)=1-J(u),
\]
\[
F(u)=C D(u)T(u)-E(u)T(u)-O(u)D(u).
\]
The desired strict inequality is equivalent to \(F(u)>0\) for every \(u>0\).

**3. Exact finite rational certificate on \(0<u\le9\).** Let \(F_{70}\) denote the Taylor polynomial of \(F\) through degree \(70\), computed by formal rational power-series multiplication. Its coefficients in degrees \(0,1,2,3\) vanish and the first coefficients are
\[
F_{70}(u)=\frac{9391}{6300}u^4-\frac{135179}{151200}u^5+\frac{8552807}{31752000}u^6+\cdots.
\]
Put \(P(u)=F_{70}(u)/u^4\), a polynomial of degree at most \(66\). For every integer \(h\in\{0,\dots,8\}\), expand \(P(h+t)\) in the Bernstein basis of degree \(66\) on \(0\le t\le1\). **Every one of the \(9\times67\) rational Bernstein coefficients is strictly greater than \(1/100\)**. This is checked by the standalone `CHECK.py`: it constructs all coefficients as exact fractions and verifies the inequalities. Since Bernstein basis functions are nonnegative and sum to one, \(P(u)>1/100\) on \([0,9]\).

To bound truncation independently of numerical approximation, on the complex disk \(|u|=100\), coefficientwise majorization of these entire series gives
\[
|A|<10^4,\quad|B|<2\cdot10^8,\quad|H|<4\cdot10^9,\quad|J|<2\cdot10^{19}.
\]
These follow from the corresponding hyperbolic-sine/cosine series and the elementary bound \(e<3\). Consequently \(|D|<3\cdot10^8\), \(|T|<3\cdot10^8\), \(|E|<2\cdot10^{19}\), \(|O|<3\cdot10^{19}\), and \(|F|<10^{29}\). Cauchy's coefficient bound gives, for \(0<u\le9\),
\[
\frac{|F(u)-F_{70}(u)|}{u^4}
\le\frac{10^{29}\,u^{67}}{100^{71}(1-u/100)}
\le\frac{10^{29}\,9^{67}\,100}{100^{71}\,91}
<\frac1{1000}.
\]
The last strict comparison is an exact integer assertion independently checked in `CHECK.py`. Therefore \(F(u)> (1/100-1/1000)u^4=9u^4/1000>0\) on \(0<u\le9\). The certificate uses a finite rational computation together with an analytic remainder proof, not numerical sampling of an infinite range.

**4. Large gaps.** For \(\omega\ge3\), use the exponential basis \(e^{-i\omega t},1,e^{i\omega t}\). Its averaged Gram matrix has diagonal entries one and off-diagonal entries \(\operatorname{sinc}(\omega)\) or \(\operatorname{sinc}(2\omega)\), where \(\operatorname{sinc}(v)=\sin(v)/v\). Every off-diagonal absolute row sum is at most \(2/\omega\le2/3\). The eigenvalues are therefore at least \(1/3\) by Gershgorin's theorem. The evaluation vector at \(2\) has squared Euclidean norm three, so
\[
K_\omega(2)\le\frac{3}{1/3}=9<657/4.
\]
The two ranges together establish the strict inequality for all \(\omega>0\).

**5. Sharpness, nonattainment and fixed-gap equality.** As \(\omega\downarrow0\), the three-dimensional spaces \(\operatorname{span}\{1,\cos\omega t,\sin\omega t\}\), after nonsingular rescaling of basis vectors, converge in their Gram matrices and evaluation vectors to the quadratic polynomial space \(\operatorname{span}\{1,t,t^2\}\). Its averaged-\(L^2\) orthogonal basis is the Legendre family \(P_0=1\), \(P_1=t\), \(P_2=(3t^2-1)/2\). Hence the limit of the squared evaluation norm at \(2\) is
\[
\sum_{j=0}^2(2j+1)P_j(2)^2=1+12+5(11/2)^2=657/4.
\]
The limiting reproducing kernel is \(1+6t+(55/2)P_2(t)\). At every positive gap the exact fixed-gap reproducing kernel constructed in step 1 attains \(K_\omega(2)\) by equality in Cauchy–Schwarz, whereas step 3 or 4 shows \(K_\omega(2)<657/4\). This proves the universal sharpness and nonattainment.

## Verification

Run `python3 CHECK.py` using Python's standard library. It reconstructs the Taylor coefficients from the four entire series, checks cancellation through cubic order, computes every Bernstein coefficient as an exact rational number on the nine unit intervals in \(u\), and checks the exact integer tail inequality. The output should conclude `Exact polynomial positivity and analytic-tail certificate: PASS`. The analytic argument supplies Cauchy's inequality, the complex-disk bound and the large-frequency Gershgorin step. The checker certifies only the finite rational algebra it actually performs.

## Relationship to prior work

Ruizhe Zhang's 2026 sparse-Fourier extrapolation theorem gives frequency-independent Chebyshev-scale bounds and discusses exterior leverage, including \(x=2\), but does not state the exact three-tone coefficient here. The existing symmetric three-tone endpoint Nikolskii calculation gives a sharp constant for **\(x=1\)**, not for the doubled-window point \(x=2\). A sharp two-frequency exterior leverage theorem controls a two-dimensional span and does not imply the three-dimensional bound. The polynomial Legendre kernel supplies only the collision-limit lower bound, not the positive-gap inequality certified above.

## Limitations

This is a sharp, natural fixed-location extrapolation result, **not** a theorem uniformly sharp for all exterior evaluation locations or all sets of three frequencies. The positivity certificate is computer-assisted but exact, independently checkable with the included complete source. It has not undergone independent mathematical validation. A specialized earlier formulation of the same sharp extrapolation inequality may exist despite the searches and inspections cited here.

## References

1. Ruizhe Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501, first public version July 11, 2026, https://arxiv.org/abs/2607.10501.
2. *Sharp endpoint Nikolskii constant for symmetric three-tone Fourier sums*, published-finding corpus published research, November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-endpoint-nikolskii-constant-for-symmetric-three-tone-fouri--e11889d28f9d.
3. *Sharp two-frequency exterior Fourier leverage and the quadratic collision defect*, published-finding corpus published research, November 1, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-frequency-exterior-fourier-leverage-and-the-quadratic--517d41b07a68.
4. Classical Legendre polynomial orthogonality and reproducing kernels for quadratic polynomials.
