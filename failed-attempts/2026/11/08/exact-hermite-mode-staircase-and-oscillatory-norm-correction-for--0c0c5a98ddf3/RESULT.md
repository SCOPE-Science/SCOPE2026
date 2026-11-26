# Exact Hermite-mode staircase and oscillatory norm correction for Gaussian annular localization

## Finding

For every fixed annular area \(L>0\), the optimal unit-energy signal concentrating its Gaussian short-time Fourier transform on the circular annulus
\[
E_{s,L}=\{(x,\xi)\in\mathbb R^2:s\le \pi(x^2+\xi^2)\le s+L\},\qquad s\ge0,
\]
is completely determined. Put
\[
\rho(s,L)=\frac L{\log(1+L/s)}\quad(s>0),\qquad \rho(0,L)=0.
\]
If \(s>0\) and \(\rho(s,L)\notin\mathbb N\), the **only** maximizers up to a nonzero complex scalar are Hermite functions of order \(\lfloor\rho(s,L)\rfloor\). If \(\rho(s,L)=j\in\mathbb N\), the full maximizing eigenspace is exactly the span of Hermite functions of orders \(j-1\) and \(j\). For \(s=0\), the Gaussian (order zero) alone maximizes. In particular, the operator norm has a complete infinite sequence of strict eigenmode changes at
\[
s_n(L)=\frac L{\exp(L/(n+1))-1},\qquad n=0,1,2,\ldots.
\]
At each \(s_n(L)\), the right derivative of the norm exceeds the left derivative by the positive amount
\[
J_n(L)=\frac{L\,s_n(L)^n e^{-s_n(L)}}{n!\,[s_n(L)+L]}.
\]

There is also a precise **oscillatory second asymptotic term**. Set
\[
C_L=\frac{L^2}{24}+\frac L4-\frac1{24},\qquad
\vartheta(s,L)=\left\{\frac L{\log(1+L/s)}\right\},
\]
where braces denote fractional part. For fixed \(L>0\), uniformly as \(s\to\infty\), including arbitrarily close to switching radii,
\[
\boxed{\|P_{s,L}\|=\frac L{\sqrt{2\pi s}}\left(1-\frac{C_L+\frac12(\vartheta(s,L)-\frac12)^2}{s}+O_L(s^{-2})\right).}
\]
The exact cluster set of the scaled next-order coefficient is
\[
\left\{\lim_{k\to\infty}s_k\left(\frac{\sqrt{2\pi s_k}}L\|P_{s_k,L}\|-1\right):s_k\to\infty\right\}
=[-C_L-1/8,-C_L].
\]
In particular, one cannot replace the oscillatory term by a single constant at order \(s^{-3/2}\).

## Assumptions and scope

Use the unit Gaussian \(\phi(t)=2^{1/4}e^{-\pi t^2}\) on \(L^2(\mathbb R)\), and the short-time Fourier transform
\[
V_\phi f(x,\xi)=\int_{\mathbb R} f(t)\overline{\phi(t-x)}e^{-2\pi it\xi}\,dt.
\]
The operator is the positive, compact concentration operator \(P_{s,L}=V_\phi^*\mathbf1_{E_{s,L}}V_\phi\), with the Lebesgue area measure \(dx\,d\xi\) and no additional normalization by the annulus area. The width parameter \(L\) is the literal Euclidean area of the annulus. Hermite functions \(h_n\) are the orthonormal eigenfunctions with \(h_0=\phi\). The index \(n\) ranges over all nonnegative integers. The statement is global in \(s\ge0\), not an assertion restricted to an enumerated collection of radii.

## Proof

**Spectral starting point.** The radial-Gaussian diagonalization of Daubechies, as quoted and applied in Knutsen (2019, Section 2.3 and Section 3.1), gives the exact Hermite eigenvalues
\[
\lambda_n(s,L)=\frac1{n!}\int_s^{s+L}u^n e^{-u}\,du.
\]
In particular \(\lambda_n>0\), and Tonelli's theorem gives \(\sum_{n\ge0}\lambda_n=L\). Thus \(\lambda_n\to0\), the operator is compact, and its norm is attained by the largest Hermite eigenvalue.

**A complete adjacent-difference test.** Since
\[
\frac{d}{du}(u^{n+1}e^{-u})=(n+1-u)u^ne^{-u},
\]
integration by parts yields the *exact* identity
\[
\lambda_{n+1}-\lambda_n=
\frac{s^{n+1}e^{-s}-(s+L)^{n+1}e^{-(s+L)}}{(n+1)!}.
\]
For \(s>0\), its sign is the sign of \(\rho(s,L)-(n+1)\). The eigenvalue sequence therefore increases strictly until the first index at or above \(\rho\), then decreases strictly, with one and only one adjacent equality when \(\rho\) is a positive integer. This gives every maximizing index and the entire optimal eigenspace, since the Hermite basis is complete. For \(s=0\) the displayed difference is strictly negative for every \(n\ge0\), proving the endpoint case.

