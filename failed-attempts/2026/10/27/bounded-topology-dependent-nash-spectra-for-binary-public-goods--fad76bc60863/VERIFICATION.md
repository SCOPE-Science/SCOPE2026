---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For exactly the degrees in scope, the stipulated response is equivalent to (I+A)x=1 over F₂. The set of solutions is nonempty since for any y in the kernel, yᵀ(I+A)y=yᵀ1=0, so 1 lies in the range of the symmetric matrix. For an independent count use the homogeneous rung recurrence z[i+1]=z[i−1]+Nz[i], with N=I+S and N²=0. Hence z[i+2]=z[i]+Nz[i+1], z[i+3]=z[i+1]+Nz[i], and z[i+4]=z[i]. The affine recurrence has the same period-four property since its additional constant e satisfies Ne=0 and cancels on the fourth step. Open ghost rungs at 0 and n+1 are zero; the homogeneous right constraint, in residue order 0,1,2,3, is z[1]=0, Nz[1]=0, z[1]=0, or vacuous. The cylinder imposes the nth shift as the identity; residues 0 and 2 leave 16 and 4 patterns, and odd residues force a constant in ker N (2 patterns). On the Möbius ladder the shift is S: residue 0 requires Nz[0]=Nz[1]=0 (4), residue 2 requires N(z[0]+z[1])=0 (8), and an odd shift squared is a two-shift, forcing both parity states in ker N, then forcing them to agree (2). The admissible sizes make the edges simple and include both initial rungs, so these counts are of distinct labeled vectors. Read the frozen direct brute-force and recurrence verifier without running it.

## originality

FAIL

The central cylindrical and twisted periodic censuses, as well as period four, are covered by a distinct stronger indexed calculation of the identical labeled solution sets, with the game merely a different interpretation of (I+A)x=1. The open row is not in that indexed theorem, but the known local recurrence specializes immediately to zero ghost rungs, with no new structural ingredient. The direct match is demonstrably later indexed; it does not establish historical priority against the frozen record.

## value

FAIL

A quantitative twist effect could be useful, but the closed comparison here just reinterprets stronger all-on polynomials. The remaining unweighted open row is a direct evaluation of the same local dynamics with zero ghost states. It does not supply an independent useful invariant beyond that routine specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
