# Three spectral regimes for stretched-scale Laplace orbit Gram determinants

## Finding
Fix real \(c>0\), \(\alpha>0\), and put \(\lambda_j=e^{-cj^\alpha}\) for positive integers \(j\). Define the unit vectors \(v_j(t)=\sqrt{2\lambda_j}\,e^{-\lambda_jt}\in L^2(0,\infty)\). Write \(G_N=(\langle v_i,v_j\rangle)_{1\le i,j\le N}\). Then
\[
\det G_N=\prod_{1\le i<j\le N}\tanh^2\!\left(\frac c2(j^\alpha-i^\alpha)\right).
\]
The sharp three-regime determinant law is
\[
\begin{array}{ll}
0<\alpha<1:&\displaystyle\lim_{N\to\infty}\frac{-\log\det G_N}{N^{2-\alpha}}=\frac{\pi^2}{2c\alpha(2-\alpha)},\\[5pt]
\alpha=1:&\displaystyle-\log\det G_N=\gamma(c)N-\beta(c)+o(1),\\[5pt]
\alpha>1:&\displaystyle\det G_N\longrightarrow \det_{\mathrm F}G\in(0,1),\quad G-I\in\mathcal S_1.
\end{array}
\]
Here \(\gamma(c)=-2\sum_{k\ge1}\log\tanh(ck/2)\), \(\beta(c)=-2\sum_{k\ge1}k\log\tanh(ck/2)\), and \(\det_{\mathrm F}\) is the Fredholm determinant. In addition, the continuous orbit \(\{(e^{-\lambda_jt}\sqrt{2\lambda_j})_{j\ge1}:t\ge0\}\) is a continuous frame for \(\ell^2\) exactly for \(\alpha\ge1\). For \(0<\alpha<1\), it is not even a Bessel family.

## Assumptions and scope
Everything takes place over complex separable Hilbert spaces; time integration uses Lebesgue measure on \([0,\infty)\). The diagonal contraction semigroup is \((T(t)x)_j=e^{-\lambda_jt}x_j\) and the generating vector is \(\varphi_j=\sqrt{2\lambda_j}\in\ell^2\). Each finite Gram determinant is strictly positive. The claim is a fixed-parameter limit as \(N\to\infty\), **not** uniform as \(\alpha\to1\), and no eigenvalue-by-eigenvalue limit is asserted in the non-Bessel regime.

## Proof
**Exact determinant.** Direct integration gives \(G_{ij}=2\sqrt{\lambda_i\lambda_j}/(\lambda_i+\lambda_j)\). The Cauchy double-alternant identity yields
\[
\det G_N=\prod_{1\le i<j\le N}\left(\frac{\lambda_i-\lambda_j}{\lambda_i+\lambda_j}\right)^2,
\]
which is the displayed hyperbolic-tangent product after substituting the \(\lambda_j\).

**Stretched-scale regime.** Put \(F_c(u)=-2\log\tanh(cu/2)\) for \(u>0\), so \(F_c\) is nonnegative, decreasing, locally integrable with a logarithmic singularity at zero, and exponentially decreasing at infinity. Expansion of the two logarithms gives
\[
\int_0^\infty F_c(u)\,du
=2\int_0^\infty\{ -\log(1-e^{-cu})+\log(1+e^{-cu})\}\,du
=\frac{\pi^2}{2c}=:J_c.
\]
For \(0<\alpha<1\), set \(b_i=\alpha i^{\alpha-1}\) and \(S_i=\sum_{k\ge1}F_c((i+k)^\alpha-i^\alpha)\). We claim
\[
S_i\sim J_c/b_i=\frac{\pi^2}{2c\alpha}i^{1-\alpha}.
\]
For fixed \(R>0\), on \(1\le k\le R/b_i\) the mean-value theorem gives \(((i+k)^\alpha-i^\alpha)/(b_ik)=1+o(1)\) uniformly, because \(k/i=O(i^{-\alpha})\). The decreasing-function Riemann-sum theorem (valid with an integrable logarithmic singularity) therefore gives \(b_i\sum_{k\le R/b_i}F_c((i+k)^\alpha-i^\alpha)\to\int_0^R F_c(u)\,du\). To control the rest, concavity gives, for \(1\le k\le i\), \((i+k)^\alpha-i^\alpha\ge \alpha(2i)^{\alpha-1}k\); for \(k\ge i\), it gives \((i+k)^\alpha-i^\alpha\ge(2^\alpha-1)k^\alpha\). Monotonicity and exponential decay of \(F_c\) show that the part \(k>R/b_i\), multiplied by \(b_i\), is bounded by a constant multiple of \(\int_{aR}^\infty F_c(u)\,du+o(1)\), where \(a=2^{\alpha-1}>0\). Letting \(R\to\infty\) proves the claim, as well as the uniform bound \(S_i\le C(1+i^{1-\alpha})\).

Now \(-\log\det G_N=\sum_{i=1}^{N-1}\sum_{k=1}^{N-i}F_c((i+k)^\alpha-i^\alpha)\). For any fixed \(0<\delta<1\), the omitted tail \(k>N-i\) in rows \(i\le(1-\delta)N\) tends to zero in total faster than any power of \(N\): its smallest argument is bounded below by a positive constant times \(N^\alpha\), and its remaining tail has exponential decay. In the last \(\delta N\) rows the bound on \(S_i\) contributes at most \(O(\delta N^{2-\alpha})\). Thus, first letting \(N\to\infty\), then \(\delta\downarrow0\), and using \(\sum_{i\le N}i^{1-\alpha}\sim N^{2-\alpha}/(2-\alpha)\), gives the claimed constant.

