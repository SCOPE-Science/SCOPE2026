# Sharp singular-value Weyl law for compact polynomial Fock–Sobolev integral sums

## Finding

Let \(n\ge1\), \(N\ge0\), and \(m,\ell\ge0\) be integers, and let \(g_0,\ldots,g_N\) be complex polynomials, not all zero. On the weighted Gaussian Fock–Sobolev Hilbert spaces specified below, consider
\[
Tf=I^n\!\left(\sum_{j=0}^{N}g_j f^{(j)}\right),\qquad (If)(z)=\int_0^z f(w)\,dw.
\]
Put
\[
d=n+m-\ell,\quad D=\max_{g_j\ne0}\bigl(j+\deg g_j\bigr),\quad
\delta=d-D\in\{1,2,\ldots\},\quad \alpha=\delta/2,
\]
and form the nonzero polynomial
\[
Q(w)=\sum_{j=0}^{N}c_jw^j,\qquad c_j=[z^{D-j}]g_j(z),
\]
where the coefficient is understood to be zero if \(D-j<0\). Define
\[
\mathcal C=\frac{1}{2\pi}\int_0^{2\pi}\bigl|Q(e^{i\theta})\bigr|^{2/\delta}\,d\theta>0.
\]
Then \(T\) is compact, and its positive singular-value counting function and ordered singular values satisfy the **sharp** laws
\[
\lim_{t\downarrow0}t^{2/\delta}\#\{k:s_k(T)>t\}=\mathcal C,\qquad
\lim_{k\to\infty}k^{\delta/2}s_k(T)=\mathcal C^{\delta/2}.
\]
For each \(p>0\), membership in the Schatten (quasi-)ideal is equivalent to \(p>2/\delta\). At the critical exponent,
\[
\lim_{K\to\infty}\frac{1}{\log K}\sum_{k=1}^{K}s_k(T)^{2/\delta}=\mathcal C.
\]
All three constants are insensitive to strictly lower total-degree terms and depend on the leading terms through the full angular polynomial, not merely through the largest coefficient.

## Assumptions and scope

For a nonnegative integer \(r\), use the exact norm
\[
\|f\|_{2,r}^{2}=\frac{1}{\pi}\int_{\mathbb C}|f(z)|^{2}(1+|z|)^{2r}e^{-|z|^{2}}\,dA(z)
\]
and denote its entire-function Hilbert space by \(\mathcal F_r^2\). The operator above maps \(\mathcal F_m^2\) to \(\mathcal F_\ell^2\). The requirement \(D<d\) is the compact total-degree regime. The theorem is for **finite** polynomial coefficient vectors, the stated normalized Gaussian norms, and integer integration order. Arbitrary entire coefficients, fractional Sobolev orders, and non-Hilbert exponents are not asserted. The counting function counts singular values with multiplicity and uses a strict threshold; changing the convention at a threshold does not change the limit. If some derivatives annihilate low-degree monomials, only finitely many columns are affected.

## Proof

**1. Exact normalized matrix coefficients.** For \(r\in\mathbb N_0\), radial integration gives
\[
\beta_r(k):=\|z^k\|_{2,r}^2
=\sum_{v=0}^{2r}\binom{2r}{v}\Gamma(k+1+v/2)
=\Gamma(k+r+1)(1+O(k^{-1/2})).
\]
Consequently \(e_k^{(r)}=z^k/\sqrt{\beta_r(k)}\), \(k\ge0\), is an orthonormal basis. A coefficient \(a_{j,h}z^h\) of \(g_j\) sends \(e_k^{(m)}\) to a scalar multiple of \(e_{k+\nu}^{(\ell)}\), where \(\nu=n+h-j\). For \(k\ge j\), that scalar is exactly
\[
a_{j,h}\frac{k!}{(k-j)!}\frac{(k-j+h)!}{(k-j+h+n)!}
\sqrt{\frac{\beta_\ell(k+\nu)}{\beta_m(k)}}
=a_{j,h}k^{-(d-j-h)/2}\bigl(1+O(k^{-1/2})\bigr).
\]
The exponent follows by combining \(k^j\), \(k^{-n}\), and \(k^{(\nu+\ell-m)/2}\). At \(k<j\), the contribution is zero; any negative output indices occur only at finitely many low inputs. This is an exact-to-asymptotic formula in the stated norm, including its leading constant \(1\).

