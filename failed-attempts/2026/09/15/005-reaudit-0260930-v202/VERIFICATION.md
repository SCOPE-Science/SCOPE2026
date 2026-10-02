---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

FAIL

There is a direct false mathematical assertion in the submitted RESULT: its Proof/evidence and Limitations assert that both SL(2)-parity branches exist topologically for the C+ open A1 fiber, and the C+ case assigns a nontrivial fiber-monodromy branch. But the complex affine line A1(C) is simply connected, so an ordinary rank-one local system on that fiber has no nontrivial monodromy. More fundamentally the cited primary HMSW II defines SL2-parity only for Q-real roots (Section 7, PDF p57 lines 4718-4728), whereas C+ is a Q-complex root (Lemma 6.5(v), p41); Theorem 8.7 pp64-66 formulates irreducibility using parity solely for real roots. Moreover HMSW II Lemma 6.5(v) says C+ open is precisely the Q-complex case with sigma_Q(alpha) negative, and Lemma 8.1(i) p59 forces alpha-coroot(lambda) noninteger whenever I(Q,tau) is irreducible there. The source's own wall and integral-difference hypotheses instead give alpha-coroot(lambda0)=0 and alpha-coroot(lambda) integer. Hence the entire C+ row has no admissible input under the stated hypotheses, not merely its nontrivial-monodromy subrow. Separately, the source assumes I(Q,tau)=L(Q,tau) at regular antidominant lambda and defines Phi(lambda0)=translation to the wall. Adams--van Leeuwen--Trapa--Vogan Corollary 16.9(2)-(3) proves translation of an irreducible module to the wall is irreducible or zero. Therefore no reducible translated output is realized under the given hypotheses. This alone does NOT refute the source's conditional 'length 2 iff both factors survive': both-survive could be an empty antecedent, and no such witness is supplied. The failure determination rests on the explicit false topological/parity assertion and invalid claimed C+ classifier, not an invented length-two counterexample. The all-n pushforward and counit claims remain unverified beyond that decisive error.

## originality

FAIL

The strongest prior comparison is explicit and directly broader on the advertised outcome question: the general Jantzen--Zuckerman wall translation theorem, as formulated in Adams et al. Corollary 16.9, applies to all real reductive groups and arbitrary singular walls, including SL(n,R) at a minimal wall, and determines zero by the wall-root tau-invariant. The record's non-vacuous three-outcome framing cannot be novel: the prior theorem allows only irreducible or zero for its irreducible source. Milicic's Theorem 2.1 already gives the regular-source irreducibility criterion via C^-(Q) and real-root SL2 parity; source 65 assumes this condition rather than proving it. An exact orbitwise translation of tau-invariant into HMSW survival data might constitute a separate refinement, but its correctness and novelty were not established. Exact Resultary search retrieved the assigned SCOPE005 self-entry; full primary reading exposed the controlling theorem.

## value

FAIL

The advertised non-vacuous three-way wall-crossing criterion has no realizable reducible outcome under its own irreducible-source assumptions, while the remaining simple-or-zero distinction and tau-invariant zero criterion are classical. The n=3 orbit census alone is not substantial at the stated claim level. A rigorously proved explicit orbitwise refinement would be a different claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
