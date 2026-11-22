# Scientific review

## Correctness (C) — PASS

The theorem fixes the unsigned Domb normalization and ordered residue pairs, including zero-length digit blocks. Independent Lucas factorization follows from carry-free binomial factors for the Apéry sum and an exact four-variable multinomial-square representation for the Domb sum. The explicit digit table reduces every pair to either a diagonal unit pair or a zero-Apéry/unit-Domb pair. A fourth-root cyclic coefficient extraction gives both integer frequency formulas; their mass is exactly \(5^L\). Positivity for \(L\ge3\) and the leading-digit-four extension prove infinite occurrence. The executable exact-integer checker has passed 300 direct comparisons, all complete small-level comparisons, and eleven exact formula levels. No finite test is treated as an infinite proof.

## Originality (O) — PASS within inspected sources, with material priority risk

The closest earlier theorem is Malik–Straub's 2015/2016 Lucas result (Theorem 3.1). It already implies both single-sequence digit products, and the present census is not independent of that strong input. Straub's January 2023 paper (Theorems 1.2–1.3) strengthens related congruences modulo prime squares; it does not state the joint Apéry–Domb pair histogram. The separate-sequence generating-function analysis by Caruso and collaborators is not a covering joint census either. Targeted primary-literature and published-result searches found no explicit same-parameter joint matrix, the seventeen missing pairs, or the conditional four-class bias. That is a bounded originality comparison, not a claim that the prior Lucas theorem is weaker in every logical sense. An unlocated prior exercise or an implicit pre-existing group-ring calculation could cover this result, so independent historical verification remains desirable.

## Mathematical value (V) — PASS

The joint law compares two classical prime-congruence sequences at exactly the first prime where the Apéry digit set has zero classes while all five Domb digits are units. The conclusion is a complete, all-depth indexwise classification, not merely a single checked congruence: only eight of twenty-five pairs are possible, each appears infinitely often, and the conditional Domb distribution on Apéry zeros has a sharp \((3^L-1)/2\) imbalance rather than uniformity at finite scales. The explicit joint finite-scale invariant offers natural benchmark data for more general joint congruence problems, while requiring no speculative downstream theorem.

## Closest sources and limitations

- A. Malik and A. Straub, *Divisibility properties of sporadic Apéry-like numbers*, arXiv:1508.00297, Theorem 3.1 and Sections 5–6: strongest directly relevant pre-existing prime-Lucas coverage; source of the digit-product method.
- A. Straub, *Gessel–Lucas congruences for sporadic sequences*, arXiv:2301.12248, originally posted 2023-01-28, Theorems 1.2 and 1.3: motivating literature and a stronger individual prime-square statement, but no joint census.
- Caruso–Fürnsinn–Vargas-Montoya–Zudilin, *Galois groups of Apéry-like series modulo primes*, 2026: studies both classical sequences in a different separate generating-function setting.

No extension modulo prime squares or general prime is claimed. Independent mathematical audit and exhaustive historical priority checking remain unperformed.

Self-review: passed. Independent audit: not yet performed.
