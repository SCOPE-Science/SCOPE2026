# The two-largest-run law for palindromic subsequences of distinct-run powers

## Finding
Let \(q\ge 2\), let \(c_1,\ldots,c_q\) be pairwise distinct letters, and let \(a_1,\ldots,a_q\) be positive integers. Set \(U=c_1^{a_1}\cdots c_q^{a_q}\) and \(W=U^k\), where \(k\ge1\). Write \(A\ge B\) for the two largest values in the run-length multiset, with multiplicities: if the largest value occurs at least twice, then \(A=B\).

The longest palindromic scattered-subsequence length of \(W\) is exactly
\[
\operatorname{LPS}(W)=kA+(k-1)B.
\]
In particular, its minimum number of letter deletions needed to obtain a palindrome is
\[
k\bigl(\sum_{i=1}^q a_i-A-B\bigr)+B.
\]
Thus the optimum depends only on the two largest run lengths, not on the cyclic order of runs or any smaller lengths.

When \(A>B\) (a unique longest run), let \(t=\#\{i:a_i=B\}\). The **complete** set of distinct optimal palindrome words consists of words
\[
c_*^A d_1^B c_*^A d_2^B\cdots d_{k-1}^B c_*^A,
\]
where \(c_*\) is the unique letter of run length \(A\), each \(d_j\) is one of the \(t\) letters of run length \(B\), and \(d_j=d_{k-j}\) for \(1\le j<k\). Consequently the number of distinct optimal palindrome words is exactly
\[
t^{\lfloor k/2\rfloor}.
\]
For \(k=1\), the empty choice of the \(d_j\) produces the sole optimal word \(c_*^A\). No optimizer-count claim is made when \(A=B\).

## Assumptions and scope
A scattered subsequence is obtained by deleting positions without changing the order of the remaining letters; its length counts letters, not run blocks. All letters \(c_i\) must be distinct, every \(a_i\) must be positive, and the period is repeated an integer number \(k\ge1\) of times. The palindromic-subsequence problem is different from palindromic contiguous-factor enumeration. Every stated equality is exact over these parameters.

## Proof
**1. Weighted block-expansion lemma.** For any words \(x,y\) on a common alphabet, assign a positive integer weight \(w(c)\) to every letter \(c\), and let \(\Phi_w(x)\) replace each occurrence of \(c\) by \(w(c)\) copies of \(c\). Then
\[
\operatorname{LCS}(\Phi_w(x),\Phi_w(y))
=\max_{v\preceq x,\ v\preceq y}\sum_{c\text{ occurring in }v}w(c),
\]
where the sum is over *occurrences* of letters in \(v\).

The right side is a lower bound, since every matched base letter can be replaced by its entire monochromatic block. Conversely, take an order-preserving positional matching of a common subsequence of the expanded words. For each pair of base positions \((i,j)\) bearing the same letter \(c\), let \(x_{ij}\) be the number of expanded matched pairs between their two blocks divided by \(w(c)\). Every row sum and column sum is at most one. Moreover, positive cells cannot cross: \(i<i'\) and \(j>j'\) cannot both carry positive mass, because this would reverse the order of matched positions. By integrality of the bipartite matching polytope, the nonnegative doubly substochastic matrix \((x_{ij})\) is a convex combination of zero-one matchings supported on its positive cells. Every such matching is an increasing common subsequence of \(x,y\), by the noncrossing property. Its weighted size is at most the right side; averaging gives the desired upper bound. This also proves the equality assertion: if the expanded alignment attains the maximum, every matching with positive coefficient in such a decomposition must be a maximum-weight base matching.

**2. The reversed permutation skeleton.** Let \(P=c_1\cdots c_q\), and let \(\widetilde P=c_q\cdots c_1\). A nonempty word \(v=v_1\cdots v_m\) embeds in \(P^k\) exactly when it has at most \(k-1\) adjacent *weak descents* in the total order \(c_1<\cdots<c_q\). This follows by greedily embedding successive letters: an equal or lower next letter requires moving to the next copy; a higher next letter stays in the current copy. Similarly \(v\) embeds in \(\widetilde P^k\) exactly when it has at most \(k-1\) adjacent weak ascents in this order. If \(e(v)\) counts equal adjacent pairs, their two descent statistics sum to \(m-1+e(v)\). Therefore every common subsequence satisfies
\[
m+e(v)\le2k-1.
\]
In particular \(m\le2k-1\), and every letter occurs at most \(k\) times in a common subsequence.

Assign weight \(a_i\) to \(c_i\). If \(A>B\), let \(h\le k\) be the number of occurrences of the unique maximum-weight letter in a common subsequence of length \(m\). Its weight is at most
\[
hA+(m-h)B\le kA+(k-1)B.
\]
When \(A=B\), the bound is simply \((2k-1)A\), the same formula. Choosing any two letters with run weights \(A,B\), the alternating word containing \(k\) occurrences of the first and \(k-1\) of the second is a palindrome; its \(2k-1\) adjacent-letter run sequence has exactly \(k-1\) weak descents in \(P\)-order, so it embeds in \(P^k\) and its reversed order. Expanding the selected letters to their entire blocks yields a palindrome embedded in \(U^k\) with length \(kA+(k-1)B\). The palindrome is an instance of the explicit alternating construction in the Finding.

**3. Upper bound and equality.** Every palindromic subsequence of \(W=\Phi_a(P^k)\) is also a common subsequence of \(W\) and \(W^R=\Phi_a(\widetilde P^k)\). The expansion lemma and Step 2 bound its length by \(kA+(k-1)B\). The alternating palindrome of Step 2 attains the bound. Subtracting from \(|W|=k\sum_i a_i\) proves the deletion formula.

**4. Complete optimal-word count when \(A>B\).** Equality in Step 2 for any maximum-weight base common subsequence forces simultaneously \(m=2k-1\), \(h=k\), \(e(v)=0\), and every other letter to have weight \(B\). Therefore the matched skeleton must alternate between the unique maximum-weight letter \(c_*\), present in *every one* of the \(k\) copies, and a single weight-\(B\) letter in each of the \(k-1\) gaps separating consecutive \(c_*\) occurrences. There are no selected letters before the first or after the last \(c_*\).

Now take **any** longest palindromic subsequence of the expanded word and align it with its reversed copy. The equality assertion in the expansion lemma expresses the normalized block-matching matrix as a convex combination of these optimal skeleton matchings. All \(k\) blocks of \(c_*\) have row sum one and hence are selected completely. Each intervening gap has a total selected normalized weight of exactly one, and all its selected letters have run weight \(B\), hence contributes exactly \(B\) letters. Let the selected gap word be \(T_j\). Each gap in the original word traverses all other distinct-letter blocks in one fixed cyclic order. Because the entire selected word is palindromic, \(T_j=T_{k-j}^R\). Both members are subsequences of the *same* fixed distinct-run block word. A nonempty word and its reverse can both be subsequences of such a block word only if each consists of repetitions of one letter (otherwise a pair of distinct letters would have to appear in both orders). This also applies to a self-mirrored central gap. It follows that \(T_j=d_j^B\), for some run-weight-\(B\) letter \(d_j\). Conversely, choosing these letters in mirror-paired gaps produces an embedded palindrome of optimal length, because every gap contains every nonmaximum letter in its fixed order. The \(k-1\) gaps form \(\lfloor k/2\rfloor\) reversal orbits, each allowing independently one of \(t\) letters. This proves the claimed characterization and count.

## Verification
The included standalone `verify.py` computes longest palindromic subsequence lengths by interval dynamic programming and compares them with the formula for \(5{,}440\) profiles (alphabet sizes \(2\) through \(5\), run lengths \(1\) through \(4\), repetition counts \(1\) through \(4\)). It checks an explicit optimal palindrome embedding in each case. It separately enumerates all optimal palindrome strings in \(107\) small cases, checking the unique-longest-run multiplicity formula. An additional exact-enumeration check on a distinct case selection of \(169\) profiles also matched. These are finite checks, not substitutes for the proof for all parameters.

Run `python3 verify.py` with Python 3; it uses only the standard library and prints a PASS line when complete.

## Relationship to prior work
Brodal, Fagerberg and Rysgaard (2024) establish the relationship between longest palindromic subsequences and longest common subsequences against the reversed string, including caveats on which backtracking procedures return an actual palindrome. Bringmann and Chaudhury (2018) study weighted longest common subsequences and run-based compression. Neither primary text's examined theorem statements provide this two-largest-run formula, its invariance under arbitrary other run weights, or the exact all-optimizer count in the unique-longest-run case. The previous permutation-power palindrome spectrum for unit run lengths already gives the special case \(A=B=1\); that case is not claimed independently.

## Limitations
The distinct-letter assumption is essential to the greedy skeleton and to the gap-order rigidity argument; no extension to repeated letters within one base period is claimed. The number of maximizers for tied *largest* run lengths \(A=B\) is not classified. Bibliographic searches cannot exclude every unindexed equivalent result; no independent audit or external validation has been performed.

## References
1. K. Bringmann and B. R. Chaudhury, *Sketching, Streaming, and Fine-Grained Complexity of (Weighted) LCS*, arXiv:1810.01238 (first public 2018-10-02), FSTTCS 2018, DOI: 10.4230/LIPIcs.FSTTCS.2018.40. https://arxiv.org/abs/1810.01238
2. G. S. Brodal, R. Fagerberg and C. M. Rysgaard, *On Finding Longest Palindromic Subsequences Using Longest Common Subsequences*, ESA 2024, DOI: 10.4230/LIPIcs.ESA.2024.35. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.35
