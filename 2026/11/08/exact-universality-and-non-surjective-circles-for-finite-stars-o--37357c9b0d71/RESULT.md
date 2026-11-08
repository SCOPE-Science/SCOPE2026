# Exact universality and non-surjective circles for finite stars of homogeneous trees

## Finding
Let \(k\ge 2\) and let \(1\le b_1<b_2<\cdots <b_k\) be integers. Construct one connected, countable, rooted, leafless directed tree \(\mathcal T\) with root \(r\) and exactly \(k\) children \(v_1,\ldots,v_k\): every vertex in the subtree rooted at \(v_j\), including \(v_j\), has exactly \(b_j\) children. Let \(H=\ell^2(V(\mathcal T);\mathbb C)\), and define the unweighted backward parent shift \(S e_r=0\) and \(S e_v=e_{\operatorname{par}(v)}\) for \(v\ne r\).

Then, for every \(\lambda\in\mathbb C\), the following exact statements hold:

1. The spectrum and point spectrum are \(\sigma(S)=\{\lambda:|\lambda|\le\sqrt{b_k}\}\) and \(\sigma_{\mathrm p}(S)=\{\lambda:|\lambda|<\sqrt{b_k}\}\). Every eigenvalue has infinite-dimensional eigenspace.
2. \(S-\lambda I\) is surjective **if and only if** \(|\lambda|\notin\{\sqrt{b_1},\ldots,\sqrt{b_k}\}\). Its range is dense for every \(\lambda\). Hence the range is dense and nonclosed at exactly those \(k\) critical circles.
3. \(S-\lambda I\) is Rota-universal **if and only if** \(|\lambda|<\sqrt{b_k}\). In particular, at every inner critical circle \(|\lambda|=\sqrt{b_j}\) with \(j<k\), the operator is Rota-universal *despite having a non-surjective, nonclosed range*. It satisfies Caradus's sufficient condition (surjectivity and infinite-dimensional kernel) exactly on \(\{\lambda:|\lambda|<\sqrt{b_k}\}\setminus\bigcup_{j<k}\{\lambda:|\lambda|=\sqrt{b_j}\}\).
4. The powers satisfy \(\|S^n\|=b_k^{n/2}\) for every integer \(n\ge1\). With the branching radii of Buckley--Seco, \(R_-=\sqrt{b_1}\) and \(R_+=\sqrt{b_k}\).

Thus the number of exceptional circles separating Rota universality from Caradus surjectivity can be arbitrarily large, even for an unweighted shift on one connected tree. The allowed exceptional radii in this construction are square roots of distinct positive integers; arbitrary positive real radii are not asserted.

## Assumptions and scope
Everything is over the complex scalars. The tree is rooted, countable, leafless, and has finite degree \(\max\{k,b_k\}=b_k\), since \(b_1<\cdots<b_k\) forces \(k\le b_k\). A Rota-universal operator on a separable infinite-dimensional Hilbert space is one whose invariant restrictions, after a nonzero scalar rescaling and similarity, model every bounded operator on such a Hilbert space. The *Caradus property* means surjectivity together with infinite-dimensional kernel; it is sufficient but not necessary for Rota universality. No assertion is made about general nonhomogeneous trees or arbitrary weighted edges.

## Proof
**Block reduction.** Write \(H=\mathbb C e_r\oplus\bigoplus_{j=1}^k H_j\), with \(H_j\) supported on the regular \(b_j\)-ary subtree. Let \(B_j\) denote its backward parent shift, which sends its local root to zero, and let \(\ell_j(x)=\langle x,e_{v_j}\rangle\) with the inner product linear in the first variable. Relative to this decomposition,
\[
 S(c,x_1,\ldots,x_k)=\left(\sum_{j=1}^k\ell_j(x_j),\ B_1x_1,\ldots,B_kx_k\right).
\]
Here \(B_jB_j^*=b_j I\), because each vertex in that subtree has exactly \(b_j\) children. Also \(\|B_j\|=\sqrt{b_j}\) and \(\|B_j^n\|=b_j^{n/2}\).

