# Exact Gaussian–Haar normal-leakage laws for oblique low-rank tangent projections

## Finding

Let integers \(m,n>r\geq1\) be fixed, let \(U\in\mathbb R^{m\times r}\) and \(V\in\mathbb R^{n\times r}\) have orthonormal columns, and put \(P=UU^{\mathsf T}\) and \(Q=VV^{\mathsf T}\). Take two **independent** real random sketches \(\Theta\in\mathbb R^{\ell_L\times m}\) and \(\Omega\in\mathbb R^{\ell_R\times n}\), with integers \(\ell_L,\ell_R\ge r\). In either of the following ensembles the indicated matrices have full column rank almost surely:

* **Gaussian:** every sketch entry is an independent standard normal random variable, with no upper bound imposed on the sketch row count.
* **Haar:** the rows of each sketch are orthonormal and their row space is uniformly distributed on the corresponding Grassmannian; here \(\ell_L\le m\), \(\ell_R\le n\).

For a fixed \(Z\in\mathbb R^{m\times n}\), define
\[
L=U(\Theta U)^\dagger\Theta,\qquad R=V(\Omega V)^\dagger\Omega,
\]
\[
\mathcal P_{\rm ob}Z=LZ+ZR^{\mathsf T}-LZR^{\mathsf T},\qquad
\mathcal P_{\rm orth}Z=PZ+ZQ-PZQ,
\]
and let \(N=(I-P)Z(I-Q)\) be the normal component. The formula for \(\mathcal P_{\rm ob}\) is the oblique tangent-space projector of Carrel–Grigori, Section 4, written in an orthonormal basis of the underlying rank-\(r\) state.

**Theorem (exact Gaussian–Haar leakage and moment boundary).** Define a factor \(a(d,r,\ell;E)\) by
\[
a(d,r,\ell;\mathrm G)=
\begin{cases}
\displaystyle\frac{r}{\ell-r-1},&\ell>r+1,\\
+\infty,&r\le\ell\le r+1,
\end{cases}
\]
for a Gaussian sketch, and
\[
a(d,r,\ell;\mathrm H)=
\begin{cases}
0,&\ell=d,\\
\displaystyle\frac{r(d-\ell)}{(d-r)(\ell-r-1)},&r+1<\ell<d,\\
+\infty,&r\le\ell\le r+1<d,
\end{cases}
\]
for a Haar row-orthonormal sketch. Put \(a_L=a(m,r,\ell_L;E_L)\) and \(a_R=a(n,r,\ell_R;E_R)\). For every fixed \(Z\):

1. If \(N=0\), then \(\mathcal P_{\rm ob}Z=\mathcal P_{\rm orth}Z\) almost surely.
2. If \(N\neq0\) and both factors are finite, then the **exact**, dimension-free-in-the-normal-block mean-square identity is
\[
\boxed{\mathbb E\|\mathcal P_{\rm ob}Z-\mathcal P_{\rm orth}Z\|_F^2
=(a_L+a_R+a_La_R)\|N\|_F^2.}
\]
3. If \(N\neq0\) and at least one factor is infinite, the expectation in (2) is infinite, although the random projected matrix is finite almost surely.

For a **common admissible row count** \(r+1<\ell\le d\), the Haar one-sided leakage factor is exactly \((d-\ell)/(d-r)\) times the Gaussian factor, strictly smaller than it. In particular, complete Haar row-orthogonal sketches produce no leakage, whereas square Gaussian sketches can produce positive or even infinite mean-square leakage.

There is also a **sharp realized-sketch worst-case statement**. Choose orthonormal complements \(U_\perp,V_\perp\) and put
\[
A=(\Theta U)^\dagger\Theta U_\perp,\qquad
B=(\Omega V)^\dagger\Omega V_\perp.
\]
Then
\[
\boxed{\sup_{Z:\,\|N\|_F=1}\|\mathcal P_{\rm ob}Z-\mathcal P_{\rm orth}Z\|_F^2
=(1+\|A\|_2^2)(1+\|B\|_2^2)-1,}
\]
where the supremum is over any matrices whose normal part has unit Frobenius norm. It is attained by a rank-one normal component formed from leading right singular vectors of \(A\) and \(B\).

As a minimal illustration, take \(m=n=2\), \(r=1\), and \(\ell_L=\ell_R=2\). The Haar-row version equals the ordinary tangent projection **for every draw**; the square-Gaussian version has **infinite expected squared discrepancy for every nonzero fixed normal component**. Thus full row count alone is not equivalent to orthogonalizing the sketch.

## Assumptions and scope

All dimensions are finite; sketches are drawn independently of the **fixed** bases and the **fixed** forcing matrix \(Z\), and independently across the two sides. Gaussian sketches have independent \(N(0,1)\) entries. Haar sketches have rows with orthonormality and uniform random row space; multiplying a sketch by a nonzero scalar does not alter its oblique projector. Only exact arithmetic is claimed. The formulas describe a single instantaneous tangent projection, not a trajectory error estimate, and do not condition on a later data-dependent choice of \(U\), \(V\), or \(Z\).

