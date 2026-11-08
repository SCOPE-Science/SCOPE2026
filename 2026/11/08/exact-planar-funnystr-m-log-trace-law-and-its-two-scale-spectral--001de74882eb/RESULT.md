# Exact planar funNyström log-trace law and its two-scale spectral-spike limit

## Finding

Let \(a>b>0\), \(A=\operatorname{diag}(a,b)\), and \(g=(g_1,g_2)^{\mathsf T}\) have independent standard real Gaussian coordinates. For every positive-definite \(M\), form the rank-one Gaussian Nyström matrix
\[
\mathcal N(M,g)=Mg(g^{\mathsf T}Mg)^{-1}g^{\mathsf T}M.
\]
Set \(f(M)=\log(I+M)\). Consider the two trace underestimation errors
\[
E_F=\operatorname{tr}f(A)-\operatorname{tr}f(\mathcal N(A,g)),\qquad
E_D=\operatorname{tr}f(A)-\operatorname{tr}\mathcal N(f(A),g).
\]
The first is the one-column, one-pass *function-after-Nyström* estimate; the second applies ordinary Nyström directly to the matrix function, using the same Gaussian direction. Both are well defined almost surely and nonnegative. Write \(B=\log(1+b)\) and \(H=E_F-B\). The following is an exact finite-sample and high-spike theorem.

**Exact law.** For \(0<h<\log((1+a)/(1+b))\),
\[
\Pr\{H\le h\}=\frac2\pi\arctan\sqrt{
\frac{a(1+a)(e^h-1)}{b((1+a)-(1+b)e^h)}}.
\]
The CDF is zero below this interval and one above it; there are no endpoint atoms. In particular,
\[
\mathbb EH=2\log\frac{\sqrt a+\sqrt b}
{\sqrt a+\sqrt{b(1+b)/(1+a)}}.
\]
With \(L_a=\log(1+a)\) and \(L_b=B\), the direct-Nyström error satisfies
\[
\mathbb E E_D=\sqrt{L_aL_b},
\]
and has CDF \(\frac2\pi\arctan\sqrt{L_a(d-L_b)/(L_b(L_a-d))}\) for \(L_b<d<L_a\), with no endpoint atoms.

**Sharp high-spike contrast.** For every fixed \(b>0\), as \(a\to\infty\), couple all matrices through the same \(g\). If \(T=g_2^2/g_1^2\), then \(T\) has the square of the standard Cauchy law and
\[
 aH\longrightarrow bT\quad\text{almost surely},\qquad
 \sqrt a\,\mathbb EH\longrightarrow2\sqrt b.
\]
In comparison,
\[
E_D\longrightarrow B(1+T)\quad\text{almost surely},\qquad
\mathbb E E_D\sim\sqrt{B\log a}\longrightarrow\infty.
\]
Thus a fixed quantile of the excess \(H\) is of order \(a^{-1}\) while its mean is of order \(a^{-1/2}\). The limiting direct error has a nonintegrable upper tail:
\[
\Pr\{B(1+T)>y\}=\frac2\pi\arcsin\sqrt{B/y}
\sim\frac2\pi\sqrt{B/y}\quad(y\to\infty,\ y>B).
\]
These comparisons concern estimator error distributions, not equal computational costs or an unbiased trace estimator.

## Assumptions and scope

The matrix is real, diagonal and two dimensional, with \(a>b>0\); rotation to another eigenbasis leaves the distribution unchanged because the sketch is isotropic Gaussian. Exactly one Gaussian vector is used with no oversampling or power iterations. Matrix logarithms are principal logarithms of positive-definite arguments, and all arithmetic is exact. The high-spike limit holds with \(b>0\) fixed and \(a\to\infty\). The degenerate equal-eigenvalue case \(a=b\) gives \(E_F=E_D=B\) deterministically; it is not part of the CDF formula. The boundary \(b=0\) gives exact rank-one recovery and is likewise excluded from the CDF formula.

## Proof

**1. A single scalar describes each approximation.** Almost surely \(g_1\ne0\). Put \(T=g_2^2/g_1^2\). A rank-one Nyström matrix has precisely one nonzero eigenvalue, its trace. Hence
\[
\mu=\operatorname{tr}\mathcal N(A,g)=\frac{a^2+b^2T}{a+bT},
\qquad\operatorname{tr}f(\mathcal N(A,g))=\log(1+\mu).
\]
With \(H=L_a-\log(1+\mu)\), algebra gives
\[
H=\log\frac{(1+a)(a+bT)}{a(1+a)+b(1+b)T}
=\log\left(1+\frac{b(a-b)T}{a(1+a)+b(1+b)T}\right).
\]
For \(a>b>0\), this increases strictly with \(T\in(0,\infty)\), from zero to \(\log((1+a)/(1+b))\). It follows that \(E_F=B+H\ge B\), the best rank-one trace-error floor for \(f(A)\).

**2. Exact distribution.** The Gaussian ratio \(g_2/g_1\) is standard Cauchy; its square has
\[
\Pr\{T\le t\}=\frac2\pi\arctan\sqrt t,\qquad t\ge0.
\]
Solving \(H=h\) for \(T\) gives
\[
T(h)=\frac{a(1+a)(e^h-1)}{b((1+a)-(1+b)e^h)}.
\]
Strict monotonicity and substitution yield the asserted CDF and all fixed quantiles without approximations.

