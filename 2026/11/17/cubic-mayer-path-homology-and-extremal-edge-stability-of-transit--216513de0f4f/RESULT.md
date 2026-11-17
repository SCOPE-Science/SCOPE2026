# Cubic Mayer path homology and extremal-edge stability of transitive tournaments

## Finding

Let \(T_n\) denote the transitive tournament on \(\{1,\ldots,n\}\), with precisely the arcs \(i\to j\) for \(i<j\). Let \(T_n^-\) denote the digraph obtained by deleting its extreme arc \(1\to n\). Work with complex coefficients and the primitive cube root \(\omega=e^{2\pi i/3}\). For the regular Mayer path complex of order \(N=3\), write \(H_p^{3,q}\), \(q=1,2\), and \(\beta_p^{3,q}=\dim_{\mathbb C}H_p^{3,q}\). Write \(\delta_{p,j}=1\) if \(p=j\) and \(0\) otherwise.

**Theorem.** For every integer \(n\ge2\), all nonnegative integers \(p\), and \(m=\lfloor n/2\rfloor\), the complete Mayer path Betti numbers of \(T_n\) are

\[
\beta_p^{3,1}(T_n)=\delta_{p,0}+\delta_{p,m-1},
\qquad
\beta_p^{3,2}(T_n)=\delta_{p,1}+\delta_{p,m-1+(n\bmod2)}.
\]

The contributions are *added* when their degrees coincide. For \(n=1\), both groups have exactly one one-dimensional class in degree zero. For every \(n\ge4\), the inclusion of Mayer path complexes induced by \(T_n^-\hookrightarrow T_n\) induces an isomorphism

\[
H_p^{3,q}(T_n^-;\mathbb C)\xrightarrow{\ \cong\ }H_p^{3,q}(T_n;\mathbb C)
\quad \text{for all } p\ge0,\ q\in\{1,2\}.
\]

More strongly, the inclusion splits at the level of the full \(3\)-complex, with complementary three-term exact bar (one basis element in each of chain degrees \(1,2,3\), and nonzero consecutive boundaries). This is an edge-deletion invariance statement for the **directed** Mayer path complex, not merely a renaming of the simplex formula.

## Assumptions and scope

A regular allowed \(p\)-path is a sequence of \(p+1\) distinct consecutive vertices joined by directed arcs. For \(T_n\) these are exactly strictly increasing subsets. For \(T_n^-\), the only excluded increasing path is the two-vertex path \((1,n)\), since no longer increasing sequence can contain that arc as a consecutive pair. On increasing elementary paths the cubic boundary is

\[
d(i_0,\ldots,i_p)=\sum_{j=0}^{p}\omega^j(i_0,\ldots,\widehat{i_j},\ldots,i_p),\qquad d\colon C_0\to0.
\]

For an arbitrary digraph, the underlying Mayer invariant \(3\)-complex has chain groups \(\Omega_p^3=\{x\in A_p:d x\in A_{p-1},\ d^2x\in A_{p-2}\}\) (with negative degrees zero); the Mayer groups are \(H_p^{3,q}=\ker(d^q\!:\Omega_p^3\to\Omega_{p-q}^3)/\operatorname{im}(d^{3-q}\!:\Omega_{p+3-q}^3\to\Omega_p^3)\). For a transitive tournament every deletion remains an increasing path, so \(\Omega_p^3(T_n)=A_p(T_n)\). Both values of \(q\), all homological degrees, and all stated finite sizes are included.

## Proof

**1. The augmented subset complex.** Let \(D_n\) have one basis element \([S]\) in *subset cardinality* degree \(|S|\) for every subset \(S\subseteq\{1,\ldots,n\}\), including the empty subset. Define \(d[S]=\sum_j\omega^{j-1}[S\setminus\{s_j\}]\) for \(S=\{s_1<\cdots<s_k\}\). Since \(1+\omega+\omega^2=0\), the usual two- and three-deletion calculation gives \(d^3=0\).

For a graded \(3\)-complex \(V\), let \(E\) have one generator in degree zero and one in degree one, with a nonzero differential between them. The \(\omega\)-tensor differential is \(d(x\otimes y)=dx\otimes y+\omega^{|x|}x\otimes dy\), and consecutive tensor coordinates encode the subset-deletion weights. Hence \(D_n\cong E^{\otimes_\omega n}\).

Define a length-\(\ell\) bar \(B_\ell(a)\), for \(1\le\ell\le3\), to have one generator in each degree \(a,a+1,\ldots,a+\ell-1\), nonzero successive differentials, and zero otherwise. Direct calculation with bases \(e_0,\ldots,e_{\ell-1}\), \(d e_j=e_{j-1}\) for \(j>0\), and the tensor formula yields

\[
B_1(a)\otimes_\omega E\cong B_2(a),\quad
B_2(a)\otimes_\omega E\cong B_3(a)\oplus B_1(a+1),\quad
B_3(a)\otimes_\omega E\cong B_3(a)\oplus B_3(a+1).
\]

For the middle identity, the twice-differentiated highest generator has nonzero coefficient \(\omega^a(1+\omega)\) in degree \(a\), forcing the length-three summand, and the remaining one-dimensional factor sits in degree \(a+1\). For the final identity, \(d^2\) has rank one from degree \(a+2\) to \(a\) and rank one from degree \(a+3\) to \(a+1\). The six-dimensional total space therefore comprises exactly the two displayed length-three bars. These rank calculations hold for every integer \(a\) because \(\omega^a\ne0\).

Since \(D_1=B_2(0)\), induction shows that every bar in \(D_n\) has length three except for **one** central bar:

