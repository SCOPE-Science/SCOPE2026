# Sharp exterior leverage for arbitrary two-frequency exponential sums

## Finding
For every real \(x\) with \(|x|\ge 1\) and every nonzero complex-valued signal
\[
g(t)=a e^{i\lambda_1t}+b e^{i\lambda_2t},\qquad a,b\in\mathbb C,\quad\lambda_1,\lambda_2\in\mathbb R,
\]
the sharp, frequency-uniform inequality is
\[
\boxed{\ |g(x)|^2\le (1+3x^2)\,\frac12\int_{-1}^{1}|g(t)|^2\,dt.\ }
\]
More precisely, for each fixed exterior \(x\), the best constant over all nonzero signals with at most two arbitrary real frequencies is \(1+3x^2\). The strict inequality holds for every individual nonzero signal, and the optimal constant is approached only when the difference between distinct frequencies tends to zero. Thus no fixed positive frequency gap can attain the universal constant.

## Assumptions and scope
The observation interval is \([-1,1]\) with normalized Lebesgue probability measure \(dt/2\), and \(x\in(-\infty,-1]\cup[1,\infty)\). Complex coefficients are unrestricted; real frequencies need not be separated or bounded. The zero signal is excluded. If the two displayed frequencies coincide, the signal reduces to one frequency, whose pointwise-to-energy ratio is \(1\). There is no claim for complex frequencies or more than two frequencies. The squared constant, rather than its square root, is an exterior leverage score.

## Proof
**1. Exact leverage at a fixed gap.** Suppose the frequencies differ by \(y=|\lambda_2-\lambda_1|>0\). Removing the central unimodular modulation does not change the ratio. For the two exponential atoms the normalized Gramian is
\[
G_y=\begin{pmatrix}1&s\\s&1\end{pmatrix},\qquad s=\frac{\sin y}{y}.
\]
The evaluation vector at \(x\) has entries of modulus one with relative phase \(xy\). By the finite-dimensional reproducing-kernel identity, the exact squared evaluation norm, maximized over nonzero coefficient vectors, is
\[
K_y(x)=\frac{2-2s\cos(xy)}{1-s^2}.
\]
Since \(|s|<1\) for \(y>0\), this expression is finite and the maximization at fixed gap is attained by coefficients proportional to \(G_y^{-1}\) applied to the evaluation vector. It suffices to show \(K_y(x)<1+3x^2\) for each fixed \(y>0\).

**2. Separated gaps.** If \(y\ge2\), then \(|s|\le1/y\le1/2\) and
\[
K_y(x)\le\frac{2}{1-|s|}\le4\le1+3x^2.
\]
The first or second bound is strict for every \(y\ge2\): equality in \(|s|\le1/2\) would require both \(y=2\) and \(|\sin 2|=1\), which is false.

**3. Closely spaced gaps.** Let \(0<y<2\), write \(z=y^2\), and set
\[
u=1-\frac z6+\frac{z^2}{120}.
\]
Alternating Taylor bounds for sine yield \(1-z/6\le s\le u\le1\), hence \(1/3<s<1\). Consider
\[
F(v,z)=2+2v-4v^2-vz.
\]
Its derivative with respect to \(v\) is \(2-8v-z<0\) whenever \(1/3<v\le1\). Consequently,
\[
F(s,z)\ge F(u,z)=\frac{z^2(20+10z-z^2)}{3600}>0\qquad(0<z<4).
\]
Rearrangement gives
\[
\frac{s z}{1-s^2}<4-\frac2{1+s}.
\]
Using \(\cos w\ge1-w^2/2\), we obtain
\[
\begin{aligned}
K_y(x)&\le\frac2{1+s}+\frac{s z x^2}{1-s^2}\\
&<4x^2-\frac{2(x^2-1)}{1+s}\\
&\le1+3x^2,
\end{aligned}
\]
where the last step is equivalent to \((x^2-1)(1-s)/(1+s)\ge0\). This proves strictness for every fixed nonzero gap.

**4. Optimality and collision rigidity.** At fixed \(|x|\ge1\), define the two-frequency signals
\[
g_\varepsilon(t)=\cos(\varepsilon t)+\frac{3x}{\varepsilon}\sin(\varepsilon t),\qquad \varepsilon>0.
\]
They have frequencies \(\{-\varepsilon,+\varepsilon\}\) and converge uniformly on compact intervals to the linear polynomial \(1+3xt\). Therefore
\[
\lim_{\varepsilon\to0^+}\frac{|g_\varepsilon(x)|^2}{\frac12\int_{-1}^1|g_\varepsilon(t)|^2dt}
=\frac{(1+3x^2)^2}{1+3x^2}=1+3x^2.
\]
This proves sharpness. If a sequence of two-frequency signals has ratios approaching the optimum, its positive gaps must converge to zero: \(K_y(x)\) is continuous for \(y>0\), is strictly below the optimum at every positive gap by steps 2 and 3, and tends to \(2\) as \(y\to\infty\). Coincident-frequency signals have ratio one and cannot be extremal. Hence frequency collision is necessary for approach to the optimum.

## Verification
A standalone standard-library program, `CHECK.py`, checks the exact rational polynomial identity in step 3 and performs 48,012 independent floating-point test assertions for the closed leverage expression, its inequality, and the explicit limiting construction. Run with `python3 CHECK.py`. These checks are corroboration, not a proof for all gaps and exterior points; the analytic argument above supplies that proof.

## Relationship to prior work
Zhang's 2026 extrapolation theorem studies exactly arbitrary-real-frequency sparse exponential signals on this observation interval, deriving general growth bounds with implicit constants and leverage-score applications. This result supplies a sharp closed constant for the two-frequency case and shows that the frequency-collision polynomial model is the unique limiting source of equality. Chen and Price (2019) supplied earlier nonsharp sparse-Fourier extrapolation estimates. Borwein and Erdélyi (2000) established broad Remez- and Nikolskii-type bounds for real exponential sums and interior evaluation, but the identified theorem statements are not the exact exterior complex-oscillatory two-frequency inequality. The degree-one algebraic polynomial reproducing kernel, \(1+3x^2\), is classical; the nontrivial assertion is that no positive-gap oscillatory two-frequency subspace ever exceeds this polynomial value. Prior work might contain an equivalent two-frequency statement under different terminology; no exhaustive uniqueness claim is made.

## Limitations
The statement does not generalize as written to three or more frequencies, complex growth/decay exponents, different observation measures, or multidimensional intervals. No quantitative stability rate for near-extremizing frequency gaps is asserted. Literature checking does not prove the absence of an unindexed equivalent theorem. An independent audit has not been performed.

## References
- R. Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, arXiv:2607.10501, first submitted 2026-07-11, https://arxiv.org/abs/2607.10501.
- X. Chen and E. Price, *Estimating the Frequency of a Clustered Signal*, arXiv:1904.13043 (2019), https://arxiv.org/abs/1904.13043.
- P. Borwein and T. Erdélyi, *Pointwise Remez- and Nikolskii-type inequalities for exponential sums*, Math. Ann. 316 (2000), 39–60, https://doi.org/10.1007/s002080050003.
