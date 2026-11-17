# A two-term boundary-chord law and logarithmic endpoint marks for the Reuleaux triangle

## Finding

Let \(K\) be the unit-width Reuleaux triangle formed by the intersection of the unit disks centered at the vertices of a unit equilateral triangle. Independently choose \(X,Y\) from \(\partial K\), each with uniform **Euclidean arclength** measure (total boundary length \(\pi\)). Set \(D=|X-Y|\). For \(0<\varepsilon<1\), put \(L=\pi/3\), \(h=2\varepsilon-\varepsilon^2\), and \(q_\varepsilon=2\arcsin((1-\varepsilon)/2)\). Define
\[
F(u,v)=8\sin(u/2)\sin(v/2)\cos((u+v)/2),\qquad 0\le u,v\le L.
\]
Let \(u_0\in(0,L)\) be the unique solution of \(F(u_0,L)=h\), and let
\[
V_h(u)=\arcsin\!\left(\sin(u/2)+\frac{h}{4\sin(u/2)}\right)-\frac u2\qquad (u_0\le u\le L).
\]
Then the **exact** finite-threshold distance law is
\[
\boxed{\Pr(D>1-\varepsilon)=\frac{6}{\pi^2}\left[L u_0+\int_{u_0}^L V_h(u)\,du\right]+\frac{3}{\pi^2}(L-q_\varepsilon)^2.}
\]
In particular, as \(\varepsilon\downarrow0\),
\[
\boxed{\Pr(D>1-\varepsilon)=\frac{6}{\pi^2}\varepsilon\left[\log(1/\varepsilon)+1+\log(4/3)\right]+o(\varepsilon).}
\]
There is also a **marked logarithmic law**. With probability tending to one conditional on \(D>1-\varepsilon\), the endpoints occupy different circular arcs. Their ordered arc labels \(J\) are then asymptotically uniform among the six possibilities. For any such ordered pair, let \(U\in(0,L)\) denote the arclength of the first point from the arc's vertex opposite to the second arc's opposite vertex. Define \(T_\varepsilon=\log U/\log\varepsilon\) and \(W_\varepsilon=(1-D)/\varepsilon\). Under the same conditioning, the joint law of \((J,T_\varepsilon,W_\varepsilon)\) converges **in total variation** to three independent uniform laws: six equally likely ordered arc pairs and two independent \(\operatorname{Uniform}[0,1]\) variables. Define \(J\) arbitrarily on the negligible same-arc event.

## Assumptions and scope

The three unit disks have centers \((0,0)\), \((1,0)\), and \((1/2,\sqrt3/2)\). Their intersection has three smooth circular arcs, each radius one and length \(L=\pi/3\), with only finitely many corner endpoints. Sampling is independent and uniform in **boundary arclength**, not uniform in enclosed area and not invariant affine-line sampling. Chords join the sampled points directly in the Euclidean plane. The scale \(\varepsilon\) is the absolute length deficit from the diameter one; no sample-size limit is taken.

For a pair of different arcs, \(U,V\in[0,L]\) measure arclength from the two opposing vertices, each being a vertex of the other arc's generating circle. Their joint density, before conditioning on the arc labels, is constant. The six ordered pair types are equivalent by the dihedral symmetries of \(K\). The logarithmic mark may lie outside \([0,1]\) at finite \(\varepsilon\); the limit assertion is convergence of probability measures on the disjoint union of six labelled copies of \(\mathbb R^2\).

## Proof

**1. Exact geometry and disjoint arc decomposition.** Consider the two arcs parametrized by
\[
 x(u)=(\cos u,\sin u),\qquad y(v)=(1-\cos v,\sin v),\qquad 0\le u,v\le L.
\]
A direct squared-distance calculation gives
\[
1-|x(u)-y(v)|^2=1-\bigl(3+2\cos(u+v)-2\cos u-2\cos v\bigr)
=8\sin(u/2)\sin(v/2)\cos((u+v)/2)=F(u,v).
\]
The range \(0\le u+v\le2\pi/3\) makes \(F\ge0\), and it is increasing in each variable because
\[
F(u,v)=4\sin(u/2)[\sin(v+u/2)-\sin(u/2)],\quad
\partial_v F=4\sin(u/2)\cos(v+u/2)\ge0.
\]
The strict version holds in the interior, and \(F(L,L)=1\). As \(D>1-\varepsilon\) is equivalent to \(F(u,v)<h\), its region on two different arcs has area
\[
I(h)=L u_0+\int_{u_0}^L V_h(u)\,du,
\]
by solving \(F(u,v)=h\) for \(v\), with \(0<v\le L\). The inverse-sine argument belongs to \([0,1]\) precisely in this range.

