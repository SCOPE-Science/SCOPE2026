# Sharp ternary signed-residue bias of four-ary Fuss–Catalan binomial numerators

## Finding
For every nonnegative integer \(n\), set \(b(n)=\binom{4n}{n}\). For each integer \(L\geq0\) and \(r\in\{0,1,2\}\), set
\[
N_r(L)=\#\{0\leq n<3^L:b(n)\equiv r\pmod3\}.
\]
Let \(U_L=N_1(L)+N_2(L)\) and \(D_L=N_1(L)-N_2(L)\). The signed frequency difference satisfies the **exact rational law**
\[
\boxed{\sum_{L\geq0}D_Lz^L=\frac{1+3z+z^2}{1-3z^2-z^3}}.
\]
In particular \(D_0=1\), \(D_1=3\), \(D_2=4\) and \(D_L=3D_{L-2}+D_{L-3}\) for \(L\geq3\), so the residue-one class strictly exceeds the residue-two class at every complete ternary cutoff.

Define \(\vartheta=2\cos(\pi/9)\), the largest root of \(t^3-3t-1=0\), and
\[
\kappa=\frac{1+3/\vartheta+1/\vartheta^2}{6/\vartheta^2+3/\vartheta^3}>0.
\]
Then
\[
\boxed{D_L=\kappa\vartheta^L+O((2\cos(2\pi/9))^L)}.
\]
For each integer \(X\geq1\), put
\[
\Delta(X)=\#\{0\leq n<X:b(n)\equiv1\pmod3\}-\#\{0\leq n<X:b(n)\equiv2\pmod3\}.
\]
The **global prefix bound and its sharpness** are
\[
\boxed{\lvert\Delta(X)\rvert=O(X^\alpha),\qquad
\max_{1\leq X\leq Y}\lvert\Delta(X)\rvert=\Theta(Y^\alpha),\quad
\alpha=\frac{\log\vartheta}{\log3}=0.5743106378\ldots.}
\]
The exponent is achieved along \(X=3^L\), not claimed as a two-sided bound at every \(X\).

As a known, separately established unsigned baseline, the nonzero total also has generating function
\[
\sum_{L\geq0}U_Lz^L=\frac{1+z-z^2}{1-2z-z^2+z^3}.
\]
The new signed law combined with the existing unsigned census gives \(N_{1,2}(L)=(U_L\pm D_L)/2\), and the two nonzero residue counts are asymptotically equidistributed because the unsigned Perron root \(2.2469796037\ldots\) is larger than \(\vartheta\). The novelty claim concerns the **signed residue distribution and sharp global prefix exponent**, not the previously established nondivisible-support formula.

## Assumptions and scope
All binomial coefficients are ordinary integers, including \(b(0)=1\). The modulus is exactly the prime \(3\). All index ranges are half-open and begin at zero. The cutoff \(L\) is an integer \(\geq0\), while \(X,Y\) are positive integers. The residue sign associated with \(b(n)\pmod3\) is \(+1\) for residue one, \(-1\) for residue two, and \(0\) for residue zero. The result applies equally to the four-ary Fuss–Catalan integers \(b(n)/(3n+1)\), because \(3n+1\equiv1\pmod3\).

## Proof
**Digit formula.** Write \(n=\sum_{j\geq0}d_j3^j\) with \(d_j\in\{0,1,2\}\) and all sufficiently high digits zero; set \(d_{-1}=0\). Since \(4n=n+3n\), there is no carry in that ternary addition exactly when \(d_j+d_{j-1}\leq2\) for every \(j\). A carry forces \(3\mid b(n)\) by Kummer's criterion. In the no-carry case, Lucas's theorem yields
\[
 b(n)\equiv\prod_{j\geq0}\binom{d_j+d_{j-1}}{d_j}\pmod3.
\]
Every admissible local factor equals one modulo three except \(\binom21=2\equiv-1\pmod3\), which occurs precisely at an adjacent digit pair \((d_j,d_{j-1})=(1,1)\). Thus the signed residue equals zero on inadmissible ternary strings and \((-1)^h\) on admissible strings, where \(h\) counts overlapping adjacent \(11\) pairs.

**Transfer and exact generating function.** For states \(0,1,2\) recording the previous digit, the unsigned and signed digit-transition matrices are, respectively,
\[
 A=\begin{pmatrix}1&1&1\\1&1&0\\1&0&0\end{pmatrix},\qquad
 B=\begin{pmatrix}1&1&1\\1&-1&0\\1&0&0\end{pmatrix}.
\]
Both are symmetric. With \(e_0=(1,0,0)^\mathsf T\) and \({\bf1}=(1,1,1)^\mathsf T\), padding the ternary expansion to exactly \(L\) digits gives \(U_L=e_0^\mathsf T A^L{\bf1}\) and \(D_L=e_0^\mathsf T B^L{\bf1}\). The exact integer matrix identities are
\[
 A^3=2A^2+A-I,\qquad B^3=3B+I.
\]
The first three signed values are \(1,3,4\). Hence \(D_L=3D_{L-2}+D_{L-3}\) and the displayed rational generating function follows by multiplying the series by \(1-3z^2-z^3\). The same computation with \(A\) gives the stated already-known unsigned generating function, which is supplied for comparison rather than novelty.

