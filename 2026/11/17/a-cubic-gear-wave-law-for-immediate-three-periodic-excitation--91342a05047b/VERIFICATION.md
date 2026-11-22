---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Any nonrest configuration fixed by F³ on a connected graph must rotate all vertices through 0→1→2 modulo3; otherwise a resting vertex adjacent to rotating neighbor would be excited. A coloring c rotates iff every vertex has a neighbor of successor color. Fix hub color and use nine states (u_i,v_i); transition M enforces successor neighborhood at subdivision v_i and original rim u_{i+1}, and N removes closed walks with no u_i of successor hub color. Thus P_n=3(tr M^n−tr N^n), including all temporal phases. Independently reconstructed the exact 9×9 matrices from local indicators and computed charpolys x^4(x²+x+1)(x³−2x²−2x−1) and x^6(x+1)(x²−2x−1), yielding the claimed cubic/Pell traces and P_3…P_8=36,84,300,954,2940,8916. Dominant positive cubic root 2.831177… exceeds Pell root 1+√2, proving the asymptotic; 2n+1 vertices give fraction (λ/9)^n. Exhaustive n3..6 stored checks are supportive, matrix identity is infinite proof.

## originality

PASS

General graph excitation structural theorems and existing wheel/full-subdivision/open-ladder population counts are legitimate background, but each uses a different graph or statistic. The full-subdivision formula cannot be specialized to a gear retaining unsubdivided hub spokes; the un-subdivided wheel transfer has a different cubic. This gear all-n closed population is not a matching indexed prior table; originality provisional.

## value

PASS

Gear/Jahangir graphs form a natural partially subdivided wheel family, and immediate primitive period-three population is a concrete exact dynamical invariant. A nontrivial nine-state transfer collapses to a cubic law and sharp exponentially small prevalence, an independently useful classification distinct from general activity criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
