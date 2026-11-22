# A complete two-step reverse-complement sphere law over fixed-point-free alphabets

## Finding
Let \(\Sigma\) be a finite alphabet of even cardinality \(q\ge2\), with an involution \(a\mapsto\bar a\) satisfying \(\bar a\ne a\). A length-one reverse-complement duplication replaces one occurrence of \(a\) by \(a\bar a\). For a source \(x\in\Sigma^n\), \(n\ge1\), let \(D_2(x)\) consist of **distinct** words obtainable after exactly two sequential duplications. Write its maximal constant-run decomposition as \(x=a_1^{r_1}\cdots a_m^{r_m}\), and define
\[
C(x)=\sum_{j=2}^{m}r_j\,\mathbf1\{a_j=\bar a_{j-1}\}.
\]
Then the following exact formula holds for every alphabet and source length:
\[
\boxed{|D_2(x)|=\frac{n(n+3)}2-C(x).}
\]
The complete distribution of the penalty statistic has generating function
\[
\boxed{\sum_{n\ge0}z^n\sum_{x\in\Sigma^n}u^{C(x)}=1+\frac{qz(1-zu)}{1-(q-1)z-2zu+qz^2u}.}
\]
For \(n\ge2\), the distinct sphere sizes are precisely all integers from \(n(n+1)/2+1\) through \(n(n+3)/2\). The maximum is attained by exactly \(q(q-1)^{n-1}\) words with no adjacent complementary pair; the minimum by exactly \(q2^{n-2}\) words whose first run has length one and whose successive run letters are complementary. At \(n=1\), both extrema equal two. Under the uniform source distribution,
\[
\mathbb E|D_2(X)|=\frac{n(n+3)}2-\frac{n-1}{q-1}+\frac{1-q^{-(n-1)}}{(q-1)^2}.
\]

## Assumptions and scope
The complement map is fixed-point-free and involutive; there is no assumption that \(q=2\). The two duplications are ordered operations but their resulting words are counted without multiplicity. The source is nonempty. The run letters \(a_j\) are adjacent-distinct, although nonadjacent run letters may coincide. The distribution generating function includes the empty source solely as the constant term 1.

## Proof
**Canonical history list.** Number the original positions \(1,\ldots,n\). Every two-duplication history has an output of one of three forms: \(F_{ij}\), duplication at two *distinct* original positions \(1\le i<j\le n\); \(P_i\), duplicating the same original position twice, replacing \(a\) locally by \(a\bar a\bar a\); and \(Q_i\), duplicating the newly inserted complement, replacing \(a\) locally by \(a\bar a a\). Operations at distinct original sites commute, and the two repeated-site histories are the only alternatives. Thus there are \(\binom n2+2n=n(n+3)/2\) canonical outputs before collision identification.

**One-step injectivity.** Distinct sites in a nonempty word give distinct one-step outputs. Indeed, for two sites \(i<j\), equality forces the symbols between them to alternate under complementation; at the last comparison, the output inserting at \(i\) contains the original symbol at \(j\), while the output inserting at \(j\) contains its distinct complement. This contradicts the fixed-point-free hypothesis.

**Appending a letter.** Let \(x=ua\), with \(|u|=n-1\ge1\). The canonical outputs that do not duplicate the final original symbol are precisely \(D_2(u)a\) and have last symbol \(a\). Among the remaining outputs, \(F_{i,n}\) for \(1\le i<n\) are exactly the one-step outputs of \(u\), followed by \(a\bar a\); they are distinct by one-step injectivity. The additional repeated-site output \(P_n=ua\bar a\bar a\) is distinct from these, because its penultimate letter is \(\bar a\) rather than \(a\). All these \(n\) outputs end in \(\bar a\). Finally \(Q_n=ua\bar a a\) ends in \(a\), and it is a new output precisely when \(ua\bar a\notin D_2(u)\). Hence
\[
|D_2(ua)|=|D_2(u)|+n+\epsilon(u,a),
\]
where \(\epsilon\in\{0,1\}\) is the indicator of nonmembership.

