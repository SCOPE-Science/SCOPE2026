# Modal isotropy is the sharp infinitesimal diminishing-returns boundary for LQR actuator additions

## Finding

For a stable diagonal continuous-time linear system with an isotropic quadratic state cost, the sign of the leading interaction between two additional actuator channels is governed by an explicit symmetric kernel. This kernel is positive semidefinite for **every pair of actuator directions** if and only if all decay rates coincide. With unequal rates, two weak actuator channels can be strictly complementary: their combined decrease of the optimal average LQR cost exceeds the sum of their separate decreases, despite stability of the uncontrolled system.

More precisely, put \(\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\), with \(\lambda_i>0\), and let \(u,v\in\mathbb R^n\) be arbitrary fixed channel directions. For \(t,s\ge0\), let \(P(t,s)\) be the positive definite stabilizing solution of
\[
-\Lambda P-P\Lambda-P(tuu^{\mathsf T}+svv^{\mathsf T})P+I=0.
\]
Define \(F(t,s)=\operatorname{tr}P(0,0)-\operatorname{tr}P(t,s)\) and its additivity defect
\[
\Delta(t,s)=F(t,0)+F(0,s)-F(t,s).
\]
Then as \((t,s)\to(0,0)\) through the nonnegative quadrant,
\[
\Delta(t,s)=ts\sum_{i,j=1}^{n}K_{ij}(u_iv_i)(u_jv_j)+O(ts(t+s)),
\quad K_{ij}=\frac{\lambda_i^2+\lambda_j^2}{8\lambda_i^3\lambda_j^3(\lambda_i+\lambda_j)}.
\]
The following are equivalent: (a) the displayed quadratic coefficient is nonnegative for all \(u,v\); (b) \(K\) is positive semidefinite; (c) all \(\lambda_i\) are equal. Under condition (c), the coefficient equals \((u^{\mathsf T}v)^2/(8\lambda^5)\). If any two modal rates differ, there are fixed \(u,v\) for which \(\Delta(t,t)<0\) for all sufficiently small \(t>0\).

For the smallest possible dimension, \(n=2\), the exact witness \(\Lambda=\operatorname{diag}(1,2)\), \(u=(1,1)^{\mathsf T}\), \(v=(1,-4)^{\mathsf T}\) gives
\[
\Delta(t,t)=-\frac{t^2}{48}+O(t^3).
\]
Here negative defect means **complementarity**, whereas positive defect means diminishing returns. This is a local-in-strength classification, not a claim of global submodularity for arbitrary actuator strengths.

## Assumptions and scope

The plant is \(\dot x=-\Lambda x+B w\), the integral objective is \(\int_0^\infty(\|x\|_2^2+\|w\|_2^2)\,d\tau\), and the two independent actuator columns of \(B\) are \(\sqrt t\,u\) and \(\sqrt s\,v\). The initial-state covariance used to average the optimal value is \(I\), so the mean optimal cost is \(\operatorname{tr}P(t,s)\). All \(n\ge1\), all real nonzero or zero channel vectors, and all strictly positive rates are admitted. No controllability assumption is required: the uncontrolled generator is strictly stable. A positive independent installation cost proportional to the number of channels cancels in the interaction \(\Delta\).

## Proof

At zero actuator strength the unique stabilizing solution is \(P_0=\operatorname{diag}(p_i)\) with \(p_i=(2\lambda_i)^{-1}\). The differential with respect to \(P\) of the Riccati equation there is the invertible Sylvester map \(X\mapsto-\Lambda X-X\Lambda\). Thus the implicit function theorem gives a real-analytic symmetric solution \(P(t,s)\) near \((0,0)\). Since the unperturbed closed loop is strictly Hurwitz, its continuation is the stabilizing solution. Positivity of \(P\) also persists locally. Standard continuous-time LQR existence extends this solution to all \(t,s\ge0\), because the strictly stable plant is stabilizable and \(Q=I\) is detectable.

Differentiate the Riccati identity with respect to \(t\) and \(s\), writing \(P_t\), \(P_s\), and \(P_{ts}\) for derivatives at zero. The first derivatives obey
\[
(P_t)_{ij}=-\frac{p_ip_ju_iu_j}{\lambda_i+\lambda_j},\qquad
(P_s)_{ij}=-\frac{p_ip_jv_iv_j}{\lambda_i+\lambda_j}.
\]
For \(U=uu^{\mathsf T}\) and \(V=vv^{\mathsf T}\), the mixed derivative satisfies
\[
-\Lambda P_{ts}-P_{ts}\Lambda
=P_tVP_0+P_0VP_t+P_sUP_0+P_0UP_s.
\]
The diagonal entries therefore give, with \(w_i=u_iv_i\),
\[
\operatorname{tr}P_{ts}=
\sum_{i,j}\frac{w_iw_j}{4\lambda_i^3\lambda_j(\lambda_i+\lambda_j)}
=\sum_{i,j}K_{ij}w_iw_j,
\]
where the second equality symmetrizes the coefficient in \(i,j\). Since \(\Delta\) vanishes identically on each coordinate axis and \(\partial_t\partial_s\Delta(0,0)=\operatorname{tr}P_{ts}\), analyticity gives the stated remainder \(O(ts(t+s))\) for fixed \(\Lambda,u,v\).

