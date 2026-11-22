# Likelihood-ratio ordering and sharp discretization bias for two half-logistic count laws

## Finding
The survival-preserving and density-mimicking count analogues of the same continuous half-logistic model are not interchangeable. For every \(\theta>0\), the first is strictly smaller in likelihood-ratio order than the second. At high resolution (\(\theta\downarrow0\)), their mass-sign crossover occurs at scaled count \(\log3\), their total-variation discrepancy is \(\theta/16+O(\theta^2)\), and their mean discrepancy tends to the nonzero constant \((1-\log2)/2\). At low resolution (\(\theta\to\infty\)), both total variation and mean discrepancy have leading term \(2e^{-\theta}\).

## Assumptions and scope
Fix \(\theta>0\), write \(q=e^{-\theta}\), and define the finite positive normalizer
\[
Z_\theta=\sum_{j=0}^{\infty}\frac{q^j}{(1+q^j)^2}.
\]
For each integer \(n\ge0\), define the two probability masses
\[
a_n=\frac{2(1-q)q^n}{(1+q^n)(1+q^{n+1})},\qquad
b_n=\frac{q^n}{Z_\theta(1+q^n)^2}.
\]
Both sum to one: \(a_n\) telescopes as the survival-preserving discretization and \(b_n\) is normalized density sampling. Denote by \(A_\theta\), \(B_\theta\) the respective nonnegative-integer random variables. Define \(d_{TV}=\frac12\sum_{n\ge0}|a_n-b_n|\). Statements apply to all \(\theta>0\), with no shape generalization.

## Proof
**Exact order and crossover.** Cancellation gives
\[
\frac{a_n}{b_n}=K_\theta\frac{1+q^n}{1+q^{n+1}},\qquad K_\theta=2(1-q)Z_\theta.
\]
For \(0<q<1\), the map \(t\mapsto(1+t)/(1+qt)\) has derivative \((1-q)/(1+qt)^2>0\); because \(q^n\) strictly decreases, the likelihood ratio strictly decreases with \(n\). Since its \(b_n\)-weighted average is one and the ratio is nonconstant, its first value exceeds one and its limit falls below one. Hence the mass difference has a unique positive-to-negative sign transition, with at most one zero at an integer index. This proves strict likelihood-ratio order, implies strict usual stochastic order, and yields the exact identity
\[
d_{TV}=\sum_{n=0}^{k_\theta}(a_n-b_n)=\Pr(A_\theta\le k_\theta)-\Pr(B_\theta\le k_\theta),
\quad k_\theta=\max\{n\ge0:a_n\ge b_n\}.
\]

**High-resolution limit.** Set \(g(y)=e^{-y}/(1+e^{-y})^2\), for \(y\ge0\). Its integrals are \(\int_0^\infty g(y)\,dy=1/2\) and \(\int_0^\infty yg(y)\,dy=\log2\). Euler–Maclaurin summation, with exponentially integrable derivatives, gives
\[
Z_\theta=\frac{1}{2\theta}+\frac18+O(\theta),\qquad
K_\theta=1-\frac\theta4+O(\theta^2).
\]
Uniformly over integer \(n\ge0\), with \(y=\theta n\),
\[
\frac{a_n}{b_n}=1+\theta\left(\frac{e^{-y}}{1+e^{-y}}-\frac14\right)+O(\theta^2),\quad
b_n=2\theta g(y)(1+O(\theta)).
\]
The leading likelihood-ratio sign changes exactly at \(e^{-y}=1/3\), hence the unique discrete crossing obeys \(\theta k_\theta\to\log3\). Summing the positive portion and using an exponentially dominated Riemann-sum expansion yields
\[
\lim_{\theta\downarrow0}\frac{d_{TV}}\theta
=\int_0^{\log3}\!2g(y)\left(\frac{e^{-y}}{1+e^{-y}}-\frac14\right)dy
=\int_{1/3}^{1}\frac{3t-1}{2(1+t)^3}\,dt=\frac1{16}.
\]
The uniform smooth expansions and exponentially decaying derivatives bound the remainder by \(O(\theta^2)\), including the single crossing cell.

For the expectations, Euler–Maclaurin also gives
\[
\mathbb EA_\theta=\sum_{n\ge1}\frac2{1+e^{n\theta}}=\frac{2\log2}{\theta}-\frac12+O(\theta),
\]
\[
\sum_{n\ge0}n g(n\theta)=\frac{\log2}{\theta^2}+O(1),\quad
\mathbb EB_\theta=\frac{2\log2}{\theta}-\frac{\log2}{2}+O(\theta).
\]
Subtracting yields the stated constant \((1-\log2)/2\).

**Low-resolution limit.** With \(q=e^{-\theta}\downarrow0\), directly expand \(Z_\theta=1/4+q+O(q^2)\), hence \(a_0=1-2q+O(q^2)\), \(b_0=1-4q+O(q^2)\), \(\mathbb EA_\theta=2q+O(q^2)\), and \(\mathbb EB_\theta=4q+O(q^2)\). By the one-crossing property the total variation equals the zero-mass difference for sufficiently small \(q\), giving \(2q+O(q^2)\) for both quantities.

## Verification
Run the standalone `check.py` using Python with SymPy and mpmath. It verifies exact monotonicity algebra, exact integrals of the logistic kernel, the \(1/16\) integral, and high-precision finite-grid reproductions at three parameter values. Numerical tests support, but do not replace, the analytic uniform expansions and sign argument.

## Relationship to prior work
Barbiero and Hitaj (2024) introduced and studied the survival-preserving and the density-mimicking laws in separate papers, including their marginal shape, estimation, and reliability properties. Their earlier alternative construction based on Cramér discrepancy is a different discretization and is not the density-sampling law compared here. The present result concerns joint distributional ordering and exact discretization bias, not the already known definitions or the generic monotone-likelihood-ratio principle for log-concave sampling kernels. The explicit \(\log3\), \(1/16\), and \((1-\log2)/2\) constants require the present model-specific asymptotic computation.

## Limitations
The result does not compare fitted parameters, generalized shape models, or any Cramér-distance-optimal discretization. It does not infer that one discretization is universally preferable for data fitting. Historical priority has been assessed against accessible source texts and database searches, not certified independently.

## References
Barbiero, A. and Hitaj, A., *Discrete half-logistic distributions with applications in reliability and risk analysis*, Annals of Operations Research (first online 19 January 2024), DOI: 10.1007/s10479-023-05807-3.

Barbiero, A. and Hitaj, A., *A Discrete Version of the Half-Logistic Distribution Based on the Mimicking of the Probability Density Function*, Journal of the Indian Society for Probability and Statistics (online 6 April 2024), DOI: 10.1007/s41096-024-00185-w.

Barbiero, A. and Hitaj, A., *An Alternative Discrete Analogue of the Half-Logistic Distribution*, Proceedings of International Mathematical Sciences (31 December 2023), DOI: 10.47086/pims.1346708.
