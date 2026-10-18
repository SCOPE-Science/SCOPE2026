# A dyadic degree dictionary for nonmaximal type B and C Schubert varieties
## Finding
Fix integers
\[
n\ge2,
\qquad
1\le r<n,
\]
and put
\[
t=n-r.
\]
Consider the Pluecker embeddings of the symplectic and odd-orthogonal isotropic Grassmannians
\[
\operatorname{IG}(r,2n)
\qquad\text{and}\qquad
\operatorname{OG}(r,2n+1).
\]

Both have dimension
\[
D=2r(n-r)+\frac{r(r+1)}2
\]
and their Schubert classes are indexed by the same set of \(t\)-strict partitions.

For such a partition \(\lambda\), let
\[
X^C_\lambda\subset\operatorname{IG}(r,2n)
\]
and
\[
X^B_\lambda\subset\operatorname{OG}(r,2n+1)
\]
be the corresponding Schubert varieties. Define
\[
\ell_t(\lambda)
=
\#\{i:\lambda_i>t\}.
\]

Then their Pluecker degrees satisfy the exact identity
\[
\boxed{
\deg(X^B_\lambda)
=
2^{\,r-\ell_t(\lambda)}
\deg(X^C_\lambda)
}.
\]

Consequently, for every odd prime \(p\),
\[
\nu_p\!\left(\deg(X^B_\lambda)\right)
=
\nu_p\!\left(\deg(X^C_\lambda)\right),
\]
while
\[
\nu_2\!\left(\deg(X^B_\lambda)\right)
=
\nu_2\!\left(\deg(X^C_\lambda)\right)
+
r-\ell_t(\lambda).
\]

For the ambient varieties, corresponding to the empty partition,
\[
\boxed{
\deg\operatorname{OG}(r,2n+1)
=
2^r
\deg\operatorname{IG}(r,2n)
}.
\]

At the opposite extreme, the top-dimensional Schubert index has exactly \(r\) parts exceeding \(t\), so the point degree agrees exactly on the two sides.

## Assumptions and scope
The base field is \(\mathbb C\). The symplectic space has dimension \(2n\) and the odd orthogonal space has dimension \(2n+1\).

The restriction
\[
r<n
\]
is essential for this formulation. It gives
\[
t=n-r\ge1,
\]
which ensures that the divisor Schubert class indexed by \((1)\) is unchanged by the type \(B\)-to-type \(C\) scaling used in the proof.

The projective degree of a Schubert variety is taken with respect to the restriction of the ambient Pluecker hyperplane class.

## Proof
Let
\[
\sigma_\lambda\in H^*(\operatorname{IG}(r,2n),\mathbb Z)
\]
and
\[
\tau_\lambda\in H^*(\operatorname{OG}(r,2n+1),\mathbb Z)
\]
denote the Schubert classes with common \(t\)-strict index \(\lambda\).

The type \(B\)-to-type \(C\) comparison in the Schubert calculus gives the rational cohomology homomorphism
\[
\Phi(\tau_\lambda)
=
2^{-\ell_t(\lambda)}\sigma_\lambda.
\]

Let
\[
h_C
\qquad\text{and}\qquad
h_B
\]
be the Pluecker hyperplane classes on the symplectic and odd-orthogonal Grassmannians. In both cases the hyperplane class is
\[
c_1(S^*)=c_1(Q).
\]
Because \(t\ge1\), the special Schubert class of degree two is unscaled:
\[
h_C=\sigma_1,
\qquad
h_B=\tau_1,
\qquad
\ell_t((1))=0.
\]
Hence
\[
\Phi(h_B)=h_C.
\]

Let \(\rho\) be the unique top Schubert index. Explicitly,
\[
\rho
=
(2n-r,\,2n-r-1,\,\ldots,\,2n-2r+1).
\]
Its size is
\[
|\rho|=D,
\]
and every one of its \(r\) parts exceeds \(t\), so
\[
\ell_t(\rho)=r.
\]

Put
\[
m=D-|\lambda|.
\]
By definition of projective degree,
\[
h_B^m\tau_\lambda
=
\deg(X^B_\lambda)\tau_\rho
\]
and
\[
h_C^m\sigma_\lambda
=
\deg(X^C_\lambda)\sigma_\rho.
\]

Apply \(\Phi\) to the first identity. Since \(\Phi(h_B)=h_C\),
\[
h_C^m\,2^{-\ell_t(\lambda)}\sigma_\lambda
=
\deg(X^B_\lambda)\,2^{-r}\sigma_\rho.
\]
Using the second identity gives
\[
2^{-\ell_t(\lambda)}
\deg(X^C_\lambda)\sigma_\rho
=
2^{-r}
\deg(X^B_\lambda)\sigma_\rho.
\]
Therefore
\[
\deg(X^B_\lambda)
=
2^{r-\ell_t(\lambda)}
\deg(X^C_\lambda),
\]
as claimed.

The statements about prime-adic valuations are immediate because the ratio is a pure power of \(2\).

## Verification
A bundled exact checker independently verifies the ambient specialization by the Weyl dimension formula.

For every
\[
2\le n\le18,
\qquad
1\le r<n,
\]
it computes the Pluecker degree of the type \(C_n\) homogeneous space \(\operatorname{IG}(r,2n)\) and the type \(B_n\) homogeneous space \(\operatorname{OG}(r,2n+1)\) directly from their positive coroot systems, then checks
\[
\deg\operatorname{OG}(r,2n+1)
=
2^r\deg\operatorname{IG}(r,2n).
\]

It also checks the size and \(t\)-length of the top Schubert partition used in the symbolic proof.

These computations are regression evidence only. The theorem for all Schubert varieties is proved by the cohomological scaling argument above.

## Relationship to prior work
Buch, Kresch, and Tamvakis develop the Schubert calculus of symplectic and odd orthogonal Grassmannians and state the type \(B\)-to-type \(C\) comparison
\[
\tau_\lambda\longmapsto
2^{-\ell_t(\lambda)}\sigma_\lambda.
\]
They also identify the special classes with Chern classes of the tautological quotient bundle, which identifies the Pluecker divisor class needed in the proof.

That comparison is described there as a standard consequence of the relationship between type \(B\) and type \(C\) Schubert structure constants, with earlier work of Bergeron and Sottile among the cited sources.

The degree identity above extracts a geometric enumerative consequence of that ring comparison for every corresponding Schubert variety. Targeted searches using Pluecker degree, Schubert-variety degree, symplectic-versus-orthogonal degree, and exact powers of two did not locate this complete degree dictionary.

## Limitations
The theorem is stated only for the nonmaximal case
\[
r<n.
\]
The maximal orthogonal and Lagrangian cases use different natural minimal embeddings and require separate normalization.

The theorem compares corresponding Schubert varieties under the standard common \(t\)-strict indexing. It does not compare arbitrary subvarieties or other line-bundle embeddings.

The originality argument has residual risk because the degree formula is a short consequence of a known cohomology-ring scaling. An older or unindexed Schubert-calculus source could have recorded the same geometric consequence without using the searched terminology.

## References
Anders S. Buch, Andrew Kresch, and Harry Tamvakis, *Quantum Pieri rules for isotropic Grassmannians*, arXiv:0809.4966, first submitted 29 September 2008; *Inventiones Mathematicae* 178 (2009), 345--405.

Nantel Bergeron and Frank Sottile, *A Pieri-type formula for isotropic flag manifolds*, *Transactions of the American Mathematical Society* 354 (2002), 4815--4829.
