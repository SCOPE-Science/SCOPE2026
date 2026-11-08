# A sharp finite-horizon load reversal for a two-state stochastic battery

## Finding

A two-state battery with a **fixed load during a prescribed discharge window** has exactly one load maximizing its mean delivered work. More sharply, the optimal load is strictly monotone as the allowed discharge duration changes, and the sign of that monotonicity reverses at an explicit, rate-independent thermodynamic threshold.

Let \(\beta,E,k,t>0\), let \(p\in(p_{\rm eq},1]\), where \(p_{\rm eq}=(1+e^{\beta E})^{-1}\), and define
\[
\Phi_p=E+\beta^{-1}\log\frac{p}{1-p}\quad (p<1),\qquad \Phi_1=+\infty.
\]
Let \(w\ge0\) be a constant load that remains unchanged throughout the discharge interval \([0,t]\). When the initial probability of occupying the excited state is \(p\), the expected net work delivered to the load is
\[
\mathcal W_t(w)
=w\left[p-\frac{1}{1+e^{\beta(E-w)}}\right]
\left[1-e^{-2kt\cosh(\beta(E-w)/2)}\right]. \tag{1}
\]
For every \(t>0\), equation (1) has a **unique positive global maximizer** \(w_*(t)\), lying in \((0,\Phi_p)\). Its complete duration-dependence classification is
\[
\begin{array}{c|c}
\beta E>2(2p-1)&w_*(t)\text{ strictly increases with }t\\
\beta E=2(2p-1)&w_*(t)=E\text{ for all }t>0\\
\beta E<2(2p-1)&w_*(t)\text{ strictly decreases with }t.
\end{array} \tag{2}
\]
The equality case is possible only for \(p>1/2\). At that boundary the single load \(w=E\) is optimal for **every finite discharge duration and every kinetic rate \(k>0\)**. For \(p\le1/2\), the first case necessarily applies.

For complete initial occupation \(p=1\), the limiting loads also have exact forms:
\[
\lim_{t\downarrow0}w_*(t)=\frac2\beta,\qquad
\lim_{t\to\infty}w_*(t)=\frac{1+W_0(e^{\beta E-1})}{\beta}, \tag{3}
\]
where \(W_0\) is the principal Lambert function. Formulae (2)--(3) concern *total mean net work at a fixed deadline*, not instantaneous maximum power or unrestricted time-varying load control.

## Assumptions and scope

A continuous-time two-state Markov system has excited-state indicator \(X\in\{0,1\}\) and internal state energies \(0,E\). With constant mechanical load \(w\), the transitions are
\[
0\to1:\quad k_{01}(w)=k e^{-\beta(E-w)/2},\qquad
1\to0:\quad k_{10}(w)=k e^{\beta(E-w)/2}. \tag{4}
\]
These obey the local detailed-balance relation \(k_{10}/k_{01}=e^{\beta(E-w)}\). The rate prefactor \(k\) is fixed independently of \(w\); changing the load changes both rates through symmetric exponential splitting. The initial excited-state probability \(p\) is fixed and exceeds its zero-load thermal equilibrium value. At a positive fixed horizon \(t\), each net \(1\to0\) event transfers work \(w\), and each \(0\to1\) event transfers work \(-w\). No switching cost, gate cost, or leakage during an earlier storage stage is included. Controls cannot change \(w\) within the horizon.

If \(p<1\), the positive-work load interval is precisely \(0<w<\Phi_p\); on \(w>\Phi_p\) the expected work is negative. If \(p=1\), all finite positive loads produce positive mean work. The result holds for arbitrary admissible real parameters without a near-equilibrium approximation.

## Proof

**1. Exact work law.** The master equation under (4) is
\[
\frac{d}{ds}\mathbb EX_s=k_{01}(1-\mathbb EX_s)-k_{10}\mathbb EX_s
=-\lambda_w(\mathbb EX_s-\pi_w),
\]
where \(\lambda_w=k_{01}+k_{10}=2k\cosh(\beta(E-w)/2)\) and \(\pi_w=k_{01}/\lambda_w=(1+e^{\beta(E-w)})^{-1}\). Hence \(\mathbb EX_t=\pi_w+(p-\pi_w)e^{-\lambda_wt}\). Pathwise, for finite Markov jump counts, \(N_{10}(t)-N_{01}(t)=X_0-X_t\). Thus the expected work is \(w[p-\mathbb EX_t]\), proving (1) exactly, including reverse transitions. This identity is not an approximation by first jumps only.

