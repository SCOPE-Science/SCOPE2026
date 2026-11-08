# Exact resonance-resolved minimum coordinate controllability of weighted circular ladders

## Finding

Let \(m\ge 3\) be an integer, and let \(t>0\). Consider the weighted circular ladder with vertex set \(\mathbb Z_m\times\{0,1\}\), unit-conductance horizontal edges \((x,b)\leftrightarrow(x+1,b)\), and vertical conductances \(t\) on \((x,0)\leftrightarrow(x,1)\). In the continuous-time system \(\dot z=-L_{m,t}z+B_Su\), every column of \(B_S\) is the coordinate vector of an independently actuated vertex of \(S\). Let \(\kappa_m(t)\) be the least possible number of such columns making the entire \(2m\)-dimensional system controllable.

Set \(h=\lfloor m/2\rfloor\), and, for \(0\le j\le h\), define

\[
\nu_j=2-2\cos(2\pi j/m),\qquad
 d_j=\begin{cases}1,&j=0\text{ or }(m\text{ even and }j=m/2),\\ 2,&\text{otherwise}.\end{cases}
\]

Then the **exact minimum coordinate-actuator number** for every \(m\ge3\) and \(t>0\) is

\[
\boxed{\kappa_m(t)=\max\left(\{2\}\cup\{d_j+d_k:0\le j<k\le h,\;2t=\nu_k-\nu_j\}\right).}
\]

Here the maximum of \(\{2\}\) alone is \(2\). Thus the minimum is always \(2\), \(3\), or \(4\), and it is completely determined by collisions between the two vertical spectral bands. Explicit **nested optimal placements** are

\[
S_2=\{(0,0),(1,0)\},\quad
S_3=S_2\cup\{(0,1)\},\quad
S_4=S_3\cup\{(1,1)\},
\]

where \(S_{\kappa_m(t)}\) is controllable and has minimum cardinality.

A striking exception is that for every **even** \(m\), the two scalar spectral modes collide at \(t=2\) without increasing the minimum: \(\kappa_m(2)=2\). For example, when \(m=6\), the four resonance levels \(t=1/2,1,3/2,2\) yield minimum numbers \(3,4,3,2\), respectively; all other positive rung weights give \(2\). When \(m=5\), the resonance \(t=\sqrt5/2\) requires four actuators, whereas \(t=(5-\sqrt5)/4\) and \(t=(5+\sqrt5)/4\) require three.

## Assumptions and scope

The graph is exactly \(C_m\square K_2\) with *uniform* positive rung conductance \(t\) and unit horizontal conductances. Holding loops, directed edges, time-varying gains, partial-state control, and arbitrary controls not constrained to distinct standard coordinate columns are outside the assertion. The actuators are independent: a sum of selected columns into one input is not the same problem. The norm and scalar sign of \(L_{m,t}\) do not affect the PBH rank test; the evolution is taken with \(-L_{m,t}\).

The formula covers every integer \(m\ge3\) and all real \(t>0\), including simultaneous collisions at different eigenvalues; no arithmetic genericity of \(m\) is assumed. The minimum at \(t=0\) is deliberately excluded because the two layers disconnect.

## Proof

**1. Fourier-by-layer decomposition.** With the indicated vertex labels,

\[
L_{m,t}=L(C_m)\otimes I_2+I_m\otimes t\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]

For each \(0\le j\le h\), the cycle eigenspace \(E_j\) has eigenvalue \(\nu_j\) and dimension \(d_j\). At \(j=0\) the basis is the constant vector; when \(m\) is even, at \(j=m/2\) it is the alternating vector. At all other \(j\), take the two real vectors \(x\mapsto\cos(2\pi jx/m)\) and \(x\mapsto\sin(2\pi jx/m)\). Their sine value at \(x=1\) is nonzero for every interior \(j\). The vertical parity vectors are \(w_+=(1,1)\) and \(w_-=(1,-1)\). Consequently the complete spectrum consists of \(E_j\otimes w_+\) at \(\nu_j\) and \(E_j\otimes w_-\) at \(\nu_j+2t\), each of dimension \(d_j\).

The sequence \(\nu_0<\cdots<\nu_h\) is strictly increasing. Thus each vertical band contributes at most one cycle eigenspace to any given eigenvalue. Cross-band equality is possible only if \(\nu_j+2t=\nu_k\) with \(j<k\), and the resulting eigenspace is the direct sum of dimensions \(d_j+d_k\). Even when several different such pairs occur for the same \(t\), they correspond to different eigenvalues. All other eigenspaces have dimension at most \(2\). Since every \(m\ge3\) has an interior Fourier index, the maximum eigenspace dimension is precisely the displayed number \(\kappa_m(t)\).

**2. Lower bound.** The real symmetric PBH criterion says that controllability by independent coordinate columns requires the restriction of each Laplacian eigenspace to the selected vertex coordinates to be injective. A \(q\)-dimensional eigenspace cannot inject into fewer than \(q\) coordinates. Thus at least the maximum eigenspace dimension, i.e. the displayed \(\kappa_m(t)\), is necessary.

**3. Two-coordinate case.** On either parity band, the restriction of every interior real Fourier pair to \((0,0),(1,0)\) is

\[
\begin{pmatrix}1&0\\\cos(2\pi j/m)&\sin(2\pi j/m)\end{pmatrix},
\]

with nonzero determinant. Every singleton is nonzero at these coordinates. The only possible cross-band collision with total dimension \(2\) joins two singleton modes: necessarily \(m\) is even, \(j=0\), \(k=m/2\), and \(2t=4\). Its two restricted columns on this same layer are \((1,1)^T\) and \((1,-1)^T\), so the restriction also has rank \(2\). Hence \(S_2\) controls every eigenlevel when the maximum multiplicity is \(2\).

