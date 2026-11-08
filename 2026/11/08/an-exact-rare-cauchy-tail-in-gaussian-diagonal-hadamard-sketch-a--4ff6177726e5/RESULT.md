# An exact rare-Cauchy tail in Gaussian-diagonal Hadamard sketch-and-solve

## Finding

For every finite integer \(m\geq1\), a scalar least-squares instance with a unit-norm design and an orthogonal unit residual has an almost-surely unique Gaussian-diagonal Hadamard sketched solution \(\widehat x_m\), but

\[
\mathbb E|\widehat x_m|^p<\infty\quad\Longleftrightarrow\quad 0<p<1.
\]

Indeed, its law is a finite mixture with an **exact standard-Cauchy component of mass \(2^{1-m}\)**. For every \(m\ge2\), putting \(T_m=m/(2\sqrt{m-1})\), the entire far tail is exactly

\[
\Pr\{|\widehat x_m|>t\}=\frac{2^{2-m}}{\pi}\arctan(1/t),\qquad t\ge T_m.
\]

For \(m=1\) the same formula holds for all \(t>0\). In particular,

\[
\lim_{t\to\infty}t\Pr\{|\widehat x_m|>t\}=\frac{2^{2-m}}{\pi}.
\]

Thus every finite sampling budget has infinite expected absolute error and infinite mean-square error, notwithstanding the exponential decrease of the Cauchy-component probability with \(m\). This concerns the **Gaussian diagonal substituted into an ordinary row-subsampled Hadamard sketch**, not the separate balanced Gaussian-pooling method.

## Assumptions and scope

Fix an integer power of two \(n\ge2\) and an unnormalized \(n\times n\) Hadamard matrix \(H\). Let \(u=(e_1+e_2)/\sqrt2\) and \(r=(e_1-e_2)/\sqrt2\). The data are the single-column design \(A=u\) and response \(b=r\), so the original least-squares minimizer is exactly \(x^*=u^{\mathsf T}r=0\), \(\|A\|_2=\|b\|_2=1\), and \(A\) has full column rank.

For any finite integer \(m\ge1\), draw \(P\) by independently choosing \(m\) uniformly distributed Hadamard row indices **with replacement**. Independently draw \(D_\gamma=\operatorname{diag}(\gamma_1,\ldots,\gamma_n)\), with independent standard real Gaussians. Let \(S=m^{-1/2}PH D_\gamma\) and define \(\widehat x_m=\arg\min_{x\in\mathbb R}\|Sux-Sr\|_2^2\). These are exactly the ingredients of the natural Gaussian-diagonal alternative discussed in Song and Zhang (2026, Section 3), not the original sign-diagonal SRHT or their proposed Gaussian-pooling sketch.

Let \(\zeta_j\) be the product of the first two Hadamard signs in sampled row \(j\), and define \(\rho=m^{-1}\sum_{j=1}^m\zeta_j\). The \(\zeta_j\) are independent uniform signs, independent of the Gaussian diagonal. Thus

\[
\Pr\{\rho=(2j-m)/m\}=2^{-m}\binom mj,\quad j=0,\ldots,m.
\]

## Proof

**Step 1: exactly identify the sketched coefficient and its denominator.** On the first two coordinates, the random Gram matrix \(S^{\mathsf T}S\) has block

\[
\begin{pmatrix}\gamma_1^2&\rho\gamma_1\gamma_2\\
\rho\gamma_1\gamma_2&\gamma_2^2\end{pmatrix}.
\]

The normal equation gives, almost surely,

\[
\widehat x_m=\frac{u^{\mathsf T}S^{\mathsf T}Sr}{u^{\mathsf T}S^{\mathsf T}Su}
=\frac{\gamma_1^2-\gamma_2^2}{\gamma_1^2+\gamma_2^2+2\rho\gamma_1\gamma_2}.
\tag{1}
\]

When \(|\rho|<1\) the denominator is a positive-definite quadratic form except at the zero Gaussian vector. At \(|\rho|=1\) it is the square of a nondegenerate Gaussian linear form. Hence the coefficient is well-defined and unique almost surely for **every** finite \(m\), including \(m=1\).

**Step 2: classify the conditional distribution.** Write \((\gamma_1,\gamma_2)=R(\cos\theta,\sin\theta)\), where \(\theta\) is uniform on a circle and independent of \(R\). Conditional on \(\rho=a\), (1) becomes

\[
Z_a=\frac{\cos(2\theta)}{1+a\sin(2\theta)}.
\]

For \(|a|<1\) the denominator is positive. Rearranging the event \(Z_a\le z\) gives \(\cos(2\theta)-az\sin(2\theta)\le z\). Its left side is a sinusoid of amplitude \(\sqrt{1+a^2z^2}\). Uniform angular measure therefore gives the exact conditional CDF

\[
F_a(z)=\begin{cases}
0,&z\le-(1-a^2)^{-1/2},\\
\displaystyle\frac12+\frac1\pi\arcsin\!\left(\frac{z}{\sqrt{1+a^2z^2}}\right),&|z|<(1-a^2)^{-1/2},\\
1,&z\ge(1-a^2)^{-1/2}.
\end{cases}
\tag{2}
\]

In particular, \(|Z_a|\le(1-a^2)^{-1/2}\) deterministically. Differentiation gives the interior density

