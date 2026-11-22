# A universal logarithmic extinction clock on the synchronous critical branch of a rational competition recurrence

## Finding
For the critical symmetric species branch of a two-species rational delay recurrence, every positive synchronous initial history obeys a *two-term asymptotic clock* with an orbit-dependent finite residual:
\[
\frac{1}{u_n^2}=\frac{2n}{3}+\frac16\log n+C+o(1).
\]
The universal primary and lag-difference amplitudes are
\[
\sqrt n\,u_n\longrightarrow\sqrt{\frac32},\qquad
n^{3/2}(u_n-u_{n-1})\longrightarrow-\sqrt{\frac38}.
\]
In particular, a neutral fixed point's qualitative attraction alone does not determine the logarithmic correction in the original iteration clock.

## Assumptions and scope
The exact-real, discrete two-species system is
\[
 x_{n+1}=\frac{x_n+x_{n-1}}{2+y_ny_{n-1}},\qquad
 y_{n+1}=\frac{y_n+y_{n-1}}{2+x_nx_{n-1}},\quad n\ge0.
\]
For **every** \(a,b\in(0,\infty)\), take \(x_{-1}=y_{-1}=a\) and \(x_0=y_0=b\). Then \(x_n=y_n=u_n\) for all \(n\ge-1\), with scalar recurrence
\[
 u_{n+1}=R(u_n,u_{n-1}),\qquad R(s,t)=\frac{s+t}{2+st}.
\]
All denominator factors are strictly positive. Natural logarithms are used; the finite constant \(C=C(a,b)\) depends on the two initial values, but the coefficients \(2/3\), \(1/6\) and both amplitudes do not. The statement is an asymptotic as integer \(n\to\infty\), not an exact finite-iteration identity.

## Proof
**1. Global convergence on the positive synchronous branch.** If \(s,t>0\), then
\[
0<R(s,t)<\frac{s+t}{2}\le\max(s,t).
\]
Thus \(M_n=\max(u_n,u_{n-1})\) is nonincreasing. In fact \(M_{n+2}<M_n\). To exclude a positive limiting maximum, consider any convergent subsequence of pairs \((u_n,u_{n-1})\to(s,t)\) with \(\max(s,t)=L>0\). Both \(R(s,t)<L\) and \(R(R(s,t),s)<L\) hold (even if one input is zero). By continuity, the two-step running maximum is then strictly less than \(L\) along this subsequence, contrary to \(M_n\downarrow L\). Hence \(u_n\to0\).

**2. Consecutive-coordinate ratios tend to one.** Put \(r_n=u_n/u_{n-1}>0\) and \(t_n=u_nu_{n-1}\to0\). Direct substitution gives
\[
r_{n+2}=G_n(r_n),\qquad G_n(r)=\frac{1+(3+t_n)r}{(2+t_{n+1})(1+r)}.
\]
For sufficiently large \(n\), every \(G_n\) sends \((0,\infty)\) into the fixed compact interval \([1/3,2]\). On that interval
\[
G_n'(r)=\frac{2+t_n}{(2+t_{n+1})(1+r)^2}
\]
converges uniformly to \((1+r)^{-2}\), whose maximum is \(9/16<1\). Also \(G_n(1)\to1\). The contraction estimate for each parity subsequence gives \(r_n\to1\).

