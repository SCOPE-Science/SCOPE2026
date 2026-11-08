# Scientific review

## Correctness — PASS

The exact domain is the incidence algebra of an ordinal sum of \(h\ge2\) nonempty antichains over any finite field. The radical is precisely the strictly upward interval span. In \(x^{h-1}\), only a chain passing through every consecutive level can contribute; hence the sole possible nonzero block is the product of consecutive random rectangular blocks. The number of right extensions of a fixed rank-\(r\) partial product to rank \(s\) follows by an invertible-coordinate reduction and an exact finite-field rank count. This proves the recursion, while the three-state width-two recurrence yields the closed expressions. The asymptotic ratio is a direct consequence of \(a/c=1-q^{-1}\). Exhaustive original-matrix checks in small prime fields and an independent extension-field implementation in \(\mathbb F_4\) passed. No finite enumeration is used to prove the all-parameter statement.

## Originality — PASS, provisional

Ladkani's derived-equivalence result and Quinn's incidence-algebra construction do not enumerate maximal-index radical elements; Fulman–Goldstein gives a single-uniform-matrix rank distribution, rather than the stated varying-width incidence-radical power distribution. A published result on Jordan lifts over finite dual numbers concerns a different ambient algebra, not a poset incidence algebra. The current contribution is the exact radical-stratum identification and transfer, its all-width count, and the width-two asymptotic rank-one concentration. Standard Gaussian-binomial matrix-rank formulas are fully credited. The main residual risk is an existing general theorem on ranks of finite-field matrix products, which could imply the transfer formula without an incidence-algebra statement; it was not established to subsume the complete final claim in the literature checked. The abstract of Petrov–Sokolov's later poset/Jordan paper was inspected, but its full text was unavailable here. Accordingly priority is provisional and not independently certified.

## Value — PASS

The maximal nilpotency index of a Jacobson-radical element is an intrinsic and natural finite-algebra invariant. The theorem computes the exact maximal-index stratum for every level-size profile and prime-power field, a computation that otherwise ranges over \(q^M\) radical elements. It also determines the canonical-rank refinement at the deepest radical power. The uniform-width-two specialization gives a closed formula and a sharp structural boundary: maximal-index elements become exponentially rare, and their top powers are asymptotically rank one, not full rank. This exact arithmetic classification and limiting behavior are motivated by radical stratification and finite-algebra representation theory, not by an arbitrary numerical slice. General finite-field rank enumeration is an input, not the claimed new result. Further value would come from extension to shorter powers or nonlayered posets; those are not asserted.

## Boundaries and closest literature

The theorem does not classify all nilpotency indices, Jordan types, or conjugacy classes. It makes no claim about the left-regular rank of a radical element. See the references and comparisons in `RESULT.md` and the structured review for material inspected and historical-priority risks. The prime-field and extension-field checkers are finite corroborations; the proof is the mathematical evidence for arbitrary parameters.

Self-review: passed. Independent audit: not yet performed.
