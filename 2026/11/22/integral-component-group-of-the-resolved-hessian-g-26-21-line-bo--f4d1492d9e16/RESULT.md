# Integral component group of the resolved Hessian \(G_{26}\) 21-line boundary

## Finding

Write \(C_m=\mathbb Z/m\mathbb Z\). For the geometrically natural nodal boundary \(D\) of the \(21\)-mirror Hessian reflection arrangement of \(G_{26}\), the complete critical group of its dual graph is

\[
K(\Gamma)\cong C_{335}\oplus C_{1005}^{4}\oplus C_{36180}^{2}\oplus C_{1013040}.
\]

This is an *integral* isomorphism, not merely an equality of orders, rational spectra, or isogeny classes. The group contains exactly eight independent \(67\)-torsion elementary factors, a nonobvious feature of the full arrangement. Its order is

\[
\left|K(\Gamma)\right|=2^8\,3^{13}\,5^8\,7\,67^8.
\]

The dual graph has \(42\) vertices, \(132\) edges, and first Betti number \(91\). The graph Laplacian has characteristic polynomial

\[
\det(tI-L)=t(t-9)^3(t-4)^3(t^3-25t^2+188t-392)(t^4-25t^3+218t^2-788t+1005)^8.
\]

For any proper regular split semistable one-parameter smoothing of \(D\) with unit node thicknesses, \(K(\Gamma)\) is also the geometric component group of the Néron model of the generic Jacobian.

## Assumptions and scope

Work over \(\mathbb C\). Fix a primitive cube root \(\omega\) with \(\omega^2+\omega+1=0\). Let the 21 projective lines be given by the three coordinate equations, the nine equations

\[
x+\omega^i y+\omega^j z=0\qquad(0\le i,j\le 2),
\]

and the nine equations

\[
x-\omega^k y=0,\quad x-\omega^k z=0,\quad y-\omega^k z=0\qquad(0\le k\le2).
\]

This is the \(G_{26}\) arrangement written explicitly in Hoge–Röhrle. Blow up precisely its points of multiplicity at least four, which comprise nine fourfold points and twelve fivefold points. Let \(D\) be the reduced union of all 21 strict line transforms and all 21 exceptional curves. **Do not** blow up the 36 ordinary nodes: their edges belong to the dual graph of the *stable* boundary under study.

Every component is isomorphic to \(\mathbb P^1\). The strict-line components have eight incident nodes each, nine exceptional curves have valency four, and twelve have valency five. In particular, every rational component meets the rest in at least three distinct points, so \(D\) is stable. The original 36 double points supply 36 direct line-to-line edges, and the 9 quadruple and 12 quintuple points supply \(9\cdot4+12\cdot5=96\) line-to-exception edges. Thus there are \(21+21=42\) vertices, \(36+96=132\) edges, and arithmetic genus \(132-42+1=91\).

## Proof

**Exact configuration reconstruction.** Represent each coefficient in \(\mathbb Q(\omega)\) as a pair of rational numbers, with product computed using \(\omega^2=-1-\omega\). For each of the \(\binom{21}{2}=210\) line pairs, take the cross product of their coefficient vectors and normalize by the first nonzero homogeneous coordinate. Equality of these normalized projective points is exact. Grouping line pairs gives precisely 36 points of multiplicity two, nine of multiplicity four, and twelve of multiplicity five. The pair count is independently checked:

\[
36\binom22+9\binom42+12\binom52=36+54+120=210.
\]

**Dual graph construction.** Index the lines by \(0,\dots,20\) and the higher-multiplicity points by \(21,\dots,41\). Place an edge between each ordinary double-point line pair, and join each line through a higher-multiplicity point to that point's exceptional vertex. This produces a connected, unweighted 42-vertex graph with the degrees stated above. Its integer Laplacian \(L\) has diagonal entries equal to the valencies and off-diagonal entry minus the edge multiplicity.

**Spanning-tree determinant.** Delete vertex 20 to form the \(41\times41\) reduced Laplacian \(R\). List the 20 remaining line vertices before the 21 exceptional vertices, so that

\[
R=\begin{pmatrix}A&B\\B^{\mathsf T}&E\end{pmatrix},\qquad E=\operatorname{diag}(e_1,\dots,e_{21}),\quad e_i\in\{4,5\}.
\]

Since \(E\) is invertible over \(\mathbb Q\), the matrix-tree theorem and exact Schur-complement identity give

\[
|K(\Gamma)|=\det R=\left(\prod_{i=1}^{21}e_i\right)\det(A-BE^{-1}B^{\mathsf T})
=2^8\,3^{13}\,5^8\,7\,67^8.
\]

