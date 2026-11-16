# Two four-plane spectra and sharp spanning stability of the seven-plane harmonic fusion frame

## Finding

The seven complex harmonic two-planes in \(\mathbb C^7\) explicitly constructed in [1, Theorem 4.2, the order-seven example] have a sharp four-plane spanning theorem. For every four-element subset \(S\subset\mathbb Z/7\mathbb Z\), write \(U_m\) for the corresponding plane, \(P_m\) for its orthogonal projector, and
\[
 A_S=\sum_{m\in S}P_m.
\]
Among the \(\binom74=35\) subsets, there are exactly two complete spectral types, including multiplicities:

* **Type A, 21 subsets:** precisely the affine images of \(\{0,1,2,3\}\). The eigenvalues of \(A_S\) are \(2\) once, \(1+\sqrt{2/3}\) once, \(1-\sqrt{2/3}\) once, \(1+1/\sqrt6\) twice and \(1-1/\sqrt6\) twice.
* **Type B, 14 subsets:** precisely the affine images of \(\{0,1,2,4\}\). The eigenvalues of \(A_S\) are \(2\) once and each of \(1\pm\sqrt{21}/6\), \(1\pm(\sqrt{21}+3)/12\), and \(1\pm(\sqrt{21}-3)/12\) once.

In particular every four of the seven planes span the ambient space; three cannot. The best common lower bound is sharp:
\[
 \min_{\substack{S\subset\mathbb Z/7\mathbb Z\\|S|=4}}\lambda_{\min}(A_S)
 =1-\sqrt{\frac23}=0.183503419\ldots,
\]
with equality for exactly the 21 type-A four-subsets. All four-plane operators have largest eigenvalue \(2\). Equivalently, their sharp worst-case spectral condition number is \(2/(1-\sqrt{2/3})\).

## Assumptions and scope

Let \(\zeta=\exp(2\pi i/7)\), \(\omega=\exp(2\pi i/3)\), \(\alpha=\sqrt{5/12}\), \(\beta=\sqrt{7/12}\). Define a multiplicative character on the nonzero residues by
\[
 \chi(1)=\chi(6)=1,\quad
 \chi(2)=\chi(5)=\omega^2,\quad
 \chi(3)=\chi(4)=\omega.
\]
For \(u\in\mathbb Z/7\mathbb Z\) let \(\Psi_0=(1,0)^{\mathsf T}\), and for \(u\ne0\) let \(\Psi_u=(\alpha,\beta\chi(u))^{\mathsf T}\). Define the \(7\)-by-\(2\) matrix \(\Phi_m\) with rows indexed by \(u\) and columns by \(r\in\{1,2\}\) through
\[
 \Phi_m(u,r)=\sqrt{2/7}\,\zeta^{mu}\,\overline{\Psi_u(r)},\qquad
 U_m=\operatorname{ran}(\Phi_m),\quad P_m=\Phi_m\Phi_m^*.
\]
This is the order-seven instance of [1, Theorem 4.2], up to the harmless conjugate convention. These seven particular rank-two subspaces are the whole domain of the theorem, not arbitrary equi-isoclinic tight fusion frames, and the matrix \(A_S\) is always a seven-dimensional positive-semidefinite operator.

## Proof

**1. Normalization.** The generating vectors obey \(\sum_{u=0}^6\Psi_u\Psi_u^*=(7/2)I_2\): the diagonal entries are \(1+6\alpha^2=7/2\) and \(6\beta^2=7/2\), while the off-diagonal is zero because \(\sum_{u=1}^6\chi(u)=0\). Fourier orthogonality therefore implies \(\Phi_m^*\Phi_m=I_2\), and \(\sum_{m=0}^6P_m=2I_7\).

**2. Two affine orbits.** Translation of plane labels \(m\mapsto m+b\) is conjugation by the unitary coordinate multiplier \(\operatorname{diag}(\zeta^{bu})\). Dilation \(m\mapsto cm\), for \(c\ne0\), is conjugate through coordinate permutation \(u\mapsto c^{-1}u\) and a fixed unitary change of the two generating coordinates, since \(\chi(c^{-1}u)=\chi(c^{-1})\chi(u)\). Thus affine-equivalent subsets produce unitarily similar operators. The affine group has order \(42\). The orbit of \(\{0,1,2,3\}\) has stabilizer order \(2\), hence size \(21\); the orbit of \(\{0,1,2,4\}\) has stabilizer order \(3\), hence size \(14\). They are distinct (their counts of three-term arithmetic-progression triples are different), and their sizes sum to \(35\). This exhausts every four-element subset.

