# Exact rational minimal-absent-subsequence enumeration for quaternary permutation powers

## Finding
For every integer \(k\ge1\), consider the finite word \(W_k=(0123)^k\) over the fixed ordered alphabet \(\{0,1,2,3\}\). A word \(v\) is a minimal absent scattered subsequence of \(W_k\) when it is not obtainable by deleting positions from \(W_k\), but deleting any single letter of \(v\) produces a subsequence of \(W_k\). Let \(m_k\) count distinct such words, not embeddings. Then
\[
\sum_{k\ge1}m_k z^k=
\frac{-4z^{10}+23z^9-54z^8+49z^7-28z^6+53z^5+3z^4+25z^3+10z}{z^{10}-6z^9+15z^8-16z^7+11z^6-16z^5+3z^4-7z^3+2z^2-4z+1}.
\]
The first twelve values are \(10,40,165,653,2585,10201,40289,159196,629004,2485317,9819749,38798730\). The formula counts the **entire minimal absent antichain**, not merely the shortest absent words. For example \(m_2=40\): exactly \(20\) have length \(3\) and \(20\) have length \(4\).

## Assumptions and scope
The alphabet is the fixed, ordered four-symbol set; \(k\) is any positive integer. The repeated block is increasing. Every permutation of the four symbols has the same count by relabeling. Only distinct *words* are counted. A subsequence need not be contiguous. Empty words and length-one words are never absent here.

## Proof
For a nonempty word \(v=v_1\cdots v_s\), define \(D(v)=\sum_{i=1}^{s-1}\mathbf1_{\{v_i\ge v_{i+1}\}}\). Greedily embedding \(v\) into consecutive increasing permutation blocks uses precisely \(1+D(v)\) blocks. Thus \(v\) embeds in \(W_k\) if and only if \(D(v)\le k-1\).

For length at least two, a minimal absent word must have \(D(v)=k\). Indeed, deleting any letter can lower \(D\) by at most one, while every single deletion must bring \(D\) below \(k\). Deleting the first or last letter lowers \(D\) by one precisely when the respective end pair is weakly decreasing. Deleting an interior letter \(b\) between \(a\) and \(c\) lowers \(D\) by
\[
\delta(a,b,c)=\mathbf1_{\{a\ge b\}}+\mathbf1_{\{b\ge c\}}-\mathbf1_{\{a\ge c\}}.
\]
For a totally ordered alphabet this quantity is at most one. Consequently the necessary and sufficient conditions for minimal absence are: \(D(v)=k\), the first and last pairs are weakly decreasing, and \(\delta(v_{i-1},v_i,v_{i+1})=1\) at every interior position. Since an increasing adjacent pair must be flanked by decreasing pairs, every such word has length between \(k+1\) and \(2k\).

Index sixteen states by ordered pairs \((a,b)\in\{0,1,2,3\}^2\), and put \(d(a,b)=\mathbf1_{\{a\ge b\}}\). Construct a polynomial matrix \(T(z)\) with its \(((a,b),(b,c))\) entry equal to \(z^{d(b,c)}\) when \(\delta(a,b,c)=1\), and zero otherwise (summing contributions if applicable). Let \(e_{(a,b)}=\mathbf1_{\{a\ge b\}}\). A minimal absent word starts with a decreasing pair, extends only along allowed transitions, and ends with a decreasing pair. Its weight is precisely \(z^{D(v)}\). Hence, as formal power series,
\[
F(z)=\sum_{k\ge1}m_kz^k=z\,e^{\mathsf T}(I-T(z))^{-1}e.
\]
The matrix inverse is a well-defined formal power series because every allowed directed cycle consumes a positive number of descents: otherwise it would consist entirely of strict increases around a closed cycle, which is impossible.

The displayed rational expression follows by exact integer-polynomial arithmetic. The accompanying `certificate.json` stores a polynomial denominator \(Q(z)\), numerator \(P(z)\), and sixteen polynomials \(H_{a,b}(z)\). The standalone `verify.py` checks the *symbolic identities*
\[
(I-T(z))H(z)=Q(z)e,\qquad z\,e^{\mathsf T}H(z)=P(z)
\]
coefficient by coefficient over the integers. Since \(Q(0)=1\), these identities prove \(F(z)=P(z)/Q(z)\) for all coefficients, not just a finite prefix. The recurrence is obtained by equating coefficients in \(Q(z)F(z)=P(z)\).

## Verification
Run `python3 verify.py certificate.json` in the folder containing the two embedded artifacts. It verifies all sixteen exact polynomial matrix identities and the numerator identity, checks the first 45 recurrence coefficients, and independently enumerates words using direct greedy subsequence membership and one-letter-deletion tests for 15 parameter configurations on alphabets of sizes two through five. These exhaustive finite checks are corroboration only; the infinite result is certified by the preceding combinatorial argument and symbolic polynomial identities. No third-party system or independent specialist has reviewed the result.

## Relationship to prior work
Kosche, Koß, Manea, and Siemer introduced and characterized minimal absent scattered subsequences and explicitly studied powers of the increasing alphabet permutation in Section 3 of *Absent Subsequences in Words* (arXiv:2108.13968, public 2021-08-31). Their Proposition 3.8 establishes a polynomial-versus-exponential separation between shortest and minimal absent subsequences, using a lower-bound family; it does **not** supply the exact all-minimal enumeration for a four-letter cycle. Their count of shortest absent words alone covers a proper slice of this result. Adamson et al., *Tight Bounds for the Number of Absent Subsequences* (arXiv:2407.18599, public 2024-07-26), investigate counts of all absent subsequences of a fixed length and extremal universality classes, not this minimal-absent antichain. A transfer-matrix method is standard; the specific full rational enumeration and its checked numerator/denominator are the asserted contribution.

## Limitations
This result is specific to powers of a permutation with exactly four distinct symbols; it does not classify arbitrary periodic or nonperiodic words. It does not claim an optimal complexity algorithm for generic input. The literature search cannot establish worldwide uniqueness, and an unindexed equivalent specialization remains possible. Finite word enumeration alone is not the proof. Independent scientific audit has not been performed.

## References
1. Maria Kosche, Tore Koß, Florin Manea, Stefan Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first public version 2021-08-31), https://arxiv.org/abs/2108.13968 ; inspected full-text Section 3: https://arxiv.org/html/2108.13968v6 .
2. Duncan Adamson, Pamela Fleischmann, Annika Huch, Florin Manea, Paul Sarnighausen-Cahn, Max Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (first public version 2024-07-26), https://arxiv.org/abs/2407.18599 ; inspected full text: https://arxiv.org/html/2407.18599v2 .
