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

The script `verification_check.py`, included alongside these six scientific files, independently evaluates private open-neighborhood witnesses in each expanded graph, then independently evaluates closed-neighborhood private witnesses in its base graph. It does not use the theorem to implement the expanded-graph super-domination test. All finite labeled simple graphs of orders one through four were checked (with \(m\in\{2,3\}\) when the base has at most three vertices, and \(m=2\) at order four). Every subset of the resulting blowups was tested; no sampling was used in these profiles.

Cyclic base graphs of lengths \(3\le n\le17\) were also checked against both the forbidden-factor characterization and the triple-state transfer trace for **all** \(2^n\) words. Selected clique-blowup cycles, namely parameters \((n,m)=(3,2),(4,2),(5,2),(6,2),(7,2),(3,3),(4,3),(5,3)\), were independently evaluated using every expanded-graph vertex subset. Both the complete all-set coefficients and the minimum-set counts matched.

Exact output from `python3 verification_check.py`:

```
VERIFY_OK labeled_graph_profiles=86 labeled_graph_subsets=21164 cycle_words=262136 direct_cycle_blowup_subsets=59200 irredundance_correspondence=PASS cyclic_transfer=PASS minimum_count=PASS
```

All reported profile sizes and checked-subset totals were obtained by the script. The finite checks do not establish the theorem for arbitrary graph order, clique size, or cycle length; those assertions depend on the proof in `RESULT.md`. No independent mathematical audit has been performed. No external formal proof system was used.
