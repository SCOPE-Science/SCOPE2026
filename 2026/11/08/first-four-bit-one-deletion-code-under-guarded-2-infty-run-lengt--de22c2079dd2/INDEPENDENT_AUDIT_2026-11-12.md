# Independent mathematical audit

## correctness

PASS

Enumerate exactly the 129 binary length-16 words whose all zero runs (including end guards) have length at least two and whose ones are isolated. Define compatibility as disjoint sets of all distinct length-15 one-deletion outputs. Any correcting code is a clique and conversely. The inspected exact branch-and-bound algorithm prunes solely using independent-set coloring upper bounds. An independently ordered exact graph-clique search found maximum 14 (87,059 search nodes), with the 14-word n16 witness and 16-word n17 witness having disjoint shadows. Zero-appending preserves admissibility and disjoint shadows by a three-case deletion argument, so no length below 17 can transmit 16 messages. This does not assert full M17.

## originality

PASS

Kulkarni–Kiyavash supplies general constrained deletion upper bounds and fractional-matching formulation, not the exact guarded n16 optimum or first 4-bit length. Earlier Resultary exact RLL optimization only through length 11 and has different/narrower finite range. No equivalent exact n16/17 threshold located, with unresolved priority from inaccessible older specialist articles.

## value

PASS

Minimum guarded blocklength for reliable transmission of a four-bit payload through one arbitrary deletion is a natural exact finite coding threshold. The sharp 14-word obstruction at n16 is not a textbook restatement of generic fractional bounds; a complete packing certificate plus explicit n17 16-message witness are reusable coding benchmarks even without a general asymptotic rate theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
