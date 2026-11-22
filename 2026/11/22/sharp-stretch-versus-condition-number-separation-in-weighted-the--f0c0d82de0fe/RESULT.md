# Sharp stretch-versus-condition-number separation in weighted theta-graph tree preconditioning

## Finding

Let a simple weighted theta graph consist of three internally vertex-disjoint paths joining the same two terminal vertices. Path \(r\in\{1,2,3\}\) has integer length \(\ell_r\ge2\), and every edge on that path has fixed conductance \(w_r>0\). Every spanning tree retaining path \(r\) intact is obtained by deleting one edge from each of the two other paths \(i,j\). Put
\[
D_i=\ell_i-1+\frac{w_i\ell_r}{w_r},\qquad
D_j=\ell_j-1+\frac{w_j\ell_r}{w_r},\qquad
C_{ij\mid r}=\frac{\sqrt{w_iw_j}\,\ell_r}{w_r},
\]
and
\[
\Lambda_\pm(r)=\frac{D_i+D_j\pm\sqrt{(D_i-D_j)^2+4C_{ij\mid r}^{2}}}{2}.
\]
If \(L_G,L_T\) are the original and tree Laplacians and \(n=\ell_1+\ell_2+\ell_3-1\), then the complete positive generalized spectrum of \((L_G,L_T)\) is
\[
\bigl\{1\text{ (multiplicity }n-3\text{)},\ 1+\Lambda_-(r),\ 1+\Lambda_+(r)\bigr\}.
\]
Consequently the **exact smallest spectral condition number over all unmodified spanning-tree preconditioners** is
\[
\kappa_*(G)=1+\min_{r\in\{1,2,3\}}\Lambda_+(r).
\]
Every minimizing retained-path choice is optimal, with **arbitrary positions of the deleted edges** on the other two paths. The total weighted stretch of that tree is \((n-1)+D_i+D_j\).

The two objectives can select **different** trees, with a sharp transition already on six vertices. For path lengths \((2,2,3)\) and conductances \((6,6,t)\), \(t>0\), write \(S\) for retaining either short path and \(L\) for retaining the long path. Their two nontrivial upper eigenvalue increments are
\[
\Lambda_S(t)=\frac{15+t+\sqrt{t^2+18t+9}}6,\qquad
\Lambda_L(t)=1+\frac{36}{t},
\]
while their off-tree stretch sums are \(F_S(t)=5+t/3\) and \(F_L(t)=2+36/t\). The globally optimal spectral tree changes from \(S\) to \(L\) at \(t=36/5\); minimum-total-stretch trees change at the strictly smaller threshold
\[
\tau_{\rm st}=\frac{3(\sqrt{57}-3)}2.
\]
For every \(\tau_{\rm st}<t<36/5\), **all spectral-condition-optimal trees retain a short path, whereas every minimum-total-stretch tree retains the long path**. For example, at \(t=7\) the short-path preconditioner's condition number is \((14+\sqrt{46})/3\), strictly below the long-path value \(50/7\), although its total stretch is \(37/3\), strictly above the long-path value \(85/7\).

Within this pathwise homogeneous-conductance class, six vertices are the smallest possible size of a simple theta graph exhibiting this strict separation: every admissible five-vertex theta graph with all three lengths at least two has lengths \((2,2,2)\), for which both objectives choose precisely the paths of maximum conductance.

## Assumptions and scope

Graphs are finite, simple, undirected, connected; all \(w_r\) are strictly positive and fixed. The three paths have no internal vertices in common, and every path has at least two edges. A preconditioner is the Laplacian of a spanning-tree **subgraph with its inherited edge weights**: no rescaling, additional edges or non-tree SPD matrices are allowed. Condition number means the largest divided by the smallest *positive* generalized eigenvalue of \(L_Gx=\lambda L_Tx\), after removing the common constant-vector nullspace. Total stretch counts each tree edge once and each omitted edge by its original conductance times the resistance of its replacement path in the tree.

## Proof

**Tree classification.** The graph has \(\ell_1+\ell_2+\ell_3\) edges and \(n=\ell_1+\ell_2+\ell_3-1\) vertices, so a tree deletes exactly two edges. Deleting two from one path leaves a cycle formed by the other two paths (and may also disconnect an internal segment). Thus exactly two *different* paths each lose one edge; the remaining path is intact. Conversely, such a deletion gives a connected acyclic graph.

**Rank-two reduction.** Orient the two deleted edges, with incidence columns \(b_i,b_j\). Set \(U=(\sqrt{w_i}b_i,\sqrt{w_j}b_j)\). Then \(L_G=L_T+UU^{\mathsf T}\). On the constant-orthogonal quotient, the nonunit generalized eigenvalues are those of \(I_2+U^{\mathsf T}L_T^\dagger U\); all remaining \(n-3\) eigenvalues are one. The diagonal entries of \(U^{\mathsf T}L_T^\dagger U\) are the deleted-edge conductance times the tree-path resistance. This gives \(D_i,D_j\), because the path contains all \(\ell_i-1\) surviving edges from its own arm and all \(\ell_r\) edges of the retained arm. The two replacement currents overlap only on the retained arm, so their resistance inner product is \(\pm\ell_r/w_r\); multiplied by \(\sqrt{w_iw_j}\), its squared magnitude is \(C_{ij\mid r}^2\). The displayed two eigenvalues and position independence follow. Since \(n-3\ge2\), the smallest positive generalized eigenvalue equals one. The stretch identity follows from the same two diagonal entries.

