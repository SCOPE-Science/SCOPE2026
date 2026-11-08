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

The proof in `RESULT.md` establishes the complete universal law. The crucial equalities are: (i) two crossed edges in each horizontal base face until the largest antipodal projection is passed, (ii) exactly two additional vertical crossings per projection pair below the threshold, (iii) the exact transform \(F_h(r)=r/\sqrt{h^2+r^2}\), (iv) the closed regular-hexagon trigonometric integrations, and (v) the sign of the derivative of the octagon probability.

Run `python geometry_hex_prism_check.py` in an environment satisfying `requirements.txt`. A fixed seed draws 350,000 unit normals for each of fifteen prism configurations (regular hexagon, regular octagon, and a nonregular centrally symmetric hexagon; five positive half-heights each). The program directly counts crossed edges and compares them directionwise to the independent projection-order formula, numerically integrates over 30,000 azimuths, verifies three analytical regular-hexagon probabilities, checks aspect-ratio recovery, and compares the octagon optimum with nearby heights. The expected success marker is `PRISM_CENTRAL_SECTION_OK`.

A Monte Carlo experiment cannot certify the theorem for every normal, every prism, or every height. No external independent audit or certification was performed. The exact statements rest on the finite combinatorial edge-classification proof and calculus in `RESULT.md`.
