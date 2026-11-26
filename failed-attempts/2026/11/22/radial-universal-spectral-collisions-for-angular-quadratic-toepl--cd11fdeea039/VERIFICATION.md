---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Scalar rotation reduces the operator to homogeneous blocks. On degree d, conditioning on the radius cancels the same positive moment in numerator and denominator. Dividing independent complex Gaussian moments by the corresponding radial Gaussian moment gives the uniform sphere integral 2*alpha!/(d+2)!. Comparing monomial inner products gives (z_i partial_j+delta_ij)/(d+3); the order of the indices agrees with the stated z_i times conjugate(z_j) symbol. This is a scalar trace term plus the differential symmetric-power action of A. An invertible change of basis triangularizing A also triangularizes this action with the occupation sums on the diagonal, even in a Jordan case. At degree zero this gives tr(A)/3. Combining repeated levels yields one or d+1 distinct values, and independent gaps give one value per occupation triple. For dependent distinct gaps choose primitive 0,p,q, unique up to reversing the endpoints as clarified in the assumptions. Equal sums require the difference of the middle occupations to be divisible by q; replacing q middle copies by q-p lower and p upper copies gives exactly one representative with middle occupation below q. Counting those representatives gives the series, linear form and exact first collision at q. Nilpotent matrices have only one spectral value on each block, not necessarily a scalar block. Independent replay /workspace/replay/05.py compared 20 exact full characteristic polynomials from angular moment matrix entries with the occupation prediction, including conjugated nonnormal matrices. Finite replay corroborates the proof; it does not establish all block degrees. Frozen checker inspected but not executed.

## originality

FAIL

No inspected paper is asserted to state the four cases in this wording. The exact problem is nevertheless mechanically covered: the published finite-degree projective Berezin transform gives the angular quadratic block including its scalar normalization; separation of the single radial moment is immediate for a degree-zero symbol. The spectral set is then the elementary triangular symmetric-power spectrum, and the only nontrivial-looking cardinality case is the standard Hilbert function of a degree-q plane monomial curve. Neither allowing arbitrary radials nor allowing complex nonnormal A obstructs the reductions. This concrete chain, not a query miss or the mere fact that some methods are known, defeats the novelty of the frozen exact invariant.

## value

FAIL

The motivating block-spectrum growth question is worthwhile and the formulas are a useful example. In this special family, however, the frozen output is a routine specialization of exact projective action followed by a standard three-point sumset/Hilbert-function calculation. Radial realization and nonnormality do not add new cases to the resulting distinct-value problem. No independently new invariant or surviving valuable repair is present in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
