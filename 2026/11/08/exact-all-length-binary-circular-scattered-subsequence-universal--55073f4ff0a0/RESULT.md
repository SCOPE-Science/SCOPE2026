# Exact all-length binary circular scattered-subsequence universality distribution

## Finding
Fix the alphabet \(\{0,1\}\). For a finite nonempty binary word \(w\) of length \(n\), define \(\iota(w)\) to be the largest \(k\ge0\) for which every binary word of length \(k\) is a scattered subsequence of \(w\). Put
\[\zeta(w)=\max_{0\le j<n}\iota(w[j:]w[:j]).\]
This counts the **best single rotation**; it does not splice several rotations to realize different subsequences. Define \(N_{n,k}=|\{w\in\{0,1\}^n:\zeta(w)=k\}|\). For all \(n\ge1\),
\[
N_{n,0}=2,\qquad
N_{n,k}=\frac{n}{n-k}\binom{n-k}{k}2^k-2\mathbf1_{\{n=2k\}}\quad(1\le k\le\lfloor n/2\rfloor),
\]
and \(N_{n,k}=0\) for larger \(k\). Equivalently, the length-\(n\) index enumerator is
\[
1+\lambda_+^n+\lambda_-^n-2\mathbf1_{\{2\mid n\}}u^{n/2},\qquad
\lambda_\pm=(1\pm\sqrt{1+8u})/2.
\]
The expression with the square root is a polynomial because the sum of the two conjugate powers is a polynomial.

## Assumptions and scope
Length \(n\) is any positive integer and words are **labelled and rooted**: rotations are included as distinct words where distinct, rather than counted as necklaces. The index is measured by subsequences, not contiguous factors. The case \(k=0\), which consists precisely of the two constant words, and the even-length maximal-index correction are part of the claim. The binomial formula uses only \(1\le k\le\lfloor n/2\rfloor\), so its denominator is positive. No assertion is made for larger alphabets.

## Proof
**Step 1: From binary universality to matchings.** A finite binary word has subsequence-universality index at least \(k\) exactly when it can be split into \(k\) successive nonempty segments, each containing both alphabet symbols (with an optional leftover suffix). Indeed, the greedy left-to-right arch factorization, cutting each arch at its first occurrence of the previously missing letter, produces precisely the maximum possible number of complete-alphabet arches; such a factorization realizes all subsequences of that length by choosing one letter per arch, while its incomplete tail prevents a longer universal index. This standard greedy-arch equivalence is recalled in the cited scattered-factor-universality literature. Every binary segment containing both symbols contains two adjacent unequal letters; choosing one such adjacent pair per segment gives \(k\) vertex-disjoint unequal-adjacency edges. Conversely, \(k\) disjoint unequal-adjacency edges in increasing order give \(k\) successive complete-alphabet segments. Hence the linear index equals the maximum matching cardinality in the path of adjacent unequal letters.

**Step 2: Circular reduction.** Place the \(n\) positions on a cycle and retain edge \(i\leftrightarrow i+1\pmod n\) precisely when their bits differ. For \(n=2\), interpret the two oppositely oriented boundary adjacencies as parallel cycle edges, with matching cardinality still one. Every rotation's path matching is a matching of this cycle. Conversely every matching of the cycle omits some cycle edge, and cutting at an omitted edge realizes it as a path matching of a rotation. Therefore \(\zeta(w)\) equals the maximum matching size \(\nu(E)\) of the circular transition-edge set \(E\).

**Step 3: Parity constraint.** Traversing the circle flips the bit once per marked transition. Thus \(E\subseteq\{0,\ldots,n-1\}\) is realizable by a binary word if and only if \(|E|\) is even, and each realizable \(E\) has exactly two labelled realizations (choice of initial bit). If \(E\) is a nonempty proper subset, its maximal cyclic runs of consecutive marked edges, of lengths \(\ell_1,\ldots,\ell_s\), are disjoint paths. Therefore \(\nu(E)=\sum_{i=1}^s\lceil\ell_i/2\rceil\). An empty edge set gives index zero. If all \(n\) edges are present, \(n\) must be even and \(\nu(E)=n/2\).

