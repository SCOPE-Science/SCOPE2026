# Square-root rank fibers of self-adjoint triangular idempotents

## Finding
For every prime power \(q\) and integer \(n\geq1\), let \(K=\mathbb F_{q^2}\) with \(\sigma(a)=a^q\). In the upper triangular matrix algebra \(A_n=T_n(K)\), define the second-kind involution
\[
X^*=J_n\,\sigma(X)^T\,J_n,
\]
where \(J_n\) is the anti-diagonal permutation matrix. Let \(H_{n,r}(q)\) be the number of matrices \(E\in A_n\) satisfying \(E^2=E=E^*\) and \(\operatorname{rank}_K(E)=r\). Then, with \(m=\lfloor n/2\rfloor\),
\[
H_{2m,r}(q)=
\begin{cases}
\binom{m}{r/2}q^{r(2m-r)},&r\in\{0,2,\ldots,2m\},\\
0,&\text{otherwise},
\end{cases}
\]
and
\[
H_{2m+1,r}(q)=\binom{m}{\lfloor r/2\rfloor}q^{r(2m+1-r)}
\qquad (0\leq r\leq2m+1).
\]
An out-of-range binomial coefficient is zero. Every allowable diagonal pattern contributes **exactly** \(q^{r(n-r)}\) distinct self-adjoint idempotents of rank \(r\). This is the square root of the corresponding unrestricted idempotent fiber \((q^2)^{r(n-r)}\) over \(K\).

For fixed \(q\), choose \(E_n\) uniformly among these self-adjoint idempotents and set \(Y_n=\operatorname{rank}_K(E_n)-n/2\). Along each congruence class of \(n\) modulo \(4\), \(Y_n\) converges in total variation, with error \(O_q(n^{-1})\), to the discrete Gaussian
\[
\mathbb P(Y=h)=\frac{q^{-h^2}}{\sum_{t\in\Lambda}q^{-t^2}}
\qquad(h\in\Lambda),
\]
with the corresponding lattice
\[
\Lambda=\begin{cases}
2\mathbb Z,&n\equiv0\pmod4,\\
2\mathbb Z+1,&n\equiv2\pmod4,\\
\mathbb Z+\frac12,&n\equiv1\text{ or }3\pmod4.
\end{cases}
\]
In particular, the centered ranks have bounded fluctuations and \(\mathbb E\operatorname{rank}_K(E_n)=n/2\) exactly for all \(n\).

## Assumptions and scope
The field \(K\) has \(q^2\) elements, with \(q\) an **arbitrary** prime power (even characteristic is included). Matrices are upper triangular relative to the fixed standard full flag. The involution reverses matrix-unit indices and applies the nonidentity field automorphism; it is an anti-automorphism, not an entrywise field-linear operation. Rank means the usual \(K\)-linear matrix rank; it equals the number of diagonal ones for an idempotent. The count concerns distinct **embedded matrices**, not similarity or unitary-conjugacy classes. Both the zero and identity idempotents are included. No assumption that the Hermitian form is anisotropic is made; the form defined by \(J_n\) is nondegenerate.

## Proof
**1. Compatible diagonals.** The diagonal entries of an upper triangular idempotent are zero or one. Since the field Frobenius fixes both, \(E^*=E\) forces \(\epsilon_i=\epsilon_{n+1-i}\) for each diagonal entry \(\epsilon_i\). Thus the binary diagonal word is a palindrome. For \(n=2m\), choosing \(k\) of the \(m\) mirrored pairs to carry ones produces rank \(r=2k\), with \(\binom mk\) choices. For \(n=2m+1\), choosing \(k\) mirrored pairs and the central bit \(b\in\{0,1\}\) gives rank \(2k+b\), with \(\binom mk\) choices.

**2. Unitary unitriangular counting lemma, including characteristic two.** Let \(J\) be the strictly upper triangular ideal of \(A_n\), \(C=1+J\), and \(N=\dim_K J=\binom n2\). The star operation preserves \(J\). Let \(C^+=\{h\in C:h^*=h\}\), and \(U=\{u\in C:u^*u=1\}\). The additive \(\mathbb F_q\)-space of star-fixed elements of \(J\) has dimension \(N\): positions \((i,j)\) and \((n+1-j,n+1-i)\) paired by reflection contribute one free element of \(K\), while self-reflected anti-diagonal positions contribute one free element of \(\mathbb F_q\). Hence \(|C^+|=q^N\).

