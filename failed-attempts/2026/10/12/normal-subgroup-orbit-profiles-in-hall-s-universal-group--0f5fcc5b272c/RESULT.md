# Normal-subgroup orbit profiles in Hall's universal group

## Finding
Let \(\Gamma_F\) be Hall's countable universal locally finite group. For a variety of groups \(\mathcal V\), let \(F_{\mathcal V}(n)\) be the relatively free \(n\)-generated group in \(\mathcal V\), and put
\[
X_{\mathcal V,n}=\{(g_1,\ldots,g_n)\in\Gamma_F^n:\langle g_1,\ldots,g_n\rangle\in\mathcal V\}.
\]
Then the simultaneous conjugacy orbits on \(X_{\mathcal V,n}\) are canonically classified by the finite-index normal subgroups of the relatively free group:
\[
\boxed{
X_{\mathcal V,n}/\operatorname{Inn}(\Gamma_F)
\ \longleftrightarrow\
\{N\trianglelefteq F_{\mathcal V}(n):[F_{\mathcal V}(n):N]<\infty\}.
}
\]
The same quotient is obtained using the full automorphism group \(\operatorname{Aut}(\Gamma_F)\). If \(\mathcal V\) is locally finite, then \(F_{\mathcal V}(n)\) is finite and the right side is its entire normal-subgroup lattice.

A concrete definable specialization is the locus of commuting exponent-\(m\) tuples
\[
C_{m,n}=\{\bar g\in\Gamma_F^n:[g_i,g_j]=1\text{ and }g_i^m=1\text{ for all }i,j\}.
\]
Here the relatively free group is \((\mathbb Z/m\mathbb Z)^n\), so the exact orbit count is
\[
\boxed{
c_m(n)=\left|\operatorname{Sub}\big((\mathbb Z/m\mathbb Z)^n\big)\right|.
}
\]
Thus a family of first-order definable tuple strata in a highly non-\(\omega\)-categorical group has an exact finite orbit profile governed by classical finite-abelian subgroup lattices.

Write \(m=\prod_p p^{a_p}\). Primary decomposition gives
\[
\boxed{c_m(n)=\prod_{p^{a_p}\parallel m}S_{a_p,n}(p),}
\]
where \(S_{a,n}(p)\) is the number of subgroups of \((\mathbb Z/p^a\mathbb Z)^n\). Specializing Birkhoff's subgroup formula to the rectangular type \((a^n)\) gives the explicit finite sum
\[
\boxed{
S_{a,n}(p)=
\sum_{n\ge r_1\ge\cdots\ge r_a\ge0}
 p^{\sum_{i=1}^{a}r_{i+1}(n-r_i)}
 \prod_{i=1}^{a}
 {\,n-r_{i+1}\brack r_i-r_{i+1}}_p,
\qquad r_{a+1}=0.
}
\]
For \(a=1\), this is the Galois number
\[
\boxed{
c_p(n)=G_n(p)=\sum_{k=0}^{n}{n\brack k}_p.}
\]
For example,
\[
(c_2(n))_{n=0}^{8}=1,2,5,16,67,374,2825,29212,417199,
\]
and
\[
(c_6(n))_{n=0}^{3}=1,4,30,448.
\]

For every fixed \(m>1\), the exact orbit count has the sharp quadratic logarithmic growth
\[
\boxed{
\log c_m(n)=\frac{n^2}{4}\log m+O_m(\log n).
}
\]
Equivalently,
\[
c_m(n)=m^{n^2/4+o(n^2)}.
\]

## Proof of the orbit classification
Fix \(\bar g=(g_1,\ldots,g_n)\in X_{\mathcal V,n}\). Since \(\Gamma_F\) is locally finite, the marked subgroup \(A=\langle\bar g\rangle\) is finite. By the universal property of the relatively free group, there is a canonical surjection
\[
\operatorname{ev}_{\bar g}:F_{\mathcal V}(n)\twoheadrightarrow A,
\qquad x_i\mapsto g_i.
\]
Its kernel \(N(\bar g)\) has finite index.

If \(N(\bar g)=N(\bar h)\), then both marked generated subgroups are the same marked quotient
\[
F_{\mathcal V}(n)/N(\bar g),
\]
so the coordinate assignment \(g_i\mapsto h_i\) extends to an isomorphism
\[
\langle\bar g\rangle\cong\langle\bar h\rangle.
\]
Rzepecki records that Hall's group is inner ultrahomogeneous: every finite partial automorphism is realized by conjugation. Applying this to the finite subgroup isomorphism above yields some \(u\in\Gamma_F\) with
\[
u^{-1}g_i u=h_i\qquad(1\le i\le n).
\]
Hence equal kernels imply simultaneous conjugacy.

Conversely, conjugation preserves every group word relation, so simultaneously conjugate tuples have the same evaluation kernel. Thus \(N(\bar g)\) is a complete conjugacy-orbit invariant.

Every finite-index normal subgroup \(N\trianglelefteq F_{\mathcal V}(n)\) occurs. The quotient \(F_{\mathcal V}(n)/N\) is a finite group, and Hall's universality embeds every finite group into \(\Gamma_F\). The images of the free generators then form a tuple with kernel exactly \(N\). This proves the bijection.

