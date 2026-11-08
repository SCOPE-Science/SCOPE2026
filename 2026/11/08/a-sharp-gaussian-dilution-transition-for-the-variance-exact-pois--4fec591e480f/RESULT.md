# A sharp Gaussian-dilution transition for the variance-exact Poisson Bernstein scale

## Finding

Let \(N\) have a Poisson distribution of mean \(\lambda>0\), let \(Z\) be an independent standard Gaussian, and let \(b>0\), \(s\geq0\). Set
\[
X=b(N-\lambda)+\sqrt{s}\,Z,\qquad
V=\lambda b^2+s,\qquad
\theta=\frac{\lambda b^2}{V}.
\]
The *variance-exact right sub-gamma scale* \(c_*(X)\) is the infimum of all \(c\geq0\) such that
\[
\log\mathbb E e^{tX}\leq\frac{Vt^2}{2(1-ct)}
\quad\text{for every }0\leq t<1/c,
\]
with the usual convention that \(1/0=+\infty\). Define, for \(x>0\),
\[
h(x)=\frac{2(e^x-1-x-x^2/2)}{x^2},\quad
\Phi_\theta(x)=\frac{\theta h(x)}{x(1+\theta h(x))},\quad
\Theta(x)=\frac{xh'(x)-h(x)}{h(x)^2}.
\]
The endpoint limits are \(\Phi_\theta(0)=\theta/3\) and \(\Theta(0)=3/4\). Then \(\Theta\) decreases strictly from \(3/4\) to zero and the following complete characterization holds.

**Theorem.** For every \(b,\lambda>0\) and \(s\geq0\):

1. If \(\theta\geq3/4\), equivalently \(s\leq\lambda b^2/3\), the exact optimum is
   \[
   c_*(X)=\frac{b\theta}{3}
   =\frac{\lambda b^3}{3(\lambda b^2+s)}.
   \]
   The variational supremum is attained only as \(x\downarrow0\).
2. If \(0<\theta<3/4\), there is a unique \(x_\theta>0\) solving \(\Theta(x_\theta)=\theta\), and
   \[
   c_*(X)=b\Phi_\theta(x_\theta)>\frac{b\theta}{3}.
   \]
   This is a unique positive optimizing tilt.
3. At the transition, writing \(\varepsilon=3/4-\theta\downarrow0\),
   \[
   x_\theta=\frac{40}{3}\varepsilon+O(\varepsilon^2),\qquad
   \frac{c_*(X)}b=\frac{\theta}{3}+\frac59\varepsilon^2+O(\varepsilon^3).
   \]
4. In the high-Gaussian-variance regime \(\theta\downarrow0\), with \(L=\log(1/\theta)\),
   \[
   x_\theta=L+3\log L-\log2+o(1),\qquad
   \frac{b}{c_*(X)}=L+3\log L+1-\log2+o(1).
   \]

## Assumptions and scope

The Poisson count and Gaussian perturbation are independent; the variance proxy in the inequality is *fixed* at the actual variance \(V\), rather than independently optimized. Only positive, right-sided moment-generating-function arguments are compared. The Gaussian term has variance \(s\); it need not be strictly positive. The positive Poisson jump size \(b\) is fixed and nonrandom, and \(\lambda>0\). In particular, the theorem does not concern negative jumps, random jump sizes, or variable quadratic proxies.

## Proof

**1. Reduction to a scalar maximum.** Independence gives, for all real \(t\),
\[
K_X(t)=\lambda(e^{bt}-1-bt)+\frac{s t^2}{2}
=\frac{Vt^2}{2}\bigl(1+\theta h(bt)\bigr).
\]
For any \(c\geq0\), the defining inequality is equivalent to
\[
(1-ct)\bigl(1+\theta h(bt)\bigr)\leq1
\quad(0<t<1/c),
\]
which, whenever \(ct<1\), is the inequality
\[
c\geq\frac1t\left(1-\frac1{1+\theta h(bt)}\right).
\]
The right-hand side is strictly less than \(1/t\), so if \(ct\geq1\) the corresponding constraint is automatically outside the admissible comparison interval. Conversely, if \(c\) bounds the right-hand side for every positive \(t\), it satisfies the required inequality on its entire admissible interval. Thus
\[
\frac{c_*(X)}b=\sup_{x>0}\Phi_\theta(x).
\]
This is also a direct specialization of the general variational framework of Chen (2026), but the subsequent optimization is established here explicitly.

**2. Global monotonicity of the transition function.** The entire power series
\[
h(x)=\sum_{n\geq1}a_nx^n,
\qquad a_n=\frac{2}{(n+2)!},
\]
has positive coefficients. Write
\[
A(x)=xh'(x)-h(x)=\sum_{n\geq2}(n-1)a_nx^n,
\qquad B(x)=h(x)^2=\sum_{n\geq2}b_nx^n,
\]
where \(b_n=\sum_{j=1}^{n-1}a_j a_{n-j}>0\). An elementary factorial convolution yields
\[
\frac{(n-1)a_n}{b_n}=r_n
=\frac{(n-1)(n+3)(n+4)}{2S_n},
\quad S_n=2^{n+4}-n^2-9n-22.
\]
To verify the convolution, rewrite \(b_n=4\sum_{k=3}^{n+1}{n+4\choose k}/(n+4)!\) and subtract the two symmetric endpoint triples \(k=0,1,2\) and \(k=n+2,n+3,n+4\) from the complete binomial sum. This gives \(b_n=4S_n/(n+4)!\). For each integer \(n\geq2\), the following difference is strictly positive:
\[
(n-1)(n+3)S_{n+1}-n(n+5)S_n
=(n-3)(n+2)2^{n+4}+n^3+16n^2+79n+96.
\]
At \(n=2\) the value is \(70>0\); for \(n\geq3\) every term on the right is nonnegative and at least one is positive. Consequently \(r_{n+1}<r_n\) for every \(n\geq2\). In particular \(r_2=3/4\).

For each \(x>0\), \(\Theta(x)=A(x)/B(x)\) is the mean of \(r_n\) under the strictly positive weights proportional to \(b_nx^n\). Differentiating these weights with respect to \(\log x\) gives
\[
\frac{d\Theta(x)}{d\log x}
=\operatorname{Cov}_x(n,r_n)<0,
\]
since \(n\mapsto r_n\) is strictly decreasing and this weight law is nondegenerate. Thus \(\Theta\) is strictly decreasing. Its limit at zero is \(r_2=3/4\). As \(x\to\infty\), elementary differentiation of \(h(x)\sim2e^x/x^2\) yields
\[
\Theta(x)=\frac{x^2(x-3)}{2e^x}(1+o(1))\longrightarrow0.
\]

**3. Exact phase transition and uniqueness.** Differentiation yields
\[
\Phi_\theta'(x)=\frac{\theta\{xh'(x)-h(x)-\theta h(x)^2\}}
{x^2(1+\theta h(x))^2}.
\]
Thus the sign of \(\Phi_\theta'\) equals the sign of \(\Theta(x)-\theta\). When \(\theta\geq3/4\), it is strictly negative at every positive \(x\), and the optimum is \(\Phi_\theta(0)=\theta/3\). When \(0<\theta<3/4\), strict monotonicity of \(\Theta\) gives exactly one positive sign change from positive to negative. Since \(\Phi_\theta(x)\to0\) as \(x\to\infty\), this is the unique global maximizer. This proves the first two assertions without assuming unimodality.

**4. Transition and high-noise expansions.** Taylor expansion gives
\[
h(x)=\frac{x}{3}+\frac{x^2}{12}+\frac{x^3}{60}+O(x^4),
\qquad
\Theta(x)=\frac34-\frac{3x}{40}+O(x^2).
\]
For \(\varepsilon=3/4-\theta\downarrow0\), analytic inversion shows
\(x_\theta=40\varepsilon/3+O(\varepsilon^2)\). Substitution into the full second-order Taylor expansion of \(\Phi_\theta\) gives
\[
\Phi_\theta(x_\theta)=\frac\theta3+\frac59\varepsilon^2+O(\varepsilon^3).
\]
For \(\theta\downarrow0\), the equation \(\Theta(x_\theta)=\theta\) and strict monotonicity imply \(x_\theta\to\infty\). The asymptotic in Step 2 gives
\[
\log(1/\theta)=x_\theta-3\log x_\theta+\log2+o(1),
\]
which can be inverted once using \(x_\theta/L\to1\) to give \(x_\theta=L+3\log L-\log2+o(1)\). At the maximizer,
\[
\Phi_\theta(x_\theta)
=\frac1{x_\theta}\left(1-\frac{h(x_\theta)}{x_\theta h'(x_\theta)}\right)
=\frac1{x_\theta}-\frac1{x_\theta^2}+O(x_\theta^{-3}),
\]
hence \(1/\Phi_\theta(x_\theta)=x_\theta+1+o(1)\). This proves the final assertion.

## Verification

The standalone Python script `verify.py` checks the factorial convolution and positive difference identity exactly using rational arithmetic for \(2\leq n\leq150\), verifies the cumulant normalization, checks the transition-function ordering and optimizers on finite numerical grids, and tests the stated critical and high-noise asymptotics on finite sample parameters. Run `python3 verify.py` from the directory containing this file. All analytic quantifiers, strict monotonicity for the complete positive axis, and the asymptotic limits are proved above, not inferred from finite tests.

## Relationship to prior work

Chen's *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws* (arXiv:2610.00032v1, first posted 2026-09-02), especially Theorem 3.1 and Proposition 5.1, supplies the general variational framework and notes that adding Gaussian variance may reduce the optimal scale; its full manuscript does not give the exact fixed-jump Poisson–Gaussian threshold, prove uniqueness of the optimizing tilt throughout this family, or give the transition/high-noise expansions above. The general variational formula and M-class characterization therefore are **not** claimed as new. Klar and Müller (2003) introduced the underlying M-class and equilibrium-order comparisons; their broader conditions do not specify the concrete threshold here. Leskelä and Välimaa (arXiv:2508.12103v1) optimize a different Poisson-shape variance proxy; that parameter optimization does not imply this fixed-variance Bernstein-scale phase diagram. The result is a specialized exact evaluation with its own coefficient monotonicity lemma, not an independent invention of sub-gamma theory.

## Limitations

The proof is for a centered Poisson count with one fixed positive jump size and an independent Gaussian. In particular, it does not assert the same transition for random jump sizes or arbitrary infinitely divisible perturbations. The smallest scale is defined relative to the exact total variance; allowing a larger proxy changes the optimization. Historical priority of this special case is not definitively established by finite literature searches. Numeric diagnostics cannot certify the continuum arguments and do not replace their proofs.

## References

- Yichuan Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (2026-09-02), https://arxiv.org/html/2610.00032v1 .
- Bernhard Klar and Alfred Müller, *Characterizations of classes of lifetime distributions generalizing the NBUE class*, 2003, author-hosted manuscript https://wwwalt.math.kit.edu/stoch/~klar/seite/veroeffentlichungen/media/mclass-copy.pdf .
- Lasse Leskelä and Ian Välimaa, *Sub-Poisson distributions: Concentration inequalities, optimal variance proxies, and closure properties*, arXiv:2508.12103v1 (2025-08-16), https://arxiv.org/html/2508.12103v1 .
