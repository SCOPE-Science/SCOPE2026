# Review of finite weight-three two-read reconstruction capacities

## Correctness — PASS

The exact domain is all thirty integers \(3\le n\le32\), with all \(\binom n3\) weight-three indexed binary words. For every one, the package provides a collision-free independent set of size \(M_3(n)\) and a partition of the entire candidate set into the same number of deletion-confusability cliques. The lower and upper bounds match, certifying finite optimality without relying on a numerical solver. `verify_direct.py` reads and verifies every certificate and all induced pairs needed for both inequalities. `verify_structural.py` independently checks the overlap definition at smaller lengths and selected larger witness sets. These tests establish **finite exactness**, not infinite behavior.

## Originality — PASS, qualified

Related prior art includes the source-general multiple-trace framework of Sala et al. (2016), the unrestricted two-read deletion theory of Chrisnata–Kiah–Yaakobi (2020), and published indexed results on weight-two two-read codes and weight-three one-read codes. The former does not determine induced-subgraph independence numbers by fixed weight; the latter two address different weights or a stronger one-read error criterion. Related graph degree, edge, and triangle counts also do not imply \(M_3(n)\). Database records were checked by scientific statement/implication. Directly inspected public main-text sections of the foundational papers did not furnish the finite table. Some relevant indexed records were available only by summaries, not full-text review; unindexed exact computations remain a priority risk. Discovery by failed keyword search is not asserted as novelty proof.

## Value — PASS

Constant-weight sources are a natural sparse-marker coding model. This is a complete exact capacity census through the standard 32-symbol finite-blocklength cutoff, not a single arbitrary length: every feasible weight-three word at each length is covered by rigorous matching optimality certificates, yielding an implementable sharp design limit. The all-range numerical pattern is reported only on its proved interval. No general theorem or downstream asymptotic code is claimed.

## Closest literature and restrictions

See the references in `RESULT.md` and comparison details in `AUDIT.json`. Priority beyond the inspected records, especially unindexed finite tables, is unresolved. The mathematical validity is internal to the finite certificates; independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
