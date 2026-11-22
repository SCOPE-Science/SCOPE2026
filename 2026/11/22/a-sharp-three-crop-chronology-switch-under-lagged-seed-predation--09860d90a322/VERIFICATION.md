---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

The result's six proof steps establish the three-cycle formula, cancellation of reversal-invariant terms, the alternating three-point identity, both factorizations, the unique positive Holling-III threshold, and period minimality. A stand-alone Python standard-library program, `check.py`, evaluates the three-cycle independently from the recursion and matches it with the claimed expression using exact rational fractions. Running `python check.py` produced `exact-rational assertions passed: 6066`.

The specifically demonstrated crop and predator parameters are \((A,B,C)=(3,2,1)\), \(\rho=1/2\), \(\eta=1/20\) and \(b=0\). The checker confirms \(\Delta_3(2)=1/325\) and \(\Delta_3(4)=-8/14875\), and direct fractions establish that the annual modeled consumption is below seed availability in both orientations. The analytical proof, rather than finite randomized tests, supports universal quantifiers over \(A>B>C>0\), \(0\le\rho<1\), \(b\ge0\), \(\eta>0\), and \(K>0\).

The formula does not describe transient predator populations, feedback of seed predation on future crop availability, spatial migration, or statistical noise. A conditional predation-loss proxy is not interchangeable with measured ecological fitness. Published-priority comparison is based on available full text of primary ecology papers and two related mathematical results, additional research summaries, and explicit implication comparisons; the absence of a search hit is not a proof of global novelty. Independent audit was not performed.
