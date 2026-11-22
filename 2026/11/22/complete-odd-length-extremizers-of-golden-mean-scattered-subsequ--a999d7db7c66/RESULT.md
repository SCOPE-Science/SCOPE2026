# Complete odd-length extremizers of golden-mean scattered-subsequence covers

## Finding

Let \(m\ge0\) and let \(\mathcal G_{2m+1}\) be the set of all binary words of length \(2m+1\) that avoid the **contiguous** factor `11`. A word \(W\) is a *master* if every \(u\in\mathcal G_{2m+1}\) is a scattered subsequence of \(W\). No restriction is placed on the master in the definition.

**Theorem.** The minimum master length is \(3m+2\). More precisely, the **entire set** of masters attaining that length is
\[
\mathcal M_m=\{(\mathtt{010})^j\,\mathtt{10}\,(\mathtt{010})^{m-j}:0\le j\le m\}\;\cup\;\{(\mathtt{010})^m\,\mathtt{01}\}.
\]
The displayed words are distinct. Consequently there are exactly \(m+2\) shortest masters for every odd target length. Every shortest master automatically avoids the factor `11`, even though this was not required. In the extremal letter-content class, it is sufficient to test only the \(2m+1\) target words containing exactly one `1`.

The previously known minimum-length formula for arbitrary target lengths is *not* presented as new; the result is the odd-length **classification and exact count**, including the unrestricted-master rigidity.

## Assumptions and scope

The alphabet is the labeled set \(\{0,1\}\). A scattered subsequence is obtained by deleting zero or more positions without reordering surviving positions. A target avoids adjacent ones when no two *consecutive positions* are both one; its embedding in the master need not use adjacent positions. All statements hold for every integer \(m\ge0\), including \(m=0\), when the two optimal masters are `01` and `10`.

For a binary word \(W\), write \(|W|_0\) and \(|W|_1\) for the numbers of occurrences of its respective letters. For \(0\le i\le2m\), put \(v_i=0^i1\,0^{2m-i}\). For an occurrence of `1` in \(W\), its *zero-rank* is the number \(c\) of `0` symbols strictly before it.

## Proof

**1. Length and forced content.** Both \(0^{2m+1}\) and \((10)^m1\) belong to \(\mathcal G_{2m+1}\). Any master therefore contains at least \(2m+1\) zeros and at least \(m+1\) ones, forcing \(|W|\ge3m+2\). Every word displayed in the theorem has exactly \(2m+1\) zeros and \(m+1\) ones, so the constructions below attain the bound. Thus a shortest master \(W\) must satisfy
\[
|W|_0=2m+1,\qquad |W|_1=m+1.
\]

**2. A rank-cover equivalence.** Given the forced letter counts, an occurrence of `1` at zero-rank \(c\) can serve as the unique one in \(v_i\) exactly when
\[
i\le c\le i+1.
\]
Indeed the \(i\) zeros before that `1` and the \(2m-i\) zeros after it must both be available; of the \(2m+1\) zeros in the master, exactly one is omitted in such an embedding. Hence \(W\) covers every single-one target \(v_i\) precisely when its \(m+1\) zero-ranks \(c_0\le\cdots\le c_m\) cover every integer \(i\in\{0,\ldots,2m\}\) by the intervals \(\{c_t-1,c_t\}\cap\{0,\ldots,2m\}\).

A repeated rank corresponds to two adjacent ones. Such a repetition leaves at most \(2m\) distinct integers covered: \(m+1\) rank intervals each contain at most two integers, while a repeated rank produces at least two duplicate memberships (and a rank at an endpoint covers only one). But \(2m+1\) distinct integers must be covered. Therefore every shortest master has strictly increasing ranks and so avoids contiguous `11`.

**3. Complete rank classification.** Let \(c_0<\cdots<c_m\). Full coverage of \(\{0,\ldots,2m\}\) implies
\[
c_0\in\{0,1\},\quad c_m\in\{2m,2m+1\},\quad c_{t+1}-c_t\in\{1,2\}\quad(0\le t<m).
\]
Conversely these conditions suffice: the first rank covers \(i=0\), the last covers \(i=2m\), and no gap of three or more can leave an uncovered index. For \(m=0\), the sole rank is \(0\) or \(1\), yielding `10` and `01`; assume \(m\ge1\) below.

