---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Pigeonhole two agents assigned to the same facility and use the triangle inequality to get OPT≥δ even off reports. Omitting one endpoint of a closest pair attains δ. If P is the product of all gaps, omitting an endpoint deletes its gap, and omitting an interior point merges its incident gaps, giving weights P/g and P(1/g_left+1/g_right). Every reciprocal occurs twice, so the normalization is 2PH. Multiplying by the actual omitted-agent cost gives the claimed expected cost. For q_j=δ/g_j, choose a maximizing q_s=1. Each adjacent ratio touching s equals the corresponding neighboring q; each other ratio is ≤1. With d=1 at an endpoint or d=2 in the interior and u the sum of neighboring q, the ratio is ≤(2k-d+u)/(2(1+u))<k-d/2. This includes ties and is strict for every finite positive-gap profile. With one unit gap and all others equal to L→∞, the ratios touching the unit gap tend to zero and the rest are 1, and the denominator tends to 2. Putting the unit gap at the appropriate index proves both suprema.

## originality

FAIL

An earlier catalogue result proves the exact omission weights, expected cost, unrestricted optimum and nonattained sharp k−1/2 bound in the same regime, for k≥2 rather than k≥3. Its proof already bounds the ratio by retaining the normalized contribution from a neighbor of a shortest gap and uses the same single-short-gap extremizing family. The conditional k−1 value is not explicitly stated there, but it follows immediately by keeping both neighbors of an interior shortest gap in those same inequalities and moving the shortest gap into the interior in the same family. There is no surviving distinct contribution beyond this direct specialization of the earlier argument.

## value

FAIL

The exact first-surplus guarantee would be useful in isolation, but is already known. On narrowing to what is not explicitly stated earlier, the one-unit improvement in the doubled numerator counts one additional neighbor of a shortest gap and leaves the same extremal family. The record does not establish a further structural theorem or an independently useful gap beyond that immediate boundary-versus-interior consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
