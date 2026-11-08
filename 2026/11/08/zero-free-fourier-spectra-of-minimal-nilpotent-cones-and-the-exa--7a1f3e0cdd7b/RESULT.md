# Zero-free Fourier spectra of minimal nilpotent cones and the exact \(3\times3\) census

## Finding

Let \(q\ge2\) be any prime power and \(n\ge3\). On \(M_n(\mathbb F_q)\) consider the affine cone \(\mathcal N_{n,q}=\{X:\operatorname{rank}X\le1,\ X^2=0\}\), the closure of the smallest nonzero nilpotent conjugacy orbit. Let \(\psi\) be any nontrivial additive character of \(\mathbb F_q\), and use the trace-pairing Fourier transform \(\widehat{1_{\mathcal N}}(A)=\sum_{X\in\mathcal N}\psi(\operatorname{tr}(AX))\). For each \(A\), let \(E(A)\) denote the number of \(\mathbb F_q\)-rational eigenlines, including lines in higher-dimensional eigenspaces but counting each line once.

The transform is exactly
\[
\widehat{1_{\mathcal N}}(A)=q^{n-1}E(A)-\sum_{j=1}^{n-1}q^j.
\]
In particular, for every frequency,
\[
\widehat{1_{\mathcal N}}(A)\equiv-q\pmod{q^2},
\]
so the unnormalized convolution operator \(T_{\mathcal N}f=1_{\mathcal N}*f\) is invertible on the entire \(q^{n^2}\)-dimensional complex function space for every characteristic.

Its smallest singular value is exactly
\[
\sigma_{\min}(T_{\mathcal N})=
\begin{cases}
2,&q=2,\\
\displaystyle\sum_{j=1}^{n-2}q^j,&q\ge3.
\end{cases}
\]
The exact cardinality is
\[
|\mathcal N|=1+\frac{(q^n-1)(q^{n-1}-1)}{q-1}.
\]
The largest singular value is exactly \(|\mathcal N|\), so the spectral condition number is \(|\mathcal N|/\sigma_{\min}\).

For \(n=3\), the complete singular spectrum follows by taking absolute values of \(q^2E-q(q+1)\) at each \(E\) in the following table. Put \(G=(q^3-1)(q^3-q)(q^3-q^2)\), the order of \(\operatorname{GL}_3(\mathbb F_q)\).

| Rational eigenline count \(E\) | Fourier eigenvalue | Multiplicity |
| --- | --- | --- |
| \(0\) | \(-q(q+1)\) | \((q^3-q)G/[3(q^3-1)]\) |
| \(1\) | \(-q\) | \(G/[q(q-1)]+q^2G/[2(q^2-1)]\) |
| \(2\) | \(q(q-1)\) | \(G/(q-1)\) |
| \(3\) | \(q(2q-1)\) | \(q(q-1)(q-2)G/[6(q-1)^3]\) |
| \(q+1\) | \(q(q^2-1)\) | \(q(q^3-1)(q+1)\) |
| \(q+2\) | \(q(q^2+q-1)\) | \(q^3(q^3-1)\) |
| \(q^2+q+1\) | \(q^4+q^3-q\) | \(q\) |

For \(q=2\), the formal values \(E=3\) and \(E=q+1\) coincide, but the multiplicity in the \(E=3\) row is zero; each frequency is counted exactly once. The table multiplicities sum to \(q^9\). Therefore the convolution rank is exactly \(q^9\) when \(n=3\), and for all \(n\ge3\) it is \(q^{n^2}\).

## Assumptions and scope

All statements hold for each finite field \(\mathbb F_q\) of prime-power order \(q\), all integers \(n\ge3\), all nontrivial additive characters \(\psi\), and all matrices \(A\in M_n(\mathbb F_q)\). The trace pairing is \(\operatorname{tr}(AX)\); transposing the frequency changes no eigenline count. Fourier and convolution are unnormalized, and singular values refer to the usual counting-measure \(\ell^2\)-norm. Congruences concern the integer-valued Fourier transform, not a congruence in a cyclotomic field.