**Dominant signed root and positivity.** The characteristic polynomial of \(B\) is \(t^3-3t-1\) with distinct real roots \(2\cos(\pi/9)\), \(2\cos(5\pi/9)\), and \(2\cos(7\pi/9)\). Their absolute values are, in decreasing order, \(\vartheta=1.8793852415\ldots\), \(2\cos(2\pi/9)=1.5320888862\ldots\), and \(2\cos(4\pi/9)=0.3472963553\ldots\). The generating function has a simple pole at \(1/\vartheta\); its leading coefficient is the displayed \(\kappa\), obtained from \(-P(1/\vartheta)/[(1/\vartheta)Q'(1/\vartheta)]\) for numerator \(P\) and denominator \(Q\). Spectral decomposition therefore proves the asymptotic including the error term. Moreover, the initial signed values and the positive-coefficient recurrence prove \(D_L>0\) for every \(L\geq0\).

**All cutoffs and optimality.** A ternary-aligned cylinder of length \(3^j\) fixes all digits above position \(j-1\), allowing its \(j\) lower digits to vary. If the fixed higher digits are already inadmissible its signed sum is zero. Otherwise its signed sum is \(\pm e_0^\mathsf TB^{j+1}e_b\) for the first fixed higher digit \(b\in\{0,1,2\}\), because the sign from all other fixed higher adjacent pairs is constant. Indeed, the extra matrix factor accounts for the boundary pair between the highest free digit and that fixed digit. The symmetry of \(B\) and its real eigenvalues imply, in Euclidean norm,
\[
 \lvert e_0^\mathsf TB^{j+1}e_b\rvert\leq\vartheta^{j+1}.
\]
The ternary expansion of any integer \(X\geq1\) partitions \([0,X)\) into at most two such aligned cylinders of each length \(3^j\), where \(0\leq j\leq\lfloor\log_3 X\rfloor\). Their signed sums therefore give \(\lvert\Delta(X)\rvert\leq2\vartheta\sum_{j\leq\lfloor\log_3X\rfloor}\vartheta^j=O(X^\alpha)\). At \(X=3^L\), the proved main term \(\kappa\vartheta^L\) is positive and asymptotic to \(\kappa X^\alpha\), giving optimality, including the max-over-cutoffs statement.

## Verification
Run `python3 checker.py` from an extracted directory containing this file. The standard-library-only script verifies both exact matrix characteristic-polynomial identities, checks the full signed and unsigned recurrences for fourteen lengths, compares the digit rule against **ordinary exact integer binomial coefficients** for all \(0\leq n<2600\), and independently enumerates all three residues for every complete ternary interval with \(0\leq L\leq7\). It prints `VERIFY_OK` on success. For \(L=6\), the three counts are \((N_0,N_1,N_2)=(572,106,51)\); for \(L=7\), they follow the printed checker output. These finite computations test the formulas but are not offered as proofs of all-length or all-cutoff assertions; the argument above supplies those quantifiers.

## Relationship to prior work
Lucas's classical theorem supplies the residue digit factorization. Cinkir and Ozturkalan (2023) develop extensions of Lucas-type prime congruence computations and binomial-sum identities; their Sections 1–4 do not formulate this diagonal signed-residue census. Barat and Grabner (2001/2002), particularly their Section 2 and Lemma 1, develop general digit-block summation and transfer techniques; the present method is a concrete specialization, but their results do not state the exact signed three-residue law, its positive closed-block bias, or this family's sharp prefix exponent. A 2026 published study of prime-relative Fuss–Catalan nondivisibility proves the no-carry criterion and already determines the **unsigned** block count and dimension for the same numerator at prime three. Neither that unsigned theorem nor its full text determines the signed residue imbalance; the unsigned support is explicitly excluded from the present novelty claim. A published signed count for \(\binom{4n}{2n}\pmod5\) concerns a different diagonal and prime and its oscillatory signed law does not imply the present positive recurrence. OEIS A006356 records the unsigned recurrence, and OEIS A188022 records the same numerical signed recurrence with an index shift, but under an unrelated tridiagonal-matrix interpretation rather than the signed residues of \(\binom{4n}{n}\); recurrence values as a table alone do not establish the binomial correspondence or arbitrary-prefix sharpness.

## Limitations
The results are specific to the modulus three and the four-to-one binomial diagonal. They do not give prime-power residue laws, leading coefficients for arbitrary real cutoffs, or uniformity as the modulus varies. Prior general digital-function methods readily motivate the proof; an unlocated equivalent specialization could affect historical originality. The finite checker does not establish infinite statements. Independent mathematical audit has not been performed.

## References
1. Z. Cinkir and A. Ozturkalan, *An extension of Lucas Theorem*, arXiv:2309.00109, first posted 2023-08-31. https://arxiv.org/abs/2309.00109
2. G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, Journal of the London Mathematical Society 64 (2001), 523–547, DOI:10.1112/S0024610701002630; lawful author manuscript: https://www.math.tugraz.at/~grabner/Publications/Binomial.pdf
3. *Prime-relative Fuss–Catalan nondivisibility: exact spectra and p-adic dimension*, published record (2026-11-08). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-prime-relative-fuss-catalan-nondivisibility-exact-spectra-and-p--fca5ba9f3d60
4. *Sharp square-root imbalance for* \(\binom{4n}{2n}\) *modulo five*, published record (2026-10-26). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-square-root-imbalance-for-binom-4n-2n-modulo-five--88cd6f9d99bb
5. The On-Line Encyclopedia of Integer Sequences, A006356, https://oeis.org/A006356; and A188022, https://oeis.org/A188022.
