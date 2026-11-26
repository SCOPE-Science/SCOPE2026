# Frobenius-dilation formula for unit groups of finite monomial algebras

## Finding

Let \(k=\mathbb F_q\) have characteristic \(p\), with \(q=p^e\), and let \(I\subset k[x_1,\ldots,x_d]\) be a proper zero-dimensional monomial ideal. Its standard monomial set is
\[
S=\{\alpha\in\mathbb N^d:x^\alpha\notin I\},\qquad N=|S|.
\]
For every integer \(r\ge0\), put
\[
s_r=|\{\alpha\in S:p^r\alpha\in S\}|.
\]
For \(R=k[x_1,\ldots,x_d]/I\), the exact number of units whose order divides \(p^r\) is
\[
|\{u\in R^\times:u^{p^r}=1\}|=q^{N-s_r}.
\]
Writing \(K_r=e(N-s_r)\), so \(K_0=0\), and
\[
m_r=2K_r-K_{r-1}-K_{r+1}\qquad(r\ge1),
\]
the complete abstract unit-group structure is
\[
R^\times\cong C_{q-1}\times\prod_{r\ge1}C_{p^r}^{m_r}.
\]
Here \(C_m\) denotes a cyclic group of order \(m\), with \(C_1\) trivial. Only finitely many \(m_r\) are nonzero.

## Assumptions and scope

The ideal \(I\) is monomial, proper, and zero-dimensional, so \(S\) is finite and the quotient is a finite-dimensional commutative local algebra with maximal ideal \(J=(x_1,\ldots,x_d)R\) and residue field \(k\). The result concerns the abstract multiplicative group of units; it does not classify ring isomorphisms or the embedding of the unit group into other groups.

## Proof

Every element of \(R\) has a unique expansion in the standard monomial basis \(\{x^\alpha:\alpha\in S\}\). The constant-term map identifies the residue field with \(k\), and each unit is uniquely \(c(1+z)\) with \(c\in k^\times\) and \(z\in J\).

In characteristic \(p\), the Frobenius identity gives
\[
(c(1+z))^{p^r}=c^{p^r}(1+z^{p^r}).
\]
If this equals \(1\), reduction modulo \(J\) gives \(c^{p^r}=1\). Since \(k^\times\) has order \(q-1\), coprime to \(p\), this forces \(c=1\); the remaining condition is \(z^{p^r}=0\).

Write \(z=\sum_{\alpha\in S\setminus\{0\}}c_\alpha x^\alpha\). Frobenius is additive in characteristic \(p\), hence
\[
z^{p^r}=\sum_{\alpha\in S\setminus\{0\}}c_\alpha^{p^r}x^{p^r\alpha},
\]
where a term is zero exactly when \(p^r\alpha\notin S\). Distinct exponent vectors remain distinct after multiplication by \(p^r\), so no surviving terms cancel. Therefore \(z^{p^r}=0\) precisely when \(c_\alpha=0\) for each nonzero \(\alpha\) with \(p^r\alpha\in S\). There are \(s_r-1\) such constrained coefficients among \(N-1\) coefficients, leaving \(N-s_r\) free coefficients. This proves the torsion count \(q^{N-s_r}\).

The group \(U=1+J\) is a finite abelian \(p\)-group, and \(R^\times\cong k^\times\times U\). Put \(K_r=\log_p|U[p^r]|=e(N-s_r)\). If \(U\cong\prod_i C_{p^{a_i}}\), then \(K_r=\sum_i\min(r,a_i)\). Taking second differences shows that the number of cyclic factors of exact order \(p^r\) is \(m_r=2K_r-K_{r-1}-K_{r+1}\). This yields the asserted full decomposition. Since \(S\) is finite, for all sufficiently large \(r\), \(s_r=1\); hence the second differences eventually vanish.

## Verification

The standalone script `verify.py` constructs quotient-ring multiplication from standard monomials and exhaustively enumerates all radical elements for four small monomial ideals over \(\mathbb F_2\) and \(\mathbb F_3\). For each ring and each \(r\in\{1,2,3\}\), it compares the direct count of solutions to \(z^{p^r}=0\) with \(q^{N-s_r}\). All 24 comparisons pass. These finite checks are sanity checks; the proof above establishes the general statement.

For example, if \(R=\mathbb F_2[x,y]/(x^3,y^3)\), then \(N=9\), \(s_1=4\), and \(s_r=1\) for \(r\ge2\). Thus \(K_1=5\), \(K_2=K_3=8\), giving \(m_1=2\), \(m_2=3\), and all later multiplicities zero. Consequently \(R^\times\cong C_2^2\times C_4^3\).

## Relationship to prior work

E. V. Zhuravlev's 2014 study treats unit groups of commutative finite local rings of characteristic \(p\) with \(\dim_k J/J^2=3\), \(\dim_k J^2/J^3=1\), \(\dim_k J^3=1\), and \(J^4=0\). His 2017 paper gives explicit unit-group structures for the different fixed layer profile \((\dim_k J/J^2,\dim_k J^2/J^3,\dim_k J^3)=(2,2,1)\), again with \(J^4=0\). The inspected 2017 theorem is a case-by-case classification for that bounded radical profile; it does not state the standard-monomial dilation formula for arbitrary zero-dimensional monomial ideals. The present claim is a uniform formula for all such ideals, using the survival counts under exponent dilation by \(p^r\).

## Limitations

The theorem assumes a commutative quotient by a monomial ideal over a finite field. It does not assert the same formula for arbitrary nonmonomial ideals or noncommutative finite local algebras. The 2014 paper's full text was not accessible during this run; its abstract and bibliographic metadata indicate a different fixed Hilbert-function case. The literature search was not exhaustive, so a broader published result implying this formula remains a residual possibility. The computational checks cover only the explicitly listed small examples.

## References

1. E. V. Zhuravlev, “On unit group of a finite local rings of characteristic \(p\),” *Siberian Electronic Mathematical Reports* 11 (2014), 362–371; published 23 May 2014. MathNet record: `semr494`.
2. E. V. Zhuravlev, “On unit group of a finite local rings with 4-nilpotent radical of Jacobson,” *Siberian Electronic Mathematical Reports* 14 (2017), 552–567. DOI: `10.17377/semi.2017.14.048`; full text inspected.
