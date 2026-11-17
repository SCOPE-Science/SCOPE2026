# Maximal common subsequences of opposite permutation powers are all longest

## Finding
Fix integers \(q\ge2\) and \(k\ge1\), and let \(P=c_0c_1\cdots c_{q-1}\) be any permutation of \(q\) different letters. Put \(X=P^k\) and \(Y=(c_{q-1}\cdots c_0)^k\), both *finite linear words*. A common scattered subsequence is **maximal** when no strict supersequence of it is a common scattered subsequence. Distinct subsequence *words*, not their embeddings, are counted.

Every maximal common subsequence of \(X,Y\) has length \(2k-1\), and thus every maximal one is longest. More precisely, after identifying \(c_i\) with \(i\), their complete set is
\[
\mathcal M_{q,k}=\{w\in\{0,\ldots,q-1\}^{2k-1}:\ w_j\ne w_{j+1}\text{ for all }j,\ \operatorname{asc}(w)=\operatorname{des}(w)=k-1\}.
\]
Here \(\operatorname{asc}(w)\) and \(\operatorname{des}(w)\) are the numbers of strict adjacent rises and falls. In particular the entire common-subsequence language is the downward subsequence closure of \(\mathcal M_{q,k}\): **no shorter maximal common subsequence exists**.

Let \(N_q(k)=|\mathcal M_{q,k}|\). Writing \([z^nt^d]\) for coefficient extraction, the exact cardinality is
\[
N_q(k)=[z^{2k-1}t^{k-1}]\frac{(1+z)^q-(1+tz)^q}{(1+tz)^q-t(1+z)^q}.
\]
The rational expression is interpreted as a formal series in \(z\), after cancellation of the common factor \(1-t\). Exactly \(q(q-1)^{k-1}\) of the maximal common-subsequence words are palindromes. For example, the counts \(N_3(k)\) for \(k=1,\ldots,8\) are \(3,10,36,132,490,1836,6930,26312\), and \(N_2(k)=2\) for every \(k\ge1\).

## Assumptions and scope
The alphabet letters are pairwise distinct, but no numerical order is required on the original alphabet; the order used for rises and falls is their order of appearance in \(P\). Both inputs have the **same positive exponent** \(k\), and their blocks have exactly opposite letter orders. The word \(w\) is embedded as a scattered subsequence: positions increase strictly but need not be consecutive. The empty word is common and never maximal because every letter appears in both inputs. All assertions cover the boundaries \(q=2\) and \(k=1\).

## Proof
**1. Greedy-cycle lemma.** For a nonempty word \(w=w_1\cdots w_m\) over \(\{0,\ldots,q-1\}\), let \(e(w)\) count adjacent equalities. Greedily match the first letter in the first copy of \(P=0\cdots(q-1)\); any next letter with a larger index stays in the same copy, whereas a smaller or equal index forces exactly one move to the next copy. The number of copies needed is therefore \(1+\operatorname{des}(w)+e(w)\). For \(Y\), whose order is reversed, it is \(1+\operatorname{asc}(w)+e(w)\). Thus
\[
w\preccurlyeq X,Y\quad\Longleftrightarrow\quad
\operatorname{asc}(w)+e(w)\le k-1\ \text{and}\ \operatorname{des}(w)+e(w)\le k-1.
\]
The greedy rule is optimal because taking the earliest available match can only leave more subsequent positions.

**2. A common word is either extendible or balanced.** If a nonempty common \(w\) contains an adjacent equal pair \(xx\), insert any other alphabet letter \(y\ne x\) between this pair. The edge \(xx\), which contributes one to both weak-descent budgets, is replaced by \(xy,yx\), which together also contribute one to each. The new, longer word remains common. Hence any maximal common word is a **Smirnov word**, meaning that no two adjacent letters agree.

For a Smirnov word write \(a=\operatorname{asc}(w)\) and \(d=\operatorname{des}(w)\). Both are at most \(k-1\). If both are strictly smaller than \(k-1\), append any letter different from the last one: just one of the two budgets increases by one, so the word remains common.

Suppose instead \(d=k-1\) and \(a<k-1\). We show an insertion increasing exactly \(a\) by one and leaving \(d\) fixed. If no such insertion existed, the first letter would have to be \(0\) (otherwise prepend \(0\)), and the last would have to be \(q-1\) (otherwise append \(q-1\)). Every rise would have to go between consecutive numbers (otherwise insert an intermediate number), and every fall would have to go directly from \(q-1\) to \(0\): on a fall \(x>y\), inserting \(q-1\) when \(x<q-1\), or inserting \(0\) when \(y>0\), would otherwise add exactly one rise without changing the number of falls. Telescoping the successive differences in \(w\) would give
\[
q-1= a-(q-1)d,\qquad a=(q-1)(d+1)\ge k,
\]
contrary to \(a<k-1\). Therefore the desired insertion exists. The symmetric argument, with the order reversed, applies if \(a=k-1\) and \(d<k-1\). Hence a common Smirnov word is maximal only when \(a=d=k-1\).

