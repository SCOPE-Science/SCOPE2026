---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS: The final statement is for synchronous Rule 54 on indexed cyclic rings n>=3, not quotient rings. Temporal columns a,b,c satisfy b_(j+1)=b_j XOR(a_j OR c_j). The exact (a,b)->(b,c) transition constructs a finite graph of 2^(2t) vertices, and rooted spatial closed walks of length n correspond bijectively to Fix(F_n^t). Independently compiled and executed a fresh table-driven C++ graph generator and zero-in/out peeling for t=1,3,5,7,9,11, enumerating all 4,194,304 vertices at t=11 and all 4,192,256 edges. Reproduced edge totals 2,56,992,16256,261632,4192256 and residual permutation-core cycle lengths (1),(1),(1),(1),(1),(1,11,11). No directed closed walk can lie outside the peeled core, and surviving in/out degree exactly one means the core is a disjoint cycle union. Thus counts 1 for the five lower odd iterates, and 1+22*1_(11|n) for iterate eleven. Since 11 is prime, the 22 nonzero eleven-site states give two primitive temporal orbits of length 11; the two given binary words translate by shifts +4 and -4, related by reflection. All-n theorem follows from complete finite temporal-column graph exhaustion, NOT from checking only rings through n=11. The theorem makes no statement about odd t>=13.

## originality

PASS

PASS best-of-knowledge: the 2008 Rule 54 glider paper and its 2014 expansion already report eleven-site waves and other temporal clocks. This finding expressly does not claim their discovery. Its all-ring exact eleven-return fixed-point count and exclusion of nonzero temporal periods 1,3,5,7,9 require full recurrent temporal-column graphs; direct wave examples and shorter-period de Bruijn diagrams do not mathematically imply these exact classifications. Search also surfaced other published Rule 54 image, 4-cycle, 6-cycle calculations, not this specific entire odd sector. A 2012 same-rule dynamics article was inaccessible in full and remains a priority risk.

## value

PASS

PASS: An exact all-circumference return-count formula, the sharp first nonzero odd temporal period and global short-odd exclusion constitute a natural complete classification of the first odd sector of a named elementary cellular automaton. The 2008 finite witness alone is known and not independently valuable, but global structural exhaustion extends significantly beyond one example. The resulting dynamic zeta and orbit facts can be reused for periodic-space-time analysis; no claim about longer periods or attraction basins is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
