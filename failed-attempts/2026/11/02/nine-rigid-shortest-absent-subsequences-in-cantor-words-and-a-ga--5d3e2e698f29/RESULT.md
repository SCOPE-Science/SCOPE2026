# Nine rigid shortest absent subsequences in Cantor words and a gap-inflation family

## Finding

For an integer \(r\geq2\), put \(m=2r\). Let \(w\) be any binary word of the form
\[
w=1\,0^{g_1}1\,0^{g_2}1\cdots0^{g_{m-1}}1,
\]
where every \(g_j\) is a positive integer, \(g_{2j}\geq3\) for all even indices in range, and \(g_1=g_{m-1}=1\). Define \(A=\{00,01,11\}\) and \(B=\{00,10,11\}\). A subsequence is obtained by deleting symbols without changing the remaining order. Then the *complete set of shortest absent subsequences* is
\[
\operatorname{SAS}(w)=\{a1^{m-3}b:a\in A,\ b\in B\}.
\]
In particular, the shortest absent length is \(m+1\), the subsequence-universality index is \(m\), and there are exactly nine shortest absent subsequences. This complete set is unchanged by arbitrarily increasing internal zero gaps while preserving the stated lower and boundary-gap conditions.

Let \(C_0=1\) and \(C_{k+1}=\mu(C_k)\) with \(\mu(1)=101\) and \(\mu(0)=000\). For every integer \(k\geq2\), the specialization \(w=C_k\) has \(m=2^k\), hence
\[
\operatorname{SAS}(C_k)=\{a1^{2^k-3}b:a\in A,\ b\in B\},\qquad |\operatorname{SAS}(C_k)|=9,
\]
and every binary word of length at most \(2^k\) is a subsequence of \(C_k\).

## Assumptions and scope

Words are finite, linear, binary, and their subsequences need not be contiguous. Subsequence universality is relative to the alphabet \(\{0,1\}\). The general gap theorem assumes an even number \(m\geq4\) of ones, first and last zero gaps exactly one, all intervening odd-indexed gaps at least one, and all even-indexed gaps at least three. The Cantor specialization uses complete substitution iterates at levels \(k\geq2\), not arbitrary prefix lengths. The quantity \(|\operatorname{SAS}(w)|\) counts distinct missing *strings*, not embeddings or occurrences.

## Proof

**1. Shortest-absence recursion.** For a finite binary word \(U\), let \(L(U)\) be the shortest length of a binary word not appearing as a subsequence, and let \(S(U)\) be the set of all absent subsequences of that length. For each letter \(c\in\{0,1\}\), if \(c\) is absent from \(U\), the candidate is the one-letter word \(c\). Otherwise let \(U_c\) be the suffix strictly after the *first* occurrence of \(c\) in \(U\). The candidate length is \(1+L(U_c)\) and the candidate set is \(cS(U_c)\). The minimum of the two lengths is \(L(U)\), and the union of candidates of minimum length is \(S(U)\). This follows because a subsequence beginning with \(c\) has an embedding if and only if its remaining suffix embeds after the first \(c\).

**2. A minimal template.** For \(r\geq2\), define
\[
W_r=101(000101)^{r-1}.
\]
It has \(2r\) ones, successive zero gaps \(1,3,1,3,\ldots,3,1\), and satisfies \(W_{r+1}=101000W_r\). We prove inductively the simultaneous assertions
\[
S(W_r)=A1^{2r-3}B,\quad L(W_r)=2r+1,
\]
\[
S(W_r[1:])=1^{2r-2}B,\quad L(W_r[1:])=2r,
\]
where \(W_r[1:]\) means deletion of the first symbol (zero-based indexing).

For \(r=2\), \(W_2=101000101\). Applying the first-occurrence recursion from step 1 gives
\[
S(W_2)=A1B,\qquad S(01000101)=11B,
\]
of lengths \(5\) and \(4\), respectively; both can also be verified by directly enumerating all binary strings of those lengths and shorter lengths.

For the induction step, write \(W_{r+1}=101000W_r\), and let \(T_i\) be the suffix beginning at position \(i\), for \(0\leq i\leq6\). Thus \(T_6=W_r\), and the suffix after the first \(1\) of \(T_3,T_4,T_5\) is \(W_r[1:]\). Use the recursion and the inductive lengths \(L(T_6)=2r+1\) and \(L(W_r[1:])=2r\). For \(i=5,4,3\), choosing first \(1\) gives length \(2r+1\), while choosing first \(0\) gives length \(2r+2\); therefore each has shortest-absence set \(1^{2r-1}B\). At \(i=2\), both first-letter choices give length \(2r+2\), and the set is \(\{0,1\}1^{2r-1}B\). At \(i=1\), the unique shorter choice starts with \(1\), giving \(1^{2r}B\) and length \(2r+2\). Finally at \(i=0\), both choices tie at length \(2r+3\); their union is
\[
1^{2r+1}B\ \cup\ \{00,01\}1^{2r-1}B=A1^{2r-1}B.
\]
These are precisely the two assertions with \(r\) replaced by \(r+1\). This proves the template lemma for every \(r\geq2\), including universality to length \(2r\).

