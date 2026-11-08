# Unique ordered switching for minimax diagonal actuator scheduling

## Finding

Consider a stable diagonal system whose input budget allows exactly one coordinate actuator at almost every time. Under distinct decay rates, its unique (up to measure-zero changes) finite-horizon schedule minimizing **worst-case terminal control energy** has only one contiguous operating interval per coordinate. In backward time, the fastest-decaying coordinate is served first and the slowest-decaying last; all resulting diagonal controllability-Gramian entries equal a common optimum.

More precisely, let \(n\ge2\), \(T>0\), and \(\lambda_1>\lambda_2>\cdots>\lambda_n>0\). There exists a unique sequence
\[
0=s_0<s_1<\cdots<s_n=T
\]
and a unique \(m>0\) satisfying
\[
\int_{s_{i-1}}^{s_i}e^{-2\lambda_i s}\,ds=m
\qquad(1\le i\le n).
\]
The globally optimal schedule activates coordinate \(i\) on backward-time interval \([s_{i-1},s_i)\). Its terminal controllability Gramian is exactly \(mI_n\), so its maximum unit-terminal-target minimum control energy is \(1/m\). Every other measurable one-active-coordinate schedule has strictly larger worst-case energy unless it agrees with this schedule almost everywhere.

The switching times can be found by **one scalar bisection**, using the recursion
\[
e^{-2\lambda_i s_i}=e^{-2\lambda_i s_{i-1}}-2\lambda_i m,
\qquad s_0=0,
\]
with \(s_n=T\). For example, for \((\lambda_1,\lambda_2)=(2,1)\) and \(T=1\), the backward-time switch is \(s_1\approx0.339745983209385\) and \(m\approx0.185769576481720\); the guaranteed worst-case unit-target energy is approximately \(5.38301275665772\).

## Assumptions and scope

Consider \(\dot z(t)=-\operatorname{diag}(\lambda_1,\dots,\lambda_n)z(t)+B_{\sigma(t)}u(t)\) for \(0\le t\le T\), where \(B_i=e_i\), \(\sigma:[0,T]\to\{1,\dots,n\}\) is any measurable *preselected schedule*, and at each time exactly the selected scalar input \(u(t)\in\mathbb R\) can act. The energy of a control is \(\int_0^T|u(t)|^2dt\). We optimize the maximum, over terminal offsets of Euclidean norm one, of the minimum energy required to reach that offset from the freely evolving initial state. Schedules that do not control every coordinate have infinite worst-case energy. The theorem applies to the continuous-time, fixed-horizon, time-invariant, decoupled stable diagonal setting with unit input gain and arbitrarily fast switching; there is no switching penalty or mandatory dwell time.

Write backward time \(s=T-t\) and \(\hat\sigma(s)=\sigma(T-s)\). The terminal controllability Gramian is
\[
W_\sigma=\operatorname{diag}(w_1,\dots,w_n),\qquad
w_i=\int_0^T\mathbf1_{\{\hat\sigma(s)=i\}}e^{-2\lambda_i s}\,ds.
\]
When \(w_i>0\) for all \(i\), the minimum-energy formula is \(y^\mathsf TW_\sigma^{-1}y\), and its maximum over \(\|y\|_2=1\) is \(1/\min_iw_i\). Thus the problem is exactly \(\max_\sigma\min_iw_i\).

## Proof

**1. Existence and uniqueness of the equal-mass intervals.** For \(\lambda>0\), set \(F_\lambda(s)=(1-e^{-2\lambda s})/(2\lambda)\). For a candidate mass \(m\ge0\), start with \(s_0(m)=0\) and define the first \(n-1\) cuts successively by
\[
F_{\lambda_i}(s_i(m))=F_{\lambda_i}(s_{i-1}(m))+m,
\qquad 1\le i<n,
\]
while these cuts remain below \(T\). Each defined \(s_i(m)\) is continuous and strictly increasing in \(m\), with \(s_i(0)=0\) and \(s_{i-1}(m)<s_i(m)\) for positive \(m\). Initially all cuts are zero. As \(m\) increases, the last cut \(s_{n-1}(m)\) must approach \(T\) at some finite threshold: if an earlier cut reaches \(T\), all later cuts are already strictly larger, so the last cut has reached \(T\) earlier. For \(m\) below that threshold define
\[
H(m)=\int_{s_{n-1}(m)}^T e^{-2\lambda_n s}\,ds-m.
\]
This function is continuous and strictly decreasing, starts at \(H(0)=F_{\lambda_n}(T)>0\), and approaches a negative number as \(s_{n-1}(m)\uparrow T\) because \(m>0\). Therefore it has exactly one root. The corresponding cuts satisfy \(0<s_1<\cdots<s_{n-1}<T\) and, with \(s_n=T\), all \(n\) interval masses equal the same positive \(m\). The scalar recursion is precisely this construction.

