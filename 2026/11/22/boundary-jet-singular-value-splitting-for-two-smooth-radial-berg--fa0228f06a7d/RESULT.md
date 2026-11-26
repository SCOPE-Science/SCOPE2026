# Boundary-jet singular-value splitting for two smooth radial Bergman Hankel channels

## Finding

Let \(\alpha>-1\), let \(\phi_1,\phi_2\in C^3([0,1];\mathbb C)\), and put \(h_i(t)=t\phi_i(t)\). On the standard weighted analytic Bergman space \(A^2_\alpha(\mathbb D)\), consider the row of big Hankel operators
\[
\mathcal R(f_1,f_2)=(I-P_\alpha)\{\overline z\phi_1(|z|^2)f_1+\overline z\phi_2(|z|^2)f_2\}.
\]
Define the boundary derivative vector \(v=(h_1'(1),h_2'(1))\) and its second-jet determinant \(\Delta=h_1'(1)h_2''(1)-h_2'(1)h_1''(1)\). Assume \(\Delta\ne0\). For every output angular frequency \(n\ge0\), \(\mathcal R\) has exactly two positive singular values \(\sigma_{n,+}\ge\sigma_{n,-}\). With \(s=\alpha+1\),
\[
\boxed{\lim_{n\to\infty}n\sigma_{n,+}=\sqrt{s}\,\|v\|_2,\qquad
\lim_{n\to\infty}n^2\sigma_{n,-}=\frac{|\Delta|}{\|v\|_2}\sqrt{\frac{s(s+1)}2}.}
\]
More precisely both limits have relative error \(O(n^{-1})\) with constants depending on the fixed parameters and symbols. The row is compact and belongs to \(\mathcal S_p\) exactly for \(p>1\). Define the lower-channel part by retaining the lower singular mode in each nonnegative angular-frequency block with \(\sigma_{n,-}<\sigma_{n,+}\), and setting it to zero at tied blocks and at frequency \(-1\). Ties can occur only at finitely many blocks. With this convention the lower-channel part belongs to \(\mathcal S_p\) exactly for \(p>1/2\). At the two respective critical exponents the blockwise logarithmic masses are
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^N\sigma_{n,+}=\sqrt{s}\,\|v\|_2,\qquad
\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^N\sigma_{n,-}^{1/2}
=\left(\frac{|\Delta|}{\|v\|_2}\sqrt{\frac{s(s+1)}2}\right)^{1/2}.
\]
On every untied nonnegative block the lower-channel operator is the row composed with the spectral projection of its domain Gram operator onto the lower eigenvalue. An equal pair has no distinguished rank-one spectral projection. The lower-channel operator is not claimed to equal a fixed linear combination of the two original Hankel operators.

For a concrete nonpolynomial pair \(\phi_1(t)=1\), \(\phi_2(t)=e^{t-1}\), both boundary-jet hypotheses hold and the constants become
\[
\lim_{n\to\infty}n\sigma_{n,+}=\sqrt{5(\alpha+1)},\qquad
\lim_{n\to\infty}n^2\sigma_{n,-}
=\frac3{\sqrt5}\sqrt{\frac{(\alpha+1)(\alpha+2)}2}.
\]
Thus the second spectral scale detects boundary curvature not seen by the dominant scalar Hankel singular-value estimate.

## Assumptions and scope

Take normalized weighted area \(d\nu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha dA(z)/\pi\). The orthogonal projection onto analytic \(A^2_\alpha\subset L^2(\nu_\alpha)\) is \(P_\alpha\). The row \(\mathcal R:A^2_\alpha\oplus A^2_\alpha\to L^2(\nu_\alpha)\ominus A^2_\alpha\) is bounded because both symbols are bounded. The real variable \(t=|z|^2\) lies in \([0,1]\). For complex symbols, all covariances and Gram matrices are Hermitian, and \(\Delta\) is interpreted through its complex modulus. No assertion is made uniformly over changing symbols or weights. The \(C^3\) assumption permits a globally bounded cubic Taylor remainder. The singular-value branches are indexed by output Fourier angular frequency, not by global decreasing order.

## Proof

