# Sharp sixth moments and spectral rigidity of Haar-orthogonal matrix coefficients

## Finding
Let \(n\ge3\) and \(1\le k\le n\) be integers, and let \(Q\) be uniformly distributed on the real Stiefel manifold of \(n\times k\) matrices with orthonormal columns (the first \(k\) columns of a Haar-uniform \(O\in\mathrm O(n)\)). For a nonzero real \(n\times k\) matrix \(A\), let \(F_A(Q)=\operatorname{tr}(A^{\mathsf T}Q)\). The exact sharp normalized sixth-moment range is
\[
\frac{15n^2}{(n+2)(n+4)}\le K_{n,k}(A):=\frac{\mathbb E F_A^6}{(\mathbb E F_A^2)^3}\le
\frac{15n^2}{(n-2)(n-1)(n+2)(n+4)}
\left(n^2+3n-2-\frac{6(n+2)}k+\frac{16}{k^2}\right).
\]
The lower equality cases are exactly rank-one coefficient matrices. The upper equality cases are exactly nonzero scalar multiples of matrices with \(A^{\mathsf T}A\) equal to the identity times a positive scalar; that is, all \(k\) singular values are equal and positive. For \(k=1\) these two cases coincide, and the ratio is constant. For \(k\ge2\), all intermediate values occur. The complete \(nk\)-dimensional real Stiefel coefficient space \(X_{n,k}\subset L^6(Q)\) satisfies
\[
d_{\mathrm{BM}}(X_{n,k},\ell_2^{nk}(\mathbb R))=
\left(\frac{n^2+3n-2-6(n+2)/k+16/k^2}{(n-1)(n-2)}\right)^{1/6}.
\]
These inequalities have exact strictly nonnegative spectral-deficit identities displayed below. In particular, when \(k=n\), the sharp upper sixth-moment ratio is exactly \(15\) for every \(n\ge3\).

## Assumptions and scope
All measures are normalized probabilities. The ambient dimension is an integer \(n\ge3\) and the frame size is \(1\le k\le n\). The coefficient field is \(\mathbb R\); no assertions are made for complex coefficients or for \(\mathrm{SO}(n)\) in small dimensions. The random frame is obtained from the full orthogonal group \(\mathrm O(n)\), including both determinant components. The real-linear map \(A\mapsto F_A\) is injective because \(\mathbb EF_A^2=\operatorname{tr}(A^{\mathsf T}A)/n\).

Put \(S=\operatorname{tr}(A^{\mathsf T}A)>0\), \(T=\operatorname{tr}[(A^{\mathsf T}A)^2]\), and \(U=\operatorname{tr}[(A^{\mathsf T}A)^3]\). If \(\sigma_1,\ldots,\sigma_k\) are all \(k\) singular values (zeros included), put \(x_i=\sigma_i^2/S\). Then \(x_i\ge0\), \(\sum_i x_i=1\), \(T/S^2=\sum_i x_i^2\), and \(U/S^3=\sum_i x_i^3\).

## Proof
**Exact moment.** Bi-orthogonal invariance permits singular-value diagonalization of \(A\). The orthogonal pairing integration rule for products of six entries [Gorin 2001; Collins–Śniady 2004] uses the 15 pair partitions of six positions. For two pairings \(p,q\), the Gram matrix entry is \(n^{c(p,q)}\), where \(c(p,q)\) is the number of alternating connected components in their union. The inverse has three entries according to \(c(p,q)=3,2,1\):
\[
a_n=\frac{n^2+3n-2}{n(n-2)(n-1)(n+2)(n+4)},\quad
b_n=-\frac1{n(n-2)(n-1)(n+4)},\quad
c_n=\frac2{n(n-2)(n-1)(n+2)(n+4)}.
\]
To verify the inverse without an external lookup, for any fixed pairing there are respectively \(1,6,8\) pairings with \(3,2,1\) components. The inverse conditions for a fixed second pairing from the same, two-component, or one-component class are
\[
 n^3a_n+6n^2b_n+8nc_n=1,
\]
\[
 n^2a_n+(n^3+n^2+4n)b_n+(4n^2+4n)c_n=0,
\]
\[
 na_n+(3n^2+3n)b_n+(n^3+3n^2+4n)c_n=0.
\]
The system has the indicated unique solution for \(n\ge3\). There are \(15\), \(90\), and \(120\) ordered pairing pairs from these three classes. Their singular-value contractions are \(S^3\), \(ST\), and \(U\), respectively. Thus
\[
\mathbb E F_A^2=\frac Sn,\qquad
\mathbb E F_A^6=\frac{15[(n^2+3n-2)S^3-6(n+2)ST+16U]}{n(n-2)(n-1)(n+2)(n+4)}.
\]
This formula is a concrete application of the pre-existing orthogonal integration calculus, not an assertion that orthogonal integration itself is new.

