---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Liu Theorem 5.3 / Corollary 5.5 gives exact P_{p,r}(a)=[a²-(I_p(r)+1)a-(J_p(r)+1)]/p. At r=0, I=J=p−1. For each proper divisor q of composite p, choose index ≤p−2 in the arithmetic residue orbit with δ_{p,q}(i)=q−1, proving I_p(q)≤p−2. For q=1, direct formula I=ceil((p−1)/2)≤p−2. If an eventual period s had g=gcd(s,p)<p, classes r=0 and r=g meet the same s-class infinitely often, forcing incompatible constituent polynomials equal. Thus every period is a multiple of p. Direct independent membership enumeration reproduced 204 (p,a) Frobenius values for p=4,6,8,9,10,12, and checked all divisor-branch obstructions. Proof is unconditional given the read published Liu branch identity.

## originality

FAIL

The contemporaneously published fixed-gap proof for h≥2 explicitly notes the gap-one result as already existing and its complete derivation, not merely its title, works unchanged upon the unexcluded algebraic substitution h=1. Its proof yields the same exact formula and no-period-collapse for every p≥2, hence all submitted composite p. The original printed theorem formally restricts h≥2; this distinction is recorded, but the gap-one claim is an immediate unaltered proof specialization, with no independent new lemma. The submitted proof is a streamlined same-branch argument, not a materially distinct fact.

## value

PASS

Least periods versus possible quasipolynomial collapse are a natural exact invariant in numerical semigroup quotient arithmetic and are explicitly motivated by Liu’s Definition 5.4. The theorem is mathematically useful, but its answer is already obtained as an unchanged h=1 specialization of a complete earlier available proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
