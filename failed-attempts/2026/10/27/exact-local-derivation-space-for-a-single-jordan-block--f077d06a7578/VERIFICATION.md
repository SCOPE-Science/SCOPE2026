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

Let A=lambda I+S. Since A is invertible, N=[L,L] and is preserved by derivations; comparing the identity on [v,x] gives BA-AB=aA with a the x component of d(x). Its trace is ak lambda, so a=0 in characteristic zero. A map commuting with S is determined by its value on the cyclic vector e_1; each such value uniquely equals p(S)e_1 for a polynomial of degree below k. Conversely, arbitrary d(x) in N and B=p(S) give derivations. Locality on e_j forces Delta(e_j) into F_j and on x forces Delta(x) into N. If v in N is nonzero with first nonzero entry j, the columns v,Sv,...,S^(k-j)v have leading coefficient v_j in successive rows, hence span F_j over K. Every flag-preserving B therefore satisfies Bv=p_v(S)v pointwise. For y=alpha x+v with alpha nonzero, use a derivation vanishing on N with value Delta(y)/alpha on x; y=0 is automatic. This proves all three dimensions by counting entries, including k=1 where both spaces have dimension two. The supplied verify.py was inspected, not executed; the finite checks through k=8 are illustrative and unnecessary to the symbolic result.

## originality

FAIL

The full local space is not printed in the matched paper, but it is a direct corollary of its displayed derivation family for exactly this Jordan action. The published local-derivation example already writes the coefficient system; after its initial zero coordinates the system is triangular with the first nonzero coordinate on the diagonal, and therefore matches any target in the same flag tail. This is an implication finding, not a claim that the paper states the dimension formula verbatim.

## value

FAIL

Quantifying how much rigidity fails is a reasonable question, and the note states the answer correctly. In this exact family the flag and dimensions are a direct image calculation in the known triangular Toeplitz derivation matrices: inspecting the leading nonzero coordinate gives each orbit and entry-counting gives the deficit. The restriction to one block removes the interactions that might give a nonroutine classification. No distinct substantive result beyond this mechanical consequence survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
