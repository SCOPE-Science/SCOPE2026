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

# Reproduction and scope

The standalone Python 3 standard-library file `verify_steiner_graph.py` reconstructs the theta–Steiner incidence matrix from the standard six-coordinate quadratic refinement and builds the full integral Laplacian. Run `python3 verify_steiner_graph.py` in the extracted folder. The concluding success string is `STEINER_GRAPH_CRITICAL_GROUP_VERIFIED_OK`.

Every one of the \(28\times63\) entries is computed rather than looked up. The code verifies the full matrix identity \(BB^{\mathsf T}=16I+11J\), both vertex degree lists, the Laplacian row sums, the exact tree number, and two local Smith reductions for each prime dividing that number. The local algorithm operates using invertible row and column operations modulo \(p^e\), checks that all \(90\) pivots have valuations below the modulus precision, and independently checks ranks modulo \(p\). It then combines the local data, checks the integral invariant-factor chain and group order, and checks cycle rank \(666\).

The geometric identification uses standard classical theta theory; the code does not certify an arbitrary curve's smoothness or produce a Néron smoothing. Computed Smith factors are exact finite integer results, not a numerical experiment. Independent human or external audit has not been performed.
