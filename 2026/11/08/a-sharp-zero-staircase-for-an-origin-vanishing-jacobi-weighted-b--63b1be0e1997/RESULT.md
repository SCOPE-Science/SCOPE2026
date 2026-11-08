# A sharp zero staircase for an origin-vanishing Jacobi-weighted Bergman kernel

## Finding

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). For every real \(\beta>-1\), equip analytic functions on \(\mathbb D\) with the Hilbert norm
\[
\|f\|_\beta^2=\frac1\pi\int_{\mathbb D}|f(z)|^2|z|^2(1-|z|^2)^\beta\,dx\,dy.
\]
Its reproducing kernel has the following exact formula, with \(s=z\overline w\) and \(N=\beta+2>1\):
\[
K_\beta(z,w)=\frac{\beta+1}{s}\bigl((1-s)^{-N}-1\bigr)\quad(s\ne0),
\qquad K_\beta(0,w)=(\beta+1)N.
\]
The exponent uses the analytic branch on \(\operatorname{Re}(1-s)>0\).

For each fixed \(w\in\mathbb D\) of modulus \(r\), **the exact number of zeros** of \(z\mapsto K_\beta(z,w)\) in \(\mathbb D\), counted with multiplicities, is
\[
\boxed{Z_\beta(r)=2\max\left\{0,\left\lceil\frac{\beta+2}{\pi}\arcsin\frac r2\right\rceil-1\right\}.}
\]
When \(r>0\), all of these zeros are simple and occur precisely at
\[
z_{k,\pm}=\frac{1-\exp\left(\pm 2\pi i k/(\beta+2)\right)}{\overline w},
\qquad k\in\mathbb Z_{>0},\quad
k<\frac{\beta+2}{\pi}\arcsin(r/2).
\]
The explicit upper bound on \(k\) keeps only the principal-angle branch; it implies \(k<(\beta+2)/6\) since \(r<1\). The kernel section at \(w=0\) is a nonzero constant.

Consequently the kernel is zero-free on all of \(\mathbb D\times\mathbb D\) **if and only if** \(-1<\beta\le4\). For \(\beta>4\), its scalar zero set in \(\{|s|<1\}\) contains exactly
\[
\boxed{2\left(\left\lceil\frac{\beta+2}{6}\right\rceil-1\right)}
\]
points, and a fixed kernel section is zero-free precisely for
\[
|w|\le 2\sin\left(\frac\pi{\beta+2}\right).
\]
At \(\beta=6j-2\), \(j\ge1\) an integer, a conjugate pair sits exactly on \(|s|=1\), hence is not included; each strict increase past that boundary value brings in two simple nonreal scalar zeros. For fixed \(0<r<1\), the corresponding basepoint-section transitions are at
\[
\beta=\frac{\pi j}{\arcsin(r/2)}-2\qquad(j\ge1).
\]
The distinction between the scalar kernel zeros and zeros in a fixed section is essential: a scalar zero \(s\) appears in the section at \(w\) exactly when \(|s|<|w|\).

## Assumptions and scope

The parameter is any real \(\beta>-1\), not merely a nonnegative integer. The weight \(|z|^2(1-|z|^2)^\beta\) is integrable and strictly positive away from the origin; monomials are orthogonal and point evaluations are bounded. Area measure is \(dx\,dy/\pi\), so there is no additional \(\pi\)-factor in the kernel formula. Both points \(z,w\) belong to the **open** disk. The zero count includes multiplicities, although all actual zeros are simple. A zero at \(|s|=1\) or \(|z|=1\) is excluded.

## Proof

**1. Norms and kernel.** For each integer \(n\ge0\), direct polar integration and the substitution \(u=|z|^2\) give
\[
\|z^n\|_\beta^2
=\int_0^1u^{n+1}(1-u)^\beta\,du
=B(n+2,\beta+1)
=\frac{\Gamma(n+2)\Gamma(\beta+1)}{\Gamma(n+\beta+3)}.
\]
Thus the reproducing kernel is the absolutely locally uniformly convergent series
\[
K_\beta(s)=\sum_{n\ge0}
\frac{\Gamma(n+\beta+3)}{\Gamma(n+2)\Gamma(\beta+1)}s^n.
\]
By the binomial series \((1-s)^{-N}=\sum_{j\ge0}\frac{\Gamma(N+j)}{\Gamma(N)\Gamma(j+1)}s^j\), its shifted nonconstant coefficients give
\[
K_\beta(s)=(\beta+1)\frac{(1-s)^{-N}-1}{s}
\]
for \(|s|<1\), with the removable value \(K_\beta(0)=(\beta+1)N>0\). Since \(\operatorname{Re}(1-s)>0\), the analytic power and its principal logarithm are unambiguous throughout this domain.

