# Exact singular spectrum of the balanced multiset-deletion weighting for order-preserving transformations

## Finding

Let \(n\ge2\) and \(1\le r\le n\). The canonical balanced weighting of the rank-\(r\) Green class of the monoid of order-preserving transformations of an \(n\)-point chain is the integer matrix \(E_{n,r}\) whose rows are multisets of size \(r-1\) and whose columns are multisets of size \(r\), both from an alphabet of size \(m=n-r+1\). Its entry counts the positions in a column multiset whose deletion gives the row multiset. This is precisely the weighting of Higgins (2026, Definition 3.4 and Corollary 3.7).

**Theorem.** If \(1\le r<n\), the complete nonzero squared-singular-value spectrum of \(E_{n,r}\) is
\[
\lambda_j=(r-j)(n+j),\qquad
\operatorname{mult}(\lambda_j)=\binom{n-r+j-1}{j},\quad 0\le j\le r-1.
\]
All these eigenvalues are positive and distinct. There are exactly \(\binom{n-1}{r-1}\) positive eigenvalues counted with multiplicity, so the matrix has full row rank. Its operator norm, least singular value, and Euclidean condition number are
\[
\|E_{n,r}\|_2=\sqrt{rn},\qquad
\sigma_{\min}(E_{n,r})=\sqrt{n+r-1},\qquad
\kappa_2(E_{n,r})=\sqrt{\frac{rn}{n+r-1}}.
\]
For the endpoint \(r=n\), the matrix consists of the single entry \(n\), hence has the unique singular value \(n\) and condition number \(1\). The stated formulas cover all other ranks, including \(r=1\) (where the condition number is also \(1\)).

## Assumptions and scope