\[
f_a(z)=\frac{1}{\pi(1+a^2z^2)\sqrt{1-(1-a^2)z^2}}.
\]

For \(a=1\), cancellation in (1) yields \((\gamma_1-\gamma_2)/(\gamma_1+\gamma_2)\); for \(a=-1\), it yields \((\gamma_1+\gamma_2)/(\gamma_1-\gamma_2)\). Each numerator-denominator pair consists of independent identically distributed \(N(0,2)\) variables. Both conditional laws are therefore **standard Cauchy**, with CDF \(F_{\pm1}(z)=1/2+\arctan(z)/\pi\). In particular the complete CDF is the explicit binomial mixture

\[
\Pr\{\widehat x_m\le z\}=2^{-m}\sum_{j=0}^m\binom mj F_{(2j-m)/m}(z).
\tag{3}
\]

**Step 3: identify the only unbounded component.** The two cases \(\rho=1\) and \(\rho=-1\) have probabilities \(2^{-m}\) each, yielding total Cauchy weight \(w_m=2^{1-m}\). For \(m\ge2\), every remaining value of \(\rho\) satisfies \(|\rho|\le1-2/m\), so its conditional support is contained in

\[
[-T_m,T_m],\qquad T_m=\frac{1}{\sqrt{1-(1-2/m)^2}}=\frac{m}{2\sqrt{m-1}}.
\]

The standard-Cauchy two-sided tail is \(2\arctan(1/t)/\pi\), hence for \(t\ge T_m\)

\[
\Pr\{|\widehat x_m|>t\}=w_m\frac{2}{\pi}\arctan(1/t)=\frac{2^{2-m}}{\pi}\arctan(1/t).
\]

For \(m=1\) the entire law is Cauchy, and the identity holds for every \(t>0\). As \(t\to\infty\), \(t\arctan(1/t)\to1\), giving the asserted exact coefficient. The Cauchy component has a finite absolute \(p\)-moment precisely when \(0<p<1\), while the remainder is compactly supported for each fixed \(m\). This proves the full moment dichotomy. In particular \(\mathbb E|\widehat x_m|=\mathbb E\widehat x_m^2=\infty\); the signed expectation is not an integrable mean, despite the symmetry of the distribution.

## Verification

The standalone script `check_tail.py` evaluates the exact binomial probabilities with rational arithmetic, checks the unconditional far-tail identity for \(1\le m\le14\), and integrates the density in (2) through an endpoint-regularizing trigonometric substitution. The script reports 105 finite arithmetic tests and confirms probability normalization in these cases. The script and finite checks do **not** prove any all-\(m\) statement, moment divergence, or priority claim; Steps 1–3 are the complete mathematical proof.

## Relationship to prior work

Song and Zhang (2026, Section 3, equation (3)) derive the same ratio (1) to show a nonvanishing failure probability for the natural Gaussian-diagonal modification of subsampled Hadamard regression, and explicitly note that \(\gamma_1/\gamma_2\) is Cauchy. That already establishes the basic obstruction to a coordinate-wise high-probability guarantee. The added claim here is **different and more precise**: the exact all-finite-\(m\) law, an explicitly weighted standard-Cauchy component arising only from row-sign collisions, the *exact* far-tail coefficient, and the complete absolute-moment threshold. These are not stated in their Section 3. Their balanced disjoint Gaussian-pooling construction is a different random map and is not affected by this result.

Song, Ye, Yin, and Zhang (2023) study fixed-direction and coordinate-wise high-probability guarantees for a sign-diagonal sketch. Price, Song, and Woodruff (2017) establish high-probability guarantees for standard SRHT and counterexamples for other sketch families. Neither of those algorithms uses this Gaussian-diagonal ratio, so their theorems do not imply this specific finite-mixture law. Classical Gaussian-ratio theory supplies the conditional Cauchy fact but does not, by itself, identify the rare Hadamard-row event probability or the unconditional exact tail threshold.

## Limitations

This is a fixed, explicitly specified **one-column** regression problem, not a universal failure theorem for every design or sampling scheme. It requires independent row sampling **with replacement** and a single Gaussian diagonal shared by all sampled rows. Sampling without replacement, resampling fresh Gaussian weights per row, truncation/regularization, or the balanced pooled transform may change or remove the heavy-tail component. No claim is made about the high-probability performance of the source paper's main algorithm. The mathematical novelty comparison is conditional on the inspected primary texts and search results; earlier equivalent Gaussian-ratio folklore may exist.

## References

1. Zhao Song and Lichen Zhang, *Hadamard Flattening and Gaussian Pooling Sketch for Least Squares with Coordinate-wise Guarantee*, arXiv:2608.26552, first public August 27, 2026, Section 3 equation (3). https://arxiv.org/abs/2608.26552
2. Zhao Song, Mingquan Ye, Junze Yin, and Lichen Zhang, *A Nearly-Optimal Bound for Fast Regression with \(\ell_\infty\) Guarantee*, arXiv:2302.00248, first public February 1, 2023. https://arxiv.org/html/2302.00248v1
3. Eric Price, Zhao Song, and David P. Woodruff, *Fast Regression with an \(\ell_\infty\) Guarantee*, arXiv:1705.10723, first public May 30, 2017. https://arxiv.org/abs/1705.10723
