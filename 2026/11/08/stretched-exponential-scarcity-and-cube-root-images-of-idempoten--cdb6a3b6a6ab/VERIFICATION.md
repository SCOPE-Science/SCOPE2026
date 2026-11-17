---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Each generator is 1-Lipschitz on L_m, and finite McShane representation f(x)=min_a min(1,f(a)+|x-a|), with |x-a| definable by max of two truncated subtractions, expresses every discrete 1-Lipschitz map. An idempotent map has interval image [a,a+d] and fixes that image pointwise. Its two exterior tails are independent lazy walks with steps -1,0,1 confined to the interval, yielding I_m=sum_{d=0}^m sum_{a=0}^{m-d}F_d(a)F_d(m-d-a), F_d(t)=(A_d^t 1)_0, with A_d the looped path adjacency. The Perron root is lambda_d=1+2 cos(pi/(d+2)); its squared first-coordinate weight 2 sin²(pi/(d+2))/(d+2) is bounded below by 8/(d+2)^3. Returning walks at even times and one self-loop at odd times provide a uniform polynomial spectral lower bound, while the spectral norm gives the upper bound. Thus log I_m=max_d[(m-d)log lambda_d]+O(log(m+2)). Minimizing B_m(d)=d log3+(m-d) log(3/lambda_d) gives the unique width t=(2*pi²/(3log3))^(1/3) and deficit C=(3/2)t log3; polynomial prefactors cannot prevent convergence in probability of d/m^(1/3). Counting all 1-Lipschitz maps by increment words with valid starts gives log N_m=m log3+O(log m). Independent brute-force enumerated m=1..5, counts 3,8,21,56,149; exact all-map counts matched 4,17,68,259,950. These finite checks do not prove the asymptotic.

## originality

PASS

The October 26 weak-CYCLE retraction paper proves the same cube-root scaling constants and uses looped path transfer matrices; that METHOD and spectral exponent are known, not original here. The present finite fuzzy CHAIN/weak PATH has a different interval-with-two-exterior-walk convolution and exact counts, as opposed to a single complementary cycle walk, and also proves definability as unary fuzzy terms and rarity versus all such terms with an O(log m) remainder. The Knauer–Pipattanajinda undirected-path paper counts all weak endomorphisms; Dimitrova et al study monoid generator ranks; Fernandes–Paulista counts directed-path idempotents with monotone maps. None of the inspected statements supplies this exact fuzzy-chain idempotent census and probability law. Very close known circle method remains an explicit originality risk.

## value

PASS

Natural, intrinsically motivated count and image-width probability law for idempotent/nonexpansive finite fuzzy unary operations (equivalently reflexive path retractions). The exact finite census, stretched-exponential rarity among all unary maps and typical fixed-interval scale are independently usable invariants, despite a similar cycle model exhibiting the same universal scaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
