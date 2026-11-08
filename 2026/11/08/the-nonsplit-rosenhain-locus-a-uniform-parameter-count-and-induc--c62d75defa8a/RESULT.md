# The nonsplit Rosenhain locus: a uniform parameter count and induced genus-two zeta functions

## Finding
Let \(q\ge5\) be an odd prime power, \(k=\mathbb F_q\), and let \(\lambda,\mu\in k\), \(\lambda\ne0,1\). Put
\[
\nu=\frac{\lambda(1-\mu)}{1-\lambda},\qquad
\Delta=\lambda(\lambda-\mu).
\]
Call the ordered marked parameter pair \((\lambda,\mu)\) *admissible* when the five elements \(0,1,\lambda,\mu,\nu\) are pairwise distinct. For any admissible pair and any \(\theta\in k^\times\), let \(C_{\lambda,\mu,\theta}\) be the smooth projective genus-two curve with affine equation
\[
y^2=\theta x(x-1)(x-\lambda)(x-\mu)(x-\nu).
\]
Among the \((q-3)^2\) admissible ordered marked pairs, exactly
\[
N_{\mathrm{ns}}(q)=\frac{(q-1)(q-3)}2
\]
have \(\Delta\) a nonsquare in \(k\); the remaining \((q-3)(q-5)/2\) have square \(\Delta\). For **every** nonsquare pair, every \(\theta\ne0\), and every \(r\ge0\),
\[
\#C_{\lambda,\mu,\theta}(\mathbb F_{q^{2r+1}})=q^{2r+1}+1.
\]
Furthermore, write \(K=\mathbb F_{q^2}\), choose \(d\in K\) with \(d^2=\Delta\), and define an elliptic curve over \(K\) by
\[
E:\quad v^2=\frac{\theta(1-\mu)}{1-\lambda}\,u(u-1)
\left(u-\frac{(1-\lambda)(\mu-2\lambda+2d)}{\mu-1}\right).
\]
Set \(a=q^2+1-\#E(K)\). Then the numerator of the Hasse--Weil zeta function of \(C\) over \(k\) is precisely
\[
L(C/k,T)=1-aT^2+q^2T^4.
\]
Equivalently, \(\operatorname{Jac}(C)\) is \(k\)-isogenous to \(\operatorname{Res}_{K/k}E\); for each \(r\ge1\),
\[
\#C(\mathbb F_{q^{2r}})=2\#E(\mathbb F_{q^{2r}})-(q^{2r}+1).
\]
Here \(E\) is base-changed from its given model over \(K\) to \(\mathbb F_{q^{2r}}\), and the count is of *marked parameter pairs*, not isomorphism classes of genus-two curves. The odd-extension equality is a sharp obstruction to using this nonsplit locus to obtain curves with more than \(q+1\) points over \(k\).

## Assumptions and scope
Characteristic is odd, including characteristic three when \(q\ge5\). The square/nonsquare condition is on the nonzero element \(\Delta\). The equation has five distinct finite roots, so its projective normalization has a unique rational point above infinity and is a smooth curve of genus two. The elliptic curve \(E\) above is nonsingular because it is the quotient by an involution of a genus-two curve; equivalently the three branch points of its displayed cubic are distinct. All claims are uniform in the nonzero twist parameter \(\theta\). Counting parameter pairs does not quotient by projective coordinate changes, quadratic twists, or automorphisms of the curves.

## Proof
**1. Exact marked-parameter count.** The substitution
\[
s=\frac{1-\lambda}{\lambda},\qquad t=1-\frac\mu\lambda
\]
is a bijection from \(\lambda\in k\setminus\{0,1\}\), \(\mu\in k\) to \(s\in k\setminus\{0,-1\}\), \(t\in k\). In these coordinates,
\[
\lambda=\frac1{s+1},\qquad \mu=\frac{1-t}{s+1},\qquad
\nu=\frac{s+t}{s(s+1)},\qquad \Delta=\lambda^2t.
\]
Directly comparing the five roots shows admissibility is equivalent to
\[
s\notin\{0,-1\},\qquad t\notin\{0,1,-s,s^2\}.
\]
For the \(q-3\) choices \(s\ne1\), four distinct values of \(t\) are forbidden; for \(s=1\), the forbidden set has three values. Thus there are \((q-3)(q-4)+(q-3)=(q-3)^2\) admissible pairs. Since \(\Delta=\lambda^2t\), it is a nonsquare exactly when \(t\) is a nonsquare. Of the four potentially forbidden values, \(0\), \(1\), and \(s^2\) never are nonsquares, so among the \((q-2)(q-1)/2\) pairs with \(s\notin\{0,-1\}\) and \(t\) nonsquare, precisely the \((q-1)/2\) choices with \(-s=t\) are inadmissible. Subtracting yields \(N_{\mathrm{ns}}=(q-1)(q-3)/2\), and subtraction from the total gives the square stratum. This argument uses only the quadratic-character partition of \(k^\times\), so it holds for all odd prime powers.

**2. Galois conjugation of the genus-one involutions.** In the notation of Iezzi--Qiu Kawakita--Timpanella, Theorem 2 and its proof, the involutions on \(C_K\) are
\[
\sigma:(x,y)\longmapsto\left(\frac{\lambda(x-\mu)}{x-\lambda},\frac{\Delta d\,y}{(x-\lambda)^3}\right),\qquad
\iota:(x,y)\longmapsto(x,-y),\qquad\tau=\iota\sigma.
\]
The automorphism identities in the cited source are algebraic and remain valid after extending to \(K\); \(\sigma\) and \(\tau\) are distinct commuting involutions with elliptic quotients \(E_\sigma=C_K/\langle\sigma\rangle\) and \(E_\tau=C_K/\langle\tau\rangle\). The displayed equation for \(E\) is the source's explicit model for one of these quotients. Since \(d^q=-d\) when \(\Delta\) is nonsquare, \(q\)-Frobenius exchanges \(\sigma\) and \(\tau\). Therefore it exchanges the two elliptic quotients and \(E_\tau\cong E_\sigma^{(q)}\) over \(K\).

**3. Trace-zero and induced zeta polynomial.** For any odd auxiliary prime \(\ell\ne\mathrm{char}(k)\), the hyperelliptic involution acts as \(-I\) on \(H^1_{\mathrm{\acute et}}(C_{\bar k},\mathbb Q_\ell)\). Let \(F\) denote geometric Frobenius on this four-dimensional space. Galois conjugation yields \(F\sigma F^{-1}=\iota\sigma=-\sigma\) on cohomology (the corresponding inverse-conjugation convention gives the same identity). Hence \(\sigma F^{2r+1}\sigma^{-1}=-F^{2r+1}\); taking traces in characteristic zero gives \(\operatorname{Tr}(F^{2r+1})=0\) for all \(r\ge0\). The Lefschetz point-count formula proves the odd-extension equality.

Over \(K\), the Kani--Rosen decomposition established in the cited source gives the isogeny \(\operatorname{Jac}(C)_K\sim E_\sigma\times E_\tau\). The two elliptic curves are Frobenius conjugate, so both have the same \(q^2\)-Frobenius trace \(a\). Consequently \(\operatorname{Tr}(F^2)=2a\). Since all odd-power traces vanish, the \(k\)-Frobenius characteristic polynomial is even, of shape \(X^4-aX^2+q^2\); the coefficient \(-a\) follows from \(\operatorname{Tr}(F^2)=2a\), and the constant \(q^2\) is the standard genus-two determinant. Reversing coefficients gives \(L(C/k,T)=1-aT^2+q^2T^4\). The Weil restriction of \(E/K\) has the same characteristic polynomial; Tate's isogeny theorem for abelian varieties over finite fields yields the claimed \(k\)-isogeny. The equality of point counts over even extensions follows from the same Frobenius eigenvalues.

## Verification
The accompanying standalone `verify.py` counts every admissible \((\lambda,\mu)\) over eleven prime fields and independently checks fourteen genus-two/elliptic point-count comparisons over quadratic fields with two twist parameters. It uses exact modular arithmetic and explicitly constructs \(\mathbb F_{p^2}=\mathbb F_p[d]/(d^2-\Delta)\). On execution it prints `VERIFY_ROSENHAIN_NONSPLIT_OK 11_prime_parameter_censuses 14_quadratic_field_curve_checks 24_F9_odd_trace_checks`. The argument above, rather than these finite tests, proves the theorem for every odd prime power and all extensions.

## Relationship to prior work
Iezzi, Qiu Kawakita, and Timpanella (arXiv:2306.01928v1, Section 3, Theorem 2) give this marked Rosenhain equation, the explicit involutions, and the elliptic-quotient equations when \(\Delta\) is square in the base field. Their proof gives the geometric ingredients after quadratic extension but does not state the nonsquare arithmetic stratum or its exact marked-parameter population. The general fact that a geometrically split abelian surface can be a Weil restriction is known, and is not claimed as new. This result's specific contribution is a complete arithmetic dichotomy for the source's **marked parameter space**, including the nonsplit-stratum count, forced odd-extension point counts, and explicit induced zeta calculation. General Weil restriction methods appear, for example, in Freeman--Satoh (2011); the genus-two Frobenius-polynomial context is discussed in Howe (2004). No uniqueness of curves up to isomorphism or originality of the underlying restriction-of-scalars mechanism is claimed.

## Limitations
The parameter count is for ordered marks; many parameters may yield isomorphic curves. A full census of distinct isomorphism classes, their automorphism groups, and their possible \(q^2\)-traces is not established. The theorem does not treat characteristic two, singular parameters, or the subcase \(\Delta\) square beyond counting its parameters. It does not claim that the elliptic quotient itself descends to \(k\). An equivalent specialization in earlier literature cannot be ruled out without a broader historical search.

## References
1. A. Iezzi, M. Qiu Kawakita, M. Timpanella, *New sextics of genus 6 and 10 attaining the Serre bound*, arXiv:2306.01928v1 (first posted 2 June 2023), Section 3, Theorem 2 and proof; https://arxiv.org/pdf/2306.01928.
2. D. Freeman and T. Satoh, *Constructing pairing-friendly hyperelliptic curves using Weil restriction*, *Journal of Number Theory* **131** (2011), 959--983, Section 3, Proposition 3.2; https://theory.stanford.edu/~dfreeman/papers/weil.pdf.
3. E. W. Howe, *On the non-existence of certain curves of genus two*, Compositio Mathematica **140** (2004), 581--592 (background on genus-two Frobenius polynomials); https://arxiv.org/abs/math/0201311.
