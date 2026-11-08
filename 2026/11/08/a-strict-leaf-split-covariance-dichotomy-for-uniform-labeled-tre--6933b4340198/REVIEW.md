# Scientific review: leaf count and edge-split profile in uniform labeled trees

## Correctness — PASS

The result is a complete exact covariance identity for every uniformly labeled tree order \(n\ge4\) and split size \(1\le k\le\lfloor n/2\rfloor\). A fixed split-event count follows from Cayley's formula, including the factor of two for balanced cuts. Conditional tree uniformity and uniform attachment endpoints give the exact conditional leaf expectation. The strict sign uses a proved all-size analytic comparison of two exponential expressions, not a numerical sample. The large-cut conditional limit follows from controlled power-series expansions. The standalone verifier exhaustively checked 280,392 trees through eight vertices and 11,014 exact comparisons, including rational sign checks through 150 vertices. Its finite sample is not mistaken for an infinite proof.

## Originality — PASS (qualified)

The nearest inspected primary sources were Janson's 2013 analysis of conditioned Galton–Watson fringe subtrees, including uniform labeled trees (arXiv:1312.1211, introduction, Examples 2.1–2.2 and degree-covariance derivation), and Fischer–Liebscher's 2015 deterministic phylogenetic leaf-set split analysis (arXiv:1510.07882, introduction, definitions, main theorem). The first provides general rooted fluctuation theory and the second treats a different split convention and deterministic extrema. Neither inspected result supplies the finite unrooted **vertex**-split leaf covariance or its complete strict sign classification. Relevant indexed comparisons covered exact terms, rooting equivalences and the effect of classical Cayley/Prüfer counts. This is best-knowledge originality, not priority certification. Meir–Moon's older rooted-cut paper was only bibliographically accessible and might conceal an implicit formula; general fringe-tree generating-function consequences remain residual risks.

## Value — PASS

Cut size describes how fragile a tree is to removing one edge, while leaves measure its branching structure. The theorem gives the full exact joint first-moment response of leafiness to every possible vertex-cut size, distinguishing the pendant class from all non-pendant classes without exceptional sizes. The uniform conditional deficit \(-1/(2e)\) when both pieces grow is an interpretable structural effect; it cannot be inferred merely from the two marginal averages. The model, quantities and all-parameter sign statement are natural and do not depend on an arbitrary small parameter slice.

## Limitations and closest literature

The claim is about covariance, not stochastic orders or tree fragmentation dynamics; it is restricted to Cayley trees and vertex-based edge splits. Broader classical enumeration and historic sources could contain an equivalent consequence. Sources: https://arxiv.org/pdf/1312.1211 ; https://arxiv.org/pdf/1510.07882 ; Meir–Moon (1970), DOI:10.1017/S1446788700006698 (full text not inspected).

Self-review: passed. Independent audit: not yet performed.
