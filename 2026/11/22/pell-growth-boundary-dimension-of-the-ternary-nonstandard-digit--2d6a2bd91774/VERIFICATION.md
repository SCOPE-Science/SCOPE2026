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

I reconstructed the carry and count certificate in RESULT.md §§1–4. Unique representatives of the three residues force the least-significant-first carry; the reachable states from zero are 0, −1, −2, and leading zeroes cycle the two negative states rather than rescuing them. For a most-significant prefix its acceptance set is the preimage of {0}; appending a digit takes one further preimage. Full and empty are absorbing, and the proper nonempty subsets give the displayed six-state graph. From there every mixed state can reach A, and from A the extensions 12 and 212 reach acceptance and rejection, respectively. Thus mixed cylinders actually contain positive-measure pieces of both eventual outcomes. For an independent exact count, the transient graph has an equitable partition {A,F}, {B,U}, {D,V}, with rows (2,1,0), (0,1,1), (1,1,0). Its characteristic polynomial is (t−1)(t²−2t−1), so initial counts 1,3,8 give the claimed numerator 1 and denominator by the recurrence. The quotient has a positive eigenvector at λ=1+√2, which lifts to the full graph. The undetermined unions decrease and their measures are O((λ/3)^n); absorption proves eventual stabilization almost everywhere. Away from the countable ternary endpoints there is a unique nested coding, and the two-sided cylinder test identifies the essential boundary exactly with the survivor image there. For the lower bound the digit-labelled Perron measure assigns O(λ^{−n}) to a level-n cylinder. An interval with 3^{−n−1}<|I|≤3^{−n} meets at most a bounded number of those grid intervals, giving the stated Frostman exponent; the cylinder cover gives the upper box bound and hence both box dimensions of the compact survivor image. Countable endpoint differences are used only for Hausdorff dimension of the essential boundary. verify_boundary.py was inspected, not executed; the independent quotient proof is exact and unbounded.

## originality

PASS

The distinct contribution is the ambiguity-prefix law and the essential-boundary dimension (with box dimensions for the compact survivor image). The same integer language, Pell block-count phenomena and measurable scaling convergence are already prior; exponential L¹ convergence of indicators in Zhou also implies almost-everywhere eventual stabilization by Borel–Cantelli. They are background, not independent novelty claims here.

## value

PASS

The measurable limit was known, but the essential boundary gives a representative-independent measure of where local membership is genuinely unstable. The exact prefix law and dimension quantify this exceptional set for the specific digit system already studied for its Pell structure; positive mass of both outcomes, rather than just finite-scale variation, makes the dimension geometrically informative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
