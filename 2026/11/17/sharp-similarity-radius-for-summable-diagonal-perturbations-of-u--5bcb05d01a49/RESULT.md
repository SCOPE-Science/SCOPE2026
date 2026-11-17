# Sharp similarity radius for summable diagonal perturbations of unilateral backward shifts

## Finding

Let \(X=\ell^p(\mathbb N;\mathbb C)\), \(1\le p<\infty\), or \(X=c_0(\mathbb N;\mathbb C)\). Denote by \(B\) the unilateral backward shift, \(Be_1=0\) and \(Be_{j+1}=e_j\). Fix \(\omega\ne0\) and \(d=(d_j)_{j\ge1}\in\ell^1(\mathbb N;\mathbb C)\). Then

\[
T=\omega B+\operatorname{diag}(d_j)
\quad\text{is boundedly similar to}\quad \omega B
\iff \quad |d_j|<|\omega|\quad\text{for every }j\ge1.
\]

In the similar regime, the proof explicitly constructs a boundedly invertible \(S\) satisfying \(TS=S\omega B\) and the quantitative (not asserted optimal) estimate

\[
\|S\|\,\|S^{-1}\|
\le \prod_{j=1}^{\infty}
\frac{1+|d_j|/|\omega|}{1-|d_j|/|\omega|}<\infty.
\]

Consequently, \(\sigma(T)=\{\lambda:|\lambda|\le|\omega|\}\) and \(\sigma_{\mathrm{pt}}(T)=\{\lambda:|\lambda|<|\omega|\}\). The operator is topologically mixing and frequently hypercyclic exactly when \(|\omega|>1\), and is supercyclic for all \(\omega\ne0\). Thus the same exact similarity criterion, rather than a dynamical sufficient condition alone, controls these behaviors.

A weighted version holds: suppose \(B_w e_{k+1}=w_ke_k\), the weights are bounded, and \(m:=\inf_{k\ge1}|w_k|>0\). For \(d\in\ell^1\), the condition \(\sup_{k\ge1}|d_k|<m\) implies \(B_w+\operatorname{diag}(d_k)\) is boundedly similar to \(B_w\). The weight-uniform condition is sufficient, not claimed necessary for arbitrary variable weights.

## Assumptions and scope

All spaces and operators are complex. Similarity means there exists an everywhere-defined boundedly invertible linear operator \(S:X\to X\) with \(TS=S\omega B\) (or \(TS=SB_w\) in the weighted case). The diagonal perturbation is absolutely summable, not merely compact; complex phases are unrestricted. All claims are on infinite-dimensional \(\ell^p\) for finite \(p\), or \(c_0\). The space \(\ell^\infty\) is excluded because the point-spectrum boundary differs.

Let \(P_j=e_j\otimes e_j^*\), the projection onto coordinate \(j\). For a general weighted shift define the tail-forward operator
\[
R_j e_k=\begin{cases}w_k^{-1}e_{k+1},&k\ge j,\\0,&k<j.\end{cases}
\]
For the constant-weight case take \(w_k=\omega\). Let \(D_N=\sum_{j=1}^N d_jP_j\), and \(D_0=0\).

## Proof

**1. Exact tail-shear identity.** For all \(j\ge1\), direct basis calculations establish
\[
B_wR_j-R_jB_w=P_j,\qquad D_jR_j=0,\qquad R_jD_{j-1}=0.
\]
Indeed, \(B_wR_j\) is the coordinate projection onto indices at least \(j\), while \(R_jB_w\) projects onto indices at least \(j+1\). Set \(Q_j=I-d_jR_j\). The three identities imply
\[
(B_w+D_j)Q_j=Q_j(B_w+D_{j-1}).
\]
Inductively, with \(S_N=Q_N\cdots Q_1\),
\[
(B_w+D_N)S_N=S_NB_w\quad\text{for every }N\ge1.
\]
The ordering is essential; no commutativity of the \(Q_j\) is assumed.

**2. Convergence and invertibility.** Assume \(0<m=\inf_{k\ge1}|w_k|\) and \(q:=\sup_j|d_j|/m<1\). Since \(\|R_j\|\le m^{-1}\), put \(c_j:=|d_j|/m\). Then \(\sum_jc_j<\infty\), \(\sup_jc_j<1\), and each \(Q_j\) is invertible by its Neumann series. In particular,
\[
\|Q_j\|\le1+c_j,\quad
\|Q_j^{-1}\|\le(1-c_j)^{-1},\quad
\|Q_j^{-1}-I\|\le\frac{c_j}{1-c_j}.
\]
The two sequences of finite ordered products \((S_N)_N\) and \((S_N^{-1})_N\) are Cauchy in operator norm: for example, for \(M>N\),
\[
\|S_M-S_N\|\le
\Big(\prod_{k\le N}(1+c_k)\Big)
\Big(\prod_{N<k\le M}(1+c_k)-1\Big),
\]
and the inverse products are controlled in the same way by the summable bounds on \(\|Q_j^{-1}-I\|\). Denote the two limits by \(S\) and \(V\). The identities \(S_NS_N^{-1}=S_N^{-1}S_N=I\) pass to the limit, so \(V=S^{-1}\). The norm-product estimate follows. Since \(D_N\to D\) in norm, the exact finite identity passes to \((B_w+D)S=SB_w\).

