# Exact mean-zero Sobolev evaluation and the finite quadratic envelope of metric cactus graphs

## Finding

Let \(G\) be a finite connected **simple cactus graph**, with every edge realized as an interval of arbitrary strictly positive length and with unweighted arclength \(ds\). A cactus means that every edge belongs to at most one simple cycle. Put \(T=\int_G ds>0\) and
\[
\mathcal H(G)=\{f\in C(G;\mathbb R):f|_e\in H^1(e),\ \int_G f\,ds=0\},\qquad E(f)=\int_G|f'|^2\,ds.
\]
The sharp squared endpoint constant is
\[
K(G)=\sup_{0\ne f\in\mathcal H(G)}\frac{\|f\|_\infty^2}{E(f)}.
\]
The theorem below gives an exact finite blockwise rational formula for \(K(G)\) when the edge lengths are rational, and a finite formula in arithmetic operations for arbitrary real edge lengths. It also completely locates the maximizing evaluation points.

Partition the edges of \(G\) into its blocks: each bridge edge is one block, and each simple cycle is another block. For every block \(B\), delete its **open** edges. For a vertex \(v\) of \(B\), let \(m_{B,v}\) be the total arclength of the exterior component attached to \(B\) at \(v\); it is zero if no exterior edges attach there. In a cactus, distinct exterior components meet \(B\) at distinct vertices. Define a measure on \(B\) by
\[
\nu_B=ds|_B+\sum_{v\in V(B)}m_{B,v}\delta_v.
\]
For a bridge block of length \(b\), use coordinate \(s\in[0,b]\), endpoint masses \(m_0,m_1\), and resistance kernel \(r_B(s,t)=|s-t|\). Define
\[
\Phi_B(s)=\frac{s^2+(b-s)^2}{2}+m_0s+m_1(b-s),\quad
J_B=\frac{b^3}{3}+b^2(m_0+m_1)+2bm_0m_1.
\]
For a cycle block of circumference \(\ell\), use clockwise coordinates \(s\pmod\ell\), attachment positions \(a_j\) with corresponding positive masses \(m_j\), and put
\[
\rho_\ell(t)=\frac{u(\ell-u)}\ell,\qquad u=t\pmod\ell\in[0,\ell),
\]
\[
\Phi_B(s)=\frac{\ell^2}{6}+\sum_jm_j\rho_\ell(s-a_j),\quad
J_B=\frac{\ell^3}{6}+\frac{\ell^2}{3}\sum_jm_j
+2\sum_{i<j}m_im_j\rho_\ell(a_i-a_j).
\]
For each \(x\in G\) and each block \(B\), define \(\pi_B(x)\) as follows: it equals \(x\) when \(x\in B\); otherwise it is the unique vertex where the block-tree path from \(x\) first meets \(B\). Set
\[
F(x)=\sum_B\Phi_B(\pi_B(x)),\qquad J=\sum_BJ_B.
\]
Then the **exact sharp norm** and its centered Green representers are
\[
\boxed{K(G)=\frac{\max_{x\in G}F(x)}{T}-\frac{J}{2T^2}},
\qquad
\boxed{g_x(y)=\frac{F(x)+F(y)}{2T}-\frac{J}{2T^2}-\frac{R_G(x,y)}2}.
\]
Here \(R_G(x,y)\) is ordinary electrical effective resistance when edge lengths are resistances. For any fixed maximizing point \(x\), all nonzero functions attaining equality with maximum at \(x\) are precisely the nonzero real scalar multiples of \(g_x\).

The maximum requires only finitely many candidates. Unless \(G\) is a single cycle, **no cut vertex, no interior bridge point, and no noncut degree-two vertex on a bridge can maximize**. The only possibilities are (i) degree-one vertices and (ii) stationary points strictly between successive attachment vertices of cycle blocks. On each such attachment-free open arc there is **at most one** stationary point, and it is a strict local maximum of \(F\) along its cycle. If \(G\) is a single cycle, every point maximizes and \(K(G)=T/12\). Thus the norming set is finite for every other cactus.

There is an explicit formula for the cycle candidates. On a cycle \(B\) with total exterior mass \(M_B=\sum_jm_j>0\), lift a consecutive pair of positive-mass attachment positions to real coordinates \(a<b\) with \(b-a\le\ell\), put \(z=(a+b)/2\), and write
\[
D_B(z)=\sum_jm_j\left(1-\frac{2((z-a_j)\bmod\ell)}\ell\right),\qquad
s_{B,(a,b)}=z+\frac{\ell D_B(z)}{2M_B}.
\]
Include \(s_{B,(a,b)}\) as a candidate if and only if \(a<s_{B,(a,b)}<b\), modulo \(\ell\). Evaluate \(F\) at those cycle candidates and at all degree-one vertices, and take the maximum. No limit or continuous optimization remains.

