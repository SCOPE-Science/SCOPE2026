# Complete dihedral spectra and obtuse-ridge reconstruction for clique-windmill Laplacian simplices

## Finding

For every pair of integers \(s\ge2\) and \(m\ge2\), let \(G_{s,m}=K_1\vee(mK_s)\) consist of a hub joined to \(m\) disjoint complete graphs (blades) of \(s\) vertices each. Set \(N=sm+1\), let \(L\) be the ordinary unweighted graph Laplacian, and fix the **canonical full-column Euclidean realization**
\[
T_{s,m}=\operatorname{conv}\{Le_v:v\in V(G_{s,m})\}\subset\mathbf1^\perp\subset\mathbb R^N.
\]
For a graph vertex \(v\), let \(F_v\) denote the facet opposite \(Le_v\). Dihedral angles are the interior angles between facets, measured in \(\mathbf1^\perp\).

Define the strictly positive quantities
\[
q=\frac{1-N^{-3}}{sm},\qquad
D=\frac{s+3}{(s+1)^2}-q,\qquad
U=\frac{s+2}{(s+1)^2}-q.
\]
Then **every ridge** of \(T_{s,m}\) belongs to exactly one of the following three classes, with the complete spectrum

| Facet pair \(\{F_v,F_w\}\) | Interior cosine | Number of ridges |
|---|---:|---:|
| Leaves in distinct blades | \(q/D\) | \(s^2\binom m2\) |
| Hub and a leaf | \(1/\sqrt{smN^3D}\) | \(sm\) |
| Two leaves in one blade | \(-U/D\) | \(m\binom s2\) |

The three angles are strictly ordered:
\[
\boxed{0<\theta_{\mathrm{cross}}<\theta_{\mathrm{hub}}<\frac\pi2<\theta_{\mathrm{blade}}<\pi.}
\]
In particular, **exactly** \(m\binom s2\) ridges are obtuse. On the set of labelled facets, connect two labels precisely when their ridge is obtuse. The resulting graph is \(mK_s\sqcup K_1\): its unique isolated vertex is the hub and its nontrivial connected components are exactly the blades. Thus the complete Euclidean dihedral data reconstruct the underlying labelled clique-windmill graph. All the simplices have the same simplex face lattice, but their obtuse-angle relations retain this graph structure.

There is a sharp one-blade boundary: at \(m=1\), the graph is the complete graph \(K_{s+1}\), its full-column Laplacian simplex is regular, and **all** interior dihedral angles equal \(\arccos(1/s)\), so none is obtuse.

For fixed \(s\ge2\) as \(m\to\infty\), the acute angles approach right angles on different scales:
\[
\frac\pi2-\theta_{\mathrm{cross}}
=\frac{(s+1)^2}{s(s+3)}m^{-1}+O_s(m^{-2}),
\]
\[
\frac\pi2-\theta_{\mathrm{hub}}
=\frac{s+1}{s^2\sqrt{s+3}}m^{-2}+O_s(m^{-3}),
\]
while
\[
\theta_{\mathrm{blade}}\longrightarrow
\arccos\left(-\frac{s+2}{s+3}\right)>\frac\pi2.
\]

## Assumptions and scope

The graph is simple, undirected, connected, and unweighted; \(s,m\) are positive **integers** with \(s,m\ge2\) except for the explicitly stated boundary case \(m=1\). The metric is inherited from the standard orthonormal coordinates of \(\mathbb R^N\) **before** any lattice-coordinate projection. A general unimodular change of lattice coordinates need not preserve these angles. For a simplex of dimension \(N-1\), every unordered pair of distinct facets meets at one codimension-two ridge, and so the theorem includes all \(\binom N2\) ridges.

## Proof

