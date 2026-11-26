# Wishart trace–logdet alignment has an exact aspect-ratio law

## Finding

Let
\[
W\sim W_p(\nu,\Sigma)
\]
be a real central Wishart matrix with positive-definite scale matrix \(\Sigma\) and real degrees of freedom
\[
\nu>p-1.
\]
Write
\[
Q=\operatorname{tr}(\Sigma^{-1}W),
\qquad
L=\log\det W,
\]
and let \(\psi_1\) denote the trigamma function. Define
\[
V_{\nu,p}=\sum_{j=1}^{p}\psi_1\!\left(\frac{\nu-j+1}{2}\right).
\]

Then the matrix/log-volume covariance is exactly
\[
\boxed{
\operatorname{Cov}(W,L)=2\Sigma,
}
\tag{1}
\]
where covariance in (1) is understood entrywise. Consequently, for every deterministic symmetric matrix \(A\),
\[
\boxed{
\operatorname{Cov}(\operatorname{tr}(AW),L)
=2\operatorname{tr}(A\Sigma).
}
\tag{2}
\]
In particular,
\[
\boxed{
\operatorname{Cov}(Q,L)=2p.
}
\tag{3}
\]

The exact variances are
\[
\operatorname{Var}(Q)=2\nu p
\]
and
\[
\operatorname{Var}(L)=V_{\nu,p},
\]
so
\[
\boxed{
\operatorname{Corr}(Q,L)
=
\sqrt{\frac{2p}{\nu V_{\nu,p}}}.
}
\tag{4}
\]

Equation (4) gives a universal aspect-ratio law. If
\[
\frac{p}{\nu}\longrightarrow r\in(0,1),
\]
then
\[
\boxed{
\operatorname{Corr}(Q,L)
\longrightarrow
c(r):=
\sqrt{\frac{r}{-\log(1-r)}}.
}
\tag{5}
\]
The function \(c\) is strictly decreasing on \((0,1)\), with endpoint limits
\[
c(r)\longrightarrow1\quad(r\downarrow0),
\qquad
c(r)\longrightarrow0\quad(r\uparrow1).
\]
More generally, along any sequence with \(p/\nu\to0\), the correlation tends to \(1\), whereas along any sequence with \(p/\nu\to1\), it tends to \(0\).

Thus standardized total Mahalanobis scatter and log generalized variance are asymptotically almost the same fluctuation in the thin-dimensional regime, retain an explicit nontrivial correlation at every fixed proportional aspect ratio, and decorrelate at the square boundary.

## Assumptions and scope

The Wishart convention is the density on positive-definite \(p\times p\) real symmetric matrices
\[
f_{\nu,\Sigma}(W)
=
\frac{|W|^{(\nu-p-1)/2}
\exp\{-\operatorname{tr}(\Sigma^{-1}W)/2\}}
{2^{\nu p/2}|\Sigma|^{\nu/2}\Gamma_p(\nu/2)}.
\]
The parameter condition \(\nu>p-1\) is exactly the nonsingular real-Wishart range for this density. Integer \(\nu\) gives the ordinary Gaussian scatter-matrix model, but the proof of (1)--(4) does not require integer degrees of freedom.

The whitening in \(Q\) is deliberate: it removes the population eigenvalue geometry and isolates the dimension/sample-size effect. For the unwhitened trace, (2) supplies the corresponding covariance immediately.

## Proof

For real \(s\) in a neighborhood of zero satisfying \(\nu+2s>p-1\), determinant-power tilting gives
\[
\frac{|W|^s f_{\nu,\Sigma}(W)}{\mathbb E_{\nu,\Sigma}|W|^s}
=
f_{\nu+2s,\Sigma}(W).
\tag{6}
\]
Indeed, multiplication by \(|W|^s\) changes only the determinant exponent in the Wishart density; the normalizing constant becomes that of degrees of freedom \(\nu+2s\).

Let \(\mathbb E_s\) denote expectation under the tilted law in (6). Since a Wishart mean is
\[
\mathbb E_s W=(\nu+2s)\Sigma,
\tag{7}
\]
differentiating (7) at \(s=0\) yields
\[
\left.\frac{d}{ds}\mathbb E_s W\right|_{s=0}=2\Sigma.
\tag{8}
\]
On the other hand, differentiating a normalized exponential tilt gives
\[
\left.\frac{d}{ds}\mathbb E_s W\right|_{s=0}
=
\operatorname{Cov}(W,\log|W|).
\tag{9}
\]
The differentiation is legitimate because (6) is valid on an open interval around zero. Equations (8)--(9) prove (1), and taking the trace after multiplication by \(A\) proves (2). Setting \(A=\Sigma^{-1}\) gives (3).

For the variance terms, whiten
\[
U=\Sigma^{-1/2}W\Sigma^{-1/2}\sim W_p(\nu,I).
\]
Its trace has Laplace transform
\[
\mathbb E e^{-t\operatorname{tr}U}
=(1+2t)^{-\nu p/2},
\]
so
\[
Q=\operatorname{tr}U\sim\chi^2_{\nu p}
\]
and therefore
\[
\operatorname{Var}(Q)=2\nu p.
\tag{10}
\]

