# Full-rank fixed-coupling chaos–extinction dichotomy for the matrix logistic map

## Finding
For the matrix logistic transformation
\[
\Phi_B(H)=BH(I-H)B^*,\qquad 0\preceq H\preceq I,
\]
there is a continuous, one-parameter family of **positive-definite** coupling matrices \(A\) with two invertible factorizations \(A=BB^*\) supporting opposite global dynamics. For each real \(0<t<1/2\), set
\[
A_t=\begin{pmatrix}4&0\\0&t^2\end{pmatrix},\qquad
B_{\mathrm{diag},t}=\begin{pmatrix}2&0\\0&t\end{pmatrix},\qquad
B_{\mathrm{swap},t}=\begin{pmatrix}0&2\\t&0\end{pmatrix}.
\]
Both factors are invertible and satisfy exactly
\[
B_{\mathrm{diag},t}B_{\mathrm{diag},t}^*=B_{\mathrm{swap},t}B_{\mathrm{swap},t}^*=A_t\succ0.
\]
Nonetheless the first factor has the invariant segment \(\{\operatorname{diag}(x,0):0\le x\le1\}\), on which it acts as the full logistic map \(x\mapsto4x(1-x)\). In particular its topological entropy on the compact Hermitian state space is at least \(\log2\), and it supports a nonatomic invariant probability with the classical arcsine density in that segment.

The second factor globally extinguishes every initial state in the *entire* compact Hermitian order interval. Specifically, with \(q_t=4t^2<1\), for all integers \(n\ge0\) and all \(0\preceq H_0\preceq I\),
\[
0\preceq\Phi_{B_{\mathrm{swap},t}}^{2n}(H_0)\preceq q_t^nH_0,
\qquad
\|\Phi_{B_{\mathrm{swap},t}}^{2n+1}(H_0)\|_{\rm op}\le4q_t^n.
\]
Thus its iterates converge to zero uniformly, its only invariant Borel probability is \(\delta_0\), and its topological entropy is zero. The same strictly positive-definite \(A_t\), with exactly the same singular values of \(B\), therefore supports both full logistic chaos and uniform global extinction.

## Assumptions and scope
All matrices are complex Hermitian \(2\times2\) states \(H\) in \(\mathcal D=\{H=H^*:0\preceq H\preceq I\}\), with the usual positive-semidefinite order. The scalar parameter \(t\) lies in the open interval \((0,1/2)\). The matrix \(B\) is fixed along each orbit; the two maps are compared at exactly the same \(A_t\), not under a time-dependent factorization. The statement does not assert that all trajectories of the diagonal factor are chaotic, or that the lower entropy bound is an exact entropy formula for the entire matrix map.

## Proof
**1. State-space invariance.** Functional calculus on \(H\in\mathcal D\) gives
\[
0\preceq H(I-H)\preceq H,\qquad 0\preceq H(I-H)\preceq I/4.
\]
For either factor, \(BB^*=A_t\preceq4I\), hence \(0\preceq\Phi_B(H)\preceq A_t/4\preceq I\). Thus the map is continuous and self-maps the compact state space \(\mathcal D\). Direct matrix multiplication proves the two identical, strictly positive-definite products and the invertibility of both factors, whose determinant magnitudes are \(2t\).

**2. An invariant chaotic subsystem.** Let \(H=\operatorname{diag}(x,0)\). Since the first factor is diagonal,
\[
\Phi_{B_{\mathrm{diag},t}}(H)=\operatorname{diag}(4x(1-x),0).
\]
The closed segment is invariant and the restriction is conjugate (via its first diagonal coordinate) to \(x\mapsto4x(1-x)\) on \([0,1]\). The latter is the standard fully chaotic logistic map, of entropy \(\log2\), with invariant probability \(dx/[\pi\sqrt{x(1-x)}]\). The pushforward of this probability to the segment is invariant for the matrix map. Entropy monotonicity under restriction to a closed invariant set gives \(h_{\rm top}(\Phi_{B_{\mathrm{diag},t}})\ge\log2\).