**Optimal trees.** All spanning trees are represented by one of the three retained-path choices. For each choice the condition number is \(1+\Lambda_+(r)\). Taking the minimum of these three explicit real numbers characterizes every optimizer. The omitted-edge positions play no role.

**Six-vertex threshold.** Direct substitution at \((\ell_1,\ell_2,\ell_3)=(2,2,3)\) and \((w_1,w_2,w_3)=(6,6,t)\) gives the four displayed functions. \(\Lambda_S(t)\) and \(F_S(t)\) are strictly increasing for \(t>0\), whereas \(\Lambda_L(t)\) and \(F_L(t)\) are strictly decreasing. The equality of the stretch sums reduces to \(t^2+9t-108=0\), with unique positive root \(\tau_{\rm st}\). Equality of the upper eigenvalue increments is equivalent (with a positive radical side) to
\[
(216/t-9-t)^2=t^2+18t+9.
\]
The difference of its two sides factors as \(-72(t+18)(5t-36)/t^2\), giving the unique positive crossing \(t=36/5\). The strict ordering \(\tau_{\rm st}<36/5\) is immediate, e.g. by inserting \(t=7\) between them. This proves the open separation interval and its boundary ties. Inserting \(t=7\) gives the exact values stated.

**Minimality.** Under the assumed lengths \(\ell_r\ge2\), the graph has \(n\ge5\). For \(n=5\), all three lengths equal two. If arm \(r\) is retained, then
\[
U^{\mathsf T}L_T^\dagger U=I_2+\frac2{w_r}
\begin{pmatrix}\sqrt{w_i}\\\sqrt{w_j}\end{pmatrix}
\begin{pmatrix}\sqrt{w_i}&\sqrt{w_j}\end{pmatrix}.
\]
Its largest eigenvalue is \(1+2(w_i+w_j)/w_r\), and its trace is \(2+2(w_i+w_j)/w_r\). Both are minimized exactly by maximizing \(w_r\). No strict stretch/spectral reversal is possible on five vertices; the six-vertex construction supplies one.

## Verification

The accompanying `verify_theta.py` constructs the full grounded graph and tree Laplacians and compares their generalized spectra and traces with the displayed formulas. The verifier passed 152 independent spanning-tree/weight/geometry instances (including every deleted-edge position for six families), together with seven symbolic comparisons of the six-vertex thresholds and exact \(t=7\) values. Run `python verify_theta.py` with NumPy, SciPy and SymPy. The finite tests are supplementary to the all-parameter proof above.

## Relationship to prior work

Low-stretch spanning-tree preconditioning and the total-stretch trace bound are established results, particularly Spielman and Woo (2009). Feng (2019) describes construction and spectral improvement of tree-backed sparsifiers, explaining why condition number rather than stretch is the numerical target. A publicly available numerical comparison of spanning trees also demonstrates that stretch rankings can be reversed on grid graphs; the existence of reversal is therefore **not** claimed as new here. The present result gives the *full exact three-arm theta spectrum*, a sharp analytic one-parameter selection frontier, arbitrary-deletion-position rigidity, and minimality within the specified family. Existing general spectral and stretch identities are used rather than re-proved as original principles.

## Limitations

The theorem concerns the generalized spectrum under fixed inherited conductances, not the eigenvalues of the graph Laplacian alone, and not preconditioners with conductance optimization. The example does not imply that minimum-stretch trees are poor in typical graphs; nor does a lower condition number guarantee a fixed runtime benefit. Publication priority remains subject to historical equivalent formulations in electrical network, support-graph and cycle-space literature. There has been no independent audit.

## References

1. Zhuo Feng, *GRASS: Graph Spectral Sparsification Leveraging Scalable Spectral Perturbation Analysis*, arXiv:1911.04382 (first public November 4, 2019), https://arxiv.org/abs/1911.04382 .
2. Daniel A. Spielman and Jaeoh Woo, *A Note on Preconditioning by Low-Stretch Spanning Trees*, arXiv:0903.2816 (2009), https://arxiv.org/abs/0903.2816 .
3. *A preconditioner that is a tree*, Numerical Linear Algebra, https://www.numerical-linear-algebra.com/essays/a-preconditioner-that-is-a-tree/ (accessed November 16, 2026 UTC).
4. Ittai Abraham and Ofer Neiman, *Using Petal-Decompositions to Build a Low Stretch Spanning Tree*, SIAM Journal on Computing 48 (2019), 227–248, https://doi.org/10.1137/17M1115575 .
