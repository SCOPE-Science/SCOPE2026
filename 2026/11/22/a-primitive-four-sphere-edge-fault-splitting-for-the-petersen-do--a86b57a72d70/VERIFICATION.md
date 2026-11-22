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

# Reproduction and proof limits

Run `python3 verify_petersen_dominance.py`. The script needs only Python 3 standard-library modules; it produces the exact complete face vectors, acyclic matching counts, directed Hasse-arrow counts, reduced mod-two Betti ranks, and fifteen-edge orbit test described in the mathematical result. Acyclic matching witnesses are generated deterministically, and the script topologically sorts the complete orientation rather than merely reporting matching sizes.

The augmented complexes include the empty simplex; its matching to a vertex produces one CW basepoint. Relative unmatched faces form a CW pair because the combined matching is acyclic and no pair crosses the subcomplex boundary. The model has seven dimension-four cells below and four additional dimension-four cells above. Since a wedge of four-spheres is three-connected, every additional three-sphere attaching map is nullhomotopic. Standard relative discrete-Morse and CW attaching arguments establish the integral homotopy splitting; binary matrix ranks are supporting checks, not a substitute for this proof.

No computation of more than one simultaneous edge deletion or of a broader Kneser family is claimed. Independent validation has not been performed.
