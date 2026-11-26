# The real nuclear norm of finite abelian convolution tensors

## Finding

Let \(G\) be a finite abelian group of order \(n\geq 1\), let \(e_g\) denote the standard orthonormal basis of the real Hilbert space \(\ell_2(G;\mathbb R)\), and set
\[
\mathcal T_G=\sum_{g,h\in G}e_g\otimes e_h\otimes e_{g+h}.
\]
Define \(r=|G[2]|\), where \(G[2]=\{g\in G:2g=0\}\). Then its exact threefold real Hilbertian projective (tensor nuclear) norm is
\[
\boxed{\|\mathcal T_G\|_{\pi,\mathbb R}=\sqrt n\,[r+\sqrt2\,(n-r)].}
\]
For the same coefficient tensor over complex Euclidean spaces, the previously known complex norm is
\[
\|\mathcal T_G\|_{\pi,\mathbb C}=n^{3/2}.
\]
Consequently,
\[
\frac{\|\mathcal T_G\|_{\pi,\mathbb R}}{\|\mathcal T_G\|_{\pi,\mathbb C}}=
\sqrt2-(\sqrt2-1)\frac rn,
\]
with equality of the real and complex norms if and only if \(G\) has exponent dividing \(2\). At order four, the real norm is \(4+4\sqrt2\) for the cyclic group and \(8\) for the Klein four-group, despite the common order and common complex norm \(8\).

## Assumptions and scope

All group operations are written additively. The standard basis has counting-measure normalization, so each \(e_g\) has Euclidean norm one. Over either scalar field \(\mathbb F\in\{\mathbb R,\mathbb C\}\), the threefold projective tensor norm is
\[
\|T\|_{\pi,\mathbb F}=\inf\left\{\sum_{j=1}^{N}\|a_j\|_2\|b_j\|_2\|c_j\|_2:
T=\sum_{j=1}^{N}a_j\otimes b_j\otimes c_j,\quad N\in\mathbb N\right\}.
\]
The dual injective norm is the supremum of the absolute trilinear evaluation over three unit Euclidean vectors; the dual pairing is the coefficient pairing. No normalized-Haar-measure factors are hidden in the formula. The assertion is for finite abelian groups; no nonabelian generalization is asserted.

## Proof

**1. Real Fourier blocks.** Let \(\widehat G\) be the character group. Use the unitary Fourier transform
\[
\widehat x(\chi)=n^{-1/2}\sum_{g\in G}x(g)\overline{\chi(g)}.
\]
Then
\[
\widehat{x*y}(\chi)=\sqrt n\,\widehat x(\chi)\widehat y(\chi),\qquad
(x*y)(k)=\sum_{g+h=k}x(g)y(h).
\]
A real vector satisfies \(\widehat x(\bar\chi)=\overline{\widehat x(\chi)}\). Exactly \(r\) characters are real-valued: their values belong to \(\{\pm1\}\), and the number of such characters equals \(|G[2]|\) by finite abelian duality. The remaining characters split into \((n-r)/2\) unordered conjugate pairs. On a real-valued character use the scalar coordinate \(a_\chi=\widehat x(\chi)\); on each chosen nonreal pair use \(X_\chi=\sqrt2\widehat x(\chi)\in\mathbb C\cong\mathbb R^2\). Parseval makes this an orthogonal real-linear change of coordinates. Applying convolution diagonalization and the real Parseval pairing gives, for all real vectors \(x,y,z\),
\[
\langle x*y,z\rangle
=\sqrt n\sum_{\chi=\bar\chi}a_\chi b_\chi c_\chi
+\sqrt{\frac n2}\sum_{\{\chi,\bar\chi\},\,\chi\ne\bar\chi}
\operatorname{Re}\bigl(X_\chi Y_\chi\overline{Z_\chi}\bigr).
\]
Thus the tensor is orthogonally block diagonal: one scalar multiplication tensor of amplitude \(\sqrt n\) for each real character, and one real complex-multiplication tensor of amplitude \(\sqrt{n/2}\) for each nonreal pair. This includes the trivial group, where the second sum is empty.

**2. The real complex-multiplication block.** In the standard orthonormal basis \((1,i)\) of \(\mathbb C\cong\mathbb R^2\), the trilinear tensor \(C\) defined by
\[
C(x,y,z)=\operatorname{Re}(xy\overline z)
\]
has precisely the four nonzero coefficients \(C_{111}=1\), \(C_{221}=-1\), \(C_{122}=1\), and \(C_{212}=1\). Thus \(\|C\|_{\pi,\mathbb R}\le4\) by its four-term coordinate decomposition. Also
\[
|C(x,y,z)|\le|x||y||z|,
\]
with equality at \(x=y=z=1\), hence \(\|C\|_{\varepsilon,\mathbb R}=1\). Duality with \(C\) itself yields
\[
\|C\|_{\pi,\mathbb R}\ge\frac{\langle C,C\rangle}{\|C\|_\varepsilon}=4.
\]
Therefore \(\|C\|_{\pi,\mathbb R}=4\), whereas the scalar unit tensor has projective norm \(1\).

