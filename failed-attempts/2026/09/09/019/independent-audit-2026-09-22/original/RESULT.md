# Certified Pasch census of STS(13) with anti-Pasch and PG(3,2) reference witnesses at STS(15)

## Context

Steiner triple systems (STS) are pairwise-balanced triple decompositions of complete
graphs. Pasch configurations (4 triples on 6 points) govern transversals,
resolvability, and the boundary between projective-plane-like and anti-Pasch
systems. Orders 13 and 15 are the first two complete non-trivial isomorphism
slices above the Fano plane (2 and 80 isomorphism classes respectively).
Anti-Pasch STS(v) are known not to exist at v = 7 and v = 13, so every STS(13)
contains a Pasch; an anti-Pasch STS(15) does exist. The exact per-class Pasch
numbers at orders 13/15 with replayable block lists and checker provenance were
the gap addressed here.

## Definitions

- An STS(v) is a set of 3-subsets (blocks) of a v-set such that every pair of
  points lies in exactly one block. Then v = 1, 3 mod 6 and b = v(v-1)/6
  (b = 26 for v = 13, b = 35 for v = 15).
- A Pasch configuration is a set of 4 blocks on 6 points. In an STS this forces
  every point to have degree 2 (a pair of disjoint block-pairs covering the
  same 6-set). Counting convention: each unordered 4-block set with 6-point
  union counts once.
- Two systems are isomorphic if a point permutation maps one block set to the
  other. |Aut| is the full automorphism-group order.
- System SHA: first 16 hex digits of sha256 of repr of the canonically sorted
  block list.

## Result

(a) STS(13) census. Up to isomorphism there are exactly 2 Steiner triple
systems of order 13:

- Type C13 (cyclic, Z_13 orbit system from base blocks {0,1,4},{0,2,7}):
  13 Pasch configurations, |Aut| = 39, system SHA 032e8986783928b2.
- Type T2 (non-cyclic): 8 Pasch configurations, |Aut| = 6,
  system SHA 8234c7fb64ba3bb2.

The exhaustive search over the canonical 7-block prefix F (6 pencil blocks
through point 0 plus block {1,3,5}) finds exactly 14400 labeled completions,
split 1920 of type C13 and 12480 of type T2 (1920 + 12480 = 14400, 0 others).
Pasch values are constant on each class ({13} resp. {8}).

(b) STS(15) witnesses (two named systems; the full 80-class spectrum is NOT
claimed):

- Anti-Pasch witness: 35-block system in artifacts/witness15_anti.json
  (system SHA 55b4a2d098b894c9), isomorphic to the cyclic STS(15) from base
  blocks {0,1,4},{0,2,9},{0,5,10} on Z_15, with 0 Pasch configurations
  (the absolute minimum, hence a minimal-Pasch extremal) and |Aut| = 60.
- High-Pasch reference: the point-line design PG(3,2) in
  artifacts/witness15_pg32.json (system SHA b8ca9d7914a921d2), constructed as
  lines {x,y,x+y} of F2^4 minus 0, with 105 Pasch configurations and
  |Aut| = 20160 = |PGL(4,2)|.

The two STS(15) witnesses are non-isomorphic. 105 is an attained reference
value, not a proven global maximum over the 80 STS(15) classes.

## Proof / evidence

1. Canonical-prefix lemma (STS(13)). Every STS(13) contains 6 blocks through a
   point plus, on the 12 remaining points, a block meeting 3 distinct pencil
   blocks (some block avoids the chosen point since 26 > 6, and it meets 3
   distinct pencil blocks). Relabelling gives the fixed 7-block prefix F, so
   every isomorphism type occurs among completions of F.
2. Exhaustive exact cover. Deterministic MRV bitmask search (stdlib only)
   enumerates all completions of F: 138 candidate triples on the 57 uncovered
   pairs give exactly 14400 solutions (~88 s on re-execution).
3. Isomorphism classification. Backtracking isomorphism search with
   third-point propagation and full Aut enumeration tests every solution
   against representatives: 1920 isomorphic to C13, 12480 to T2, 0 others;
   hence exactly 2 types. The verifier independently re-derives Aut 39/6.
4. Pasch counting, two independent implementations. Pairwise
   block-completion counter (each Pasch found exactly 6 times, asserted
   divisible by 6) and definition-level 4-block-subset 6-point-union counter
   (sound by the lemma that 3 concurrent STS blocks already span 7 points, so
   4 blocks on 6 points have max degree at most 2, hence all degrees 2) agree
   on every committed list: 13/13, 8/8, 0/0, 105/105. An independent
   fresh-code recount reproduces 13, 8, 0, 105.
5. STS(15) witnesses. The anti-Pasch system is byte-identical (same system
   SHA) to the cyclic STS(15) A above (measured 0 Pasch by both counters; 0 is
   the global lower bound, hence minimal). PG(3,2) is constructed directly as
   F2^4 lines (measured 105 by both counters); the stored list byte-equals the
   direct construction, and |GL(4,2)| = 15*14*12*8 = 20160. verify.py replays
   STS validity, both Pasch counts, both Aut orders, both SHAs, and pairwise
   non-isomorphism: all 28 checks VERIFY_OK.

## Limitations

- The full per-class Pasch distribution over all 80 STS(15) classes is NOT
  claimed; only the two named STS(15) witnesses are committed.
- Maximality of 105 over STS(15) is NOT claimed; it is a high-Pasch reference
  value attained by PG(3,2).
- The 14400/1920/12480 counts are labeled completions of the fixed prefix F,
  not isomorphism-class counts themselves; the class census (2 types) follows
  from the classification step.

## Reproducibility

Stdlib-only Python 3. From output/:

```
python3 artifacts/verify.py      # 28 checks, VERIFY_OK
python3 artifacts/census13.py    # full re-enumeration (~90 s) -> census13.json
```

Verification-critical artifacts copied to output/artifacts/: sts_lib.py,
verify.py, census13.py, dlxsolve.py, census13.json, witness15_anti.json,
witness15_pg32.json. Witness-generation search script (wit15b.py) is
provenance only; witnesses are verified purely from committed block lists.

## References

- F. Demirkale, D. Donovan, M. Grannell, Enumerations of maximum partial
  triple systems on 16 and 17 points, arXiv:1708.07646. Confirms 80 STS(15);
  Pasch data only for new 16/17-point systems.
- A. C. H. Ling, C. J. Colbourn, M. J. Grannell, T. S. Griggs, Construction
  Techniques for Anti-Pasch Steiner Triple Systems,
  doi:10.1112/s0024610700008838. General anti-Pasch constructions; v=7,13
  exceptional boundary.
- P. Kaski, P. R. J. Ostergard, The Steiner triple systems of order 19,
  doi:10.1090/s0025-5718-04-01626-6. Per-design Pasch census at order 19.
- M. Prazmowska, K. Prazmowski, Operation of weaving partial Steiner triple
  systems, arXiv:1403.4916. Weaving-product anti-Pasch series.
- J. T. Baldwin, Strongly minimal Steiner Systems III, arXiv:2201.11566.
  Model-theoretic infinite anti-Pasch families.
- M. J. Grannell, T. S. Griggs, E. Mendelsohn, A small basis for four-line
  configurations in Steiner triple systems, doi:10.1002/jcd.3180030107.
  Pasch count determines other 4-line counts; no values supplied.
- I. Yu. Mogilnykh, F. I. Solov'eva, Pasch configurations in Mollard Steiner
  triple systems, doi:10.1109/sibircon.2017.8109876. Mollard-family Pasch study.
