# Singular zero-to-infinite inverse-valence transition in a cosine-flux Chialvo map

## Finding

For the cosine-memristive reduced Chialvo map
\[
T_{r,k}(x,\phi)=\left(x^2e^{r-x}+k_0+kx\cos(\pi\phi),\;k_1x-k_2\phi\right),
\]
on the strictly positive input quadrant \(Q=(0,\infty)^2\), assume \(r,k_0\in\mathbb R\), \(k_1,k_2>0\), and \(k\in\mathbb R\). For every nonzero coupling \(k\), **every target** \((X,\Phi)\in\mathbb R^2\) has countably infinitely many distinct preimages in \(Q\); the map restricted to \(Q\) is therefore onto the entire plane. All but finitely many of the preimages are regular (nonzero Jacobian determinant). With the target and parameters fixed, the counting function
\[
N_{X,\Phi}(R)=\#\{(x,\phi)\in Q:T_{r,k}(x,\phi)=(X,\Phi),\ 0<x\le R\}
\]
satisfies the sharp leading asymptotic
\[
\boxed{N_{X,\Phi}(R)=\frac{k_1}{k_2}R+O(1)\qquad(R\to\infty).}
\]
The leading coefficient depends only on the flux slope, not on the nonzero coupling amplitude, recovery parameter, bias, or target.

More precisely, put \(\nu=k_1/k_2\) and \(z_j=(\Phi+k_2(j+1/2))/k_1\). For every sufficiently large integer \(j\), there is exactly one positive preimage whose flux coordinate lies in \((j,j+1)\). It has the expansion
\[
x_j=z_j+\frac{(-1)^{j+1}(X-k_0)}{\pi k\nu z_j}+O(z_j^{-2}),\qquad
\phi_j=\frac{k_1x_j-\Phi}{k_2}.
\]

At the decoupled endpoint \(k=0\), the contrast is absolute: no target has more than two preimages in \(Q\), and the image is contained in the proper strip
\[
\bigl(k_0,k_0+4e^{r-2}\bigr]\times\mathbb R.
\]
Thus arbitrarily small nonzero cosine coupling produces a singular jump from finite inverse valence to unbounded, asymptotically linear inverse multiplicity, as well as surjectivity from strictly positive input states.

## Assumptions and scope

All assertions concern the exact untruncated real map above. The full-plane target is arbitrary, including targets with negative coordinates; only source points are required strictly positive. The coupling \(k\) may have either sign. The constants in the asymptotic remainder may depend on all fixed parameters and the target; no uniformity as \(k\to0\) is claimed. A preimage is *regular* if \(\det DT_{r,k}\ne0\).

## Proof

