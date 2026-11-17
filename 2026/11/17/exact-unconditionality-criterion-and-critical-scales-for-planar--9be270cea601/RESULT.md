# Exact unconditionality criterion and critical scales for planar Kaczmarz reconstruction

## Finding

For a sequence of unit vectors \((e_n)_{n\ge0}\) in a **real or complex Hilbert space of dimension two**, write
\[
 r_n=|\langle e_n,e_{n-1}\rangle|,\quad
 p_0=1,\quad p_n=\prod_{k=1}^{n}r_k,\quad
 a_n=p_{n-1}\sqrt{1-r_n^2}\qquad(n\ge1).
\]
The ordinary sequential Kaczmarz residual after observing \(e_0,\ldots,e_n\) has exact operator norm \(p_n\), and its auxiliary reconstruction vectors satisfy \(\|g_0\|=1\), \(\|g_n\|=a_n\) for \(n\ge1\). For every integer \(m\ge0\), the **exact finite absolute reconstruction amplification** is
\[
 \sup_{\|x\|=1}\sum_{n=0}^{m}|\langle x,g_n\rangle|=\sqrt{1+\left(\sum_{n=1}^{m}a_n\right)^2}.
\]
It follows that the sequence reconstructs every input in its given order if and only if \(p_n\to0\), whereas an effective sequence reconstructs **unconditionally for every input** if and only if
\[
 \sum_{n=1}^{\infty}p_{n-1}\sqrt{1-r_n^2}<\infty.
\]
This distinction occurs already in the plane. Indeed, all positive decreasing sequences \((p_n)_{n\ge0}\) with \(p_0=1\) and \(p_n\downarrow0\) can occur as exact residual-norm profiles of planar Kaczmarz sequences, for which the unconditionality criterion becomes
\[
 \sum_{n=1}^{\infty}\sqrt{p_{n-1}^2-p_n^2}<\infty.
\]

Two continuous parameter families exhibit sharp boundaries. For \(a>0\), \(b>a\), set
\[
 r_n=\sqrt{1-\frac a{n+b}}\quad(n\ge1).
\]
Its residuals are
\[
 p_n^2=\frac{\Gamma(b+1)\Gamma(n+b+1-a)}{\Gamma(b+1-a)\Gamma(n+b+1)},\qquad
 p_n\sim C_{a,b}n^{-a/2},\qquad
 C_{a,b}=\sqrt{\frac{\Gamma(b+1)}{\Gamma(b+1-a)}}.
\]
Every such sequence is effective, but its reconstruction is unconditionally convergent for all inputs **precisely when \(a>1\)**. Its absolute coefficient sum grows as \(2\sqrt a C_{a,b}m^{(1-a)/2}/(1-a)\) for \(0<a<1\) and as \(C_{1,b}\log m\) for \(a=1\); for \(a>1\), the tail is asymptotic to \(2\sqrt a C_{a,b}m^{(1-a)/2}/(a-1)\).

There is a second, logarithmic transition exactly at the critical power. Fix \(b>1\), \(\sigma\ge0\), prescribe
\[
 p_n=\sqrt{\frac b{n+b}}\left(\frac{\log b}{\log(n+b)}\right)^\sigma\quad(n\ge0),
\]
and realize it by the construction below. Then the sequence is always effective, but universal unconditional reconstruction holds **exactly for \(\sigma>1\)**. The absolute coefficient sum at \(\sigma=1\) diverges at the exact order \(\sqrt b\log b\,\log\log m\).

## Assumptions and scope

The inner product is linear in its first argument. Let \(E_nx=\langle x,e_n\rangle e_n\) and \(Q_n=I-E_n\). For every input \(x\), define \(x_0=E_0x\), then recursively
\[
 x_n=x_{n-1}+\langle x-x_{n-1},e_n\rangle e_n\qquad(n\ge1).
\]
The associated auxiliary vectors are defined by \(g_0=e_0\) and \(g_n=e_n-\sum_{j=0}^{n-1}\langle e_n,e_j\rangle g_j\). Thus \(x_n=\sum_{j=0}^{n}\langle x,g_j\rangle e_j\). A sequence is *effective* when \(x_n\to x\) for every input; a reconstruction is *unconditionally convergent* when these particular vector summands converge independently of rearrangement. All results concern these exact noiseless, sequential, unrelaxed updates; they do not assert unconditionality for arbitrary other expansion coefficients or higher-dimensional Hilbert spaces.

