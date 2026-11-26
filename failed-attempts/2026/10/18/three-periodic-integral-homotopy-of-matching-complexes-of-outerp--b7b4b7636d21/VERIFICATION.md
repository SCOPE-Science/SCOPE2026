---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Deleting the second vertex in the path independence complex gives a cone and its link is the path shortened by three; the base cases give the required path types, with the empty complex used only as an augmented join unit. No two spokes can occur in one matching. For the spoke at i its base is the join of the matching complexes of paths on i-1 and n-i vertices. The noncontractible links thus occur in residue pairs (1,1), (0,0), or (0,1)/(1,0) for n=0,1,2 mod 3, respectively. For n=3k>=6 the k sphere links have dimension k-2, so all their inclusions into the S^(k-1) base are null; attaching cones adds k spheres of dimension k-1. For n=3k+1, the end-spoke link embeds into the path base as the deletion of a path endpoint in the independence formulation, with contractible endpoint link Ind(P_(3k-2)); its inclusion is an equivalence. Taking its cone first makes the base contractible, and the remaining k sphere links each add S^k. For n=3k+2>=5 the base is contractible from the start and there are 2k+2 contributing links. These are homotopy cofibers of simplicial inclusions, not deductions from a field Betti table. Direct low-order cases are a point at n=1, three points at n=2, and two segments plus an isolated point at n=3. An independent matching enumeration and augmented boundary computation for n=2 through 8 over F2 and F3 gave ranks 2,2,1,4,3,2,6 in the predicted degrees. Replay: /workspace/branches/81c7746e-66bf-4315-8cce-5ef1ec76663c/finite_check.py and finite_check_output.txt. These finite checks are supplementary and cannot establish integral homotopy or exclude torsion for all n. The frozen verifier was inspected, not executed.

## originality

FAIL

Two distinct indexed catalogue results give the same ordinary matching-complex homotopy classification. The strongest mirror entry specifies the same fan, ordinary matchings, geometric realization, and all three wedge formulas including n=2. The remaining n=1 observation is just the one-edge graph and is not a distinct scientific claim. The mirrors have later catalogue dates; this establishes substantive current coverage, not earlier publication, origin or priority over the frozen record. The published qualitative outerplanar theorem alone would not justify this decision.

## value

PASS

As a mathematical classification, the exact sphere degree and multiplicity for all fans provide concrete information beyond qualitative wedge existence, and the contractible-base step at n=1 mod 3 explains the different counts. This is a natural all-orders question, not a tiny-instance exercise. The value of the classification as mathematics is separate from whether this rendition adds a distinct result to the corpus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
