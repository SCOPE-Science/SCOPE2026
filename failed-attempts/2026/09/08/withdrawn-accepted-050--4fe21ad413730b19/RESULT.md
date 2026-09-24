# Certified binary 2-abelian-cube-free words of length 200000

## Context
Huova–Karhumäki (arXiv:1104.4273, 2011) introduced k-abelian avoidability and left open the smallest alphabet avoiding 2-abelian cubes: two or three letters. The only computational evidence cited there is a binary 2-abelian-cube-free word of length 100000. Ternary 2-abelian-square-freeness terminates (longest length 537) and 4-letter abelian avoidability is infinite, so the binary 2-abelian-cube case is the live open boundary. No longer witness or obstruction dataset was found in the nearest priors, exact-phrase arXiv search, or OEIS.

## Definitions
Alphabet {0,1}. Blocks X, Y with |X|=|Y|=m are **2-abelian equivalent** iff first(X)=first(Y), last(X)=last(Y), and the four digram counts (00,01,10,11) inside each block agree. For m=1 the digram counts are vacuous, so 000 and 111 are the m=1 cubes. A **2-abelian cube** is three consecutive length-m blocks pairwise 2-abelian equivalent. A word is **2-abelian-cube-free** if no factor is such a cube.

## Result
There exist two explicit binary 2-abelian-cube-free words of length 200000, doubling the published 100000 benchmark:
- `word_200000_seed1.txt` (canonical): 200000 bits, 100001 zeros + 99999 ones; sha256 `3a6a502c258b46d9315c8a17c381bcdb989d70f815a499ffa87ff3db2a0823b9`; begins `11001100100101001011…`, ends `…1011001011001010010100`.
- `word_200000_seed0.txt` (second witness): 200000 bits; sha256 `d553031fccd00bb20e3cbc806dd75d07e66591a7aa72e5fb15e55fe46d441d9d`.
- Constructor `search.c` (deterministic seeded greedy DFS with backtracking; 75763 backtracks seed 1).
- Obstruction profile for the seed-1 run: 149086 blocked placements, 75764 backtrack rows, 1178 distinct arms, max arm m=33707; top arms m=1: 68754, m=2: 13412, m=3: 10622, m=6: 8778, m=9: 5714. Tables: `obstruction_histogram.csv`, `obstruction_sample.csv` (first 5000 native rows with digram signatures).
- No claim of infinite avoidability is made; this is a finite benchmark advance.

## Proof / evidence (computational certificate)
Standalone checker `verify.c` rebuilds digram prefix sums Q[k][i]=#{pairs starting at j<i} from the filed letters only, then tests every end position e and arm m (3m<=e) with boundary-letter early exit; m=1 handled exactly as 000/111; m=2 by direct digram compare. Digram count in [l,r) is Q[r-1]-Q[l]; block windows are exactly the m-1 internal digrams of each arm. Total candidate pairs at n=200000 is 6666633333 = sum_e floor(e/3).
- Full replays (auditor-rebuilt binary): `OK: length 200000 2-abelian-cube-free (checks 6666633333)` for **both** words (~46 s in C).
- Regression: `001001001` reports `CUBE at s=0 m=3`; `000` reports `CUBE at s=0 m=1`.
- Cross-check vs independent brute-force checker `brute_check.py` (stdlib Counters, no prefix sums): both 2000-prefixes OK under both programs; 40/40 random-word first-cube agreement; auditor re-checked 1500-prefixes OK.
- A prior checker window bug (wrong digram windows for the first two blocks) was found and repaired (two-line fix, dead loop removed); words and scope unchanged; all archived replays use the repaired checker.
- Reproduction: `gcc -O2 -o verify verify.c && ./verify w.txt` → expect `OK: length 200000 2-abelian-cube-free`; `gcc -O2 -o search search.c && ./search 200000 1 w.txt obs.csv` regenerates the canonical word and native log (~1 min).

## Limitations
- Finite benchmark only: pressures but does not resolve the open 2-vs-3-letter threshold.
- Obstruction profile describes this greedy search's failures, not an intrinsic density census.
- Verifier is O(n^2/6) (~46 s in C at n=200000); fully-vectorized Python audit was too slow and not used as the certificate.
- Only binary alphabet tested; no ternary comparison.

## Reproducibility
Word files (200001 bytes = 200000 bits + newline), `verify.c`, `brute_check.py`, `search.c`, verify logs, regression and cross-check logs, and obstruction histogram/sample tables are archived in `output/artifacts/`. SHA256 hashes listed above and in METADATA.

## References
- M. Huova, J. Karhumäki, Observations and Problems on k-abelian avoidability, arXiv:1104.4273 (2011).
- M. Rao, M. Rosenfeld, Avoidability of long k-abelian repetitions, arXiv:1507.02581 (2015).
- A. Glen, B. Halldórsson, S. Kitaev, Crucial words for abelian powers, arXiv:0812.4730.
- J. Cassaigne, G. Richomme, K. Saari, L. Q. Zamboni, Avoiding abelian powers in binary words with bounded abelian complexity, arXiv:1005.2514.