## Proof

**Projection-product identity.** The residual \(R_nx=x-x_n\) equals \(Q_nQ_{n-1}\cdots Q_0x\). In dimension two every \(Q_j\) is a rank-one orthogonal projection; its range is the orthogonal line to \(e_j\). For two consecutive such lines, the modulus of the overlap of unit generators equals \(|\langle e_j,e_{j-1}\rangle|=r_j\) (also in the complex plane). Hence multiplication of rank-one projections gives
\[
 \|R_n\|=\prod_{j=1}^{n}r_j=p_n.
\]
The equality includes cases when one or more adjacent vectors are orthogonal or parallel. Therefore effectiveness is equivalent to \(p_n\to0\), since the residuals converge to zero on every vector precisely when their norm does in finite dimension.

**Auxiliary norms and exact amplification.** The coefficient of the \(n\)-th update is \(\langle R_{n-1}x,e_n\rangle=\langle x,R_{n-1}^{*}e_n\rangle\); thus \(g_n=R_{n-1}^{*}e_n=Q_0\cdots Q_{n-1}e_n\) for \(n\ge1\), agreeing with the stated recursive definition. Applying the rightmost projection first gives \(\|Q_{n-1}e_n\|=\sqrt{1-r_n^2}\). The subsequent rank-one projections contribute \(r_{n-1},\ldots,r_1\), so \(\|g_n\|=a_n\). Each \(g_n\), \(n\ge1\), belongs to the **single line** \(e_0^\perp\), orthogonal to \(g_0=e_0\). For \(x\) of unit norm put \(s=|\langle x,e_0\rangle|\) and \(t=\|Q_0x\|\); then \(s^2+t^2=1\) and
\[
 \sum_{n=0}^{m}|\langle x,g_n\rangle|=s+t\sum_{n=1}^{m}a_n.
\]
Maximizing over the Euclidean quarter circle proves the exact factor \(\sqrt{1+(\sum a_n)^2}\), and also exhibits attaining inputs. Since every \(e_n\) is unit, \(\|\langle x,g_n\rangle e_n\|=|\langle x,g_n\rangle|\). In finite-dimensional normed spaces, unconditional convergence of a series implies absolute convergence, by applying the scalar unconditional-convergence criterion to every coordinate. Conversely, absolute convergence implies unconditional convergence. Hence an effective sequence is universally unconditional if and only if \(\sum a_n<\infty\). If the sum diverges, taking \(x\) to be a unit vector in \(e_0^\perp\) gives a conditionally convergent reconstruction: its ordered partial sums tend to \(x\), but the sum of norms diverges.

**Realization.** Given a positive nonincreasing profile \(p_0=1\), \(p_n\to0\), set \(r_n=p_n/p_{n-1}\in(0,1]\), \(\theta_n=\arccos r_n\), \(\Theta_n=\sum_{k=1}^{n}\theta_k\), and \(e_n=(\cos\Theta_n,\sin\Theta_n)\in\mathbb R^2\), taking \(\Theta_0=0\). Then the overlap between consecutive vectors has modulus \(r_n\), so the prior identities give \(\|R_n\|=p_n\) and \(a_n=\sqrt{p_{n-1}^2-p_n^2}\). Thus the necessary-and-sufficient criterion is realizable at every positive decreasing profile, not merely a formal bound.

**Polynomial boundary.** With \(r_n^2=(n+b-a)/(n+b)\), multiplying the factors and using the gamma recursion yields the exact displayed gamma quotient. Stirling's ratio asymptotic then gives \(p_n\sim C_{a,b}n^{-a/2}\). It follows directly that
\[
 a_n=p_{n-1}\sqrt{\frac a{n+b}}\sim \sqrt a\,C_{a,b}n^{-(a+1)/2}.
\]
The integral test proves the threshold \(a>1\) and the displayed partial-sum or tail equivalents, with \(a=1\) giving the logarithmic divergence.

