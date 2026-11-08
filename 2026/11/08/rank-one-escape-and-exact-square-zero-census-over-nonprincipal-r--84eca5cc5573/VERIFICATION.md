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

# Reproducing finite checks

Use Python 3 standard library only. Run `python verify.py` from the directory containing the files. A successful run finishes with the exact marker `VERIFY_OK`.

The standalone program independently enumerates every entry assignment to small matrices, squares each matrix using ring-specific addition and multiplication, and computes the residue-field rank by Gaussian elimination. The comparison formulas implement the Gaussian-binomial count independently of the enumeration and check every permitted reduction rank. Representative results include \(n=3\) over \(\mathbb Z/4\mathbb Z\) with counts (512,672), \(n=2\) over dual numbers of residue-field order two with (16,12), \(n=2\) over \(\mathbb Z/9\mathbb Z\) with (81,72), and \(n=2\) over the eight-element algebra \(\mathbb F_2[u,v]/(u,v)^2\) with (256,48), \(n=2\) over \(\mathbb F_3[u,v]/(u,v)^2\) with (6561,648), and \(n=2\) over \(\mathbb F_2[u,v,w]/(u,v,w)^2\) with (4096,192). It separately computes the rank of the anticommutator linear map in dimensions up to four for prime fields of sizes 2, 3, and 5, as a check on the critical kernel dimension.

These finite checks do not certify the all-n nonprincipal theorem or the rank-one escape asymptotic. The mathematical proof establishing those claims is contained in RESULT.md. Neither external independent audit nor external validation was performed.
