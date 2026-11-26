---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Single-letter deletions characterize minimality by subsequence transitivity. A candidate with at least six runs contains the proper absent subsequence 10101. For two runs the embeddings of 0^p1^q have capacity corners (a,b+d) and (a+c,d); reversal handles 1^p0^q and gives the four missing corners after the single-letter cases. For 0^p1^q0^r, if p<=a or r<=e an embedding of the appropriate proper suffix or prefix extends to the whole word; hence both bounds must be exceeded. Decreasing either outside run and requiring an embedding forces p=a+1,r=e+1, and q>1 would preserve both obstructions after an interior deletion. With q=1 the merged-zero deletion needs c>=2. The pattern 1^p0^q1^r instead has box capacities b,c,d, so only one coordinate can exceed by one with the others equal to one. The zero deletion for the two excess-one-run cases requires d>=2 or b>=2; the excess-zero-run case always passes. For four runs beginning in zero the suffix forces capacities b,c,d, leaving only an excess first run a+1 with all other runs singleton; the internal deletions give c,d>=2. Reversal gives the other four-run case. The proper prefix and suffix of a five-run candidate starting in zero force all five capacities. Starting in one leaves only 10101, whose internal deletions require b,c,d>=2. These templates are distinct, and exactly their stated threshold conditions apply. For a fixed set of k satisfied thresholds there are 2+k free increments after a minimum length 5+k; its count is binom(n-4,k+1). The eight indicator patterns produce multiplicities 1,3,1,2,1 at K=7,8,9,10,13 respectively, giving the stated series, probabilities and leading deficit 40/n. Independent greedy-prefix and deletion-state enumeration in /workspace/branches/audit_word_obstructions.py matched complete antichains for all 1024 tuples in [1,4]^5. This supports, but is not the proof of, the symbolic result.

## originality

FAIL

A distinct indexed finding supplies precisely the full antichain, the seven unconditional and six conditional forms with the same necessary and sufficient conditions, and the identical cardinality law. The exact length distribution and mean are not quoted from that record, but are routine composition counts from its complete threshold formula. This establishes scientific coverage, not priority or provenance; the catalogue dates do not decide either.

## value

FAIL

The five-run symbolic antichain itself is a natural and useful low-run case, but it is already supplied in full by the indexed basis theorem. The proposed aggregate remainder concerns a reasonable statistic, yet follows mechanically from the already explicit three binary thresholds and stars and bars; it needs no new structural or computational result. No independently valuable uncovered claim warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
