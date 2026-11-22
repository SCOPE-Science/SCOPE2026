# Reentrant antipodal and tetrahedral worst tours in a rectangular prism

## Finding
For each real \(t>0\), let \(Q_t=\{(i,j,tk):i,j,k\in\{0,1\}\}\) be the eight corners of a right rectangular prism. For any subset \(S\subseteq Q_t\) with at least two members, let \(T(S)\) be the minimum over cyclic tours through all members of the sum of the cubes of their Euclidean edge lengths; a two-point tour traverses the pair twice. Then
\[
\max_{S\subseteq Q_t,\ |S|\ge2}T(S)
=\max\left\{2(2+t^2)^{3/2},\quad
\begin{cases}
4(1+t^2)^{3/2},&0<t\le1,\\
4\sqrt2+2(1+t^2)^{3/2},&t\ge1.
\end{cases}\right\}.
\]
Set \(t_-=\sqrt{(2-2^{2/3})/(2^{2/3}-1)}\approx0.838101654884\) and let \(t_+\approx1.435766218641\) be the unique solution \(t>1\) of \((2+t^2)^{3/2}-(1+t^2)^{3/2}=2\sqrt2\). For \(0<t<t_-\) and \(t>t_+\), exactly four subsets attain the maximum: the four antipodal pairs. For \(t_-<t<t_+\), exactly two subsets attain it: the four-corner parity tetrahedra. At either threshold all six subsets attain it, and no others do. This is a genuine reentrant change of the maximizer as the prism elongates.

## Assumptions and scope
Only corner subsets are considered; vertices may not be replaced by arbitrary interior or boundary points. The two horizontal edge lengths are one, the vertical length is \(t>0\), the ambient distance is Euclidean, and the tour cost is the *sum* of the cubes of edge lengths, not its cube root. The result makes no assertion for non-corner point configurations or other powers.

## Proof
Label corners by their bits \(0,\ldots,7\), taking bit 2 as the vertical coordinate. Put
\[A=1,\quad B=t^3,\quad C=2\sqrt2,\quad D=(1+t^2)^{3/2},\quad E=(2+t^2)^{3/2}.\]
Every possible tour edge has exactly one of these five costs: respectively a horizontal unit edge, a vertical edge, a horizontal face diagonal, a vertical face diagonal, or a body diagonal.

The antipodal pairs have tour cost \(2E\). Each parity tetrahedron has six edges, split into a pair of horizontal diagonals of cost \(C\) and four vertical diagonals of cost \(D\). Any Hamiltonian four-cycle omits a perfect matching, hence its optimum is \(P(t)=\min(4D,2C+2D)\). As \(D\le C\) exactly when \(t\le1\), this gives the displayed expression for the parity candidate.

We prove that every other subset has strictly lower cost than \(\max(2E,P(t))\) using an exact finite certificate, `certificate.json`, checked by `verify_cube_prism.py`. Here are the inequalities underlying the certificate, so its validity is not a numerical sampling assumption. In both parameter regimes, \(D\ge A+B\), \(E\ge B+C\), \(E\ge D+A\), \(C\ge2A\), and all five costs are nonnegative. The first three follow from \((u+v)^{3/2}\ge u^{3/2}+v^{3/2}\) for nonnegative \(u,v\). For \(0<t\le1\), also \(A\ge B\), \(C\ge D\), and \(2E\ge2D+C\): indeed \(E-D\) increases with \(t\) and starts at \(2\sqrt2-1>\sqrt2=C/2\). For \(t\ge1\), also \(B\ge A\), \(D\ge C\), and \(E\ge B+A+C\): \(E-B\) is increasing and at \(t=1\) equals \(3\sqrt3-1>1+2\sqrt2\).

Translations by bitwise XOR and interchange of the two horizontal coordinates preserve all five edge-cost classes. They partition the 247 corner subsets of cardinality at least two into precisely 32 orbits. For each orbit and each of the two regimes, `certificate.json` lists (i) a genuine cyclic order of its representative vertices, (ii) a target equal to either \(2E\) or the corresponding \(P(t)\), and (iii) nonnegative rational coefficients expressing the *target minus the proposed tour cost* as a sum of the twelve nonnegative inequalities just established (including the five elementary nonnegative-cost inequalities). Thus a valid tour of cost at most the displayed maximum exists in every orbit for every real \(t>0\). The checker proves these 64 vector identities exactly with rational arithmetic and independently checks the tours and orbit coverage. Except in the antipodal-pair and parity-tetrahedron orbits, each certificate includes an inequality that is strictly positive for \(t>0\); consequently there are no other maximizers. This finite proof checks every possible subset, but only constructs one upper-bounding tour per orbit, which is all that is required for a sharp maximum.

Finally, in \(0<t\le1\), the ratio \(E/D=((2+t^2)/(1+t^2))^{3/2}\) decreases strictly; \(2E=4D\) occurs uniquely at \(t_-\). In \(t\ge1\), \(E-D\) grows strictly from \(3\sqrt3-2\sqrt2<2\sqrt2\) to infinity; \(2E=2C+2D\) occurs uniquely at \(t_+\). These crossings give the stated equality classification.

## Verification
Run `python3 verify_cube_prism.py` alongside `certificate.json` with Python 3 standard library. The certificate has 32 orbit representatives, two witnesses per representative, and 64 exact rational nonnegative-cone identities. Direct floating-point Held–Karp checks on numerous sample aspect ratios gave the same maximizers, but these are corroboration only; the all-parameter proof is the exact certificate and the analytic inequalities above. The certificate is complete only for the eight corners of \(Q_t\).

## Relationship to prior work
The collection *Open problems from the Length Optimization event at MDS 2026* poses the unrestricted three-dimensional cubic-power tour bound. Balogh, Clemen and Dumitrescu's 2024 paper supplies the four-corner parity-tetrahedron lower construction and considers cube-vertex restrictions in sufficiently high dimension; it does not assert this anisotropic rectangular-prism profile. The symmetric case \(t=1\), including a power-exponent cube-corner classification, is already known; the new assertion is the entire non-isotropic aspect-ratio phase profile, its two sharp thresholds, and reentrant equality classification. The result does not answer the unrestricted continuous-point open problem.

## Limitations
This is an exact theorem for finite vertex subsets of a two-equal-side rectangular prism, not for all subsets of a continuous prism and not for unequal horizontal lengths or alternative powers. An exhaustive verification is not automatically a proof of external mathematical priority. Historical records containing a stronger unindexed prism theorem could subsume this claim. The scientific review is not an independent mathematical audit.

## References
- Y. Teplitskaya (editor), *Open problems from the Length Optimization event at MDS 2026*, arXiv:2611.03403v1 (first public 2026-11-02), https://arxiv.org/html/2611.03403v1, Section 4.
- J. Balogh, F. C. Clemen, A. Dumitrescu, *On a Traveling Salesman Problem for Points in the Unit Cube*, Algorithmica 86 (2024), 3054–3078, https://doi.org/10.1007/s00453-024-01257-w, Sections 2, 3, 5.