**2. All scalar zeros.** Suppose \(0<|s|<1\) and \(K_\beta(s)=0\). Then \(\exp[-N\operatorname{Log}(1-s)]=1\). Taking moduli shows \(|1-s|=1\). Since \(\operatorname{Arg}(1-s)\in(-\pi/2,\pi/2)\), the phase must be \(2\pi k/N\) for some nonzero integer \(k\); equivalently
\[
s=1-\exp(2\pi i k/N).
\]
The canceled solution \(k=0\) gives \(s=0\), not a kernel zero. Because \(|s|=2|\sin(\pi k/N)|\), the open-disk condition and the principal argument range together are exactly \(0<|k|<N/6\). Thus the scalar roots occur in conjugate pairs indexed by positive integers \(k<N/6\), giving the claimed total count. In particular no such integer exists iff \(N\le6\), equivalently \(\beta\le4\).

**3. Fixed-basepoint zero count and sharp transition.** For fixed \(w\ne0\), the map \(z\mapsto s=z\overline w\) is a complex-linear bijection from \(\mathbb D\) to \(\{|s|<r\}\). For an index \(k>0\), the latter membership is equivalent to
\[
2\sin(\pi k/N)<r
\quad\Longleftrightarrow\quad
k<\frac{N}{\pi}\arcsin(r/2).
\]
This equivalence is valid on the admissible principal-angle arc: since \(r<1\), it forces \(k<N/6<N/4\), on which the sine is increasing. The number of positive integers strictly less than a positive real \(x\) is \(\max\{0,\lceil x\rceil-1\}\). Each contributes the two signs, proving the exact displayed formula and the basepoint threshold. Setting \(r\uparrow1\) gives the scalar count; the limit is taken through \(r<1\), so roots exactly on the boundary are excluded. Solving the strict inequality for \(\beta\) gives the stated transition values.

**4. Simplicity.** At a nonzero scalar root \(s_0\), the numerator derivative is \(N(1-s_0)^{-N-1}\ne0\). Division by \(s_0\ne0\) preserves a simple zero. Multiplication by \(\overline w\ne0\) preserves multiplicity in the \(z\)-section. There are no other zeros.

## Verification

The standalone script `check.py` checks the closed kernel against separately computed beta-moment coefficients for representative nonintegral and integral \(\beta\), exact integer coefficient identities, explicit section zeros for multiple \(r\), strict-boundary counts, and the six-step scalar threshold. Execute `python3 check.py` using the standard Python library. Its expected terminal line is `RADIAL_BERGMAN_STAIRCASE_PASS checks=659`. These are finite corroborations; the argument above proves the infinite-parameter theorem.

For example \(\beta=5\) gives \(N=7\), exactly two scalar zeros with radius \(2\sin(\pi/7)\), and the section has those zeros precisely when \(|w|>2\sin(\pi/7)\). At \(\beta=10\), \(N=12\), the second pair is exactly on the scalar boundary and remains excluded. At \(\beta=11\), two interior conjugate pairs are present.

## Relationship to prior work

The standard radial Bergman moment expansion and the general principle that radial kernel sections have finitely many zeros appear in Perälä, *Vanishing Bergman Kernels on the Disk* (2017), including its Theorem 3.5. That paper studies generated weights and qualitative zero-count possibilities, not the complete two-variable count for the present explicit origin-depleted Jacobi family. Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space* (2022), analyzes weights formed from finite products of Blaschke factors; the boundary factor \((1-|z|^2)^\beta\) is not covered by that weight specification when \(\beta\ne0\).

Related classifications for Euclidean boundary-distance powers and lower fixed Jacobi orders concern different weights or a finite set of orders. They do not determine the full real-parameter zero staircase and basepoint-section phase diagram proved here. The derivation uses classical beta and binomial identities; no claim is made that those identities themselves are new.

## Limitations

The exact classification is for the single origin-vanishing factor \(|z|^2\) with arbitrary real boundary exponent, not for general origin powers \(|z|^{2a}\), nonradial weights, or higher-dimensional domains. The explicit algebraic count does not establish robustness under weight perturbations. The relation to any unlocated broader kernel formula could affect historical priority; no independent external mathematical audit has been performed.

## References

1. A. Perälä, *Vanishing Bergman Kernels on the Disk*, arXiv:1703.05976v1, first publicly posted 2017-03-17; especially Sections 1 and 3, Theorems 3.3 and 3.5. https://arxiv.org/abs/1703.05976
2. E. Miña-Díaz, *A representation for the reproducing kernel of a weighted Bergman space*, arXiv:2212.08118v1, first publicly posted 2022-12-15; Section 1 and Theorem 1.1. https://arxiv.org/abs/2212.08118
