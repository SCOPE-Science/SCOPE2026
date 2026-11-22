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

Finite ascent ker T^p=ker T^(p+1) stabilizes all higher kernels; hence T and every power are injective on the algebraic ran T^p, even if it is not closed. For x with arbitrary-order lifts, set z_n=T^p y_(n+p) for independently chosen lifts. Each z_n is the unique ran T^p solution of T^n z_n=x; therefore T z_(n+1)=z_n automatically without a compactness or completeness assumption. Choose near-infimal unrelated y_(n+p) to obtain one same-chain estimate ||z_n||<=||T^p||(1+1/(n+p+1))a_(n+p), and use fixed-shift limsup roots and the obvious reverse inequality. Empty lifts give both +infinity; zero x gives zero. For T(a,f)=(∫f,tf), direct multiplication gives ker T^n=C⊕{0} for n>=1 and T^n(a,f)=(∫t^(n-1) f,t^n f); x_s=(-log s,1_[s,1]) has a_n=||t^-n1_[s,1]|| and growth 1/s. Closed invariant graph complement would require multiplier 1/t in L², impossible, while I_r is nonclosed for each 0<r<1. The pointwise growth theorem is stronger than merely the radial equality and entails it for strict thresholds.

## originality

PASS

The full Aznay–Chabbabi–Zariouh primary text Proposition 3.1 explicitly gives I_r=K_r under injectivity; Lemma 3.2 requires a closed finite-codimension invariant subspace and Theorem 5.2 closed radial spaces and a closed sum. A finite-ascent T is generally noninjective and ran T^p may be nonclosed, so none is a directly covering theorem. Its proof suggests the algebraic trick but does not state or imply the exact pointwise infimal exponential growth equality absent an added argument; result gives a concrete nonsplitting case. Qualified PASS subject to older spectral-set literature risk.

## value

PASS

Lossless gluing of unrelated inverse-power preimages into a unique coherent chain under an algebraic finite-ascent condition (without closed ranges or complements) fills a structural gap in local operator theory. The exact growth-rate equivalence and pathological nonsplitting/nonclosed example are natural reusable statements, not mere relettering of an injective theorem, because the original T may be noninjective and its stabilized range noncomplete.

The dated certificate retains the supplied scientific assessment, sources and limitations.