**Geometric-scale regime.** If \(\alpha=1\), group factors by \(k=j-i\): \(-\log\det G_N=\sum_{k=1}^{N-1}(N-k)F_c(k)\). Since \(F_c(k)=O_c(e^{-ck})\), both \(\sum F_c(k)\) and \(\sum kF_c(k)\) converge absolutely, yielding \(\gamma(c)N-\beta(c)+O_c(Ne^{-cN})\). (The sign of the constant term is negative.)

**Supergeometric-scale regime and Fredholm limit.** If \(\alpha>1\), \(\lambda_j\) are distinct and \(G_{ij}=\operatorname{sech}((c/2)|j^\alpha-i^\alpha|)\). For \(j>i\), convexity yields \(j^\alpha-i^\alpha\ge\alpha i^{\alpha-1}(j-i)\). Hence \(\sum_{i<j}|G_{ij}|<\infty\), so \(G-I\) is trace class (write the matrix as a trace-norm-convergent sum of rank-one entries). If \(Wx=\sum_jx_jv_j=0\) in \(L^2\), the finite measure \(\sum_jx_j\sqrt{2\lambda_j}\,\delta_{\lambda_j}\) has zero Laplace transform. Absolute convergence follows from Cauchy–Schwarz and \(\sum_j\lambda_j<\infty\). The uniqueness of the Laplace transform of a finite measure gives \(x_j=0\) for every \(j\). Thus \(G=W^*W=I+K\) is injective; Fredholm index zero gives bounded invertibility. Positivity implies \(\det_{\mathrm F}G>0\), while \(\det G_N<1\) and its monotonically decreasing product converges to a strict value below one. Fredholm determinant continuity under trace-norm finite-section compression identifies the limit with \(\det_{\mathrm F}G\).

**Frame threshold.** For \(\alpha=1\), the full Gram matrix is Toeplitz with entries \(\operatorname{sech}(c|i-j|/2)\). Poisson summation gives its continuous symbol
\[
f_c(\theta)=\frac{2\pi}{c}\sum_{h\in\mathbb Z}\operatorname{sech}\!\left(\frac{\pi(\theta+2\pi h)}c\right)>0
\]
for real \(\theta\); its positive minimum and finite maximum give two-sided bounds. For \(\alpha>1\), bounded invertibility was shown above. For \(0<\alpha<1\), select blocks of \(L_i=\lfloor i^{1-\alpha}\rfloor\) successive indices starting at \(i\). Their pairwise phase differences \(j^\alpha-k^\alpha\) are uniformly bounded, so their positive Gram entries are bounded below by a constant independent of \(i\). Unit coefficient vectors constant on each block have Gram quadratic forms at least a constant times \(L_i\to\infty\), excluding any Bessel upper bound. The equivalence of Gram bounds with continuous-frame inequalities follows by identifying \(G\) with the matrix of the orbit analysis quadratic form.

## Verification
The included standalone checker numerically evaluates the Cauchy product and the finite Gram determinant independently, tests the exact \(\alpha=1\) finite-pair identity, checks the predicted normalized stretched-regime trends and supergeometric limit stabilization. These finite tests are only diagnostics; the proof above establishes the infinite assertions. All analytic interchanges use nonnegative functions or absolutely convergent sums. 

## Relationship to prior work
The qualitative frame/reconstruction distinction discussed by Berner, Herr and Jorgensen (arXiv:2611.03358, first submitted 2 November 2026) and the diagonal functional-calculus frames of Krishtal, Mashreghi and Miller (arXiv:2607.20798, first submitted 22 July 2026) motivate explicit Gram stability questions. The standard Carleson separation criterion already explains qualitatively why the geometrically spaced case has a Riesz bound; that is not claimed as new. The contribution here is the sharp finite-volume determinant rate through the previously nonuniform stretched, geometric and trace-class regimes, including its explicit \(\pi^2\) constant. Standard Cauchy determinant identities supply one ingredient, not the limit calculation. The other relevant continuous-semigroup frame literature concerns operator-model equivalences rather than these determinant asymptotics.

## Limitations
No uniform crossover estimate is established as \(\alpha\to1\), no universal eigenvalue distribution is claimed for the unbounded Gram regime, and no historical priority beyond the inspected literature can be certified. The determinant product and frame boundary derive from classical identities and standard separation theory; originality is confined to their precise joint asymptotic regime analysis for this natural spectral grid. External independent verification has not been performed.

## References
1. C. Berner, J. E. Herr and P. E. T. Jorgensen, *Frame properties of effective stationary sequences*, arXiv:2611.03358 (first submitted 2026-11-02). https://arxiv.org/html/2611.03358v2
2. I. Krishtal, J. Mashreghi and B. Miller, *Frames from Functional Calculus*, arXiv:2607.20798 (first submitted 2026-07-22). https://arxiv.org/abs/2607.20798
3. Classical Cauchy double-alternant determinant formula, and classical Fourier transform of the hyperbolic secant; both identities are stated explicitly in the proof.
