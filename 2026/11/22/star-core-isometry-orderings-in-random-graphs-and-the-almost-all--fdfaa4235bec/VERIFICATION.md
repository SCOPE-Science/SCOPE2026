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

# Verification

Compile and execute `check_exhaustive.cpp` with a C++17 compiler (`c++ -O2 -std=c++17 check_exhaustive.cpp -o verify && ./verify`). This independently enumerates all \(33{,}867\) labelled simple graphs of orders one through six, checks every candidate closed-neighborhood witness certificate, and for all \(52{,}923\) certified graph-center pairs checks that four differently selected star-first vertex orders yield correct original distances on every prefix. Its observed output is `PASS all 33867 labeled graphs of order at most six; 52923 certified (graph, center) pairs; four star-first orders per pair.`

Execute `python3 check_random.py` to reproduce an independently programmed seeded sample of 630 labelled graphs of orders seven through twenty; 6,015 center certificates pass, and all tested prefix distances agree with full graph distances. Observed output is `PASS 630 seeded random graphs; 6015 independently certified centers, every prefix BFS-checked`.

The all-order mathematical argument does **not** depend on extrapolating these finite experiments. The proof in `RESULT.md` directly establishes (a) the deterministic prefix-isometry criterion; (b) exact single-pair witness failures and the binomial union bound; (c) the asymptotic sufficient density condition; and (d) the Burnside comparison that legitimately transfers the uniform labelled property to unlabelled connected graph classes. A full combinatorial check of every \(G(n,p)\) outcome for arbitrary \(n\) is neither attempted nor needed.

The probabilistic density threshold is sufficient, not sharp; priority outside the primary literature searched is uncertain. No independent scholarly audit is claimed.
