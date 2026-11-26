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

For linear alternating binary words with exactly five positive runs, a mixed witnessing border uses matching transitions. For four runs this forces matched 01 (or 10) transitions and gives precisely the two tail inequalities; for five runs it matches both transitions of the first return to 0, forcing b=d and both endpoint tails at most c. A unary witness in a five-run factor requires equal tails strictly longer than c. These exhaust the border types. One-letter tests give whole runs, remove the indicated three-run endpoints, cap the four-run tails, and kill the capped bridges exactly when their five-run extension is closed (b=d). In the five-run cases an unequal unary tail loses closure, and mixed tails are maximal only at their coordinatewise caps. Summing distinct intervals gives the count. With s=a+c+e and t=b+d the zero-tail contribution H has 3H <= 2s−2 and the one-tail contribution V satisfies 3V <= 2t for t >= 2. The zero-tail bound is attained for each s >= 4 by the listed residue choices, and (b,d)=(1,2) then attains the unrestricted maximum for n >= 7. Direct n=5,6 cases give 6,8, respectively; H>=0, V>=1 and (n−4,1,1,1,1) gives the minimum. For the symmetric constraint a=e=x, b=d=v, H=x+c−2 if c<=x and H=2x otherwise. In both cases 3(H+v)<=2n−3; for n=3k,3k+1,3k+2 the triples (x,v,c)=(k−1,1,k),(k−1,1,k+1),(k−1,2,k) attain the bound after flooring, for k>=2. Independent first-return checks matched all endpoint sets on 1,024 tuples and direct extrema (including the symmetric subfamily) at n=5..19.

## originality

PASS

Pass for the complete unrestricted five-run specialization and sharp fixed-length optimization, not for the general border-pair method or the symmetric subcase. A distinct same-day result demonstrably gives the exact symmetric enumeration and extremum. The unrestricted optimization and sharp residue-class advantage over that benchmark are supported as distinct by the inspected comparisons; no priority order is inferred from dates.

## value

PASS

Five runs are the first alternating binary shape allowing a repeated unary run separated by two same-symbol returns; the occurrence census exposes competing long-unary and nonunary spanning mechanisms. Exact endpoints and sharp extrema give reproducible worst-case instances for occurrence enumeration. In particular fixed-length optimization over symmetric templates misses the true extremum at infinitely many lengths, with explicit witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
