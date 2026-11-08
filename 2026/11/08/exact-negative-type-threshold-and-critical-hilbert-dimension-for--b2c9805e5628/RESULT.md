# Exact negative-type threshold and critical Hilbert dimension for ternary symmetric forms

## Finding
Let \(q\ge 3\) be any **odd prime power**. On the additive group \(V=\operatorname{Sym}_3(\mathbb F_q)\), equip distinct matrices with the rank distance \(d(X,Y)=\operatorname{rank}_{\mathbb F_q}(X-Y)\). There is a unique \(\beta_q\in(0,1)\) satisfying
\[
q^2(3^{\beta_q}-2^{\beta_q})=1.
\]
For every real \(t>0\), the powered distance kernel \(d(X,Y)^t\) is conditionally negative semidefinite **if and only if** \(0<t\le\beta_q\). It is strictly negative definite on the real zero-sum coefficient space when \(0<t<\beta_q\), and has a zero-sum nullspace of dimension \(q^2(q-1)(q^3-1)\) exactly at \(t=\beta_q\). The nullspace is precisely the real span of additive characters of rank-three symmetric frequency matrices (under the usual real pairing of conjugate characters).

For \(0<t<\beta_q\), the least dimension of a real Euclidean realization satisfying \(\|z_X-z_Y\|^2=d(X,Y)^t\) is \(q^6-1\). At \(t=\beta_q\), the least dimension is exactly
\[
(q^3-1)(q^2+1).
\]
The exponent also obeys the sharp asymptotic law
\[
\lim_{\substack{q\to\infty\\q\text{ odd prime power}}}q^2\beta_q=\frac1{\log(3/2)}.
\]

## Assumptions and scope
Here \(\operatorname{Sym}_3(\mathbb F_q)\) consists of all symmetric three-by-three matrices over the finite field of **odd** cardinality \(q\); it has \(q^6\) elements. The rank takes the values \(0,1,2,3\) and is subadditive, so the stated distance is a metric. For \(t>0\), its diagonal entries are zero. Strict negative type means
\[
\sum_{X,Y\in V}a_Xa_Yd(X,Y)^t<0
\]
for all nonzero real vectors \((a_X)_{X\in V}\) with \(\sum_Xa_X=0\). The theorem does not cover fields of characteristic two, higher symmetric-matrix sizes, or distances other than the rank distance and its indicated powers.

## Proof
Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\). Because \(2\) is invertible, \((A,B)\mapsto\operatorname{tr}(AB)\) is a nondegenerate bilinear pairing on \(V\). For each frequency \(B\in V\), let \(S_j(B)\) denote
\[
S_j(B)=\sum_{\substack{A\in V\\\operatorname{rank}A=j}}\psi(\operatorname{tr}(AB)),\qquad j=1,2.
\]
For nonzero \(B\), the full character sum vanishes, so the powered-distance multiplier is
\[
F_B(t)=-3^t+(1-3^t)S_1(B)+(2^t-3^t)S_2(B).
\]

**The rank-one transform.** A rank-one symmetric matrix is uniquely \(a vv^{\mathsf T}\) for a fixed representative of each projective line \([v]\in\mathbb P^2(\mathbb F_q)\) and \(a\ne0\). If \(Z(B)\) is the number of projective isotropic points of \(v^{\mathsf T}Bv\), then
\[
S_1(B)=qZ(B)-(q^2+q+1).
\]
The zero-loci of quadratic forms on three variables have, respectively, \(q+1\) projective points when \(B\) has rank one, \(2q+1\) or \(1\) when it has split or anisotropic rank two, and \(q+1\) when it is nondegenerate of rank three. Accordingly, \(S_1\) equals \(-1,q^2-1,-q^2-1,-1\) in those four cases.

