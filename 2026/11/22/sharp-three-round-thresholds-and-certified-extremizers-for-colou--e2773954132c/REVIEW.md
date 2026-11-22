# Scientific review: sharp three-round coloured-pair thresholds

## Correctness — PASS

The proof derives an exact three-step full-pair criterion from the recursive rank definition. For each of the \(q\) classes defined by a distinguished root, its selected partner needs \(q\) additional distinct witnesses, forcing \(q^2+q+1\) vertices. Counting root support and all \(q^2\) partner-to-class nonzero incidences, with overlap possible only on the \(inom q2\) partner pairs, proves the all-size minimum \(q^3-inom q2-1\). A canonical equality construction realizes the bound for any converse involution. The normal-form proof uniquely identifies each peripheral vertex from its state to its own partner, yielding the precise certified isomorphism-type product. The independent definition-level recursion and structural checker pass in `checker.py`; finite checks do not substitute for the general proof.

## Originality — PASS within inspected evidence

The rank definition and general finite-rank construction in López-Callejas–Navarro-Castillo (arXiv:2604.14461v1, 2026-04-15) are prior work. The published graph extremal result of 2026-11-08 already proves the \(q=2\) values \(7\) and \(6\) and unpointed uniqueness; no novelty is claimed for that specialization. Its full proof and the relevant original arXiv HTML sections were inspected. Searches of published-finding corpus and the web for the state-general threshold, the oriented \(13\)/\(23\) case, equivalent full-pair profiles, and the \(5832\) certified count did not disclose an exact or stronger covering result. This supports best-knowledge originality; it does not certify worldwide priority, and equivalent unindexed earlier results remain a risk.

## Value — PASS

The contribution is a structural, all-parameter extremal theorem for a natural class of finite models, not a routine small-order census. It simultaneously provides sharp host order, sharp nonzero-support complexity and a complete minimum-order certified-extremizer classification. The oriented three-state case has a nontrivial new threshold and thousands of explicitly parametrized certified shapes. The value lies in the natural exact frontier and its equality structure, without invoking any speculative downstream results.

## Limits and references

The \(5832\) count is of **rooted-and-certified** structures and is not an unpointed oriented-graph count; it must not be interpreted otherwise. Only the minimal-order equality types are fully enumerated. The optional checker is a finite corroboration, not an infinite theorem prover. Relevant sources:

- C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461v1, 2026-04-15: https://arxiv.org/html/2604.14461v1
- *Sharp rank-three onset and six-edge extremum for finite graphs*, 2026-11-08: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-rank-three-onset-and-six-edge-extremum-for-finite-graphs--a3c35b6162f1/RESULT.md

Self-review: passed. Independent audit: not yet performed.
