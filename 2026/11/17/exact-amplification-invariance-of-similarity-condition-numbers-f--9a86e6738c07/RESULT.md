# Exact amplification invariance of similarity condition numbers for complex two-by-two matrices

## Finding
For matrices \(A,B\in M_2(\mathbb C)\), define the optimal similarity condition number
\[
 s(A,B)=\inf\{\|Y\|\,\|Y^{-1}\|:Y\in GL_2(\mathbb C),\ YA=BY\},
\]
with value \(+\infty\) if no such \(Y\) exists. Operator norms are Euclidean spectral norms. For every nonzero complex Hilbert space \(K\), the corresponding optimal similarity number of the amplified operators on \(\mathbb C^2\otimes K\) is **exactly** \(s(A,B)\), including the infinite case:
\[
 \boxed{\ s(A\otimes I_K,B\otimes I_K)=s(A,B).\ }
\]
In particular, for every integer \(q\ge1\) and \(t\ge1\), the similarity-amplification function of Aouichaoui (2026) satisfies the sharp identity
\[
 \boxed{\ \theta_{2,q}(t)=t.\ }
\]
Here \(\theta_{2,q}(t)\) is the supremum of \(s(A,B)\) over pairs with \(s(A^{(q)},B^{(q)})\le t\), where \(A^{(q)}\) is the orthogonal sum of \(q\) copies of \(A\).

There is also a closed formula for every similar pair. If \(A=B=\lambda I_2\), then \(s(A,B)=1\). If both have the same single eigenvalue \(\lambda\) and nonzero nilpotent parts \(N_A=A-\lambda I_2\), \(N_B=B-\lambda I_2\), then
\[
 \boxed{\ s(A,B)=\max\left\{\frac{\|N_A\|}{\|N_B\|},\frac{\|N_B\|}{\|N_A\|}\right\}.\ }
\]
If both have the same two distinct eigenvalues \(\lambda\ne\mu\), set
\[
 P_A=\frac{A-\mu I_2}{\lambda-\mu},\quad
 P_B=\frac{B-\mu I_2}{\lambda-\mu},\quad
 g(P)=\|2P-I_2\|.
\]
Then
\[
 \boxed{\ s(A,B)=\max\left\{\frac{g(P_A)}{g(P_B)},\frac{g(P_B)}{g(P_A)}\right\}.\ }
\]
All finite minima are attained. If the matrices are not similar, the similarity number is infinite.

## Assumptions and scope
All matrices are complex \(2\)-by-\(2\), all similarities are bounded complex-linear invertible operators, and all norms are induced Hilbert-space operator norms. The Hilbert multiplicity space \(K\) may be finite- or infinite-dimensional, but must be nonzero. The convention for infinite similarity number is explicit. The theorem does not concern unrelated matrix sizes, non-Hilbert norms, or simultaneous intertwining of several operator pairs.

## Proof
**Step 1: similarity types.** Two complex \(2\)-by-\(2\) matrices are similar exactly when their characteristic polynomials and minimal polynomials agree. When \(K\ne\{0\}\), amplification preserves the spectrum and every polynomial identity, in both directions: \(p(A\otimes I_K)=p(A)\otimes I_K\) vanishes exactly when \(p(A)=0\). Hence similarity of the amplified operators forces similarity of the original matrices. If they are not similar, both optimal similarity numbers are infinite. It remains to consider similar pairs.

**Step 2: scalar case.** Similar scalar matrices coincide and the identity intertwiner has condition number one. The same is true after any amplification.

**Step 3: one Jordan block.** For a nonscalar pair with a repeated eigenvalue, \(N_A\) and \(N_B\) are nonzero square-zero rank-one operators. Every invertible intertwiner satisfies \(YN_A=N_BY\), so
\[
 \|N_B\|\le\|Y\|\,\|Y^{-1}\|\,\|N_A\|
\]
and the reversed inequality also holds. These inequalities continue to hold after tensoring with \(I_K\), since \(\|N_A\otimes I_K\|=\|N_A\|\). Conversely, each nonzero rank-one nilpotent on a Hilbert plane has orthonormal coordinates in which it equals \(aE_{12}\), where \(a\) is its norm. Thus suitable unitary conjugations reduce the pair to \(aE_{12}\), \(bE_{12}\). The diagonal matrix \(\operatorname{diag}(b/a,1)\) intertwines them and has condition number \(\max\{a/b,b/a\}\). Tensoring this matrix with \(I_K\) attains the same bound after amplification.

**Step 4: distinct eigenvalues, lower bound.** Each spectral idempotent satisfies \(P_A^2=P_A\), \(P_B^2=P_B\). Any invertible intertwiner of the original pair or their amplifications also intertwines the corresponding spectral idempotents. Therefore it conjugates \((2P_A-I_2)\otimes I_K\) to \((2P_B-I_2)\otimes I_K\). In both directions the elementary similarity norm inequality gives
\[
 \|Y\|\,\|Y^{-1}\|\ \ge\
 \max\left\{\frac{g(P_A)}{g(P_B)},\frac{g(P_B)}{g(P_A)}\right\}.
\]
The tensor norms equal the matrix norms, even for infinite-dimensional \(K\).

