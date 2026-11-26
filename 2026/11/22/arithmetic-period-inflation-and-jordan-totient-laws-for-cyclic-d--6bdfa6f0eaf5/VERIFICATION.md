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

On Z/(nt), addition by d has gh cycles for h=gcd(t,b), since gcd(n/g,b)=1. Each cycle is a class modulo gh; the t repeats of an original index advance modulo h by n/g, coprime to h, so each compatible class receives exactly t/h repetitions. Its sum is (t/h)S_r. Telescoping forces this to vanish, and conversely one arbitrary symbol per cycle gives one unique circular lift. Simultaneous vanishing is m∣t/h since m is the order of the sum vector, so the fixed count is κ^(gh) or zero. For p∣m the condition is v_p(t)−min(v_p(t),v_p(b))≥v_p(m), giving the least multiplier, and other primes are unconstrained. The κ^d lifts are parametrized by a consecutive d-symbol prefix via the reversible stride recurrence. At t=κb the formula counts all κ^d, so their periods divide nκb. For a primitive displayed target, shift-commutation forces each least lift period to be a multiple of n, and an orbit of length nt passes the specified indexed target exactly t times; divisor inversion and division by t then give the claimed census. For arbitrary displayed n the word need not be primitive and the fixed-point/least-admissible-multiplier statement is relative to that display. Uniform independent coordinates give independent uniform residue sums, and for a∣κ exactly a^g vectors are killed by a; inversion gives J_g(a), with distinct a giving different multipliers by the prime valuations. Conditioning can change this law: at κ=2,n=2,d=1 only 01 and 10 are primitive and both have nonzero sum. For κ=3,n=1,d=4,y=(1), the fixed counts at 3,6,12 are 3,9,81 and invert to 3,6,72 least-period counts. The checker was read, not run: its primitive-period loop samples binary-symbol targets even at larger moduli, and its printed 81,090 total counts enumerated prefix lifts across target fibers, not 81,090 distinct fibers. Neither detail affects the all-parameter proof.

## originality

PASS

The claim credited is the closed target-dependent vector-order fixed-point law for arbitrary modulus and stride, together with its exact unconditional Jordan-totient distribution, not the difference code, general algorithms for preimage periods, ordinary Möbius inversion, or the previously classified binary Rule 90 minimum. The prior finite-prefix and graph representations apply to the model and compute individual answers, but the inspected statements do not supply this all-parameter arithmetic classification or the distribution without enumeration.

## value

PASS

The formulas reduce a natural finite-fiber period question to residue sums and prime valuations, without enumerating the κ^d lifts, including over composite alphabets. They predict period obstruction, multiplicity and frequency over random targets in one classification. The restriction to unconditional displayed-length sampling is useful and explicit; no general nonlinear code or primitive-conditioned distribution is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
