---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The centered iid displacements across pairs of runs oscillate in both directions, so every fixed level is hit. In the distance-to-target variable the drifts are -v and +v. Substituting the constant plus decaying mode with exponent sqrt(v^2+2Df)/D verifies the two backward equations and both target values. Bounded stopping identifies the solution; strong Markov at T_x then gives the spatial kernel, whose derivative is G_D. For the stated right-continuous modification one can use the finite-state chain with these finite-dimensional distributions. At any fixed level the Brownian component immediately crosses upward after first hitting, giving right continuity there almost surely. In the exponential coupling, the j-th start is the sum of the first j positive lengths, the preceding negative lengths and any initial negative length. It converges to the j-th rate-f/(2v) Poisson arrival, and its mark converges to an independent unit exponential. In fact a_D <= f/(2v) bounds every coupled start below in index by the corresponding limiting start in position, so only finitely many indices can ever enter a bounded window, and fixed boundaries have probability zero in the limit. This also proves the joint count-and-width statement, with full widths and no use of finite observation time. The frozen verify.py checks the backward equations on a grid (using the analytic asymptotic plus fraction at its far boundary), the matrix exponential, and finite rate scalings. It does not verify the point process and was not run; the proof is decisive.

## originality

FAIL

A distinct published Resultary entry gives the same spatial generator and the same full marked limit at positive initial sign. Setting q=f and changing marks from z=length/D to w=vz sends v exp(-vz) dz to exp(-w) dw and leaves the start rate unchanged. The other deterministic initial sign adds an independent Exp(b_D) delay that tends to zero and an excluded start at zero; it is not a distinct island-limit theorem. This is a failure to establish a distinct contribution against the current indexed evidence, not proof that the later-dated entry has chronological priority or that the frozen theorem is false.

## value

PASS

The marked process is a scientifically useful observable for completed first-visit deposition: on a fixed window the number of negative islands remains of order one even though their widths are of order D/v. Start intensity, width law and their limiting independence cannot be read off from the minority color fraction alone. This evaluates the significance of the island law, not the originality of re-stating it; the equivalent coverage prevents acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
