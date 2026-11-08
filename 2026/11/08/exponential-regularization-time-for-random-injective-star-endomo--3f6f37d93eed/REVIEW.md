# Self-review

**Claim reviewed:** the complete finite-size coefficient formula for the first regular-power distribution in injective partial star endomorphisms, and convergence of the time scaled by \(\sqrt{n-1}\) to the mean-one exponential distribution.

## Correctness — PASS

The source's Theorem 2.3 identifies precisely which individual maps are regular. Restricting to maps with the hub absent from their domain yields an exact deficiency law with successive-weight ratio \((m-j)/((j+1)(j+2))\), and an exponentially tight concentration window around \(\sqrt m\). The exact conditional survival probability of a backward chain of length \(r\) is a finite product whose logarithm tends to \(-x\) at \(r=\lfloor x\sqrt m\rfloor\). A Lah-number count shows that a typical map has a nontrivial cycle. The cycle keeps nonhub images alive in every power and makes the first regular power exactly one more than the hub backward-chain length. The exact survival formula subtracts a rank-one exceptional event enumerated by ordered path forests with bounded component lengths, giving a coefficient of \(\exp(\sum_{s=1}^t z^s)\). Direct enumeration through six vertices, all exact finite-size survival identities, and numerical limit checks passed. No finite experiment is treated as proof.

## Originality — PASS (provisional publication priority)

Dimitrova–Fernandes–Koppitz (arXiv:2401.11741v1) established the monoid classification and fixed-element regularity; these are explicitly prior. Their sequel (arXiv:2410.21084v1) gives presentations. Ganyushkin–Mazorchuk (arXiv:math/0511431v1) developed general partial-injection chain/orbit counts, Lah numbers and square-root defect behavior. Janson–Mazorchuk (2005) gives sharp cardinality and deficiency asymptotics. Laradji–Umar (2013) already derives bounded-path nilpotent generating functions: the exponential generating-function kernel of the exact correction is credited as prior, not original. Its inspected results do not state the first-regular-power limit theorem for star endomorphisms. The new result is therefore the complete first-power-hitting distribution with a bounded-path-forest correction, together with its exponential scaling law, not the general theory of partial injections or static regularity. A previously published dominating hitting-time theorem would supersede the novelty conclusion and remains the main residual risk.

## Mathematical value — PASS

A semigroup whose nonregular elements are explicitly characterized invites a quantitative question: how many repetitions of a typical nonregular map are required to reach the regular part? The exponential limit distinguishes typical random power dynamics from fixed-element Green-relation theory and demonstrates nonconcentration at the natural \(\sqrt n\) scale. The exact finite-size formula also determines every hitting-time multiplicity and explains a nontrivial exceptional forest correction. It is an infinite-family structural probability law with an explicit mechanism, rather than a routine finite count.

## Limitations and independent status

Only injective partial endomorphisms of growing stars, sampled uniformly, are covered. Earlier precise cardinalities and regularity criteria are prior literature. Bibliographic priority is subject to further independent checking, notably of general partial-injection limit theorems. Verification did not include an independent mathematical review.

Self-review: passed. Independent audit: not yet performed.
