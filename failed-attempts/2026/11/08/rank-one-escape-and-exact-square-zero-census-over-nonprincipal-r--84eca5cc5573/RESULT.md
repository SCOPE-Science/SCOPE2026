# Rank-one escape and exact square-zero census over nonprincipal radical-square-zero local rings

## Finding
Let \(R\) be a finite commutative local ring with maximal ideal \(\mathfrak m\) satisfying \(\mathfrak m^2=0\), residue field \(k=R/\mathfrak m=\mathbb F_q\), and \(d=\dim_k\mathfrak m\ge2\). For each \(n\ge1\), let \(X\) vary uniformly among the matrices in \(M_n(R)\) with \(X^2=0\), and write \(T_n=\operatorname{rank}_k(\overline X)\). For each integer \(0\le t\le\lfloor n/2\rfloor\), the exact number of such matrices with \(T_n=t\) is

\[
\boxed{N_{n,t}(R)={n\brack t}_q{n-t\brack t}_q\,|\operatorname{GL}_t(k)|\,q^{d((n-t)^2+t^2)}.}
\]

The law depends on \(R\) only through \(q\) and \(d\), even when \(R\) is nonprincipal or of mixed characteristic. In particular, the all-zero-reduction stratum has cardinality \(N_{n,0}=q^{dn^2}\). For every fixed \(q\) and \(d\ge2\), there is an **exact first rare-event asymptotic**:

\[
\boxed{\Pr(T_n\ne0)\sim\frac{q^{-2(d-1)(n-1)}}{1-q^{-1}},\qquad \Pr(T_n=1\mid T_n\ne0)\longrightarrow1.}
\]

Thus a uniformly sampled square-zero matrix has zero residue-field reduction with probability tending exponentially to one; the overwhelmingly dominant exception has reduction rank exactly one. This is a different large-dimension behavior from the previously established approximately uniform residue-rank law for length-two chain rings (one-dimensional radical), which is **not** claimed as new here.

## Assumptions and scope
The ring is finite, unital, commutative, local, and has square-zero nonzero maximal ideal of residue-field dimension at least two. For example, \(R=\mathbb F_q[u_1,\ldots,u_d]/(u_i u_j:1\le i,j\le d)\), with \(d\ge2\), has the stipulated properties. The theorem also includes any nonsplit finite local ring having the same invariants. The rank \(T_n\) is defined over the residue field and is not a rank over \(R\). The symbol \({a\brack b}_q\) denotes a Gaussian binomial coefficient, and \(|\operatorname{GL}_0(k)|=1\). For the asymptotics, \(q\) and \(d\) remain fixed and \(n\to\infty\).

Writing \(P_j(q)=\prod_{i=1}^{j}(1-q^{-i})\) and \(P_0(q)=1\), the exact formula becomes

\[
N_{n,t}(R)=q^{dn^2-2(d-1)t(n-t)}\frac{P_n(q)}{P_t(q)P_{n-2t}(q)}.
\]

The formula gives a count of zero for \(t>\lfloor n/2\rfloor\). It counts elements, not isomorphism or conjugacy classes. Every matrix is taken on one fixed free \(R\)-module of rank \(n\).

## Proof
**1. Count the residue matrices.** If \(A\in M_n(k)\) satisfies \(A^2=0\) and has rank \(t\), then its image \(U\) has dimension \(t\), its kernel \(W\) has dimension \(n-t\), and \(U\subseteq W\). Conversely, choosing a nested pair \(U\subseteq W\subseteq k^n\) of these dimensions and an isomorphism \(k^n/W\to U\) determines one such operator \(A\). There are \({n\brack t}_q\) choices for \(U\), \({n-t\brack t}_q\) choices for \(W\) containing it, and \(|\operatorname{GL}_t(k)|\) choices for the isomorphism. This proves the residue-matrix factor in the claimed count.

**2. Construct a square-zero lift for every residue operator.** Every such \(A\) is similar over \(k\) to the direct sum of \(t\) copies of the two-by-two nilpotent Jordan block and \(n-2t\) zero one-by-one blocks. The same zero-and-one block matrix over \(R\) has square zero. Every invertible matrix over \(k\) lifts to an invertible matrix over \(R\): the determinant of any lift remains a unit. Therefore conjugating the standard lift by a lift of the similarity matrix produces some \(X_0\in M_n(R)\) with \(X_0^2=0\) and \(\overline X_0=A\). This argument works without a coefficient-field embedding and in mixed characteristic.

**3. Compute the entire lift fiber.** Every matrix lifting \(A\) has a unique expression \(X=X_0+Y\), \(Y\in M_n(\mathfrak m)\). Since \(\mathfrak m^2=0\), the equality \(X^2=0\) is equivalent to \(AY+YA=0\) in \(M_n(\mathfrak m)\). Here the residue operator \(A\) acts canonically on \(\mathfrak m\), because any two representatives of a residue scalar differ by an element annihilating \(\mathfrak m\). Choosing a \(k\)-basis of \(\mathfrak m\) identifies this condition with \(d\) independent copies of \(AB+BA=0\) for \(B\in M_n(k)\).

The operators \(B\mapsto AB+BA\) and \(B\mapsto AB-BA\) have equal kernel dimensions. Indeed, on each two-dimensional Jordan block choose a diagonal involution which conjugates \(A\) to \(-A\), and use the identity on the zero blocks; thus \(A\) and \(-A\) are similar, also in characteristic two. More explicitly, if \(SAS^{-1}=-A\), then \(AB+BA=0\) if and only if \(A(BS^{-1})=(BS^{-1})A\). The latter is the centralizer space of \(A\). As a \(k[z]\)-module, \(k^n\) has decomposition \((k[z]/(z^2))^t\oplus k^{n-2t}\), where \(z\) acts by \(A\). Taking dimensions of homomorphism spaces between summands gives the centralizer dimension