**The rank-two transform.** Each rank-two symmetric \(A\) has a unique two-plane \(W=\operatorname{im}A\); its contribution over that plane is the full-rank symmetric-binary-form character sum at the restriction \(B|_W\). In two dimensions, that character sum equals \(q^2(q-1)\), \(0\), \(-q\), or \(+q\) when the restricted form has, respectively, rank zero, rank one, split rank two, or anisotropic rank two. This follows by subtracting the zero and rank-one sums from the vanishing full character sum on \(\operatorname{Sym}_2(\mathbb F_q)\).

If \(B\) has rank one, its two-dimensional radical is the only plane with zero restriction; the others have rank-one restriction. Hence \(S_2(B)=q^2(q-1)\). If \(B\) has rank two with one-dimensional radical \(R\), there are \(q+1\) planes containing \(R\) and \(q^2\) not containing \(R\). Exactly two radical-containing planes have zero restriction in the split case and none in the anisotropic case. On all \(q^2\) complementary planes, the restriction has the binary type of \(B\). This yields \(S_2(B)=q^3-2q^2\) for split rank two and \(S_2(B)=q^3\) for anisotropic rank two.

For nondegenerate rank-three \(B\), every two-plane is \(u^{\perp_B}\) for a unique projective point \([u]\). If \(B(u)=0\), its restriction has rank one and contributes zero; otherwise its binary discriminant is split exactly when \(\eta(-\det B)\eta(B(u))=1\), where \(\eta\) is the quadratic character. Therefore
\[
S_2(B)=-q\,\eta(-\det B)\sum_{[u]\in\mathbb P^2(\mathbb F_q)}\eta(B(u)).
\]
For completeness, diagonalize \(B\) and use additive-character orthogonality and the classical identity \(G^2=\eta(-1)q\) for a quadratic Gauss sum \(G\). For every nonzero \(s\in\mathbb F_q\), the number of vectors solving \(v^{\mathsf T}Bv=s\) is
\[
q^2+q\eta(-\det B)\eta(s).
\]
Multiplying by \(\eta(s)\), summing over nonzero \(s\), and dividing by the \(q-1\) representatives of each projective point gives
\[
\sum_{[u]}\eta(B(u))=q\eta(-\det B).
\]
Consequently \(S_2(B)=-q^2\), independent of its determinant type. This proves the entire four-sector character table.

**Signs and the unique threshold.** Substitution gives the exact four nonconstant multipliers:
\[
\begin{aligned}
\text{rank one:}\quad &-1-q^2(q-1)(3^t-2^t),\\
\text{rank two, split:}\quad &-1+q^2(q-2)(2^t-1)-q^2(q-1)(3^t-1),\\
\text{rank two, anisotropic:}\quad &-1+q^2[(3^t-1)-q(3^t-2^t)],\\
\text{rank three:}\quad &-1+q^2(3^t-2^t).
\end{aligned}
\]
The first is less than \(-1\). The split rank-two multiplier is also less than \(-1\), because \(3^t-1>2^t-1>0\) and \(q-1>q-2\). For the anisotropic rank-two multiplier, observe for every \(t>0\) that
\[
3(3^t-2^t)-(3^t-1)=2\cdot3^t-3\cdot2^t+1>0.
\]
Indeed this expression vanishes at zero and its derivative is positive for nonnegative \(t\), because \(2\log3>3\log2\) and \(3^t\ge2^t\). Since \(q\ge3\), the anisotropic multiplier is likewise less than \(-1\). The rank-three multiplier is strictly increasing, starts at \(-1\), and is positive at \(t=1\). Hence it has the unique zero \(\beta_q\in(0,1)\), with the claimed sign on either side.

Because Fourier characters diagonalize every translation-invariant real symmetric kernel on \(V\), conditional negative semidefiniteness is equivalent to nonpositivity of these multipliers for every nontrivial character. This proves the exact negative-type interval and strictness. There are \(q^3-1\) rank-one matrices and \((q^2+q+1)q^2(q-1)=q^2(q^3-1)\) rank-two matrices. Thus there are exactly
\[
q^6-1-(q^3-1)-q^2(q^3-1)=q^2(q-1)(q^3-1)
\]
rank-three frequency matrices. Double-centering the matrix of squared distances gives a positive semidefinite Gram matrix with rank the number of strictly negative nonconstant Fourier eigenvalues. This proves the minimum embedding dimensions and the exact critical nullspace.

