---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Reconstructed all even and odd deck transforms of a(x,y)=(x+L,y), b(x,y)=(-x,y+H): twice the injectivity radius is min(L,2H,sqrt(H^2+dist(2x,LZ)^2)). Uniform x gives delta/H uniform on [0,q/2], hence M(q)=q^(-3/2) int_0^(q/2) min(q,2,sqrt(1+u^2)) du. Four integral branches cover every q>0; on (1,2/sqrt3) derivative has sign of Psi(q)=q^2-q sqrt(q^2-1)-3 arcosh(q), strictly decreasing from 1 through zero; other branches strictly decrease. Independent high-precision root/integral checks gave q*=1.03526637121326352489, M*=0.50278123528050473982 and M(1)=0.5, agreeing with package. No nonflat shapes are covered; numbers are corroboration, derivative proof supplies global uniqueness.

## originality

PASS

Best-of-knowledge distinct sharp mean-area-normalized injectivity-radius optimizer. The deck displacement / pointwise embedded disk expression is prior, and Sabourau already optimizes the SINGLE largest disk; separate Katz-Sabourau theorem optimizes the worst-case systolic length. The earlier flat Klein metric-radius result optimizes the minimax farthest-point distance, a different functional. None implies the mean optimizer without a new integration and global optimization; exact priority remains non-exhaustive.

## value

PASS

An intrinsic typical embedded-disk radius, averaged over the whole flat manifold and normalized by area, is a natural geometric invariant; the unique nonsquare optimizer differs from the square systolic optimizer throughout a complete one-dimensional moduli space. The numerical improvement is small but the change of extremal shape and strict equality theorem give substantive mathematical motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