**Logarithmic boundary.** The prescribed residual profile is positive, has \(p_0=1\), decreases to zero, and is therefore realizable. The adjacent-ratio identity reads
\[
 r_n^2=\frac{n+b-1}{n+b}\left(\frac{\log(n+b-1)}{\log(n+b)}\right)^{2\sigma}.
\]
Expansion at infinity gives \(1-r_n^2\sim1/n\), hence
\[
 a_n=p_{n-1}\sqrt{1-r_n^2}\sim
 \frac{\sqrt b(\log b)^\sigma}{n(\log n)^\sigma}.
\]
The logarithmic integral test proves convergence precisely for \(\sigma>1\), divergence at \(\sigma=1\) with \(\sqrt b\log b\,\log\log m\) leading term, and the other two regimes. This closes all stated cases without numerical extrapolation.

## Verification

`check.py` is a standalone standard-library diagnostic. It independently constructs the recursive auxiliary vectors, computes matrix residual products and absolute-amplification witnesses for several planar angle sequences, checks exact gamma products for the polynomial family, and checks finite-parameter logarithmic estimates. On execution it returned `PLANAR_KACZMARZ_EXACT_OK 583 finite checks`. These finite experiments are supplementary only; the infinite-sequence and sharp-threshold conclusions follow from the analytic projection identities and classical series tests given above.

## Relationship to prior work

Berner, Herr, and Jorgensen (2026), Theorems 4.1 and 4.13, prove the sharp unconditional-reconstruction classification for **stationary** effective sequences represented by singular spectral measures: unconditional reconstruction for every input holds exactly at finite atomic support. Their finite-dimensional stationary examples are automatically unconditional. The present result instead shows that **nonstationary effective sequences already in dimension two** may fail unconditionality, and computes the exact criterion and sharp rate boundaries there. The stationary theorem does not imply the present classification.

Haller and Szwarc (2005) establish the general residual-projection identity, auxiliary recursion, and a partial-isometry characterization of effectiveness. These are used as standard foundations rather than claimed as new. Their effectiveness criterion does not by itself give the summability threshold for the norms of the *reconstruction terms* in nonstationary planar sequences. Herr and Weber (2017) give general effective-sequence formulas and singular-measure Fourier reconstructions; they do not give the present angular criterion. The elementary equivalence of finite-dimensional unconditional and absolute convergence is also standard.

## Limitations

The proof is confined to exact rank-one projections in dimension two; its collinearity argument does not generalize directly to dimension three or above. The polynomial and logarithmic families have specifically prescribed overlaps and are not claimed to cover all possible asymptotic rates. Sharpness means necessary-and-sufficient for the stated families, not an optimal stability bound for noisy observations. A logically equivalent statement in older angle-projection or frame-expansion literature could affect historical priority; the comparisons conducted do not establish universal uniqueness.

## References

1. C. Berner, J. E. Herr, and P. E. T. Jorgensen, *Frame Properties of Effective Stationary Sequences*, arXiv:2611.03358, first public 2 November 2026. https://arxiv.org/abs/2611.03358
2. R. Haller and R. Szwarc, *Kaczmarz Algorithm in Hilbert Space*, *Studia Mathematica* **169** (2005), 123–132. https://doi.org/10.4064/sm169-2-2 ; author full text https://www.math.uni.wroc.pl/~szwarc/ps/rainis.pdf
3. J. E. Herr and E. S. Weber, *Fourier Series for Singular Measures*, *Axioms* **6** (2017), 7. https://doi.org/10.3390/axioms6020007
4. S. Kwapień and J. Mycielski, *On the Kaczmarz Algorithm of Approximation in Infinite-Dimensional Spaces*, *Studia Mathematica* **148** (2001), 75–86. https://doi.org/10.4064/sm148-1-7
