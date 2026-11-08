# Scientific review

## Correctness (C): PASS

The central \(10\) is unique, forcing a two-position attractor to cover it; the two \(01\) boundary occurrences then restrict a second marker to four possibilities whenever the middle run lengths are at least two. Pure-run maxima and the first/last boundary-factor inclusion test prove necessary and sufficient inequalities for each pair. A canonical three-position attractor and two explicit lower-bound regimes prove the global minimum-size formula even with singleton outer runs. The proof explicitly treats the subtle \(b=1\), \(c=1\) cases in the size formula, and the exact pair list is limited to \(a,b,c,d\ge2\). The included independent direct checker and mask-based census agree on 1,296 parameter quadruples and 625 complete nondegenerate pair lists. No finite calculation is used as proof of the unbounded claim.

## Originality (O): PASS, with remaining priority risk

The source that appeared on 2026-02-18 (https://arxiv.org/abs/2602.16152) counts and classifies smallest attractors for Fibonacci and period-doubling words, with a later extension to Thue–Morse; it does not enumerate optimal attractors of all four-run binary words. The 2019 study (https://ceur-ws.org/Vol-2504/paper8.pdf) and 2021 structural treatment (https://arpi.unipi.it/retrieve/e0d6c92f-ec13-fcf8-e053-d805fe0aa794/MRRRS_TCS2021.pdf) discuss the two-attractor classification problem and special word structures, but the inspected sections do not state or imply this four-parameter phase diagram. A previous exact classification of the periodic family \( (0^a1^b)^m \) covers the symmetric slice \(a=c,b=d,m=2\), but not the four-variable phase diagram or the unequal-run pair classification. Targeted phrase, equivalent-formulation, and mathematical-record searches found no theorem covering the full result. The absence of a matching search result is not a proof of historical originality; non-indexed, hard-to-access, or later-discovered equivalent statements remain a residual risk.

## Value (V): PASS

Characterizing the minimum attractor size of a binary word is a structural compression question. The four-run class is the first alternating-run stratum capable of requiring three positions; the theorem gives an exact phase transition across every positive four-run length quadruple. The four-candidate geometry classifies every size-two witness in the natural nondegenerate class and distinguishes genuine two-position rigidity from the two separate three-position obstructions. The result is an infinite natural classification, not an arbitrary finite cutoff or a generic algorithm implementation.

## Verification limits and closest literature

The exact numerical checks use independent occurrence scanning and factor-position masks; they do not establish an infinite theorem by enumeration. The nearest 2019/2021 structural sources and the 2026 morphic-word paper were compared by mathematical implications, not just titles. Complete global publication-priority adjudication and independent mathematical audit have not been performed.

Self-review: passed. Independent audit: not yet performed.
