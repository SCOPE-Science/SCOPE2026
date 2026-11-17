# A logarithmic limiting law for dihedral angles of cycle graphical zonotopes

## Finding

For every integer \(n\ge4\), let \(e_{n+1}=e_1\) and consider the standard cycle graphical zonotope
\[
Z_n=\sum_{i=1}^{n}[0,e_i-e_{i+1}]\subset H_n,\qquad H_n=\{x\in\mathbb R^n:\sum_i x_i=0\},
\]
with the Euclidean metric inherited from \(\mathbb R^n\). It has dimension \(n-1\). An *interior ridge dihedral angle* is the angle between the two supporting facets containing a codimension-two face, measured on the side of the polytope.

**Exact angular multiset.** For each ordered triple of positive integers \((a,b,c)\) with \(a+b+c=n\), put
\[
\theta_{a,b,c}=\pi-\arccos\sqrt{\frac{ac}{(a+b)(b+c)}}.
\]
The complete ridge-angle multiset of \(Z_n\) has exactly \(2n\) copies of \(\theta_{a,b,c}\) for every such ordered triple (add multiplicities when different triples produce the same angle). Thus all angles are obtuse. Its total count is \(n(n-1)(n-2)\); this count itself is already contained in the known cycle-zonotope face polynomial [2] and is not claimed as new.

The unique minimum angle is
\[
\theta_{\min}=\pi-\arccos\frac1{n-1}
\]
with multiplicity \(2n\). Define \(p_n=\lfloor (n-1)^2/4\rfloor\). The unique maximum angle value is
\[
\theta_{\max}=\pi-\arccos\sqrt{\frac{p_n}{p_n+n}},
\]
with multiplicity \(2n\) for odd \(n\) and \(4n\) for even \(n\).

**Nondegenerate limiting angular law.** Let \(\Theta_n\) be the angle of a uniformly selected ridge, and put \(W_n=\cos^2\Theta_n\). Then \(W_n\) converges in distribution to a random variable \(W\in(0,1)\) whose cumulative distribution function is, for \(0<w<1\),
\[
\boxed{\Pr(W\le w)=\frac{2w\,(w-1-\log w)}{(1-w)^2}.}
\]
The cumulative distribution is \(0\) at and below \(0\), and \(1\) at and above \(1\). Moreover,
\[
\boxed{\lim_{n\to\infty}\mathbb E\cos^2\Theta_n=\mathbb EW=\frac{\pi^2}{3}-3.}
\]
Equivalently, \(\Theta_n\) converges to the obtuse angle \(\pi-\arccos\sqrt W\), which has a non-atomic, nondegenerate distribution.

## Assumptions and scope

The graph is the simple unweighted cycle on \(n\ge4\) vertices, and the generators are the **standard** root vectors \(e_i-e_{i+1}\). A global translation does not change the dihedral angles, but an arbitrary nonsimilarity affine deformation may change them. Ridges are counted as distinct faces, rather than distinct values of their angles. The assertion is confined to the intrinsic inherited-Euclidean metric and does not address arbitrary weighted cycles or general graphs. The limiting law is for uniform **face** sampling, not surface-area-weighted sampling or Gaussian random directions.

## Proof

**1. Face combinatorics.** A face exposed by a linear functional \(u\in H_n\) has free generators \([0,e_i-e_{i+1}]\) exactly at edges with \(u_i=u_{i+1}\); all other summands select an endpoint. For a face of dimension \(n-3\), its free-edge subgraph is a forest with \(n-3\) edges: precisely three cycle edges have been removed. The free edges form three nonempty consecutive path components, which are blocks \(A,B,C\) of sizes \(a,b,c>0\). The three deleted edges link the contracted blocks into a triangle. A functional exposing a ridge assigns three distinct block heights whose orientation around this triangle is acyclic. Conversely, every choice of three deleted edges and an acyclic orientation of the triangle exposes one ridge. The latter has six orientations; hence \(6\binom n3=n(n-1)(n-2)\) ridges. This recovers, rather than extends, the known face count of [2, Proposition 5.2].

**2. The two facets and their angle.** For a fixed ridge, name the low, middle and high blocks \(A,B,C\), respectively. Every facet of a cycle graphical zonotope corresponds to a nonempty proper cyclic interval, since its equality edges must have two connected components. The two facets containing the ridge have outward unit normals proportional to \(-v_A\) and \(v_C\), where \(v_S=\mathbf1_S-|S|\mathbf1/n\); this also follows directly because the contracted triangle's adjacent level coarsenings join the low and middle blocks, or the middle and high blocks. Since \(A\cap C=\varnothing\),
\[
\langle-v_A,v_C\rangle=\frac{ac}{n},\qquad
\|v_A\|^2=\frac{a(n-a)}n,\qquad
\|v_C\|^2=\frac{c(n-c)}n.
\]
Their exterior normal angle has cosine \(\sqrt{ac/((a+b)(b+c))}\); the interior dihedral angle is its supplement. This proves the stated \(\theta_{a,b,c}\) for every ridge.

**3. Multiplicities.** To encode a ridge, orient the cyclic order of the blocks and distinguish the block with middle height. For any fixed ordered positive composition \((a,b,c)\), the initial boundary can be placed at any of \(n\) cyclic edges, and there are two possible orders of the high and low heights. Thus each ordered composition contributes \(2n\) ridges. Equivalently, a triple of cut edges has three choices of middle block and two choices of which extreme is low. Summing over \(\binom{n-1}{2}\) positive compositions yields the prior-known total ridge count.