If \(c_0=0\), the \(m\) increments total at least \(2m\); they can total at most \(2m\), so all increments are two and \(c_m=2m\). This yields \(10(010)^m\). If \(c_0=1,c_m=2m+1\), all increments are two, yielding \((\mathtt{010})^m\mathtt{01}\). In the remaining case \(c_0=1,c_m=2m\), the increments total \(2m-1\), so exactly one is one and every other increment is two. Its choice among the \(m\) rank gaps gives exactly the \(m\) words \((\mathtt{010})^j\mathtt{10}(\mathtt{010})^{m-j}\) with \(1\le j\le m\). The impossible endpoint pair \((0,2m+1)\) would require increments summing to \(2m+1\), beyond their maximum. Thus there are precisely \(m+2\) candidate shortest masters, and each is uniquely determined by its rank sequence.

**4. All admissible targets are covered.** Every adjacent two-letter block of a word avoiding contiguous `11` is one of `00`, `01`, or `10`, and all three are scattered subsequences of `010`. Fix \(0\le j\le m\) and partition any \(u\in\mathcal G_{2m+1}\) into its first \(j\) consecutive two-letter blocks, one following letter, and its remaining \(m-j\) two-letter blocks. Embed the blocks one per copy of `010`, and embed the remaining single letter in `10`. This embeds \(u\) into \((\mathtt{010})^j\mathtt{10}(\mathtt{010})^{m-j}\). Alternatively partition into \(m\) consecutive two-letter blocks and a final letter; embed the blocks in \((010)^m\) and the final letter in `01`. Therefore all candidates cover the entire target family and attain the lower bound.

The rank-cover condition from Step 2 is thus not merely necessary among masters with \(2m+1\) zeros and \(m+1\) ones: by Steps 3 and 4, it is **sufficient** for full coverage of the golden-mean target family. This finishes the proof.

## Verification

Run `python3 verify.py` from the directory containing this file. The standalone checker enumerates, for each \(1\le k\le12\), all binary words with the exact two letter counts required at minimum length, without pre-imposing avoidance of `11`; it directly checks coverage of every length-\(k\) `11`-avoiding target and separately checks all single-one targets. Both independent predicates return exactly the claimed shortest hosts. It examines \(36{,}940\) candidate hosts in these tests. It also verifies every stated construction directly against all targets for \(13\le k\le20\). The included `verification_output.txt` was produced by running the included checker.

The program is finite corroboration, not a proof for unbounded \(m\); Steps 1–4 supply the general proof.

## Relationship to prior work

Adamson, Fleischmann, Huch, Koß, Manea and Nowotka study ordinary full-alphabet subsequence universality in regular languages and automata-based decision/counting methods. Their 2023 work requires *all* binary length-\(k\) patterns, not only those avoiding contiguous `11`, and does not give the present odd-length optimizer classification. Lagoutte and Tavenas study hardness of shortest common supersequences with constrained input strings (including an explicit different binary three-letter target family); their results do not enumerate the masters of the present complete golden-mean family.

An earlier exact-length result for run-capped binary subsequence masters gives \(2k-\lfloor k/(r+1)\rfloor\) for targets avoiding \(1^{r+1}\), and singles out the divisible-length unique master. Its specialization \(r=1\) already gives the length \(3m+2\) and even-length uniqueness. Neither statement determines how many optimum masters exist at odd target lengths, their exact list, or why an unrestricted optimal host must avoid `11`. Those are the contributions proved here. Published results on *contiguous-factor* universal cycles for the golden-mean language concern a different covering relation and have exponentially growing rather than linear host lengths.

## Limitations

This theorem concerns binary, fixed odd target length, the single forbidden contiguous factor `11`, and **scattered** containment. It neither classifies optimal hosts for longer forbidden runs nor gives a new formula for minimum length. The prior-work comparison cannot exclude unpublished or unindexed equivalent optimizer classifications. No independent mathematical audit has been performed.

## References

1. D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658, first posted 2023-11-17. https://arxiv.org/abs/2311.10658
2. A. Lagoutte and S. Tavenas, *The complexity of Shortest Common Supersequence for inputs with no identical consecutive letters*, arXiv:1309.0422, first posted 2013-09-02. https://arxiv.org/abs/1309.0422
3. Earlier exact-length statement for binary run-capped scattered-subsequence master words (unpublished mathematical record; no external bibliographic identifier). The present proof independently establishes the necessary length bound and claims novelty only for the odd-length optimizer classification.
