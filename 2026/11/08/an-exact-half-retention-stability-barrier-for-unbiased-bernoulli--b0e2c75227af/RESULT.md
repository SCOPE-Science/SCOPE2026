# An exact half-retention stability barrier for unbiased Bernoulli error feedback

## Finding
For scalar strongly convex quadratic minimization under independently resampled **unbiased** Bernoulli compression, classical error feedback converges in mean square from every nonzero scalar initialization **if and only if** the retention probability exceeds one half and the normalized fixed stepsize is below the sharp threshold
\[
  p>\frac12,\qquad 0<h<\frac{4p-2}{3-2p}.
\]
In particular, at every \(0<p\le 1/2\), **no positive constant stepsize** yields mean-square convergence under classical error feedback. In contrast, omitting error feedback while retaining the identical unbiased compressor is mean-square convergent exactly when \(0<h<2p\). When \(1/2<p<1\), the error-feedback interval is strictly smaller than the memoryless interval. The classification includes \(p=1\), for which both algorithms reduce to gradient descent and have stability interval \(0<h<2\).

## Assumptions and scope
Let \(a>0\), \(f(x)=ax^2/2\), and \(h=\eta a>0\). Let \((\xi_k)_{k\ge0}\) be independent Bernoulli random variables with \(\Pr(\xi_k=1)=p\in(0,1]\), independent of the deterministic initial condition \(x_0\ne0\). The compressor is \(\mathcal C_p(z;\xi)=\xi z/p\), so its conditional expectation is \(z\). Classical error feedback uses \(e_0=0\) and, for every integer \(k\ge0\),
\[
 u_k=hx_k+e_k,\qquad d_k=\mathcal C_p(u_k;\xi_k),\qquad x_{k+1}=x_k-d_k,\qquad e_{k+1}=u_k-d_k.
\]
Mean-square convergence means \(\lim_{k\to\infty}\mathbb E[x_k^2]=0\). The comparison method uses \(x_{k+1}=x_k-\mathcal C_p(hx_k;\xi_k)\) with no residual state. There are no additive gradient noises, no changing stepsizes, and no correlations between different compression calls.

## Proof
Write \(m_k=\mathbb E[x_k^2]\), \(v_k=\mathbb E[e_k^2]\), and \(c_k=\mathbb E[x_ke_k]\). Since \(\xi_k\) is independent of the past and \(\mathbb E[\mathcal C_p(u_k;\xi_k)\mid u_k]=u_k\), we have
\[
 \mathbb E[e_{k+1}\mid x_k,e_k]=0,\quad
 \mathbb E[e_{k+1}^2\mid x_k,e_k]=\frac{1-p}{p}(hx_k+e_k)^2.
\]
The pathwise identity \(x_{k+1}-e_{k+1}=(1-h)x_k-e_k\) then gives
\[
 \mathbb E[x_{k+1}e_{k+1}\mid x_k,e_k]=\mathbb E[e_{k+1}^2\mid x_k,e_k],
\]
because the remaining factor is measurable with respect to the past and the conditional residual mean vanishes. Hence \(c_k=v_k\) for every \(k\ge1\), without an assumption that \(c_0=v_0\) is preserved by arbitrary correlated initial states.

A conditional expansion yields the exact, closed two-dimensional moment recursion for all \(k\ge1\):
\[
 \binom{m_{k+1}}{v_{k+1}}=N_{p,h}\binom{m_k}{v_k},\qquad
 N_{p,h}=\begin{pmatrix}
 1-2h+h^2/p &(1+2h)/p-2\\
 (1-p)h^2/p &(1-p)(1+2h)/p
 \end{pmatrix}.
\]
The initial step has \(m_1=x_0^2(1-2h+h^2/p)\) and \(v_1=x_0^2(1-p)h^2/p\). For \(0<p<1\) both are strictly positive. The trace and determinant are
\[
 T=\frac{1+h^2+2h-4hp}{p},\qquad D=\frac{(1-p)(1-2h^2)}p.
\]
The three Schur–Jury inequalities for the polynomial \(z^2-Tz+D\) reduce to
\[
 1-T+D=\frac{h}{p}\bigl(4p-2-(3-2p)h\bigr)>0,
\]
\[
 1+T+D=\frac{2-(2p-1)h(2-h)}p>0,\qquad
 1-D=\frac{2p-1+2(1-p)h^2}p>0.
\]
For \(p>1/2\) and \(0<h<(4p-2)/(3-2p)\), the first is positive, \(h<2\), and the other two are strictly positive: indeed \(h(2-h)\le1\), while \(2p-1\le1\). Thus \(N_{p,h}\) is Schur stable, so both moments decay geometrically. For \(0<p\le1/2\) the first inequality fails for every \(h>0\); for \(1/2<p<1\) it fails at and above the displayed threshold, so in both cases its spectral radius is at least one.

