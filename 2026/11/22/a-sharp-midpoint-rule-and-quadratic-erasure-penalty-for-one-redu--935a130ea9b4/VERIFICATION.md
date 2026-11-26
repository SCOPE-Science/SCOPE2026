---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

After deleting a grid row uⱼ, the row Gram matrix consists of an (N−1)-dimensional identity block, a unit diagonal entry for the new row, and a coupling vector of norm √(1−|aⱼ|²), where aⱼ is the deleted basis coefficient of the new unit row. Restricting to the two coupled directions gives eigenvalues 1±√(1−|aⱼ|²), also valid for N=2; deleting the added row instead leaves the identity. Both the best worst-erasure lower squared singular value and the best worst-erasure condition number therefore reduce to maximizing minⱼ|aⱼ|. The geometric sum gives the stated common numerator; the largest denominator comes from the grid point nearest the antipode, with distances in grid units t for even N and 1/2−t for odd N on 0<t≤1/2. For even N the numerator increases and the denominator decreases on the half-gap. For odd N, in x=1/2−t, the log derivative of cos(πx)/cos(πx/N) is strictly negative since tan(πx)>(1/N)tan(πx/N). Reflection and grid rotations give exactly the midpoints and the stated parity constants. Non-grid coefficients are all nonzero; at a grid point a duplicate fails when a different row is lost. Expanding γₙ=1/N+O(N⁻³) gives B*=1/(2N²)+O(N⁻⁴) and the rationalized condition number κ*=(1+√(1−γₙ²))/γₙ=2N+O(N⁻¹). The uniform regrid comparison follows by subtracting a unit projector from (N+1)I/N.

## originality

PASS

The rank-two replacement formula and Fourier cardinal functions have close precedents. The supported distinct claim is the exact all-N placement optimum when the entire critical grid stays and any one of its rows or the added row can be erased, including parity constants and the sharp penalty relative to regridding. The closest indexed results optimize different designs or do not take the worst erasure of this retained grid.

## value

PASS

Retaining an existing sampling grid while adding one measurement is a natural design constraint. Exact recovery alone hides a loss of robustness: the sharp squared lower singular value scales as N⁻² rather than the N⁻¹ of an equally weighted regrid with the same row count. The optimizer, parity effect and loss quantify what cannot be avoided by moving the one available sample. The substantive contribution is this constrained optimum, not the elementary computation for a single known deletion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
