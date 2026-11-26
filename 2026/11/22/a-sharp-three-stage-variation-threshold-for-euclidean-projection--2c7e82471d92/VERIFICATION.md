---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The claim is for unweighted cyclic variation, Euclidean projection, and positive radius. At a boundary point, write V as a maximum of signed edge sums. The tight sign vectors agree on nonzero edges and vary independently on zero edges, so their common equality space enforces constant values on the zero-edge blocks and one equation with normal g=QD^Ts. This gives the face derivative J=Q−ggᵀ/||g||²; the finite polyhedral projection cells yield the global bound by subdivision of a segment. Jensen applied to a cyclically ordered selection of one vertex per block gives V(Qv)≤V(v). Block j has g-value 0 or ±2/ℓ_j; therefore V(g)≤2Σ_j|g_j|=||g||², and |gᵀv|≤V(Qv). These give the bound 2. In the zero-sum difference hyperplane, every ℓ¹-unit vector is a convex combination of the normalized transfers (e_i−e_j)/2 by transporting positive to negative mass, with zero included by symmetry. These pull back to arc indicators modulo constants. I inspected verify_cycle_tv.py and independently enumerated exact integer face/arc ratios: for each nonconstant sign assignment up to reversal, scan the blocks between chosen boundary edges, take L=lcm(1,…,n), set q_j=L times the average of the arc on block j and d_j=L(s_before−s_after)/ℓ_j, and compute V in block order on q_j B−d_j A with denominator 2LB, where B=Σℓ_j d_j² and A=Σℓ_j d_j q_j. Face counts and maxima by r were (3,3)/(0,1), (6,12,7)/(0,1,1), and (10,30,35,15)/(0,1,4/3,3/2). The submitted certificate can be replayed as documented in VERIFICATION.md; no uploaded code was executed in this review. For the large-cycle witness the face normal is 2(e_1−e_4), and the perturbed arc indicator becomes (1,1/2,1,0,1/2,0,…), with cyclic variation 3 for n=5 and 4 for n≥6 versus input variation 2. Both projection residuals are positive multiples of the normal and all edge signs persist. Interior pairs attain 1; scaling verifies arbitrary τ>0.

## originality

PASS

The closest actual statements cover the path analogue, a penalized denoiser, or a different feasible set. None of the compared statements gives the cyclic two-input projector law, notably the five-cycle value and the delayed onset of 2. This is a best-of-current-knowledge conclusion, not absolute historical priority.

## value

PASS

A sharp two-input norm determines exactly when a standard periodic regularizer can amplify variation in a perturbation. The closing edge makes the path result unusable at the small sizes: the nonexpansive four-cycle, strict five-cycle intermediate constant, and uniform factor two thereafter give a complete and structurally explained transition, not merely a certificate at one arbitrary size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