**Spectral optimization.** Define \(D_n=(n-2)(n-1)(n+2)(n+4)>0\), \(C_n=15n^2/D_n\), and
\[
H_n(x)=n^2+3n-2-6(n+2)\sum_i x_i^2+16\sum_i x_i^3.
\]
Then \(K_{n,k}(A)=C_n H_n(x)\). Write \(e=(1,0,\ldots,0)\) and \(u=(1/k,\ldots,1/k)\). The following two identities hold exactly for every \(x\) in the nonnegative probability simplex:
\[
 H_n(x)-H_n(e)=\sum_{i<j}x_ix_j[12n-8-16(x_i+x_j)],
\]
\[
 H_n(u)-H_n(x)=\frac1k\sum_{i<j}(x_i-x_j)^2
 [6(n+2)-16/k-16(x_i+x_j)].
\]
Since \(x_i+x_j\le1\), the first bracket is at least \(12n-24>0\), and for \(k\ge2\) the second bracket is at least \(6n-12>0\). Both deficits are therefore nonnegative and vanish precisely at their stated endpoints: only one positive coordinate for the first, and every coordinate equal for the second. Multiplying by \(C_n\) proves both sharp inequalities, all equality cases and quantitative spectral rigidity. At \(k=1\), both sums are empty. The coefficient sphere has dimension \(nk-1\ge2\), is connected, and \(K\) is continuous, proving that every intermediate ratio occurs.

**Optimal Euclidean distance.** Let \(\|A\|_X=\|F_A\|_{L^6}\). Any Euclidean comparison on real coefficient matrices is a positive quadratic form \(q\). If \(m\sqrt{q(A)}\le\|A\|_X\le M\sqrt{q(A)}\) for every \(A\), averaging \(q\) over left \(\mathrm O(n)\) and right \(\mathrm O(k)\) preserves the inequalities and yields a scalar multiple of \(\|A\|_F^2\). This follows directly because independent sign changes kill off-diagonal terms in the coordinate quadratic form and independent permutations equalize its diagonal coefficients. Thus the Frobenius ellipsoid is optimal; its sharp norm distortion is the ratio of the upper and lower \(L^6/L^2\) constants, i.e. \((K_{\max}/K_{\min})^{1/6}\), giving the displayed formula.

## Verification
Run `python check_orthogonal_sixth.py` with Python 3 and SymPy. The checker independently multiplies the 15-by-15 pairing Gram matrix by its exact symbolic inverse; reconstructs the sixth-moment polynomial; computes forty independent sixth moments by conditional integration of the first two columns of a random orthogonal frame; checks both sharp endpoint families for every \(3\le n\le80\); and checks both exact nonnegative spectral deficits in 1080 rational test cases. Finite cases corroborate the algebra; the proof above supplies the all-dimensional quantifiers. The checker is included as a standalone file without external project data.

## Relationship to prior work
Gorin, arXiv:math-ph/0112012, derived a general monomial-integration recursion and explicitly calculated the three-diagonal-entry second-power integral in his equation (33): it is exactly the quantity \(a_n\) above. Collins and Śniady, arXiv:math-ph/0402073, established general orthogonal pairing/Weingarten integration. These source results imply a method to calculate the moment polynomial, so the polynomial by itself is not claimed as an independent novelty. The distinct claim here is the simultaneous exact two-sided \(L^6/L^2\) optimization for all rectangular coefficient matrices, complete equality geometry, both globally nonnegative spectral-deficit identities, and optimal Euclidean distortion across every frame size. The prior work inspected concerns integration formulas, not those norm optimizations.

## Limitations
This result applies only to real matrix coefficients on the full Haar orthogonal frame space, integer dimensions \(n\ge3\), and sixth moments. It does not give the corresponding sharp classifications for complex coefficients, even higher moments, or determinant-one orthogonal groups in small dimensions. The moment formula itself is a deduction from established group integration; bibliographic uncertainty remains over a possible unindexed earlier treatment of its sharp norm geometry. Independent mathematical audit has not been performed.

## References
1. T. Gorin, *Integrals of monomials over the orthogonal group*, arXiv:math-ph/0112012v1 (public 2001-12-07), especially Sections 2–4 and equation (33). https://arxiv.org/abs/math-ph/0112012
2. B. Collins and P. Śniady, *Integration with respect to the Haar measure on unitary, orthogonal and symplectic group*, arXiv:math-ph/0402073v1 (public 2004-02-26), especially Section 3.2. https://arxiv.org/abs/math-ph/0402073
