# Resonant saturation and missing dimensions for cyclic Savitzky–Golay variation gain

## Finding
For an integer \(m\ge2\), let \(T_{m,n}\) be the real cyclic quadratic Savitzky–Golay center smoother with radius \(m\), on \(n\ge2m+1\) equally spaced observations. Let
\[
V_n(x)=\sum_{i=0}^{n-1}|x_{i+1}-x_i|,
\qquad x_n=x_0,
\]
and define its sharp two-input variation coefficient by
\[
L_{m,n}=\sup_{V_n(x-y)>0}
\frac{V_n(T_{m,n}x-T_{m,n}y)}{V_n(x-y)}.
\]
Set
\[
A_m=3m^2+3m-1,\quad
D_m=(2m+1)(4m^2+4m-3),\quad
w_{m,j}=\frac{3(A_m-5j^2)}{D_m}\quad(-m\le j\le m),
\]
and introduce the positive and negative support thresholds
\[
a_m=\max\{j\in\{0,\ldots,m\}:5j^2<A_m\},
\qquad
b_m=\min\{j\in\{0,\ldots,m\}:5j^2>A_m\},
\qquad P_m=2a_m+1.
\]
The **exact sharp saturation set** of cyclic lengths at which the variation gain reaches the full absolute kernel mass is
\[
\boxed{
L_{m,n}=\sum_{j=-m}^{m}|w_{m,j}|
\quad\Longleftrightarrow\quad
2P_m\le n\le 4b_m-2
\ \text{or}\ n\ge P_m+2m+1.
}
\]
Outside these integer ranges, the inequality is strict. In every dimension the full exact value, including the intervening strict-deficit lengths, has the finite formula
\[
\boxed{
L_{m,n}=\frac12\max_{1\le s<n}
\sum_{i=0}^{n-1}|c_i-c_{i-s}|,
}
\]
where indices are modulo \(n\), \(c_{j\bmod n}=w_{m,j}\) for \(-m\le j\le m\), and the remaining cyclic kernel entries are zero. Every maximizing shift is attained by a real binary one-block input.

The usual case without zero kernel coefficients has \(b_m=a_m+1\): the full mass is attained at the **isolated resonant length** \(n=2P_m\), lost for each length \(2P_m+1\le n\le P_m+2m\), and regained permanently from \(n=P_m+2m+1\). If a coefficient vanishes, then \(b_m=a_m+2\) and the first resonant set widens to \(2P_m\le n\le2P_m+4\). Exact zero coefficients occur precisely at integer solutions of \(5j^2=3m^2+3m-1\), for example \(m=6\), \(j=5\).

At the classical five-tap radius \(m=2\), the sharp coefficients for \(n=5,6,7\), and every \(n\ge8\), respectively, are
\[
1,\qquad\frac{47}{35},\qquad\frac{44}{35},\qquad\frac{47}{35}.
\]
Consequently a larger cycle can have **strictly smaller** sharp variation gain than a shorter one. Moreover, as \(m\to\infty\), both the first resonant length and the permanent-saturation threshold are of order \(m\):
\[
\frac{2P_m}{m}\longrightarrow4\sqrt{\frac35},\qquad
\frac{P_m+2m+1}{m}\longrightarrow2+2\sqrt{\frac35}.
\]
The shared full-kernel gain has the already-known limit \(3\sqrt{3/5}-1\); the new assertion is exactly **which finite cycles attain it** and the intervening gap.

## Assumptions and scope
The filter is the ordinary unweighted least-squares fit of a polynomial of degree at most two on each centered \(2m+1\)-point window, evaluated at its center, with periodic wraparound and no repeated sample within a window. Since the window is symmetric, the degree-three fit has identical center weights. The data and coefficients are real, \(m\) is any integer at least two, and \(n\) is any integer at least \(2m+1\).

The seminorm vanishes on constants, which the filter preserves. The supremum uses arbitrary distinct inputs with positive variation of their difference; for this linear filter it is equivalently the operator norm of the induced map on the quotient by constants. No probabilistic assumptions are made.

