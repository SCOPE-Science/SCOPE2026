# Exact rank and nullspace of quadratic-product Fourier kernels over prime-square rings

## Finding
Fix an odd prime \(p\), write \(R=\mathbb Z/p^2\mathbb Z\), and choose any \(a,b\in R^\times\). Let \(\zeta=\exp(2\pi i/p^2)\) and define the \(p^2\)-by-\(p^2\) complex matrix
\[
H_{a,b}(s,t)=\zeta^{a st+b(st)^2},\qquad s,t\in R.
\]
Then the **exact rank and nullity**, independently of the two unit coefficients, are
\[
\boxed{\operatorname{rank}_{\mathbb C}H_{a,b}=p^2-\frac{(p-1)^2}{2}=\frac{p^2+2p-1}{2}},\qquad
\boxed{\dim\ker H_{a,b}=\frac{(p-1)^2}{2}}.
\]
There is also an explicit orthogonal character basis of the kernel. Let \(U=R^\times\), \(K=1+pR\), and for \(\chi\in\widehat U\) let \(r_\chi\in\mathbb F_p\) be characterized by
\[
\chi(1+ph)=\exp(2\pi i r_\chi h/p),\quad h\in\mathbb F_p.
\]
For each \(\chi\), define \(v_\chi\in\mathbb C^R\) by \(v_\chi(t)=\chi(t)\) on \(U\) and \(v_\chi(t)=0\) otherwise. Then an orthogonal basis of \(\ker H_{a,b}\) is the collection of \(v_\chi\) such that
\[
\boxed{\left(\frac{a^2-8b r_\chi}{p}\right)=-1},
\]
where the Legendre symbol is evaluated on coefficients reduced modulo \(p\). In particular, the missing signal directions are exactly the unit-supported multiplicative character modes corresponding to a nonsquare stationary discriminant.

## Assumptions and scope
All arithmetic inside the phase is performed modulo \(p^2\); \(R\) is a ring, not the field of size \(p^2\). Both \(a\) and \(b\) must be units. No scalar normalization is used; multiplying the matrix by a nonzero scalar does not affect its rank or kernel. The Legendre symbol takes values \(-1,0,1\); the displayed basis includes only \(-1\). Character orthogonality refers to the multiplicative group \(U\), of order \(p(p-1)\). This is an exact all-odd-prime theorem, not an assertion about higher prime-power exponents or a bound on nonzero singular values.

## Proof
**1. Multiplicative-character decomposition.** Put \(P(x)=ax+bx^2\) and \(e_m(x)=\exp(2\pi i x/m)\). Partition \(R\) into the units \(U\), the nonzero elements \(p\mathbb F_p^\times\), and \(\{0\}\). The kernel depends only on the product \(st\), so multiplication by units on the column variable and inverse multiplication on the row variable intertwine the matrix. On unit-supported character vectors, the unit-to-unit block acts, up to inversion of the character, by the scalar
\[
L_\chi=\sum_{u\in U}\chi(u)e_{p^2}(P(u)).\tag{1}
\]
For characters nontrivial on \(K=1+pR\), both the row-to-nonunit and nonunit-to-row couplings vanish by orthogonality on \(K\). Thus each such \(\chi\) contributes exactly one one-dimensional block, zero precisely when \(L_\chi=0\).

**2. Exact stationary calculation.** Since \(p\) is odd, \(U\) splits as a product of the Teichmüller subgroup \(W\) of order \(p-1\) and \(K\). For each \(x\in\mathbb F_p^\times\), let \(w_x\in W\) be its unique lift. Expand at \(u=w_x(1+ph)\):
\[
P(u)\equiv P(w_x)+p h x(a+2bx)\pmod {p^2}.
\]
Summing over \(h\in\mathbb F_p\) gives the **exact identity**
\[
L_\chi=p\sum_{\substack{x\in\mathbb F_p^\times\\2bx^2+ax+r_\chi=0}}
\chi(w_x)e_{p^2}(P(w_x)).\tag{2}
\]
The discriminant is \(\Delta=a^2-8b r_\chi\). For \(r_\chi=0\), one solution of the quadratic is zero and the other \(-a/(2b)\) is a unit; hence (2) has exactly one summand. A repeated nonzero root also gives one nonvanishing summand. If \(\Delta\) is a nonsquare, (2) is empty, so \(L_\chi=0\).