To see that spectral nonstability actually prevents decay from the stipulated residual-free initial condition, rather than merely from some exotic covariance state, note that in the excluded regimes \(N_{p,h}\) has **strictly positive entries**. The diagonal terms are positive; the upper-right entry is positive for \(p\le1/2\), and for \(p>1/2\) it is positive whenever \(h\ge (4p-2)/(3-2p)>p-1/2\). Its lower-left entry is positive for \(p<1\) and \(h>0\). Perron–Frobenius gives a strictly positive left Perron vector; its inner product with the strictly positive moment vector \((m_1,v_1)\) cannot decay when the Perron root is at least one. Since that vector's components remain nonnegative and the left Perron vector has positive entries, \(m_k\) cannot tend to zero (if \(m_k\to0\), then the strictly positive recurrence and the \(v_k\)-to-\(m_{k+1}\) coefficient would force \(v_k\to0\), contradicting the Perron projection). At \(p=1\), the residual vanishes identically and \(x_k=(1-h)^kx_0\), giving the same formula with upper limit two.

For memoryless unbiased compression, direct conditioning gives
\[
 \mathbb E[x_{k+1}^2]=\left(1-2h+\frac{h^2}{p}\right)\mathbb E[x_k^2],
\]
whose multiplier is strictly below one exactly for \(0<h<2p\). Finally for \(1/2<p<1\),
\[
 2p-\frac{4p-2}{3-2p}=\frac{2(1-p)(2p+1)}{3-2p}>0.
\]
This establishes all assertions, including sharp equality and nonconvergence at the boundary.

## Verification
The accompanying `verify.py` expands the two Bernoulli transition matrices symbolically, checks the moment closure, characteristic polynomial and three Schur expressions, and enumerates finite stochastic prefixes with exact rational arithmetic for several probabilities and stepsizes. `verification_output.txt` records the successful replay. These calculations are diagnostic and are not a replacement for the argument proving the all-parameter, infinite-horizon statement.

## Relationship to prior work
Horváth and Richtárik (2020, arXiv:2006.11077), especially Section 2 and Algorithm 2, use the same classical residual mechanism with unbiased compressors and establish that error feedback can be disadvantageous; their general convergence comparisons do not state the exact all-probability scalar fixed-stepsize window above. Berg Thomsen, Taylor and Dieuleveut (2025, arXiv:2506.05271) derive tight optimized worst-case Lyapunov rates for contractive compression, and Berg Thomsen, Taylor and Dieuleveut (2026, arXiv:2605.31594) extend this approach to distributed error feedback; neither inspected main statement gives this exact fixed-compressor, all-stepsizes, zero-residual moment phase diagram. A related published Bernoulli error-feedback result treats the **unscaled, biased** compressor \(z\mapsto\xi z\), whose exact stability window is \(0<h<2p/(2-p)\). Its full proof exploits the residual becoming zero on successful transmission and the resulting geometric renewal law. For the present unbiased amplifier \(z\mapsto\xi z/p\), that renewal/reset premise fails: successful transmission leaves residual \(e_{k+1}=(1-1/p)u_k\), which is typically nonzero. Thus the cited theorem does not imply the present sharp formula by a stepsize substitution. Known qualitative comparisons and general Schur stability theory are not claimed as new.

## Limitations
The classification concerns a scalar exact quadratic, iid Bernoulli calls, a fixed positive stepsize, and an initially zero error residual. It does not imply instability for optimally rescaled/biased compression, decreasing stepsizes, multidimensional strongly convex problems, controlled dependence between compression calls, or every error-feedback variant. As with a new specialist calculation, publication precedence beyond the inspected sources remains possible; an independent scientific audit has not been performed.

## References
- S. Horváth and P. Richtárik, *A Better Alternative to Error Feedback for Communication-Efficient Distributed Learning*, arXiv:2006.11077, initial public posting 2020-06-19, https://arxiv.org/abs/2006.11077 .
- D. Berg Thomsen, A. Taylor, and A. Dieuleveut, *Tight analyses of first-order methods with error feedback*, arXiv:2506.05271, https://arxiv.org/abs/2506.05271 .
- D. Berg Thomsen, A. Taylor, and A. Dieuleveut, *A Tight Theory of Error Feedback Algorithms in Distributed Optimization*, arXiv:2605.31594, https://arxiv.org/abs/2605.31594 .
- *Sharp mean-square stability loss for Bernoulli error-feedback sparsification*, research record https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-mean-square-stability-loss-for-bernoulli-error-feedback-sp--db9fbbc3513e (primary full result and proof inspected).
