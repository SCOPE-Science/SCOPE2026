# Sharp residual dependence of odd and even nonoverlined gaps in overpartitions

## Finding
Let \(\Pi_n\) be uniformly sampled from the \(\overline p(n)\) overpartitions of an integer \(n\geq0\). Let \(G_o\) and \(G_e\) be the least positive odd and even integers, respectively, that do **not** appear as nonoverlined parts of \(\Pi_n\). Define \(U_n=(G_o-1)/2\) and \(V_n=G_e/2-1\). Then for all integers \(r,s,n\geq0\),
\[
\Pr(U_n\ge r,\,V_n\ge s)=\frac{\overline p(n-r^2-s(s+1))}{\overline p(n)},
\]
where \(\overline p(t)=0\) for negative integers \(t\). For every \(n\), these variables are negatively quadrant dependent; for \(n\ge4\), their squared values have strictly negative covariance.

As \(n\to\infty\),
\[
\left(\frac{U_n^2}{\sqrt n},\frac{V_n^2}{\sqrt n}\right)
\Longrightarrow (E_1,E_2),
\]
where \(E_1,E_2\) are independent exponential variables with rate \(\pi/2\). Although the variables become asymptotically independent after scaling, their unscaled squared-gap covariance has the *sharp residual dependence law*
\[
\boxed{\operatorname{Cov}(U_n^2,V_n^2)\sim -\frac{4}{\pi^3}\sqrt n.}
\]
In particular, for fixed real \(x,y>0\), \(r=\lfloor x n^{1/4}\rfloor\), \(s=\lfloor y n^{1/4}\rfloor\),
\[
\log\frac{\Pr(U_n\ge r,V_n\ge s)}{\Pr(U_n\ge r)\Pr(V_n\ge s)}
=-\frac{\pi x^2y^2}{4\sqrt n}+O_{x,y}(n^{-3/4}).
\]

## Assumptions and scope
An overpartition permits at most one overlined copy of each positive part size, as well as any number of nonoverlined copies. A part occurring **only** overlined is absent for both statistics here. We do not require a part to be wholly absent. This is different from parity-restricted sums of the full overpartition minimal excludant. All random variables and probabilities are with respect to the uniform measure on overpartitions of fixed weight \(n\). The covariance theorem is an asymptotic for integer \(n\to\infty\), not a finite-size equality.

## Proof
**1. Exact two-parameter removal bijection.** The event \(U_n\ge r\) requires one nonoverlined copy of each \(1,3,\ldots,2r-1\); the event \(V_n\ge s\) requires one nonoverlined copy of each \(2,4,\ldots,2s\). Removing exactly those mandatory copies decreases the weight by
\[
1+3+\cdots+(2r-1)+2+4+\cdots+2s=r^2+s(s+1).
\]
The remaining object is an unrestricted overpartition; reinsertion reverses the operation, even when overlined copies of required sizes are also present. This proves the stated joint survival identity, including the empty and impossible cases.

**2. Finite-size repulsion.** Write \(P_n(t)=\overline p(n-t)/\overline p(n)\). Engel's overpartition log-concavity, with the initial coefficients \(1,2,4,8\) checked directly, implies for nonnegative integers \(A,B\)
\[
P_n(A+B)\le P_n(A)P_n(B).
\]
If \(A+B\le n\), this follows by multiplying the decreasing successive ratios of \(\overline p\); otherwise the left side is zero, and analogous boundary cases are immediate. Taking \(A=r^2\), \(B=s(s+1)\) proves negative quadrant dependence. For \(n\ge4\), the term \(r=s=1\) is strict by strict log-concavity at the intervening indices. The identity
\[
\operatorname{Cov}(U_n^2,V_n^2)
=\sum_{r,s\ge1}(2r-1)(2s-1)
\left[P_n(r^2+s(s+1))-P_n(r^2)P_n(s(s+1))\right]
\tag{1}
\]
follows from \(u^2=\sum_{r=1}^u(2r-1)\) and finiteness of all sums. Every summand is nonpositive, and for \(n\ge4\) at least one is strictly negative.

