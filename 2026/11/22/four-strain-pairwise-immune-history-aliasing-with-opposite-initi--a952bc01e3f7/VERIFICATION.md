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

The normalized derivative of the positive pooled target compartment follows by summing the frozen linear-in-target equations: it depends on the susceptible history distribution only through its response mean. Inclusion–exclusion with the triple mass t yields exactly four odd cells of mass t and four even cells of mass 1/4−t; no other constraints besides 0≤t≤1/4 remain. The product response has slope −(1−c)^3, hence its range endpoints and width are sharp. An independent rational check verified the full pair tables, eligibility with strictly positive cells in both interior distributions, and the two opposite signed normalized derivatives in the frozen example. The comparison keeps the model parameters, susceptible total, and seeded compartment identical. With at most two prior labels all cells are fixed by the given moments, so no smaller case can exhibit this ambiguity. The general moment test is also correct: lower-order observed moments span the corresponding monomials, and uniform even/odd laws on any higher-order support with a nonzero Möbius coefficient agree on all strictly lower inclusion moments while differing on the top moment. This proves the iff for all distributions, not for every individual feasible fiber.

## originality

PASS

The fair three-bit fiber and moment-span test are not independent novelty: the former is a specialization of known fixed-margin table geometry, and the latter is classical linear algebra. The supported distinct claim is the sharp model-specific minimum for a hidden sign reversal at matched admissible states, including positivity and the specified product response. The strongest inspected analogues do not establish that model-specific conclusion.

## value

PASS

The model-specific result shows that pairwise data cannot in general even certify the direction of initial change, despite a separable per-history response and absence of zero susceptible cells. The small sharp boundary identifies when complete pairwise observation does and does not suffice. It is an identifiability warning for interpreting model summaries, not a claim about actual spread or a recommendation to change it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
