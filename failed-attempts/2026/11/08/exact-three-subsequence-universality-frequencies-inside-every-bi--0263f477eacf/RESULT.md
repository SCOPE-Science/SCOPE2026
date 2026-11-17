# Exact three-subsequence-universality frequencies inside every binary two-deck class

## Finding

Let \(A,B\geq 3\) be integers and \(0\leq C\leq AB\). Let \(L_{A,B,C}\) be the set of binary words containing exactly \(A\) copies of \(a\), \(B\) copies of \(b\), and \(C\) scattered occurrences of \(ab\). Write \(D=AB-C\). A word is *3-subsequence-universal* if it contains all eight binary words of length three as scattered subsequences. Let \(E(A,B,C)\) count the members of \(L_{A,B,C}\) that are not 3-subsequence-universal. Write \([P]\) for \(1\) if proposition \(P\) holds and \(0\) otherwise.

**Exact conditional spectrum theorem.** For every such triple,

\[
\begin{aligned}
E(A,B,C)={}&[C\leq A]+[C\leq B]+[D\leq A]+[D\leq B]\\
&+[A\mid C]+[B\mid C]\\
&-[C=1]-[D=1]-[C=A]-[D=A]-[C=B]-[D=B]\\
&-3[C=0]-3[D=0].
\end{aligned}
\]

Furthermore, \(0\leq E(A,B,C)\leq2\), and both extremes and the intermediate value occur. The class has exactly

\[
\left[q^C\right]\begin{bmatrix}A+B\\A\end{bmatrix}_q-E(A,B,C)
\]

3-subsequence-universal members, where \(\begin{bmatrix}A+B\\A\end{bmatrix}_q=\prod_{i=1}^{A}(1-q^{B+i})/(1-q^i)\). Thus its exact conditional 3-universality probability is \(1-E(A,B,C)/\left[q^C\right]\begin{bmatrix}A+B\\A\end{bmatrix}_q\). The total number of non-3-universal words over all \(C\) with this fixed composition is \(3(A+B)-6\), and hence the total number of 3-universal words with this composition is \(\binom{A+B}{A}-3(A+B)+6\).

In particular, every fiber contains at most two non-3-universal words, even when the fiber itself has arbitrarily large cardinality.

## Assumptions and scope

Letters \(a,b\) are distinct; all word counts refer to indexed finite words, with distinct words identified by their letter sequences. A scattered subsequence is obtained by deleting positions without reordering. The symbol \(\mid\) denotes integer divisibility, with \(A,B\geq3\), so all divisions are well-defined. Every \(C\in\{0,\ldots,AB\}\) determines a nonempty class. The theorem does not assert the displayed exception formula when either multiplicity is less than three: then a necessary unary length-three pattern is missing from every word. The assertions are exact for arbitrary, not bounded, multiplicities.

## Proof

**Step 1: the six uniquely determined avoiders.** Because \(A,B\geq3\), every class member contains both \(aaa\) and \(bbb\). For each other length-three pattern, if a class member avoids the pattern, that member is forced to have one of the following six forms. The stated arithmetic condition is both necessary and sufficient. All displayed exponents are nonnegative in their stated ranges.

| Avoided pattern | Existence condition | Unique avoiding word |
|---|---|---|
| \(aab\) | \(C\leq B\) | \(b^{B-C}ab^Ca^{A-1}\) |
| \(abb\) | \(C\leq A\) | \(b^{B-1}a^Cba^{A-C}\) |
| \(baa\) | \(D\leq B\) | \(a^{A-1}b^Dab^{B-D}\) |
| \(bba\) | \(D\leq A\) | \(a^{A-D}ba^Db^{B-1}\) |
| \(aba\) | \(A\mid C\) | \(b^{B-C/A}a^Ab^{C/A}\) |
| \(bab\) | \(B\mid C\) | \(a^{C/B}b^Ba^{A-C/B}\) |

To prove uniqueness for \(aab\), no \(b\) may follow the second \(a\); hence every \(b\) lies before or between the first two \(a\)'s. A \(b\) between those two positions contributes one \(ab\) pair, while a \(b\) before them contributes none. Exactly \(C\) must occupy the former region. This determines the listed word. For \(abb\), no \(a\) may precede two \(b\)'s, so all \(a\)'s lie after the penultimate \(b\); exactly \(C\) of them lie between the last two \(b\)'s, again determining the word. Reversing \(a\) and \(b\), and replacing \(C\) by \(D\), proves the two corresponding forms for \(baa\) and \(bba\). Avoidance of \(aba\) forces every \(b\) outside the interval between the first and last \(a\), hence all \(a\)'s form one block; its number of trailing \(b\)'s is uniquely \(C/A\). The final form is symmetric. These derivations also verify that all six forms have the claimed letter multiplicities and pair count.

**Step 2: classify all coincidences.** Fix \(0<C<AB\). If \(C\leq\max(A,B)\), then \(D>\max(A,B)\), since \(AB>2\max(A,B)\) for \(A,B\geq3\). Thus none of the \(D\)-side forms occurs. The only repeated canonical words on this side are the following equalities, with each equality valid precisely under the indicated condition:

\[
\begin{array}{c|c}
\text{coincident avoiders}&\text{condition}\\\hline
aab,abb&C=1\\
abb,aba&C=A\\
aab,bab&C=B
\end{array}
\]

