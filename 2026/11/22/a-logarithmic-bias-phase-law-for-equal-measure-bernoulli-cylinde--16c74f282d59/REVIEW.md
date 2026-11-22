# Scientific review

## Correctness — PASS

The theorem is proved for every integer \(k\ge3\) and every \(0<p<1\), not extrapolated from finite cases. The weighted autocorrelation polynomials are derived by listing all proper borders of the two specified words. Substituting the two polynomials into the standard first-hit denominator gives the explicit one-variable equation \(G(p,t)=0\) with a unique root in the required interval. Its derivative bounds show that \(t(p)\) is strictly decreasing; the crossover factor \(H_k(p)\) is therefore strictly increasing. Strict opposite endpoint orderings, the continuity of the Perron roots, and the unique possible equality together prove exactly one actual crossing. Polynomial elimination gives the unique algebraic \(t_k\), and a uniform implicit expansion proves both asymptotic coefficients. Critical boundary checks include \(D_U(1/q)<0\), \(D_V(1/q)<0\), and the positivity of the quadratic \(q^2-pq+kp^2\).

`CHECK.py` independently compares exact finite-state survival probabilities with generating-function coefficients for 1,848 rational cases and tests 630 additional overlap/phase conditions, including known \(k=2\) behavior. Finite diagnostics are supportive only; the proof, not enumeration, establishes the universal theorem. No independent audit has been performed.

## Originality — PASS within inspected evidence

The nearest published overlap is Bonanno–Cristadoro–Lenci (2022), Remark 3.7: it already exhibits the \(k=2\) pair and observes a numerical bias crossover. That instance is explicitly excluded from the new parameter claim. Proposition 2.4 in the same work gives the general weighted denominator but not the all-\(k\) unique crossing or \(\log 2\) two-term asymptotic for \(k\ge3\). Chandgotia–Marcus–Richey–Wu (2024 preprint) provide general unweighted forbidden-word shift structure, while Bóna–Maga–Richey (first public 4 June 2026) analyze border-dependent letter frequencies and pose broader ordering questions. The full accessible relevant sections and exact example in the primary 2022 text were compared at the level of statements and implications. Published research-record searches of the pair family and the logarithmic threshold did not identify a matching theorem. The possibility of an unlocated older formulation, or a longer worked example elsewhere, remains a priority risk; a search gap alone is not proof of novelty.

## Value — PASS

Two holes have exactly equal Bernoulli measure for every bias yet reverse their escape ordering once, at a parameter that is fully classified for an unbounded natural family. The structural competition is between \(k\) zero-only self-overlaps and one long mixed self-overlap. The logarithmic scaling \(p_k\sim(\log2)/k\), together with the explicit second-order term, gives a sharp parameter scale that the isolated published \(k=2\) example cannot predict. This is a genuine parameter-phase theorem for open symbolic dynamics, not a new numerical value for an old six-symbol pair or a routine formula substitution.

## Closest source and limits

Bonanno, Cristadoro and Lenci, *Maximal escape rate for shifts* (2022), Proposition 2.4 and Remark 3.7, https://arxiv.org/html/2112.14248v2. The general weighted-correlation identity and previously known length-six crossover are credited. The theorem applies to iid binary sources and exactly the stated family; it makes no broader optimality claim. Historical priority is provisional. Mathematical independence has not been established.

Self-review: passed. Independent audit: not yet performed.
