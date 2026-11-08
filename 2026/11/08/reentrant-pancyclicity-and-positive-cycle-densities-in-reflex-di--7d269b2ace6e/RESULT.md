# Reentrant pancyclicity and positive cycle densities in reflex directional nearest-neighbour graphs

## Finding

Fix the intensity-one stationary planar Poisson point process \(\mathcal P\). Put \(C_\alpha=\{r(\cos\vartheta,\sin\vartheta):r>0,\ |\vartheta|\le\alpha/2\}\) for \(0<\alpha<2\pi\), and set \(C_{2\pi}=\mathbb R^2\setminus\{0\}\). Draw a directed edge from every point \(x\in\mathcal P\) to its closest other point \(y\) with \(y-x\in C_\alpha\). All outgoing neighbors are almost surely unique. For each integer \(k\ge3\), let \(p_k(\alpha)\) be the Palm probability that the vertex at the origin lies on a directed simple \(k\)-cycle.

**Theorem (reentrant full cycle spectrum).** For every \(k\ge3\),
\[
p_k(\alpha)=0\quad(0<\alpha\le\pi\text{ or }\alpha=2\pi),
\qquad p_k(\alpha)>0\quad(\pi<\alpha<2\pi).
\]
Moreover \(p_k\) is continuous on \((0,2\pi]\), so its positive reflex-aperture values vanish at both boundaries. Write \(Q_R=[-R,R]^2\), let \(N_R\) count all points of \(\mathcal P\cap Q_R\), and let \(C_{k,\alpha}(R)\) count those on directed simple \(k\)-cycles in the *full-plane* graph. For every fixed \(\alpha\), almost surely
\[
\lim_{R\to\infty}\frac{C_{k,\alpha}(R)}{N_R}=p_k(\alpha).
\]
For every fixed \(k\ge3\) and every compact \(K\subset(\pi,2\pi)\), there is \(c_{k,K}>0\) such that, almost surely,
\[
\liminf_{R\to\infty}\inf_{\alpha\in K}\frac{C_{k,\alpha}(R)}{N_R}\ge c_{k,K}>0.
\]
The positive-density assertion can be realized simultaneously for *all* integer lengths and *all* reflex apertures, by taking a countable exhaustion by compact aperture intervals.

**Exact Palm integral.** With \(x_0=x_k=0\), for distinct \(x_1,\ldots,x_{k-1}\in\mathbb R^2\), let \(d_i=\|x_{i+1}-x_i\|\), and let \(A_\alpha(\boldsymbol x)\) be the indicator that every displacement \(x_{i+1}-x_i\) lies in \(C_\alpha\) and, within the finite set \(\{x_0,\ldots,x_{k-1}\}\), is the *strictly nearest* eligible successor of \(x_i\). Define the sector-disc union
\[
V_\alpha(\boldsymbol x)=\bigcup_{i=0}^{k-1}\Bigl\{z\in\mathbb R^2:\|z-x_i\|<d_i,\ z-x_i\in C_\alpha\Bigr\}.
\]
Then the exact (not asymptotic) formula is
\[
\boxed{\displaystyle p_k(\alpha)=\int_{(\mathbb R^2)^{k-1}}A_\alpha(\boldsymbol x)\exp\bigl(-|V_\alpha(\boldsymbol x)|\bigr)\,d\boldsymbol x.}
\]
The integral is finite, since it equals a probability; it counts each directed cycle through the Palm origin exactly once.

## Assumptions and scope

The Poisson process has intensity one on the *whole plane*, not a finite square with a truncated-edge convention. Sector rays use any fixed orientation; rotational invariance makes the probabilities aperture-dependent only. Endpoints of angular sectors are included, with no effect almost surely for a fixed aperture. The notation \(k\) always denotes an integer at least three. A directed simple \(k\)-cycle has distinct vertices \(x_0,\ldots,x_{k-1}\) and edges \(x_i\to x_{i+1\bmod k}\). Full-plane outgoing neighbors exist almost surely for each positive aperture. The ratio of counts is considered only for large \(R\) with \(N_R>0\), which eventually holds almost surely.

