# The incidence-rank clock of reversible waves on finite projective planes

## Finding
Let \(\Pi\) be **any** finite projective plane of order \(s\ge2\), with \(v=s^2+s+1\) points and as many lines. Form its bipartite point-line incidence graph \(G_\Pi\), with binary adjacency matrix \(A\). Over any finite field \(\mathbb F_Q\), where \(Q=2^f\) and \(f\ge1\), let the reversible wave map be
\[
 T(u,w)=(Au+w,u),\qquad (u,w)\in(\mathbb F_Q^{2v})^2.
\]
All states are immediately periodic. Their exact global temporal order is **six** when \(s\) is odd and **twelve** when \(s\) is even. More strongly, the following statement gives every fixed-point and primitive-orbit population.

Put \(p(X)=X^2+X+1\), let \(\rho=\operatorname{rank}_{\mathbb F_2}B\) for the \(v\)-by-\(v\) point-line incidence matrix \(B\), and for a positive integer \(t\) put \(b(t)=2^{\nu_2(t)}\). As an \(\mathbb F_Q[X]\)-module, with \(X\) acting by \(T\), the full two-time-row space is
\[
\begin{aligned}
 s\text{ odd}:\quad & [\mathbb F_Q[X]/(X+1)^2]^{\oplus2}
       \oplus[\mathbb F_Q[X]/p(X)^2]^{\oplus(v-1)},\\
 s\text{ even}:\quad & [\mathbb F_Q[X]/p(X)^2]
       \oplus[\mathbb F_Q[X]/(X+1)^4]^{\oplus2r}
       \oplus[\mathbb F_Q[X]/(X+1)^2]^{\oplus z},
\end{aligned}
\]
where in the even case \(r=\rho-1\ge1\) and \(z=2(v-1)-4r\ge0\).

Consequently, for every positive integer \(t\), the exact number of states fixed by the \(t\)-th update is \(Q^{E(t)}\), where
\[
E(t)=\begin{cases}
2\min(2,b(t))\bigl(1+(v-1)\mathbf1_{3\mid t}\bigr),&s\text{ odd},\\
2\mathbf1_{3\mid t}\min(2,b(t))+2r\min(4,b(t))+z\min(2,b(t)),&s\text{ even}.
\end{cases}
\]
The exact number of labelled configurations of *least* period \(d\) is \(\sum_{e\mid d}\mu(d/e)Q^{E(e)}\); dividing by \(d\) gives the number of temporal orbits. The possible least periods, all realized, are \(\{1,2,3,6\}\) for odd \(s\), and \(\{1,2,3,4,6,12\}\) for even \(s\).

The orbit census **recovers the incidence-code rank**: for every plane,
\[
|\operatorname{Fix}(T)|=Q^{2(v-\rho)}.
\]
Thus among planes of the same order, two wave systems have identical fixed-point populations at every time if and only if their incidence matrices have the same binary rank. No claim of distinguishing all nonisomorphic planes is made.

For the Desarguesian plane \(\operatorname{PG}(2,2^e)\), \(e\ge1\), a self-contained finite-field argument below gives \(\rho=3^e+1\), making the even-order census completely explicit. In particular, for the Fano plane over \(\mathbb F_2\), the fixed-space dimensions at times \(1,2,3,4,6,12\) are respectively \(6,12,8,24,16,28\).

## Assumptions and scope
A finite projective plane of order \(s\ge2\) is an incidence structure with \(v=s^2+s+1\) points and lines, each point on \(s+1\) lines, each line containing \(s+1\) points, and precisely one common line for distinct points (dually, one common point for distinct lines). It need not be Desarguesian. Incidence entries are reduced from \(\{0,1\}\) to characteristic two; the update field may be any finite extension \(\mathbb F_Q\). Each state consists of two **ordered, labelled** configurations on all \(2v\) graph vertices; neither phase nor graph automorphisms are quotiented out. Incidence rank \(\rho\) always means rank over \(\mathbb F_2\), unchanged by extension of scalars. Möbius inversion is over positive divisors, and \(\nu_2(t)\) is the usual nonnegative two-adic valuation.

