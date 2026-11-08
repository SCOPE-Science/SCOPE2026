# Exact self-Fourier singular spectrum on the nonzero nilpotent cone in \(2\times2\) matrices

## Finding

Let \(q\ge2\) be a prime power, let \(F=\mathbb F_q\), and let \(\psi:F\to\mathbb C^\times\) be any nontrivial additive character. Write
\[
\mathcal N_q=\{X\in M_2(F):X\ne0,\ X^2=0\},\qquad
H_q=(\psi(\operatorname{tr}(XY)))_{X,Y\in\mathcal N_q}.
\]
The set has \(q^2-1\) elements. The **complete unnormalized singular-value multiset** of \(H_q\) is:

* If \(q\) is even: \(1\) with multiplicity \(1\), and \(q\) with multiplicity \(q^2-2\).
* If \(q\) is odd: \(1\) with multiplicity \(1\), \(\sqrt q\) with multiplicity \(q\), \(q\) with multiplicity \(q^2-q-3\), and \(q^{3/2}\) with multiplicity \(1\).

Every multiplicity in these formulas is nonnegative, and repeated values are merged (none coincide for the permitted values). Thus \(H_q\) is nonsingular for **every** prime power and every nontrivial additive character. Its sharp Euclidean singular-value condition number is \(q\) in even characteristic and \(q^{3/2}\) in odd characteristic. In particular, every complex signal supported on \(\mathcal N_q\) is uniquely determined by its ambient additive Fourier transform sampled on \(\mathcal N_q\) itself.

## Assumptions and scope

The Fourier matrix is not divided by \(q\) or any square root. The pairing is the matrix trace of a product, not the entrywise dot product. For each \(q\), the statement holds uniformly in the choice of nontrivial additive character \(\psi\). No restriction to an individual conjugacy orbit is made; over odd fields both nonzero rational nilpotent orbits are present. The origin is excluded. Characteristic \(2\) is included, even though the full trace pairing restricted to the traceless Lie algebra is then degenerate. The claim concerns complex linear recovery, not phaseless recovery or recovery with omitted samples.

## Proof

**1. Parameterize the punctured cone.** Put
\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
\nu_t=\begin{cases}(1,t)^{\mathsf T}&t\in F,\\(0,1)^{\mathsf T}&t=\infty,\end{cases}
\qquad X_{t,s}=s\nu_t\nu_t^{\mathsf T}J,
\]
where \(t\in\mathbb P^1(F)\) and \(s\in F^\times\). The matrix \(X_{t,s}\) has rank \(1\), trace \(0\), and square \(0\); conversely every nonzero square-zero \(2\times2\) matrix has one-dimensional image equal to its kernel and is uniquely of this form after choosing the normalized representative \(\nu_t\). There are \((q+1)(q-1)=q^2-1\) such matrices. For \(\Delta(t,r)=\det(\nu_t,\nu_r)\), a direct rank-one trace calculation gives exactly
\[
\operatorname{tr}(X_{t,s}X_{r,v})=-sv\Delta(t,r)^2.
\]
Here \(\Delta(t,r)=0\) exactly when \(t=r\), in all characteristics.

**2. Diagonalize the scalar directions.** Each fibre \(\{X_{t,s}:s\in F^\times\}\) carries the multiplicative-character basis. Let \(\chi\) range over the \(q-1\) unitary multiplicative characters of \(F^\times\); the normalized vectors \(s\mapsto\chi(s)/\sqrt{q-1}\) yield an orthonormal splitting of the domain (and likewise the range). If \(\chi=1\), the scalar block between different projective points is
\(\sum_{v\in F^\times}\psi(-sv\Delta^2)=-1\), whereas the same-point block equals \(q-1\). Hence the corresponding \((q+1)\times(q+1)\) matrix is \(qI-\mathbf1\mathbf1^{\mathsf T}\); its singular values are \(1\) once and \(q\) exactly \(q\) times.

For \(\chi\ne1\), the same-point block is zero, and for \(t\ne r\), changing variables in the classical Gauss sum yields
\[
\sum_{v\in F^\times}\chi(v)\psi(-sv\Delta(t,r)^2)
=G_\psi(\chi)\,\chi(-1)^{-1}\chi(s)^{-1}\chi(\Delta(t,r))^{-2},
\quad G_\psi(\chi)=\sum_{v\in F^\times}\chi(v)\psi(v).
\]
Thus this sector maps isometrically (up to a scalar) to the inverse-character sector and its singular values equal \(\sqrt q\) times those of the \((q+1)\times(q+1)\) matrix
\[
K_\chi(t,r)=\begin{cases}0&t=r,\\\chi(\Delta(t,r))^{-2}&t\ne r.\end{cases}
\]
The standard exact Gauss-sum identity \(|G_\psi(\chi)|=\sqrt q\) holds for every nontrivial \(\chi\) and every nontrivial additive \(\psi\). It follows by expanding \(|G|^2\), changing the two nonzero variables to their ratio, and using character orthogonality; no asymptotic estimate is used.