A separate exact characteristic-polynomial calculation for \(L\) yields the displayed degree-42 factorization. Differentiation at \(t=0\) and division by 42 reproduces the same tree count, providing an independent check on the determinant.

**Integral invariant factors.** For each of the five primes dividing \(\det R\), perform elementary row and column operations over the \(p\)-adic integers, represented exactly modulo \(p^N\) with \(N\) larger than the total valuation of the determinant. At each stage choose a pivot of least \(p\)-valuation in the trailing block. Such a pivot divides the remaining entries \(p\)-adically; after inversion of its unit part, clear its column and, implicitly, its row. The trailing matrix then presents the remaining elementary divisors. This is exact Smith reduction over a discrete valuation ring; its precision exceeds the determinant valuation, so no nonzero invariant factor can be confused with zero.

The resulting lists of *positive* elementary-divisor exponents are:

| Prime | Positive valuations of the 41 reduced Smith factors |
|---|---|
| \(2\) | \(2,2,4\) |
| \(3\) | \(1,1,1,1,3,3,3\) |
| \(5\) | eight copies of \(1\) |
| \(7\) | one copy of \(1\) |
| \(67\) | eight copies of \(1\) |

All omitted valuations are zero. Multiplying the five sorted elementary-divisor lists componentwise gives 33 unit factors followed by

\[
335,\quad 1005,1005,1005,1005,\quad 36180,36180,\quad 1013040.
\]

These form a divisibility chain and their product equals the spanning-tree determinant. Repeating all prime-local computations after deleting vertex 41, rather than vertex 20, gives exactly the same exponents. This proves the complete integral group claim. For the final Néron interpretation, apply the standard identification of the component group of a proper regular split semistable curve with the Jacobian of its unit-length dual graph.

## Verification

The standalone `verify.py` rebuilds the line equations in \(\mathbb Q(\omega)\), performs all \(210\) exact intersections, reconstructs every graph edge, checks the genus, factors the degree-42 Laplacian polynomial, evaluates the exact 20-dimensional rational Schur determinant, and computes prime-local Smith exponents from two differently rooted \(41\)-square Laplacians. Run it in a Python environment with SymPy:

```sh
python -m pip install -r requirements.txt
python verify.py
```

Successful execution prints `G26_HESSIAN_STABLE_BOUNDARY_INTEGRAL_CRITICAL_GROUP_OK`. None of these checks use approximate complex coordinates or probabilistic modular rank heuristics.

## Relationship to prior work

The defining \(G_{26}\) reflection polynomial and the arrangement's non-supersolvability are established by Hoge–Röhrle. The original arrangement and its geometric uses go back to Hirzebruch. Roulleau explicitly records the line-intersection multiplicities \((t_2,t_4,t_5)=(36,9,12)\). Busonero–Melo–Stoppino explain the general stable-curve critical-group and component-group correspondence. These are important inputs, but neither the explicit invariant-factor list above nor its \(67\)-primary part follows from the cited geometric incidence counts alone; the integral reduction is supplied here. An older unindexed integral sandpile computation is a residual historical-priority risk.

## Limitations

The statement concerns exactly the defined reduced stable boundary, **not** the graph obtained by also blowing up ordinary double points. Its unconditional assertion is the graph-group computation. The Néron interpretation assumes a proper regular split semistable smoothing and unit node thicknesses; the result does not cover arbitrary thickness vectors, arithmetic twists, or other resolution choices. The computation is mathematically checked here but has not received independent mathematical validation, and originality cannot be certified against all unindexed prior literature.

## References

- T. Hoge and G. Röhrle, *On supersolvable reflection arrangements*, arXiv:1209.1919 (first public submission 10 September 2012), especially the defining \(G_{26}\) polynomial in Lemma 3.2(v): https://arxiv.org/abs/1209.1919
- F. Hirzebruch, *Arrangements of Lines and Algebraic Surfaces*, 1983, https://hirzebruch.mpim-bonn.mpg.de/id/eprint/244/1/hirzebrucharr.pdf
- X. Roulleau, *Conic Configurations via Dual of Quartic Curves*, *Rocky Mountain J. Math.* 51 (2021), §3.3, DOI:10.1216/rmj.2021.51.721; https://www.i2m.univ-amu.fr/perso/xavier.roulleau/Site_Pro_English/Publications_files/Conic%20configurations%20via%20dual%20of%20quartic%20curves.pdf
- S. Busonero, M. Melo and L. Stoppino, *On the complexity group of stable curves*, arXiv:0808.1529, https://arxiv.org/abs/0808.1529
