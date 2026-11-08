# Periodic-Parseval bound for randomized Matérn Fourier covariance matrices

## Finding

The equispaced Fourier Matérn approximation has a provable root-mean-square truncation rate of \(2\nu+d/2\), rather than the uniform-kernel rate \(2\nu\), for **every bounded sampling density** on the unit cube. More precisely, under the definitions below, for any independent \(X,Y\) with common density \(\rho\),
\[
q:=\left(\mathbb E\bigl|k_{h,m}(X-Y)-k(X-Y)\bigr|^2\right)^{1/2}
\le a_h+C_{d,\nu}\sqrt R\,\ell^{-2\nu}(hm)^{-(2\nu+d/2)},
\tag{1}
\]
where \(R=\|\rho\|_\infty\), \(a_h\) is the exact uniform periodic-alias bound defined below, and
\[
C_{d,\nu}=\frac{\Gamma(\nu+d/2)}{\pi^{d/2}\Gamma(\nu)}
\left(\frac{\nu}{2\pi^2}\right)^\nu
\sqrt{\frac{2^{d+1}d\,5^{d-1}}{4\nu+d}}.
\tag{2}
\]
This bound holds for **every** integer dimension \(d\ge1\), smoothness \(\nu\ge1/2\), length scale \(\ell>0\), mesh width \(0<h\le1\), and integer cutoff \(m\ge1\), with no smoothness hypothesis on \(\rho\).

For \(N\ge2\) independent points \(X_1,\ldots,X_N\) with density \(\rho\), define the true and approximate covariance matrices \(K_{ij}=k(X_i-X_j)\) and \(\widetilde K_{ij}=k_{h,m}(X_i-X_j)\). With \(e(z)=k_{h,m}(z)-k(z)\), their **exact**, finite-sample mean-square relation is
\[
\frac{\mathbb E\|\widetilde K-K\|_F^2}{N^2}
=\left(1-\frac1N\right)q^2+\frac{|e(0)|^2}{N}.
\tag{3}
\]
Put \(M=\sup_{z\in[-1,1]^d}|e(z)|\). If \(M>0\), then, for every \(s>0\),
\[
\Pr\!\left\{\frac{\|\widetilde K-K\|_F^2}{N^2}>
\left(1-\frac1N\right)(q^2+s)+\frac{|e(0)|^2}{N}\right\}
\le \exp\!\left(-\frac{Ns^2}{2M^4}\right).
\tag{4}
\]
For every **fixed** choice of kernel, density, \(h\), and \(m\),
\[
N^{-1}\|\widetilde K-K\|_F\longrightarrow q
\qquad\text{almost surely as }N\to\infty.
\tag{5}
\]
Consequently, if the alias term is at most a fixed multiple of the right-hand algebraic truncation term, the conjectured root-mean-square \((hm)^{-2\nu-d/2}\) scale holds with an explicit constant and high probability for sufficiently large \(N\). No claim of uniformity in simultaneously varying \(N,h,m,\ell\) is made.

## Assumptions and scope

Use the Fourier convention
\[
\widehat k(\xi)=\int_{\mathbb R^d}k(z)e^{-2\pi i\langle\xi,z\rangle}\,dz.
\]
The unit-variance stationary Matérn covariance, with range parameter \(\ell\), has the Fourier representation
\[
\widehat k(\xi)=
\frac{2^d\pi^{d/2}(2\nu)^\nu\Gamma(\nu+d/2)}{\Gamma(\nu)}
\frac{\ell^d}{(2\nu+4\pi^2\ell^2\|\xi\|_2^2)^{\nu+d/2}}.
\tag{6}
\]
Equivalently its spatial form is \(k(z)=2^{1-\nu}\Gamma(\nu)^{-1}(\sqrt{2\nu}\|z\|_2/\ell)^\nu K_\nu(\sqrt{2\nu}\|z\|_2/\ell)\), with \(k(0)=1\) by continuity. Formula (6), which fixes the normalization unambiguously, can also be checked by integrating it over all \(\mathbb R^d\).

