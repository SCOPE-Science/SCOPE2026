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

# Verification and reproducibility

Both attached programs use only the Python 3 standard library and exact integer operations. Run `python verify/period3_census.py` and compare its JSON output byte for byte with `verify/period3_census_output.json`; run `python verify/direct_reversible_simulation.py` and compare with `verify/direct_reversible_simulation_output.json`. The first program checks all 256 de Bruijn graphs, every strongly connected component, the precise 129/116/11 partition, every one of the 252 integer spectral gaps at exponent 56, the exact sixteen-node characteristic polynomials for Rules 50 and 76, and selected third-iterate fixed counts. The second directly constructs the reversible evolution and checks every pair state for all 256 rules and four ring lengths, 3 through 6, against the transfer enumeration. The digest for that complete array is `8b3dd0c8f39afe4fa27d5682c028881e732c0a3f761d8481be4a33301fa4ca4d`.

The correctness proof of the all-length result is the finite-state trace identity plus exact integer certificates and standard Perron bounds. Small-ring simulations serve as independent checks, not an infinite proof. The 1989 and 2024 related full papers could not be reviewed; originality remains subject to historical verification. External independent audit has not been performed.