A multiset \(t\) of size \(k\) over \(m\) colors is identified with its multiplicity vector \(u\in\mathbb N_0^m\) with \(\sum_i u_i=k\). For a column \(t\) and a row \(s\), define \(E_{n,r}(s,t)=\#\{h: \text{deletion of the entry in position }h\text{ from }t\text{ yields }s\}\), with repeated values counted at every occurrence. This fixes the weighting normalization: \(E_{n,r}\) is **not** the underlying zero-one interlacing matrix. The field of the spectral calculation is \(\mathbb R\), with the standard Euclidean inner product on multiset coordinates. Multiplicities refer to eigenvalues of \(E_{n,r}E_{n,r}^{\mathsf T}\); an unused right nullspace may occur because the matrix is rectangular.

## Proof

Put \(m=n-r+1\). For each integer \(k\ge0\), let \(H_k\) be the real homogeneous polynomials of total degree \(k\) in \(m\) indeterminates, with its monomial basis declared orthonormal. Thus \(\dim H_k=\binom{m+k-1}{k}\). Define the deletion map \(D_k:H_k\to H_{k-1}\), for \(k\ge1\), by \(D_k=\sum_{i=1}^m\partial_{x_i}\). In the monomial basis the coefficient of \(x^{u-e_i}\) in \(D_kx^u\) is \(u_i\), exactly the number of ways to delete color \(i\). Therefore \(E_{n,r}\) is the matrix of \(D_r\).

Let \(U_k=D_{k+1}^{*}:H_k\to H_{k+1}\). By transposition, \(U_kx^u=\sum_i(u_i+1)x^{u+e_i}\). Directly on every monomial of degree \(k\), the commutator satisfies
\[
D_{k+1}U_k-U_{k-1}D_k=(2k+m)I_{H_k},
\]
where \(U_{-1}D_0=0\). Indeed, different-coordinate summands commute, and for each coordinate the difference between lowering-then-raising and raising-then-lowering is \(2u_i+1\), summing to \(2k+m\). Consequently
\[
\|U_kh\|^2=\|D_kh\|^2+(2k+m)\|h\|^2,
\]
so every \(U_k\) is injective, and every \(D_{k+1}\) is surjective.

For each \(j\ge0\), define the primitive subspace \(K_j=\ker D_j\subseteq H_j\), with \(K_0=H_0\). Surjectivity implies for \(m\ge2\)
\[
\dim K_j=\binom{m+j-1}{j}-\binom{m+j-2}{j-1}=\binom{m+j-2}{j}.
\]
Repeated commutation gives, for any \(h\in K_j\) and \(p\ge1\),
\[
D_{j+p}U^{p}h=p(2j+m+p-1)U^{p-1}h.
\]
Here \(U^p\) is the composition of degree-raising maps, and the convention for \(p=0\) is the identity. Inductively, \(H_k=\bigoplus_{j=0}^k U^{k-j}K_j\). To prove this decomposition, use the orthogonal splitting \(H_k=\operatorname{im}U_{k-1}\oplus K_k\), since \(D_k=U_{k-1}^*\), and induct on \(k\); injectivity of \(U_{k-1}\) guarantees no lost summands.

The row Gram operator is \(D_rU_{r-1}\) on \(H_{r-1}\). On the summand \(U^{r-1-j}K_j\), the preceding formula (with \(p=r-j\)) yields
\[
D_rU_{r-1}\big(U^{r-1-j}h\big)
=(r-j)(r+j+m-1)U^{r-1-j}h.
\]
Substitute \(m=n-r+1\) to obtain \((r-j)(n+j)\). Distinctness follows from \((r-j)(n+j)=rn-j(n-r+j)\), strictly decreasing in \(j\) for \(n>r\), and the multiplicity is \(\dim K_j=\binom{n-r+j-1}{j}\). Each eigenvalue is positive because \(0\le j<r\), proving full row rank.

The largest is \(rn\), at \(j=0\), and the smallest is \((r-(r-1))(n+r-1)=n+r-1\), at \(j=r-1\). Taking square roots gives the asserted norm, least singular value and condition number. If \(m=1\), there is one monomial at each degree and the deletion operator sends the degree-\(r\) monomial to \(r\) times the degree-\(r-1\) monomial, giving the separate endpoint case. This also handles the trivial \(r=1\) spectrum by the general formula.

## Verification

The accompanying standalone `verify.py` constructs integer deletion matrices by independently removing each multiset entry. It checks matrix dimensions, the previously known constant margins, exact commutators, traces, and full row rank, then numerically checks the complete Gram spectrum for every \(2\le n\le10\) and every \(1\le r\le n\), including the square endpoint. The observed result was `VERIFY_OK cases=54`. These finite checks are consistency tests, not an infinite proof. For example, \(n=5,r=3\) gives squared singular values \(15\) once, \(12\) twice, and \(7\) three times.

## Relationship to prior work

Higgins (2026, Section 3, Definition 3.4, Lemma 3.5 and Corollary 3.7) constructs precisely this deletion weighting, proves its support respects the semigroup's transversal relation, and obtains constant row and column sums. Those facts determine the leading squared singular value \(rn\) but not the remaining eigenvalues and multiplicities. The present result supplies the complete spectrum, rank, and exact conditioning for that new canonical semigroup-theoretic matrix; it does not reassert the permutation-matching existence theorem.

Fomin (1994) develops the general use of up/down operators on graded graphs. The commutator and primitive-space argument used here are in that tradition; these methods are not asserted to be new. What is evaluated is the specific multiplicity-sensitive deletion operator introduced in the 2026 semigroup construction. An equivalent formulation in older operator/graded-graph literature remains a priority risk.

## Limitations

The theorem applies to the **weighted** deletion matrix and does not give the spectrum of the unweighted transversal incidence matrix, the permutation matching itself, or matrices for other transformation semigroups. The endpoint \(r=n\) is treated separately. Spectra are over the real numbers and depend on the ordinary Euclidean monomial-coordinate normalization; changing row or column weights changes the singular values. No assertion of absolute publication priority or independent validation is made.

## References

1. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1 (first posted 2026-10-01), especially Section 3, Definition 3.4 and Lemma 3.5; https://arxiv.org/pdf/2610.01912.
2. S. Fomin, *Duality of graded graphs*, Journal of Algebraic Combinatorics **3** (1994), 357–404, doi:10.1023/A:1022412010826. General graded up/down-operator context.
