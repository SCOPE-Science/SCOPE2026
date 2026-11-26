# A uniform vacuum gap for critical Cantor–Bergman localization

## Finding
For every integer \(m\ge2\), the radial Cantor localization operator defined below has a **uniform normalized gap** between its vacuum eigenvalue \(\lambda_{m,0}\) and all other monomial eigenvalues:
\[
\left(\frac32\right)^m\left(\lambda_{m,0}-\sup_{k\ge1}\lambda_{m,k}\right)>\frac1{200}.
\]
In particular the constant Bergman monomial is the unique top mode, and for any unit vector \(f\) its squared distance from the constant subspace is at most \(200(3/2)^m(\|T_m\|-\langle T_m f,f\rangle)\). The exact finite-stage norm formula and identification of the previously characterized balanced even-stage limit at the vacuum index are
\[
\|T_m\|=\int_{3^m C_{2m}}\frac{dt}{(1+t)^2},\qquad
\lim_{m\to\infty}\left(\frac32\right)^m\|T_m\|=\mathcal C:=\sum_{q\in\mathcal D}\int_0^1\frac{d\mu(u)}{(1+q+u)^2}.
\]
Here \(\mathcal D\) is the set of all nonnegative integers whose base-three digits belong to \(\{0,2\}\), and \(\mu\) is the standard middle-third Cantor probability measure. The series is absolutely convergent. Numerical finite-stage approximations suggest \(\mathcal C\approx0.65270\); this displayed decimal is not used as an analytical certificate.

## Assumptions and scope
Let \(C_n\subset[0,1]\) denote the usual \(n\)-step middle-third Cantor prefractal, a union of \(2^n\) closed intervals of length \(3^{-n}\). Equip \(A^2(\mathbb D)\) with \(\langle f,g\rangle=\int_{\mathbb D}f\overline g\,dA/\pi\). The monomials \(e_k(z)=\sqrt{k+1}\,z^k\), \(k\in\mathbb N_0\), form an orthonormal basis. For \(m\in\mathbb N\) set
\[
 E_m=3^m C_{2m},\qquad \Omega_m=\left\{z\in\mathbb D:\frac{|z|^2}{1-|z|^2}\in E_m\right\}.
\]
Define \(T_m\) by \(\langle T_m f,g\rangle=\int_{\Omega_m}f\overline g\,dA/\pi\). Let \(\delta=\log 2/\log3\in(0,1)\). Let \(\mu_n\) be the probability measure with density \((3/2)^n\mathbf1_{C_n}\) on \([0,1]\), and \(\mu=\lim_{n\to\infty}\mu_n\) weakly. Define \(\mathcal D_m\) as the base-three digit set \(\{\sum_{j=0}^{m-1}2\epsilon_j3^j:\epsilon_j\in\{0,1\}\}\) and \(\mathcal D=\bigcup_m\mathcal D_m\).

## Proof
**1. Exact spectral reduction.** Since the symbol is radial, the monomial basis diagonalizes \(T_m\). With \(t=|z|^2/(1-|z|^2)\) and the normalized area measure,
\[
 \lambda_{m,k}=\int_{E_m}g_k(t)\,dt,\qquad g_k(t)=\frac{(k+1)t^k}{(1+t)^{k+2}},\quad k\ge0.
\]
The exact two-scale decomposition \(E_m=\bigcup_{q\in\mathcal D_m}(q+C_m)\) (up to interval endpoints) yields the finite measure
\[
 \nu_m:=\left(\frac32\right)^m\mathbf1_{E_m}(t)\,dt=\sum_{q\in\mathcal D_m}\delta_q*\mu_m,
\qquad L_{m,k}:=\left(\frac32\right)^m\lambda_{m,k}=\int g_k\,d\nu_m.
\]
Here \(\delta_q\) denotes a point mass, not the Cantor dimension.

**2. Uniform Cantor growth.** Every finite-stage Cantor distribution function satisfies
\[
 F_{\mu_n}(x)\le x^\delta\quad (0\le x\le1).
\]
Proof by induction from \(F_{\mu_0}(x)=x\) uses the two self-similar branches. On the right branch the necessary inequality is \(1+y^\delta\le(2+y)^\delta\) for \(0\le y\le1\), whose difference decreases to zero at \(y=1\). Since \(\nu_m([0,t])=2^m F_{\mu_{2m}}(t/3^m)\), with the distribution function extended by zero below zero and one above one, it follows **for every** \(t\ge0\) that
\[
 F_m(t):=\nu_m([0,t])\le t^\delta.
\]
For \(t\ge3^m\), this follows from \(\nu_m([0,t])=2^m\le t^\delta\). This uniform inequality is the key global estimate.

**3. A uniform bound for every nonconstant monomial.** For \(k\ge1\), the density \(g_k\) increases up to \(a_k=k/2\) and decreases afterwards. Stieltjes integration by parts and \(F_m(t)\le t^\delta\) give
\[
 L_{m,k}\le a_k^\delta g_k(a_k)+\delta\int_{a_k}^\infty t^{\delta-1}g_k(t)\,dt\le A_k+J_k,
\]
where \(A_k=(k/2)^\delta g_k(k/2)\) and
\[
 J_k=\frac{\delta\Gamma(k+\delta)\Gamma(2-\delta)}{\Gamma(k+1)}.
\]
The exact recurrence \(J_{k+1}/J_k=(k+\delta)/(k+1)<1\) proves that \(J_k\) decreases. The logarithmic derivative of \(A_x\), treating its index continuously, is
\[
 \frac{d}{dx}\log A_x=\frac{\delta}{x}+\frac1{x+1}-\log(1+2/x)<0\quad(x\ge2).
\]
Indeed \(\log(1+2/x)\ge2/(x+1)\) and \(\delta/x<1/(x+1)\) for \(x\ge2\). Hence \(A_k\le A_2=3/16\) for \(k\ge2\). Elementary enclosures \(0.6309<\delta<0.6310\), \(\pi<3.14160\) and \(\sin(\pi\delta)>0.915\), obtainable from alternating Taylor inequalities, imply
\[
 J_1=\frac{\pi\delta^2(1-\delta)}{\sin(\pi\delta)}<0.505,
 \qquad J_2=\frac{1+\delta}{2}J_1<0.412.
\]
Consequently \(L_{m,k}<0.600\) for all \(k\ge2\), independently of \(m\).

