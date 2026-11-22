# Scientific review: three-site maximal-distance-minimizer phase portrait

## Correctness — PASS

The claimed object is the shortest connected compact planar network visiting three equal-radius closed disks centered at \((-1,0),(1,0),(0,h)\). The three-terminal Steiner-tree inequality reduces the unrestricted network problem to minimizing the convex sum of point-to-disk distances. Symmetry reduces it to a one-variable piecewise elementary function whose minimum occurs at the constrained Fermat height \(1/\sqrt3\). The supporting interval, all boundary cases, the enclosing-disk collapse radius, and the order in which branches disappear are derived explicitly in `RESULT.md`. The projection-segment construction realizes equality. The stdlib verification program passed 644 formula/projection tests and 20 independent two-dimensional grid comparisons; a separate global numerical optimizer passed 200 randomized cross-checks. The analytical argument, not the finite tests, justifies the universal quantifiers.

## Originality — PASS, subject to historical-priority risk

A 2026 open-problems collection gives the maximal-distance-minimizer definition and asks for explicit target sets, but does not state this isosceles two-parameter profile. The classical three-terminal Steiner solution and the existence of three-point tripod and segment examples are known; these are explicitly credited. The 2022 inverse-problem paper (Observation 2.11, Proposition 2.14) explicitly covers the finite-site Steiner reduction and the initial trimmed-tripod regime for sufficiently small tolerance; both are acknowledged as prior art. Its statements inspected do not imply the later large-radius phases or the displayed global \((h,r)\)-portrait. A related indexed four-site square result is a different geometric family and does not itself imply the three-site classification. Searches under maximal-distance minimizer, disk-transversal Steiner tree, neighborhood-network, and Fermat–Torricelli aliases revealed no direct covering theorem. Indexed-search failure is not proof of novelty; historically unindexed equal-disk network literature and the inaccessible full four-site record are residual risks.

## Mathematical value — PASS

The target is the minimal noncollinear finite MDM configuration, and the tolerance radius changes a network's topology rather than merely its scale. An exact complete classification over two continuous geometric parameters identifies five canonical network types, their sharp boundaries, and the exceptional direct three-arm-to-point collapse at the natural shape threshold \(h=\sqrt3\). The result supplies a reusable exact test case for geometric network optimization and is not offered as a solution of the open circle, stadium, or arbitrary-compact-set problems. The qualitative three-point shapes alone would not be claimed as new; the complete simultaneous length/topology profile is the valued contribution.

## Scope and limitations

The theorem constructs canonical minimizers but does not classify every minimizer or prove uniqueness. It is restricted to three equally tolerant isosceles sites. Its proof assumes standard elementary facts about rectifiable connected continua and three-terminal Steiner trees, which are explained in the result. The secondary computational tests are finite sanity checks. A further independent literature review is warranted before any priority claim.

Self-review: passed. Independent audit: not yet performed.