For two points on the same unit-radius circular arc, the chord length is \(2\sin(|u-v|/2)\). Thus the condition \(D>1-\varepsilon\) is \(|u-v|>q_\varepsilon\); its area inside \([0,L]^2\) is exactly \((L-q_\varepsilon)^2\). There are six ordered different-arc pairs and three same-arc pairs; dividing their areas by the total squared perimeter \(\pi^2\) proves the exact formula.

**2. The logarithmic two-term area estimate.** Let \(h\downarrow0\) and choose \(\rho=h^{1/3}\). Decompose \([0,L]^2\) into a central square \([0,\rho]^2\), two edge strips \([\rho,L]\times[0,\rho]\) and \([0,\rho]\times[\rho,L]\), and the remaining square \([\rho,L]^2\). On the central square, Taylor expansion of the exact trigonometric expression gives uniformly
\[
F(u,v)=2uv[1+O(\rho^2)].
\]
Because \(h/(2\rho^2)\to0\), comparison with the hyperbolic area formula shows
\[
\operatorname{area}\{(u,v)\in[0,\rho]^2:F(u,v)<h\}
=\frac h2\left[1+\log\frac{2\rho^2}{h}\right]+o(h).
\]
The error is at most \(O(h\rho^2[1+\log(\rho^2/h)])=o(h)\), by comparison with the thresholds \(h/[1\pm C\rho^2]\).

In the first edge strip, for \(u\ge\rho\), the positive solution \(v_h(u)\) satisfies \(v_h(u)=O(h/\rho)=o(\rho)\). Taylor expansion at \(v=0\) and \(\partial_vF(u,0)=2\sin u\) give uniformly
\[
v_h(u)=\frac{h}{2\sin u}\left[1+O(h/\rho^2)\right].
\]
Its strip area is \(\frac h2\int_\rho^L\csc u\,du+o(h)\), since \((h/\rho^2)\log(1/\rho)\to0\). The other strip has equal area by symmetry. On \([\rho,L]^2\), the ratio \(F(u,v)/(uv)\) is bounded below by a positive absolute constant on \((0,L]^2\), so \(F\ge c\rho^2\gg h\) and there is no contribution. Consequently,
\[
\begin{aligned}
I(h)&=\frac h2\left[1+\log\frac{2\rho^2}{h}\right]
+h\int_\rho^L\csc u\,du+o(h)\\
&=\frac h2\left[1+\log\frac{8\tan^2(L/2)}{h}\right]+o(h)
=\frac h2\left[\log(1/h)+1+\log(8/3)\right]+o(h).
\end{aligned}
\]
Here \(\int\csc u\,du=\log\tan(u/2)\), \(\tan(L/2)=1/\sqrt3\), and \(\tan(\rho/2)\sim\rho/2\). Finally, \(h=2\varepsilon+O(\varepsilon^2)\) and \((L-q_\varepsilon)^2=O(\varepsilon^2)\). Substitution in the exact formula proves the stated two-term law, with its remainder \(o(\varepsilon)\).