A matrix with \(N\neq0\) is not required to have rank one; the result holds uniformly across all nonzero normal residual shapes. For \(N=0\), the leakage is identically zero even at an infinite-moment sketch count.

## Proof

**Step 1 (exact orthogonal block splitting).** The two maps \(L\) and \(R\) are idempotents with ranges \({\rm ran}(U)\) and \({\rm ran}(V)\) respectively; hence \(\mathcal P_{\rm ob}\) and \(\mathcal P_{\rm orth}\) agree on the tangent space \(\{Z:(I-P)Z(I-Q)=0\}\). Their discrepancy on arbitrary \(Z\) is thus \(\mathcal P_{\rm ob}N\). Write \(N=U_\perp C V_\perp^{\mathsf T}\). Direct multiplication gives
\[
\mathcal P_{\rm ob}N
=UA C V_\perp^{\mathsf T}+U_\perp CB^{\mathsf T}V^{\mathsf T}-UACB^{\mathsf T}V^{\mathsf T}.
\]
The three displayed terms are pairwise Frobenius orthogonal because their left or right factors belong to mutually orthogonal subspaces. Therefore, exactly for every realized sketch,
\[
\|\mathcal P_{\rm ob}N\|_F^2
=\|AC\|_F^2+\|CB^{\mathsf T}\|_F^2+\|ACB^{\mathsf T}\|_F^2.\tag{1}
\]
For unit Frobenius \(C\), bound each term by the corresponding top singular values. Equality holds for \(C=x y^{\mathsf T}\), where \(x\) and \(y\) are leading right singular vectors of \(A\) and \(B\), proving the sharp deterministic operator-norm statement.

**Step 2 (one-sided rotational isotropy).** For either ensemble, orthogonal transformations fixing \(U\) leave the sketch distribution invariant. Thus, whenever finite, \(\mathbb E(A^{\mathsf T}A)=a_L I_{m-r}\) and \(\mathbb E(B^{\mathsf T}B)=a_R I_{n-r}\). The coefficients are obtained by computing \(\mathbb E\|A\|_F^2/(m-r)\), and similarly for \(B\). Both sides are independent. Hence taking expectations in (1) gives respectively \(a_L\|C\|_F^2\), \(a_R\|C\|_F^2\), and \(a_La_R\|C\|_F^2\). This also proves (2) for unequal sketch ensembles.

**Step 3 (Gaussian factor and exact integrability threshold).** Orthogonal invariance permits \(U=[I_r;0]\). Split \(\Theta=[G\ H]\), where \(G\in\mathbb R^{\ell\times r}\) and \(H\in\mathbb R^{\ell\times(d-r)}\) are independent standard Gaussian matrices. Then \(A=G^\dagger H\) and conditional Gaussian second moments give
\[
\mathbb E[\|A\|_F^2\mid G]=(d-r)\,\mathrm{tr}(G^{\mathsf T}G)^{-1}.
\]
The inverse-Wishart moment identity yields \(\mathbb E\mathrm{tr}(G^{\mathsf T}G)^{-1}=r/(\ell-r-1)\) when \(\ell>r+1\), and infinity for \(r\le\ell\le r+1\). It follows from the density near singular Gaussian matrices, and includes equality at the boundary. For a fixed nonzero \(C\), the same conditional calculation gives \(\mathbb E[\|AC\|_F^2\mid G]=\|C\|_F^2\,\mathrm{tr}(G^{\mathsf T}G)^{-1}\); therefore divergence is not an artifact of taking a worst case over \(C\).

**Step 4 (Haar factor and finite-population correction).** Let \(T=\Theta^{\mathsf T}\Theta\), an orthogonal rank-\(\ell\) projector, and \(W=U^{\mathsf T}TU\). For \(r\le\ell\le d\), \(W\) is invertible almost surely. Writing \(A=W^{-1}U^{\mathsf T}TU_\perp\) and using \(T^2=T\) gives the exact identity
\[
AA^{\mathsf T}=W^{-1}-I_r.\tag{2}
\]
If \(\ell=d\), then \(T=I_d\) and \(A=0\) for every draw. Otherwise, rotate the random row subspace so that \(T=\mathrm{diag}(I_\ell,0)\) and replace the fixed \(U\) by a Haar-random \(d\times r\) orthonormal frame. A Gaussian representation for this frame is
\[
\binom{G}{K}(G^{\mathsf T}G+K^{\mathsf T}K)^{-1/2},
\]
where \(G\) has \(\ell\) rows, \(K\) has \(d-\ell\) rows, and their entries are independent standard normals. Cyclicity of trace gives
\[
\mathrm{tr}(W^{-1})-r=\mathrm{tr}\bigl[(G^{\mathsf T}G)^{-1}K^{\mathsf T}K\bigr].\tag{3}
\]
Since \(G,K\) are independent, the expectation of (3) is \((d-\ell)r/(\ell-r-1)\) when \(\ell>r+1\), and is infinite for \(\ell\le r+1<d\). Divide by \(d-r\) using rotational isotropy in Step 2 to obtain the Haar formula. With \(d-\ell>0\), the same divergence applies to any fixed nonzero normal block \(C\): every fixed nonzero orthogonal direction has the same infinite second moment by isotropy and Tonelli's theorem.

