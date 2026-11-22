# Sharp derivative-only certificates for the two fifth-root endpoint quadratures

## Finding

**Theorem (sharp derivative-only a posteriori integration certificate).** Fix any real \(a<b\), put \(h=b-a\), and let \(f\in C^6[a,b]\) be real with \(f^{(6)}(x)\ge0\) throughout. Define the two endpoint-jet quadratures

\[
Q_\pm[f]=\frac h2(f(a)+f(b))
-\frac{h^2c_{2,\pm}}2(f'(b)-f'(a))
+\frac{h^3c_{3,\pm}}6(f''(a)+f''(b))
-\frac{h^4c_{4,\pm}}{24}(f'''(b)-f'''(a)),
\]

where

\[
c_{2,\pm}=\pm\frac{\sqrt5}{10},\quad
c_{3,\pm}=\frac{-5\pm3\sqrt5}{20},\quad
c_{4,\pm}=\frac{-2\pm\sqrt5}{10}.
\]

These are the real quadratures produced by the two conjugate classes of nontrivial fifth roots in the fourth-term complex-shift construction of Wang [1, equation (3.22) and Table 3.1]. The coefficients themselves are not claimed as new.

Write \(I[f]=\int_a^b f(x)\,dx\) and \(\Delta[f]=Q_-[f]-Q_+[f]\). Then \(\Delta[f]\ge0\), and

\[
\boxed{
Q_+[f]+\alpha\Delta[f]\le I[f]\le
Q_+[f]+\beta\Delta[f],
\qquad
\alpha=\frac12-\frac{13}{12\sqrt5},\quad
\beta=\frac12-\frac1{\sqrt5}.
}
\]

Both \(\alpha=0.015518604875\ldots\) and \(\beta=0.052786404500\ldots\) are **optimal**, even when restricting to smooth functions with nonnegative sixth derivative. Thus the certified interval width is precisely \(\Delta[f]/(12\sqrt5)\), only approximately \(3.7268\%\) of the two-rule gap.

Among all fixed affine blends \(T_\theta=Q_++\theta\Delta\), the unique estimator minimizing the supremum of \(\lvert I[f]-T_\theta[f]\rvert/\Delta[f]\) over \(\Delta[f]>0\) in this class is

\[
\boxed{T_*=Q_++\left(\frac12-\frac{25}{24\sqrt5}\right)\Delta,\qquad
\lvert I[f]-T_*[f]\rvert\le\frac{\Delta[f]}{24\sqrt5}.}
\]

The constant \(1/(24\sqrt5)\) is sharp. The same conclusions hold with inequalities reversed when \(f^{(6)}\le0\), by applying the theorem to \(-f\). Summing across any finite partition of \([a,b]\) preserves the same constants for a globally fixed sign of \(f^{(6)}\).

## Assumptions and scope

The interval is real and nondegenerate. The function is real-valued and has a continuous sixth derivative with a known global sign. All endpoint values and derivatives through order three are evaluated exactly. The rules are local linear functionals using the same eight endpoint data values (four derivatives or values at each endpoint); no interior function evaluation is required. If \(f^{(6)}\equiv0\), both quadratures and the integral coincide and \(\Delta=0\); otherwise \(\Delta>0\).

The result is a shape-constrained **integration certificate**, not a bound for arbitrary smooth integrands or a floating-point stability theorem. The coefficients in \(Q_\pm\) are taken from [1]; their new use is the sharp double-sided enclosure and minimax certificate.

## Proof

**1. Normalization and exactness.** Set \(g(t)=f(a+ht)\), \(0\le t\le1\). By scaling, \(I[f]-Q_\pm[f]=h(\int_0^1g-Q_\pm[g])\) with the formulas above at \(h=1\). Each rule is invariant under reflection \(t\mapsto1-t\), and direct substitution shows that it integrates monomials of degrees zero through four exactly (the fifth-root coefficient identities). Reflection then gives exactness for degree five, since the remaining centered odd monomial has zero integral and zero rule value. Alternatively, direct substitution verifies all six moments.

**2. Exact sixth-order error kernels.** The Peano kernel identity, valid for every \(g\in C^6[0,1]\) because both rules annihilate degree-five polynomials, gives

\[
\int_0^1g(t)\,dt-Q_\pm[g]
=\int_0^1K_\pm(s)g^{(6)}(s)\,ds,
\quad
K_\pm(s)=\frac1{5!}\left(\int_0^1(x-s)_+^5\,dx-Q_\pm[(x-s)_+^5]\right).
\]

For \(s\in(0,1)\), the left endpoint jets of the truncated power vanish. The right endpoint value and its first three derivatives are \((1-s)^5\), \(5(1-s)^4\), \(20(1-s)^3\) and \(60(1-s)^2\), respectively. Substitution, expansion, and factorization produce, with \(z=s(1-s)\),

\[
\boxed{
K_+(s)=\frac{z^2}{720}\left(\frac{3\sqrt5}{2}-3-z\right),
\qquad
K_-(s)=-\frac{z^2}{720}\left(\frac{3\sqrt5}{2}+3+z\right).
}
\]

These identities hold at the endpoints by continuity. Since \(0\le z\le1/4\) and \(3\sqrt5/2-3>1/4\), the first kernel is nonnegative and the second is nonpositive, both strictly signed in the open interval. Their difference is

\[
K_+(s)-K_-(s)=\frac{\sqrt5}{240}z^2>0\quad(0<s<1).
\]

Consequently \(\Delta[f]=h^7\int_0^1(K_+-K_-)(s)f^{(6)}(a+hs)\,ds\ge0\). If the sixth derivative is nonzero somewhere, continuity makes the integral strictly positive.

