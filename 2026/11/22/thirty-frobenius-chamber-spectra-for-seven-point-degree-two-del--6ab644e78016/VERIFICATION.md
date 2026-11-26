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

Ampleness of -K and adjunction imply every geometric negative curve is a (-1)-curve of anticanonical degree one. Beyond the seven exceptional divisors the plane degree d and multiplicities satisfy sum(m_i)=3d-1 and sum(m_i^2)=d^2+1; Cauchy with seven entries bounds d by three, leaving exactly the stated line/conic/cubic classes. Riemann–Roch and ampleness of -K realize each as effective and irreducible. A nonzero intersection of two such curves destroys negative definiteness of their 2x2 principal block. Conversely a disjoint support T has matrix -I. For a stable support, its orbit-sum divisor is rational over k, and D=-K+2 sum(T) has positive part -K+sum(T), nef and big with square 2+|T|, zero precisely against the curves in T. This D is interior: for ample A near -K, the nearby divisor A+2 sum(T) has positive part A+sum((A.C)C), nonnegative on all curves and big, and negative part sum((2-A.C)C), still with positive coefficients on T. Uniqueness gives the converse descent implication. The anticanonical map sends each exceptional curve isomorphically to a line; its paired lift is -K-C. This Geiser action commutes with the ordinary label permutation, and twisting multiplies Frobenius by Geiser. As an independent exact check, I indexed the 28 Geiser pairs by unordered point-label pairs with repetitions (diagonal for exceptional/cubic pairs), used the Picard pairing to form the compatibility graph, and enumerated cliques breadth-first by size. The counts were 1,56,756,4032,10080,12096,6048,576. I generated the 15 partitions from cuts of seven labels, computed each support's return period under both actions, and divided the period counts by the lengths. All 30 profiles and fixed counts match the printed table; the fixed-support size distributions also match the bundled JSON. Cycle lengths dividing the extension degree give exactly the displayed extension-field formula. The ordinary rank-three examples each have two point orbits plus H and different fixed counts, 11 and 13.

## originality

PASS

The geometric 33645 count, the exceptional configuration, and the relevant Weyl-group/Frobenius inputs are prior. The distinct claim is the evaluated action on every Zariski support for the specified 30 cases, including all extension degrees. Neither the compared chamber tables nor the broader tables of surfaces by Frobenius type give those support spectra. The exact catalogue hit for degree two is the assigned record itself.

## value

PASS

The support spectra distinguish arithmetic forms of a natural birational chamber decomposition, including two blowups of the same arithmetic Picard rank. They also give exact extension-field rationality and show what the central quadratic twist changes, for example three rational chambers versus one for a seven-point orbit. These are useful data that neither the geometric total nor a fixed-rank invariant contains, over a complete geometrically motivated family rather than an arbitrary collection of permutations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