**3. Expected function-after-Nyström error.** By Gaussian rotational symmetry, \(g/\|g\|\) has uniform angle \(\theta\in[0,\pi)\). For positive \(u,v\), the elementary logarithmic integral is
\[
\frac1\pi\int_0^\pi\log(u\cos^2\theta+v\sin^2\theta)\,d\theta
=2\log\frac{\sqrt u+\sqrt v}{2}.
\]
To prove it, write the quantity inside the logarithm as
\[
\left|\frac{\sqrt u+\sqrt v}{2}
+\frac{\sqrt u-\sqrt v}{2}e^{2i\theta}\right|^2,
\]
and use the mean-value identity for the logarithm of the modulus of an affine analytic function whose zero is outside the unit disk. Since
\[
1+\mu=\frac{a(1+a)\cos^2\theta+b(1+b)\sin^2\theta}
{a\cos^2\theta+b\sin^2\theta},
\]
subtracting two such integrals shows
\[
\mathbb E\log(1+\mu)
=2\log\frac{\sqrt{a(1+a)}+\sqrt{b(1+b)}}{\sqrt a+\sqrt b}.
\]
Subtract from \(L_a\) and simplify to obtain the stated exact \(\mathbb EH\).

**4. Direct Nyström.** Apply the same rank-one trace identity to \(f(A)=\operatorname{diag}(L_a,L_b)\). It yields
\[
E_D=\frac{L_aL_b(1+T)}{L_a+L_bT}.
\]
This increases strictly from \(L_b\) to \(L_a\); inversion as in Step 2 yields its CDF. By the substitution \(u=\tan\theta\),
\[
\frac1\pi\int_0^\pi\frac{d\theta}{L_a\cos^2\theta+L_b\sin^2\theta}
=\frac1{\sqrt{L_aL_b}}.
\]
Multiplying by \(L_aL_b\) proves \(\mathbb E E_D=\sqrt{L_aL_b}\). This scalar trace-residual expectation is a standard rank-one identity and is used as a comparator, not presented as a new general theorem.

**5. Asymptotics and nonuniform integrability.** In the exact formula from Step 1, hold \(T<\infty\) fixed. As \(a\to\infty\), the argument of \(\log(1+\cdot)\) is \(bT/a+O(a^{-2})\), proving \(aH\to bT\) almost surely. For the mean, expand the positive exact expression from Step 3:
\[
\mathbb EH=2\sqrt{b/a}+O(a^{-1}).
\]
The two rates differ because \(\mathbb ET=\infty\): convergence of \(aH\) is not uniform integrability. In Step 4, \(L_a\to\infty\), so \(E_D\to L_b(1+T)\) almost surely, whereas its exact finite-parameter mean diverges like \(\sqrt{L_b\log a}\). Finally \(\Pr\{T>t\}=(2/\pi)\arctan(t^{-1/2})\), which gives the displayed direct-error upper tail. Every boundary and quantifier follows from these explicit expressions.

## Verification

The standalone `verify.py` uses Python's standard library. It checks 6,020 assertions: exact rational Nyström identities, finite-parameter distribution inversions, midpoint evaluation of the two derived angular integral identities, and several high-spike constant and fixed-quantile comparisons. Run `python3 verify.py`; the expected terminal line is `VERIFICATION_OK checks=6020`. The proof above, not the finite checker, establishes the distributional and asymptotic claims.

## Relationship to prior work

Persson and Kressner (first public preprint September 22, 2022) define the function-after-Nyström method, study operator-monotone matrix functions and trace approximations, and give nuclear-norm expectation bounds under oversampling hypotheses. Their Theorem 3.9 assumes at least two target and oversampling columns and does not state an unoversampled planar CDF, its exact mean, or the two-scale spike limit. Their numerical comparisons with direct function-matrix sketching motivate the present distribution-level question, rather than establish these formulas.

Saibaba, Alexanderian and Ipsen (first public preprint May 16, 2016) analyze Gaussian subspace-based log-determinant estimators and spectral-gap error bounds. Their compressed-subspace estimator is not either Nyström estimator defined here. General rank-one Nyström trace-residual formulas already imply the direct comparator's mean \(\sqrt{L_aL_b}\); its rediscovery is not claimed as originality. The asserted contribution is the exact logarithmic function-after-Nyström error law and the sharp mean-versus-quantile spike asymptotics, together with their transparent comparison to direct Nyström. Classical Cauchy-ratio and logarithmic angular-integral identities are deliberately treated as known proof tools.

## Limitations

This is a precisely specified two-dimensional, one-column benchmark. It is not a dimension-free improvement theorem, a guarantee for oversampled or power-iterated variants, or a comparison at matched matrix-vector cost. The transformed estimate is biased downward; there is no claim that either approximation by itself provides an unbiased trace estimator. A special-case result may have appeared in less accessible literature under other terminology; the research-level novelty assessment is not independent publication clearance.

## References

1. D. Persson and D. Kressner, *Randomized low-rank approximation of monotone matrix functions*, first public arXiv posting 2022-09-22, https://arxiv.org/abs/2209.11023 . Relevant sections: 2, 3.3, 4, 5.
2. A. K. Saibaba, A. Alexanderian and I. C. F. Ipsen, *Randomized Matrix-free Trace and Log-Determinant Estimators*, first public arXiv posting 2016-05-16, https://arxiv.org/abs/1605.04893 . Relevant sections: 2–4.
3. A. Gittens and M. W. Mahoney, *Revisiting the Nyström Method for Improved Large-scale Machine Learning*, JMLR 17 (2016), https://jmlr.org/beta/papers/v17/gittens16a.html . General low-rank approximation background, not a source of the stated function-level CDF.
