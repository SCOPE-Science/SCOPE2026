# A boundary-derivative singular-value law for harmonic Bergman Toeplitz commutators

## Finding

Fix a real number \(\alpha>-1\), and let \(\mathcal H^2_\alpha(\mathbb D)\) be the complex Hilbert space of square-integrable harmonic functions on the unit disk for the probability measure
\[
d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dx\,dy.
\]
Write \(P_\alpha\) for orthogonal projection onto this harmonic Bergman space and \(T_\phi=P_\alpha M_\phi|_{\mathcal H^2_\alpha}\) for a bounded-symbol Toeplitz compression. Let \(f,g\) be **nonconstant complex analytic polynomials**, and put
\[
C_{f,g}=T_fT_{\overline g}-T_{\overline g}T_f,
\qquad
L(f,g)=\frac1{2\pi}\int_0^{2\pi}\sqrt{|f'(e^{i\theta})g'(e^{i\theta})|}\,d\theta.
\]
Then \(L(f,g)>0\), and the singular values of \(C_{f,g}\), in nonincreasing order with multiplicities, satisfy the exact two-sided tail law
\[
\boxed{\lim_{j\to\infty}j^2s_j(C_{f,g})=4(\alpha+1)L(f,g)^2.}
\]
Equivalently, with \(N_C(t)=\#\{j:s_j(C)>t\}\),
\[
\boxed{\lim_{t\downarrow0}\sqrt t\,N_{C_{f,g}}(t)
=2\sqrt{\alpha+1}\,L(f,g).}
\]
Thus \(C_{f,g}\) is compact and, for every \(p>0\),
\[
C_{f,g}\in\mathcal S_p\quad\Longleftrightarrow\quad p>\tfrac12.
\]
At the sharp weak-\(\mathcal S_{1/2}\) endpoint one additionally has
\[
\boxed{\lim_{J\to\infty}\frac1{\log J}
\sum_{j=1}^{J}s_j(C_{f,g})^{1/2}
=2\sqrt{\alpha+1}\,L(f,g).}
\]
For a constant \(f\) or \(g\), the commutator is identically zero; those degenerate cases are excluded from the positive-coefficient assertion.

## Assumptions and scope

The scalar field is complex. All polynomials are evaluated on the closed unit disk, so their Toeplitz operators are bounded. The allowed weight range is the full probability-weight range \(\alpha>-1\). The singular-value limit concerns the entire commutator, not a single angular diagonal or finite section. Nothing is asserted for unbounded analytic symbols or for arbitrary nonsmooth boundary symbols. The coefficient is independent of the polynomial degrees except through the boundary derivatives, and includes the two harmonic frequency tails.

## Proof

**1. Exact angular matrix.** Put
\[
h_r=\frac{\Gamma(r+1)\Gamma(\alpha+2)}{\Gamma(r+\alpha+2)}\quad(r\ge0).
\]
The orthonormal harmonic monomials are \(e_k=z^k/\sqrt{h_k}\) for \(k\ge0\), and \(e_{-j}=\overline z^{\,j}/\sqrt{h_j}\) for \(j\ge1\). For each integer \(m\ge1\), \(T_{z^m}e_k=w_m(k)e_{k+m}\), with the **exact** positive coefficient
\[
w_m(k)=
\begin{cases}
\sqrt{h_{k+m}/h_k},&k\ge0,\\
\sqrt{h_{-k}/h_{-k-m}},&k\le-m,\\
h_m/\sqrt{h_{-k}h_{k+m}},&-m<k<0.
\end{cases}
\]
This follows by integrating the sole angularly matching monomial. The adjoint \(T_{\overline z^n}=T_{z^n}^*\) shifts backward by \(n\). Consequently
\[
[T_{z^m},T_{\overline z^n}]e_k
=\bigl(w_n(k-n)w_m(k-n)-w_m(k)w_n(k+m-n)\bigr)e_{k+m-n}.
\]
The displayed matrix identity is valid for every integer \(k\), including the finitely many crossing indices.

**2. Uniform leading coefficients of the two ends.** Write \(a=\alpha+1>0\). The gamma-ratio expansion
\[
\log h_x=\log\Gamma(\alpha+2)-a\log x-\frac{a(a+1)}{2x}+O(x^{-2})
\]
and its differentiated versions show, for fixed positive \(m,n\), that the coefficient in the previous display is
\[
-\frac{amn}{k^2}+O(k^{-3})\quad(k\to+\infty),
\qquad
+\frac{amn}{|k|^2}+O(|k|^{-3})\quad(k\to-\infty).
\]
For clarity, on the positive tail this coefficient has the exact form
\[
\frac{h_kh_{k+m-n}/h_{k-n}-h_{k+m}}{\sqrt{h_kh_{k+m-n}}},
\]
for all sufficiently large \(k\). Taking logarithms of the numerator ratio gives the negative mixed second difference of \(\log h_x\), with leading term \(-amn/k^2\). The negative tail follows by the same formula with reversed frequencies and exchanged shifts. Because the polynomial degrees are finite, both error estimates hold simultaneously for all occurring \((m,n)\).

Write \(f(z)=\sum_{m\ge0}a_mz^m\) and \(g(z)=\sum_{n\ge0}b_nz^n\). All terms with a zero index commute with everything. The positive-frequency tail of \(C_{f,g}\), up to finitely many central rows, is therefore a finite-band matrix of the form
\[
-a\,\bigl(q_{j-k}k^{-2}\bigr)_{j,k\ge1}+R_+,
\qquad
q(e^{i\theta})=f'(e^{i\theta})\,\overline{g'(e^{i\theta})},
\]
where every fixed-band entry of \(R_+\) in column \(k\) is \(O(k^{-3})\). The negative-frequency tail has the same structure with sign reversed and frequencies reflected: its Laurent symbol is \(q(e^{-i\theta})\). These symbols have the same distribution of absolute values under normalized circle measure. There are only finitely many matrix coefficients connecting the two tails, so their contribution is finite rank.

