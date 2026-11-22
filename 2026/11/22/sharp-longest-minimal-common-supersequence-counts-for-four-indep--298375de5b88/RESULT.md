# Sharp longest minimal common-supersequence counts for four independent binary run lengths

## Finding

For arbitrary positive integers \(a,b,c,d\), let \(A=0^a1^b\) and \(B=1^c0^d\). A word is a *minimal common supersequence* when it contains both \(A\) and \(B\) as scattered subsequences, but no proper scattered subsequence contains both. The maximum length of such a word is exactly
\[
L=a+b+c+d-1.
\]
Define
\[
H(a,b,c,d)=
\begin{cases}
\displaystyle\binom{d+b-1}{b},&a=1,\\
\displaystyle\binom{a+c-1}{c},&a>1,\ d=1,\\
\displaystyle\binom{a+c-2}{c-1}\binom{d+b-2}{b-1},&a>1,\ d>1.
\end{cases}
\]
The number of **distinct** minimal common supersequences attaining the maximum length is exactly
\[
\boxed{M(a,b,c,d)=H(a,b,c,d)+H(c,d,a,b).}
\]
The two summands classify disjoint sets: respectively those sharing exactly one zero and those sharing exactly one one between the input embeddings. In particular, all four run lengths may vary independently; no symmetry or equality is assumed. For instance, \((a,b,c,d)=(1,3,2,3)\) gives exactly \(10+6=16\) distinct longest words, at length \(8\).

## Assumptions and scope

All words are finite over \(\{0,1\}\). A scattered subsequence may delete any positions while retaining order. Deletion minimality means **every** single-position deletion destroys at least one of the two required subsequences; by upward closure, this is equivalent to minimality under all proper scattered subsequences. Each output word is counted once independently of its number of embeddings. The term *longest* refers to the greatest length among deletion-minimal common supersequences, not a shortest common supersequence.

The central structural description is as follows. The words contributing \(H(a,b,c,d)\) have exactly \(a+d-1\) zeros and \(b+c\) ones, and are
\[
w=P1\,0^h1Q,
\]
where \(P\) has \(x\) zeros and \(c-1\) ones, \(Q\) has \(y\) zeros and \(b-1\) ones, and one of these three alternatives applies:
\[
\begin{array}{ll}
(a,d\ge2):&x=a-1,\ h=1,\ y=d-1,\\
(a=1):&x=0,\ 1\le h\le d,\ y=d-h,\\
(a\ge2,d=1):&y=0,\ 1\le h\le a,\ x=a-h.
\end{array}
\]
When \(a=d=1\), use the second alternative, yielding the unique word of that type. The other branch is obtained by simultaneously exchanging zero and one and interchanging the two inputs; it contributes \(H(c,d,a,b)\).

## Proof

**1. A strict global length bound.** Let \(w\) be an arbitrary minimal common supersequence. Choose any embedding of \(A\) and any embedding of \(B\) into \(w\). Their union must cover every position of \(w\), since deleting an uncovered position would preserve both inputs. Thus \(|w|\le |A|+|B|\). If equality held, both embeddings would be disjoint and, moreover, each input would have a *unique* embedding: replacing either chosen embedding by a different embedding would leave some position unused in the union with the fixed other embedding.

In a hypothetical word containing exactly \(a+d\) zeros and \(b+c\) ones, write \(z_a\) for the position of the \(a\)-th zero and \(o_c\) for the position of the \(c\)-th one. If \(z_a<o_c\), there are at least \(b+1\) ones after \(z_a\): the \(c\)-th one and the last \(b\) ones. Consequently \(A\) embeds in at least two ways (choose the last \(b\) ones, or use the preceding \(c\)-th one and the last \(b-1\)). If \(o_c<z_a\), there are at least \(d+1\) zeros after \(o_c\), giving two embeddings of \(B\) analogously. These exhaust the distinct-position possibilities, contradicting uniqueness. Therefore \(|w|\le a+b+c+d-1\).

**2. Exactly two count branches at equality.** Suppose \(|w|=L\). Since the union of the chosen embeddings covers \(w\), the number \(Z\) of zeros is at most \(a+d\), and the number \(O\) of ones is at most \(b+c\). Since their sum is one below \(a+b+c+d\), either \((Z,O)=(a+d-1,b+c)\) or \((Z,O)=(a+d,b+c-1)\). These branches are disjoint. Analyze the first one; complementation and input exchange yield the second.

**3. A forced central zero gap.** For the zero-sharing branch, use canonical valid embeddings: the first \(a\) zeros and last \(b\) ones for \(A\), the first \(c\) ones and last \(d\) zeros for \(B\). Their zero sets share precisely the \(a\)-th zero, and their one sets are disjoint. Since they cover \(w\), this shared zero lies strictly between the \(c\)-th one and the \((c+1)\)-st one. Hence the word has a unique representation \(P1\,0^h1Q\) with \(h\ge1\), where \(P\) consists of the letters before the \(c\)-th one and \(Q\) of those after the \((c+1)\)-st one. Let their zero counts be \(x,y\); then \(x+h+y=a+d-1\), \(x+h\ge a\), and \(h+y\ge d\).