**3. Two-step matrix-order contraction for the swapped factor.** The pointwise inequality \(0\preceq\Phi_B(H)\preceq BHB^*\) yields, for each state \(H\in\mathcal D\),
\[
0\preceq\Phi_B^2(H)\preceq B\Phi_B(H)B^*\preceq B^2H(B^*)^2.
\]
For \(B=B_{\mathrm{swap},t}\), exact multiplication gives \(B^2=2tI\). Therefore
\[
0\preceq\Phi_B^2(H)\preceq4t^2H=q_tH.
\]
Repeating this estimate at the actual states of each trajectory gives \(0\preceq H_{2n}\preceq q_t^nH_0\). For odd iterates,
\[
0\preceq H_{2n+1}\preceq BH_{2n}B^*\preceq q_t^nBH_0B^*\preceq q_t^nBB^*,
\]
so \(\|H_{2n+1}\|_{\rm op}\le4q_t^n\) and \(\|H_{2n}\|_{\rm op}\le q_t^n\). This is uniform in initial state, and proves global exponential convergence to zero.

**4. Invariant laws and topological entropy.** For any \(\Phi_B\)-invariant Borel probability \(\nu\) and any continuous \(f\) on \(\mathcal D\), invariance gives \(\int f\,d\nu=\int f\circ\Phi_B^n\,d\nu\). The proved uniform convergence makes the latter tend to \(f(0)\), proving \(\nu=\delta_0\). Given any separation radius \(\epsilon>0\), choose \(N_\epsilon\) so every state has image within \(\epsilon/3\) of zero after time \(N_\epsilon\). For arbitrarily long orbits, the number of \(\epsilon\)-separated points is then bounded by the finite \(\epsilon\)-spanning number for the first \(N_\epsilon\) iterates on compact \(\mathcal D\), independent of the observation horizon. Hence topological entropy vanishes. The two factors therefore realize the stated contrast at the same positive-definite coupling matrix.

## Verification
The standalone standard-library-only program `checker.py` constructs the two factors with exact rational arithmetic for three rational parameters \(t=1/5,1/4,2/5\). It verifies the identical positive-definite products, the exact identity \(B_{\mathrm{swap},t}^2=2tI\), state invariance, the Loewner upper bound on all even iterates through finite time on 45 exact positive-semidefinite sample initial matrices, and exact reproduction of the logistic scalar orbit on the diagonal segment. It performed 1,779 passed assertions. The conclusions concerning **all** states, time horizons and irrational \(t\) follow from the analytic proof, not from those finite tests.

## Relationship to prior work
Pawela and Życzkowski introduced the Hermitian matrix logistic map with \(A=BB^*\) and gave graph-directed coupling examples and a two-node appendix with diagonal and coupled factors. They do not establish the present fixed-**positive-definite**-\(A\) entropy/extinction dichotomy. Earlier analysis of critical nonnormal Jordan factors gives polynomial extinction rather than this uniform geometric extinction at fixed singular values. An earlier rank-one factorization example exhibits a related contrast for **singular** \(A\); it cannot imply the result for invertible factors and strictly positive-definite \(A_t\). The present proof is an order-theoretic two-step contraction combined with an invariant chaotic segment, not an inference from the eigenvalues of \(A_t\) alone. General stability criteria for linear products are familiar and not claimed new; the assessment concerns their exact dynamical application to the nonlinear matrix logistic transformation at a fixed full-rank coupling matrix.

## Limitations
The result exhibits a positive-width family of counterexamples to sufficiency of positive-definite \(A\), not a classification of every factorization or of arbitrary two-node networks. The chaotic statement is existence of an invariant subsystem and lower entropy bound; its full phase-space physical basin and the exact full-space entropy are not determined. The extinction bound is sufficient and is not asserted sharp at \(t=1/2\). General results or unindexed literature could contain an equivalent invertible-factor comparison. Independent mathematical audit has not been performed.

## References
1. Ł. Pawela and K. Życzkowski, *Matrix logistic map: fractal spectral distributions and transfer of chaos*, arXiv:2303.06176, first posted 2023-03-10, especially Eq. (6), coupled-graph section, and Appendix A. https://arxiv.org/abs/2303.06176.
2. R. L. Devaney, *An Introduction to Chaotic Dynamical Systems*, 2nd ed., Addison-Wesley, 1989 (standard full logistic map and its entropy).
3. *Rank-sensitive critical decay in a two-node nonnormal matrix logistic map* (2026, online research record); a separate neutral Jordan-boundary problem, with polynomial rather than geometric decay.
