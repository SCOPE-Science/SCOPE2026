# Independent three-axis audit — 2026-09-22

Review date (UTC): 2026-09-23. Reviewer: separate AI audit. Source tree: `02b46b770bbf86eb8d479505405bf08cf61c7a0d`, verified unchanged before review.

## Correctness

The central ceiling `gamma(G) <= floor((n+2)/4)` for striped maximal outerplanar graphs is consistent with the known striped bound of Campos–Wakabayashi. The record's exact solver/census data are internally coherent, and its attaining examples do establish sharpness for the checked sizes. The failure is not that the numerical maximum formula is false.

## Originality

The literature review in the accepted record is materially wrong. Wei Zhuang, *Domination and Outer Connected Domination in Maximal Outerplanar Graphs*, Graphs and Combinatorics 37 (2021), 2679–2696, DOI 10.1007/s00373-021-02383-w, states that Campos and Wakabayashi proved for striped maximal outerplanar graphs `gamma <= floor(n/4)` when `n ≡ 0,1 (mod 4)` and `gamma <= ceil(n/4)` otherwise, and Zhuang explicitly **characterizes all graphs achieving equality for this bound** and slightly improves the bound in further cases. The piecewise ceiling is exactly `floor((n+2)/4)`. Thus the record's claim that prior literature states neither per-`n` sharpness nor extremal geometry is contradicted by a directly on-topic 2021 paper.

## Scientific value

After accounting for the published sharp bound and equality characterization, the remaining contribution is a finite computational census through `n=20` plus one periodic witness family. Those data may be useful as supplementary enumeration, but they no longer support the accepted record's theorem-level novelty claim; the main extremal geometry has already been characterized in the literature. A repair would require reframing the record around a substantially different census-only contribution rather than a bounded correction to the accepted finding.

## Disposition

**FAILED.** Decisive originality failure; the accepted package should be withdrawn with its source preserved.
