# A positive-trace obstruction to Jacobi stability in planar point-mass fields

## Finding
For every finite nonempty collection of positive point masses in the normalized planar rotating potential \(U(z)=\tfrac12\|z\|^2+\sum_{j=1}^{k}m_j/\|z-a_j\|\), the KCC deviation tensor \(P=\nabla^2U-I_2\) has \(\operatorname{tr}P=\sum_{j=1}^{k}m_j/\|z-a_j\|^3>0\) at every nonsingular configuration. Consequently, no regular trajectory is Jacobi-stable under the strict criterion that every eigenvalue of \(P\) has negative real part. This is a statement about that criterion, not a claim of ordinary linear or orbital instability.

## Assumptions and scope
Let \(k\geq1\), let \(m_j>0\), and let the fixed centers \(a_j\in\mathbb R^2\) be distinct. Set \(r_j=\|z-a_j\|\), \(u_j=(z-a_j)/r_j\), and \(\Omega=\mathbb R^2\setminus\{a_1,\ldots,a_k\}\). Consider the normalized planar rotating second-order system
\[
\ddot z+2J\dot z=\nabla U(z),\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad J^2=-I_2,
\]
with \(U(z)=\tfrac12\|z\|^2+\sum_{j=1}^{k}m_j/r_j\). The centers need not be assumed to form a physically self-consistent relative equilibrium; the theorem is a property of this explicitly stated differential system. Singular configurations are excluded.

## Proof
In the KCC convention used for the classical restricted three-body problem, the deviation curvature tensor is \(P=\nabla^2U-I_2\). The identity follows from the constant Coriolis matrix, whose square is \(-I_2\). Since the Hessian of \(\tfrac12\|z\|^2\) is \(I_2\),
\[
P=\sum_{j=1}^{k}\nabla^2\!\left(\frac{m_j}{r_j}\right).
\]
Direct differentiation, valid for \(r_j>0\), gives
\[
\nabla^2\!\left(\frac{m_j}{r_j}\right)=\frac{m_j}{r_j^3}\left(3u_ju_j^{\mathsf T}-I_2\right).
\]
Because \(\operatorname{tr}(u_ju_j^{\mathsf T})=1\) and \(\operatorname{tr}(I_2)=2\), each summand has trace \(m_j/r_j^3\). Hence
\[
\operatorname{tr}P=\sum_{j=1}^{k}\frac{m_j}{r_j^3}>0\qquad(z\in\Omega).
\]
The matrix \(P\) is real symmetric, so its eigenvalues are real and sum to a strictly positive number. At least one eigenvalue is therefore positive at every \(z\in\Omega\). The strict Jacobi-stability condition, which requires all eigenvalues to have negative real parts along a trajectory, fails at every time on every trajectory that remains in \(\Omega\). This proves the claim.

## Verification
The Hessian identity is obtained by differentiating \(r^{-1}\) in two dimensions; its trace is \(r^{-3}\), not zero. The quadratic centrifugal term cancels the \(-I_2\) contribution in the KCC tensor, leaving the sum of point-mass Hessians. No numerical experiment is needed. The conclusion is limited to the stated KCC criterion and does not establish physical instability.

## Relationship to prior work
The primary source on Jacobi stability for the classical restricted three-body problem defines the same deviation tensor and gives the two-center trace identity. That identity already implies the global two-center special case; the present claim does not present that special case alone as new. The extension here is the explicit theorem for an arbitrary finite number of positive centers and the resulting global criterion failure. Searches for equivalent KCC/point-mass statements did not return a direct arbitrary-center match. General KCC references cited by the primary source were not individually inspected, so a broader prior formulation remains a residual risk.

## Limitations
The theorem assumes a planar system with unit rotating-frame normalization and potential \(\tfrac12\|z\|^2+\sum_j m_j/r_j\), with positive masses and singular centers removed. It concerns the strict KCC Jacobi-stability test only; it does not imply Lyapunov instability, orbital instability, or any statement about trajectories that collide with a center. The arbitrary-center extension is elementary, and uninspected general KCC literature could contain a related statement.

## References
1. *Jacobi stability analysis of the classical restricted three-body problem*, arXiv:2104.02432v1, first posted 2021-04-06. The definitions of the KCC deviation tensor and the two-center trace identity are the relevant source results.