**Suffix membership lemma.** For every nonempty \(u\),
\[
ua\bar a\in D_2(u)\quad\Longleftrightarrow\quad u\text{ has suffix }\bar a a^r\text{ for some }r\ge0.
\]
If \(r=0\), duplicate the final \(\bar a\), giving an appended \(a\), then duplicate the appended \(a\). If \(r>0\), duplicate the \(\bar a\) immediately before the terminal \(a\)-run, thereby adding one indistinguishable \(a\) to that run, and then duplicate the final \(a\). Conversely, if \(u\) ends outside \(\{a,\bar a\}\), neither insertion can make its final original symbol precede an ending \(a\bar a\) without changing that original suffix. If \(u\) ends in \(a\), the last \(\bar a\) must be the second inserted symbol after a terminal \(a\); the first insertion must add an \(a\) to that terminal run, which is possible only after a preceding \(\bar a\). If \(u\) ends in \(\bar a\), the lemma already applies with \(r=0\). These cases exhaust all canonical histories.

**Recurrence and induction.** Appending \(a\) increases \(C\) by exactly one when the preceding word has suffix \(\bar a a^r\): this starts a complementary-following run or extends one by a letter. Otherwise \(C\) is unchanged. Hence \(\epsilon(u,a)=1-C(ua)+C(u)\). Substitute in the recurrence and use the base case \(|D_2(a)|=2\) to prove the claimed formula for every \(n\).

**Distribution and endpoints.** Every first run of length \(r\) contributes \(z^r\), so its series is \(R(z)=z/(1-z)\). Each later run has either one complementary choice, with penalty exponent equal to its length and weight \(R(zu)\), or \(q-2\) other distinct choices, each with weight \(R(z)\). Summing the geometric series of later runs gives
\[
1+\frac{qR(z)}{1-R(zu)-(q-2)R(z)}
=1+\frac{qz(1-zu)}{1-(q-1)z-2zu+qz^2u}.
\]
The penalty lies between zero and \(n-1\), and every intermediate value is attained by a two-run word with first run length \(n-c\) and a complementary second run of length \(c\). The penalty is zero exactly when no adjacent pair is complementary, giving \(q(q-1)^{n-1}\) choices. Its value \(n-1\) requires the first run to have length one and every later run to follow its predecessor by complementation: the initial letter has \(q\) choices, and for each subsequent position either the previous letter is repeated or its complement starts a new run, with the second position forced complementary. This gives \(q2^{n-2}\) for \(n\ge2\). To compute the mean, the \(j\)th noninitial position contributes to \(C\) precisely when the run beginning at or before it is complementary to its predecessor; summing its probability (or differentiating the displayed rational function at \(u=1\)) gives the stated expectation.

## Verification
The standalone `verify_direct.py` enumerates exact two-step output sets for all binary words of lengths at most 10, quaternary words of lengths at most 7, and six-letter alphabet words of lengths at most 5, comparing each to its run penalty. The independent `verify_transfer.py` compares an exact integer run-transfer dynamic program with direct run-statistic enumeration, including extremal multiplicities, for alphabet sizes two, four and six. Both use the complement operation \(a\mapsto a\mathbin{\mathrm{xor}}1\). These finite checks confirm the implementation; the induction and generating-function derivation establish the unlimited-parameter result.

## Relationship to prior work
Zabokritskiy's 2026 analysis of reverse-complement and palindromic duplications treats two-error descendant bounds and code constructions. A separately published exact odd-block-length upper bound, including duplication length one, proves the maximum \(n(n+3)/2\). The present formula explains all deviations below that maximum for every source and fixed-point-free alphabet and gives the full probability law. Sun and Ge's 2026 study addresses correction of reverse-complement duplications, including single-symbol errors, rather than this complete two-step output-volume statistic. The exact maximum is therefore acknowledged as prior work, not claimed as new.

## Limitations
The result does not cover complement maps with fixed points, duplication blocks longer than one, or three or more sequential duplications. The source distribution is uniform only for the expectation statement; the wordwise formula is deterministic. An equivalent formula in unindexed coding-theory literature cannot be excluded without an independent bibliographic audit.

## References
1. D. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779, first posted 2026-09-01, https://arxiv.org/abs/2609.00779.
2. Sun and Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151, first posted 2026-02-01, https://arxiv.org/abs/2602.01151.
3. *Sharp two-step sphere maximum for odd-length reverse-complement duplication*, published research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-step-sphere-maximum-for-odd-length-reverse-complement--a03a87770ec6.
