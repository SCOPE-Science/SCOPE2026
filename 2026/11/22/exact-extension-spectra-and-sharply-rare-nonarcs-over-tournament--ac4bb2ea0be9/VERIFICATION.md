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

# Verification and its limits

The proof in `RESULT.md` treats all finite tournament bases and all fixed new tuple arities. The companion `verify.py` is an independent finite diagram enumerator: it enumerates ternary statuses of every old-new and new-new pair with the old tournament fixed, rejects exactly the forbidden all-nonarc triples, and compares these counts with the weighted independent-set graph formula. For checked pairs \((n,r)\) satisfying \(nr+\binom r2\le12\), every ternary assignment was examined, including \((3,3)\), so those *finite cases* are exhaustive. It separately enumerates every triangle-free nonarc graph for \(1\le r\le5\), checks the leading weights and multiplicities, and reproduces the explicit formulas for \(r=1,2,3\). The real recorded standard output is `verification_output.txt`, ending `ALL_EXACT_ENUMERATION_CHECKS_OK`.

Run with `python3 verify.py`. No special external libraries, fetched datasets, pseudorandom choices, or private files are needed. The exhaustive computation does not prove the infinite-family or asymptotic results; those require the symbolic diagram decomposition, the two- and three-edge weight bound and the denominator comparison established in `RESULT.md`. A public-date-sensitive literature comparison was completed on the cited preprints and available thesis; this is not independent historical-priority certification.