**Transitions and non-smoothness.** The function \(\rho(s,L)\) is strictly increasing and continuous from \(0\) to \(+\infty\) as \(s\) ranges from \(0\) to \(+\infty\). Hence every positive integer is crossed exactly once, at the stated \(s_n(L)\). Let \(D(s)=\lambda_{n+1}(s,L)-\lambda_n(s,L)\), and take \(s=s_n(L)\). At that crossing the two endpoint factors in the difference formula coincide. Their derivative difference gives
\[
D'(s_n)=\frac{L\,s_n^{n}e^{-s_n}}{n!(s_n+L)}>0.
\]
The norm equals \(\lambda_n\) immediately to the left and \(\lambda_{n+1}\) immediately to the right. Thus its derivative has the claimed positive jump, with no other non-smooth points.

**Sharp correction and its cluster set.** Put \(m=\lfloor\rho(s,L)\rfloor\) and \(\delta=m-s\). For each fixed \(L>0\), the elementary expansion \(\rho=s+L/2+O_L(s^{-1})\) shows that \(\delta\) stays bounded as \(s\to\infty\). Uniform Stirling expansion, valid for bounded \(\delta\) and \(0\le v\le L\), gives
\[
\frac{(s+v)^m e^{-(s+v)}}{m!}
=\frac1{\sqrt{2\pi s}}\left(1-\frac{\delta/2+(v-\delta)^2/2+1/12}{s}+O_L(s^{-2})\right).
\]
The average of the coefficient over \(0\le v\le L\) is exactly
\[
\frac1L\int_0^L\left(\frac\delta2+\frac{(v-\delta)^2}{2}+\frac1{12}\right)dv
=C_L+\frac12\left(\delta-\frac{L-1}{2}\right)^2.
\]
Since \(\delta=L/2-\vartheta(s,L)+O_L(s^{-1})\), substitution proves the norm expansion with a uniform \(O_L(s^{-2})\) error in the bracket. This remains valid at crossings, where either tied Hermite order computes the norm.

Finally \(\rho(s,L)\) is continuous, strictly increasing, and unbounded. For any \(u\in[0,1)\), there are radii \(s_j\to\infty\) with \(\rho(s_j,L)=j+u\); the endpoints are attained as limits when \(u\to1\). Hence the squared fractional-part term takes precisely all subsequential limiting values in \([0,1/8]\), proving the claimed interval and excluding a constant second coefficient.

## Verification

The accompanying standalone `verify_annulus.py` uses only Python's standard library. It numerically integrates the *independently evaluated Poisson density* with composite Simpson quadrature for representative widths, radii, and Hermite indices, and checks the adjacent-difference identity, exact transition equations, switch-eigenvalue equality, derivative-jump formula and the stated large-radius approximation. Running `python verify_annulus.py` prints `ANNULUS_MODE_CHECKS_PASS 1320`. The analytical argument above, not the finite numerical tests, establishes all-radius and all-index conclusions.

## Relationship to prior work

Daubechies established Hermite diagonalization for radial-Gaussian localization. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets* (first public July 1, 2019), Section 3.1, studies precisely the unit-area annulus. Its stated result confines the largest eigenvalue to one of two adjacent modes and estimates its norm to leading order with an error at order \(R^{-3}\). The present result resolves the exact competition, gives all switch radii and complete maximizing eigenspaces for arbitrary annular area, and identifies the full oscillatory coefficient of the previously bounded next-order term. The **known diagonalization, finite-area integral formula, and leading asymptotic are prior work**, not claimed as new.

Galbis (first preprint February 3, 2021) proves a general norm *upper bound* for radial Fock Toeplitz symbols; this bound does not specify the maximizing Hermite mode or annular switches. Marceca and Romero (first preprint April 13, 2021) establish eigenvalue-count deviations for STFT concentration; their results do not give the exact mode and next-order norm at a fixed-area annulus. Nicola and Tilli (first preprint July 18, 2022) obtain sharp *global* norm bounds under constraints on the symbol, with ball-type extremizers, rather than this one-annulus mode classification.

## Limitations

The problem is for a one-dimensional signal with normalized Gaussian window and circular annuli of fixed positive area. It gives no eigenvector classification for other windows, nonradial regions, or higher-dimensional phase spaces. The asymptotic error bound assumes that \(L\) is fixed; it is not uniform when \(L\) grows with \(s\). The exact switching law follows simply from the special radial-Gaussian spectral representation, and a possibly unlocated equivalent result for uniformly mixed Poisson laws or Fock Toeplitz operators remains a historical-priority risk. Independent mathematical validation has not been performed.

## References

1. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets*, first public 2019-07-01, arXiv:1907.00848 (especially Sections 2.3 and 3.1); published as *... I*, Journal of Fourier Analysis and Applications 26 (2020), article 47. https://arxiv.org/abs/1907.00848 ; https://doi.org/10.1007/s00041-020-09751-9
2. I. Daubechies, *Time-frequency localization operators: A geometric phase space approach*, IEEE Trans. Information Theory 34 (1988), 605–612 (foundational diagonalization).
3. A. Galbis, *Norm estimates for selfadjoint Toeplitz operators on the Fock space*, arXiv:2102.02031, first public 2021-02-03. https://arxiv.org/abs/2102.02031
4. F. Marceca and J. L. Romero, *Spectral deviation of concentration operators for the short-time Fourier transform*, arXiv:2104.06150, first public 2021-04-13. https://arxiv.org/abs/2104.06150
5. F. Nicola and P. Tilli, *The norm of time-frequency and wavelet localization operators*, arXiv:2207.08624, first public 2022-07-18. https://arxiv.org/abs/2207.08624
