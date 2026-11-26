# Exact singular spectrum and branching norm law for finite-tree ancestor integration

## Finding
Let \(b\geq2\) and \(h\geq1\) be integers. On the full rooted \(b\)-ary tree of depth \(h\), let \(I_{b,h}\) sum a function along every root-to-vertex path, with counting measure on **all** vertices. Define \(T_{b,\ell}\), for \(\ell=0,\ldots,h\), to be the symmetric tridiagonal matrix of size \(\ell+1\) with diagonal \((b+1,\ldots,b+1,1)\) and nearest off-diagonal entries \(-\sqrt b\). For \(\ell=0\), the diagonal is simply \((1)\). Then the singular-value multiset is exactly
\[
\operatorname{sv}(I_{b,h})=\{\lambda^{-1/2}:\lambda\in\operatorname{spec}(T_{b,h})\}
\uplus\mathop{\biguplus}_{\ell=0}^{h-1}
\left\{\lambda^{-1/2}:\lambda\in\operatorname{spec}(T_{b,\ell})\right\}^{\uplus (b-1)b^{h-\ell-1}}.
\]
Here \(\uplus\) means multiset union and the superscript denotes repetition of an entire multiset. Every eigenvalue of a block \(T_{b,\ell}\) is positive and is a zero of
\[
U_{\ell+1}\!\left(\frac{b+1-\lambda}{2\sqrt b}\right)
-\sqrt b\,U_\ell\!\left(\frac{b+1-\lambda}{2\sqrt b}\right)=0,
\]
with \(U_j\) the Chebyshev polynomial of the second kind. In particular, the exact sharp \(\ell^2\)-norm is
\[
\|I_{b,h}\|_{2\to2}=\lambda_{\min}(T_{b,h})^{-1/2},
\qquad
\lim_{h\to\infty}\frac{(b-1)\|I_{b,h}\|_{2\to2}}{b^{(h+2)/2}}=1.
\]
The norm-maximizing input is unique up to a nonzero scalar and can be chosen strictly positive and constant on each level. Its integrated values grow strictly from the root to the leaves. As a comparison, for the path case \(b=1\),
\[
\|I_{1,h}\|_{2\to2}=\frac{1}{2\sin(\pi/(4h+6))}
\sim\frac{2h+3}{\pi}.
\]

## Assumptions and scope
The vertex set comprises all \(1+b+\cdots+b^h\) vertices of a rooted finite homogeneous tree. The Hilbert norm is the unweighted counting norm, not a boundary-only norm or a probability-normalized level norm. The ancestor order includes the root and the queried vertex: \((I_{b,h}f)(v)=\sum_{u\preceq v}f(u)\). The matrices are over the real or complex scalars. Throughout, \(b\) is a fixed integer at least two when taking the depth limit. No assertion is made for irregular branching or arbitrary vertex weights.

## Proof
**1. Grounded difference factorization.** Define \((Bg)(o)=g(o)\) and \((Bg)(v)=g(v)-g(\operatorname{parent}(v))\) for non-root vertices. Direct telescoping gives \(B=I_{b,h}^{-1}\). Therefore the inverse squares of the singular values of \(I_{b,h}\) are exactly the eigenvalues of the positive definite \(Q=B^*B\). The associated quadratic form is
\[
\langle Qg,g\rangle=|g(o)|^2+
\sum_{v\neq o}|g(v)-g(\operatorname{parent}(v))|^2.
\]
Consequently, \(Q\) has diagonal \(b+1\) at each non-leaf, diagonal \(1\) at each leaf, and entry \(-1\) on each edge; all other entries vanish. The root's extra unit diagonal term matters: this is not the ordinary graph Laplacian.