**2. Global strict log concavity.** Set \(x=\beta(w-E)\), \(s=2kt\), \(c(x)=\cosh(x/2)\), and \(h_s(c)=(1-e^{-sc})/c\). On the positive-work interval,
\[
\mathcal W_t(w)=\frac w2\,[p-(1-p)e^x]e^{-x/2}h_s(c(x)). \tag{5}
\]
Let \(A(y)=1-y/(e^y-1)\) for \(y>0\). Then \(A(y)>0\) and
\[
A'(y)=\frac{e^y(y-1)+1}{(e^y-1)^2}>0,
\]
because the numerator starts at zero and has derivative \(ye^y>0\). Direct differentiation gives
\[
\frac{d}{dx}\log h_s(c(x))=-\frac12\tanh(x/2)A(sc(x)),
\]
\[
\frac{d^2}{dx^2}\log h_s(c(x))=-\frac14\left[\operatorname{sech}^2(x/2)A(sc(x))
+sc(x)\tanh^2(x/2)A'(sc(x))\right]<0. \tag{6}
\]
Moreover, \(\log w\) is strictly concave for \(w>0\), and \(\log[p-(1-p)e^{\beta(w-E)}]\) is concave on its positive domain (strictly so for \(p<1\)); the remaining term \(-x/2\) is affine. Equation (5) is therefore strictly log-concave in \(w\) wherever \(\mathcal W_t(w)>0\).

At \(w=0\), mean output is zero. For \(p<1\), the output also tends to zero as \(w\uparrow\Phi_p\); it is negative for larger loads. For \(p=1\), equation (1) tends to zero as \(w\to\infty\), since \(p-\pi_w\sim e^{-\beta(w-E)}\). Hence an interior maximizer exists and strict log-concavity proves uniqueness globally.

**3. Sign and monotonicity of the optimum.** The logarithmic first-order condition is \(F(w,t)=0\), where
\[
F(w,t)=\frac1w-\frac{\beta(1-p)e^x}{p-(1-p)e^x}-\frac\beta2
-\frac\beta2\tanh(x/2)A(2kt\cosh(x/2)). \tag{7}
\]
Equation (6) implies \(\partial_wF<0\). As \(A\) is strictly increasing, \(\partial_tF\) has sign opposite to \(w-E\) for \(w\ne E\), so by implicit differentiation, \(\operatorname{sgn}(dw_*/dt)=-\operatorname{sgn}(w_*-E)\).

For \(p>1/2\), \(E\) lies inside the positive-work domain and
\[
F(E,t)=\frac1E-\frac{\beta}{2(2p-1)}, \tag{8}
\]
independently of \(k,t\). Since \(F\) decreases strictly with \(w\), equation (8) places the unique optimum above, exactly at, or below \(E\) according as \(\beta E\) is below, equal to, or above \(2(2p-1)\). Its time derivative then has the signs in (2). For \(p\le1/2\), \(\Phi_p\le E\); every admissible optimum is below \(E\) and strictly increases with time, again in agreement with (2). The equality case is precisely \(w_*(t)=E\) for all positive times.

**4. Fully occupied limit.** At \(p=1\), equation (7) simplifies to
\[
\frac{1}{\beta w}-\frac12-\frac12\tanh\left(\frac{\beta(w-E)}2\right)
A\left(2kt\cosh\left(\frac{\beta(w-E)}2\right)\right)=0. \tag{9}
\]
For \(t\downarrow0\), \(A(y)\to0\), giving \(w_*(0+)=2/\beta\). For \(t\to\infty\), \(A(y)\to1\), and (9) becomes \(\beta w=1+e^{\beta(E-w)}\). Rearranging gives \(\beta w-1=W_0(e^{\beta E-1})\). Strict monotonicity of the left-hand side in (9), together with interior bounds on its unique root, justifies passage to both limits. This proves (3) and the theorem.

## Verification

The accompanying `verify_load.py` independently computes net expected work in two ways: from the solution of the master equation and from the exact two-state transition probabilities. It brackets the analytic stationary point, checks its global comparisons with other positive-work loads, and tests duration monotonicity on deterministic parameter families including the exact all-horizons boundary. Run with `python3 verify_load.py`. Its finite tests complement, but are not used as a replacement for, the all-parameter proof (5)--(9).

## Relationship to prior work

Lin, Liu, and Ma introduced the active-matter battery model, the local detailed-balance discharge rates, and an optimization of *instantaneous* discharge power at fixed state of charge (their equations (11)--(15)). Their result does not by itself optimize the net output after the occupation evolves over a prescribed duration under one unchanging load. The present finding uses their rate model to resolve that separate fixed-horizon problem, obtaining strict global uniqueness and the load-direction boundary (2). The independent circuit-based, multistage constant-current optimization of Liu, Lin, and Ma considers different dynamical and control objects and does not imply (2). General stochastic heat-engine efficiency results concern cyclic machines rather than this finite-horizon two-state load theorem. Exact two-state matrix exponentials and detailed balance are standard; neither is claimed as novel by itself.

## Limitations

This is a theorem for the idealized, symmetric-rate-splitting two-state Markov model with a **constant load** and a fixed initial marginal. It does not optimize arbitrary time-dependent feedback loads, guarantee positive work on each trajectory, include fuel or state-preparation cost, or establish physical implementation of exact rate splitting for arbitrarily high loads. The finite-horizon optimum generally differs from the instantaneous-power-optimal load. The limiting case \(p=1\) is an ideal fully excited initial preparation. Independent external review has not been performed, and overlap with inaccessible or unlocated broader literature remains a priority risk.

## References

1. Y.-Q. Lin, R.-H. Liu, and Y.-H. Ma, *Active-Matter Battery*, arXiv:2610.00428v1, first publicly submitted 30 September 2026, https://arxiv.org/html/2610.00428 .
2. R.-H. Liu, Y.-Q. Lin, and Y.-H. Ma, *Finite-Time Thermodynamics of Battery Discharging: Power-Efficiency Trade-Off and Optimization*, arXiv:2607.03157v1, first publicly submitted 3 July 2026, https://arxiv.org/abs/2607.03157 ; *Entropy* 28 (2026), 852, https://doi.org/10.3390/e28080852 .
3. T. Schmiedl and U. Seifert, *Efficiency at maximum power: An analytically solvable model for stochastic heat engines*, *EPL* 81 (2008), 20003, https://doi.org/10.1209/0295-5075/81/20003 .
