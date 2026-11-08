# Self-review

## Correctness — PASS

For every positive integer \(n\), its nonzero base-\(3\) digit product is \(2^{t(n)}\), with \(t(n)\) the count of digit \(2\). An odd prodigious integer must use only digits \(0,1\), whose lowest two digits restrict its residue modulo \(9\) to \(\{0,1,3,4\}\); this set permits no three consecutive step-\(2\) residues. For even integers, the seven classes \(26,50,62,74,78,98,106\pmod{108}\) each have exactly one factor of \(2\), but at least two digit-\(2\)'s in the lowest three ternary positions. Their cyclic separation among even residues modulo \(108\) has largest gap \(14\); any fourteen step-\(2\) even terms hit an obstruction. The \(13\) terms from \(108\) through \(132\) pass the exact divisibility test. Adding \(4\cdot3^K\), \(K\ge5\), leaves all their digit products unchanged and preserves divisibility, yielding infinitely many attaining examples. All finite claims can be independently recalculated with the included script; the universal statement is proved by modular exhaustion, not search to a finite cutoff.

## Originality — PASS within inspected evidence

The closest source, Gohn et al., *Arithmetic Progressions of b-Prodigious Numbers* (Journal of Integer Sequences 25 (2022), Article 22.8.7), was inspected through its introduction, Theorems 3 and 5, the following maximality results, and its concluding section. Its arithmetic-progression formula assumes \(d\mid b\) or \(d=b/2\) for even \(b\). Those assumptions exclude the present \((b,d)=(3,2)\) parameter pair; it does not imply the exact value \(13\). Sanna's 2018 arXiv paper concerns counting functions rather than progression maxima. OEIS A055471 lists decimal prodigious numbers, not the ternary sharp difference-\(2\) invariant. Targeted indexed searches did not reveal an equivalent theorem. An unindexed or later equivalent statement remains a possible risk.

## Mathematical value — PASS

This is the first omitted positive-step case for the smallest nonbinary base of the established prodigious-progression problem: the published theory includes step \(1\) but not step \(2\) in base \(3\). The exact answer \(13\), as contrasted with the known consecutive-step maximum \(5\), is not a direct substitution in existing formulas; its upper bound uses a concrete mixed radix/valuation obstruction, while infinitely many starts achieve it. Exact small-base sharp cases are natural calibration results for the broader unaddressed case \(d\nmid b\), not arbitrary numerical slices.

## Closest literature and residual limits

Relevant primary references: Gohn et al. (2022), https://cs.uwaterloo.ca/journals/JIS/VOL25/Wong/wong42.pdf; Sanna (2018), https://arxiv.org/abs/1809.05463; OEIS A055471, https://oeis.org/A055471. The proof establishes no claims for other \((b,d)\) pairs, does not classify all maximizing starts, and is subject to the usual risk of undiscovered equivalent prior work.

Self-review: passed. Independent audit: not yet performed.
