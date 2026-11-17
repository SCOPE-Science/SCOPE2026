---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

PASS: For a,b,D,r0,r1>0, starting from each last-reset-site type, the Brownian displacement at an independent Exp(rj) time has exactly symmetric Laplace density κj e^{−κj|z|}/2, κj=√(rj/D). Summing all periodic Voronoi cells (not just nearest-neighbor transitions) yields p(κ)=[sinh(κa/2)+sinh(κb/2)]/[2sinh(κ(a+b)/2)] and d(κ)=[a sinh(κb/2)−b sinh(κa/2)]/[2sinh(κ(a+b)/2)]. An independent numerical quadrature of >100 Voronoi cells at (a,b,κ)=(1,2,.5),(1,2,2),(1,1,1),(2,1,.9) reproduced both to ≈10^−16 and normalized total probability. By spatial reflection, type-1 conditional displacement is −d(κ1). The irreducible two-type Markov chain has stationary probabilities p1/(p0+p1),p0/(p0+p1); Markov-additive reward/time strong laws yield v=(p1d0−p0d1)/(p1/r0+p0/r1). Exponential tails and Brownian maximum bound control incomplete holding intervals, upgrading reset-epoch law to full physical-time a.s. velocity. H(κ)=d/p=[aR−b]/(1+R) with R=sinh(κb/2)/sinh(κa/2) changes strictly with sign(b−a) because x coth(x) increases. Thus v=0 iff a=b or r0=r1 and otherwise its sign is sign((b−a)(r0−r1)). Series p=1/2+O(κ²), H=ab(b−a)κ²/24+O(κ⁴) yield the exact t² coefficient under rj=tcj; exponential tails imply high-t vanishing. Continuity plus strict sign yield at least one finite absolute-speed maximizer, not uniqueness. All-site nearest quantization and last-site memory are essential.

## originality

PASS

PASS (best-of-knowledge): Alston–Bertrand (arXiv:2401.12772; Phys Rev E 2025) fully analyzes nearest-site resetting on periodic arrays with one spatially uniform Poisson rate and optimizes macroscopic self-diffusion; that uniform clock cannot produce the new alternating-site-type drift. A more recent published Resultary general periodic-array paper likewise gives D_eff with uniform rate; it does not include label-conditioned rate switching or a nonzero directed velocity. Separate ratchet-resetting articles use asymmetric potentials and common reset clocks, not the staggered Voronoi projection with last-site clock memory. No identical two-parameter exact current/sign formula found.

## value

PASS

PASS: Geometric asymmetry alone and clock asymmetry alone both yield zero current, whereas combining them creates a directed current with exact sign, a quadratic weak-reset onset and existence of an optimal finite common clock scale. This is a motivated, globally classified minimal ratchet mechanism on the infinite line rather than a contrived numerical slice. The complete analytical Markov-reward reduction is useful for site-dependent stochastic transport despite not giving fluctuations or unique optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