**2. Principal weighted Laurent band.** Let \(D_\alpha\) act on \(\ell^2(\mathbb N_0)\) by \(D_\alpha e_k=(1+k)^{-\alpha}e_k\). Let \(V_b\) be the unilateral forward shift of integer order \(b\) for \(b\ge0\) and the backward shift for \(b<0\). Under the two monomial unitaries, the integral sum becomes
\[
\widetilde T=W+R,\qquad
W=\sum_{j=0}^{N}c_j V_{n+D-2j}D_\alpha.
\]
Indeed, the terms having \(j+h=D\) have the displayed leading weights, with \(n+h-j=n+D-2j\); all other terms have at least one extra half-power of decay. The finitely many row-boundary discrepancies are finite rank. The remainder is a fixed finite sum of bands with column coefficients \(O((1+k)^{-\alpha-1/2})\). Truncating the first \(M\) columns is rank at most \(M\), and the norm of the remaining finite band is \(O(M^{-\alpha-1/2})\). Thus
\[
s_M(R)=O(M^{-\alpha-1/2}),\qquad N_R(t)=O(t^{-1/(\alpha+1/2)})=o(t^{-1/\alpha}).
\]
The Laurent polynomial symbol of \(W\) is
\[
P(e^{i\theta})=\sum_j c_j e^{i(n+D-2j)\theta}
=e^{i(n+D)\theta}Q(e^{-2i\theta}).
\]
Its modulus has precisely the same normalized distribution as \(|Q(e^{i\theta})|\), because multiplication by a unimodular factor changes no modulus and angle-doubling preserves normalized Haar measure.

**3. Finite-band weighted Weyl lemma.** For a fixed nonzero finite Laurent polynomial \(P\) and every \(\alpha>0\), the compact band operator \(W_P=(\sum_b p_bV_b)D_\alpha\) obeys
\[
\lim_{t\downarrow0}t^{1/\alpha}N_{W_P}(t)
=\frac{1}{2\pi}\int_0^{2\pi}|P(e^{i\theta})|^{1/\alpha}\,d\theta.
\]
Here is an elementary proof, including the infinite-index tails. Put \(L=t^{-1/\alpha}\). Fix \(0<\varepsilon<R_0<\infty\) and compress \(L^\alpha W_P\) to column and row indices in \([\varepsilon L,R_0L]\cap\mathbb N_0\), obtaining a finite matrix \(A_L\). For every positive integer \(q\), direct expansion of closed band walks gives
\[
\lim_{L\to\infty}\frac1L\operatorname{Tr}\bigl[(A_L^*A_L)^q\bigr]
=\frac1{2\pi}\int_\varepsilon^{R_0}\int_0^{2\pi}
 x^{-2\alpha q}|P(e^{i\theta})|^{2q}\,d\theta\,dx.
\]
To justify this equality, discard the \(O(1)\) indices within the fixed band width of either endpoint. On each remaining closed walk, every index differs by \(O(q)\) from the starting index. Its rescaled column weight converges uniformly to \(x^{-\alpha}\), and the sum of coefficients over zero-net-displacement walks is exactly the zeroth Fourier coefficient of \(|P|^{2q}\). Division by \(L\) turns the remaining starting-index sum into a Riemann sum. The zeroth moment is the dimension divided by \(L\), namely \(R_0-\varepsilon\), so the same conclusion holds for every polynomial in the squared singular values. All such values lie in a common compact interval depending on \(\varepsilon\); polynomial approximation extends the limit to continuous functions. For the indicator of the set above singular-value threshold \(1\), approximation applies because the limiting threshold set \(x^{-\alpha}|P(e^{i\theta})|=1\) has two-dimensional measure zero: for each \(\theta\), it contains at most one \(x>0\).

Restoring the discarded low columns changes the counting function by at most \(\varepsilon L+O(1)\). Beyond \(R_0L\), the operator norm is at most \(\|P\|_\infty(R_0L)^{-\alpha}\); choosing \(R_0\) large makes its rescaled norm arbitrarily small. The row-compression discrepancy at each block endpoint has rank bounded by the fixed band width. Ky Fan inequalities therefore sandwich the full normalized counting function between nearby finite-block thresholds with an error at most \(\varepsilon+o(1)\). Let \(\varepsilon\downarrow0\), \(R_0\uparrow\infty\), and the auxiliary threshold shifts tend to zero. Integrating over the positive radial variable yields
\[
\frac1{2\pi}\int_0^{2\pi}\left[\int_0^\infty
\mathbf1\{x^{-\alpha}|P(e^{i\theta})|>1\}\,dx\right]d\theta
=\frac1{2\pi}\int_0^{2\pi}|P(e^{i\theta})|^{1/\alpha}\,d\theta.
\]
This proves the lemma for all \(\alpha>0\) and allows Laurent terms of either shift direction. It uses no unproved infinite-dimensional inference from a finite sample.

