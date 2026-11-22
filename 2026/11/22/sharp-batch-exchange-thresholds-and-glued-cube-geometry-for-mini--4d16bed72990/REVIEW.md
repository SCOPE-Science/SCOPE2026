# Scientific review

## Correctness — PASS

For all labelled complete tripartite graphs with \(2\le a\le b\le c\), triangle-incidence counting gives the sharp minimum \(ab\). Equality forces exactly one removed edge per triangle and excludes edges with lower incidence multiplicity. The resulting binary exact-one equations classify all optimizers: one when \(b<c\), \(2^a\) when \(a<b=c\), and \(3\cdot2^n-3\) when \(a=b=c=n\). Family intersections are exactly the three pure sides. Batch-exchange Hamming distances prove the first nontrivial threshold and the three glued antipodal cubes, with the claimed edge count and diameter. The standalone `verify.py` checked 405579 feasible-bounded edge subsets on five small graph instances, balanced exact-one solutions for \(n=2,3,4\), and optimum-exchange metrics through \(n=7\). Finite computations are corroborative, not infinite proofs.

## Originality — PASS, priority provisional

Zhao and Li (arXiv:2611.08547v1, 2026-11-05) treat the complete multipartite extremal edge bound, but their Theorem 2 does not classify optimizers or their exchanges. Amarnani, De Burgos and Broughton (arXiv:2307.08824v1, 2023-07-17) establish triangle packing/covering equality on a broader host class, including a decomposition of triangle covers in Section 2; the numerical optimum is therefore known. Their Section 2 implicitly covers the complete-tripartite optimizer families, so those are treated as known structural inputs. Their inspected text did not discuss optimum-preserving batch-exchange graphs, thresholds, glued-cube metric geometry, or diameter. Related published mathematical results on Hamming triangle-free vertex sets and batch-induced-matching reconfiguration concern different objects and do not dominate this claim.

Historical-priority risk remains: Lakshmanan, Bujtás and Tuza (2012), *Small Edge Sets Meeting all Triangles of a Graph*, was available only as bibliographic information and abstract, not full text, and unindexed equivalent results are possible. A failed keyword search is not proof of uniqueness.

## Value — PASS

The optimal configurations of a classical triangle-edge-transversal problem are assembled into an exact reconfiguration geometry, yielding the smallest move budget permitting any nontrivial exchange. The balanced case yields a concrete family of highly constrained optimum states with a three-cube amalgamation, exact size, edge count and distance diameter. These features matter beyond the already-known scalar bound.

## Limitations

Exactly three partite classes, each of order at least two; only optimum-preserving atomic batch exchanges are studied. No statement is made about intermediate configurations inside a batch, higher multipartite graphs, or independent audit. The preceding historical-priority risk is not resolved.

Self-review: passed. Independent audit: not yet performed.
