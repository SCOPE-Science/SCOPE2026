---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The all-maximal stable state plus one chip at t has a legal one-topple sequence t, all nonsink A, then remaining B, ending stable. Least action bounds each toppling count by one for every stable state. For equality t has height a-1 and every other B vertex has at least one chip. Subtracting one at those B vertices after deleting the old sink lowers both their unfired heights and thresholds by one; after t fires, the residual legal once-per-vertex order is precisely burning in the deleted graph rooted at t. The inverse is stable and recurrent: a forbidden subset cannot contain t, whose height is at least its internal degree, and any subset avoiding t has a burning witness from the auxiliary recurrent state. Thus the maximum count is the tree count of K_(a-1,b), including a=2 when this graph is a star. Dividing by the complete bipartite tree count yields the probability. Independently, stationarity and chip mass balance give expected total topplings over B exactly one, since exactly those vertices lose a chip to the sink per toppling. Stationary height balance at each nonsink A gives b E[u_A]=E[sum_B u]=1. Thus E[T]=1+(a-1)/b and the stated activity fraction and balanced asymptotic follow. An independent forbidden-subconfiguration enumeration and legal stabilizer gave (recurrent, full, max, mean, share)=(12,1,4,4/3,1/4) for (2,3) and (12,4,4,2,2/3) for (3,2). The original scripts were inspected, not executed.

## originality

FAIL

A distinct indexed Resultary record gives the same sink-deletion and rerooting bijection and count for all finite connected undirected loopless graphs. The bipartite law is its exact specialization. The remaining mean and rare-event fraction follow directly from stationary mass and height balance and division. The distinct record is dated the same day: this establishes mathematical coverage and no demonstrated independent contribution, not chronological priority or a provenance judgment.

## value

FAIL

A rare event carrying an order-one share of activity is a useful interpretation. But once the identical deletion law is available, its claimed exact invariant needs only routine bipartite tree counts, conservation, and an elementary limit. The specialized presentation adds no separate structural result or independently nonmechanical invariant of value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