**Step 5 (boundary, strict comparison, and minimal case).** The nonnegative identity (1) implies that either divergent one-sided term forces infinite total expectation for nonzero \(C\), independent of the other side. The Haar/Gaussian ratio follows by division of the two finite factors. For \(d=2,r=1,\ell=2\), the Haar sketch has \(T=I_2\), while the Gaussian factor is infinite because \(\ell=r+1\); the two-sided conclusion follows from (1). All claims are established for arbitrary prescribed finite dimensions and admissible sketch counts.

## Verification

The standalone program `CHECK.py` reconstructs the two oblique projectors from independent Gaussian sketch matrices, tests the three-block Frobenius identity against direct matrix multiplication, tests the sharp realized-sketch operator norm with singular vectors and random competitors, and independently draws Haar-row sketches through QR. With seed 20261014, 36 deterministic sketch-shape checks and 6,000 samples per ensemble at \(r=1,m=8,n=9,\ell_L=\ell_R=6\) gave mean leakage ratios approximately \(0.554486\) (Gaussian) and \(0.171187\) (Haar), compared with the exact expectations \(0.5625\) and \(0.171875\). These samples do not prove an expectation, an infinite-moment claim, or the universal theorem; Steps 1–5 do.

Run with Python 3 and NumPy: `python CHECK.py`.

## Relationship to prior work

Carrel and Grigori (arXiv:2607.03402v1, Section 4, particularly Lemma 4.2 and Proposition 4.4) derive the two-sided oblique tangent projector and explain the deterministic failure mechanism when the normal component of the vector field is large. Their result is the basis of the operator considered here; it does not give the present finite-dimensional Gaussian–Haar mean-square comparison or its integrability boundary.

Tropp, Yurtsever, Udell and Cevher (arXiv:1609.00048v2, Appendix A, especially Fact A.1 and Lemma A.5) establish the classical Gaussian pseudoinverse mean and a one-sided sketched low-rank reconstruction error. Those established identities are used explicitly in Step 3; the Gaussian one-sided ingredient is **not** claimed as new. The present mathematical object is the two-sided oblique tangent projector, with a sharp realized normal-to-tangent norm and an exact finite-population Haar contrast.

Lacotte, Liu, Dobriban and Pilanci (arXiv:2002.00864v5, Sections 1–3) compare Haar/SRHT and Gaussian sketches for the **iterative Hessian sketch**, through limiting inverse-moment spectral laws. Those bounds do not describe the exact pointwise rank-\(r\) two-sided tangent leakage or the finite-dimensional boundaries here. Niu, Garg, Dereziński and Liao (arXiv:2605.24955, Sections 1–2) analyze bias/variance of random-*sampling* oblique projections in regression and CUR; their studied sampling models and objectives differ from the independent real Gaussian and Haar row-space tangent projector evaluated here.

## Limitations

This is an instantaneous projection result for fixed data and sketches sampled independently of that data. It is not an end-to-end dynamical low-rank error bound. Haar row-orthonormal sketches may entail different computational costs; the theorem does not claim they are uniformly preferable in runtime. Finite expectations may still be large near the sketch threshold. No result is asserted for sparse, structured, non-Gaussian independent-entry or complex sketch distributions. The classical inverse-Wishart ingredient is acknowledged, and independent external validation and exhaustive bibliography review have not occurred.

## References

1. B. Carrel and L. Grigori, *Sketch low-rank dynamics: orthogonal vs. oblique projections*, arXiv:2607.03402v1, publicly submitted 2026-07-03. https://arxiv.org/html/2607.03402v1
2. J. A. Tropp, A. Yurtsever, M. Udell and V. Cevher, *Practical sketching algorithms for low-rank matrix approximation*, arXiv:1609.00048v2, Appendix A. https://arxiv.org/pdf/1609.00048
3. J. Lacotte, S. Liu, E. Dobriban and M. Pilanci, *Optimal iterative sketching with the subsampled randomized Hadamard transform*, arXiv:2002.00864v5. https://arxiv.org/pdf/2002.00864
4. C. Niu, S. Garg, M. Dereziński and Z. Liao, *Debiasing random oblique projections for subsampled OLS and fast CUR in high dimensions*, arXiv:2605.24955. https://arxiv.org/abs/2605.24955
