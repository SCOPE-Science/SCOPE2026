# Exact mean-square jitter tolerance of heavy-ball acceleration

## Finding

Let \(H\) be a real symmetric positive-definite matrix with least and greatest eigenvalues \(0<\mu\le L\). For the quadratic \(f(x)=\tfrac12(x-x_\star)^\mathsf T H(x-x_\star)\), consider heavy-ball iteration with independent identically distributed scalar stepsize perturbations:
\[
e_{k+1}=\big[(1+\beta)I-\alpha(1+\xi_k)H\big]e_k-\beta e_{k-1},
\]
where \(e_k=x_k-x_\star\), \(0\le\beta<1\), \(\alpha>0\), \(\alpha L<2(1+\beta)\), \(\mathbb E\xi_k=0\), and \(\mathbb E\xi_k^2=s^2<\infty\). Each perturbation is independent of the initial pair and previous perturbations and is *common to all coordinates* within its step. Then for every deterministic initial pair, \(\mathbb E\|e_k\|_2^2\) decays geometrically to zero if and only if
\[
\boxed{s^2<\frac{2(1-\beta)}{\alpha L}-\frac{1-\beta}{1+\beta}.}
\]
At the boundary at least one deterministic initial pair fails to converge in mean square; above it at least one deterministic initial pair has exponentially unbounded second moments along a subsequence. The result is independent of every noise-distribution detail beyond mean zero and finite variance.

At the deterministic Chebyshev-optimal heavy-ball parameters
\[
\alpha_\star=\frac4{(\sqrt L+\sqrt\mu)^2},\qquad
\beta_\star=\left(\frac{\sqrt L-\sqrt\mu}{\sqrt L+\sqrt\mu}\right)^2,
\]
the sharp jitter-variance tolerance is
\[
\boxed{s^2<\frac2{\sqrt\kappa(\kappa+1)}},\qquad\kappa=L/\mu.
\]
In contrast, gradient descent using its deterministic minimax step \(2/(\mu+L)\) tolerates exactly \(s^2<1/\kappa\). For \(\kappa>1\), the heavy-ball tolerance is strictly lower by factor \(2\sqrt\kappa/(\kappa+1)\), asymptotically \(2/\sqrt\kappa\). This is a comparison of two *deterministically tuned* methods, not a claim about optimally robust retuning.

## Assumptions and scope

The state space is finite-dimensional real Euclidean space. The random sequence is iid, has zero mean and a finite nonnegative second moment, is independent of the deterministic initial pair, and is multiplied against the full gradient rather than separately sampled per eigendirection. The base heavy-ball parameters are deterministically Schur-stable on the entire Hessian spectrum, ensured by \(0\le\beta<1\) and \(0<\alpha L<2(1+\beta)\). Steps \(1+\xi_k\) are not assumed positive for the general theorem, although the exact counterexample below has strictly positive random steps. Geometric mean-square convergence refers to convergence of the full error for every deterministic \((e_0,e_{-1})\), with a geometric bound allowed to depend on the matrix, parameters and initialization.

## Proof

**Scalar reduction.** Diagonalize \(H\). Every curvature \(\lambda\in[\mu,L]\) obeys \(y_{k+1}=(a+\eta_k)y_k-\beta y_{k-1}\), where \(a=1+\beta-\alpha\lambda\), \(\eta_k=-\alpha\lambda\xi_k\), and \(v=\mathbb E\eta_k^2=(\alpha\lambda)^2s^2\). The second-moment map on symmetric matrices is
\[
\mathcal K_v(X)=MXM^\mathsf T+vX_{11}E,\quad
M=\begin{pmatrix}a&-\beta\\1&0\end{pmatrix},\quad E=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]
No cross-mode independence assumption is needed: summing the scalar modal second moments yields the squared Euclidean error.

**Exact positive-definite comparison.** The hypotheses imply \(|a|<1+\beta\). Put \(D=(1-\beta)[(1+\beta)^2-a^2]>0\) and
\[
W=\frac1D\begin{pmatrix}1+\beta&a\\a&1+\beta\end{pmatrix}\succ0.
\]
Direct multiplication gives \(W=MWM^\mathsf T+E\), \(W_{11}=(1+\beta)/D\), and
\[
\mathcal K_v^2(W)-W=(vW_{11}-1)\,[E+\mathcal K_v(E)].
\]
The bracket is positive definite: its determinant is \(1+v>0\) and its lower-right entry is one. Since \(\mathcal K_v\) preserves positive-semidefinite matrices, \(vW_{11}<1\) implies \(\mathcal K_v^2(W)\preceq(1-\varepsilon)W\) for some \(\varepsilon>0\), and thus geometric contraction of the moments for every deterministic initial state. At equality, \(\mathcal K_v(W)=W\), a nonzero fixed covariance; since \(W\) is a finite sum of rank-one initial covariances, at least one deterministic initial state fails mean-square convergence. If \(vW_{11}>1\), the same two-step comparison is \(\mathcal K_v^2(W)\succeq(1+\varepsilon)W\), and at least one deterministic initial pair has an exponentially growing subsequence of second moments.

