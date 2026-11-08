# Scientific review

**Correctness — PASS.** The three-gap reconstruction follows directly from comparing the full cyclic rotations and tracking the letter preceding each row. The three possible BWT one-marks yield a complete adjacency classification. Counting balanced, repeated, and distinct gap triples and applying the marked-position double count gives the stated distribution for every integer length at least four. The standalone verifier recomputes both transforms and finite counts by separate methods; its checks do not substitute for the all-length proof.

**Originality — PASS (qualified).** The classical two-run characterization by Mantaci and coauthors, as presented by Simpson and Puglisi (2008), already settles the two-run family and is not claimed. The contribution is the explicit full population of four- and six-run outcomes for fixed binary weight three, together with a sharp gap-order criterion. The Simpson–Puglisi paper develops two-run and multicategory-block structure; Giuliani et al. (2020) study reversal; Fici et al. (2023) study morphism operations. None of these inspected texts yields this conditional distribution. Exact-phrase, semantic, published-finding corpus and accessible-record checks returned no statement covering the same indexed-word counts. An unindexed equivalent or a broader enumerative theorem remains possible.

**Value — PASS.** BWT run count is a standard measure of compressibility and index size. A complete fixed-composition distribution distinguishes the exceptional compressible words from the generic maximum-run case and quantifies their decay: the four-run population is quadratic in word length while the entire population is cubic. This is an infinite, natural, fully classified sparse-content regime, not an isolated table entry.

The theorem applies only to circular BWTs and exactly three ones, not the BWT with a terminal sentinel or words of other weights. Independent review is still outstanding.

Self-review: passed. Independent audit: not yet performed.
