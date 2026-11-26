# Exact finite-height crossover at the Euler boundary of tetration distributions

## Finding

Let \(F_{2k+1}\) be the cumulative distribution function given by the right-associated power tower of odd height \(2k+1\) with common base \(x\in(0,1)\), and let \(F_\infty\) be its pointwise limiting CDF. For every real \(a\), set
\[
 t_{k,a}=e\left(1+\frac{a}{k}\right),\qquad x_{k,a}=\exp(-t_{k,a})
\]
for all sufficiently large positive integers \(k\). Define the continuous function
\[
 H(a)=\begin{cases}
 \displaystyle\frac1e\sqrt{\frac{6a}{1-e^{-2a}}},&a\ne0,\\[3pt]
 \displaystyle\frac{\sqrt3}{e},&a=0.
 \end{cases}
\]
Then, **locally uniformly in \(a\in\mathbb R\)**,
\[
 \lim_{k\to\infty}\sqrt{k}\left(\frac1e-F_{2k+1}(x_{k,a})\right)=H(a),\tag{1}
\]
\[
 \lim_{k\to\infty}\sqrt{k}\left(\frac1e-F_\infty(x_{k,a})\right)=\frac{\sqrt{6a_+}}e,
 \qquad a_+=\max(a,0),\tag{2}
\]
and therefore
\[
 \lim_{k\to\infty}\sqrt{k}\left(F_\infty(x_{k,a})-F_{2k+1}(x_{k,a})\right)
 =H(a)-\frac{\sqrt{6a_+}}e.\tag{3}
\]
In particular, exactly at the Euler threshold,
\[
 F_\infty(e^{-e})-F_{2k+1}(e^{-e})\sim\frac{\sqrt3}{e\sqrt{k}}.\tag{4}
\]
For any fixed \(a<b\), if \(X_{2k+1}\) has CDF \(F_{2k+1}\), the full local probability-mass profile is
\[
 \sqrt{k}\,\Pr\!\left(x_{k,b}<X_{2k+1}\le x_{k,a}\right)
 \longrightarrow H(b)-H(a).\tag{5}
\]
The limiting CDF instead has the piecewise profile in (2), with its one-sided square-root boundary. These are finite-height, moving-parameter conclusions, not just static infinite-tower asymptotics.

## Assumptions and scope

The tower is recursively \(y_1(x)=x\) and \(y_{m+1}(x)=x^{y_m(x)}\), and \(F_{2k+1}=y_{2k+1}\). The source establishes that these odd towers are CDFs and that \(F_\infty=\lim_{k\to\infty}F_{2k+1}\) exists and is continuous. The theorem assumes real \(a\) in a fixed compact set when making a locally uniform statement; then \(t_{k,a}>0\) for all sufficiently large \(k\). Neither a fixed positive distance from the Euler threshold nor a uniform claim over unbounded \(a\)-ranges is assumed. \(W\) denotes the principal real Lambert function on \((0,\infty)\).

## Proof

**1. Exact conjugation and cubic return map.** Put \(t=-\log x\), \(z_m=t y_m\), and \(g_t(z)=t e^{-z}\); thus \(z_{m+1}=g_t(z_m)\) and \(z_1=t e^{-t}\). Let \(w=W(t)\). It obeys \(t=w e^w\) and \(g_t(w)=w\). With \(u_j=z_{2j+1}-w\), the exact two-step recurrence is
\[
 u_{j+1}=T_w(u_j),\qquad
 T_w(u)=w\left[\exp\bigl(w(1-e^{-u})\bigr)-1\right].\tag{6}
\]
A Taylor expansion, uniform for \(w\) in a fixed neighborhood of \(1\), is
\[
 T_w(u)=w^2u+\frac{w^2(w-1)}2u^2
 +\frac{w^2(w^2-3w+1)}6u^3+O(u^4).\tag{7}
\]
Under \(t=t_{k,a}\), uniformly for bounded \(a\), the inverse-function theorem at \(W(e)=1\) gives
\[
 w=1+\frac{a}{2k}+O(k^{-2}),\qquad
 T_w(u)=u\left[1+\frac ak-\frac{u^2}{6}
 +O\!\left(k^{-2}+\frac{|u|}{k}+|u|^3\right)\right].\tag{8}
\]
All constants in (7)--(8) can be chosen uniformly over a compact range of \(a\).

