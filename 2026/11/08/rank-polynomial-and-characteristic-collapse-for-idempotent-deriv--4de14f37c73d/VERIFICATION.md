---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: Reconstructed all derivations from [U,U]=[W,W]=0 and the independently labeled U tensor W brackets (a,b>=2 eliminate off-diagonal quotient blocks). The invariant-center action is S=A tensor I+I tensor B with arbitrary central shear. The idempotence equations T^2=T, S^2=S, S Phi+Phi T=Phi yield A,B projections and S^2-S=2 A tensor B; thus odd characteristic demands ij=0, while characteristic 2 has unrestricted i,j. The allowed Phi eigenspace blocks have dimension (a+b-i-j)s+(i+j)(ab-s), s=i(b-j)+(a-i)j, giving precisely the stated rank t+s and Gaussian-binomial multiplicities. For balanced n in odd characteristic, the log-q weight is (3n^2+2n)k-(2n+2)k^2 with maximizer ~3n/4. In characteristic 2, the A=B=I stratum alone has q^(2n^3) maps of rank 2n; all competitor exponents are separated by order n^2. Checked the actual verify.py construction of the Phi nullspace and source code; the explicit finite-field histograms are corroborative, not an asymptotic proof. A test of q=2,n=2 gives the formula 1+3072 z^3+74752 z^4+3072 z^5+512 z^6.

## originality

PASS

PASS (best of knowledge): The examined graph-Lie derivation literature gives structural blocks and derivation dimensions but not the complete finite-field idempotent-operator rank census with arbitrary shears, and related idempotent-derivation rank spectra are for nonisomorphic Lie algebras. The odd/characteristic-two concentration law is a separate claim beyond the original graph algebra framework. A general unlocated counting theorem for two-step nilpotent graph Lie algebras remains possible.

## value

PASS

PASS: The number of distinct idempotent derivations of each operator rank is a natural invariant of a precisely specified graph Lie algebra, not a generating-set rank or arbitrary restriction. The stark fixed-field transition (typical rank quadratic in n in odd characteristic but linear in n in characteristic two) is mathematically structural and is not determined by the existence of gradings or Lie algebra dimension. The center shears are an essential, nontrivial part of the actual operators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
