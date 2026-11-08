# Scientific assessment

## Correctness — PASS

The descendant-count formula is derived from disjoint descendant sets at a fixed depth, with exact enumeration for spine and tooth vertices. Convexity bounds the maximal number of branch levels in any length-\(n\) window and the root window supplies a matching lower bound. For each fixed power, increasing branch gaps force a diagonal Calkin image with essential norm exactly \(2\) after squaring. The factorization \(S-\lambda I=S(I-\lambda Q)\) proves surjectivity and preserves an infinite-dimensional kernel for \(|\lambda|<1\). The sharp resolvent lower bound is obtained from an explicitly normalized superposition of tooth vectors, not from finite sampling. The upper bound follows from the norm-convergent resolvent power series. All constants and ranges are explicit or quantified. A standalone checker passed 2,946 finite consistency tests.

**Risk and scope:** The checker cannot replace the analytic proof. The theorem does not give a leading resolvent constant or universality on the boundary circle.

## Originality — PASS (best-knowledge comparison)

Buckley and Seco's 2026 parent-shift paper supplies the general descendant-count framework and establishes universality subject to their assumption (A4) of infinitely many disjoint branching subtrees. The present comb has all branching vertices along one spine and fails that hypothesis. Its direct surjectivity argument, exact polynomial norm growth, uniform essential-power norm, and sharp resolvent exponent are not asserted by that paper. The published realization theorem for irreducible unilateral weighted shifts concerns equal ordinary and essential power-norm profiles; these combs instead have different profiles. Targeted searches for aliases such as directed-tree backward shifts, sparse spine branching, Calkin power-boundedness and polynomial resolvent growth found no statement implying the whole theorem.

**Risk and scope:** Classical results on directed-tree shifts and general polynomial resolvent growth might imply part of the theorem after specialization. The comparison is not an independently certified priority determination.

## Mathematical value — PASS

The theorem gives a whole continuum of explicitly defined unweighted operator examples for which Rota universality coexists with arbitrarily prescribed fractional polynomial growth exponents, even though the essential norm of every positive power remains fixed. This is a structural distinction between ordinary and Calkin dynamics and produces a sharp resolvent growth exponent and pairwise nonsimilarity across the family. It tests the relevance of branching-disjointness assumptions in a recently developed tree-shift framework, rather than computing an arbitrary finite instance.

## Closest literature and limitations

Buckley and Seco, *Rota universality of shifts on trees*, arXiv:2610.40089v1 (2026), is the principal motivation. Additional sources considered were Jabłoński–Jung–Stochel, arXiv:0911.3821; Chavan–Trivedi, arXiv:1510.03075v2; and Grosse-Erdmann–Papathanasiou, arXiv:2012.15542v3. No statement about all weighted or all directed trees is proposed.

Self-review: passed. Independent audit: not yet performed.