**3. Elementary weighted-Laurent counting lemma.** Let \(q\not\equiv0\) be any finite Laurent polynomial and let \(B_q\) on \(\ell^2(\mathbb N)\) have entries \((B_q)_{j,k}=q_{j-k}/k^2\). Then
\[
\lim_{t\downarrow0}\sqrt t\,N_{B_q}(t)
=\frac1{2\pi}\int_0^{2\pi}\sqrt{|q(e^{i\theta})|}\,d\theta.
\tag{*}
\]
Here is a proof rather than an appeal to an unverified asymptotic theorem. For fixed \(0<\varepsilon<1<R\), restrict indices to the interval from \(\varepsilon/\sqrt t\) to \(R/\sqrt t\). Its omitted low-index part has rank at most \(\varepsilon/\sqrt t+1\). Its high-index remainder has norm at most \(\|q\|_\infty\,t/R^2\), so it has no singular values above \(t\) if \(R>\sqrt{\|q\|_\infty}\). Divide the remaining interval into finitely many geometric blocks with successive endpoint ratio at most \(1+\delta\). Erasing cross-block entries changes the matrix by a uniformly bounded-rank operator (the bandwidth and number of blocks are fixed when \(\varepsilon,R,\delta\) are fixed). On a block with left endpoint \(K\), replacing \(k^{-2}\) by \(K^{-2}\) changes its operator norm by at most \(C_q\delta K^{-2}\). Weyl's singular-value inequalities control the counts by thresholds differing by this bound.

For a length-\(\ell\) block the unweighted section is the ordinary finite Toeplitz matrix \(T_\ell(q)\). Its singular-value empirical measures converge to the pushforward of normalized Lebesgue measure by \(|q|\): indeed \(T_\ell(q)^*T_\ell(q)\) differs from \(T_\ell(|q|^2)\) by uniformly bounded rank, and normalized traces of fixed powers of the latter converge to the Fourier integrals of \(|q|^{2r}\); polynomial approximation then proves empirical-measure convergence. In every fixed geometric block, its length tends to infinity as \(t\downarrow0\). Thus the asymptotic count from that block is its length times the angular proportion on which \(K^{-2}|q|>t\), subject to arbitrarily small \(\delta\)-threshold errors. Sending \(t\downarrow0\), then \(\delta\downarrow0\), sums these contributions into
\[
\int_\varepsilon^R\!\frac1{2\pi}\int_0^{2\pi}
\mathbf 1_{\{|q(e^{i\theta})|>y^2\}}\,d\theta\,dy.
\]
A constant-modulus symbol is treated by threshold squeezing, or directly as a scalar monomial Laurent symbol. Finally send \(\varepsilon\downarrow0\) and \(R\to\infty\). Tonelli's theorem evaluates the resulting double integral as the right side of (*). This establishes the lemma including symbols with zeros.