**3. Determine each projective block.** Suppose \(\chi^2\ne1\). Each row of \(K_\chi\) has \(q\) off-diagonal entries of modulus \(1\), so the diagonal of \(K_\chi K_\chi^*\) is \(q\). For distinct \(t,u\), its \((t,u)\) entry is
\[
\sum_{r\in\mathbb P^1(F)\setminus\{t,u\}}
\chi^2\!\left(\frac{\Delta(u,r)}{\Delta(t,r)}\right).
\]
The map \(r\mapsto\Delta(u,r)/\Delta(t,r)\) is a projective fractional-linear transformation, restricting to a bijection from the indicated \(q-1\) points onto \(F^\times\). Because \(\chi^2\) is nontrivial, its sum over \(F^\times\) is zero. Therefore \(K_\chi K_\chi^*=qI\), so **all \(q+1\) singular values of this sector are \(q\)** after the Gauss-sum factor. This is an exact complex-conference identity, not a numerical observation.

If \(\chi^2=1\) and \(\chi\ne1\), which occurs precisely for the unique quadratic character when \(q\) is odd, every off-diagonal entry of \(K_\chi\) is \(1\). Thus \(K_\chi=\mathbf1\mathbf1^{\mathsf T}-I\), with singular values \(q\) once and \(1\) with multiplicity \(q\). After multiplication by \(\sqrt q\), these are \(q^{3/2}\) once and \(\sqrt q\) with multiplicity \(q\).

**4. Count dimensions and sharp bounds.** When \(q\) is even, the group \(F^\times\) has odd order, so its only character satisfying \(\chi^2=1\) is the trivial one. Exactly \(q-2\) nontrivial characters contribute \(q+1\) singular values equal to \(q\); including the trivial sector gives \(q+(q-2)(q+1)=q^2-2\) copies of \(q\) and one copy of \(1\). When \(q\) is odd, one nontrivial quadratic character contributes the two exceptional singular levels, and the remaining \(q-3\) characters contribute \(q+1\) copies of \(q\) each. Together with the trivial sector this gives \(q+(q-3)(q+1)=q^2-q-3\) copies of \(q\), \(q\) copies of \(\sqrt q\), and the two singletons. Each total is \(q^2-1\), so all sectors are accounted for and no zero singular value occurs. The smallest singular value is \(1\); the maxima are respectively \(q\) and \(q^{3/2}\), proving the stated sharp condition numbers. \(\square\)

## Verification

The self-contained source `check_spectrum.py` constructs the ambient trace-pairing entries for every nonzero square-zero matrix, using an explicit arithmetic model of \(F\). With NumPy it compares the directly computed singular values against the exact formulas, without using the character-block calculation. Tested field sizes are \(q=2,3,4,5,7,8,9,11\), including nonprime extension fields in both characteristics. The largest absolute singular-value discrepancy observed across these tests was below \(8\times10^{-15}\). Replay with `OPENBLAS_NUM_THREADS=1 python check_spectrum.py`; the required external Python package is specified in `requirements.txt`. The finite tests are evidence for implementation and normalization only; the infinite family is established by the preceding proof.

## Relationship to prior work

Fourier transforms on finite reductive Lie algebras and their nilpotent subsets are classical objects. Kawanaka (1982) and the accessible full-text analysis of Taylor (online 2016, especially Section 6) study transforms of invariant functions and associated representations. Achar–Mautner (arXiv 2012) establish a Fourier–Sato autoequivalence of nilpotent-cone sheaf categories: this is not a numerical singular-value statement for the matrix of arbitrary complex functions on the punctured finite-field cone. The present theorem instead determines every singular value of a **square restricted character matrix**, on every scalar and projective direction and for all characteristics.

Related Fourier-sampling results for a half-cone of symmetric rank-one squares over odd fields and for origin-included nondegenerate quadratic cones in even ambient dimensions do not directly imply the present punctured three-dimensional nilpotent-cone spectrum. The present proof also uses the classical finite-field multiplicative-character/conference-matrix orthogonality identity; that identity is not claimed to be new. The decisive synthesis is the exact fibre decomposition and its sampling consequence for this natural nilpotent locus.

## Limitations

No statement is made for nilpotent matrices of order \(3\) or higher, for individual nonzero rational nilpotent orbits, or for deleting further rows or columns. No phaseless uniqueness follows. Complete historical priority is not established: Kawanaka (1982) was identifiable but its full original article was unavailable in this review; a stronger unexamined result could imply this formula. None of the accessible, materially inspected sources established such an implication. The provided computation is finite and does not independently certify the proof.

## References

1. P. N. Achar and C. Mautner, *Sheaves on nilpotent cones, Fourier transform, and a geometric Ringel duality*, arXiv:1207.7044, first submitted 2012-07-30. https://arxiv.org/abs/1207.7044 (full HTML text available).
2. J. Taylor, *Generalized Gelfand–Graev representations in small characteristics*, Nagoya Math. J. 224 (2016), 93–167; online 2016-09-09; https://doi.org/10.1017/nmj.2016.33 (full HTML text, Sections 3 and 6 inspected).
3. N. Kawanaka, *Fourier transforms of nilpotently supported invariant functions on a simple Lie algebra over a finite field*, Invent. Math. 69 (1982), 411–435, https://doi.org/10.1007/BF01389363 (bibliographic record; complete source inaccessible during comparison).
