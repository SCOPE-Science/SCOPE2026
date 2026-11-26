---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The signed cycle has characteristic polynomial t^(2p)+1, so its complex planes have the odd weights 1,3,…,2p−1 modulo 4p. All weights except p are units modulo 4p; weight p alone has the order-p kernel P=<c^4>. Thus only the corresponding circle has nontrivial stabilizer and the residual C4 acts freely on the quotient by P. Radial coordinates identify the latter quotient with S¹*L, where L is the free C_p quotient of the complementary sphere with the printed weights. The double suspension of the connected lens space is 2-connected, so the free fourfold covering is universal and Hurewicz gives π_3=C_p, including p=3. The path of diagonal rotations from the identity to c descends to the intermediate quotient; trivial induced action on H_3 transfers to π_3 by Hurewicz. The odd torsion of L shifts by two. At p the residual C4 transfer preserves those localized groups. At 2 the subgroup <c^p> acts freely by odd weights, giving an ordinary C4 lens space; the subsequent P quotient need not be free, and does not use a covering transfer. After admissible subdivision its quotient chains are coinvariants; as p is invertible over Z_(2), averaging is exact and diagonal torus isotopy makes the action on homology trivial. This yields the claimed C4 in every eligible odd degree at 2; outside 2,p the same argument gives sphere homology. Local groups and the top class recover exactly the printed integral groups, with H_3=C12 for p=3. The frozen verify_b6.py was inspected only: it checks boundary compositions and reports finite-field Betti vectors, and cannot prove integral exponents or the infinite result. Independent mathematical check: branches/ae11161a-46ac-4ed9-83b3-40963089d33b/independent-check.md.

## originality

FAIL

The homeomorphism and low homotopy are a correct specialization, but on comparison with Armstrong's ordinary covering construction and the earlier exact suspended-lens calculation for two regular C_p modules minus one trivial line, the independent structural increment is not established. The precise equivalence uses the representation itself, not a title match: c^4 permutes two coordinate cycles of length p with sign product +1 on each, so re-signing along each cycle makes the C_p action two ordinary regular modules. Suspending the earlier k=2 cyclohedral quotient adds exactly the missing trivial line. Armstrong already supplies the passage from quotient by point stabilizers to the universal cover; the standard connected torus action supplies trivial monodromy. The older cyclohedral statement is for p≥5, but p=3 requires only the same direct representation-sphere join and the classical three-dimensional L(3;1,2), not a new small-prime phenomenon. The integral homology is explicitly credited to Kawasaki and is not independent originality.

## value

FAIL

The family is natural and the calculation is a useful illustration of the distinction between an ordinary and an orbifold cover. But as a narrow original classification, the exact covering space is a suspension of the previously classified prime-order quotient under the same real moving representation; the ordinary covering map, low homotopy, deck triviality and homology follow from standard constructions with no additional invariant settled. The finite-field example does not add an independently useful unknown fact. This is an expository specialization rather than a surviving new valued claim; no repair is being submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
