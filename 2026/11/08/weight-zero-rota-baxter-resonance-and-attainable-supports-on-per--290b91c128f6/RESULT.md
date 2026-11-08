# Weight-zero Rota–Baxter resonance and attainable supports on permutation evolution algebras

## Finding
Let \(K\) be a field, \(n\ge1\), \(\sigma\in S_n\), and \(a_1,\ldots,a_n\in K^\times\). Consider the evolution algebra \(E\) with natural basis \(e_1,\ldots,e_n\), \(e_ie_j=0\) for \(i\ne j\), and \(e_i^2=a_i e_{\sigma(i)}\). Its structure matrix is monomial and invertible, hence \(E^2=E\). A weight-zero Rota–Baxter operator is a \(K\)-linear map \(R:E\to E\) satisfying
\[
R(x)R(y)=R(R(x)y+xR(y))\qquad(x,y\in E).
\]
For each permutation cycle \(C\), call it *resonant* if \(2^{|C|}=1\) in \(K\), and let \(r\) be the number of resonant cycles. The following conclusions hold simultaneously:

1. For every weight-zero Rota–Baxter operator \(R\), the active set \(T_R=\{i:R(e_i)\ne0\}\) is a union of resonant cycles. Moreover, \(R(e_i)\ne0\) holds if and only if the coefficient of \(e_i\) in \(R(e_i)\) is nonzero.
2. Conversely, **every** union of resonant cycles occurs as \(T_R\) for some diagonal weight-zero Rota–Baxter operator. Consequently exactly \(2^r\) different active sets occur.
3. All diagonal weight-zero Rota–Baxter operators form a \(K\)-linear subspace of \(\operatorname{End}_K(E)\) of dimension \(r\), parametrized by one scalar per resonant cycle.
4. In characteristic zero and in characteristic two every weight-zero Rota–Baxter operator is zero. In odd characteristic \(p\), the resonant cycles are exactly those with length divisible by \(\operatorname{ord}_p(2)\).
5. If \(n\ge2\), the coefficients are \(a_i=1\), and \(\sigma\) is one resonant \(n\)-cycle, this same algebra has weight-zero Rota–Baxter operators of rank \(1\) and rank \(n\). In particular, the complete operator variety is not merely the diagonal subspace.

## Assumptions and scope
All statements hold over arbitrary fields, including finite fields and imperfect fields. The permutation may have fixed points and multiple cycles; every weight \(a_i\) is assumed nonzero. The active set is basis-independent up to the relabeling forced by a change of natural basis, because perfect evolution algebras have monomial natural-basis changes. The theorem classifies *supports and the diagonal solution locus*, not all off-diagonal solutions.

## Proof
Write \(R(e_i)=\sum_j r_{ji}e_j\), and set \(d_i=r_{ii}\). The Rota–Baxter identity applied to \(x=y=e_i\) reads
\[
\sum_j a_jr_{ji}^{\,2}e_{\sigma(j)}
  = 2a_i d_i\sum_j r_{j,\sigma(i)}e_j.\tag{1}
\]
Because \(\sigma\) is a permutation and every \(a_j\ne0\), the left side vanishes if and only if the entire \(i\)-th column of \(R\) vanishes. Thus \(d_i=0\) forces \(R(e_i)=0\), and the reverse implication is immediate. Comparing coefficients of \(e_{\sigma(i)}\) in (1) gives
\[
d_i^2=2d_i d_{\sigma(i)}.\tag{2}
\]
If \(\operatorname{char}K=2\), equation (2) gives \(d_i=0\) for all \(i\), hence \(R=0\). Otherwise, any active \(i\) has \(d_i\ne0\), and (2) implies
\[
d_{\sigma(i)}=\frac{d_i}{2}\ne0.\tag{3}
\]
Iterating (3) around the cycle \(C\) containing \(i\) yields \(d_i=2^{-|C|}d_i\), so \(2^{|C|}=1\) in \(K\). Consequently the active set is a union of resonant cycles; necessity is proved.