**3. The fifth-order slow graph, with a controlled remainder.** Define
\[
f(t)=t-\frac{t^3}{3}+\frac{t^5}{9}.
\]
Straight rational polynomial division gives the exact Taylor jet
\[
 R(f(t),t)-f(f(t))=-\frac{t^7}{27}+O(t^9),\qquad t\to0.
\]
Let \(e_n=u_{n+1}-f(u_n)\). The mean-value theorem applied to \(s\mapsto R(s,u_n)-f(s)\) shows
\[
 |e_{n+1}|\le q|e_n|+K u_n^7
\]
for all sufficiently large \(n\), where \(1/2<q<1\) can be chosen arbitrarily close to \(1/2\) and \(K<\infty\). Indeed
\[
 \partial_sR(s,t)=\frac{2-t^2}{(2+st)^2},\qquad
 \partial_sR(0,0)-f'(0)=-\frac12.
\]
Because \(u_{n+1}/u_n\to1\), choose \(\varepsilon>0\) and a late index so that \(u_{n+1}\ge(1-\varepsilon)u_n\) and \(q/(1-\varepsilon)^7<1\). Dividing the preceding inequality by \(u_{n+1}^7\) gives a uniformly contracting recursion for \(|e_n|/u_n^7\). Consequently \(e_n=O(u_n^7)\), so
\[
 u_{n+1}=u_n-\frac{u_n^3}{3}+\frac{u_n^5}{9}+O(u_n^7).
\]
This argument directly controls the stable lag mode; it does not merely assert a formal center-manifold expansion.

**4. The logarithmic clock.** Set \(w_n=u_n^{-2}\). The binomial expansion of the last step, with its proved remainder, gives
\[
w_{n+1}-w_n=\frac23+\frac{1}{9w_n}+O(w_n^{-2}).
\]
Since \(w_n\to\infty\), averaging the increments yields \(w_n/n\to2/3\). Therefore \(w_n=2n/3+O(\log n)\) and
\[
w_{n+1}-w_n=\frac23+\frac{1}{6n}+O\!\left(\frac{\log n}{n^2}\right).
\]
The error is summable, as is \(1/n-\log(1+1/n)\). Thus
\[
 C=\lim_{n\to\infty}\left(w_n-\frac{2n}{3}-\frac16\log n\right)
\]
exists and is finite. The leading amplitude follows from \(w_n/n\to2/3\). Finally, shifting the fifth-order step back one index gives
\[
 u_n-u_{n-1}=-\frac13u_{n-1}^3+O(u_{n-1}^5),
\]
and hence the asserted limit \(-\frac13(3/2)^{3/2}=-\sqrt{3/8}\). This completes the proof.

## Verification
The standalone, Python-standard-library checker `verify.py` evaluates the exact rational Taylor jets using fraction arithmetic. It confirms the \(-1/27\) seventh-order defect and the \(2/3\), \(1/9\) coefficients in the inverse-square expansion. It also reports finite diagnostics for four positive initial pairs at \(n=10^5\) and \(n=10^6\). These finite tests support arithmetic and reproducibility, but only the preceding analysis establishes the infinite-orbit conclusions.

## Relationship to prior work
Liu, Li and Zhong (2017), Theorem 13 and the preceding critical-parameter analysis, study the entire two-species system at \(p=q=2\) and identify convergence behavior and its axis equilibria. Qian and Shi (2011) study precisely the resulting one-species rational recurrence with general denominator parameter and establish qualitative stability, attractivity and absence of prime two-cycles. Those results provide qualitative context and cover the reduction, but the inspected theorem/proof sections do not state the present universal \(1/6\) logarithmic clock, finite inverse-square residual or lag-difference amplitude. The present result is a quantitative refinement of an established critical branch, not a claim that the recurrence or its convergence is new.

## Limitations
No global assertion is made for unequal species histories, where trajectories can approach nonzero axis equilibria. The constant \(C(a,b)\) is defined by an infinite limit rather than a closed form. No independent mathematical validation or uniqueness certification is claimed. The literature comparison is limited to the specified inspected sources and actual indexed searches; unindexed equivalent asymptotics may exist.

## References
- K. Liu, P. Li, W. Zhong, “Global Dynamics of Rational Difference Equations \(x_{n+1}=(x_n+x_{n-1})/(q+y_ny_{n-1})\) and \(y_{n+1}=(y_n+y_{n-1})/(p+x_nx_{n-1})\),” *Discrete Dynamics in Nature and Society* (2017), article 1295089; first public date 2017-05-03. https://doi.org/10.1155/2017/1295089
- X. Qian, Q.-h. Shi, “Qualitative behavior of a rational difference equation,” *Advances in Difference Equations* (2011), article 6; first public date 2011-06-03. https://doi.org/10.1186/1687-1847-2011-6
