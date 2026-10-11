# Binary palindromic periodicities have order n times 2 to the n over 2
## Finding
Let \(a_n\) denote the number of binary length-\(n\) palindromic periodicities. Then
\[
a_n=\Theta\!\left(n2^{n/2}\right).
\]
In particular,
\[
\lim_{n\to\infty} a_n^{1/n}=\sqrt{2}.
\]
This settles the order of growth and the exponential growth constant. It does not determine a leading constant, possible parity-dependent constants, or lower-order terms.

## Assumptions and scope
A nonempty finite binary word \(x\) is called a palindromic periodicity when it has a symmetric word-period \(z\) of length at most \(|x|\); a word is symmetric when it is a conjugate of its reversal, equivalently a product of two palindromes. This is the characterization used in Fici--Shallit--Simpson. For a length-\(m\) word, write positions in \(\mathbb Z/m\mathbb Z\).

## Proof
For \(h\in\mathbb Z/m\mathbb Z\), let \(R_h(i)=h-i\). A binary word \(z\) of length \(m\) is symmetric exactly when it is fixed by at least one reflection \(R_h\): the equality \(z_i=z_{h-i}\) says that the reversal of \(z\) is a cyclic shift of \(z\).

The involution \(R_h\) has one fixed position when \(m\) is odd; when \(m\) is even it has either zero or two fixed positions. Hence its number of cycles is at most \(m/2+1\), and the number \(S_m\) of symmetric binary words of length \(m\) satisfies
\[
S_m\le m2^{m/2+1}.
\]
Every length-\(n\) palindromic periodicity has some symmetric word-period of a length \(m\le n\), and a chosen period word determines at most one length-\(n\) prefix of its infinite repetition. Therefore
\[
a_n\le\sum_{m=1}^n S_m
 \le 2\sum_{m=1}^n m2^{m/2}
 \le \frac{2}{1-2^{-1/2}}\,n2^{n/2},
\]
so \(a_n=O(n2^{n/2})\).

For the matching lower bound, it is enough to count primitive symmetric words of length \(n\), since every symmetric word is itself a palindromic periodicity. For a fixed reflection \(R_h\), any imprimitive fixed word has a proper period \(d\mid n\) and descends to a length-\(d\) word fixed by the induced reflection. Thus the number of imprimitive words fixed by \(R_h\) is at most
\[
\sum_{d\mid n,\,d<n}2^{d/2+1}=O\!\left(n2^{n/4}\right).
\]
If \(n\) is odd, every one of the \(n\) reflections fixes exactly \(2^{(n+1)/2}\) words. If \(n\) is even, \(n/2\) of the reflections have two fixed positions and each fixes exactly \(2^{n/2+1}\) words. Finally, a primitive word cannot be fixed by two distinct reflections, because the composition of two distinct reflections is a nontrivial rotation, which would give the word a proper period. Hence the primitive fixed-word sets for distinct reflections are disjoint. It follows in both parity cases that
\[
S_n=\Omega\!\left(n2^{n/2}\right),
\]
and therefore \(a_n\ge S_n=\Omega(n2^{n/2})\). Combining the two bounds proves the claim. Taking \(n\)-th roots gives the stated limit.

## Verification
The proof is independent of finite computation. The accompanying standard-library verifier checks the reflection characterization and directly enumerates all binary words through length \(14\), reproducing the published A374495 values
\[
2,4,8,16,32,58,108,190,336,560,948,1574,2568,4116.
\]
It also recomputes the numbers of symmetric words over the same range and checks the direct inequality that every symmetric word is a palindromic periodicity.

## Relationship to prior work
Fici, Shallit, and Simpson introduced the counting question explicitly: they ask asymptotically how many binary palindromic periodicities of length \(n\) there are, list the initial terms (OEIS A374495), and record the immediate lower bound \(\Omega(2^{n/2})\) coming from palindromes. Their structural characterization that a palindromic periodicity is exactly a word with a symmetric word-period is the starting point here.

The enumeration of symmetric words (products of two palindromes) is classical; Kemp studied that language in 1982. The proof above does not require Kemp's formula: it obtains both the needed upper count and a matching primitive-word lower count directly from reflection orbits. The new point asserted here is the transfer from symmetric period words to the full palindromic-periodicity language, yielding the previously unstated \(\Theta(n2^{n/2})\) order for A374495.

## Limitations
This result is only a coarse asymptotic in the multiplicative-constant sense. It does not prove that \(a_n/(n2^{n/2})\) converges, does not identify parity-dependent leading constants, and does not provide an exact recurrence or generating function for A374495. Literature search cannot certify absence of all unpublished or unindexed statements; the closest classical source already enumerates symmetric words, so an unnoticed prior observation combining that enumeration with the 2024 symmetric-period characterization remains a residual originality risk.

## References
1. G. Fici, J. Shallit, and J. Simpson, *Some Remarks on Palindromic Periodicities*, arXiv:2407.10564, first posted 2024-07-15; later published as *On Palindromic Periodicities*, LIPIcs CPM 2025, Article 11.
2. J. Simpson, *Palindromic Periodicities*, arXiv:2402.05381, first posted 2024-02-08.
3. R. Kemp, *On the number of words in the language of products of two palindromes*, Discrete Mathematics 40 (1982), 225--234, DOI 10.1016/0012-365X(82)90123-6.
4. OEIS A374495, number of binary palindromic periodicities of length \(n\).
5. OEIS A007055, number of binary words of length \(n\) that are products of two palindromes; references Kemp's enumeration.
