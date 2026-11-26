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

Legendre gives V=s₂(3n)−ν₂(3n+1)=s₂(3n+1)−1. For an independent all-depth derivation write 3n+1=a·2^L+b with 0≤b<2^L and a∈{0,1,2}. For each b exactly one a makes a·2^L+b≡1 mod 3, giving a bijection, including at L=0; a=0 iff b≡1 mod 3. Thus V=K−I with K=s₂(b), I=1_{b≡1 mod 3}. If R_L(t) sums t^K over b≡1, the cubic root-of-unity filter and alternating residues of binary places give Σ_L R_L(t)z^L=(1/3)[1/(1−(1+t)z)+(−1+(2t−1)z)/(1−(1−t+t²)z²)]. In each two-bit factor the two nontrivial character terms have paired product 1−t+t². Substituting P_L=(1+t)^L+(t^−1−1)R_L gives the advertised rational function (R_L has no constant term in t). V=0 is exactly b=0 or b=2^i with even i, giving 1+ceil(L/2). At even L the all-ones b has residue 0 and is the sole maximizer, with a=1 and n=(2^{L+1}−2)/3. At odd L it has residue 1 and loses one; each single-bit deletion has residue 0 or 2 and joins it at the maximum L−1. Uniform b gives K binomial(L,1/2) and p=E I=(1−(−1)^L/2^L)/3. The same character filter gives Cov(K,I)=0 at even L and 2^{−L−1} at odd L: differentiation at t=1 of the paired factor contributes exactly L/2 for even L, while for odd L the unpaired digit contributes 1/2 to the covariance numerator before dividing by 2^L. The variance L/4+p(1−p)−2 Cov(K,I) is exactly the displayed formula. The bounded difference |V−K|≤1 proves the stated Gaussian limit from the binomial limit. Separately, exact binomial quotients were checked against the recurrence for all 8,191 index instances in L=0,…,12, including the edges and exact moments; this corroborates the unrestricted proof.

## originality

PASS

The distinct result is the evaluated all-depth binary valuation census of the fixed quaternary sequence and the exact edge and moment formulas. Earlier general modular representations directly cover the same coefficients at fixed precision; classical enumeration, Legendre arithmetic, digit filters and finite-state methods are not claimed new. The passages examined do not supply the evaluated full census or a stronger evaluated distribution that specializes to it.

## value

PASS

The quaternary sequence is classical; its complete valuation histogram over exact dyadic blocks is a natural divisibility invariant. The all-depth enumeration distinguishes an isolated even-depth maximizer from L+1 odd-depth maximizers and quantifies the exact bias and variance corrections to a binomial law. The binomial-scale limit is elementary once the counting reduction is made, but it is not the basis of value on its own. The evaluated census and sharp edges are usable without recomputing individual modular tree counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
