---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The primary source gives \(\omega=\arccos((N-4)/N)\) and \(F_N(2t)=\sin^4(\omega t/2)\). Unit fidelity at integer effective time requires \(\omega/\pi\in\mathbb Q\). Then \(2\cos\omega=2-8/N\) is both rational and an algebraic integer, hence one of \(-2,-1,0,1,2\); integer \(N\ge2\) yields exactly \(N=2,4,8\), with first physical times \(2,4,6\). For every other \(N\), irrational rotation makes \(t\omega\) dense modulo \(2\pi\), so the fidelity supremum is one but is never attained. The package verifier reconstructs the effective matrix and checks the source fidelity formula on a finite grid; those checks are supplementary to the all-size argument.

## originality

FAIL

FAIL on implication-level originality. The 2016 primary paper already gives the complete exact fidelity function for every integer \(N\) and every integer time. The submitted perfect-versus-pretty-good trichotomy is then a direct arithmetic corollary: apply the standard rational-angle algebraic-integer observation to the source's \(\cos\omega=(N-4)/N\), and irrational-rotation density to the same one-frequency formula. The source's prose overstates 'perfect' transfer for arbitrary \(N\), but the mathematical formula it publishes already dominates the final claim under the owner's corollary/implication rule. Chan–Zhan's later generic PGST theory independently confirms that discrete-time PGST is governed by spectral angle arithmetic.

## value

PASS

Despite originality failure, the exact classification is mathematically motivated and useful: it corrects a substantive exact-versus-'almost perfect' ambiguity in a published state-transfer example, identifies the complete exceptional set, and distinguishes unattained PGST from exact transfer. This is a natural boundary classification rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