**All surjectivity thresholds.** For \(|\lambda|<\sqrt{b_j}\), the bounded map \(Q_j=B_j^*/b_j\) satisfies \(B_jQ_j=I\), and
\[
 (B_j-\lambda I)Q_j(I-\lambda Q_j)^{-1}=I.
\]
For \(|\lambda|>\sqrt{b_j}\), \(B_j-\lambda I\) is invertible by a Neumann series. At \(|\lambda|=\sqrt{b_j}\), it is not surjective. Indeed the closed span of normalized uniform-level vectors in \(H_j\) reduces \(B_j\) to \(\sqrt{b_j}\) times the classical scalar unilateral backward shift \(B\); \(B-zI\) fails to be surjective for \(|z|=1\) because its adjoint has normalized approximate eigenvectors (constant-modulus phase packets) with residual tending to zero. Thus \(\operatorname{Ran}(B_j-\lambda I)\ne H_j\) exactly at the circle \(|\lambda|=\sqrt{b_j}\).

For \(\lambda\ne0\), the lower block equations in \((S-\lambda I)(c,x_1,\ldots,x_k)=(d,y_1,\ldots,y_k)\) can be solved for every target precisely when every \(B_j-\lambda I\) is surjective. The upper equation then determines \(c\). At \(\lambda=0\), each \(B_j\) is onto; after solving the lower equations, changing \(x_1\) by a multiple of \(e_{v_1}\in\ker B_1\) corrects the upper target. This proves the stated surjectivity set.

For density, \(S^* y=\overline\lambda y\) forces \(y_r=0\) if \(\lambda\ne0\), then inductively \(y_v=0\) at every depth, as \((S^*y)_v=y_{\operatorname{par}(v)}\). If \(\lambda=0\), leaflessness implies \(S^*y=0\) only when \(y=0\). Therefore \(\ker(S^*-\overline\lambda I)=\{0\}\) for every \(\lambda\), establishing dense range. The ranges at critical circles are accordingly dense and nonclosed.

**An infinite-multiplicity reducing co-shift.** Inside the regular \(b_k\)-ary subtree choose a countably infinite antichain of vertices \(w_i\), for example the vertices with child-addresses \(0^i1\), \(i\ge0\). For each \(w_i\) choose two distinct children and define, for \(n\ge0\),
\[
 f_{i,n}=\frac1{\sqrt{2b_k^n}}\left(\sum_{u\in\operatorname{Desc}_n(w_i0)}e_u-\sum_{u\in\operatorname{Desc}_n(w_i1)}e_u\right).
\]
The vectors \(f_{i,n}\), for all \(i,n\), are orthonormal because their supports lie in pairwise disjoint subtrees, and different levels have disjoint supports. Direct summation of coordinates gives
\[
 Sf_{i,0}=0,\qquad Sf_{i,n}=\sqrt{b_k}\,f_{i,n-1}\ (n\ge1),\qquad S^*f_{i,n}=\sqrt{b_k}\,f_{i,n+1}.
\]
The cancellation in \(Sf_{i,0}\) is crucial: it removes coupling to the rest of the connected tree. Their closed span \(M\) reduces \(S\), and \(S|_M\) is unitarily equivalent to \(\sqrt{b_k}\) times an infinite-multiplicity backward unilateral shift. For each \(|\lambda|<\sqrt{b_k}\), its translate is surjective and has infinite-dimensional kernel (use the right-inverse series above separately on each copy). By Caradus's theorem this restriction is Rota-universal. Therefore \(S-\lambda I\) itself is Rota-universal, regardless of what happens to the range on the orthogonal complement.

