---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An endpoint removes one pair; an internal deletion of the middle of abc changes the profile by −e_ab−e_bc+e_ac. Enumerating the eight triples and four endpoint pairs gives six distinct changes. Translating by the original profile preserves distinctness. The pair-path formula imposes both endpoints, even when n=2 and they coincide (the sole pair disappears, giving N_1(2)=4). For a word with realized set S, summing t^|T|(1−t)^(6−|T|) over T containing S gives t^|S|, so the allowed-feature transfer enumerates exactly the desired statistic. Independently constructed all 64 matrices from the change vectors and computed their transfer fractions as bordered determinants: with U=I−zM_T, multiply det([[U,v_T],[−v_T^T,0]]) by z² and divide by det(U). After multiplication by J, each of the 64 fractions divided exactly as a polynomial; summing with binomial weights gives zero for each cross-product difference against the six frozen P_j/Q_j. This checks the identities for all lengths. A separate literal enumeration through n=14 also agreed. The first sixth-class term is 12z^9, with no lower term. Both cross-pair changes require opposite boundary pairs (probability 1/8 for n≥4); conditioned on them, disjoint triples entirely within the interior miss one of 000,111,010,101 with probability at most 4(7/8)^floor((n−4)/3). Thus the asymptotic limit is 1/8. The frozen scripts were inspected, not executed.

## originality

PASS

The six local deletion changes and the implication from deletion saturation to insertion saturation receive distinct same-day coverage. The surviving claim is the exact six-way one-deletion law, including its attainable cutoff, multiplicity and asymptotic frequency. No inspected distinct statement supplies this law. The insertion classification imposes different local events and its numerical answers do not carry across to deletion. There is residual risk from older histogram-channel terminology and one inaccessible Markov-type paper.

## value

PASS

The projected deletion ball is a natural combinatorial observable: identical pair multiplicities can merge distinct edited words. Exact all-length class frequencies answer what is lost under this projection. The exact onset and nonzero limiting frequency of saturation give useful boundary data beyond the six-vector upper bound or a sample table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
