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

# Verification and limits

The structural face decomposition and nullhomotopic cofiber attachment in `RESULT.md` form a proof for all integer parameters, with no reliance on finite experiments. The free graph-cycle lattices give the integral wedge types; explicit top-chain and loop arguments give split primitive map statements. The certificate `verify_starcut.py` independently enumerates the actual graph's disconnected induced triples and constructs the Alexander dual; a separate implementation constructs the claimed join model. Both face sets match exactly for all \(4\le a,b\le6\) and every \(0\le t\le b\) (54 finite instances). Complete binary boundary elimination agrees with all predicted Betti ranks. `verification_output.txt` records the actual program output.

Run `python3 verify_starcut.py` using Python 3.9 or later; it uses only the Python standard library. The checker verifies finite cases over \(\mathbb F_2\), not integral Smith forms or an unbounded parameter space. Those limitations do not substitute for the universal topological proof. The original three-cut complex is classified in integral homology and maps only; its full homotopy type and automorphism action are open here.