**Non-antipodal phenomenon.** Take a central circle of length \(10\); attach a circle of length \(2\) at central coordinate \(0\) and another circle of length \(3\) at coordinate \(1\). Then \(T=15\). The unique maximizing point belongs to the central circle at coordinate \(28/5\), neither an antipode of an attachment point nor the midpoint of the larger attachment-to-attachment arc. The exact sharp constant is
\[
\boxed{K(G)=\frac{1777}{1500}}.
\]
The total integrated resistance is \(J=4033/10\); the maximum integrated resistance is \(F(28/5)=2341/75\). This example separates the general theorem from the previously solved single-anchor rose and two-loop bridge geometries, whose norming points are loop antipodes.

## Assumptions and scope

The graph is finite, connected, simple, and has at least one edge; loops and parallel combinatorial edges are not needed because subdividing cycles allows arbitrary lengths and multiple distinct attachments. Edge lengths may be arbitrary real positive numbers. Arclength is unweighted, vertices have zero mass, functions are real, continuous at junctions and edgewise \(H^1\), and the only constraint is zero global arclength mean. The norm is the supremum over all geometric points, not merely graph vertices. Kirchhoff matching is a property of the extremizing Green functions, not an additional constraint on arbitrary functions.

The two block types have disjoint open edge sets, and the block-incidence graph is a tree. The exterior component of a block attached at a particular block vertex contains all edges reached without traversing the open edges of that block. In particular, its arclength excludes the block itself. On the case of an individual bridge between two endpoints with no exterior mass, the formula gives \(K=b/3\). On an isolated circle, it gives \(K=\ell/12\).

## Proof

**1. The centered Green/effective-resistance identity.** The seminorm \(E\) is a Hilbert norm on \(\mathcal H(G)\). Continuous point evaluation is bounded by one-dimensional Sobolev estimates along finite paths and the mean-zero constraint. Let \(g_x\) denote its energy Riesz representer. Its centered Green kernel \(G(x,y)=g_x(y)\) is symmetric, has zero integral in either variable and satisfies the variational equation \(E(g_x,f)=f(x)\) for all \(f\in\mathcal H(G)\). The effective resistance is the squared energy-dual norm of a difference of evaluations, so
\[
R_G(x,y)=G(x,x)+G(y,y)-2G(x,y).
\]
Integrate once in \(y\), then twice in \(x,y\). If \(F_*(x)=\int_G R_G(x,y)\,dy\) and \(J_*=\int_G\int_G R_G(y,z)\,dy\,dz\), the zero-mean condition yields
\[
G(x,x)=\frac{F_*(x)}T-\frac{J_*}{2T^2},\qquad
G(x,y)=\frac{F_*(x)+F_*(y)}{2T}-\frac{J_*}{2T^2}-\frac{R_G(x,y)}2.
\]
Cauchy–Schwarz now proves the sharp embedding and equality functions, provided the claimed finite formula really computes \(F_*\) and \(J_*\).

**2. Orthogonal resistance addition across cactus blocks.** In an electrical network joined to another network at one vertex, effective resistance between points in different components is the sum of their resistances to the common vertex. Every cactus block is a bridge or a single circle; the unique block-tree path between two points visits each block at most once. Repeated cut-vertex decomposition therefore proves, for all \(x,y\in G\),
\[
R_G(x,y)=\sum_B r_B(\pi_B(x),\pi_B(y)).
\]
The resistance in a bridge interval is \(|s-t|\). On a circle there are two parallel arcs of lengths \(u\) and \(\ell-u\), so resistance is \(u(\ell-u)/\ell\). This includes points in different or the same block and remains true when a point lies at an attachment vertex. Each projection pushes global arclength to precisely \(\nu_B\), since the mass outside \(B\) collapses at its unique gate. Hence integrating the resistance sum gives
\[
F_*(x)=\sum_B\int_B r_B(\pi_B(x),z)\,d\nu_B(z)=F(x)
\]
and \(J_*=\sum_B\iint_{B\times B}r_B(z,w)\,d\nu_B(z)d\nu_B(w)=J\). Direct integration gives the displayed \(\Phi_B,J_B\) formulas. Specifically, the interval–interval integral of absolute distance is \(b^3/3\), the circle–circle integral is \(\ell^3/6\), and the circle integral of resistance to a fixed point is \(\ell^2/6\). All atom–continuum and atom–atom terms then follow by expansion.

**3. Convexity of bridge profiles.** While \(x\) moves along the interior of a bridge block \(B\), every other block projection is fixed. Thus the entire dependence on its coordinate \(s\) is \(\Phi_B(s)\), whose second derivative is exactly \(2>0\). Consequently no interior bridge point is a maximizer. The same statement rules out a degree-two subdivision vertex on a bridge.

