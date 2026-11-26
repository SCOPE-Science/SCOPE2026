# Exact length-refined minimal absent subsequences of the binary alternating word

## Finding

For every integer \(m\ge1\), let \(W_m=(01)^m\). A word \(u\in\{0,1\}^*\) is a **minimal absent subsequence** (MAS) of \(W_m\) if it is not a scattered subsequence of \(W_m\) but every proper scattered subsequence of \(u\) is. Let \(M_{m,k}\) count the different MAS words of length \(k\). Then

\[
F(x,y)=\sum_{m\ge1}\sum_{k\ge1}M_{m,k}x^m y^k
=\frac{xy^2\bigl(3+(y^2-2y)x+2y^3x^2\bigr)}{1-2xy+x^2y^2-x^3y^4}.
\]

In particular, writing \(P_m(y)=\sum_{k\ge1}M_{m,k}y^k\),
\[
P_1(y)=3y^2,\qquad P_2(y)=4y^3+y^4,\qquad P_3(y)=5y^4+4y^5,
\]
with the all-length recurrence
\[
P_m(y)=2yP_{m-1}(y)-y^2P_{m-2}(y)+y^4P_{m-3}(y)\quad(m\ge4).
\]

The total-count series is
\[
\sum_{m\ge1}|\operatorname{MAS}(W_m)|x^m
=\frac{x(3-x+2x^2)}{1-2x+x^2-x^3}
=3x+5x^2+9x^3+16x^4+28x^5+49x^6+\cdots.
\]
For the unique positive root \(\alpha\approx1.754877666\) of \(\alpha^3-2\alpha^2+\alpha-1=0\), the count is \(\Theta(\alpha^m)\). By contrast, \(W_m\) has exactly \(m+2\) **shortest** absent subsequences. Thus exponential-versus-linear separation already occurs for the smallest nontrivial alphabet.

## Assumptions and scope

The source alphabet and target alphabet are both exactly \(\{0,1\}\), the source is the linear word \(W_m\) beginning with \(0\) and ending with \(1\), and positions of a subsequence are required to increase strictly. The indices satisfy \(m\ge1\) and \(k\ge1\). Distinct target words, not their embeddings, are counted. The empty target is always present. A proper subsequence may delete any nonempty collection of target positions; because subsequence presence is downward closed, checking the \(|u|\) single-letter deletions suffices for minimality.

Define for nonempty \(u=u_1\cdots u_k\)
\[
E(u)=k+\mathbf1_{\{u_1=1\}}+\sum_{i=2}^k\mathbf1_{\{u_i=u_{i-1}\}}.
\]
For \(k\ge2\), the following exact structural criterion is part of the finding: \(u\) is an MAS of \(W_m\) if and only if (i) it does not start with \(01\), (ii) it avoids contiguous \(010\) and \(101\), and (iii) either \(E(u)=2m+1\), or \(E(u)=2m+2\) and \(u_k=u_{k-1}\). There are no length-one MAS for \(m\ge1\).

## Proof

**Embedding-cost identity.** In the infinite alternating sequence \(010101\cdots\), the first \(0\) can be embedded at position one and the first \(1\) at position two. Greedily embedding each further letter costs one additional position when it differs from its predecessor and two positions when it agrees. Greedy embeddings are earliest possible by induction, so the last required position is exactly \(E(u)\). Consequently,
\[
u\preccurlyeq W_m\quad\Longleftrightarrow\quad E(u)\le2m.
\]
Here \(\preccurlyeq\) denotes scattered-subsequence occurrence.

**Deletion criterion.** For a word of length at least two, deleting its first letter decreases \(E\) by zero precisely when its first two letters are \(01\); otherwise the decrease is two. Deleting an internal letter decreases \(E\) by zero precisely when the three consecutive letters centered there are \(010\) or \(101\); otherwise the decrease is two. Deleting the last letter decreases \(E\) by one if the final letters differ and by two if they agree. These are exact identities obtained by writing the two affected adjacency indicators. Hence if \(E(u)>2m\) and every single-letter deletion has cost at most \(2m\), the zero-drop patterns must be absent. The last-letter drop is at most two, so \(E(u)\) is either \(2m+1\) or \(2m+2\), with equal final letters required in the latter case. Conversely these conditions make every deletion fit inside \(W_m\), proving the structural classification.

**Weighted run grammar.** Write \(u\) as maximal constant runs. If a run has length \(\ell\), its contribution to the weight \(t^{E(u)}y^{|u|}\), before the extra first-letter factor, is \(t^{2\ell-1}y^\ell\). Introduce
\[
A(t,y)=\frac{ty}{1-t^2y},\qquad B(t,y)=\frac{t^3y^2}{1-t^2y},
\]
representing runs of length at least one and at least two. The structural restrictions say that every internal run has length at least two, a multi-run word starting with \(0\) has first run of length at least two, while a word starting with \(1\) has no such restriction on its first run. A single-run candidate must have length at least two. The extra factor \(t\) records a first letter \(1\).

