# Three-band spectral phase transition for symmetrized tensors of alternating weighted shifts

## Finding
Let \(S\) be a unilateral weighted shift on complex \(\ell^2(\mathbb N_0)\), with \(Se_j=w_j e_{j+1}\) and \(w_{2j}=a>0\), \(w_{2j+1}=b>0\). On the symmetric and antisymmetric squares, define \(T_+=S\odot S^*\) and \(T_-=S\wedge S^*\), using the factor \(1/2\) in the symmetrization. Put
\[
 c=ab,\qquad d=\frac{|a^2-b^2|}{2},\qquad L=\frac{a^2+b^2}{2}.
\]
**Theorem.** The full spectra, approximate-point spectra, and Fredholm essential spectra are equal for the two tensor products:
\[
 \sigma(T_+)=\sigma(T_-)=\sigma_{\mathrm{ap}}(T_+)=\sigma_{\mathrm{ap}}(T_-)=\sigma_{\mathrm{ess}}(T_+)=\sigma_{\mathrm{ess}}(T_-)
 =[-c,c]\cup[-L,-d]\cup[d,L].
\]
Moreover, \(\|T_+\|=\|T_-\|=L\) is not attained by either operator on a nonzero vector. In contrast, \(\|S\|^2=\max(a,b)^2\), so the strict norm shortfall for \(a\ne b\) is \(d\). There are three disjoint bands precisely when \(\max(a,b)/\min(a,b)>1+\sqrt 2\); otherwise the spectrum is \([-L,L]\). Endpoints belong to the essential spectrum, not to isolated finite-dimensional outlier bands.

## Assumptions and scope
All Hilbert spaces are complex. The weights \(a,b\) are arbitrary finite **strictly positive real numbers**; they need not be distinct. The flip \(R(e_i\otimes e_j)=e_j\otimes e_i\) defines orthogonal \(+1\) and \(-1\) eigenspaces, identified with the symmetric square and exterior square. Explicitly,
\[
 H=\frac12(S\otimes S^*+S^*\otimes S),\qquad T_\pm=H|_{\ker(R\mp I)}.
\]
The Fredholm essential spectrum is the set of real \(\lambda\) for which \(T_\pm-\lambda I\) is not Fredholm. These operators are bounded and selfadjoint, so their full and approximate-point spectra coincide. Only this two-factor, two-periodic setting is asserted.

## Proof
**1. Exact finite decomposition.** The mutually orthogonal subspaces
\[
 K_n=\operatorname{span}\{e_i\otimes e_{n-i}:0\le i\le n\},\qquad n=0,1,2,\ldots,
\]
reduce \(H\), and their direct sum is the full tensor square. In the ordered indicated basis, \(H|_{K_n}=J_n\) is a real symmetric \((n+1)\)-by-\((n+1)\) Jacobi path with zero diagonal and consecutive off-diagonal weights
\[
 h_{n,i}=\frac{w_iw_{n-i-1}}2,\qquad 0\le i<n.
\]
The flip is reflection of the path, commutes with \(J_n\), and its two eigenspaces supply precisely the corresponding blocks of \(T_+\) and \(T_-\). Every block is finite.

**2. All possible finite-block spectral locations.** For even \(n\), the opposite indices \(i\) and \(n-i-1\) have different parity. Thus every edge equals \(ab/2=c/2\). The path's spectrum lies in \((-c,c)\) for every finite \(n\), including its reflection-parity restrictions.

For odd \(n=2m-1\), the indices have the same parity, so the edges alternate between \(A=a^2/2\) and \(B=b^2/2\), beginning and ending with \(A\). Reordering the path by even/odd vertex indices makes its matrix
\[
 J_{2m-1}\simeq\begin{pmatrix}0&C_m\\ C_m^*&0\end{pmatrix},\qquad C_m=A I_m+B L_m,
\]
where \(L_m\) is the strict lower shift on \(\mathbb C^m\). Hence its eigenvalue magnitudes are the singular values of \(C_m\), and all are at most \(A+B=L\).

If \(A\ge B\), the reverse triangle inequality gives \(\|C_mx\|\ge(A-B)\|x\|\), so every singular value lies in \([A-B,A+B]=[d,L]\).

If \(A<B\), the upper-left \((m-1)\)-by-\((m-1)\) principal corner of \(C_m^*C_m\) (when \(m>1\)) is the tridiagonal matrix with diagonal \(A^2+B^2\) and both adjacent diagonals \(AB\). It is bounded below by \((B-A)^2I\), because it equals the compression of a sum of two shift terms or, directly, because the norm of its offdiagonal part is at most \(2AB\). Cauchy interlacing then shows that **at most one** eigenvalue of \(C_m^*C_m\) can be below \((B-A)^2\). On the other hand \(\|C_me_m\|=A\), hence its smallest singular value is at most \(A<ab=c\) (since \(a<b\)). Every other singular value is at least \(B-A=d\). This remains valid for \(m=1\), with the sole singular value equal to \(A\). Therefore in both cases every spectral point of each odd block belongs to \([-c,c]\cup[-L,-d]\cup[d,L]\). Together with the even blocks, this proves the upper inclusion for both infinite operators.

