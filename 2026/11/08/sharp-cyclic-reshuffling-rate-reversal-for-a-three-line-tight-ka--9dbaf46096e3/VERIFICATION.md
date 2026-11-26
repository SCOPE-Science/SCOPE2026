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

Reconstructed the sweep in the basis with change-of-coordinates diag(1,sqrt(3)), where 64 times the sweep has entries 64-96w+24w²+8w³, -24w², 8w²-8w³, 64-96w+24w² in row-major order. Integer polynomial multiplication with metric diag(1,3) reproduces the trace, determinant, discriminant and squared Frobenius norm in the proof. Below the positive discriminant zero the squared radius decreases as (1-w)^3; from that zero to 6/5 the trace is negative and strictly decreasing, and above 6/5 the absolute determinant exceeds the proposed minimum. Orthogonal conjugacy of all orders and invariance under rotation by pi/3 make the fresh-permutation second moment scalar, and independence allows iteration. The independent-row factor and strict difference follow by the tight-frame identity and expansion. The reshuffling derivative changes sign once below 1 and is positive above it (the minimum of w^5/(w-1)^2 is at 5/3). Exact integer substitution brackets its zero between l=8388/10000 and h=8389/10000 and gives (1-h)^3+l^6/32>3/200. At the cyclic optimum the repeated negative eigenvalue and nilpotency give S=lambda I+N; the Frobenius identity gives ||N||=w_C^3/4. The one-epoch operator norm squared exceeds the trace average, and ||S^2||<0.0104<r_*. The Jordan norm formula and derivative bound on arsinh(k gamma) bound successive squared-norm ratios by c_*((k+1)/k)^2<r_* for k>=2. This proves the infinite-horizon assertion, not just the first tested powers. Inspected frozen verify.py, verification_output.txt and VERIFICATION.md as evidence, not as an independent replay. The matrix coefficients and rational inequalities above give a reproducible algebraic check without executing uploaded code.

## originality

PASS

Pass is for the strictly one-epoch versus every-later-epoch comparison between the fixed-order worst case and fresh reshuffling at separately optimized asymptotic relaxations. The same frame, independent-row law, cyclic spectral curve and characteristic transition are already covered; even the fresh-reshuffling scalar law follows readily from the earlier sweep matrix, conjugacy and independence. The older crossing compares a reused random order with IID at a common nonoptimal relaxation and an isotropic initial covariance. It does not give the separately optimized worst-case comparison or exclude all later crossings in the present setup.

## value

PASS

An exact benchmark compares equal work on a natural redundant tight frame while isolating the difference between an asymptotic spectral factor, finite-horizon operator norm and isotropic expected error. The defective cyclic optimum makes the strict crossover at exactly the first-to-second epoch meaningful; it is not a universal algorithm ranking or a new method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