Let \(S(t,y)\) count all candidate words with these local restrictions, weighted by \(t^{E(u)}y^{|u|}\), and let \(T(t,y)\) count those whose last two letters agree. Single-run words contribute \((1+t)B\) to both series. Multi-run words have a first-run factor \(B+tA\), any number of internal runs of type \(B\), and a last-run factor \(A\) for \(S\) or \(B\) for \(T\). Thus
\[
S=(1+t)B+\frac{(B+tA)A}{1-B},\qquad
T=(1+t)B+\frac{(B+tA)B}{1-B}.
\]

The deletion criterion implies the exact coefficient formula
\[
P_m(y)=[t^{2m+1}]S(t,y)+[t^{2m+2}]T(t,y).
\]
Extracting the odd powers of \(S+t^{-1}T\), substituting \(x=t^2\), and simplifying the rational functions gives precisely the displayed formula for \(F(x,y)\). Cross-multiplication yields the stated initial polynomials and recurrence for every \(m\ge4\); this formal-power-series calculation requires no convergence assumptions.

**Shortest absent subsequences and growth.** Any binary word of length \(m\) can be embedded by selecting its \(i\)-th letter from the \(i\)-th \(01\) block of \(W_m\), while \(0^{m+1}\) is absent. Hence shortest absent subsequences have length \(m+1\). For words \(u\) of this length, writing \(r\) for the number of runs and \(s=\mathbf1_{\{u_1=1\}}\), the identity \(E(u)=2(m+1)-r+s\) shows that absence is equivalent to \(r-s\le1\). These words are exactly \(1^j0^{m+1-j}\) for \(0\le j\le m+1\), giving \(m+2\) words. Finally, the denominator of \(F(x,1)\) has one simple positive zero of minimal modulus, at \(x=\alpha^{-1}\), where \(\alpha\approx1.754877666\) solves \(\alpha^3-2\alpha^2+\alpha-1=0\). The other two reciprocal roots are a complex-conjugate pair of modulus below one, proving \(|\operatorname{MAS}(W_m)|=\Theta(\alpha^m)\).

## Verification

The accompanying `verify_binary_mas.py` independently checks each candidate of lengths one through \(2m+1\) against the literal subsequence definition for every \(m=1,\ldots,9\), a total of 1,398,078 target words. Its direct results match the local deletion criterion and the generating-function polynomials. A separate stars-and-bars count over run lengths agrees with the generating-function recurrence for \(m=1,\ldots,160\). The first ten total counts are \(3,5,9,16,28,49,86,151,265,465\). Run `python3 verify_binary_mas.py`; Python standard library is sufficient. These are finite independent checks, not substitutes for the all-length proof above.

## Relationship to prior work

Kosche, Koß, Manea, and Siemer introduced systematic characterizations and algorithms for minimal and shortest absent subsequences. Their Theorem 3.1 is a general structural test; Proposition 3.6 studies polynomially many shortest versus exponentially many minimal absent subsequences for an even alphabet size at least four. The exact binary length-refined formula, local classification, and growth constant above are not stated there. Their general result about decreasing shortest absent subsequences of repeated increasing-alphabet blocks is consistent with the \(m+2\) shortest count here, which is not separately claimed as novel.

Manea, Ringleb, Siemer, and Winkler give improved general-purpose enumeration algorithms; this is a different type of result and does not state the family-specific bivariate census. Troníček's 2023 work describes a general counting algorithm, but its full text was not accessible during the comparison, leaving a literature risk.

The univariate sequence \(3,5,9,16,28,\ldots\) already occurs in OEIS A005314 (at shifted indices), for example as a composition-counting sequence and a binary substring-avoidance sequence. Numerical coincidence is acknowledged, and no novelty is claimed for that integer sequence in isolation. The specific minimal-absent-subsequence interpretation, structural theorem, and joint generating function are the contributions compared here. A separate previously studied invariant of alternating words counts scattered palindromes, not minimal absent subsequences.

## Limitations

The proof applies only to the exact binary linear family \((01)^m\); it does not classify minimal absent subsequences of arbitrary binary words or periodic sources with longer periods. The constant and total sequence are not asserted to be new as stand-alone numbers. Published general enumeration algorithms may evaluate this special case without supplying an explicit formula, and equivalent but unlocated specialized enumerations remain a residual novelty risk. The result has received no independent mathematical audit.

## References

1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first posted 2021-08-31); *Fundamenta Informaticae* 189 (2023), 199–240. DOI: 10.3233/FI-222159. In particular Theorem 3.1, Proposition 3.6, Theorem 4.21.
2. F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (2025), Sections 1–3.
3. Z. Troníček, *On Problems Related to Absent Subsequences*, COCOA 2023, LNCS 14462, 351–363, DOI: 10.1007/978-3-031-49614-1_26 (abstract inspected; full text unavailable).
4. OEIS Foundation, A005314, integer sequence with initial entries \(0,1,2,3,5,9,16,28,49,\ldots\), entry and combinatorial comments.
