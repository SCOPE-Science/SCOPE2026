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

For the ordinary game on GP(10,2), the covered set and next mover are sufficient: a previous move's whole closed neighborhood is covered, so no repeated move can be legal. Every proper set admits a move and each legal move strictly enlarges it. With terminal D=S=0, the exact recurrence is D(U)=1+min S(U∪N[v]) and S(U)=1+max D(U∪N[v]) over legal v. The independent reachable-set DAG run used 11,846 dominated masks and checked all openings and all 760 conditional scores for distinct ordered opening/reply pairs under both conventions. It returned roots (9,8), uniform opening values, and distance-1-through-5 totals (9,8,8,8,9) and (9,9,8,9,9). The shell counts are (3,6,6,3,1); distinct closed neighborhoods have the same cardinality four so all nineteen distinct replies are legal. Hence S's optimal replies are neighbors and the antipode (four), while D's are precisely distance three (six). Frozen replay sources and logs are artifacts/game_dp.cpp, game_dp.py, cpp_output.txt and python_output.txt in the record directory; they were inspected, not executed. Independent replay: /workspace/branches/0a2fa392-a5ad-47f5-a702-3f2fd5f52e46/gp102_game_check.py and companion gp102_game_check_output.txt.

## originality

PASS

The standard game, its general bounds and starting-player effects are prior. The closest same-day record has an exactly matching Dominator-first response profile on the Desargues graph, but Desargues is bipartite, whereas GP(10,2) contains five-cycles, and its Staller-first profile and value differ. No inspected statement for the dodecahedral graph gives the complete two-convention profile or a theorem forcing it. This is a best-of-knowledge judgment on the specific dodecahedral result, not priority of the minimax recurrence or of starting disadvantage in general.

## value

PASS

A canonical cubic Platonic graph gives a natural test of the difference between starting conventions. The full distance profile explains which replies are responsible, distinguishing neighbors and the antipode from intermediate distances under one start and singling out only distance three under the other. This exact invariant is usable to benchmark strategies and compare other cubic symmetric graphs; it is not just a recomputed scalar or a claim that the starting disadvantage itself is new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