**3. Additivity of these orthogonal trilinear blocks.** For any family of tensors supported on mutually orthogonal coordinate subspaces *in all three factors*, the projective norm of their block-direct sum is the sum of their projective norms. The triangle inequality gives the upper bound. For the lower bound, choose a norm-one injective dual witness on each block (finite-dimensional norm duality). Their block sum has injective norm at most one: for block components of unit vectors,
\[
\sum_j\|x_j\|\|y_j\|\|z_j\|
\le\left(\sum_j\|x_j\|^2\right)^{1/2}
\left(\sum_j\|y_j\|^2\right)^{1/2}
\left(\sum_j\|z_j\|^2\right)^{1/2}.
\]
The sum of the block witnesses pairs with the block-diagonal tensor to give the sum of their individual projective norms. Combining this observation with Steps 1 and 2,
\[
\|\mathcal T_G\|_{\pi,\mathbb R}
=r\sqrt n+\frac{n-r}{2}\,4\sqrt{n/2}
=\sqrt n\,[r+\sqrt2(n-r)].
\]
The argument constructs both an explicit rank-one decomposition at this cost and a dual certificate attaining it; no numerical optimization is used.

**4. Complex scalar field and field gap.** Over \(\mathbb C\), the unitary Fourier transform makes the convolution trilinear tensor a sum of exactly \(n\) disjoint pure character-coordinate tensors, each of modulus \(\sqrt n\). Their total projective cost is \(n\sqrt n\). The injective norm of the original tensor equals \(\sqrt n\): for complex inputs, the Fourier convolution identity and Cauchy–Schwarz give \(\|x*y\|_2\le\sqrt n\|x\|_2\|y\|_2\), attained by a normalized character. Since \(\|\mathcal T_G\|_{\mathrm{HS}}^2=n^2\), duality against \(\mathcal T_G/\sqrt n\) gives the opposite projective bound \(n^{3/2}\). This is also the abelian case of Derksen's established complex group-algebra formula. Finally, \(r=n\) precisely when every character is real-valued, equivalently when every group element has order at most two, proving the stated equality criterion.

## Verification

The accompanying standalone `verify.py` implements the group convolution array, real and complex orthonormal Fourier bases, both transformed tensors, and the block-dual certificate for direct products of cyclic groups. Running `python verify.py` with NumPy checks the groups with invariant-factor lists \((1),(2),(3),(4),(5),(6),(7),(8),(2,2),(2,3),(2,4),(3,3),(2,2,2)\). All tests passed, including orthogonality, absence of cross-block entries, the four-coefficient complex-multiplication blocks, certificate pairing, and sampled injective inequalities. Finite checks are supplementary only; Steps 1–4 prove the theorem for *all* finite abelian groups.

## Relationship to prior work

Prochno's October 2026 construction uses exactly this cyclic convolution support, but Proposition 3.1 determines its trilinear/injective norm and Hilbert–Schmidt norm, not its real threefold projective norm. Derksen's 2015 work already computes the **complex-field** projective norm for arbitrary finite group-algebra tensors (and therefore gives \(n^{3/2}\) here); that part is background, not claimed as new. Dai and Lim study the real complex-multiplication tensor and its norm \(4\), an essential constituent of the proof, but do not determine the real group-algebra norm or its dependence on the size of the \(2\)-torsion subgroup. The new result is the exact real assembly and its sharp, group-dependent field gap. The earlier paper of Giladi and collaborators concerns general projective tensor geometry rather than the real norm of this particular group-algebra tensor.

## Limitations

The calculation uses abelian Fourier blocks and does not provide a nonabelian real Wedderburn-block formula. It does not assert that the individual tensor rank is the number of terms in an optimal projective-norm decomposition. The complex-field value and the local \(\mathbb C\)-multiplication norm were known; their combination with real Fourier block additivity is short, and additional older literature on real group-algebra tensor norms could contain an equivalent classification. The numerical checks cannot establish an infinite family theorem. Independent mathematical review and final publication-priority assessment have not been performed.

## References

1. J. Prochno, *Cyclic group tensors and the volume ratio of projective tensor products*, arXiv:2610.29524v1 (first submitted 21 October 2026), especially Proposition 3.1. https://arxiv.org/html/2610.29524v1
2. H. Derksen, *On the Nuclear Norm and the Singular Value Decomposition of Tensors*, Found. Comput. Math. 16 (2016), 779–811; preprint arXiv:1308.3860, especially Section 1.6, Theorem 1.11 and Corollary 1.12. https://arxiv.org/abs/1308.3860
3. Z. Dai and L.-H. Lim, *Numerical stability and tensor nuclear norm*, preprint arXiv:2207.08769v1, particularly Section 5.1. https://arxiv.org/abs/2207.08769
4. S. Friedland and L.-H. Lim, *Nuclear Norm of Higher-Order Tensors*, Math. Comp. 87 (2018), 1255–1281, arXiv:1410.6072. https://arxiv.org/abs/1410.6072
5. O. Giladi, J. Prochno, C. Schütt, N. Tomczak-Jaegermann and E. Werner, *On the geometry of projective tensor products*, J. Funct. Anal. 273 (2017), 471–495, arXiv:1608.08436. https://arxiv.org/abs/1608.08436
