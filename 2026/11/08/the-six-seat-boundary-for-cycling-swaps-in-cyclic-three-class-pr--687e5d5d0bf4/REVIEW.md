# Scientific review: six-seat cyclic exchange dynamics

## Correctness — PASS
The finite statement quantifies over every type word for \(n=3,4,5,6\) and every distinct seat pair, so exhaustive finite enumeration supplies a complete decision proof, not a heuristic. The utility comparison accounts for exchanged agents retaining their original type but moving to the opposite seat; the pure-Python SCC implementation validates counts \(0,0,0,6\), all six component sizes \(6\), all \(36\) exact orbit states, and all six explicit positive-gain steps. The witness independently demonstrates actual strict cycling; the graph enumeration proves the minimality boundary. The scope does not extend to larger \(n\).

## Originality — PASS, with residual publication-priority risk
Berriaud, Constantinescu and Wattenhofer (arXiv:2305.09549) prove stable-seating existence for all three-class binary cyclic games (Theorem 6.6), including this cyclic approval pattern (Lemma 10); they also exhibit failure of swap convergence on a path with a different profile (Lemma 4). Neither theorem implies the first nonconvergent order for this highly symmetric binary cyclic class or its complete six-seat directed-component census. Their complete text, especially Sections 6.3.1, 6.3.2 and Appendix 0.A.5, was compared for this question. Ceylan, Chen and Roy (IJCAI 2023) focus on existence/optimization complexity rather than improving trajectories; only the abstract and accessible overview were available for that comparison. No matching exact result was found in the queried public and published-mathematics records; this is not proof of global novelty.

## Value — PASS
Three cyclic preference classes are the critical asymmetric binary case in the initiating paper's existence theorem. Proving the **first** failure of unrestricted swap convergence, despite guaranteed stable solutions, identifies a substantive distinction between static existence and dynamic attainability. The full smallest-order SCC census determines precisely where and how cycling begins, rather than merely providing an unrelated toy example; every bad state has the same balanced type counts and belongs to one symmetry orbit. These constraints and the exact finite boundary inform convergence claims and swap-rule design in this model.

## Scientific risks and limits
The result is a sharply scoped finite theorem, not a convergence theorem or equilibrium classification for arbitrary cycle size. Cycle-bearing SCCs have exits and are not absorbing. Full publication-priority verification outside accessible full text and indexed mathematical records remains unavailable. Evidence has not undergone an independent external audit.

Self-review: passed. Independent audit: not yet performed.
