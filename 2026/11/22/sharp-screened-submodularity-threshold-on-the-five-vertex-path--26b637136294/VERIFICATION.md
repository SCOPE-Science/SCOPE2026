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

# Exact verification

Execute `python3 verify.py` with Python 3.9 or later in the extracted directory. The script has no third-party dependencies. It computes \(\det(\mu I+L_S)/\mu\) for all 64 subsets of the six unit candidate edges of the five-vertex path via the complete 120-permutation determinant formula, and constructs every second-difference numerator with exact polynomial arithmetic.

Expected output:

```text
PASS: 64 determinant polynomials and 240 exhaustive elemental inequalities
PASS: 210 strictly positive shifted certificates, 29 identities, one quartic witness
PASS: quartic isolating interval (5/4,13/10), unscreened witness 3/70
```

The inequality \(F_\mu(S+e)+F_\mu(S+f)-F_\mu(S+e+f)-F_\mu(S)\ge0\) for distinct unchosen edges is checked for all 240 configurations. The program verifies exact nonnegative coefficient expansions in \(v=\mu-5/4\), not approximate signs of individual numerical evaluations. The exceptional polynomial factorization and the two exact rational endpoint values isolate the unique positive threshold. Together these are a finite exact proof for all real \(\mu\ge0\) within the stated graph family.

It does not test graphs of other sizes or continuous nonuniform edge weights. The cited source papers and publication priority are not mathematically certified by this program, and no independent audit has been performed.
