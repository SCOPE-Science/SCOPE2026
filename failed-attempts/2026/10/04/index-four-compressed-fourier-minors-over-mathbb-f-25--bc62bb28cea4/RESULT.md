# Index-four compressed Fourier minors over \(\mathbb F_{25}\)
## Finding
Let
\[
\mathbb F_{25}=\mathbb F_5(\alpha),\qquad \alpha^2=2,
\]
and let \(H\) be the unique index-\(4\) subgroup of \(\mathbb F_{25}^{\times}\), so \(|H|=6\). For a character
\[
\chi:H\longrightarrow\mathbb C^\times,
\]
consider the compressed Fourier matrix associated with the pair \((H,\chi)\).

The matrix has the nonvanishing-minors property exactly in the following cases:
\[
\operatorname{ord}(\chi)\in\{1,6\}.
\]
Thus the trivial character and the two faithful characters have the property, whereas both order-\(3\) characters and the unique order-\(2\) character fail it.

With a primitive element \(g=1+2\alpha\), \(H=\langle g^4\rangle\), and
\[
\chi_j(g^4)=\zeta_6^j,\qquad 0\le j\le5,
\]
the exact minor census is:
\[
\begin{array}{c|c|c|c}
j&\operatorname{ord}(\chi_j)&\text{matrix size}&\text{zero nonempty square minors}\\ \hline
0&1&5&0\\
1&6&4&0\\
2&3&4&10\\
3&2&4&34\\
4&3&4&10\\
5&6&4&0.
\end{array}
\]

## Assumptions and scope
The compressed Fourier transform and the nonvanishing-minors property are used in the sense of Garcia--Karaali--Katz and Díaz Padilla--Ochoa Arango. For a nontrivial character the compressed matrix has one row and column for each of the four nonzero \(H\)-orbits. For the trivial character the zero orbit is also included, giving a \(5\times5\) matrix.

The conclusion is only for the unique index-\(4\) subgroup of \(\mathbb F_{25}^{\times}\). It is not a classification of all index-\(4\) subgroups over arbitrary finite fields.

## Proof
Write
\[
\zeta=\exp(2\pi i/30).
\]
Since \(\zeta_6=\zeta^5\) and \(\zeta_5=\zeta^6\), every entry of every compressed matrix lies in the exact cyclotomic ring
\[
\mathbb Z[\zeta]\cong
\mathbb Z[X]\big/\left(X^8+X^7-X^5-X^4-X^3+X+1\right).
\]

Represent \(\mathbb F_{25}\) by pairs \(u+v\alpha\), with multiplication determined by \(\alpha^2=2\). The element
\[
g=1+2\alpha
\]
has order \(24\), so
\[
H=\langle g^4\rangle
\]
has order \(6\), and \(1,g,g^2,g^3\) represent its four nonzero multiplicative cosets. The absolute trace is
\[
\operatorname{Tr}_{\mathbb F_{25}/\mathbb F_5}(u+v\alpha)=2u.
\]

For \(0\le j\le5\), define \(\chi_j(g^{4t})=\zeta_6^{jt}\). Up to the harmless row and column normalizations in the standard compressed basis, the entry indexed by representatives \(r,s\) is
\[
M_j(r,s)=
\sum_{t=0}^{5}
\zeta_6^{jt}\,
\zeta_5^{\operatorname{Tr}(g^{4t}rs)}.
\]
Changing from \(\chi_j\) to its inverse only interchanges \(j\) with \(6-j\), so the stated classification by character order is independent of that convention.

The accompanying exact verifier constructs these matrices in \(\mathbb Z[\zeta]\), reduces every product modulo the displayed cyclotomic polynomial, and evaluates every nonempty square minor by the Leibniz determinant formula. There are \(251\) such minors in the \(5\times5\) trivial-character matrix and \(69\) in each \(4\times4\) nontrivial-character matrix. The exhaustive counts are exactly the six rows displayed above.

For the order-\(3\) characters, a concrete vanishing minor is obtained from row representatives \(1,g\) and column representatives \(1,g^3\). For the order-\(2\) character, the entry with row representative \(1\) and column representative \(g\) is already zero. Conversely, all \(251\) minors for the trivial character and all \(69\) minors for each faithful character are nonzero in the cyclotomic ring. This is exhaustive because all characters of the cyclic group \(H\) are the six \(\chi_j\).

## Verification
`verify.py` is a standalone exact-arithmetic replay. It checks that \(g\) has order \(24\), builds \(H\), constructs all six compressed Fourier matrices, and recomputes every square minor in the quotient ring by the cyclotomic polynomial of order \(30\). It uses integers only; no floating-point zero test is involved.

The expected terminal line is `VERIFY_OK`. The verified zero-minor counts are
\[
0,\ 0,\ 10,\ 34,\ 10,\ 0
\]
for \(j=0,1,2,3,4,5\), respectively.

## Relationship to prior work
Garcia, Karaali, and Katz introduced the compressed Fourier transform for \(\chi\)-symmetric functions and linked the nonvanishing-minors property to sharp uncertainty inequalities. Their non-prime-field results include the full multiplicative subgroup, index-\(2\) subgroups, and the index-\(3\) trivial-character case.

Díaz Padilla and Ochoa Arango explicitly continue that program for small-index subgroups. Their paper lists the previously known non-prime cases and then gives a characterization for index-\(3\) subgroups with nontrivial characters. The inspected full text does not treat index \(4\), and targeted searches for an index-\(4\) or \(\mathbb F_{25}\) compressed-Fourier minor classification found no covering result.

The present calculation gives a concrete next-index classification and shows a character-order split within one fixed subgroup: the trivial and faithful characters satisfy nonvanishing minors, while the intermediate orders do not.

## Limitations
This is a finite, exact classification for \(\mathbb F_{25}\), not a theorem for all fields with \(4\mid(q-1)\). The exhaustive certificate establishes the statement for the displayed field model; field isomorphism and representative-independence of the compressed transform make the NVM classification intrinsic to \(\mathbb F_{25}\) and \(H\).

The literature search cannot exclude an unindexed or differently phrased equivalent computation.

## References
1. D. F. Díaz Padilla and J. A. Ochoa Arango, "On an uncertainty principle for small index subgroups of finite fields," arXiv:2310.09992, first posted 16 October 2023.
2. S. R. Garcia, G. Karaali, and D. J. Katz, "An improved uncertainty principle for functions with symmetry," arXiv:1807.07648; Journal of Algebra 586 (2021), 899--934.
