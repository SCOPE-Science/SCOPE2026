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

For each 1 let k be its number of preceding zeros and let A be the total number of zeros. With B=sum k and Q=sum k², the scattered count is AB-Q. Hence Q-B is even, imposing the stated residue condition modulo gcd(2,m). Conversely the pairs (1,1),(2,4) span all (B,Q) with this condition because (2,4)-2(1,1)=(0,2). Represent their coefficients by nonnegative multiplicities and choose the preceding-zero counts strictly increasing using multiples of m. This gives legal separated 1s and any specified A residue, ending in 0. To end in 1, reserve the last marker at A and subtract (A,A²) in residue coordinates, which preserves the parity condition; choose A large enough for the remaining markers and require a zero before the reserved 1. The exact letter actions are 0:(a,b,c)->(a+1,b,c+b) and 1:(a,b,c)->(a,b+a,c); their m-th powers are identities. Prepending 0^m and inserting 0^m before each 1 preserves the full counter action and makes the suffix legal from either boundary flag. Thus a safe inverse returns any chosen triple to (0,0,0) and sends another distinct triple to a nonzero triple. Read c immediately if nonzero, or append 0 if only b is needed, or append 0^m10 when c=b=0 to expose a; the base stays at output residue zero in each comparison. Equal triples with different flags are separated by 1 followed by a safe accepting continuation. Every legal state has an accepting continuation, unlike the sink; the empty prefix needs no extra boundary flag. This yields exactly the asserted Boolean quotient for odd and even m. An independent moment-coordinate DFA and positional enumeration agreed for all ten m=2..11. Replay: `python3 /workspace/branches/review_checks.py 1`.

## originality

PASS

The unrestricted modular output-state size and its parity-restricted orbit are already known. The distinct claim is the complete Boolean quotient under the additional Fibonacci constraint. Its proof shows that the full legal counter orbit is retained, that legal suffixes distinguish different counters even for Boolean acceptance, and that each counter has two distinguishable legal boundary states plus the global sink. The indexed and primary comparisons do not establish prior coverage of this result.

## value

PASS

This gives a sharp deterministic memory bound for a natural binary run constraint and scattered statistic. It explains why the constraint preserves the counter transformations but still requires two legal copies of every counter state when recognizing the Boolean language. The parity-dependent cubic law and the sink term quantify effects neither an orbit count nor an avoidance automaton alone determines.

The dated certificate retains the supplied scientific assessment, sources and limitations.
