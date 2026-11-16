# Sharp two-erasure recovery of low-degree Wigner signals on tetrahedral rotations

## Finding

There are twelve rotational symmetries of a regular tetrahedron. The complex vector space of Wigner functions on \(\mathrm{SO}(3)\) of degrees zero and one has dimension ten. Retaining exactly ten of these twelve rotations yields unique reconstruction **if and only if** the relative rotation between the two deleted nodes has order three. Of the \(\binom{12}{2}=66\) deletion pairs, precisely 48 permit reconstruction, and precisely 18 do not.

With the normalization specified below, the entire squared singular spectrum in the reconstructible case is
\[
\boxed{\{1/12,\ 1/4,\ 1^{[8]}\}},
\]
where superscripts in brackets denote multiplicity. Thus the sharp squared frame bounds are \(1/12\) and \(1\), and the sharp reconstruction condition number is \(\sqrt{12}\). In the nonreconstructible case the squared spectrum is
\[
\boxed{\{0,\ 1/3,\ 1^{[8]}\}}.
\]
A single missing observation instead produces \(\{1/6,1^{[9]}\}\). Ten observations are minimal by dimension, and the 48 reconstructible choices achieve that minimum.

## Assumptions and scope

Let \(G\cong A_4\) be the order-twelve subgroup of \(\mathrm{SO}(3)\) fixing a regular tetrahedron setwise. Write \(\rho:G\to\mathrm{SO}(3)\) for the faithful real three-dimensional rotational representation. The ten-dimensional signal space is
\[
\mathcal W=\operatorname{span}_{\mathbb C}\bigl\{1,\ R\mapsto R_{ij}:1\le i,j\le3\bigr\}\subset L^2(\mathrm{SO}(3)).
\]
The domain has the normalized Haar inner product. For any retained set \(S\subseteq G\), samples carry the fixed full-design normalization
\[
\|R_Sf\|_S^2=\frac1{12}\sum_{g\in S}|f(g)|^2,
\]
without renormalizing to the number of retained nodes. The eigenvalue multisets below are those of the positive operator \(R_S^*R_S\) on \(\mathcal W\). Both complex and real coefficients are allowed; the same squared singular values hold for the real signal space.

## Proof

**1. Full-design Parseval property.** The restriction \(\rho\) of the three-dimensional rotation representation to \(G\) is irreducible over \(\mathbb C\): as the standard representation of \(A_4\) on the four tetrahedral vertices, it is the four-dimensional permutation representation minus its fixed line. Its character has values \(3\) at the identity, \(-1\) at each of the three nonidentity half-turns, and \(0\) at each of the eight order-three rotations. Consequently
\[
\frac1{12}\sum_{g\in G}|\chi_\rho(g)|^2
=\frac{9+3}{12}=1.
\]
Thus \(\rho\) is irreducible; its matrix coefficients and the constant function are mutually orthogonal under normalized Haar measure on \(\mathrm{SO}(3)\) and under uniform counting measure on \(G\), with identical Schur orthogonality constants. Hence \(R_G\) is an isometry from \(\mathcal W\) into \(\ell^2(G,1/12)\).

**2. The exact projection kernel.** The orthogonal projector \(P\) in the twelve-coordinate sample space onto \(R_G\mathcal W\) has the matrix entries
\[
P_{g,h}=\frac{1+3\chi_\rho(g^{-1}h)}{12}.
\]
Here matrix entries refer to the coordinate-value basis (where the weighted inner product is a scalar multiple of Euclidean inner product). In particular,
\[
P_{g,g}=\frac56,\qquad
P_{g,h}=\begin{cases}-\frac16,&g^{-1}h\text{ is a half-turn},\\ \frac1{12},&g^{-1}h\text{ has order three}.
\end{cases}
\]

