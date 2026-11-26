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

For odd p<q, only p can divide (p+1)(q+1), and this occurs precisely if p divides q+1; for p=2 every odd q qualifies, including q=3 where q itself also divides p+1. In the odd-prime progression sum the only removed prime with q<p is q=2 at p=3, so the O(1) adjustment is valid. Fixed p gives x/[p(p-1)log x] by the reduced-class PNT. For Y<p≤x^(1/4) the BT bound normalized by x/log x is at most 4/[p(p-1)]. For larger p the count of integers in the residue class is ≤x/p²+1, with total O(x^(3/4)+√x). This gives the correct nested-limit argument and absolutely convergent constant. The independent fixed-point sieve enclosed C between 773156601234798/10^15 and 773157601313296/10^15, using an error ≤78498/10^15 in the partial sum and ≤10^-6 in the tail. Factoring by greatest prime divisor reproduced counts 145,1059,8170,65886. The frozen checker was inspected, not run; its binary floating-point summation alone is not an outward-rounded bound.

## originality

PASS

The distinct statement supported here is an explicit asymptotic for the Duffinian exception set, not discovery of the series or a new counting method. The matching-constant catalogue theorem treats p|q−1 and does not itself count this set; the direct Duffinian predecessor gives only an order bound. The scientific significance of transferring their ingredients is evaluated separately below.

## value

FAIL

The exception count is naturally motivated but the exact leading constant here is a routine residue substitution in the earlier noncyclic semiprime calculation. That proof already establishes the exact same sum: replacing +1 with −1 keeps the reduced-class main term and BT bound and changes the integer upper bound by at most one per modulus. The only small endpoint case is q=2 at p=3; the p=2 class is identical. The Duffinian local criterion was already established, and no new invariant value, quantified error, or additional distribution information survives this transfer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
