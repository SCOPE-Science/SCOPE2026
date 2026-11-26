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

A shorter circle arc containing a grid site gives its length as the additive distance, and an arc in a grid gap gives an endpoint with sum at most 1/n. Thus for n≥3 the additive maximizing locus is exactly antipodality; each such point has a site with both coordinate distances positive, giving strict improvement for p>1 by compactness. The derivative of the ℓ_p norm at 1 is −(a+b)H(a/(a+b)); continuity of t^p log(t) through zero for p near 1 gives a uniform expansion near a+b=1/2. The optimizer has normal displacement δ=O(ε), because the short arc near antipodality contains a site and bounds F_1 by 1/2−|δ|. Select the site nearest each semicircle midpoint, a uniformly positive distance from the endpoints. For δ=εz, their affine coefficients are z−h_+ and −z−h_−, where h_±=H(1/2+2e_±)/2. Their minimum is at most −(h_++h_−)/2. At a minimizing phase this bound is attained to first order by z=(h_+−h_−)/2, since the other sites inside either arc have no larger entropy penalty. At the chosen odd phase x=−1/4 neither endpoint is a grid site; for even n, z=0 so endpoint sites keep distance 1/2. Even n gives e_+=e_− and maximizes both offsets at 1/(2n); odd n gives e_++e_−=1/(2n) and entropy concavity puts the minimum at the endpoints. Entropy Taylor expansion yields both size corrections. For n=2 the additive radius is at most 1/2 by averaging the two site distances, and (0,1/2) attains 1/2 for all p. Substituting n=3 gives the stated known coefficient. An independent 20,000-phase sample at each n=4,…,16 corroborated the reduced minimum only; the frozen script was inspected, not run.

## originality

PASS

Credit the three-site result and its first-variation method; the supported distinct claim is the sharp n≥4 fixed-diagonal classification and parity-dependent coefficients. The closest examined results do not resolve the general grid-phase minimum or the even/odd switch. This is a scoped conclusion from checked evidence, not a claim of exhaustive priority.

## value

PASS

The exact first-order radius for a natural prescribed torus design is useful beyond showing strict onset. In the odd case moving O(p−1) off the antipodal locus strictly improves the first-order optimum over restricting to that locus: the best purely antipodal penalty is H(1/2+1/(2n))/2, strictly above the mean of the two endpoint entropies divided by two by strict concavity. Even n instead requires no such displacement. This gives a concrete reason for the sharp distinction and its surviving finite-size correction without claiming optimal unconstrained placements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
