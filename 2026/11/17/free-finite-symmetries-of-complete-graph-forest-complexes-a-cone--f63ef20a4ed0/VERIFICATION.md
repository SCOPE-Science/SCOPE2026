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

The standalone script `verify.py` uses only the Python standard library. Run `python verify.py` in a directory containing the script; `verify.out` gives the actual recorded output. All groups and actions tested are constructed directly, all edge orbits are independently enumerated, and acyclicity is independently checked both in the lifted graph and in the coned multigraph with union-find.

The tests exhaustively examine 104557 face-orbit selections across regular actions of cyclic groups of orders 2, 3 and 4, the Klein four-group and the nonabelian symmetric group of order 6, in selected numbers of free orbits up to four. The script also checks the alternating weighted-forest formula against direct finite multigraph enumeration and several larger coefficient calculations. Final output: `FREE_GROUP_FOREST_CONE_EQUIVALENCE_PASS`.

The implementation deliberately tests only finite inputs. It cannot certify the asserted all-finite-groups theorem, shellability, PL homeomorphism, or novelty; those require the mathematical arguments in the accompanying result. The singleton zero-involution case is an empty realization rather than a conventional nonempty wedge.