**3. Optimal enclosure coefficients.** When \(\Delta>0\), the normalized relative error is a weighted mean of the kernel ratio

\[
\frac{I[f]-Q_+[f]}{\Delta[f]}
=\frac{\int_0^1 r(s)(K_+-K_-)(s)f^{(6)}(a+hs)\,ds}
{\int_0^1(K_+-K_-)(s)f^{(6)}(a+hs)\,ds},
\quad r(s)=\frac{K_+(s)}{K_+(s)-K_-(s)}
=\frac12-\frac1{\sqrt5}-\frac{s(1-s)}{3\sqrt5}.
\]

Because \(s(1-s)\in[0,1/4]\), precisely \(\alpha\le r(s)\le\beta\). Integrating with nonnegative weight proves the enclosure. Its constants are sharp: choose smooth nonnegative sixth derivatives supported in shrinking neighborhoods of \(s=1/2\) to approach \(\alpha\), and near an interior point tending to an endpoint to approach \(\beta\). Six integrations, with arbitrary zero integration constants, give \(C^\infty\) test functions with precisely those sixth derivatives. Thus neither constant can be strengthened. The strict inequalities hold whenever \(f^{(6)}\not\equiv0\), but sharp values occur as limits.

The sharp range of the error ratio is exactly \([\alpha,\beta]\), so the worst normalized error of \(T_\theta\) is \(\max\{|\theta-\alpha|,|\theta-\beta|\}\). Its unique minimizer is \(\theta=(\alpha+\beta)/2=1/2-25/(24\sqrt5)\), with optimal value \((\beta-\alpha)/2=1/(24\sqrt5)\). A finite partition preserves the inequalities cellwise; the global gap is the sum of nonnegative local gaps. Sharpness also holds for the one-cell partition.

## Verification

Run `python check_kernel.py` with SymPy. It independently reconstructs the Peano kernel from endpoint truncated-power jets, checks exactness on degree-zero through degree-five monomials, verifies the two exact nonnegative kernel-margin factorizations, verifies the minimax midpoint, and checks 57 independent nonnegative-sixth-derivative Bernstein-polynomial cases using exact algebraic arithmetic. It returns `VERIFY_OK`. The finite test cases are **not** the proof of the all-function inequality; that proof is the kernel factorization and nonnegative-weight argument above.

As an illustrative check (not needed for the proof), on \([0,1]\) for \(f(x)=e^x\), \(Q_+=1.7182708987785464\ldots\), \(Q_-=1.7187921411165625\ldots\), and the certified refined enclosure is approximately \([1.7182789877324342,\,1.7182984132874435]\), containing the exact integral \(e-1=1.7182818284590452\ldots\).

## Relationship to prior work

Wang [1, Section 3.2, equation (3.22) and Table 3.1] supplies exactly the two real fifth-root endpoint-jet formulas, but stops at polynomial accuracy and does not assert their sixth-order Peano kernels, opposite error signs, optimal double-sided relative-gap enclosure, or minimax blending constant. No new quadrature coefficients or fifth-root construction are claimed.

Wąsowicz [2] and Kania–Wąsowicz [3] study shape-certified integration for higher-order-convex functions, particularly three-point Gauss versus four-point Lobatto rules. Their quadratures use function values at interior nodes rather than endpoint derivatives, so their sharp constants do not imply the present endpoint-jet certificate. Bui-Thanh, Villatoro and Krishnanunni [4] study the **interpolatory** two-endpoint Hermite quadrature (degree seven from four jets at each endpoint); the present fifth-root rules are noninterpolatory degree-five rules. The Peano kernel theorem itself is standard [5]; applying it to the fifth-root rules and obtaining their sharp signed kernel-ratio range is the additional assertion here.

## Limitations

The sign of the sixth derivative must be known or separately proved; an unknown or sign-changing sixth derivative is outside the guarantee. Endpoint derivatives through order three may be expensive or inaccurate. The inequalities concern exact arithmetic; cancellation, approximate derivatives, and finite-precision error are not addressed. The closed interval bounds are the closure of attainable ratios; for a nonzero continuous sixth derivative, the normalized ratio lies strictly between their endpoints. The theorem does not establish a universal superiority over Gauss–Lobatto quadrature or an optimality result among all quadratures using the same endpoint data. No independent mathematical audit or exhaustive historical-priority verification has been performed.

## References

1. Junping Wang, *Beyond Taylor: Divergence-Based Functional Expansions and Their Application to Numerical Integration*, arXiv:2602.01467v1, first posted 2026-02-01. https://arxiv.org/abs/2602.01467
2. Szymon Wąsowicz, *Adaptive integration of 5-convex and 5-concave functions*, arXiv:2601.16796v1, first posted 2026-01-23. https://arxiv.org/abs/2601.16796
3. Tomasz Kania and Szymon Wąsowicz, *Refined Gauss–Lobatto bounds for odd-order convexity*, arXiv:2609.34918, first posted 2026-09-28. https://arxiv.org/abs/2609.34918
4. Tan Bui-Thanh, Giancarlo Villatoro and C. G. Krishnanunni, *From an Elementary Proof of Error Representation for Hermite Quadrature to a Rediscovery of Legendre Polynomials and Rodrigues Formula*, arXiv:2602.18634, first posted 2026-02-20. https://arxiv.org/abs/2602.18634
5. Standard Peano kernel theorem for quadrature linear functionals; see, e.g., P. J. Davis and P. Rabinowitz, *Methods of Numerical Integration*, 2nd ed., Academic Press, 1984.
