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

Li–Tang's exact dissection gives T(8n)/9=4[q^n]H. Their Theorem 3.1 initial vector gives the first normalized 24-series congruent to 2ρξ; dividing its product by H gives E(q²)^3 E(q³)/(E(q)^3 E(q⁶)), which is 1 modulo 3 by cubing. Thus the first bridge negates the normalized 8-series mod 3. For m≥1, the unit multiplier in Theorem 1.2(i) persists after dividing by 3^(m+3), with residual modulus 3^(3m) divisible by 3; all normalizations are integral by the prior divisibility result. This proves support equality for every positive integer n, also when a coefficient vanishes. The level-18 lift has modularity sums 24 and −120 for H, character χ_−3 and cusp orders (−5,2,1,1,1,1). The Fricke transform of A is 9(E4(3z)−E4(z)); widths give A-orders 6 and 3 above the level-three zero cusp, so HA is cuspidal with first coefficient −80. The prime conclusion was also checked without depending on the inaccessible cited wording of the prime-Hecke theorem: cubing Euler factors gives H≡G=η(z)^8η(2z)^8 mod 3. The level-2 eta criterion gives G∈S_8(Γ0(2)) (sums 24,24, trivial character and cusp orders 1,1). In weight 12 and level 2, G E4=Δ(z)+256Δ(2z) exactly: the constant through q³ agree (0,1,232,252), and the level-2 Sturm/vanishing bound is 3. Since E4≡1 mod 3, the coefficient at every odd prime p is τ(p)≡p(1+p) mod 3 by the classical Ramanujan congruence. In particular it is 2 on p≡1 mod 54, and Dirichlet gives infinitely many such primes. Multiplying by 36 gives residue 72 mod 108 and the support equality propagates sharpness to all m. This independent argument gives a stronger prime statement, but the disposition assesses the original quantified claim.

## originality

PASS

The internal lower bounds and the m≥1 equivalence are direct consequences of prior work; the m=0 bridge is elementary from prior series. Credit the distinct claim narrowly as the explicit eight-branch prime sharpness conclusion, propagated simultaneously to all levels. The strongest related catalogue classification is for the twelve branch. The residual support is reducible to a familiar tabulated modular form and in fact to Δ modulo 3, but the inspected sources do not state the needed all-prime congruence for this form or the eight-branch conclusion. The catalogue identification and classical Ramanujan congruence alone require the additional eta and modular identity bridge checked here. No priority claim or novelty for the underlying Hecke, eta or tau tools.

## value

PASS

Uniform divisibility lower bounds leave open whether they are ever sharp on the very thin sequence of prime inputs, let alone at the same primes for every scaling level. The finding provides such a set with a definite nonzero residue and ties it to the support of one modular series. Besides sharpening the known divisibility theorem, this separates prime-index sharpness from global lacunarity, which has no comparable witness content. The key prime residue is a mathematically useful exact fact, not a numerical check or a claim of novelty for the standard congruence tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
