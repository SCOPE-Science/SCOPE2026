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

# Verification of the Rule 73 temporal-two zeta functions

`verify.py` reconstructs the local elementary Rule 73 truth table, the four- and sixteen-state directed graphs, all elementary directed cycles and every vertex-disjoint cycle selection, and independently obtains the exact determinants. It checks strong connectivity, cycles of coprime lengths, and the rational isolation intervals of the dominant positive roots. It then compares graph traces to exhaustive updates for cyclic rings of lengths 1 through 17. `verify_output.txt` is the captured standard output from the successful run.

`check_direct.py` is a separately written bit-level updater that uses only the three neighborhoods with output one; it compares exact traces inferred from the determinant polynomials with direct updates for *every* binary indexed configuration on rings of lengths 1 through 18, a total of 524,286 configurations. `direct_output.txt` contains the successful run output.

To reproduce, with Python 3 and no third-party libraries, execute `python3 verify.py` and `python3 check_direct.py` in a directory containing these files. Exact all-length validity is proven by the cyclic closed-walk correspondence and finite directed-cycle determinant identities. The bounded exhaustive check by itself does not prove the infinite statement.

No independent audit has been performed. Priority against unindexed literature remains uncertain.
