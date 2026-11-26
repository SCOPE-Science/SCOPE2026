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

The published deterministic opinion–infection–vaccination equations agree with the frozen update on the physical state space. The extra probability clips are inactive there: gamma and q are probabilities and the sum of the two new transition shares of the susceptible mass is at most that mass. Every clique vertex has a strictly positive same-sign neighbor surplus, at least 3−2=1 at a portal. For every finite omega and positive epsilon the opinion update is constant in a relative neighborhood of each such corner. The vaccination fixed values follow from phi V=(1−V)gamma. The full Jacobian has a zero opinion row block; in the remaining coordinates the infection blocks are triangular with diagonal factors (1−alpha) on positive nodes and (1−alpha)Id+lambda A_MM on negative nodes, while vaccination factors are −phi and 1−phi, respectively. For a strict subthreshold radius the infection multipliers have modulus less than one, including alpha=1, so smooth extension to a neighborhood and an adapted norm give exponential attraction relative to the state space. For instability, the presence of a feasible positive eigenvector needs a boundary argument: on the negative component with largest radius, while a trajectory stays sufficiently close, susceptibility is uniformly near one and the pressure is bounded below by (1−delta)lambda times the infection sum over neighbors in that component, with delta arbitrarily small (expand 1 minus the product by telescoping). After shrinking the neighborhood, the inner product of infection with the positive component Perron vector therefore grows by a uniform factor greater than one. Arbitrarily small nonnegative seeds in that component must exit. The induced components are precisely the negative runs; eliminating the three satellites gives r−3/(r−2)=2 cos(pi/(ell+1)) for the positive Perron eigenvector. Its larger root is increasing in ell, and the empty case has radius zero. The word count follows by splitting according to the trailing negative run, and 12/25<1/2<2(3+sqrt(13))/25 proves the four-community witness. Independent replay checked the 254 words through seven communities, the run-count recurrence and the exact strict witness inequality; the arbitrary-size statements rest on the proof. Equality is not classified, and no stochastic assertion follows.

## originality

FAIL

The finding is mathematically correct, but the complete classification is covered as a corollary of the available comparison results. The general strict-majority theorem in Resultary 4241e10db284 covers the same map and includes every labeled corner on this chain, as well as the qualitative equal-coverage reversal itself. The remaining explicit spectral calculation is a direct substitution into the classical rooted-product theorem of Godsil–McKay; the count is its immediate bounded-run word enumeration and the numerical witness is a substitution. Thus no scientifically distinct remainder is established against the checked corpus. This is an assessment of demonstrable coverage now, not a finding that the later-catalogued general record predates the frozen result or evidence about the direction of derivation.

## value

FAIL

The public-health motivation and the structural effect of equal coverage with different clustering are worthwhile. But the claimed increment is an exact family instance of an available stronger same-model threshold, whose needed radius is supplied by the known rooted-product formula; the count and example are routine deductions from those statements. The bounded replay and the accessible presentation do not supply a distinct scientific contribution under the value standard for exact facts. No independently valuable remainder or repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
