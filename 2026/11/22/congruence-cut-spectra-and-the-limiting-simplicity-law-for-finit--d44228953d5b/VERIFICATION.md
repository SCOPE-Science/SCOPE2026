---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The two lattice identities give antitonicity and isotonicity, which force the arrow to be top on ordered inputs and bound each descending arrow by each edge in its interval. Transitivity gives the reverse bound by the meet of those edges. Conversely the interval rule satisfies the four axioms for arbitrary edge values. Underlying Heyting congruences are the terminal collapses: identifying a<b forces a equivalent to top by comparing b→a and a→a. For a cut k, each edge above it has congruent inputs to the corresponding diagonal, so its output must be at least c_k. Conversely, on a first argument in the tail and second argument b<k, the value is the minimum of a fixed lower interval meet and a tail interval meet at least c_k; this is constant modulo the cut. All other cases are immediate from the same interval formula. The proposed choices s_j=n−1 for prescribed cuts and j−1 otherwise witness all exact sets. Counting edgewise under any required set T gives the product in (6), then indicator expansion and inclusion–exclusion verify both enumerators, with s_0 free (including n=2). For the limit, E_1 has probability (1−1/n)^{n−2}; for 2≤k≤n/2 the event E_k outside E_1 requires an earlier zero independent of the tested suffix, giving the summable bound (k−1)e^{−k/3}/n for large n. For k>n/2, put r=n−k and bound (r/n)^{r−1} by r·2^{−(r−2)}/n for r≥2. Thus the excess over E_1 is O(1/n). Independent direct quotient-table enumeration, replayed with python3 /workspace/independent_arithmetic_checks.py, matched the displayed polynomials for n=2 through 6. The supplied checker was inspected but not executed.

## originality

PASS

The supported new content is the exact surviving-cut distribution for all abstract arrows on the fixed Gödel chain, including all cut fibers and the uniform-model simplicity law. The already tabulated edge normal form and raw total are inputs. General congruence theory may streamline the individual compatibility criterion but does not provide the stated counting and asymptotic results in the passages inspected.

## value

PASS

Simplicity and preservation of congruences are intrinsic properties of the expanded algebra. Exact fibers distinguish which cuts survive, not just how many; every profile can occur and the uniform limiting simple fraction is strictly between zero and one. These answer natural classification and distribution questions not settled by counting raw arrows or their box reducts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
