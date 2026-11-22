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

Run `python3 verify.py` with Python 3 (standard library only). It constructs normalized homogeneous point and line coordinates over fields of orders two and three, enumerates every subset of at most \(q\) incidence faults, recomputes shortest graph paths from independently determined undamaged witnesses, and checks the complete conical and connectedness preconditions. The resulting exhaustive counts are 232 configurations for order two and 23,479 for order three. In selected cases it enumerates every radius-two clique and simplex and recomputes mod-two chain ranks; the observed nonzero reduced Betti number is exactly \(q^3-t\) in degree two. These binary checks cannot prove integral torsion-freeness or a general all-order statement; those follow from the explicit natural suspension and graph-cycle-lattice proof in `RESULT.md`.

The independent audit channel has not been performed. In particular, no outside expert certification or independent validation is asserted.
