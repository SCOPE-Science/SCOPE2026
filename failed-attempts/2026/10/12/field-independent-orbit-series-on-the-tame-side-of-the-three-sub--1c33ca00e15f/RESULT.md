# Field-independent orbit series on the tame side of the three-subspace boundary

## Finding
Let \(K\) be any field and let \(N_d(K)\) be the number of \(\operatorname{GL}_d(K)\)-orbits on ordered triples
\[
(U_1,U_2,U_3)
\]
of linear subspaces of \(K^d\). Then \(N_d(K)\) is independent of \(K\). Writing the common value as \(N_d\),
\[
\boxed{
N_d=\sum_{j=0}^{\lfloor d/2\rfloor}\binom{d-2j+7}{7}
}
\]
and
\[
\boxed{
\sum_{d\ge 0}N_d z^d=\frac{1}{(1-z)^8(1-z^2)}.
}
\]
Consequently
\[
N_d=\frac{d^8}{2\cdot 8!}+O(d^7).
\]

The first values are
\[
1,\ 8,\ 37,\ 128,\ 367,\ 920,\ 2083,\ 4352,\ 8518,\ 15792.
\]

This gives an exact finite-dimensional orbit-growth invariant on the tame side of the sharp three-versus-four distinguished-subspace boundary emphasized by Laskowski and Ulrich: over a field, three distinguished subspaces have only countably many countable models, whereas four distinguished subspaces already give a Borel-complete class.

## Assumptions and scope
The triples are ordered, and equivalence is simultaneous transport by one invertible linear map of the ambient space. No finiteness assumption is placed on the field. The formula concerns finite ambient dimension \(d\); it does not claim a new classification of arbitrary infinite-dimensional triples.

The argument uses the classical three-subspace problem. An ordered triple of subspaces is the same as an injective representation of the inward \(D_4\) quiver, with the three leaf maps realized as inclusions into the central ambient vector space.

## Proof
The \(D_4\) quiver has twelve indecomposable finite-dimensional representations, and exactly three of them are noninjective. Hence the subspace problem has nine injective indecomposable types.

Eight of these have one-dimensional ambient space. They are indexed by subsets \(S\subseteq\{1,2,3\}\): the ambient space is \(K\), and
\[
U_i=
\begin{cases}
K,& i\in S,\\
0,& i\notin S.
\end{cases}
\]
The ninth is the two-dimensional generic block
\[
K^2;\qquad
U_1=\langle e_1\rangle,\quad
U_2=\langle e_2\rangle,\quad
U_3=\langle e_1+e_2\rangle.
\]

By Krull--Schmidt, every finite-dimensional triple decomposes uniquely up to isomorphism as a direct sum of these nine blocks. Thus an isomorphism type is specified by multiplicities
\[
(m_S)_{S\subseteq\{1,2,3\}}\in\mathbb N^8
\quad\text{and}\quad
g\in\mathbb N,
\]
with ambient dimension constraint
\[
\sum_S m_S+2g=d.
\]
For fixed \(g=j\), the eight one-dimensional multiplicities form a weak composition of \(d-2j\) into eight parts, giving
\[
\binom{d-2j+7}{7}
\]
possibilities. Summing over \(0\le j\le\lfloor d/2\rfloor\) proves the formula.

The generating function is the direct product of the eight weight-one multiplicity series and the one weight-two multiplicity series:
\[
\left(\frac{1}{1-z}\right)^8\frac{1}{1-z^2}.
\]
Near \(z=1\), this is
\[
\frac{1}{2(1-z)^9}\bigl(1+O(1-z)\bigr),
\]
so coefficient asymptotics give
\[
N_d=\frac{1}{2}\binom{d+8}{8}+O(d^7)
=\frac{d^8}{2\cdot8!}+O(d^7).
\]

The decomposition also yields a concrete dimension-theoretic readout of the nine multiplicities. For distinct \(i,j,k\in\{1,2,3\}\),
\[
m_\varnothing=\dim K^d/(U_1+U_2+U_3),
\]
\[
m_{\{1,2,3\}}=\dim(U_1\cap U_2\cap U_3),
\]
\[
m_{\{i,j\}}
=\dim\frac{U_i\cap U_j}{U_1\cap U_2\cap U_3},
\]
\[
m_{\{i\}}
=\dim\frac{U_i}{U_i\cap(U_j+U_k)},
\]
and the generic multiplicity is
\[
g=
\dim\frac{U_1\cap(U_2+U_3)}
{(U_1\cap U_2)+(U_1\cap U_3)}.
\]
On each of the nine indecomposable blocks these expressions pick out exactly the corresponding multiplicity, so additivity under direct sums recovers the full canonical data.

## Verification
A standalone exact checker independently enumerates every linear subspace of \(\mathbb F_2^d\), every element of \(\operatorname{GL}_d(\mathbb F_2)\), and every ordered triple of subspaces for \(0\le d\le3\). It computes the orbit counts
\[
1,\ 8,\ 37,\ 128,
\]
exactly matching the formula.

The same checker independently extracts the first \(101\) coefficients of
\[
\frac{1}{(1-z)^8(1-z^2)}
\]
and compares them with the binomial-sum formula. It returns

`VERIFY_OK 4340 exact assertions`.

This computation is a finite replay, not the proof of the field-independent theorem; the proof is the \(D_4\) indecomposable classification plus Krull--Schmidt.

## Relationship to prior work
Laskowski and Ulrich prove that left modules with four distinguished submodules are Borel complete and explicitly note that, when the ring is a field, three distinguished submodules instead have only countably many countable models. They cite the representation theory of quivers and the classical subspace problem for the latter fact. Their paper contains no occurrence of “orbit” and does not state a finite-dimensional orbit enumerator or generating function.

The classical \(D_4\) solution of the three-subspace problem is prior mathematics. Expository treatments list twelve \(D_4\) indecomposables and note that exactly three are noninjective, leaving the nine blocks used here. The contribution isolated here is the exact graded orbit series, its field-independence, and its polynomial asymptotic, presented as a quantitative finite-dimensional invariant of the tame side of the modern Borel-complexity threshold.

Targeted searches for an orbit-count formula, the rational generating function, and equivalent binomial sums did not locate an explicit statement.

## Limitations
The result is a short consequence of the classical three-subspace classification, so unindexed folklore or an implicit generating-series computation in older representation-theory literature remains a substantial originality risk. The formula does not address four subspaces, where parameter families already arise in finite dimension, nor does it provide a new proof of the Borel-completeness result.

## References
1. M. C. Laskowski and D. S. Ulrich, *Borel complexity of modules*, arXiv:2209.06898, first submitted 14 September 2022; Annals of Pure and Applied Logic 177 (2026), 103780, DOI 10.1016/j.apal.2026.103780.
2. M. Prest, *Model Theory and Modules*, London Mathematical Society Lecture Note Series 130, Cambridge University Press, 1988; see the subspace problem cited by Laskowski--Ulrich.
3. J. Baez, *Free Modular Lattice on 3 Generators*, Visual Insight, American Mathematical Society, 2016, for an expository \(D_4\) list distinguishing the nine injective indecomposables from the three noninjective ones.
