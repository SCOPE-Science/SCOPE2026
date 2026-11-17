# A universal alternating-grid BDF4 stability law and an order-five obstruction

## Finding

For the standard variable-step backward differentiation formula of order four (BDF4), applied to the test equation \(y'=0\), every **fixed** two-periodic positive step-length sequence \(h,rh,h,rh,\ldots\), with \(h>0\) and \(r>0\), is strongly zero-stable: every parasitic Floquet multiplier has modulus strictly below one. There is no upper restriction on the fixed step ratio \(r\), although the strict damping margin is not uniform as \(r\to0\) or \(r\to\infty\).

More precisely, put \(q=r+r^{-1}\) and
\[
D=24q^2+154q+221,\quad A=24q^2+34q-43,\quad B=6q+19,\quad C=2q+5.
\]
The two-step difference-state monodromy has characteristic polynomial
\[
\boxed{\chi_4(\lambda)=\lambda^3+\frac AD\lambda^2+\frac BD\lambda-\frac CD.}
\]
All three roots lie strictly inside the unit disk for every finite \(r>0\). Its sharp, unattained all-ratio spectral-radius supremum is \(1\).

This property fails at the next BDF order. For standard variable-step BDF5 and ratio \(r=10\), the four-dimensional two-step parasitic monodromy has characteristic polynomial
\[
\chi_5(\lambda)=\frac{44681585\lambda^4+58282373\lambda^3+3875537\lambda^2-698295\lambda+152460}{44681585}.
\]
In particular,
\[
\boxed{\chi_5(-1)=-\frac{8874496}{44681585}<0,}
\]
so it has a real root below \(-1\), giving exponentially growing parasitic solutions. These claims concern the **fixed two-periodic, zero-equation recurrence** only.

## Assumptions and scope

For \(k\in\{4,5\}\), variable-step BDF\(k\) means differentiating the degree-\(k\) polynomial interpolant through the \(k+1\) most recent grid values at the newest time point and equating that derivative to the right-hand side. The steps alternate exactly; ratios are \(r,r^{-1},r,r^{-1},\ldots\), not arbitrary independent ratios. Initialize arbitrary \(k\) scalar values. A scheme is zero-stable here when its homogeneous sequences are bounded in the number of steps for each fixed \(r\), uniformly as the global grid scale \(h\to0\). Complex and real initial data are allowed. The constant solution mode is retained and neutral; the parasitic modes are all the other modes.

## Proof

**1. Difference transfer.** Normalize the current step to length one and let its ratio to the immediately preceding step be \(r\). The interpolation abscissae relative to the current time are
\[
0,\;-1,\;-1-r^{-1},\;-2-r^{-1},\;-2-2r^{-1}
\]
for BDF4; append \(-3-2r^{-1}\) for BDF5. Let \(\alpha_j\) be the derivative at zero of the \(j\)-th Lagrange basis polynomial. Thus \(\alpha_j\) can be computed exactly by differentiation of the product
\[
\ell_j(t)=\prod_{\substack{0\le m\le k\\m\ne j}}\frac{t-t_m}{t_j-t_m}.
\]
For \(y'=0\), define \(B_j=-\alpha_j/\alpha_0\) for \(1\le j\le k\), so \(y_n=\sum_{j=1}^k B_j y_{n-j}\) and \(\sum_jB_j=1\). With \(\delta_n=y_n-y_{n-1}\), the state \((\delta_n,\delta_{n-1},\ldots,\delta_{n-k+2})^\mathsf T\) evolves by a companion-like matrix whose first row is
\[
\left(-\sum_{j=2}^k B_j,\;-\sum_{j=3}^k B_j,\;\ldots,\;-B_k\right),
\]
with ones on the first subdiagonal and zero elsewhere.

For BDF4 the resulting one-step difference-state transfer is
\[
M_4(r)=\begin{pmatrix}
\dfrac{r^2(16r^2+36r+17)}{(r+2)(3r+2)(4r+1)} &
-\dfrac{r(12r^2+19r+8)}{(r+2)(3r+2)(4r+1)} &
\dfrac{r^2(2r+1)^2}{(r+2)(3r+2)(4r+1)}\\
1&0&0\\0&1&0
\end{pmatrix}.
\]
The two-step matrix is \(P_4(r)=M_4(r^{-1})M_4(r)\). Direct rational multiplication and the trace/principal-minor/determinant formula give the displayed \(\chi_4\). Reversing the phase yields \(M_4(r)M_4(r^{-1})\), with the same characteristic polynomial.

**2. Strict Schur stability for every \(r>0\).** Since \(q=r+r^{-1}\ge2\), the coefficients of \(\chi_4\) are real, and \(D>0\), \(C>0\). The cubic Jury/Schur criterion for \(z^3+az^2+bz+c\) is \(|c|<1\), \(1+a+b+c>0\), \(1-a+b-c>0\), and \(1-b+ac-c^2>0\). In the present normalization these follow from the exact identities
\[
D-C=8(3q^2+19q+27)>0,
\]
\[
D+A+B-C=48(q+2)^2>0,
\]
\[
D-A+B+C=32(4q+9)>0,
\]
\[
D^2-BD-AC-C^2=16(36q^4+450q^3+2047q^2+3982q+2802)>0.
\]
Hence \(\rho(P_4(r))<1\) for every \(r>0\). Since \(P_4\) is a fixed matrix for each fixed periodic ratio, its powers decay geometrically up to a harmless finite constant; its difference-state sequence is summable. The original values, obtained by accumulating differences, therefore remain uniformly bounded. The untouched constant mode contributes only a bounded constant.

**3. Sharp nonuniformity.** Dividing the polynomial by \(D\) and letting \(q\to\infty\) gives \(\chi_4(\lambda)\to\lambda^2(\lambda+1)\). Roots of monic polynomials vary continuously as multisets with their coefficients, so a parasitic multiplier tends to \(-1\) as \(r\to0\) or \(r\to\infty\). The strict inequality in Step 2 proves that the spectral-radius supremum \(1\) is not attained for finite \(r\).

**4. Order-five counterexample.** Construct \(M_5(r)\) using the same exact Lagrange-derivative and difference-transfer procedure but with the extra oldest abscissa. Evaluating \(P_5=M_5(1/10)M_5(10)\) over the rational numbers and expanding \(\det(\lambda I-P_5)\) yields the displayed quartic. Since its leading coefficient is positive, \(\chi_5(\lambda)\to+\infty\) as \(\lambda\to-\infty\), whereas \(\chi_5(-1)<0\). The intermediate-value theorem gives a real root strictly below \(-1\). A corresponding eigendirection yields exponentially increasing differences and hence unbounded BDF5 values. The same two-step spectrum applies to the reciprocal phase.

## Verification

The standalone `verify.py` uses only Python standard-library exact rational arithmetic. It independently reconstructs interpolation derivative weights, both transfer matrices, monodromy polynomials and the four strict Jury numerator identities for twelve rational ratios, and checks the BDF5 quartic at six rational evaluation points. Invocation: `python3 verify.py`. Recorded result: `PASS 169 exact rational assertions`. These finite checks do not prove the statements for every real positive \(r\); Steps 1–4 above give the analytic proof and exact sign certificates.

## Relationship to prior work

Söderlind, Fekete and Faragó (arXiv:1804.04553, earliest public version 2018-04-12) prove zero-stability for sufficiently fine smooth deformations of uniform grids, where adjacent ratios tend to \(1\). Fixed alternating ratios bounded away from \(1\) violate their smoothness hypothesis, so that theorem does not imply the present all-ratio conclusion. Li and Liao (arXiv:2201.00527, first posted 2022-01-03) treat BDF2 and BDF3 on variable grids; their method orders do not cover BDF4 or BDF5. Calvo, Grande and Grigorieff (1990, DOI:10.1007/BF01386395) give sufficient mesh-ratio bounds for variable-order BDF methods on general grids, rather than a stated exact unrestricted two-periodic BDF4 law. Their full text could not be inspected, so possible specialist precedence remains a material originality uncertainty.

## Limitations

No uniform spectral margin or stability constant as \(r\to0,\infty\) is asserted. Nothing here establishes absolute stability for \(y'=\lambda y\) with \(\lambda\ne0\), stability for arbitrary nonperiodic variable grids, convergence rates for nonzero right-hand sides, or universal failure of BDF5 at every ratio. The displayed BDF5 result is an explicit existence counterexample. Classical root criteria and Lagrange interpolation are used without claiming novelty. A 1990 paper with a plausible broader stability topic could not be assessed in full, so the originality assessment is provisional pending specialist review.

## References

1. G. Söderlind, I. Fekete, I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, first posted 2018-04-12, arXiv:1804.04553, https://arxiv.org/html/1804.04553v1 ; *BIT Numerical Mathematics* 58 (2018), 1125–1143.
2. Z. Li, H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, first posted 2022-01-03, arXiv:2201.00527, https://arxiv.org/html/2201.00527v1 ; *SIAM Journal on Numerical Analysis* 60 (2022), 2253–2272.
3. M. Calvo, T. Grande, R. D. Grigorieff, *On the zero stability of the variable order variable stepsize BDF-Formulas*, *Numerische Mathematik* 57 (1990), 39–50, https://doi.org/10.1007/BF01386395 (abstract checked; full text unavailable).
