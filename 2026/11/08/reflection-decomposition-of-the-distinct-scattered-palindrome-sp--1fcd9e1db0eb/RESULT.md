# Reflection decomposition of the distinct scattered-palindrome spectrum of any finite palindrome

## Finding
Let \(A\) be any finite word over an arbitrary finite alphabet \(\Sigma\), and let \(c\in\Sigma\). Define \(\operatorname{Sub}(A)\) as its set of **distinct** scattered subsequence strings, including the empty word \(\varepsilon\). Let \(\operatorname{SPal}(H)\) denote the nonempty palindromic strings occurring as scattered subsequences of a host \(H\). For a word \(V\), write \(V^{\mathrm R}\) for its reversal. Then the following are exact, disjoint language decompositions (all unions are disjoint):

\[
\begin{aligned}
\operatorname{SPal}(AA^{\mathrm R})
&=\{VV^{\mathrm R}:V\in\operatorname{Sub}(A)\setminus\{\varepsilon\}\}
\;\dot\cup\;
\{V^{\prime}d(V^{\prime})^{\mathrm R}:V^{\prime}d\in\operatorname{Sub}(A)\},\\
\operatorname{SPal}(AcA^{\mathrm R})
&=\{VV^{\mathrm R}:V\in\operatorname{Sub}(A)\setminus\{\varepsilon\}\}
\;\dot\cup\;
\{VcV^{\mathrm R}:V\in\operatorname{Sub}(A)\}
\;\dot\cup\;
\{V^{\prime}d(V^{\prime})^{\mathrm R}:V^{\prime}d\in\operatorname{Sub}(A),\ d\ne c\}.
\end{aligned}
\]

In the expressions \(V^{\prime}d\), the letter \(d\) is the final letter of a nonempty subsequence, and \(V^{\prime}\) may be empty. Define polynomials
\[
S_A(z)=\sum_{V\in\operatorname{Sub}(A)\setminus\{\varepsilon\}}z^{|V|},\qquad
E_{A,c}(z)=\sum_{\substack{V\in\operatorname{Sub}(A)\setminus\{\varepsilon\}\\\mathrm{last}(V)=c}}z^{|V|}.
\]
For \(F_H(t)=\sum_{U\in\operatorname{SPal}(H)}t^{|U|}\), the complete graded identities are
\[
\boxed{F_{AA^{\mathrm R}}(t)=S_A(t^2)+t^{-1}S_A(t^2)}
\]
and
\[
\boxed{F_{AcA^{\mathrm R}}(t)=S_A(t^2)+t\bigl(1+S_A(t^2)\bigr)
+t^{-1}\bigl(S_A(t^2)-E_{A,c}(t^2)\bigr).}
\]
Both are polynomials despite the apparent inverse power. In particular,
\[
\bigl|\operatorname{SPal}(AA^{\mathrm R})\bigr|=2S_A(1),\qquad
\bigl|\operatorname{SPal}(AcA^{\mathrm R})\bigr|=3S_A(1)+1-E_{A,c}(1).
\]

## Assumptions and scope
Words are finite; the alphabet is finite but has no imposed cardinality or symbol-frequency restriction; the half-word may be empty. All subsequences are scattered (order-preserving deletions), and equal resulting strings are counted **once**, independently of their number of embeddings. In the first identity the host length is even; in the second the host has the displayed central letter. The empty palindrome is excluded. The formula counts the entire length distribution, not only the maximum subsequence length or total number.

For coefficient use, put \(d_m=[z^m]S_A(z)\), \(e_{m,c}=[z^m]E_{A,c}(z)\), \(d_0=1\), and set out-of-range coefficients to zero. For \(m\ge1\), both length-\(2m-1\) and length-\(2m\) counts in \(AA^{\mathrm R}\) equal \(d_m\). In \(AcA^{\mathrm R}\), the length-\(2m\) count equals \(d_m\), and for \(m\ge0\) the length-\(2m+1\) count equals \(d_m+d_{m+1}-e_{m+1,c}\).

## Proof
**Symmetric embedding normalization.** Let a palindrome \(U\) of length \(2m\) or \(2m+1\) be embedded in a palindromic host \(H\) of length \(N\), at increasing positions \(p_1<\cdots<p_{|U|}\). For \(1\le i\le m\), put \(q_i=N+1-p_{|U|+1-i}\). As \(H\) and \(U\) are palindromes, \(p_i\) and \(q_i\) carry the same symbol \(U_i\). Both sequences \((p_i)\) and \((q_i)\) are strictly increasing. Their termwise minima \(r_i=\min(p_i,q_i)\) are therefore strictly increasing. Also \(p_i<p_{|U|+1-i}\), so \(p_i+q_i<N+1\); at least one of these two integer positions is at most \(\lfloor N/2\rfloor\). Thus \(r_1<\cdots<r_m\) lies in the left half and spells the left half \(V\) of \(U\). In particular **every** palindromic scattered subsequence of \(H\) has left half \(V\) in \(\operatorname{Sub}(A)\).

