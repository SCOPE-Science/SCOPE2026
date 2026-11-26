# Exact reset thresholds for cyclic automata with a single jump merge

## Finding
For integers \(n\ge2\) and \(1\le h<n\), let the state set be \(Q=\mathbb Z/n\mathbb Z\). There are two letters:
\[a(i)=i+1\pmod n,\qquad b(0)=h,\quad b(i)=i\ \text{for }i\ne0.\]
A word is a **reset word** if its image of the full state set has cardinality one. Write \(R(n,h)\) for the shortest reset-word length, with \(R(n,h)=\infty\) when no reset word exists. The complete result is
\[
R(n,h)=\begin{cases}
1+(n-2)(n-h+1),&\gcd(n,h)=1,\\
\infty,&\gcd(n,h)>1.
\end{cases}
\]
For coprime parameters an optimal word is \(W_{n,h}=b(a^{n-h}b)^{n-2}\). Its length is the displayed finite value. In particular, the classical longest case \(h=1\) has \(R(n,1)=(n-1)^2\); the opposite adjacent merge \(h=n-1\) has the linear value \(R(n,n-1)=2n-3\).

## Assumptions and scope
All words use exactly the two unit-cost letters \(a,b\); powers of a letter are repetitions, not extra generator letters. All states are read under the forward action of words from left to right. The parameter \(h\) is represented by its standard integer in \(\{1,\ldots,n-1\}\); reversing the direction of the generator \(a\) is not a length-preserving alphabet substitution. No extra inverse-permutation letter is allowed. The assertion holds for all integers in the specified range, including \(n=2\).

## Proof
**Failure of synchronization when not coprime.** Put \(g=\gcd(n,h)\). The letter \(b\) leaves every residue modulo \(g\) unchanged (it sends \(0\) to a multiple of \(g\)); the letter \(a\) adds one modulo \(g\). Thus each input word acts by one common translation on residue classes modulo \(g\). If \(g>1\), two states in distinct residue classes can never be merged. Consequently no reset word exists.

**Inverse intervals.** Assume \(\gcd(n,h)=1\). Equip \(Q\) with the circular order
\[0,h,2h,\ldots,(n-1)h\pmod n.\]
An interval means a nonempty set of \(k\) consecutive points in this cyclic order, where \(1\le k\le n\). For \(k<n\) there is a unique **left endpoint**: the first point encountered in the forward \(+h\) direction. For an interval \(T\), its inverse image under \(a\) is \(a^{-1}(T)=T-1\); this is an interval of the same size, whose left endpoint is reduced by one modulo \(n\). The inverse image under \(b\) is
\[b^{-1}(T)=(T\setminus\{0\})\cup\bigl(\{0\}\text{ if }h\in T;\ \varnothing\text{ otherwise}\bigr).\]
Since \(0\) is immediately before \(h\) in this circular order, this operation on an interval either leaves it unchanged, removes its right endpoint \(0\), or adds \(0\) immediately before its left endpoint \(h\). In the removal case the left endpoint is unchanged whenever the inverse image is nonempty. In the addition case the size increases exactly one, the previous left endpoint must be \(h\), and the new left endpoint is \(0\). In particular, every nonempty inverse image of an interval is again an interval.

**Lower bound.** Take any reset word \(w\), mapping all of \(Q\) to some state \(q\). Read its letters in reverse, starting from the singleton \(\{q\}\), taking inverse images successively. Every inverse-image set is nonempty (it contains the antecedents of \(q\) under the corresponding suffix) and is an interval by the preceding paragraph. The interval starts with size one and ends with size \(n\). Only an inverse \(b\)-step can increase its size, and then by exactly one. Therefore at least \(n-1\) such growing steps occur. Immediately after any growing step the left endpoint is \(0\), while immediately before the next growing step the left endpoint must be \(h\). Non-growing inverse \(b\)-steps do not move the left endpoint; each inverse \(a\)-step subtracts one from its label. Hence between consecutive growing steps there must be at least \(n-h\) inverse \(a\)-steps: this is the smallest positive integer \(m\) for which \(-m\equiv h\pmod n\). There are at least \(n-2\) such gaps. Counting these mandatory letters gives
\[|w|\ge(n-1)+(n-2)(n-h)=1+(n-2)(n-h+1).\]
Extra non-growing or shrinking steps cannot decrease this bound.