**1. Exact Fourier and covariance reduction.** Write \(\mu_m=\int_0^1 t^m(\alpha+1)(1-t)^\alpha\,dt=\Gamma(\alpha+2)\Gamma(m+1)/\Gamma(m+\alpha+2)\), and use the orthonormal analytic monomials \(e_m(z)=z^m/\sqrt{\mu_m}\). For \(n\ge0\), both inputs \((e_{n+1},0)\) and \((0,e_{n+1})\) are mapped into angular Fourier frequency \(n\). Multiplication produces \(z^n h_i(t)/\sqrt{\mu_{n+1}}\). Its projection onto analytic functions is the multiple of \(z^n\) obtained by replacing \(h_i\) with its expectation under the beta probability measure
\[
 d\beta_n(t)=\frac{t^n(1-t)^\alpha}{B(n+1,\alpha+1)}\,dt.
\]
Therefore the squared-singular-value matrix at angular frequency \(n\) is exactly
\[
 G_n=\frac{\mu_n}{\mu_{n+1}}
 \left[\operatorname{Cov}_{\beta_n}(h_i,h_j)\right]_{i,j=1}^2,
 \quad \operatorname{Cov}(f,g)=\mathbb E(f\overline g)-\mathbb Ef\,\overline{\mathbb Eg}.
\]
The input degree zero gives a two-input block at angular frequency \(-1\). Its two output vectors are \(\overline z\phi_1(t)\) and \(\overline z\phi_2(t)\); the analytic projection is zero at this frequency. These vectors are linearly independent: a relation would give a linear dependence of the continuous \(\phi_i\) on \((0,1)\), and hence of the \(h_i\), contradicting \(\Delta\ne0\). This block has rank two and has no bearing on high-rank asymptotics. Distinct angular frequencies are orthogonal in both domain and target, so the block decomposition is exact. With \(\Delta\ne0\), \(h_1,h_2,1\) are linearly independent on an interval adjacent to \(1\); hence \(G_n\) is positive definite for every \(n\ge0\).

**2. Gamma boundary layer and its quantitative control.** Set \(U=1-t\) and \(X_n=nU\) under \(\beta_n\). Then \(U\) has the beta law with parameters \(s=\alpha+1\) and \(n+1\), and for every fixed integer \(r\ge0\),
\[
 \mathbb E X_n^r=n^r\frac{(s)_r}{(n+s+1)_r}=(s)_r+O(n^{-1}).
\]
In particular the centered first and second powers of \(X_n\) have uniformly bounded sixth moments and converge in Gram matrices to those of a gamma random variable \(X\) with shape \(s\) and unit scale. The ratio \(\mu_n/\mu_{n+1}=(n+s+1)/(n+1)=1+O(n^{-1})\). Taylor's theorem, using \(C^3\) on the closed interval, gives
\[
 h_i(1-U)=h_i(1)-v_iU+\frac{w_i}{2}U^2+O(U^3),\qquad w_i=h_i''(1).
\]
After centering and writing \(Y_n=X_n-\mathbb EX_n\), \(Z_n=X_n^2-\mathbb EX_n^2\), the two target vectors satisfy, in their beta-measure \(L^2\) spaces,
\[
 F_{i,n}:=h_i-\mathbb E h_i=-\frac{v_i}{n}Y_n+\frac{w_i}{2n^2}Z_n+E_{i,n},\qquad \|E_{i,n}\|_2=O(n^{-3}).
\]
The remainder bound follows from \(\mathbb E U^6=O(n^{-6})\), not from finite numerical testing.

**3. Larger eigenvalue and second exterior-power coefficient.** The Gram matrix has trace
\[
 \operatorname{tr}G_n=\frac{s(|v_1|^2+|v_2|^2)}{n^2}+O(n^{-3}).
\]
For its determinant use the Gram/exterior-product identity \(\det(\langle F_i,F_j\rangle)=\|F_1\wedge F_2\|^2\). The leading order-one terms of both vectors are collinear and cancel in the wedge; the first surviving term is
\[
 F_{1,n}\wedge F_{2,n}=
 -\frac{\Delta}{2n^3}(Y_n\wedge Z_n)+O_{\wedge^2L^2}(n^{-4}).
\]
For the limiting gamma variable, direct moment expansion gives
\[
 \operatorname{Var}(X)=s,\quad
 \operatorname{Cov}(X,X^2)=2s(s+1),\quad
 \operatorname{Var}(X^2)=2s(s+1)(2s+3),
\]
so \(\|Y\wedge Z\|^2=2s^2(s+1)\). The exact beta moments converge with \(O(n^{-1})\) errors. Including the scalar factor \((\mu_n/\mu_{n+1})^2\),
\[
 \det G_n=\frac{|\Delta|^2s^2(s+1)}{2n^6}+O(n^{-7}).
\]
If \(\lambda_{n,+}\ge\lambda_{n,-}\) are eigenvalues of \(G_n\), the trace and determinant imply
\[
 \lambda_{n,+}=\frac{s\|v\|_2^2}{n^2}+O(n^{-3}),\quad
 \lambda_{n,-}=\frac{|\Delta|^2s(s+1)}{2\|v\|_2^2n^4}+O(n^{-5}).
\]
Taking their positive square roots proves both stated branch limits and the relative \(O(n^{-1})\) bounds.