**Sharp outer boundary, eigenvalues and growth.** Every \(B_j-\lambda I\) has trivial kernel for \(|\lambda|\ge\sqrt{b_j}\): its normalized radial backward shift has no eigenvalue of modulus at least one, and more generally its pure-coisometry decomposition has no such eigenvalues; equivalently, the descendant-level Cauchy inequality forces an eigenvector's squared mass to diverge whenever \(|\lambda|^2\ge b_j\). Consequently \(S-\lambda I\) is injective for \(|\lambda|\ge\sqrt{b_k}\), and so cannot be Rota-universal: it cannot have an invariant restriction similar to a nonzero scalar multiple of a nonzero square-zero operator, which must have a nontrivial kernel. Below the outer radius, the reducing co-shift supplies infinitely many eigenvectors. The root coupling is solvable as above, so \(\sigma_{\mathrm p}(S)\) is precisely the open outer disk. The spectral radius and spectral disk follow from \(\|S^n\|^2=\sup_v\#\operatorname{Desc}_n(v)=b_k^n\), since the root has \(\sum_j b_j^{n-1}\le k b_k^{n-1}\le b_k^n\) descendants at depth \(n\), and the largest regular subtree attains \(b_k^n\). Finally, \(\inf_v\#\operatorname{Desc}_n(v)=\min\{b_1^n,\sum_j b_j^{n-1}\}\); its exponential growth rate is \(b_1\), since \(b_k>b_1\). This proves the growth-radius formula.

## Verification
The included `check_tree.py` is executable with Python 3 and only the standard library. Running `python check_tree.py` gives `PASS: 532 finite structural check groups; 20 finite star truncations.` It directly checks branching counts, root coupling, orthonormal wavelets, and the two shift identities across five heterogeneous branching lists and four truncation depths. The infinite-dimensional spectral and universality statements follow from the analytical proof above; the finite checks alone cannot establish them.

## Relationship to prior work
Buckley and Seco, *Rota universality of shifts on trees* (arXiv:2610.40089v1, October 29, 2026), prove Rota universality and surjectivity for \(|\lambda|<R_-\), identify the spectral radius \(R_+\), and explicitly ask about the intermediate annulus. Their all-binary example has \(R_-=R_+\); it does not display the separation between Rota universality and the Caradus condition at interior circles established here. The present finite-star construction resolves both questions for this particular family, not for general trees.

Budzynski, Dymek, Planeta and Ptak, *Weighted shifts on directed trees: their multiplier algebras, reflexivity and decompositions* (arXiv:1702.00765v1), provide general Wold-type decompositions for tree shifts, which conceptually explain homogeneous co-shift pieces. Partington and Pozzi, *Universal shifts and composition operators* (Operators and Matrices 5 (2011), 455--467, DOI 10.7153/oam-05-33), study a distinct family of bilateral weighted shifts and Caradus universality. Neither inspected statement identifies the exact punctured surjectivity locus of the connected finite-star parent shift. The result is compatible with these general principles and uses classical co-shift and Caradus arguments; it does not claim those ingredients as new.

## Limitations
The exceptional radii are restricted to \(\sqrt{b_j}\) for integer branch degrees. The proof does not show that failure of the Caradus sufficient condition prevents universality; indeed it proves the contrary in this family. It does not classify the spectrum or universality of arbitrary directed trees. Classical direct-sum and finite-rank-coupling theory could implicitly subsume aspects of the result under a different formulation, so publication priority requires independent expert assessment.

## References
1. J. Buckley and D. Seco, *Rota universality of shifts on trees*, arXiv:2610.40089v1 (first public October 29, 2026), https://arxiv.org/pdf/2610.40089.
2. P. Budzynski, P. Dymek, A. Planeta and M. Ptak, *Weighted shifts on directed trees: their multiplier algebras, reflexivity and decompositions*, arXiv:1702.00765v1, https://arxiv.org/pdf/1702.00765.
3. J. R. Partington and E. Pozzi, *Universal shifts and composition operators*, Operators and Matrices **5** (2011), 455--467, https://files.ele-math.com/articles/oam-05-33.pdf.
