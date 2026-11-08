# The first four-position string attractors among distinct-gap marker words

## Finding
Let \(\mathcal G\) comprise all words
\[
W(g_1,\ldots,g_k)=1\,0^{g_1}1\,0^{g_2}1\cdots0^{g_k}1,
\qquad k\ge1,
\]
where the \(g_i\) are **pairwise distinct positive integers**, with no assumption on their order. A string attractor of \(W\) is a set of positions such that every distinct nonempty contiguous factor of \(W\) has an occurrence meeting the set. Write \(\gamma(W)\) for the smallest possible size.

**Sharp first-attainment theorem.** The least word length among members of \(\mathcal G\) with \(\gamma(W)\ge4\) is \(18\). Among *all* members with length at most \(18\), precisely two require four positions: the reversal pair with gap vectors
\[
(1,3,2,7),\qquad (7,2,3,1).
\]
All other members of \(\mathcal G\) of length at most \(18\) satisfy \(\gamma(W)\le3\). Both exceptional words have \(\gamma(W)=4\).

## Assumptions and scope
The alphabet is \(\{0,1\}\). All gaps are positive integers and distinct from one another, but may appear in an arbitrary permutation. Positions are numbered \(0,1,\ldots,|W|-1\). A factor is *contiguous*, not a scattered subsequence; factors are counted distinctly, but every occurrence may be used to witness attraction. This is an exact statement **only through length \(18\)**, plus sharpness of the threshold; it is not a formula for arbitrarily long distinct-gap words. The relevant first-public guiding source [3] was posted on 2022-06-01.

## Proof
**1. A four-position witness.** Put
\[
W=W(1,3,2,7)=\mathtt{101000100100000001},
\quad S=\{0,3,8,13\}.
\]
Its five 1-markers occur at positions \(0,2,6,9,17\). A factor with two or more occurrences of the symbol \(1\) contains a complete adjacent-marker block \(1\,0^{g_i}1\). Since all four gap lengths differ, any occurrence of this block must be at the corresponding adjacent-marker pair; the four pairs' spans are \([0,2]\), \([2,6]\), \([6,9]\), and \([9,17]\), each meeting \(S\). A factor consisting entirely of zeros embeds in the final length-seven zero run, with an occurrence meeting position \(13\).

For a factor having exactly one 1, write it as \(0^a1\,0^b\). The possible nonnegative exponent pairs are exactly the union of the five rectangles
\[
[0,0]\!\times\![0,1],\quad [0,1]\!\times\![0,3],\quad
[0,3]\!\times\![0,2],\quad [0,2]\!\times\![0,7],\quad
[0,7]\!\times\![0,0].
\]
Here interval notation includes both integer endpoints. If \(a=0\), choose the marker at position \(0\) for \(b\le1\), at \(2\) for \(2\le b\le3\), and at \(9\) for \(4\le b\le7\); these occurrences meet \(0,3,13\), respectively. If \(a=1\) or \(2\), choose the marker at \(9\), using position \(8\) within the factor. If \(a=3\), necessarily \(b\le2\); choose the marker at \(6\), using position \(3\). If \(4\le a\le7\), necessarily \(b=0\); choose the final marker at \(17\), using position \(13\). Thus \(S\) attracts every factor, proving \(\gamma(W)\le4\).

**2. A six-factor obstruction to three positions.** For each factor \(f\), let \(C(f)\) be the union of the position sets of all its occurrences in \(W\). Direct string matching gives the following complete occurrence-coverage table:

| Factor \(f\) | \(C(f)\) as inclusive intervals |
|---|---|
| `101` | \([0,2]\) |
| `10000` | \([9,13]\) |
| `00010` | \([3,7]\) |
| `00001` | \([13,17]\) |
| `001000` | \([7,12]\) |
| `0001` | \([3,6]\cup[14,17]\) |

Every attractor must meet each \(C(f)\). One point belongs to \([0,2]\) to cover `101`. Two remaining points would have to cover disjoint \([3,7]\) (for `00010`) and \([13,17]\) (for `00001`), one in each. Covering `10000` forces the latter point to be \(13\); covering `001000` forces the former point to be \(7\). Yet neither \(7\) nor \(13\) lies in \([3,6]\cup[14,17]\), so `0001` is uncovered. Hence \(\gamma(W)\ge4\), and the size equals four.