**3. Independent uniform logarithmic and deficit marks.** Conditional on any fixed ordered distinct-arc pair and \(D>1-\varepsilon\), the variables \((u,v)\) have constant density \(1/I(h)\) on \(F(u,v)<h\). Set \(t=\log u/\log\varepsilon\) and \(w=(1-D)/\varepsilon\). For each fixed \((t,w)\in(0,1)^2\), we have \(u=\varepsilon^t\downarrow0\), and the unique \(v\) satisfying \(D=1-\varepsilon w\) obeys \(v\sim\varepsilon^{1-t}w\). Thus \(u,v\to0\) and
\[
\frac{\partial(1-D)}{\partial v}=\frac{\partial_vF}{2D}\sim u.
\]
The Jacobian is therefore
\[
\left|\frac{\partial(u,v)}{\partial(t,w)}\right|
=|\log\varepsilon|u\frac{\varepsilon}{\partial_v(1-D)}
\sim\varepsilon|\log\varepsilon|.
\]
The area law from Step 2 yields \(I(2\varepsilon-\varepsilon^2)\sim\varepsilon|\log\varepsilon|\). Hence the transformed conditional density tends to one pointwise almost everywhere on \((0,1)^2\). Its restriction there has total mass tending to one (Fatou's lemma and the fact that the full density integrates to one), so Scheffé's lemma gives convergence in \(L^1\) on \(\mathbb R^2\), including vanishing mass outside the unit square. This proves total variation. The ordered arc pair is exactly uniform among the six on the event of distinct arcs by symmetry, and the conditional same-arc probability is \(O(\varepsilon^2/[\varepsilon\log(1/\varepsilon)])=o(1)\). Mixing gives the stated joint independent uniform limit.

## Verification

The standalone script `verify_reuleaux_boundary.py` constructs the arcs independently from their circle centers, checks the squared-distance defect at several parameter points, evaluates the exact one-dimensional quadrature, and compares it with the two-term asymptotic. At \(\varepsilon=10^{-6}\), exact quadrature gives probability \(9.18163843707\times10^{-6}\), versus \(9.18164012455\times10^{-6}\) from the two-term law (relative discrepancy approximately \(1.84\times10^{-7}\)). A separate simulation of 1,200,000 independent boundary point pairs at three thresholds agreed with the exact formula within its predeclared five-standard-error bounds. The script printed `REULEAUX_BOUNDARY_TWO_TERM_MARKED_DIAGNOSTIC_OK`. These are finite checks; Step 2 and Step 3, not the simulation, prove the asymptotic and total variation limit.

## Relationship to prior work

Bäsel's *Random chords and point distances in regular polygons* (arXiv:1204.2707; first public 12 April 2012) derives invariant-line chord distributions and interior pair-distance laws for **straight-edged regular polygons**, not the boundary-uniform point pair law for a curvilinear constant-width body here. Two published Reuleaux results are especially close but use distinct probability measures: *A logarithmic terminal chord law for the Reuleaux triangle* concerns motion-invariant randomly selected **lines**, and *Logarithmic near-diameter distance tails for every regular Reuleaux odd-gon* concerns **area-uniform interior** endpoint pairs. The latter establishes an \(\varepsilon^3\log(1/\varepsilon)\) law, not the boundary sampling's \(\varepsilon\log(1/\varepsilon)\) two-term law. Neither inspected proof contains the exact present boundary sampling formula or the independent logarithmic endpoint and normalized-deficit marks. These different schemes cannot be exchanged without a nontrivial endpoint Jacobian. The classical geometry of the Reuleaux triangle and the notion of multiple random-chord sampling schemes are not novel claims.

## Limitations

The explicit formula and the two-term asymptotic hold for the unit Reuleaux **triangle**, not arbitrary constant-width curves or all regular Reuleaux odd-gons. The marked result concerns two independent uniformly arclength-sampled endpoints and is not a statement about invariant random affine lines or uniform interior points. The exact integral formula applies to \(0<\varepsilon<1\); the asymptotic and total-variation statements require \(\varepsilon\downarrow0\). The simulation checks selected finite thresholds only. An older general treatment by Coleman (1969) and Gates (1987) could not both be read in full; the available descriptions concern different random-path or chord models, but complete historical priority remains unverified. Independent verification is not claimed.

## References

1. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first public 12 April 2012, https://arxiv.org/abs/1204.2707; *Acta Mathematica Universitatis Comenianae* **83** (2014), 1–18, https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/view/71.
2. *A logarithmic terminal chord law for the Reuleaux triangle* (published mathematical result), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-logarithmic-terminal-chord-law-for-the-reuleaux-triangle--bbcd3963fc69; the RESULT.md was inspected in full.
3. *Logarithmic near-diameter distance tails for every regular Reuleaux odd-gon* (published mathematical result), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-logarithmic-near-diameter-distance-tails-for-every-regular-reule--f7a617353911; the RESULT.md was inspected in full.
4. F. Tong, M. Ahmadi, and J. Pan, *Random Distances Associated with Arbitrary Triangles*, arXiv:1312.2498 (first public 29 November 2013), https://arxiv.org/abs/1312.2498.
5. R. Coleman, *Random Paths through Convex Bodies*, *Journal of Applied Probability* **6** (1969), 430–441, https://doi.org/10.2307/3212012 (description available; full article not inspected).