**Step 5: distinct eigenvalues, matching intertwiner.** Choose normalized ordered eigenvectors \(u_+,u_-\) for \(A\). Because the eigenvalues are distinct, their absolute inner-product overlap is \(\cos\alpha\) for a unique \(\alpha\in(0,\pi/2]\). After independently rephasing the eigenvectors and conjugating by a unitary, their coordinates are
\[
 u_+=(\cos(\alpha/2),\sin(\alpha/2)),\quad
 u_-=(\cos(\alpha/2),-\sin(\alpha/2)).
\]
Likewise for \(B\), with an angle \(\beta\in(0,\pi/2]\) and eigenvectors \(v_+,v_-\) with the same prescribed eigenvalue labeling. In these coordinates the spectral projection onto the first eigenline along the second satisfies
\[
 2P_A-I_2=\begin{pmatrix}0&\cot(\alpha/2)\\ \tan(\alpha/2)&0\end{pmatrix},
 \qquad g(P_A)=\cot(\alpha/2).
\]
The identical formulas with \(\beta\) hold for \(B\). The positive diagonal matrix
\[
 Y_0=\operatorname{diag}\left(\frac{\cos(\beta/2)}{\cos(\alpha/2)},
 \frac{\sin(\beta/2)}{\sin(\alpha/2)}\right)
\]
sends the first ordered eigenbasis to the second and hence intertwines the two canonical matrices. Its condition number is
\[
 \max\left\{\frac{\tan(\alpha/2)}{\tan(\beta/2)},
 \frac{\tan(\beta/2)}{\tan(\alpha/2)}\right\}
 =\max\left\{\frac{g(P_A)}{g(P_B)},\frac{g(P_B)}{g(P_A)}\right\}.
\]
Undoing the unitary coordinate changes leaves the condition number unchanged. This proves the precise original similarity number, with attainment. Tensoring the optimal intertwiner with \(I_K\) meets the amplified lower bound. Therefore no nonzero Hilbert amplification can improve the optimal condition number.

**Step 6: optimality of the amplification function.** The established equality yields \(\theta_{2,q}(t)\le t\). For the matrices \(A=E_{12}\) and \(B=tE_{12}\) with \(t\ge1\), the Jordan-case formula gives \(s(A,B)=s(A^{(q)},B^{(q)})=t\). Hence \(\theta_{2,q}(t)\ge t\) as well.

## Verification
The proof is exact and uses no computational premise. A separate supplementary checker applies real canonical eigenbasis matrices with a deterministic range of angles and verifies the intertwining identity, spectral-idempotent formula, and optimal condition number. It also checks the Jordan witnesses. The checker is not an exhaustive or infinite-dimensional certification: the general conclusion is obtained from the algebraic proof and operator-norm inequalities above.

An equivalent computable expression for the projection invariant is
\[
 g(P)=\|P\|+\sqrt{\|P\|^2-1},
\]
valid for every rank-one idempotent on a complex Hilbert plane. This follows directly from \(\|P\|=\csc\alpha\) in the canonical coordinates.

## Relationship to prior work
Aouichaoui (2026) proves finite dimension-dependent bounds for similarity cancellation and shows that for sufficiently large matrix sizes direct-sum amplification can **strictly improve** optimal similarity conditioning. The present theorem gives an exact converse boundary in dimension two, including arbitrary Hilbert multiplicity, and determines the full function \(\theta_{2,q}\) rather than merely its finiteness or continuity at one. Jiang, Ma, Shi, and Zhang (2026) prove quantitative general-dimension bounds and discuss the earlier similarity-cancellation problem; their reported bounds and examples do not imply the equality here. Demmel (1983) gives the sharp conditioning of diagonalizing a two-block spectral decomposition; in the Hilbert plane this identifies \(g(P)\) as the optimal conditioning to *orthogonalize one pair* of eigenspaces. The present exact ratio for *two different matrix realizations* and its amplification invariance are not the same one-matrix diagonalization statement.

## Limitations
The result exploits the complete classification of complex Hilbert-plane Jordan structures and fails as a general all-dimension statement in light of known higher-dimensional counterexamples. It does not provide a threshold for the first larger dimension at which strict amplification improvement occurs. The primary literature comparison inspected relevant statements and methods, but an independently conducted priority review is absent; an equivalent older formulation under eigenvector-angle or interpolation terminology remains possible. All mathematical assertions above are proved without treating finite tests as proof.

## References
- M. A. Aouichaoui, *Similarity cancellation and primitive operator roots*, arXiv:2611.01298v1 (first public version 2026-10-31), https://arxiv.org/html/2611.01298v1 .
- C. Jiang, M. Ma, R. Shi, Y. Zhang, *The Ulam–Kaplansky problem in operator algebras*, arXiv:2607.20593v2 (first version 2026-07-22; version inspected 2026-11-05), https://arxiv.org/html/2607.20593v2 .
- J. W. Demmel, *The Condition Number of Similarities that Diagonalize Matrices*, Technical Report UCB/CSD-83-127 (1983), https://www2.eecs.berkeley.edu/Pubs/TechRpts/1983/CSD-83-127.pdf .
