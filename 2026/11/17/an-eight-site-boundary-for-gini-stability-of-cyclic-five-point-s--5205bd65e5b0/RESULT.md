# An eight-site boundary for Gini stability of cyclic five-point Savitzky–Golay smoothing

## Finding
For every integer \(n\ge5\), let \(S_n\) be the periodic five-point quadratic Savitzky–Golay smoother on real \(n\)-tuples,
\[
(S_nf)_i=\frac{-3f_{i-2}+12f_{i-1}+17f_i+12f_{i+1}-3f_{i+2}}{35},\qquad i\in\mathbb Z/n\mathbb Z.
\]
For complete-pair Gini variation \(G_n(f)=\sum_{0\le i<j<n}|f_i-f_j|\), its exact two-input operator seminorm \(L_n=\sup_{G_n(f-g)>0}G_n(S_nf-S_ng)/G_n(f-g)\) satisfies
\[
L_5=\frac67,\qquad L_6=\frac{101}{105},\qquad L_7=\frac{69}{70},\qquad L_8=\frac{251}{245}.
\]
Consequently, \(G_n(S_nf-S_ng)\le G_n(f-g)\) for every pair of real signals **if and only if** \(5\le n\le7\). For every \(n\ge8\) a single-coordinate impulse gives the strict ratio
\[
\frac{G_n(S_ne_0)}{G_n(e_0)}=\frac{47n-125}{35(n-1)}=1+\frac{12n-90}{35(n-1)}>1.
\]
The sharp dimension-uniform envelope is
\[
\sup_{n\ge5}L_n=\frac{47}{35},\qquad
\frac{47n-125}{35(n-1)}\le L_n\le\frac{47}{35}\quad(n\ge5).
\]
No exact formula for fixed \(n\ge9\) is claimed.

## Assumptions and scope
The filter acts on the cycle \(\mathbb Z/n\mathbb Z\) with **periodic wraparound** and the fixed classical five-point degree-two least-squares stencil; it is not the endpoint-adjusted filter on an open interval. Every input coordinate is real, the sampling masses are equal, and every distinct unordered vertex pair is included once in \(G_n\). The seminorm annihilates constants. For \(n\ge5\), the five cyclic positions in each window are distinct. Equality of two-input and one-input operator ratios follows from linearity of \(S_n\).

## Proof
**1. Polynomial-fitting normalization.** On the five offsets \(j=-2,-1,0,1,2\), the least-squares evaluation functional at zero in the span of \(1,j,j^2\) has weights \(h_j=1/5-(j^2-2)/7\). Indeed \(j^2-2\) is orthogonal to \(1,j\), has squared norm \(14\), and has value \(-2\) at the center. Thus \(35h_j=(-3,12,17,12,-3)\) in offset order, and \(\sum_jh_j=1\). In particular constants are fixed.

**2. Exact binary-cut reduction.** For a nonempty proper subset \(A\subset\mathbb Z/n\mathbb Z\) with \(|A|=k\), define
\[
F_n(A)=\sum_{0\le i<j<n}\left|\sum_{r=-2}^{2}w_r\bigl(\mathbf1_A(i+r)-\mathbf1_A(j+r)\bigr)\right|,
\quad (w_{-2},\ldots,w_2)=(-3,12,17,12,-3).
\]
Then \(G_n(\mathbf1_A)=k(n-k)\) and
\[
L_n=\max_{\varnothing\ne A\subsetneq\mathbb Z/n\mathbb Z}\frac{F_n(A)}{35|A|(n-|A|)}.
\]
To prove this equality, sort the distinct values of any real vector \(f\). Its layer-cake decomposition is \(f=c\mathbf1+\sum_t a_t\mathbf1_{A_t}\) with \(a_t\ge0\) and nested upper level sets \(A_t\). The Gini seminorm of \(f\) equals \(\sum_t a_t|A_t|(n-|A_t|)\), while the triangle inequality and constant preservation give \(G_n(S_nf)\le\sum_t a_tG_n(S_n\mathbf1_{A_t})\). Thus binary cuts control *every* real input; conversely each cut is an admissible input.

**3. Complete finite base calculation.** Complementation and rotation leave the cut ratio unchanged. The following entries are the integer maxima of \(F_n(A)\) among **all** \(\binom nk\) subsets with \(|A|=k\). By complementation it suffices to show \(1\le k\le\lfloor n/2\rfloor\):

