---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

At each vertex compare the central bit to its four distinct neighbors; minority fixes iff same-neighbor count <=2 and majority fixes iff >=2. A length-4 de Bruijn closed walk of length n encodes each labelled fixed cyclic binary word uniquely for n>=5. Complement symmetry decomposes the 16x16 transfer into two 8x8 signed blocks with displayed characteristic polynomials; exact SymPy determinants independently reconstructed all six factors, and direct enumeration of every cyclic binary word n=5..12 reproduced tr(T^n). Perron-Frobenius primitivity for the dominant nonnegative blocks plus root-modulus bounds separate lambda_minus>lambda_plus, proving the exponential ratio. Scope excludes nonfixed orbits and five-site including-center voting.

## originality

PASS

The explicit joint minority/majority spectral polynomials and exponential same-graph fixed-state entropy separation were not found in comparisons; transfer technology and radius-one majority enumeration are pre-existing. Plausible 1994 radius-r majority literature not fully inspected is explicitly at-risk.

## value

PASS

The same natural 4-regular graph and exactly matched tie conventions give a controlled quantitative comparison of local anti-coordination and coordination. Explicit degree-five vs degree-three transfer factors and a strict exponential entropy gap for all n are nontrivial exact invariants, not merely a generic transfer computation recipe.

The dated certificate retains the supplied scientific assessment, sources and limitations.
