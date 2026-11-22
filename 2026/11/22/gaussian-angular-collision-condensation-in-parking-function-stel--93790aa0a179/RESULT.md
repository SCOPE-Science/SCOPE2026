# Gaussian angular-collision condensation in parking-function stellohedra

## Finding
For each integer \(n\ge2\), let \(\mathbf b=(b_1,\ldots,b_n)\) have positive integral entries with \(b_1\ge2\), let \(s_j=\sum_{i=1}^{j}b_i\), and let \(P_n(\mathbf b)\subset\mathbb R^n\) be the convex hull of positive integral vectors whose sorted entries \(a_{(j)}\) satisfy \(a_{(j)}\le s_j\). Equip \(\mathbb R^n\) with its standard Euclidean metric. Write \(p_v\) for the spherical Gaussian normal-cone mass of vertex \(v\), equivalently the probability that an independent standard Gaussian linear objective exposes \(v\).

Every vertex arises from a permutation of \((1^k,s_{k+1},\ldots,s_n)\), for a unique \(0\le k\le n\). Here \(1^k\) means \(k\) entries equal to one; there are \(n!/k!\) such vertices. Every vertex in layer \(k\) has the **parameter-independent** angle
\[
p_{n,k}=\frac{1}{2^n(n-k)!}.
\]
Consequently, if two independent isotropic Gaussian objectives expose vertices \(V,V'\), then their exact coincidence probability is
\[
\boxed{C_n:=\mathbb P(V=V')=4^{-n}L_n(-1)},\qquad
L_n(-1)=\sum_{j=0}^n\frac{\binom nj}{j!},
\]
and
\[
\boxed{C_n\sim\frac{e^{-1/2}}{2\sqrt\pi}\,n^{-1/4}e^{2\sqrt n}4^{-n}}.
\]
Conditional on coincidence, let \(J_n\) be the number of coordinates of the common vertex not equal to one. Then
\[
\mathbb P(J_n=j\mid V=V')=\frac{\binom nj/j!}{L_n(-1)}\quad(0\le j\le n),
\qquad
\boxed{\frac{J_n-\sqrt n}{n^{1/4}}\ \Longrightarrow\ N(0,1/2)}.
\]
By comparison, an ordinarily exposed vertex has \(J_n\sim\operatorname{Bin}(n,1/2)\). Thus conditioning two independent directions to expose the same vertex shifts the active-coordinate count from order \(n\) to order \(\sqrt n\).

The canonical star-graph associahedron \(Q_n\), formed as the Minkowski sum of all unit simplices of nonempty connected induced subsets of the star with \(n\) leaves, in its coordinate-sum hyperplane in \(\mathbb R^{n+1}\), is combinatorially equivalent to \(P_n(\mathbf b)\). Nevertheless its corresponding isotropic Gaussian collision probability is
\[
C_n^\star=\frac{n!}{((n+1)!)^2}\sum_{j=0}^n j!\sim(n+1)^{-2},
\]
so the sharp realization-sensitive gap is
\[
\boxed{\frac{C_n}{C_n^\star}\sim\frac{e^{-1/2}}{2\sqrt\pi}\,n^{7/4}e^{2\sqrt n}4^{-n}}.
\]
For the boundary case \(b_1=1\), layers zero and one merge. Its collision probability becomes exactly \(4^{-n}(L_n(-1)+2n/n!)\); the displayed leading asymptotic still holds, although this boundary family need not have the same stellohedral combinatorial type.

## Assumptions and scope
All Gaussian directions are standard isotropic in the **ambient** Euclidean space of the realization specified, rather than carried through a nonorthogonal affine equivalence. For \(P_n(\mathbf b)\), \(b_1\ge2\) unless the boundary formula explicitly says \(b_1=1\); the other entries may vary freely with \(n\) but are positive. The angles are normalized to sum to one. The asymptotics hold for arbitrary such sequences of parameter vectors. \(L_n\) is the usual degree-\(n\) Laguerre polynomial, with the finite sum above serving as its definition at \(-1\). The contrast compares two different canonical Euclidean realizations of one combinatorial type, not the same polytope under orthogonal motion.

## Proof
**1. Vertex layers and exposure cones.** The vertices of a generalized parking-function polytope are precisely permutations of \(v_k=(1^k,s_{k+1},\ldots,s_n)\), \(0\le k\le n\). This antecedent vertex description is proved in the cited work of Bayer and collaborators; it is also explicit for the two-parameter subfamily in Hanada–Lentfer–Vindas-Meléndez. When \(b_1\ge2\), all layers are disjoint and the entries \(s_j\) are strictly increasing. Given distinct nonzero objective coordinates \(g_{(1)}<\cdots<g_{(n)}\), rearrangement uniquely assigns the \(k\) unit entries to the lowest \(k\) objective coordinates and the increasing larger entries to the remaining objectives in increasing order. The corresponding support scores satisfy
\[
\langle g,v_{k+1}\rangle-\langle g,v_k\rangle=(1-s_{k+1})g_{(k+1)}.
\]
Since \(s_{k+1}>1\), the optimum is exactly \(k=\#\{i:g_i<0\}\). Thus a given exposed vertex is specified by its set of \(k\) negative objective coordinates and the relative ordering of its \(n-k\) positive coordinates. Independent centered Gaussian signs and the independent uniform order of positive magnitudes give \(p_{n,k}=2^{-n}/(n-k)!\). There are \(n!/k!\) distinct vertices in that layer. In particular \(\sum_k(n!/k!)p_{n,k}=2^{-n}\sum_k\binom nk=1\).

**2. Exact angular coincidence and conditioning.** Independence of two exposing directions gives \(\mathbb P(V=V')=\sum_v p_v^2\). On setting \(j=n-k\), substitution yields
\[
\sum_{k=0}^n\frac{n!}{k!}\frac{1}{4^n((n-k)!)^2}
=4^{-n}\sum_{j=0}^n\frac{\binom nj}{j!}.
\]
The probability of a collision in layer \(j\) is the corresponding summand, proving the conditional law. For one exposing direction, the number of positive objective coordinates is \(\operatorname{Bin}(n,1/2)\), hence the unconditional law of \(J_n\).

**3. The Laguerre asymptotic and conditional central limit.** Introduce \(c_{n,j}=n^j/(j!)^2\) for \(j\ge0\), and \(r_{n,j}=(n)_j/n^j\) for \(j\le n\) (zero otherwise). Then \(L_n(-1)=\sum_{j\ge0}c_{n,j}r_{n,j}\) and \(0\le r_{n,j}\le1\). The ratio \(c_{n,j+1}/c_{n,j}=n/(j+1)^2\) is strictly decreasing. Stirling expansion uniformly on \(j=\sqrt n+u n^{1/4}\) with bounded \(u\) gives
\[
\log c_{n,j}=2\sqrt n-\log(2\pi\sqrt n)-u^2+o(1).
\]
The monotone ratios bound the two tails by exponentially decaying Gaussian tails on that scale; they also control the outer region where \(j/\sqrt n\) is bounded away from one. Riemann summation therefore yields
\[
\sum_{j\ge0}c_{n,j}\sim\frac{e^{2\sqrt n}}{2\sqrt\pi\,n^{1/4}},
\quad\frac{j-\sqrt n}{n^{1/4}}\Longrightarrow N(0,1/2)
\]
under the probability law proportional to \(c_{n,j}\). Moreover, on every such central window,
\[
\log r_{n,j}=\sum_{i=0}^{j-1}\log(1-i/n)
=-\frac{j(j-1)}{2n}+O(j^3/n^2)=-\frac12+o(1).
\]
As \(r_{n,j}\) is bounded by one, its expectation under the \(c\)-weighted law converges to \(e^{-1/2}\); the normalized \(c r\)-weighted and \(c\)-weighted laws have total variation distance tending to zero. This proves both the sharp Laguerre constant and the collision-conditioned Gaussian limit. Equivalently the sum of \(c_{n,j}\) is the modified Bessel function \(I_0(2\sqrt n)\); the elementary ratio/Laplace argument above does not require taking its asymptotics on trust.

**4. The star realization and the metric gap.** For the standard simplex-sum star associahedron, a generic objective in the coordinate-sum hyperplane has the same coordinate ordering as \(n+1\) independent Gaussian scores (subtracting the mean does not change ranks). Its exposed vertex is determined by the ordered list of the \(k\) leaves whose scores lie above the hub. Each fixed list occurs for \((n-k)!\) of the \((n+1)!\) full orders; there are \(n!/(n-k)!\) such lists. This establishes its exact angles and the displayed sum for \(C_n^\star\). Since \(\sum_{j=0}^n j!/n!=1+O(1/n)\), we have \(C_n^\star\sim(n+1)^{-2}\). The cited stellohedron identification establishes combinatorial equivalence. Combining with Step 3 proves the ratio.

**5. Boundary at \(b_1=1\).** The base vertices for \(k=0\) and \(k=1\) coincide, while all other layers remain distinct. For each such common vertex, its angle is the sum of the disjoint events having no negative coordinate, with its positive scores in the specified order, and having exactly its unit-coordinate negative, with the remaining positive scores so ordered. Thus the two former angles \(2^{-n}/n!\) and \(2^{-n}/(n-1)!\) merge. The sum of their squared masses increases by \(2n/(4^n n!)\), giving the boundary formula. It is exponentially negligible relative to the main Laguerre term.

## Verification
The companion standalone `checker.py` enumerates, for each \(n=2,3,4,5\) and four distinct parameter vectors, every independent sign configuration and every ordering of distinct objective magnitudes. It directly maximizes over all distinct parking-polytope vertices, checks that each resulting angle equals the formula, and checks the exact collision sum by rational arithmetic. Thus 16 full family cases (including the merged \(b_1=1\) boundary) were exhaustively checked at the chamber level. Exact-arithmetic Laguerre weights and their collision-conditioned first two moments were evaluated for \(n=10,25,50,100,400,1600\), with the derived asymptotic constants checked at larger orders. These computations are finite diagnostics; Steps 1–5 are the proof for unbounded \(n\).

## Relationship to prior work
The generalized parking-function vertex description, its stellohedral combinatorial type, and normal-fan descriptions are antecedents, not claimed here as original. Hanada–Lentfer–Vindas-Meléndez analyze the initial two-parameter polytope family; Bayer and collaborators derive its full general vertex and normal structure; Liu–Thawinrak extend normal-fan descriptions to a wider family. Their results imply that the simple cone patterns can be reconstructed, so **neither the fan itself nor its chamber-counting method is a novelty claim**. Published work on the classical parking polytope also supplies a binomial exposed-vertex layer law. Separately, the Gaussian collision spectrum of the standard simplex-sum star associahedron has been studied. The present contribution is the new **collision-conditioned square-root-rank Gaussian law**, its exact Laguerre normalization and sharp constant uniformly across arbitrary parking parameters, and the quantified exponentially different angular collision behavior of two combinatorially equivalent canonical Euclidean stellohedra. Prior independent normal-fan descriptions do not by themselves state or establish that limit or this cross-realization comparison.

## Limitations
The result concerns isotropic Gaussian exposure of vertices, not uniformly sampled vertices, volume measure, or affine-invariant quantities. The conditional limit holds for coincident vertices exposed by two **independent** directions and should not be interpreted as an ordinary rank law. The two stellohedral models have distinct induced Euclidean metrics under their nonorthogonal identifications; the result does not assert a difference between combinatorial types. Exact angular spectra can be mechanically deduced from previously known normal fans; the principal originality claim is restricted to the sharp collision and conditional limit, and its geometric comparison. Historical priority remains subject to an unindexed equivalent or an overlooked metric computation. No independent mathematical audit has been performed.

## References
1. M. Hanada, J. Lentfer, and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885 (first public 2022-12-13), https://arxiv.org/abs/2212.06885.
2. M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387 (first public 2024-03-12), Theorem 2.3 and Corollary 3.14, https://arxiv.org/abs/2403.07387.
3. F. Liu and W. Thawinrak, *Parking Function Polytopes*, arXiv:2512.14199 (first public 2025-12-16), Sections 5–7, https://arxiv.org/abs/2512.14199.
4. M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053 (first public 2022-09-24), https://arxiv.org/abs/2209.12053.
5. *Two critical Rényi windows in the angular spectra of star-graph polytopes*, publicly available result, 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-two-critical-r-nyi-windows-in-the-angular-spectra-of-star-graph--e1b409771cb8.
6. *Gaussian width fluctuations of classical parking-function polytopes and their exposed vertex layers*, publicly available result, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-gaussian-width-fluctuations-of-classical-parking-function-polyto--f22c06d75d0e.