For \(k=1\), retain the negative contribution from the increasing part of \(g_1\). Since \(g_1(t)=2t/(1+t)^3\),
\[
 L_{m,1}\le A_1+J_1-\delta\int_0^{1/2}t^{\delta-1}g_1(t)\,dt
\le A_1+J_1-\frac{2\delta}{\delta+1}\frac{2^{-1-\delta}}{(3/2)^3}.
\]
The same elementary interval enclosures yield \(A_1=(8/27)2^{-\delta}<0.192\) and the last positive term \(>0.073\); thus \(L_{m,1}<0.624\) for all \(m\).

**4. A strict four-cylinder lower bound for the vacuum.** For \(m\ge2\), all four shifts \(q\in\{0,2,6,8\}\) belong to \(\mathcal D_m\). Conditional on the first Cantor digit, \(\mu_m\) has mean \(1/6\) or \(5/6\) with probability \(1/2\) each. By convexity of \(u\mapsto(1+q+u)^{-2}\),
\[
 L_{m,0}\ge\frac12\sum_{q\in\{0,2,6,8\}}
 \left[\frac1{(1+q+1/6)^2}+\frac1{(1+q+5/6)^2}\right]
 =\frac{253146344807189721168}{402458387931340458025}>0.629.
\]
Thus \(L_{m,0}>0.629\), whereas \(\sup_{k\ge1}L_{m,k}\le0.624\). The difference is strictly greater than \(1/200\). This proves that \(k=0\) is the unique maximizing index and gives the stated finite-stage norm. Expanding a unit vector in the monomial basis bounds its Rayleigh deficit below by the spectral gap times the sum of the squared nonconstant coefficients, giving the distance estimate.

**5. Sharp limiting constant.** On each bounded interval, \(\nu_m\) converges weakly to \(\nu:=\sum_{q\in\mathcal D}\delta_q*\mu\): for fixed \(q\), \(\mu_m\Rightarrow\mu\), while sufficiently large shifts cannot meet a fixed compact set. The uniform bound \(F_m(t)\le t^\delta\) supplies a uniform tail estimate for \(g_0(t)=(1+t)^{-2}\): by integration by parts,
\[
 \int_{(R,\infty)}g_0\,d\nu_m\le 2\int_R^\infty\frac{t^\delta}{(1+t)^3}\,dt=O(R^{\delta-2}),
\]
with an implied constant independent of \(m\). It also bounds the corresponding tail for \(\nu\). Therefore \(L_{m,0}\to\int g_0\,d\nu=\mathcal C\), strictly positive and finite. This completes the proof.

## Verification
The included standalone `CHECK.py` uses exact rational arithmetic for the four-cylinder bound, checks the interval inequalities used above, and independently computes finite-stage normalized eigenvalues from exact rational interval endpoints. It prints its test count. These tests are supplementary; the result for all indices and all \(m\ge2\) follows from the analytical estimates in the proof.

## Relationship to prior work
Abreu, Mouayn and Voigtlaender establish the beta-prime eigenvalue representation and sharp two-sided order for middle-third Cantor Bergman localization (arXiv:2201.11705, Proposition 4.1, Theorem 2.1 and Proposition 4.5; their unweighted parameter is \(\alpha=1/2\)). *Sharp subsequential constants for Bergman concentration on balanced Cantor annuli* [4] gives the same normalized even-stage limit as a maximum over monomial indices (their unweighted parameter is \(b=1\)), without identifying the index. Knutsen's studies concern Gaussian-window time-frequency localization. The Gaussian dominance theorem [5] for all radial Cantor scales also implies qualitative Bergman dominance: \(g_k(t)=\int_0^\infty e^{-s}s e^{-st}(st)^k/k!\,ds\), so each Bergman eigenvalue is an average of the corresponding Gaussian eigenvalues over dilations. The explicit stage-independent gap at the normalized Bergman scale here uses the Cantor growth and four-cylinder estimates above.

## Limitations
The unique-maximizer statement is proved for all integers \(m\ge2\), not every real dilation or every Bergman weight. The sharp constant is expressed as a convergent Cantor integral series, not a claimed elementary closed form. The displayed decimal approximation is exploratory. The result does not provide convergence rates or a classification of other real dilation phases. An equivalent unlocated statement in earlier literature remains possible; independent mathematical validation has not been performed.

## References
Abreu, L. D., Mouayn, Z., and Voigtlaender, F., *A fractal uncertainty principle for Bergman spaces and analytic wavelets*, arXiv:2201.11705 (first public 2022-01-27), J. Math. Anal. Appl. 519 (2023), 126699.

Knutsen, H., *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets*, arXiv:1907.00848 (2019).

Knutsen, H., *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets II*, arXiv:2104.10976 (2021).

[4] *Sharp subsequential constants for Bergman concentration on balanced Cantor annuli*, https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-sharp-subsequential-constants-for-bergman-concentration-on-balan--23a4c7691d0b.

[5] *Exact Gaussian spectral dominance for every radial middle-third Cantor mask*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-gaussian-spectral-dominance-for-every-radial-middle-third--4db46e8786d3.
