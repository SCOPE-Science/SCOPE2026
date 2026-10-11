# A sharp symmetry-only gate–loss tradeoff for binary-octahedral bosonic qubits
## Finding
Consider the two-mode binary-octahedral covariant encoding of arXiv:2609.26660v1 with physical representation \(\rho_4\) of \(2O\). For a two-dimensional logical representation \(\lambda\), define the symmetry-selection depth
\[
\delta(\lambda)=\min\left\{K+L>0:\operatorname{Hom}_{2O}\!\left(\operatorname{Sym}^K(\rho_4)\otimes\operatorname{Sym}^L(\rho_4^*),\operatorname{End}_0(\lambda)\right)\neq0\right\},
\]
where \(\operatorname{End}_0(\lambda)\) is the traceless logical-operator representation. Across the six two-dimensional logical representations listed in Table 3 of that paper,
\[
\begin{array}{c|cccccc}
\lambda&
\rho_1\oplus\rho_1&
\rho_1\oplus\rho_2&
\rho_2\oplus\rho_2&
\rho_3&
\rho_4&
\rho_5\\ \hline
\delta(\lambda)&2&2&2&4&2&2 .
\end{array}
\]

Consequently, \(\rho_3\) is the unique listed logical representation for which symmetry alone forces the Knill–Laflamme conditions for the complete one-photon-loss error set \(\{I,a_1,a_2\}\). The source assigns the projective logical gate group \(S_3\) to \(\rho_3\). The two irreducible choices \(\rho_4,\rho_5\), which instead carry the larger projective logical gate group \(S_4\), already admit a non-scalar logical sector at total creation/annihilation degree \(2\); therefore one-photon correction for those choices is not forced by symmetry and would require additional cancellation from the seed state. This is a symmetry-only obstruction, not a proof that suitably tuned \(\rho_4\)- or \(\rho_5\)-based codes cannot correct one photon.

No listed logical representation is symmetry-forced to correct every two-photon-loss error: for \(\rho_3\), the first permitted non-scalar sector appears at total degree \(4\), including the \((K,L)=(2,2)\) block.

## Assumptions and scope
The group is the binary octahedral group \(2O\), and the physical two-mode representation is the source paper's \(\rho_4\). Error monomials are graded exactly as in the source by
\[
\mathcal E_{K,L}=\operatorname{Sym}^K(\rho_4)\otimes\operatorname{Sym}^L(\rho_4^*).
\]
The logical choices are precisely the six two-dimensional representations in the source's Table 3. The result concerns what the group-representation selection rule forces before optimizing a coherent-state seed.

For a logical representation \(\lambda\), the QEC matrix associated with an error block is an equivariant map into \(\operatorname{End}(\lambda)\). Its scalar part is the span of the identity. Thus a block is forced to be scalar whenever it has no irreducible constituent in common with \(\operatorname{End}_0(\lambda)\). The definition of \(\delta(\lambda)\) records the first total error degree at which symmetry ceases to guarantee scalarity.

## Proof
The source proves that QEC matrices transform as group-representation morphisms. Hence Schur's lemma implies that an error sector \(\mathcal E_{K,L}\) can contribute a non-scalar logical operator only when it shares an irreducible constituent with \(\operatorname{End}_0(\lambda)\).

The source's \(2O\) character table and its physical choice \(\rho_4\) give
\[
\begin{aligned}
\operatorname{Sym}^0(\rho_4)&=\rho_1,\\
\operatorname{Sym}^1(\rho_4)&=\rho_4,\\
\operatorname{Sym}^2(\rho_4)&=\rho_6,\\
\operatorname{Sym}^3(\rho_4)&=\rho_8,\\
\operatorname{Sym}^4(\rho_4)&=\rho_3\oplus\rho_7 .
\end{aligned}
\]
The first mixed sectors are
\[
\begin{aligned}
\mathcal E_{1,1}&=\rho_1\oplus\rho_6,\\
\mathcal E_{1,2}&=\rho_4\oplus\rho_8,\\
\mathcal E_{1,3}&=\rho_3\oplus\rho_6\oplus\rho_7,\\
\mathcal E_{2,2}&=\rho_1\oplus\rho_3\oplus\rho_6\oplus\rho_7.
\end{aligned}
\]
These decompositions follow by exact character inner products. The source explicitly gives the same low-degree sectors used in its binary-octahedral analysis, including \(\mathcal E_{0,1}=\rho_4\), \(\mathcal E_{0,2}=\rho_6\), \(\mathcal E_{0,3}=\rho_8\), \(\mathcal E_{1,1}=\rho_1\oplus\rho_6\), and \(\mathcal E_{2,2}=\rho_1\oplus\rho_3\oplus\rho_6\oplus\rho_7\).