**2. A global dual certificate.** Define positive weights \(p_i\) by \(p_1=1\) and
\[
\frac{p_{i+1}}{p_i}=\exp\!\bigl(-2(\lambda_i-\lambda_{i+1})s_i\bigr),
\qquad 1\le i<n,
\]
then normalize them so \(\sum_i p_i=1\). Define \(g_i(s)=p_i e^{-2\lambda_i s}\). The logarithms \(\log g_i(s)=\log p_i-2\lambda_i s\) are affine with strictly increasing slopes as \(i\) increases. Adjacent lines cross at \(s_i\). Since \(s_1<\cdots<s_{n-1}\), the upper envelope equals \(g_i(s)\) strictly inside \((s_{i-1},s_i)\), with equality only at the finitely many endpoints. One can see this for any pair \(i<j\): their crossing time is
\[
\frac{\log p_i-\log p_j}{2(\lambda_i-\lambda_j)}
=\frac{\sum_{\ell=i}^{j-1}(\lambda_\ell-\lambda_{\ell+1})s_\ell}
{\sum_{\ell=i}^{j-1}(\lambda_\ell-\lambda_{\ell+1})},
\]
a positive-weighted average of the intervening adjacent switch times. Hence no nonadjacent line can displace \(g_i\) in its designated interval.

For any competing measurable schedule \(\tau\), the elementary inequalities
\[
\min_i w_i(\tau)\le \sum_i p_i w_i(\tau)
=\int_0^Tg_{\hat\tau(s)}(s)\,ds
\le\int_0^T\max_i g_i(s)\,ds
=\sum_i p_i m=m
\]
establish global optimality. The constructed schedule attains equality and its Gramian equals \(mI_n\).

**3. Uniqueness and energy.** The strict upper-envelope selection is unique at every \(s\) except the finitely many switch times. Thus equality in the second inequality above forces the competing schedule to equal the constructed one almost everywhere. The minimum-energy controllability formula then gives exactly \(\max_{\|y\|_2=1}y^\mathsf TW^{-1}y=1/m\). This proves the asserted unique global optimal schedule and value, not merely stationarity or a relaxed design.

## Verification

The standalone \(\texttt{verify.py}\) in this package computes the proposed switching times using scalar bisection for 60 test systems with \(2\le n\le6\), checks equalized Gramian entries, verifies the weighted upper-envelope certificate at 401 interior times per system, and compares against randomized measurable step schedules. It uses only Python's standard library and prints \(\texttt{VERIFY_OK 25620}\). These finite tests are independent numerical checks of the exact formulas, not a substitute for the global analytic proof. Reproduce with \(\texttt{python3 verify.py}\).

## Relationship to prior work

Actuator scheduling with a pointwise sparsity budget and a worst-case-control-energy criterion is an established design question. Ballotta, Joseph and Rahul Thete (arXiv:2407.12125) formulate pointwise-sparse discrete-time scheduling, explicitly list inverse minimal Gramian eigenvalue as the worst-case energy measure, and give feasible greedy/MCMC methods, without an exact continuous-time ordered-switch classification. Kondapi, Sriram, Joseph and Murthy (arXiv:2506.18514, first posted June 23, 2025) analyze time-varying-support discrete-time control, primarily optimizing trace-inverse Gramian and developing approximate greedy guarantees. Ballotta et al.'s 2026 survey (arXiv:2610.09787, initial preprint October 7, 2026) confirms the contemporary relevance of actuator scheduling and minimal-energy control, but only its metadata/abstract were available for direct comparison here. The present theorem addresses a different, explicit continuous-time subclass with a worst-case rather than trace-inverse objective; none of the inspected source statements supplies its ordered intervals, one-dimensional equal-mass recursion, or uniqueness certificate.

Related fixed-actuator-covariance design (Trélat and Zuazua, arXiv:2609.37081) studies time-independent actuator ranks and gain budgets, not the stated time-varying one-channel support. Its abstract was available but not its full text, leaving a historical-priority limitation rather than warranting an assertion about uninspected details. The dual weighted-envelope argument uses elementary minimax design ideas; the novelty assessment concerns their sharp global schedule classification in this specific control model, not the generic control-Gramian formula or the idea of maximizing its smallest eigenvalue.

## Limitations

The theorem applies only to scalar unit gains, diagonal stable generators with *distinct* positive rates, continuous time, no switching costs or dwell limits, and a fixed actuator schedule chosen in advance. It does not address coupled systems, multiple simultaneous actuators, discrete-grid implementation, state-dependent scheduling, noise, robust uncertainty, or fixed stationary actuator covariance. The bound is an exact analytic theoretical optimum; numerical root evaluations are illustrative and not independently certified. Relevant unindexed results in optimal experimental design or older time-sharing control may contain equivalent formulations; full historical-priority certification is not claimed. Independent mathematical validation has not been performed.

## References

1. K. P. V. S. Kondapi, C. Sriram, G. Joseph, and C. R. Murthy, *Discrete-Time Linear Dynamical System Control Using Sparse Inputs With Time-Varying Support*, arXiv:2506.18514v1, first submitted 2025-06-23, https://arxiv.org/abs/2506.18514.
2. L. Ballotta, G. Joseph, and I. R. Thete, *Pointwise-Sparse Actuator Scheduling for Linear Systems With Controllability Guarantee*, arXiv:2407.12125v1 (2024), https://arxiv.org/abs/2407.12125.
3. L. Ballotta et al., *Sparsity in control problems: Recent trends and open challenges*, arXiv:2610.09787v1, first submitted 2026-10-07, https://arxiv.org/abs/2610.09787.
4. E. Trélat and E. Zuazua, *Optimal Actuator Design across Ranks and Control Horizons*, arXiv:2609.37081 (2026), https://arxiv.org/abs/2609.37081.