## Proof
**1. Universal incidence identity.** Let \(J\) be the all-ones \(v\)-by-\(v\) matrix. Counting common incident lines and points gives
\[
BB^{\mathsf T}=B^{\mathsf T}B=sI+J
\]
over any characteristic-two field. The row and column sums of \(B\) are both \(s+1\) modulo two, and \(v\) is odd. Hence the point and line coordinate spaces each split into the constants \(U=\langle\mathbf1\rangle\) and the zero-sum hyperplane \(W=\ker(\mathbf1^{\mathsf T})\). Both \(B\) and \(B^{\mathsf T}\) preserve this splitting. The graph adjacency is \(A=\begin{psmallmatrix}0&B\\B^{\mathsf T}&0\end{psmallmatrix}\).

**2. Odd plane order.** If \(s\) is odd, \(B\mathbf1=B^{\mathsf T}\mathbf1=0\), and \(BB^{\mathsf T}=I+J\) acts as the identity on \(W\). Thus \(B\) is invertible from the line copy of \(W\) to the point copy, while \(A\) is zero on the two constant vectors and squares to the identity on the \(2(v-1)\)-dimensional sum-zero part. On that part, the kernel of \(A+I\) has dimension \(v-1\) (one freely chosen vector on a shore determines the other), so the characteristic-two Jordan form consists of \(v-1\) copies of \(J_2(1)\). The remaining two adjacency blocks are \(J_1(0)\). In particular \(\rho=v-1\).

**3. Even plane order.** If \(s\) is even, both incidence matrices fix \(\mathbf1\), while \(BB^{\mathsf T}=J\), so \(A\) swaps the two constant vectors and its restriction \(A_W\) to the paired zero-sum spaces has square zero. Put \(r=\operatorname{rank}(B|_W)=\rho-1\). Then \(\operatorname{rank}(A_W)=2r\). Every square-zero operator has only nilpotent Jordan blocks of lengths one and two; hence
\[
A\sim J_2(1)\oplus J_2(0)^{\oplus2r}\oplus J_1(0)^{\oplus z},\quad z=2(v-1)-4r.
\]
Here \(r\ge1\) because an incidence matrix with \(s+1<v\) cannot have only the constant column-space; the formula also proves \(z\ge0\).

**4. Reversible-wave transfer.** The inverse of \(T=\begin{psmallmatrix}A&I\\I&0\end{psmallmatrix}\) is \(\begin{psmallmatrix}0&I\\I&A\end{psmallmatrix}\), so all states are periodic. A single adjacency block \(J_1(0)\) transfers to one temporal \((X+1)^2\)-block. A single \(J_2(0)\) transfers to one temporal \((X+1)^4\)-block: its temporal characteristic polynomial is \((X+1)^4\), and \(\operatorname{rank}(T+I)^2=2\) on the corresponding four-space, identifying the unique length-four Jordan block. A single \(J_2(1)\) transfers to one temporal \(p(X)^2\)-block: the characteristic polynomial is \(p(X)^2\), and the identity \(T+T^{-1}=\operatorname{diag}(A,A)\) gives \(p(T)=T\operatorname{diag}(A+I,A+I)\), which has rank two and square zero on that four-space. The factor \(p(X)\) is separable irreducible over \(\mathbb F_2\). These correspondences prove both asserted module decompositions over \(\mathbb F_2\) and, after scalar extension, over \(\mathbb F_Q\).

**5. Populations and sharp orders.** For a cyclic \(g(X)^a\)-module with monic \(g\), the dimension of the \(t\)-fixed subspace is \(\deg\gcd(g(X)^a,X^t-1)\). In characteristic two the multiplicities of \(X+1\) and \(p(X)\) in \(X^t-1\) are respectively \(b(t)\) and \(b(t)\mathbf1_{3\mid t}\). Summing the contributions proves \(E(t)\). The largest \((X+1)\)-block has order at most four, and \(p(X)^2\) has exact order six. In the odd case the latter and a length-two \((X+1)\)-block are present, making order six; in the even case \(r\ge1\) supplies a length-four block, making order twelve. All periods in the statement occur by choosing vectors in the displayed primary blocks and taking direct sums; these are exactly the divisors of the respective global orders. Möbius inversion proves the primitive-count formula. Finally \(E(1)=2(v-\rho)\) in both parity cases, recovering \(\rho\).

