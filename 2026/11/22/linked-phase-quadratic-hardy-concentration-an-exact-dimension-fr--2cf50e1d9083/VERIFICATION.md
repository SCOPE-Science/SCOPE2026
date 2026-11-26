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

Independent reconstruction: after fixing the phase of z1, the two relative phases are independent Haar angles and each half-circle Fourier integral is 1/2 at zero, zero at nonzero even indices, and sin(pi*j/2)/(pi*j) otherwise. A mismatch in any outside exponent integrates to zero. Normalizing Dirichlet radial moments cancels d(d+1) because both monomials have total degree two. The all-internal sector gives B2; choosing one outside coordinate gives one B1 for each of d-3 choices; choosing an outside quadratic monomial gives one scalar 1/4 for each of (d-3)(d-2)/2 choices, including zero copies at d=3. In B2 split the pairs (z1z3,z1z2) and (z3^2,z2^2) into normalized sums and differences, keeping z1^2 and z2z3 fixed; this gives the stated B+ and B-. B1 has antisymmetric eigenvalue 1/4-1/(4*pi); on the symmetric sector its off-diagonal is sqrt(2)/8, giving the two stated radical values. An independent interval calculation by diagonal similarity removing sqrt(2), Machin bounds and outward determinant arithmetic certified the four B+ endpoint sign pairs (+,-),(-,+),(+,-),(-,+), and the two B- pairs (+,-),(-,+). It also separates the B1 eigenvalues into (0.100,0.112), (0.170,0.171), (0.470,0.473). Degree exhausts the roots, and the extrema, simple and both from B+, are about 0.0490369093591 and 0.638963446318. Their ratio agrees with 13.0302552642263; it is the squared singular-value condition number. No simulation is needed for the claim.

## originality

PASS

Credit standard normalized moments, torus symmetry and finite-section spectral methods. The strongest matched exact statements treat different angular symbols; neither their spectra nor the inspected general block theorem contains the specific joint-cell eigenvalues, multiplicities or sharp constant. This is a best-of-knowledge conclusion, not priority certification.

## value

PASS

This is a natural next restriction after the single-phase wedge: two sign tests sharing a coordinate, with the goal of measuring loss of information rather than merely finding the cell volume. The complete quadratic spectrum answers both concentration and stability questions; the sharp universal condition number and its attaining sector distinguish this joint mask from the one-wedge benchmark. This is a useful exact low-degree benchmark, not a claim of a general Toeplitz theorem or a result for real spherical harmonics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
