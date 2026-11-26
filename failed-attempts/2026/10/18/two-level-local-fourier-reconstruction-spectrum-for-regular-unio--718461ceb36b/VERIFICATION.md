---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Fixed length and the local common-rotation slice impose the two zero-sum constraints. The reference modes 1 through m−1 vanish. Differentiation gives 2π Dc_k=−U_k+exp(−ikδ)V_k, δ=2πα/m, in unnormalized Fourier coordinates. For a conjugate pair k,m−k the complex two-row Gram matrix has diagonal 2 and off-diagonal modulus 2|cos(πα)|; the real input norm on this block has the Parseval factor 2/m. The even-m unpaired block has real U,V, Gram eigenvalues 1±|cos(πα)| and Parseval factor 1/m. These give exactly m(1±|cos(πα)|)/(4π²), each with real multiplicity m−1 (the values coincide at half duty), including m=2. The lower value is positive for 0<α<1. Taylor expansion on the separated labeled slice gives a uniform-in-direction cubic error for fixed m,α; singular directions attain the two optimal leading constants. The analytic inverse is local on this slice. The exact derivation verifies the theorem; the 45 numerical cases in the bound package were reported there and the script was inspected, not executed.

## originality

FAIL

A distinct published Resultary record contains the full constrained Jacobian theorem with the identical formula, multiplicities, condition number, local inverse and the same conjugate-frequency proof, and more. The energy bounds are an immediate Taylor consequence of that spectrum, not a distinct surviving claim. This is a finding of substantive overlap, not an inference about chronological priority or record lineage from catalogue dates.

## value

PASS

As a mathematical result, a sharp condition number for the minimal-dimensional local moment system at a natural regular family answers a substantive stability question not answered by qualitative global recovery. It shows independence of the number of arcs, loss of conditioning toward extreme duties, and the unique locally isotropic duty. This is meaningful content even though the independent originality assessment finds it already covered in a distinct record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
