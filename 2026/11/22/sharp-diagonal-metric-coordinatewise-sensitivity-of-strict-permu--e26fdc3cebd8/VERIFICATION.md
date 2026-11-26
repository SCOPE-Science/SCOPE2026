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

Rearrangement forces the consecutive-value groups of every ordered-partition face; distinct generating entries make the coordinate differences span the sum-zero tangent space of each block. Every subset is realizable as one block with all other coordinates singleton. If T is a face's tangent space, inputs mapping to its relative interior have the form z+W⁻¹v with z in the face and v in the corresponding normal cone. Since T and W⁻¹T⊥ are complementary (positivity of W), face and cone relative interiors give a full open affine cell. The face-affine equality-constrained minimizer on a block B is y_i−a_i(∑_{j∈B}y_j−γ_B)/∑_{j∈B}a_j; the absolute row sum is 1+(|B|−2)a_i/∑_B a_j for |B|≥2 (zero for singleton blocks). The closed cells cover all inputs by the projection optimality condition, so summing affine bounds along segments yields the global upper bound. A short coordinate-sign perturbation in an open maximizing cell attains it exactly. For each fixed block size one can replace the maximizing row weight by a global maximum A and take the remaining smallest weights; ties do not affect the result. The full block gives the lower metric bound 2−2/n with equality requiring equal weights; the supremum n−1 is approached by divergence of one inverse weight, but all denominators strictly exceed A. For the proper-face example the candidates are 1+100/102, 303/103 and 503/203. Independently reconstructed two exact KKT witnesses and obtained 303/103: python3 /workspace/reproductions/check_frozen_math.py 5. No uploaded checker was executed.

## originality

PASS

The supported distinct claim is the exact unweighted coordinate-input/output norm for anisotropic quadratic projection: the prefix maximum over possible active blocks, finite attainment, and proper-face distinction. Standard face geometry and projection algorithms supply ingredients, not the sharp maximization in available statements. Neither the self-hit nor the distinct log-KL record establishes prior coverage. Exact primary passages on some of the known methods were inaccessible, so this is a bounded assessment.

## value

PASS

The exact coordinate amplification is useful when diagonal losses give differently scaled coordinate penalties but the error budget is per-coordinate. A proper face can defeat the natural prediction from the full affine hull; the formula identifies which subset carries the worst error without enumerating all faces, and quantifies how much the weights matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