In particular \(x\le a-1\) and \(y\le d-1\). All first \(c\) ones are essential for \(B\): a later first-group one cannot be used to complete \(B\), as fewer than \(d\) zeros follow the \((c+1)\)-st one. The last \(b\) ones are similarly essential for \(A\), because fewer than \(a\) zeros precede the \(c\)-th one. Thus all ones are essential regardless of how the zeros within \(P,Q\) are interleaved.

**4. Characterizing essential zeros.** If \(x>0\), deleting a zero from \(P\) preserves \(B\). To destroy \(A\), the available zeros before the \((c+1)\)-st one must be tight: \(x+h=a\). Conversely this equality makes each prefix zero essential. Similarly, if \(y>0\), each suffix zero is essential exactly when \(h+y=d\). Removing a central zero preserves both inputs if and only if *both* inequalities remain valid; hence central zeros are essential exactly when \(x+h=a\) or \(h+y=d\).

If \(a,d\ge2\), neither \(x=0\) nor \(y=0\) is possible in a minimal word: for example \(x=0<y\) and suffix tightness would force \(a=1\) after using \(x+h+y=a+d-1\), while \(x=y=0\) leaves \(h=a+d-1\), from which a central zero can be removed. Therefore both \(x,y>0\), both tightness equalities hold and subtraction yields \(h=1,x=a-1,y=d-1\). If \(a=1\), the inequalities imply \(x=0\) and \(h+y=d\), with exactly \(1\le h\le d\). If \(a>1,d=1\), symmetrically \(y=0,x+h=a\), with \(1\le h\le a\). Each displayed family satisfies all essentiality conditions, so every listed word is indeed minimal.

**5. Counting and noncollision.** With \(x\) zeros, the prefix \(P\) may interleave them arbitrarily with \(c-1\) ones, giving \(\binom{x+c-1}{c-1}\) words. The suffix independently contributes \(\binom{y+b-1}{b-1}\). At \(a,d\ge2\), substitution gives the product in \(H\). At \(a=1\), summing over \(y=0,\ldots,d-1\) gives the hockey-stick identity
\[
\sum_{y=0}^{d-1}\binom{y+b-1}{b-1}=\binom{d+b-1}{b}.
\]
The case \(d=1,a>1\) is symmetric and gives \(\binom{a+c-1}{c}\). All described words have distinct central boundaries (defined by the \(c\)-th and \((c+1)\)-st ones), and the two global count branches have different letter inventories. Their sum is therefore the exact count, and its positivity proves that \(L\) is attained.

## Verification

The standalone `verification/exhaustive.py` enumerates every binary word at the target length and one longer for all \(81\) positive parameter quadruples with each coordinate at most three. It independently checks both subsequence requirements and every single deletion, finding \(866\) target-length minimal words and none one symbol longer. The separate `verification/constructive.py` enumerates candidate interleavings and direct deletion minimality for all \(625\) quadruples with coordinates at most five, checks the two branches' disjointness, and verifies the formula across \(130102\) reconstructed words. The exact command/output files are included. These are finite corroborations only; the unrestricted positive-integer claim is proved in the five steps above.

## Relationship to prior work

Sopp, Liyanage, Gong and Zhu (2026) establish general algorithms for finding and enumerating minimal common supersequences of two arbitrary strings, including an output-delay bound; their general DAG construction does not present the four-run binomial formula above. Fraser, Irving and Middendorf (1996) give a dynamic programming algorithm for the *length* of longest minimal common supersequences, not a count of all longest words in this four-parameter family. Existing explicit opposite-block length spectra treat the two-parameter subfamilies \(0^m1^m\) versus \(1^m0^m\), and \(0^a1^b\) versus \(1^b0^a\); both are recovered here in their longest layer, with the latter's count \(2\binom{a+b-2}{a-1}^2\). Those special cases are not claimed as new. The present result counts longest words for four freely chosen positive run lengths, including exceptional boundary branches at \(a=1\) or \(d=1\).

## Limitations

No formula is claimed here for the number at shorter minimal-supersequence lengths, for three or more inputs, for patterns with more transitions or for higher alphabets. Search and inspectable literature cannot exclude an equivalent unindexed or previously unrecognized corollary, particularly of older algorithms; no independent review is claimed. The verification scripts check finite instances, not the entire infinite family.

## References

1. B. Sopp, A. Liyanage, M. Gong and B. Zhu, *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591v1, first public 2026-03-23. https://arxiv.org/html/2603.22591v1
2. C. B. Fraser, R. W. Irving and M. Middendorf, *Maximal Common Subsequences and Minimal Common Supersequences*, *Information and Computation* **124** (1996), 145–153. https://www.academia.edu/54088366/Maximal_Common_Subsequences_and_Minimal_Common_Supersequences
3. C. B. Fraser, *Subsequences and Supersequences of Strings*, University of Glasgow doctoral thesis (1995), Chapter 6. https://theses.gla.ac.uk/74575/1/10992195.pdf
4. *Exact minimal-supersequence spectra for unequal opposite binary runs* (2026), public mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-minimal-supersequence-spectra-for-unequal-opposite-binary--d41f14eae316
5. *Complete length spectrum of minimal common supersequences for opposite binary blocks* (2026), public mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-length-spectrum-of-minimal-common-supersequences-for-op--5df86cdf4ed9