## Proof

**Step 1: orbit parameterization and exact character sum.** Every nonzero rank-one, square-zero matrix is \(uv^{\mathsf T}\) for a nonzero column \(u\) and a nonzero column \(v\) satisfying \(v^{\mathsf T}u=0\). Exactly \(q-1\) ordered pairs \((u,v)\) give each such matrix, by \((u,v)\mapsto(cu,c^{-1}v)\). Thus, writing \(U\) for the set of nonzero columns,
\[
\widehat{1_{\mathcal N}}(A)=1+\frac{1}{q-1}\sum_{u\in U}\left(\sum_{v\in u^\perp}\psi(v^{\mathsf T}Au)-1\right).
\]
The inner complete hyperplane character sum is \(q^{n-1}\) if \(Au\in\mathbb F_q u\), and zero otherwise, by the character-orthogonality theorem. Exactly \((q-1)E(A)\) vectors \(u\in U\) satisfy that eigenvector condition. Consequently
\[
\widehat{1_{\mathcal N}}(A)=1+q^{n-1}E(A)-\frac{q^n-1}{q-1}
=q^{n-1}E(A)-\sum_{j=1}^{n-1}q^j.
\]
The derivation also shows \(|\mathcal N|=1+(q^n-1)(q^{n-1}-1)/(q-1)\) by setting \(A=0\).

**Step 2: invertibility and optimal least singular value.** For \(n\ge3\), all terms \(q^j\) with \(j\ge2\) are divisible by \(q^2\); moreover \(n-1\ge2\). Hence every Fourier eigenvalue is congruent to \(-q\) modulo \(q^2\) and cannot vanish. The set \(\mathcal N\) is stable under \(X\mapsto-X\), so convolution is self-adjoint and its singular values are exactly \(|\widehat{1_{\mathcal N}}(A)|\).

Write \(B=\sum_{j=1}^{n-2}q^j\). Then \(\widehat{1_{\mathcal N}}(A)=q^{n-1}(E(A)-1)-B\). If \(q\ge3\), one has \(0<B<q^{n-1}/2\), so the unique closest possible integer \(E\ge0\) to \(1+B/q^{n-1}\) is \(E=1\), and the minimum modulus is \(B\). This minimum occurs for \(A\) equal to a one-dimensional scalar block direct-summed with a companion matrix of an irreducible polynomial of degree \(n-1\); irreducible polynomials exist over all finite fields. If \(q=2\), then \(B=2^{n-1}-2\), and the least modulus is \(2\), attained at \(E=2\) by a direct sum of one nontrivial Jordan block of length \(n-1\) at eigenvalue zero and a one-dimensional block at eigenvalue one. No noninteger \(E\) is possible, so these minima are sharp. The largest singular value is \(|\mathcal N|\), attained at \(A=0\), by the triangle inequality.

**Step 3: exact three-by-three multiplicities.** Classification by rational Jordan/Frobenius types gives at most seven values of \(E(A)\); a formally listed type is empty when \(q=2\). Irreducible-cubic characteristic polynomials give \(E=0\). A single length-three Jordan block, or a direct sum of a linear and an irreducible-quadratic block, gives \(E=1\). Two distinct eigenvalues with a nontrivial length-two Jordan block give \(E=2\), and three distinct eigenvalues give \(E=3\). A length-two Jordan block and a one-dimensional block at the *same* eigenvalue give \(E=q+1\). Diagonalizable matrices with one eigenvalue of multiplicity two and another of multiplicity one give \(E=q+2\). Scalar matrices give \(E=q^2+q+1\).

