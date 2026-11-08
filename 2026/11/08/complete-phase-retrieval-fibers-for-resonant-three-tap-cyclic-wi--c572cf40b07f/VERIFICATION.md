---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

The algebraic proof in `RESULT.md` establishes the stated classification for every even \(N\ge6\) and all windows satisfying the endpoint-balance and circulant-invertibility hypotheses. The standalone checker `verify_chirp.py` computes exact group-ring intensity autocorrelations for the explicit windows \(g=(1,3,e^{2\pi i/N})\) and their two nonequivalent full-support signals. Running `python3 verify_chirp.py` outputs `CHIRPED_THREE_TAP_PASS dimensions=18 exact_correlation_rows=1242`.

The 18 tested orders and 1242 correlation entries are finite diagnostics, not a substitute for an infinite proof. No claim is made for zero-containing signals, unbalanced endpoint powers, singular zero-lag circulants, or incomplete frequency sampling. No independent audit has been carried out.
