# The Manhattan endpoint doubles planar Kuhn-optimal lattice frames

## Finding
Let \(K_p=\{x\in\mathbb R^2:\|x\|_p\le1\}\) for \(1\le p\le\infty\), with the usual convention \(1/\infty=0\). For every ordered linearly independent pair \((a,b)\in(\mathbb Z^2)^2\), let \(\rho_p(a,b)\) be the larger of the minimal \(\ell_p\)-circumradii of \(\operatorname{conv}\{0,a,a+b\}\) and \(\operatorname{conv}\{0,b,a+b\}\), permitting independent centers for the two triangles. Then
\[
\min_{\det(a,b)\ne0}\rho_p(a,b)=2^{1/p-1}.
\]
For every \(1<p\le\infty\), the full set of minimizing **ordered** frames consists of the \(24\) pairs satisfying
\[
a,b,a+b\in S:=\{(\pm1,0),(0,\pm1),(\pm1,\pm1)\}.
\]
All these frames are unimodular. At \(p=1\), the full set consists of the \(48\) ordered frames satisfying
\[
\|a\|_1,\ \|b\|_1,\ \|a+b\|_1\le2.
\]
Exactly \(24\) of these have \(|\det(a,b)|=1\), and the other \(24\) have \(|\det(a,b)|=2\). Every determinant-two optimizer generates the checkerboard sublattice \(\{(m,n)\in\mathbb Z^2:m+n\equiv0\pmod2\}\). Thus the numbers of **unordered** minimizing frames are \(12\) for \(p>1\) and \(24\) for \(p=1\), while the optimal radius remains continuous in \(p\). The additional minimizers at \(p=1\) are precisely the allowed index-two lattice frames.

## Assumptions and scope
The underlying lattice is the fixed standard lattice \(\mathbb Z^2\), and frames may generate proper finite-index sublattices. Translation centers of the two packet triangles are chosen independently in \(\mathbb R^2\). Both \(\ell_p\)-balls and frame vectors use the fixed standard coordinates. Frames are ordered for the numerical counts; each unordered two-element set corresponds to exactly two ordered frames. No requirement that frames form a lattice basis is imposed. The \(p=\infty\) case is the square, and \(p=1\) is the diamond; for finite \(p\), the notation has its usual meaning.

## Proof
**Lower bound.** Every one of the three vectors \(a,b,a+b\), up to sign, is an edge difference of either packet triangle. A translate of \(rK_p\) has \(\ell_p\)-diameter \(2r\). Hence
\[
\rho_p(a,b)\ge\tfrac12\max\{\|a\|_p,\|b\|_p,\|a+b\|_p\}.
\]
Write \(s_p=2^{1/p}\). When \(1\le p<\infty\), the only nonzero integer vectors of norm strictly below \(s_p\) are the four signed coordinate unit vectors. Indeed, \(s_p\le2\), an integer coordinate of magnitude at least two has norm at least two, and two nonzero coordinates have norm at least \(s_p\). If \(a,b,a+b\) all had norm strictly below \(s_p\), independence would make \(a,b\) perpendicular signed coordinate unit vectors, whose sum has norm exactly \(s_p\), a contradiction. For \(p=\infty\), each nonzero integer vector already has norm at least \(s_\infty=1\). Hence \(\rho_p(a,b)\ge s_p/2\) for all frames. For \(a=e_1,b=e_2\), both packet triangles lie in the unit square, whose center is at \(\ell_p\)-distance at most \(s_p/2\) from each point. Thus the lower bound is attained.

**The strict-side classification.** For \(1<p<\infty\), the nonzero integer vectors with norm at most \(s_p\) are precisely the four signed coordinate units and the four signed diagonals; the same description holds at \(p=\infty\), where this is just the nonzero lattice content of the unit coordinate square. Consequently an optimal frame must satisfy \(a,b,a+b\in S\). Conversely, every such pair gives both packet triangles within a (possibly translated) axis-aligned unit square. To see this coordinatewise, observe that the only independent possibilities are a pair of perpendicular signed coordinate units or a signed diagonal paired with a signed coordinate unit which cancels one of its diagonal coordinates. In both cases the coordinates of the three vertices of either packet triangle span intervals of length at most one. Each triangle therefore fits in a translate of \((s_p/2)K_p\). Counting the perpendicular-unit pairs gives \(4\cdot2=8\) ordered frames. Choosing a diagonal and a cancelling axis vector gives \(4\cdot2=8\), with either order, for \(16\) more. Thus there are \(24\) ordered optimizers. Their determinants all have absolute value one.