The map \(c\mapsto c^*c\) from \(C\) onto \(C^+\) is **surjective**. To prove this, filter \(J\) by powers \(J^d\). Suppose a star-fixed element has been made congruent to \(1\) modulo \(J^d\) by a star-congruence \(h\mapsto(c^*)^{-1}hc^{-1}\). Its degree-\(d\) error is fixed by star on \(J^d/J^{d+1}\). The map \(x\mapsto x+x^*\) is onto this fixed space: choose \(\lambda\in K\) with \(\lambda+\lambda^q=1\), which exists by surjectivity of the field trace, and for any fixed quotient vector \(y\) take \(x=\lambda y\). Then \(x+x^*=y\), including in characteristic two. A correction \(1+x\) eliminates the degree-\(d\) error; induction up to \(J^n=0\) yields the factorization. For any \(h\in C^+\), two factorizations \(h=c_1^*c_1=c_2^*c_2\) differ by left multiplication by an element of \(U\). Since \(|C|=q^{2N}\), this proves \(|U|=q^N\).

The same argument works for any star-stable subalgebra of strictly upper triangular matrices whose matrix-entry positions are closed under multiplication and reflection: its star-fixed additive space has \(\mathbb F_q\)-dimension equal to its number of allowed upper entries. The trace argument is unchanged on each mirror orbit.

**3. One unitary orbit per palindromic diagonal.** Fix a palindromic binary diagonal word and let \(e\) be the corresponding diagonal idempotent. If \(E=E^2=E^*\) has this diagonal, set
\[
b=Ee+(1-E)(1-e)\in C.
\]
The diagonal of \(b\) is all ones, so it is invertible, and \(be=Eb\). Taking stars and using \(e=e^*\) and \(E=E^*\) shows that \(h=b^*b\) commutes with \(e\). Moreover \(h=h^*\) and \(h\in C\). The star-stable upper-unitriangular centralizer \(C_e=\{c\in C:ce=ec\}\) consists precisely of entries joining positions with equal diagonal bits. Applying the factorization lemma within \(C_e\) gives \(h=c^*c\) for some \(c\in C_e\). Thus \(u=bc^{-1}\) belongs to \(U\) and satisfies \(ue=Eu\). Therefore every self-adjoint idempotent having the fixed diagonal is in the \(U\)-conjugacy orbit of \(e\).

**4. Orbit size.** The stabilizer of \(e\) in \(U\) is the unitary group of \(C_e\). If the diagonal has \(r\) ones and \(n-r\) zeros, \(C_e\) has \(\binom r2+\binom{n-r}2\) permissible strict upper entries, irrespective of their order. The filtered factorization argument gives
\[
|U_e|=q^{\binom r2+\binom{n-r}2}.
\]
Orbit–stabilizer therefore gives
\[
|U\cdot e|=q^{\binom n2-\binom r2-\binom{n-r}2}=q^{r(n-r)}.
\]
Different diagonals cannot lie in the same unitriangular orbit, since conjugation by an element with identity diagonal preserves the diagonal. Combining this count with Step 1 proves both exact rank formulas. Ordinary upper triangular idempotents over \(K\) with a fixed binary diagonal form a full upper-unitriangular orbit of size \(|K|^{r(n-r)}=q^{2r(n-r)}\); this explains the square-root comparison.

**5. Quantitative discrete-Gaussian limit.** For a rank \(r\) in the permitted parity class, write \(h=r-n/2\) and \(m=\lfloor n/2\rfloor\). The exponent identity \(r(n-r)=n^2/4-h^2\) implies that, after factoring out \(q^{n^2/4}\binom m{\lfloor m/2\rfloor}\), the exact unnormalized rank weight is
\[
w_{n,h}=\beta_{n,h}q^{-h^2},\qquad
\beta_{n,h}=\frac{\binom m{\lfloor r/2\rfloor}}{\binom m{\lfloor m/2\rfloor}}.
\]
For permitted \(r\), \(0\le\beta_{n,h}\le1\). Standard ratios of neighboring binomial coefficients give, uniformly over permitted \(r\),
\[
0\le1-\beta_{n,h}\le \frac{C(1+h^2)}{m},
\]
for an absolute constant \(C\) when \(m\ge2\): near the middle, express the ratio as a product of at most \(O(|h|+1)\) factors differing from one by \(O((|h|+1)/m)\); when the displayed right side exceeds one the inequality is trivial. The omitted tails outside \(0\le r\le n\) contribute \(O(q^{-c n^2})\) to the summable Gaussian weights. Because \(\sum_{h\in\Lambda}(1+h^2)q^{-h^2}<\infty\), the unnormalized weights and their normalizers differ from those of the limiting lattice Gaussian by \(O_q(1/m)\). Normalization yields the asserted total-variation bound for each residue class, and the exact complement involution \(E\mapsto1-E\) gives the mean \(n/2\).

