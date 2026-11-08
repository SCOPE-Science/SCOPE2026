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
# Verification record

The mathematical proof derives the sign pattern of the first-difference coefficient vector directly from log-concavity, then derives the global equality and index-by-index deficit by exact finite summation. Its claims cover every infinite full-support log-concave probability mass function, not only numerical examples. The Bessel reduction uses the series and adjacent probability ratios given in the reference.

A standalone standard-library Python script `verify_stein.py` was executed from the actual assembled scientific folder. It returned `PASS 21970 exact-rational and numeric diagnostic assertions`. The exact-rational tests enumerate all binary indicator sets on 59 finite log-concave test profiles, verify pointwise envelopes, global factors, deficit identities, and maximizer criteria; additional finite-prefix tests explore a concentrated family. The finite profiles are diagnostics only and do not prove the full-support universal statement or historical priority.

Reproduction: place `verify_stein.py` in the extracted folder and run `python3 verify_stein.py` using Python 3. No downloaded sources, network access, random seed, or external packages are required for this check. Independent assessment has not been performed.
