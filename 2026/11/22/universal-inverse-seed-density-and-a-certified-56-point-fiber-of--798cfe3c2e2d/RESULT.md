# Universal inverse-seed density and a certified 56-point fiber of the sine-polynomial plane map

## Finding

For the symmetric-parameter member of the two-dimensional sinusoidally constrained polynomial map introduced in [1], define, for every real \(t\ge10\),
\[
 F_t(x,y)=\bigl(\sin(t y(x+1)),\sin(t x(y+1))\bigr),\qquad (x,y)\in Q=[-1,1]^2.
\]
This is the published parameter line \(a=b=\log_{10}t\). For a target \(w=(\xi,\eta)\in Q\), let \(N_t(w)=\#\{z\in Q:F_t(z)=w\}\) count **distinct** preimages, including those on the boundary. Put \(k(w)=\mathbf 1_{\{|\xi|=1\}}+\mathbf 1_{\{|\eta|=1\}}\).

**Theorem.** There is an absolute constant \(C\) such that simultaneously for every \(t\ge10\) and \(w\in Q\),
\[
 \left|N_t(w)-\frac{13}{3\pi^2}\,2^{-k(w)}t^2\right|\le Ct.
\]
For every fixed \(w\in Q\) and every continuous \(\varphi:Q\to\mathbb R\),
\[
 \lim_{t\to\infty}\frac{1}{N_t(w)}\sum_{F_t(z)=w}\varphi(z)
 =\frac3{13}\iint_Q |1+x+y|\varphi(x,y)\,dx\,dy.
\]
In particular, the limiting proportions of preimages above and below the line \(x+y=-1\) are exactly \(25/26\) and \(1/26\). At the source's smallest symmetric admissible parameter \(a=b=1\), or \(t=10\), an exact finite certificate gives
\[
 \boxed{N_{10}(0,0)=56.}
\]
There are exactly 43 preimages in the interior of \(Q\) and 13 on its boundary; 49 lie on \(x+y>-1\), and 7 lie on \(x+y<-1\). All statements concern **one-step inverse fibers**, not invariant measures or Lyapunov exponents.

## Assumptions and scope

The phase space is the *closed* forward-invariant square \(Q=[-1,1]^2\); the map is evaluated over real numbers with exact trigonometric functions, not in floating-point arithmetic. The parameter \(t\ge10\) is real and corresponds to the equal-gain diagonal \(a=b=\log_{10}t\) of the formula in [1]. The large-\(t\) limit is a mathematical continuation beyond the finite numerical parameter window \(1\le a,b\le12\) investigated in [1]. For boundary targets, duplicate branches of the inverse sine are counted only once. Neither preimages outside \(Q\) nor numerical rounding collisions are counted. \(O(t)\) means a constant uniform in all target coordinates, including targets on the sides and corners of \(Q\).

## Proof

**1. An exact global fold normal form.** Factor the map into the quadratic phase map and coordinatewise sine:
\[
 G(x,y)=(y(x+1),x(y+1)),\qquad F_t=(\sin(t\,\cdot),\sin(t\,\cdot))\circ G.
\]
Introduce \(u=x-y\) and \(v=x+y+1\). Direct expansion yields
\[
 G_1=\frac{v^2-(u+1)^2}{4},\qquad
 G_2=\frac{v^2-(u-1)^2}{4},\qquad
 \det DG=-(1+x+y)=-v.
\]
Thus \(G\) is injective on each of the closed polygonal sheets \(Q_+=Q\cap\{v\ge0\}\) and \(Q_-=Q\cap\{v\le0\}\), and its only critical locus in \(Q\) is the straight fold \(v=0\). Indeed, the difference of the two phase coordinates determines \(u\), and their sum determines \(v^2\); the sign of \(v\) chooses the sheet. Both sheet images \(E_\pm=G(Q_\pm)\) have piecewise smooth, rectifiable boundaries, since they are polynomial images of finite polygonal boundaries.

**2. Exact inverse enumeration.** For \(s\in[-1,1]\), write \(\mathcal P_s\) for the distinct phases
\[
 \mathcal P_s=\{\arcsin(s)+2\pi j:j\in\mathbb Z\}\cup
 \{\pi-\arcsin(s)+2\pi j:j\in\mathbb Z\}.
\]
When \(|s|=1\), the two progressions coincide (after reindexing); otherwise they are disjoint. Every preimage of \(w\) arises uniquely from a phase pair \((P,R)\in\mathcal P_\xi\times\mathcal P_\eta\) for which
\[
 u=\frac{R-P}{t},\qquad V=1+u^2+\frac{2(P+R)}t\ge0,
\]
and at least one of \(v=\sqrt V\) or \(v=-\sqrt V\) satisfies
\[
 |u|-1\le v\le3-|u|,
 \qquad x=\frac{v-1+u}{2},\quad y=\frac{v-1-u}{2}.
\]
At \(V=0\), the two displayed signs produce only one point. This formula is exhaustive: the inequalities are exactly the four square constraints \(-1\le x,y\le1\). All phases necessarily lie in \([-2t,2t]\), so the enumeration is finite for fixed \(t\).

**3. Uniform lattice counting.** For fixed \(w\), the allowable phase pairs are a union of \(2^{2-k(w)}\) distinct translates of the lattice \((2\pi\mathbb Z)^2\). After scaling by \(1/t\), the lattice spacing is \(h=2\pi/t\). For a fixed bounded Jordan region with rectifiable boundary, counting points of any translated square lattice of mesh \(h\) gives
\[
 \#\bigl(E\cap(h\mathbb Z^2+\zeta)\bigr)=\frac{\operatorname{area}(E)}{h^2}+O(h^{-1}),
\]
uniformly in the translation \(\zeta\): enclose each counted point in a mesh cell; disagreement with the area occurs only in the \(O(h)\)-wide boundary strip, of area \(O(h)\). Apply this on both \(E_+\) and \(E_-\); their common boundary and other boundary fibers contribute only \(O(h^{-1})\), including any fold coincidences. Because \(G\) is one-to-one on either sheet, change of variables gives
\[
 \operatorname{area}(E_+)+\operatorname{area}(E_-)
 =\iint_Q|\det DG|\,dx\,dy
 =\iint_Q|1+x+y|\,dx\,dy.
\]
The signed integral is \(4\), while the integral of \(-(1+x+y)\) over the lower-left triangle \(Q_-\) is \(1/6\). Hence the absolute integral is \(4+2(1/6)=13/3\), with sheet areas \(25/6\) and \(1/6\). As each phase lattice has point density \(t^2/(4\pi^2)\), summing over \(2^{2-k(w)}\) lattices yields the stated coefficient and uniform \(O(t)\) remainder. This is a direct two-sheet argument and does not assume a globally invertible phase map.

**4. Spatial law.** For any continuous \(\varphi\), the inverse of \(G\) restricted to each compact sheet is continuous onto its image. Shifted-grid Riemann sums of \(\varphi\circ(G|_{Q_\pm})^{-1}\) therefore converge to its integral over \(E_\pm\). The change of variables transforms their sum into \(\int_Q\varphi|\det DG|\). Dividing by the preimage count from Step 3 proves weak convergence. The sheet areas give the proportions \(25/26\) and \(1/26\).

**5. The exact \(t=10\) fiber.** For \(w=(0,0)\), the phases are \(P=m\pi\) and \(R=n\pi\). Because \(6\pi<20<7\pi\), it suffices to consider \(-6\le m,n\le6\). The inverse formula in Step 2, together with a rational enclosure of \(\pi\) from Machin's arctangent identity, certifies exactly 43 strict interior solutions. The remaining 13 are the explicit boundary solutions
\[
 (-1,-1+j\pi/10),\qquad (-1+j\pi/10,-1),\qquad j=0,1,\ldots,6,
\]
with \((-1,-1)\) listed only once. The attached standard-library checker performs rigorous rational interval comparisons of every phase pair and records no unresolved cases. In particular, the exact total is \(43+13=56\). The sign of \(v\) in the same enumeration gives 49 and 7 preimages on the respective open sides of the fold.

## Verification

Run `python3 check.py` with a standard Python 3 interpreter. The checker verifies the quadratic coordinate identities over rational sample points, the exact \(13/3\) Jacobian-area calculation, a rigorous \(\pi\) interval using alternating series, all 169 possible phase-index pairs at \(t=10\), the 43 strict interior solutions, and the 13 exact boundary solutions. It uses rational comparisons and integer square-root bounds, not floating-point decisions. The asymptotic statements are proved analytically in Steps 3–4; finite tests do not certify the infinite limit. The implementation supplies a reproducible finite certificate only for the fixed \(t=10\) count.

## Relationship to prior work

The original source [1], Equation (3) and Section 3, defines this map and studies numerical Lyapunov exponents, bifurcation plots, entropy diagnostics and image-encryption applications. Its text does not supply the global quadratic fold form, target-independent preimage growth, limiting inverse-preimage density or the exact 56-point fiber. The subsequent use of the same map in [2], Section 2.1, presents the defining equations and simulation-based sequence analyses, not inverse-fiber results. The proof employs standard area/multiplicity principles [3] and elementary lattice-cell estimates; neither technique alone supplies the displayed map-specific Jacobian constant, fold geometry or the exact finite count. The result should not be interpreted as a claim that the general techniques are new.

## Limitations

No assertion is made about forward orbit convergence, positive entropy, finite-precision implementations or encryption security. The \(O(t)\) estimate is a coarse, potentially nonoptimal discrepancy bound, not an exact second-order asymptotic. The limit for empirical preimage measures is taken at fixed target (although the counting error is uniform in target). The scientific priority statement is limited to the cited literature and accessible searchable records; equivalent unindexed work may exist. An independent mathematical audit has not been performed.

## References

[1] W. Feng, Q. Wang, H. Liu, Y. Ren, J. Zhang, S. Zhang, K. Qian and H. Wen, *Exploiting Newly Designed Fractional-Order 3D Lorenz Chaotic System and 2D Discrete Polynomial Hyper-Chaotic Map for High-Performance Multi-Image Encryption*, Fractal and Fractional 7 (2023), 887, first public December 16, 2023. https://doi.org/10.3390/fractalfract7120887

[2] *A Novel Multi-Channel Image Encryption Algorithm Leveraging Pixel Reorganization and Hyperchaotic Maps*, Mathematics 12 (2024), 3917. https://doi.org/10.3390/math12243917

[3] *Area formula*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Area_formula (background method only).
