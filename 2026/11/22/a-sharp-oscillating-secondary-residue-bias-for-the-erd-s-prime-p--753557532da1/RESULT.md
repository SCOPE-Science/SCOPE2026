# A sharp oscillating secondary residue bias for the Erdős prime-power quotient sum

## Finding
For each positive integer \(n\), define \(w(1)=0\) and
\[
w(n)=\sum_{p^a\parallel n}\frac{n}{p^a}\quad(n>1),
\]
where the sum is over exact prime-power divisors. Set
\[
D(X)=\#\{1\le n\le X:w(n)\equiv1\pmod3\}-\#\{1\le n\le X:w(n)\equiv2\pmod3\}.
\]
There is an explicit nonzero complex constant \(K\), given below by a convergent Euler product, such that, as real \(X\to\infty\),
\[
\boxed{D(X)=\frac{2X}{\sqrt3\log X}\operatorname{Im}\!\left(K\exp\!\left(\frac{i\sqrt3}{2}\log\log X\right)\right)+O\!\left(\frac{X}{(\log X)^2}\right).}
\]
In particular the residue classes one and two have an infinitely reversing secondary bias, with sharp oscillation
\[
\limsup_{X\to\infty}\frac{\log X}{X}D(X)=\frac{2|K|}{\sqrt3},\qquad
\liminf_{X\to\infty}\frac{\log X}{X}D(X)=-\frac{2|K|}{\sqrt3}.
\]
The two residue counts have the same leading density \(7/18\), already known from a more general distribution theorem. Neither that density nor its all-modulus generalization is claimed as new.

## Assumptions and scope
The integer \(n\) ranges over all positive integers, \(X\) is real and tends to infinity, and residue congruences are modulo three. The Riemann zeta function is written \(\zeta_{\mathrm R}(s)\) to distinguish it from the primitive cube root \(\omega=\exp(2\pi i/3)\). Let \(\chi\) be the nonprincipal real Dirichlet character modulo three, and put \(z=i\sqrt3/2\). For \(\operatorname{Re}(s)>1\), define
\[
E_p(s)=\begin{cases}
\dfrac{1+(\omega-1)p^{-s}}{1-p^{-s}},&p\equiv1\pmod3,\\[3pt]
\dfrac{1-\omega^2p^{-s}+(\omega-1)p^{-2s}}{1-p^{-2s}},&p\equiv2\pmod3.
\end{cases}
\]
Define
\[
H(s)=(1-3^{-s})^z\prod_{p\ne3}E_p(s)(1-p^{-s})^z(1-\chi(p)p^{-s})^{-1/2},
\qquad
K=\frac{H(1)}{\Gamma(z)\sqrt{L(1,\chi)}}.
\]
Powers take their branches by continuation from real \(s>1\), using the usual absolutely convergent logarithms near \(s=1\); the square root of \(L(1,\chi)=\pi/(3\sqrt3)>0\) is positive. This product is absolutely convergent and nonzero at \(s=1\).

## Proof
**1. Fourier encoding.** Write \(u\) for an integer coprime to three. For each exact prime power \(q=p^a\parallel u\), its inverse modulo three equals \(+1\) if \(q\equiv1\) and \(-1\) if \(q\equiv2\). Let \(c_+(u)\) and \(c_-(u)\) count these respective prime-power factors. Consequently,
\[
w(u)\equiv u(c_+(u)-c_-(u))\pmod3.
\]
Set \(f(u)=\chi(u)\omega^{c_+(u)-c_-(u)}\) when \(3\nmid u\), and \(f(u)=0\) otherwise. This is multiplicative, not necessarily completely multiplicative. The cubic root identity gives the exact indicator identity
\[
\mathbf1_{w(u)\equiv1\ (3)}-\mathbf1_{w(u)\equiv2\ (3)}
=\frac{2}{\sqrt3}\operatorname{Im}f(u).
\]
If \(n=3^a u\) with \(a\ge1\) and \(3\nmid u\), then the defining arithmetic function satisfies \(w(n)=u+3^aw(u)\), so \(w(n)\equiv u\pmod3\). For each \(a\), the difference between the counts of \(u\equiv1\) and \(u\equiv2\) through \(X/3^a\) has absolute value at most one. There are at most \(\lfloor\log_3 X\rfloor\) possible positive \(a\), whence
\[
D(X)=\frac2{\sqrt3}\operatorname{Im}\sum_{n\le X}f(n)+O(\log X).
\]

