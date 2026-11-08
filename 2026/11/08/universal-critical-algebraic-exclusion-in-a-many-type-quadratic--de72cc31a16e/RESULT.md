# Universal critical algebraic exclusion in a many-type quadratic population map

## Finding

For any integer \(m\ge2\) and \(a>0\), define a homogeneous quadratic population map on the strictly positive cone of \(\mathbb R^{m+1}\):
\[
H_i(x)=\frac{\theta_i x_i}{2}\left(2\sum_{k=1}^{m+1}x_k-x_i\right),
\quad \theta_1=2a,\quad \theta_j=a\ (2\le j\le m+1).
\]
For the orbit \(x^{(t)}=H^{\circ t}(x^{(0)})\) and its population composition \(p_j^{(t)}=x_j^{(t)}/\sum_k x_k^{(t)}\), **every** strictly positive starting state has the same asymptotic critical extinction profile:
\[
\lim_{t\to\infty}t\bigl(1-p_1^{(t)}\bigr)=\frac{2m}{2m+1},\qquad
\lim_{t\to\infty}t p_j^{(t)}=\frac{2}{2m+1}
\quad(2\le j\le m+1).
\]
The universal constants are independent of the positive initial state and common coefficient \(a\). The first type approaches composition one; the \(m\) subordinate types approach zero at the exact inverse-time rate.

For comparison, replace \(\theta_1\) by \(ra\) while keeping all subordinate coefficients equal to \(a\). If \(r>2\), every strictly positive initial composition admits constants \(C_j\in(0,\infty)\) such that
\[
\lim_{t\to\infty}\left(\frac r2\right)^t p_j^{(t)}=C_j
\quad(2\le j\le m+1).
\]
If \(1-1/(2m)<r<2\), there is a strictly positive stationary composition
\[
p_1^*=\frac{2mr+1-2m}{1+mr},\qquad
p_j^*=\frac{2-r}{1+mr}\quad(2\le j\le m+1).
\]
At and above \(r=2\) no strictly positive stationary composition exists. This comparison locates a precise transition between a positive stationary composition, universal algebraic exclusion and geometric exclusion; it does **not** claim convergence to the interior stationary composition on the lower side.

## Assumptions and scope

Here \(m\) is any fixed integer at least two, \(t\) is an integer iteration index tending to infinity, and every component of \(x^{(0)}\) is strictly positive. No normalization or restriction on the total initial mass is required. All coordinates of every finite iterate of the homogeneous map remain positive. Population compositions are well-defined even on orbits whose absolute total mass tends to zero or diverges. The main asymptotic theorem treats exactly \(\theta_1=2a\) and \(\theta_j=a\); the supercritical statement treats all fixed \(r>2\). A zero initial subordinate coordinate is excluded: such a type stays zero, so the universal \(m\)-type coefficient need not hold.

## Proof

**Projective recursion.** Let \(p_i=x_i/\sum_kx_k\). Homogeneity cancels the total mass and common positive scale. For arbitrary \(r>0\), compositions evolve by
\[
F_i(p)=\frac{\vartheta_i p_i(2-p_i)}{\sum_k\vartheta_kp_k(2-p_k)},
\qquad \vartheta_1=r,\ \vartheta_j=1\ (j\ge2).
\]
All iterates remain strictly positive. Thus it suffices to study this self-map of the interior of the probability simplex.

**Monotone loss of total subordinate mass at criticality.** Set \(r=2\), write \(u=\sum_{j=2}^{m+1}p_j=1-p_1\) and \(B=\sum_{j=2}^{m+1}p_j^2\). Since \(0<u<1\) and \(0<B\le u^2\), direct substitution gives
\[
E=2+2u-2u^2-B,\qquad
p_j'=\frac{p_j(2-p_j)}{E},\qquad
u'=\frac{2u-B}{E},
\]
where the prime denotes one iteration. Consequently
\[
u-u'=\frac{(1-u)(2u^2+B)}{E}>0.
\]
The denominator satisfies \(1\le E\le4\). Hence \(u_t\) decreases to a limit \(u_\infty\in[0,1)\). If \(u_\infty>0\), then \(u_t-u_{t+1}\ge(1-u_0)2u_\infty^2/4>0\) for every \(t\), impossible. Therefore \(u_t\to0\).

**No premature summability and equalization.** The same identity gives \(u_t-u_{t+1}\le3u_t^2\). Once \(u_t\le1/6\), \(u_{t+1}\ge u_t/2\), whence
\[
0<\frac1{u_{t+1}}-\frac1{u_t}\le6.
\]
It follows that \(u_t\ge1/(C+6t)\) for some finite \(C>0\) and all sufficiently large \(t\); in particular \(\sum_tu_t=\infty\).

The scalar function \(v\mapsto v(2-v)\) is strictly increasing on \((0,1)\), so the ordering of the \(m\) subordinate coordinates is preserved. Let \(q_{\max,t}\) and \(q_{\min,t}\) be their maximal and minimal values, and put \(R_t=q_{\max,t}/q_{\min,t}\ge1\). The coordinate update gives
\[
R_{t+1}=R_t\frac{2-q_{\max,t}}{2-q_{\min,t}}\le R_t.
\]
If \(R_t\to R_\infty>1\), then for sufficiently large \(t\), \(q_{\max,t}-q_{\min,t}=q_{\max,t}(1-1/R_t)\ge c u_t\) for a constant \(c>0\), because \(q_{\max,t}\ge u_t/m\). Furthermore, since the derivative of \(\log v\) is at least \(1/2\) on \([1,2]\),
\[
\log R_t-\log R_{t+1}
=\log(2-q_{\min,t})-\log(2-q_{\max,t})
\ge \tfrac12(q_{\max,t}-q_{\min,t})
\ge\tfrac c2u_t.
\]
Summing contradicts \(\sum_tu_t=\infty\) and \(R_t\ge1\). Thus \(R_t\to1\), which implies
\[
\frac{p_j^{(t)}}{u_t}\to\frac1m
\quad(2\le j\le m+1),\qquad
\frac{B_t}{u_t^2}\to\frac1m.
\]

