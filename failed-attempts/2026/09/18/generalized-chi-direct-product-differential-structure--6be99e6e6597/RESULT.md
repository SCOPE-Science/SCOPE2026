# Exact inherited invariants for stretched generalized chi permutations

## Scope of the corrected claim

Let
\[
\chi_{n,v}(x)_i=x_i+x_{i+v}x_{i+2v}+x_{i+2v},\qquad i\in\mathbb Z/n\mathbb Z,
\]
and put
\[
d=\gcd(n,v),\qquad \ell=n/d.
\]
Feng, Wang, Yu and Zhang's arXiv v2 (21 September 2026) explicitly observes that \(\chi_{n,v}\) is a stretching of ordinary \(\chi\): the coordinates split into \(d\) interleaved tracks of length \(\ell\), and the map acts as ordinary \(\chi_\ell\) on each track. Their v2 also explicitly observes elementary equivalence between \(\chi_{n,v}\) and their second family \(\chi_{n,-2v}\).

Those two structural observations are therefore **prior work and are not claimed here**. This corrected record keeps only the exact invariant consequences that are not stated in that v2 remark.

Assume the generalized map is a permutation, equivalently \(\ell\) is odd (or, writing \(n=2^k n_0\) with \(n_0\) odd, \(2^k\mid v\)). Then:

1. **Exact order**
   \[
   \operatorname{ord}(\chi_{n,v})
   =\operatorname{ord}(\chi_{n,-2v})
   =2^{\left\lceil\log_2((\ell+1)/2)\right\rceil}.
   \]

2. **Inverse algebraic degree**
   \[
   \deg(\chi_{n,v}^{-1})
   =\deg(\chi_{n,-2v}^{-1})
   =\frac{\ell+1}{2}.
   \]
   For \(\chi_{n,v}\), each inverse coordinate has
   \[
   \binom{(\ell+1)/2}{m}
   \]
   monomials of degree \(m\), hence \(2^{(\ell+1)/2}-1\) nonconstant monomials in total.

3. **Complete differential factorization.** After reindexing rows and columns by the interleaved-track coordinates, if
   \(a=(a^{(0)},\ldots,a^{(d-1)})\) and
   \(b=(b^{(0)},\ldots,b^{(d-1)})\), then
   \[
   N_{\chi_{n,v}}(a,b)
   =\prod_{r=0}^{d-1}N_{\chi_\ell}(a^{(r)},b^{(r)}),
   \]
   where \(N_F(a,b)=|\{x:F(x+a)+F(x)=b\}|\). Equivalently, the DDT is a \(d\)-fold Kronecker product of the DDT of \(\chi_\ell\), up to permutation of rows and columns. Elementary equivalence gives the same differential spectrum for \(\chi_{n,-2v}\).

4. **Exact differential uniformity**
   \[
   \boxed{\delta(\chi_{n,v})=\delta(\chi_{n,-2v})=2^{n-2}},
   \]
   equivalently maximum differential probability \(1/4\).

5. **Iteration preserves the track partition.** Every iterate of either explicit family preserves the \(d\) interleaved coordinate tracks. For even-dimensional permutations, \(d\ge2\), so the nonlinear layer alone never creates cross-track diffusion.

For the nondegenerate nonlinear degree-two permutations in Feng et al.'s full classified family, their shift equivalence to one of the two explicit families transfers shift-invariant quantities such as differential uniformity and inverse algebraic degree with \(\ell=n/\gcd(n,v-w)\).

## Derivation

Feng et al. v2 Remark 1 supplies the interleaved-track decomposition. A direct product of \(d\) copies of the same permutation has the same order as one copy, so the known order formula for ordinary odd \(\chi_\ell\) gives the first statement.

Coordinate relabeling preserves algebraic degree and monomial counts. The known inverse formula for ordinary odd \(\chi_\ell\) therefore gives inverse degree \((\ell+1)/2\) and the displayed monomial counts for the stretched family. Feng et al. v2 Remark 2 supplies elementary equivalence of the second family, which preserves algebraic degree.

For a Cartesian product, the derivative equation separates independently block by block, giving the product formula for \(N_F(a,b)\). For ordinary odd \(\chi_\ell\), the known differential formula has maximum probability \(1/4\). A difference supported in one block attains that value, while a difference supported in more than one block multiplies additional factors no larger than \(1/4\). Therefore the stretched \(n\)-bit permutation also has maximum differential probability \(1/4\), i.e. differential uniformity \(2^{n-2}\).

The iterate statement follows because a direct product remains a direct product under composition; the elementary-equivalent second family has the corresponding conjugate track structure.

## Relation to prior work and revision history

The original SCOPE record was published on 18 September 2026, one day after arXiv:2609.19548 v1. It treated the map-level interleaved-track decomposition and the equivalence of the two generalized families as part of its contribution.

On 21 September 2026, Feng et al. posted v2 with “added a few remarks.” Remark 1 now explicitly says that \(\chi_{n,v}\) is a stretching of ordinary \(\chi\), splitting the state into \(\gcd(n,v)\) interleaved tracks on which ordinary \(\chi\) acts separately. Remark 2 explicitly says that \(\chi_{n,v}\) and \(\chi_{n,-2v}\) are elementary equivalent and therefore have identical cryptographic parameters. Those statements supersede the record's structural originality claim.

The surviving contribution of this corrected record is the explicit transfer of known ordinary-\(\chi\) order and inverse data, the exact Kronecker factorization of the DDT, the closed differential-uniformity value \(2^{n-2}\), and the resulting iteration/diffusion consequences. These are straightforward but useful deductions from the now-published track decomposition.

## Limitations

- No priority is claimed for the interleaved-track decomposition or the equivalence of the two generalized families; both are explicit in arXiv:2609.19548v2.
- The invariant-transfer arguments are elementary once the v2 decomposition is known, so the scientific contribution is a compact characterization rather than a deep new structural theorem.
- Exact order is asserted for the two explicit families. Broader classified-family statements are limited to invariants preserved by the source's shift equivalence.
- The result concerns the nonlinear layer itself and is not a cryptanalytic break of a full cipher with external diffusion.

## References

1. X. Feng, Q. Wang, J. Yu, A. Zhang, *A generalization of the map chi*, arXiv:2609.19548v2, revised 21 September 2026.
2. J. Schoone, J. Daemen, *The state diagram of chi*, Designs, Codes and Cryptography 92 (2024), 1393--1421.
3. J. Schoone, J. Daemen, *Algebraic properties of the maps chi_n*, Designs, Codes and Cryptography 92 (2024), 2341--2365.
