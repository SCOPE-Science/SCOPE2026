---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The written two-certificate lemma I={N:R(N)>=2}=(ab+<a,b>) union ((a+cb)+<a,b>) is correct: a positive z produces a d+S witness and two z=0 solutions differ by integer multiples of (b,-a), forcing an ab+S witness. Conversely d+S and ab+S each yield two distinct coefficient triples. Minimal representatives of S in bj mod a are bj, giving exact thresholds ab+bj for j<c and a+bj otherwise; closure by adding a yields all subsequent same-residue integers. The maximum comparison uses bc-a>0. The one-genus and one-Sylvester sum follow from finite arithmetic progressions, including N=0. The Pell recurrence preserves gcd and c=u<a for i>=3. A separately written integer-DP check verified 923 coprime parameter triples and 329,758 values of N, including exact residue thresholds, g_1,n_1,s_1; this is finite corroboration, not proof of all-parameter quantifiers.

## originality

FAIL

FAIL due to decisive prior mathematical implication. The 2026-10-13 published RESULT for three consecutive Pell-type numbers proves a more general arbitrary-coprime A<B and C=A+uB first-crossing formula for u>=2 (in its proof, beyond its Pell specialization). Setting p=1 and u=c gives the exact submitted two-layer Apéry threshold for every c>=2 in the claimed domain; its published g_1 coincides. Lemma 1 of Komatsu and Mu (arXiv:2307.08998v2) already derives genus and Sylvester sums mechanically from an Apéry set. The leftover c=1 is covered by the 2026-10-26 complete multiplicity phase for (a,b,a+b), including g_1 and genus; its threshold and Sylvester sum follow from the same elementary finite formulas. The new paper contributes a different simple two-certificate proof but no surviving distinct final invariant.

## value

FAIL

The mathematical problem is intrinsically natural (counted representations with a redundant third coin), but the submitted p=1 Apéry thresholds and Frobenius invariant for c>=2 are already part of a previously published and more general p-threshold theorem. The c=1 low-multiplicity case is covered by a published co-generated triple classification. The genus and Sylvester-sum expressions are immediate universal Apéry formulas after substituting known thresholds. A different short proof of the same values, without a new motivated invariant, remaining stronger statement, or independently valuable structural obstruction, is not an original scientific contribution meeting the value bar. This is a rejection on positive earlier coverage, not a lack of online matches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
