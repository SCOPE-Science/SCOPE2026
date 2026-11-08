# Rank-one positivity and rank-two sign loss in implicit BUG diffusion

## Finding

Consider the unaugmented, fixed-rank implicit basis-update-and-Galerkin (BUG) method for the matrix diffusion equation
\[
\dot W=L_xW+WL_y+\alpha W.
\]
For every pair of finite, symmetric, irreducible graph-diffusion generators \(L_x,L_y\) (nonnegative off-diagonals, zero row sums), every \(\alpha\le0\), and every step \(h>0\), a nonzero, entrywise nonnegative rank-one input produces an **entrywise strictly positive rank-one output**. Consequently every subsequent fixed-rank-one BUG iterate remains strictly positive.

The universal guarantee stops at rank one. There are connected three-node diffusion paths \(L_x,L_y\), a nonnegative rank-two \(3\times3\) input \(W\), and a positive step \(h\), all with integer/rational data, for which the **exact**, untruncated rank-two BUG step produces a negative entry. The ordinary full-rank backward-Euler step for the same input and diffusion operators is strictly positive. Thus discrete energy stability and the use of implicit solves do not alone imply positivity for the rank-two BUG update, even without a singular-value truncation.

## Assumptions and scope

Take \(d_x,d_y\ge2\). Each real symmetric matrix \(L_j\) is a connected weighted-graph generator: off-diagonal entries are nonnegative, row sums are zero, and its positive-weight undirected graph is connected. The scalar reaction coefficient is \(\alpha\le0\). All steps and factorizations are exact; \(h>0\) is arbitrary.

For \(W=USV^{\mathsf T}\), where \(U,V\) have orthonormal columns, one unaugmented rank-\(r\) implicit BUG step computes the two independent subspace updates
\[
\begin{split}
(1-h\alpha)K-hL_xK-hK(V^{\mathsf T}L_yV)&=US,\\
(1-h\alpha)J-hL_yJ-hJ(U^{\mathsf T}L_xU)&=VS^{\mathsf T}.
\end{split}
\]
Let \(U_+,V_+\) be orthonormal bases of their column spaces. Form \(S_*=U_+^{\mathsf T}WV_+\) and solve
\[
(1-h\alpha)S_+-h(U_+^{\mathsf T}L_xU_+)S_+-hS_+(V_+^{\mathsf T}L_yV_+)=S_*.
\]
The output is \(W_+=U_+S_+V_+^{\mathsf T}\). These are the algebraic unweighted specialization of the source's implicit BUG \(K,L,S\) steps. The proof concerns graph-diffusion spatial matrices with identity mass matrices; it does not assert that every higher-order finite-element stiffness matrix has the required sign structure.

## Proof

**Part I: rank-one preservation.** Write \(W=suv^{\mathsf T}\) with \(s>0\), \(u,v\ge0\) Euclidean unit vectors (possible for any nonzero nonnegative rank-one matrix). Define the nonnegative graph Dirichlet energies
\[
\delta_x=-u^{\mathsf T}L_xu,\qquad \delta_y=-v^{\mathsf T}L_yv.
\]
The first two BUG solves reduce to
\[
K=s\bigl[(1+h(\delta_y-\alpha))I-hL_x\bigr]^{-1}u,
\qquad
J=s\bigl[(1+h(\delta_x-\alpha))I-hL_y\bigr]^{-1}v.
\]
Each bracket is a nonsingular irreducible \(M\)-matrix. Indeed its inverse is the integral of a strictly positive (for positive time) graph-diffusion semigroup with a positive exponential weight; hence its inverse is entrywise strictly positive. Thus every entry of \(K,J\) is strictly positive. Choose \(u_+=K/\|K\|_2\) and \(v_+=J/\|J\|_2\). The scalar projected datum \(s_*=s(u_+^{\mathsf T}u)(v_+^{\mathsf T}v)\) is strictly positive. Finally,
\[
s_+=\frac{s_*}{1+h(\delta_{x,+}+\delta_{y,+}-\alpha)}>0,
\quad
\delta_{x,+}=-u_+^{\mathsf T}L_xu_+,\quad
\delta_{y,+}=-v_+^{\mathsf T}L_yv_+.
\]
Therefore \(W_+=s_+u_+v_+^{\mathsf T}\) is strictly positive, and the argument repeats at every step.

**Part II: exact rank-two obstruction.** Set \(\alpha=0\), \(h=20\), and take
\[
L_x=\begin{pmatrix}-3&3&0\\3&-4&1\\0&1&-1\end{pmatrix},\qquad
L_y=\begin{pmatrix}-12&12&0\\12&-32&20\\0&20&-20\end{pmatrix},
\]
\[
F=\begin{pmatrix}3&0\\14&3\\0&7\end{pmatrix},\qquad
G=\begin{pmatrix}13&3\\1&0\\5&3\end{pmatrix},\qquad
W=FG^{\mathsf T}=\begin{pmatrix}39&3&15\\191&14&79\\21&0&21\end{pmatrix}.
\]
Both \(F,G\) have column rank two and \(W\ge0\). All graph edges are positive and all row sums of \(L_x,L_y\) vanish.

