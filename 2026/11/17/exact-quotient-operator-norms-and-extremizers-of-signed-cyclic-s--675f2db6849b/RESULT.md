# Exact quotient operator norms and extremizers of signed cyclic shifts

## Finding
For every signed cyclic unitary shift on \(\mathbb C^n\), \(n\ge3\), the operator-norm distance of its Hermitian part to the subspace of self-adjoint operators with zero prescribed cyclic edge entries has an exact three-branch formula. In the invertible cases its best approximation is unique. At the singular even-cycle parity the complete set of best approximants is an explicit two-dimensional rectangle. This is a classification of **complex Hermitian** operator-norm minimizers, not just a construction of one real symmetric minimizer.

Specifically, let \(\varepsilon_j\in\{+1,-1\}\) for \(0\le j<n\), with indices taken modulo \(n\), and put \(\mu=\prod_j\varepsilon_j\). Let \(Ue_j=\varepsilon_je_{j+1}\) be the unitary signed cyclic shift and \(A=U+U^*\). Let \(\mathcal W\) be the real vector space of Hermitian matrices \(W\) such that \(W_{j,j+1}=0\) for all \(j\). Thus \(A+\mathcal W\) is the affine class of matrices whose cyclic nearest-neighbor entries equal the prescribed signs; diagonal and nonedge entries are unrestricted.

The exact operator-norm quotient is
\[
\tau_{n,\mu}:=\inf_{W\in\mathcal W}\|A+W\|_{\mathrm{op}}=\frac{2n}{\|A\|_{\mathcal S_1}}
=\begin{cases}
n\sin\!\left(\frac{\pi}{2n}\right),& n\text{ odd},\\[2mm]
\frac n2\tan\!\left(\frac\pi n\right),& n\text{ even and }\mu=(-1)^{n/2},\\[2mm]
\frac n2\sin\!\left(\frac\pi n\right),& n\text{ even and }\mu\ne(-1)^{n/2}.
\end{cases}
\]
Write \(S=\operatorname{sgn}(A)\), assigning zero to zero eigenvalues. The canonical optimal completion is \(B_0=\tau_{n,\mu} S\). If \(A\) is nonsingular (all odd cases and the even sine branch), **this is the unique Hermitian minimizer**. If \(A\) is singular (exactly the even tangent branch), its kernel is two-dimensional, spanned by orthonormal vectors \(u,v\) supported respectively on the even and odd vertices, with all entries on their own parity nonzero. **Every** Hermitian minimizer, and no others, has the form
\[
B_0+a\,uu^*+b\,vv^*,\qquad a,b\in[-\tau_{n,\mu},\tau_{n,\mu}].
\]
In particular the original signed adjacency operator \(A\) is already optimal precisely when \((n,\mu)=(4,+1),(4,-1),(6,-1)\). In all other cases the sign-functional construction strictly improves its norm.

## Assumptions and scope
The Hilbert space is finite-dimensional and complex, \(n\ge3\), with real signs on successive edges. The operator norm is the largest singular value; \(\|\cdot\|_{\mathcal S_1}\) is the sum of singular values. The completion class is **Hermitian** with exactly the cyclic nearest-neighbor positions prescribed and no restrictions on the remaining positions. For \(n=3\) all off-diagonal entries are prescribed; for \(n=4\) both opposite-vertex entries are free. No assumption of positivity or zero diagonals is imposed. Two sign patterns with the same \(\mu\) are unitarily switching-equivalent.

The classification belongs to the operator-norm best-approximation problem for finite Hilbert-space operators (primary MSC2020 47A30). The motivating source discusses a more general Hermitian matrix-completion problem and uses a linear-algebra primary classification; its results and this operator-quotient classification are distinguished below.