## Proof
**1. Coefficients and signs.** The center weight formula follows by solving the even \(2\times2\) normal equations of quadratic least squares. Indeed, with \(S_k=\sum_{j=-m}^{m}j^k\), the coefficient of observation \(j\) in the fitted constant term is
\[
\frac{S_4-S_2j^2}{S_0S_4-S_2^2}
=\frac{3(A_m-5j^2)}{D_m}.
\]
These weights sum to one and reproduce the quadratic monomial at the center. Since \(A_m>0\), weights are strictly positive for \(|j|\le a_m\), strictly negative for \(b_m\le |j|\le m\), and zero only when \(5j^2=A_m\). In particular \(b_m\in\{a_m+1,a_m+2\}\). For \(m\ge2\), \(A_m/5>(m+1)^2/4\), so \(P_m\ge m+1\) and hence \(2P_m\ge2m+1\). Also \(P_m>m-b_m\).

**2. Exact norm via two-point differences.** Let \(\Delta x\) be the cyclic forward difference vector. Its entries sum to zero, and every zero-sum vector is a cyclic difference of some real input. Convolution commutes with \(\Delta\), so
\[
V_n(T_{m,n}x)=\|C_{m,n}\Delta x\|_1,
\]
where \(C_{m,n}\) denotes convolution by \(c\). Any zero-sum vector \(u\) decomposes as a finite positive combination of \(e_i-e_j\) with total coefficient mass \(\|u\|_1/2\), by pairing its positive and negative masses. Thus, by the triangle inequality, the norm on the zero-sum subspace is exactly
\[
\max_{i\ne j}\frac{\|C_{m,n}(e_i-e_j)\|_1}{2}
=\frac12\max_{1\le s<n}\sum_i|c_i-c_{i-s}|.
\]
The reverse inequality uses a single \(e_i-e_j\); integrating that difference around the cycle gives a contiguous binary block input and proves attainment.

**3. Equality with full kernel mass.** The triangle inequality gives \(L_{m,n}\le\sum_i|c_i|=\sum_{j=-m}^m|w_{m,j}|\). Equality holds precisely when some shift \(s\) has no overlap between two strictly positive coefficients and no overlap between two strictly negative coefficients: at each coordinate \(|c_i-c_{i-s}|=|c_i|+|c_{i-s}|\) if and only if \(c_i c_{i-s}\le0\).

The positive support is the cyclic arc \(\{-a_m,\ldots,a_m\}\) of length \(P_m\). Its translate is disjoint exactly when
\[
P_m\le s\le n-P_m.
\]
The negative support is the union of the integer arcs \(\{-m,\ldots,-b_m\}\) and \(\{b_m,\ldots,m\}\). Their nonzero positive pairwise displacements comprise exactly the interval \([1,m-b_m]\) within a negative arc and \([2b_m,2m]\) between the two arcs (interpreted as integer intervals). Since \(s\) and \(n-s\) are at least \(P_m>m-b_m\), the negative sets remain disjoint if and only if neither \(s\) nor \(n-s\) belongs to \([2b_m,2m]\).

Hence the two nonoverlap requirements are equivalent to
\[
s,\ n-s\in [P_m,2b_m-1]\ \cup\ [2m+1,\infty),
\]
where all intervals are integer intervals. A pair of entries in the first interval has every possible sum from \(2P_m\) to \(4b_m-2\). A first-interval entry and a second-interval entry have precisely the possible sums at least \(P_m+2m+1\); two second-interval entries give no earlier sum. This proves the stated if-and-only-if saturation set and strictness outside it.

**4. Arithmetic exceptions and limiting lengths.** The quantity \(\sqrt{A_m/5}\) is the unique positive real sign-change threshold. If it is nonintegral, then \(b_m=a_m+1\) and the first saturation interval has a single integer. If it is integral, then \(b_m=a_m+2\) and that interval contains five consecutive integers. For \(m=6\), \(A_m=125=5\cdot5^2\). Finally, \(a_m/m\to\sqrt{3/5}\), and thus the two normalized length limits follow. The standard kernel-mass limit is obtained by the Riemann sum
\[
\sum_{j=-m}^m|w_{m,j}|\longrightarrow
\int_{-1}^{1}\left|\frac{9-15u^2}{8}\right|\,du
=3\sqrt{\frac35}-1.
\]
This last kernel-norm value, unlike the finite-cycle saturation classification, is already available in prior work.

