---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A player facing j other cooperators among L=n-1 has exact action advantage d_L(j)=-L/2+lambda[3j(L-j)-L(L-1)/4], obtained by counting j(L-j) mixed coplayer pairs and the two homogeneous triple cases. A k-cooperator pure profile is Nash iff d_L(k-1)>=0>=d_L(k), with all defectors always stable and all cooperators never stable. The resulting binomial labeled census holds including indifference. The discrete concave quadratic has maximum at floor(L/2), giving lambda_c=L/[2(3floor(L²/4)-L(L-1)/4)] and parity-sensitive first-appearance counts. Its descending zero crossing allows at most two consecutive cooperative k-values. The one-defector inequality d_L(L-1)>=0 is possible exactly for n<=12, at lambda>=2(n-1)/[(n-2)(13-n)]. Independently enumerated 1,240 exact rational payoff profiles; infinite-n proof is the combinatorial advantage identity and discrete concavity.

## originality

PASS

Best-of-knowledge PASS. Civilini et al. introduced the relevant two- and three-player payoff table and analyzed its continuum evolutionary/replicator cooperation transition in the fully inspected full paper and supplement. This is credited as prior motivation. The submitted theorem is a finite static pure-Nash census of all labeled profiles and a sharp parity/tie/onset and n=12/13 obstruction; the mean-field evolutionary bifurcation does not supply these integer pure-equilibrium counts. An equivalent anonymous game equilibrium classification could exist in unindexed literature.

## value

PASS

The complete exact Nash census of a physically motivated higher-order cooperation game is a natural small combinatorial model, especially because finite parity changes equilibrium multiplicity at the onset and there is a strict population cutoff for a one-defector state. This gives a benchmark without claiming stochastic adoption dynamics or a general hypergraph theorem; the enumerative answer itself is useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