**4. Schatten classification and endpoints.** From the exact orthogonal Fourier decomposition, the nonzero singular-value multiset consists of the two branches for \(n\ge0\), plus two singular values from frequency \(-1\). The branches have asymptotic orders \(n^{-1}\) and \(n^{-2}\) with strictly positive constants, so their gap is positive for all sufficiently large \(n\). Ties at finite frequencies are possible: for \(\alpha=0\), \(h_1(t)=t\) and \(h_2(t)=\sqrt{15}(t^2-t)\), one has \(\Delta=2\sqrt{15}\) and \(G_0=I_2/6\) by the uniform-beta moments. The complete row is compact and its \(p\)-power singular sum converges exactly when \(p>1\). The lower-channel part with the stated convention omits at most finitely many lower singular modes and has its \(p\)-power sum finite exactly for \(p>1/2\). Harmonic-series summation, using the proved relative error bounds, gives the two logarithmic masses. Counting the branches above a threshold \(u\downarrow0\), the upper branch contributes asymptotically \(\sqrt{s}\|v\|_2/u\), whereas the lower branch contributes only \(O(u^{-1/2})\). Consequently the globally ordered singular values of the full row satisfy \(s_J(\mathcal R)\sim\sqrt{s}\|v\|_2/J\); those of the lower-channel part satisfy \(s_J\sim (|\Delta|/\|v\|_2)\sqrt{s(s+1)/2}/J^2\). Finite initial blocks do not affect either limit.

## Verification

The included `checks/check_jet.py` recomputes Gram determinants by exact rational beta moments for 89 positive integer degrees in the unweighted case and independently tests the nonpolynomial exponential pair with 65-digit beta integrals at degree 300 and two real weights. It passed 271 finite assertions. The exact determinant for the polynomial pair \(h_1(t)=t\), \(h_2(t)=t^2\) when \(\alpha=0\) is \(4/((n+3)^3(n+4)^2(n+5))\). These checks corroborate but do not replace the infinite-dimensional argument. Execute `python checks/check_jet.py` with `mpmath` installed.

## Relationship to prior work

Bourass–El-Fallah–Marrhich–Naqos (2021) analyze scalar Bergman Hankel singular values for anti-analytic holomorphic symbols, including the coordinate symbol. Keshavarzi–Wu (2024) give broad scalar Schatten criteria based on mean oscillation, but not the present exact two-channel singular branches. The published Laguerre covariance work (2026) gives an exact polynomial moment hierarchy for radial Toeplitz semicommutators \(u^i\), where \(u=1-|z|^2\). Its beta covariance calculation is relevant to the polynomial special case here. However its fixed polynomial symbol theorem neither contains arbitrary \(C^3\) nonpolynomial pairs nor a remainder theorem yielding the universal two-channel boundary-jet coefficient. The different published bianalytic Toeplitz commutator boundary-jet law (2026) uses order-two polyanalytic compression and has cubic rather than the present first-/second-order row-Hankel singular scales. These are related mechanisms, but not the same operators or implications.

## Limitations

The theorem is for the standard weighted analytic disk and two channels of the same angular order, with \(C^3\) radial amplitudes and \(\Delta\ne0\). It does not classify degenerate jets, arbitrary nonradial symbols, or higher-channel ranks. The lower-channel part is a spectral construction, not an independently specified single Hankel operator. A future generic polynomial-covariance or matrix Hankel theorem could subsume the statement; a bounded literature search cannot establish historical priority. The result has received no independent validation.

## References

1. M. Bourass, O. El-Fallah, I. Marrhich, H. Naqos, *On singular values of Hankel operators on Bergman spaces*, arXiv:2102.01743v1, first posted 2021-02-02, https://arxiv.org/abs/2102.01743 .
2. H. Keshavarzi, F. Wu, *Schatten class Hankel operators on weighted Bergman spaces induced by regular weights*, Bulletin des Sciences Mathématiques 191 (2024), 103402, https://doi.org/10.1016/j.bulsci.2024.103402 .
3. *Laguerre spectral branches of radial Bergman Toeplitz covariance defects*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-laguerre-spectral-branches-of-radial-bergman-toeplitz-covariance--36e9af76bb65 .
4. *A universal boundary-jet law for noncommuting radial poly-Bergman Toeplitz operators*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-universal-boundary-jet-law-for-noncommuting-radial-poly-bergma--db55972da5c1 .
