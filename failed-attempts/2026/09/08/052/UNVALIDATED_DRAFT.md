# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Complete-cap witnesses in AG(3,4): verified sizes {8,10,12,13,14,16}, puncture certificates, and a partial 9-search log

## Abstract
We fix coordinates AG(3,4) = F4^3 (64 points, 336 affine 4-point lines) and certify,
by two independent stdlib-only Python programs with byte-identical incidence data,
explicit complete caps (no three collinear; every exterior point on a secant) of sizes
8, 10, 12, 13, 14, 16; a per-point secant cover for the 8-cube; exact puncture data
(all 12+66+220 subcaps of our 12-cap of sizes 11/10/9 are incomplete); and a logged
partial search of 1,057,473 nine-caps containing {0,1} with zero complete examples.
We do NOT prove maximality, a completeness gap, or absence at sizes 9/11/15.

## 1. Coordinates and definitions
- F4 = {0,1,2,3} with addition = XOR and multiplication 1*x=x, 2*2=3, 2*3=1, 3*3=2, 0*x=0.
- Point id = 16x+4y+z for (x,y,z) in F4^3; 64 points 0..63.
- Directions: 21 nonzero vectors with first nonzero coordinate 1. Lines: 336 cosets of
  4 points. Verified: every one of the C(64,2)=2016 pairs lies on exactly one line.
- Cap: no line contains >=3 of the set. Secant: line with exactly 2. Complete cap:
  cap + every point outside the set lies on at least one secant.

## 2. Theorem (verified fragment)
The following point sets are complete caps in AG(3,4):
- size 8 (cube): [0,1,4,5,16,17,20,21] (= F2^3 embedded as {0,1}^3);
- size 10: [13,17,23,30,31,37,40,52,57,62];
- size 12: [6,15,18,25,28,39,40,43,57,59,62,63];
- size 13: [4,7,13,14,34,35,36,44,46,48,50,53,55];
- size 14: [0,3,13,15,16,18,21,22,37,38,45,47,50,51];
- size 16: [3,5,10,12,19,22,27,30,32,39,43,44,48,52,58,62].
Moreover: (a) each of the 56 points outside the 8-cube lies on an explicit cube secant
(stored per-point cover); (b) every 11-, 10-, 9-subset of the listed 12-cap is a cap
but none is complete (counts 12/66/220 caps, 0 complete).

## 3. Proof (computation, replayable)
1. Rebuild F4/lines as above; assert 21 directions, 336 lines, pair-uniqueness 2016/2016.
2. For each witness: assert distinctness, range, cap property (all 336 line intersections <=2),
   and completeness (secant-covered exterior = all exterior; uncovered list empty).
3. Cube cover: for each of 56 exterior points store a 2-subset of the cube collinear with it;
   verifier checks both cube-membership and line incidence.
4. Puncture: enumerate C(12,11)+C(12,10)+C(12,9) subsets, test cap and completeness directly.
All checks pass under an independent verifier (`verify.py`) using its own line build,
separate from the search library (`caps3034.py`). Log: `verify.log` ("ALL CHECKS PASS").

## 4. Partial 9-search (evidence only, NOT a theorem)
Depth-first cap enumeration fixing {0,1} (`enum9.py`) with a 2M-node budget enumerated
1,057,473 nine-caps and found 0 complete ones (92 s pilot). This is explicitly
non-exhaustive and is reported only as a logged partial-search artifact, not absence.

## 5. What is NOT claimed; conjecture vs proof
- Proved: the witness/completeness/puncture facts above (machine-checked).
- Computed evidence (not proof): failure to find complete 9-, 11-, 15-caps by annealing/greedy.
- Conjecture/uncertainty: whether complete caps exist at 9/11/15; the maximal size and any
  integer gap over 9-14; minimality of the small examples. Exhaustive census is open.
- Originality: no claim of novelty for the 8-cube (standard F2^3 embedding); novelty claimed
  only for the explicit checked package (witnesses + puncture + replay pipeline) as a citable
  fragment. No literature exhaustive AG(3,4) 9-14 census was found by the lane's triage, but
  a missed prior source remains possible (see report limitations).

## 6. Reproduction
```
python3 output/artifacts/verify.py        # full replay, expect ALL CHECKS PASS
timeout 100 python3 output/artifacts/enum9.py  # partial-9 pilot (2M nodes)
```
SHA256: caps3034.py cfbbc69c..., witnesses.json bbdc6869...,
cube_secant_cover.json 8a1ba56a..., verify.py 6db5e962..., enum9.py 74385f41...