**1. Facet-normal identity.** Connectedness implies \(\ker L=\operatorname{span}\{\mathbf1\}\) and that the \(N\) Laplacian columns are affinely independent in \(H=\mathbf1^\perp\). Let \(L^+\) be the Moore--Penrose inverse of \(L\). For every \(x\in H\), the unique barycentric coordinates of \(x\) with respect to the columns are
\[
\lambda_v(x)=\frac1N+\langle L^+e_v,x\rangle,
\quad\sum_v\lambda_v(x)=1,
\quad x=\sum_v\lambda_v(x)Le_v.
\]
Thus the inward facet normal is \(L^+e_v\), and the cosine of the interior angle between facets \(F_v,F_w\) is
\[
\cos\theta_{vw}
=-\frac{C_{vw}}{\sqrt{C_{vv}C_{ww}}},
\qquad C=(L^+)^2.
\tag{1}
\]
The minus sign is essential: the interior dihedral angle is supplementary to the angle between outward normals.

**2. Orthogonal spectral decomposition.** Index the hub by \(0\) and the leaves in \(m\) blocks of \(s\) indices. The zero-sum space splits orthogonally into: (i) vectors summing to zero **within** each blade, dimension \(m(s-1)\); (ii) vectors constant within each blade, with zero hub coordinate and blade constants summing to zero, dimension \(m-1\); and (iii) the line spanned by \(v=(-(N-1),1,\ldots,1)\). The Laplacian eigenvalues on these spaces are, respectively, \(s+1\), \(1\), and \(N\). The corresponding orthogonal projections are \(P_{\rm intra},P_{\rm block},P_{\rm hub}\), where
\[
P_{\rm intra}|_{\rm leaves}=I_m\otimes\left(I_s-\frac{J_s}{s}\right),\quad
P_{\rm block}|_{\rm leaves}=\left(I_m-\frac{J_m}{m}\right)\otimes\frac{J_s}{s},\quad
P_{\rm hub}=\frac{vv^{\mathsf T}}{N(N-1)}.
\]
Both first projections have zero hub row and column. Hence
\[
L=(s+1)P_{\rm intra}+P_{\rm block}+NP_{\rm hub},
\]
\[
\boxed{C=(s+1)^{-2}P_{\rm intra}+P_{\rm block}+N^{-2}P_{\rm hub}.}
\tag{2}
\]

**3. Exact normal Gram entries.** Evaluating (2) on the hub and leaf coordinates gives
\[
C_{00}=\frac{sm}{N^3},\qquad
C_{0v}=-\frac1{N^3}\quad(v\ne0),
\]
\[
C_{vv}=D\quad(v\ne0),\qquad
C_{vw}=\begin{cases}
U,&v\ne w\text{ are leaves in one blade},\\
-q,&v,w\text{ are leaves in different blades}.
\end{cases}
\tag{3}
\]
Indeed \(P_{\rm intra}\) contributes \((1-1/s)/(s+1)^2\) to a leaf diagonal and \(-1/[s(s+1)^2]\) within a blade; \(P_{\rm block}\) contributes \((1-1/m)/s\) within one blade and \(-1/(sm)\) across blades; the hub projector contributes \(1/(smN^3)\) to each leaf-leaf entry. Simplification yields exactly \(D,U,q\). Inserting (3) in (1) proves the three claimed cosine formulas.

**4. Strict signs and angle order.** Since \(m\ge2\) and \(N\ge5\),
\[
0<q<\frac1{2s},\quad
U>\frac{s+2}{(s+1)^2}-\frac1{2s}
=\frac{s^2+2s-1}{2s(s+1)^2}>0,
\]
\[
D-q>\frac{s+3}{(s+1)^2}-\frac1s
=\frac{s-1}{s(s+1)^2}>0.
\]
Also \(D<(s+3)/(s+1)^2<1\). The same-blade cosine is negative, while the other two are strictly positive and less than one. The cross-blade cosine exceeds the hub-leaf cosine: after squaring and clearing positive denominators, this is equivalent to
\[
q^2(sm)N^3>D.
\]
But the left-hand side is \((N^3-1)^2/[(N-1)N^3]>1>D\) for \(N\ge5\). Because \(\arccos\) is strictly decreasing, the claimed strict ordering follows.

