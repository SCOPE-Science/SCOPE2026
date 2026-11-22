# Three exact noise-correlation phases for the optimal order of a three-step geometric SGD ladder

## Finding
For the scalar quadratic \(f(y)=y^2/2\), consider three additive-noise gradient steps, performed once each with normalized learning rates \(x\), \(2x\), and \(4x\), where \(0<x\le1/4\). Let the successive zero-mean oracle errors have a stationary covariance \(\operatorname{Cov}(\xi_i,\xi_j)=\sigma^2\rho^{|i-j|}\), with \(\sigma^2>0\) and \(-1<\rho<1\). We optimize the final expected squared error \(\mathbb E[y_3^2]\) over the six fixed permutations of these three learning rates, from any deterministic initial value.

Define the two rational phase boundaries
\[
\rho_-(x)=-\frac{x(24x^2-24x+7)}{1-4x^2},\qquad
\rho_+(x)=\frac{x}{2(1-x)(1-2x)}.
\]
Throughout the stated range, \(-1<\rho_-(x)<0<\rho_+(x)<1\). Denote by \(142\), for instance, the chronological rates \((x,4x,2x)\). Then the complete minimizer classification is:

* For \(-1<\rho<\rho_-(x)\), the **unique** optimal order is \(142\).
* For \(\rho_-(x)<\rho<\rho_+(x)\), the **unique** optimal order is \(421\) (descending rates).
* For \(\rho_+(x)<\rho<1\), the **unique** optimal order is \(412\).
* At \(\rho=\rho_-(x)\), precisely \(142\) and \(421\) tie for the minimum; at \(\rho=\rho_+(x)\), precisely \(421\) and \(412\) tie.

The result does **not** require jointly Gaussian errors: their means and displayed covariance suffice. The same classification minimizes the expected quadratic objective, since it is one half of the stated mean-square error.

As a concrete fully rational instance, at \(x=1/5\) the thresholds are \(\rho_-=-79/105\) and \(\rho_+=5/24\). At \(\rho=-9/10\), the optimal \(142\) has final variance \(628\sigma^2/15625\), compared with \(1217\sigma^2/15625\) under descending order. At \(\rho=1/2\), the optimal \(412\) has variance \(7699\sigma^2/15625\), compared with \(8049\sigma^2/15625\) for descending order.

## Assumptions and scope
Let \(y_0\in\mathbb R\) be deterministic. For \(k=0,1,2\), the update is
\[
y_{k+1}=y_k-h_k(y_k+\xi_k)=(1-h_k)y_k-h_k\xi_k.
\]
Each \((h_0,h_1,h_2)\) is a permutation of \((x,2x,4x)\). No independence across the three oracle errors is assumed; in particular, unconditional zero means must not be conflated with conditional unbiasedness. The Toeplitz covariance given above is positive definite for \(|\rho|<1\). The final deterministic error is common to all permutations. The result is a finite-horizon, three-query theorem, not a convergence assertion about an infinite learning-rate sequence. The first date among the cited motivating sources is 2019-04-29.

## Proof
**1. Exact bias and covariance formula.** By iterating the recursion, for every order \(p=(a,b,c)\) with \(\{a,b,c\}=\{1,2,4\}\),
\[
y_3=P(x)y_0-\sum_{j=0}^2w_j\xi_j,
\quad P(x)=(1-x)(1-2x)(1-4x),
\]
where
\[
(w_0,w_1,w_2)=\bigl(ax(1-bx)(1-cx),\; bx(1-cx),\;cx\bigr).
\]
Consequently
\[
\mathbb E[y_3^2]=P(x)^2y_0^2+\sigma^2F_{abc}(x,\rho),
\]
\[
F_{abc}=w_0^2+w_1^2+w_2^2+2\rho(w_0w_1+w_1w_2)+2\rho^2w_0w_2.
\]
Since \(w_0+w_1+w_2=1-P(x)\) does not depend on order, all six variance polynomials agree at \(\rho=1\). Hence every difference \((F_p-F_q)/(1-\rho)\) is affine in \(\rho\).

**2. The two changes of winner.** Direct expansion gives two exact polynomial identities
\[
F_{142}-F_{421}=-4x^2(\rho-1)\bigl[\rho(1-4x^2)+24x^3-24x^2+7x\bigr],
\]
\[
F_{412}-F_{421}=4x^2(\rho-1)\bigl[\rho(4x^2-6x+2)-x\bigr].
\]
The unique zeros within \((-1,1)\), respectively, are \(\rho_-(x)\) and \(\rho_+(x)\). Their strict range and separation follow from the five exact polynomial-positivity checks in the standalone verifier.

