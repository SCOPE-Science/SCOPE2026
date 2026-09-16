"""Script N: prove the W-star family C7-free in general.
Setup: B_rec levels: V1^(0) (top, depth0), V1^(1) (depth1, = W's block), V2^(1) rest, etc.
x0 in V1^(0). Star edges: {x0, w1, w2}, w1,w2 in W=V1^(1).
Depth-profile of star edge: {0,1,1}. B edges: {d,d,e} with e>d.
Claim attempt: no C7 uses a star edge; B-only C7 impossible (descent lemma).
For a C7 containing star window {x0,w1,w2} (consecutive triple in cycle order),
analyze neighbor windows. Key: x0's B-links: {x0,y,w} with y in V1^(0), w deeper.
w1,w2 in W: their B-links within V2^(0)-subproblem.
Try: enumerate depth-profile words over alphabet {0,1,2+} for cycles containing
a (0,1,1)-window and show each forces a non-edge window. Computational proof for
the PATTERN part: enumerate all depth-words w in {0,1,2}^7 cyclic with some window
of type (0,1,1)-up-to-perm, check against allowed B-edge types {(d,d,e): e>d} +
star type {(0,1,1)}: which words survive? If NONE fully survives -> LEMMA PROVED."""
import itertools

def allowed(t, star=True):
    s = tuple(sorted(t))
    a, b, c = s
    if a == b or b == c:
        return False
    # B type: exactly two equal, third strictly greater
    if (a == b and c > b) or (b == c and a < b):
        return True
    # star type: {0,1,1}
    if star and s == (0, 1, 1):
        return True
    return False

surv = []
for w in itertools.product([0, 1, 2], repeat=7):
    wins = [tuple(sorted((w[i], w[(i+1)%7], w[(i+2)%7]))) for i in range(7)]
    if not any(x == (0, 1, 1) for x in wins):
        continue
    if all(allowed(x) for x in wins):
        surv.append(w)
print("depth-words with >=1 star-window and all windows allowed:", len(surv))
for w in surv[:40]:
    wins = [tuple(sorted((w[i], w[(i+1)%7], w[(i+2)%7]))) for i in range(7)]
    print(w, wins)
