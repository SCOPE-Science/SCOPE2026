---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The orthonormal Laguerre basis and Laplace inner products yield J_W(t)=4N_W(t)/P_W(t)^2 on the full t>=0 domain. Independent SymPy expansion verified exactly J_W(W-1)=(W+1)/W, J_W(t)-(W+1)/W=-(t-W+1)^2H_W(t)/(W P_W(t)^2), the derivative -8(t-W+1)Q_W(t)/P_W(t)^3, and discriminant 16W(W-3). At W=3, J-4/3=-4(t-2)^2(t-5)^2/[3(t^2-4t+16)^2], giving both global carrier levels. For W>3 the negative region of H is a bounded interval t>W and strict convexity of Q there gives a unique maximum. The high-frequency substitution Q_W(W+u)=W(2u^2-8u+2)+u^3+2u^2+u proves the 2+sqrt(3) branch. Constraints on equal amplitudes, phase and omega>=2a are essential.

## originality

PASS

A full accessible Hu–Yu paper treats scaled Laguerre spectral error and optimal scaling, not this fixed-scale two-mode single-carrier exact global rational minimax. Wang–Zhao–Zhao describes adaptive multiple carriers and error estimates but its full text was inaccessible; no equivalent exact switch found in Resultary. Best-of-knowledge PASS with this explicit priority risk.

## value

PASS

The discontinuous exact optimal-carrier switch at the simplest nontrivial two-tone, two-Laguerre-mode setup is a substantive boundary in frequency-adaptive spectral approximation, not a normalization exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