**4. Remainder removal and consequences.** Apply the lemma to \(W\). The singular-counting perturbation inequalities
\[
N_{A+B}(t)\le N_A((1-\eta)t)+N_B(\eta t),\qquad 0<\eta<1,
\]
and the symmetric lower bound obtained by exchanging \(A+B\) and \(A\) show that \(R\), having \(N_R(t)=o(t^{-1/\alpha})\), cannot change the leading constant. Therefore \(N_T(t)\sim\mathcal C t^{-1/\alpha}\). Monotone inversion of the counting function gives \(s_k(T)\sim\mathcal C^\alpha k^{-\alpha}\). Summation of the corresponding powers proves the precise Schatten cutoff; at \(p=1/\alpha\), the asymptotic \(s_k(T)^p\sim \mathcal C/k\) and harmonic summation give the stated logarithmic residue. Finally \(Q\not\equiv0\) because distinct \(j\)'s contribute distinct monomials, so \(\mathcal C>0\).

## Verification

For the standard Gaussian Fock space, take \(n=3\), \(m=\ell=0\), \(g_0(z)=z\), \(g_1(z)=1\). Then \(D=1\), \(d=3\), \(\delta=2\), \(Q(w)=1+w\), and
\[
\mathcal C=\frac1{2\pi}\int_0^{2\pi}|1+e^{i\theta}|\,d\theta=\frac4\pi.
\]
The nonorthogonal two-band sum \(Tf=I^3(zf+f')\) consequently satisfies \(s_k(T)\sim 4/(\pi k)\), and \(\sum_{k\le K}s_k(T)\sim (4/\pi)\log K\). Its two matrix bands have exact weights
\[
 a_k=\sqrt{\frac{k+1}{(k+2)(k+3)(k+4)}}\quad\text{at shift }4,
\qquad b_k=\frac{\mathbf1_{k\ge1}}{\sqrt{(k+1)(k+2)}}\quad\text{at shift }2.
\]
A standalone finite-section diagnostic checks these weights against the integration and factorial formulas, diagonalizes the associated parity-tridiagonal finite Gram matrix, and evaluates the angular integral independently. It reports \(182\) passed assertions. The finite diagnostic is supplementary; the full theorem is proved in the preceding four steps. Reproduce it using \(\texttt{python fock_weyl_check.py}\) with NumPy and SciPy installed.

## Relationship to prior work

Dong and Hu, *Carleson Measures and Integral Operators on Fock–Sobolev Spaces* (arXiv:2611.01959v1), define this generalized integral operator and prove its boundedness and compactness total-degree criteria. Their Theorem 1.5 and equation (50) identify the critical-degree Laurent Toeplitz operator modulo compacts and give its exact essential norm. The present theorem works at the strictly subcritical degree, keeps the first nonzero compact order, and determines the **ordered singular-value asymptotics**, the corresponding sharp angular coefficient and weak-Schatten residue. The critical-degree Fredholm and essential-norm results do not supply these numerical compact-tail constants.

Mengestie's 2017 work on classical Volterra-type Fock–Sobolev operators and his 2015 work on generalized Volterra companions establish Schatten membership and norm comparabilities for other operator families, not this full mixed-derivative polynomial family with its ordered-singular-value constant. Classical Avram–Parter/locally Toeplitz and Birman–Solomyak pseudodifferential Weyl principles are substantively related to the weighted-band step; the proof above gives a self-contained version and explicitly derives the Gaussian Fock coefficient symbol. Such broader machinery may provide an alternative derivation and reduces any claim of methodological novelty. No priority or independence claim is made.

## Limitations

Only the leading Weyl coefficient and its critical logarithmic residue are determined, not a second asymptotic term or individual finite-index singular values. The proof uses exact Gaussian radial moments and finite polynomial coefficient vectors. It is not asserted for general entire coefficients, arbitrary weights, non-Hilbert exponents or infinite sums. Standard pseudodifferential Weyl results may subsume the abstract finite-band lemma; originality is claimed, to the extent supported by the cited literature comparison, for the explicit full Fock–Sobolev integral-sum spectral classification. No independent validation or publication-priority certification has been performed.

## References

1. J. Dong and S. Hu, *Carleson Measures and Integral Operators on Fock–Sobolev Spaces*, arXiv:2611.01959v1, first public version November 1, 2026. https://arxiv.org/html/2611.01959v1
2. T. Mengestie, *Spectral properties of Volterra-type integral operators on Fock–Sobolev spaces*, arXiv:1702.08157 (2017). https://arxiv.org/abs/1702.08157
3. T. Mengestie, *Schatten class generalized Volterra companion integral operators*, arXiv:1507.03536 (2015). https://arxiv.org/abs/1507.03536
4. C. Garoni and S. Serra-Capizzano, *Spectral Distribution Results Beyond the Algebra Generated by Variable-Coefficient Toeplitz Sequences: The GLT Approach*, J. Fourier Anal. Appl. 24 (2018), 997–1031. https://doi.org/10.1007/s00041-017-9525-y
5. Birman–Solomyak, classical spectral asymptotics for negative-order pseudodifferential operators (general background); a contemporary account: https://doi.org/10.1016/j.jfa.2022.109704
