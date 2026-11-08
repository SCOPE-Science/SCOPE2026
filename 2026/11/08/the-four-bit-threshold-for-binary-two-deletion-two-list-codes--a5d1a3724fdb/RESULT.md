# The four-bit threshold for binary two-deletion two-list codes

## Finding
For a binary alphabet, define \(M_2(n)\) as the greatest size of a length-\(n\) code in which *each* received length-\(n-2\) word arises as a subsequence of at most two different codewords, where \(n\ge2\). Then
\[
M_2(8)=15,
\qquad
\min\{n\ge2:M_2(n)\ge16\}=9.
\]
Thus transmitting sixteen distinguishable messages with a list of at most two candidates after two arbitrary deletions requires exactly nine transmitted bits; eight are insufficient. This is a finite combinatorial theorem, proved by exact-arithmetic certificates and explicit words.

## Assumptions and scope
A code is a subset of \(\{0,1\}^n\), not a multiset. Deletions remove exactly two positions, possibly adjacent, retaining the order of remaining symbols. A received word is counted once per possible parent, regardless of how many deletion-position pairs yield it. A code is **two-list-decodable** if every received word has at most two distinct parents in the code. No probabilistic channel assumptions are needed. Only integers \(n\ge2\) are considered.

## Proof
**Incidence model.** Enumerate the \(256\) binary length-eight words in lexicographic order, indexed \(0,\ldots,255\), and the \(64\) length-six words, indexed \(0,\ldots,63\). Set \(A_{ij}=1\) when deleting two positions from source word \(j\) can produce output word \(i\), and \(0\) otherwise. For the selection indicator \(z_j\in\{0,1\}\), feasibility is exactly
\[
\sum_{j=0}^{255}A_{ij}z_j\le2\quad(0\le i<64).
\]
The accompanying certificate supplies a complete binary branching tree over the selection indicators. There are exactly \(199\) nodes and \(100\) leaves. Each internal node splits one previously unfixed indicator into the \(0\) and \(1\) branches. Every possible code therefore follows exactly one path to a leaf.

**Exact upper-bound leaves.** At a leaf, write \(F_1\) for indices fixed to one, \(F_0\) for those fixed to zero and \(J\) for free indices. Set \(b_i=2-\sum_{j\in F_1}A_{ij}\). Some leaves show an index \(i\) with \(b_i<0\); no feasible code belongs to these leaves. Every other leaf gives an explicitly listed vector \(y=(y_i)\) of nonnegative **rational** coefficients. With \(c_j=\sum_i y_i A_{ij}\), every feasible \(0\le z_j\le1\) at that leaf satisfies
\[
|C|=|F_1|+\sum_{j\in J}z_j
\le |F_1|+\sum_i b_i y_i
+\sum_{j\in J}\max\{0,1-c_j\}.
\]
This follows by multiplying each residual incidence inequality by \(y_i\), and bounding \((1-c_j)z_j\) above by \(\max(0,1-c_j)\). In all noncontradictory certificate leaves the right-hand side is **strictly less than sixteen**, verified with exact integer fractions. The standalone verifier enumerates all incidence entries independently from the deletion definition, checks completeness of the branching tree, and evaluates every displayed rational bound with exact arithmetic. Consequently \(M_2(8)\le15\), with no floating-point optimization assumption.

**Attainment at eight bits.** The following fifteen length-eight codewords form a two-list-decodable two-deletion code:

```text
00000000 00000111 00001000 00011111 00110110
01000011 01010010 01110011 10001100 10111100
11001001 11100000 11110111 11111000 11111111
```

Each length-six output is checked to have at most two distinct codeword parents. Hence \(M_2(8)=15\).

**Sixteen messages at nine bits.** The next sixteen length-nine words form a valid code:

```text
000000000 000000111 000001000 000011111
000110110 001000011 001010010 001110011
010001100 010111100 011001001 011100000
011110111 011111000 011111111 101001101
```

Their complete seven-bit output incidence is checked directly, so \(M_2(9)\ge16\).

**Why no shorter block works.** Prefixing a common fixed symbol to all codewords preserves the two-list two-deletion property: for any shared output \(v\) of the extended words, deleting its first symbol produces a common output of length two shorter than the original codeword, hence of length \(n-2\) from each original word. Thus \(M_2(n+1)\ge M_2(n)\) for all \(n\ge2\). Therefore if any blocklength below eight supported sixteen messages, so would length eight, contradicting \(M_2(8)=15\). Together with the nine-bit witness, this proves the asserted threshold.

## Verification
Run `python3 checker.py certificate.json` with Python 3's standard library. It regenerates all \(16{,}384\) binary incidence entries from the two-deletion definition, checks the complete branch-tree partition and all exact rational dual bounds, and checks every length-six or length-seven received word against the two explicit codes. (The incidence matrix has \(64\times256=16{,}384\) entries; actual ones are reconstructed, not presumed.) The certificate is an independently checkable finite proof object: its validity does not depend on trusting a solver's claimed optimality or termination log.

## Relationship to prior work
Guruswami and Håstad (2020) constructed large binary codes list-decodable from two deletions with list size two, emphasizing asymptotic redundancy, while Lin (2026) proved new asymptotic lower bounds for general list sizes and deletion counts. Both establish the relevance of this channel; neither inspected text states the exact length-eight value or the sixteen-message blocklength threshold. Earlier small-parameter computations and related error models are not assumed to settle this parameter. The certificate supplies the exact finite obstruction separately from asymptotic existence results.

## Limitations
This result is restricted to a binary alphabet, two deletions, list size two, and the particular first sixteen-message threshold; it does not provide an all-length formula, an efficient family of encoders or decoders, or uniqueness of the exhibited codes. Novelty is evaluated against inspected accessible literature; earlier unindexed finite tables remain a historical-priority risk. Independent mathematical review has not been performed.

## References
- Andrew D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650, first posted 2026-09-22, https://arxiv.org/abs/2609.26650.
- Venkatesan Guruswami and Johan Håstad, *Explicit two-deletion codes with redundancy matching the existential bound*, arXiv:2007.10592, first posted 2020-07-21, https://arxiv.org/abs/2007.10592.
