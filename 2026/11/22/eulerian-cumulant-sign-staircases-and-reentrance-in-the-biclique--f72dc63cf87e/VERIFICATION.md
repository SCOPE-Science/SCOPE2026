---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The independent-set weights give Z=x^m+x^n-1, all nonempty same-shore moment blocks on the marked shore have weight a*p^s, and every block mixing shores vanishes. The one opposite mark must therefore occupy a singleton in the moment-cumulant formula. For k remaining blocks the weight is (-1)^k k! times the product of their moments, with Stirling multiplicity, proving b*p^(r+1)*F_r(a). The polynomial is the rth derivative at u=0 of 1/(1-a+a exp(u)); summing the geometric expansion by the Eulerian identity gives -a(1-a)^(r-1) A_r(-a/(1-a)). The Eulerian recurrence alternates signs at the simple negative roots of the preceding polynomial; signs at zero and negative infinity give the two exterior intervals, yielding all r-1 simple interior a-roots by induction. Reciprocity pairs a with 1-a. The sign of da/dx is that of (m-n)x^n-m. This yields the three stated ranges, strictly monotone when n>=m, and a single nondegenerate minimum otherwise. The positive prefactor cannot change a sign; reaching a simple polynomial root at the minimum gives a double zero with no reversal. For K3,2 the larger root is above the minimum and the smaller below; the two cubic roots with x>1 give z=0.21851631751816... and 2.41135460666566..., with signs negative, positive, negative. Independently checked 69 exact cases by extracting the marked square-free coefficient of the partition-function logarithm; the analytic derivation, not that grid, governs every admissible size and positive z.

## originality

PASS

The surviving distinct result is the complete finite cross-shore cumulant sign classification for every stated size and order, with an explicit two-crossing example. The independence polynomial, moment-cumulant inversion and Eulerian real-rootedness are established inputs. The strongest inspected prior results on the biclique concern partition/one-point quantities, and the closest sign-transition work changes the observable or model.

## value

PASS

This is a complete all-order sign classification for a natural connected response which is not encoded by the pair anticorrelation or by mean occupancy. It explains sharp transitions and reentrance in a simple finite geometry rather than presenting a single chosen numerical example. The five-site example is minimal for two reversals in this family: smaller graphs have either r=2, whose sole root is 1/2 and cannot be hit twice, or (m,n,r)=(3,1,3), whose minimum a=27/31 is above both roots. Arbitrary order and the distinction between true and tangential zeros add usable information beyond the elementary moment formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