**3. Uniform second-order asymptotic.** The classical overpartition Rademacher expansion yields, for some \(c>0\) and large positive integers \(m\),
\[
\overline p(m)=\frac{e^{\pi\sqrt m}}{8m}
\left(1-\frac1{\pi\sqrt m}+O(e^{-c\sqrt m})\right).
\tag{2}
\]
Let \(f(t)=\pi\sqrt t-\log(8t)+\log(1-(\pi\sqrt t)^{-1})\). On \(t\in[n/2,n]\),
\[
f''(t)=-\frac\pi{4t^{3/2}}+O(t^{-2}).
\]
For \(A,B\ge1\) and \(A+B\le H\sqrt n\log n\), with any fixed \(H>0\), the exact double integral for the mixed difference of \(f\), and the exponentially small remainder in (2), give uniformly
\[
\begin{aligned}
\Delta_n(A,B)&=\log\frac{\overline p(n-A-B)\overline p(n)}{\overline p(n-A)\overline p(n-B)}\\
&=-\frac{\pi AB}{4n^{3/2}}
\left(1+O_H(\log n/\sqrt n)\right).
\end{aligned}
\tag{3}
\]
The four-point exponential errors are negligible relative to \(AB/n^{3/2}\), even for \(A=B=1\). Taylor expansion of the single-ratio logarithms yields
\[
P_n(A)P_n(B)=
\exp\left(-\frac\pi{2\sqrt n}(A+B)\right)
\left(1+O_H((\log n)^2/\sqrt n)\right).
\]
Combining this with \(e^{\Delta_n}-1=\Delta_n(1+O_H((\log n)^2/\sqrt n))\), we obtain the uniform **difference**, rather than only separate first-order approximations:
\[
\begin{aligned}
&P_n(A+B)-P_n(A)P_n(B)\\
&=-\frac{\pi AB}{4n^{3/2}}
\exp\left(-\frac\pi{2\sqrt n}(A+B)\right)
\left(1+O_H((\log n)^2/\sqrt n)\right).
\end{aligned}
\tag{4}
\]
The fixed-scale logarithmic dependence statement in the finding is the specialization of (3), using \(A=x^2\sqrt n+O(n^{1/4})\), \(B=y^2\sqrt n+O(n^{1/4})\).

**4. Uniform tail control.** The Rademacher leading term and monotonicity of \(\overline p\) imply absolute constants \(c_0,C_0>0\) such that
\[
0\le P_n(A)\le C_0 e^{-c_0 A/\sqrt n}\qquad(n\ge1,\ A\ge0).
\tag{5}
\]
For \(0\le A\le n/2\), compare (2) at \(n-A\) and \(n\), using \(\sqrt n-\sqrt{n-A}\ge A/(2\sqrt n)\); for \(n/2<A\le n\), monotonicity and comparison with \(\overline p(\lfloor n/2\rfloor)\) give an exponentially small bound. The case \(A>n\) is zero, and finitely many small \(n\) are absorbed into \(C_0\). By negative quadrant dependence, the absolute value of the bracket in (1) is at most \(P_n(A)P_n(B)\). There are at most \(O(n)\) weighted mass from each gap variable (\(U_n,V_n\le\sqrt n+1\)); hence the contribution of \(A+B>H\sqrt n\log n\) is \(O(n^2 n^{-c_0 H})\). Choosing a fixed sufficiently large \(H\) makes this \(o(\sqrt n)\). This also justifies extending the main term from (4) to the full positive quadrant.

**5. Evaluating the covariance constant.** Put \(a=\pi/2\). Standard Riemann sums (replace \(r\) by \(n^{1/4}t\)) show
\[
\begin{aligned}
\sum_{r\ge1}(2r-1)r^2 e^{-a r^2/\sqrt n}
&\sim\frac{n}{a^2}=\frac{4n}{\pi^2},\\
\sum_{s\ge1}(2s-1)s(s+1)e^{-a s(s+1)/\sqrt n}
&\sim\frac{n}{a^2}=\frac{4n}{\pi^2}.
\end{aligned}
\]
Substitute (4) in (1), use the uniform relative error and (5) to discard tails, and multiply the two Riemann sums. This gives
\[
\operatorname{Cov}(U_n^2,V_n^2)
\sim-\frac\pi{4n^{3/2}}\left(\frac{4n}{\pi^2}\right)^2
=-\frac4{\pi^3}\sqrt n.
\]
Finally, taking \(r\sim\sqrt{x}\,n^{1/4}\), \(s\sim\sqrt{y}\,n^{1/4}\) in the exact survival ratio and the single-term expansion from (2) gives \(\Pr(U_n^2/\sqrt n>x,\,V_n^2/\sqrt n>y)\to e^{-\pi(x+y)/2}\). Its product factorization identifies the asserted joint exponential weak limit, including the coordinate axes by continuity.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter (no external packages). The checker explicitly enumerates overpartitions through weight \(12\), comparing \(208\) two-parameter survival counts to the removal formula, and checks \(108036\) exact-integer negative-dependence inequalities through weight \(3000\). It also evaluates finite squared-gap covariances and compares them with the predicted constant. The recorded output is `verification-output.txt`. No finite test proves the limit: the analytic proof above does.

