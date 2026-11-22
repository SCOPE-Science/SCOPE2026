# Crown-preorder support enumerators have simple negative roots in every even order

## Finding

For every integer \(m\ge 3\), let \(\mathcal C_{2m}\) be the crown poset with minimal vertices \(a_0,\ldots,a_{m-1}\), maximal vertices \(b_0,\ldots,b_{m-1}\), and strict comparisons \(a_i<b_i\) and \(a_i<b_{i+1\pmod m}\). Let \(H_m(t)\) be the lattice-point support enumerator of its preorder polytope. Its degree-\(m\) gamma-polynomial is exactly

\[
\Gamma_m(q)=\sum_{j=0}^{m}\gamma_{m,j}q^j=M_{C_{2m}}(q)-q^m
=q^m\left(2T_m\left(1+\frac1{2q}\right)-1\right),
\]

where \(M_{C_{2m}}\) is the ordinary matching-generating polynomial of the cycle on \(2m\) vertices, and \(T_m\) is the Chebyshev polynomial of the first kind. More explicitly, \(\gamma_{m,0}=1\) and

\[
\gamma_{m,j}=\frac{2m}{2m-j}\binom{2m-j}{j}-\mathbf 1_{\{j=m\}}\qquad(1\le j\le m),
\quad H_m(t)=\sum_{j=0}^{m}\gamma_{m,j}t^j(1+t)^{2m-2j}.
\]

**All \(2m\) zeros of \(H_m(t)\) are simple, real, and strictly negative.** The gamma-polynomial zeros, all distinct and strictly below \(-1/4\), are

\[
q_j=\frac1{2(\cos\theta_j-1)}=-\frac1{4\sin^2(\theta_j/2)},\quad
\theta_j=\frac{[3j+1+(j\bmod2)]\pi}{3m},\quad 0\le j<m.
\]

For each \(q_j\), the corresponding two roots of \(H_m\) are the distinct negative reciprocal solutions of \(t/(1+t)^2=q_j\). For example, \(\Gamma_3(q)=1+6q+9q^2+q^3\) and \(H_3(t)=1+12t+48t^2+75t^3+48t^4+12t^5+t^6\).

## Assumptions and scope

The ground set has \(2m\) **distinct labelled elements** with \(m\ge3\), indices interpreted cyclically, and no additional comparisons. The polytope is

\[
Q_m=\{x\in\mathbb R_{\ge0}^{2m}:\sum_{v\in I}x_v\le|I|\text{ for every order ideal }I\subseteq\mathcal C_{2m}\}.
\]

Its support polynomial counts integer points once, by the number of positive coordinates:

\[
H_m(t)=\sum_{x\in Q_m\cap\mathbb Z^{2m}}t^{|\{v:x_v>0\}|}.
\]

We use the published disjoint-matchable-pairs formula for gamma coefficients, not a claim of a new general positivity theorem: for a poset \(P\), \(\gamma_j\) counts pairs of disjoint \(j\)-subsets \((R,S)\), each counted once, for which a bijection \(R\to S\) maps every element weakly upward. It applies to the support polynomial here by Zhong's Theorem 1 and matching proof [2].

## Proof

**1. Matchable pairs are cycle-matchable endpoint subsets.** Every source of a disjoint upward-matched pair in the crown must be minimal: a maximal element has no distinct element above it. Every target must be maximal: nothing distinct lies below a minimal element. Thus every pair with \(j>0\) is uniquely specified by a \(j\)-subset of minima and a \(j\)-subset of maxima that admit a perfect matching in the bipartite graph of cover relations, which is \(C_{2m}\).

**2. Correct for repeated matching witnesses only at the top degree.** For \(j<m\), the vertices chosen from both sides form a **proper induced subgraph** of the simple cycle, hence a disjoint union of paths and isolated vertices. Any perfect matching of a forest is unique (remove a leaf and repeat). Consequently, counting its matchable endpoint pairs is the same as counting size-\(j\) matchings of \(C_{2m}\). For \(j=m\), the sole endpoint pair is the full bipartition, while the cycle has exactly two perfect matchings. Therefore \(\Gamma_m=M_{C_{2m}}-q^m\) coefficientwise, including the constant coefficient one. This removes exactly one overcounted witness, not an entire class of pairs.

**3. Count cycle matchings exactly.** For \(1\le j\le m\), the number of \(j\)-matchings in \(C_{2m}\) is

\[
\frac{2m}{j}\binom{2m-j-1}{j-1}=\frac{2m}{2m-j}\binom{2m-j}{j}.
\]

To see this, double-count a matching together with a marked selected edge: fix one edge among \(2m\), and choose the remaining \(j-1\) mutually separated edges in the path produced by deleting the two edges adjacent to it. The familiar no-adjacency path count is \(\binom{2m-j-1}{j-1}\). Each matching has \(j\) eligible marks. This yields the stated formula for every coefficient.