**2. Local Euler factors and analytic factorization.** For any prime \(p\equiv1\pmod3\), one has \(f(p^a)=\omega\) at every positive exponent. For \(p\equiv2\pmod3\), the values alternate between \(-\omega^2\) at odd exponents and \(\omega\) at even exponents. This gives the two displayed rational factors \(E_p(s)\), while \(E_3(s)=1\). Using \(\omega+\omega^2=-1\), the prime coefficients satisfy
\[
f(p)=z-\frac12\chi(p)\quad(p\ne3).
\]
Therefore, comparing each Euler factor's first power of \(p^{-s}\),
\[
\sum_{n\ge1}\frac{f(n)}{n^s}
=\zeta_{\mathrm R}(s)^zL(s,\chi)^{-1/2}H(s).
\]
The first-order terms in the logarithm of every local factor defining \(H\) cancel. Uniformly for \(\operatorname{Re}(s)>1/2\) in compact neighborhoods of one, the remaining factors differ from one by \(O(p^{-2\operatorname{Re}(s)})\). Thus \(H\) has a normally convergent Euler product there and is analytic near one.

The value \(H(1)\) is nonzero: \(E_p(1)=1+O(1/(p-1))\) for \(p\ge5\), with \(|E_p(1)-1|\le1/(p-1)<1\); the remaining prime \(p=2\) has
\[
E_2(1)=\frac{1-\omega^2/2+(\omega-1)/4}{3/4}\ne0.
\]
All other local scalar factors are nonzero, and their convergent logarithmic corrections have finite sum. Since the gamma function has no zeros, \(\Gamma(z)\ne0\); also \(L(1,\chi)>0\). Hence \(K\ne0\).

**3. Asymptotic.** The fixed-modulus Dirichlet \(L\)-function and zeta function have the customary zero-free neighborhood of \(s=1\). The Selberg–Delange theorem for an Euler product \(\zeta_{\mathrm R}(s)^z\) times a holomorphic nonzero factor applies to the bounded multiplicative coefficients \(f\). Its leading term, with one-term error, is
\[
\sum_{n\le X}f(n)=\frac{H(1)L(1,\chi)^{-1/2}}{\Gamma(z)}X(\log X)^{z-1}
+O\!\left(X(\log X)^{\operatorname{Re}(z)-2}\right).
\]
Because \(\operatorname{Re}(z)=0\), this error is \(O(X/(\log X)^2)\). Insert the Fourier identity from step one and absorb the \(O(\log X)\) term. Since \((\log X)^z=\exp(i\sqrt3\log\log X/2)\), this proves the stated oscillating formula.

**4. Sharpness and sign changes.** The phase \((\sqrt3/2)\log\log X+\arg K\) is continuous, strictly increasing, and unbounded. For arbitrarily large \(X\) it is congruent to \(\pi/2\) or \(-\pi/2\) modulo \(2\pi\). Along these sequences, the normalized error tends to zero, attaining the two asserted limits. The elementary bound \(|\operatorname{Im}(Ke^{it})|\le|K|\) gives the corresponding global upper and lower bounds. The density \(7/18\) for each nonzero class is a pre-existing result, not needed to derive the discrepancy itself.

## Verification
Run `python3 check_bias.py`. It verifies the exact Fourier identity by independent integer factorization at the first 20,000 integers, the exceptional three-divisible reduction, 64 prime-power local identities, and 30 Euler-series coefficients. These finite checks do not prove the Selberg–Delange asymptotic, the Euler-product nonvanishing, or the infinite limsup/liminf, which are proved mathematically above.

## Relationship to prior work
John M. Campbell's November 2026 work studies the value set of the same prime-power quotient function and supplies the literature-led motivation. A preceding result on this exact function already gives the natural residue density for every fixed modulus and a stronger conditional distribution; it expressly makes no claim of an effective convergence error. Those density statements do not imply the present sharp secondary term, rotating phase, or infinitely many sign changes. The Selberg–Delange method is established technology; the claim here is the arithmetic identification of the nonzero complex exponent and Euler factor, and the resulting secondary law for this particular arithmetic function. A generalized result on complex-valued multiplicative functions could subsume the analytic method, but no inspected source gives this specific residue-bias statement.

## Limitations
The result concerns fixed modulus three only. The implied constant is not numerically certified, and no uniformity in growing moduli or effective explicit threshold for the first sign reversal is asserted. The density law is previously covered, and there is no independent expert validation. Limited inspection of older unpublished or unindexed sources leaves a residual priority risk. The finite checker tests arithmetic identities, not an infinite asymptotic.

## References
- John M. Campbell, *On a problem due to Erdős concerning \(w_1(n)\)*, arXiv:2611.07617v1 (first publicly posted November 5, 2026), https://arxiv.org/abs/2611.07617.
- D. Koukoulopoulos and K. Soundararajan, *The structure of multiplicative functions with small partial sums*, arXiv:1909.13105, https://arxiv.org/abs/1909.13105.
- A. Granville and D. Koukoulopoulos, *Beyond the LSD method for the partial sums of multiplicative functions*, arXiv:1710.01389, https://arxiv.org/abs/1710.01389.
- Selberg–Delange's classical asymptotic theorem for multiplicative functions; the use here is for a fixed nonintegral complex exponent and fixed conductor-three Dirichlet character.
