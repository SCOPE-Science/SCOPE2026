---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For length t, y+2z=u=n-at and x=t-u+z, so max(0,u-t)<=z<=floor(u/2). At n0=(a+1)(a+2) through n0+a-1 the possible lengths are a+2,a+3 and, at the stated ends, a+1 or a+4. Summing their counts gives (2), at most p in both parities. Adding an a-coin injects representations along each residue class, extending the bound to all smaller positive n. At m=n0+a the three contributions 2,k+2,2 give k+6. For c=m+2, the totals at c and c+2 in the even case are k+6,k+5, and the totals at c-1,c,c+1 in the odd case are k+6,k+6,k+5. The possible lengths there are a+2 through a+4, including at a=7. Cofiniteness follows by adding any representable n-m to each representation of m, and the same injection gives closure. Any generator other than m is in its Apéry set, so e<=m. If equality held, every nonzero Apéry element would be a generator, in contradiction to the decomposable sum u+v whose predecessor u+v-m is a gap. Separately, I enumerated (y,z) and then all admissible n for eight a values of both parities from 7 to 32, and checked full finite generating sets using the conductor bound C=m+a²-1 and the fact that n>=C+m is decomposable. Replay: python3 -I /tmp/opencode/frozen_audit_small_checks.py, denumerant(). The frozen program was read, not run; its bounded initial scan of generators by itself does not bound the final embedding dimension.

## originality

FAIL

The distinct same-day Resultary record 6dc430dbb315 does not state the MED result, nor does its largest-gap theorem by itself imply it. However, its proof contains an exact, broader residue-block census which covers all decisive counts by direct specialization. This is demonstrable mathematical coverage, not a claim of earlier publication, dependence, or priority between the same-day records. The standard Apéry obstruction turns those covered counts into the frozen conclusion without a separate structural theorem.

## value

PASS

The structural question is natural: where can high-threshold representation semigroups cease to have maximal embedding dimension? An infinite family with parity-sensitive explicit local obstructions, beyond the original small-p formulas, makes that failure concrete rather than merely tabulating a few embedding dimensions. As a consequence of the overlapping census it is useful interpretively, but not accepted as a distinct finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