**3. Exclusion of all other orders over whole intervals.** Let \(I_1=[-1,\rho_-]\), \(I_2=[\rho_-,\rho_+]\), and \(I_3=[\rho_+,1]\), with proposed winners \(142\), \(421\), and \(412\). For each of the three winners and all five other orders \(q\), the expression
\[
D_{q,p}(x,\rho)=\frac{F_q(x,\rho)-F_p(x,\rho)}{1-\rho}
\]
is affine in \(\rho\). Positivity on each interval is therefore equivalent to positivity at its two endpoints, a total of 30 exact rational inequalities in \(x\). All 30 are established by the `verify.py` certificate: substitute \(x=t/4\), clear an explicitly positive denominator, and expand the numerator in the Bernstein basis on \(0\le t\le1\). Every Bernstein coefficient is a nonnegative exact rational number, proving each inequality for the *entire continuum* of \(x\), without sampling. Nonzero certificates are strictly positive for \(0<t\le1\) (each has a positive coefficient and a positive value at \(t=1\)). The comparisons with the other four orders are strict even at the two winner-crossing boundaries. Thus the minimizer classification, including tie multiplicities, is exhaustive.

**4. Why three steps is the first possible reversal.** With two distinct positive learning rates \(a>b\), curvature one, and correlation \(\rho<1\), direct expansion gives
\[
\operatorname{Var}(y_2\mid(a,b))-\operatorname{Var}(y_2\mid(b,a))
=2\sigma^2ab(a-b)(\rho-1)<0.
\]
The deterministic biases again coincide, so descending learning-rate order always wins with two steps. The two non-descending phases in the theorem first become possible at three steps.

## Verification
The self-contained exact-SymPy verifier `verify.py` derives all six variances from the specified update, confirms the two displayed identities, proves five threshold-range inequalities, certifies the full set of 30 endpoint comparisons using exact Bernstein coefficients, and tests the generic two-step identity. It also checks 12 strict rational phase-interior examples and both stated rational variance benchmarks. Execute with Python 3.10 or newer and `sympy>=1.11`:

```bash
python verify.py
```

Expected output begins `PASS: 30 exact Bernstein endpoint comparisons`. This symbolic certificate is the proof of the endpoint positivity lemma; finite examples alone do not prove the continuum statement. An exact finite sequence does not imply anything about an infinite-horizon learning-rate schedule.

## Relationship to prior work
Ge, Kakade, Kidambi, and Netrapalli [1] motivate geometrically decreasing steps and last-iterate analysis but do not establish a colored-noise permutation phase diagram for a fixed finite multiset. Lang, Zhang, and Xiao [2] study an adaptive learning-rate-drop procedure, not all orders of a prescribed three-step ladder. Doan, Nguyen, Pham, and Romberg [3] analyze Markovian gradient sampling and finite-time convergence bounds but not this exact terminal variance optimizer. Hu, Doshi, and Eun [4] compare asymptotic SGD efficiency under dependent input sequences; their covariance ordering does not assert the present three-step all-permutation thresholds. A published result for temporally independent oracle noise proves descending step order minimizes finite-horizon quadratic noise risk [5]; its independent-noise hypothesis corresponds only to \(\rho=0\) here and does not settle either correlated phase. These comparisons are statements of implication under differing hypotheses, not claims of priority based solely on differing titles. No independent historical-priority audit has been performed.

## Limitations
The ratio between the three rates is fixed at \(1:2:4\), and their largest normalized rate is at most one. The noise covariance is the stationary AR(1) second-moment form, not an arbitrary colored spectrum. The proof says nothing about correlated oracle **conditional** means, online adaptive schedules, momentum, nonquadratic losses, multidimensional Hessians, or horizons beyond three. The normalizations of curvature and noise variance are essential to interpreting the thresholds. Earlier equivalent derivations not identified by the cited comparisons remain possible.

## References
1. Rong Ge, Sham M. Kakade, Rahul Kidambi, Praneeth Netrapalli. *The Step Decay Schedule: A Near Optimal, Geometrically Decaying Learning Rate Procedure For Least Squares*. arXiv:1904.12838 (first public 2019-04-29). https://arxiv.org/abs/1904.12838
2. Hunter Lang, Pengchuan Zhang, Lin Xiao. *Using Statistics to Automate Stochastic Optimization*. arXiv:1909.09785 (first public 2019-09-21). https://arxiv.org/abs/1909.09785
3. Thinh T. Doan, Lam M. Nguyen, Nhan H. Pham, Justin Romberg. *Finite-Time Analysis of Stochastic Gradient Descent under Markov Randomness*. arXiv:2003.10973 (first public 2020-03-24). https://arxiv.org/abs/2003.10973
4. Jie Hu, Vishwaraj Doshi, Do Young Eun. *Efficiency Ordering of Stochastic Gradient Descent*. arXiv:2209.07446 (first public 2022-09-15). https://arxiv.org/abs/2209.07446
5. *Descending spectral steps minimize every terminal quadratic noise risk*. Published research record, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-descending-spectral-steps-minimize-every-terminal-quadratic-nois--2f7a38830384