Conversely, for each resonant cycle \(C\), choose an anchor \(i_C\) and a scalar \(t_C\in K\). For \(0\le j<|C|\) set \(d_{\sigma^j(i_C)}=2^{-j}t_C\). On nonresonant cycles set \(d_i=0\). The assignment is consistent around each resonant cycle, and satisfies \(d_i=2d_{\sigma(i)}\). Define \(R_t(e_i)=d_ie_i\). If \(i\ne j\), both sides of the Rota–Baxter identity vanish, since \(R_t\) is diagonal. If \(i=j\), it reduces to
\[
a_i d_i^2 e_{\sigma(i)}=2a_id_i d_{\sigma(i)}e_{\sigma(i)},
\]
which holds. Therefore every choice of parameters gives a weight-zero Rota–Baxter operator; moreover every diagonal solution satisfies (2) and has this form. Each nonzero \(t_C\) activates precisely cycle \(C\), proving the \(2^r\) support count and dimension \(r\) of the diagonal solution subspace. Since \(2^L-1\) is a nonzero integer for all \(L\ge1\), there are no resonant cycles in characteristic zero, nor in characteristic two. In odd characteristic \(p\), resonance is the familiar divisibility condition \(\operatorname{ord}_p(2)\mid L\).

Finally, for an unweighted single cycle, index the basis by \(i\in\mathbb Z/n\mathbb Z\), let \(\lambda_i=2^{-i}\) (well-defined cyclically by resonance), and let \(v=\sum_i e_i\). Then \(v^2=v\) and \(v e_i=e_{\sigma(i)}\). The diagonal map \(D(e_i)=\lambda_i e_i\) is a full-rank operator as above. Define \(P(e_i)=\lambda_i v\). It has rank one and satisfies, for all basis indices,
\[
P(e_i)P(e_j)=\lambda_i\lambda_jv,
\quad
P(P(e_i)e_j+e_iP(e_j))
= (\lambda_i\lambda_{\sigma(j)}+\lambda_j\lambda_{\sigma(i)})v
=\lambda_i\lambda_jv.
\]
Thus both ranks are achieved. This completes the proof.

## Verification
The standalone `verify.py` independently evaluates the defining Rota–Baxter identities for each ordered pair of basis vectors. It exhaustively enumerates all \(p^{n^2}\) matrices in the five configurations \((n,p)=(2,2),(2,3),(2,5),(2,7),(3,3)\), and tests the support criterion for every solution. In the resonant case \((n,p)=(2,3)\) it finds exactly five operators: zero, two invertible diagonal operators, and two non-diagonal rank-one operators. It also constructs the diagonal maps for every permitted support on six weighted permutation examples with multiple cycles, and directly checks rank-one and full-rank maps on the unweighted three-cycle over \(\mathbb F_7\). The recorded output concludes `VERIFY_OK checks 22822`. Every calculation is finite; the proof above, not those experiments, establishes the general theorem.

## Relationship to prior work
The 2026 survey by Kaygorodov, Martín González and Viruel (arXiv:2610.22248v1, Question 39) asks for graph-theoretic classifications of Rota–Baxter operators on perfect evolution algebras. The present theorem answers the exact support-existence question and classifies the diagonal weight-zero locus for a natural graph family, without purporting to classify all operators. Qaralleh, Mukhamedov and Khakimov (arXiv:2601.08669v1) classify Rota–Baxter operators on **nilpotent** evolution algebras of maximal nilindex in characteristic zero, with acyclic triangular structure matrices. Those hypotheses exclude the present perfect permutation algebras. Ladra and Murodov (arXiv:1906.09098v1, Section 3 and Theorem 3.3) compute weight-zero operators in dimension two over \(\mathbb C\), covering the low-dimensional characteristic-zero context but not the modular cycle-support criterion. The equality of the diagonal recurrence with a familiar derivation-type recurrence does not by itself give a theorem about the supports of all potentially non-diagonal Rota–Baxter operators. Priority beyond these specific comparisons is not established by search alone.

## Limitations
This is not a classification of all Rota–Baxter matrices: off-diagonal solutions occur, as the rank-one example demonstrates. It does not address nonzero Rota–Baxter weights, perfect evolution algebras with non-monomial structure matrices, or ranks other than the two constructed extremes. The literature comparison does not rule out an equivalent theorem in obscure or inaccessible earlier work. The finite-field checker is corroboration only, not an infinite certificate. No independent audit has been performed.

## References
1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public: 2026-10-15), Question 39.
2. I. Qaralleh, F. Mukhamedov and O. Khakimov, *Rota-Baxter operators of nilpotent evolution algebras with maximal nilindex*, arXiv:2601.08669v1 (first public: 2026-01-13), Sections 2–4.
3. M. Ladra and Sh. N. Murodov, *On chains and Rota-Baxter operators of evolution algebras*, arXiv:1906.09098v1 (2019), Section 3, Theorem 3.3.
