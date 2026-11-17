# Independent mathematical audit

## correctness

PASS

PASS: Every query leaves ℓ positive and n−ℓ negative starts, hence a depth-d tree needs 2^(d−1)≤w=min(ℓ,n−ℓ). Root query at x=ℓ−1 leaves consecutive blocks of 2^floor(log₂w) starts on either branch. Every block of size ≤w can be split exactly at a chosen prefix by querying its cut position; balanced recursive cuts attain 1+floor(log₂w). Cyclic-gap traces yield 1+n z+n(w−1)z² (no triple can be shattered). Łoś transfers fixed finite-depth witnesses and finite 2-rank characterizes stability of this formula. Independent exact rank/minimax checks for all 136 (n,ℓ) pairs n=2..17 matched. Not a classification of the entire ultraproduct theory.

## originality

PASS

PASS qualified: Existing general thicket/2-rank–stability equivalence, the 4-point translate special case, and fixed-width intervals on a finite chain do not themselves enumerate the exact cyclic-window adaptive rank for every width. Chain windows have boundaries and only n−r+1 starts, whereas here n cyclic starts with complementary width symmetry. Best-of-knowledge originality only; a reduction in unpublished circular-arc learning literature remains a risk.

## value

PASS

PASS: Exact optimal online mistake bound for a natural one-parameter circular set family, with sharp growth despite static VC dimension ≤2, provides a quantitative example of how online rank diverges from VC. The ultraproduct bounded-minority-width criterion is an exact stability boundary and nontrivial natural complete classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
