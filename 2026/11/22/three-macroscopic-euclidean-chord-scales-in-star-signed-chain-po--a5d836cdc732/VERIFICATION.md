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

Between successive z-layer boundaries −1,0,1, each coordinate interval is an affine interpolation of its boundary intervals. Taking the same relative position in each interval gives a feasible endpoint-layer convex decomposition. The only layer vertices are the box corners, and these really are global vertices: the active hub and leaf bounds give full rank at ±1, and at zero the active e_i and e_i+e_z normals (up to signs) give full rank. For ordered pairs the per-leaf factors are 2+2q^4 at (0,0), 2+2q in the two equal nonzero types, and 1+2q+q^4 in each unequal type. The unequal types have ordered hub-gap weights 4q+2q^4. Subtract all 3·2^m diagonals and halve. Among all terms, the largest exponent is 4m+4 with ordered coefficient 2, and the next is 4m+1, with 4m contributions from the opposite nonzero hubs and 4 from the zero/nonzero hubs. Dividing each per-leaf factor by four yields conditional iid laws with means 2, 1/2, 3/2 and variances 4, 1/4, 9/4, respectively. The bounded hub gaps vanish on both scales. The conditional diagonal probability on either equal-hub class is 2^(−m), and it is zero on unequal classes, so both the mixture and the three CLTs survive removal of the diagonal. Independently enumerated exact active-facet intersections and all unordered chords for m=2,3; every coefficient agrees. The source checker was inspected, not executed: its loop to m=100 checks totals, zeros and top shell; the second-shell assertion itself is only in the loop through m=8. The symbolic shell proof covers all m.

## originality

PASS

The anchored polytope, vertex count, volume and diameter are background. No inspected source covers the evaluated full discrete vertex-pair spectrum, its second shell, and its three-scale limit and conditional Gaussian laws in the specified metric. Reasonable bounded searches do not settle global priority.

## value

PASS

The exact histogram recovers a finite metric statistic not visible in the face vector, continuous covariance or diameter, and shows that uniform vertices do not concentrate at one normalized pair distance even as m grows. The three masses, type fluctuations and exact multiplicity of near-diameter pairs make this a useful benchmark contrasting discrete vertex geometry with interior geometry on a naturally defined polytope family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
