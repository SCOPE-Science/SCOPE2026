# Three shortest absent subsequences in a rich-word morphic family

## Finding

For a finite word \(w\) on alphabet \(\Sigma\), let \(\operatorname{SAS}_{\Sigma}(w)\) denote the set of shortest words over \(\Sigma\) that are **not** scattered subsequences of \(w\). Subsequence occurrences are order-preserving and need not be contiguous.

**Stable three-word theorem.** Let \(L\) be any nonempty finite alphabet, let \(a,b\) be two new, distinct letters, and let \(U\in L^*\) contain every letter of \(L\). Put \(\Sigma=L\cup\{a,b\}\) and \(R=UaUb\). For every integer \(m\ge2\) and every \(Z\in (L\cup\{b\})^*\), set
\[
H_m=(RRb)^m Z.
\]
Then \(H_m\) has scattered-subsequence universality index exactly \(2m\), and its **complete** shortest-absent language is
\[
\operatorname{SAS}_{\Sigma}(H_m)
=\{a^{2m+1},\;ba^{2m},\;b^2a^{2m-1}\}.
\]
In particular there are precisely three shortest absent subsequences, independent of the size of \(L\), the internal order and multiplicity of letters in \(U\), the number of blocks, and the choice of \(a\)-free tail \(Z\).

**Sharp morphic transition.** For \(d\ge3\), let \(\Sigma_d=\{0,\ldots,d-1\}\) and let \(\varphi_d(i)=0(i+1)\) for \(0\le i\le d-2\) and \(\varphi_d(d-1)=0(d-1)(d-1)\). Set \(W_k=\varphi_d^k(0)\), \(a=d-2\), and \(b=d-1\). The complete shortest-absent languages at the first three iterates using all \(d\) letters are
\[
\begin{aligned}
\operatorname{SAS}_{\Sigma_d}(W_{d-1})
  &=\{aa\}\cup\{bc:c\in\Sigma_d\},\\
\operatorname{SAS}_{\Sigma_d}(W_d)
  &=\{aaa,baa\}\cup\{bbc:c\in\Sigma_d\setminus\{b\}\},\\
\operatorname{SAS}_{\Sigma_d}(W_{d+1})
  &=\{a^5,ba^4,b^2a^3\}.
\end{aligned}
\]
Thus the numbers of shortest absent subsequences are respectively \(d+1,d+1,3\), with shortest absent lengths \(2,3,5\). The three-word phenomenon begins at an alphabet-dependent but explicitly identified substitution boundary.

## Assumptions and scope

The stable theorem assumes \(m\ge2\), \(L\ne\varnothing\), and \(\operatorname{alph}(U)=L\). Letters \(a,b\) do not belong to \(L\). The tail \(Z\) may be empty but cannot contain \(a\). The morphic corollary assumes \(d\ge3\) and the specified nonuniform morphism, not the standard multinacci substitution. The alphabet for absence is always the **full** specified alphabet; symbols cannot be silently removed. Each language equality means that every unlisted word of the corresponding shortest-absent length *does* embed, and every word of shorter length embeds.

## Proof

**1. Arch decomposition of the stable family.** A complete alphabet arch is a shortest consecutive piece, starting at a specified boundary, that contains every letter of \(\Sigma\). Because \(U\) contains every letter of \(L\), the following is the greedy arch factorization of \(H_m\):
\[
\begin{array}{ll}
A_1=A_2=UaUb,\\
A_3=bUa,\quad A_4=UbUa,\\
A_{2j-1}=UbbUa,\quad A_{2j}=UbUa & (3\le j\le m),\\
T=UbbZ.
\end{array}
\]
Here \(H_m=A_1\cdots A_{2m}T\). Every displayed arch contains all of \(\Sigma\); its last symbol is its first occurrence of that particular symbol within the arch. The first two arches end with \(b\), and every later arch ends with \(a\). The tail \(T\) contains all letters except \(a\) (and has no \(a\)). Therefore \(H_m\) contains every word of length \(2m\) by taking one letter from each arch, whereas \(a^{2m+1}\) cannot occur because exactly \(2m\) copies of \(a\) occur. Its universality index is \(2m\).

**2. Exact language, not just its length.** Number the \(2m\) occurrences of \(a\) in \(H_m\) from left to right. Let \(P_j\) be the prefix strictly preceding its \(j\)-th \(a\), for \(1\le j\le2m\), and put \(P_{2m+1}=H_m\). In particular,
\[
P_2=UaUbU.
\]
This word has every letter, but only one \(a\) and one \(b\). A length-two word ending in \(L\) embeds using the initial complete block \(UaUb\) and the trailing \(U\); a word ending in \(a\) fails precisely when its first letter is \(a\) or \(b\); and a word ending in \(b\) fails precisely when its first letter is \(b\). Hence
\[
\{v\in\Sigma^2:v\not\preccurlyeq P_2\}=\{aa,ba,bb\}.
\]
For each \(3\le j\le 2m+1\), the arch decomposition gives \(P_j=A_1\cdots A_{j-1}T_j\), where \(T_j\) contains **every** letter of \(\Sigma\setminus\{a\}\). For \(j=3\), \(T_3=bU\); for subsequent internal boundaries, it is \(UbU\) or \(UbbU\); at the final boundary it is \(UbbZ\). Consequently every length-\(j\) word ending in a symbol different from \(a\) embeds, by choosing the first \(j-1\) letters in successive complete arches and the final symbol in \(T_j\).

