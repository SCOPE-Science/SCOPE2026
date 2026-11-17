---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The exact Markov state (a,b,h) has intra-clique rates binom(a,2), binom(b,2), cross rate lambda h, and a hypergeometric loss in h after an internal dimer. On s=nt, the limiting vacant proportions and matched overlap are (1/(1+s),1/(1+s),1/(1+s)^2), yielding Poisson crossing intensity lambda/(1+s)^2. A bounded supermartingale Lyapunov F=h/a+h/b controls crossings after S/n by O(1/(1+S)), completing X_n=>Poisson(lambda). At jamming each clique has at most one vacancy; each cross-dimer removes one on either side, giving pathwise R_n=2 1_{n-X_n odd}, and the parity probabilities follow from the Poisson pgf. The proof's worst-case generator inequality was compared to the full earlier exact derivation and verifier state recurrences. The finite-state verifier code uses correct hypergeometric rates; no claim of having rerun its whole script is made.

## originality

FAIL

FAIL by direct exact prior mathematical coverage. The full published October 26 Resultary theorem has precisely the same graph (two K_n linked by n paired matching edges), internal unit rates and bridge rate lambda, proves the same limit X_n=>Poisson(lambda) and same pathwise terminal defect U_n=2 1_{n-X_n not congruent to 0 mod 2}. It additionally includes lambda=0. The submitted record on November 8 with lambda>0 is wholly contained in the earlier result, not a new theorem. Both source full proofs, including the same count-state fluid and Lyapunov argument, were read.

## value

FAIL

FAIL independent-value bar: the entirety of the conclusion and its parity-jamming interpretation is printed in a stronger earlier theorem, with the same exact graph and rates, so this submission adds no separate classification, counterexample, or motivated invariant beyond rederiving known mathematics. Correctness and replication do not restore scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
