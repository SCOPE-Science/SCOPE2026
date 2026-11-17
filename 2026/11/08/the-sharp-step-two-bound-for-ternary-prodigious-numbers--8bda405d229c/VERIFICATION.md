---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

If n is odd, ternary prodigious n has no digit 2, hence n mod9 in {0,1,3,4} and at most 2 consecutive step-two odd terms. For even n with n=2 mod4, two 2 digits among three lowest ternary positions force 4|p3(n) but 4∤n. The exact CRT classes are {26,50,62,74,78,98,106} mod108, spaced by even step indices with maximum cyclic gap 14, so every 14-term even run hits one forbidden class. Independent exhaustive check of all 54 even residue starts and 9 odd residues reproduced this obstruction. Direct digit products of 108,110,...,132 equal [1,2,1,2,4,1,1,2,2,2,4,2,4] and divide each term. Adding 4*3^K for every K>=5 prepends two unit digits with no carry and preserves all divisibility, proving infinitely many sharp progressions. The universal claim follows from residue argument, not an unbounded scan.

## originality

PASS

The previously published b-prodigious progression theorem handles stride d dividing the base and d<b/2, or d=b/2 for even bases; base b=3 and stride d=2 is outside both domains. The sharp length 13 and infinite attainment are a nontrivial, motivated first excluded fixed-stride parameter with no inspected equivalent table.

## value

PASS

The natural prodigious-number progression problem in a first excluded odd-base stride admits a sharp global cutoff 13, substantially longer than the known contiguous-run bound 5, with an elementary structural obstruction and infinite sharpness family. This is a useful, self-contained natural exact invariant with motivated parameters; no sweeping generality is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
