# Scientific assessment

## Correctness — PASS

The proof identifies the four shortest factor spans required to reach one through four ones, so there is no unexamined substring type. The variables \((m,p,q,r)\) form a bijection with the possible one-sided profiles at fixed length. Every boundary case in the count of ordered internal gaps is treated separately; the exterior slack contributes exactly \(r+1\). The squared-class generating function is obtained from disjoint geometric sums, not guessed from coefficients. Finite direct sliding-window checks through length \(22\) and symbolic integer-coordinate checks through length \(200\) agree, without being substituted for the proof.

## Originality — PASS (historically qualified)

Fici and Lipták establish the definition of prefix-normal forms and display finite unrestricted-size tables (2011). Burcsi et al. calculate the weight-four **number of prefix-normal representatives** (2016); that is only the number of classes, not the cardinality distribution of their inverse images. Balister and Gerke investigate the largest class across all Hamming weights (2019), not the exact weight-four extremal value or complete fibers. OEIS A238110 contains unrestricted maxima and does not imply the weight-four spectrum. Searches of available published findings and relevant historical claims found no equal or stronger all-length one-sided weight-four fiber theorem. An unindexed equivalent cannot be excluded.

## Value — PASS

The source literature singles out prefix normal forms as a canonical jumbled-matching index, and asks about the size of its equivalence classes. This theorem supplies the full ambiguity distribution in a natural fixed-composition family, including an exact second moment, a unique extremal normal form and a sharp random-collision constant. Those facts do not follow from knowing the previously published count of the number of forms and are usable for quantitative reconstruction ambiguity in sparse strings.

## Limits and closest literature

The observation is strictly one-sided. Agreement on full factor-Parikh sets requires both the maximum-one and minimum-one profiles; no result about the latter is claimed. The closest sources are Fici–Lipták (2011), Burcsi et al. (2014, 2016), Balister–Gerke (2019) and OEIS A238110. The historical-priority risk is incomplete coverage of unindexed documents; no stronger covering theorem was located in the inspected materials.

Self-review: passed. Independent audit: not yet performed.
