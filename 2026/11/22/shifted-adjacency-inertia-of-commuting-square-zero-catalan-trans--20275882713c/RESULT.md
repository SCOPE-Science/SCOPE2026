# Shifted adjacency inertia of commuting square-zero Catalan transformations

## Finding
Let \(n\ge3\) be an integer. In the Catalan transformation monoid \(\mathcal C_n\) of order-preserving, order-decreasing self-maps of \([n]\), write \(z\) for the constant map with value one and set \(S_n=\{f\in\mathcal C_n:f^2=z\}\). Form the simple graph \(G_n\) on **all** members of \(S_n\), including \(z\), joining distinct vertices when their maps commute. Let \(A_n\) be its real adjacency matrix. Define \(\operatorname{In}(B)\) to be the ordered triple of positive, negative, and zero eigenvalue multiplicities of a symmetric real matrix \(B\).

**Theorem.** The graph has \(|S_n|=2^{n-2}\) vertices and
\[
\boxed{\operatorname{In}(A_n+I)=\bigl(n-2,\ n-3,\ 2^{n-2}-2n+5\bigr).}
\]
In particular the eigenvalue \(-1\) of \(A_n\) has multiplicity exactly \(2^{n-2}-2n+5\), and \(\operatorname{rank}_{\mathbb R}(A_n+I)=2n-5\). The remaining eigenvalues comprise exactly \(n-2\) numbers greater than \(-1\) and \(n-3\) numbers less than \(-1\), counted with multiplicity. If the universal zero vertex is omitted, the corresponding graph \(G_n^{\ast}\) instead satisfies
\[
\boxed{\operatorname{In}(A_n^{\ast}+I)=\bigl(n-2,\ n-3,\ 2^{n-2}-2n+4\bigr).}
\]
Both formulas hold without asymptotic or genericity assumptions.

## Assumptions and scope
Composition is functional composition, with the right factor applied first; \(z\) is an absorbing zero. The condition \(f^2=z\) includes \(f=z\). Adjacency never includes loops, even when a map commutes with itself. The shifts use identity matrices of the respective graph orders. All ranks and inertias in this statement are over \(\mathbb R\), although the monoid itself is defined combinatorially.

For a nonconstant \(f\in S_n\), put \(a_f=f(n)\) and \(b_f=\max\{i\in[n]:f(i)=1\}\). Then \(2\le a_f\le b_f\le n-1\). Its *interval type* is \(I_f=[a_f,b_f]\) within the interior chain \(\{2,\dots,n-1\}\). Assign the zero map the full interior interval \(I_z=[2,n-1]\). Different maps can have the same interval type.

## Proof
**1. Normal form and the square-zero count.** Each member of \(\mathcal C_n\) fixes one and is weakly increasing. For nonconstant \(f\) with \(b=b_f\), the initial fiber of one is precisely \([1,b]\). Now \(f^2=z\) if and only if every value in \(\operatorname{im}f\) belongs to that initial fiber, equivalently \(a_f\le b\). Thus the suffix of length \(n-b\) is an arbitrary weakly increasing word with entries in \(\{2,\dots,b\}\); it automatically respects order decrease since every suffix index exceeds \(b\). For fixed \(2\le b\le n-1\) the number of words is \(\binom{n-2}{b-2}\). Including \(z\) gives
\[
|S_n|=1+\sum_{b=2}^{n-1}\binom{n-2}{b-2}=2^{n-2}.
\]
Every nonempty interior interval \([a,b]\) occurs: choose the map whose initial \(b\) values equal one and whose remaining entries equal \(a\).

**2. Commutation becomes interval intersection.** For nonzero \(f,g\in S_n\), the composite \(g\circ f\) equals \(z\) exactly when \(g\) sends every image value of \(f\) to one. By the initial-one-fiber property this is equivalent to \(a_f\le b_g\). Likewise \(f\circ g=z\) exactly when \(a_g\le b_f\). At least one of these two conditions always holds: if \(b_f\le b_g\), then \(a_f\le b_f\le b_g\), and the alternative order is symmetric. Thus two members of \(S_n\) commute precisely when both products are \(z\), which for nonzero members is equivalent to
\[
[a_f,b_f]\cap[a_g,b_g]\ne\varnothing.
\]
The zero map commutes with everything, as does its associated full interval intersect every type. The equivalence is also valid when two nonzero maps have the same type and when they are equal.

**3. Exact matrix blow-up.** Write \(p=n-2\) and \(\mathscr I_p\) for all \(m=p(p+1)/2\) nonempty intervals of a \(p\)-point chain, relabeled \([1,p]\). Let \(H_p\) be their symmetric *loop-retaining* intersection matrix, so \((H_p)_{I,J}=1\) precisely when \(I\cap J\ne\varnothing\). Let \(X\) be the \(|S_n|\)-by-\(m\) incidence matrix assigning each map to its interval type. Each interval occurs, hence \(X\) has linearly independent columns. By step 2 the exact identity is
\[
A_n+I=XH_pX^{\mathsf T}.
\]
Extending the independent columns of \(X\) to a basis shows that this symmetric matrix is congruent over \(\mathbb R\) to \(H_p\oplus0_{|S_n|-m}\). Therefore its nonzero inertia equals that of \(H_p\).

