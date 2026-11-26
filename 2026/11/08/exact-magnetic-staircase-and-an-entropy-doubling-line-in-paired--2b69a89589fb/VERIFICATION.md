---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Writing k for the number of opposite-spin pairs gives H/J=2s²−n+(K/J−1)(n−2k)−2(h/J)s, because the all-edge interaction depends only on total magnetization 2s. The constraints on pair counts give exactly k=0 or 1 through n−|s| in steps of two, according to the parity of n−|s|. The sign of K−J thus selects the minimum or maximum feasible k, and all k tie at equality. Choosing the pair types and opposite-pair orientations gives every stated multiplicity. Forward sector differences divided by 2J are t_s−t; for 0<K<J the consecutive threshold gaps alternate between 2K/J and 4−2K/J, both positive, and for K≥J the gap is 2. At K=0 the gap of the first type vanishes, giving exactly the listed triple transitions, including s=−1,0,1 at zero field for odd n. Spin reversal supplies all other signed cases. At fixed unscaled couplings and field, |s| is bounded uniformly in n, so the sector counts have exponential rates n log 2 off K=J and 2n log 2 on it; summing the at most three coexisting sectors preserves the rate.

## originality

PASS

The supported distinct claim is the exact ground-sector classification of the deterministic matching deformation for all couplings and fields in scope, with the triple crossings and residual entropy contrast. The unperturbed complete-graph case is routine and not credited separately. Related exact solutions use different graphs, interaction signs, or spin spaces and do not give this matching deformation.

## value

PASS

The perturbation continuously connects two standard highly symmetric graph models, rather than selecting an arbitrary field grid. It separates which types of configurations carry the residual entropy: essentially aligned pairs below equal coupling, opposite pairs above it, and both kinds available without a matching-energy penalty on the equality line. The exact field transitions, triple degeneracies at the deleted matching, and quantitative entropy contrast give a usable zero-temperature benchmark across the deformation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
