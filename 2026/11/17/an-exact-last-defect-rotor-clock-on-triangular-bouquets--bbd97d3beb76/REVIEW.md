# Scientific review: An exact last-defect rotor clock on triangular bouquets

## Correctness — PASS

The claim concerns a fully specified chip-and-rotor state, rotor orders and initial hub direction, not arbitrary initial hub orientations. The published unicycle characterization establishes the necessary and sufficient recurrence criterion. The four exhaustively listed local rotor pairs cost two hub excursions of six moves when initially good and four moves when initially defective. The last untouched internal cycle proves all earlier states nonrecurrent, and first arrival at that cycle produces a unicycle, proving the exact clock. The binomial combinatorics then establish the all-size generating polynomial, sharp maximum and mean. A tight geometric trailing-good correction to a binomial defect count proves the central limit theorem. Independently coded state-repeat and functional-cycle checks agreed for 21,844 states over seven sizes. The formal proof, rather than these finite tests, supplies the all-size quantifier.

## Originality — PASS (best-knowledge)

Holroyd et al. (arXiv:0801.3306, Theorem 3.8) establish general unicycle recurrence; the inspected full-text sections do not supply these first-entry times. Poghosyan and Priezzhev (arXiv:1310.1225) study dimer/contour motion in recurrent rotor-router Euler tours, but only the abstract was inspected; equivalent results could remain in its uninspected body. Searches for rotor-router, Eulerian-walker, last-defect, unicycle, friendship-graph and windmill formulations and indexed nearby results revealed no matching formula or stronger statement. Records on triangular bouquets for majority, XOR, integer diffusion and parallel chip firing concern different update rules and do not imply the result. Remaining literature-priority uncertainty is explicit in AUDIT.json.

## Mathematical value — PASS

The exact time-shell polynomial distinguishes rare worst-case rotor initializations from normal fluctuations on an infinite, natural non-tree graph family. The exact last-defect mechanism simultaneously gives all counts, a sharp finite-size worst case and a Gaussian typical clock; it does not merely repackage the general unicycle theorem or report finite experiments. The restriction to one hub scan convention is essential and stated.

## Limitations

Absolute historical novelty is not certified, and independent mathematical review has not occurred. The formula is for one chip starting at the hub with a specified rotor scheme and independent peripheral initial rotors. It makes no assertion about all hub initial rotors or other cycle bouquets.

Self-review: passed. Independent audit: not yet performed.
