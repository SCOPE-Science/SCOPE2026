# Sharp frame-bound offsets and conditioning regrets for the two-sided exponential Gabor window

## Finding

Let \(g(t)=e^{-|t|}\), which has unit \(L^2(\mathbb R)\) norm. For integer redundancy \(n\ge2\), take the rectangular lattice \((\eta/n)\mathbb Z\times\eta^{-1}\mathbb Z\) with \(\eta>0\). Let \(A_n(\eta)\) and \(B_n(\eta)\) be the sharp lower and upper frame bounds divided by \(n\). Write \(\eta_{A,n}\) for the maximizer of \(A_n\) and \(\eta_{B,n}\) for the minimizer of \(B_n\); these optimizers are known to exist uniquely [1]. As integer \(n\to\infty\),
\[
 \eta_{A,n}=2\log n+\log6+O((\log n)^2/n^2),\qquad
 \eta_{B,n}=2\log n+\log3+O((\log n)^2/n^2).
\]
Define \(J_A(s)=\tfrac23s+4e^{-s}\) and \(J_B(s)=\tfrac43s+4e^{-s}\). With convergence uniform for \(s\) in each compact real interval,
\[
\begin{aligned}
 \frac{n^2}{\log n}\big[A_n(\eta_{A,n})-A_n(2\log n+s)\big]
 &\longrightarrow J_A(s)-J_A(\log6),\\
 \frac{n^2}{\log n}\big[B_n(2\log n+s)-B_n(\eta_{B,n})\big]
 &\longrightarrow J_B(s)-J_B(\log3).
\end{aligned}
\]
Both limiting losses are nonnegative with unique zeros at the respective minimizing offsets. In particular the lower-bound-optimal and upper-bound-optimal parameters differ asymptotically by \(\log 2\).

Now use the **previously established** condition-number optimizer \(\eta_{K,n}=2\log n+\log4+O((\log n)^2/n^2)\) for \(K_n=B_n/A_n\) [2]. Its limiting additive gaps to the upper- and lower-bound optimizers are \(\eta_{K,n}-\eta_{B,n}\to\log(4/3)\) and \(\eta_{A,n}-\eta_{K,n}\to\log(3/2)\). The resulting sharp individual frame-bound regrets are
\[
\begin{aligned}
 \lim_{n\to\infty}\frac{n^2}{\log n}\big[A_n(\eta_{A,n})-A_n(\eta_{K,n})\big]
 &=\frac13+\frac23\log\frac23>0,\\
 \lim_{n\to\infty}\frac{n^2}{\log n}\big[B_n(\eta_{K,n})-B_n(\eta_{B,n})\big]
 &=\frac43\log\frac43-\frac13>0.
\end{aligned}
\]

## Assumptions and normalization

Use \(M_\omega T_xg(t)=e^{2\pi i\omega t}g(t-x)\) and the unweighted sum of squared Gabor analysis coefficients. The physical sharp bounds in this convention are \(nA_n,nB_n\). For \(h=\eta\), \(x=h/n\), the exact normalized formulas [1, §8, Eq. (8.2)] are
\[
 A_n(h)=\tanh(h/2)\big[x\operatorname{csch}x-h\operatorname{csch}h\big],\qquad
 B_n(h)=\coth(h/2)\big[x\coth x+h\operatorname{csch}h\big].
\]
The factor \(1/n\) in the normalization can be seen from the Walnut multiplier: the physical frame operator has coefficients \(h\sum_k g(t-kh/n)g(t-kh/n-\ell h)\) for translation by \(\ell h\); its scalar multiplier at integer redundancy acquires a prefactor \(h/n\) after division by \(n\). This normalization does not move either optimizer or change the condition number. All logs are natural. No assertions are made for other windows, noninteger redundancy, nonrectangular lattices, or loss convergence uniformly over unbounded offsets.

## Proof