**3. Gap inflation preserves the exact shortest-absence set.** The specified inequalities on \(g_j\) ensure that \(W_r\) is a subsequence of \(w\), obtained by deleting surplus zeros between the corresponding consecutive ones. Therefore every string of length at most \(2r\) embeds in \(w\), and every length-\(m+1\) string outside \(A1^{m-3}B\) embeds in \(w\).

It remains to show all nine candidate strings are absent in \(w\). For \(a\in A\), set \(\alpha=2-|a|_1\). Because \(w\) begins in \(1\) and has just one zero between its first two ones, any attempted embedding of \(a\) followed by further ones must skip at least \(\alpha\) of the initial source ones before the continuing ones. Analogously, for \(b\in B\) set \(\beta=2-|b|_1\); the final symbol is \(1\) and there is just one zero between the last two ones, so an attempted embedding of preceding ones followed by \(b\) leaves at least \(\beta\) source ones unavailable at the end. The middle block together with \(a\) and \(b\) requires
\[
(m-3)+|a|_1+|b|_1=m+1-\alpha-\beta
\]
source ones, but only \(m-\alpha-\beta\) can be used between those forced boundary exclusions, a contradiction. Thus all nine are absent. Combined with the previous containment, this proves their completeness and their minimal length.

**4. Cantor specialization.** In \(C_k\) the positions of the \(2^k\) ones, in increasing order, are the numbers \(\phi(j)=\sum_{h=0}^{k-1}2b_h3^h\), where \(0\leq j<2^k\) and \(b_h\) are the binary digits of \(j\). For \(1\leq j<2^k\), carrying the trailing binary ones gives
\[
\phi(j)-\phi(j-1)=3^{\nu_2(j)}+1.
\]
Hence the zero gap between the \(j\)-th and \((j+1)\)-st ones is exactly \(3^{\nu_2(j)}\). Every odd-indexed gap is one, every even-indexed gap is at least three, and the first and last gaps are one. The general theorem therefore applies with \(m=2^k\) for every \(k\geq2\).

## Verification

The standalone `checker.py` implements an independent literal earliest-embedding test, plus a right-to-left suffix dynamic program computing *actual* shortest absent subsequence sets. It checks all complete Cantor iterates for levels \(2\) through \(7\), including \(2^7=128\) ones and word length \(2187\). For levels \(2\) through \(4\), it independently enumerates every binary candidate at the predicted shortest missing length. It also tests eight reproducibly generated gap-inflated instances with even numbers of ones from \(4\) through \(18\). These finite checks all pass. They verify examples and implementation consistency, not the unbounded induction on their own.

Reproduce with `python3 checker.py` (Python standard library only).

## Relationship to prior work

Simon-congruence research such as Karandikar, Kufleitner and Schnoebelen (arXiv:1310.1278v1, 2013) treats equality of length-bounded scattered-factor spectra and their global congruence index, not an exact shortest-absence spectrum for Cantor iterates. Kosche, Koß, Manea and Siemer (arXiv:2108.13968v1, 2021), especially their Theorem 3.5 and Lemma 3.20, develop a general description of shortest absent subsequences and monotonicity under subsequence inclusion. These supply related conceptual tools but do not state the explicit nine-word family or the zero-gap stability theorem. Fleischmann and colleagues (arXiv:2202.07981v1, 2022), Section 4, study nearly universal words and report that a general full classification for multiple missing subsequences remains open; they do not classify the specified Cantor or gap family. The 2020 scattered-factor universality paper establishes general universality notions, not this explicit special-family result. No historical novelty or independent verification beyond the stated comparisons is asserted as certain.

## Limitations

The nine-word conclusion depends on the two unit boundary gaps and lower bounds on the internal gaps; arbitrary binary words with the same total number of ones need not satisfy it. No formula is claimed for higher-length absent subsequences, the entire minimal-absent-subsequence set, arbitrary Cantor prefixes, or counting distinct embeddings. The proof is self-contained but its literature-priority assessment is necessarily qualified: further synonymous or unpublished formulations may exist. The 2020 universality paper was accessible by abstract rather than complete primary full text in this comparison.

## References

1. P. Karandikar, M. Kufleitner, P. Schnoebelen, *On the index of Simon's congruence for piecewise testability*, arXiv:1310.1278v1, first posted 2013-10-03. https://arxiv.org/abs/1310.1278
2. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1, first posted 2021-08-31. https://arxiv.org/abs/2108.13968
3. P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, D. Nowotka, *m-Nearly k-Universal Words — Investigating Simon Congruence*, arXiv:2202.07981v1, first posted 2022-02-16. https://arxiv.org/html/2202.07981v1
4. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, first posted 2020-03-10. https://arxiv.org/abs/2003.04629
