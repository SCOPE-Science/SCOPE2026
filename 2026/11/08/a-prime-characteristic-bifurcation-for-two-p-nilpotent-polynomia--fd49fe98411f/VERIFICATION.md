---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Over any field of characteristic p>0, ∂x and ∂y have p-th power zero, yielding D^p=E^p=0. Every derivation kills t=x^p y^p, so (DE)^n(x)=t^n x and H^n(x)=t^n x for H=[D,E]; monomial independence proves associative infinite-dimensionality and failure of local finiteness of H. Writing D=x^p(x∂y), E=y^p(y∂x), H=t(x∂x−y∂y) gives [D_i,E_j]=H_{i+j}, [H_i,D_j]=2D_{i+j+1}, [H_i,E_j]=−2E_{i+j+1}. For odd p all current families are generated and linearly independent by x/y monomial supports. For p=2 the 2 coefficients vanish, leaving 3D Heisenberg Lie algebra, but central H=DE+ED and square-zero D,E generate the rank-four K[H] envelope on {1,D,E,DE}; monomial actions on x,y show independence and K[T] is a polynomial algebra. Valid for arbitrary nonperfect K, char2 included. Inspected finite monomial tests supplement these symbolic unrestricted proofs.

## originality

PASS

Best-of-knowledge PASS: explicit uniform p-nilpotent pair with infinite associative algebra, characteristic-dependent odd-p infinite current Lie algebra versus char2 three-dimensional Heisenberg Lie, and exact rank-four char2 operator envelope. Bezushchak–Petravchuk Theorem 1 is a sufficient criterion requiring every commutator to act finitely; H^n(x)=t^n x violates it. Theorem does not itself construct or classify this exact boundary example. Existing Lie/Clifford algebra vocabulary is an alias risk, checked semantically rather than only with exact generator names.

## value

PASS

Gives a sharp structural counterexample to weakening a recent finite-dimensionality criterion to mere nilpotence of selected generators, and exhibits a nontrivial modular characteristic-two collapse of Lie dimension without collapsing associative dimension. The complete operator envelope is reusable algebraic information, not a trivial substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
