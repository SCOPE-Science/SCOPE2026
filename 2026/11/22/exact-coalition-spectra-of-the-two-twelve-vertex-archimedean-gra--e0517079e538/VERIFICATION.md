---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction of exact finite enumeration

The checkable claim concerns only the two twelve-vertex graphs defined in `RESULT.md`. Execute `sh verify.sh` with C++17 and Python 3 to compile, enumerate and compare the counters. The expected final stdout marker is `COALITION_PAIR_VERIFY_OK`.

The restricted-growth-string routine visits \(4,213,597\) unique unordered partitions per graph and tests every block. The different least-unassigned-subset routine visits the same mathematical partition family using missed-neighborhood masks. Both independently return cuboctahedral counts by number of blocks \((24,10128,194733,582874,378855,47900,762)\) for \(k=2,\ldots,8\), and truncated tetrahedral counts \((171,24846,258625,441384,153715,7422,93)\). All other coefficients vanish. Exhaustive degree-eight partition lists have \(762\) and \(93\) entries, and the explicit generated graph automorphisms group these into \(23\) and \(7\) orbits, respectively.

`orbit_cubo.json` and `orbit_trunc.json` contain complete orbit representatives, block-size profiles, and the number of optimum configurations in each orbit. `opt_cubo.txt` and `opt_trunc.txt` contain all degree-eight certificates as twelve-bit masks. The finite proof does not depend on external numerical databases. This is self-review and is not an independent scholarly audit; historical publication priority and generalization remain open.