**2. Exhaustive orthogonal level/contrast decomposition.** The level-constant subspace has orthonormal basis \(e_k=b^{-k/2}\mathbf1_{\{\operatorname{depth}=k\}}\), for \(k=0,\ldots,h\). Its \(Q\)-matrix is \(T_{b,h}\). For any parent \(u\) at level \(k<h\), choose an orthonormal basis \(w\) of the \((b-1)\)-dimensional child-vector space whose coordinates sum to zero. For each such \(w\), and each \(j=0,\ldots,h-k-1\), let \(e_{u,w,j}\) assign value \(b^{-j/2}w_i\) at every vertex lying \(j\) generations below child \(i\) of \(u\), and zero elsewhere. These vectors have unit norm. For distinct parents, contrasts, or levels, orthogonality follows from disjoint supports or the zero-sum property. Their span for fixed \((u,w)\) is \(Q\)-invariant: the parent coupling cancels because \(\sum_i w_i=0\); the other couplings give \(-\sqrt b\), and the leaf/non-leaf diagonals are as above. Hence this span is represented by \(T_{b,h-k-1}\). There are exactly \((b-1)b^k\) such spans at parent level \(k\), giving the stated multiplicity \((b-1)b^{h-\ell-1}\) for \(\ell=h-k-1\). The dimension identity
\[
(h+1)+\sum_{\ell=0}^{h-1}(b-1)b^{h-\ell-1}(\ell+1)
=\sum_{k=0}^h b^k
\]
proves that these mutually orthogonal invariant subspaces exhaust the ambient Hilbert space. This proves the entire multiset formula, including collisions between eigenvalues from distinct blocks.

**3. Characteristic equations and sharp optimizer.** Expand the determinant of \(T_{b,\ell}-\lambda I\) from the leaf. On the first \(\ell\) positions the usual recurrence has diagonal \(b+1-\lambda\) and off-diagonal-square \(b\). Thus its leading determinants equal \(b^{j/2}U_j((b+1-\lambda)/(2\sqrt b))\). Inserting the final diagonal \(1-\lambda\) yields
\[
\det(T_{b,\ell}-\lambda I)=
 b^{(\ell+1)/2}\left(U_{\ell+1}\!\left(\frac{b+1-\lambda}{2\sqrt b}\right)
 -\sqrt b\,U_{\ell}\!\left(\frac{b+1-\lambda}{2\sqrt b}\right)\right).
\]
All roots are positive since they arise from restrictions of \(B^*B>0\). The matrix \(II^*\) has strictly positive entries: its \((v,w)\) entry equals the number of common ancestors of \(v,w\), at least one. Perron–Frobenius gives a simple largest eigenvalue and a unique positive unit eigenvector up to phase. Tree-automorphism symmetry forces that eigenvector to be level-constant, hence the least eigenvalue of \(Q\) comes from \(T_{b,h}\), and the norm-maximizing input is similarly positive and level-constant. Writing the integrated maximizing output as \(g=If\) and its value at depth \(k\) as \(g_k>0\), let \(\lambda=\lambda_{\min}(T_{b,h})\). The constant test function in the quadratic form gives \(0<\lambda\le 1/(1+b+\cdots+b^h)<1\). The leaf eigen-equation implies \(g_h-g_{h-1}=\lambda g_h>0\). The interior eigen-equations imply \(g_k-g_{k-1}=b(g_{k+1}-g_k)+\lambda g_k\), so backwards induction yields strict level increase all the way to the root.

