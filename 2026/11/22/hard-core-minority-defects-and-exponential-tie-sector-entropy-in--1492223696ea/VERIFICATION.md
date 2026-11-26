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

For histogram (L,L,r) with r<L, subtracting the deleted cyclic triple from the totals gives the open-neighbor votes. A boundary C of an adjacent C-run and the center of CAC or CBC have an opposite unique winner, ruling out distance one and two. At an isolated C an equal pair of leader neighbors also gives an opposite unique winner. Within each C-gap, any equal leader pair must be an internal doublet surrounded by the other leader: triples of the same leader and doublets abutting C are prohibited. Such an internal doublet is prohibited when L-r>=2 because a competing leader uniquely wins. When L-r=1, the total of 2r+2 leader sites leaves only two extra sites above two per gap, permitting at most one equal edge, whereas an even cyclic binary word has an even number of equal edges. Thus alternation is necessary in this boundary case as well. Conversely the allowed triples leave the incumbent either a winner or unchanged on a leading tie, including C when not a maximizing opinion. Marking a C gives n choices times the weak compositions of n-3r into r parts; divide by r and multiply by six for naming the minority and alternating. The three-state cyclic trace encodes these same placements; parity projection keeps r congruent to n mod 2 and the subtractions remove the empty packing for even n and the three perfect packings for 3|n. The trace is the sum of eigenvalue powers. For z=1 the other two roots are conjugate of modulus lambda^(-1/2)<0.827 (lambda>1.465). For z=-1 the real root is -u with u^3+u^2=1, 0.7548776<u<0.7548777, so the conjugate pair has modulus u^(-1/2)<1.151. These bounds prove the stated error and eventual positivity for the entropy limit (B_6=0 is immaterial). Fresh exact enumeration counted votes on the actual complement edges for n=5..12, yielding totals 30,0,42,72,54,150,198,252; an independent trace recurrence matched the spacing counts for n=5..100. The all-n conclusion uses the proof, not these finite tests.

## originality

PASS

The standard hard-core placement enumeration and transfer calculation are not themselves claimed as new. The supported distinct result is the exact dynamical equivalence of that model, with an alternating leader background, to the positive-minority tied-leader sector on the cycle complement; it also yields the stated labelled count and sector entropy.

## value

PASS

The two-leader tie is precisely where a nonmaximizing minority can persist under this update. The exact structure, including the boundary where locally permitted doublets are excluded only by cyclic parity, explains how that persistence leads to a positive, computable aggregate entropy. This is a natural all-length sector and not an arbitrary finite sample or merely a count of arrangements imposed in advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
