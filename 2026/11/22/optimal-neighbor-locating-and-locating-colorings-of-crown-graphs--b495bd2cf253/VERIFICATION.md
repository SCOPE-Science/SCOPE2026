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

Every mixed independent class is a unique matched L_i,R_i pair. The remaining index set U gives pure-shore classes, and if U is empty the matched pairs cannot be distinguished. In a common pure left class, two vertices at indices i,j differ in either code exactly when one of their matched right endpoints is a singleton: all other pure left classes are at distance two from both, mixed classes at one, and a nonsingleton pure right class at one. A matched right singleton has distances three and one, respectively, contributing precisely the missing neighbor color. The argument is symmetric on the other shore. Same-colored matched vertices with U nonempty are distinguished by any pure left class (distances two and one and adjacency only on one side). This proves equivalence for every proper coloring. If there are p mixed classes and m=n-p residual indices, and r singleton and t nonsingleton right classes, each left class contains at most one of the m-r indices in nonsingleton right classes. Thus for t>=1 there are at least p+(m-r)+r+t>=n+1 classes; if t=0, the m right singletons and at least one pure left class give the same lower bound. The single pure left class and all right singletons show attainability. At equality with t>=1, t=1 and every left class has one index of the right block B. Symmetry permits at most one of those left classes to be nonsingleton, so all of U minus B join that class if the set is nonempty. This gives exactly the one-shore or two-block forms, with the one-index case counted only once. For fixed m this counts m*2^(m-1)-2m+2 partitions without names; binomial summation gives n*3^(n-1)-(n-2)*2^n-2. An independent proper-partition enumeration for n=3–6 found 41, 354, 4,125, 61,375 proper partitions and 17, 74, 307, 1,200 optima, respectively, with no discrepancies between the two coloring tests. That enumeration corroborates only the finite orders; the supplied programs were inspected, not executed.

## originality

PASS

The supported additions are the sharp all-order equality, equivalence at the level of each proper partition, and exact rigidity and enumeration. The twin-free upper bound is already implied and is not credited as novel. The only exact catalogue match is the assigned item.

## value

PASS

These two separation notions can differ on general graphs. On a natural dense bipartite family, the theorem identifies which geometric obstructions make the notions agree, characterizes every optimum rather than giving a single construction, and counts the optima as partitions of the given vertex set. The exact classification and labeled-vertex count add information not present in the standard upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
