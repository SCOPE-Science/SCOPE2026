# Scientific review: cyclic burning-sequence source-slide graphs

## Correctness — PASS

For every integer \(k\ge2\), the state space is precisely the **ordered strict** optimal burning sequences, defined by the distance inequalities and covering union in Bonato–Janssen–Roshanbin's original paper (arXiv:1507.06524, §2). The radius-length sum is \(k^2\), forcing disjoint arc tilings when \(n=k^2\) and a single one-vertex overlap when \(n=k^2-1\). The proof checks that coverings with these overlap conditions satisfy the source-separation restrictions, establishes unique cyclic-order encodings (including the singleton radius-zero arc), classifies exactly two legal slides in the one-short case and proves that their directed orbit winds through \(kn\) distinct placements per cyclic label order. The \(k=2\) boundary is proved separately. Independent C++17 exhaustive state/move/component checking for \(2\le k\le5\) and Python set-based checking for \(2\le k\le4\) agree. These checks do not prove the infinite case; the tiling/winding argument does.

## Originality — PASS (qualified)

**Statement compared, not just keywords.** The original burning paper proves \(b(C_n)=\lceil\sqrt{n}\rceil\) and a general criterion for valid sequences; these are reused but do not determine all optimal cyclic schedules or their local source-slide graph. Nagao and Ogawa's full two-page 2022 public conference version, pp.25–26, defines BSRP by **swapping the order of a fixed set of source vertices**, restricted to path forests. Neither its move relation nor its graph family implies the present fixed-time adjacent source relocations on cycles. The 2024 ESA row-generation paper constructs optimal schedules but does not report this configuration graph in its inspected abstract and page metadata. Queries of the published mathematical finding index for exact objects, alternate terms, cyclic near-square schedule enumeration, and component geometry returned no covering result. An exact result could exist unindexed or inside inaccessible later full text; novelty is not certified as global uniqueness.

## Value — PASS

The result supplies an exact graph-isomorphism classification for a natural infinite family of optimal influence-spreading schedules. It identifies a sharp mobility transition under deletion of one vertex: all optima become isolated at the square threshold, whereas the one-short cycle admits only large cyclic orbits, with a single overlap defect moving through the ring. The count, component number, and component diameter provide meaningful benchmarks for reconfiguring source placements without changing ignition order, beyond the known scalar burning number. This is a structural classification, not a routine numeric increment or a name substitution.

## Verification and limits

Package files `check_reconfig.cpp` and `check_python_reconfig.py` implement separate exhaustive enumerations; execution outputs are included. They reproduce all asserted graph types in their finite ranges. A mathematical proof covers all \(k\ge2\). Scope excludes relaxed burning, changing the set by jumps, swapping source order, and other host graphs. The full 2025 Nagao–Ogawa chapter was not accessible during inspection; the publicly read 2022 version describes the distinct operation. Unindexed prior work remains a residual historical-priority risk. No independent scholarly audit has been undertaken.

Self-review: passed. Independent audit: not yet performed.
