# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified integral-spectrum census of all connected cubic graphs with n <= 8,
# with exact characteristic polynomials, Hoffman-ratio residuals, Cauchy-interlacing
# replay, and integral benchmark rows (Petersen-10, Heawood-14)

## Abstract

We certify a complete exact integral-spectrum census of all connected cubic
graphs with even orders n = 4, 6, 8: 8 isomorphism classes in total
(1 + 2 + 5, reproducing OEIS A002851 in this range). For each class we commit an
explicit edge list and its exact adjacency characteristic polynomial computed in
integer arithmetic, derive the integral/non-integral verdict from factorisation
over Z, and replay three independent checks: (i) numeric eigenvalues are roots
of the committed polynomial, (ii) the Hoffman ratio bounds on the independence
number alpha and chromatic number chi hold against exactly computed alpha and
chi, with the residual table, and (iii) Cauchy interlacing holds on the
vertex-0-deleted card spectrum. Four of the eight classes are integral
(K4; the two 6-vertex cubics, i.e. K_{3,3} and the triangular prism; and the
3-cube Q3 at n = 8). All eight characteristic polynomials are pairwise
distinct, so there is no non-isomorphic cospectral pair at n <= 8. Two bonus
named-graph rows outside the census -- the Petersen graph (n = 10, integral,
spectrum {3, 1^5, (-2)^4}) and the Heawood graph (n = 14, non-integral,
Hoffman-tight with alpha = 7, chi = 2) -- are certified by the same pipeline.
The full n <= 14 target (621 classes) is NOT claimed: a direct n = 10 run timed
out in this environment, so scope is honestly restricted to n <= 8 + benchmarks.

## 1. Census generation and completeness

Fix n in {4, 6, 8}. Pin N(0) = {1, 2, 3} without loss of generality (any cubic
graph relabels so). Complete the lowest-index deficit vertex against every
eligible partner recursively; every labelled simple 3-regular completion with
this pinning is visited exactly once (unique construction path). Connected
completions (BFS) are deduplicated by exact backtracking isomorphism search
after cheap invariant bucketing. The run yields class counts 1, 2, 5 with leaf
counts 2, 32, 7416 and connected completions 2, 32, 7392, matching OEIS A002851
(1, 2, 5, 19, 85, 509, ...) in this range. Pairwise non-isomorphism of the
committed representatives is re-verified independently in `verify.py`.

## 2. Exact spectra and integral verdicts

For each representative, det(xI - A) is computed exactly (sympy integer
determinant) and factored over Z. The integral verdict is "all factors linear".
Numeric spectra (numpy eigvalsh) are checked to satisfy the committed
polynomial with residual < 1e-4 and lambda_max = 3.

| class | charpoly (leading..constant) | factors over Z | integral | spectrum |
|---|---|---|---|---|
| n4-c0 (K4) | 1,0,-6,-8,-3 | (x-3)(x+1)^3 | yes | 3,(-1)^3 |
| n6-c0 (prism) | 1,0,-9,-4,12,0,0 | (x-3)(x-1)x^2(x+2)^2 | yes | 3,1,0^2,(-2)^2 |
| n6-c1 (K3,3) | 1,0,-9,0,0,0,0 | (x-3)(x+3)x^4 | yes | 3,-3,0^4 |
| n8-c0 | 1,0,-12,-8,38,48,-12,-40,-15 | (x-3)(x-1)(x+1)^4(x^2-5) | no | 3,sqrt5,-sqrt5,1,(-1)^4 |
| n8-c1 | 1,0,-12,-4,38,16,-36,-12,9 | (x-3)(x-1)(x+1)^2(x^2-3)(x^2+2x-1) | no | 3,sqrt3,-sqrt3,... |
| n8-c2 | 1,0,-12,-2,36,0,-31,12,0 | (x-3)x(x^2+x-4)(x^2+x-1)^2 | no | 3,... |
| n8-c3 (Q3 cube) | 1,0,-12,0,30,0,-28,0,9 | (x-3)(x+3)(x-1)^3(x+1)^3 | yes | 3,-3,1^3,(-1)^3 |
| n8-c4 | 1,0,-12,0,34,-16,-20,16,-3 | (x-3)(x+1)(x-1)^2(x^2+2x-1)^2 | no | 3,... |

