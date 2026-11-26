# A universal bounded-degree decoration with no coordinate-dominant spectral measure

## Finding

**Theorem.** Let \(B=(V,E)\) be any countably infinite, connected, simple graph of uniformly bounded vertex degree. Construct \(G(B)\) by adjoining, at each vertex \(v\in V\), two distinct pendant vertices \(a_{v,1},a_{v,2}\) and two pendant chains \(v-b_{v,i}-c_{v,i}\), for \(i\in\{1,2\}\). Keep every original edge of \(B\), and give every edge weight one. Let \(A\) be the selfadjoint adjacency operator of \(G(B)\) on \(\ell^2(V(G(B)))\), and let \(P_\lambda=\mathbf{1}_{\{\lambda\}}(A)\) denote its spectral projection at \(\lambda\).

The coordinate support of an eigenspace means the set of vertices where some vector in that eigenspace is nonzero. The entire eigenspace at \(0\) has coordinate support exactly the short leaves. The eigenspaces at \(1\) and \(-1\) are orthogonal and have the **same** coordinate support, exactly the long-arm vertices. These two coordinate sets are disjoint, and each excludes the original vertices. The vertex spectral masses are precisely

\[
\begin{array}{c|ccc}
\text{vertex type}&\langle P_0\delta_x,\delta_x\rangle&\langle P_1\delta_x,\delta_x\rangle&\langle P_{-1}\delta_x,\delta_x\rangle\\ \hline
x\in V&0&0&0\\
x=a_{v,i}&1/2&0&0\\
x=b_{v,i}\ \text{or}\ c_{v,i}&0&1/4&1/4
\end{array}
\]

Each of the three eigenspaces is infinite-dimensional. Consequently **no standard coordinate vector \(\delta_x\) is a dominant vector for \(A\)**: its scalar spectral measure fails to dominate some other vertex measure. Equivalently, \(G(B)\) is a connected, countably infinite bounded-degree graph without any spectrally dominant vertex. In particular, choosing \(B\) to be the one-way infinite path gives a **one-ended unweighted tree of maximum degree six** with this property.

## Assumptions and scope

A graph is simple and unweighted. Original vertices \(V\) and all new pendant vertices are pairwise distinct. Because \(\deg_B(v)\le d\) uniformly, \(\deg_{G(B)}(v)\le d+4\), and all pendant vertices have degree at most two. Thus the adjacency matrix defines a bounded selfadjoint operator on the stated Hilbert space. Connectedness and infinitude are inherited from \(B\).

For a vertex \(x\), its scalar spectral measure is \(\mu_x(S)=\langle\mathbf{1}_S(A)\delta_x,\delta_x\rangle\) for Borel sets \(S\subset\mathbb R\). A vertex \(x\) is spectrally dominant if \(\mu_y\ll\mu_x\) for every vertex \(y\). This is domination of spectral measures, not graph-theoretic domination by adjacency.

## Proof

For an arbitrary \(\ell^2\) eigenvector \(f\) with eigenvalue \(\lambda\), denote the amplitude at an original vertex by \(x_v\), at the short leaves by \(y_{v,i}\), at the intermediate long-arm vertices by \(u_{v,i}\), and at their terminal vertices by \(z_{v,i}\). The eigenvalue equations, holding at each original vertex \(v\) and both indices \(i\), are

\[
\begin{aligned}
\lambda y_{v,i}&=x_v,\\
\lambda z_{v,i}&=u_{v,i},\\
\lambda u_{v,i}&=x_v+z_{v,i},\\
\lambda x_v&=\sum_{w\sim_B v}x_w+y_{v,1}+y_{v,2}+u_{v,1}+u_{v,2}.
\end{aligned}
\]

**At \(\lambda=0\):** the first equation forces \(x_v=0\) for every \(v\). The second forces \(u_{v,i}=0\); the third then forces \(z_{v,i}=0\); the final equation reduces to \(y_{v,1}+y_{v,2}=0\). Conversely, all square-summable combinations of these antisymmetric leaf-pair vectors solve the equations. Consequently

\[
\ker A=\overline{\operatorname{span}}\left\{e_{v,0}=\frac{\delta_{a_{v,1}}-\delta_{a_{v,2}}}{\sqrt2}:v\in V\right\}.
\]

**At \(\lambda=1\):** from \(z_{v,i}=u_{v,i}\) and \(u_{v,i}=x_v+z_{v,i}\) one obtains \(x_v=0\). Thus \(y_{v,i}=0\), and the last equation is \(u_{v,1}+u_{v,2}=0\). The complete eigenbasis consists of

