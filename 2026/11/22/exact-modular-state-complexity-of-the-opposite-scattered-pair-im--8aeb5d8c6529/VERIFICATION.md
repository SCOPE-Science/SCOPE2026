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

The appending rules are exact: a new 0 creates b new 10 pairs, and a new 1 creates a new 01 pairs. If c counts 01 pairs, then d=2c-ab, so the allowable residues are exactly d+ab divisible by g=gcd(m,2). At fixed residues a,b choose actual counts a+m,b+m; adjacent swaps traverse every 01-count between zero and their product. Thus every c residue occurs, giving precisely m^3/g reachable states, and the same argument realizes all allowable suffix triples. For a suffix with letter-count residues A,B, the endpoint imbalance is d+E+aB-bA. Each of the choices (-a,0), (-a,1), (-a+1,-b) can produce acceptance from (a,b,d), since one final letter count is zero modulo m. If all three also accepted from another state, subtraction of the resulting affine equalities gives first delta a=0, then delta b=0 and delta d=0, without division (hence also for even or composite m). This proves minimality of the complete DFA. Independently, the triples form the concatenation group and the accepting subset d=0 has trivial left-translation stabilizer: the identity forces a stabilizer's d=0 and the two unit-axis elements force b=a=0. Hence all reached states have distinct suffix languages. Replay: RESULT.md lines 24–66. VERIFICATION.md and verify_modular_pair_balance.py report finite checks; the uploaded code was inspected but not run.

## originality

PASS

The supported contribution is the exact number of right quotients for this binary zero-imbalance language over all moduli. Parikh pair counts and their sum, modular group counters, and permutation-automata methods are background. The examined sources do not establish this specific quotient size and acceptance minimality together. Strong nearby indexed records are distinguished by their actual available statements, not by date or title.

## value

PASS

This is a natural modular order-sensitive analogue of a letter-balance test. The exact deterministic memory requirement matters even for simple counters: the parity obstruction halves the state space at every even modulus, but no further quotient arises from testing only zero. The latter is an all-modulus minimality theorem about decision rather than output, not the routine construction of a product counter or a tiny computed instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