**Even host.** A nonempty even palindrome \(VV^{\mathrm R}\) lies in \(AA^{\mathrm R}\) exactly when \(V\) lies in \(A\), since a chosen embedding in \(A\) and its reflection in \(A^{\mathrm R}\) concatenate to an embedding. For an odd palindrome \(VdV^{\mathrm R}\), reflect an embedding in \(H\) if necessary to place its central letter in the left half \(A\) (the even-length host has no central letter). The normalized positions \(r_i\) above satisfy \(r_i\le p_i<p_{m+1}\), so they and the chosen central position witness \(Vd\in\operatorname{Sub}(A)\). Conversely, any occurrence of \(Vd\) in \(A\) can be completed with the reflected occurrence of \(V^{\mathrm R}\). This proves the first disjoint decomposition.

**Odd host.** Even palindromes are treated identically. For odd \(VdV^{\mathrm R}\) with \(d=c\), the left-half normalization gives \(V\in\operatorname{Sub}(A)\); choosing the actual central \(c\) then supplies the palindrome. When \(d\ne c\), the selected middle symbol cannot occupy the global center. By reflecting the embedding if necessary it lies in the left half, and the previous argument gives \(Vd\in\operatorname{Sub}(A)\). The converse again uses the reflected right half. The three sets are disjoint because of even/odd parity and the odd palindrome's central letter; each parametrization is injective because the left half and central letter are recoverable from the output. This establishes the second decomposition.

**Enumeration and recurrence.** Substituting \(t^{2|V|}\), \(t^{2|V|-1}\), or \(t^{2|V|+1}\) for the respective disjoint parametrizations yields the two displayed polynomial identities and their coefficients. Independently, the necessary input polynomials can be computed without enumerating subsequences. Maintain \(E_{A,d}(z)\), initially zero for each letter. After appending letter \(a\) to a prefix, replace only
\[
E_{\mathrm{new},a}(z)=z\left(1+\sum_{d\in\Sigma}E_{\mathrm{old},d}(z)\right),
\]
leaving all other ending-letter polynomials unchanged. This is exact: every nonempty subsequence ending \(a\) is precisely a distinct prior subsequence (possibly empty) followed by \(a\), and every subsequence ending a different letter is unchanged. The recurrence reconstructs \(S_A=\sum_d E_{A,d}\) and the designated \(E_{A,c}\).

## Verification
The standalone Python program `verify.py` computes complete *sets* of subsequence strings for the mirror hosts and for both claimed decompositions; it compares sets, graded length coefficients and total counts. Exhaustive half-words over alphabets of sizes \(2\), \(3\), and \(4\) were checked through lengths \(7\), \(6\), and \(5\), respectively: 2,713 half-words and 11,962 host instances. The program returned `VERIFY_OK`. These finite checks corroborate, but are not the proof of, the universally quantified statements; the preceding normalization argument supplies the proof.

## Relationship to prior work
Mahalingam and Pandoh, *Counting Scattered Palindromes in a Finite Word* (arXiv:2108.02729v1, 2021), define the same distinct-string statistic, give general bounds and establish a binomial spectrum for the special mirrored word in which each first-half letter is distinct (Proposition 5.1). That special case is subsumed here, but their general bounds and example do not specify the all-half-word language identities, the correction for repeated letters, or the odd central-letter spectrum. Holub and Saari, *On Highly Palindromic Words*, establish binary reconstruction up to reversal from the set of scattered palindromes; their conclusion does not supply a graded count for every symmetric host. Hasan and coauthors, *On Palindromic Sequence Automata and Applications* (2013), develop an automaton representation for arbitrary hosts and longest-common-palindrome applications; the mirror decomposition is a separate structural specialization. General distinct-palindromic-subsequence dynamic programming also counts arbitrary hosts without the stated reflection law.

## Limitations
The identities require a genuinely symmetric host, not an arbitrary source. They count distinct output strings, not index sets of embeddings or contiguous palindromic factors. The fully general mirror theorem was not located in the inspected sources, but unpublished or unindexed equivalent formulations remain possible. The derivation is an ordinary mathematical proof and finite computational cross-check, not an independent external audit.

## References
1. K. Mahalingam and P. Pandoh, *Counting Scattered Palindromes in a Finite Word*, arXiv:2108.02729v1 (first public 2021-08-05), https://arxiv.org/abs/2108.02729.
2. Š. Holub and K. Saari, *On Highly Palindromic Words* (2009), https://www.karlin.mff.cuni.cz/~holub/soubory/subpal.pdf.
3. M. M. Hasan, A. S. M. S. Islam, M. S. Rahman, and A. Sen, *On Palindromic Sequence Automata and Applications*, CIAA 2013, pp. 158–168, DOI:10.1007/978-3-642-39274-0_15.