**4. Exact leading asymptotic.** For any radial vector with \(g_h=1\), define
\[
R_h=\sum_{j=0}^h b^{-j},\qquad N_h=\sum_{k=0}^h b^k.
\]
The radial energy is \(E(g)=g_0^2+\sum_{k=1}^h b^k(g_k-g_{k-1})^2\). Telescoping from the external zero boundary and applying Cauchy–Schwarz yields \(E(g)\ge 1/R_h\). The strictly increasing positive least eigenvector has \(0<g_k\le1\), so its squared norm is at most \(N_h\). Therefore \(\lambda\ge1/(R_hN_h)\). For the reverse inequality take the energy-minimizing trial profile
\[
\widetilde g_k=R_h^{-1}\sum_{j=0}^k b^{-j}.
\]
It has \(E(\widetilde g)=1/R_h\), and \(\sum_{k=0}^h b^k\widetilde g_k^2=N_h(1+o(1))\), because \(1-\widetilde g_k\le C_b b^{-(k+1)}\), and the total loss from \(N_h\) is \(O_b(h+1)\). The Rayleigh quotient gives \(\lambda\le (R_hN_h)^{-1}(1+o(1))\). Since \(R_h\to b/(b-1)\) and \(N_h\sim b^{h+1}/(b-1)\), the claimed asymptotic follows. In the separate path case \(b=1\), the tridiagonal matrix has diagonal \((2,\ldots,2,1)\) and off-diagonal \(-1\). The standard sine eigenvectors with a zero boundary before the root and a Neumann-type leaf boundary give its least eigenvalue \(4\sin^2(\pi/(4h+6))\), yielding the stated exact path norm.

## Verification
The standalone `check_tree.py` reconstructs the actual full \(Q=B^*B\) and the predicted Jacobi-block spectrum independently, then compares their eigenvalues for \(b\in\{2,3,4\}\) and \(h\in\{1,2,3,4\}\). These finite tests agree to numerical tolerance \(10^{-10}\). Further tridiagonal calculations for depths \(8,12,16\) check the asymptotic scaling. These computations test the formulas but are not used as proofs for all degrees and depths; the decomposition and variational argument above supply the infinite-parameter proof. Run `python check_tree.py` with NumPy and SciPy installed.

## Relationship to prior work
Arcozzi–Rochberg–Sawyer's 2002 theorem defines the same ancestor primitive on trees and characterizes the associated weighted Hardy embedding inequality in general, without providing an exact finite homogeneous-tree singular spectrum. Evans–Harris–Lang address approximation numbers for continuous/metric-tree Hardy operators, not the stated finite vertex-counting operator. Rojo–Robbiano's 2007 abstract gives tridiagonal spectral decompositions for weighted *graph Laplacians* on regular-level trees. Such decompositions are methodologically close, but the present inverse square \(B^*B\) has an additional unit *grounding term* at the root, and exact finite singular values and the depth-asymptotic constant are not asserted by the accessible abstract. The full article could not be examined, leaving a specific residual coverage risk. Later work on multi-parameter tree Hardy trace inequalities treats operator bounds and trace conditions, rather than this singular multiset.

## Limitations
Only the complete homogeneous tree, unweighted counting \(\ell^2\), and the root-inclusive ancestor summation are covered. The exact spectrum is an implicit polynomial-root characterization, not elementary radicals at arbitrary depth. The fixed-branching asymptotic is not uniform in \(b\) growing with \(h\). The 2007 weighted-rooted-tree spectral article was not available in full during comparison; it could contain a general boundary-perturbation reduction implying part of this result. Novelty here should be viewed with that explicit uncertainty; no independent validation has been performed.

## References
1. N. Arcozzi, R. Rochberg, E. Sawyer, *Carleson measures for analytic Besov spaces*, Rev. Mat. Iberoam. 18 (2002), 443–510, doi:10.4171/RMI/326 (first published 2002-08-31), especially introduction and Theorem 3. https://doi.org/10.4171/RMI/326
2. W. D. Evans, D. J. Harris, J. Lang, *The approximation numbers of Hardy-type operators on trees*, arXiv:math/0003215 (2000). https://arxiv.org/abs/math/0003215
3. O. Rojo, M. Robbiano, *On the spectra of some weighted rooted trees and applications*, Linear Algebra Appl. 420 (2007), 310–328, doi:10.1016/j.laa.2006.07.011 (abstract accessed; full text not inspected). https://doi.org/10.1016/j.laa.2006.07.011
4. N. Arcozzi, P. Mozolyako, K.-M. Perfekt, *Some properties related to trace inequalities for the multi-parameter Hardy operators on poly-trees*, arXiv:1811.01036 (2018). https://arxiv.org/abs/1811.01036