**3. Finite exclusion and uniqueness below the sharp threshold.** Any member has
\[
|W|=k+1+\sum_{i=1}^k g_i\ge k+1+\frac{k(k+1)}2.
\]
Thus \(|W|\le18\) forces \(1\le k\le4\): for \(k=5\) the minimum is already \(21\). For each \(1\le k\le4\), enumerate all ordered injective gap vectors with entries drawn from \(\{1,\ldots,17\}\) and \(\sum_i g_i+k+1\le18\). There are exactly \(16,98,246,168\) such vectors for \(k=1,2,3,4\), respectively, a total of \(528\).

The supplied `verify.py` constructs every one of these \(528\) words; enumerates all distinct factors and, for each factor, the union of positions occupied by any occurrence; and tests position subsets in increasing cardinality against every such coverage set. The loop uses the full, proved finite parameter range, not a sample, and implements exactly the definition of \(\gamma\). Its full output has \(\gamma\ge4\) in **precisely** the two gap vectors above, both with value four. Therefore every shorter member has \(\gamma\le3\) and no other member of length at most \(18\) achieves four. The second exceptional word is the reversal of the first; reversal preserves factor occurrence coverage and hence attractor size, also giving a conceptual confirmation of its value.

## Verification
Run `python3 verify.py` in the directory containing the complete provided standalone file. It prints `VERIFY_OK` only after checking all \(528\) eligible words, all factor coverages, independently checking each returned witness using direct occurrence searches, confirming the six-factor obstruction, checking \(117\) distinct factors in the displayed witness, and asserting the exact two exceptional gap vectors. The overall histogram by gap count is: for \(k=1\), sixteen words of attractor size two; for \(k=2\), ninety-eight of size two; for \(k=3\), forty-two of size two and two hundred four of size three; for \(k=4\), one hundred sixty-six of size three and two of size four. An additional exact mixed-integer-programming check using a separate solver formulation agreed on all \(528\) words; that computational comparison does not constitute an independent scientific audit. The finite exhaustion is part of the rigorous proof only because the length cutoff bounds all possible parameter vectors.

## Relationship to prior work
String attractors originate in [1]; the combinatorial treatment [2] establishes, among other properties, reversal invariance, but does not determine this restricted sharp threshold. [3] studies infinite words' attractor complexities, not the exact distinct-gap finite threshold. General exact optimization algorithms in [4] do not imply a family-specific first-attainment classification without the explicit exhaustive computation. The unrestricted binary-word table [5] already has words requiring four attractor positions at length \(12\); our threshold \(18\) is **only** for the defined distinct-positive-gap marker family. Existing results for **strictly increasing** gaps are not claimed here: dropping the ordering assumption is essential and cannot be inferred by permutation invariance, since factor structures depend on gap order. The reversal pair is expected from the known symmetry, whereas the sharp cutoff and uniqueness are the additional facts.

## Limitations
No statement is made about the complete attractor-size spectrum above length \(18\) or about repeated/zero-length gaps, and no independent scientific audit has occurred. The enumeration is finite but exhaustive after a proved parameter bound. An unindexed equivalent result or an unnoticed stronger theorem in the literature remains a bibliographic risk.

## References
1. D. Kempa and N. Prezza, *At the Roots of Dictionary Compression: String Attractors* (preprint 2017), https://arxiv.org/abs/1709.05314.
2. S. Mantaci et al., *A Combinatorial View on String Attractors*, *Theoretical Computer Science* (2021), open author version: https://arpi.unipi.it/retrieve/e0d6c92f-ec13-fcf8-e053-d805fe0aa794/MRRRS_TCS2021.pdf.
3. A. Restivo, G. Romana and M. Sciortino, *String Attractors and Infinite Words* (first public 2022-06-01), https://arxiv.org/abs/2206.00376.
4. H. Bannai et al., *Computing NP-hard Repetitiveness Measures via MAX-SAT* (2022), https://arxiv.org/abs/2207.02571.
5. OEIS A339391, *Maximum, over all binary strings of length \(n\), of the size of the smallest string attractor*, https://oeis.org/A339391.
