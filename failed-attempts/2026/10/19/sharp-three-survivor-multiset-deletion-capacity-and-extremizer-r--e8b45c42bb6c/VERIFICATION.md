---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Sharing a deletion output is precisely having intersection weight I≥3: select three units from the coordinatewise minimum. Each word with a triple uses a coordinate no other such word can use for a triple, so there are at most q heavy words. For two light words x,y the coordinate maxima total at most 2q, giving I≥2n−2q≥4. Above 2q a light word cannot exist. Pure words and one capped word of the required mass (when it fits) attain the bounds. At n=q+1 the two supplied light vectors have intersection exactly 2: two opposite-half singleton overlaps for even q, or a single doubled overlap for odd q. At either rigidity length there must be exactly q heavy words assigned to different coordinates and a single light word. At 2q every light entry is 2, forcing purity of all heavy words. At 2q−1 there is precisely one light entry 1, at s, with all others 2. At an assigned coordinate other than s the two units of allowed overlap are exhausted, and at s the remaining budget of one forces at most one unit off s (each other light entry is 2). All q choices for the s-word are mutually distinct choices of codebook and compatible with the other words, and the light word distinguishes the q choices of s. This gives the stated 1 and q² counts without extrapolation.

## originality

FAIL

The exact capacity and strict first boundary are covered by distinct, stronger accessible statements. The remaining endpoint enumeration, though made explicit here, is a direct consequence of the indexed theorem's heavy/light structure and its confusability rule. This is mathematical coverage in the checked corpus, not a determination that the covering texts predate or were independent of this frozen result.

## value

FAIL

The capacity phase transition is a natural exact coding invariant and would be of substance on its own. In comparison with the verified coverage, however, the only proposed increment is to count the labels of the two forced capped vectors and the at-most-one extra unit dictated by the already available structure. There is no independent additional classification of compatible codes beyond this endpoint specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