If every rate equals \(\lambda\), then every \(K_{ij}=1/(8\lambda^5)\), so \(w^{\mathsf T}Kw=(\sum_iw_i)^2/(8\lambda^5)\ge0\). Conversely, choose two unequal rates \(a,b\). Their principal two-by-two kernel has
\[
K_{aa}=\frac1{8a^5},\quad K_{bb}=\frac1{8b^5},\quad K_{ab}=\frac{a^2+b^2}{8a^3b^3(a+b)},
\]
\[
K_{aa}K_{bb}-K_{ab}^2
=-\frac{(a-b)^2(a^2+ab+b^2)}{64a^6b^6(a+b)^2}<0.
\]
Hence \(K\) is not positive semidefinite. To realize a negative quadratic direction as products of actual input coordinates, set \(u_i=u_j=1\), \(v_i=1\), \(v_j=-K_{ab}/K_{bb}\), and all other coordinates to zero. Then \(w^{\mathsf T}Kw=K_{aa}-K_{ab}^2/K_{bb}<0\). The remainder gives \(\Delta(t,t)<0\) for every sufficiently small positive \(t\). In the explicit \(a=1,b=2\) witness with \(v=(1,-4)\), substitution yields \(w^{\mathsf T}Kw=-1/48\). This proves all assertions, including the sharp all-direction equivalence.

## Verification

A standalone Python 3 standard-library checker, `checker.py`, uses exact rational arithmetic to compute the mixed Riccati derivative independently by the Sylvester equations and compare it with the closed-form kernel for randomly sampled rational data in dimensions one through six. It also checks the equal-rate formula, the rational two-mode witness, and the two-rate determinant identity. The included deterministic invocation `python3 checker.py` produced `PASS: 2043 exact rational assertions`. These finite tests detect implementation/algebraic mistakes but do not prove the all-parameter classification; that proof is the calculation above.

## Relationship to prior work

Azmi and Wachsmuth, *Optimal Actuator Support Design for Infinite-Horizon Linear-Quadratic Parabolic Control Problems* (arXiv:2611.12553, version 1, November 9, 2026) motivate sensitivity of infinite-horizon LQ cost to changes of actuator support using Riccati and Lyapunov identities. Their support calculus is a related, more general first-order framework. Inspection of the complete accessible manuscript, particularly Sections 3.3--3.4 on the exact comparison and first-order support expansion and Section 4 on the topological derivative, did not identify the exact two-channel mixed kernel or the all-direction modal-isotropy criterion here. A general comparison formula could nonetheless imply intermediate variation identities after additional specialization.

Watanabe, Hirayama, Sasaki, Nagata and Nonomura, *Actuator Selection Based on a Reduced-Order Model Using Balanced Proper Orthogonal Decomposition with Input-Output Projection*, Actuators 15 (2026), 234, use Riccati-based actuator selection and discuss greedy/submodularity motivation. Their accessible full article and actuator-selection section concern algorithms and numerical performance, rather than the exact infinitesimal sign classification. Classical Gramian submodularity statements concern a linear Gramian set function, not the nonlinear stabilizing algebraic Riccati solution. Independently published equivalences or broader results may exist; absence from targeted searches is not a priority certificate.

## Limitations

The sign classification concerns the leading mixed response at **zero actuator strength** for a stable, real diagonal plant with identity state and input penalties and identity initial-state covariance. No claim is made that the equal-rate model has global diminishing returns at finite strength, nor that the two-mode negative defect persists outside a sufficiently small neighborhood. The explicit comparison does not directly quantify the performance of any greedy actuator selection algorithm. For arbitrary non-diagonal generators or anisotropic penalties, the kernel changes. This is an analytical result with finite reproducibility checks, not independently validated mathematical certification.

## References

- B. Azmi and D. Wachsmuth, *Optimal Actuator Support Design for Infinite-Horizon Linear-Quadratic Parabolic Control Problems*, arXiv:2611.12553v1 (2026-11-09), https://arxiv.org/abs/2611.12553.
- M. Watanabe, K. Hirayama, Y. Sasaki, T. Nagata, and T. Nonomura, *Actuator Selection Based on a Reduced-Order Model Using Balanced Proper Orthogonal Decomposition with Input-Output Projection*, Actuators 15(5), 234 (2026), https://doi.org/10.3390/act15050234.
- F. Cortesi, T. H. Summers, and J. Lygeros, *Submodularity of Energy Related Controllability Metrics* (2014), https://personal.utdallas.edu/~ths150130/papers/CortesiSummersLygeros2014.pdf (controllability-Gramian context; not a source of the claimed Riccati interaction formula).