## Proof

**1. Exclusion at the endpoints.** When \(0<\alpha<\pi\), every allowed nonzero displacement has positive projection on the sector bisector, so the projection strictly increases around each directed edge and cycles are impossible. At \(\alpha=\pi\) the projection is nondecreasing; almost surely no two Poisson points have exactly equal projection, so it is strictly increasing on each actual edge. At \(\alpha=2\pi\), an outgoing edge to the globally nearest other point has nonincreasing length along any subsequent directed walk, because the previous point is an admissible competitor. When the walk does not immediately reverse, the edge length decreases strictly almost surely, since all relevant interpoint distances are distinct. A directed cycle of length at least three would give a strict circular chain of inequalities, which is impossible.

**2. A robust deterministic cycle for every reflex aperture and every length.** Fix \(\pi<a\le b<2\pi\), an integer \(k\ge3\), and put \(\delta=(a-\pi)/2>0\) and \(s=\min\{1,\tan\delta\}/8\). Use \(k\) points
\[
z_i=\bigl(is/(k-2),0\bigr)\quad(0\le i\le k-2),\qquad z_{k-1}=(-s,1).
\]
For every \(\alpha\in[a,b]\), the nearest eligible successors in this finite set are exactly
\[
z_0\to z_1\to\cdots\to z_{k-2}\to z_{k-1}\to z_0.
\]
Indeed, every forward horizontal edge has direction zero, whereas every reverse horizontal edge has angle \(\pi\), excluded for \(\alpha\le b<2\pi\). For \(z_{k-2}\to z_{k-1}\) the angle is \(\pi/2+\arctan(2s)\), strictly below \(a/2=\pi/2+\delta\) because \(2s\le\tan\delta/4\) if \(\delta\le\pi/4\), and otherwise \(2s=1/4<\tan\delta\). The closing edge from \(z_{k-1}\) to \(z_0\) has angle \(-\pi/2+\arctan(s)\), always eligible. Horizontal successors have strictly smaller distance than any farther eligible horizontal point and than \(z_{k-1}\); the final point sees \(z_0\) strictly closer than any other point of the horizontal chain. This yields strict distance and angular inequalities, which persist under sufficiently small perturbations of the points, **uniformly over the compact interval** \([a,b]\).

**3. Positive-density events.** Enclose the witness set in the interior of a square \(T\) of side \(L=10\) with distance greater than two from its boundary. Select \(\eta=\eta(k,a,b)>0\) so that the disjoint open balls \(B(z_i,\eta)\) remain in \(T\) and any choice of one point from each produces the same directed \(k\)-cycle for all \(\alpha\in[a,b]\), with all needed edges shorter than two. The Poisson event that there is exactly one point in each ball and no other point in \(T\) has probability
\[
q=e^{-L^2}(\pi\eta^2)^k>0.
\]
Because the selected vertices lie farther than two from the tile boundary, no point outside \(T\) can displace an internal successor. In a tiling by disjoint translates of \(T\), these events are independent Bernoulli events with probability \(q\). The strong law and \(N_R/(2R)^2\to1\) show that the proportion of points in \(k\)-cycles is asymptotically bounded below by \(kq/L^2\), simultaneously for all \(\alpha\in[a,b]\). For a general compact \(K\), choose \([a,b]\supset K\) inside the reflex interval, yielding \(c_{k,K}=kq/100\). Exhaust the reflex interval by rational compact intervals, and intersect the probability-one events across the countably many lengths and intervals.

**4. Exact limiting fraction.** For each fixed \(\alpha\), the mark identifying whether a Poisson point lies on a directed \(k\)-cycle is measurable and translation-covariant. The stationary Poisson point process is ergodic, so the point-process ergodic theorem gives convergence of the count divided by area to its Palm expectation \(p_k(\alpha)\). Since the point density tends to one, the ratio to \(N_R\) converges as stated.