\[
2t^2+2t(n-2t)+(n-2t)^2=(n-t)^2+t^2.
\]

Consequently each \(A\) has exactly \(q^{d((n-t)^2+t^2)}\) square-zero lifts, proving the formula and parameter universality.

**4. Prove the sharp rare-event law.** Put \(a_{n,t}=N_{n,t}/N_{n,0}\). For fixed \(q\) and \(d\ge2\), the positivity of

\[
P_\infty(q)=\prod_{i\ge1}(1-q^{-i})>0
\]

implies \(P_\infty(q)\le P_j(q)\le1\) for every \(j\ge0\). The ratio formula above gives an exact identity for the first nonzero-rank term:

\[
\boxed{a_{n,1}=q^{-2(d-1)(n-1)}\frac{(1-q^{-(n-1)})(1-q^{-n})}{1-q^{-1}}.}
\]

For \(n\ge4\) and every \(2\le t\le\lfloor n/2\rfloor\), we have \(t(n-t)\ge2(n-2)\), and therefore

\[
0\le \sum_{t=2}^{\lfloor n/2\rfloor}a_{n,t}\le \frac n{2P_\infty(q)^2}q^{-4(d-1)(n-2)}.
\]

Dividing by \(a_{n,1}\) yields

\[
\sum_{t\ge2}a_{n,t}/a_{n,1}=O_{q,d}\bigl(nq^{-2(d-1)(n-3)}\bigr)=o(1).
\]

Since \(a_{n,1}\to0\), the conditional probability of rank one among nonzero reductions equals \(a_{n,1}/\sum_{t\ge1}a_{n,t}\to1\). Likewise,

\[
\Pr(T_n\ne0)=\frac{\sum_{t\ge1}a_{n,t}}{1+\sum_{t\ge1}a_{n,t}}=a_{n,1}(1+o(1))\sim\frac{q^{-2(d-1)(n-1)}}{1-q^{-1}}.
\]

This also proves that \(\#\{X\in M_n(R):X^2=0\}=q^{dn^2}\bigl(1+\frac{q^{-2(d-1)(n-1)}}{1-q^{-1}}(1+o(1))\bigr)\). Both the sharp coefficient and the rank-one conditional concentration are independent of any finer ring structure. The proof applies in every residue characteristic.

## Verification
Run the self-contained Python 3 program `verify.py`, which counts small square-zero matrices entry by entry over finite fields, length-two chain rings, dual numbers, and the nonprincipal ring \(\mathbb F_2[u,v]/(u,v)^2\); it also independently checks the dimension of \(\{B:AB+BA=0\}\) for relevant small Jordan types. The nonprincipal cases at \(n=2\) yield rank-count vectors \((256,48)\) for \(q=2,d=2\), \((6561,648)\) for \(q=3,d=2\), and \((4096,192)\) for \(q=2,d=3\). Additional finite checks against the exact product identity and numerical normalized rank profiles were performed. Experiments are consistency checks only; the all-dimension and asymptotic statements are proved above.

## Relationship to prior work
The rank-refined square-zero count for **length-two chain rings** (\(d=1\)) and its uniform limiting reduction-rank distribution were already established and are expressly excluded from the novelty claim. The present theorem concerns the qualitatively different **nonprincipal radical** regime \(d\ge2\), establishes the complete element census there, and proves a sharp exponentially small rank-one escape probability with its leading constant. Simply repeating the known chain-ring rank law would not yield the new probability behavior for \(d\ge2\).

Brešar, Gardella, and Thiel (arXiv:2404.18116v1, first public 2024-04-28, primary MSC 16S50) study commutator-polynomial images in matrix rings and exploit coefficient algebras with multi-dimensional square-zero radicals for an obstruction in Theorem 2.2. They give a natural motivation for the nonprincipal-radical regime but do not establish square-zero element counts or the rank-one escape law.

Prasad, Singla, and Spallone (arXiv:1212.6157v2) develop similarity classification for matrices over local rings of length two and discuss nonprincipal square-zero radicals in Section 10. Their Section 6.2 provides a nilpotent-lift framework, but no stated theorem gives the present element-level rank census for arbitrary \(d\ge2\), nor the sharp asymptotic conditional rank-one result. Ekhad and Zeilberger (arXiv:math/9512224) count square-zero upper triangular matrices over a finite field, a distinct locus. Elementary Jordan and centralizer formulas used in the proof are prior mathematics, not claimed original.

## Limitations
The result requires \(d\ge2\) and \(\mathfrak m^2=0\); it does not extend automatically to longer radicals, arbitrary nonlocal or noncommutative coefficient rings, or other matrix equations. The known \(d=1\) formula and uniform law are deliberately not part of the novelty claim. The leading escape constant is an asymptotic with fixed \(q,d\); its dependence is not asserted to be uniform when either parameter grows. A broader published matrix-equation or local-algebra enumeration might imply the theorem in another formulation. Independent publication-priority verification has not been performed.

## References
1. Matej Brešar, Eusebio Gardella, Hannes Thiel, *Products of commutators in matrix rings*, arXiv:2404.18116v1 (2024-04-28), https://arxiv.org/html/2404.18116v1 .
2. Amritanshu Prasad, Pooja Singla, Steven Spallone, *Similarity of matrices over local rings of length two*, arXiv:1212.6157v2, https://arxiv.org/html/1212.6157v2 .
3. Shalosh B. Ekhad, Doron Zeilberger, *An Explicit Formula for the Number of Solutions of \(X^2=0\) in Triangular Matrices over a Finite Field*, arXiv:math/9512224, https://arxiv.org/abs/math/9512224 .
