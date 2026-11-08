# Maximal-circumference clocks for reversible waves on characteristic-two hypertori

## Finding

Let \(d\ge3\), \(f\ge1\), and let \(n_i=2^{s_i}\) with \(s_i\ge2\) for every \(1\le i\le d\). Set \(Q=2^f\), \(N=\prod_{i=1}^d n_i\), \(H=\frac12\max_i n_i\), \(L=2H=\max_i n_i\), and \(c=N/H\). On the labelled sites of the Cartesian product \(G=C_{n_1}\square\cdots\square C_{n_d}\), let \(A\) denote open-neighbor summation over \(\mathbb F_Q\). Consider the two-time-level reversible update
\[
F(u,v)=(Au+v,u),\qquad (u,v)\in\mathbb F_Q^N\oplus\mathbb F_Q^N.
\]
Then, with \(J_m(\alpha)\) denoting the size-\(m\) Jordan block of eigenvalue \(\alpha\), the **complete** similarity classifications over \(\mathbb F_Q\) are
\[
A\sim J_H(0)^{\oplus c},\qquad
F\sim J_L(1)^{\oplus c}.
\]
In particular, the sharp permutation order of \(F\) is \(L\), independent of the number of spatial directions, provided their lengths remain fixed. Every state is periodic from time zero. For every positive integer \(t\), the number of labelled configurations fixed by the \(t\)-fold update is exactly
\[
\#\operatorname{Fix}(F^t)=Q^{c\min(2^{\nu_2(t)},L)}.
\]
All primitive periods are powers of two dividing \(L\). Writing \(L=2^S\), the number of labelled states with primitive period \(2^j\) is
\[
P(1)=Q^c,\qquad
P(2^j)=Q^{c2^j}-Q^{c2^{j-1}}\quad(1\le j\le S),
\]
and the exact number of primitive temporal cycles of that length is \(P(2^j)/2^j\). These populations are strictly positive, and no other primitive periods occur.

For illustration, on the three-dimensional \(4\times4\times4\) torus, \((N,L,c)=(64,4,32)\), so the binary system has \(2^{32}\) fixed states, \(2^{64}-2^{32}\) states of period two, and \(2^{128}-2^{64}\) states of period four. On the \(4\times4\times8\) torus, \((N,L,c)=(128,8,32)\), and the corresponding primitive period-eight population is \(2^{256}-2^{128}\).

## Assumptions and scope

The graph \(C_{n_i}\) is the simple undirected cycle of length \(n_i\); the lower bound \(n_i\ge4\) prevents double-counted neighbors. All sums and linear algebra are over \(\mathbb F_Q\) of characteristic two, and every state consists of **two** successive spatial configurations. The state counts distinguish labelled sites and time phases, while a primitive cycle identifies states related by temporal iteration. The theorem covers **every** \(d\ge3\), every tuple of power-of-two side lengths at least four, every characteristic-two finite field, and every positive temporal exponent. It does not assert the same classification for an odd side length, a different local rule, or a one-time-level update.

## Proof

**1. The one-direction nilpotent module.** Fix a side length \(n=2^s\ge4\) and write its cyclic shift as multiplication by \(x\) in \(R_n=\mathbb F_Q[x^{\pm1}]/(x^n-1)\). Since the characteristic is two, with \(z=x+1\) there is a canonical algebra identification
\[
R_n\cong\mathbb F_Q[z]/(z^n),\qquad x+x^{-1}=x^{-1}z^2.
\]
The factor \(x^{-1}\) is a unit. Consequently, multiplication by \((x+x^{-1})^j\) has rank \(\max(n-2j,0)\) for all integers \(j\ge0\). The operator is nilpotent of index \(n/2\). The ranks of all powers uniquely determine the nilpotent Jordan block sizes, and these ranks are exactly those of \(J_{n/2}(0)\oplus J_{n/2}(0)\). In particular, as a module for the indeterminate \(t=x+x^{-1}\),
\[
R_n\cong\bigl(\mathbb F_Q[t]/(t^{n/2})\bigr)^{\oplus2}.
\]
This is an isomorphism of modules, not a claim that \(t\) and \(z\) are equal.

**2. The multidirectional diagonal generator.** For the full torus, the spatial configuration space is the tensor product \(R=\bigotimes_{i=1}^d R_{n_i}\). Let \(t_i\) denote the neighbor-sum operator in direction \(i\), and let \(h_i=n_i/2\). The preceding module decomposition identifies the action of \(A=t_1+\cdots+t_d\) with \(2^d\) direct copies of multiplication by \(w=t_1+\cdots+t_d\) on
\[
B=\mathbb F_Q[t_1,\ldots,t_d]/(t_1^{h_1},\ldots,t_d^{h_d}).
\]
Choose an index \(k\) with \(h_k=H=\max_i h_i\). Regard \(w\), together with \(t_i\) for \(i\ne k\), as the new polynomial variables. This is an invertible linear substitution because \(t_k=w+\sum_{i\ne k}t_i\). Its crucial relation is
\[
t_k^H=(w+\sum_{i\ne k}t_i)^H=w^H+\sum_{i\ne k}t_i^H=w^H.
\]
The equality uses that \(H\) is a power of two; the final equality holds since every \(h_i\) divides \(H\) and \(t_i^{h_i}=0\). Thus
\[
B\cong\frac{\mathbb F_Q[w,t_i\ (i\ne k)]}{(w^H,t_i^{h_i}\ (i\ne k))}
\]
and multiplication by \(w\) is a direct sum of \(\prod_{i\ne k}h_i\) Jordan blocks of size \(H\). Across \(2^d\) copies this yields \(c=2^d\prod_{i\ne k}h_i=N/H\) blocks: \(A\sim J_H(0)^{\oplus c}\). In particular, \(A^H=0\) and \(\dim\ker A=c\).

