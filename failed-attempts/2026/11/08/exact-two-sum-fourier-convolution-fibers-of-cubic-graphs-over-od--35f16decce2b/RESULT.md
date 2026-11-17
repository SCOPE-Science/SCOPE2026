# Exact two-sum Fourier-convolution fibers of cubic graphs over odd cyclic rings

## Finding
For an odd prime \(p\) and integer \(k\ge1\), put \(q=p^k\), \(R=\mathbb Z/q\mathbb Z\) and
\[
C_q=\{(x,x^3):x\in R\}\subset R^2.
\]
Let \(r_q(s,t)\) count **ordered** pairs \((x,y)\in R^2\) with \(x+y=s\) and \(x^3+y^3=t\). These are exactly the coefficients of \(1_{C_q}*1_{C_q}\). The complete representation-multiplicity function has the following closed description, including every zero fiber.

For \(s\in R\), choose any integer representative and set
\[
h=\min\{k,v_p(3s)\},\qquad v_p(0)=+\infty.
\]
If \(h=k\), then \(r_q(s,t)=q\) for the unique \(t\equiv4^{-1}s^3\pmod q\), and it is zero otherwise. If \(h<k\), put \(\ell=k-h\), \(c=(3s)/p^h\), a unit modulo \(p^\ell\), and \(z=4t-s^3\). If \(z\not\equiv0\pmod{p^h}\), then \(r_q(s,t)=0\). Otherwise let
\[
w\equiv(z/p^h)c^{-1}\pmod{p^\ell}.
\]
Then
\[
\boxed{r_q(s,t)=p^h\,\#\{u\bmod p^\ell:u^2\equiv w\pmod{p^\ell}\}.}
\]
More explicitly, for **each fixed** \(s\) with \(h<k\), the positive multiplicities among all \(q\) target values \(t\) are as follows:

* One target has multiplicity \(p^{h+\lfloor\ell/2\rfloor}\).
* For each integer \(a\) satisfying \(0\le a<\ell/2\), exactly \(\frac{p-1}{2}p^{\ell-2a-1}\) targets have multiplicity \(2p^{h+a}\).
* Every remaining target has multiplicity zero.

These are disjoint multiplicity classes because \(p\) is odd. Thus the **entire twofold-sum representation spectrum** is determined, rather than merely its fourth moment.

Define
\[
T_p(\ell)=\begin{cases}
1+\frac{p(p^\ell-1)}{2(p+1)},&\ell\ \text{even},\\
1+\frac{p^{\ell+1}-1}{2(p+1)},&\ell\ \text{odd}.
\end{cases}
\]
The exact sumset size is
\[
\boxed{|C_q+C_q|=\begin{cases}
1+(p-1)\sum_{\ell=1}^{k}p^{\ell-1}T_p(\ell),&p\ne3,\\
3+2\sum_{\ell=1}^{k-1}3^\ell T_3(\ell),&p=3.
\end{cases}}
\]
In particular, there is a genuine arithmetic branch at \(p=3\), where the reduction modulo \(3\) of the cubic graph becomes an additive subgroup.

The exact ordered additive energy (the squared convolution norm) is
\[
\boxed{E(C_q)=\sum_{s,t\in R}r_q(s,t)^2
=\begin{cases}
q^2\left[1+k\left(1-\frac1p\right)
+\frac{k(k+1)}2\left(1-\frac1p\right)^2\right],&p\ne3,\\[2pt]
3^{2k-1}(2k^2+4k+3),&p=3.
\end{cases}}
\]
For the constant-input Fourier extension \(\mathcal E_q1(\xi,\eta)=q^{-1}\sum_{x\in R}e^{2\pi i(\xi x+\eta x^3)/q}\), with counting measure on \(R^2\), character orthogonality yields the exact fourth moment
\[
\boxed{\sum_{\xi,\eta\in R}|\mathcal E_q1(\xi,\eta)|^4=E(C_q)/q^2.}
\]
The normalized fourth moment consequently grows quadratically in the prime-power exponent, unlike the linear depth dependence of the quadratic-parabola divisor sum. By the Chinese remainder theorem, for **every odd integer \(N\ge3\)**, the corresponding cubic graph modulo \(N\) has sumset size and additive energy obtained by multiplying the displayed prime-power values over \(p^k\parallel N\). The complete convolution multiplicity distribution similarly factors across the primary components.

## Assumptions and scope
All residues and ordered pairs are counted in the indicated finite commutative ring. The prime-power claims include the ramified characteristic-three branch but exclude the prime two because division by four and the invertibility of the centered change of variables fail in characteristic two. The composite-modulus consequence follows only for odd moduli, with the usual Chinese remainder identification. The extension input is the constant function, not an arbitrary weight, and no sharp unrestricted extension norm is asserted.

## Proof
**Step 1: center a pair.** Fix \(s=x+y\) and write \(u=x-y=2x-s\). Since \(q\) is odd, \(u\mapsto(x,y)=((s+u)/2,(s-u)/2)\) is bijective. The cubic identity gives
\[
4(x^3+y^3)=s^3+3su^2.
\]
Thus the target equation is \(3su^2\equiv4t-s^3\pmod q\). The \(p\)-adic order \(h\) of the coefficient, capped at \(k\), gives exactly the two cases in Finding. When \(h<k\), the condition that \(z\) be divisible by \(p^h\) is necessary; dividing gives the square-root congruence modulo \(p^\ell\). Each root there has exactly \(p^h\) lifts for \(u\) modulo \(p^k\), proving the fiber formula. If \(h=k\), the cubic sum is independent of \(u\), proving the single target with multiplicity \(q\).

**Step 2: classify square roots.** If \(w\equiv0\pmod{p^\ell}\), the congruence \(u^2\equiv0\) is equivalent to \(u\equiv0\pmod{p^{\lceil\ell/2\rceil}}\), giving \(p^{\lfloor\ell/2\rfloor}\) roots. If \(w\ne0\) modulo \(p^\ell\), any root forces \(v_p(w)=2a<\ell\). Write \(w=p^{2a}w_0\) with \(w_0\) a unit. There are roots exactly when \(w_0\) reduces to a quadratic residue modulo \(p\); Hensel's elementary simple-root lifting yields exactly \(2p^a\) roots modulo \(p^\ell\). There are \(\frac{p-1}{2}p^{\ell-2a-1}\) eligible values of \(w\) of this type. As \(t\) ranges through the admissible congruence class modulo \(p^h\), the associated \(w\) ranges bijectively over \(\mathbb Z/p^\ell\mathbb Z\). This proves every stated fiber multiplicity and the number \(T_p(\ell)\) of positive targets, by a finite geometric series.

**Step 3: sumset cardinality.** If \(p\ne3\), then \(h=v_p(s)\), capped at \(k\); exactly one \(s\) has \(h=k\), and exactly \((p-1)p^{\ell-1}\) values have \(h=k-\ell\) for \(1\le\ell\le k\). This yields the first sumset formula. If \(p=3\), then \(h=\min\{k,1+v_3(s)\}\); exactly three \(s\)'s have \(h=k\), and exactly \(2\cdot3^\ell\) have \(h=k-\ell\) for \(1\le\ell\le k-1\). This yields the second formula.

**Step 4: energy from a product-congruence count.** For each fixed \(s\), the square-sum \(\sum_t r_q(s,t)^2\) counts pairs of centered parameters \((u,u')\) satisfying
\[
3s(u^2-u'^2)\equiv0\pmod{p^k}.
\]
The linear change \((u,u')\mapsto(u-u',u+u')\) is invertible modulo odd \(q\). For \(h<k\), set \(\ell=k-h\); the congruence reduces to \(ab\equiv0\pmod{p^\ell}\) and has
\[
p^\ell+\ell(p-1)p^{\ell-1}
=p^\ell\left[1+\ell\left(1-\frac1p\right)\right]
\]
solutions modulo \(p^\ell\). Indeed, for each \(0\le j<\ell\), exactly \((p-1)p^{\ell-j-1}\) values of \(a\) have valuation \(j\), and they admit \(p^j\) values of \(b\); the case \(a=0\) contributes \(p^\ell\). Lifting the two variables to modulo \(p^k\) multiplies the count by \(p^{2h}\). Hence
\[
\sum_t r_q(s,t)^2=p^{k+h}\left[1+(k-h)\left(1-\frac1p\right)\right],
\]
with the same expression interpreted as \(p^{2k}\) when \(h=k\).

When \(p\ne3\), sum the one case \(h=k\) and the \((p-1)p^{k-h-1}\) values for each \(h<k\). The resulting geometric-valuation sum simplifies to
\[
E(C_q)=q^2\left[1+k\frac{p-1}{p}
+\frac{k(k+1)}2\left(\frac{p-1}{p}\right)^2\right].
\]
For \(p=3\), there are three cases with \(h=k\), while each \(1\le h<k\) occurs for \(2\cdot3^{k-h}\) values of \(s\). The corresponding sum is
\[
E(C_{3^k})=3^{2k}\left[3+2(k-1)+\frac23k(k-1)\right]
=3^{2k-1}(2k^2+4k+3).
\]

**Step 5: Fourier moment and composite moduli.** Expanding the fourth power of the normalized character sum and summing over \((\xi,\eta)\in R^2\) uses character orthogonality twice, leaving precisely the ordered quadruples with equal graph-point sums and the factor \(q^{-2}\). This proves the Fourier identity. The Chinese remainder theorem identifies the graph of the cubic map modulo odd \(N\) with the Cartesian product of its prime-power graph factors, and both the convolution coefficients and their squared sums multiply. This proves the claimed composite-modulus extension without introducing additional hypotheses.

## Verification
The standalone `CHECK.py` independently enumerates all ordered pair sums by integer arithmetic and compares their exact multiplicities against the valuation-and-square-root formula at **every** target. It also compares both the closed sumset and energy formulas against direct counts. The exhaustive test covers \(p=3\) through exponent \(6\), \(p=5\) through exponent \(4\), \(p=7\) through exponent \(3\), and primes \(11,13,17,19\) through exponent \(2\), for **21 parameter pairs** and **1,382,853 target entries**. Six coprime composite moduli are additionally checked against the Chinese remainder prediction by direct enumeration. Its successful output starts `CHECK_OK composite_cases=6 cases=21 targets=1382853 largest_modulus=729`. The experiment is corroborative only: Steps 1–5 prove the infinite families.

## Relationship to prior work
Iosevich, Li and Yu's 2026 finite-ring spectral-synthesis work develops Fourier-ratio bounds and exact synthesis constants for quadratic paraboloids. Its discussion of additive energy supplies the general fourth-moment identity but does not calculate the cubic graph's prime-power two-sum fibers. Hughes and Wooley's paper treats Fourier restriction for the same monomial curve over truncated integers; its common-sum factorization is closely related but its results concern high-moment bounds, not the complete modular convolution spectrum. A publicly available finite-field cubic-graph result determines the sharp \(L^2\)-to-\(L^4\) norm and extremizers in characteristics other than two and three; its constant-input collision count corresponds to the \(k=1\), \(p\ne3\) case and is **not claimed as new here**. A published finite-field fifth-power-graph result gives an analogous complete two-sum spectrum for a different graph over fields, not the prime-power cubic family. A public study of cubic-graph orthogonal exponential bases modulo prime squares concerns spectrality rather than additive convolution fibers. The new content here is the prime-power all-fiber classification, its exceptional characteristic-three behavior, exact sumsets and energies through all odd moduli.

## Limitations
The results exclude even moduli, make no assertion about arbitrary input weights or the optimal extension operator norm, and rely on the ordinary square-root lifting theorem for odd prime powers. The checked indexed literature did not identify the same modular fiber classification, but earlier algebraic-number-theory computations or general local-zeta methods may encode it in another form. Unindexed equivalent work cannot be ruled out; independent mathematical audit is not claimed. No finite test is used as a proof for unbounded exponents.

## References
1. A. Iosevich, Z. Li, K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404v1, first public 2026-09-21, Sections 4, 6 and 8.2.
2. K. Hughes, T. D. Wooley, *Discrete restriction for \((x,x^3)\) and related topics*, arXiv:1911.12262v1, first public 2019-11-27, especially Sections 1–2.
3. *Exact sharp finite-field cubic-graph \(L^2\) to \(L^4\) extension norm and extremizers*, published result, October 2026, published-finding corpus record `2026/10/4/SCOPE-exact-sharp-finite-field-cubic-graph-l-2-to-l-4-extension-norm-a--2db777d1e47b`.
4. *Complete two-sum spectrum of the finite-field fifth-power graph*, published result, October 2026, published-finding corpus record `2026/10/11/SCOPE-complete-two-sum-spectrum-of-the-finite-field-fifth-power-graph--f9410cde2e91`.
5. *All exponential spectra of the cubic graph over prime-square cyclic rings*, published result, October 2026, published-finding corpus record `2026/10/11/SCOPE-all-exponential-spectra-of-the-cubic-graph-over-prime-square-cyc--a783058468ac`.
