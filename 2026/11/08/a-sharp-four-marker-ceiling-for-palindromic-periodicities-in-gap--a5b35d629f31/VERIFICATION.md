---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Using w symmetric-period definition, proper word-period p=|w|−ℓ exactly corresponds to border ℓ. For pairwise distinct complete zero-gaps a proper border cannot include two 1s, because the duplicate border would repeat a complete internal gap. Zero-only border ℓ∈[0,min(a,e)] yields circular gap t=a+e−ℓ traversing [max(a,e),a+e]. A one-marker border exists iff a<=last internal gap and e<=first internal gap and leaves m−1 distinct circular gaps. Dihedral reflection of circular gaps: with m>=5 at least two pairs of gaps must coincide, impossible with only one variable closing gap; m=4 requires closing gap = middle internal gap, m=3 requires equal one of two internals or one-marker border; m<=2 always symmetric. Checked literal periodic-palindromic definition on all 5803 eligible binary words through length 15 with independent enumeration. This supports but does not replace the unlimited-length proof.

## originality

PASS

Simpson and Fici–Shallit–Simpson provide the symmetric-period equivalence, and prior published 2026-11-02 Resultary gives a complete weight-three enumeration with circular-gap criterion. Those cover substantial m<=3 background but do not imply the sharp four-marker ceiling and exact m=4 boundary test under the distinct-internal-gaps hypothesis. The complete classification across any number of markers is a new restricted-language statement; no claim to original symmetric-period characterization or weight-three counting.

## value

PASS

The pairwise-distinct internal marker-gap condition is a natural combinatorics-on-words nonrepetition promise. A sharp finite cap on the number of markers for palindromic periodicity and exact m=3,4 membership inequalities turn a global existential periodic-palindrome predicate into a small arithmetic test. The four-marker witness proves sharpness; this is a complete natural finite classification rather than arbitrary enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