## Proof
**1. Spectral decomposition.** The signed shift is unitary and satisfies \(U^n=\mu I\). Consequently its eigenvalues are the \(n\)-th roots of \(\mu\); hence the eigenvalues of \(A=U+U^*\) are
\[
\lambda_k=2\cos\left(\frac{2\pi k+\delta}{n}\right),\quad 0\le k<n,\qquad \delta=\begin{cases}0,&\mu=1,\\\pi,&\mu=-1.\end{cases}
\]
The only case with zero eigenvalues is \(n\) even and \(\mu=(-1)^{n/2}\). There the two zero eigenvalues are simple as roots of \(U\), so \(\dim\ker A=2\). The two kernel eigenvectors may be recombined into one vector on each parity class: the recurrence \(\varepsilon_{j-1}x_{j-1}+\varepsilon_j x_{j+1}=0\) preserves parity and propagates every nonzero starting entry without zeros. Since all signs have modulus one, each parity-supported normalized kernel vector has component magnitude \(\sqrt{2/n}\) on its supporting parity.

**2. Exact dual lower bound.** For each Hermitian completion \(B=A+W\), the diagonal and off-edge entries of \(W\) have zero overlap with \(A\), giving
\[
\operatorname{Tr}(AB)=\operatorname{Tr}(A^2)=2n.
\]
Trace Hölder duality therefore yields \(2n\le\|A\|_{\mathcal S_1}\,\|B\|_{\mathrm{op}}\), or \(\|B\|_{\mathrm{op}}\ge\tau:=2n/\|A\|_{\mathcal S_1}\).

**3. Construct an optimal completion.** Define \(S=\operatorname{sgn}(A)\) by spectral calculus. Since \(U\) commutes with \(A\), it commutes with \(S\). Conjugation by the signed shift cycles the edges, showing that \(S_{j,j+1}=c\varepsilon_j\) for one real constant \(c\). Thus
\[
\|A\|_{\mathcal S_1}=\operatorname{Tr}(AS)=2nc,
\]
so \(c=\|A\|_{\mathcal S_1}/(2n)>0\). It follows that \(B_0:=S/c=\tau S\) has exactly the prescribed edge entries. Since \(S\) has eigenvalue \(\pm1\) on the nonzero spectral subspace of \(A\), \(\|B_0\|_{\mathrm{op}}=\tau\); the lower bound is attained.

**4. Classify every optimizer.** Fix a Hermitian feasible \(B\) with \(\|B\|_{\mathrm{op}}=\tau\). In an orthonormal eigenbasis \(e_k\) of \(A\), equality in the trace Hölder bound means
\[
\langle Be_k,e_k\rangle=\tau\,\operatorname{sgn}(\lambda_k)\qquad\text{whenever }\lambda_k\ne0.
\]
Since \(\tau I\pm B\) are positive semidefinite, equality in the extreme Rayleigh quotient forces \(Be_k=\tau\operatorname{sgn}(\lambda_k)e_k\) for every nonzero \(\lambda_k\). Thus \(B=\tau S+Z\), where \(Z\) is Hermitian, supported on \(\ker A\), and \(\|Z\|_{\mathrm{op}}\le\tau\). If \(A\) is invertible, \(Z=0\), proving uniqueness.

In the nullity-two case choose the parity-supported orthonormal kernel vectors \(u,v\). The general Hermitian \(Z\) is \(a uu^*+b vv^*+\gamma uv^*+\bar\gamma vu^*\). For any adjacent even–odd vertices \(i,j\), its edge entry is \(\gamma u_i\bar v_j\) or \(\bar\gamma v_i\bar u_j\). Since the corresponding components are nonzero and the prescribed edge of \(B_0\) cannot change, \(\gamma=0\). Therefore \(Z=a uu^*+b vv^*\), and \(\|Z\|_{\mathrm{op}}\le\tau\) is exactly \(|a|,|b|\le\tau\). Conversely, each such \(Z\) is supported on nonedges and has norm at most \(\tau\), proving the full rectangle classification.