**3. An exact integral cyclotomic matrix.** Put \(h_S(d)=\sum_{m\in S}\zeta^{md}\) for \(d\in\mathbb Z/7\mathbb Z\), and \(T=\operatorname{diag}(\alpha,1,1,1,1,1,1)\). The matrix \(B_S=42T^{-1}A_ST\) has entries, for \(u,v\in\{0,\ldots,6\}\),
\[
 (B_S)_{uv}=h_S(u-v)
 \begin{cases}
 12,&u=0,\\
 5,&u\ne0,\ v=0,\\
 5+7\chi(v)\overline{\chi(u)},&u\ne0,\ v\ne0.
 \end{cases}
\]
(The first case includes \(u=v=0\).) Hence all matrix entries lie in \(\mathbb Z[\zeta,\omega]\), and \(B_S\) is similar to \(42A_S\), so their eigenvalues differ only by the positive factor \(42\).

Write \(Y=t-42\). The exact characteristic polynomials, proved using integer cyclotomic arithmetic in the accompanying complete checker, are
\[
 \begin{aligned}
 \det(tI_7-B_{\{0,1,2,3\}})
   &=(t-84)(Y^2-1176)(Y^2-294)^2,\\
 \det(tI_7-B_{\{0,1,2,4\}})
   &=(t-84)(Y^2-1029)(Y^4-735Y^2+21609).
 \end{aligned}
\]
The checker verifies these two identities for **each of the 35 subsets**, rather than only checking representatives and relying on a claimed symmetry. It implements \(\mathbb Z[\zeta,\omega]\) as the rank-12 integer module with \(1+\zeta+\cdots+\zeta^6=0\) and \(1+\omega+\omega^2=0\), computes all seven traces of matrix powers, and reconstructs each characteristic polynomial using Newton identities. No floating-point equality or unproved modular rank lift is used. Every subset is compared with one of the two stated polynomial factorizations and their counts are checked to be \(21\) and \(14\).

**4. Eigenvalues and sharp bound.** The first factorization gives the stated type-A spectrum after division by \(42\). In the second, \(\sqrt{1029}=7\sqrt{21}\), and
\[
 Y^4-735Y^2+21609
 =\left(Y^2-\tfrac{49}{4}(\sqrt{21}+3)^2\right)
  \left(Y^2-\tfrac{49}{4}(\sqrt{21}-3)^2\right),
\]
which gives type B. Both spectra are positive. The smaller of their two least eigenvalues is \(1-\sqrt{2/3}\), because \(\sqrt{2/3}>\sqrt{21}/6\). Four planes therefore span, and any three can span at most six dimensions. The factors also show \(\lambda_{\max}(A_S)=2\) for every subset. This establishes the complete classification and sharp extremal count.

## Verification

Run `python3 exact_four_plane.py` with a Python 3 standard-library installation. The expected final line is `PASS: all 35 exact integer-cyclotomic matrices have the declared characteristic polynomials`, preceded by the two characteristic coefficient vectors and counts. The test runs over all \(35\) choices and checks equality in a faithful degree-12 cyclotomic integer representation. This finite enumeration is an exhaustive proof of the explicit finite characteristic-polynomial assertions. The matrix derivation and eigenvalue factorization are provided above; merely inspecting a numerical eigensolver would not verify the statements.

## Relationship to prior work

[1] constructs the seven planes, proves their tightness and pairwise equi-isoclinicity, and prints their generating vectors; neither the two four-subset spectra nor the sharp four-block bound is stated there. [2] studies covers of complete graphs and symmetric conference matrix realizations of related fusion frames but does not give the four-subspace spectrum of this specific complex order-seven harmonic family. [3] constructs a different, fully permutation-symmetric family; the two unequal four-subset spectra here specifically distinguish the present family from a totally symmetric one.

Other published classifications of four-block spectra treat the real quadratic-character planes at field order thirteen and a rank-only problem at field order nine. Their hypotheses and matrices differ: their results do not imply the explicit eigenvalues, counts or sharp lower bound at complex field order seven. The claim here is limited to the new four-plane spectral calculation, not a new construction of the underlying EITFF.

## Limitations

No assertion is made for arbitrary seven-plane systems, weighted selections, more general finite fields, or noisy perturbations beyond the optimal positive frame bound. This is one exact finite order-seven calculation certified by complete cyclotomic computation; it is not an infinite-family classification. An earlier equivalent tabulation in specialist complex conference-matrix or fusion-frame literature cannot be categorically excluded by the literature checked here. Independent mathematical verification has not been performed.

## References

[1] M. Fickus, J. W. Iverson, J. Jasper, D. G. Mixon, *Harmonic Grassmannian codes*, arXiv:2112.14267v1, first public 28 December 2021, Theorems 3.4 and 4.2, especially the seven-plane example. https://arxiv.org/html/2112.14267v1

[2] M. Fickus, J. W. Iverson, J. Jasper, D. G. Mixon, *Equi-isoclinic subspaces, covers of the complete graph, and complex conference matrices*, arXiv:2212.12617v1, 23 December 2022. https://arxiv.org/pdf/2212.12617

[3] M. Fickus, J. W. Iverson, J. Jasper, D. G. Mixon, *Totally symmetric Grassmannian codes*, arXiv:2406.19542 (first public 27 June 2024; title of revised version), especially the distinction between fully symmetric and harmonic EITFFs. https://arxiv.org/abs/2406.19542
