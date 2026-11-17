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

For reflection w_i=w_{c-i}, a k-window at i reflects to reversed window at C-i, C=c-k+1. Each of q^ceil(k/2) palindrome factors occurs once in every residue mod n, forcing every fixed residue of r->C-r to lift uniquely to a distinct fixed start mod L=n q^k. Thus q^ceil(k/2)f_n(C)<=f_L(C)<=2. Odd n gives f_n=1 and necessity q=2,k<=2; repetition (01)^n and (0011)^n is perfect for odd n by gcd(n,2)=gcd(n,4)=1 and palindromic up to rotation. Even n and C even would give f_n=2 with L even and an impossible >=4 fixed starts, so C odd. For odd n nonexceptions, reversal acts freely and bracelet count equals half of existing necklace count. The even example is a necessary-condition witness, not full sufficiency.

## originality

PASS

Best-of-knowledge originality after comparing statements, direct implications and inspected primary source material.

## value

PASS

Achirality is the natural dihedral fixed-point obstruction when moving from perfect necklaces to bracelets. A complete all-odd-multiplicity existence/nonexistence theorem and exact parity constraint on even axes give an independently useful classification and a direct symmetry correction for known necklace counts, without claiming to solve even-multiplicity existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
