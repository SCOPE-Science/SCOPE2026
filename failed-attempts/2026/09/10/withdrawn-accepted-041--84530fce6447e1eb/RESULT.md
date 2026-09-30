# Multiplicity-2 joint initial degeneration at a deformed tropical bitangent tangency: explicit non-faithful pair (preset-fallback certificate)

## Context
Smooth tropical plane quartics carry 7 tropical bitangent classes (Baker–Len–Morrison–Pflueger–Ren; Cueto–Markwig 41 shapes up to symmetry). Geiger–Panizzut showed bitangent shapes can deform within a fixed combinatorial type of quartic (deformation classes), with Cueto–Markwig real-lift conditions independent of the deformation. A separate question is simultaneous faithful tropicalization of a quartic together with a bitangent line: Baker–Payne–Rabinoff / Gubler–Rabinoff–Werner plus the Sturmfels–Tevelev formula reduce faithfulness at a cell to the joint initial degeneration having multiplicity one (transverse reduced point). Prior sources give shape taxonomies, generic 4-to-1 lifting counts, and general faithful criteria, but no pair-specific joint initial-degeneration multiplicity for a named deformed shape.

## Definitions
- `4Δ₂` lattice points `(i,j)`, `i+j ≤ 4`, ordered `(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3),(4,0),(3,1),(2,2),(1,3),(0,4)`.
- Height vector `λ₃ = [0,5,5,9,8,5,11/2,9,9,4,1,7,8,7,1]` (Geiger–Panizzut Example 2.1, post-deformation, shape F regime).
- Integer valuations `μ = −4λ₃ = [0,−20,−20,−36,−32,−20,−22,−36,−36,−16,−4,−28,−32,−28,−4]`.
- `Q₀(x,y) = Σ t^{μ(i,j)} x^i y^j` over `K = ℚ((t))`, all residue coefficients 1 (smooth valuated quartic).
- Type `T*`: regular subdivision of `λ₃` (upper hull, max-convention): 16 unimodular triangles, identical triangulation to the `λ₁`-regime; motif edge `p₂₀–p₃₁ = (2,0)–(3,1)` in triangles `{(2,0),(3,0),(3,1)}` and `{(2,0),(2,1),(3,1)}`.
- `B₀: t¹⁴·x + y + t⁷ = 0`, coefficient valuations `(14,0,7)` (deformed bitangent line, Cueto–Markwig shape `S* = (F)` regime).
- Tangency cell `W = (−11,3)` in `μ`-scale (`(−11/4,3/4)` in `λ`-scale), midpoint of the dual tropical edge `(−14,6)–(−8,0)` to the motif edge.

## Result
At `W`, with quartic weight `μ(p) + p·W` and line weight `val + p·W`:
- Quartic minimum `−58` attained exactly on `{(2,0),(3,1)}` (next weight `−55`, gap 3), so `in_W(Q₀) = x² + x³y = x²(1+xy)`.
- Line weights `(x: 3, y: 3, const: 7)`, tie `x∼y` at 3, gap 4, so `in_W(B₀) = x+y` (up to torus scaling).
- Joint initial ideal `J = (x²+x³y, x+y) ⊂ k[x,y]` has lex (`x>y`) reduced Gröbner basis `G = [x+y, y⁴−y²] = [x+y, y²(y²−1)]` (eliminate `x = −y`).
- Saturating the boundary component `y = 0` (point `x = y = 0`) by the torus monomial `xy` gives `(x+y, y²−1)`: two reduced torus points `(−1,1)`, `(1,−1)`. Torus length `dim_k k[y]/(y²−1) = 2`.
- Combinatorial check: Newton segment `(2,0)–(3,1)` direction `(1,1)` meets line direction `(−1,1)` with `|det| = 2`.
- Hence the joint initial degeneration at `W` has multiplicity exactly 2, not 1. By BPR/GRW + Sturmfels–Tevelev, `(Q₀,B₀)` is **not faithfully tropicalized in P²** at `W` and requires a tropical modification (binary test: mult 2 vs mult 1 for the faithful case).

## Proof / evidence
- `output/artifacts/subdivision.json`: 16 unimodular triangles, same triangulation for both regimes, motif edge present.
- `output/artifacts/verify_cert.py` (stdlib + sympy, exact `Fraction` arithmetic): asserts the min-weight ties, gaps 3 and 4, lex Gröbner basis, saturation `y²−1`, and determinant 2; prints `CERT_OK torus-length=2 det=2 GB=[x+y, y^4-y^2] W=(-11,3)`.
- `output/artifacts/singular_replay.sing`: identical computation archived for execution where Singular exists (expected `[x+y, y⁴−y²]`, saturation `[x+y, y²−1]`, vdim 2).
- `output/artifacts/certificate.json`: compact record of `Q₀/B₀/W`, initial forms, GB, gaps, determinant, verdict.
- Auditor independently re-ran the replay, recomputed all weights by hand-equivalent arithmetic, verified the Gröbner elimination, saturation count, determinant, and regularity/unimodularity of the subdivision for both height vectors.

## Limitations
- Singular/polymake absent in the computation environment; Gröbner basis via sympy with archived Singular replay (immaterial for this 2-generator ideal).
- The full-target one-ray tropical modification fan along `B*` (modified ideal, transverse modified initials, modified polyhedral complex) is NOT claimed.
- Algebraic smoothness of `Q₀` beyond tropical smoothness (unimodular subdivision, residue coefficients 1) is not separately certified; immaterial to the multiplicity/non-faithful inference.

## Reproducibility
Run `PYTHONPATH= python3 output/artifacts/verify_cert.py` (requires Python 3 + sympy). Expected output: `CERT_OK torus-length=2 det=2 GB=[x+y, y^4-y^2] W=(-11,3)`. Where Singular is available, run `output/artifacts/singular_replay.sing`.

## References
- M. A. Cueto, H. Markwig, Combinatorics and real lifts of bitangents to tropical quartic curves, arXiv:2004.10891.
- A. Geiger, M. Panizzut, A tropical count of real bitangents to plane quartic curves, arXiv:2112.04433.
- Y. Len, H. Markwig, Lifting tropical bitangents, arXiv:1708.04480.
- W. Gubler, J. Rabinoff, A. Werner, Skeletons and tropicalizations, arXiv:1404.7044 (Baker–Payne–Rabinoff program).
- H. Markwig, S. Payne, K. Shaw, Bitangents to plane quartics via tropical geometry, arXiv:2207.01305.
- polymake TropicalQuarticCurves extension + QuarticCurves database, https://polymake.org/doku.php/extensions/tropicalquarticcurves
