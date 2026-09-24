# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/061`  
**Audit date (UTC):** 2026-09-24  
**Reviewer:** separate AI audit; not Lean verification or expert attestation.

## Source identity and claim

Audited source tree: `06a52daf0614ed67a52348285bb21a1df316206c`.  
Audited `RESULT.md` blob: `cb1651c405cd6574dda12d9dcd36e1ffe20abbd8`.

The record claims a complete linear-extension census for all unlabeled posets through n=8, complete incomparable-pair sorting probabilities, verification of the 1/3–2/3 property in that range, and extremal/witness data including a balance-1/3 witness.

## Correctness — PASS

I independently reconstructed the two headline posets from the listed cover relations and counted linear extensions by subset dynamic programming and by direct permutation enumeration.

For poset 8#14584 the independent count is `e(P)=9`. Its four incomparable pairs are `(1,2)`, `(2,3)`, `(5,6)`, `(6,7)`, and each orientation splits the nine extensions 6–3, so its balance constant is exactly 1/3.

For poset 8#558 the independent count is `e(P)=2520`; pair `(1,8)` splits 2484–36, giving the stated `1/70` smaller probability. The aggregate class counts used by the record agree with the standard unlabeled-poset counts. No correctness defect was found in the finite computation.

## Originality — FAIL

Fresh literature checking finds decisive prior coverage that the original audit missed.

Anish Gupta, *Balance Constants, Majority Cycles, and the Gold Partition Conjecture through Fourteen Elements*, arXiv:2607.23926v2 (July 2026), reports exact extremal balance data through 14 elements and explicitly states that orders 12 and 13 reproduce the earlier census of De Loof, De Baets, and De Meyer. The paper's earlier version also states that De Loof, De Baets, and De Meyer “computed all mutual rank probabilities and determined the worst balanced posets through order 13.” Its Theorem/Corollary framework establishes the 1/3 balance bound through 14, and the current abstract records exact classes attaining 1/3. Thus the record's n<=8 mutual-rank/balance census, its assertion that every non-chain in that range has a 1/3–2/3 pair, and its balance-extremal search are strictly inside a previously computed and published range.

The older source identified there is De Loof, De Baets, and De Meyer, *Counting linear extension majority cycles in partially ordered sets on up to 13 elements*, Comput. Math. Appl. 59 (2010), 1541–1547, DOI 10.1016/j.camwa.2009.12.021. Gupta also credits the all-pairs ideal-lattice recurrence to De Loof, De Meyer, and De Baets (Fund. Inform. 71 (2006), 309–321).

The record's explicit CSV may repackage data in a convenient form, but the mathematical headline about complete mutual-rank probabilities and worst balance through n=8 is already covered by the stronger prior census.

## Scientific value — FAIL after subtracting known coverage

Once the preexisting mutual-rank/balance census is removed, the surviving contribution is principally a repackaged small-order linear-extension table and replay scripts for n<=8. Those can be useful as software fixtures, but they do not constitute a substantial new scientific regime, theorem, algorithmic improvement, or frontier result relative to the prior exact census through 13 and the 2026 extension through 14. The record therefore fails the campaign's scientific-value standard even though the computations are correct.

## Repair attempt

A bounded repair was considered: narrow the record to an independently replayable n<=8 linear-extension dataset while explicitly crediting the prior mutual-rank census. That leaves a data-format/reproduction artifact rather than a scientifically substantial new result, so it does not rescue all three axes.

## Disposition

**FAILED.** Correctness passes, but originality and scientific value fail. The complete package should be preserved in the assigned failed-attempt destination.

## Access notes

The decisive Gupta paper was available in full through ordinary lawful open access/arXiv. Its text identifies the earlier De Loof literature and the exact overlap. No Oxford fallback was required.