**3. Reverse inclusion, separately for both reflection sectors.** The even-degree matrices \(J_{2m}\) are constant-edge paths. For each \(\lambda\in[-c,c]\), the bilateral constant-edge Jacobi operator with edge \(c/2\) has a plane-wave generalized eigenfunction with energy \(\lambda=c\cos\theta\). Truncate that wave over a long interval placed far from both ends and far from the reflection midpoint of \(J_{2m}\). Its residual-to-norm ratio is \(O(\text{window length}^{-1/2})\). Reflect the truncation; the two supports are disjoint and, at a distance exceeding one lattice step, noninteracting. Their normalized sum and difference are, respectively, reflection-even and reflection-odd approximate eigenvectors with the **same** residual ratio. Choosing larger and larger \(m\) establishes every point of \([-c,c]\) in the approximate-point and essential spectra of both tensor products.

Similarly, the two-sided Jacobi matrix with alternating edges \(A,B\) has two-component Bloch waves. Its dispersion relation is
\[
 \lambda^2=A^2+B^2+2AB\cos\theta,\quad 0\le\theta\le\pi,
\]
so the two bulk intervals are \([-L,-d]\) and \([d,L]\). Truncate a corresponding Bloch wave within the left bulk of \(J_{2m-1}\), leaving an increasing empty gap to the midpoint and the endpoints. The same disjoint-support reflection-even/odd construction gives approximate eigenvectors for both parity restrictions with errors tending to zero. Because all these Weyl vectors can be chosen in *different degree blocks*, they are mutually orthogonal; hence all three intervals lie in both operators' Fredholm essential spectra. In particular there is no possibility of an extra isolated spectral value outside the displayed union. This proves all spectral identities.

**4. Sharp norm and nonattainment.** The common spectral edge \(L\) is contained in both spectra, and Step 2 proves \(\|T_\pm\|\le L\), yielding the norm formula. In an even-degree finite block the norm is strictly less than \(c\le L\), by the strict spectral bound for a finite constant-edge path. For an odd-degree block, \(\|C_m\|<A+B=L\): equality in \(\|(AI_m+BL_m)x\|\le A\|x\|+B\|L_mx\|\le(A+B)\|x\|\) would force \(\|L_mx\|=\|x\|\), and equality of the first triangle inequality would force \(L_mx\) to be a positive scalar multiple of \(x\), impossible for a nonzero vector since \(L_m\) is nilpotent. Thus no finite degree block has eigenvalue \(L\) or \(-L\). The direct sum has no eigenvectors at either endpoint. Since a bounded selfadjoint operator attains its norm only if an eigenvector exists at an endpoint of modulus equal to the norm, neither \(T_+\) nor \(T_-\) attains its norm.

Finally \(\|S\|^2=\max(a,b)^2=L+d\). The outer and central intervals overlap precisely if \(d\le c\). Writing \(r=\max(a,b)/\min(a,b)\), the opposite inequality is \(r^2-1>2r\), equivalent to \(r>1+\sqrt2\), giving the sharp three-band criterion.

## Verification
The proof's nonstandard finite-block location lemma is independently reconstructible from the bidiagonal singular-value reduction and principal-submatrix interlacing, without numerical computation. `periodic_tensor_spectrum_check.py` computes actual finite path matrices, their two reflection sectors, the corresponding odd-degree bidiagonal singular values, and their inclusion in the proposed bands. Its finite tests are diagnostic only: the infinite-dimensional spectral inclusions, endpoint sharpness and essential-spectrum assertions depend on the argument above, not on finite enumeration.

## Relationship to prior work
Garcia, O'Loughlin and Yu (2023) explicitly computed the constant-weight model and asked for general weighted shifts. Tian, Wang and Zhu (first publicly posted 23 July 2025) studied **norm equalities for convergent** shift weights; a nonconstant alternating sequence lies outside their standing convergence assumption. Yang and Zhang (first publicly posted 9 September 2025, Theorem 3.3) gave a general *finite-degree polynomial algorithm for point spectra* of weighted-shift symmetrizations; this supplies the block-level context but does not state or imply by a quoted closed-form theorem the complete three-band full/essential spectrum, sharp parameter threshold, or norm nonattainment for positive nonconstant two-periodic weights. A separate published one-spike result concerns a single exceptional initial weight followed by a constant tail, with isolated detached essential points rather than periodic continuum bands. These distinctions concern mathematical implications, not merely titles.

## Limitations
Only positive two-periodic weights and two-fold tensor products are treated. No complete classification of individual finite-degree eigenvalues or point-spectrum multiplicities is asserted; the Fredholm essential spectral support is fully determined. The criterion is spectral, not a claim of optimal stability under arbitrary perturbations. Exact positivity of both weights is essential to the strict nonattainment argument. Previous spectral-polynomial algorithms encompass the finite decomposition used here, so the incremental contribution is the explicit *global limit* and three-band transition, not discovery of that decomposition. An older equivalent periodic spectral calculation outside the inspected references remains a bibliographic risk.

## References
1. S. R. Garcia, R. O'Loughlin, J. Yu, *Symmetric and Antisymmetric Tensor Products for the Function-Theoretic Operator Theorist*, arXiv:2306.14807 (first posted 26 June 2023), especially Theorem 8.1 and Problem 7. https://arxiv.org/abs/2306.14807
2. X. Tian, P. Wang, Z. Zhu, *The norms for symmetric and antisymmetric tensor products of the weighted shift operators*, arXiv:2507.17181 (first posted 23 July 2025), especially Theorem 1.3. https://arxiv.org/abs/2507.17181
3. Y. Yang, Y. Zhang, *On the spectrum of the symmetric tensor products of certain Hilbert-space operators*, arXiv:2509.07374 (first posted 9 September 2025), especially Theorem 3.3. https://arxiv.org/abs/2509.07374
