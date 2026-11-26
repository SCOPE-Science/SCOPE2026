---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For odd N, the core unanimously follows the initial majority M. A peripheral vertex follows the core's prevailing sign when 2X<c-1 or 2X>c+1 and keeps its own bit otherwise. In the keep-bit regime moving the c core bits to M cannot reverse the original majority. Hence c>ell rules out reversal, and for ell>c the low-core/high-total event is X<=floor((c-2)/2), X+Y> N/2, with its complementary counterpart. The joint binomial CLT gives correlation sqrt(c/N); the exceptional at-most-two core counts have probability O(c^(-1/2)), and the Gaussian angular measure gives arccos(1/sqrt(1+rho))/pi for finite rho>=1. One quarter is a limit, not a finite-system equality. The independent replay `python3 /workspace/reproduce.py` exhaustively checked 114408 labeled profiles and verified the (10,11) example separately. That computation does not prove the limit.

## originality

FAIL

The headline quarter boundary and the whole finite-ratio limit are already elementary consequences of the exact one-round open-neighborhood map in the distinct published complete-split-graph attractor record: identical at every even core size, differing only on two central X values at odd core sizes. The zero branch and even-core exact finite law also follow from that map. The odd-core finite tie-threshold adjustment is real and is not asserted to be already in the source; it does not establish originality of the advertised boundary. This is demonstrable implication, not an inference about chronological priority from a same-day listing.

## value

PASS

As a mathematical question, the exact probability of a one-step global reversal and its response to transferring one vertex between the classes are meaningful for a natural two-tier voting model. The quarter-versus-zero limit explains topology sensitivity, but is covered as assessed above; isolating the finite odd-core tie adjustment alone would not retain that motivation as a distinct boundary theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
