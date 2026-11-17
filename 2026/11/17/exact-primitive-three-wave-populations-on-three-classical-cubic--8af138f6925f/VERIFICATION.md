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

## Reproducibility

Run `python3 levi_wave_verify.py` with a standard Python interpreter (Python 3.9+). The script constructs Möbius–Kantor as \(GP(8,3)\), Pappus from nine explicit incidence triples, and Desargues as \(GP(10,3)\). The algorithm enumerates each point shore of size \(m\) with one color fixed (all \(3^{m-1}\) possibilities); it counts compatible colors of the other shore with two independent exact cover procedures. Outputs and internal assertions are recorded in `levi_wave_verify.out`. On \(K_{3,3}\), the additional direct \(3^6\)-state synchronous-update enumerator returns the same result.

## Interpretation and limits

This is a complete finite calculation, with an elementary characterization of its counted objects, not a finite experiment purporting to prove a separate infinite claim. The source code contains all graph adjacency specifications and has no external dependencies. Primitive period three is distinguished from fixed and other periods; divide phase-state counts by three to obtain orbit counts. Self-review does not constitute external mathematical certification or prove historical priority.
