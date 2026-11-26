# A two-qubit Rényi-2 counterexample to product-state entropy-diagram factorization
## Finding
Let \(H_2(p)=-\log_2\sum_i p_i^2\) be collision entropy. Consider the two-qubit computational measurement \(Z\otimes Z\) and the product Hadamard measurement \(X\otimes X\), whose basis-change matrix is
\[
U=H\otimes H,\qquad H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]
For
\[
|\psi\rangle=\frac{3|00\rangle-|01\rangle-|10\rangle+|11\rangle}{\sqrt{12}},
\]
the two measurement distributions are permutations of
\[
\left(\frac9{12},\frac1{12},\frac1{12},\frac1{12}\right),
\]
so both collision probabilities equal \(7/12\) and therefore
\[
\bigl(H_2^Z,H_2^X\bigr)=\left(\log_2\frac{12}7,\log_2\frac{12}7\right).
\]
By contrast, every product density state \(\rho_1\otimes\rho_2\) satisfies
\[
H_2^Z+H_2^X\geq \log_2\frac{256}{81}.
\]
The displayed entangled state has
\[
H_2^Z+H_2^X=\log_2\frac{144}{49}<\log_2\frac{256}{81},
\]
because \(49\cdot256>81\cdot144\). Thus no product state can share its entropy pair. Conjecture V.6 of arXiv:1509.00398, as written without a Rényi-duality restriction, is therefore false already for \(d=4\) and orders \((2,2)\).

## Assumptions and scope
The measurements are rank-one projective measurements on two qubits. The first is the computational basis and the second is obtained by applying a Hadamard on each qubit. Rényi logarithms use base \(2\). The comparison class is all product density operators \(\rho_1\otimes\rho_2\), including mixed local states. The conclusion concerns Conjecture V.6 exactly as stated in the source. The source notes that it *mostly* assumes dual Rényi parameters, but Conjecture V.6 itself does not impose duality and invokes additivity of Rényi entropy without such a restriction. No claim is made here about dual pairs or the Shannon case.

## Proof
Write a one-qubit density matrix by its Bloch vector \(r=(x,y,z)\), with \(x^2+y^2+z^2\leq1\). Its collision probabilities for the computational and Hadamard measurements are
\[
C_Z=\frac{1+z^2}2,\qquad C_X=\frac{1+x^2}2.
\]
Putting \(s=x^2+z^2\leq1\) and using \(x^2z^2\leq s^2/4\),
\[
C_ZC_X=\frac{1+s+x^2z^2}4
\leq\frac{1+s+s^2/4}4
\leq\frac9{16}.
\]
For a product state, both measurement distributions factor, so their collision probabilities multiply across the two qubits. Hence
\[
C_Z(\rho_1\otimes\rho_2)C_X(\rho_1\otimes\rho_2)
=\prod_{j=1}^2 C_Z(\rho_j)C_X(\rho_j)
\leq\left(\frac9{16}\right)^2=\frac{81}{256}.
\]
Because \(H_2=-\log_2 C\), this is equivalent to
\[
H_2^Z+H_2^X\geq-\log_2\frac{81}{256}=\log_2\frac{256}{81}.
\]

For the proposed state, computational probabilities are \((9,1,1,1)/12\), so \(C_Z=7/12\). Direct multiplication by \(H\otimes H\) gives
\[
(H\otimes H)|\psi\rangle
=\frac{|00\rangle+|01\rangle+|10\rangle+3|11\rangle}{\sqrt{12}},
\]
and thus \(C_X=7/12\) as well. Therefore its collision-product is \(49/144\), strictly larger than the product-state ceiling \(81/256\), since
\[
49\cdot256-81\cdot144=880>0.
\]
Equivalently its entropy sum is strictly smaller than every product-state entropy sum. Finally, the coefficient matrix of \(|\psi\rangle\) has determinant \(2/12\neq0\), so the state is entangled.

## Verification
The accompanying verifier reconstructs the Hadamard transform from exact integer arithmetic, checks normalization and both collision probabilities, checks entanglement by the nonzero coefficient determinant, and verifies the exact rational separation \(49/144>81/256\). The single-qubit ceiling is proved symbolically above for every Bloch vector, including mixed states; finite sampling is not used as a substitute for that argument.

## Relationship to prior work
Abdelkhalek et al., arXiv:1509.00398, define entropy diagrams for arbitrary fixed Rényi orders, solve the qubit problem, and state Conjecture V.6: when \(U=U_1\otimes U_2\), every state's entropy pair should be reproduced by a product state. Their text explicitly uses Rényi additivity as the consequence of this conjecture. The counterexample above targets that statement at \((2,2)\).

Schwonnek, arXiv:1801.04602, later proves additivity of optimal linear uncertainty bounds for **Shannon entropy** and product projective measurements. That theorem does not cover Rényi-2. The same paper remarks that arbitrary Schur-concave generalizations can fail and cites an unavailable private-communication Tsallis example; it does not supply the explicit Rényi-2 state, the exact \(81/256\) product ceiling, or an implication establishing the present claim.

## Limitations
This result does not refute the Shannon specialization, which is covered positively by the later additivity theorem. It also does not decide Conjecture V.6 if one repairs its statement by explicitly restricting to dual Rényi pairs. The result gives an exact separating witness, not a complete description of the two-qubit Rényi-2 entropy diagram.

## References
1. K. Abdelkhalek, R. Schwonnek, H. Maassen, F. Furrer, J. Duhme, P. Raynal, B.-G. Englert, and R. F. Werner, *Optimality of entropic uncertainty relations*, arXiv:1509.00398v1 (2015), DOI:10.1142/S0219749915500458.
2. R. Schwonnek, *Additivity of entropic uncertainty relations*, arXiv:1801.04602v4 (2018), DOI:10.22331/q-2018-03-30-59.
3. MSC2020 81S07, *Uncertainty relations, also entropic*.
