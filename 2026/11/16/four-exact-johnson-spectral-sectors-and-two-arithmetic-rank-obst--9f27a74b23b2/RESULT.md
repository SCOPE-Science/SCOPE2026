# Four exact Johnson spectral sectors and two arithmetic rank obstructions for cubic Walsh sampling on Boolean slices

## Finding

For all integer dimensions \(n\ge6\) and slice weights \(0\le k\le n\), let \(S_{n,k}\subset\{-1,1\}^n\) be the sign vectors with exactly \(k\) negative coordinates. Let \(\chi_A(x)=\prod_{i\in A}x_i\) for each three-element index set \(A\). Equip \(S_{n,k}\) with uniform probability. The Gram matrix \(G_{AB}=\mathbb E_{x\in S_{n,k}}[\chi_A(x)\chi_B(x)]\) is indexed by all triples.

Put \(s=n-2k\). Every eigenvalue, including all zero eigenvalues, is one of the four exactly factored quantities below:

\[
\begin{aligned}
\lambda_0&=\frac{s^2(s^2-3n+2)^2}{6n(n-1)(n-2)},\\
\lambda_1&=\frac{(n^2-s^2)(s^2-n+2)^2}{2n(n-1)(n-2)(n-3)},\\
\lambda_2&=\frac{s^2(n^2-s^2)((n-2)^2-s^2)}{n(n-1)(n-2)(n-3)(n-4)},\\
\lambda_3&=\frac{(n^2-s^2)((n-2)^2-s^2)((n-4)^2-s^2)}{n(n-1)(n-2)(n-3)(n-4)(n-5)}.
\end{aligned}
\]

The multiplicity of \(\lambda_j\) is \(m_j=\binom nj-\binom n{j-1}\), for \(j=0,1,2,3\), taking \(\binom n{-1}=0\). Equal levels from different sectors have their multiplicities added. Thus the exact rank is \(\sum_{j:\lambda_j>0}m_j\).

The rank-defect locus is explicit: the constant sector vanishes exactly at \(s=0\) or \(s^2=3n-2\); the first sector exactly at \(|s|=n\) or \(s^2=n-2\); the second exactly at \(s=0\) or \(|s|\in\{n,n-2\}\); and the third exactly at \(|s|\in\{n,n-2,n-4\}\). In the interior \(3\le k\le n-3\), all losses are therefore either balanced-slice losses (sectors zero and two) or one of two disjoint arithmetic resonance families. The rank-one defect family is \(n=(u^2+2)/3\) with \(u^2\equiv1\pmod3\); the first-sector defect family is \(n=u^2+2\), for admissible integers \(u=|s|\). For example, \(n=17,k=5\) loses precisely one dimension and \(n=11,k=4\) loses precisely \(10\) dimensions.

## Assumptions and scope

The space of cubic characters is the coefficient space \(\mathbb R^{\binom n3}\) with its standard Euclidean inner product, and the sample measure is uniform probability on the chosen fixed-weight slice. The Gram matrix is a coefficient-side Gram, not the full Boolean-cube concentration operator. Indices are distinct within each triple. The formulas apply to boundary shells including \(k=0\) and \(k=n\) and have no hidden genericity assumptions. The restriction rank is the Gram rank because it is a squared sampling matrix.

## Proof

**1. Symmetry and the moments.** Set \(e_t=[z^t](1+z)^{(n+s)/2}(1-z)^{(n-s)/2}\), so \(e_0=1\), \(e_1=s\), and \(t e_t=s e_{t-1}-(n-t+2)e_{t-2}\) for \(t\ge2\). Since the negative-coordinate positions form a uniform \(k\)-subset, the product of any \(t\) distinct signs has expectation \(\mu_t=e_t/\binom nt\). The Gram entry for triples \(A,B\) is exactly \(\mu_{6-2|A\cap B|}\).

**2. Incidence expansion.** Let \(B_t\) be the inclusion matrix from \(t\)-subsets to triples: \(B_t(A,T)=\mathbf1_{T\subseteq A}\). Then \((B_tB_t^\mathsf T)_{AB}=\binom{|A\cap B|}t\). Writing the four values for intersection cardinality \(0,1,2,3\) in the binomial basis gives
\[
G=\sum_{t=0}^3 a_t B_tB_t^\mathsf T,\qquad
(a_0,a_1,a_2,a_3)=(\mu_6,\mu_4-\mu_6,\mu_2-2\mu_4+\mu_6,1-3\mu_2+3\mu_4-\mu_6).
\]

