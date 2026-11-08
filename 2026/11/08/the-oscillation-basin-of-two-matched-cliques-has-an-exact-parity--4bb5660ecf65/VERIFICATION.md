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

The local fields are derived directly from the two row-cliques and matching. The even/odd case split is exhaustive for all \(n\ge2\). The critical odd-order case is counted by four column multiplicities; in particular the only extra one-step oscillation predecessors have multiplicities \((1,k,k-1,1)\) or \((1,k-1,k,1)\), with \(n=2k+1\). Each family has \(n!/(k!(k-1)!)\) labelled states. No initial state can enter a primitive two-cycle after more than one update.

`check_direct.py` evaluates all 87,376 distinct initial states for \(2\le n\le8\) using open-neighbor bit masks, compares the fixed, immediately two-periodic and eventually two-periodic populations, and checks the maximal transient duration. `check_multinomial.py` makes a logically separate enumeration of 135,746 exact column-type quadruples over \(2\le n\le40\), independently updates representative states, and compares the weighted counts with the formulas. Run `python3 check_direct.py` and `python3 check_multinomial.py`. Both use the Python standard library. Captured outputs are in `check_direct.out` and `check_multinomial.out`.

These finite computations do not establish the theorem for arbitrary \(n\). The proof does; the computations can detect implementation or algebraic slips within tested ranges. No external validation, formal proof assistant, or independent audit was performed.
