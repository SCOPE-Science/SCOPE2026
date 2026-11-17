# Opposite-endpoint gap and exponential-dimensional crossover for sharp nonlinear Riesz bounds

## Finding
For every integer \(n\ge3\), the optimal constant \(C^*_{n,\alpha}\) in the nonlinear Riesz-potential BBM subrepresentation inequality and the Hoang–Moen–Pérez bound \(H_{n,\alpha}\) have the same leading pole as \(\alpha\downarrow0\), yet their **absolute difference has a positive, explicitly determined finite part** in every fixed dimension. More strongly, the dimension-normalized gap obeys a uniform two-parameter law:
\[
\boxed{\gamma_{n,1}\bigl(H_{n,\alpha}-C^*_{n,\alpha}\bigr)
=\left(\frac n2\right)^{-\alpha/2}\left[\delta_n+O(\alpha)\right],
\quad \delta_n=\log2+\frac{\psi(n/2)-\psi((n-1)/2)}2.}
\]
The remainder constant can be chosen independently of \(n\ge3\) for all \(0<\alpha\le1/2\). The positive sequence \(\delta_n\) strictly decreases from \(\delta_3=1\) to \(\log2\).

In the coupled limit \(n\to\infty\), \(\alpha\downarrow0\) with \(\alpha\log n\to\lambda\in[0,\infty]\), with \(e^{-\infty/2}:=0\),
\[
\boxed{\gamma_{n,1}\bigl(H_{n,\alpha}-C^*_{n,\alpha}\bigr)
\longrightarrow e^{-\lambda/2}\log2,\qquad
\alpha\gamma_{n,1}C^*_{n,\alpha}\longrightarrow e^{-\lambda/2}.}
\]
Thus the dimension and fractional-order limits of the normalized gap do not commute:
\[
\lim_{n\to\infty}\lim_{\alpha\downarrow0}\gamma_{n,1}(H_{n,\alpha}-C^*_{n,\alpha})=\log2,
\qquad
\lim_{\alpha\downarrow0}\lim_{n\to\infty}\gamma_{n,1}(H_{n,\alpha}-C^*_{n,\alpha})=0.
\]
The transition occurs when the dimension grows exponentially in the reciprocal fractional order.

