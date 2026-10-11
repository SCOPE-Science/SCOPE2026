---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The projective orbit map G->H·[eta] has uniform fibers of cardinality |G|/m(eta). For nonzero f in C^2, the coefficient vanishes exactly when [pi(g)eta] is the single ray [f-perp], so the zero set is empty or one whole fiber; varying f realizes every orbit ray and proves p0(pi,eta)=1/m(eta). The quotient H acts faithfully on CP^1, and each nonidentity projective unitary fixes at most two rays, so a ray outside the finite union of fixed sets has trivial stabilizer and orbit size |H|, yielding the global minimum. The sharp sample threshold follows because no nonzero coefficient can vanish on more than |G|/m points and one can attain exactly that fiber.

## originality

FAIL

Führ--Oussa already define the zero-proportion invariant, prove its invariance under quotienting by the projective kernel, state the sharp uniform-sampling consequence, and give the exact full-spark formula p0=(d-1)/|G|. In complex dimension two, a generic ray for the faithful projective quotient has trivial stabilizer because each nonidentity projective unitary fixes only finitely many rays; its orbit is therefore a set of |H| distinct rays, which is automatically full spark in C^2. This mechanically gives the submitted minimized value p0(pi)=1/|H|. For a fixed window, the remaining formula p0(pi,eta)=1/m(eta) is the immediate orbit--stabilizer evaluation of the source definition because f-perp is one projective ray. The claimed sampling threshold is then exactly the source's sampling observation. The package is mathematically correct, but the final claim is a routine dimension-two specialization of the published framework rather than an independent theorem.

## value

FAIL

The fixed-window formula is a one-line dimension-two application of orbit--stabilizer to the published p0 definition, while the minimized value and sampling statement are already mechanically supplied by the source's projective-kernel/full-spark framework once a generic trivial-stabilizer ray is observed. This is a useful explanatory corollary but does not clear the required bar against routine textbook specializations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
