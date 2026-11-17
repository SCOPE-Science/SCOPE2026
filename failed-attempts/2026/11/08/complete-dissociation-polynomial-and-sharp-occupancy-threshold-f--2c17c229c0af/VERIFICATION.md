---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Rook graph equals line graph L(K_{m,n}); induced degree≤1 for selected edges forces only vertex-disjoint K_2, K_{1,2} and K_{2,1}. Three component counts give exactly the factorial summand m!n!/[2^{p+q}p!q!a!(m-p-2q-a)!(n-2p-q-a)!]. Every selected edge uses at least 3/2 host vertices except isolated K2, bounding size by min(2m,2n,floor(2(m+n)/3)), with constructive feasible p,q,a in each aspect-ratio regime. Independent full subset enumeration matches every coefficient for 10 boards through 4×4, including 6×6 top coefficient 8100 from exact formula; no finite check is treated as infinite proof.

## originality

FAIL

FAIL. A previously published Nov 8 maximal-dissociation theorem for the SAME rook graph explicitly proves the identical three-component classification AND the identical UNRESTRICTED factorial count for each component triple (a,b,c). It then adds a maximality predicate to its displayed summation. Deleting precisely that predicate yields the entire candidate all-set polynomial term-by-term, with the same constraints under variable renaming. This is a direct mathematical corollary of the earlier published proof, despite a different maximal-versus-all theorem title. The max formula is elementary optimization of the same existing feasible component constraints, and earlier 2011 work and PUMaC also cover special maxima. It cannot be accepted solely because the unrestricted polynomial was not separately boxed.

## value

FAIL

FAIL for this final claim: although all-cardinality dissociation data are intrinsically meaningful, the precise formula is a one-line removal of the maximality condition from an already published all-component counting lemma. The claimed sharp occupancy maximum follows directly from the same constraints and elementary upper bounds/construction; no additional previously unproved structural ingredient remains. Mathematical correctness and complete code do not restore independent value beyond that prior implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
