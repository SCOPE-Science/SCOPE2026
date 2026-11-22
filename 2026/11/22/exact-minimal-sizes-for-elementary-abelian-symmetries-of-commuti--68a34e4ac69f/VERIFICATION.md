---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof uses direct wreath-product group-set structure and the inequality \(p^d\geq pd\); no exhaustive computation is asserted as an all-rank proof. Reproduce representative checks with `python3 CHECK.py`; the script builds each claimed extremizer for primes \(2\), \(3\), and \(5\), tests commuting generators and braid identities on all triples, and brute-force computes full centralizers when there are at most eight points. Expected terminal marker: `COMMUTING_PERMUTATION_BRAID_CENTRALIZERS_OK`.

The general claim does not include arbitrary braid solutions. Historical-priority checking is finite and may miss previously unindexed equivalents. Independent mathematical audit has not been performed.