**3. Remove two nodes.** Let \(E=\{g,h\}\) be the erased set. Since full restriction is an isometry,
\[
R_{G\setminus E}^*R_{G\setminus E}=I_{\mathcal W}-R_E^*R_E.
\]
The two nonzero eigenvalues of \(R_E^*R_E\) agree, including multiplicities, with those of the principal \(2\times2\) submatrix \(P_{E,E}\). That matrix has diagonal \(5/6\) and off-diagonal \(b\in\{-1/6,1/12\}\), so its eigenvalues are \(5/6\pm b\). If \(b=-1/6\), they are \(1\) and \(2/3\), giving retained eigenvalues \(0,1/3\) and eight further eigenvalues equal to one. If \(b=1/12\), they are \(11/12\) and \(3/4\), giving retained eigenvalues \(1/12,1/4\) and eight further eigenvalues equal to one. This also proves that the upper Riesz bound is exactly one and the invertible condition number exactly \(\sqrt{12}\).

**4. Classification and witnesses.** Each tetrahedral rotation has exactly three half-turn partners and eight order-three partners. Unordered deletion-pair counts are therefore \(12\cdot3/2=18\) and \(12\cdot8/2=48\). If \(g^{-1}h\) is a half-turn, the vector supported at the two erased nodes with values \(+1\) and \(-1\) is fixed by the projection \(P\), because the two columns differ only at those coordinates. In fact, the corresponding continuous nonzero witness is explicitly
\[
f_{g,h}(R)=\frac14\bigl(\operatorname{tr}(Rg^{-1})-\operatorname{tr}(Rh^{-1})\bigr),
\]
which equals \(+1\) at \(g\), \(-1\) at \(h\), and zero at the ten retained group elements. Thus it is the restriction of a unique nonzero \(f\in\mathcal W\) and vanishes on the ten retained nodes. Finally, any fewer than ten observations cannot injectively sample the ten-dimensional space. For a single deletion, the one-by-one deleted principal block has eigenvalue \(5/6\), giving retained squared spectrum \(\{1/6,1^{[9]}\}\).

## Verification

The accompanying dependency-free file `tetra_wigner_check.py` constructs \(A_4\) as the twelve even permutations of four vertices. It computes the irreducible character as the number of fixed vertices minus one, forms the full rational projector, checks \(P^2=P\) and \(\operatorname{tr}P=10\), exhausts all 66 deletion pairs, checks each exact squared spectrum and the 18/48 pair census, and verifies the invisible two-point witnesses for all 18 singular pairs. All calculations use exact rational numbers, not numerical tolerances. The script returned the four PASS messages documented in `VERIFICATION.md`.

## Relationship to prior work

The full 12-node tetrahedral rotation-group quadrature of degree two is **already established** by Gräf and Potts (2009, section 4). Its associated full-grid low-degree isometry is therefore background, not asserted as new here. The present result is the complete **minimal 10-node erasure classification**, including sharp conditioning and the exact half-turn obstruction. Price and McEwen (2023) address Wigner transforms and sampling theorems using structured grids and accelerated algorithms, rather than the two-erasure geometry of this tetrahedral sampling set. McEwen et al. (2015) give another structured rotation-group sampling theorem. A published Wigner-sampling spectrum on twelve fivefold icosahedral rotations concerns a different node set and different representation degrees. Existing results on three-cycle sampling for symmetric groups and on tetrahedral Fourier support do not supply these retained-node singular spectra.

## Limitations

The assertion concerns exactly the constant-plus-degree-one subspace, the actual tetrahedral rotational subgroup and fixed full-design weights \(1/12\); it does not treat arbitrary sampling positions, optimized nonuniform weights, larger bandlimits or noisy model mismatch. The new spectrum is derived from classical character orthogonality and an explicit finite projection; an earlier specialized erasure-frame result with the same spectral conclusion remains a possible historical-priority risk. Computational verification supplements, but does not replace, the full finite-group proof.

## References

1. M. A. Price and J. D. McEwen, *Differentiable and accelerated spherical harmonic and Wigner transforms*, arXiv:2311.14670v1, first public 2023-11-24. https://arxiv.org/html/2311.14670v1
2. M. Gräf and D. Potts, *Sampling sets and quadrature formulae on the rotation group*, Chemnitz preprint 8 (2009), particularly Section 4 and the twelve-point tetrahedral design. https://www-user.tu-chemnitz.de/~potts/paper/so3.pdf
3. J. D. McEwen, M. Büttner, B. Leistedt, H. V. Peiris and Y. Wiaux, *A novel sampling theorem on the rotation group*, arXiv:1508.03101, first public 2015-08-13. https://arxiv.org/abs/1508.03101
