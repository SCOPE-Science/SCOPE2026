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

The edge normal form follows by choosing positive scales for the three alternating rays to sum to zero and then imposing closure. Independently, the three supporting strips have coordinates X, Y, X+Y with widths a+c+t, b+c, a+b respectively. Their midpoints satisfy m_(X+Y)-m_X-m_Y=t/2. For asymmetry at most s, each center coordinate must deviate from its midpoint by at most the corresponding half-width times (s-1)/(s+1); compatibility holds exactly when the sum of those allowances is at least |t|/2. This recovers the credited containment formula and handles t=0. For t>0, the vertex shoelace area divided by t² is B=1/2+U+xy+xz+yz. The three opposite-pair edge lengths add when forming P-P; their cyclic central hexagon has area 4A(P)+t². The three opposite midpoint differences give absolute area t²/8. Hence R=4+1/B and W=1/(8B). At fixed U=(2-s)/(s-1)>0, the pair sum covers (0,U²/3] on the positive simplex, via a segment from its center towards a corner. The center is the unique maximum of B, and the half-variance identity follows by expanding that pair sum. Order-three affine symmetry permutes the three alternating edge rays and consequently their lengths (the only positive relation between the normalized rays has equal coefficients); it is equivalent to x=y=z, which also makes the intervening lengths equal. Sequences at the strict endpoint approach simplex corners up to cyclic relabeling. At (U,0,0) the limiting vertices reduce to (0,0),(U,0),(U,1),(-1,1), a nondegenerate trapezoid for U>0; the other corners are cyclic variants.

## originality

PASS

The earlier exact asymmetry formula and Wigner/symmetral area relation are inputs. The closest neighboring results do not supply the complete fixed-s intervals or the endpoint rigidity and reciprocal-excess identity. The separate optimization uses a joint normal-form area computation and the fixed-asymmetry simplex, not just substitution into a universal bound.

## value

PASS

Both asymmetry and difference-area excess are natural affine invariants. The theorem measures their exact tradeoff on the first noncentrally symmetric parallel-opposite polygon class, improving unconditional bounds and distinguishing an attained symmetric extremum from a nonattained quadrilateral limit. It quantifies how imbalance affects the area ratio at fixed asymmetry rather than reasserting the known Wigner identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