The same classification holds for \(\operatorname{Aut}(\Gamma_F)\)-orbits: inner automorphisms are automorphisms, while any automorphism preserves all word relations and hence the kernel. Therefore the inner and full-automorphism orbit partitions agree on every finite tuple locus above.

## Abelian exponent and the exact count
For the variety of abelian groups of exponent dividing \(m\), the relatively free group is
\[
F_{\mathcal V}(n)=(\mathbb Z/m\mathbb Z)^n.
\]
It is abelian, so every subgroup is normal. The general orbit theorem therefore gives
\[
c_m(n)=\left|\operatorname{Sub}\big((\mathbb Z/m\mathbb Z)^n\big)\right|.
\]
Primary decomposition of a finite abelian group is characteristic, so every subgroup splits as the direct product of its \(p\)-primary parts. This yields the product over \(p^{a_p}\parallel m\).

For \((\mathbb Z/p^a\mathbb Z)^n\), a subgroup type is encoded by a nonincreasing sequence
\[
n\ge r_1\ge r_2\ge\cdots\ge r_a\ge0,
\]
where \(r_i\) is the \(i\)-th column length of the subgroup's partition type. Birkhoff's formula gives exactly the summand displayed above. Summing over all possible subgroup types gives \(S_{a,n}(p)\). When \(a=1\), the ambient group is the vector space \(\mathbb F_p^n\), so its subgroups are precisely its vector subspaces and the sum is the Galois number.

## Asymptotic
Let
\[
C_p=\prod_{j\ge1}(1-p^{-j})^{-1}<\infty.
\]
For every Gaussian coefficient,
\[
p^{k(N-k)}\le {N\brack k}_p\le C_p\,p^{k(N-k)}.
\]
In a Birkhoff summand, the explicit power of \(p\) together with the degrees of the Gaussian factors has total exponent
\[
\sum_{i=1}^{a}
\left[r_{i+1}(n-r_i)+(r_i-r_{i+1})(n-r_i)\right]
=
\sum_{i=1}^{a}r_i(n-r_i).
\]
Each term is at most \(\lfloor n^2/4\rfloor\), so there are at most \((n+1)^a\) subgroup types and
\[
S_{a,n}(p)\le C_p^a(n+1)^a p^{a\lfloor n^2/4\rfloor}.
\]
For the matching lower bound, take
\[
r_1=\cdots=r_a=\lfloor n/2\rfloor.
\]
That single subgroup-type term is at least
\[
p^{a\lfloor n^2/4\rfloor}.
\]
Hence
\[
\log S_{a,n}(p)=a\lfloor n^2/4\rfloor\log p+O_{p,a}(\log n).
\]
Multiplying the primary factors gives
\[
\log c_m(n)=\lfloor n^2/4\rfloor\log m+O_m(\log n)
=\frac{n^2}{4}\log m+O_m(\log n).
\]

## Verification
The standalone verifier independently reconstructs the finite combinatorial shadow of the theorem. It enumerates finite-field subspaces by reduced row-echelon forms, brute-forces subgroup lattices of \((\mathbb Z/m\mathbb Z)^n\) for several small \((m,n)\), checks the Chinese-remainder splitting for every subgroup of \((\mathbb Z/6\mathbb Z)^n\) through \(n=3\), and compares direct subgroup enumeration with the specialized Birkhoff formula for homocyclic groups.

It also constructs canonical marked-quotient evaluation tables and verifies that the relation kernel is recovered from each table and that distinct kernels give distinct marked quotients. Finally it checks the growth sandwiches on a range of parameters. Running `python3 verification.py` performs 767 assertions and prints `VERIFY_OK`.

These finite computations are consistency checks. The infinite statement itself follows from Hall universality, inner ultrahomogeneity, and the universal property of relatively free groups.

## Prior boundary
The following ingredients are prior and are not claimed as new: Hall's construction and universality, the conjugacy/inner-ultrahomogeneity property, relatively free groups and varieties, Birkhoff's finite-abelian subgroup formula, and Galois numbers. The retained contribution is their exact synthesis into a canonical finite-tuple orbit classification for Hall's group, together with the explicit commuting exponent-\(m\) conjugacy profile and its sharp \(m^{n^2/4+o(n^2)}\) growth law.

## Sources
- Tomasz Rzepecki, *Inner ultrahomogeneous groups*, arXiv:2405.19640. First submitted May 30, 2024. The paper lists primary MSC \(03\mathrm C45\), states that Hall's universal group is universal for countable locally finite groups, and records its inner ultrahomogeneity.
- P. Hall, *Some Constructions for Locally Finite Groups*, Journal of the London Mathematical Society 34 (1959), 305-319, DOI 10.1112/jlms/s1-34.3.305.
- Garrett Birkhoff, *Subgroups of Abelian Groups*, Proceedings of the London Mathematical Society s2-38 (1935), 385-401, DOI 10.1112/plms/s2-38.1.385.
- Thomas W. Cusick, *Finite Vector Spaces and Certain Lattices*, Electronic Journal of Combinatorics 5 (1998), DOI 10.37236/1355. This is a convenient source for the standard Galois-number terminology.