**3. Johnson harmonic diagonalization.** For \(n\ge6\), the real triples permutation module splits orthogonally into Johnson harmonic sectors \(U_j\), \(0\le j\le3\), of dimensions \(m_j=\binom nj-\binom n{j-1}\). The incidence identity is
\[
(B_tB_t^\mathsf T)|_{U_j}=
\begin{cases}
\binom{3-j}{t-j}\binom{n-t-j}{3-t} I,&j\le t,\\
0,&j>t.
\end{cases}
\]
It follows directly by lifting a degree-\(j\) harmonic coefficient vector first to \(t\)-subsets and then to triples, counting extensions of each fixed \(j\)-set, and canceling contributions from lower degrees; alternatively it is the standard Johnson inclusion-matrix eigenvalue identity. Hence
\[
\lambda_j=\sum_{t=j}^3 a_t\binom{3-j}{t-j}\binom{n-t-j}{3-t}.
\]

**4. Exact factorization and completeness.** Substitute the recurrence for \(e_t\), reduce the four rational expressions, and factor them. This gives exactly the four displayed formulas. The standalone symbolic checker verifies these four identities using polynomial falling-factorial binomial coefficients, without numerical fitting. The sector dimensions sum to \(\binom n3\), so there are no omitted eigenspaces.

**5. Zero classification.** Every denominator is positive for \(n\ge6\). The factors \(n^2-s^2\), \((n-2)^2-s^2\), and \((n-4)^2-s^2\) are nonnegative for admissible \(s=n-2k\) whenever the corresponding factor appears in a positive-level interior sector; at boundaries the displayed zero factors exhaust the additional losses. Checking zeros of each numerator gives the exact sector list above. The two unbalanced interior resonance equations \(s^2=3n-2\) and \(s^2=n-2\) cannot both hold for \(n\ge6\), since they would imply \(2n=0\). They have infinitely many admissible integer solutions (choose \(s=u\) with \(u\not\equiv0\pmod3\) in the first case, or \(s=u\) in the second, and take sufficiently large \(u\)); parity is automatic in both formulas. This proves the complete rank law, including the infinite exceptional families.

## Verification

Run \(`python verify_symbolic.py`\) to reconstruct and factor all four eigenvalues from the elementary-moment recurrence and Johnson incidence formula. Run \(`python verify.py`\) with Python 3 and NumPy for direct slice-enumeration Gram matrices for all 57 \(n,k\) cases with \(6\le n\le11\), plus four larger exceptional parameter tests. The scripts are self-contained and included with this result. Finite tests corroborate the infinite proof; they are not substitutes for it.

## Relationship to prior work

The standard harmonic decomposition of Johnson slices is developed in Filmus's 2014 work on slice bases. Rao's November 2021 paper investigates Fourier transforms of restrictions to a Boolean slice and gives general representation machinery, but the inspected introduction and technical sections do not state the four factored pure-cubic Gram eigenvalues or the two arithmetic rank-defect families. A published all-degree q-ary Hamming sphere result addresses alphabets \(q\ge3\) and the *full* degree-at-most-\(d\) Fourier band, not the binary *homogeneous cubic* band. A published cubic-spherical-harmonic hypersimplex result studies a different, continuous spherical harmonic feature space and different Pell-type rank losses. General Johnson association-scheme diagonalization predates the present calculation and is not claimed as new.

## Limitations

The result addresses only homogeneous degree-three Walsh features and their coefficient Gram on a single binary fixed-weight slice; it does not optimize condition numbers or extend to other interaction orders. Numerical checks end at the indicated finite sizes. The precise formula is independently reproducible but historic novelty remains subject to a broader search of association-scheme and design literature. No independent mathematical audit has been performed.

## References

[1] S. Rao, *The Fourier Transform of Restrictions of Functions on the Slice*, arXiv:2111.03213v1, publicly posted 2021-11-05, https://arxiv.org/abs/2111.03213.

[2] Y. Filmus, *An Orthogonal Basis for Functions over a Slice of the Boolean Hypercube*, arXiv:1406.0142, https://arxiv.org/abs/1406.0142.

[3] *An all-degree spectral law for Fourier sampling on q-ary Hamming spheres*, publicly available mathematical finding (2026), https://github.com/published-finding corpus/2026.

[4] *Pell resonances in cubic spherical-harmonic sampling on hypersimplices*, publicly available mathematical finding (2026), https://github.com/published-finding corpus/2026.
