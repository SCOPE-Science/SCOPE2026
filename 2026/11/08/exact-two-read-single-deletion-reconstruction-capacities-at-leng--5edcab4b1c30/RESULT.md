# Exact two-read single-deletion reconstruction capacities at lengths three and four

## Finding

Let \(q\ge 2\) be an integer and let \(\Sigma\) be a labeled alphabet of size \(q\). For a length-\(n\) word \(w\), write \(D(w)\) for the **set of distinct** length-\(n-1\) words obtainable by deleting exactly one symbol from \(w\). Define \(M_q(n)\) as the greatest cardinality of \(C\subseteq\Sigma^n\) such that, for every two distinct \(u,v\in C\),

\[
|D(u)\cap D(v)|\le 1.
\]

Equivalently, any two distinct deletion outputs of a transmitted codeword uniquely determine that codeword among the codewords, whenever two distinct outputs are available. Then, for every integer \(q\ge2\),

\[
\boxed{M_q(3)=\frac{q^2(q+1)}{2},\qquad M_q(4)=\frac{q^2(q^2+1)}{2}.}
\]

This result concerns two **distinct observed outputs**; it does not assert recovery from a single read, or from two identical copies of the same read.

## Assumptions and scope

Words are ordered and labeled; no quotient by permutations of positions or alphabet symbols is taken in the definition of code size. Deletion occurs at an arbitrary one of the \(n\) positions, and coincident results from different deletion positions are counted only once in \(D(w)\). A valid code excludes precisely the pairs of words having two or more different one-deletion outputs in common. The theorem covers every finite alphabet size \(q\ge2\) at block lengths three and four. The alphabet is otherwise unconstrained.

## Proof

**1. Alphabet-support separation.** Let \(\operatorname{supp}(w)\) be the set of symbols occurring in the word \(w\). For any two *different* outputs \(z,z'\in D(w)\),

\[
\operatorname{supp}(z)\cup\operatorname{supp}(z')=\operatorname{supp}(w).
\]

Indeed, a symbol that is absent from a one-deletion output must have appeared exactly once in the original word, and that unique occurrence must have been deleted. If the same symbol were absent from two outputs, both deletions would have to remove the same position, so the outputs would coincide, contrary to their being different. Now suppose \(u\ne v\) have two distinct common deletion outputs \(z,z'\). Taking their support union both as outputs of \(u\) and as outputs of \(v\) yields \(\operatorname{supp}(u)=\operatorname{supp}(v)\). Thus the confusability graph, in which two distinct words are joined when \(\lvert D(u)\cap D(v)\rvert\ge2\), has no edges between different **exact alphabet supports**.

**2. Canonical support graphs.** For \(1\le k\le n\), define \(G_{n,k}\) to have as vertices every length-\(n\) word whose symbol support is precisely \(\{0,1,\ldots,k-1\}\). Two distinct vertices are adjacent if they possess at least two distinct common one-deletion outputs. A relabeling of the \(k\) symbols is a graph isomorphism, so every support subset of size \(k\) contributes exactly \(\alpha(G_{n,k})\) codewords in an optimal code, where \(\alpha\) is the independence number. There are \(\binom qk\) possible supports, and no confusability edges cross between them. Consequently,

\[
M_q(n)=\sum_{k=1}^{\min(q,n)}\binom qk\alpha(G_{n,k}).
\]

This is an equality: independently choose an optimal independent set for every exact support subset.

**3. Complete small canonical certificates.** The following table supplies exact independence numbers. The \(\#V\) column counts all surjective words on \(k\) labels. The matching column reports the number of pairwise vertex-disjoint confusability edges in the supplied certificate; the independent-set column reports the number of pairwise nonadjacent vertices in its supplied certificate.

| \(n\) | \(k\) | \(\#V\) | Independent-set size | Disjoint matching edges | \(\alpha(G_{n,k})\) |
|---:|---:|---:|---:|---:|---:|
|3|1|1|1|0|1|
|3|2|6|4|2|4|
|3|3|6|3|3|3|
|4|1|1|1|0|1|
|4|2|14|8|6|8|
|4|3|36|18|18|18|
|4|4|24|12|12|12|

The literal witnesses are in `certificates.json`. The standard-library program `verify.py` reads these witnesses, reconstructs all vertices and deletion sets from the definitions, and checks (i) each listed independent set has no internal edge, (ii) every listed matching pair really is an edge, (iii) different matching edges have disjoint endpoints, and (iv) in every row the independent-set size plus matching-edge count equals the vertex count. Such a matching proves the **upper** bound \(\alpha(G_{n,k})\le\#V-|M|\), since an independent set can use at most one endpoint of each matching edge. The supplied independent set proves the equal **lower** bound. No optimizer, untrusted solver output, or unexplained enumeration is required to verify any row.

**4. Assemble all alphabet sizes.** Substituting the proven seven independence numbers gives

\[
\begin{aligned}
M_q(3)&=\binom q1+4\binom q2+3\binom q3=\frac{q^2(q+1)}2,\\
M_q(4)&=\binom q1+8\binom q2+18\binom q3+12\binom q4=\frac{q^2(q^2+1)}2.
\end{aligned}
\]

Here binomial coefficients are interpreted as zero for \(k>q\). These identities hold for all integer \(q\ge2\), completing the proof.

## Verification

From the directory containing the accompanying files, run:

```bash
python3 verify.py certificates.json
```

The checker relies only on the Python standard library, enumerates each small canonical support graph from the channel definition, independently validates the two complementary certificates for each of the seven cases, and checks the resulting algebraic expressions numerically for alphabet sizes from two through forty-nine. It additionally checks the support-separation property directly for every pair of ternary words of lengths three and four. The expected final line begins `VERIFY_OK`. The complete finite certificate, rather than the sample numerical checks, proves the all-alphabet result in conjunction with the support-separation lemma.

## Relationship to prior work

The adversarial multiread reconstruction model was studied in the literature on sequence reconstruction from insertion and deletion traces, including Sala, Gabrys, Schoeny and Dolecek (2016), and the later deletion-specific reconstruction code work of Cai and coauthors (2020). Those investigations provide motivation, general characterizations and asymptotic constructions; they do not state the two all-alphabet finite-length optima above in the inspected material. A related published analysis of the same two-read single-deletion confusability graph computes its **number of edges**, but an edge-count formula does not determine an independence number or optimal code size. Standard one-read single-deletion-correcting codes impose the strictly stronger requirement of no shared deletion output and are not covered by these capacity formulas. The special matching-and-independent-set certificates identify the missing extremal data in these short cases.

## Limitations

The theorem establishes the exact capacity only at lengths three and four. It makes no assertion that analogous closed forms hold at higher lengths, or that every received word admits two distinct outputs. The historical novelty search includes relevant accessible full-text material, published-record searches and known nearby constructions, but cannot rule out unindexed equivalent statements. Independent validation by a separate expert has not been performed.

## References

1. F. Sala, R. Gabrys, C. Schoeny and L. Dolecek, *Exact Reconstruction from Insertions in Synchronization Codes*, arXiv:1604.03000, first posted 2016-04-11. <https://arxiv.org/abs/1604.03000>.
2. K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376 (2020), <https://arxiv.org/abs/2001.01376>.
3. J. Chrisnata, H. M. Kiah and E. Yaakobi, *Optimal Reconstruction Codes for Deletion Channels*, arXiv:2004.06032 (2020), <https://arxiv.org/abs/2004.06032>.
4. Related published result: *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, published research record <https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91>.