The exact rank-two update can be evaluated without normalization or square roots, by using any bases for the updated column spaces. Put \(M_G=G^{\mathsf T}G\), \(N_G=G^{\mathsf T}L_yG\), \(M_F=F^{\mathsf T}F\), \(N_F=F^{\mathsf T}L_xF\). Solve the six-by-six linear systems specified by
\[
(I-hL_x)KM_G-hKN_G=WG,\qquad
(I-hL_y)JM_F-hJN_F=W^{\mathsf T}F.
\]
Write \(P=K^{\mathsf T}K\), \(Q=J^{\mathsf T}J\), \(H=K^{\mathsf T}L_xK\), \(T=J^{\mathsf T}L_yJ\). The exact projected coefficient solves the four-by-four linear system
\[
PCQ-hHCQ-hPCT=K^{\mathsf T}WJ.
\]
The BUG output is \(W_+=KCJ^{\mathsf T}\). These equations are exactly the three Galerkin subproblems in the bases \(G,F,K,J\), and hence are invariant under any invertible change of basis, including the source's QR orthonormalization.

Performing these *rational* solves gives the strictly verified sign interval
\[
-\frac9{100}<(W_+)_{33}<-\frac8{100}.
\]
The attached standard-library verifier constructs all three systems from the displayed matrices, solves them using exact fractions, verifies each equation, and checks these strict bounds. Thus this is an exact counterexample, not a rounding error or an SVD-truncation artifact. On the other hand, the full backward-Euler operator \(I-h(L_x\otimes I+I\otimes L_y)\) is an irreducible nonsingular \(M\)-matrix, so its inverse sends \(W\ge0\), \(W\ne0\) to an entrywise strictly positive matrix.

## Verification

Run `python3 verify.py` from the directory containing this result. The verifier uses only the Python standard library and checks the displayed rational rank-two instance, the original subspace Galerkin equations, the strict negativity interval, strict positivity of full-rank backward Euler, and 24 supplementary rank-one examples. Its finite examples support but do not replace the rank-one \(M\)-matrix proof. The exact fraction computation, not a floating-point approximation, certifies the rank-two negative entry.

## Relationship to prior work

Saha, Yang and Yin, *Low-cost non-iterative Sylvester solvers for dynamical low-rank approximation of reaction-diffusion equations*, arXiv:2610.18419 (first public October 13, 2026), supply the implicit BUG substeps, weighted variational interpretation, unique solvability, and \(L^2\)-stability. Their results do not assert componentwise positivity. The present claim is restricted to the matrix-diffusion/graph-Laplacian specialization and distinguishes rank-one positivity from rank-two sign loss for those exact untruncated steps.

The older basis-update/Galerkin integrators of Ceruti and Lubich, arXiv:2010.02022, motivate forward-time low-rank substeps but do not supply the method-specific positivity dichotomy above. Work on nonnegative corrections for low-rank Vlasov approximations, including Kormann–Nazarov–Wen, arXiv:2606.31662, and Wu–Becker–Qiu–Zhang, arXiv:2607.26272, establishes that positivity is an important constraint; those corrections apply to different schemes and do not imply a guarantee for rank-one implicit graph diffusion or the untruncated BUG rank-two counterexample.

## Limitations

The universal guarantee is for nonnegative rank-one data and symmetric connected graph generators, with \(\alpha\le0\) and exact arithmetic. The failure example is a particular rank-two \(3\times3\) graph-diffusion instance; it does not say every rank-two input fails, give a sharp timestep threshold, or establish behavior for arbitrary higher-order mass-lumped finite-element discretizations. No SVD rank truncation is performed in the example. Positivity is a componentwise statement, distinct from the \(L^2\) energy stability proved in the motivating article. No independent validation has been performed.

## References

1. J. Saha, J. Yang, P. Yin, *Low-cost non-iterative Sylvester solvers for dynamical low-rank approximation of reaction-diffusion equations*, arXiv:2610.18419, https://arxiv.org/abs/2610.18419 (2026).
2. G. Ceruti, C. Lubich, *An unconventional robust integrator for dynamical low-rank approximation*, arXiv:2010.02022, https://arxiv.org/abs/2010.02022 (2020).
3. K. Kormann, M. Nazarov, J. Wen, *Positivity-preserving dynamical low-rank methods for the Vlasov equation*, arXiv:2606.31662, https://arxiv.org/abs/2606.31662 (2026).
4. Y. Wu, S. Becker, J. Qiu, X. Zhang, *Nonnegative Low-Rank Matrix Correction under an Orthogonality Constraint in Conservative Vlasov Simulations*, arXiv:2607.26272, https://arxiv.org/abs/2607.26272 (2026).
