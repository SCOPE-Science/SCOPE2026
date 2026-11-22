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

For 3 equal exterior circles of radius 0<r<1/2 at triangle vertices, the Cao–Llibre degree<=4 normal form specializes to displayed A_i and positive-time Floquet exponents chi_i=(2*pi*kappa*r^2/(abs(delta_i)*H_i))*S_i with S_i=(omega_3-omega_2,omega_1-omega_3,omega_2-omega_1). Under each |omega_i|>|kappa|r, delta_i=sign(omega_i)sqrt(omega_i^2-kappa^2r^2), H_i=omega_i+delta_i sqrt(1-4r^2)-2kappa*(sqrt(3)/2)r^2 have sign omega_i by 2vr<1. For kappa!=0 neutral is S_i=0; the equilateral vertex-axis reflection interchanges other centers and reverses polynomial vector field in time at precisely this relation, so Cao–Llibre reversible-periodic-orbit lemma guarantees local period annulus. For kappa=0 their Proposition6.3 already gives a first integral/annuli. Set w_i=abs(delta_i) H_i omega_i/(2*pi*r^2)>0; telescoping sum w_i chi_i=kappa sum omega_i S_i=0, forcing mixed transverse signs if any chi nonzero. Six permutations of (3,1,-4) in omega_i=v/3+2a_i realize each allowed mixed triple for every r in (0,1/2), all periodicity bounds strictly hold. Reconstructed algebra and inspected symbolic checker, independently checked sign constructions and weighted identity, rather than relying on VERIFY_OK alone.

## originality

PASS

Cao–Llibre arXiv:2611.05696v1 (Nov3 2026) Theorem D and Propositions6.1–6.3 contain exactly the general quartic normal form, periodicity condition, characteristic exponents and kappa=0 annulus; Lemma2.4 establishes generic reversible orbit theorem. These are all **prior**. Their paper does not classify the equal-radius equilateral nonzero-kappa neutral axes, prove each forces the exact reflection invariance, derive the positive-weight Floquet sign obstruction, or show all six feasible patterns. This is a genuine geometry-specific structural refinement, best-of-knowledge original. The earlier generic reflection lemma is cited as a premise, not new.

## value

PASS

The neutral Floquet boundary of a prescribed invariant periodic circle is a mathematically meaningful degeneracy where multiplier 1 alone cannot distinguish weak isolated cycle from an annulus. Equilateral geometry forces reversibility and rules out nonhyperbolic isolated circles while proving a sharp sign-balance law and six realizations. This is substantive phase-portrait rigidity in a natural three-circle family, not a rote parameter rename.

The dated certificate retains the supplied scientific assessment, sources and limitations.