This follows by comparing the positions and lengths of the nonempty constant-letter runs in the six forms. If \(D\leq\max(A,B)\), the symmetric three equalities are \(baa=bba\) exactly when \(D=1\), \(bba=aba\) exactly when \(D=A\), and \(baa=bab\) exactly when \(D=B\). The low-\(C\) and low-\(D\) regimes are disjoint. In the remaining central regime, the only possible avoiders are those of \(aba\) and \(bab\), and they cannot coincide: a word with all its \(a\)'s contiguous and all its \(b\)'s contiguous has \(C\in\{0,AB\}\). Equalities on the same side are pairwise disjoint as words, even when two conditions occur at the same value of \(C\); no nonendpoint word lies in three or more of the six avoidance categories.

At \(C=0\) the four canonical candidates for \(aab,abb,aba,bab\) coincide in the one word \(b^Ba^A\), requiring a correction of three to the raw total. At \(D=0\) the four candidates for \(baa,bba,aba,bab\) coincide in \(a^Ab^B\), again requiring a correction of three. Consequently, starting with one for each existing avoidance candidate and subtracting the six pair coincidences and two endpoint triple-overcounts yields exactly the claimed indicator formula.

**Step 3: bound and compositions.** In the middle region \(\min(C,D)>\max(A,B)\), there are at most the two \(aba\)- and \(bab\)-avoiders. In either boundary region, there are at most two *distinct* canonical words by the coincidence classification: the only way to have three or four simultaneously existing candidates is when one or two merge with a base candidate, as listed above. At the endpoints there is only one. Thus \(E\leq2\), with nonnegativity automatic because \(E\) counts words. Values \(0,1,2\) occur already for \(A=B=3\) at \(C=4,0,2\), respectively.

Summing the six positive indicator contributions over all \(C=0,\ldots,AB\) gives \(3(A+B+2)\). Each of the six isolated collision corrections contributes one, and the two endpoint corrections together contribute six. Hence \(\sum_C E(A,B,C)=3(A+B)-6\).

**Step 4: total fiber size.** Writing a word according to its \(A+1\) gaps between consecutive \(a\)'s, the number of \(ab\) pairs is the sum of the gap indices weighted by their \(b\)-multiplicities. This is the standard partition-in-a-rectangle bijection, so the polynomial counting class sizes by \(C\) is \(\begin{bmatrix}A+B\\A\end{bmatrix}_q\). Subtracting the proven exact number \(E\) gives the asserted count and probability. Summing over \(C\) gives \(\binom{A+B}{A}-3(A+B)+6\).

## Verification

The included standalone Python 3 program `verify.py` constructs every binary word with \(3\leq A,B\leq8\), independently counts all eight length-three subsequences by a greedy embedding test, groups words by exact \(ab\)-pair count, and compares: (i) the proposed exception formula; (ii) the distinct six canonical avoiders; (iii) an independent dynamic-programming construction of the Gaussian fiber coefficient. It also verifies the summed composition identity. This exhausts 48,200 words and 1,125 distinct parameter fibers. A second finite test compares the formula with the canonical-word set for all \(3\leq A,B\leq16\), totaling 17,885 parameter fibers. Output: `VERIFY_OK`.

These finite checks do not establish the theorem for arbitrary parameters. That conclusion follows from the uniqueness and collision proof above. Reproduce with `python3 verify.py` from the directory containing the checker.

## Relationship to prior work

Fazekas, Huang and Mercaş (2026), *Subsequence Analysis Problems for Binary Parikh Matrices*, Section 4, Lemma 4.3, gives the arithmetic **existence** conditions for avoiding each length-three subsequence; Theorem 4.4 determines when all representatives are 3-universal. Those existence conditions and their structural arguments are the necessary starting point, **not claimed as original here**. Their Section 5 investigates fixed-pattern containment probability and an additive approximation scheme. The present theorem instead determines the **exact number of representatives failing simultaneous containment of any length-three pattern**, resolves all overlaps among the six avoidance types, and obtains exact conditional probabilities within each individual two-deck class and the uniform two-exception bound. No existing claim of exact conditional counts is inferred merely from a title or abstract; the comparison is against the full Sections 3–5.

Richomme (2025/2026) develops the partition structure inside binary two-binomial classes. Golafshan (2026) determines their full class-size distribution via hyperplane arrangements and Gaussian coefficients. Neither of those works supplies a three-universality refinement of the class-size coefficients. A previously published unrestricted-length law for subsequence-universality indices counts words without conditioning on \(C\), so it does not itself state this conditional classification.

## Limitations

The theorem addresses 3-subsequence universality, not arbitrary universality indices, and assumes \(A,B\geq3\). It extends the published per-pattern avoidance characterizations by tracking overlaps and exact multiplicities; it should not be interpreted as an independent discovery of those characterizations, nor as an efficient algorithm for counting arbitrary four-letter pattern avoidance. The denominator is a Gaussian-binomial coefficient that can have large bit complexity. The structural novelty comparison is made to accessible indexed literature; an equivalent prior exact conditional count not found in that material remains a priority risk. Independent external review has not been performed.

## References

1. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717, first available October 5, 2026, https://arxiv.org/abs/2610.06717. Relevant sections: 3, 4 (especially Lemma 4.3 and Theorem 4.4), and 5.
2. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159, first available October 8, 2025, https://arxiv.org/abs/2510.07159. Relevant sections: partition model and two-binomial equivalence.
3. M. Golafshan, *Binary binomial equivalence via hyperplane arrangements*, arXiv:2606.23426, first available June 22, 2026, https://arxiv.org/abs/2606.23426. Relevant sections: binary two-binomial class sizes and Gaussian coefficients.
