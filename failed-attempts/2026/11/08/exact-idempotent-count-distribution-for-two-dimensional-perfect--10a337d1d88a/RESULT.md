# Exact idempotent-count distribution for two-dimensional perfect evolution algebras over finite fields

## Finding
Let \(q\ge2\) be a prime power and \(E\) a two-dimensional perfect evolution algebra over \(\mathbb F_q\), sampled by choosing its invertible structure matrix uniformly from \(\operatorname{GL}_2(\mathbb F_q)\) in a fixed natural basis. Write \(K(E)\) for the number of **nonzero** solutions of \(u^2=u\), and let \(L=(q^2-1)(q^2-q)\). Put \(h=(q-1)^3\) if \(q\) is odd, and \(h=0\) if \(q\) is even. Then the exact multiplicity for \(K(E)=k\) is
\[
(N_0,N_1,N_2,N_3)=\left(\frac L3,\frac{L-h}{2},h,\frac{L-3h}{6}\right).
\]
No other value of \(K(E)\) occurs. In particular, exactly one-third of invertible two-dimensional evolution-algebra structure matrices are idempotent-free, for **every** prime power \(q\). In even characteristic the distribution is exactly \((1/3,1/2,0,1/6)\), while odd characteristic has a precise finite-field correction.

## Assumptions and scope
A two-dimensional evolution algebra has a natural basis \(e_1,e_2\) with \(e_1e_2=0\). Perfection means \(E^2=E\), equivalently that its \(2\times2\) structure matrix is invertible. Uniform means counting all invertible matrices relative to one fixed, labeled natural basis; the theorem is **not** a uniform distribution over isomorphism classes. The zero vector is always an idempotent but is excluded from \(K(E)\). Every prime power is included, including \(q=2\), and all characteristic-two extension fields are included.

## Proof
**1. Reduction to a projective binary cubic.** Let \(W\) be the invertible structure matrix, acting on the coordinate square vector according to \(u^2=W^{\mathsf T}(x^2,y^2)^{\mathsf T}\) in the convention where rows specify natural-basis squares. The map \(W\mapsto N=(W^{\mathsf T})^{-1}\) is a bijection of \(\operatorname{GL}_2(\mathbb F_q)\). Write
\[
N=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]
An idempotent \((x,y)\) satisfies \(x^2=ax+by\) and \(y^2=cx+dy\). For any projective direction \([X:Y]\in\mathbb P^1(\mathbb F_q)\), the vectors \((X^2,Y^2)\) and \(N(X,Y)^{\mathsf T}\) are proportional precisely when
\[
F_N(X,Y)=bY^3+aXY^2-dX^2Y-cX^3=0.
\]
Because \(N\) is invertible and \((X^2,Y^2)\ne(0,0)\), the proportionality scalar is nonzero. Thus exactly one nonzero scaling of that direction is an idempotent: if \(N v=\lambda v^{[2]}\), then \(\lambda v\) is the unique idempotent on that line. Hence \(K(E)\) equals the number of distinct \(\mathbb F_q\)-rational zeros of the binary cubic \(F_N\) on \(\mathbb P^1\). This is at most three, because \(F_N\ne0\) for \(N\ne0\).

**2. Binary cubic counting.** The map \(N\mapsto F_N\) is a linear bijection of the four-dimensional space of matrices with the four-dimensional space of binary cubics. Every nonzero binary cubic without a rational projective zero has a degree-three irreducible dehomogenization; since it has no zero at infinity, its \(X^3\) coefficient is nonzero. There are \((q^3-q)/3\) monic irreducible cubics over \(\mathbb F_q\), and \(q-1\) nonzero scalar choices. Thus there are \((q-1)(q^3-q)/3=L/3\) rootless nonzero binary cubics. Their associated matrices cannot be singular, as shown next. So \(N_0=L/3\).

All nonzero binary cubics with three **distinct** rational projective zeros are nonzero scalar multiples of products of the three corresponding distinct linear factors. Their number is
\[
(q-1)\binom{q+1}{3}=L/6.
\]
All nonzero binary cubics with exactly two distinct rational projective zeros form the scalars times a product with root multiplicity pattern \((2,1)\); there are \((q+1)q(q-1)=q(q^2-1)\) such cubics. These counts apply to all characteristics.