**2. Uniform entry into the neutral neighborhood.** The odd tower subsequence is strictly increasing and stays below the fixed point or the lower member of its two-cycle, as appropriate (see the directly applicable monotonicity and branch statements in the source's Lemma 4.1 and Theorem 4.2). Thus \(u_j<0\) and \(u_j\) increases. At \(w=1\), \(T_1(u)>u\) for every \(-1\le u<0\). Indeed for \(u=-v\) with \(0<v<1\), this inequality is equivalent to \(e^v-1<-\log(1-v)\), which holds strictly by the power series coefficient inequality \(1/n!<1/n\) for every integer \(n\ge3\); the endpoint \(v=1\) follows directly. The initial displacement \(u_0=t e^{-t}-W(t)\) tends to \(e^{1-e}-1\in(-1,0)\). Therefore, for every \(\delta>0\), a finite \(J(\delta)\) exists such that \(-\delta<u_j<0\) for \(j\ge J(\delta)\), all sufficiently large \(k\), and every \(a\) in a prescribed compact set. This follows from uniform positivity of \(T_w(u)-u\) on a compact interval slightly larger than \([e^{1-e}-1,-\delta]\) when \(w\to1\), together with monotonicity. In particular,
\[
 \lim_{J\to\infty}\limsup_{k\to\infty}\sup_{|a|\le A}\frac1k\sum_{j=J}^{k-1}|u_j|=0 \quad(A<\infty).\tag{9}
\]

**3. Inverse-square linearization with a controlled remainder.** For \(j\ge J(\delta)\), define \(r_j=u_j^{-2}\). The factor in brackets in (8) is positive and bounded away from zero. On expanding its reciprocal square,
\[
 r_{j+1}=\left(1-\frac{2a}{k}\right)r_j+\frac13+\varepsilon_{j,k},\tag{10}
\]
\[
 |\varepsilon_{j,k}|\le C_A\left(|u_j|+\frac{|u_j|r_j}{k}+\frac{r_j}{k^2}+\frac1k\right).\tag{11}
\]
A coarse version of (8), valid for sufficiently small fixed \(\delta\), first gives
\[
 r_{j+1}\le\left(1+\frac{C_A}{k}\right)r_j+C_A.
\]
Iteration from the fixed index \(J(\delta)\), at which \(r_J\) remains bounded as \(k\to\infty\), shows \(\max_{J\le j\le k}r_j\le C'_A k\). This implies that the sum of the errors in (11) is \(o(k)\), uniformly for bounded \(a\): divide by \(k\), use (9), and note that \(r_j/k^2=O(k^{-1})\). The finitely many omitted initial indices contribute \(o(k)\). Solving (10) now yields
\[
 \frac{r_k}{k}=\frac1{3k}\sum_{j=J}^{k-1}\left(1-\frac{2a}{k}\right)^{k-1-j}+o(1)
 \longrightarrow \frac13\int_0^1 e^{-2a(1-s)}\,ds
 =\begin{cases}\frac{1-e^{-2a}}{6a},&a\ne0,\\\frac13,&a=0.\end{cases}\tag{12}
\]
The limit is positive, continuous and uniform on each compact \(a\)-interval. Since \(u_k<0\), (12) gives \(\sqrt{k}u_k\to-\sqrt{6a/(1-e^{-2a})}\) (continuous value \(-\sqrt3\)). Finally \(F_{2k+1}(x_{k,a})=(w+u_k)/t_{k,a}\) while \(w/t_{k,a}=e^{-1}+O(k^{-1})\) uniformly. This proves (1).

**4. Infinite-height branch on both sides.** If \(a\le0\), then \(t_{k,a}\le e\) and the infinite odd-tower limit equals \(w/t_{k,a}=e^{-1}+O(k^{-1})\), giving the zero branch in (2). If \(a>0\), it equals the lower point of the attracting two-cycle. For the two \(z\)-coordinates \(z_-<z_+\) of that cycle, let \(z_\pm=q e^{\pm s}\) with \(s>0\). The cycle equations force
\[
 q=\frac{s}{\sinh s},\qquad t=q\exp\bigl(s+q e^{-s}\bigr),\qquad
 \log\frac{t}{e}=\frac{s^2}{6}+O(s^4).\tag{13}
\]
As \(t=e(1+a/k)\), this implies \(s=\sqrt{6a/k}+O_A(k^{-3/2})\). Also \(z_-=q e^{-s}=1-s+O(s^2)\), so the lower probability \(z_-/t=e^{-1}-e^{-1}\sqrt{6a/k}+O_A(k^{-1})\). The estimates are uniform through \(a=0\) on compact sets by continuity and the uniform square-root inversion of (13). This proves (2). Subtraction gives (3); setting \(a=0\) gives (4). Because \(x_{k,b}<x_{k,a}\) for \(a<b\), subtracting two instances of (1) gives the local probability-mass formula (5). The right-hand side is strictly positive for \(a<b\): the derivative of \(a/(1-e^{-2a})\) has positive numerator \(1-(1+2a)e^{-2a}\), by \(e^{2a}>1+2a\) for \(a\ne0\), and positivity extends smoothly through zero. \(\square\)

## Verification

The accompanying standard-library-only `verify.py` implements the exact defining iteration for the finite CDF and the analytic crossover profiles. It checks the return-map identity, signs and monotonicity of odd iterates, the strict positivity of the crossover function, finite-height mass orientation, and numerical approach at multiple parameter values and heights. Its numerical tests are finite diagnostics; the proof of the uniform continuum limit is (6)--(13), not extrapolation from computation.

## Relationship to prior work

Thornton, *A Tetration Distribution* (arXiv:2611.03895v1, November 2, 2026), proves the odd-tower CDF construction and its infinite-height branch structure, states algebraic convergence at the Euler threshold, and numerically reports the cusp amplitude. It does not supply the moving \(1/k\)-parameter window, the exact finite-height profile \(H\), or the finite-window probability-mass law. Corless, Jeffrey and Joby, *Two-cycles in the infinite exponential tower* (2023), and the classical Euler/Karamata parametrizations cover equilibrium two-cycle geometry and some local expansions, but not the joint finite-iteration/vanishing-detuning CDF limit. The formula here is consistent with the general cubic flip normal form. Toledo (2022) classifies convergence of powers and logarithm towers for various fixed initial data but does not give a moving-parameter, finite-height critical profile. The present conclusion requires controlling the singular finite-iteration scaling from a fixed nonlocal starting value; its application to the probability distribution yields (3) and (5).

## Limitations

The theorem is a local boundary-layer statement, uniform only for bounded \(a\). It does not prove a global optimal Kolmogorov-distance constant, a finite-height density scaling limit, the location of the mode, or convergence rates outside the \(1/k\) detuning scale. The exact equilibrium cusp coefficient alone is not claimed novel. Historical priority is subject to other unlocated papers on finite-iteration scaling at an exponential flip. No independent external validation is claimed.

## References

1. M. A. Thornton, *A Tetration Distribution*, arXiv:2611.03895v1 (first public version, 2026-11-02), https://arxiv.org/html/2611.03895v1 . Sections 2 and 4, especially Lemma 4.1 and Theorem 4.2.
2. R. M. Corless, D. J. Jeffrey and J. Joby, *Two-cycles in the infinite exponential tower*, Maple Transactions 3(4) (2023), https://rcorless.github.io/Two-cycles.html and https://doi.org/10.5206/mt.v3i4.17247 .
3. F. J. Toledo, *On the convergence of infinite towers of powers and logarithms for general initial data: applications to Lambert W function sequences*, Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas 116, article 71 (2022), https://doi.org/10.1007/s13398-022-01213-9 . Fixed-parameter convergence and initial-data domains.
4. E. W. Weisstein, *Power Tower*, MathWorld, https://mathworld.wolfram.com/PowerTower.html . Classical convergence and two-cycle context.