**The diamond endpoint and exact count.** The invertible linear isometry
\[
U:\mathbb R^2\to\mathbb R^2,\qquad U(x,y)=(x+y,x-y)
\]
satisfies \(\|U(x,y)\|_\infty=\|(x,y)\|_1\). For any finite planar set \(F\), the smallest enclosing \(\ell_\infty\)-square has radius half its \(\ell_\infty\)-diameter: center each coordinate interval at its midpoint. It follows that the minimal enclosing \(\ell_1\)-ball has radius half the \(\ell_1\)-diameter. Applying this to the two triangles gives the **exact formula**
\[
\rho_1(a,b)=\tfrac12\max\{\|a\|_1,\|b\|_1,\|a+b\|_1\}.
\]
Thus the minimizing frames are precisely those satisfying the three stated norm bounds.

The nonzero integer vectors of \(\ell_1\)-norm at most two consist of four signed units, four signed diagonals, and four signed doubled coordinate units. The first two families give exactly the same \(24\) ordered frames as above. An independent pair involving a doubled coordinate unit must pair it with a diagonal which cancels its doubled coordinate in the sum: \(4\) choices for the doubled unit, \(2\) diagonals, and \(2\) orders, giving \(16\) ordered frames. A pair of independent diagonals has acceptable sum precisely for the two transversal diagonal choices per first diagonal, giving \(4\cdot2=8\) ordered frames. There are no other possibilities: a doubled unit paired with an independent unit has sum of norm three; two independent doubled units have sum of norm four. In total \(24+16+8=48\) ordered frames.

The additional \(16+8=24\) frames all have determinant of absolute value two, whereas the first \(24\) are unimodular. Every doubled unit or diagonal has even coordinate sum, so both vectors in each new frame lie in the index-two checkerboard lattice. Their span also has index two by the determinant formula and is therefore exactly that checkerboard lattice. Finally, division by two gives unordered counts \(12\) and \(24\); the formula \(2^{1/p-1}\) is continuous at \(p=1\). This proves every assertion.

## Verification
A standalone script `verify.py` independently enumerates all candidate vectors in the finite \(\ell_1\)-norm-two shell and the finite nonzero unit coordinate square; asserts the complete ordered counts \(48\) and \(24\), determinant multiplicities, and checkerboard congruences; and checks each packet triangle's diameter at the diamond endpoint and unit-square enclosure for the other exponents. The script was executed successfully. The global infinite-lattice lower bound and the sharp radius formula above are analytic proofs, not inferred from finite enumeration.

## Relationship to prior work
Fei Xue introduced \(\kappa\)-covering minima as an optimization over translates of the full permutation-simplex packet for a fixed independent lattice frame. His equation (3.2) ALREADY establishes the exact numerical value \(\kappa(B_p^2,\mathbb Z^2)=2^{1/p-1}\) for the standard planar balls, and the present result does not claim novelty for that value. The new assertion is the exhaustive classification and multiplicity of all minimizing frames, including the discontinuous appearance of index-two frames at the diamond endpoint. The present finding classifies every optimal integer frame along the planar \(\ell_p\) scale, distinguishing proper sublattice optimizers at the polyhedral diamond endpoint. Lian and Xue's covering-body criterion, and Grozev and Nikolov's permutation-simplex covering results, concern related covering mechanisms but do not provide the stated checkerboard optimizer count. A separate all-dimensional classification of cube-optimal Kuhn frames already covers the \(p=\infty\) end; the newly distinct content here is the sharp \(p=1\) transition and its uniform \(p>1\) comparison. A prior classification of all \(\ell_1\)-optimizer frames under equivalent terminology cannot be ruled out solely by literature search.

## Limitations
Only the standard planar integer lattice and the standard coordinate \(\ell_p\) norms are treated. The theorem does not classify optimal frames in higher dimensions, other lattices, or arbitrary centrally symmetric bodies. The reference to the checkerboard lattice is for the \(p=1\) norm only. Independent mathematical validation has not been conducted. Historical originality remains subject to specialist review and potentially unknown equivalent older formulations.

## References
1. Fei Xue, *On \(\kappa\)-covering minima*, arXiv:2610.39034v1, first submitted 2026-10-28.
2. Yanlu Lian and Fei Xue, *Minimal Covering Bodies and a Minkowski-Type Criterion for Lattice Coverings*, arXiv:2606.14584v1, first submitted 2026-06-12.
3. Grozev and Nikolov, arXiv:2610.21572v1, manuscript on Kuhn-simplex covering and parallelotope containment, first available 2026-10.
