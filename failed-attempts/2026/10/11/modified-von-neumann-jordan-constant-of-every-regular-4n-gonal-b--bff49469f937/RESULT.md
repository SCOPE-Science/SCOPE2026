# Modified von Neumann–Jordan constant of every regular \((4n)\)-gonal Banach plane
## Finding
For every integer \(n\ge1\), let \(X_{4n}\) be the real two-dimensional Banach space whose unit ball is a Euclidean regular \(4n\)-gon, up to linear isometry. Then
\[
C'_{\mathrm{NJ}}(X_{4n})
=
\sec^2\!\left(\frac{\pi}{4n}\right).
\]

Thus the whole fourfold regular-polygon family has an exact modified von Neumann--Jordan profile. In particular,
\[
C'_{\mathrm{NJ}}(X_4)=2,
\qquad
C'_{\mathrm{NJ}}(X_8)=4-2\sqrt2,
\qquad
C'_{\mathrm{NJ}}(X_{12})=8-4\sqrt3.
\]
Moreover,
\[
C'_{\mathrm{NJ}}(X_{4n})
=
1+\frac{\pi^2}{16n^2}+O(n^{-4}),
\]
so these polyhedral planes approach the Hilbert value \(1\) quadratically in the number of fourfold sectors.

## Assumptions and scope
All spaces are real and two-dimensional. The modified von Neumann--Jordan constant is
\[
C'_{\mathrm{NJ}}(X)
=
\sup_{x,y\in S_X}
\frac{\|x+y\|^2+\|x-y\|^2}{4}.
\]

Fix
\[
N=4n,
\qquad
\alpha=\frac{\pi}{N}.
\]
Normalize the regular \(N\)-gon so that its Euclidean inradius is \(1\). Its unit ball is
\[
B_N
=
\bigcap_{j=0}^{N-1}
\left\{
z\in\mathbb R^2:
\langle u_j,z\rangle\le1
\right\},
\]
where
\[
u_j
=
\left(
\cos\frac{2\pi j}{N},
\sin\frac{2\pi j}{N}
\right).
\]
The Euclidean circumradius is
\[
R_N=\sec\alpha.
\]

## Proof
For every \(z\in\mathbb R^2\),
\[
\|z\|_N
=
\max_{0\le j<N}\langle u_j,z\rangle
\le
\|z\|_2,
\]
because each \(u_j\) is a Euclidean unit vector.

If \(x\in S_{X_N}\), then \(x\in B_N\), so its Euclidean norm is at most the circumradius:
\[
\|x\|_2\le R_N=\sec\alpha.
\]
Therefore, for arbitrary \(x,y\in S_{X_N}\),
\[
\begin{aligned}
\|x+y\|_N^2+\|x-y\|_N^2
&\le
\|x+y\|_2^2+\|x-y\|_2^2
\\
&=
2\|x\|_2^2+2\|y\|_2^2
\\
&\le
4R_N^2.
\end{aligned}
\]
The middle equality is the Euclidean parallelogram identity. Hence
\[
C'_{\mathrm{NJ}}(X_N)\le R_N^2=\sec^2\alpha.
\tag{1}
\]

To attain (1), take the two adjacent vertices symmetric about the facet normal at angle \(0\):
\[
x
=
R_N(\cos\alpha,\sin\alpha),
\qquad
y
=
R_N(\cos\alpha,-\sin\alpha).
\]
Both are unit vectors for the polygonal norm. Since
\[
R_N\cos\alpha=1,
\]
their sum is
\[
x+y=(2,0).
\]
The positive horizontal axis is a facet-normal ray, so
\[
\|x+y\|_N=2.
\]

Their difference is
\[
x-y=(0,2R_N\sin\alpha)=(0,2\tan\alpha).
\]
Because \(N=4n\), the direction \(\pi/2\) is also a facet-normal direction:
\[
\frac{\pi}{2}
=
2n\alpha.
\]
Therefore the polygonal norm agrees with the Euclidean norm on the vertical axis, and
\[
\|x-y\|_N=2\tan\alpha.
\]
Consequently
\[
\frac{\|x+y\|_N^2+\|x-y\|_N^2}{4}
=
1+\tan^2\alpha
=
\sec^2\alpha.
\]
Together with (1), this proves
\[
C'_{\mathrm{NJ}}(X_{4n})
=
\sec^2\!\left(\frac{\pi}{4n}\right).
\]

