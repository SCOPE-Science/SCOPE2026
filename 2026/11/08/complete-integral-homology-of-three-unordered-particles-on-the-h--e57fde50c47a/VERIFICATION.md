---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The three-particle Heawood full-vertex reduced Świątkowski chain model is the published graph-configuration model: for 14 trivalent vertices and 21 edges, weight-three chain ranks are (1771,6468,7644,2912). The actual frozen artifacts/verify_integral.py reconstructs signed boundaries, tests integer d²=0, applies unimodular ±1 Schur complements, verifies rank-one remaining d2 block by proportionality and gcd 2, and repeats d3 with two pivot orderings. Its asserted Smith factors d1: 1^1770; d2:1^4689,2; d3:1^2911 give rational ranks (1770,4690,2911), free Betti (1,8,43,1), and H1 torsion Z/2. Since coker(d3) is torsion-free, H2 embeds there and is torsion-free, so H2=Z^43. Direct independent chain-rank formula and Euler count 1771-6468+7644-2912=35 agree. The full 7,644-column integer Smith computation was inspected in source but was not independently re-executed in this run; a logged PASS alone is not adopted as evidence.

## originality

PASS

The new final invariant is integral H2(B3(Heawood);Z)=Z^43 with no torsion of any prime order. The closest earlier same-object full RESULT.md (Oct 11) explicitly stops at H3=Z and mod-2/mod-3 Betti vectors (1,9,44,1)/(1,8,43,1) and states it does not claim integral H1/H2. These field computations exclude only corresponding small-prime torsion and do not imply no 5-primary or higher-prime torsion in H2. General graph braid H1 formulas and graph-product cycle generation likewise do not supply this integer d3 Smith classification. No earlier exact integral H2 was found in targeted aliases; this is best-of-knowledge, not publication priority proof.

## value

PASS

The Heawood/Fano incidence graph is a natural nonplanar trivalent configuration-space test case; the exact missing integral degree-two group after a prior same-object field computation resolves a genuine torsion-order ambiguity, not a numerical relabeling. The integral torsion-free conclusion may be used to benchmark further three-particle graph-braid homology computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
