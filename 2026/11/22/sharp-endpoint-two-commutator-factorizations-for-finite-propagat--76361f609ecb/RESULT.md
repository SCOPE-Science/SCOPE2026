# Sharp endpoint two-commutator factorizations for finite-propagation defect contractions

## Finding
Let \(H=\ell^2(\mathbb N_0)\). For every nonzero bounded \(T\) with \(s=\|T\|\), set \(C=T/s\) and \(D=(I-C^*C)^{1/2}\). Assume a common finite lower propagation radius: for some integer \(r\ge0\) and all \(i,j\ge0\),
\[
 i<j-r\quad\Longrightarrow\quad\langle Ce_j,e_i\rangle=\langle De_j,e_i\rangle=0.
\]
Then there are four bounded idempotents \(P_1,Q_1,P_2,Q_2\) on \(H\) such that
\[
 T=[P_1,Q_1][P_2,Q_2],\qquad
 \|[P_1,Q_1]\|=\|[P_2,Q_2]\|=\sqrt{\|T\|}.
\]
Moreover the factors satisfy \(AA^*=B^*B=sI\), with \(A=[P_1,Q_1]\) and \(B=[P_2,Q_2]\). Hence the lower bound \(\|T\|\le\|X\|\|Y\|\), valid for every factorization, is attained inside the class of products of two idempotent commutators.

## Assumptions and scope
An idempotent means a bounded operator \(P\) satisfying \(P^2=P\), not necessarily an orthogonal projection. A pure isometry \(V\) satisfies \(V^*V=I\) and \(\bigcap_{n\ge0}V^nH=\{0\}\). Its multiplicity is \(\dim\ker V^*\). The finite propagation condition concerns the *normalized operator and its exact defect square root*, not merely the original operator. It includes arbitrary diagonal contractions (radius zero) and arbitrary unilateral contractive weighted shifts (radius one), including norm-one cases whose defect does not have a bounded inverse. The zero operator factors trivially and is omitted only to avoid division by zero.

## Proof
Write \(f(k)=2k+2r+3\) and \(g(k)=2k+2r+4\). Define isometries on the standard basis by \(Ve_k=e_{f(k)}\) and \(Je_k=e_{g(k)}\). Their ranges are orthogonal, so \(V^*J=0\). Define \(W=VC+JD\). The exact identity \(C^*C+D^2=I\) gives
\[
 W^*W=C^*C+D^2=I,\qquad V^*W=C.
\]
For each \(j\ge0\), both \(Ce_j\) and \(De_j\) are supported on coordinates \(k\ge\max(0,j-r)\), so every coordinate of \(We_j\) has index at least \(2\max(0,j-r)+2r+3>j\). Likewise \(Ve_j\) is supported at an index greater than \(j\). Hence for either isometry \(U\in\{V,W\}\), one has \(U^nH\subseteq\overline{\operatorname{span}}\{e_j:j\ge n\}\), proving purity.

Both multiplicities are infinite. For \(V\), infinitely many even coordinates lie in \(\ker V^*\). For \(W\), put \(D_*=(I-CC^*)^{1/2}\). The identity \(DC^*=C^*D_*\), obtained first for polynomials and then by uniform functional calculus, shows that the map \(y\mapsto -VD_*y+JC^*y\) is an isometry with image orthogonal to \(W(H)\): its squared norm is \(\langle(D_*^2+CC^*)y,y\rangle=\|y\|^2\), while its inner product with \(Wx\) vanishes. Therefore \(\dim\ker W^*=\infty\).

We recall and verify the needed algebraic fact. Every pure isometry of infinite multiplicity is unitarily equivalent, by the Wold decomposition, to its direct sum of four copies, and also to its negative (alternate the signs on successive wandering levels). For every bounded \(X\), the operator \(\operatorname{diag}(X,X,-X,-X)\) is a commutator of idempotents: put \(Y=\begin{psmallmatrix}0&I+4X^2\\I&0\end{psmallmatrix}\) (on two copies), so \(Y^2=I+4\operatorname{diag}(X,X)^2\). Let \(Z=\operatorname{diag}(X,X)\), \(P=\begin{psmallmatrix}I&0\\0&0\end{psmallmatrix}\), and
\[
 Q=\begin{pmatrix}(I+Y)/2&Z\\-Z&(I-Y)/2\end{pmatrix}.
\]
Since \(Y\) commutes with \(Z\), direct multiplication gives \(Q^2=Q\) and \([P,Q]=\begin{psmallmatrix}0&Z\\Z&0\end{psmallmatrix}\), unitarily equivalent to \(\operatorname{diag}(Z,-Z)\). Consequently every scalar multiple of any pure infinite-multiplicity isometry, or its adjoint, is an idempotent commutator; this also follows from Aouichaoui's 2026 Lemma 3.2.

Apply the algebraic fact to \(A=\sqrt{s}V^*\) and \(B=\sqrt{s}W\). Then \(AB=sV^*W=sC=T\), \(AA^*=sI=B^*B\), and \(\|A\|\|B\|=s\), as claimed. For a concrete boundary case, \(C=\operatorname{diag}(1,1-1/3,1-1/4,\ldots)\) has norm one but is not unitary, and its defect square root is diagonal with nonclosed range; the theorem still gives exact attainment.

## Verification
The displayed identities prove the infinite-dimensional result. The accompanying `CHECK.py` constructs finite sections of the isometric embedding for diagonal, forward-weighted, backward-weighted, and two-cycle block-monomial contractions; it tests \(W^*W=I\), \(V^*W=C\), \(V^*J=0\), and strict support advance in 80 assertions. The finite checks diagnose formula transcription only; they do not replace the operator proof. The explicit polynomial idempotent identities above provide an independent algebraic check of the commutator reduction.

## Relationship to prior work
Aouichaoui (2026, Theorem 3.3) proves a factorization \(T=AB\) of arbitrary bounded operators by two idempotent commutators with \(AA^*=B^*B=cI\) for each \(c>\|T\|\); its endpoint construction for unitary \(T\) is separate. The present theorem realizes \(c=\|T\|\) for the finite-propagation defect class, including norm-one operators that are neither unitary nor strictly contractive. Marcoux, Radjavi, and Zhang (2023) obtained a universal three-factor theorem and density of two-factor products, but not this endpoint norm-attaining construction. The mechanism is a basis-dependent forward embedding of both the contraction and its defect, not an inference from a strict inequality by taking limits.

## Limitations
No endpoint assertion is made for arbitrary contractions whose defect square root has unbounded lower propagation. The result does not assert uniqueness of factors, nor a sharp bound on the norms of the *underlying idempotents*. General broader norm-attainment statements could subsume this theorem and should be checked in further bibliographic review.

## References
1. M. A. Aouichaoui, *Optimal lengths of commutators of idempotents and similarity of nilpotent operators to their negatives*, arXiv:2611.01316v1 (first posted 31 October 2026), §§2–3, especially Proposition 2.1, Lemma 3.2 and Theorem 3.3. https://arxiv.org/html/2611.01316v1
2. L. W. Marcoux, H. Radjavi, Y. Zhang, *Around the closure of the set of commutators of idempotents in B(H): Biquasitriangularity and factorisation*, J. Funct. Anal. 284 (2023), 109854, especially §7. https://doi.org/10.1016/j.jfa.2023.109854