Finally,
\[
\sec^2 t=1+t^2+O(t^4)
\]
as \(t\to0\). Substituting
\[
t=\frac{\pi}{4n}
\]
gives
\[
C'_{\mathrm{NJ}}(X_{4n})
=
1+\frac{\pi^2}{16n^2}+O(n^{-4}).
\]

## Verification
The proof is analytic and covers every integer \(n\ge1\). Its critical inputs are the exact inradius/circumradius relation for a regular polygon, the Euclidean parallelogram identity, and the arithmetic fact that \(4\mid N\) makes both coordinate axes facet-normal directions.

The bundled `verify.py` independently reconstructs the inradius-one polygonal norm for
\[
N=4,8,12,16,20,24,32,40.
\]
For each value it checks that the two stated adjacent vertices are unit vectors and that their modified von Neumann--Jordan quotient equals
\[
\sec^2\!\left(\frac{\pi}{N}\right)
\]
to high precision. It also performs deterministic boundary sampling as a non-proof stress test of the upper bound.

Finite sampling is not used to justify the universal quantifier; the infinite-family upper bound and equality construction are the symbolic argument above.

## Relationship to prior work
Zuo, Huang, Huang and Wang study Gao-type constants for absolute normalized norms on \(\mathbb R^2\), explicitly recall \(C'_{\mathrm{NJ}}\), and develop exact methods for concrete two-dimensional norms. Their paper is classified under MSC \(46B20\) and \(46B25\). The inspected full publisher text does not contain “regular” or “octagon” and does not state a regular-polygon family formula.

Ciesielski and Płuciennik develop upper and modified upper \(n\)-th von Neumann--Jordan constants. Their full publisher text identifies
\[
\overline C^{(2)}_{m\mathrm{NJ}}(X)=C'_{\mathrm{NJ}}(X)
\]
and gives exact formulas for classical \(L^p\) and \(\ell^p\) spaces, but no regular-polygon theorem was located in the inspected statements.

A 2023 paper by Komuro, Mitani and Okazaki is particularly relevant because its abstract reports calculations of modified von Neumann--Jordan constants for extreme absolute normalized norms on \(\mathbb R^2\). Its repository metadata and abstract were inspected, but the available PDF download could not be text-inspected in the present environment. No indexed abstract or search result states the formula above or an all-regular-\(4n\) theorem, so this source remains an explicit residual literature risk rather than being treated as non-covering full text.

Public research-index searches under the exact invariant, regular-polygon aliases, the dodecagonal specialization, and the secant-square formula returned an exact regular-octagon parameterized von Neumann--Jordan result and general results for other spaces, but no theorem covering all regular \(4n\)-gons. The octagonal result is one member of the present infinite family and therefore is treated as prior coverage of that special case, not as evidence of family-level novelty by itself.

## Limitations
The theorem treats regular polygons with side count divisible by \(4\). The equality construction uses the perpendicular facet-normal direction and does not claim the same formula for regular polygons with
\[
N\equiv2\pmod4.
\]

The result determines the modified two-variable von Neumann--Jordan constant, not the unrestricted von Neumann--Jordan constant nor higher modified \(n\)-th constants.

Bibliographic and semantic searches cannot prove absolute novelty. The 2023 extreme-norm paper is a concrete access residual risk because only its metadata and abstract, not its full PDF text, were inspected.

## References
1. Z. Zuo, Y. Huang, H. Huang and J. Wang, “The Gao-Type Constant of Absolute Normalized Norms on \(\mathbb R^2\),” Mathematics 10 (2022), 4591, doi:10.3390/math10234591. Published 4 December 2022. MSC: 46B20, 46B25.
2. M. Ciesielski and R. Płuciennik, “On some modifications of n-th von Neumann--Jordan constant for Banach spaces,” Banach Journal of Mathematical Analysis 14 (2020), 650–673, doi:10.1007/s43037-019-00033-1.
3. N. Komuro, K.-I. Mitani and T. Okazaki, “Geometrical constants of 2-dimensional spaces with extreme norms in \(AN_2\),” RIMS Kôkyûroku 2260 (2023), 129–136.
