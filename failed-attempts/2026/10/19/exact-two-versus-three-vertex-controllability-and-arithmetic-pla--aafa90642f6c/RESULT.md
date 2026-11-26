# Exact two-versus-three vertex controllability and arithmetic placements on weighted wheels

## Finding
Let \(m\ge4\) and let \(W_m=K_1\vee C_m\) have rim vertices \(0,\ldots,m-1\) and hub \(\star\). Assign conductance \(a>0\) to every rim edge and \(b>0\) to every spoke. For the full-state system \(\dot x=-Lx+B_Su\), each column of \(B_S\) is the standard unit vector at one selected vertex. Define \(\mu_j=2-2\cos(2\pi j/m)\) and the set of interior resonances
\[
\mathcal R_m=\left\{\frac{m}{\mu_j}:1\le j<m/2\right\}.
\]
The minimum possible number of selected vertices is exactly
\[
\gamma(W_m;a,b)=\begin{cases}3,&a/b\in\mathcal R_m,\\2,&a/b\notin\mathcal R_m.\end{cases}
\]
At an interior resonance the hub and two adjacent rim vertices are an optimal three-input set; otherwise two adjacent rim vertices are optimal.

For \(a/b\notin\mathcal R_m\), **all** minimum two-input placements are the following pairs of rim vertices \(\{r,r+t\}\), with \(1\le t<m\), modulo rim indices:

- For odd \(m\), exactly those with \(\gcd(t,m)=1\).
- For even \(m\), when \(a/b\ne m/4\), exactly those with \(\gcd(t,m/2)=1\).
- For even \(m\), when \(a/b=m/4\), exactly those with \(\gcd(t,m)=1\).

There are respectively \(m\varphi(m)/2\), \(m\varphi(m/2)\), and \(m\varphi(m)/2\) unordered optimal pairs in these three cases. At an interior resonance there are no controllable pairs. For each odd prime \(m\ge5\), at every interior resonance **every** three distinct vertices, including those involving the hub, form a controllable optimal set; the number of optimal three-sets is consequently \(\binom{m+1}{3}\).

## Assumptions and scope
The graph is undirected; spoke and rim conductances are each strictly positive and uniform within their respective edge orbits. A separate independent scalar actuator is attached to each selected vertex; this is controllability of the whole state, not controllability of only the follower subnetwork, not zero-forcing, and not generic structural controllability under arbitrary edge weights. The hub is counted as one vertex. The graph family begins at \(m=4\), avoiding the distinct triangle/complete-graph normalization. Ratios \(a/b\) are exact real parameters. The boundary \(a/b=m/4\) is meaningful only for even \(m\).

## Proof
**Spectral decomposition.** In the orthogonal direct sum of the constant vector, the vector \(v_\star=(-m,1,\ldots,1)\) (hub first), and the rim Fourier characters of nonzero frequency, the weighted Laplacian has eigenvalues \(0\), \((m+1)b\), and
\[
\lambda_j=b+a\mu_j,\qquad 1\le j\le\lfloor m/2\rfloor.
\]
For \(1\le j<m/2\), the \(\lambda_j\)-eigenspace has real basis with hub coordinate zero and rim coordinates \(\cos(2\pi jr/m)\) and \(\sin(2\pi jr/m)\). If \(m\) is even, the remaining \(j=m/2\) space has dimension one with rim coordinate \((-1)^r\). The values \(\mu_j\) strictly increase over the listed range, so the **only** possible eigenvalue collision is \(\lambda_j=(m+1)b\), equivalent to \(a\mu_j=mb\). An interior collision creates one eigenspace of dimension three; an antipodal collision, only possible for even \(m\) at \(a/b=m/4\), creates a dimension-two space.

**Input lower bounds.** The Popov–Belevitch–Hautus criterion for symmetric \(L\) says full controllability holds precisely when restriction of each real Laplacian eigenspace to the chosen input vertices is injective. At least two inputs are needed, because \(j=1\) gives a two-dimensional eigenspace unless its collision makes the dimension larger. At every interior collision the merged eigenspace is three-dimensional, hence at least three inputs are necessary.

**Sufficiency.** For adjacent rim inputs \(0,1\), every unmerged interior Fourier eigenspace restricts to the matrix
\[
\begin{pmatrix}1&0\\ \cos(2\pi j/m)&\sin(2\pi j/m)\end{pmatrix},
\]
which is nonsingular since \(0<2\pi j/m<\pi\). The constant, hub-versus-rim, and any separate alternating one-dimensional eigenspaces have nonzero restrictions. At the antipodal collision the fused two-dimensional space restricts to the two rim rows of the constant-on-rim vector and the alternating vector, producing \(\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)\), also nonsingular. Thus adjacent rim inputs attain the lower bound whenever no interior collision occurs. At an interior collision take \(\{\star,0,1\}\). The hub entry of \(v_\star\) equals \(-m\), while Fourier vectors vanish at the hub; the two adjacent rim rows have the previously computed nonsingular Fourier determinant. All other eigenspaces likewise restrict injectively. Hence three inputs suffice.