\[
D_{2m}:\ B_1(m),\qquad D_{2m+1}:\ B_2(m).
\]

For \(n\ge2\) exactly one of its length-three bars is \(B_3(0)\). Indeed it first occurs at \(n=2\), survives tensoring once with \(E\), and all newly created bars start in positive degree. Its degree-zero generator spans the unique empty-subset line.

**2. Passing to ordinary path degree.** The unaugmented tournament Mayer complex is \(D_n\) modulo the empty-subset line, with cardinality degree \(k\) reindexed as homological degree \(p=k-1\). Quotienting \(B_3(0)\) by its bottom line gives \(B_2(1)\) (in cardinality degree); all other bars remain unchanged. Under the homological reindexing, there is one permanent \(B_2(0)\), plus \(B_1(m-1)\) when \(n=2m\), or \(B_2(m-1)\) when \(n=2m+1\), plus only length-three bars. A length-three bar has zero \(H^{3,1}\) and \(H^{3,2}\); a length-two bar beginning in degree \(a\) contributes a single \(H^{3,1}\) in degree \(a\) and a single \(H^{3,2}\) in degree \(a+1\); a length-one bar contributes one in its degree to both. The formulas follow, including coincident-degree multiplicities. The case \(n=1\) is immediate from its lone vertex.

**3. Deleting the extreme edge.** Let \(C=\Omega^3(T_n)\) and \(U=\Omega^3(T_n^-)\), with \(n\ge4\). Denote the missing edge basis element by \(e=(1,n)\), and let \(\lambda\) extract its coefficient from the full \(C_1\). All increasing paths of three or more vertices remain allowed after deletion. Consequently \(U_p=C_p\) for \(p=0\) or \(p\ge4\), while

\[
U_1=\ker\lambda,\qquad U_2=\ker(\lambda d:C_2\to\mathbb C),\qquad
U_3=\ker(\lambda d^2:C_3\to\mathbb C).
\]

These are kernels of nonzero functionals. For instance, take the increasing four-vertex path \(x=(1,2,3,n)\). Its double differential has coefficient \(\omega^2+1=-\omega\ne0\) on \(e\). Thus \(x,dx,d^2x\) have nonzero images in the three successive one-dimensional quotients \(C_3/U_3,C_2/U_2,C_1/U_1\), respectively. They span a \(d\)-stable exact three-step bar: \(d(x)=dx\), \(d(dx)=d^2x\), \(d(d^2x)=d^3x=0\). Its intersection with \(U\) is zero degree by degree and it surjects onto \(C/U\). Therefore

\[
C=U\oplus\operatorname{span}\{x,dx,d^2x\}
\]

as \(3\)-complexes. Since a length-three bar contributes no Mayer homology for either \(q\), inclusion induces the asserted isomorphisms.

## Verification

The standalone `verify_mayer.py` constructs all increasing-path boundary matrices, verifies cubic nilpotency, and computes \(H^{3,1}\) and \(H^{3,2}\) by exact Gaussian elimination over \(\mathbb F_7\) and \(\mathbb F_{13}\), using primitive cube roots \(2\) and \(3\), respectively. It checks every \(1\le n\le9\), and for \(4\le n\le9\) it checks a nonzero missing-edge coefficient for \(d^2(1,2,3,n)\) and \(d^3=0\). It reports 36 Betti profiles and 12 deletion-bar checks passing; expected output is in `verification_output.txt`. These finite-field checks corroborate but do not replace the complex-characteristic-zero proof in the preceding section.

## Relationship to prior work

Karaguler and Wei (May 15, 2026) introduce Mayer path homology and characterize admissible low-dimensional generators and first-cycle conditions, but do not classify all Mayer groups of all transitive tournaments or the extremal-edge inclusion. Suwayyid and Wei (October 17, 2024) calculate the cubic Mayer Betti numbers of the **first seven ordinary simplices**; those finite instances coincide with the tournament groups and are explicitly not claimed as new. The new all-size bar decomposition extends them, and the deleted-edge comparison concerns a graph-specific path complex rather than an ordinary full simplex. The general \(N\)-complex and \(q\)-tensor mechanisms are classical (Kapranov; Tikaradze); their broad statements do not themselves supply the complete edge-deletion assertion or the displayed all-size degree formulas. A related calculation for directed ladders concerns a different path family.

## Limitations

The result is for the **primitive cubic root** over \(\mathbb C\), the specified transitive tournament and its one extreme-edge deletion. It neither determines Mayer groups at other roots nor covers deletions of arbitrary arcs, and it does not assert invariance under directed homotopy equivalence. The published simplex computations establish the first seven no-deletion cases; priority of the all-size extension remains contingent on other unindexed literature. Independent mathematical validation has not been performed.

## References

1. D. Karaguler and G.-W. Wei, *Mayer Path Homology*, arXiv:2605.16525, first public May 15, 2026. https://arxiv.org/abs/2605.16525
2. F. Suwayyid and G.-W. Wei, *Persistent Mayer Dirac*, Journal of Physics: Complexity 5 (2024), 045005, first published October 17, 2024, doi:10.1088/2632-072X/ad83a5. https://pmc.ncbi.nlm.nih.gov/articles/PMC11488505/
3. M. Kapranov, *On the q-analog of homological algebra*, arXiv:q-alg/9611005 (1996). https://arxiv.org/abs/q-alg/9611005
4. A. Tikaradze, *Homological constructions on N-complexes*, J. Pure Appl. Algebra 176 (2002), 213–222, doi:10.1016/S0022-4049(02)00076-2. https://doi.org/10.1016/S0022-4049(02)00076-2
