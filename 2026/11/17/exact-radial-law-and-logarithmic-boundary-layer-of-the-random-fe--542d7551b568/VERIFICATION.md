---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

PASS. Three iid arclength-uniform circular points yield Dirichlet(1,1,1) cyclic gaps. A sampled triangle has angle >=120 degrees with probability exactly 1/3, so its distance-minimizing geometric median is the corresponding boundary vertex; rotational invariance makes this atom uniform on the circumference. For interior 120-degree minimizers, invert the three ray-circle intersections from (median coordinate z, common angle phi) and both cyclic ray orderings. The absolute angular Jacobian is (sqrt(3)/2)(sum t_j)/(product h_j), h_j=sqrt(1-|z|^2+(v_j dot z)^2). Combined with the uniform angle input this gives the planar integral density and rho(0)=3sqrt(3)/(4pi^2). Four separate angular singular neighborhoods at the rim yield rho(r)=(3/pi^3)log(1/(1-r^2))+O(1); radial integration produces the 6/pi^2 near-boundary coefficient. Independent finite-difference determinants match the Jacobian to 1e-8; fresh 60,000-triangle simulation gives boundary frequency 0.3304 and CDF matches the analytic density near r=0.2,0.5,0.8 to 0.0015. These experiments are only corroborative.

## originality

PASS

PASS, bounded. Várilly's primary full geometric article controls deterministic Fermat location relative to the triangle's Euler-line geometry, not the random point's pushforward distribution. Mordukhovich–Nam gives deterministic existence, uniqueness and algorithms for the same geometric median but no random spatial density. The full prior inradius distribution of the identical circle-triangle model is an invariant of a different center and cannot determine the Fermat location; a known earlier Steiner length-saving atom gives the same 1/3 probability but not the interior law or log rim divergence. Exact-object and alternate-terminology Resultary/web searches disclosed no statement implying the entire mixed radial law. A non-indexed stochastic-geometry median density remains an explicit priority risk.

## value

PASS

PASS. The unique geometric median is the canonical three-site facility-location point. Its full location distribution under the simplest rotationally invariant boundary sampling model is a natural exact geometric-probability question: the coexistence of a uniform boundary atom, a nontrivial bulk density, and a sharp logarithmic boundary layer cannot be inferred from angle statistics or the deterministic Fermat condition alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