**Critical exponent and its constant.** The exact reciprocal increment is
\[
\frac1{u_{t+1}}-\frac1{u_t}
=\frac{(1-u_t)(2+B_t/u_t^2)}{E_t(u_{t+1}/u_t)}.
\]
As \(u_t\to0\), we have \(E_t\to2\), \(u_{t+1}/u_t=(2-B_t/u_t)/E_t\to1\), and \(B_t/u_t^2\to1/m\). Therefore the reciprocal increment converges to \(1+1/(2m)\). Summing the increments and applying the elementary Cesàro mean limit gives
\[
\lim_{t\to\infty}\frac1{t u_t}=1+\frac1{2m},\quad
\lim_{t\to\infty}t u_t=\frac{2m}{2m+1}.
\]
Multiplying by \(p_j^{(t)}/u_t\to1/m\) proves the critical formula for every subordinate coordinate.

**Geometric exclusion for \(r>2\).** Define \(w_{j,t}=p_j^{(t)}/p_1^{(t)}\). The exact ratio formula is
\[
\frac{w_{j,t+1}}{w_{j,t}}=\frac{2-p_j^{(t)}}{r(1+u_t)}
\le\frac2r=:\lambda<1.
\]
Therefore \(\sum_tu_t<\infty\), \(u_t\to0\), and \(p_1^{(t)}\to1\). Moreover
\[
\frac{w_{j,t+1}}{\lambda w_{j,t}}=\frac{1-p_j^{(t)}/2}{1+u_t}.
\]
Each factor is strictly positive and the sum over \(t\) of its absolute distance from one is finite, since \(\sum_t u_t<\infty\) and \(p_j^{(t)}\le u_t\). Thus its infinite product converges to a strictly positive finite limit, yielding \(\lambda^{-t}w_{j,t}\to C_j\in(0,\infty)\); because \(p_1^{(t)}\to1\), the same limit holds for \(\lambda^{-t}p_j^{(t)}\).

**Stationary-composition threshold.** In a strictly positive stationary composition all fitness factors \(\vartheta_i(2-p_i)\) must agree. The equality of subordinate weights forces their coordinates to equal some \(q>0\). With \(p_1=1-mq\), equal fitness reduces to \(r(1+mq)=2-q\). Consequently \(q=(2-r)/(1+mr)\) and \(p_1=(2mr+1-2m)/(1+mr)\), which are positive precisely when \(1-1/(2m)<r<2\). In particular, no strictly positive stationary composition exists at or above \(r=2\). This finishes the proof.

## Verification

The dependency-free `CHECK.py` derives the normalized map from the homogeneous map using exact rational arithmetic, checks algebraic drift identities and the interior stationary compositions exactly, and performs numerical tests in dimensions \(m=2,\dots,7\) to illustrate the critical inverse-time law and the supercritical ratio bound. The script prints a PASS line on success and raises on failure. These finite checks neither prove the infinite-time limits nor substitute for the analytic argument above.

## Relationship to prior work

Shoyimardonov and Rozikov introduced the same homogeneous quadratic operator and classified fixed points and local stability. Their first public preprint (20 September 2024) and the subsequent journal article analyze the low-dimensional global dynamics. In particular, the equality of a leading coefficient to twice another is recognized as a nonhyperbolic center-manifold boundary, but neither inspected text provides the all-dimensional universal inverse-time composition coefficient or the full strictly positive initial-state conclusion proved here. Previous projective-convergence statements in the positive-interior equilibrium regime do not imply the theorem: at this critical parameter the only candidate limiting composition is on the simplex boundary, so the needed interior-positivity hypothesis fails. The algebraic proof and the exact decay constants are the contribution, not the underlying operator or classical techniques.

## Limitations

This result is about **relative compositions**, not the absolute magnitude \(\sum_i x_i^{(t)}\), which may vary substantially with the initial mass because the map is homogeneous quadratic. It assumes all coordinates initially positive and equal subordinate coefficients. It does not establish the global attraction of the lower-parameter interior stationary composition, any uniform estimate as \(r\downarrow2\), or a full classification with unequal subordinate rates. The explicit transition may be a special case of an unidentified broader asymptotic theorem in discrete replicator dynamics; the literature comparison is not a proof of publication priority. No independent validation has been performed.

## References

1. S. K. Shoyimardonov and U. A. Rozikov, *Discrete-Time Dynamical Systems Generated by a Quadratic Operator*, arXiv:2409.13450v1, publicly posted 20 September 2024, https://arxiv.org/abs/2409.13450.
2. S. K. Shoyimardonov and U. A. Rozikov, same work, *Russian Journal of Nonlinear Dynamics* 21 (2025), 399–418, DOI:10.20537/nd250803, https://nd.ics.org.ru/nd250803/.
