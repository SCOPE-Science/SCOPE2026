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

The executable `artifacts/verify.py` directly constructs the graph with a common hub, enumerates each orientation bitmask for small edge counts, tests global directed acyclicity by indegree elimination, and counts vertices of outdegree zero. A second, symbolic-product route generates the expected coefficients. The two routes agree on 168 graph profiles. The program additionally verifies total orientation counts and strict coefficient log-concavity on 21,824 profiles, polynomial discriminant identity on 44-cubed triples, and the repeated-block threshold on 54-squared pairs, as well as the re-entrant integer phase for block sizes 5 and 6 through 1000. Its expected last line is `VERIFY_OK`.

Exact enumeration here is finite; the unrestricted theorem follows from the self-contained mathematical proof in `RESULT.md`. Mathematical priority and all statements outside the verified finite windows have not been independently audited.
