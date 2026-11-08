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

Run `python verify.py` and `python finite_models.py` with standard Python 3. The first program checks all nine canonical block probes, the 30 term-function closure, all 512 projected term kernels and the fixed-dimensional formula. Its exact observed output is `verify_output.txt`. The second program constructs actual subspaces, meets and joins over fields of orders two and three in ambient dimensions one through three, checks each of 26,405 ordered triples and compares the nine equation bits with the classical normal-form multiplicities; its exact output is `finite_models_output.txt`.

The proof of all-field validity uses D4 three-subspace decomposition, componentwise term evaluation, and explicit nine-probe separation. The programs are finite checks and do not replace that theorem. Marking all three generators and naming zero and unit are essential; arbitrary first-order types, unmarked lattice isomorphism and infinite-dimensional ambient spaces are outside the claim. Independent audit has not been performed.
