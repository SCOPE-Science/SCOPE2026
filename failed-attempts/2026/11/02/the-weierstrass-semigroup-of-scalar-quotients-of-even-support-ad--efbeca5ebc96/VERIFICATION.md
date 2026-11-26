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

Set s=r^h+1 and D=2(r-1). For a root y and any place above X=infinity, its negative valuation gives r times its pole order equal to es where e is the local ramification index. Since gcd(r,s)=1, r divides e; the extension degree is at most r, proving degree r, total ramification and unique infinity. The Y derivative -1 makes the affine model smooth, and monic reduction gives its k[X]-basis 1,Y,...,Y^(r-1). The congruences r^j=1 mod D on the supported indices and 2r=2 mod D give the stated faithful tame diagonal action. The full affine invariant ring is spanned by X^iY^j with i+2j=0 mod D, and pole orders upstairs ir+js are distinct by reduction modulo r. At the fixed infinity the index is D, so no leading-pole cancellation occurs downstairs either. For fixed j the least i gives a_j=r+jL for j>0, with a_0=0; other i add multiples of r downstairs. The relation DL=1 mod r makes these representatives exhaustive and distinct modulo r, giving the Apéry and Riemann–Roch assertions. Splitting a nonzero Apéry entry into two positive nongaps would either add a positive multiple of r to its own residue minimum, or use positive indices summing to j or j+r, already larger than a_j. Adding the generators to jL shows these and only these top residue gaps are pseudo-Frobenius. The genus sum is (r-1)(L+1)/2=(r^h-1)/4, and 2g=F+type gives almost symmetry; the type exceeds one. Independent finite enumeration of divisible upstairs pole orders corroborated the Apéry and gap formulas, including the nonprime case (r,h)=(9,2).

## originality

FAIL

There is verified equivalent coverage of the entire prime-r case, including the primary application singled out in the Finding. The same-day twisted Artin–Schreier record 60088f5a2835 treats this very marked curve in invariant coordinates and is broader in f for r=p. Its pole functions also furnish the stated basis by taking powers of u and using its Apéry theorem. Same-day ordering is unresolved, so this is not a priority allegation. The other stated scope, r=p^e for e>1, is not literally asserted in that record. But no material distinct theorem is established by that extension here: the same twisted-cover construction and pole calculation extend directly using the additive group of F_r and scalar group F_r^times, with gcd(r,d-1)=1. This is a scope extension, not evidence that the prime-power theorem was explicitly published there.

## value

FAIL

One-point Riemann–Roch bases on these curves are useful, and the proof is correct. But the advertised prime-field maximal family is already covered by the exact twisted-curve theorem, including the basis as a direct consequence of its pole functions. The remaining prime-power scope uses the same scalar quotient and degree/coprimality pole argument without a new mathematical obstruction or independent application substantiated by the record. The marginal contribution is a routine extension and restatement of a covered narrow invariant; no separate valuable repair was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
