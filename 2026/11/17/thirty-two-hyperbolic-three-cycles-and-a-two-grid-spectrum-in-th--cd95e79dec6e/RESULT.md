# Thirty-two hyperbolic three-cycles and a two-grid spectrum in the orthogonal tents map

## Finding
On the flat torus \(\mathbb T^2=(\mathbb R/\mathbb Z)^2\), let \(f(t)=2\min\{t,1-t\}\) for canonical \(0\le t<1\), and define the symmetric orthogonal tents map
\[
H(x,y)=\left(u,\{y+f(u)\}\right),\qquad u=\{x+f(y)\},
\]
where braces denote fractional part. Its third iterate has **exactly 100 distinct fixed points**. Precisely four are fixed by \(H\), at \(\{0,1/2\}^2\), and the remaining 96 have least period three, yielding **exactly 32 distinct primitive three-cycles**. No third-iterate fixed locus has positive dimension.

Every one of these 32 cycles avoids all switching lines and is a hyperbolic saddle. The exact distribution of the trace of its three-step derivative is
\[
\begin{array}{c|ccc}
\operatorname{tr}(DH^3)&102&-34&-98\\\hline
\text{number of primitive cycles}&16&8&8.
\end{array}
\]
There are no elliptic or parabolic primitive three-cycles. All 100 third-iterate fixed points belong to the union of the two rational torus grids of mesh \(1/18\) and \(1/50\). Exactly 28 are in the first grid and 76 in the second; their intersection consists of the four fixed points, so 24 primitive three-periodic points are exclusive to the first grid and 72 to the second. In fact, the trace \(-34\) class is precisely the mesh-\(1/18\) class, whereas the trace \(102\) and \(-98\) classes are precisely the mesh-\(1/50\) class.

## Assumptions and scope
The map is the composition of a horizontal slope-two tent shear with an orthogonal vertical slope-two tent shear. Coordinates are canonical representatives in the half-open square \([0,1)^2\); values at zero, one-half, and identified torus edges are included. A primitive three-cycle consists of three distinct points satisfying \(H^3(p)=p\), and regularity means avoiding all shear folding lines at each of the three iterates. The derivative exists on each such orbit, and its third-return matrix has determinant one. No perturbation of the tent slopes is considered.

## Proof
**1. Complete affine branch covering.** For each step choose four binary labels \((j,m,l,k)\in\{0,1\}^4\). Here \(j\) chooses the lower or upper horizontal tent branch, \(m\) is the horizontal integer reduction, \(l\) chooses the lower or upper vertical tent branch, and \(k\) is the vertical integer reduction. Set
\[
(a,d)=\begin{cases}(2,0),&j=0,\\(-2,2),&j=1,\end{cases}
\qquad
(b,e)=\begin{cases}(2,0),&l=0,\\(-2,2),&l=1.\end{cases}
\]
On the corresponding cell, the torus map has the integer-affine expression
\[
H(z)=M_{a,b}z+c_{j,m,l,k},\qquad
M_{a,b}=\begin{pmatrix}1&a\\b&1+ab\end{pmatrix},
\qquad
c_{j,m,l,k}=\binom{d-m}{b(d-m)+e-k}.
\]
The branch is valid exactly when the canonical input lies in the designated half of the horizontal fold, its unreduced horizontal shear lies in \([m,m+1)\), the resulting horizontal coordinate lies in the designated half of the vertical fold, and its unreduced vertical shear lies in \([k,k+1)\). At fold equalities either adjacent affine formula is allowed; their values agree. Since both unreduced shear coordinates lie in \([0,2)\), the wrap bits zero and one exhaust all possibilities. Thus all 16 affine branches, including their boundary incidences, cover the torus exactly.

**2. No infinite families.** There are \(16^3=4096\) formal three-step branch itineraries. Their affine linear parts are products of three matrices \(M_{a,b}\), while integer translations do not affect derivatives. Direct exhaustive multiplication of the \(4^3=64\) possible sign triples yields the following trace multiplicities among the 4096 formal itineraries:
\[
\begin{array}{c|rrrrrrrr}
\operatorname{tr}(M)&-98&-82&-34&-2&22&38&102&198\\\hline
\text{multiplicity}&384&768&768&128&768&384&768&128.
\end{array}
\]
In particular **no trace equals two**. Every branch derivative has determinant one, so \(\det(I-M)=2-\operatorname{tr}(M)\ne0\) for every formal itinerary. Consequently each affine itinerary has at most one point fixed by its third iterate: solve \((I-M)z=c\) with exact rational arithmetic and impose its three intermediate branch inequalities. It is impossible for a whole line or polygon of third-periodic points to survive.

