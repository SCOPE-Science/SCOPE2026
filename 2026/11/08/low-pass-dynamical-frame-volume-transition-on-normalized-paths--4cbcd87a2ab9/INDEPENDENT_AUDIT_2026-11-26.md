# Independent mathematical audit

## correctness

PASS

The corrected proof in repairs/4/RESULT.md uses n as the number of edges and k=r−1≥4. The cosine eigenvectors follow from the interior averaging recursion and the reflected boundary; after conjugation by the square root of the degree matrix, the Gramian determinant ratio is the squared product of the vertex-mode ratios, since the nonzero Vandermonde factor cancels. Write H_k(θ) for the product of cos²(ℓθ). It decreases strictly up to π/(2k). Beyond that and up to π/2 the geometric sum has magnitude at most 1/sin θ≤k/√2 by the sine chord bound, giving Σ sin²(ℓθ)≥(1−1/√2)k/2>7k/50 and H_k(θ)<e^(−7k/50). For n≥12k, (ℓπ/n)²≤1/2 and log(1−t²)≥−2t² give H_k(π/n)≥e^(−π²k/72)>e^(−7k/50). Thus the first interior grid angle strictly beats every farther nonreflected interior site. The interior factor 2^r then beats the endpoint ratio 1 (log 2≥1/2). Reflection establishes exactly two maximizers; the proof includes the bound at equality n=12k and requires no finite extrapolation. The frozen result's three-mode transition and cubic bound are mathematically correct: for three modes the secondary lobe has maximum 2/(3√6) and n=2,3,4,5 have interior product maxima 0,1/4,0,1/4; for the cubic bound the one-factor off-lobe estimate is sufficient. Those frozen claims are not being certified as original. The frozen CHECK.py was inspected, not run, and the repaired verification file separates it from the new analytic bound.

## originality

PASS

This PASS is for the repaired r≥5, n≥12(r−1) global one-vertex guarantee only. Originality of the frozen finding as submitted fails: the indexed 2026-11-02 phase diagram explicitly gives the same determinant ratio and the exact same three-mode transition, even with the same calculus proof. The repair credits those results, removes the duplicate claim, and keeps and strengthens the uniform large-bandwidth comparison to a linear sufficient length. The closest inspected prior results provide the factorization, low-mode phase diagrams, or endpoint-versus-inward comparisons, but do not give the uniform all-vertex conclusion at r≥5.

## value

PASS

The repaired bound gives a uniform global answer when the number of selected modes is allowed to grow linearly with path length, rather than classifications for two, three and four modes or a comparison of two nominated designs. The all-interior product control is essential to the optimization; beating endpoints alone does not settle it. The improvement from cubic to linear sufficient length changes the guaranteed bandwidth scale from order n^(1/3) to order n, without claiming an exact cutoff. The frozen three-mode result is useful but is not a new contribution of this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
