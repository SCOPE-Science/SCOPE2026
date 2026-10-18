---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Independently recursed over every ordered exponent composition of 5 and strictly increasing odd primes <=383, with rational exact I(p^a)=σ(p^a)/p^a and admissible monotone prefix upper bounds. Obtained exactly 121 abundant values, smallest 945, largest 442365; first/tail integers matched the claimed families and independent OEIS A287646 table. For unbounded primes the source proves a separate extremal upper bound for largest prime >=389 across all support sizes r<=5, so q<=383 is exhaustive; Ω<=4 extremal 3·5·7·11 ratio=2304/1155<2; no finite cutoff used as unexplained infinite fact.

## originality

FAIL

OEIS A287646, authored M. F. Hasler on 2017-05-30, explicitly provides the entire row for odd PRIMITIVE abundant numbers with Ω=5, and linked A287728 states row length 121, start 945 and end 442365. Every odd abundant integer with Ω=5 is automatically primitive abundant because no odd number with Ω<=4 is abundant. Therefore the existing exact row is IDENTICAL to the claimed entire first Ω=5 abundant set; its full enumeration algorithm is already given. The ten compact prime families merely reformat known exact elements, not a previously unknown classification.

## value

FAIL

The mathematical task of an exact first odd-abundant layer is natural, but the final scientific deliverable solely re-enumerates a 121-member layer tabulated with a general all-rows enumeration algorithm in OEIS since 2017. Repackaging a known list as ten prime support ranges is an unmotivated presentation gain without a new structural theorem, so it falls under known-table recomputation rather than a valuable independent unknown invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
