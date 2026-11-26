---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The complexity counts and quantitative fiber/merger assertions hold. Complementation gives 0<β<1/2 with no 11. With s the first letter, the number of changes is K_n+K_(n−1)−s, so only t_1,t_(n−1),t_n affect the reduction, and successive regions give four different (s,changes) pairs. Counting ordinary rotation cells and summing their lengths gives the stated rank gaps and natural frequencies. An equal reduced Parikh vector for different reduced words requires the same even run count and opposite starting letters; the stated merger holds in every realized order. The list of cases is nonminimal: APT is impossible, since in the carry case { (n−1)β }>1−β>β forces P<A<T. The additional APT row is vacuous; if read as an attainability assertion it is false. TPA, TAP and PAT all occur. The length-one/two checks and restoration by complement are correct. An independent exact rational cell check (branches/replay_04.py) used 891 representatives of open slope-order chambers for 3≤n≤25, reproducing all actual orders, multiplicities, interval masses and mergers. The all-length result uses the symbolic argument, not this bounded check. The frozen verifier was read, not run.

## originality

FAIL

The record omits the decisive Sturmian 2-Abelian classification of Karhumäki–Saarela–Zamboni (arXiv:1301.5104v1, Proposition 2.8 and Theorem 4.1 with Lemma 4.2 and its proof). On factors with no 11 and a fixed length, put m=|w|_1 and let s,e be its first and last letters. The reduced word has m ones and m+1−s−e zeros and first letter s; these determine s,e,m, which in turn determine the reduced word. The same s,e,m characterize 2-Abelian equivalence by Proposition 2.8 (also directly by the counts of each length-two factor). Thus the four-type run reduction is the known 2-Abelian partition in another form. The prior proof identifies its cuts in lexicographic order at the three exceptional transitions j=1,n−1,n, exactly the three rotation breakpoints, giving the fiber sizes and, with the ordinary rotation-frequency correspondence, their frequencies. Reduced Abelian equivalence simply forgets the ordering of s,e, i.e. takes reversal orbits of the known types. Evaluating s,e,m on the known three cuts gives the displayed merger by direct substitution; it does not supply a substantively distinct classification.

## value

FAIL

The reduced complexities are motivated, but the exact four fibers are a known partition under the proved equivalence, and the new terminology for the three Abelian classes is obtained by directly forgetting endpoint order. The size and frequency formulas then sum those same cells. No independently useful unknown exact fact beyond this mechanical specialization is established in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
