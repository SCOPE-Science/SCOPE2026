# Quadratic inverse-sheet growth and a boundary criticality jump in a cosine-memristor map

## Finding

For the two-dimensional sine–cosine memristive map
\[
F_{a,b,c}(x,y)=\bigl(c+a\sin(bx\cos y),\,x+y\bigr),
\qquad a,b>0,\quad c\in\mathbb R,
\]
the number of real one-step predecessors of a fixed output \((U,V)\), truncated at \(|x|\le R\), has a universal **quadratic** growth law. Define
\[
N_R(U,V)=\#\{(x,y)\in\mathbb R^2:F_{a,b,c}(x,y)=(U,V),\ |x|\le R\}.
\]
For every fixed \((U,V)\) and every \(R>0\), the following three exhaustive cases hold:
\[
\boxed{
N_R(U,V)=
\begin{cases}
0,&|U-c|>a,\\[2pt]
\displaystyle\frac{2b}{\pi^2}R^2+O_{a,b,c,U,V}(R),&|U-c|<a,\\[5pt]
\displaystyle\frac{b}{\pi^2}R^2+O_{a,b,c,U,V}(R),&|U-c|=a.
\end{cases}}
\]
In particular, the image of \(F_{a,b,c}\) is exactly the closed vertical strip \(\{(U,V):|U-c|\le a\}\); every target in this strip has countably infinitely many distinct real predecessors. At both strip edges **all** the predecessors are critical points of the map, while in the interior the number of critical predecessors with \(|x|\le R\) is at most \(O_{b,V}(R)\). Thus the leading quadratic growth in the strip interior consists entirely of regular inverse sheets.

For every fixed output \((U,V)\), the same leading coefficients, with \(O(R)\) errors, hold if the truncation \(|x|\le R\) is replaced by the symmetric observation window \(\max\{|x|,|y|\}\le R\).

## Assumptions and scope

All input and output coordinates are **real**, not taken modulo \(2\pi\). The parameters \(a,b\) are strictly positive and \(c\) is any real number. The output \((U,V)\) remains fixed as \(R\to\infty\). The predecessor count uses distinct points without multiplicity, including at tangencies and at endpoints. The asymptotic error constant can depend on the displayed fixed parameters and output, and no uniformity over moving outputs or varying parameters is asserted. The map is the \(\mathrm{MM}_1\) model of Ramadoss et al. [1], with output coordinates written \((U,V)\).

## Proof

**1. Scalar reduction.** The second output equation gives \(y=V-x\) uniquely. Put
\[
s=\frac{U-c}{a},\qquad \phi_V(x)=bx\cos(V-x).
\]
The predecessor equation is therefore exactly
\[
\sin\phi_V(x)=s,\qquad y=V-x.
\]
If \(|s|>1\), there are no solutions. If \(|s|\le1\), the continuous function \(\phi_V\) is unbounded both above and below on the positive real half-line: choose arbitrarily large positive \(x\) successively satisfying \(V-x\in2\pi\mathbb Z\) and \(V-x\in\pi+2\pi\mathbb Z\). Consequently its image contains every real value, so the scalar equation has infinitely many solutions. As the real-analytic function \(\sin\phi_V-s\) is not identically zero, its zero set is discrete and at most countable. This proves the exact image and the countable-infinite-fiber assertion.