**4. Three-coordinate case.** Add \((0,1)\) to obtain \(S_3\). Existing eigenspaces of dimension at most \(2\) remain injective by the preceding argument unless a cross-band collision has created a new larger eigenspace. At any collision of dimension \(3\), one participating mode is an interior cosine/sine pair at some \(j\), and the other is a singleton at index \(0\) or (for even \(m\)) \(m/2\). Let \(b\in\{0,1\}\) indicate the vertical parity of the pair, and let \(\sigma\in\{1,-1\}\) be the singleton's value at cycle coordinate \(1\). In a suitable column order, the restricted matrix on \(S_3\) is

\[
\begin{pmatrix}
1&0&1\\
\cos(2\pi j/m)&\sin(2\pi j/m)&\sigma\\
(-1)^b&0&(-1)^{1-b}
\end{pmatrix}.
\]

Its determinant has absolute value \(2|\sin(2\pi j/m)|>0\), independent of \(\sigma\). Therefore \(S_3\) controls all eigenlevels when the maximum multiplicity is \(3\), even with several simultaneous distinct resonances.

**5. Four-coordinate case.** Add \((1,1)\) to obtain \(S_4\). At a dimension-\(4\) collision, both participating modes are interior Fourier pairs and have opposite vertical parities. The invertible row operation taking each same-cycle-coordinate pair of layer observations to its sum and difference separates these two parity sectors. Up to nonzero constant factors, the resulting matrix is block diagonal with the two blocks

\[
\begin{pmatrix}1&0\\\cos(2\pi j/m)&\sin(2\pi j/m)\end{pmatrix},\qquad
\begin{pmatrix}1&0\\\cos(2\pi k/m)&\sin(2\pi k/m)\end{pmatrix}.
\]

Both determinants are nonzero. Every smaller eigenspace is already seen by a subset of these four rows. Therefore \(S_4\) controls all eigenlevels when the maximum multiplicity is \(4\). Combining steps 2–5 proves the theorem for every allowed parameter.

For even \(m\), the only possible difference \(\nu_k-\nu_j=4\) is \(\nu_{m/2}-\nu_0\), involving two singleton modes. Hence at \(t=2\) no multiplicity exceeds \(2\), proving the stated exceptional nonincrease.

## Verification

The included standard-library `verify.py` independently constructs Fourier eigenvectors and checks the full weighted-Laplacian eigen-equation, spectral collision grouping, and PBH ranks of the proposed optimal placements for each positive resonance weight and one generic weight, over all \(3\le m\le23\). It also performs exact rational eigenspace and rank verification for every distinct resonance and an off-resonant value when \(m=3,4,6\). Execute `python3 verify.py` from the folder containing this text. The expected final line is `VERIFY_OK`. The observed counts are 550 floating-point parameter instances, 9,634 Fourier PBH rank checks, and 19,154 eigenvector identity checks, plus 10 exact-rational instances, 56 exact-rational PBH rank checks, and 96 exact eigenvector identities. Floating-point tests have explicit tolerances and are **not** a proof of any all-parameter statement; the analytic PBH argument above establishes the quantified theorem.

## Relationship to prior work

Parlangeli and Notarstefano (arXiv:1109.3556, first public September 16, 2011) give a sharp arithmetic characterization of reachable vertex pairs on a *single cycle*; their Theorem IV.10 and Corollary IV.11 include controllability from two adjacent cycle vertices. Our theorem uses that spatial Fourier feature but adds an independently weighted second layer and completely resolves cross-band eigenspace collisions, including the distinction between scalar–scalar, scalar–double and double–double collisions and the associated three- and four-actuator constructions.

Anđelić, Brunetti and Stanić (2020, DOI 10.1007/s00373-020-02212-6), in their accessible manuscript, give a general Cartesian-product spectral table and single-*binary-vector* controllability theorems (Section 3, Table 1, Theorem 5). Their framework provides the product eigenspace ingredients, but their single-input setting excludes every prism graph with repeated Fourier eigenvalues and does not determine the minimum number or nested locations of independent coordinate inputs at tuned rung weights. The present claim does **not** assert novelty for the standard spectral tensor-product identity or the PBH test. Rahmani et al. (2009) provide broader graph-symmetry necessary conditions rather than the stated weighted circular-ladder classification. Related indexed research on circular-ladder mixing, bounded-band sensor frames, and graph-complex topology concerns distinct questions and does not imply the claimed driver count.

## Limitations

The theorem covers one family of uniformly weighted, undirected prisms and an exact algebraic notion of full-state controllability. It neither optimizes control energy nor establishes robustness to perturbations, and the minimal placements can be ill-conditioned near resonance despite full PBH rank. The verification program's floating-point grouping is finite evidence only. Although accessible and especially relevant original manuscripts have been compared at the level of statements, an unindexed or inaccessible specialist treatment may overlap this classification. Independent mathematical and publication-priority reviews have not occurred.

## References

1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556, first public 2011-09-16. https://arxiv.org/abs/1109.3556
2. M. Anđelić, M. Brunetti and Z. Stanić, *Laplacian Controllability for Graphs Obtained by Some Standard Products*, Graphs and Combinatorics 36 (2020), 1593–1602. https://doi.org/10.1007/s00373-020-02212-6 ; lawful open manuscript: https://www.iris.unina.it/retrieve/e268a731-dc2d-4c8f-e053-1705fe0a812c/gc2.pdf
3. A. Rahmani, M. Ji, M. Mesbahi and M. Egerstedt, *Controllability of Multi-Agent Systems from a Graph-Theoretic Perspective*, SIAM Journal on Control and Optimization 48 (2009), 162–186. https://doi.org/10.1137/060674909