**3. Passing to reversible two-time-level dynamics.** In block notation,
\[
F=\begin{pmatrix}A&I\\I&0\end{pmatrix},\qquad
F^{-1}=\begin{pmatrix}0&I\\I&A\end{pmatrix}.
\]
Direct multiplication in characteristic two gives \(F+F^{-1}=\operatorname{diag}(A,A)\) and
\[
F^2+I=\operatorname{diag}(A,A)F.
\]
The two matrices on the right commute. Since \(A^H=0\), it follows that \(F^{2H}=I\). The integer \(L=2H\) is a power of two, so \((F+I)^L=F^L+I=0\); all Jordan blocks of \(F\) therefore have eigenvalue one and length at most \(L\), already over \(\mathbb F_Q\).

To count the blocks, solve \((F+I)(u,v)=0\). The lower equation gives \(v=u\); the upper then gives \(Au=0\). Hence \(\dim\ker(F+I)=\dim\ker A=c\), so \(F\) has exactly \(c\) unipotent Jordan blocks. Their sizes add to the full dimension \(2N=cL\); since each size is at most \(L\), all must be exactly \(L\). This proves \(F\sim J_L(1)^{\oplus c}\) and its sharp order \(L\).

**4. Every fixed-point and orbit count.** Write \(t=2^r q\) with odd \(q\). As polynomials evaluated at a unipotent matrix, \(F^t-I=(F^{2^r}-I)U(F)\), where \(U(1)=q=1\) in characteristic two. Because \(U(F)\) is invertible, its kernel equals the kernel of \((F+I)^{2^r}\). On a size-\(L\) unipotent Jordan block this has dimension \(\min(2^r,L)\). Summing over the \(c\) blocks proves the fixed-point formula. The only possible least periods divide \(L\), and for adjacent powers of two the difference between successive fixed-point counts gives exactly the stated primitive-state populations. Dividing those populations by their period counts primitive cycles. Their positivity for \(Q\ge2\) establishes that every stated length occurs, including the full sharp length \(L\).

## Verification

The supplied `verification/check_graph.py` independently constructs the physical periodic-neighbor matrix directly from coordinates, forms the two-time-level matrix, and verifies power ranks and fixed dimensions for side-length tuples \((4,4)\), \((4,8)\), \((8,4)\), \((8,8)\), \((4,16)\), \((4,4,4)\), and \((4,4,8)\). The separate `verification/check_polynomials.py` constructs adjacency in the truncated-coordinate basis \(z_i=x_i+1\), then checks the spatial nullity progression on seven tuples, including \((4,4,4,4)\). Both use exact binary bit-vector Gaussian elimination and report PASS. Their captured outputs are `verification/check_graph_output.txt` and `verification/check_polynomials_output.txt`. Reproduce with `python3 verification/check_graph.py` and `python3 verification/check_polynomials.py` from the extracted package root. The scripts test finite cases; the general theorem follows from the preceding algebraic proof, not from extrapolating the tests.

## Relationship to prior work

The additive group-algebra representation and general higher-order cellular-automaton framework are classical; Martin, Odlyzko and Wolfram (1984) explicitly discuss multidimensional additive rules in §4D, including the orthogonal-neighbor polynomial, and higher-order rules in §4E. Their multidimensional period bound in Theorem 4.8 assumes side lengths not divisible by the characteristic, so it does not cover the present power-of-two circumferences; §4E does not derive the asserted multidimensional two-time-level Jordan or orbit classification. Macfarlane (2004) studies one-dimensional reversible second-order rules and matrix equivalences, not the present \(d\ge3\) hypertori. Chang, Su, Akın and Şah (2017; preprint dated 2016-09-30) supply Kronecker-sum and generalized Jordan methods, principally for one-time-level automata with null boundary conditions; their theorem does not give this reversible time-layer classification under periodic boundaries. The first-order **two-dimensional** torus and one-dimensional wave specializations are excluded from the originality claim rather than counted as new cases. The assessed contribution is precisely the explicit uniform Jordan form and complete primitive-orbit census for **all** \(d\ge3\) power-of-two hypertori.

## Limitations

The proof requires characteristic two and power-of-two side lengths at least four. Nothing is asserted for mixed odd and even circumferences or other update coefficients. General Jordan-computation techniques appear in the prior literature and can be applied to related matrices; historical priority of an independently derived equivalent special formula in literature not located by the searches cannot be ruled out. Independent external review of the new theorem has not occurred. The finite checks are reproducibility tests, not formal certification of arbitrary dimensions.

## References

1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644. DOI: 10.1103/RevModPhys.55.601. First published 1983-07-01.
2. O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. DOI: 10.1007/BF01223745; §§4D–4E.
3. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A **37** (2004), 10791–10814. DOI: 10.1088/0305-4470/37/45/006; published 2004-10-28.
4. C.-H. Chang, J.-Y. Su, H. Akın and F. Şah, *Reversibility Problem of Multidimensional Finite Cellular Automata*, Journal of Statistical Physics **168** (2017), 208–231. DOI: 10.1007/s10955-017-1799-6; prior preprint arXiv:1609.09572 dated 2016-09-30.
