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

The exact first-stage checker was compiled as C++17 with optimization and replayed from the final source content. It generated every labeled ordered unequal pair and every undirected shift neighbor for each \(2\le q\le7\), enumerated all candidate sensor sets of both sizes \(k-1\) and \(k\), compared the mask trial total to the exact binomial count, computed all optimum masks, and partitioned those masks under alphabet adjacent-transpositions and reversal. It printed `VERIFY_OK` and the capacity/optimum-count/orbit-count sequence \((1,2,1),(3,20,3),(4,168,7),(5,84,2),(7,11040,16),(8,13860,5)\).

The second source `secondary_check.py` built the undirected neighbor sets using ordered-pair objects rather than bits, independently enumerated optimal and one-smaller subsets for \(q=2,3,4,5,6\), and independently checked the \(q=7\) attaining set. It printed `ALTERNATE_OK`. A separate exact integer-constraint model of domination and outsider separation also returned the same integer minima for \(q=6,7\), serving as corroboration rather than as the proof certificate. Direct enumeration of the complete group action for the largest two orders confirmed orbit-size distributions \(120^{[2]},360^{[4]},720^{[7]},1440^{[3]}\) and \(630^{[2]},2520,5040^{[2]}\).

The exact complete-search counts at \(q=7\) were \(26{,}978{,}328\) rejected seven-sensor candidates and \(118{,}030{,}185\) tested eight-sensor candidates. No external solver tolerance, probabilistic test, or extrapolation is used in the proof. Results for \(q\ge8\), physical error models, and any claim of global historical uniqueness are not verified. The review above is not an independent audit.