**Step 4: Closed transfer-matrix trace.** Read the marked/unmarked edge positions cyclically. A zero edge resets a run. For a one edge, a matching contribution occurs at the first, third, fifth, etc. position in its run. Use states \(0\) (reset), \(1\) (odd positive run length), \(2\) (even positive run length). Weight each marked edge by \(v\) and each matching contribution by \(u\). The weighted transition matrix, with rows as source states, is
\[
T(v)=\begin{pmatrix}1&vu&0\\1&0&v\\1&vu&0\end{pmatrix}.
\]
For each **proper** transition subset, there is a unique cyclic compatible state assignment, and its trace weight is \(v^{|E|}u^{\nu(E)}\). The all-marked subset when \(n\) is even has two alternating compatible state assignments, each of weight \(v^n u^{n/2}\), rather than one. (For odd \(n\), there is no closed all-marked assignment.) Thus the even-cardinality filter on transition subsets, multiplied by the two binary-bit assignments, gives
\[
\sum_{k\ge0}N_{n,k}u^k=\operatorname{tr}(T(1)^n)+\operatorname{tr}(T(-1)^n)-2\mathbf1_{\{2\mid n\}}u^{n/2}.
\]
The characteristic polynomial of \(T(v)\) is \(x\bigl(x^2-x-(v+v^2)u\bigr)\). For \(v=-1\), its eigenvalues are \(1,0,0\), so \(\operatorname{tr}(T(-1)^n)=1\) for \(n\ge1\). For \(v=1\), its nonzero eigenvalues are \(\lambda_\pm=(1\pm\sqrt{1+8u})/2\). This proves the polynomial identity in the Finding.

**Step 5: Extract coefficients.** Write \(s_n(u)=\lambda_+^n+\lambda_-^n\), with recurrence \(s_n=s_{n-1}+2u s_{n-2}\), \(s_0=2\), \(s_1=1\). Induction in this recurrence, or the standard cycle-matching coefficient identity, gives for \(1\le k\le\lfloor n/2\rfloor\)
\[
[u^k]s_n(u)=\frac{n}{n-k}\binom{n-k}{k}2^k.
\]
One proof of the coefficient identity is to count size-\(k\) matchings of the \(n\)-cycle: if a fixed distinguished vertex is uncovered there are \(\binom{n-k-1}{k}\) matchings; if covered there are \(2\binom{n-k-1}{k-1}\), and their sum simplifies to \(\frac{n}{n-k}\binom{n-k}{k}\). Each selected edge has the two weights that make \(2^k\). The constant coefficient is \(s_n(0)=1\) for every \(n\ge1\), hence \(1+s_n(0)=2\). Subtracting the all-marked overcount yields the claimed complete distribution. \(\square\)

## Verification
Run `python3 verify.py` using only the Python standard library. The checker enumerates every binary word of lengths \(1\) through \(12\), independently computes scattered-subsequence universality for every rotation by testing every length-\(k\) subsequence pattern, and compares the result to dynamic-programming maximum matching on the cycle and to the closed formula. It further checks nonnegativity, total count \(2^n\), and the even maximal-index correction at all lengths \(1\) through \(500\). The observed final line is `VERIFY_OK exhaustive_words=8190 length_range=1..12 symbolic_lengths=1..500`. These finite checks corroborate but do not replace the preceding proof.

## Relationship to prior work
The circular scattered-factor-universality notion and greedy arch decomposition already appear in Barker and collaborators' 2020 study. Adamson's 2023 ranking/unranking paper counts general linear subsequence-universal words, and the 2023 regular-language study gives algorithms for counting linear regular-language universality. Those sources do not state this explicit **all-length binary circular-index distribution**. The length-\(2k\), index-\(k\) special case reduces to the previously established \(2^{k+1}-2\) count of minimum-length circular-universal binary words; that boundary case is not claimed as new. General algorithms or an unlocated equivalent census may nevertheless cover the formula.

## Limitations
This is an exact binary, finite-word theorem, not a higher-alphabet or infinite-word statement. All claims are for rooted words, not necklaces. The proof uses known binary arch/matching facts as ingredients. Finite experiments do not prove the all-length result; that follows from the transfer-matrix argument. Literature searches cannot exclude every unindexed equivalent result. No independent scientific audit has been performed.

## References
1. Barker et al., *Scattered Factor-Universality of Words*, first arXiv version 2020-03-10, https://arxiv.org/abs/2003.04629.
2. Adamson, *Ranking and Unranking k-subsequence universal words*, first arXiv version 2023-04-10, https://arxiv.org/abs/2304.04583.
3. Adamson et al., *k-Universality of Regular Languages*, first arXiv version 2023-11-17, https://arxiv.org/abs/2311.10658.
