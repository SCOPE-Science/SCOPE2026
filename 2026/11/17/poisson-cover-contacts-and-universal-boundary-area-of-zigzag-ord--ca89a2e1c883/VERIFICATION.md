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

## Reproduction
Run `python3 CHECK.py` with standard Python 3. The exact integer ideal-state recurrence enumerates the whole distribution of the number of cover-adjacent pairs for all \(2\le n\le17\), independently checks Euler zigzag counts and mean one, and prints selected zero-contact probabilities and variances. No third-party packages or networks are required.

## Scientific verification
Exact face area: the induced metric of an equality coordinate pair multiplies the contracted coordinate measure by \(\sqrt2\). The divergence theorem yields respectively \(\sqrt2 nV\) cover area and \(2nV\) coordinate area. The spectral operator \(UD\) has eigenfunctions \(\sqrt2\sin((j+\tfrac12)\pi t)\), with top eigenvalue \(4/\pi^2\) and gap ratio \(1/9\). Replacing a chosen kernel with \(I\) is exact coordinate identification, not a numerical approximation. The factorial-moment proof makes the two limits explicit: first length \(n\to\infty\) at fixed separation, then separation \(h\to\infty\).

## Limits
No finite enumerations are asserted to prove convergence. Checks do not assess unseen literature or establish independent mathematical validation.
