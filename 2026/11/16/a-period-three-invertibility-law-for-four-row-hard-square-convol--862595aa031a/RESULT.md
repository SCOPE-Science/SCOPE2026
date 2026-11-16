# A period-three invertibility law for four-row hard-square convolution

## Finding
Let \(G_n=P_4\square P_n\) be the Cartesian grid on four rows and \(n\ge1\) columns, with open boundary conditions. Put \(H_n=\mathbb F_2^{V(G_n)}\), and let \(f_n:H_n\to\{0,1\}\) indicate independent vertex sets, including the empty set. Use **unnormalized counting convolution** \(T_ng=f_n*g\), and define its unnormalized Walsh multipliers
\[
W_n(u)=\sum_{I\subseteq V(G_n)\atop I\text{ independent}}(-1)^{\sum_{v\in I}u_v},\qquad u\in H_n.
\]
Then, for every integer \(n\ge1\),
\[
\boxed{T_n\text{ is invertible}\ \Longleftrightarrow\ n\not\equiv1\pmod3.}
\]
For every \(n\equiv1\pmod3\), there is an explicit three-column-periodic frequency with \(W_n(u)=0\). In each invertible dimension, an explicit two-column-periodic frequency has \(|W_n(u)|=1\), so
\[
\boxed{\min_{u\in H_n}|W_n(u)|=1,\qquad \|T_n^{-1}\|_{\ell^2(H_n)\to\ell^2(H_n)}=1}
\]
for every \(n\not\equiv1\pmod3\). The norm uses ordinary counting \(\ell^2\) measure; the same operator norm holds for normalized counting measure, provided the convolution itself remains unnormalized.

## Assumptions and scope
Number the rows from top to bottom by \(0,1,2,3\) and columns from left to right by \(1,\dots,n\). Encode a four-bit column by an integer mask \(a\in\{0,\dots,15\}\), with row \(i\) occupied when its bit \(2^i\) is set. The allowed within-column masks, in fixed order, are
\[
\mathcal S=(0,1,2,4,5,8,9,10).
\]
Two successive columns \(a,b\in\mathcal S\) are compatible precisely when their bitwise AND vanishes. A frequency is a column-wise sequence of masks \((s_1,\dots,s_n)\), where mask \(s_j\) specifies which vertex characters are negative in column \(j\). No assumption is made on \(n\), weights, boundary identifications, or frequencies beyond those stated: the grid has ordinary open boundaries and every frequency in \(H_n\) is considered.

## Proof
For each sign mask \(s\in\{0,\dots,15\}\), define the integer \(8\times8\) matrix, indexed by \(a,b\in\mathcal S\),
\[
M_s(a,b)=\begin{cases}(-1)^{|a\cap s|},&a\cap b=\varnothing,\\0,&\text{otherwise.}\end{cases}
\]
Here intersections refer to the corresponding subsets of rows. Let \(e\) be the basis vector for empty mask \(0\), and let \(\mathbf1\) be the all-one column vector. A column-by-column decomposition of independent sets proves exactly
\[
W_n(s_1,\ldots,s_n)=\mathbf1^{\mathsf T}M_{s_n}\cdots M_{s_1}e.\tag{1}
\]
This also proves that every frequency is represented, because all \(16\) sign masks are allowed in each column.

**Parity.** Set \(A=M_0\). Since all signs are congruent to one modulo two,
\[
W_n(u)\equiv a_n:=\mathbf1^{\mathsf T}A^ne\pmod2
\]
for every frequency \(u\). Direct multiplication of the displayed, fully defined \(8\times8\) matrix over \(\mathbb F_2\) gives, for \(0\le j\le10\),
\[
(a_0,\ldots,a_{10})\bmod2=(1,0,1,1,0,1,1,0,1,1,0).
\]
Thus \(\mathbf1^{\mathsf T}A^j(A^3-I)e=0\) modulo two for each \(0\le j\le7\). By the Cayley–Hamilton theorem for this eight-dimensional matrix over \(\mathbb F_2\), the same identity holds for all \(j\ge0\). Hence \(a_{n+3}\equiv a_n\pmod2\), and \(a_n\) is odd precisely for \(n\not\equiv1\pmod3\). In those dimensions every \(W_n(u)\) is odd, and no Fourier multiplier can vanish.