**Every two-input placement.** No two-input set containing the hub controls a two-dimensional rim Fourier mode because the hub coordinate is zero on both basis vectors. Thus a feasible pair must lie on the rim. For a pair at circular separation \(t\), the determinant on interior mode \(j\) equals \(\sin(2\pi jt/m)\). If \(m\) is odd, it vanishes for an interior \(j\) precisely when \(\gcd(t,m)>1\): since \(m\mid 2jt\) and \(m\) is odd, \(m\mid jt\); a proper divisor produces an eligible interior frequency. If \(m=2q\), vanishing occurs precisely when \(q\mid jt\), for some \(1\le j<q\), equivalently \(\gcd(t,q)>1\). The antipodal collision adds independent constant-on-rim and alternating restrictions precisely when \(t\) is odd. For even \(m\), these conditions jointly amount to \(\gcd(t,m)=1\). With no collision or only the antipodal collision, these Fourier tests cover every eigenspace. Counting eligible ordered separations and dividing by two gives the three stated totient formulas.

**Prime-order universal triples.** Suppose \(m\ge5\) is an odd prime and an interior collision occurs at frequency \(j\). For any three distinct rim vertices, the merged eigenspace restricts via columns \((1,\cos\theta_r,\sin\theta_r)\), and three distinct points on the unit circle cannot be collinear; the determinant is nonzero. For a triple consisting of the hub and two distinct rim vertices, the hub distinguishes the radial column, while \(\sin(2\pi jt/m)\ne0\) for their nonzero separation \(t\) by primality. All other Fourier eigenspaces restrict injectively because the prime-order two-point Fourier determinants never vanish. Thus every three-set controls, and three inputs are necessary by the fused dimension.

## Verification
The standalone `verify.py` constructs full weighted Laplacian matrices independently of the Fourier formulas, groups numerically recovered eigenspaces, checks the PBH criterion for **every** two-vertex choice for every \(4\le m\le18\) at generic positive ratios and at each exact spectral-collision ratio, and independently checks exact rational Kalman ranks in selected small instances. It enumerates all three-vertex choices at every interior resonance for prime \(m\in\{5,7,11\}\). Run `python verify.py` after installing the two dependencies listed in `requirements.txt`; the successful package check prints `VERIFY_OK 12705 checks`. These are finite corroborations only. The all-order assertions and exact count rely on the proof above.

## Relationship to prior work
The path-and-cycle controllability work of Parlangeli and Notarstefano supplies the classical motivation and cycle-frequency background. Rahmani–Ji–Mesbahi–Egerstedt study symmetry obstructions for multiagent network control. Hsu studies interconnections and minimum control on threshold graphs; those classes do not furnish this weighted wheel position classification. Yang and collaborators study Laplacian controllability of non-simple ring graphs without the same universal hub; this does not determine collision with the hub-versus-rim mode. The exact formula here isolates **spoke/rim spectral resonance** and gives all minimum vertex placements, including the antipodal arithmetic exception. A published general PBH or spectral multiplicity theorem alone does not yield the arithmetic input placement classification without checking every eigenspace restriction.

## Limitations
Weights must remain uniform within rim and spoke orbits and strictly positive. At an interior resonance for composite \(m\), the theorem gives a sufficient optimal triple, not an enumeration of every optimal triple. For odd primes, every triple is characterized. No claim is made for general weighted wheels with heterogeneous individual conductances, other graph joins, energy optimality, robustness to parameter perturbations, or zero-forcing. Completeness of indexing of all past wheel-controllability literature is not proved; potentially equivalent variants might be written in representation-theoretic or leader-selection terminology. Independent review has not been performed.

## References
1. S. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1 (first posted 2011-09-16), https://arxiv.org/abs/1109.3556.
2. A. Rahmani, M. Ji, M. Mesbahi, M. Egerstedt, *Controllability of Multi-Agent Systems from a Graph-Theoretic Perspective*, SIAM J. Control Optim. 48 (2009), 162–186, https://doi.org/10.1137/060674909.
3. S.-P. Hsu, *Laplacian Controllability of Interconnected Graphs*, arXiv:1808.03022 (2018), https://arxiv.org/abs/1808.03022.
4. S.-P. Hsu, *Minimal Laplacian controllability problems of threshold graphs*, IET Control Theory Appl. 13 (2019), 1639–1645, https://doi.org/10.1049/iet-cta.2018.5875.
5. *Laplacian Controllability of a Class of Non-Simple Ring Graphs*, IFAC World Congress 2020 paper, https://ifatwww.et.uni-magdeburg.de/ifac2020/media/pdfs/2047.pdf.
