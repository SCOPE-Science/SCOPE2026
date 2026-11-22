# Scientific review

## Correctness — PASS

The classification follows from a Cauchy–Schwarz incidence bound: every independent set meeting both shores of a projective-plane incidence graph has at most \(v-q\) members. Thus an independent set of size \(v\) or \(v-1\) lies within one shore. The graph diameter is three, so all colours numbered at least three are singletons; the second colour occurs at most twice and its two vertices, if present, must be nonincident on opposite shores. The resulting unique type-I centre / type-II leaf classification establishes the exact named count and the disjoint-star recolouring graph for every existing finite plane of order \(q\ge2\). The counting argument treats all planes, not just coordinatizable ones. Both finite-instance programs were run directly, confirming 50,400 named Fano states and 260 order-three reduced states.

## Originality — PASS with residual risk

Goddard and coauthors introduced broadcast colouring in 2008; Fresán-Figueroa, González-Moreno and Olsen proved the packing chromatic number of incidence graphs of finite projective planes in 2019. Neither the already-known palette threshold nor the fact that entire shores are maximum independent sets is claimed new. The new statement distinguishes and counts every optimal colouring, then proves that the full one-vertex recolouring graph is a disjoint union of stars, including its exact component count. The inspected 2019 full paper's theorem/lemma and the available 2008 primary material do not report this classification. Indexed nearby findings on projective-plane dominated colourings use a different validity predicate and do not imply packing recolourings. An unindexed equivalent theorem could exist; source coverage is necessarily incomplete.

## Value — PASS

Packing chromatic number alone says nothing about the structure or mobility of its minimizers. The exact optimum classification shows that all higher-colour singleton placements freeze while the single nonincident second-colour move has \(q^2\) choices, producing \(2v(v-1)!\) disconnected star components. This provides a meaningful all-order extremal mobility theorem on every finite projective plane, including non-Desarguesian planes, rather than a routine minimum-value recomputation.

## Closest literature and limits

Goddard et al., *Broadcast Chromatic Numbers of Graphs* (2008), source of the archival framework; Fresán-Figueroa et al., *On the packing chromatic number of Moore graphs* (2019), Theorem 3.1 and Lemma 3.1, already establishes the minimum palette. General \(S\)-packing definitions appear in Goddard–Xu (2012). We verified the relevant published theorem statement but cannot rule out older unpublished or unindexed enumerations. Finite scripts verify representative orders two and three, not every order. The proved claim assumes finite planes exist and is restricted to minimum palettes, fixed colour names and a single recoloured vertex per move.

Self-review: passed. Independent audit: not yet performed.