**4. Removal of errors and conclusion.** A banded matrix with column entries \(O(k^{-3})\) has a tail after index \(K\) of norm \(O(K^{-3})\). At singular threshold \(t\), truncating at \(K\asymp t^{-1/3}\) gives \(N_R(ct)=O_c(t^{-1/3})=o(t^{-1/2})\) for every fixed \(c>0\). Thus the \(R_\pm\) terms do not affect (*) by Weyl counting inequalities. The finite-rank central couplings likewise have no leading effect. Apply (*) to the two tails, multiply their counting coefficients by \(\sqrt a\), and add. This proves
\[
\lim_{t\downarrow0}\sqrt t\,N_{C_{f,g}}(t)
=2\sqrt a\int_{\mathbb T}\sqrt{|f'g'|}\,dm=2\sqrt a\,L(f,g).
\]
Monotone counting-function inversion yields the singular-value limit. The stated \(\mathcal S_p\) dichotomy follows by comparison with \(j^{-2}\). Finally \(s_j^{1/2}\sim2\sqrt a\,L/j\), and harmonic-sum comparison yields the logarithmic limit. No finite computation has been used to infer an infinite-dimensional limit.

## Verification

The accompanying `check.py` recomputes the exact weighted angular matrix, tests the coefficients for multiple integral and nonintegral weights and monomial pairs, checks sample polynomial-band coefficients, and compares a finite compression's singular values with the predicted boundary-derivative coefficient. Its fixed test case has \(L=1.1715731238\ldots\), so the predicted constant is \(5.4903343374\ldots\) at \(\alpha=0\). The checker passes 411 explicitly counted assertions and reports the finite-size approach to that value. These numerical tests do not establish the counting lemma; its proof is in the preceding section.

Run from this directory with Python 3, after installing the two dependencies in `requirements.txt`, using `python check.py`.

## Relationship to prior work

Tian, Wang, and Zhao (2026) establish the qualitative commuting rigidity of analytic and coanalytic Toeplitz operators on the harmonic Bergman disk. This finding instead supplies a sharp spectral distribution and a boundary-integral constant for their nonzero commutators. Dong and Zhou (2013) develop the angular projection formulas and symmetry numbers for individual quasihomogeneous commutators; those are not new here. The individual monomial mixed commutators and their \(j^{-2}\) asymptotics have also been evaluated previously; their special cases are not claimed as new. The present boundary integral describes **interference between distinct monomial diagonals** for arbitrary pairs of analytic polynomials. Chbichib and Ghiloufi (2026) study \([M_u,P_\alpha]\) on the ambient \(L^2\), which is a different operator with order-\(j^{-1}\) singular decay. These sources supply relevant background but not the displayed order-\(j^{-2}\) polynomial pair law.

## Limitations

The proof assumes polynomial symbols, rather than arbitrary analytic functions of low boundary regularity. The result is leading-order only; it does not provide finite-index singular values, an exact trace norm, or a full spectral phase distribution. The counting lemma is established for finite Laurent symbols, and does not automatically extend to discontinuous symbols. A more general pseudodifferential/Birman–Solomyak Weyl theorem may imply the result indirectly; the literature comparison does not certify definitive historical priority. The result has not undergone independent mathematical review.

## References

1. X. Tian, J. Wang, X. Zhao, *Commuting analytic and co-analytic Toeplitz operators on the harmonic Bergman space*, arXiv:2609.14635 (first public September 13, 2026), https://arxiv.org/abs/2609.14635.
2. X.-T. Dong and Z.-H. Zhou, *Commuting Quasihomogeneous Toeplitz Operators on the Harmonic Bergman Space*, Complex Analysis and Operator Theory 7 (2013), 1267–1285, doi:10.1007/s11785-012-0223-0.
3. K. Chbichib and N. Ghiloufi, *Spectral properties of commutators on harmonic Bergman spaces of the unit disk*, arXiv:2605.24698 (first public May 23, 2026), https://arxiv.org/abs/2605.24698.
4. M. Huang, J. Wang, X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638 (first public October 7, 2026), https://arxiv.org/abs/2610.09638.