**5. Evaluate the trace norm.** The eigenvalue formula yields
\[
\|A\|_{\mathcal S_1}=2\sum_{k=0}^{n-1}\left|\cos\left(\frac{2\pi k+\delta}{n}\right)\right|.
\]
Separating positive and negative cosines and using the elementary progression identity \[\sum_{k=r}^{s}\cos(\alpha+kh)=\frac{\sin((s-r+1)h/2)}{\sin(h/2)}\cos(\alpha+(r+s)h/2)\] on each contiguous positive or negative arc gives
\[
\sum_{k=0}^{n-1}\left|\cos\left(\frac{2\pi k+\delta}{n}\right)\right|=
\begin{cases}
\csc(\pi/(2n)),&n\text{ odd},\\
2\cot(\pi/n),&n\text{ even and }\mu=(-1)^{n/2},\\
2\csc(\pi/n),&n\text{ even and }\mu\ne(-1)^{n/2}.
\end{cases}
\]
Substitution into \(2n/\|A\|_{\mathcal S_1}\) gives the stated three branches. Finally, \(A\) itself attains the trace bound exactly when its nonzero eigenvalues all have the same modulus; for \(n\ge7\) the first two angles in the positive arc already have distinct positive cosines (for \(\mu=+1\), angles \(0,2\pi/n\); for \(\mu=-1\), angles \(\pi/n,3\pi/n\)). The cases \(n=3,4,5,6\) are checked directly from the same eigenvalue formula and yield precisely the three displayed signed cycles. This establishes the theorem.

## Verification
For independent numerical diagnostics, execute `python checks/signed_cycle_check.py` using Python 3 with NumPy. It diagonalizes both signed holonomy classes for \(3\le n\le64\), verifies the trace and closed-form constants, edge preservation by \(B_0\), its optimal norm, and the stated nullity parity. It also checks samples throughout the predicted optimizer rectangle and verifies that the off-parity coupling changes a constrained edge. These are finite floating-point diagnostics only; the proof above establishes all integer dimensions and all complex Hermitian completions.

## Relationship to prior work
Bottazzi and Varela (2026, Sections 2 and 6.1) set up Hermitian spectral-norm completion, establish a dual lower bound, and characterize when an **unweighted unsigned adjacency matrix itself** is optimal. Their results do not state the exact signed-cycle quotient values or the complete optimizer geometry; the lower-bound mechanism in Step 2 is deliberately credited to their general framework. Cohen and Pereira (2021) study symmetric completions of cycles through rank and inertia rather than prescribing the minimum operator norm. The latter comparison is based on accessible substantial article sections on rank and inertia, not verified entire formatted full text; it remains a priority risk. Basic cosine eigenvalues of signed cycles and trace Hölder duality are classical. A specialized earlier norm-completion formula expressed through equivalent dual variables may exist and should be checked before claiming publication priority.

## Limitations
Only equal-magnitude real signed cycle edges are classified. Different positive edge magnitudes, arbitrary unit-complex phase holonomy, non-Hermitian minimizers, and general graph patterns are not covered by the extremizer classification. The norm-optimality statement is finite-dimensional and does not imply an infinite graph operator theorem. The source literature and matching published records examined do not establish exhaustive novelty; independent mathematical and literature review remains outstanding.

## References
1. T. Bottazzi and A. Varela, *Characterizations of minimal Hermitian completions via moments and subdifferentials*, arXiv:2611.10323v1 (first public 2026-11-06), Sections 2, 5, and 6.1, https://arxiv.org/html/2611.10323v1.
2. N. Cohen and E. Pereira, *Symmetric completions of cycles and bipartite graphs*, Linear Algebra and its Applications 614 (2021), 164–175, https://doi.org/10.1016/j.laa.2020.03.029. Substantial publisher-indexed text examined; complete formatted full text not verified.
3. R. Bhatia, *Matrix Analysis*, Springer, 1997, for finite-dimensional matrix spectral calculus and trace norm duality.
