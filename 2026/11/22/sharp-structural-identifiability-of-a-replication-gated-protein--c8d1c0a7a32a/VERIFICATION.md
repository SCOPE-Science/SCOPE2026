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

# Verification and exact limits

The result follows algebraically from the finite-sum Laplace transform of the defined birth/replication process. In particular, the pole at \(-\Lambda k\) has order \(\ell\), the distinct pole at \(-(k+\alpha)\) has order \(\ell+N-1\), and a coincident pole has order \(\ell+N\). The leading Laurent coefficients are explicitly nonzero on the amplified parameter domain; the one-stage swapped-rate difference has a strict finite-sum sign for every \(\ell\ge2\). These analytic verifications support arbitrary positive parameters and arbitrary finite positive integer thresholds and replication stages.

The standalone `check.py` was executed with Python 3 and SymPy, producing two `PASS` lines. It verifies 40 selected exact rational configurations; for each it tests the initial rate invariant and all pole multiplicities. It also confirms nine symbolic rate-swap polynomial identities, a concrete pair of indistinguishable one-protein FPT laws and their distinguishable two-protein FPT laws, and three independent finite-state absorbing-chain resolvents. Those finite checks are supplementary and do not prove completeness by themselves.

The reference article and a general phase-type identifiability review were read in available full text at the relevant model, theorem, and supplement sections. Related 2020 protein-hourglass and 2026 mRNA FPT articles were only accessible as summaries and remain literature-priority limitations. No inference from finite noisy measurements, protein degradation, or other gene regulation laws has been established.
