---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Let P=a⊗phi, nonzero rank1. Nijenhuis equation forces a²∈ka and scalar relation λphi(x)phi(y)=phi(x)phi(ay)+phi(y)phi(xa)-phi(a)phi(xy). In Kronecker A_m=k e⊕k f⊕V with e²=e,f²=f,ev=v=vf,V²=0, image line is necessarily kv, k(e+u), k(f+u) or k1. Radical branch has phi(v)phi(1)=0; idempotent branches phi(1)=0 or phi is scalar e*/f*; unit branch phi scalar character. Seven varieties X_e,X_f,Y,L_e,L_f,U_e,U_f cover the locus, are closed/geometrically irreducible and pairwise nondominating; the incidence cone Y has affine dimension 2m. Dimensions and finite-field count follow by line-by-line decomposition, including zero once. Independent exhaustive F2 m=2 implementation checks original identity on every rank1 map, yielding 99 nonzero. The proof covers arbitrary fields, m≥2, and reduced geometry; finite checks cannot prove all fields.

## originality

PASS

PASS for the all-characteristic seven irreducible components of the reduced rank-at-most-one associative Nijenhuis operator locus on m-Kronecker path algebra, plus explicit finite-field point formula. This is distinct from ordinary similarity/orbit counts for split square-zero LOCAL algebras and small-dimensional associative algebra tables. Only rank≤1, m≥2, and reduced variety are claimed.

## value

PASS

PASS: A geometrically complete and characteristic-uniform decomposition of the natural rank≤1 operator variety of the Kronecker quiver algebra is a substantial exact classification. The nontrivial radical-incidence component and all-q census are not numerical artifacts or restatements of small-dimensional complex-algebra tables; they provide structural input for further operator stratification even without a higher-rank theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
