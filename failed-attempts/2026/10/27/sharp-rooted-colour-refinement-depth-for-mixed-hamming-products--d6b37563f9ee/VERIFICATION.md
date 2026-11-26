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

Let P_t be the round-t partition; the claimed depth is the first t with P_t=P_{t+1}. Regular degree and exactly h neighbours in layer h−1 give the frontier induction: at round t the entire layer t has one colour, the higher layers have a separate common colour, and earlier layers stay separated. At round two, the distance-one class splits by the within-layer neighbour count q−2. At distance h≥2, the multiset of deletion profiles contains j_q copies of j−e_q; summing gives (h−1)j, so it distinguishes every profile in round h+1 once the previous layer is resolved. The top layer has only one profile. Equal-size coordinate permutations and root-symbol-fixing alphabet permutations act transitively on each profile, so profiles cannot split and are exactly the eventual orbits. The frontier proves both lower bounds: in a homogeneous product the last two layers are still merged at round k−2 if k≥2, and in a mixed product the layer k−1 is monochromatic at round k−1 despite different profiles obtained by omitting different sizes. For k=1 the initial partition is already stable. The class cardinalities follow by choosing the changed coordinates and their nonroot symbols. The supplied code and its recorded output are consistent finite corroboration; no run was needed for this general proof.

## originality

FAIL

A distinct earlier Resultary record states the same sharp dichotomy, orbit partition, and enumeration, and in fact describes every intermediate partition. This is verified statement-level coverage of the asserted contribution, not a similarity hit or a shared date. The frozen text's acknowledgment of special cases does not resolve it.

## value

PASS

As a mathematical statement, the all-dimensions sharp one-root stabilization bound is useful: it identifies when the naturally marked product's refinement becomes orbit-exact, and separates the nonlinear refinement procedure from a smaller linear module. This assessment does not count the duplicate as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