If there are two distinct nonzero roots \(x,y\), the two terms in (2) cannot cancel. Indeed, both \(\chi(w_x)\) and \(\chi(w_y)\) have order dividing \(p-1\). Cancellation would force \(e_{p^2}(P(w_x)-P(w_y))\) to have order coprime to \(p\), hence to be \(1\). But from \(x+y=-a/(2b)\) one gets
\[
P(w_x)-P(w_y)\equiv(x-y)(a+b(x+y))=\frac{a}{2}(x-y)\ne0\pmod p,
\]
a contradiction. Therefore \(L_\chi=0\) **if and only if** \(\Delta\) is nonsquare.

**3. The lower-conductor blocks are invertible.** A character with \(r_\chi=0\) factors through \(\mathbb F_p^\times\). For each nontrivial such character, the unit and nonzero-multiple-of-\(p\) sectors form a \(2\)-by-\(2\) block. Both cross entries are nonzero multiples of a finite-field Gauss sum \(\sum_{x\ne0}\chi(x)e_p(ax)\), whose modulus equals \(\sqrt p\). The nonunit-to-nonunit entry vanishes because that submatrix consists entirely of ones. The block therefore has nonzero determinant, independently of its unit-to-unit entry.

For the trivial character, there are three sectors: constant functions on \(U\), on \(p\mathbb F_p^\times\), and at \(0\). In these (unnormalized indicator) bases the block is
\[
\begin{pmatrix}
T&-1&1\\
-p&p-1&1\\
p(p-1)&p-1&1
\end{pmatrix},\qquad T=\sum_{u\in U}e_{p^2}(P(u)).
\]
Its determinant is exactly \(-p^3\ne0\). Thus no lower-conductor character contributes to the kernel.

**4. Counting all missing modes.** As \(r\) runs over \(\mathbb F_p\), \(a^2-8br\) runs bijectively through \(\mathbb F_p\). Exactly \((p-1)/2\) values are nonsquares. Every such \(r\) has precisely \(p-1\) extensions to characters of \(U\), by freely choosing the character on \(W\). Their unit-supported vectors are pairwise orthogonal. Steps 1–3 show that these and only these vectors lie in the kernel; their number is \((p-1)^2/2\). Subtraction from the matrix size \(p^2\) gives the asserted rank.

## Verification
Run `python3 CHECKER.py` with Python 3 and NumPy. The verifier checks the stationary discriminant and the two-root noncancellation congruence using exact integer arithmetic for 140 parameter cases over odd primes through 151. It independently assembles the entire complex matrix and checks its numerical SVD rank in 20 cases (primes \(3,5,7,11,13\), four unit-coefficient pairs each), with a recorded separation between zero and positive singular values. The marker is `QUADRATIC_PRODUCT_RANK_CHECK_PASS`. Finite tests corroborate but do not prove the theorem; the all-prime conclusion is the preceding character calculation.

## Relationship to prior work
Kelmer's study of multiplicatively twisted Kloosterman sums over prime-power rings (arXiv:0801.4162, especially Proposition 2.1 and the proof of Theorem 1) provides the closely related local stationary-phase technique. Its phase is \(a u+b u^{-1}\), not the quadratic polynomial \(a u+b u^2\), and its asymptotic equidistribution theorem is not an exact rank-and-kernel theorem for the matrix defined here. The stationary-phase technique itself is not claimed as new. Iosevich and Koh's quadratic-surface restriction paper (arXiv:0804.4505) concerns Fourier extension bounds on finite fields, rather than nonlinear critical sampling on a nonreduced cyclic ring.

Published work on prime-square Fourier minors and on parabolic extension over prime-square rings concerns the *ordinary* Fourier matrix or fourth moments of a two-frequency extension operator, respectively; neither implies the rank of the present quadratic-product matrix. The exact novelty claim is the all-prime rank defect and its full discriminant-indexed nullspace, not a new character-orthogonality or Gauss-sum identity.

## Limitations
The theorem does not determine individual nonzero singular values, numerical stability on the surviving subspace, or ranks for arbitrary coefficients that are not units. It is specifically about exponent two in the ring \(\mathbb Z/p^2\mathbb Z\); higher prime-power levels have additional stationary behavior. Although direct overlap searches did not identify the precise claim, an older generalized prime-power stationary-phase or matrix-kernel classification could contain an equivalent statement. Independent mathematical review has not been performed.

## References
1. D. Kelmer, *Distribution of twisted Kloosterman sums modulo prime powers*, arXiv:0801.4162, initially public 2008-01-27, especially Section 2. https://arxiv.org/abs/0801.4162
2. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505, initially public 2008-04-28. https://arxiv.org/abs/0804.4505
3. B. Alexeev, J. Cahill, and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first submitted 2011-10-17 (background on Fourier minors, not on this nonlinear sampling kernel). https://arxiv.org/abs/1110.3548