**5. Counts, reconstruction, and boundary.** There are \(s^2\binom m2\) pairs of leaves from different blades, \(sm\) hub-leaf pairs, and \(m\binom s2\) same-blade pairs. Their sum is \(\binom N2\). Precisely the last category is obtuse. Its facet-label graph consists of \(m\) disjoint \(K_s\)'s and the isolated hub, proving exact graph reconstruction. For \(m=1\), \(G_{s,1}=K_{s+1}\), so \(L=NI-J\) and \(C=N^{-2}(I-J/N)\); the normalized off-diagonal cosine is \(1/s\), proving the stated sharp boundary.

**6. Two acute scales.** For fixed \(s\), as \(m\to\infty\), \(q=(sm)^{-1}+O_s(m^{-4})\), \(D=(s+3)/(s+1)^2+O_s(m^{-1})\), and \(N=sm+1\). Expanding the three cosine formulas and using \(\arcsin z=z+O(z^3)\) yields the two displayed acute-angle expansions and the obtuse-angle limit.

## Verification

The self-contained companion `check_clique_windmill_angles.py` uses Python 3 exact rational arithmetic. For every \(2\le s\le6\) and \(1\le m\le5\), it constructs the graph Laplacian independently, inverts \(L+J/N\) by rational Gauss--Jordan elimination, subtracts \(J/N\) to obtain \(L^+\), squares it, and checks **every** Gram entry against (3), including the one-blade boundary. It also checks positive-sign and angle-order inequalities for \(m\ge2\). The recorded replay was:

```text
CLIQUE_WINDMILL_ANGLE_PASS exact_parameter_pairs=25 all_ridges=2625 max_order=31
```

The finite tests independently corroborate the exact entries; the proof using (1)--(3) covers **all** admissible integers.

## Relationship to prior work

Braun and Meyer introduced Laplacian simplices and established their basic lattice and Ehrhart properties, with detailed examples for trees, cycles, and complete graphs. Meyer and Pllaha studied duality and codes for the same simplex construction. Neither inspected work determines the complete Euclidean dihedral spectrum for clique windmills or the ability to reconstruct their blades from obtuse ridges. Abdian, Ashrafi, Beineke, and Oboudi study **Laplacian spectral determination** of friendship-related graphs rather than Euclidean facet angles of the associated simplices.

A previously published theorem on **vertex-transitive** Laplacian simplices supplies the general barycentric facet-normal identity used in (1), but its symmetric-graph radius statements do not apply to these non-vertex-transitive clique windmills (\(m\ge2\)). A separate published theorem treats the **symmetric edge polytope** of the same windmill graphs, a different polytope and a different inball problem; neither theorem evaluates the off-diagonal Gram entries, angle signs, or reconstruction assertion here. A published complete-bipartite Laplacian-simplex result instead concerns minimum enclosing spheres, not the current nonbipartite angular invariant.

## Limitations

All results concern the original full-column inherited Euclidean metric and equal-sized clique blades. They do not claim angle invariance under nonorthogonal lattice-coordinate changes, or an analogue for arbitrary unequal blades, edge weights, or higher-order graph joins. The generic pseudoinverse identity is not claimed new. Priority remains provisional: unsurveyed sources may contain equivalent angle formulas; the supplied computations are finite checks and not independent proof certification.

## References

1. B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085, first public version 2017-06-21, https://arxiv.org/abs/1706.07085.
2. M. Meyer and T. Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960, first public version 2018-09-09, https://arxiv.org/abs/1809.02960.
3. A. Z. Abdian, A. R. Ashrafi, L. W. Beineke, and M. R. Oboudi, *Laplacian Spectral Determination of Path-Friendship Graphs*, arXiv:1903.11121, first public version 2019-03-26, https://arxiv.org/abs/1903.11121.
4. *Vertex-transitive Laplacian simplices have spectral inradii and degree-controlled circumradii*, published research record, identifier `841b23980b76` (2026).
5. *Euclidean inballs of clique-windmill symmetric edge polytopes*, published research record, identifier `3dbe8167618b` (2026).
6. *Sharp vertex-contact transition for complete-bipartite Laplacian simplices*, published research record, identifier `ac6d13296de7` (2026).