| \(n\) | maximum for \(k=1\) | \(k=2\) | \(k=3\) | \(k=4\) |
|---|---:|---:|---:|---:|
| 5 | 110 | 180 | — | — |
| 6 | 157 | 256 | 303 | — |
| 7 | 204 | 338 | 414 | — |
| 8 | 251 | 420 | 531 | 560 |

All these maxima are attained by a contiguous arc of the corresponding size. The standalone program `check_sg_gini.py` is an **exhaustive exact-integer certificate**: for each \(n=5,6,7,8\), it visits every mask \(1\le m\le2^n-2\), constructs the corresponding cut, calculates all \(\binom n2\) integer pair differences after applying \(35S_n\), and checks the table and the consecutive-arc witnesses. It checks **472 cuts without skipping any** (30, 62, 126, 254). Dividing each table entry by \(35k(n-k)\) gives the four stated sharp norms. This finite enumeration proves precisely the four finite base cases, not an unenumerated infinite family.

**4. An infinite family of strictly amplifying witnesses.** For every \(n\ge5\), \(35S_ne_0\) has exactly five nonzero entries with multiset \((-3,-3,12,12,17)\) and \(n-5\) zero entries. Its five nonzero entries contribute \(110\) to their mutual pair variation: \(4\cdot15+2\cdot20+2\cdot5=110\). Each zero contributes \(47\) in variation against those five entries. Hence \(35G_n(S_ne_0)=47n-125\), whereas \(G_n(e_0)=n-1\). The resulting ratio exceeds one exactly when \(n\ge8\). This algebraic calculation proves the statement in **every** larger dimension, independently of any finite experiment.

**5. Sharp uniform envelope.** Each cyclic shift preserves \(G_n\), and the triangle inequality yields
\[
G_n(S_nf)\le\frac{|-3|+|12|+|17|+|12|+|-3|}{35}G_n(f)=\frac{47}{35}G_n(f).
\]
The preceding impulse ratios tend to \(47/35\) as \(n\to\infty\); therefore the supremum over the whole family is exactly \(47/35\). This is a supremum statement, not a classification of all finite-dimension extremizers.

## Verification
Run `python3 check_sg_gini.py` with standard Python 3. It checks the three polynomial-reproduction moments, all 472 cuts for the four finite dimensions, the table and arc witnesses, and the closed impulse identity for dimensions 5–100. A separate small collection of integer-signal tests corroborates (but does not prove) the real-input extension. The all-real-input reduction and all-dimension witness and envelope are analytical parts of the proof. The checker uses only integers and `fractions.Fraction`; it requires no third-party packages.

## Relationship to prior work
Savitzky and Golay (1964) introduced local least-squares convolution smoothing. Schafer (2011) analyzes its frequency response; Candan and Inan (2014), especially their five-point derivation and finite-difference representation, give the identical stencil and implementation. Those contributions supply the historical operator, **not** the complete-pair Gini operator seminorm on finite periodic samples. A mathematical research record concerning the positivity defect of quadratic Savitzky–Golay kernels quantifies negative convolution mass but does not supply the sharp eight-site boundary. The present claim is the precise Gini cut classification and limiting family envelope, not the known five filter coefficients or a positivity-defect restatement.

## Limitations
The exact fixed-size seminorm is determined here only for \(5\le n\le8\). The two-sided bounds hold for every \(n\ge5\), with a sharp dimension-uniform supremum, but no formula for the exact norm in each larger dimension is asserted. This theorem is restricted to periodic, equally weighted, real-valued data and the fixed classical five-point quadratic/cubic center smoother. Nonperiodic boundary rules, longer Savitzky–Golay windows, weighted least squares and other dispersion seminorms are not covered. Although inspected literature does not imply the eight-site result, its historical originality has not been independently certified.

## References
1. A. Savitzky and M. J. E. Golay, *Smoothing and Differentiation of Data by Simplified Least Squares Procedures*, Analytical Chemistry 36 (1964), 1627–1639, doi:10.1021/ac60214a047; reproduced as Appendix A in Stanford RSL Technical Report 70-11, https://ntrs.nasa.gov/api/citations/19700027052/downloads/19700027052.pdf.
2. R. W. Schafer, *What Is a Savitzky-Golay Filter?*, IEEE Signal Processing Magazine 28 (2011), 111–117, doi:10.1109/MSP.2011.941097.
3. Ç. Candan and H. Inan, *A unified framework for derivation and implementation of Savitzky–Golay filters*, Signal Processing 104 (2014), 203–211, doi:10.1016/j.sigpro.2014.04.016; author-hosted text https://web.stanford.edu/~inanh/papers/unified-sg.pdf.