For these strata the counts follow from \(|\operatorname{GL}_3(\mathbb F_q)|=G\) and the stabilizer formula \(\#\operatorname{orbit}=G/\#\operatorname{centralizer}^{\times}\). The required unit-centralizer orders are respectively \(q^3-1\) for an irreducible cubic; \(q^2(q-1)\) for a single length-three Jordan block; \((q^2-1)(q-1)\) for quadratic-plus-linear; \(q(q-1)^2\) for a length-two block plus a distinct eigenvalue; \((q-1)^3\) for distinct diagonal eigenvalues; \(q^3(q-1)^2\) for a length-two block plus a same-eigenvalue line; and \(|\operatorname{GL}_2(\mathbb F_q)|(q-1)\) for a diagonalizable double plus a distinct simple eigenvalue. Multiply these class sizes by, respectively, \((q^3-q)/3\), \(q\), \(q(q^2-q)/2\), \(q(q-1)\), \(\binom q3\), \(q\), and \(q(q-1)\) choices of field elements or irreducible polynomials, and add the \(q\) scalar matrices. These computations give exactly the seven multiplicities listed in the theorem and sum to \(q^9\). The Fourier-multiplier formula gives each eigenvalue.

## Verification

The standalone file `nilpotent_spectrum_checker.py` reconstructs the nonzero rank-one square-zero cone directly, enumerates eigenlines independently, and computes additive Fourier sums over the cone. Execute `python3 nilpotent_spectrum_checker.py` with Python and NumPy installed. It tests **every frequency** over \(\mathbb F_2\) (512 frequencies) and \(\mathbb F_3\) (19683 frequencies), including the complete predicted eigenline-multiplicity census. It also checks 701 fixed-seed frequencies each over \(\mathbb F_4\) and \(\mathbb F_5\), using explicit field arithmetic and exact cyclotomic character grouping rather than floating-point tolerance. Successful execution ends with `ALL_MINIMAL_NILPOTENT_SPECTRUM_CHECKS_OK`. These finite tests are corroboration; the proof above is valid for all dimensions and field orders.

## Relationship to prior work

Fourier transforms of invariant functions on finite reductive Lie algebras and character-sum reductions to generalized Green functions were treated by Letellier [1], including an explicitly relevant chapter on transforms of adjoint-orbit indicators. The present elementary hyperplane-sum formula concerns one very specific nilpotent orbit closure and supplies its zero-free integer spectrum, sharp least singular value, and full three-by-three multiplicity census. The chapter's complete text could not be inspected, so an equivalent earlier specialization remains possible. Achar and Mautner [2] study geometric Fourier–Sato transforms and categorical duality on nilpotent cones over complex reductive groups, not this explicit finite-field additive indicator spectrum. Delsarte's bilinear-forms Fourier theory [3] concerns matrix rank classes rather than the smaller trace-zero rank-one nilpotent orbit. The elementary character-orthogonality and conjugacy-class counting methods are standard and are not claimed to originate here.

## Limitations

No unconditional priority claim is made. A pre-existing general orbit-Fourier theorem, Green-function specialization, or unavailable detailed table may imply the same explicit formulas. Direct full-text comparison with Letellier's orbit-indicator chapter was not possible. The exact seven-stratum classification is only asserted for matrix size three; for larger sizes the formula through rational eigenline counts and the sharp spectral bounds remain valid, but no full multiplicity table is claimed. Finite checks do not independently certify universal statements. Independent mathematical audit and validation have not been performed.

## References

[1] Emmanuel Letellier, *Fourier Transforms of Invariant Functions on Finite Reductive Lie Algebras*, Lecture Notes in Mathematics 1859, Springer eBook first released 15 November 2004, DOI: https://doi.org/10.1007/b104209; particularly Chapter 7, *Fourier Transforms of the Characteristic Functions of the Adjoint Orbits*.

[2] Pramod N. Achar and Carl Mautner, *Sheaves on nilpotent cones, Fourier transform, and a geometric Ringel duality*, arXiv:1207.7044, originally posted 30 July 2012, https://arxiv.org/abs/1207.7044.

[3] Philippe Delsarte, *Bilinear forms over a finite field, with applications to coding theory*, J. Combin. Theory Ser. A **25** (1978), 226–241, DOI: https://doi.org/10.1016/0097-3165(78)90015-8.
