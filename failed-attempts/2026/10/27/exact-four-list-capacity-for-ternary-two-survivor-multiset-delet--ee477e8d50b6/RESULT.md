# Exact four-list capacity for ternary two-survivor multiset deletion

## Finding
For each integer \(n\ge 2\), let \(A_4(n)\) be the largest cardinality of a family \(\mathcal C\) of distinct ternary multisets of cardinality \(n\) such that **every** unordered multiset of two surviving symbols has at most four possible parents in \(\mathcal C\). Then
\[
\boxed{A_4(n)=\begin{cases}
6,&n=2,\\
10,&n=3,\\
11,&n\ge4.
\end{cases}}
\]
In particular, the natural bound of twelve codewords obtained by assigning four codewords to each of the three monochromatic received multisets is unattainable throughout \(n\ge4\). Eleven codewords are always attainable. This is an exact all-length capacity theorem for a fixed, natural high-deletion/list-decoding regime.

## Assumptions and scope
An alphabet has three **labeled** symbols \(\{0,1,2\}\). A source multiset of cardinality \(n\) is identified with its multiplicity vector \(x=(x_0,x_1,x_2)\in\mathbb Z_{\ge0}^3\), where \(x_0+x_1+x_2=n\). A possible channel output is a vector \(y\in\mathbb Z_{\ge0}^3\) with \(y_0+y_1+y_2=2\) and \(y_i\le x_i\) for every coordinate. Thus the channel deletes exactly \(n-2\) symbols, forgetting their order; an unordered output is counted once, independent of deletion multiplicity.

A code \(\mathcal C\) is **four-list-decodable** if for each such output \(y\), at most four distinct codewords \(x\in\mathcal C\) satisfy \(y\le x\) coordinatewise. There is no requirement for efficient decoding. The result concerns four-list decoding, not unique decoding or ordered deletion subsequences. No claim is made about other alphabet sizes, output lengths, or list allowances.

## Proof
Write \(e_0,e_1,e_2\) for the three coordinate unit vectors and put
\[
\mathcal R=\{2e_0,2e_1,2e_2,e_0+e_1,e_0+e_2,e_1+e_2\}.
\]
For a source vector \(x\), define its distinct-output degree
\[
d(x)=\#\{y\in\mathcal R:y\le x\}.
\]
The four-list condition gives the **incidence bound**
\[
\sum_{x\in\mathcal C}d(x)
=\sum_{y\in\mathcal R}\#\{x\in\mathcal C:y\le x\}
\le 6\cdot4=24.\tag{1}
\]

For \(n=2\), all six possible source multisets may be used: each output is compatible only with itself. For \(n=3\), all ten source multisets may be used: a two-symbol multiset has exactly three distinct three-symbol parents, obtained by adjoining one of the three alphabet symbols. These achieve the trivial total-source bounds.

Now fix \(n\ge4\). Every source vector contains a repeated symbol, so every codeword is compatible with at least one of the three monochromatic outputs; thus monochromatic capacity alone gives the preliminary bound \(3\cdot4=12\). The **three pure** words \(ne_i\) are exactly the words of degree one. The **six nearly pure** words \((n-1)e_i+e_j\), where \(i\ne j\), are exactly the words of degree two. Every remaining word has degree at least three. Indeed, if exactly two symbols occur with both counts at least two, its possible outputs are precisely the two monochromatic pairs and the mixed pair, giving degree three. If all three symbols occur, all three mixed pairs are outputs, and since \(n\ge4\), at least one monochromatic pair is also an output; hence its degree is at least four. Conversely, a two-symbol word with one multiplicity one is nearly pure, and a one-symbol word is pure.

Suppose twelve codewords existed. The twelve smallest possible source-output degrees sum to
\[
3\cdot1+6\cdot2+3\cdot3=24.
\]
By (1), equality is compulsory. In particular, the code must contain **all nine** pure and nearly pure words and exactly three additional words of degree three. Each monochromatic output \(2e_i\) already has precisely three parents among those nine: the pure word \(ne_i\) and the two nearly pure words with majority symbol \(i\). It therefore has room for only one further parent. But every degree-three word has exactly two positive coordinates, both at least two, so its output set contains **two** monochromatic outputs. The three additional degree-three words would contribute six monochromatic incidences to the three remaining slots, a contradiction. Larger codes cannot exist either, since any twelve-element subcode would satisfy the same constraints. Thus \(A_4(n)\le11\).