Let \(J_m=\{-m,\ldots,m\}^d\) and define
\[
k_{h,m}(z)=h^d\sum_{j\in J_m}\widehat k(hj)e^{2\pi ih\langle j,z\rangle}.
\]
Define the periodization \(P_h(z)=\sum_{q\in\mathbb Z^d}k(z+q/h)\), its alias \(A_h(z)=P_h(z)-k(z)\), and
\[
a_h=\sup_{z\in[-1,1]^d}|A_h(z)|.
\]
Matérn exponential spatial decay implies \(a_h<\infty\). The spectral coefficients are absolutely summable for \(\nu>0\), so all Fourier decompositions and integrations below are justified. The point density \(\rho\) is merely measurable, nonnegative, supported on \([0,1]^d\), integrates to one, and satisfies \(\|\rho\|_\infty=R<\infty\). An independent sample is required; deterministic or strongly dependent locations are not covered by the probabilistic claims.

## Proof

**1. Exact alias–tail decomposition.** Poisson summation, valid here by integrability and sufficient decay of \(k\) and \(\widehat k\), gives
\[
P_h(z)=h^d\sum_{j\in\mathbb Z^d}\widehat k(hj)e^{2\pi ih\langle j,z\rangle}.
\]
Write \(T_{h,m}(z)=h^d\sum_{j\notin J_m}\widehat k(hj)e^{2\pi ih\langle j,z\rangle}\). Then \(e(z)=A_h(z)-T_{h,m}(z)\). The sign is unimportant for the norm but is recorded to avoid ambiguity.

**2. Periodic-Parseval localization.** The tail \(T_{h,m}\) has period \(1/h\) in each coordinate. For any \(1/h\)-periodic square-integrable \(f\), a side-one cube can be contained in a full period cube whenever \(h\le1\); its nonnegative squared integral is at most the full-period integral. Covering \([-1,1]^d\) by \(2^d\) side-one cubes and using orthogonality on a period gives
\[
\int_{[-1,1]^d}|T_{h,m}(z)|^2\,dz
\le2^d\int_{[0,1/h]^d}|T_{h,m}(z)|^2\,dz
=2^d h^d\sum_{j\notin J_m}|\widehat k(hj)|^2.
\tag{7}
\]
Here full-period Parseval gives \(\int_{[0,1/h]^d}|T_{h,m}|^2=h^{-d}\sum|h^d\widehat k(hj)|^2=h^d\sum|\widehat k(hj)|^2\). This localization does **not** require Fourier decay or smoothness of the density.

**3. A bounded density controls the difference measure.** The density of \(X-Y\) is \(v(z)=\int\rho(x)\rho(x-z)\,dx\), extended by zero, so it is supported on \([-1,1]^d\) and satisfies \(v(z)\le R\int\rho(x-z)\,dx\le R\). Consequently
\[
\mathbb E|T_{h,m}(X-Y)|^2
\le 2^d R h^d\sum_{j\notin J_m}|\widehat k(hj)|^2.
\tag{8}
\]

**4. Squared spectral lattice tail.** From (6), for every nonzero \(\xi\),
\[
0\le\widehat k(\xi)\le B_{d,\nu}\ell^{-2\nu}\|\xi\|_2^{-(2\nu+d)},\qquad
B_{d,\nu}=\frac{\Gamma(\nu+d/2)}{\pi^{d/2}\Gamma(\nu)}\left(\frac{\nu}{2\pi^2}\right)^\nu.
\tag{9}
\]
For any \(m\ge1\), the elementary half-space lattice bound of Barnett–Greengard–Rachh, Lemma 4, applied with exponent parameter \(2\nu+d/2\), yields
\[
\sum_{j\notin J_m}\|j\|_2^{-(4\nu+2d)}
\le\frac{2d\,5^{d-1}}{4\nu+d}\,m^{-(4\nu+d)}.
\tag{10}
\]
Combining (8)–(10) gives
\[
\left(\mathbb E|T_{h,m}(X-Y)|^2\right)^{1/2}
\le C_{d,\nu}\sqrt R\,\ell^{-2\nu}(hm)^{-(2\nu+d/2)}.
\tag{11}
\]
By \(|A_h(z)|\le a_h\) on the support of \(X-Y\) and the triangle inequality in \(L^2\), (1) follows.

**5. Matrix identity and probability.** There are exactly \(N\) diagonal matrix entries with deterministic error \(e(0)\), and \(N(N-1)\) off-diagonal entries with individual second moment \(q^2\). Linearity of expectation proves (3), with no independence assumption between different matrix entries.

