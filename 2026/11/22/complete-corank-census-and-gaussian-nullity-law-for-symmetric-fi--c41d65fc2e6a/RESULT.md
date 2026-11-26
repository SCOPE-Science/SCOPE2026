# Gaussian nullity law for symmetric finite-field tridiagonal matrices

## Finding

Fix a prime power \(q\ge 2\). Let \(A_n\) be uniformly distributed over symmetric tridiagonal \(n\times n\) matrices over \(\mathbb F_q\), with all \(2n-1\) diagonal and subdiagonal entries independent and uniform, including zero. Set \(K_{n,q}=\dim_{\mathbb F_q}\ker A_n\) and
\[
\delta_q=q^2+q-1,\qquad \mu_q=\frac{1}{\delta_q},\qquad
\sigma_q^2=\frac{1}{\delta_q}-\frac{q^2-q+1}{\delta_q^3}>0.
\]
Then
\[
\mathbb E K_{n,q}=\mu_q n+O_q(1),\qquad
\operatorname{Var}(K_{n,q})=\sigma_q^2n+O_q(1),\qquad
\frac{K_{n,q}-\mu_q n}{\sigma_q\sqrt n}\xrightarrow{\mathrm{law}}\mathcal N(0,1).
\]
Thus the nullity has positive linear density and fluctuations of order \(\sqrt n\), unlike the tight nullity of the uniform full symmetric ensemble over the same field.

## Assumptions and scope

The field size is fixed as \(n\) tends to infinity, and the result includes characteristic two. Zero offdiagonal entries are essential: if all are conditioned to be nonzero, the nullity is at most one. The all-corank generating function below is a supporting corollary of the known invertible census and the decomposition at zeros; it is not asserted as a separate originality contribution.

## Proof

### From the invertible census to a corank generating function

Let \(S(z)\) count invertible matrices by dimension and let \(T(z)\) count all matrices by dimension, with the empty matrix counted once in both. The nonsingular counts of Martínez-Moro, Rodnit and Jitman (Theorem 2.1), with initial values \(q-1\) and \(q^2(q-1)\) at dimensions one and two, give
\[
S(z)=\frac{N(z)}{1-q(q-1)z-q^2(q-1)z^2},\qquad
N(z)=(1+(q-1)z)(1-q(q-1)z).
\]
Direct counting gives \(T(z)=1+qz/(1-q^2z)=(1-q(q-1)z)/(1-q^2z)\).

A matrix splits uniquely into a sequence of blocks at its zero offdiagonals. A block has nullity at most one: in a kernel vector, its first coordinate determines all the others by the rows with nonzero next offdiagonal. This includes singletons and uses no restriction on characteristic. Write \(B_0(z)\) and \(B_1(z)\) for the counting series for such blocks with nullity zero and one. The unique block decomposition and additivity of nullity give \(1/S=1-B_0\) and \(1/T=1-B_0-B_1\). Thus the full generating function for the unnormalized nullity polynomials \(Z_{n,q}(t)\), with \(Z_{0,q}=1\), is
\[
\begin{aligned}
\sum_{n\ge 0}Z_{n,q}(t)z^n
 &=\frac{1}{1-B_0(z)-tB_1(z)}
 =\frac{1}{(1-t)/S(z)+t/T(z)}\\
 &=\frac{N(z)}{1-(q(q-1)+t)z-q^2(q-1)z^2}.
\end{aligned}
\]
This identity holds formally for every fixed prime power \(q\). In particular, \(Z_{1,q}(t)=q-1+t\), \(Z_{2,q}(t)=q^2(q-1)+(q^2-1)t+t^2\), and for \(n\ge3\) the homogeneous recurrence has first coefficient \(q(q-1)+t\) and second coefficient \(q^2(q-1)\).

### Dominant root and fluctuation law

