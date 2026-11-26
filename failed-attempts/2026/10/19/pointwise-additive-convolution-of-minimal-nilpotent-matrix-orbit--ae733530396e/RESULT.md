# Pointwise additive convolution of minimal nilpotent matrix orbits over finite fields

## Finding

Let \(q\) be a prime power and \(n\ge 2\). The minimal nonzero nilpotent conjugacy orbit in \(M_n(\mathbb F_q)\) is
\[
\mathcal O=\{A\in M_n(\mathbb F_q):\operatorname{rank}A=1,\ A^2=0\}.
\]
For each prescribed matrix \(C\), set
\[
F(C)=\#\{(A,B)\in\mathcal O^2:A+B=C\},\qquad
H=\frac{(q^n-1)(q^{n-1}-1)}{q-1}.
\]
Then \(|\mathcal O|=H\), and the following exhaustive, disjoint cases give the **pointwise self-convolution** \(1_{\mathcal O}*1_{\mathcal O}\) of the orbit indicator under matrix addition.

1. If \(C=0\), then \(F(C)=H\).
2. If \(\operatorname{rank}C=1\) and \(C^2=0\), then \(F(C)=2q^{n-1}-q-2\). This includes the zero-fiber boundary \(n=q=2\).
3. If \(\operatorname{rank}C=2\), \(\operatorname{tr}C=0\) and \(C^2=0\), then \(F(C)=q(q+1)\). Such a target requires \(n\ge4\).
4. If \(\operatorname{rank}C=2\), \(\operatorname{tr}C=0\) and \(\operatorname{rank}(C^2)=1\), then \(F(C)=2q\). Such a target has nilpotent Jordan type \((3,1^{n-3})\) and requires \(n\ge3\).
5. Suppose \(\operatorname{rank}C=\operatorname{rank}(C^2)=2\) and \(\operatorname{tr}C=0\). Set \(W=\operatorname{im}C\), let \(T=C|_W\in\operatorname{GL}(W)\), and define \(c=-\det T\in\mathbb F_q^\times\). Then:
   * In odd characteristic, \(F(C)=q-1\) when \(c\) is a square and \(F(C)=q+1\) when \(c\) is a nonsquare.
   * In characteristic two, \(F(C)=0\) if \(T\) is scalar, and \(F(C)=q\) if \(T\) is nonscalar (equivalently, one Jordan block for its unique nonzero eigenvalue).
6. In every other case, \(F(C)=0\).

Thus this is an exact formula for **every** matrix \(C\) and **every** finite field. The characteristic-two scalar exclusion is essential: a nonscalar invertible trace-zero restriction is representable, while a scalar one is not.

For example, in \(M_3(\mathbb F_3)\) the nonzero-fiber size distribution is: one target of fiber size \(104\), \(104\) targets of fiber size \(13\), \(624\) of size \(6\), \(702\) of size \(4\), and \(1404\) of size \(2\). Their weighted sum equals \(104^2=10816\), the number of ordered summand pairs.

## Assumptions and scope

The ambient matrix dimension \(n\) is an integer at least \(2\), and \(q\) is any prime power. Matrix rank, trace, powers, image, and determinants are over \(\mathbb F_q\). Only **nonzero rank-one square-zero** summands are allowed; the zero matrix is not a summand. Pairs are ordered. A rank-two case with impossible dimension is vacuous. The quadratic character is used only in odd characteristic; here "square" means a nonzero square in \(\mathbb F_q\).

The restriction \(T=C|_W\) in case 5 is well-defined because \(W=\operatorname{im}C\) is \(C\)-invariant. Indeed, \(\operatorname{rank}C^2=2\) makes \(T\) invertible. The determinant is taken on the two-dimensional space \(W\) and is basis independent.

## Proof

**Step 1 (orbit size and rank restriction).** Every \(A\in\mathcal O\) admits a factorization \(A=u\varphi\) with a nonzero column \(u\), a nonzero linear functional \(\varphi\), and \(\varphi(u)=0\). Two such pairs define the same matrix precisely when they differ by \((u,\varphi)\mapsto(su,s^{-1}\varphi)\) for \(s\in\mathbb F_q^\times\). Counting gives \(H\) as stated. Every sum of two members has rank at most two and trace zero. For \(C=0\), each \(A\in\mathcal O\) uniquely determines the partner \(B=-A\), so \(F(0)=H\).

**Step 2 (rank one).** Fix \(C=u_0\varphi_0\in\mathcal O\). If rank-one matrices \(A\) and \(B\) sum to rank one, either their image lines coincide or their row-functional lines coincide. In the first case both images equal \(\mathbb F_qu_0\), and \(A=u_0\varphi\), \(B=u_0(\varphi_0-\varphi)\) with \(\varphi(u_0)=0\). Requiring both summands nonzero gives \(q^{n-1}-2\) possibilities. In the second case both row-functional lines coincide with that of \(C\), giving another \(q^{n-1}-2\) possibilities. Their intersection consists precisely of \(A=sC\), \(B=(1-s)C\) with \(s\in\mathbb F_q\setminus\{0,1\}\), so it has size \(q-2\). Inclusion–exclusion proves the stated rank-one fiber. A non-nilpotent rank-one target has nonzero trace and hence no representation.