In the constant-weight case, the hypotheses \(d\in\ell^1\) and \(|d_j|<|\omega|\) for all \(j\) imply \(\sup_j|d_j|<|\omega|\): the terms tend to zero, so a positive supremum is attained within finitely many indices. Thus the construction gives sufficiency and the stated explicit condition bound.

**3. Sharp necessity for scalar weights.** Fix any \(j\). The recurrence
\[
x_1=1,\qquad x_{k+1}=\omega^{-1}(d_j-d_k)x_k
\]
gives a nonzero vector \(x\) with \(x_{j+1}=0\) and every later coordinate zero. Therefore \(Tx=d_jx\): each \(d_j\) is a finite-support eigenvalue. On \(\ell^p\), \(p<\infty\), and \(c_0\), the eigenvalue equation \(\omega Bx=\lambda x\) has the nonzero geometric solutions \(x_k=(\lambda/\omega)^{k-1}x_1\) exactly when \(|\lambda|<|\omega|\). Similarity preserves the point spectrum. Hence if some \(|d_j|\ge|\omega|\), similarity is impossible. This proves the equivalence, including equality at the boundary.

**4. Dynamical consequences.** Similarity preserves full and point spectra, supercyclicity, mixing, and (frequent) hypercyclicity. The scalar backward shift has closed-disk spectrum and open-disk point spectrum on these spaces. If \(|\omega|>1\), choose \(S_0 e_k=\omega^{-1}e_{k+1}\). On finite-support vectors, \((\omega B)^n\) eventually vanishes, while \(\sum_{n\ge0}S_0^ny\) converges absolutely. The standard frequent-hypercyclicity criterion gives frequent hypercyclicity; its usual stronger forward/backward approximation yields mixing. If \(|\omega|\le1\), its powers are bounded, excluding hypercyclicity and mixing. Scalar multiplication of an operator does not affect supercyclicity; the unilateral backward shift is supercyclic. All these statements transfer to \(T\).

## Verification

The included `check_similarity.py` uses exact rational arithmetic (no external packages) to test the ordered product on 147 finite-support vectors for seven variable-weight families, together with ten finite-support eigenvectors at or outside the constant-weight spectral boundary. It reports 157 successful finite cases. The finite tests are not used as a substitute for the operator-norm convergence proof, the infinite-dimensional spectral characterization or the general quantifiers. The independently written algebraic equalities in Proof steps 1–3 establish those conclusions.

## Relationship to prior work

Messaoudi, Tofanin Neto and Tsokanos [1] introduce this exact diagonal-plus-weighted-backward-shift family and prove dynamical sufficient conditions, a conditional Schauder-basis statement, and a criterion for shadowing. Their Theorem 3.1, Corollary 3.5 and proofs in §§4–5 do not assert a boundedly invertible operator conjugating every summably perturbed shift below the sharp constant-weight spectral radius to the unperturbed shift. In particular, a stated Schauder-basis hypothesis is not itself an unconditional basis-equivalence theorem.

Sahari, Taha and Randriamihamison [2] analyze the spectrum of diagonal perturbations of **bilateral** weighted shifts. A spectral description, even where applicable, does not imply bounded similarity. Robert [3] studies similarity of **rank-one** perturbations of the Hardy backward shift using rational-function intertwiners; his Theorem 1.1 does not state a simultaneous similarity theorem for arbitrary summable diagonal perturbations on all finite \(\ell^p\) and \(c_0\). Grivaux, Matheron and Menet [4] study typical dynamical behavior for the broader diagonal-plus-backward-shift class; their Section 4 concerns generic ergodicity and spectral features rather than this exact norm-convergent ordered product.

The tail-shear factorization is elementary once recognized; stronger existing operator-similarity or Schauder-basis theorems might imply part of this result by reduction. The priority claim is therefore qualified rather than asserted absolutely.

## Limitations

The all-weights statement has only a uniform sufficient radius. The constant-weight equivalence is established only for absolutely summable diagonals. We do not claim an optimal numerical condition number, a classification for nonsummable diagonals or the \(\ell^\infty\) case. The polynomial matrix computations cover finitely many rational test cases; no finite computation certifies the infinite proof. Bibliographic completeness beyond the inspected literature cannot be guaranteed. No independent external audit has been performed.

## References

[1] A. Messaoudi, J. L. Tofanin Neto, I. Tsokanos, *Dynamical Properties of Perturbed Weighted Shifts*, arXiv:2610.15023v1, first public 2026-10-10. https://arxiv.org/abs/2610.15023

[2] M. L. Sahari, A. K. Taha, L. Randriamihamison, *The spectrum of diagonal perturbation of weighted shift operator*, arXiv:1609.05203, first public 2016-09-15. https://arxiv.org/abs/1609.05203

[3] L. Robert, *Similarity of perturbations of the shift and a different product of rational functions*, *Operators and Matrices* 8 (2014), 89–98; arXiv:1207.3428. https://files.ele-math.com/articles/oam-08-03.pdf

[4] S. Grivaux, É. Matheron, Q. Menet, *Linear dynamical systems on Hilbert spaces: typical properties and explicit examples*, arXiv:1703.01854. https://arxiv.org/abs/1703.01854