For the irreducible logical representations,
\[
\operatorname{End}_0(\rho_3)=\rho_2\oplus\rho_3,
\qquad
\operatorname{End}_0(\rho_4)=\rho_6,
\qquad
\operatorname{End}_0(\rho_5)=\rho_6.
\]
The first identity is also stated in the source's \(\rho_3\) analysis. The second follows from
\(\rho_4\otimes\rho_4^*=\rho_1\oplus\rho_6\). For the third, the character table gives \(\rho_5=\rho_2\otimes\rho_4\) with one-dimensional \(\rho_2\), so conjugation by \(\rho_5\) has the same operator representation as conjugation by \(\rho_4\).

Therefore neither \(\rho_2\) nor \(\rho_3\) occurs in any \(\mathcal E_{K,L}\) with \(K+L<4\), while \(\rho_3\) occurs at degree \(4\). Hence \(\delta(\rho_3)=4\). The constituent \(\rho_6\) already occurs in \(\mathcal E_{0,2}\) and \(\mathcal E_{1,1}\), while it does not occur at degrees \(0\) or \(1\), so
\[
\delta(\rho_4)=\delta(\rho_5)=2.
\]

For the reducible logical choices, extra non-scalar invariant operators occur in the trivial isotypic sector. Explicitly,
\[
\begin{aligned}
\operatorname{End}_0(\rho_1\oplus\rho_1)&=3\rho_1,\\
\operatorname{End}_0(\rho_1\oplus\rho_2)&=\rho_1\oplus2\rho_2,\\
\operatorname{End}_0(\rho_2\oplus\rho_2)&=3\rho_1.
\end{aligned}
\]
The literal block \(\mathcal E_{0,0}\) is excluded from the definition because its only physical operator is the identity. At positive degree, \(\mathcal E_{1,1}=\rho_1\oplus\rho_6\) contains the trivial irrep, so all three reducible choices have symmetry-selection depth \(2\). This is the representation-theoretic origin of the source's observation that reducibility allows a non-scalar logical invariant in the same isotypic sector as scalar no-jump terms.

Finally, the Knill–Laflamme products generated by \(\{I,a_1,a_2\}\) have \(K,L\le1\), hence total degree at most \(2\). Only \(\rho_3\) has \(\delta>2\), proving the uniqueness statement. For two-photon errors one must include \((K,L)=(2,2)\), and that sector already contains \(\rho_3\), so even \(\rho_3\) is not protected by this selection rule alone at that order.

## Verification
The bundled `verify.py` performs exact arithmetic in the character ring \(\mathbb Z[\sqrt2]\). It checks orthogonality of the eight \(2O\) irreducible characters, reconstructs symmetric powers of \(\rho_4\) through degree \(4\), decomposes every error sector needed above, reconstructs the traceless logical-operator representations, and returns the depth vector
\[
(2,2,2,4,2,2).
\]
The computation is a finite verification of the stated character decompositions. The logical conclusion is analytic and follows from the equivariance theorem and Schur's lemma; the script is not being used as evidence for an unbounded statement.

## Relationship to prior work
St-Amand, Burelle, and Royer develop the equivariant-QEC-matrix framework, give the binary-octahedral character table, enumerate the six two-dimensional logical representations and their projective logical gate groups, and analyze selected logical choices in detail. Their text highlights the adverse effect of reducible logical representations and explicitly studies \(\rho_3\), but it does not tabulate the first non-scalar error degree for all six Table-3 choices or state the resulting uniqueness of \(\rho_3\) for symmetry-forced one-photon correction.

Denys and Leverrier introduced the covariant bosonic-code construction that realizes single-qubit Clifford operations through Gaussian transformations. Kubischta and Teixeira subsequently formulated a broader intrinsic representation-theoretic viewpoint on quantum codes and intrinsic depth. Those frameworks support the general principle that symmetry sectors control error detection; the present statement is the specific binary-octahedral calculation for the new six-choice table and its gate-versus-loss consequence.

## Limitations
The theorem is deliberately about symmetry-forced error correction. If an allowed non-scalar intertwiner exists, a particular coherent-state seed can still make its coefficient vanish accidentally or by optimization. Thus \(\delta(\rho_4)=\delta(\rho_5)=2\) is not a no-go theorem for actual one-photon-correcting codes with those logical representations.

The result does not optimize fidelity, coherent-state amplitude, average photon number, or recovery maps. It also does not classify representations outside the six two-dimensional logical choices in Table 3. Earlier general representation-theoretic work may contain terminology equivalent to the abstract depth definition, but the exact \(2O\) six-choice vector and the resulting \(S_3\)-versus-\(S_4\) symmetry-only tradeoff were not found in the inspected sources.

## References
1. F. St-Amand, J.-P. Burelle, and B. Royer, *Error Correction Properties of Covariant Bosonic Encodings*, arXiv:2609.26660v1 (2026).
2. A. Denys and A. Leverrier, *Quantum Error-Correcting Codes with a Covariant Encoding*, Phys. Rev. Lett. 133, 240603 (2024), arXiv:2306.11621.
3. E. Kubischta and I. Teixeira, *Intrinsic Quantum Codes: One Code To Rule Them All*, arXiv:2511.14840 (2025).
4. E. Kubischta and I. Teixeira, *MacWilliams Identities for Intrinsic Quantum Codes*, arXiv:2604.16023 (2026).