**4. Transfer matrix and Chebyshev identity.** The matching polynomial of a cycle of length \(L\ge3\) equals the trace of the \(L\)-th power of the binary monomer–dimer transfer matrix \(A=\left(\begin{smallmatrix}1&q\\1&0\end{smallmatrix}\right)\): the two states record whether the preceding edge is selected, and every cyclic legal edge word contributes \(q^{\#\mathrm{selected}}\). Its eigenvalues solve \(\lambda^2-\lambda-q=0\). The two eigenvalue squares sum to \(1+2q\) and multiply to \(q^2\). The defining identity for Chebyshev power sums therefore gives

\[
\operatorname{tr}(A^{2m})=2q^m T_m\left(\frac{1+2q}{2q}\right),
\]

first for \(q>0\) and then identically as polynomials. Subtracting \(q^m\) proves the stated gamma-polynomial identity.

**5. All zeros are real, negative, and simple.** A nonzero \(q\) is a zero of \(\Gamma_m\) if and only if \(T_m(u)=1/2\) with \(u=1+1/(2q)\). Because \(T_m(\cos\theta)=\cos(m\theta)\), its \(m\) solutions in \((-1,1)\) are \(u_j=\cos\theta_j\) with the displayed strictly increasing angles \(0<\theta_0<\cdots<\theta_{m-1}<\pi\). Each solution is simple: \(\sin(m\theta_j)=\pm\sqrt3/2\ne0\). Hence all \(q_j=1/[2(u_j-1)]\) are distinct and strictly below \(-1/4\); the polynomial has degree \(m\), so these are all its roots.

For \(t\ne-1\), the gamma expansion factors as

\[
H_m(t)=(1+t)^{2m}\Gamma_m\left(\frac{t}{(1+t)^2}\right).
\]

For each \(q_j<0\), the equation \(q_j(1+t)^2=t\) has two distinct real negative roots because its discriminant is \(1-4q_j>0\), its root product is \(1\), and its sum is \(1/q_j-2<0\). Distinct gamma roots cannot share a solution. Finally, \(H_m(-1)=(-1)^m\gamma_{m,m}=(-1)^m\ne0\), so none was lost at the excluded substitution point. The \(m\) pairs exhaust degree \(2m\), establishing strict real-rootedness for all \(m\ge3\).

## Verification

The included standalone `verify.py` uses only Python's standard library. Invoke `python3 verify.py`. It independently counts disjoint matchable pairs for every \(3\le m\le8\), enumerates lattice points using every order ideal at \(m=3,4,5\), checks the transfer-matrix count and gamma coefficients for all \(3\le m\le50\), and asserts exact agreement throughout. Its success indicator is `VERIFY_OK`. These are finite regression checks; the five-step proof above handles all \(m\).

## Relationship to prior work

Athanasiadis and Chapoton [1] introduced the preorder support polynomial and conjectured its real-rootedness (Conjecture 5.3), verified only in small sizes and some families. Zhong [2] established the general gamma-positivity and disjoint-matchable-pairs formula that is used here; this general theorem itself is not claimed as new. Cao and Fu [3] prove simple negative roots for the **Ehrhart \(h^*\)-polynomial of the crown's order polytope**, which has degree \(2m-2\), whereas the present result concerns the **support polynomial of the preorder polytope**, of degree \(2m\); neither polynomial is identified with the other. A 2026 crown-free flag-sphere paper [4] excludes crowns from its flag-realisation theorem and discusses the matching formula without recording the cycle-corrected Chebyshev support polynomial or its root locus in its available specialist account. These results share objects or mathematical ingredients but do not state this all-order support-polynomial classification.

The cycle matching polynomial and its Chebyshev power sum are standard; the new synthesis is their exact endpoint-pair correction and the resulting complete crown-preorder support enumerator and zero location.

## Limitations

This theorem concerns **only** the specified height-two crown posets, not all preorders. Strict real-rootedness is not asserted for arbitrary preorders and does not produce a flag-polytope realisation for crowns. It does not establish any implication for the separate crown order-polytope Ehrhart numerator. The matching theorem [2] and elementary cycle enumerator are external established ingredients; the novel claim is the exact crown specialization and all-order root classification. Historical novelty is based on bounded targeted literature searches, not a priority certificate. The available specialist account of [4] was read; its full underlying paper was not independently inspected. All computational checks are finite. Independent mathematical verification is not claimed.

## References

[1] F. Chapoton and C. A. Athanasiadis, *Polytopes and posets associated to preorders* (first posted 2026-05-26), arXiv:2605.26916v1. https://arxiv.org/abs/2605.26916

[2] Y. Zhong, *Gamma-positivity of support enumerators of preorders* (first posted 2026-11-12), arXiv:2611.16858v1, Theorem 1 and Section 2. https://arxiv.org/abs/2611.16858

[3] Y. Cao and H. Fu, *Real-rooted Ehrhart \(h^*\)-polynomials of crown posets and wheel and whirl matroids* (first posted 2026-10-29), arXiv:2610.40496v1, Theorem 1.1. https://arxiv.org/abs/2610.40496

[4] Anonymous, *Preorder polytopes: matching endpoint pairs, flag spheres and the Athanasiadis–Chapoton conjectures*, candidate public release (2026-11-15), doi:10.5281/zenodo.24235777, available theorem summary at https://www.evidencepress.org/releases/preorder-polytope-flag-spheres/
