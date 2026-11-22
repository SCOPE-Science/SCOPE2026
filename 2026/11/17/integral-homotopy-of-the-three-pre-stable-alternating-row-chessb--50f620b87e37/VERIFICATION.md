---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For n=4,5,6, A4 acts freely on oriented cells in the sense of no inversions because chosen rook columns are fixed and distinct. Orbit cells in dimension 0..3 have counts (n,binom(n,2),2binom(n,3),2binom(n,4)); a two-orbit parity label gives d2 triangle incidence identical for ± and d3 u^eps=t_jkl^{-eps}-t_ikl^{eps}+t_ijl^{-eps}-t_ijk^{eps}. The one-skeleton is complete and 2-cells fill all triangle loops, so every quotient is simply connected. Independently reconstructed the exact integer parity-orbit boundary matrices for all three widths and computed Smith forms: n=4 d1=1^3,d2=1^3,d3=1^2; n=5 d1=1^4,d2=1^6,d3=1^9; n=6 d1=1^5,d2=1^10,d3=1^24 plus 3, with d2*d3=0. The unit d2 forms and simple connectivity allow a wedge-of-S2 model for the 2-skeleton; pi2=H2 and integral diagonalization of 3-cell attaching maps give Q4=3S2, Q5=5S2+S3, Q6=5S2+Moore(Z/3,2)+5S3. Thus torsion is integral and the claim is only finite widths, no n>=7 extension.

## originality

PASS

Qualified PASS: classical ordinary (unquotiented) chessboard complex homology, general connectivity and 2026 generalized chessboard results do not provide A4 row-orbit CW boundary operators. Published A4 four-row quotient findings at n=7 and n>=7 concern different widths and do not imply their n=4,5,6 homotopy types or the sharp first three-torsion emergence at n=6. The primary 2026 paper was inspected in full PDF, including theorems/appendices; no matching quotient theorem identified.

## value

PASS

The three natural pre-shellability widths give a complete, non-arbitrary finite boundary classification for a symmetry quotient of a standard chessboard complex. The transition at n=6 to a genuine order-three Moore summand is invisible in rational ranks and scientifically useful for equivariant integral topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
