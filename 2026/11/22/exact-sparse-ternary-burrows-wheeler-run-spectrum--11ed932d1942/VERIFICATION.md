---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The unique 1 makes every necklace primitive and canonically gives three nonnegative zero gaps. Rows starting in zeros first sort by decreasing leading-zero length, then by the next nonzero letter; for the two rows with next letter 2, the comparison is b versus c and at equality the B row reaches 1 first. The same tie-break applies to the marker-start rows. A gap contributes its nonzero predecessor on its first active level only; further levels at a constant active set contribute zeros, so one zero preserves all run boundaries for two or more levels. The multiplicities give a geometric factor for each repeated active-set size. Independently, I used all weak rankings of the three gaps with zero allowed and with adjacent positive length increments either 1 or at least 2. I sorted the literal rotations of each representative and used integer polynomial arithmetic to reproduce every numerator over (1-z)(1-z^2)(1-z^3) in exactly 111 cases; I also enumerated and sorted all rotations at each length 3–54 as a finite cross-check. For positivity, F3 has denominator 1-z^6 and numerator z^4(2+2z+z^2+3z^3+z^4+2z^5), F5=zF3/(1-z), F4 has positive numerator z^4(1+2z+3z^2) over (1-z^2)(1-z^3), and F6 has a z^6 contribution with denominator containing 1-z. Contributions below six runs grow at most linearly, versus quadratically many necklaces.

## originality

PASS

The supported distinct claim is the all-length joint census of frequencies by linear run count at the ordered ternary content (n-3,1,2), not the standard transform, general inversion, gap-order methods, or the existence of odd runs by itself. No inspected source covered the whole run census or implied the rational generating functions as a direct specialization.

## value

PASS

BWT runs are the statistic used in run-length compression; this is a natural first sparse ternary extension of the three-marker binary family, with just one marker changing letter. The complete generating functions quantify which run values persist at every length, how often each exceptional value occurs, and the concentration on six runs. This gives a reusable fixed-content benchmark rather than a single example of an odd run count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