**4. No cut-vertex maxima.** At a cut vertex belonging to a cycle with exterior mass \(m>0\), the cycle profile \(\Phi_B\) has an upward jump of \(2m\) in its one-sided derivative at that vertex (orient the circle consistently). A local maximum would require the left derivative nonnegative and right derivative nonpositive; such a jump makes both impossible. If a cut vertex belongs only to bridge blocks, let \(q\ge2\) be its degree and let \(a_i\) be the total lengths of the \(q\) branch components obtained by deleting the vertex. The directional derivative of \(F\) into branch \(i\) is \(T-2a_i\). These derivatives sum to \((q-2)T\); for \(q\ge3\), one is positive. For \(q=2\), if neither derivative is positive, both vanish, and the strict bridge convexity from Step 3 makes the vertex nonmaximal. Thus only degree-one bridge endpoints survive.

**5. Strictly concave cycle arcs.** On a cycle with at least one exterior attachment, \(\Phi_B(s)=\ell^2/6+\sum_jm_j\rho_\ell(s-a_j)\). Between adjacent positive-mass attachment coordinates, every term is quadratic with second derivative \(-2m_j/\ell\), and therefore the sum has strictly negative second derivative \(-2M_B/\ell\). Its unique unconstrained stationary point is the displayed \(s_{B,(a,b)}\). Only if it lies in that open arc can it be a local maximum. The finite candidate rule follows from Steps 3–4. A cycle having zero exterior mass forces the whole connected graph to be just that circle; its \(F\) is constant. Thus there are no omitted cases. Comparing candidate values determines **all** global maximizers, and the Green-kernel equality statement from Step 1 determines every norm-attaining function.

**6. Non-antipodal example.** Put \(S=(10^2+2^2+3^2)/6=113/6\). The central circle's resistance integral is \(F(s)=S+2\rho_{10}(s)+3\rho_{10}(s-1)\). On \(1<s<10\), its derivative is \(28/5-s\); on \(0<s<1\), it is \(-2/5-s\). The unique central maximum is at \(s=28/5\), with \(F=2341/75\). The largest values on the two attached circles equal \(S+46/5\) and \(S+54/5\), both strictly smaller. Summing the three exact cycle block contributions gives \(J=4033/10\), and substitution into Step 1 yields \(1777/1500\). This also proves uniqueness of the maximizing evaluation point.

## Verification

The attached standalone `verify_cactus.py` checks exact rational identities against a separately implemented calculation of the continuous Green diagonal, for eight nonisomorphic test structures (bridges, trees, circles, roses, bridges between circles, and cacti with several attachment sites). In the independent method the evaluation point is inserted as a mesh node, a grounded rational Kirchhoff matrix is inverted, and exact quadratic edge bubbles account for the constant arclength source. It compares every sample directly with \(F(x)/T-J/(2T^2)\), checks candidate upper bounds, and includes the non-antipodal example. Executing with Python 3, SymPy and NetworkX prints `EXACT_INDEPENDENT_KIRCHHOFF_GREEN_COMPARISONS_PASSED 264` and `ALL_CACTUS_BLOCK_ENVELOPE_CHECKS_PASSED`. These finite checks corroborate but do not replace the all-graph proof in the preceding section.

## Relationship to prior work

Solomyak's 2002 preprint concerns approximation numbers and uniform Sobolev approximation on general metric graphs. Baker and Faber (2004, revised 2005) develop the metrized-graph Laplacian and effective resistance; their Theorem 9 gives precisely the series and cut-vertex laws used in Proof Step 2, and their Exercise 12 notes piecewise quadratic resistance. These foundational facts are prior work and not claimed as new. Wang and Pan (2015) optimize the *discrete vertex-pair* Kirchhoff index over combinatorial cacti; it is a different measure and optimization variable. Earlier exact sharp evaluations for certain individual roses, parallel-path graphs, and linked-loop networks are covered cases, not separate novelty here. The claimed new result is the complete arbitrary-positive-length cactus block-integral norm formula, global finite quadratic candidate rule, exhaustive norming-location classification, and explicit non-antipodal global example. General resistance and Green theory may contain equivalent formulas implicitly; this remains a priority risk and should be reviewed independently before any publication claim.

## Limitations

This result assumes simple cactus topology and unweighted arclength. It does not cover graphs with overlapping cycle edges (for example theta graphs), arbitrary edge densities or vertex masses, finite-\(L^p\) norms, higher derivative order, or any certification of bibliographic novelty. The finite checker covers only the stated examples and rational sample points; it is not an exhaustive proof. While the formula supplies all candidates, its computational cost is not optimized or asserted to be linear time. Independent mathematical audit has not been performed.

## References

1. M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, arXiv:math/0206235, first posted 2002-06-23, https://arxiv.org/abs/math/0206235.
2. M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428, first posted 2004-07-25, revised 2005-07-01, https://arxiv.org/abs/math/0407428 (especially Theorem 9 and Exercise 12).
3. W.-R. Wang and X.-F. Pan, *Cacti with maximum Kirchhoff index*, arXiv:1511.03080, first posted 2015-11-10, https://arxiv.org/abs/1511.03080.