For fixed \(n\), set \(N=n/2\), \(b_n=(\gamma_E-\psi(N))/2-\log2\), and \(\zeta(2)=\pi^2/6\). The sharp constant has the further expansion
\[
\boxed{\gamma_{n,1}C^*_{n,\alpha}=
\frac1\alpha+(b_n-1)
+\left(\frac{b_n^2}2-b_n+\frac{3\psi_1(N)+\zeta(2)}8\right)\alpha
+O_n(\alpha^2),}
\]
where \(\psi_1=\psi'\) is the trigamma function. In particular \(\gamma_{3,1}=1/(2\pi^2)\), so \(H_{3,\alpha}-C^*_{3,\alpha}\to2\pi^2\).

## Assumptions and scope
For an integer \(n\ge3\), a parameter \(0<\alpha<1\), and a compactly supported smooth real function \(f\), define
\[
\mathcal D^\alpha f(x)=\int_{\mathbb R^n}\frac{|f(x)-f(y)|}{|x-y|^{n+\alpha}}\,dy,
\quad
I_\beta g(x)=\gamma_{n,\beta}\int_{\mathbb R^n}\frac{g(y)}{|x-y|^{n-\beta}}\,dy,
\quad
\gamma_{n,\beta}=\frac{\Gamma((n-\beta)/2)}{2^\beta\pi^{n/2}\Gamma(\beta/2)}.
\]
Here \(C^*_{n,\alpha}\) is the smallest constant in
\[
(1-\alpha)I_\alpha(\mathcal D^\alpha f)(x)
\le C^*_{n,\alpha}I_1(|\nabla f|)(x),
\quad f\in C_c^\infty(\mathbb R^n),\quad x\in\mathbb R^n,
\]
and the comparison constant established by Hoang–Moen–Pérez, in the same convention, is
\[
H_{n,\alpha}=\frac{2^{2-\alpha}\pi^{n/2}\Gamma((3-\alpha)/2)}
{\alpha\,\Gamma((n+\alpha-1)/2)}.
\]
All limits in the coupled regime require \(n\to\infty\) through integers and \(\alpha\downarrow0\). No claim is made about the unrestricted planar optimal constant or about functions outside the defining smooth test class.

## Proof
**1. Exact input and separation of the pole.** The exact sharp-constant theorem and hypergeometric series of Jleli–Samet (Theorem 1.3 and Proposition 6.1 of arXiv:2611.10656v1) give, for \(N=n/2\),
\[
\gamma_{n,1}C^*_{n,\alpha}
=(1-\alpha)\alpha Q_n(\alpha)
\sum_{k=0}^{\infty}A_{n,k}(\alpha)
\left[\frac1{(\alpha+2k)^2}+\frac1{(n+2k)^2}\right],
\]
\[
Q_n(\alpha)=\frac{2^{-\alpha}\Gamma(N-\alpha/2)}
{\Gamma(N)\Gamma(1+\alpha/2)},\qquad
A_{n,k}(\alpha)=\frac{(N+\alpha/2)_k(1+\alpha/2)_k}{(N)_k\,k!},
\]
where \((u)_k\) is the rising factorial. Since \(A_{n,0}=1\), write the series as \(\alpha^{-2}+R_n(\alpha)\), with
\[
R_n(\alpha)=\frac1{n^2}+\sum_{k\ge1}A_{n,k}(\alpha)
\left[\frac1{(\alpha+2k)^2}+\frac1{(n+2k)^2}\right].
\]
For \(0\le\alpha\le1/2\) and \(N\ge3/2\), monotonicity of \((x+\alpha/2)/x\) in \(x\) gives
\[
0<A_{n,k}(\alpha)\le\left(\frac{(1+\alpha/2)_k}{k!}\right)^2\le C(k+1)^\alpha.
\]
Termwise parameter derivatives of order up to two are bounded by \(C_j(k+1)^{1/2}(1+\log(k+1))^j\) for \(j=0,1,2\), with constants independent of \(n\). Multiplying by denominators bounded by \(C(k+1)^{-2}\) proves a common summable majorant. Thus \(R_n\), \(R_n'\), and \(R_n''\) are uniformly bounded on \([0,1/2]\), for all \(n\ge3\). In particular
\[
\gamma_{n,1}C^*_{n,\alpha}
=\frac{1-\alpha}{\alpha}Q_n(\alpha)
\left[1+\alpha^2R_n(\alpha)\right].
\]

**2. Uniform finite-gap expansion.** Set \(m=N-1/2\) and
\[
U_n(\alpha)=N^{\alpha/2}Q_n(\alpha),\quad
V_n(\alpha)=N^{\alpha/2}\frac{2^{1-\alpha}\Gamma(m)\Gamma((3-\alpha)/2)}
{\sqrt\pi\,\Gamma(m+\alpha/2)},
\quad
W_n(\alpha)=(1-\alpha)U_n(\alpha)[1+\alpha^2R_n(\alpha)].
\]
The formulas above imply the exact identity
\[
\gamma_{n,1}(H_{n,\alpha}-C^*_{n,\alpha})
=N^{-\alpha/2}\frac{V_n(\alpha)-W_n(\alpha)}\alpha.
\]
Both \(V_n(0)\) and \(W_n(0)\) equal one. The differences \(\log N-\psi(N+s)\) are uniformly bounded for \(N\ge3/2\) and \(|s|\le1/4\). The Gamma factors are positive and their logarithmic first and second derivatives involve only these bounded differences and trigamma values at arguments bounded away from zero. Together with the bounds on \(R_n\), this proves \(\sup_{n,\alpha}(|V_n''(\alpha)|+|W_n''(\alpha)|)<\infty\). Direct differentiation at zero yields
\[
V_n'(0)-W_n'(0)=\log2+\frac{\psi(N)-\psi(N-1/2)}2=\delta_n.
\]
Taylor's theorem, divided by \(\alpha\), therefore gives \((V_n-W_n)/\alpha=\delta_n+O(\alpha)\), **with an error independent of dimension**. The trigamma \(\psi_1\) is positive and strictly decreasing, hence \(\delta_n\) is strictly decreasing; its initial and limiting values follow from \(\psi(3/2)-\psi(1)=2-2\log2\) and \(\psi(x+1/2)-\psi(x)\to0\).

**3. Joint exponential crossover and noncommutation.** Uniformly for \(0<\alpha\le1/2\) and integers \(n\ge3\), the digamma bound above gives
\[
\log U_n(\alpha)=O(\alpha),
\]
with an absolute constant. It follows that \(\alpha\gamma_{n,1}C^*_{n,\alpha}=N^{-\alpha/2}[1+O(\alpha)]\), uniformly in dimension. If \(\alpha\log n\to\lambda\in[0,\infty]\), then \(N^{-\alpha/2}\to e^{-\lambda/2}\) (interpreted as zero at infinity) and \(\delta_n\to\log2\). The two coupled limits follow. At fixed \(\alpha>0\), the prefactor \(N^{-\alpha/2}\) forces the normalized gap to zero as \(n\to\infty\); at fixed dimension the small-order gap tends to \(\delta_n\). This proves the stated noncommutation.

**4. Three-term fixed-dimensional expansion.** Since \(A_{n,k}(0)=1\), dominated convergence and the uniform derivative control show
\[
R_n(\alpha)=\frac{\zeta(2)+\psi_1(N)}4+O_n(\alpha).
\]
Expanding the logarithm of \(Q_n\) at zero yields
\[
Q_n(\alpha)=1+b_n\alpha+
\left(\frac{b_n^2}2+\frac{\psi_1(N)-\zeta(2)}8\right)\alpha^2+O_n(\alpha^3).
\]
Substitution into Step 1, and collection of coefficients, gives the asserted Laurent expansion. The fixed-dimensional finite-gap constant is \(\delta_n/\gamma_{n,1}\).

## Verification
The source's sharpness theorem and series formula were read in full at their controlling statements, including their normalization. Independent algebraic derivation checked the Gamma factors and two derivatives at zero. Direct numerical truncations of the positive hypergeometric series for dimensions \(3,4,5,10\) and orders \(0.2,0.08,0.03\), together with the explicit HMP formula, approached the predicted finite gaps and three-term coefficients. These finite checks do not establish any infinite-series or all-dimensional statement; Steps 1–4 provide those proofs. The uniform big-O constants are existential and are not optimized.

## Relationship to prior work
Hoang, Moen and Pérez obtained the explicit comparison constant \(H_{n,\alpha}\). Claros and Pérez proved the nonlinear Riesz-potential BBM limit as \(\alpha\uparrow1\). Jleli and Samet proved the exact optimal constant for every \(n\ge3\) and \(0<\alpha<1\), and showed strict improvement over the earlier bound; their endpoint analysis emphasizes \(\alpha\uparrow1\). The present result is **an asymptotic theorem extracted from their exact series**, not an independent sharp-constant formula. Its additional statement is a dimension-uniform opposite-endpoint remainder, a nonzero finite gap, and the exponential joint-scaling transition; those require a uniform estimate not supplied by the fixed-parameter sharpness theorem. Existing primary texts and indexed results inspected for overlap did not state or imply the quantified uniform transition without further analysis.

## Limitations
The result applies to \(n\ge3\) only; the unrestricted two-dimensional exact constant remains unresolved in the cited source. The normalization by \(\gamma_{n,1}\) is essential for comparing dimensions. No claim of independent validation or exhaustive bibliographic uniqueness is made. Because an exact positive series was already available, alternative derivations or unindexed statements of the endpoint asymptotics could exist. Proof estimates here are uniform near \(\alpha=0\) only and give no new information at \(\alpha=1\).

## References
- M. Jleli and B. Samet, *Sharp Constants and First-Order Asymptotics in a Bourgain–Brezis–Mironescu Formula for Riesz Potentials*, arXiv:2611.10656v1 (first posted 7 November 2026), Theorem 1.3, Corollary 1.4, Proposition 6.1, Corollary 6.2. https://arxiv.org/abs/2611.10656
- A. Claros and C. Pérez, *Bourgain–Brezis–Mironescu Formula for Riesz Potentials*, arXiv:2604.06827 (first posted 8 April 2026). https://arxiv.org/abs/2604.06827
- C. Hoang, K. Moen and C. Pérez, *A New Look at the Subrepresentation Formulas*, arXiv:2406.13772 (first posted 19 June 2024). https://arxiv.org/abs/2406.13772
