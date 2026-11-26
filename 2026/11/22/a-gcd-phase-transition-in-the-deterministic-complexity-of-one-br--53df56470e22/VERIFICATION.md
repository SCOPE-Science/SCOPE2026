---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The epsilon-free NFA accepts exactly by choosing a b with the correct prefix residue and checking the suffix residue. A word with T letters a leaves a unique C index i=T mod r; each D index is T-t mod s for an eligible b at a-count t, with r|t. Thus all D indices lie in J_i defined by i mod g. For reachability fix T congruent to i and at least lcm(r,s)-1. For each j in the desired subset J_i, CRT gives one t in [0,lcm(r,s)-1]; these t are distinct since their residues modulo s differ. Mark exactly those positions. This yields exactly r*2^(s/g) reachable subsets. Distinct D sets are separated by rotating a symmetric-difference element to zero. For equal unsaturated D sets, including the empty set in different classes, use CRT to rotate a missing eligible D position to zero and precisely one of the two C phases to zero; the final b then adds D_0 only to that phase. If equal D sets are saturated, the classes must coincide (they are nonempty), and rotation preserves saturation while b adds nothing; acceptance is controlled only by the rotated class. Exactly g classes result from saturation, proving the minimal complete formula even for r=1, s=1, and r=s. The NFA never loses its C state, and there is no missing sink state to count. From the submitted scripts and logs I confirmed their stated methods and ranges without executing them. My separate python3 -B /workspace/reviews/modular_check.py uses Brzozowski double reversal and compares the quotient map and merging blocks on all 49 pairs through 7. Reached/minimized pairs include (r,s)=(1,7):128/128, (7,1):14/8, (6,4):24/20, (6,6):12/12, (6,7):768/763; 8176 direct binary word comparisons matched. The finite check supports, but is not used in place of, the CRT and right-language proof.

## originality

PASS

Best-of-knowledge pass for the two independently variable guards, the exact arithmetic quotient and its full list of identifications. The known modular-suffix exponential example is not itself original or needed as a priority claim. The paper's generic hardness motivation and the use of CRT, subset construction and Myhill–Nerode theory are prior tools.

## value

PASS

This naturally parameterized one-branch determinization example separates reachable subset count from minimal DFA count and explains every residual-language identification. It exposes which parameter, s/g, governs exponential growth, including linear growth when s/g stays bounded, and gives a reusable exact witness for congruence effects in restricted determinization. The joint structural classification, not the familiar free-prefix exponential example or a small table, carries the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
