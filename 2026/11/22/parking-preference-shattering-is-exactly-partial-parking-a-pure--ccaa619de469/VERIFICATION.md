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
# Reproduction and limits

Run `python3 check_parking.py` with Python 3.8 or later, from the directory containing the included program. The program depends only on the standard library; expected output is in `check_output.txt`.

It enumerates all classical parking functions and all row-distinct query supports for sizes \(n=2,3,4,5\). For each support it independently obtains the collection of realized Boolean traces by checking every valid word, and compares this to the analytic shattering criterion. It also compares exact face-polynomial coefficients with the claimed closed formula. It separately enumerates all target lists for sizes through \(n=6\) to test the partial parking count, and verifies a family of matroid-exchange failures through \(n=8\).

These are genuine finite verification checks, not a computer proof for all \(n\). The all-parameter justification and the boundary conditions \(n=1,2\), \(s=0\), and \(s=n\) are in `RESULT.md`. No independent audit or external certification has been performed.
