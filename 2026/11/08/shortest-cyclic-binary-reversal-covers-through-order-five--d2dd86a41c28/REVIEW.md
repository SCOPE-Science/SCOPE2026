# Scientific review

## Correctness — PASS

The claimed domain is the complete finite set of circular binary words of orders \(1\) through \(5\), with reversal applied to factors and rotation used to identify cycles. Burnside counting gives \((2^n+2^{\lceil n/2\rceil})/2\) required factors. Every covering cycle contains a window \(0^n\), which reduces the complete search to rooted words. An explicit bitmask/suffix-state recurrence certifies nonexistence at every shorter candidate length and the exact rooted counts at the optimum. Separate direct enumeration agrees on optimal lengths, rotation classes, symmetry classes and the lists of all order-four and order-five optima. Both independent programs were executed successfully on these exact inputs.

## Originality — PASS, with historical-priority risk

Burris–Motta–Shipman (arXiv:1608.08480, sections 3–5) study unoriented de Bruijn sequences and Eulerization, including linear examples at orders four and five, but do not enumerate optimal binary circular necklaces or prove these cycle-count values. Fici et al. (arXiv:1511.08431, sections 1–5) develop linear shortest-superstring-with-reversals approximation and complexity results, not an exact cyclic census. Targeted literature and research-record searches did not identify the length-and-count statement. The absence of indexed matches does not prove absolute historical priority; specialized older tables remain a risk.

## Value — PASS

Reverse-direction coverage is a natural superstring/universal-cycle requirement. The first orders after the one-visit obstruction are a motivated test of how closing the word changes the covering optimum. The result supplies sharp cyclic lengths, all optimal cycles and the reversal/complement symmetry census rather than a routine witness or a merely numerical upper bound. This exact finite classification makes explicit the boundary between ordinary de Bruijn traversal and reversal-constrained cyclic covering.

## Scope and remaining limits

No higher-order, nonbinary, reverse-complement or noisy-channel claim is made. A finite exhaustive proof is legitimate because all shorter lengths and all optimum candidates are enumerated and the programs implement precisely stated recurrences; it should not be extrapolated to unexamined orders.

Self-review: passed. Independent audit: not yet performed.