Finally, since \(\beta_q\to0\) and \(3^t-2^t=t\log(3/2)+O(t^2)\) as \(t\to0\), the equation \(q^2(3^{\beta_q}-2^{\beta_q})=1\) yields the displayed asymptotic limit.

## Verification
The standalone file `check_symmetric_three.py` reconstructs the rank-one and rank-two indicator functions on all \(q^6\) symmetric matrices for prime orders \(q=3,5,7\). It independently computes their six-dimensional finite additive Fourier transforms using `numpy.fft.fftn`, correctly accounting for the factor of two in each off-diagonal trace-pairing coordinate. Every nonzero frequency is classified by matrix rank and binary discriminant type, and the resulting Fourier coefficients are compared with the four-sector table above.

Run `python check_symmetric_three.py --primes 3 5 7` after installing Python 3 and NumPy. The recorded run returned `SYMMETRIC_THREE_RANK_NEGATIVE_TYPE_PASS`, with \(728\), \(15624\), and \(117648\) nontrivial frequencies checked, respectively. Small-field checks do not prove the claim for nonprime prime powers; the character argument above does.

For \(q=3\), the critical exponent is approximately \(0.224108978488750\) and the minimum critical Euclidean dimension is \(260\). For \(q=5\), these are approximately \(0.090929239000314\) and \(3224\); for \(q=7\), approximately \(0.048204578872791\) and \(17100\).

## Relationship to prior work
The symmetric-bilinear-forms association scheme and its general character eigenvalues are established in K.-U. Schmidt's 2014 manuscript, whose spectral framework motivates the question. Its eigenvalue theorem, coding applications, and appendix were inspected. The present theorem does not claim those earlier eigenvalues as new: it determines the signs of their particular powered-distance combination across all nonconstant sectors, the single zero crossing, and the precise endpoint embedding rank. S. Sánchez's 2011 work gives general supremal negative-type criteria for arbitrary finite metric spaces, but not this all-field closed threshold. General rank-metric results for unrestricted bilinear matrices do not directly settle the inherited symmetric-subspace metric, because restricting to symmetric matrices changes the character spectrum and may increase the allowable exponent.

## Limitations
The theorem requires odd characteristic and three-by-three symmetric matrices. The code checks prime fields \(3,5,7\), not every prime power or all powers of the distance. The all-field assertion relies on the displayed counting proof, not numerical extrapolation. Independent mathematical validation has not been performed. The underlying character table is already known; a previously unlocated calculation combining that table with standard negative-type theory could subsume the claimed endpoint formula. No exhaustive historical-priority claim is made.

## References
1. Kai-Uwe Schmidt, *Symmetric bilinear forms over finite fields with applications to coding theory*, initial arXiv posting 2014-10-27, arXiv:1410.7184v1, https://arxiv.org/abs/1410.7184. Relevant material: Introduction, Section 2, Theorem 2.2, Appendix A.
2. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, initial arXiv posting 2011-08-02, arXiv:1108.0451v1, https://arxiv.org/abs/1108.0451. Relevant material: Definitions 1.1 and 1.3 and Section 2.
3. Yangxian Wang, Chunsen Wang, Changli Ma and Jianmin Ma, *Association Schemes of Quadratic Forms and Symmetric Bilinear Forms*, Journal of Algebraic Combinatorics 17 (2003), 149–161, DOI:10.1023/A:1022978613368. The accessible HTML rendition was inspected for its introduction, definitions, principal statements, and the opening of its duality argument; no powered-rank-distance theorem was identified in the inspected material.
