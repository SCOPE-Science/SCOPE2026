---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For any fixed odd positive h, local q² constraints on invertible p mod q² exclude exactly two units when q∤h and none when q|h. CRT plus PNT in fixed reduced progressions gives the finite-sieve product. For q≤X^(1/4), Brun–Titchmarsh bounds the summed large-square tail by O(X/log X∑_{q>Y}1/[q(q−1)]); for larger q elementary candidate counts O_h(X^(3/4)+X^(1/2))=o(π(X)). Hence Δ(h)=∏_{q≥3,q∤h}(1−2/[q(q−1)]). Direct local checks re-enumerated q=3,5,7 modulo 11025 for 9 odd shifts. The q=3 factor is 2/3; the elementary 3,5,7 lower product plus q≥11 tail proves C>1/2, so C≤Δ(h)<2/3 for 3∤h and 3C/2≤Δ(h)<1 when 3|h; endpoints sharp along odd primorial shifts. This is an infinite analytic sieve, not finite sample inference.

## originality

FAIL

Original double-flat density with arbitrary fixed odd shifts is covered as a specialization of Broughan (2012) double shifted flat-prime asymptotics, not just the older h=1 paper; the additional two separated bands follow by immediate manipulation of the local q=3 factor and a simple Euler-product lower bound. General coverage defeats novelty even though the exact displayed upper/lower endpoint typography is not in the title.

## value

FAIL

The fixed odd-shift density is a direct covered specialization of a previously developed general double-shift flat-prime sieve (2012); the q=3 density gap and sharp endpoints follow from one local Euler-product factor plus an elementary positive-product estimate. The object is natural, but after removing the previously covered theorem no new nonroutine invariant/classification or substantive mathematical gap survives. Correctness and a clear statement do not independently establish mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