**3. Exact complete census.** The standalone `checker.py` enumerates each of the 4096 finite itineraries, solves the two rational fixed equations, checks every intermediate inequality, and re-evaluates the original global map at each retained candidate. Exactly **177 valid itinerary–point incidences** result. Of their distinct points, 97 occur once, two occur eight times, and one occurs 64 times. The three multiple-incidence points are exactly \((1/2,0)\), \((0,1/2)\), and \((1/2,1/2)\); the additional point \((0,0)\) occurs once. Therefore there are exactly \(97+2+1=100\) distinct points. The four canonical corner/half-corner points are fixed by \(H\), and direct iteration confirms that every other point has least period three. Division of the remaining 96 points by three gives 32 disjoint cycles. This is exhaustive finite symbolic elimination, not finite-orbit sampling.

**4. Regularity, exact return spectrum and arithmetic support.** On every primitive three-cycle the intermediate values \(y\) and \(u\) avoid zero and one-half. Therefore the ordinary derivative at each step is \(M_{a,b}\). For each of the 32 cyclically identified triples, the exact product of its three derivative matrices has determinant one and trace \(102\), \(-34\), or \(-98\), with multiplicities 16, eight and eight respectively. Each trace has absolute value greater than two, hence both reciprocal Floquet multipliers are real and one has modulus greater than one; all these cycles are hyperbolic saddles. The arithmetic support has a direct algebraic explanation. Each step matrix satisfies \(M_{a,b}\equiv I\pmod{2}\), and hence so does every three-step product \(M\). Thus every entry of \(I-M\), and every entry of its two-dimensional adjugate, is even. Since the affine translation is integral, the rational solution of \((I-M)z=c\) has coordinate denominators dividing \(|2-\operatorname{tr}(M)|/2\). For trace \(-34\) this bound is \(18\); for traces \(102\) and \(-98\) it is \(50\). The 24 trace-\(-34\) points therefore belong to the \(1/18\) grid, the remaining 72 primitive points belong to the \(1/50\) grid, and the four fixed points belong to both. These 28 and 76 points exhaust the third-fixed-point set from Step 3, with four in their intersection. The attached `cycles.csv` lists one canonical representative from each cycle with the exact trace, permitting direct reproduction of the entire spectrum.

## Verification
Run `python3 checker.py` in the extracted folder; only the Python standard library is used. The checker independently builds all 16 branch affine maps, enumerates all 4096 three-step words, proves their linear fixed equations nonsingular by checking every possible matrix product, solves all 4096 rational systems, verifies every branch and torus boundary incidence, and groups the 100 unique solutions into 32 three-cycles. It also verifies the fixed points, regularity, exact trace distribution, both grid counts, determinant-one identities, and equality of the generated canonical representatives to every entry of `cycles.csv`. All integer/rational operations are exact: no floating-point tolerance, bounded orbit search or numerical interpolation is used. The proof of completeness is the exhaustive affine partition and the absence of singular fixed equations, not a numerical experiment.

## Relationship to prior work
Myers Hill, Sturman and Wilson introduced the orthogonal non-monotonic shear framework and the symmetric slope-two cusp, and proved mixing results in their 2021 and 2023 works. Their 2023 work identifies four two-periodic line segments and derives polynomial correlation bounds, but does not provide the exact primitive three-cycle census or its return-trace spectrum. The published mathematical record *Eighty primitive four-cycles in the orthogonal tents map* gives a distinct period-four census, including 16 nonsmooth period-four cycles; its return-period divisibility does not imply a third-period count. Another related exact periodic-arc study treats a different one-parameter **single**-tent-shear map with a linear rather than tent-shaped second shear and therefore does not cover the two-tent map above. The result here adds a finite but structurally natural short-period classification, including the absence of three-periodic switching cycles, not a reformulation of measure mixing or density of rational periodic points.

## Limitations
Only least period three is classified; the already-known two-periodic line families, period four and all higher periods are outside this theorem. The result concerns the precise slope-two symmetric map, not a parameter neighborhood, and says nothing about long-time mixing speeds beyond the cited literature. All three-cycle stability claims are linear hyperbolicity, not estimates of global invariant manifolds. The originality comparison relies on the inspected primary materials and indexed records and cannot exclude unindexed equivalent work. Independent mathematical validation has not been performed.

## References
1. J. Myers Hill, R. Sturman, M. C. T. Wilson, *Exponential Mixing by Orthogonal Non-Monotonic Shears*, arXiv:2112.05463, first posted 2021-12-10. https://arxiv.org/abs/2112.05463
2. J. Myers Hill, R. Sturman, M. C. T. Wilson, *Loss of Exponential Mixing in a Non-Monotonic Toral Map*, arXiv:2303.08515, first posted 2023-03-15, primary MSC2020 37A25. https://arxiv.org/abs/2303.08515
3. *Eighty primitive four-cycles in the orthogonal tents map*, exact full-period-four census in the public published-finding corpus collection, 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-eighty-primitive-four-cycles-in-the-orthogonal-tents-map--a8aec9ff96f0/RESULT.md
4. *Eight exact arcs of primitive three-periodic points at a toral-shear resonance*, distinct one-tent map in the public published-finding corpus collection, 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-eight-exact-arcs-of-primitive-three-periodic-points-at-a-toral-s--89b5051ec434/RESULT.md
