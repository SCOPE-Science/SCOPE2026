# Complete norming-corner resonance for affine projection on biased Boolean cubes

## Finding

Let \(d\ge2\), \(0<p<1\), and let \(\mu_p\) be the product Bernoulli\((p)\) probability measure on \(\{0,1\}^d\). Write \(P_{d,p}\) for the real \(L^2(\mu_p)\)-orthogonal projection onto the affine functions, including the constant. Let \(u=\min(p,1-p)\), and call a corner *rare* when every coordinate takes the less probable outcome. Every point is an evaluation site because \(\mu_p\) has full support.

**Complete equality classification.** If \(p\ne1/2\), the rare corner is the **unique** evaluation point attaining the sharp \(L^\infty\)-projection norm, except when
\[
(d-1)u\in\mathbb Z.
\]
At precisely those resonances, exactly \(d+1\) corners attain the norm: the rare corner and the \(d\) corners differing from it in exactly one coordinate. No corner at Hamming distance two or more from the rare corner is norming. If \(p=1/2\), **every** one of the \(2^d\) corners is norming. At any norming corner \(x\), every norm-attaining real input at that evaluation is \(f(y)=\pm\operatorname{sgn}K(x,y)\) wherever the kernel is nonzero, with arbitrary values of modulus at most one at its zeros.

The underlying **norm value and rare-corner existence are not claimed new**. Earlier published results give them, including the exact binomial identity
\[
\|P_{d,p}\|_{\infty\to\infty}=\frac1u\,\mathbb E|J-(d-1)u|,\qquad J\sim\operatorname{Bin}(d,u),
\]
and its fixed-bias Gaussian and sparse-bias Poisson limits. The independent contribution assessed here is the exhaustive equality classification and the arithmetic resonance criterion; this does not reannounce the known sharp norm or those asymptotics as novel.

## Proof

For \(x,y\in\{0,1\}^d\), the normalized affine reproducing kernel is
\[
K(x,y)=1+\sum_{i=1}^{d}\frac{(x_i-p)(y_i-p)}{p(1-p)},\qquad
\|P_{d,p}\|=\max_x\mathbb E_{\mu_p}|K(x,Y)|.
\]
The last identity follows by choosing the input sign of a maximizing kernel row. If \(p=1/2\), bit-flips act transitively and preserve \(\mu_p\); all rows therefore have the same norm.

It remains to consider \(0<p<1/2\), with \(q=1-p\); interchanging zeros and ones proves the case \(p>1/2\). At an evaluation coordinate equal to one, its centered kernel summand has values \(-1\) (probability \(q\)) and \(q/p\) (probability \(p\)). At an evaluation coordinate equal to zero, the summand has values \(-1\) (probability \(p\)) and \(p/q\) (probability \(q\)). When the other coordinates and constant contribute \(z\), replacing an output zero by one increases the conditional absolute kernel expectation by
\[
D_p(z)=q|z-1|+p|z+q/p|-p|z-1|-q|z+p/q|.
\]
Splitting at \(-q/p,-p/q,1\) gives the exact nonnegative piecewise formula
\[
D_p(z)=\begin{cases}
2p(z+q/p),&-q/p<z<-p/q,\\
2(q-p)(1-z),&-p/q\le z<1,\\
0,&z\le-q/p\text{ or }z\ge1.
\end{cases}
\]
Thus every such replacement weakly increases the row norm, proving that the all-ones corner is norming. Strictness is equivalent to a positive-probability configuration of the remaining coordinates with \(-q/p<z<1\).

Suppose among the other \(d-1\) evaluation coordinates, \(r\) are ones and \(s=d-1-r\) are zeros. Choose \(j\in\{0,\ldots,r\}\) high outcomes among the ones and \(\ell\in\{0,\ldots,s\}\) high outcomes among the zeros. All such configurations have positive probability, and their residual contribution is
\[
z=2-d+j/p+\ell/q.
\]
Writing \(t=p(d-1)\), the strictness window is exactly
\[
t-1<j+(p/q)\ell<t.
\]
If \(s\ge1\), this window always contains an admissible pair. Indeed \(r+s(p/q)>t\). If \(r<t-1\), take \(j=r\) and increase \(\ell\) in increments \(p/q<1\) until first exceeding \(t-1\); the crossing occurs below \(t\) and before \(\ell>s\). If \(r\ge t-1\) and \(t\notin\mathbb Z\), choose \(j=\lfloor t\rfloor,\ell=0\). If \(r\ge t-1\) and \(t\in\mathbb Z\), choose \(j=t-1,\ell=1\). Therefore **every coordinate replacement is strictly improving whenever another zero remains among the other evaluation coordinates**.

When \(s=0\), the other \(d-1\) coordinates are all rare ones and the possible values of \(j\) are integers. There is an integer in the open interval \((t-1,t)\) exactly when \(t\notin\mathbb Z\). Hence this final replacement is strict in the nonresonant case and is an equality at resonance. Applying the coordinate replacements successively, any corner with two or more common zeros must undergo a strict improvement before reaching the all-ones corner; one with exactly one common zero ties precisely at resonance. This proves the complete equality classification for all \(d\ge2\) and \(0<p<1\).

Finally, at each maximizing row \(x\), equality in \(|\int Kf|\le\int|K|\) for real \(|f|\le1\) requires one globally consistent sign of \(K(x,\cdot)f(\cdot)\) on all nonzero kernel atoms. This gives the stated input characterization.

## Independent finite corroboration and limits

An independent exact-fraction full-cube enumeration of all output Hamming classes for each dimension \(2\le d\le8\) and seven rational biases checked every claimed maximizing class, including resonances. These 49 finite cases corroborate, but do not prove, the universal statement; the piecewise increment and integer-window argument prove all dimensions and real biases. The theorem does not cover heterogeneous coordinate biases or non-affine Fourier masks, and does not assert new norm values, projection constants, or asymptotics. Historical priority of the equality classification remains a best-of-knowledge assessment rather than a certification.

## Prior mathematics

1. *Balanced bias minimizes sharp affine Fourier amplification on the Bernoulli cube*, published October 26, 2026, https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-balanced-bias-minimizes-sharp-affine-fourier-amplification-on-th--71f416ba0fcb. Establishes the exact affine-band norm, rare-corner maximization, and Gaussian/Poisson laws, but does not classify all maximizing corners.
2. *A universal rare-vertex norming law for biased Boolean Fourier multipliers*, published October 25, 2026, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-a-universal-rare-vertex-norming-law-for-biased-boolean-fourier-m--40f4b54b28c0. Establishes a broader convex-order maximization theorem; expressly does not classify uniqueness or ties.
3. *A universal rare-vertex principle for Bernoulli first-chaos multipliers*, published October 18, 2026, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-a-universal-rare-vertex-principle-for-bernoulli-first-chaos-mult--2d1e4412cee2. Treats the centered first chaos (without the constant) and does not classify the affine-band equality set.
4. N. Keller, *A Simple Reduction from a Biased Measure on the Discrete Cube to the Uniform Measure*, arXiv:1001.1167 (2010), https://arxiv.org/abs/1001.1167. Provides the biased Walsh framework, not the extremal equality classification.
5. P. Nayar, *FKN Theorem on the Biased Cube*, arXiv:1311.3179 (2013), https://arxiv.org/abs/1311.3179. Concerns \(L^2\)-approximation to affine Boolean functions rather than exact endpoint norming rows.