**Matching construction.** The candidate \(W_{n,h}=b(a^{n-h}b)^{n-2}\) has precisely the length of the lower bound. To show it resets, start from the target singleton \(\{h\}\) and apply the inverse letters of \(W_{n,h}\) in reverse order. First \(b^{-1}\) gives \(\{0,h\}\). Whenever the current inverse set is \(\{0,h,\ldots,kh\}\) (a cyclic interval with \(k+1<n\) points), \((a^{n-h})^{-1}\) shifts it to \(\{h,2h,\ldots,(k+1)h\}\) because \(-(n-h)\equiv h\pmod n\), and the next \(b^{-1}\) adds \(0\). After \(n-1\) growing steps its inverse image is the whole \(Q\). Therefore every state is mapped to \(h\) by \(W_{n,h}\). Combining this construction and the lower bound proves the exact formula. For \(n=2\) the word consists just of \(b\) and the same argument holds.

## Verification
The standalone script `verify.py` computes the shortest possible reset length by a breadth-first search of the **forward subset automaton**, independently of the inverse-interval proof. It checks every parameter \(2\le n\le12\), \(1\le h<n\), including all nonsynchronizing cases, for a total of 66 automata. It also checks interval preservation for 3,448 cyclic-interval instances and directly replays the proposed reset words for all coprime parameters with \(2\le n\le100\). The observed output is:

`VERIFY_OK exhaustive_BFS_n=2..12 cases=66 inverse_intervals=3448 constructive_witness_n=2..100`

Run with a standard Python 3 interpreter: `python3 verify.py`. The finite checks corroborate, rather than replace, the universal proof above.

## Relationship to prior work
The parameter \(h=1\) is a labeling of the classical Černý family, whose quadratic reset threshold is established. Don's Proposition 15 (2016) treats circular automata with a rank-deficient letter and coprime excluded-to-contracting distance, proving synchronization and the bound \((n-1)^2\), not the present exact distance-dependent reset threshold. Volkov's 2024 paper (first public as a 2023 preprint) supplies broad synchronizability conditions but no shortest-word formula for these generators. Rystsov's 2025 Černý-type analysis, Theorems 4.4–4.5, gives a general synchronization criterion and a reset-word construction: on specializing its cyclic generator to the present \(a\), that construction yields the **upper-bound witness** \(W_{n,h}\). The witness and gcd criterion are accordingly not claimed as new. The contribution here is the matching all-words lower bound, which upgrades the earlier general bound and construction to the exact formula for every coprime \(n,h\).

## Limitations
The formula concerns only the **directed** generator \(a(i)=i+1\), with no separate inverse letter. Enlarging the alphabet, allowing variable letter costs, or changing the action of \(b\) can change the minimum. No exact reset thresholds are claimed for broader families of circular automata. The result has undergone the stated mathematical and computational checks but has not received independent validation. Earlier literature using different automaton conventions may contain an equivalent formula; that remains a bibliographic risk, particularly in older work on simple idempotents.

## References
1. H. Don, *The Černý Conjecture and 1-Contracting Automata*, Electronic Journal of Combinatorics 23(3), P3.12 (2016), DOI 10.37236/5616, especially Proposition 15.
2. M. V. Volkov, *Synchronization of Primitive Automata*, RAIRO – Theoretical Informatics and Applications 58 (2024), article 3, DOI 10.1051/ita/2024003; preprint arXiv:2306.13317 first posted 2023-06-23; primary MSC 68Q45.
3. I. Rystsov, *Cerny type automata and rank conjecture*, arXiv:2501.19166 (2025), especially Theorems 4.4–4.5.
4. I. K. Rystsov, *Estimation of the Length of Reset Words for Automata with Simple Idempotents*, Cybernetics and Systems Analysis 36 (2000), 339–344, DOI 10.1007/BF02732984.
5. I. K. Rystsov, *Cerny's Conjecture for Automata with Simple Idempotents*, Cybernetics and Systems Analysis 58 (2022), DOI 10.1007/s10559-022-00428-3.