**2. There are only linearly many monotonicity pieces.** Differentiate:
\[
\phi'_V(x)=b\bigl(\cos(V-x)+x\sin(V-x)\bigr).
\]
For \(|x|\ge1\), any stationary point has \(\sin(V-x)\ne0\) and satisfies
\[
\tan(V-x)=-\frac1x.
\]
Between consecutive poles of \(\tan(V-x)\), the function \(\tan(V-x)+1/x\) is strictly decreasing, since its derivative is
\[
-\sec^2(V-x)-\frac1{x^2}<0.
\]
Thus there is at most one stationary point in each such interval, on either side of the origin. The stationary points in the fixed compact interval \([-1,1]\) are finite because \(\phi'_V\) is a nonzero real-analytic function. It follows that the number of intervals of monotonicity of \(\phi_V\) within \([-R,R]\) is \(O_V(R+1)\).

**3. Count roots through phase variation.** For \(-1<s<1\), the distinct values of \(t\) satisfying \(\sin t=s\) have asymptotic density \(1/\pi\) per unit length of \(t\). At \(s=\pm1\), they instead lie on a single progression of step \(2\pi\), so their density is \(1/(2\pi)\). On each interval of strict monotonicity of \(\phi_V\), counting these phase levels incurs an error bounded by an absolute constant. Summing over monotonicity pieces, and correcting any double counting of points at shared endpoints, gives
\[
N_R(U,V)=\begin{cases}
\displaystyle\frac1\pi\operatorname{Var}_{[-R,R]}(\phi_V)+O_V(R+1),&|s|<1,\\[4pt]
\displaystyle\frac1{2\pi}\operatorname{Var}_{[-R,R]}(\phi_V)+O_V(R+1),&|s|=1.
\end{cases}
\]
This counting identity remains valid even at a critical point where two monotonicity intervals meet, because the total number of such meetings is \(O(R+1)\).

**4. Sharp variation asymptotic.** By the reverse triangle inequality,
\[
\left|\operatorname{Var}_{[-R,R]}(\phi_V)-b\int_{-R}^R|x\sin(V-x)|\,dx\right|
\le b\int_{-R}^R|\cos(V-x)|\,dx\le2bR.
\]
Since \(|\sin t|\) has mean \(2/\pi\), its centered version has a bounded periodic primitive. Integration by parts on each half-line then shows, for fixed \(V\),
\[
\int_{-R}^R|x\sin(V-x)|\,dx
=\frac2\pi\int_{-R}^R|x|\,dx+O_V(R+1)
=\frac{2R^2}{\pi}+O_V(R+1).
\]
Therefore \(\operatorname{Var}_{[-R,R]}(\phi_V)=2bR^2/\pi+O_{b,V}(R+1)\). Substitution into the counting identity yields all three displayed asymptotic cases, with the factor-of-two drop exactly at the boundary. The argument is analytic and covers all \(R\), rather than relying on finite enumeration.

**5. Criticality and alternative window.** The Jacobian determinant is
\[
\det DF_{a,b,c}(x,y)=ab\cos(bx\cos y)\bigl(\cos y+x\sin y\bigr).
\]
On either output boundary \(|s|=1\), the first cosine factor vanishes at every predecessor. In the open strip, \(\cos\phi_V(x)\ne0\) at a predecessor; hence criticality is equivalent to \(\phi'_V(x)=0\), and Step 2 bounds these points by \(O(R+1)\).

Finally, with \(y=V-x\), the square observation window corresponds to \(x\in[-R,R]\cap[V-R,V+R]\). Its symmetric difference with \([-R,R]\) consists of at most two end intervals of total length at most \(2|V|\). On these fixed-length intervals \(|\phi'_V(x)|=O_{b,V}(R+1)\), and the monotone-piece level count above implies that at most \(O_{b,V}(R+1)\) predecessors are gained or lost. Thus the same quadratic coefficients hold for the square window.

## Verification

The accompanying standalone Python standard-library file `inverse_count_verify.py` counts inverse roots by partitioning finite input windows into monotone phase intervals, then tests the quadratic coefficients at multiple radii. Its successful run prints `COSINE_MEMRISTOR_INVERSE_VERIFY_OK`; representative counts for \(b=1.3\), \(V=0.7\), \(s=0.2\) at \(R=20,40,80,160\) are respectively \(107,425,1686,6747\), compared with leading coefficient \(2b/\pi^2\approx0.263435\). For \(s=1\) the corresponding counts are \(53,212,843,3374\), compared with \(b/\pi^2\approx0.131718\). These finite diagnostics exercise the formulas but do **not** establish the asymptotics; Steps 1–5 prove the infinite statement.

## Relationship to prior work

Ramadoss et al. [1] introduce the exact sine–cosine memristive map and investigate fixed points, bifurcation, symmetry and iterated attractors. The complete source text does not give this exact inverse-fiber count, its quadratic coefficient, or the criticality distinction on the image boundary. Han et al. [2] and Zhang et al. [3] investigate differently defined two-dimensional memristive maps coupled to cosine terms, chiefly through dynamical simulations and attractor analysis; their formulas do not imply this MM1 inverse classification. General facts about sine levels and bounded periodic primitives supply techniques, but do not themselves state the resulting image geometry and coefficient for this published map. No claim of exhaustive literature uniqueness is made.

## Limitations

This is a theorem about the global **one-step inverse relation** in the full real plane. It does not classify forward attractors, bounded invariant sets, cryptographic properties, higher-period orbit counts or the effect of quotienting the memory coordinate modulo \(2\pi\). The asymptotic remainder may depend on a fixed target; it need not remain uniform if the target moves with the window. The finite numerical checks are diagnostics, not independent certification. An unindexed equivalent analysis may exist and priority would then require reassessment.

## References

[1] J. Ramadoss, O. A. Almatroud, S. Momani, V.-T. Pham and V. P. Thoai, *Discrete Memristance and Nonlinear Term for Designing Memristive Maps*, Symmetry **14** (2022), 2110, publicly published 11 October 2022, DOI: https://doi.org/10.3390/sym14102110 .

[2] X. Han, X. Bi, B. Sun, L. Ren and L. Xiong, *Dynamical Analysis of Two-Dimensional Memristor Cosine Map*, Frontiers in Physics **10** (2022), DOI: https://doi.org/10.3389/fphy.2022.911144 .

[3] L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang, W.-P. Lyu and Q.-S. Bi, *Extremely hidden multi-stability in a class of two-dimensional maps with a cosine memristor*, Chinese Physics B **31** (2022), 100503, DOI: https://doi.org/10.1088/1674-1056/ac7294 .