**Constructive singularity.** Set
\[
P=M_{14}M_0M_{11},\qquad r=\mathbf1^{\mathsf T}M_{11},\qquad v_j=P^je.
\]
Exact integer multiplication gives
\[
rv_0=rv_1=rv_2=rv_3=0,\qquad v_4=v_0+2v_1+2v_2.\tag{2}
\]
The span of \(v_0,v_1,v_2,v_3\) is invariant under \(P\), by the second identity. The row \(r\) annihilates this invariant span, by the first four identities. Consequently \(rP^ke=0\) for every \(k\ge0\). For length \(n=3k+1\), choose the column-frequency masks by repeating \((11,0,14)\) from the left. Equation (1) then becomes
\[
W_{3k+1}(11,0,14,11,\dots,11)=rP^ke=0.
\]
This proves singularity in *every* remaining dimension; no finite enumeration is used to extrapolate it.

**A sharp unit multiplier.** Set \(Q=M_3M_{15}\). Another exact integer matrix identity is
\[
Q^6e=e.\tag{3}
\]
For the frequency obtained by repeating the two column masks \((15,3)\), (1) and (3) give a twelve-periodic multiplier sequence. Its values for lengths \(1\) through \(12\) are exactly
\[
(0,1,-1,2,-1,1,0,1,1,0,1,1).
\]
Every index not congruent to \(1\pmod3\) has multiplier \(1\) or \(-1\). This proves the sharp minimum. Finally, the Walsh characters form an orthogonal basis and diagonalize counting convolution, with eigenvalues \(W_n(u)\). Their nonvanishing gives the invertibility criterion, and the minimum modulus gives the stated \(\ell^2\) inverse norm.

## Verification
Run `python3 verify_grid4.py` from the package directory. The checker regenerates matrices from the mask definitions, verifies all three infinite-proof matrix certificates (the scalar parity relation, the four-dimensional invariant span, and the twelfth-step unit-witness cycle), and compares the resulting signed transfer sums to independently constructed full Walsh–Hadamard spectra for \(n=1,2,3,4\). Its expected terminal marker is `GRID4_WALSH_PERIOD3_PASS`. Exhaustive small cases yield respectively \(5,0,0,11304\) zero multipliers at lengths \(1,2,3,4\); the infinite classification follows from the proof, not those counts.

## Relationship to prior work
The hard-square model and transfer matrices for independent vertex sets of rectangular square grids are classical. Bousquet-Mélou, Linusson and Nevo (2007) study independence complexes and the *uniform-activity* value at \(-1\), explicitly providing a generating function for the alternating count on ordinary four-row rectangles (Section 7.1). That specialization sets all vertex signs equal and does not determine whether **any** of the \(2^{4n}\) independent coordinatewise choices yields a zero, or the least nonzero multiplier. Oh and Lee (2016) prove a state-matrix enumeration of the *univariate* independent-set generating polynomial of a rectangular grid, not the full multivariate family of signs. Here the new claim is the all-column-sign Fourier invertibility dichotomy plus two periodic constructive witnesses; neither unsigned enumeration nor uniform-activity evaluation alone implies it.

## Limitations
The theorem does not give the exact number or full distribution of zero frequencies in singular dimensions, the nonzero Fourier-multiplier multiplicities, sharp projection norms onto singular ranges, or analogous classifications for other grid widths or boundary conditions. The displayed source comparisons are bounded rather than a certification of historical priority. No independent external mathematical audit has been performed.

## References
1. M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890v1, first public preprint 2007-01-30; full-text sections 1, 6 and 7.1, https://arxiv.org/html/math/0701890v2.
2. S. Oh and S. Lee, *Enumerating independent vertex sets in grid graphs*, arXiv:1609.00515v1, first public preprint 2016-09-02; full-text sections 1, 3 and 4, https://arxiv.org/html/1609.00515v1.