\[
e_{v,+}=\frac{\delta_{b_{v,1}}-\delta_{b_{v,2}}+\delta_{c_{v,1}}-\delta_{c_{v,2}}}{2},\qquad v\in V.
\]

**At \(\lambda=-1\):** the second equation gives \(z_{v,i}=-u_{v,i}\), while the third again forces \(x_v=0\). The first yields \(y_{v,i}=0\), and the final equation yields \(u_{v,1}+u_{v,2}=0\). Hence a complete eigenbasis is

\[
e_{v,-}=\frac{\delta_{b_{v,1}}-\delta_{b_{v,2}}-\delta_{c_{v,1}}+\delta_{c_{v,2}}}{2},\qquad v\in V.
\]

The displayed vectors are orthonormal within each family, and the three families are pairwise orthogonal. They exhaust the respective full eigenspaces by the pointwise elimination above; there are no unaccounted, possibly delocalized eigenvectors at these three eigenvalues. Since \(V\) is infinite, each eigenvalue has infinite multiplicity.

For a selfadjoint operator, \(\mu_x(\{\lambda\})=\|P_\lambda\delta_x\|^2\). Squaring the coefficients of \(\delta_x\) against the complete orthonormal bases gives the table in the theorem. In particular, all original vertices have zero mass at \(0\); each short leaf sees the atom \(0\) but misses the atom \(1\); each long-arm vertex sees the atoms \(1\) and \(-1\) but misses the atom \(0\). Thus every vertex's spectral measure assigns zero to a singleton which another vertex's spectral measure charges positively. No vertex is dominant. Finally, if \(B\) is the infinite ray, attaching finite trees at its vertices preserves the tree property and the number of ends, and the maximum degree is six. This completes the proof.

## Verification

The proof is a direct analysis of the infinite operator and does not rely on finite-size extrapolation. The accompanying `checker.py` performs exact rational-arithmetic checks on decorated finite path, cycle and small connected base graphs: it verifies all three eigenvector families, exact eigenspace nullities, normalization and the mass table. Run with `python3 checker.py`; the packaged reproducibility record reports `PASS 208 exact finite checks on decorated base graphs; infinite claim is proved independently.`

A separate periodic-fiber check for the bilateral-line case has symmetric-sector characteristic polynomial \(\lambda(\lambda^2-1)(\lambda-2\cos\theta)-4\lambda^2+2\), which is nonzero at \(\lambda\in\{0,1,-1\}\). The direct elimination above is stronger: it proves the same complete point eigenspaces for every admissible base graph without Fourier or Floquet assumptions.

## Relationship to prior work

Bruchez, de la Harpe and Nagnibeda introduce and study spectrally dominant vertices, exhibit connected **finite** trees without them (including the seven-vertex double-pendant motif), and explicitly identify a bounded-degree connected **infinite** example with no dominant vertex as an unresolved question. Their finite example and terminology are acknowledged; the claim here is the universal infinite extension with complete spectral projection masses. Spectral dominance does not follow from the existence of a compactly supported eigenvector alone: one must show that no other eigenvectors at the same eigenvalue restore missing atoms at other coordinates. The full-eigenspace elimination resolves that issue.

Sabri and Youssef develop general construction recipes and characterizations for localized flat-band eigenfunctions in periodic graphs. Those results contextualize the compactly supported eigenmodes but do not, in the inspected statements, establish the vertex-by-vertex scalar-spectral-measure obstruction for arbitrary bounded-degree base graphs. Hirschler and Woess develop finite-host graph-substitution spectra and discuss spectrally nondominant host vertices; they distinguish the infinite-host case as further work.

## Limitations

The construction is sufficient, not a characterization of all infinite graphs without spectrally dominant vertices. No minimal degree, minimum motif size or robustness under arbitrary edge perturbations is claimed. Only the three indicated point spectral projections are classified; the remainder of the spectrum depends on the base graph. Previously unexamined results on flat bands or decorated graphs could bear on priority.

## References

1. C. Bruchez, P. de la Harpe, T. Nagnibeda, *Spectral measures and dominant vertices in graphs of bounded degree*, first posted 25 May 2022, arXiv:2205.12819, especially Sections 3, 5 and 7. https://arxiv.org/abs/2205.12819
2. M. Sabri, P. Youssef, *Flat bands of periodic graphs*, 2023, arXiv:2304.06465, especially Sections 1–3 and 6. https://arxiv.org/abs/2304.06465
3. T. Hirschler, W. Woess, *The spectra of graph substitutions*, 2025, arXiv:2507.21733, especially Sections 3–4 and 7. https://arxiv.org/abs/2507.21733