**5. Continuity.** Under the Palm law, fix any \(\alpha_0\in(0,2\pi)\). Every finite forward orbit through at most \(k\) steps has unique finite outgoing neighbors. The outgoing decision at each inspected point is stable when \(\alpha\) varies sufficiently little: the winning distance is finite; only finitely many Poisson points lie in a slightly larger disk; and almost surely none of these points lies exactly on either angular boundary at \(\alpha_0\). Hence the event that the root lies on a \(k\)-cycle is locally constant in aperture for almost every configuration. The same argument holds at the endpoint \(2\pi\), where every finite inspected nearest-neighbor edge is admitted for all sufficiently wide apertures. Dominated convergence establishes continuity of \(p_k\), including at \(\pi\) and at \(2\pi\).

**6. Exact integral.** Under the Palm law at zero, apply the multivariate Campbell-Mecke formula to ordered distinct \((k-1)\)-tuples of the remaining Poisson points. The finite-set indicator \(A_\alpha\) enforces the desired successors against the points of the candidate cycle; the extra points of the Poisson process must avoid the union \(V_\alpha\) of distance-preempting sector-discs. Poisson void probability gives \(\exp(-|V_\alpha|)\). Every directed cycle containing zero generates precisely one tuple in forward order, so integration yields \(p_k\) without a factorial factor.

## Verification

The accompanying standalone \(\texttt{checker.py}\) checks the strict witness cycle against **all possible competitors** among the constructed vertices for multiple reflex apertures approaching both phase boundaries and lengths up to fifty; it also checks perturbation stability and absence of cycles longer than two in fully unconstrained generic finite samples. These finite checks validate the geometric ingredients but do not substitute for the infinite-Poisson void, ergodicity, and continuity arguments. The proof uses only standard Poisson, probability, and elementary geometric facts.

## Relationship to prior work

Georgiou, Tawhari and Wade [1] define directional nearest-neighbor graphs and prove limit theorems for total edge length only for sectors narrower than a half-plane. Their Section 1.4 specifically singles out reflex sectors as unexplored and expects new phenomena; their stated results do **not** quantify directed cycle-length spectra. Eppstein, Paterson and Yao [2] prove that ordinary unrestricted nearest-neighbor graphs admit only directed two-cycles (their Section 2); this agrees with, but does not imply, the interior reflex behavior. Earlier work on nearest-neighbor *pairs* and a distinct prior study of reciprocity in reflex sectors concerns directed cycles of length exactly two, not the all-length phenomenon and its positive spatial densities. The present theorem is not an extension of the published edge-length CLT to reflex sectors.

## Limitations

The theorem establishes positivity but not a closed scalar evaluation or sharp near-boundary asymptotic for \(p_k(\alpha)\). It concerns homogeneous planar Poisson input and one common orientation of the angular sector. The displayed integral is explicit but high-dimensional. The exact values of the exponential lower bounds from tiles are typically extremely small and are not claimed sharp. The comparison to directional and unrestricted nearest-neighbor literature is not an exhaustive historical-priority certification; related older geometric-proximity results may exist beyond the material inspected.

## References

[1] N. Georgiou, Q. M. Tawhari, A. Wade, *Gaussian and non-Gaussian limits for the total edge-length of random directional nearest-neighbour graphs*, arXiv:2610.40140v1, first posted 2026-10-29, https://arxiv.org/html/2610.40140v1. See Definitions 1.1–1.3 and Section 1.4 (reflex cones).

[2] D. Eppstein, M. S. Paterson, F. F. Yao, *On Nearest-Neighbor Graphs*, Discrete & Computational Geometry 17 (1997), 263–282, https://doi.org/10.1007/PL00009293. Author-hosted full text https://www.ics.uci.edu/~eppstein/pubs/EppPatYao-DCG-97.pdf; Section 2 explicitly rules out cycles longer than two in ordinary nearest-neighbor graphs.

[3] Standard Poisson Campbell-Mecke formula, Poisson void probabilities, and spatial ergodic theorem for translation-covariant point marks; all are applied with their hypotheses stated in the proof.