**Step 3 (rank two and exchange lines).** Let \(C\) have rank two and put \(W=\operatorname{im}C\). If \(C=A+B\) with \(A,B\in\mathcal O\), their image lines \(L=\operatorname{im}A\) and \(M=\operatorname{im}B\) are distinct and satisfy \(W=L\oplus M\). Denote by \(\pi_L\) and \(\pi_M\) the projections of \(W\) onto the respective lines along the other. Then necessarily
\[
A=\pi_L C,\qquad B=\pi_M C.
\]
Conversely, each ordered complementary pair \((L,M)\) yields these two rank-one nonzero operators. They are square-zero exactly when
\[
T(L)\subseteq M,\qquad T(M)\subseteq L,
\qquad T=C|_W.
\]
These are the two zero diagonal entries of the \(2\)-by-\(2\) matrix of \(T\) in a basis adapted to \((L,M)\). Hence \(\operatorname{tr}T=\operatorname{tr}C=0\) is necessary; once it holds, making the first diagonal entry vanish also makes the second vanish.

**Step 4 (counting all complementary pairs).** The map \(C:V\to W\) is surjective, so \(\operatorname{rank}T=\operatorname{rank}C^2\). If \(T=0\), every ordered decomposition of the two-space \(W\) into two lines works: there are \((q+1)q\). If \(T\) is nonzero of rank one and trace zero, then \(T\) is nilpotent with one-dimensional kernel \(K\). Taking \(L=K\) permits \(q\) choices of its complement \(M\). For each of the other \(q\) lines \(L\), the unique choice is \(M=T(L)=K\). The total is \(2q\).

If \(T\) is invertible, every admissible \(L\) must be non-invariant, and for each such \(L\) there is exactly one choice \(M=T(L)\). Therefore
\[
F(C)=(q+1)-e(T),
\]
where \(e(T)\) is the number of eigenlines of \(T\) over \(\mathbb F_q\). Cayley–Hamilton and \(\operatorname{tr}T=0\) give \(T^2=cI_W\) with \(c=-\det T\ne0\). For odd \(q\), there are two eigenlines if \(c\) is square and no eigenlines if it is nonsquare. For even \(q\), \(X^2-c=(X-\sqrt c)^2\), so a scalar \(T\) has \(q+1\) eigenlines and a nonscalar \(T\) has exactly one. These yield all advertised fiber sizes and the scalar exclusion.

If \(\operatorname{rank}C>2\) or \(\operatorname{tr}C\ne0\), Step 1 rules out a representation. If \(\operatorname{rank}C=2\), Steps 3–4 cover all ranks \(0,1,2\) of \(T\). This exhausts the matrix space and proves the theorem.

## Verification

A standalone pure-Python enumerator, `verify_fibers.py`, constructs **actual matrices** \(A=u\varphi\) with \(A^2=0\), forms every ordered sum, and compares all observed fibers against a separately implemented rank/trace/eigenline calculation. Full target-space exhaustions were completed for \((n,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2)\). Arithmetic over \(\mathbb F_4\) uses its polynomial representation. In each case the mass identity \(\sum_C F(C)=H^2\) held and every target matched. This is finite corroboration; the general theorem rests on the proof above.

## Relationship to prior work

Wang–Wu and Botha's characterization of sums of two unrestricted square-zero endomorphisms is recalled as Theorem 1.2 in de Seguins Pazzis [1]. That theorem determines when a decomposition exists, but imposes no rank-one restriction and supplies no pointwise finite-field multiplicities. Hua [2] counts simultaneous-conjugacy orbits of general nilpotent matrix tuples; his orbit-counting problem does not prescribe the sum of two rank-one summands. Danchev–García–Gómez Lozano [3] study the different decomposition into a potent and a square-zero summand. The result here instead evaluates the additive self-convolution of the **single minimal nilpotent orbit**. The related two-step transvection product class law concerns matrix multiplication and aggregated conjugacy classes; it does not determine additive prescribed-target fibers, notably their square/nonsquare and characteristic-two scalar distinctions.

## Limitations

The theorem does not count representations by arbitrary-rank square-zero matrices, by more than two summands, or over general finite local rings. The formula is a finite-field point count and does not claim scheme-theoretic fiber structure. Scientific priority outside the inspected literature cannot be guaranteed; in particular, an equivalent orbital convolution in older finite-group or representation-theoretic literature remains possible. Independent audit has not been performed.

## References

[1] Clément de Seguins Pazzis, *Sums and products of two quadratic endomorphisms of a countable-dimensional vector space*, arXiv:2107.04273 (first posted 2021-07-09), especially the finite-dimensional Theorem 1.2 and discussion of the exchange property. https://arxiv.org/abs/2107.04273

[2] Jiuzhao Hua, *On Numbers of Tuples of Nilpotent Matrices over Finite Fields under Simultaneous Conjugation*, arXiv:2102.07290 (first posted 2021-02-15). https://arxiv.org/abs/2102.07290

[3] Peter Danchev, Esther García, Miguel Gómez Lozano, *Decompositions of Matrices into Potent and Square-Zero Matrices*, arXiv:2102.10460 (first posted 2021-02-20). https://arxiv.org/abs/2102.10460
