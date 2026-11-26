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

Conjugation by a vertex permutation is a signed edge-coordinate isometry preserving the cut space. The averaged projection still fixes every cut vector and has range in that space, so it suffices to minimize over the invariant family. An elementary stabilizer check also verifies the reduction at m=2 or n=2: a clique-edge column i,j is odd under the transposition of its ends, so its potential is a(e_i-e_j); a cross-edge column i,u has clique potential b(e_i-1_A/m), and a potential on B that is constant off u. Fixing class-constant gradients and the B-mean-zero gradients sets that B potential to -e_u/m. Fixing A-mean-zero gradients leaves just ma+nb=1. The frozen Q_t exhausts these columns with a=(m+nt)/(mN), b=(1-t)/N. The clique column sum is 2(N-1)|a|; the cross column sum is the one in the proof, whose last two absolute terms have a constant signed sum mN in its common denominator. Thus, with K=(m-1)(m+2n-2), on [0,1] the two norms are 2(N-1)(m+nt)/(mN) and 1+K(1-t)/(mN). They cross at t_*=(m-2)(n-1)/D, D=2n(N-1)+K. The first norm for t>1 and the second norm for t<0 cannot improve the crossing. Substitution gives the stated minimum, and at t=0 the cross norm is maximal, with excess K t_* /(mN). This excess is zero exactly at m=2, and taking leading terms on the diagonal gives the three limits.

## originality

FAIL

There is verified, exact coverage by a distinct catalogued result of the unrestricted cut constant, the attaining invariant projection and the precise orthogonality threshold. The canonical orthogonal norm also follows by explicit specialization of a separate same-day general multipartite theorem. The gap and limits then require only subtraction and leading terms. The two-sided coverage record has a later catalogue label than the assigned frozen record; this audit is not a finding that it predates the frozen mathematics. But the frozen package and accessible sources do not establish earlier public priority for the assigned result, and no uncaptured substantive claim remains in it. A supported distinct claim is not established, independently of the correctness of the mathematics.

## value

FAIL

The mathematical question itself is worthwhile: an exact gap on an infinite natural graph family would quantify when the canonical cut projection fails to minimize the edge-l1 norm. But that gap and the full optimality characterization are already recoverable from the verified exact coverage. The frozen calculation uses the same two column orbits and one-parameter optimization as the encompassing cut theorem. No further structural phenomenon, parameter range, or meaningfully different method is left; the diagonal limits are immediate consequences of the covered formulas. The rejection is of the added scientific contribution of this record, not of the usefulness of the invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