Put \(L=\log n\) and write \(h=2L+s\) on a fixed strip \(|s|\le C\). There \(x=h/n=O_C(L/n)\) and \(v=e^{-h}=O_C(n^{-2})\). The exact formulas give
\[
\begin{aligned}
 A_n(h)&=1-h^2/(6n^2)-2(1+h)v+O_C(h^4/n^4),\\
 B_n(h)&=1+h^2/(3n^2)+2(1+h)v+O_C(h^4/n^4),\\
 A_n'(h)&=(h/n^2)\big[-1/3+2e^{-s}\big]+O_C(h^3/n^4),\\
 B_n'(h)&=(h/n^2)\big[2/3-2e^{-s}\big]+O_C(h^3/n^4).
\end{aligned}
\]
Indeed \(x\operatorname{csch}x=1-x^2/6+O(x^4)\) and \(x\coth x=1+x^2/3+O(x^4)\); their Taylor remainders are analytic and differentiate to \(O(x^3/n)\) with respect to \(h\). The two prefactors expand as \(1\mp 2v+O(v^2)\), and \(h\operatorname{csch}h=2hv+O(hv^3)\). Their remainders, represented by convergent series in \(v\), differentiate to \(O(v^2)\) and \(O((1+h)v^3)\). Products with \(x^2\) contribute \(O_C(h^2/n^4)\) to the derivatives as well. This proves the derivative estimates without differentiating an unspecified error bound.

The leading brackets have roots \(s_A=\log6\) and \(s_B=\log3\), respectively. Taking \(C\) large enough, the derivatives have opposite signs at \(2L+s_i\pm1\) with the appropriate maximum or minimum sign pattern. From [1, §8], for all sufficiently large \(n\), the global optimizer of \(A_n\) is in \((\operatorname{arccosh}n,4\operatorname{arccosh}n)\), and \(\log A_n\) is strictly concave there; \(B_n\) is strictly convex on \((0,\infty)\). Both bracketing points belong to that interval for large \(n\). The sign brackets therefore contain the respective global optimizers. At the optimizer, division of the derivative equation by \(h/n^2\) makes the leading bracket \(O_C(L^2/n^2)\). Its slope as a function of \(s\) is bounded away from zero on the bracket. The location estimates follow by the mean-value theorem.

Substituting \(h=2L+s\) in the first two expansions gives, uniformly for bounded \(s\),
\[
 n^2(1-A_n(2L+s))=\tfrac23L^2+LJ_A(s)+O_C(1),\qquad
 n^2(B_n(2L+s)-1)=\tfrac43L^2+LJ_B(s)+O_C(1).
\]
Subtract the respective optimal value and divide by \(L\). The optimal offsets tend to \(s_A,s_B\) and lie on the same bounded strips, giving the uniform loss limits. Since \(J_A''=J_B''=4e^{-s}>0\), their unique minima are at the displayed roots. The previously known \(\eta_{K,n}\) has offset tending to \(\log4\); uniform convergence allows evaluation along that sequence. Evaluating \(J_A(\log4)-J_A(\log6)\) and \(J_B(\log4)-J_B(\log3)\) gives the two coefficients. Both are positive by strict convexity and the distinct offsets.

## Verification and relation to prior work

The companion `check_gabor.py` can be run with Python 3 and `mpmath`. Its finite tests sample the bound expansions, derivatives, optimizer locations, truncated Walnut multipliers, and regrets. Some tests also check the previously known condition-number behavior. These diagnostics are not proofs of the uniform limits or of priority.

Faulhuber and Shafkulovska [1] provide the exact functions, optimizer uniqueness, and finite-redundancy convexity and localization. The earlier symmetric-window high-density result [2] already gives the \(\log4\) offset with the same remainder order and, through its uniform expansion, the centered condition-number profile. Neither is claimed here; the increment is the separate lower- and upper-frame-bound asymptotics and the two individual penalties at the known condition-number-optimal lattice. The asymmetric fixed unequal-tail case [3] uses a different logarithmic centering and is not uniform towards equal rates. Historical priority for the distinct symmetric-window increment remains provisional.

1. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, [arXiv:2204.02917v2](https://arxiv.org/html/2204.02917v2), Theorem 2.7 and §8.
2. *High-density logarithmic balancing for optimal two-sided-exponential Gabor frames*, [Resultary record](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-high-density-logarithmic-balancing-for-optimal-two-sided-exponen--f41cc49ca05f/RESULT.md), finding and Eqs. (3)–(7).
3. *A logarithmic-logarithmic lattice law for asymmetric exponential Gabor frames*, [Resultary record](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-a-logarithmic-logarithmic-lattice-law-for-asymmetric-exponential--9ccc03766e12/RESULT.md), finding and assumptions.