**3. Remove the singular matrices.** Any nonzero singular \(N\) has rank one and can be represented as \(N=u v^{\mathsf T}\). For such a matrix,
\[
F_N(X,Y)=(v_1X+v_2Y)(u_1Y^2-u_2X^2).
\]
A rank-one matrix is specified uniquely by its projective column direction \([u]\), projective row direction \([v]\), and one of \(q-1\) nonzero scalars. Hence every rootless cubic comes from an invertible matrix.

When \(q\) is odd, the quadratic factor \(u_1Y^2-u_2X^2\) has two distinct rational projective roots for exactly \((q-1)/2\) choices of \([u]\), one distinct root for exactly two choices (the coordinate directions), and zero roots for the remaining \((q-1)/2\) choices. For each two-root quadratic, \(q-1\) choices of the linear root differ from both quadratic roots, producing three distinct roots; with the rank-one scalar the count is \((q-1)^3/2\) singular matrices with three distinct roots. Singular matrices with exactly two distinct roots arise either by choosing the linear root equal to one of two roots, contributing \((q-1)^2\), or by choosing it different from the unique quadratic root in either of the two single-root quadratic directions, contributing \(2q(q-1)\). Therefore their combined number is \((q-1)(3q-1)\).

When \(q\) is even, the map \(z\mapsto z^2\) is an automorphism of \(\mathbb F_q\). Thus the quadratic factor of every rank-one matrix is the square of a linear form and has exactly one rational projective root. Every singular cubic has at most two distinct rational projective roots, and exactly two when its separate linear factor has a different root. There are \((q+1)q(q-1)=q(q^2-1)\) such singular cubics; there are none with three distinct roots.

**4. Subtraction and completion.** If \(q\) is odd, among invertible matrices the number with two roots is
\[
N_2=q(q^2-1)-(q-1)(3q-1)=(q-1)^3=h,
\]
and the number with three roots is
\[
N_3=L/6-(q-1)^3/2=(L-3h)/6.
\]
If \(q\) is even, subtracting singular cubics yields \(N_2=0=h\) and \(N_3=L/6\). Finally, using \(N_0+N_1+N_2+N_3=L\), we obtain \(N_1=(L-h)/2\) in every characteristic. These identities also cover the smallest field \(\mathbb F_2\), where the histogram is \((2,3,0,1)\). This completes the proof.

## Verification
Run the standalone Python 3 program `CHECK.py` with `python3 CHECK.py`; it uses only the standard library. Its output, recorded verbatim in `CHECK_OUTPUT.txt`, terminates in `VERIFY_OK`. It exhaustively enumerates all invertible \(2\times2\) matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8,\mathbb F_9,\mathbb F_{11}\), checks their nonzero idempotents by direct substitution, checks the corresponding projective cubic zeros by a separate calculation, and checks all four closed formulas. Finite enumeration corroborates rather than proves the general theorem; the complete symbolic count above covers every prime power.

## Relationship to prior work
Kaygorodov, Martín González, and Viruel (2026), Remark 23, prove that the **mean** number of nonzero idempotents of uniformly selected invertible evolution-algebra matrices is exactly one in every dimension. Our four-level distribution implies that mean in dimension two but is not a consequence of the mean. Their Theorem 18 addresses existence of idempotent-free perfect evolution algebras over finite fields, while the present result quantifies the exact proportion and distinguishes the parity of the field.

Wei and Zou (2023), Theorem 4.1, enumerate **isomorphism classes** of perfect evolution algebras over finite fields, not the idempotent-count distribution of uniformly sampled labeled invertible matrices. Cabrera Casado, Martín Barquero, and Martín González (2023) classify dimension-two perfect evolution algebras over domains through moduli, again a different weighting and invariant. The binary-cubic factorization and projective-root approach here supplies an explicit full histogram.

## Limitations
The counts are of structure matrices, not isomorphism types. Dimension three and higher, and nonperfect evolution algebras, are outside the theorem. The binary-cubic factorization argument is elementary; the formula may be implicit in other work on random binary cubic forms, finite-field dynamics, or low-dimensional evolution algebras not yet identified. No claim of independently certified historical priority is made.

## References
- I. Kaygorodov, C. Martín González, and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (2026), especially Remark 23 and Theorem 18. https://arxiv.org/abs/2610.22248
- Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (2023), especially Theorem 4.1. https://arxiv.org/abs/2310.12368
- Y. Cabrera Casado, D. Martín Barquero, and C. Martín González, *Two-dimensional perfect evolution algebras over domains*, Journal of Algebraic Combinatorics 58 (2023), 569–587. https://doi.org/10.1007/s10801-022-01196-1
