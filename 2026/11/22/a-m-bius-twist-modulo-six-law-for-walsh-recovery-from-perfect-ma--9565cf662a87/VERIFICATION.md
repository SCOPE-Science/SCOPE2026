---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Switching at vertices multiplies every perfect matching by the same sign; the nonseam cycle edges form a spanning path, so fixing them all positive is possible and picks a unique edge-sign representative. The switching kernel consists exactly of the two constant assignments, giving 2^(2n-1) full signs per reduced representative. To check the matching transfer, remove the endpoints of at least one chosen chord. The remaining circumference pieces are paired with their antipodal translates. Each piece has a unique perfect matching if it has even length in vertices and none otherwise, so all remaining cycle edges occur in antipodal pairs and give the cyclic monomer-dimer model. Its two transfer terms are the no-seam and seam contributions a and hd: fixing the seam dimer removes the two extreme column indices. If no chord is chosen the two alternating circumference matchings are invariant under the antipodal shift for even n and interchanged for odd n. Only the odd case needs the additional weights 1 and h. This gives (1), including n=3. The mod-2 transfer has order 3; its nonidentity powers have trace 1 and the identity power forces a,d odd and b,c even. At odd multiples of three, either possible zero would give ad=1 mod 4 and thus determinant 1 mod 4, contrary to -1. At multiples of six, h=+1 and a+d=0 would instead give determinant 3 mod 4, contrary to +1. The exact six-letter identity preserves parity and product; the six seeds give the optimal surviving gap in all residue classes. At n=6k any concatenation of the eight listed ±I blocks with h=-1 gives a zero, with distinct words and disjoint switching classes. The operator norms are the reciprocals of the least surviving absolute multipliers in the stated counting convention. A fresh bounded exact check agreed with all 4,080 reduced sign configurations for n=3–10, including 36 reduced zeros at n=6; it evaluated all six seeds and eight transfer blocks and tested propagation through n=60 (transfer only).

## originality

PASS

Provisional for the all-edge signed Möbius-ladder zero criterion, exact surviving gap, and constructive family of null characters. Earlier unsigned counts and general dimer identities are relevant, but the directly comparable signed cycle-prism statement has materially different zero and gap rules. The proof adapts a transfer approach rather than introducing signed matching methods or claiming novelty for the unsigned count.

## value

PASS

The all-edge recoverability and exact counting-measure inverse norm are natural, nontrivial invariants of a classical cubic graph family. The comparison isolates a real boundary-condition effect: the Möbius twist removes the entire odd-multiple-of-three failure class and changes worst-case surviving stability at the other singular lengths. The null witnesses quantify actual rank loss; this is more than another unsigned enumeration or a finite spectrum table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
