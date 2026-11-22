# Double-occurrence subsequence languages are classified by palindromic triples

## Finding

Let \(\Sigma\) be a labeled alphabet of cardinality \(q\ge3\). Fix a target word \(p=p_1\cdots p_m\in\Sigma^m\), where \(m\ge2\) and \(p_i\ne p_{i+1}\) for \(1\le i<m\). For a host word \(w\), let \(c_p(w)\) be the number of **indexed scattered** occurrences: increasing index tuples whose selected letters spell \(p\). Put

\[
t(p)=\#\{i:2\le i\le m-1,\ p_{i-1}=p_{i+1}\},\qquad
B_{q,p}(n)=\#\{w\in\Sigma^n:c_p(w)=2\}.\]

**Theorem (exact two-occurrence enumerator and equivalence classes).** For all such \(q,m,p\), including all \(n\ge0\),

\[
\boxed{\sum_{n\ge0}B_{q,p}(n)z^n
=\frac{z^{m+1}}{[1-(q-1)z]^2[1-(q-2)z]^{m-1}}
\left(\frac{2+t(p)}{1-(q-2)z}+\frac{m-2-t(p)}{1-(q-3)z}\right).}
\]

Two adjacency-distinct patterns of equal length over the same labeled alphabet have identical two-occurrence enumerators **if and only if** they have the same value of \(t(p)\). Each \(t\in\{0,\ldots,m-2\}\) occurs, giving exactly \(m-1\) different sequences. The number of labeled target patterns in the class \(t\) is

\[q(q-1)\binom{m-2}{t}(q-2)^{m-2-t}.\]

The first coefficient that distinguishes the classes is at length \(m+2\):

\[B_{q,p}(m+1)=m,\qquad
\boxed{B_{q,p}(m+2)=m^2(q-2)+m(2q-3)+t(p)+2.}\]

For each fixed \(q,m,p\),

\[
B_{q,p}(n)=\frac{m+2+t(p)}{2(q-1)}n(q-1)^n+O_{q,m}((q-1)^n).
\]

Thus the leading coefficient varies between \((m+2)/[2(q-1)]\) and \(m/(q-1)\). These bounds are sharp: a cyclic three-letter target realizes the first, and an alternating two-letter target realizes the second.

## Assumptions and scope

The alphabet is finite, labeled, and not endowed with an order. Both the target and host are ordinary words; an occurrence is an **index choice**, not a distinct resulting subsequence word and not a contiguous factor. Adjacent letters of the target are unequal, but nonadjacent letters may coincide; in particular palindromic length-three factors are permitted. No assertion is made for targets with equal adjacent letters or for occurrence counts other than exactly two. The formal generating functions have integer coefficients and are equal as formal power series.

## Proof

**1. Rigidity of two embeddings.** For any two embeddings \(a=(a_1,\ldots,a_m)\) and \(b=(b_1,\ldots,b_m)\), the coordinatewise minimum and maximum are themselves strictly increasing valid embeddings. Strict increase holds because both input tuples increase strictly; the selected letters at coordinate \(i\) both equal \(p_i\). If exactly two embeddings exist and they were incomparable coordinatewise, their minimum and maximum would supply other embeddings, contradiction. Thus the two embeddings \(a,b\) can be ordered so \(a_i\le b_i\) for every \(i\). If they differ in two coordinates \(j<k\), the tuple formed from \((a_1,\ldots,a_j)\) followed by \((b_{j+1},\ldots,b_m)\) is strictly increasing, spells \(p\), and is distinct from both. Consequently there is a **unique** coordinate \(j\) at which the two embeddings differ. Denote the two selected positions there by \(u<v\). This is the *fork coordinate*.

**2. Gap classification.** The union of the two embeddings has exactly \(m+1\) selected positions, spelling \(p_1\cdots p_{j-1}p_jp_jp_{j+1}\cdots p_m\). These delimit \(m+2\) possibly empty gaps. The two exterior gaps may use any letter except \(p_1\) and \(p_m\) respectively; each has \(q-1\) allowed letters. In every ordinary interior gap, between selected consecutive target letters \(p_i,p_{i+1}\), a copy of either endpoint letter would create another embedding by moving that selected position. Since the target is adjacency-distinct, each of the \(m-1\) ordinary gaps has \(q-2\) allowed letters.

The remaining gap lies between the two selected copies of \(p_j\). An inserted \(p_j\) would give a third fork choice; an inserted \(p_{j-1}\), if it exists, would move the preceding coordinate of the later embedding; an inserted \(p_{j+1}\), if it exists, would move the following coordinate of the earlier embedding. Thus this *fork gap* must avoid \(p_j\) and its existing neighbors. At \(j=1,m\) there are two distinct forbidden letters; at an interior \(j\) there are two if \(p_{j-1}=p_{j+1}\), and three otherwise. Write \(s_j=q-2\) in the former cases and \(s_j=q-3\) in the latter cases.

All these exclusions are also **sufficient**. The leftmost greedy embedding reads the first copy of \(p_j\) and all other designated positions; this follows by induction from the absence of the next needed letter in each preceding ordinary gap, as well as the fork-gap exclusions. The rightmost greedy embedding reads the second copy and the same other positions by the reversed argument. Every embedding is coordinatewise between these greedy extrema. Since the extrema agree outside coordinate \(j\), every embedding must use those same \(m-1\) positions; inside the fork interval the only copies of \(p_j\) are the two selected ones. Hence there are exactly two embeddings. The two extremal embeddings and the fork coordinate are intrinsic to the host, so there is no overcounting between fork classes or between gap fillings.

**3. Rational enumeration.** A gap admitting \(a\) independent letter choices per position contributes \(1/(1-az)\). There are \(m+1\) selected positions, two boundary gaps, \(m-1\) ordinary internal gaps, and one fork gap. Thus for fixed fork \(j\),

\[
F_j(z)=\frac{z^{m+1}}{[1-(q-1)z]^2[1-(q-2)z]^{m-1}(1-s_jz)}.
\]

Exactly \(2+t(p)\) forks have \(s_j=q-2\) (the endpoints and the interior length-three palindromes); the remaining \(m-2-t(p)\) have \(s_j=q-3\). Summing \(F_j\) proves the displayed rational generating function for all lengths, including the zero cases \(n\le m\).

**4. Complete equivalence and asymptotics.** Extracting the coefficients of \(z^{m+1}\) and \(z^{m+2}\) gives the stated two initial values. Since the second depends on \(p\) through \(t(p)\) with coefficient exactly one, different values of \(t\) cannot produce identical entire enumerators. Conversely, the rational formula depends on \(p\) only through \(t\), proving the equivalence assertion.

Choose \(p_1\) in \(q\) ways and \(p_2\ne p_1\) in \(q-1\) ways. At each later position, choosing the letter from two steps earlier creates a palindromic triple (one option); choosing a letter distinct from both predecessors avoids it (\(q-2\) options). Exactly \(t\) of the \(m-2\) choices must be of the first type. The class-size formula follows and is positive for every \(0\le t\le m-2\).

Finally the dominant pole \(z=(q-1)^{-1}\) is a double pole; the remaining poles have strictly smaller exponential bases \(q-2\) and \(q-3\). Evaluating the regular factor at this dominant pole gives coefficient \((m+2+t)/[2(q-1)]\) for the principal \([1-(q-1)z]^{-2}\) term. Standard coefficient extraction proves the asymptotic with the indicated error. The cyclic pattern over three symbols has \(t=0\), while alternating two distinct symbols give \(t=m-2\), proving sharpness.

## Verification

The included standard-library Python program `verify_two_scattered.py` independently counts occurrences with a capped subsequence dynamic program, reconstructs the two position tuples by separate explicit backtracking, and checks the unique-fork coordinate. In parallel it computes each fork's predicted coefficient by multiplying ordinary geometric-series coefficients. The exact coefficients, each fork histogram, and the length-\(m+2\) formula are checked against exhaustive enumeration. The recorded output `verification_output.txt` reports 534 parameter-pattern-length instances covering 1,472,158 host words over binary, ternary and four-symbol alphabets, including 147,576 two-occurrence host words with independently reconstructed embeddings. Binary checks are supplemental; the theorem itself assumes \(q\ge3\).

Examples for ternary targets of length three: target `012` gives \(B(5)=20\), while target `010` gives \(B(5)=21\). This difference is the palindromic-triple statistic, not a difference in length, alphabet or adjacent-repeat structure.

## Relationship to prior work

Bruda [1], first available publicly on 2026-06-30, proves a general eventual-polynomial theorem for **binary** subsequence frequencies and gives a general-alphabet result for **one** occurrence (Proposition 4.1 and Appendix A.2). Section 4.1 formulates the general-alphabet, arbitrary-positive-frequency shape; it does not provide the present all-length, fork-refined two-occurrence formula or the palindromic-triple classification. Menon and Singh [2], Section 3.1, prove an exact **binary** formula for two copies (Proposition 3.4); in the binary adjacency-distinct case every internal triple is palindromic, so it cannot distinguish the nonbinary classes. The known exact ternary `012` result is recovered as the case \(q=m=3,t=0\); its covered coefficients are not claimed as new. Mansour, Rastegar and Roitershtein [3] count order-isomorphic patterns, a different pattern-occurrence convention; their general asymptotic limit does not assert the exact literal-subsequence enumerator above.

The mathematical distinction is not an expansion of a known single concrete sequence: the new formula identifies exactly how two embeddings branch over **every adjacency-distinct target** and detects interior length-three palindromes, a local statistic invisible to the one-occurrence count.

## Limitations

The theorem is restricted to adjacency-distinct patterns and precisely two indexed embeddings. Its asymptotic is for fixed alphabet and target length as host length grows, and does not claim uniform estimates if those parameters grow. No independent audit or independent external validation has been performed. Priority remains conditional on accessible literature: a currently inaccessible or unindexed publication could contain an equivalent all-alphabet formula; in particular, an announced general proof of a related subsequence-frequency shape was not available for full comparison. The finite verification is not a substitute for the proof above.

## References

1. G. Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578, version first posted 2026-06-30. https://arxiv.org/abs/2607.02578 . Full accessible manuscript, particularly Sections 1 and 4.1 and Appendix A.2.
2. K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870, 2023; *Discrete Mathematics* 347 (2024), 113928. https://arxiv.org/html/2306.07870v1 . Especially Section 3.1, Proposition 3.4.
3. T. Mansour, R. Rastegar and A. Roitershtein, *Finite automata, probabilistic method, and occurrence enumeration of a pattern in words and permutations*, arXiv:1905.05646, 2019. https://arxiv.org/abs/1905.05646 . Introduction and pattern-definition comparison.
