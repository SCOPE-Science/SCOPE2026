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

The probability-measure addition kernel for exact degree j on S^3 is (j+1)U_j, since U_j(1)=j+1 and the degree dimension is (j+1)^2. For cumulative cutoff L and positive W the sample Gram is W^(1/2)K_L W^(1/2). The two signed-axis and corner sectors give the proposed adjacency diagonalization: the corner cube is diagonal in Walsh degrees, with values 4-2k, the rectangular incidence block only couples degrees zero and one, and the constant and linear coupled blocks give eigenvalues (8,-4) and (4,-2) respectively. The other even modes contribute nine zeros and one further -4, while the other odd modes give four further copies of -2. Thus the common sectors of antipodal parity and 1/2-adjacency, in order (constant, even -4, even 0, odd 4, odd -2), have dimensions (1,2,9,4,8). Substituting the five possible inner products in the normalized kernels gives exact-degree sample eigenvalue rows (1,0,0,0,0), (0,0,0,1,0), (0,0,1,0,0), (0,0,0,0,2), (0,5,5/3,0,0); adding the rows up to each cutoff gives exactly the claimed cumulative ranks and L=4 spectrum. Positive weights preserve ranks by congruence. The cube-root coloring is flat, even, sum zero and has adjacency eigenvalue -4 by neighbor counts. Testing W^(-1/2) times this vector and the all-ones vector gives the two Rayleigh bounds with common denominator sum_x 1/w_x and eigenvalue ratio five. Equality forces the constant-vector test to be a minimum eigenvector, giving constant weights entrywise. The reciprocal polynomial takes values 1/lambda at all four eigenvalues; the kernel-based interpolation formula is the unique minimum-norm solution by orthogonality to the restriction kernel. The arguments apply to all strictly positive weights and count the two points of each antipodal pair separately. The frozen finite matrix checker was read but not executed.

## originality

FAIL

The exact ranks and band spectrum are mechanical sums of the normalized exact-degree spectra on common eigenspaces stated in a distinct indexed theorem on the same 24-cell. The weighted optimum and uniqueness, although not stated in that record, then follow from the published diagonal-preconditioning feasibility formulation by transitive averaging and its positive-semidefinite equality case at the constant minimum eigenvector. No independent spectral or conditioning invariant remains beyond these implications. This is verified mathematical coverage in the inspected sources, not a historical claim of priority based on catalogue dates.

## value

FAIL

Both the cumulative interpolation slot and optimal weighting are meaningful questions for these standard nodes. Here the exact ranks and spectrum are a sum of already specified common spectral blocks, the exact inverse is ordinary interpolation of 1/t on those eigenvalues, and the weight characterization follows directly from the known feasibility formulation and symmetry, with the constant-vector equality condition. The frozen work does not establish a distinct valuable mathematical invariant beyond these deductions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