**6. Explicit Desarguesian rank (not a new rank assertion).** Let \(s=2^e\). The line indicator on the nonzero projective point \([x:y:z]\) corresponding to \(ax+by+cz=0\) is \(1+(ax+by+cz)^{s-1}\). As the coefficients \((a,b,c)\) vary, the powers span precisely the \(3^e\) distinct homogeneous monomials \(x^i y^j z^k\) of total degree \(s-1\) whose exponents add without binary carries. Indeed, in \((ax+by+cz)^{s-1}\) all other multinomial coefficients vanish modulo two, while the \(3^e\) surviving coefficient functions \(a^i b^j c^k\) are independent on \(\mathbb F_s^3\) by reduced-polynomial uniqueness. The corresponding monomial functions of \([x:y:z]\) are independent: a homogeneous polynomial of degree \(s-1\) vanishing on all projective points vanishes on all of \(\mathbb F_s^3\) and hence is zero, since its degree in each coordinate is less than \(s\). The constant function is independent of them, because summing over all projective points gives \(1\) for the constant (the number \(v\) is odd) and \(0\) for each monomial (sum first over all nonzero affine triples, using \(\sum_{a\in\mathbb F_s} a^j=0\) for \(0\le j<s-1\)). Finally the sum of all line indicators is the constant \(1\) (each point lies on the odd number \(s+1\) of lines). Therefore the line-indicator span is exactly the constant plus those \(3^e\) monomials, and \(\rho=3^e+1\). This agrees with the established projective-code dimension formula cited below.

## Verification
Two standalone ordinary Python programs are included. Running `python3 check_matrix.py` independently constructs the projective incidences for field orders \(2,3,4,5,8\), computes the binary incidence ranks, forms the full reversible wave matrices, and compares the actual fixed-space nullities at times \(1,2,3,4,6,12\) against the theorem. Running `python3 check_orbits.py` performs individual neighbor-by-neighbor synchronous updates for \(54{,}204\) deterministic state tests on orders \(2,3,5\), checking allowed periods and attainment of the maximal period. The included logs record the actual runs. The matrix program tests characteristic-two incidence matrices and does not require creating a large explicit field \(\mathbb F_Q\); the field-extension conclusion is proved algebraically. These finite tests corroborate but do not replace the argument for all finite projective planes.

## Relationship to prior work
Second-order reversible cellular automata, including general underlying neighborhood rules, are established in Vlasov's 2013 treatment and earlier work of Toffoli and Margolus. Lavrauw, Storme and Van de Voorde study codes from projective incidence matrices, including their row spaces and duals; Bariffi, Mattheus, Neri and Rosenthal explicitly state the classical binary code dimension \(2^{2e}-3^e+2^e\) for \(\operatorname{PG}(2,2^e)\). These foundational results do not give an incidence-graph reversible-wave module or orbit census. Work on strongly regular graph waves does not subsume this result: a projective-plane incidence graph is bipartite with diameter three, not a nontrivial strongly regular graph. The present contribution is the complete period and fixed-point classification on incidence graphs of **all** finite projective planes, together with the equivalence between its temporal census and the binary incidence rank; the classical incidence identities and code-rank formula are not claimed as new.

## Limitations
The theorem concerns finite fields of characteristic two and the specified reversible two-row update only. It does not determine which incidence ranks occur among nonisomorphic non-Desarguesian planes, nor does it classify isomorphisms of full wave systems from equality of periodic-point data. The new mathematics has not been independently peer reviewed; undiscovered historical overlap remains possible. Direct state tests cover the stated finite orders, not all planes or all configurations.

## References
- A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first submitted 2013-11-18, especially Section 3. https://arxiv.org/abs/1311.4297
- M. Lavrauw, L. Storme and G. Van de Voorde, *On the code generated by the incidence matrix of points and hyperplanes in PG(n,q) and its dual*, arXiv:1201.3290, first submitted 2012-01-16, especially Sections 1–2. https://arxiv.org/abs/1201.3290
- J. Bariffi, S. Mattheus, A. Neri and J. Rosenthal, *Moderate-density parity-check codes from projective bundles*, Designs, Codes and Cryptography 90 (2022), Theorem 3.4. https://doi.org/10.1007/s10623-022-01054-y
- A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A 37 (2004), starting at 10791. https://doi.org/10.1088/0305-4470/37/45/006