In particular the integral members at n <= 8 are exactly K4, the two n = 6
cubics, and the cube Q3 -- consistent with the Bussemaker-Cvetkovic
13-graph classification restricted to this range (no new integral cubic
appears here beyond the known small members).

## 3. Cospectral finding at n <= 8

The eight coefficient tuples above are pairwise distinct (byte comparison in
`verify.py`), hence all cospectral classes are singletons: there is NO
non-isomorphic cospectral pair among connected cubic graphs with n <= 8. This
is a proved finite negative result inside the slice (not a failure to search).
The fallback's "smallest pair in n <= 14" is therefore not delivered; the
target slice minimum, if it exists, lies at n >= 10.

## 4. Hoffman ratio bounds with exact alpha/chi

For cubic G with eigenvalues lmin <= ... <= lmax = 3:
alpha(G) <= -n*lmin/(3-lmin), chi(G) >= 1 - 3/lmin.
Exact alpha by subset search, exact chi by k-colouring backtracking:

| class | alpha vs bound | chi vs bound |
|---|---|---|
| n4-c0 | 1 <= 1.0000 (tight) | 4 >= 4.0000 (tight) |
| n6-c0 | 2 <= 2.4000 | 3 >= 2.5000 |
| n6-c1 | 3 <= 3.0000 (tight) | 2 >= 2.0000 (tight) |
| n8-c0 | 3 <= 3.4164 | 3 >= 2.3416 |
| n8-c1 | 3 <= 3.5672 | 3 >= 2.2426 |
| n8-c2 | 3 <= 3.6847 | 3 >= 2.1712 |
| n8-c3 | 4 <= 4.0000 (tight) | 2 >= 2.0000 (tight) |
| n8-c4 | 3 <= 3.5672 | 3 >= 2.2426 |

No violation occurs; tight cases are K4, K3,3, Q3 (all bipartite-or-complete
extremals). The vertex-0-deleted card spectrum satisfies Cauchy interlacing
l_i <= c_i <= l_{i+1} for every row (replayed in `verify.py`).

## 5. Benchmark rows (outside census scope)

* Petersen-10: edges {outer C5, 5 spokes, inner {i,i+2} star}; charpoly
  1,0,-15,0,75,-24,-165,120,120,-160,48 = (x-3)(x+2)^4(x-1)^5; integral;
  spectrum {3,1^5,(-2)^4}; alpha = 4 <= 4.0 (tight), chi = 3 >= 2.5.
* Heawood-14: Fano-plane point-line incidence (bipartite, girth 6); charpoly
  1,0,-21,0,168,0,-700,0,1680,0,-2352,0,1792,0,-576 = (x-3)(x+3)(x^2-2)^6;
  non-integral; alpha = 7 <= 7.0 (tight), chi = 2 >= 2.0 (tight).

## 6. Reproduction

```
python3 census.py 4 6 8        # regenerates graphs_n8.json; asserts 1,2,5
python3 analyze.py graphs_n8.json  # exact charpolys + bounds -> analysis.json
python3 verify.py              # independent replay -> VERIFY_OK
```

Needs only stdlib + numpy + sympy. `census.py` n = 8 takes ~0.5 s; n = 10 did
not finish within ~9 min in this lane (labeled search without nauty/geng), so
n >= 10 census rows are explicitly excluded from the claim.

## 7. Limitations and uncertainty

* Scope is n <= 8 (8 classes), NOT the full n <= 14 (621 classes) target.
* No smallest cospectral pair is exhibited (proved absent at n <= 8).
* Isomorphism testing is exact backtracking (fine at n <= 8) but does not scale;
  counts rely on the unique-construction-path argument plus A002851 agreement.
* Numeric eigenvalues used only for bounds/interlacing display; integrality
  verdicts rest on exact factorisation.

## References

* Harary-Schwenk, Which graphs have integral spectra? (1974).
* Bussemaker-Cvetkovic, There are exactly 13 connected cubic integral graphs (1976).
* Bussemaker et al., Cubic graphs on <= 14 vertices, JCT-B (1977); OEIS A002851.
* Godsil-McKay, Constructing cospectral graphs (1982).
* Brouwer-Spence, Cospectral graphs on 12 vertices (2009); OEIS A006608.
* Hoffman, On eigenvalues and colorings of graphs (1970).
* MathWorld: Cubic Graph; Integral Graph; Cospectral Graphs (counts cited live).