For any length-\((j-1)\) word \(v\), the last available occurrence of \(a\) in \(P_j\) is the \((j-1)\)-th occurrence. Thus
\[
va\preccurlyeq P_j\quad\Longleftrightarrow\quad v\preccurlyeq P_{j-1}.
\]
The missing length-\(j\) words are therefore exactly the missing length-\((j-1)\) words of \(P_{j-1}\), each with one appended \(a\). Iterating from \(P_2\) to \(P_{2m+1}\) produces precisely \(\{aa,ba,bb\}a^{2m-1}\), which is the asserted three-word language. The universality-index argument proves these are the **shortest** absent words.

**3. Ruler prefix identity for the rich-word morphism.** For \(d\ge3\), define
\[
U=(\nu_2(1),\nu_2(2),\ldots,\nu_2(2^{d-2}-1)),
\]
interpreting entries as alphabet symbols, where \(\nu_2(t)\) is the exponent of two dividing the positive integer \(t\). It uses exactly the letters \(\{0,\ldots,d-3\}\). The usual ruler-word recursion, or the identity \(\nu_2(2t)=\nu_2(t)+1\) and \(\nu_2(2t-1)=0\), gives
\[
W_{d-1}=UaUb=R,\qquad \varphi_d(U)0=UaU.
\]
The only exceptional image is \(\varphi_d(b)=0bb\), so
\[
\varphi_d(R)=(\varphi_d(U)0)b(\varphi_d(U)0)bb=RRb,
\]
whence
\[
W_d=RRb,\qquad W_{d+1}=(RRb)^2\,0bb.
\]
The stable theorem with \(m=2\) and \(Z=0bb\) gives the third language in the morphic transition.

**4. The two preceding levels.** For \(R=UaUb\), the single full-alphabet arch ends with its sole \(b\). Every length-two word beginning in \(L\) embeds, by choosing its first letter in the first \(U\) and its second in the later occurrence, or at \(a\) or \(b\); every length-two word beginning with \(a\) except \(aa\) embeds; and no length-two word beginning with \(b\) embeds. This gives \(\{aa\}\cup\{bc:c\in\Sigma\}\).

For \(RRb\), its first two \(R\)'s are complete arches, so all words of length two embed. Any length-three word ending in \(b\) embeds with the last \(b\). A word ending in \(a\) can embed exactly when its initial two letters embed before the second \(a\), namely in \(P_2=UaUbU\); the missing initial pairs are \(aa,ba,bb\), giving \(aaa,baa,bba\). For a final letter \(c\in L\), the last \(c\) lies in the second \(R\)'s last \(U\). Every initial pair other than \(bb\) embeds before that \(c\): if the second letter is not \(b\), take the first in the first \(R\) and the second in the first \(Ua\) of the second \(R\); if it is \(b\), take the first non-\(b\) before the first \(R\)'s terminal \(b\). The pair \(bb\) cannot lie before this last \(c\), since only one \(b\) precedes it. This gives exactly \(bbc\) for \(c\in L\), completing the middle formula and the proof.

## Verification

The standalone `check.py` reconstructs morphic iterates directly from the substitution, independently computes the shortest-absent length and complete language from a next-occurrence dynamic program, and also compares against direct exhaustive enumeration for small alphabets. Its recorded execution checked 630 instances, including all three transition levels at alphabet sizes \(3\) through \(8\), arbitrary full-support lower-alphabet blocks, several block counts and suffixes, with 22 additional exhaustive length-level comparisons. These are finite consistency tests; the all-parameter result follows from the preceding structural proof, not the tests. Run with `python3 check.py` in the directory containing that file.

## Relationship to prior work

The motivating family is the nonuniform rich-word morphism studied by Dvořáková, Mol and Pelantová [1], whose work investigates repetition thresholds, return words and the structure of rich infinite words. Their paper defines exactly \(\varphi_d\) but does not present scattered-subsequence absence languages. Kosche, Koß, Manea and Siemer [2] develop general arch-based descriptions of shortest absent subsequences for arbitrary finite words; their Theorem 3.4 is an abstract characterization, not this exact uniform three-word classification, and does not give the sharp \(d+1,d+1,3\) transition. Manea, Ringleb, Siemer and Winkler [3] study efficient general enumeration algorithms rather than these concrete morphic words. The proof above makes the complete implication comparison explicit rather than treating differences in terminology as novelty.

## Limitations

The theorem does **not** classify shortest absent subsequences of all iterates \(W_k\) for unbounded \(k\) at a fixed \(d\); the morphic classification is restricted to exactly the three identified ranks. Its robust extension concerns specially structured concatenations \((RRb)^mZ\), not arbitrary rich words. A nonindexed earlier specialization of general arch theory could overlap the claim; primary-source priority remains an external validation question.

## References

[1] L. Dvořáková, L. Mol, E. Pelantová, *An automated approach to structure theorems for minimally repetitive rich words*, arXiv:2611.13676v1, first posted 2026-11-10, https://arxiv.org/abs/2611.13676.

[2] M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968; Fundamenta Informaticae 189 (2023), 199–240, https://fi.episciences.org/12396/pdf.

[3] F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471v1 (2025-04-30), https://arxiv.org/abs/2504.21471.
