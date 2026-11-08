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
# Verification methods and reproducibility

Run `python3 verify.py` in the directory containing `verify_output.txt`. No third-party libraries, downloads, or random seeds are needed.

The executable directly enumerates partitions, constructs edges by transferring a unit between rows, computes clique Euler characteristics of lower links, and compares each local increment against the claimed height-gap weight. This tests all 1,211 partitions through \(n=17\).

Separately, a formal-series state machine marks distinct cumulative multiplicities and internal gaps; through \(n=35\), its output matches independent direct partition enumeration on 81,155 partitions. The first 25 sphere-rank values also match the published numerical table. Coefficients through \(n=50\) are recorded in `verify_output.txt`, with the terminal marker `ALL_VERIFY_OK`.

The complete proof in `RESULT.md` establishes the theorem for every positive integer. The code checks finite instances and the arithmetic of the generating function; it does not certify an infinite assertion by enumeration. The theorem concerns integral homotopy type; no independent scientific audit has been performed.
