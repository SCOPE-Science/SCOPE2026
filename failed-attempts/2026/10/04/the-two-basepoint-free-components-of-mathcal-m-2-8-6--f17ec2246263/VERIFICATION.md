---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The Brill--Noether number is \(-4\), so the expected dimension is 17. A plane sextic of genus eight has two nodes and the Severi quotient has dimension 17. For a nonbirational basepoint-free \(g^2_6\), Haburcak--Teixidor's cover lemma forces rational image; the only factorizations are \((e,k)=(3,2)\) and \((2,3)\), and their rational-image dimension bound gives 15 for k=2 and 17 for k=3, so only a triple cover of a conic survives. The trigonal Hurwitz locus is irreducible of dimension 17 and carries \(2A\). Coppens--Kato's nodal-plane criterion gives gonality \(6-2=4\) for the general two-nodal sextic, separating the loci. To close a point left implicit in the submitted proof, a generically basepointed component cannot swallow the 17-dimensional trigonal locus: after removing fixed base points a nondegenerate \(g^2_e\) has \(e\le5\); birational plane models then have arithmetic genus at most six, and the only nonbirational possibility is e=4 as a double cover of a conic, i.e. the 15-dimensional hyperelliptic locus. Thus the two 17-dimensional loci are indeed components of the stated basepoint-free type. The packaged arithmetic checker and a fresh independent calculation reproduce all numerical bounds.

## originality

FAIL

The final classification is already a routine boundary specialization of the machinery printed in Haburcak--Teixidor. Their Lemma 6.1 and Proposition 6.2 proof reduce any nonbirational basepoint-free component to a rational plane image and derive the inequality that, at even equality \(2d=g+4\), forces \(2k=d\); their Remark 6.4 supplies the corresponding gonality locus, and Example 6.6 performs the same argument at the nearby even-equality cell \((g,d)=(12,8)\), using Coppens--Kato to distinguish the Severi component. Substituting \((g,d)=(8,6)\) gives k=3 and the trigonal component with no new structural lemma. Under the required implication-based standard, omission of the low-genus number from the paper does not make this corollary original.

## value

FAIL

The \((8,6)\) cell is geometrically natural, but after the source's general cover lemma, its even-equality calculation, Remark 6.4 and the worked \((12,8)\) analogue are in hand, the submitted classification requires only the substitutions \(6=3\cdot2\), a one-line dimension inequality, and the already-cited nodal-plane gonality theorem. That is the kind of routine parameter specialization the common value bar excludes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