## Verification
The standalone `verify.py` uses exact integer and rational arithmetic. It reconstructs the weights, verifies constant and quadratic reproduction, computes the sharp shift-difference norm and an attaining binary block in every tested case, and compares exact saturation to the stated interval criterion for all radii \(2\le m\le20\) over cyclic lengths spanning both boundaries. It independently tests the support-disjointness equivalence for radii \(21\le m\le120\), including the exceptional zero-coefficient radius \(m=86\). It checks the four five-tap values and the zero-coefficient thirteen-tap example. These are finite corroborations; all-dimensional validity follows from the preceding exact support argument.

## Relationship to prior work
Savitzky and Golay (1964) introduced the center-fitting convolution weights and tabulated the quadratic/cubic windows. Their paper addresses practical least-squares smoothing and its polynomial reproduction, not the induced cyclic total-variation operator norm as a function of cycle length.

*Seven points maximize the positivity defect of quadratic Savitzky–Golay smoothing* (2026) establishes the exact negative kernel mass, the equivalent \(\ell_1\) kernel norm, its seven-point maximum, and the same asymptotic kernel-mass limit. Those facts are **previously known** and are used as context, not claimed here. A kernel-norm bound alone does not say whether the restriction to zero-sum cyclic differences attains that bound; indeed at radius two the lengths six and seven have different sharp gains. The new classification resolves exactly this missing finite-cycle attainment question at every radius, including arithmetic zero-coefficient cases.

The pairwise-column formula is a classical Dobrushin–Deutsch–Zenger type coefficient (see Kirkland and Neumann, 2009), and is also **not** claimed as new. Their paper studies equality between that coefficient and a spectral-eigenvalue bound for general matrices; this does not characterize equality between the coefficient and the absolute kernel mass of periodic Savitzky–Golay smoothers. The new support-arithmetic classification requires the specific positive and negative arcs and their cyclic translations.

Related results on the five-point cyclic filter in complete-pair Gini variation concern a different seminorm: complete-pair differences are not adjacent cyclic differences, and no implication supplies the present all-radius cycle-length saturation criterion. Marchand and Marmet (1983) documented overshoot and frequency artifacts of least-squares smoothing, while Schmid, Rath and Diebold (2022) analyzed its frequency response and filtering alternatives. These descriptions do not establish the present two-input cyclic-variation saturation law. The 1983 full text was not recovered from the accessible sources, so that comparison retains a priority risk.

## Limitations
The result is for real, equal-weight, equally spaced center coefficients with periodic boundary handling and at least one complete nonaliasing window. It does not address nonperiodic endpoints, irregular sampling, higher even polynomial degrees, weighted fits, or repeated-filter convergence. The simple shift formula yields every exact intermediate coefficient but does not express all of those coefficients as a closed elementary function of the radius and cycle length. Historical priority cannot be certified from finite source coverage, particularly because the full 1983 paper was unavailable.

## References
1. A. Savitzky and M. J. E. Golay, *Smoothing and Differentiation of Data by Simplified Least Squares Procedures*, Analytical Chemistry **36** (1964), 1627–1639, DOI: https://doi.org/10.1021/ac60214a047. An archival reproduction of the full text appears as Appendix A of https://ntrs.nasa.gov/api/citations/19700027052/downloads/19700027052.pdf.
2. *Seven points maximize the positivity defect of quadratic Savitzky–Golay smoothing*, publicly available mathematical result, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-seven-points-maximize-the-positivity-defect-of-quadratic-savitzk--401e21174d7a.
3. P. Marchand and L. Marmet, *Binomial smoothing filter: A way to avoid some pitfalls of least-squares polynomial smoothing*, Review of Scientific Instruments **54** (1983), 1034–1041, DOI: https://doi.org/10.1063/1.1137498.
4. M. Schmid, D. Rath and U. Diebold, *Why and How Savitzky–Golay Filters Should Be Replaced*, ACS Measurement Science Au **2** (2022), 185–196, DOI: https://doi.org/10.1021/acsmeasuresciau.1c00054.
5. S. J. Kirkland and M. Neumann, *The Case of Equality in the Dobrushin–Deutsch–Zenger Bound*, Linear Algebra and its Applications **431** (2009), 2373–2394, https://mural.maynoothuniversity.ie/id/eprint/2189/.
