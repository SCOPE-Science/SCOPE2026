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

Track zero residue a, scattered-pair residue c and trailing-zero length truncated at r. At length r no continuation containing 1 is legal, and all-zero continuations preserve c, so the terminal right languages are exactly 0* and the empty language, the latter shared with the sink. The witness 01^(t+1)(01)^(k-1)0^j realizes any active (a,c,j): choose positive k congruent to a-j and nonnegative t congruent to c-k(k+1)/2; each zero-run followed by 1 has length one. For any active j, the legal suffix 1^b 0 1^d leaves residue c+a(b+d)+d. For each chosen total f modulo m, choose d=-c-af and b=f-d modulo m, represented by positive integers. This accepts from (a,c) and leaves residual (c'-c)+(a'-a)f from (a',c'). A nonidentical pair is distinguished by one of f=0,1, without assuming a field or dividing by two modulo m. For identical counters and j<j'<r, first add r-j' zeros and use the same family of suffixes: the larger run is forced to reject and the smaller admits a zero residue. The active states admit a continuation containing 1, so they differ from both terminal classes. For r=1 the avoidance language is 1*0*, the count is identically zero and the three distinct right languages are 1*0*, 0* and empty. Independent zero-budget quotient enumeration and positional word checks agreed for 42 parameter pairs including r=1, m composite, and short and long trailing runs. Replay: `python3 /workspace/branches/review_checks.py 2`.

## originality

PASS

Earlier exact results cover the two components separately, and a general product gives only an upper bound. The exact active classes and the collapse from all long-run counter states to two terminal right languages are distinct. Other close indexed constrained counters change the scattered pattern, the forbidden factor or the invariant. The comparison supports the specified interaction, not priority for modular pair counters or forbidden-factor automata in isolation.

## value

PASS

The result is an exact quotient for a motivated combination of a local run constraint and a global modular count. It resolves where the standard product wastes states: residues cease to matter except for acceptance when the run reaches r, but none of the active residues or run lengths collapse. This quantifies a real interaction uniformly over composite moduli, and the r=1 change illustrates precisely when the count becomes vacuous.

The dated certificate retains the supplied scientific assessment, sources and limitations.
