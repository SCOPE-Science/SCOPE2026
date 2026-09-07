# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents a former public SCOPE result that failed an independent
> live-literature originality revalidation. The proposed claim is not a validated
> SCOPE finding and must not be cited as one.

## Former record

- **Original record:** `SCOPE-20260907-011`
- **Failed-attempt record:** `SCOPE-FAIL-20260907-032`
- **Title:** Exact maximal Sidon census in Z_60: maximum size 7 with full dihedral classification
- **Domain:** Additive Combinatorics
- **Original round:** 2026-09-07-first-light-01
- **Original lane:** 28
- **Revalidated at:** 2026-09-07T14:34:19Z

## Claim reviewed

In Z_60 with Sidon = k(k+1)/2 sums distinct equivalently k(k-1) ordered differences distinct-nonzero, (a) exact maximum size is 7 with witness {0,1,3,7,12,20,38} and no Sidon 8-set exists, and (b) there are exactly 50092 rooted 7-sets / 7156 translation classes / 3578 dihedral classes with zero periodic/self-mirror classes.

## Decisive originality failure

Claim-level comparison: candidate Theorem (a) asserts in Z_60 with sums-distinct (k(k+1)/2 sums) equivalently differences-distinct (k(k-1) ordered nonzero differences) definition, max size is exactly 7 with witness {0,1,3,7,12,20,38} (28 sums, 42 diffs) and no 8-set. Buratti-Stinson defines (v,k)-MGR identically as k distinct residues mod v with all i!=j differences distinct (hence nonzero), proven equivalent to candidate weak-Sidon and by candidate Lemma 1 to sums-Sidon including 2-torsion. Quantifiers match universally over all 8-subsets of Z_60; parameter range is the single point v=60,k=8 inside the 58-62 block; exact constants match: need 56 distinct differences of 59 nonzero residues, counting bound k(k-1)+1=57<=60 allows 8 (Buratti Thm 1.1 v>=k^2-k+1). Buratti Theorem 2.3 plus Table 1, obtained by exhaustive backtracking for k<=11, states MGR(7)={v>=48} (so (60,7) exists) and MGR(8)={57} U {v>=63} with explicit row '58<=v<=62 does not exist' (so (60,8) does not exist). Proof/computation scope matches: exhaustive search deciding existence at those (v,k). Conclusion matches: max<=7 and >=7, i.e. exactly 7. Lower-bound witness is also not new: any optimal 7-mark Golomb ruler of length 25 yields a (60,7)-MGR by Lemma 2.1. Therefore subclaim (a) is substantively covered/implied by concrete 2020 prior art. Subclaim (b) census 50092 rooted / 7156 translation / 3578 dihedral with SHA-256 checksums was not found in inspected sources: Buratti Table 1 gives one example per small (v,k) and invokes Lemma 2.1 for v>=51 at k=7 rather than enumerating all (60,7)-MGRs; Gordon and OEIS give no such counts; targeted terminology searches (difference packing, OOC, modular Golomb enumeration) surfaced no 50092/7156/3578 tabulation. Census enumeration per se appears new, but it does not salvage originality of the headline maximality theorem as stated; record presents max-7 as new theorem with replayable log, which overlaps published tabulation. Hence overall FAIL/FLAG: maximum component requires disclosure and downgrade to census-only novelty.

## Nearest prior work found live

- [Buratti & Stinson - New Results on Modular Golomb Rulers, Optical Orthogonal Codes and Related Structures](https://arxiv.org/abs/2007.01908) — covers the claim. Directly decides the maximality subclaim (a): Theorem 2.3 gives MGR(8)={57} U {v>=63} so v=60 has no 8-set, and MGR(7)={v>=48} so v=60 has a 7-set; Table 1 explicitly lists '58<=v<=62, k=8, does not exist' by exhaustive backtracking search. Same objects (8-subsets of Z_60), same distinct-differences hypothesis, same constants (56 differences, counting bound 57<=60), same nonexistence conclusion. Candidate 534k-node DFS re-proves this published 2020 tabulation.
- [Buratti & Stinson publisher version - ARS MATHEMATICA CONTEMPORANEA](https://doi.org/10.26493/1855-3974.2374.9ff) — related context. Authoritative journal version of the same Buratti-Stinson tabulation (Ars Math. Contemp. 20, 2020, DOI 10.26493/1855-3974.2374.9ff). Confirms peer-reviewed status and 2020 priority date for the (60,8) nonexistence / (60,7) existence determination; does not add census enumeration beyond Table 1 single examples.
- [Gordon - Modular Golomb Rulers and Almost Difference Sets](https://arxiv.org/abs/2408.16721) — related context. Background equivalence: lambda=0 almost difference set = modular Golomb ruler = (v,k,1) difference packing (cf. Buratti Theorem 1.5). Investigates constructions from difference sets and octic residues; confirms terminology mapping but contains no Z_60 maximality table and no 50092/7156/3578 census, so does not cover candidate beyond definitional background.
- [OEIS A005282 - Mian-Chowla B2 sequence](https://oeis.org/A005282) — related context. Interval B2 / optimal Golomb ruler sequence (Mian-Chowla). Different problem: integer differences without modulo wrap-around and without 2-torsion distance-30 collision. Gives k<=8 counting intuition and k>=7 lower bound via classical rulers (e.g. length-25 7-mark ruler gives (v,7)-MGR for v>=51 by Lemma 2.1) but does not close 8-vs-7 at v=60 nor enumerate cyclic extremals.

## Recovery conditions

Do not republish the already-known maximal-size-seven claim. A new submission must isolate and independently validate a census-only theorem, disclose the Buratti-Stinson overlap, and recheck whether the counts or classification have appeared in the modular-Golomb-ruler literature.

## Priority caveat

This is not an award of academic priority; it is only a literature-overlap assessment on the documented live search and does not establish primacy, independence, or correctness.

The former result and its artifacts are preserved in this directory solely so that
future SCOPE topic selection can avoid repeating the same claim or can formulate a
genuinely distinct, explicitly sourced claim.