**4. Inertia of the interval-intersection matrix.** Index intervals \([a,b]\), and take an arbitrary column interval \(J=[c,d]\). Since \(c\le d\) and \(a\le b\), the corresponding row function is
\[
 h_{[a,b]}(J)=\mathbf 1_{c\le b}-\mathbf 1_{d<a}.
\]
Consequently, for \(a<b\),
\[
 h_{[a,b]}=h_{[a,a]}+\sum_{j=a}^{b-1}\bigl(h_{[j,j+1]}-h_{[j,j]}\bigr).
\]
Thus all rows of \(H_p\) lie in the span of its \(p\) singleton rows and \(p-1\) adjacent-pair rows; in particular \(\operatorname{rank}H_p\le2p-1\). The principal submatrix \(B_p\) on these \(2p-1\) intervals has block form
\[
B_p=\begin{pmatrix}I_p&U\\U^{\mathsf T}&V\end{pmatrix},
\]
where \(U_{i,j}=1\) if \(i\in\{j,j+1\}\) and zero otherwise, and \(V_{j,k}=1\) if \(|j-k|\le1\) and zero otherwise. The diagonal entries of \(U^{\mathsf T}U\) are two and its neighboring off-diagonal entries are one, with all others zero. Hence \(V-U^{\mathsf T}U=-I_{p-1}\). The Schur-complement congruence gives
\[
\operatorname{In}(B_p)=(p,p-1,0).
\]
In particular \(B_p\) is nonsingular and \(\operatorname{rank}H_p=2p-1\). A real symmetric matrix of rank \(2p-1\) with a nonsingular principal submatrix of that order is congruent to that principal submatrix plus a zero block, so
\[
\operatorname{In}(H_p)=\bigl(p,p-1,m-(2p-1)\bigr).
\]
This includes the boundary \(p=1\), interpreting the zero-dimensional blocks in the usual way.

**5. Final inertia.** As the incidence matrix \(X\) has full column rank, steps 3--4 show
\[
\operatorname{In}(A_n+I)=\bigl(p,p-1,|S_n|-(2p-1)\bigr),
\]
which is the first formula after substituting \(p=n-2\) and \(|S_n|=2^{n-2}\). Removing \(z\) leaves every interval type represented by a nonzero square-zero map, so the same full-column-rank argument applies with one fewer row. That gives the second formula. No finite experiments are used to justify arbitrary \(n\).

## Verification
The accompanying standalone `checker.py` constructs all weakly increasing order-decreasing self-maps of each chain independently for \(3\le n\le10\), then filters \(f\) by direct computation of \(f\circ f=z\). It constructs the commuting matrix by direct composition, tests the claimed interval-type equivalence for every ordered pair, separately constructs the interval matrix \(H_p\) and incidence matrix \(X\), and checks the exact integer equality \(A_n+I=XH_pX^{\mathsf T}\). It then numerically checks the inertia of both graphs and of \(H_p\) against the exact formulas. All eight configurations passed, as recorded in `checker_output.txt`, including \(256\) square-zero maps at \(n=10\). Numerical eigenvalue calculations are supporting checks only; the Schur-complement argument in the proof is exact for every integer \(n\ge3\).

Run `python3 checker.py` in an environment with Python 3 and NumPy. The expected final output line is `VERIFY_OK`.

## Relationship to prior work
Grensing and Mazorchuk (2012) treat the Catalan monoid as an algebraic and categorical object, providing the archival source for the chosen family. Toker (2021, especially Lemma 4.1) gives a mutual-zero-product criterion in the **larger** two-sided zero-divisor graph of the Catalan monoid and derives graph properties such as degree, clique number, chordality, and perfectness. The present commuting graph is the square-zero induced subsystem (together with a specified universal zero vertex), and the interval-intersection description is not claimed as an independent discovery of the broad zero-product criterion. What is asserted here is the exact inertia of its *shifted adjacency matrix* for all chain lengths, including the large \(-1\)-eigenspace and the precise positive/negative split.

Korkmaz and Ayık (2021) study generator ranks of bounded-potency nilpotent subsemigroups, rather than adjacency inertia. The public record “Exact generator rank of the square-zero ideal in Catalan transformation monoids” computes this same square-zero ideal's size and generating rank, not the shifted spectrum of commutation. The public record “Six rank-three theories of complete discrete-interval intersection graphs” studies first-order logical equivalence of the unduplicated interval graph; it supplies neither the matrix inertia formula nor its semigroup blow-up. Other published inverse-relation matrix-inertia results concern the different relation of mutual semigroup inverses, not commuting square-zero maps. These are comparisons of the mathematical assertions, not of title similarity.

## Limitations
The theorem gives the inertia of \(A_n+I\) but not the complete list of its nonzero eigenvalues, explicit characteristic polynomials, or ranks over finite fields. It does not give the spectrum of the full two-sided zero-divisor graph or the commuting graph on every Catalan transformation. Historically general results on interval-intersection matrices or graph blow-ups might subsume the Schur-complement calculation; the inspected primary literature and targeted searches do not eliminate this priority risk. The computational checks are limited to finite chain lengths and do not constitute a separate proof of the universal claim.

## References
1. A.-L. Grensing and V. Mazorchuk, “Categorification of the Catalan monoid,” initial arXiv version 12 November 2012, arXiv:1211.2597. https://arxiv.org/abs/1211.2597
2. K. Toker, “Zero-divisor graphs of Catalan monoid,” *Hacettepe Journal of Mathematics and Statistics* **50** (2021), 387–396, DOI: 10.15672/hujms.702478. Full text: https://dergipark.org.tr/en/download/article-file/1002929
3. E. Korkmaz and H. Ayık, “Ranks of nilpotent subsemigroups of order-preserving and decreasing transformation semigroups,” *Turkish Journal of Mathematics* **45** (2021), 1626–1634, DOI: 10.3906/mat-2008-19.
4. “Exact generator rank of the square-zero ideal in Catalan transformation monoids,” public research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-exact-generator-rank-of-the-square-zero-ideal-in-catalan-transfo--4699c0491091/RESULT.md
5. “Six rank-three theories of complete discrete-interval intersection graphs,” public research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-six-rank-three-theories-of-complete-discrete-interval-intersecti--7082ff1cf8a2/RESULT.md
