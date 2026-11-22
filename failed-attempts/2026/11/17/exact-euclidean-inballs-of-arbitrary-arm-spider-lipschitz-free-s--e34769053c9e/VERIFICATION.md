---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For all q>=3 positive integer arm lengths, the polar of the edge-molecule crosspolytope is a cube of signed edge potentials. The pairwise variance identity along an arm yields (L+1)(u-v)>=w²-s²; changing a nonmonotone signed arm to a ramp gives strict gain at least (w²-s²)(1/(L+1)-1/N)>0. Thus extremizing potentials must use constant gradients per arm. Their normalized squared norm is sum u_i - delta²/N with triangular signed weights w_i. Center symmetry makes this global inradius, maximizers count |E|, and independent arm depth vectors give center-locus rank n-rank(E). Own exhaustive signed-edge test of (1,2,3,4), (1,1,2,3), (2,2,2) matches exact norm and contact count; finite only. The printed occurrence of nu_i in the theorem is an obvious undefined symbol for its explicitly defined u_i; the proof and example unambiguously specify sum u_i. It is a minor notational defect, not the reason for rejection.

## originality

FAIL

REJECTED due decisive older broader coverage: Resultary 2026-11-08 weighted spider Hilbert-valued Lipschitz-variance theorem already states EVERY optimizer is armwise radial and gives the SCALAR exact optimum R-eta² for arbitrary vertex probability and positive edge lengths, with eta a signed partition of weighted radial arm moments. For unweighted graph and uniform p_v=1/N, its q_i=w_i/N and R=sum u_i/N, hence N Var=sum u_i-delta²/N. This is exactly the polar facet norm optimization and contact sign classification. The alleged new strict screening lemma is an alternate derivation of already established equality geometry; the center-rank formula is immediate perpendicularity to those known contacting normals.

## value

FAIL

The more general 2026-11-08 theorem already supplies the mathematically central signed-partition optimization and complete maximizing radial configuration. The only additional packaging—Euclidean polarity and affine dimension n-rank of the known winning sign vectors—is a short routine deduction for a tree crosspolytope. In contrast to an independently unknown exact invariant, the claimed principal formula and contact data are mechanically implied by published stronger coverage; the source theorem cannot be passed by relabeling the norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