**3. Length and completeness.** For a Smirnov word, the number of edges is \(m-1=a+d\). Hence saturation forces \(m=2k-1\), so every maximal word has that length. Such words exist for every \(q\ge2\): alternate the first two letters, starting with either one, for \(2k-1\) positions. Conversely any word of length \(2k-1\) with balanced \(a=d=k-1\) and no repeats satisfies both greedy-cycle bounds. No longer common word exists, because every adjacent pair contributes at least one to the sum of the two weak-descent counts, yielding \(m-1\le2(k-1)\). Thus precisely these words are simultaneously maximal and longest. Repeated extension of any common word terminates in this set, giving the downward-closure statement.

**4. Enumeration.** Let
\[
F_q(z,t)=\sum_{m\ge1}\sum_{\substack{w\in\{0,\ldots,q-1\}^m\\w_j\ne w_{j+1}}}z^m t^{\operatorname{des}(w)}.
\]
For \(j=0,\ldots,q-1\), let \(f_j\) be the analogous generating series restricted to words ending in \(j\), and let \(T=\sum_jf_j\). Appending \(j\) gives
\[
f_j=z\left(1+\sum_{i<j}f_i+t\sum_{i>j}f_i\right).
\]
Writing \(S_j=\sum_{i\le j}f_i\), one obtains
\[
(1+zt)S_j=(1+z)S_{j-1}+z(1+tT),\quad S_{-1}=0,\quad S_{q-1}=T.
\]
Summing the geometric progression and solving for \(T\) gives
\[
F_q(z,t)=T=\frac{(1+z)^q-(1+tz)^q}{(1+tz)^q-t(1+z)^q}.
\]
In a length \(2k-1\) Smirnov word every edge is a rise or fall, so requiring \(k-1\) falls forces \(k-1\) rises; extracting the stated coefficient counts \(\mathcal M_{q,k}\). This rational function also follows by specializing the known Smirnov-word descent enumerator of Ellzey--Wachs; the novelty claimed here is **the exact MCS-language identification**, not the independent invention of the Smirnov enumerator.

Finally a palindrome of odd length \(2k-1\) has its \(k-1\) first-half comparisons mirrored with the opposite direction. It has balanced rises and falls exactly when adjacent letters differ. Choosing its first letter in \(q\) ways and each successive first-half letter in \(q-1\) ways proves the palindromic count.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It independently constructs the literal sets of subsequences of \(P^k\) and \((P^{\mathrm{rev}})^k\), identifies maximal words by directly trying every one-letter insertion, compares the claimed ascent/descent classification, cross-checks the number and palindromic subcount, and verifies the rational generating function by checking polynomial coefficients. On the packaged file it reports `VERIFY_OK configurations=17 common_words=8323 maximal_words=3228 polynomial_cells=816`. The exhaustive configurations have \(2\le q\le6\), \(1\le k\le4\) and \(qk\le16\); polynomial coefficients are checked to length \(16\) for alphabets of sizes \(2,\ldots,7\). These checks are finite corroboration, not substitutes for the proof.

## Relationship to prior work
Hirota--Sakai (arXiv:2307.10552) and Conte--Grossi--Punzi--Uno (arXiv:2307.13695) give general polynomial preprocessing and representation/enumeration procedures for arbitrary maximal common subsequences. The present classification concerns the special but infinite parameter family consisting of a permutation power paired with its *opposite-order* power; those general algorithms do not imply a fixed formula asserting that all maximal solutions are longest. Ellzey--Wachs (arXiv:1901.01591, especially their equation (1.7)) establishes the general descent enumerator of Smirnov words; its finite-alphabet specialization supplies the enumerative component, while the nontrivial new contribution is the word-language equivalence and maximality rigidity. Bukh--Cox (arXiv:1912.03510) investigates longest common subsequences involving periodic words and independent random words, not this deterministic reverse-order pairing. The ternary result for \((012)^r\) against \((021)^s\) concerns a different relative ordering (a single reversal of the last pair) and does not imply the present arbitrary-alphabet full reversal statement. A previously determined longest-palindromic-subsequence length and palindromic-subsequence spectrum for permutation powers also give the LCS length (via the standard reverse-word reduction) and some palindromic counts, but not the classification of **every** maximal common subsequence or its nonpalindromic Smirnov spectrum.

## Limitations
The theorem requires opposite block orders and equal exponents; it asserts nothing for arbitrary pairs of permutations or unequal exponents. An exact coefficient expression is supplied, not a simpler elementary closed formula for every \(q,k\). The rational Smirnov descent series is already known, and is not claimed as independently new. No independent external audit has been performed; an unindexed equivalent formulation of the full MCS rigidity theorem may exist.

## References
- M. Hirota and Y. Sakai, *Efficient algorithms for enumerating maximal common subsequences of two strings*, arXiv:2307.10552 (first public 2023-07-20), https://arxiv.org/abs/2307.10552.
- A. Conte, R. Grossi, G. Punzi and T. Uno, *A Compact DAG for Storing and Searching Maximal Common Subsequences*, arXiv:2307.13695 (first public 2023-07-25); ISAAC 2023, https://arxiv.org/abs/2307.13695.
- B. Ellzey and M. L. Wachs, *On enumerators of Smirnov words by descents and cyclic descents*, arXiv:1901.01591 (first public 2019-01-06), https://arxiv.org/abs/1901.01591.
- B. Bukh and C. Cox, *Periodic words, common subsequences and frogs*, arXiv:1912.03510 (first public 2019-12-07), https://arxiv.org/abs/1912.03510.