For equality, take the three pure words, all six nearly pure words, and the following two words involving all three symbols:
\[
(n-2,1,1),\qquad(1,n-2,1).\tag{2}
\]
For every \(n\ge4\), these eleven vectors are distinct. Each monochromatic output \(2e_i\) has three parents among the nine core words and at most one extra parent from (2), because the two vectors have different unique coordinates of multiplicity at least two. Each mixed output \(e_i+e_j\) has precisely two parents among the nine core words and both words from (2), giving four. Consequently every received output has at most four parents, establishing \(A_4(n)\ge11\). Together with the upper bound this completes the proof for all \(n\ge2\).

## Verification
The included `verify.py` independently constructs all six possible two-symbol outputs, all source multiplicity vectors at finite lengths, and the eleven-codeword construction. It confirms the construction for each integer \(4\le n\le128\), checks the exact degree-one, degree-two and degree-three classification for \(4\le n\le32\), and **exhaustively enumerates** every twelve-word subset at \(n=4\) and \(n=5\), respectively \(455\) and \(293930\) subsets. None is four-list-decodable. It also checks the complete small-length bounds at \(n=2,3\). Run `python3 verify.py` with Python 3 standard library only; the output of an actual run is included as `CHECKS.txt`.

As an additional independent finite check, a zero-one integer linear program with one column per source multiset and one capacity-four row per received multiset found proven optima of eleven at \(n=4,5,6,8,12\). These checks support reproducibility but do not replace the infinite symbolic proof above.

## Relationship to prior work
The motivating work *Multiset Deletion-Correcting Codes: Bounds and Constructions* [1] establishes the unordered multiset deletion channel and bounds and constructions for **unique-decodable** codes. Its two-survivor parameter range does not yield the present four-list capacity. The subsequent *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes* [2] investigates polynomial and geometrical aspects of multiset deletion balls, but the inspected results do not assert the exact four-list profile above. The foundational multiset-channel study [3] likewise concerns distinct error-correction objectives. For contrast, constant-list insertion-deletion results for **ordered words** [4] do not give exact capacity in the unordered ternary simplex.

At list allowance three, the nine pure and nearly pure words are feasible: each monochromatic output has exactly three parents and each mixed output exactly two. Conversely, since every ternary length-\(n\ge4\) source includes a repeated symbol, three monochromatic outputs each with capacity three bound every such list-three code by nine. Thus list allowance four is the first allowance for which the simple monochromatic capacity bound fails in this two-survivor ternary regime.

The key distinction is between imposing pairwise disjoint output balls and limiting each received ball's **codeword incidence to four**. The present formula sharpens the elementary monochromatic-output packing count \(3\cdot4=12\) by one at all lengths from four onward. No complete priority assertion is made about unpublished or unindexed equivalent computations.

## Limitations
The theorem fixes alphabet size three, exactly two surviving symbols, and list allowance four; it does not classify all optimal codes or determine unrestricted parameter families. The proof is self-contained and infinite in the source length, while finite checks provide corroboration only. Historical priority is assessed against the specifically inspected primary sources and searched research records; independently existing unindexed or inaccessible work remains possible. No independent external audit or formal certification has been performed.

## References
[1] *Multiset Deletion-Correcting Codes: Bounds and Constructions*, arXiv:2601.05636 (first public posting 2026-01-09), https://arxiv.org/html/2601.05636.

[2] *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322 (2026), https://arxiv.org/html/2603.18322.

[3] *Codes in the Space of Multisets—Coding for Permutation Channels With Impairments*, arXiv:1612.08837 (2016), https://arxiv.org/html/1612.08837.

[4] *Constant-List Insertion–Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395 (2026), https://arxiv.org/html/2609.21395.
