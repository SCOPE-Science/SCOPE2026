---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Reconstructed the Parseval normalization for f_a(d)=p^{-1/2} exp(2πida/p) over the nonzero squares, for every prime p≥7, p≡3(mod4). Quadratic Gauss evaluation yields H_ab=-1+i√p χ(b-a), and G_B=((p-1)I+H)/(2p). Checked the source verifier implements exact integer-polynomial 4x4 determinants for T/O/I/S and resulting P_T/P_O/P_S, not a merely numerical loop. Double regularity with d=(p−1)/2 and t=(p−3)/4 counts each class: n_T=p(p−1)(p−3)(p−7)/64, n_O=n_I=p(p−1)(p−3)(p+1)/192, n_S=p(p−1)(p−3)(p+1)/64. P_T−P_S=16p(y−1) and P_O−P_S=8p(y+p−1) imply the largest root is uniquely of type S; y_S<p+1 by positivity and quartic comparison, so the minimum retained lower bound is (p+1−y_S)/(2p)>0. At p=7 type T is absent, but S occurs. Enumerations at finitely many primes confirm, not prove, the universal statement. No scientific contradiction found.

## originality

FAIL

FAIL: a separately published and fully inspected Resultary mathematical finding on exactly the same prime-order quadratic-residue harmonic frame already states all three four-subset Gram characteristic polynomials (under unit-frame scaling) and exactly the same counts, and its proof derives them from precisely the same Paley tournament matrices. The new retained-frame lower bound is a direct endpoint consequence of that complete pre-existing spectrum and the standard identity S_retained=I−F_B F_B*. The earlier distinct extremizer for two-sided operator-norm deviation is not a distinct source of novelty for the new endpoint.

## value

FAIL

FAIL: the meaningful four-erasure stability problem is already settled at a stronger informational level by the prior complete same-object four-column spectral census and multiplicities. Extracting the positive spectral endpoint and converting normalization gives no independently valuable missing invariant, structural insight, classification or new parameter beyond a direct corollary. Computational reproducibility and sharpness do not rescue covered mathematics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
