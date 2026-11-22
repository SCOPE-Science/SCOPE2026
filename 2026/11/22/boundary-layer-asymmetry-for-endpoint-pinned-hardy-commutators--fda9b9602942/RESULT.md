# Boundary-layer asymmetry for endpoint-pinned Hardy commutators

## Finding
The classical Hardy average on real \(L^2(0,1)\) is
\[
(Hf)(x)=\frac1x\int_0^x f(t)\,dt.
\]
For any real Lipschitz multiplier \(b\), let \(C_b=[M_b,H]=M_bH-HM_b\) and put \(\mathcal E(b)=\|C_b\|_{\mathcal S_2}^2\). Suppose \(b(0)=b(1)=0\) and \(\operatorname{Lip}(b)\le1\). The familiar tent \(b_0(x)=\min\{x,1-x\}\), although pointwise maximal among nonnegative admissible symbols, is **not** an optimizer of \(\mathcal E\) even within a simple three-ramp class.

For \(0\le a\le1/2\), define
\[
b_a(x)=\begin{cases}
-x,&0\le x\le a,\\
x-2a,&a\le x\le a+1/2,\\
1-x,&a+1/2\le x\le1.
\end{cases}
\]
Every \(b_a\) has pinned endpoints and unit Lipschitz constant. Its energy is exactly
\[
\boxed{E(a)=\mathcal E(b_a)=\frac5{12}-a^2+\frac a2+2a^2\log a+
\left(-2a^2+2a+\frac12\right)\log\left(a+\frac12\right)}
\]
with the continuous convention \(a^2\log a=0\) at \(a=0\). There is a **unique global maximizer within this entire three-ramp family**, at \(a=a_*\), the unique root in \((1/100,1/64)\) of
\[
\boxed{E'(a)=\frac72-2a+4a\log a+(2-4a)\log\left(a+\frac12\right)-\frac1{a+1/2}=0.}
\]
Its numerical values are \(a_*\approx0.012728930893744\) and \(E(a_*)\approx0.0706614134611041\), whereas
\[
E(0)=E(1/2)=\frac5{12}-\frac12\log 2\approx0.0700930763866940.
\]
In particular the explicit rational choice \(a=1/64\) already gives \(E(1/64)\approx0.0706407509531613>E(0)\). This is a strict counterexample to a natural tent-extremality heuristic for the Hilbert–Schmidt commutator energy.

## Assumptions and scope
The domain is the real Hilbert space \(L^2(0,1)\) with Lebesgue measure. Symbols are real functions on the closed interval, endpoint-pinned and at most one-Lipschitz. \(M_b\) denotes multiplication by \(b\); the Hilbert–Schmidt norm uses the usual sum of squared singular values and is not an ordinary operator norm. The explicit maximization is *only* within the above one-parameter, three-ramp family; the full extremal problem for all endpoint-pinned Lipschitz symbols is not resolved. No uniqueness beyond the named family is asserted. Replacing \(b\) by \(-b\) leaves its energy invariant.

## Proof
**1. Kernel identity.** Direct subtraction gives
\[
(C_bf)(x)=\int_0^1\mathbf1_{\{0<t<x<1\}}\frac{b(x)-b(t)}x f(t)\,dt.
\]
For any unit-Lipschitz \(b\), \(|b(x)-b(t)|\le x-t\), hence the displayed kernel is square integrable and
\[
\mathcal E(b)=\int_0^1\frac1{x^2}\int_0^x(b(x)-b(t))^2\,dt\,dx.
\]
This proves that the calculation is for the actual Hilbert–Schmidt norm, with no missing normalization factor.

**2. Exact three-ramp integration.** Write \(c=a+1/2\). Substituting the three affine formulas into the inner integral and dividing by \(x^2\) gives, respectively, on \((0,a)\), \((a,c)\), and \((c,1)\),
\[
\begin{aligned}
J_1(x)&=x/3,\\
J_2(x)&=x/3-2a^2/x+2a^3/x^2,\\
J_3(x)&=x/3-(2a+1/2)/x+(a^2+3a/2+1/4)/x^2.
\end{aligned}
\]
Each expression follows by elementary polynomial integration over the earlier ramps and the current ramp. Integrating \(J_1\) over \((0,a)\), \(J_2\) over \((a,c)\), and \(J_3\) over \((c,1)\) and collecting terms gives the displayed exact formula for \(E(a)\). The endpoint cases follow by continuity. In particular, both endpoint configurations are the tent up to sign.

**3. Number and location of critical points.** Differentiating yields the formula for \(E'\). A third differentiation simplifies exactly to
\[
E'''(a)=-\frac{4(4a^2+4a-1)}{a(2a+1)^3}.
\]
Thus \(E''\) increases on \((0,(\sqrt2-1)/2)\) and decreases thereafter. Also \(E''(a)\to-\infty\) as \(a\downarrow0\), whereas \(E''(1/2)=3-4\log2>0\). It follows that \(E''\) changes sign exactly once, from negative to positive. Consequently \(E'\) first strictly decreases and then strictly increases.

The endpoint limits satisfy \(E'(0+)=E'(1/2-)=3/2-2\log2>0\). Exact rational logarithm enclosures (also implemented in the checker) give \(E'(1/100)>0\) and \(E'(1/64)<0\). Hence \(E'\) has exactly two roots on \((0,1/2)\): a unique local maximum \(a_*\in(1/100,1/64)\), followed by a unique local minimum. Finally \(E(0)=E(1/2)\), and \(E\) increases immediately to the right of zero, proving that \(a_*\) is the unique global maximum on \([0,1/2]\). No numerical optimization or sampled sign test is used for the continuum assertion. The bound \(\log2<3/4\) proves the required strict endpoint inequalities.

**4. Explicit failure of tent extremality.** The rational-logarithm certificate proves
\[
E(1/64)-E(0)>0.00054767456646.
\]
Since both symbols belong to the full endpoint-pinned unit-Lipschitz class, its tent is not a global maximizer. This does *not* identify a global optimizer among arbitrary symbols.

## Verification
Run `python3 verify.py` using Python 3's standard library. It independently evaluates exact rational intervals enclosing all required logarithms by an atanh series, certifies the signs of \(E'\), isolates the unique maximizing root, verifies the strict rational witness, and compares the analytic energy against a direct quadrature of the original double kernel. Its terminal marker is `ALL_ENDPOINT_PINNED_HARDY_CERTIFICATES_PASS`. Rational intervals—not the quadrature—prove the critical strict inequalities. The analytic sign structure proves the uncountably many remaining positions.

## Relationship to prior work
Fu and Lu (2009) and Yu and Lu (2013) study Hardy-type commutators, principally boundedness and function-space estimates. The openly readable full 2013 treatment establishes Herz and central Morrey boundedness; it does not state this endpoint-pinned Hilbert–Schmidt energy formula. The 2009 publisher page supplies a first-publication date and abstract, but its full text was not available for line-by-line exclusion.

The published Hardy power-commutator theorem in the published-finding corpus record `33677ede3aa1` determines the singular-value asymptotic and the squared Hilbert–Schmidt norm for symbols \(x^\alpha\); these unpinned monomials do not cover the sign-changing three-ramp class or the unique endpoint-pinned maximizer claimed here. The real-variable Cesàro commutator result `7e2b67f7c66b` concerns a different integral kernel with a factor \(1/(1-t)\), and thus does not imply the formula. The separate Cesàro spectral-tail optimization `9856fd98253d` concerns monotone endpoint-gap-one symbols and an asymptotic singular-value coefficient, not the present pinned Hilbert–Schmidt quantity. These comparisons establish nonimplication for the inspected statements, not absolute bibliographic uniqueness.

## Limitations
The one-parameter extremal classification does not solve the unrestricted Lipschitz-symbol optimization. The full 2009 Fu–Lu text and potentially older unindexed commutator papers remain historical-priority risks. The theorem does not concern general Schatten norms, complex symbols, weighted \(L^2\) spaces, or operator-norm sharp constants. Independent mathematical validation and historical-priority certification have not been performed.

## References
- Z. Fu and S. Lu, *Commutators of generalized Hardy operators*, Mathematische Nachrichten **282** (2009), 832–845, doi:10.1002/mana.200610775 (first publisher posting 21 May 2009).
- X. Yu and S. Lu, *Boundedness for a Class of Generalized Commutators of Fractional Hardy Operators with a Rough Kernel*, Abstract and Applied Analysis (2013), article 431692, doi:10.1155/2013/431692 (public full text inspected).
- *A universal singular-value Weyl law for Hardy power commutators*, published-finding corpus (published 18 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-universal-singular-value-weyl-law-for-hardy-power-commutators--33677ede3aa1 .
- *Exact Jacobi singular system of a real-variable Cesàro commutator*, published-finding corpus (published 8 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-jacobi-singular-system-of-a-real-variable-ces-ro-commutato--7e2b67f7c66b .
- *Sharp spectral-tail extremizers for monotone multipliers of the real-variable Cesàro operator*, published-finding corpus (published 8 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-spectral-tail-extremizers-for-monotone-multipliers-of-the--9856fd98253d .
