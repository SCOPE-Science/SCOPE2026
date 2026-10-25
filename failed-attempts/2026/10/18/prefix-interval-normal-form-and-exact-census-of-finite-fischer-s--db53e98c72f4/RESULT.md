# Prefix-interval normal form and exact census of finite Fischer–Servi chain frames

## Finding
Let \(C_n=\{0<1<\cdots<n-1\}\) for every integer \(n\geq1\). Write \(A_i=\{j:iRj\}\). On this chain, the Fischer–Servi conditions
\[
(\leq\circ R)\subseteq(R\circ\leq),\qquad (R\circ\geq)\subseteq(\geq\circ R)
\]
are equivalent to the following normal form: (i) the nonempty rows \(A_i\) form an initial segment of the list of rows, (ii) their minima are nondecreasing, and (iii) every prefix union \(U_i=\bigcup_{j\leq i}A_j\) is either empty or an initial interval \(\{0,\ldots,M_i\}\).

This yields an exact recurrence for the number \(F_n\) of such relations, with
\[
(F_1,F_2,F_3,F_4,F_5,F_6,F_7,F_8)=(2,9,118,4849,697066,378458905,798895662718,6646002156252993).
\]
Moreover \(2^{(n-1)^2}\leq F_n\leq2^{n^2}\), so \(\lim_{n\to\infty}\log_2(F_n)/n^2=1\). The finite-chain duality in the reference identifies these labelled frames with Fischer–Servi modal expansions of the corresponding \((n+1)\)-element Gödel algebra.

## Assumptions and scope
Relational composition is read left to right: \(x(S\circ T)z\) means \(xSy\) and \(yTz\) for some \(y\). The order on \(C_n\) is the displayed total order. The count distinguishes relations on this fixed chain; its only order automorphism is the identity. We do not count arbitrary forest frames or frames satisfying additional Dunn conditions.

## Proof
For (FS1), if \(i\leq j\) and \(k\in A_j\), the witness on the right of \((\leq\circ R)\subseteq(R\circ\leq)\) exists precisely when \(A_i\) has an element at most \(k\). Thus a later nonempty row forces all earlier rows nonempty and requires \(\min A_i\leq\min A_j\). This is also sufficient. For (FS2), \(i(R\circ\geq)k\) means \(k\leq j\) for some \(j\in A_i\), whereas \(i(\geq\circ R)k\) means \(k\in A_l\) for some \(l\leq i\). Hence (FS2) is equivalent to downward closure of \(U_i\) for every \(i\), and finite-chain downsets are precisely initial intervals.

The recurrence uses a live state \((a,M)\), where \(a\) is the minimum of the last nonempty row, \(M\) is the right endpoint of the current prefix union, and initially \((a,M)=(0,-1)\). For each live state, an empty next row contributes exactly one terminal continuation (all remaining rows are forced empty). A nonempty next row \(S\subseteq C_n\) is allowed exactly when
\[
\min S\geq a,\qquad [0,\max(M,\max S)]=[0,M]\cup S,
\]
interpreting \([0,-1]=\varnothing\). Its new live state is \((\min S,\max(M,\max S))\). Starting with weight one at \((0,-1)\), sum terminal weights after \(n\) steps and all live weights after the last step. Each valid relation gives exactly one path, so the recurrence is exact, not an experimental extrapolation.

For the lower bound, require \(A_0=C_n\) and require \(0\in A_i\) for every \(i>0\), leaving the remaining \(n-1\) positions of each later row arbitrary. These \(2^{(n-1)^2}\) relations satisfy the normal form. The upper bound is the total number \(2^{n^2}\) of binary relations. Dividing logarithms by \(n^2\) gives the limit.

## Verification
The standalone file `verify.py` executes the transfer recurrence through \(n=8\), and independently tests both defining inclusions for all \(2^{n^2}\) relations at each \(n\leq4\). The counts at \(n\leq4\) agree exactly. The full proof applies at every \(n\); these finite checks are not its substitute.

## Relationship to prior work
Flaminio, Godo, Menchón and Rodriguez (arXiv:2110.02528v1, 6 October 2021), Definition 6.1, supply the two Fischer–Servi frame conditions and prove their modal-algebra representation, including recovery of the frame (Proposition 6.3). Their study also cites earlier IK- and HK1-frame dualities. The present contribution is the chain-specific row/prefix-union normal form, explicit exact transfer census, and asymptotic entropy statement; these are not asserted to be independent of the underlying representation theory. Searches also covered the names IK-frame, HK1-frame, interval union, and Ferrers descriptions.

## Limitations
This is a self-reviewed mathematical argument, not an independent validation or priority certificate. The possible existence of an earlier equivalent enumeration under alternate terminology remains a priority risk. The recurrence counts all labelled admissible frame relations, not just inequivalent presentations under nontrivial forest automorphisms. A closed-form expression or precise subquadratic correction to \(\log_2 F_n\) is not established.

## References
1. T. Flaminio, L. Godo, P. Menchón and R. O. Rodriguez, *Algebras and relational frames for Gödel modal logic and some of its extensions*, arXiv:2110.02528v1 (2021-10-06), Section 6.1, Definition 6.1 and Proposition 6.3. https://arxiv.org/html/2110.02528v3
2. A. Palmigiano, *Dualities for Intuitionistic Modal Logics* (2004), identified as earlier IK-frame duality in reference [29] of reference 1.
3. E. Orłowska and I. Rewitzky, *Discrete Dualities for Heyting Algebras with Operators*, Fundamenta Informaticae 81 (2007), identified as earlier HK1-frame duality in reference [28] of reference 1.