Set \(a(t)=q(q-1)+t\) and \(\lambda_\pm(t)=(a(t)\pm\sqrt{a(t)^2+4q^2(q-1)})/2\), taking the positive square root at \(t=1\). The roots there are \(q^2\) and \(-(q-1)\), so on a small complex neighborhood of 1 they are distinct, both nonzero, and \(|\lambda_- /\lambda_+|\le\rho<1\). Partial fractions (a constant polynomial part affects dimension zero only) give, for \(n\ge1\),
\[
Z_{n,q}(t)=c(t)\lambda_+(t)^n+d(t)\lambda_-(t)^n
\]
with analytic \(c,d\). At \(t=1\), \(Z_{n,q}(1)=q^{2n-1}\), so \(c(1)=1/q\). In a smaller neighborhood \(c\) has no zeros. For \(s\) complex close to zero the normalized moment generating function is therefore
\[
\mathbb E e^{sK_{n,q}}=q c(e^s)
\left(\frac{\lambda_+(e^s)}{q^2}\right)^n(1+O_q(\rho^n)),
\]
with analytic uniform error. The logarithmic error and its first two derivatives at zero are \(O_q(\rho^n)\) by Cauchy's estimate on a smaller disk.

Writing \(D(t)=\sqrt{a(t)^2+4q^2(q-1)}\), differentiation of the root equation gives \(\partial_t\log\lambda_+(t)=1/D(t)\) and \(\partial_t^2\log\lambda_+(t)=-a(t)/D(t)^3\). At \(t=1\), \(D(1)=\delta_q\) and \(a(1)=q^2-q+1\). Applying the chain rule at \(t=e^s\) gives the stated mean and variance coefficients; the variance is positive since \(\delta_q^2>q^2-q+1\). Expanding \(\log(\lambda_+(e^s)/q^2)\) at zero to second order and setting \(s=iu/(\sigma_q\sqrt n)\) gives the centered characteristic functions tending to \(e^{-u^2/2}\) for each real \(u\). The continuity theorem proves the Gaussian limit.

## Verification

`check_tridiagonal.py` builds matrices explicitly, computes rank by row elimination, and compares the finite nullity histograms with the supporting generating function. The recorded `check_output.txt` covers 9,887 matrices across 18 field-size and dimension pairs, including \(\mathbb F_4\). Those checks do not establish the large-dimension limit, which follows from the proof above.

## Relationship to prior work and limitations

Martínez-Moro, Rodnit and Jitman give the invertible counts for all prime powers in the same symmetric unrestricted tridiagonal ensemble, as well as prescribed-determinant results. The block-series identity above shows explicitly how their invertible counts and the total counts determine the positive-corank coefficients for this pattern. For \(q=2\), the connected-path rank distribution of Safarji, O'Brien and Quinlan (Theorem 2.2) gives an alternative starting point: it counts the two ranks of every all-nonzero-offdiagonal block, so the composition of those block counts recovers the unrestricted binary polynomial. Neither cited result states the Gaussian law with the mean and variance coefficients above. The asymptotic analysis concerns the uniform symmetric tridiagonal ensemble, not dense symmetric matrices, independent upper- and lower-diagonal entries, general zero patterns, finite chain rings, or a simultaneous limit in \(q\) and \(n\). An undiscovered ensemble-specific asymptotic comparison remains possible.

## References

1. E. Martínez-Moro, N. Rodnit and S. Jitman, *On the enumeration of symmetric tridiagonal matrices with prescribed determinant over commutative finite chain rings*, arXiv:2509.17719, §2.1, Theorems 2.1–2.2. https://arxiv.org/abs/2509.17719
2. B. Safarji, C. O'Brien and R. Quinlan, *The rank distribution of matrices representing graphs with a long induced path over the field of two elements*, arXiv:2509.10332, §2, Theorem 2.2. https://arxiv.org/abs/2509.10332
3. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, Annals of Probability 43 (2015), 1274–1314, §4. https://arxiv.org/abs/1211.0504
