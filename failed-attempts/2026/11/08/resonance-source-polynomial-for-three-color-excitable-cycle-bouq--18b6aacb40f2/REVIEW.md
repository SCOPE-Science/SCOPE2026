# Independent mathematical audit

## correctness

PASS

Over a three-step return, each vertex is identically zero or advances each step. A zero trace adjoining an advancing trace would see color 1 and could not stay zero. Thus on this connected graph nonzero return states are exactly colorings with a successor-colored neighbor at every vertex; all advance globally and have least period three. Trees are uniquely forced by leaf-to-root induction (child equal to parent minus one), and cannot support their roots. On a petal with hub phase fixed, each consecutive pair of differences must have preceding 2 or following 1, which gives exactly 2^a1^(L-a) or 2^a01^(L-a-1). Counting zero total modulo 3 in the two families gives respectively (r+1,r), (r,r+1) or (r+1,r) for L=3r, 3r+1 or 3r+2. Hub support is possible only in the pure 1 or pure 2 word, each valid exactly at 3|L. Independence at fixed hub phase, deletion of the no-support choices, and three possible hub phases give the asserted polynomial and all its corollaries; each orbit has three states with the same support count. `python3 /workspace/branches/independent_math_replay.py 1` exhaustively replayed three simultaneous updates using bit sets on 100,845 states of seven graphs, including a rooted branching attachment, a nonresonant example and mixed lengths; all histograms and the unique fixed point agreed. Proof rather than the finite check covers arbitrary lengths and trees.

## originality

FAIL

A distinct indexed theta-network result already gives the exact local transfer weights required for this census. Its terminal-coalescence specialization gives the complete frozen polynomial, not just the positivity criterion or a boundary case. This is demonstrated statement-and-proof coverage, not a claim about chronological priority between records with the same catalogue date.

## value

FAIL

Source redundancy in a bouquet is a natural observable, and the explicit formula is a useful exposition. But every coefficient and the deletion interpretation follow mechanically by identifying the terminals in the already source-resolved path counts, then applying a single constant-term subtraction. No separately motivated, nonmechanical surviving claim was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
