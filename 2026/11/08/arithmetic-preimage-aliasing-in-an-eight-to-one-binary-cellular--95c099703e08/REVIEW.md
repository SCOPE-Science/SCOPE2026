# Scientific self-review

## Correctness — PASS
The local rule is reproduced from Appendix B of arXiv:2610.33131v1. Four-bit de Bruijn vertices capture every length-five neighborhood and every cyclic word, including short rings. Closed-walk traces give exact inverse counts. Three integer characteristic polynomials are independently reconstructed by Newton identities from matrix traces and factor into roots of unity and zero; those identities algebraically determine every length, not only the tested range. A separate exhaustive direct-state enumeration checks ring lengths one through twelve and all length-sixteen alternating preimages. The period-sixteen conclusion follows from the all-length count, without requiring brute-force completeness at larger lengths.

## Originality — PASS within inspected evidence
The 2026 motivating paper explicitly lists this rule and proves bi-infinite eight-to-one LEO behavior, but its full-text Appendix B and surrounding graph-theoretic results do not state the cyclic inverse count arithmetic or minimum alternating predecessor period. The full text of Mariot–Leporati–Dennunzio–Formenti (2017), specifically its introductory scope and Section 3/Lemma 6, provides the general preimage-period algorithm and thus owns the method, but predates the specific 2026 local rule and does not state its formulas. Published published-finding corpus records relating to affine finite-volume clock factors and quadratic-rule invertibility concern different local rules/invariants. Search absence does not establish global historical novelty; unexamined specialized tables remain a risk.

## Mathematical value — PASS
Periodic input-output lifting and minimal spatial period are natural invariants of surjective cellular automata. The sharp impossibility of any cyclic precursor of a period-two alternating target below length 16, contrasted with eight precursors on every multiple of 16, is an exact arithmetic obstruction invisible to the known global eight-to-one property. The simultaneous complete six-divisibility census for homogeneous targets distinguishes two low-complexity output classes, and the sixteen-fold threshold is independent of the finite ring's size once divisibility is fixed. This resolves a naturally motivated explicit test case of a recently classified nonlinear non-bipermutive LEO rule. No general algorithm, arbitrary-output theorem or broad conjecture is claimed.

## Limitations and closest literature
The generic u-closure graph method of Mariot et al. makes the problem computable and is fully credited, not rediscovered. The present claim is a concrete arithmetic solution, not method-level novelty. Historical priority may be affected by unknown specialized computations or rule-equivalence tables; the record does not assert independent certification.

Self-review: passed. Independent audit: not yet performed.
