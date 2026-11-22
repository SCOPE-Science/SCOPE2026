---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

A Haar-uniform plane through the centroid of a right equilateral triangular prism with base edge 1 and physical height H intersects 3,4,5 edges in the trichotomy of crossing horizontal/vertical prism edges. The order statistic of the three horizontal dot products, and independent azimuth and |normal_z| coordinates, give elementary arcsine integrals for all three probabilities. With q=2/sqrt(4+3H^2), A=asin(q/2), B=asin(sqrt3*q/2), C=asin(q), the stated p3=1-6A/pi and p5=6(2B-A-C)/pi, p4=1-p3-p5 are sound for all H>0; the derivative comparison has one positive zero H≈0.613688176745 and p5max≈0.385155805674. Independently converted to the prior geometrically identical circumradius-one prism via h=sqrt3 H/2 (prior h denotes HALF height) and evaluated p3,p5 at H=.1,.613688,1,2,10: formulas agree to floating-point roundoff. Correctness follows from direct edge-sign enumeration and exact spherical integrals/monotone derivative, not five numerical points.

## originality

FAIL

FAIL decisively: a Resultary-published November 1 2026 theorem already provides the COMPLETE Haar-central three-point section law for the identical regular triangular prism, and proves the UNIQUE pentagon optimal half-height h*=0.5314695510636 and maximum 0.3851558056742. Its base circumradius=1 and half-height=h, while submitted base side=1/full height=H; h=(sqrt3/2)H makes the two statements geometrically identical. The earlier three arccosine formulas equal the submitted three arcsine formulas by complementary-angle identities. The earlier result also has the exact same sharp optimum and derivative uniqueness. A second full 2026-11-02 published central section law independently covers the three types for all heights. Novel notation and change of scale are not novelty.

## value

FAIL

FAIL for unchanged submission: this is an exact replication, under similarity and inverse-trigonometric identities, of a previously evaluated complete law and sharp maximizer. The object is naturally motivated and has intrinsic mathematical interest, but the submitted record contributes no independently unknown invariant or new structural lemma; the same optimal physical shape and probability were already proved. A new simulation certificate or disclaimer cannot restore originality/value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
