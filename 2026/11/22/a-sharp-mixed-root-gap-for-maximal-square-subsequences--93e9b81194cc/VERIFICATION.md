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

Root containment agrees with complete-square containment: copy an embedding twice in one direction; in the other, if the first embedded X ends in the first Y, use it, otherwise the entire second X lies in the second Y. The first X need not literally cross the junction, but the suffix argument still applies. A mixed deficient root needs length at least two and a maximum root needs length at least three. At host length six, the only possible length-three square fills the host, so every shorter root is contained in its root. At length seven, if the deficient root is 10, a feasible root of length three must avoid 10, hence lies in {000,001,011,111}; the unary options leave too few letters of the other kind for 1010. A bounded independent insertion check gives the following complete list among insertions that contain 1010: from 001001, hosts 0010010, 0010101, 0101001, 1001001, where the first and last are rejected by extensions 010 and 100; from 011011, hosts 0101011, 0110101, 0110110, 1011011, where the last two are rejected by extensions 110 and 101. Complementing gives the other four qualifying words; their stated reversal/complementation orbits follow. A separate bounded census of all 255 binary hosts through length seven agreed. In Wₘ the two ones force each mixed root to have exactly one 1; if the root is 0ᵃ10ᵇ then its square must fit a+b zeros in the single central zero position. Thus 10 embeds as a square and cannot extend; all mixed roots have length at most two. The 2m+1 zeros and two ones then give maximum root length m for m≥3.

## originality

PASS

Credit the known root-order and one-letter extension criteria and the earlier indexed implication that a mixed maximal root can be deficient. The supported distinct claims are the sharp binary threshold with all eight minimal hosts and the unbounded ratio with a fixed-length mixed maximal root in the exhibited family. Neither inspected prior result yields these quantitative statements.

## value

PASS

Recent maximal-square algorithms make it natural to ask how small a binary input can already contain a genuinely mixed maximal solution shorter than the maximum and whether the distinction can be arbitrarily large. A smallest-host classification with all equality cases and an all-m fixed-two-marker construction answer these questions; the mixed requirement rules out trivial unary deficiencies. The quantitative statements add to the known qualitative overlap without claiming to predict any algorithm's output.

The dated certificate retains the supplied scientific assessment, sources and limitations.