For concentration let \(U_N=[N(N-1)]^{-1}\sum_{i\ne j}|e(X_i-X_j)|^2\). Changing just one sampling location can alter \(U_N\) by at most \(2M^2/N\). The bounded-differences inequality therefore yields
\[
\Pr\{U_N-q^2>s\}\le\exp\left(-\frac{Ns^2}{2M^4}\right).
\]
The identity \(N^{-2}\|\widetilde K-K\|_F^2=(1-1/N)U_N+|e(0)|^2/N\) proves (4). Applying the same inequality to both tails and the first Borel–Cantelli lemma for each fixed rational tolerance yields \(U_N\to q^2\) almost surely; taking nonnegative square roots proves (5). If \(M=0\), all errors are zero and the conclusions hold trivially. This completes the proof.

## Verification

The accompanying `verify.py` uses only the Python standard library. Running `python verify.py` executes finite checks of the Fourier spectral normalization for the one-dimensional \(\nu=1/2\) and \(\nu=3/2\) cases, the spectral-envelope inequality in dimensions one through three, periodic-Parseval localization on one- and two-dimensional trigonometric polynomials, and the exact diagonal/off-diagonal expectation combinatorics. It does not certify the infinite lattice sum, Poisson summation or the concentration inequality; those are proved above using analytic identities and standard inequalities. The recorded replay passed 171 finite assertions.

## Relationship to prior work

Barnett, Greengard and Rachh, *Uniform approximation of common Gaussian process kernels using equispaced Fourier grids* (2023 preprint; 2024 journal), give the alias–tail decomposition and a uniform Matérn approximation rate of order \((hm)^{-2\nu}\), and explicitly formulate the improved covariance-matrix rate \((hm)^{-2\nu-d/2}\) for iid locations with bounded density as Conjecture 9. Their Section 4 proposes a Fourier-autocorrelation heuristic and describes a rigorous proof as open. This note establishes the precise bounded-density bound via a localized periodic Parseval argument, gives explicit constants, and adds finite-sample diagonal and concentration formulas. It uses their previously proved half-space lattice inequality, rather than claiming that lemma as new.

Greengard, Rachh and Barnett, *Equispaced Fourier representations for efficient Gaussian process regression from a billion data points* (2022–2023), provide the computational scheme, uniform kernel error control, and a heuristic grid prescription; the full text does not prove the bounded-density mean-square rate. Bachmayr, Graham, Nguyen and Scheichl, *Unified Analysis of Periodization-Based Sampling Methods for Matérn Covariances* (2019), concerns periodization for random-field sampling and eigenvalue decay, not the stated iid off-grid covariance-matrix result; only its abstract and available descriptive information were inspected, so possible broader implications remain a publication-precedence risk.

## Limitations

The probabilistic theorem applies to iid sample locations with a bounded density on a unit cube; unbounded or singular sampling laws are not covered. The explicit rate is for **truncation**, and the separately controlled alias term must be comparably small for the conjectured total-error scaling. The high-probability and almost-sure statements take \(N\to\infty\) with the numerical parameters fixed; they do not assert a uniform triangular-array result if \(h,m,\ell\) vary with \(N\). The non-negligible finite-\(N\) diagonal term may dominate when \(N\) is too small. No numerical floating-point roundoff, posterior-prediction, spectral-norm optimality, or sharp-constant theorem is claimed. Publication precedence beyond inspected primary literature is not independently certified.

## References

1. A. H. Barnett, P. R. Greengard, M. Rachh, *Uniform approximation of common Gaussian process kernels using equispaced Fourier grids*, arXiv:2305.11065v1, first public 2023-05-18, especially Proposition 1, Lemma 4, Theorem 5 and Conjecture 9, https://arxiv.org/html/2305.11065v1 . Journal version: *Applied and Computational Harmonic Analysis* 71 (2024), 101640.
2. P. R. Greengard, M. Rachh, A. H. Barnett, *Equispaced Fourier representations for efficient Gaussian process regression from a billion data points*, arXiv:2210.10210v2, https://arxiv.org/html/2210.10210v2 .
3. M. Bachmayr, I. G. Graham, V. K. Nguyen, R. Scheichl, *Unified Analysis of Periodization-Based Sampling Methods for Matérn Covariances*, arXiv:1905.13522, https://arxiv.org/abs/1905.13522 .
