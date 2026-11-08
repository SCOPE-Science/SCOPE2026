# Self-review

**Claim reviewed.** Exact smallest dedicated-leader sets and their counts for
the fixed unweighted Laplacian on two \(m\)-cliques joined by \(k\) disjoint
matching edges, for \(m\ge3\) and \(2\le k\le m\).

## Correctness — PASS

The \(m\)-eigenspace of the partial-matching graph is precisely the kernel
of two explicit class-sum constraints of rank two. Its dimension is
\(2m-k-2\). With exactly that many input coordinates, the PBH condition
reduces to observing one vertex from every class except two with linearly
independent constraint columns. The three column types \(M,U,V\) show
that the omitted classes must have different types. The remaining
eigenspaces are explicitly calculated and detected. In the full-matching
case, the two multiplicity-\(m-1\) eigenspaces require one selected
endpoint from every pair except one. The exact counts follow by
exhausting the disjoint possibilities, with no probabilistic step.

Separate small-case tests build actual graph matrices, not merely
counting expressions. All 1,094 minimum-size subset comparisons in nine
cases agree with the theorem and a full Kalman-rank witness is checked.
Finite tests do not substitute for the dimension-general proof.

## Originality — PASS, with residual priority risk

The fully accessible 2014 zero-forcing paper studies controllability
for a qualitative family of matrices; the asserted theorem instead
classifies every minimum dedicated input set for a *fixed* graph
Laplacian. These differ concretely: at \(m=3,k=2\), 12 two-leader
sets control the fixed Laplacian, but only four of those are
zero-forcing. The 2019 threshold-graph result does not apply because
these graphs have induced four-vertex paths. The 2022 critical-set
study covers other named network families and does not state a
matched-clique enumeration. Published single-bridge forcing results
motivate excluding \(k=1\) from this theorem rather than claiming
that slice as new.

No accessible primary text or matching indexed result established
the complete \(2\le k\le m\) classification or the enumeration.
Unindexed or inaccessible equivalents remain a real risk; absence
from a search index is not proof of priority.

## Value — PASS

This is a natural fixed-dynamics input-location optimization on
two dense groups connected by a tunable number of matched bridges.
It gives not just the minimum control budget but the exact allowable
vertex configurations and an enumerative invariant for every
connectivity regime. The equality
\(N(m,m-1)=N(m,m)=m2^{m-1}\), despite different optimal-set geometries,
is an exact, interpretable transition. The finite non-zero-forcing
example shows why general strong-structural sufficient tests do not
settle the entire fixed-Laplacian problem.

## Limitations and literature

The claim excludes \(k=1\), \(m=2\), weighted networks, and generic or
shared input design. It does not extend its conclusions to all
graph-structured matrices. Closely related primary publications
are Monshizadeh–Zhang–Camlibel (arXiv:1403.4868),
Hsu (doi:10.1049/iet-cta.2018.5875),
and Dai (doi:10.1049/cth2.12385).

Self-review: passed. Independent audit: not yet performed.