## Relationship to prior work
Aricheta and Donato established the **single**, all-size nonoverlined mex and least-multiplicity-gap generating functions; the forced-copy mechanism is acknowledged. Donato later considered alternative overlined/all-part definitions. Veena and Fathima's 2026 odd-mex statistic selects the **odd values of the full mex** and does not determine the least missing odd size, while Sarkar, Thejitha and Fathima's 2026 even-mex statistic similarly selects even values of a full-mex variable using presence of either overlined or nonoverlined parts. Bhoria, Eyyunni and Santra (2026) enumerate how many integers below the largest part are missing regardless of overlining, not the separate odd/even **nonoverlined** initial gaps. The present statistics search separately among odd and even **nonoverlined** sizes, and the result is their joint negative dependence and quantitative squared-gap covariance, not a marginal q-series identity. Engel's log-concavity and Mukherjee's finite-difference analysis, together with Sills's overpartition expansion, are prior analytical inputs. No claim is made that these ingredients are new. Full-text comparisons found no theorem specifying the joint two-color law or the covariance constant. Undiscovered equivalent general theorems of multiplicative measures on partitions remain a priority risk.

## Limitations
The covariance theorem does not give a finite-size closed formula without summation or a sharp universal remainder term. It does not cover a definition that counts overlined-only parts as present. The sign is strict for \(n\ge4\) for the **squared** gaps; we do not claim universal strictness for all other functionals. Computation is finite corroboration and independent mathematical audit has not been performed.

## References
1. V. M. R. Aricheta and J. A. L. Donato, *Minimal Excludant over Overpartitions*, arXiv:2309.04398, first posted 2023-09-08. https://arxiv.org/abs/2309.04398
2. J. A. Donato, *On Minimal Excludant over Overpartitions*, arXiv:2507.04402, first posted 2025-07-06. https://arxiv.org/abs/2507.04402
3. V. V. S. and S. N. Fathima, *On the sum of odd minimal excludants over overpartitions*, arXiv:2609.32207, first posted 2026-09-26. https://arxiv.org/abs/2609.32207
4. D. Sarkar, M. P. Thejitha and S. N. Fathima, *A Note On Certain Minimal Excludants Over Overpartitions*, arXiv:2609.21649, first posted 2026-09-18. https://arxiv.org/abs/2609.21649
5. B. Engel, *Log-concavity of the overpartition function*, arXiv:1412.4603; Ramanujan Journal 43 (2017). https://arxiv.org/abs/1412.4603
6. G. Mukherjee, *Inequalities for higher order differences of the logarithm of the overpartition function and a problem of Wang–Xie–Zhang*, arXiv:2204.00055; Research in Number Theory 9 (2023), article 9. https://arxiv.org/abs/2204.00055
7. A. V. Sills, *A Rademacher Type Formula for Partitions and Overpartitions*, International Journal of Mathematics and Mathematical Sciences (2010), article 630458. https://doi.org/10.1155/2010/630458
8. T. Y. He et al., *The r-chain minimal and maximal excludant sizes of an overpartition*, arXiv:2501.12864, first posted 2025-01-22. https://arxiv.org/abs/2501.12864
9. S. C. Bhoria, P. Eyyunni and S. Santra, *On the number of missing integers in partitions*, arXiv:2604.12557, first posted 2026-04-14; primary MSC 11P81/11P83/11P84. https://arxiv.org/abs/2604.12557