Bartlett decomposition gives
\[
L-\log|\Sigma|
\stackrel{d}{=}
\sum_{j=1}^{p}\log Z_j,
\qquad
Z_j\ \text{independent},
\quad
Z_j\sim\chi^2_{\nu-j+1}.
\]
Since
\[
\operatorname{Var}(\log\chi^2_k)=\psi_1(k/2),
\]
we obtain
\[
\operatorname{Var}(L)=V_{\nu,p}.
\tag{11}
\]
Combining (3), (10), and (11) proves (4).

For proportional growth with \(p/\nu\to r\in(0,1)\), the trigamma expansion
\[
\psi_1(x)=\frac1x+O(x^{-2})
\]
is uniform over the arguments in (11), because they are bounded below by a positive multiple of \(\nu\). Hence
\[
V_{\nu,p}
=
2\sum_{j=1}^{p}\frac1{\nu-j+1}+o(1)
\longrightarrow
-2\log(1-r).
\tag{12}
\]
Substitution in (4) gives (5).

If \(p/\nu\to0\), the same expansion gives
\[
V_{\nu,p}\sim\frac{2p}{\nu},
\]
so (4) tends to one. If \(p/\nu\to1\), the elementary lower bound
\[
\psi_1(x)>\frac1x
\]
gives
\[
V_{\nu,p}
>
2\sum_{j=1}^{p}\frac1{\nu-j+1},
\]
and the sum diverges because \((\nu-p+1)/\nu\to0\). Thus (4) tends to zero.

Finally,
\[
\frac{d}{dr}\frac{r}{-\log(1-r)}<0
\qquad(0<r<1),
\]
because
\[
\frac{r}{1-r}>-\log(1-r).
\]
Therefore \(c(r)\) is strictly decreasing.

## Verification

The proof of the finite identity is symbolic and does not rely on simulation. The accompanying checker independently evaluates the joint transform
\[
\mathbb E\left[|U|^s e^{t\operatorname{tr}U}\right]
=
2^{ps}
\frac{\Gamma_p(\nu/2+s)}{\Gamma_p(\nu/2)}
(1-2t)^{-p(\nu/2+s)}
\]
for a grid of dimensions and degrees of freedom. Mixed finite differences recover the covariance \(2p\), while pure second differences recover \(2\nu p\) and the trigamma sum. It also checks the exact correlation range and the three aspect-ratio regimes.

The finite numerical replay is supplementary. The all-parameter proof is (6)--(12).

## Relationship to prior work

Cai, Liang, and Zhou study the law and estimation of the log determinant of a Gaussian sample covariance matrix. Their full public manuscript proves the Bartlett decomposition of the log determinant, gives its exact trigamma variance, and derives high-dimensional logdet central limit theorems. A targeted full-text search of that manuscript finds no occurrence of the trace statistic, so it does not state the mixed finite covariance (1)--(3) or the exact correlation (4). Their first public arXiv version dates from 2013-09-02 and lists Primary MSC 62H12 and 62H10.

Letac and Massam compute a broad class of invariant polynomial moments of Wishart matrices. Their stated scope is polynomial invariants and powers of the matrix and its inverse; the logarithmic determinant mixed moment in (1)--(3) is not among the stated polynomial moment family.

Bai and Silverstein's general central limit theorem for linear spectral statistics is substantially broader asymptotically. In the proportional regime away from the hard edge, applying a joint linear-spectral-statistic CLT to the functions \(x\) and \(\log x\) can in principle cover an asymptotic covariance statement after evaluating its covariance functional. The exact finite matrix identity (1), its arbitrary linear-functional form (2), and the one-formula interpolation through the thin and hard-edge endpoint regimes are not consequences of an asymptotic statement alone. This broader theorem is therefore a genuine residual coverage risk for the interior limit (5), not for the finite identity.

Searches under the aliases “trace”, “total scatter”, “log determinant”, “log generalized variance”, “generalized variance”, “Wishart”, and “sample covariance” did not locate a source stating the exact finite covariance or correlation formula.

## Limitations

The finding is for the central real Wishart family. Complex Wishart normalization changes the constants, and noncentral Wishart laws do not obey the determinant-power shift (6) in this simple form.

The whitened trace \(Q\) uses the population scale \(\Sigma\), so it is an invariant theoretical scatter statistic rather than an immediately observable quantity when \(\Sigma\) is unknown.

The determinant-power tilt is a short exponential-family calculation. The value of the result is the exact mixed law and its aspect-ratio interpretation; the individual Wishart mean, Bartlett decomposition, trace variance, and logdet variance are classical.

General linear-spectral-statistic theory creates residual prior-work risk for the proportional interior limit, although it does not by itself supply the exact finite covariance identity.

## References

1. T. T. Cai, T. Liang, and H. H. Zhou, “Law of Log Determinant of Sample Covariance Matrix and Optimal Estimation of Differential Entropy for High-Dimensional Gaussian Distributions,” arXiv:1309.0482, first submitted 2013-09-02; *Journal of Multivariate Analysis* 137 (2015), 161–172, DOI 10.1016/j.jmva.2015.02.003.
2. G. Letac and H. Massam, “All Invariant Moments of the Wishart Distribution,” *Scandinavian Journal of Statistics* 31 (2004), 295–318, DOI 10.1111/j.1467-9469.2004.01-043.x.
3. Z. D. Bai and J. W. Silverstein, “CLT for Linear Spectral Statistics of Large-Dimensional Sample Covariance Matrices,” *Annals of Probability* 32 (2004), 553–605, DOI 10.1214/AOP/1078415845.
