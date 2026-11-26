# Independent mathematical audit

## correctness

PASS

Fix the 0/1 coordinates of a relative interior. With the cap slack, the dimension is the number of free coordinates minus one, so a two-face has three free coordinates of residual rank one, or rank two with at most one tail among them. In rank one choose the r−1 fixed head ones first and then choose any triple from the remaining p+t−r+1 positions. In rank two the counts are C(p,3)C(p−3,r−2) and t C(p,2)C(p−2,r−2). With a fixed tail one, the residual three free head coordinates have rank one or two; Pascal gives t C(p,3)C(p−2,r−2). On the tight cap the face lattice is that of the direct product of the head hypersimplex of rank r−1 and the tail rank-one simplex. Its squares are exactly edge × edge, giving C(p,2)C(p−2,r−2)C(t,2); its triangles have the other factor fixed. Those with tail factor fixed are in the fixed-tail-one count, and those with head factor fixed in the first count with three free tails. This accounts for all cap-active triangles exactly once. Free coordinates and fixed ones distinguish the faces; the reasoning includes r=p and zero binomial terms. The triangles have sides √2 and square factors are orthogonal of length √2. For fixed r, the first and last triangle terms have degree r+2 and the middle terms are lower degree, giving the stated Φ with k=r−1. The odds Φ/(1−Φ) are (3/2)kα(1−α)²/[1+kα²(1−α)]. Their derivative has sign 1−3α−kα²(1−α), strictly decreasing from positive to negative on (0,1/3) and negative beyond it. The root satisfies kα²=(1−3α)/(1−α), giving α=k^(−1/2)+O(k^(−1)). At the root inverse odds are 2(2−3α)/[3kα(1−α)²]=4/(3√k)+O(k^(−1)), giving the same leading frequency deficit. No simultaneous N-and-r asymptotic or reliance on the supplied finite checker is needed.

## originality

PASS

The supported distinct result is the evaluated, type-refined panhandle law with its ordered-limit optimizer and sharp high-rank deficit. The two face shapes and their areas, the defining inequalities, and general methods that already compute the unrefined f-vector are prior—not independent novelty claims. The finite counts are an explicit specialization, not a new general counting method.

## value

PASS

The distribution of the two polygon areas is a concrete metric refinement of the f-vector in a standard matroid family. It reveals a unique proportional choice favoring squares and a sharp rank-dependent approach to square dominance. This is more than recomputing generic shape possibilities or tabulating small cases, and it makes no claim for simultaneous size-and-rank growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