**4. Sharp extremes.** The squared exterior cosine is
\[
q^2=\frac{ac}{(n-a)(n-c)}=\frac{a}{n-a}\frac{c}{n-c}.
\]
It increases strictly with either \(a\) or \(c\) at fixed \(n\), and the minimum is attained exactly at \(a=c=1\). For a maximum, first decrease \(b\) to its smallest permitted value \(1\), then observe \(q^2=ac/(n+ac)\). Therefore \(a+c=n-1\) and the maximum is attained precisely by the balanced pair \(a,c\), with product \(p_n\). The number of maximizing ordered compositions is one if \(n\) is odd and two if \(n\) is even. Since \(\pi-\arccos q\) increases with \(q\), the extreme values and multiplicities follow.

**5. The continuous law.** By Step 3, \((a,b,c)\) is uniformly distributed over all positive integer compositions of \(n\) when a ridge is chosen uniformly. Thus \((a/n,b/n,c/n)\) converges to \((A,B,C)\), uniformly distributed on the open simplex \(A+B+C=1\), i.e. \(\operatorname{Dirichlet}(1,1,1)\). This is the elementary Riemann-sum limit over lattice points in a triangle. The continuous mapping theorem gives
\[
W_n\Longrightarrow W=\frac{AC}{(A+B)(B+C)}.
\]
Write \(U=A\), \(V=A+B\). The pair \((U,V)\) has density \(2\) on \(0<U<V<1\), as the order statistics of two independent uniforms. Then
\[
W=\frac{U(1-V)}{V(1-U)}.
\]
For \(0<w<1\), its sublevel set is precisely
\[
0<U\le\frac{wV}{1-(1-w)V},\qquad 0<V<1.
\]
Integrating the joint density gives
\[
\Pr(W\le w)=2\int_0^1\frac{wv}{1-(1-w)v}\,dv
=\frac{2w(-\log w-1+w)}{(1-w)^2}.
\]
Because \(0\le W_n\le1\), bounded-continuous convergence also yields convergence of expectations. Finally, using \(\int_0^v u/(1-u)\,du=-v-\log(1-v)\),
\[
\begin{aligned}
\mathbb EW&=2\int_0^1\frac{1-v}{v}\bigl[-v-\log(1-v)\bigr]dv\\
&=-1-2\left[\int_0^1\frac{\log(1-v)}v\,dv-\int_0^1\log(1-v)\,dv\right]\\
&=-1-2\left[-\frac{\pi^2}{6}+1\right]=\frac{\pi^2}{3}-3.
\end{aligned}
\]
The standard evaluation of the logarithmic integral follows by integrating the nonnegative series \(-\log(1-v)=\sum_{k\ge1}v^k/k\) termwise and evaluating \(\sum_{k\ge1}1/k^2=\pi^2/6\). This completes the proof.

## Verification

The standalone `verify_cycle_angles.py` requires only Python 3 and the standard library. For \(4\le n\le7\), it constructs the vertices independently from nonconstant cyclic edge orientations, enumerates all cyclic-interval facets, computes exact affine dimensions for every pairwise facet intersection, and compares the resulting rational squared outward-normal cosines with the composition formula, including extremal multiplicities. The exact exhaustive results were: at \(n=4,5,6,7\), the ridge counts are \(24,60,120,210\), respectively, with \(2,4,6,9\) different squared-cosine levels. The analytic argument, not these finite checks, establishes the all-dimensional and limiting claims.

## Relationship to prior work

Grujić [2, Proposition 5.2] already proves the complete face-count polynomial of this same cycle graphical zonotope, so neither the ridge count nor the three-cut face decomposition is claimed new. Padrol, Pilaud and Poullot [1, Section 1.3] give the standard graphical-zonotope normal-fan framework and connected-partition and orientation descriptions. Pešović and Stojadinović [3] study enumerators between graphical zonotopes and graph-associahedra; Poullot [4] studies their deformation cones. Those combinatorial and deformation descriptions do not state a Euclidean ridge-angle multiset or its limiting distribution. Existing work [5,6] analyzes other metric or spectral invariants of the same cycle graphical zonotope but not these angles. The proposed additional result is the **metric** composition-by-composition angular formula, sharp extremes, and explicit logarithmic limiting law with its exact second-cosine moment.

## Limitations

The claim does not address nonuniform sampling of ridges, weighted cycle generators, or other metric realizations. This is a mathematical proof with finite corroborating computations, not an independent or machine-formal certification. A differently named or unindexed prior calculation of the same angle distribution may exist; the available source comparisons do not logically certify global priority.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422v1 (first public 2021-11-24), Section 1.3; https://arxiv.org/html/2111.12422v2 .
2. V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931 (2016), Proposition 5.2; https://arxiv.org/html/1604.06931v2 .
3. M. Pešović, T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053 (first public 2022-09-24); https://arxiv.org/abs/2209.12053 .
4. G. Poullot, *Deformation cones of graphical zonotopes for \(K_4\)-free graph*, arXiv:2404.02669 (first public 2024-04-03); https://arxiv.org/abs/2404.02669 .
5. *Gaussian intrinsic-volume profiles for cycle graphical zonotopes*, published mathematical record, 2026; https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-gaussian-intrinsic-volume-profiles-for-cycle-graphical-zonotopes--3ae59b7ce98c/RESULT.md .
6. *Laplacian spectrum and spanning-tree complexity of cycle graphical zonotopes*, published mathematical record, 2026; https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-laplacian-spectrum-and-spanning-tree-complexity-of-cycle-graphic--8dfabf4d984d/RESULT.md .
