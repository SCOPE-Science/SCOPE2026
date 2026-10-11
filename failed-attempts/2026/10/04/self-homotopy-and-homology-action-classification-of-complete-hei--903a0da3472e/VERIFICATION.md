---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The map classification is correct. A monotone self-map either preserves levels, sends some lower point upward and thereby makes the whole upper shore constant, or dually sends an upper point downward and makes the lower shore constant; these disjoint cases give the stated total count. A level-preserving pair with both shore maps nonconstant is isolated in the pointwise map poset, while all remaining maps connect through constants, yielding one null/zero-homology component. The order complex is \(K_{p,q}\), and \(H_1\cong\widetilde H_0(A)\otimes\widetilde H_0(B)\); a shore map with image size \(r\) has reduced-\(H_0\) rank \(r-1\), so the tensor rank and Stirling image-size profile follow. An independent exact enumeration for \(p=q=3\) reproduced 951 maps and 577 components, one of size 375 and 576 singleton components.

## originality

FAIL

Two published SCOPE results strictly cover the novelty-bearing substance. The general mapping-space decomposition for \(P_{p,q}\to P_{r,s}\) already gives the total map count, the unique nonisolated component, the isolated-map count, and the homotopy-class formula for independent source and target sizes; setting \(r=p,s=q\) gives the assigned self-homotopy classification. The published top-homology theorem for arbitrary finite weak orders already says that top homology is nonzero exactly for levelwise nonconstant maps, with rank \(\prod_i(s_i-1)\), and that an isomorphism occurs exactly for a homeomorphism. At height two this is precisely the assigned \(H_1\) rank theorem. The remaining Stirling rank-profile formula is then routine counting of endofunctions by image size. Thus the final claim is mechanically implied by broader published results.

## value

FAIL

The formulas are mathematically clean, but after the broader mapping-space and top-homology theorems are published, the height-two self case is a direct specialization and the exact rank profile is routine image-size enumeration. It no longer fills an independent structural or exact-invariant gap under the common value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