**1. Reduction to a scalar oscillatory inverse equation.** Fix \((X,\Phi)\in\mathbb R^2\) and \(k\ne0\). The second component uniquely determines
\[
\phi=\nu x-\frac{\Phi}{k_2},\qquad \nu=\frac{k_1}{k_2}>0.
\]
Write \(A=X-k_0\) and
\[
g(x)=\frac{A-x^2e^{r-x}}{kx}=\frac{A}{kx}-\frac{x e^{r-x}}k.
\]
The first component becomes
\[
\cos\left(\pi\left(\nu x-\frac{\Phi}{k_2}\right)\right)=g(x).
\]
For fixed admissible parameters and target, \(g(x)=O(x^{-1})\) and \(g'(x)=O(x^{-2})\) as \(x\to\infty\). In particular these bounds remain valid when \(A=0\).

**2. Exactly one large root in each flux cell.** For each integer \(j\) define
\[
I_j=\left(\frac{\Phi+k_2j}{k_1},\ \frac{\Phi+k_2(j+1)}{k_1}\right).
\]
For all sufficiently large \(j\), the entire cell lies in \(x>0\), its corresponding flux lies in \((j,j+1)\subset(0,\infty)\), and throughout the cell \(|g(x)|<1/2\), \(|g'(x)|<\pi\nu\sqrt3/2\). At the endpoints, the cosine equals \((-1)^j\) and \((-1)^{j+1}\) while \(|g|<1/2\), giving opposite signs for the continuous difference \(h(x)=\cos(\pi(\nu x-\Phi/k_2))-g(x)\). Thus a root exists in each cell.

Any such root necessarily obeys \(|\cos(\pi(\nu x-\Phi/k_2))|<1/2\). On the middle subinterval of the flux cell where this holds, the sine has constant sign and absolute value greater than \(\sqrt3/2\); hence
\[
h'(x)=-\pi\nu\sin\left(\pi\left(\nu x-\frac\Phi{k_2}\right)\right)-g'(x)
\]
never vanishes and has a fixed sign. All zeros lie in this middle interval, so there is precisely one zero in each sufficiently high cell.

**3. Counting, discreteness, and regularity.** Each high flux cell contributes exactly one preimage. The number of completed cells through \(x=R\) differs from \(\nu R\) by \(O(1)\). There are only finitely many preimages in the bounded remaining portion \(x>0\) satisfying the positive-flux condition: near \(x=0\), if \(A\ne0\) the first component tends to \(k_0\ne X\), whereas if \(A=0\), division by \(x>0\) yields \(x e^{r-x}+k\cos(\pi(\nu x-\Phi/k_2))=0\). This is analytic through \(x=0\) and is not identically zero (its cosine term oscillates with nondecaying amplitude as \(x\to\infty\)). Any bounded interval therefore contains only finitely many roots. Hence \(N_{X,\Phi}(R)=\nu R+O(1)\), and the fiber is countably infinite with all but finitely many roots in the uniquely controlled high cells.

For the Jacobian, let
\[
G(x)=x^2e^{r-x}+k_0+kx\cos\left(\pi\left(\nu x-\frac\Phi{k_2}\right)\right)-X.
\]
The chain rule gives
\[
\det DT_{r,k}\left(x,\nu x-\Phi/k_2\right)=-k_2 G'(x).
\]
At each sufficiently high root the first-cell argument gives \(G'(x)=kx h'(x)\) (since \(G=kx h\)) and \(h'(x)\ne0\); hence those preimages are regular.

**4. Inverse-location asymptotics.** Denote the unique root in cell \(j\) by \(x_j\) and its center by \(z_j\). The equation \(\cos(\pi\phi_j)=g(x_j)=O(x_j^{-1})\) puts \(\phi_j\) within \(O(x_j^{-1})\) of \(j+1/2\). Therefore \(x_j-z_j=O(z_j^{-1})\). Expanding
\[
\cos\bigl(\pi(j+1/2+\nu(x_j-z_j))\bigr)
=(-1)^{j+1}\pi\nu(x_j-z_j)+O(z_j^{-3})
\]
and
\[
g(x_j)=\frac{X-k_0}{kz_j}+O(z_j^{-3})+O(e^{-z_j/2})
\]
for sufficiently large \(j\), yields the claimed expansion, in fact with a remainder at most \(O(z_j^{-3})\) after absorbing the exponential, so the stated \(O(z_j^{-2})\) is conservative.

**5. Decoupled boundary.** At \(k=0\), the first component equals \(k_0+x^2e^{r-x}\). Its derivative is \(x(2-x)e^{r-x}\), which is positive for \(0<x<2\) and negative for \(x>2\). Thus the first coordinate is at most two-to-one on \(x>0\) with range \((k_0,k_0+4e^{r-2}]\). For each such \(x\), the prescribed second coordinate determines at most one \(\phi\). Requiring \(\phi>0\) can only reduce this count. This completes the proof.

## Verification

The included `verify.py` symbolically verifies the Jacobian/reduced-derivative identity and checks 558 remote preimages of the original two-variable map, generated across several positive and negative couplings, flux slopes, biases, recovery parameters, and signed targets. It checks residuals, positive-domain conditions, regular Jacobians, and the lattice-location expansion. Run `python verify.py` in an environment with Python, SciPy, and SymPy. The code tests finite cases; the root count and all-target assertions are established by the analytic argument above, not by sampling.

## Relationship to prior work

Kumar and Chandramouli introduced the same memristive reduced Chialvo map in arXiv:2605.00442v1 (public May 1, 2026). Their analyses concern equilibria, bifurcations, numerical attractors, and neuron networks; the full-text sections inspected do not give an inverse-fiber census, the zero-to-infinite valence transition, or the asymptotic preimage density. Han, Bi, Sun, Ren, and Xiong (2022) study a distinct memristor cosine map; its numerical dynamical analysis does not imply the present formula. General noninvertible-map theory recognizes critical curves and inverse multiplicities but does not itself supply these model-specific quantitative statements. This source comparison supports a provisional priority assessment only, not a comprehensive originality guarantee.

## Limitations

The theorem concerns inverse images of the *untruncated* planar map. Its large positive preimages may be far outside bounded physically meaningful regimes; the theorem does not assert their forward orbits remain in the positive quadrant. It does not establish any attractor, synchronization property, numerical robustness, or uniform behavior as \(k\to0\). Full historical priority requires independent scholarly review.

## References

- A. Kumar and V. V. M. S. Chandramouli, *Dynamical analysis of r-Chialvo neuron map with cosine memristive*, arXiv:2605.00442v1 (first posted 2026-05-01), https://arxiv.org/abs/2605.00442 .
- X. Han, X. Bi, B. Sun, L. Ren, and L. Xiong, *Dynamical Analysis of Two-Dimensional Memristor Cosine Map*, Frontiers in Physics 10 (2022), doi:10.3389/fphy.2022.911144, https://doi.org/10.3389/fphy.2022.911144 .
- *Noninvertible maps*, Scholarpedia, https://www.scholarpedia.org/article/Noninvertible_maps (background taxonomy; no model-specific claim).
