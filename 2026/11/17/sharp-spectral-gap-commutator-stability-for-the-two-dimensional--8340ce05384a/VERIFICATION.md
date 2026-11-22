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

PASS. Traceless 2×2 Hermitian A,B correspond to Pauli vectors v,w with lengths r,s>0 and cosine u. Scalar-shift normalization cancels traces. The product trace is twice the affine chord L(x) of f(x)=cosh(sqrt x) over a=(r-s)² and b=(r+s)² at x=r²+s²+2rs u, while trace e^(A+B)=2f(x). The unnormalized Frobenius commutator norm² is 8r²s²(1-u²)=2(x-a)(b-x), so the noncommuting quotient is f[a,x,b]. Hermite–Genocchi representation and f'''(z)>0 for z≥0 imply strict increase with u and sharp endpoint constants f[a,a,b], f[a,b,b]. The f''(0)=1/12 and simplex integration of area 1/2 yield universal sharp lower 1/24 as r,s→0; equal gaps r=s→∞ force C+ to diverge exponentially, so uniform upper fails. Independent direct Pauli matrix checks at r=.8,s=1.4 and five orientations reproduce increasing quotient .0508009 to .0567817. Infinite continuum proof from positive entire power series, not sample. Commuting limit ratios are not defined but both original bounds vanish, and zero-gap slices contribute zero.

## originality

PASS

PASS, with residual possibility of an earlier specialized sharp matrix-inequality lemma. The Forrester–Thompson exact 2×2 Pauli trace formula is prior work; the submitted result optimizes its chord defect against squared commutator for arbitrary prescribed two half-gaps and establishes sharp bounds and strict angular monotonicity. A 2026 tensor-paper upper estimate without spectral-scale restriction is incompatible with the demonstrated large-gap counterexample and does not dominate this theorem.

## value

PASS

PASS. The theorem gives an exact stability modulus and identifies the sharp 1/24 universal lower boundary and impossibility of global upper bounds, clarifying a genuine false scale-free claim in active Golden–Thompson research. Fixed-gap extremizers and tensor slice implications are structural, not generic Taylor expansions or a textbook repetition of Golden–Thompson.

The dated certificate retains the supplied scientific assessment, sources and limitations.
