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

# Reproducibility and verification limits

Run `python3 verify.py` with Python 3. The code uses only the standard library and exact `fractions.Fraction` arithmetic. It checks that the permitted residue-class set has eight members; half-plane intersection produces the eight stated areas and their exact sum \(16/3\); the maximum of \(u+2v\) over the polygon collection is \(4\); and the resulting tail constant equals \(1/24\). It also directly maximizes the minimum of four rational sawtooth functions over all linearity cells for \(31\) small admissible parameter pairs and verifies the individual formula in the cited source.

The program exhaustively enumerates the *parameterized source families* at coordinate cutoffs \(200,400,800\), reproducing the respective near-critical primitive-set counts \(4125,16343,65133\). It additionally checks the finite tail counts at thresholds \(1/2,1,2\): for the three cutoffs these are \((685,180,38)\), \((2749,685,180)\), and \((10860,2749,685)\).

These are checks of finitely many parameters and of eight exact rational polygon identities. They are not an exhaustive independent verification of the source's general classification or of all primitive quadruples at arbitrary height. The unbounded height law and limiting distribution are proved mathematically in RESULT.md by local residue counting, Möbius inversion, and polygon-area scaling. No independent audit or formal verification is claimed.
