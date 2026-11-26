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

One can select a uniformly random sampling label and rotate its angle out. The other n-1 angles are still iid uniform, and the order-statistic gap chart has constant density (n-1)!. On any gap, the nearest competitors are its two incident sites (the first sites along the two directions); this proves the midpoint rule even for a gap longer than a semicircle. Odd n: the geometric series for I+P gives the signed inverse with the stated factor; the cyclic map (I+P)/2 fixes the all-ones direction and has sum-zero determinant 2^(1-n). Positive inverse gaps sum to one and form an exact realization up to rotation. Even n: nullspace is the alternating vector, the two parity sums are 1/2, and recursion gives spacings affine in T=S_0. The alternating identity ensures the omitted closing equation, and positivity of every gap is exactly the open interval stated. The mixed coordinates (T,l_1,...,l_(n-2)) give a triangular change of variables with absolute determinant 2^(-(n-2)); its constant density on the feasible set gives both normalization and the uniform conditional law. Boundaries are null for the stated density convention. The covariance check follows by restricting the scalar Dirichlet covariance to the sum-zero subspace and multiplying by the squared Fourier multipliers. Independent replay: python3 /workspace/review_checks/voronoi.py computed exact chart determinants and parity/inverse checks through n=20; at n=4 it independently checks Delta=2 min_i l_i and integrates the resulting density 48 min_i l_i to 1 on the half-unit square. The frozen nested tools/verify.py was also inspected, not treated as a proof.

## originality

PASS

The Dirichlet spacing law, cyclic midpoint averaging and the general slice-volume principle are prior. The supported distinct finding is the parity-resolved, explicit inversion and chart-normalized finite joint law on the full clockwise cell vector, including its conditional inverse family. Neither local statistics nor the generic simplex law computes that particular inverse family and its endpoints in the inspected sources.

## value

PASS

All ordered cell lengths are a natural observable of a point pattern. The exact law and inverse distinguish full identifiability from a positive interval of unrecoverable gaps, and in the latter case quantify that uncertainty and the marginal density in the correct dimension. Unlike the projection principle alone, the normalized closed chart formula is directly usable for finite joint probabilities and feasible reconstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
