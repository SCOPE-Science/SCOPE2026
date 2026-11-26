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

An odd circular length exchanges vertex parity and a length-two edge preserves it, so the counts of even-even and odd-odd edges are equal. If 3 divides n, each residue class modulo 3 initially has even size and length-three edges remain within it, so a single length-one edge with no length twos makes two classes impossible to finish. Each of the six displayed blocks covers its interval with the specified ordinary differences, which are also the circular lengths because 3<=n. For b>0 even, use b/2-1 pure length-two blocks, triples of length threes, singles of length one, and a residue block consuming the final two length twos with zero, one or two length threes. For b=0 and c=3q+r, pair each residual length three with a length one if a>=r. The remaining a<r cases are the pure length-three cycle (the map from even labels to odd labels by +3 mod 2n is a bijection) and a=1,r=2, precisely the obstruction. This includes n=3 and proves the equivalence for arbitrary n, independently of the tests. A definition-based independent matching recursion reproduced every profile for 3<=n<=10, with counts 5,9,12,15,20,25,29,36; these finite checks corroborate rather than prove the infinite statement.

## originality

FAIL

A distinct earlier-dated local Resultary record states the same complete cyclic classification, exception, six-block construction and pure-length-three wraparound. The match includes the genuinely three-length profiles; this is not just known two-length material. This finding concerns demonstrable catalog coverage, not historical priority or provenance.

## value

FAIL

A complete three-length classification is well motivated as a tractable part of the prime seating conjecture with an additional composite-order obstruction. But this submitted finding reproduces the available exact classification and construction, rather than extending them; the corroborating enumeration does not add a separate substantive theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
