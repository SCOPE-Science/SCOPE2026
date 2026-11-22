# Penultimate-level numerical semigroups: the exact embedding-dimension threshold and unique obstruction

## Finding

**Theorem.** Fix an integer \(m\ge3\). For any numerical semigroup \(S\subseteq\mathbb N_0\) with multiplicity \(m\), and any ordered \((m-1)\)-tuple of positive members \((x_1,\ldots,x_{m-1})\), one has

\[
 x_1+\cdots+x_{m-1}-m\notin S
 \quad\Longleftrightarrow\quad
 \bigl(S=\langle m,a\rangle\text{ with }a>m,\ \gcd(m,a)=1\bigr)
 \ \text{and}\ \ x_1=\cdots=x_{m-1}=a.
\]

In particular, writing \(\mathscr L_{n,m}\) for the established class of \(n\)-level numerical semigroups of multiplicity \(m\),

\[
 \mathscr L_{m-2,m}=
 \{S:m(S)=m,\ e(S)\ge3\}.
\]

Every excluded semigroup has exactly **one** violating ordered tuple, whose defective sum is its Frobenius number \((m-1)a-m\). This classifies the last proper tier immediately before the all-semigroup tier \(\mathscr L_{m-1,m}\).

## Assumptions and scope

A *numerical semigroup* is a cofinite additive submonoid of \(\mathbb N_0\). Its multiplicity \(m(S)\) is its least positive element and its ordinary embedding dimension \(e(S)\) is the size of its unique minimal additive generating set. Following the published hierarchy, \(S\in\mathscr L_{n,m}\) means that \(m(S)=m\) and \(x_1+\cdots+x_{n+1}-m\in S\) for **every ordered tuple**, repetitions allowed, of nonzero elements of \(S\). No restriction on conductor, genus, or other generators is imposed. The result is for all integer multiplicities \(m\ge3\).

## Proof

**1. Divisible residues.** Take positive \(x_1,\ldots,x_{m-1}\in S\). If any \(x_i\) is divisible by \(m\), then \(x_i-m\in S\), so the required difference is in \(S\). Otherwise put \(r_i=x_i\bmod m\ne0\). If any nonempty subcollection of the residues sums to zero modulo \(m\), its corresponding positive-element sum is a positive multiple of \(m\) and is therefore at least \(m\); after subtracting \(m\), it remains a nonnegative multiple of \(m\) in \(S\). The remaining summands stay in \(S\). Thus failure requires a zero-sum-free residue sequence of length \(m-1\) in the cyclic group \(\mathbb Z/m\mathbb Z\).

**2. Extremal cyclic lemma.** Such a sequence must consist of \(m-1\) copies of a single generator \(r\) of \(\mathbb Z/m\mathbb Z\). Indeed, its \(m\) prefix sums, including zero, are pairwise different (otherwise an intervening nonempty consecutive block sums to zero), hence occupy the whole cyclic group. If two neighboring residues were different, swapping them would change only the one prefix sum between them. The changed prefix sum would coincide with one of the other, unchanged \(m-1\) prefix sums, contradicting zero-sum-freeness after the swap. Therefore all residues equal \(r\). If \(r\) had order less than \(m\), an initial block of that order, of length at most \(m-1\), would sum to zero. Thus \(\gcd(r,m)=1\).

**3. A two-generator core and its gaps.** Let \(w_r\) be the smallest element of \(S\) congruent to \(r\) modulo \(m\). Each tuple member is \(x_i=w_r+k_i m\) for a nonnegative integer \(k_i\). Put \(T=\langle m,w_r\rangle\subseteq S\). By coprimality, \(T\) is a two-generated numerical semigroup, with Frobenius number

\[
 F_T=(m-1)w_r-m.
\]

For completeness, its gap reflection is elementary: any nonnegative integer \(z\notin T\) has a unique expression \(z=jw_r+\ell m\) with \(0\le j<m\) and integer \(\ell\); since \(z\notin T\), one has \(1\le j<m\), \(\ell\le-1\). Hence

\[
 F_T-z=(m-1-j)w_r+(-1-\ell)m\in T.
\]

If \(S\ne T\), choose a gap \(z\in S\setminus T\); then \(F_T-z\in T\subseteq S\), so \(F_T\in S\). It follows that

\[
 \sum_{i=1}^{m-1}x_i-m=F_T+\bigl(\sum_i k_i\bigr)m\in S.
\]

**4. The unique failure.** Failure thus forces \(S=T\) and every \(k_i=0\): indeed, if \(\sum_i k_i\ge1\), then \(F_T+m=(m-1)w_r\in T\), hence the defective sum is in \(T\). If all \(k_i=0\), then the defective sum equals \(F_T\notin T\). Since \(w_r>m\) and \(\gcd(w_r,m)=1\), the semigroup \(T\) has exactly the two minimal generators \(m,w_r\). Conversely every two-generated semigroup \(\langle m,a\rangle\) with \(m<a\) and \(\gcd(m,a)=1\) has the violating tuple \((a,\ldots,a)\). The second minimal generator is unique, so this is the only violating tuple. This proves both assertions. \(\square\)

## Verification

The standalone `verification.py` enumerates Kunz-coordinate descriptions of all numerical semigroups whose nonzero Apéry representatives have coordinates in \(\{1,2,3,4\}\) for multiplicities \(3\) through \(7\). It independently computes minimal generators by additive decomposability, tests all multisets of \(m-1\) nonzero Apéry representatives, and checks that two-generated semigroups have exactly their predicted witness whereas higher embedding dimensions have none. It checks **2,344** semigroups. Run `python verification.py` to reproduce `VERIFY_OK 2344`. Finite checks corroborate, but do not replace, the unrestricted proof.

## Relationship to prior work

Robles-Pérez and Rosales (2021), Remark 3.13, define the general \(n\)-level hierarchy, prove its endpoint \(\mathscr L_{m-1,m}\) contains every multiplicity-\(m\) semigroup, and give examples showing its strict inclusions. Their Example 3.14 provides a two-generated exclusion and a three-generated inclusion when \(m=5\); these examples and the existing hierarchy are not new. Llena and Rosales (2025) develop the second-level case and its algorithms, with attention to embedding dimension. The theorem above adds the uniform all-multiplicity characterization of the **penultimate** tier and the unique ordered-tuple failure classification. It does not claim to introduce the hierarchy, the two-generator Frobenius formula, cyclic zero-sum extremality, or the \(m=5\) examples.

## Limitations

Only the final proper level is classified; no complete description of the earlier levels \(\mathscr L_{n,m}\), for \(n<m-2\), is claimed. Theorem applies to numerical semigroups under the standard ordinary embedding dimension, not unrelated geometric notions of embedding dimension. Historical priority remains provisional: an unindexed formulation of this precise corollary could exist. No independent mathematical audit has been completed.

## References

1. D. Llena and J. C. Rosales, *Second-Level Numerical Semigroups*, Mathematics **13** (2025), article 593, published 11 February 2025, DOI: https://doi.org/10.3390/math13040593 .
2. A. M. Robles-Pérez and J. C. Rosales, *Modular Frobenius pseudo-varieties*, Collectanea Mathematica **74** (2023), 133–147; first published online 28 October 2021. DOI: https://doi.org/10.1007/s13348-021-00339-0 .