Consequently the *exact* modal threshold is
\[
v<\frac{(1-\beta)[(1+\beta)^2-a^2]}{1+\beta},
\quad\text{equivalently}\quad
s^2<\frac{2(1-\beta)}{\alpha\lambda}-\frac{1-\beta}{1+\beta}.
\]
The right side decreases strictly with \(\lambda\); the largest eigenvalue \(L\) is therefore necessary and sufficient for all modes. Substitution of the classical Chebyshev-optimal parameters gives \(2/[\sqrt\kappa(\kappa+1)]\). For gradient descent, each modal mean-square factor is \((1-\alpha\lambda)^2+(\alpha\lambda)^2s^2\), and its exact upper-spectrum tolerance under \(\alpha=2/(\mu+L)\) is \(1/\kappa\).

**Strict rational separation.** Take \(H=\operatorname{diag}(1,9)\), and let \(\xi_k\) independently equal \(2/7\) or \(-2/7\) with probability \(1/2\) each. With \(\alpha_\star=1/4\), \(\beta_\star=1/4\), the high-curvature modal second-moment transfer matrix has characteristic polynomial
\[
\chi(z)=\frac{3136z^3-3648z^2+264z-49}{3136}.
\]
Since \(\chi(1)=-297/3136<0\), it has a real root greater than one and fails mean-square stability. With deterministic-minimax gradient descent \(\alpha=1/5\), the two modal squared-error factors are \(788/1225\) and \(1108/1225\), both strictly smaller than one. Both random stepsizes in this example are positive.

## Verification

The standalone file `verify_heavyball.py` uses SymPy exact symbolic algebra and Python rational-number enumeration. It checks the deterministic covariance identity, its determinant, the two-step semidefinite comparison, the cubic characteristic polynomial, the exact variance threshold, monotonicity across the full Hessian spectrum, Chebyshev endpoint simplifications, rational separation, and all \(2^k\) sign paths for \(0\le k\le8\) on selected deterministic initial states. `verify_output.txt` records an actual successful replay. The all-parameter and all-dimensional assertions are proved above; finite enumeration is not claimed as an infinite proof.

## Relationship to prior work

Bollapragada, Chen and Ward (2022) analyze accelerated minibatch heavy-ball through matrix-product bounds and sufficiently large minibatches. Loizou and Richtárik (2017) prove stochastic heavy-ball convergence under stochastic quadratic models and sufficient conditions. Dang, Babanezhad and Vaswani (2024) obtain noise-adaptive guarantees and batch-size thresholds for strongly convex quadratics. Velikanov, Kuznedelev and Yarotsky (2022) analyze a spectrally expressible minibatch stochastic-momentum class via generating functions; their specific noise covariance structure is not this general scalar common-jitter model. Hodgkinson and Mahoney (2020) develop qualitative multiplicative-noise recurrence and heavy-tail mechanisms, not the displayed exact threshold. Gürbüzbalaban and coauthors (2023) treat randomized stepsizes primarily for SGD. Mulayoff and Michaeli (2023) give exact SGD mean-square stability, not the momentum comparison here. The deterministic heavy-ball tuning itself and random-coefficient second-moment methods are classical and are not claimed as novel.

## Limitations

Only iid scalar common-stepsize fluctuations of a fixed SPD quadratic are treated, not correlated schedules, additive stochastic gradients, componentwise stochastic Hessians, nonquadratic functions, or data-dependent noise. The exact comparison concerns classical deterministic minimax tunings; a different momentum/stepsize choice can trade deterministic speed against robustness. Similar random-coefficient autoregressive Lyapunov criteria may exist in specialist literature; full historical uniqueness is not established. Independent mathematical review has not been performed.

## References

- Bollapragada, R., Chen, T., and Ward, R., *On the fast convergence of minibatch heavy ball momentum*, first arXiv posting 2022-06-15, https://arxiv.org/abs/2206.07553.
- Loizou, N., and Richtárik, P., *Linearly convergent stochastic heavy ball method for minimizing generalization error*, 2017, https://arxiv.org/abs/1710.10737.
- Hodgkinson, L., and Mahoney, M. W., *Multiplicative noise and heavy tails in stochastic optimization*, 2020, https://arxiv.org/abs/2006.06293.
- Velikanov, M., Kuznedelev, D., and Yarotsky, D., *A view of mini-batch SGD via generating functions: conditions of convergence, phase transitions, benefit from negative momenta*, 2022, https://arxiv.org/abs/2206.11124.
- Gürbüzbalaban, M., Hu, Y., Şimşekli, U., and Zhu, L., *Cyclic and Randomized Stepsizes Invoke Heavier Tails in SGD than Constant Stepsize*, 2023, https://arxiv.org/abs/2302.05516.
- Mulayoff, R., and Michaeli, T., *Exact Mean Square Linear Stability Analysis for SGD*, 2023, https://arxiv.org/abs/2306.07850.
- Dang, A., Babanezhad, R., and Vaswani, S., *(Accelerated) Noise-adaptive Stochastic Heavy-Ball Momentum*, 2024, https://arxiv.org/abs/2401.06738.
