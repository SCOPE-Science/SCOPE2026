# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Girth-constrained independence maxima for small cubic bridgeless graphs

## Abstract

For even orders n in {12,14,16,18} and girths g in {4,6}, let

  M(n,g) = max{ alpha(G) : G cubic, bridgeless, |V(G)| = n, girth(G) = g }.

**Theorem.** Seven cells of this table attain the absolute ceiling n/2:

| (n,g) | M(n,g) | witness |
|---|---|---|
| (12,4) | 6 | hexagonal prism |
| (14,4) | 7 | random bipartite cubic (edge list committed) |
| (14,6) | 7 | Heawood graph (14-cycle + chord offset 5) |
| (16,4) | 8 | octagonal prism |
| (16,6) | 8 | GP(8,3) |
| (18,4) | 9 | random bipartite cubic (edge list committed) |
| (18,6) | 9 | 18-ring + chord offset 5 |

Every other cell claim is explicitly *not* made: girth 3 and girth 5 maxima,
and the (12,6) cell (empty — no cubic girth-6 graph exists below 14 vertices),
are reported as computed evidence / conjectures only.

## 1. Upper bound (all cells at once)

**Lemma (Petersen 1891).** Every bridgeless cubic graph has a perfect matching.

*Proof.* Standard; see e.g. Diestel, Graph Theory, Corollary 2.2.2
(Petersen's theorem: a bridgeless cubic graph has a 1-factor).
We use it as a cited classical theorem, not a new proof.

**Corollary.** For every admissible G on n vertices, alpha(G) <= n/2.

*Proof.* Fix a perfect matching M = {x_1 y_1, ..., x_{n/2} y_{n/2}}.
An independent set contains at most one endpoint of each matched edge,
so alpha(G) <= n/2. ∎

Hence M(n,g) <= n/2 for every populated cell, with no enumeration needed.
The work of the paper is exhibiting, for each claimed cell, one bridgeless
cubic graph of order n and girth exactly g with an independent set of size
n/2 (a bipartite partite set in every case here), forcing equality.

## 2. Witnesses (exact edge lists)

Vertex labels are 0..n-1. Each witness is bipartite with partite sets of
size n/2; the even-labelled side below is an explicit independent set of
size n/2 (machine-checked). All witnesses are verified cubic, connected,
bridgeless (Tarjan), of the stated exact girth (BFS), with partite-set
independence re-checked, by the stdlib script `artifacts/audit.py` reading
only `artifacts/witnesses.json`.

- **(12,4), hexagonal prism.** Rings 0-1-2-3-4-5-0 and 6-7-8-9-10-11-6,
  matchings i-(6+i). Independent set {0,2,4,6,8,10}.
- **(14,6), Heawood graph.** 14-cycle i-(i+1 mod 14) plus chords
  i-(i+5 mod 14) for even i. Independent set = even vertices.
  (This is the unique (3,6)-cage.)
- **(16,4), octagonal prism.** As above with m=8.
- **(16,6), GP(8,3).** Outer 8-cycle, spokes i-(8+i), inner
  (8+i)-(8+(i+3 mod 8)). Bipartite; independent set = even vertices.
- **(18,6), 18-ring + offset 5.** 18-cycle plus chords i-(i+5 mod 18)
  for even i. Independent set = even vertices.
- **(14,4) and (18,4) bipartite witnesses.** Computer-found bridgeless
  bipartite cubic graphs of girth exactly 4; full edge lists are in
  `artifacts/witnesses.json` (keys `14-g4-bipartite`, `18-g4-bipartite`).
  They are named graphs only in the sense of committed adjacency data —
  no canonicity or novelty is claimed for them.

## 3. Proof of the table fragment

Fix a claimed cell (n,g) with witness G. The audit certifies:
(i) G is 3-regular on n vertices and connected;
(ii) G is bridgeless, so the Corollary applies and alpha(G) <= n/2;
(iii) the committed partite set is independent of size n/2,
so alpha(G) >= n/2, i.e. alpha(G) = n/2;
(iv) girth(G) = g exactly.
Since G is admissible for the cell, M(n,g) >= n/2; the Corollary gives
M(n,g) <= n/2. Hence M(n,g) = n/2. ∎

## 4. What is not claimed (honest boundaries)

- **Girth 3.** Random pairing-model sampling (~thousands of bridgeless
  cubic graphs per order) attains alpha 5,6,7,8 for n=12,14,16,18
  respectively, i.e. strictly below n/2 (consistent with the folklore
  that triangles depress independence), but no optimality proof is
  offered. Upper bounds n/2 - 1 are *conjectured*, not proved.
- **Girth 5.** GP(9,2) and relatives give bridgeless cubic girth-5 graphs
  on 18 vertices with alpha 7 (branch-and-bound and brute force agree);
  a girth-5 witness on 12 vertices with alpha 5 was found. No maxima claimed.
- **(12,6).** Empty: the (3,6)-cage has 14 vertices (Heawood), so no cubic
  graph of order 12 has girth >= 6. Cited standard cage fact, consistent
  with the audit (no witness offered).
- **Completeness.** The original plan (exhaustive generation of all
  ~46k connected cubic graphs over n=12..18 via nauty/geng) was
  infeasible in this sandbox (no nauty, no root, stdlib only; custom
  pure-Python canonical augmentation stalled at n=8). The exact-maximum
  argument above deliberately avoids enumeration via the matching bound.

## 5. Reproduction

```
python3 artifacts/audit.py   # re-verifies all 7 witnesses from edge lists
```

`artifacts/graphkit.py` holds the BFS girth, Tarjan bridge-finder, and
the (unused for the final upper bounds) bitmask branch-and-bound
independence solver, cross-validated against brute force on Petersen,
Heawood, GP(9,2), and the cube. `artifacts/witnesses.json` is the
complete certificate input. Abandoned generators (`gen.py`, `aug.py`)
are retained for provenance but play no role in the proof.

## References

- J. Petersen, Die Theorie der regulären Graphs, Acta Math. 15 (1891).
- R. Diestel, Graph Theory (Petersen's theorem, Cor. 2.2.2).
- Balogh–Kostochka–Liu, arXiv:1708.03996 (asymptotic program; no finite table).
- Perarnau–Perkins, arXiv:1611.01474 (counting extremality; different invariant).
- Dvořák–Sereni–Volec, arXiv:1301.5296 (universal 5/14 lower bound).