## Verification
The accompanying standalone program `verify.py` constructs \(K=\mathbb F_{q^2}\) explicitly for \(q=2\) and \(q=3\), enumerates every star-fixed upper triangular matrix having a binary palindromic diagonal, tests \(E^2=E\) by direct finite-field multiplication, and compares every rank multiplicity with the claimed formula. Run `python verify.py`. The tested pairs are \((q,n)=(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(3,4)\). The code does not rely on orbit-stabilizer or the factorization lemma. It prints `VERIFY_OK` after all tests. These finite computations do not replace the general proof.

## Relationship to prior work
Fornaroli (2023, arXiv:2306.12512) classifies involutions of the second kind on finitary incidence algebras and their equivalence; the chain incidence algebra is \(T_n(K)\). Urure–Silva (2023, DOI:10.1080/00927872.2022.2158193) classifies second-kind involutions on upper triangular matrix algebras up to equivalence. The latter paper's full text was not accessible for inspection. The present claim fixes the *standard* involution and counts its individual fixed idempotents **by rank**, not involution equivalence classes.

Gargate–Gargate (2020, arXiv:2009.04243, Theorems 1.1–1.2) gives the unrestricted upper triangular idempotent parametrization and its finite-field count; for each diagonal rank-\(r\) pattern over \(K\), it yields \(q^{2r(n-r)}\), not the star-fixed \(q^{r(n-r)}\). Hou (2019 online, DOI:10.1080/03081087.2019.1596223) similarly describes unrestricted triangular idempotents. Diniz–Ramos–Galdino (2020, arXiv:2006.08452) studies graded polynomial identities for triangular involutions over characteristic-zero fields, rather than finite-field fixed-idempotent rank enumeration. The exact star-fixed rank polynomial, one-unitary-orbit-per-palindrome theorem, and parity-dependent quantitative limits were not located in these inspected sources. Priority is provisional because inaccessible full text or a wider flag-counting theorem may imply aspects of the result.

## Limitations
The construction uses the distinguished reversal–Frobenius involution on the triangular matrix algebra over a quadratic finite-field extension. It does not count idempotents fixed by every possible first-kind involution, nor classify arbitrary selfadjoint matrices or arbitrary poset incidence algebras. The limit is for fixed \(q\) as \(n\to\infty\). The general factorization and orbit lemmas are proved here; small-field enumeration alone does not prove them. No independent mathematical audit has been performed.

## References
1. É. Z. Fornaroli, *Involutions of the second kind on finitary incidence algebras*, first submitted June 21, 2023, arXiv:2306.12512, https://arxiv.org/abs/2306.12512 (Sections 2–4).
2. I. Gargate and M. Gargate, *\((k+1)\)-potent matrices in triangular matrix groups and incidence algebras of finite posets*, first submitted August 30, 2020, arXiv:2009.04243, https://arxiv.org/abs/2009.04243 (Theorems 1.1–1.2).
3. R. I. Quispe Urure and D. C. Silva, *Involutions of the second kind for upper triangular matrix algebras*, *Communications in Algebra* **51** (2023), 2326–2333, DOI:10.1080/00927872.2022.2158193 (abstract and citation metadata available; full text inaccessible).
4. X. Hou, *Idempotents in triangular matrix rings*, *Linear and Multilinear Algebra* **69** (2021), 296–304, DOI:10.1080/03081087.2019.1596223 (abstract and citation metadata available).
5. D. Diniz, A. Ramos and J. L. Galdino, *Graded identities with involution for the algebra of upper triangular matrices*, first submitted June 15, 2020, arXiv:2006.08452, https://arxiv.org/abs/2006.08452.
