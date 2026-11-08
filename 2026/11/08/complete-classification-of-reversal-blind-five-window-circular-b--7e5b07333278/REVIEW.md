# Self-review

## Correctness — PASS

The precise model quotients each five-bit cyclic window only by reversal, retaining its arc position as the target label. It permits one palindromic read but forbids two reads with the same reversal class. The upper bound of twenty possible classes is exact: eight palindromes and twelve two-element reversal orbits. This bounds all feasible circumferences by twenty. The state-graph recursion explores every binary outgoing edge from every one of sixteen four-bit start states unless its reversal class has already occurred; every valid cyclic word corresponds to a registered closed walk. The complete output contains exactly twenty necklaces at lengths six through ten and twelve; no other length from five through twenty occurs. A distinct full-indexed-word enumerator agrees. Pairwise mask intersections at each length rule out a two-identifier codebook. These are finite exhaustive proofs, not extrapolations. No external independent scientific certification is claimed.

## Originality — PASS, with historical-priority risk

The closest classical primary articles have genuinely different quantifiers. Grubman, Şekercioğlu and Wood (arXiv:1502.02199, §§1–2) require each **ordered** window to identify both an identifier and an orientation; §4.5 optionally relaxes positional identification, not reading-direction information. Burris, Motta and Shipman (arXiv:1608.08480, §§1–5) minimize the length of **linear** words that **cover** all reversal classes, allowing repeats; they do not enumerate **cyclic** walks that use each class at most once. The orientable-sequence tradition starting with Dai, Martin, Robshaw and Wild (1993) excludes palindromic windows to identify reading direction, unlike the position-only problem here. In contrast, the length-twelve witness has four palindromic windows.

The distinct claim is the complete twenty-necklace classification, sharp maximum period twelve, and complete same-length capacity zero/one for the reversal-blind position-only model. No checked exact table or stronger published result implied it. The 1993 paper was not available in complete text; possible historical overlap remains a specific residual risk and merits independent review. The assessment does not establish absolute priority from a failed search.

## Value — PASS

An unoriented five-bit sensor can localize a read to one marked arc without determining which end was read first; this setting occurs naturally when a circular marker can be viewed from either side or without a trusted direction. The exhaustive theorem determines every feasible ring size and *every* binary marker realizing positional identification, not merely one example. It identifies a strong structural collapse compared with the oriented five-window model: no two such markers can coexist at any fixed circumference, and the largest admissible circumference is twelve. Such a classification is a natural exact design limit, not an arbitrary subfamily count or an unmotivated computational slice.

## Closest literature, limitations and remaining risks

The published related material includes arXiv:1502.02199 (2015), *Orientable Sequences* (1993), arXiv:1608.08480 (2016), and modern orientable-sequence descriptions. The main residual risk is the full inaccessible historical orientable-sequence text; the accessible definitions nevertheless explicitly exclude palindromes. The result does not treat noise, larger alphabets, other window sizes, or orientation inference. The certificate is finite computation with an independently written second algorithm, not an externally performed audit.

Self-review: passed. Independent audit: not yet performed.
