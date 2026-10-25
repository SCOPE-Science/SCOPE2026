---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS. For <=4 odd distinct prime factors, sigma(n)/n <= (4/3)(6/5)(8/7)(12/11)=2304/1155<2; >=6 factors imply n>=255255>39585. Independently scanned every odd n<=39585 with SymPy exact factorization, extracted all 12 squarefree five-prime candidates, and checked all proper-divisor pairs. No qualifying n<39585; n=39585 has exactly (105,1365),(455,1015); sigma=80640. This proves the unbounded minimum because the structural bound makes this finite census exhaustive.

## originality

FAIL

FAIL. OEIS A341475 is an older exact table of ALL 2-near-perfect numbers, and its linked b-file contains 39585 as term 175, with all smaller members explicit at indices 1..174. Screening these earlier entries for odd squarefreeness yields none; 39585 itself is odd squarefree. Thus the precise numerical minimum is already a direct consequence of the published table even without those category words in its title. The ancillary >=5 support bound is an immediate four-prime reciprocal-product bound and does not rescue the original numerical novelty.

## value

FAIL

FAIL. The natural minimum is arithmetically meaningful but was already determined in the existing comprehensive exact table. The remaining five-prime support observation is an elementary size bound, not an independently motivated structural classification or unknown exact invariant; the submitted package is therefore largely a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
