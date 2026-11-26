# Simultaneous entropy and Nyström-trace optimal landmarks on screened cycles

## Finding

Let \(C_n\) be the simple, unweighted cycle on \(n\ge3\) labelled vertices, let \(L_n\) be its combinatorial Laplacian, and let \(K=(\mu I+L_n)^{-1}\), where \(\mu>0\). For any nonempty landmark set \(S\subseteq\{0,\ldots,n-1\}\), put
\[
\widetilde K_S=K_{:,S}K_{S,S}^{-1}K_{S,:},\qquad
E(S)=\operatorname{tr}(K-\widetilde K_S),\qquad
D(S)=\det K_{S,S}.
\]
Fix an integer budget \(1\le k\le n\). List the vertices of an arbitrary \(k\)-element \(S\) in cyclic order and let \(g_1,\ldots,g_k\) be its positive, cyclic successive arc lengths; then \(\sum_i g_i=n\). Write \(n=kq+r\) with \(0\le r<k\), and define
\[
F_0=1,\quad F_1=\mu+2,\quad
F_j=(\mu+2)F_{j-1}-F_{j-2}\quad(j\ge2),\qquad
f_j=\frac{\partial}{\partial\mu}\log F_j=\frac{F'_j}{F_j}.
\]
Then **the following three conditions are equivalent**:

1. \(S\) globally minimizes the trace error \(E\) among all \(k\)-element landmark sets.
2. \(S\) globally maximizes the principal determinant \(D\) among all \(k\)-element landmark sets.
3. Every cyclic gap belongs to \(\{q,q+1\}\), with exactly \(r\) gaps of length \(q+1\).

In particular, the optimum is independent of the screening parameter. Its values and number of labelled optimal subsets are exactly
\[
E_*=r f_q+(k-r)f_{q-1},\qquad
D_*=\frac{F_q^rF_{q-1}^{k-r}}{2(\cosh(n\theta)-1)},\qquad
N_*=\frac nk\binom{k}{r},
\]
where \(\theta=\operatorname{arcosh}(1+\mu/2)>0\). Every non-balanced gap pattern is strictly suboptimal on **both** criteria.

There is also a sharp second-best classification when \(n=kq\), \(2\le k<n\), and \(q\ge2\). The subsets achieving the smallest **strictly positive** trace excess, and simultaneously the largest **strictly suboptimal** determinant, are precisely those with one gap \(q-1\), one gap \(q+1\), and the other \(k-2\) gaps equal to \(q\). Their number is \(n(k-1)\), their trace excess is
\[
E_2-E_*=f_q+f_{q-2}-2f_{q-1}>0,
\]
and their determinant ratio is
\[
\frac{D_2}{D_*}=\frac{F_{q-2}F_q}{F_{q-1}^2}=1-\frac{1}{F_{q-1}^2}<1.
\]
Thus the leading determinant loss under the least damaging nonoptimal landmark displacement is explicit at every positive shift.

## Assumptions and scope

The cycle is a simple graph, with unit positive edge conductances and **uniform** positive vertex killing/screening \(\mu\). Vertices are labelled and observed exactly, without independent measurement noise. The Nyström approximation is the unrescaled, standard column-subset formula above; all inverses exist because \(\mu I+L_n\) is positive definite. The trace objective is the nuclear/trace norm of the positive-semidefinite Nyström residual. The determinant objective is the marginal covariance volume of the observed coordinates, equivalently the minimization of the conditional Gaussian entropy of the unobserved coordinates. These two different criteria are compared on the **same** kernel and over the same fixed-cardinality family.

The theorem does **not** assert the conclusion for arbitrary circulant kernels, weighted cycles, nonuniform screening, noisy observations, or generic graphs. Nor does it assert that a nested optimal chain across increasing budgets always exists.

## Proof

**1. Complementary precision identity.** Set \(A=\mu I+L_n\), \(T=V\setminus S\), and \(K=A^{-1}\). In the block partition \((S,T)\), the Schur complement of \(K_{S,S}\) in \(K\) is exactly \(A_{T,T}^{-1}\), by the block inverse identity. Therefore the residual \(K-\widetilde K_S\) has zero rows and columns on \(S\), while its \(T\times T\) block is \(A_{T,T}^{-1}\). Consequently
\[
E(S)=\operatorname{tr} A_{T,T}^{-1}.
\]
Jacobi's complementary principal-minor identity also gives \(D(S)=\det A_{T,T}/\det A\). Both statements hold for all \(1\le k\le n\), with the empty-matrix conventions \(\det(\varnothing)=1\) and \(\operatorname{tr}(\varnothing)=0\).

**2. Independent path segments.** Deleting the selected vertices from the cycle leaves \(k\) disjoint (possibly empty) paths of lengths \(m_i=g_i-1\). The corresponding principal precision block is tridiagonal on each path, with diagonal \(\mu+2\) even at endpoints and off-diagonal \(-1\). Its determinant \(F_m\) satisfies the stated continuant recurrence. Since \(\partial_\mu A_{T,T}=I\), Jacobi's determinant differentiation identity yields \(\operatorname{tr}A_{T,T}^{-1}=\partial_\mu\log\det A_{T,T}\). Hence the two exact decompositions are
\[
E(S)=\sum_{i=1}^k f_{g_i-1},\qquad
D(S)=\frac{\prod_{i=1}^k F_{g_i-1}}{\det A}.
\]
All factors are positive.

**3. Strict convexity for trace; strict concavity for determinant.** Let \(\theta>0\) satisfy \(\cosh\theta=1+\mu/2\). Solving the continuant recurrence gives
\[
F_m=\frac{\sinh((m+1)\theta)}{\sinh\theta},\qquad
f_m=\frac{(m+1)\coth((m+1)\theta)-\coth\theta}{2\sinh\theta}.
\]
For \(x>0\), let \(h(x)=x\coth(\theta x)\). Direct differentiation gives
\[
h''(x)=2\theta\operatorname{csch}^2(\theta x)
\bigl(\theta x\coth(\theta x)-1\bigr)>0.
\]
The final inequality follows from \(z\cosh z>\sinh z\) for every \(z>0\), since the difference has derivative \(z\sinh z>0\) and vanishes at zero. Thus \(m\mapsto f_m\) is a **strictly convex** integer sequence for every \(\mu>0\). On the other hand \(x\mapsto\log\sinh((x+1)\theta)\) has second derivative \(-\theta^2\operatorname{csch}^2((x+1)\theta)<0\) on \(x\ge0\), so \(m\mapsto\log F_m\) is **strictly concave**.

**4. Smoothing every unequal gap pair.** If two positive gaps obey \(g_i\ge g_j+2\), replacing them by \(g_i-1\) and \(g_j+1\) is feasible and preserves the gap sum. Strict discrete convexity gives a strict decrease in \(\sum_i f_{g_i-1}\), whereas strict discrete concavity gives a strict increase in \(\sum_i\log F_{g_i-1}\). Every composition of \(n\) into \(k\) positive parts is realizable by a cyclic landmark set, and repeated smoothing terminates at precisely the vectors with all parts differing by at most one. Conversely, any nonbalanced vector admits a strictly improving smoothing. This proves all global optimizer claims and all equality cases, without finite enumeration.

**5. Exact optimum, census, and runner-up.** At a balanced composition, \(r\) of the \(m_i\) equal \(q\), and \(k-r\) equal \(q-1\), proving the claimed optimum formulas except the denominator. The cycle precision eigenvalues are \(\mu+2-2\cos(2\pi j/n)\). Their product equals \(2(\cosh(n\theta)-1)\), by the standard Chebyshev product identity; alternatively, this follows from the two roots \(e^{\pm\theta}\) of the continuant recurrence. To count distinct labelled optima, choose one starting labelled vertex (\(n\) choices) and order the \(k\) gaps (\(\binom{k}{r}\) choices). Every selected subset is represented exactly \(k\) times, by the choice of its starting selected vertex, giving \(N_*=n\binom{k}{r}/k\).

Now suppose \(n=kq\), \(2\le k<n\). Every nonbalanced composition can be improved by strict smoothing until the constant composition is reached. At the step immediately preceding that endpoint, precisely one part is \(q-1\) and another is \(q+1\), all others being \(q\). Therefore such one-step compositions are simultaneously the best of all nonoptimal compositions for both criteria. They are distinct whenever the ordered positions of the two exceptional gaps differ, yielding \(nk(k-1)/k=n(k-1)\) labelled sets. Their objective differences follow by cancellation. Finally the continuant Wronskian identity
\[
F_m^2-F_{m-1}F_{m+1}=1\qquad(m\ge1)
\]
starts at \(m=1\) and is preserved by the recurrence, giving the stated exact determinant ratio.

As one practical consequence, the optimal designs need not be nested across budgets: on \(C_6\), every two-landmark optimum is an antipodal pair (gaps \(3,3\)), whereas every three-landmark optimum is one of the two alternating triples (gaps \(2,2,2\)); no such triple contains an antipodal pair.

## Verification

Run `python3 check.py` in a directory containing this file and `check.py` (Python 3 standard library only). The verifier reconstructs the continuants and their derivatives with exact fractions, exhaustively compares all landmark subsets on cycles of orders \(3\) through \(10\) at three rational screening parameters, checks optimum values, equality sets, and subset counts, and checks the sharp runner-up values when the order is a nontrivial multiple of the budget. For cycles through order \(7\), it separately constructs and inverts the actual precision and covariance matrices, verifies complementary principal minors, and checks direct Nyström Schur-complement traces for every subset at two rational shifts. It also verifies the nonnesting example on \(C_6\).

The verifier returned `PASS 8695 exact rational checks including all subsets at n<=10; independent n<=7 direct covariance comparisons` on the packaged source. **Finite tests do not establish the universal theorem**; the all-size and all-positive-parameter proof is the strict-convexity/concavity and balancing argument above.

## Relationship to prior work

Belabbas and Wolfe (2009, first arXiv version June 24, 2009) characterize Nyström trace errors using Schur complements and explain determinantal landmark selection; their general framework is used, but their paper does not supply the cycle-specific, all-budget simultaneous optimizer and equality classification, or the sharp second-best deficit. Guestrin, Krause and Singh (2005) motivate Gaussian-process sensor placement and mutual-information designs; their approach does not yield the finite-cycle formulas here. Baz, Alonso and Pérez-Fernández (2023) study correlation matrices of Gaussian Markov random fields on cycles, focusing on their construction and asymptotics rather than fixed-budget Nyström landmark selection.

Related continuous-interval Ornstein–Uhlenbeck optimal-design results can favor equidistant sampling for individual criteria, but neither the periodic discrete precision model nor the joint trace/determinant statement with integer gap census and runner-up ratio follows from the inspected formulations. More recent general masked-circular-Gaussian-process analyses concern arbitrary covariances and measurement noise, and should not be confused with an exact landmark optimality classification for the particular noiseless screened-Laplacian kernel. Publication priority beyond the inspected sources remains uncertain.

## Limitations

The classification requires exact observations, an unweighted cycle, and strictly positive **uniform** screening; other covariance models need new proofs and may have different optimizers. It is not a comparison to unconstrained best rank-\(k\) spectral approximation. The runner-up formula is claimed only when the cycle order is a nontrivial multiple of the landmark budget. The theorem establishes no complexity lower bounds, guarantees for noisy observations, or independent formal certification. The finite checker supports reproducibility but does not certify the infinite parameter range.

## References

1. C. Guestrin, A. Krause and A. P. Singh, *Near-optimal sensor placements in Gaussian processes*, ICML (2005), 265–272. DOI: 10.1145/1102351.1102385. https://mlanthology.org/icml/2005/guestrin2005icml-near/
2. M.-A. Belabbas and P. J. Wolfe, *On landmark selection and sampling in high-dimensional data analysis*, arXiv:0906.4582v1 (June 24, 2009); Phil. Trans. R. Soc. A **367** (2009), 4295–4312. https://arxiv.org/abs/0906.4582
3. J. Baz, P. Alonso and R. Pérez-Fernández, *Correlation matrices of Gaussian Markov random fields over cycle graphs*, Linear Algebra and its Applications **663** (2023), 32–61. DOI: 10.1016/j.laa.2022.12.028.
4. K. Sikolya and S. Baran, *On the optimal designs for the prediction of complex Ornstein–Uhlenbeck processes*, Communications in Statistics – Simulation and Computation, first arXiv:1808.03444 (2018). https://arxiv.org/abs/1808.03444
5. J. Tsuzurugi, *Finite-Mask Gaussian-Process Reconstruction on a Periodic Sensor Ring: Mask-Geometry Dependence, Fourier-Mode Coupling, and Posterior Trace*, arXiv:2609.14007 (2026). https://arxiv.org/abs/2609.14007
