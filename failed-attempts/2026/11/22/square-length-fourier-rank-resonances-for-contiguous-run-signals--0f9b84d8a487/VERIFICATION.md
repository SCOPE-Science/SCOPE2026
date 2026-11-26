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

The boundary map B(x)=(x_1,x_1+x_2,...,x_{n-1}+x_n,x_n) identifies the spatial Boolean cube with even words of length m=n+1 and sends the interval [a,b] to the weight-two generator at coordinates a-1,b, indexed from zero. Its dual gives the frozen prefix signs. The unnormalized eigenvalue is ((m-2j)^2-m)/2, with binom(n,j) frequency representatives having first coordinate zero and weight j. It vanishes only for m=s^2, when the two represented layers give total nullity binom(s^2,s(s-1)/2) by reflection and Pascal. The maximum absolute eigenvalue is the degree n(n+1)/2. At resonance, the nearest allowed absolute coordinate levels off s are s-2 and (if available) s+2, giving smallest nonzero absolute eigenvalue 2(s-1), including s=2. The condition number is on the surviving subspace, not the full singular operator. The complement of the zero-frequency mask has inverse Walsh kernel with the two stated Krawtchouk terms. Its counting-measure endpoint norms equal the absolute row/column sum. Averaging conjugates of any projection over translations fixes the range pointwise and does not increase either norm; Fourier diagonalization makes the averaged projection unique. Off resonance the projection is the identity. Stirling applied at the offset s/2 from m/2 (one standard deviation for a fair binomial of size m=s^2) gives the stated 2 sqrt(2/(pi e))/s lost fraction along resonances.

## originality

FAIL

The named arithmetic rank transition and complete spectrum are a direct recoding of the published halved-cube spectrum. This is exact conjugacy of the operators, not analogy by parameter. The surviving Hilbert numbers and Stirling estimate are direct evaluations of that spectrum. No source inspected explicitly prints the endpoint binomial sum for this notation, but it is the standard Krawtchouk shell expansion of the complement of a known Walsh eigenspace, with the usual translation symmetrization giving minimality. The frozen record does not go beyond this evaluation to a new endpoint estimate or structure. This FAIL rests on demonstrated coverage or mechanical implication, not on the unresolved order of same-day catalogue records or on an unsuccessful source lookup.

## value

FAIL

The interval convolution is a natural operator, but the asserted transition and recovery condition number re-express the known halved-cube spectrum and read off its closest nonzero squared levels. The remaining endpoint claim evaluates the canonical projector by the usual character-layer sum and averages over the group. It provides neither an independent unknown exact invariant beyond that mechanical evaluation, nor new estimates or structure for the endpoint norms. The three examples are useful checks rather than a separate scientific contribution. No worthwhile narrower repair of the frozen claims is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
