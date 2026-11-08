# Exact prime-power cubic-chirp ambiguity and Gabor lifting spectrum

## Finding

Fix an odd prime \(p\), an integer \(k\geq1\), and \(N=p^k\). The unnormalized cubic chirp on the cyclic group \(\mathbb Z/N\mathbb Z\) is \(g(x)=\exp(2\pi i x^3/N)\). Define its ambiguity function by
\[
 A_g(a,b)=\sum_{x\bmod N}\overline{g(x)}g(x+a)\exp(-2\pi i bx/N).
\]
The following is a complete, all-frequency modulus and zero classification (including the exceptional prime \(3\)). Define \(t=v_p(a)\in\{0,\ldots,k-1\}\) for \(a\ne0\).

**Primes \(p\ge5\).** At \(a=0\), the only nonzero value is \(|A_g(0,0)|=N\). For \(a\ne0\),
\[
 |A_g(a,b)|=\begin{cases}p^{(k+t)/2},&p^t\mid b,\\0,&p^t\nmid b.\end{cases}
\]
For each \(t\), the positive modulus \(p^{(k+t)/2}\) occurs at exactly \(m_t=(p-1)p^{2(k-t)-1}\) frequency pairs; \(N\) occurs once. The ambiguity support has exactly
\[
 R_{p,k}=\frac{p^{2k+1}+1}{p+1}
\]
points.

**The exceptional prime \(p=3\).** If \(0\leq t\leq k-2\),
\[
 |A_g(a,b)|=\begin{cases}3^{(k+t+1)/2},&3^{t+1}\mid b,\\0,&3^{t+1}\nmid b.\end{cases}
\]
For the entire terminal translation stratum \(3^{k-1}\mid a\) (including \(a=0\)), the ambiguity is nonzero precisely for \(b=0\), where its modulus is \(N\). The positive modulus in the first display occurs at exactly \(m_t=2\,3^{2(k-t-1)}\) pairs for each \(0\leq t\leq k-2\), and \(N\) occurs at exactly three pairs. Therefore
\[
 R_{3,k}=\frac{3^{2k}+3}{4}.
\]
An empty range of \(t\) (as at \(k=1\)) contributes no entries.

**Operator spectrum.** Define \(T_a h(x)=h(x-a)\), \(M_b h(x)=\exp(2\pi i bx/N)h(x)\), and \(g_{a,b}=M_bT_a g\). Let the complex-linear Gabor intensity lifting map be
\[
 \mathcal L_g:M_N(\mathbb C)\longrightarrow\mathbb C^{N^2},\quad
 \mathcal L_g(H)_{a,b}=\operatorname{tr}(H g_{a,b}g_{a,b}^*),
\]
with Hilbert--Schmidt inner product on matrices and counting-measure Euclidean norm on outputs. The multiset of its \(N^2\) singular values is exactly \(\{\sqrt N|A_g(a,b)|:(a,b)\in(\mathbb Z/N\mathbb Z)^2\}\), including zeros. In particular, its rank equals \(R_{p,k}\). For \(p\ge5\), the positive singular values are \(p^{k+t/2}\) with multiplicities \(m_t\) and \(p^{3k/2}\) once; its positive-spectrum condition number is \(p^{k/2}\). For \(p=3\), the positive singular values are \(3^{k+(t+1)/2}\) with multiplicities \(m_t\) and \(3^{3k/2}\) three times; its positive-spectrum condition number is \(3^{(k-1)/2}\). The respective nullities are \(N^2-R_{p,k}\). As \(k\to\infty\) with \(p\) fixed, the fraction of identified matrix directions tends to \(p/(p+1)\) for primes \(p\ge5\), but to \(1/4\) for the prime \(3\).

## Assumptions and scope

All arithmetic is on the **cyclic ring** \(\mathbb Z/p^k\mathbb Z\), not on the generally noncyclic additive group of \(\mathbb F_{p^k}\). The vector \(g\) is not normalized by \(N^{-1/2}\); consequently the stated singular values are those for its raw rank-one projectors. Multiplying \(g\) by \(N^{-1/2}\) divides every singular value by \(N\) without changing rank, zeros, or positive condition number. Frequency signs are fixed by the displayed definition of \(A_g\); reversing the modulation sign only permutes frequencies. The domain of \(\mathcal L_g\) is **all complex matrices**, rather than only Hermitian matrices or rank-one signal matrices. No assertion of nonlinear phase retrieval follows solely from the lifting-rank formula.

## Proof

**Quadratic reduction.** Expanding the cubic phase gives the exact identity
\[
 A_g(a,b)=\exp(2\pi ia^3/N)\sum_{x\bmod N}\exp\!\left(\frac{2\pi i}{N}[3ax^2+(3a^2-b)x]\right).
\]
For a general quadratic Gauss sum \(G(A,B;p^k)\), let \(w=\min\{v_p(A),k\}\), with \(v_p(0)=+\infty\). If \(w<k\), grouping variables by their residues modulo \(p^{k-w}\) proves that \(G=0\) unless \(p^w\mid B\); when divisible, \(G=p^wG(A/p^w,B/p^w;p^{k-w})\). The coefficient \(A/p^w\) is a unit modulo \(p^{k-w}\). Since \(p\) is odd, the change of variables \((x,y)\mapsto(x-y,x+y)\) is bijective, and additive-character orthogonality gives
\[
 |G(U,V;p^j)|^2=\sum_{x,y}\exp\!\left(\frac{2\pi i}{p^j}[U(x^2-y^2)+V(x-y)]\right)=p^j
\]
for every unit \(U\). Thus the nonzero modulus is exactly \(p^{(k+w)/2}\). If \(w=k\), the quadratic term is zero and linear-character orthogonality makes \(G=N\) for \(B=0\pmod N\), and zero otherwise. These statements also prove all claimed zero/nonzero equivalences, not merely necessary vanishing conditions.

**Valuation strata.** If \(p\ge5\), for every nonzero \(a\) with \(v_p(a)=t\), the quadratic coefficient \(3a\) has valuation \(t\), while \(3a^2\) is divisible by \(p^t\). Thus the Gauss criterion reduces to \(p^t\mid b\). There are \((p-1)p^{k-t-1}\) such translations and \(p^{k-t}\) permitted modulations, yielding \(m_t\). At \(a=0\) only \(b=0\) survives.

For \(p=3\), a nonzero translation of valuation \(t\le k-2\) has \(v_3(3a)=t+1\); also \(3a^2\) is divisible by \(3^{t+1}\). This yields the second modular criterion and the multiplicity \((3-1)3^{k-t-1}\cdot3^{k-t-1}=2\,3^{2(k-t-1)}\). If \(3^{k-1}\mid a\), then both \(3a\) and \(3a^2\) vanish modulo \(3^k\), leaving a linear character: only \(b=0\) survives, for each of the three such translations. Summing geometric series gives the two stated ranks. Their limits follow directly after division by \(N^2=p^{2k}\).

**Lifting spectrum, including zero modes.** The \(N^2\) Weyl operators \(M_bT_a/\sqrt N\) form an orthonormal Hilbert--Schmidt basis. For a fixed Weyl input, the squared \(\ell_2\)-norm of its measurement vector under \(\mathcal L_g\) is \(N|A_g(a,b)|^2\); outputs for distinct Weyl inputs are orthogonal by the two-variable character orthogonality in the measurement indices. Therefore the complete singular-value multiset, not just the extreme frame bounds, is \(\sqrt N\) times the ambiguity-modulus multiset. The minimum positive modulus is \(p^{k/2}\) for \(p\ge5\) and \(3^{(k+1)/2}\) for \(p=3,k\ge2\) (for \(k=1\) all nonzero moduli equal \(N\)); the maximal modulus is \(N\). This proves the condition numbers, including \(k=1\).

## Verification

The included `check.py` computes the ambiguity values directly by numerical discrete Fourier transforms at every frequency for ten cyclic prime-power cases: \((p,k)=(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(11,1)\). It compares the full modulus matrix with the proved valuation prediction, support counts, and the Moyal/Parseval identity \(\sum_{a,b}|A_g(a,b)|^2=N^3\). For \(N=9\), it also constructs the full \(81\)-by-\(81\) complex lifting matrix and compares every singular value with the Weyl prediction. Numerical tolerance and finite test scope are explicit in the checker. Algebraic Gauss-sum orthogonality, rather than sampled data, proves the general theorem.

Reproduction: `python3 check.py` using Python 3 and NumPy. The final expected marker is `CUBIC_CHIRP_AMBIGUITY_STRATA_TESTS_OK`.

## Relationship to prior work

Bojarovska and Flinth (first public version 19 March 2015) established general Gabor lifting/ambiguity diagonalization and gave a negative observation about Alltop sequences as unrestricted phase-retrieval windows. This finding **does not claim** that diagonalization or that negative observation is new. Li (2026), Proposition 5.1, proved necessary ambiguity zeros for cubic chirps on \(p^k\) when \(p\ge5\) and \(k\ge2\). It already covers the vanishing half of the divisibility condition for higher-valuation translations, so that part is not novel. The claim assessed here is the *complete* nonvanishing converse, exact moduli and multiplicities, full complex lifted singular spectrum and rank, and especially the different complete \(p=3\) branch. A classical quadratic Gauss-sum calculation is a key existing tool; its use here is not claimed as new.

## Limitations

These are spectral statements about one explicit window on odd cyclic prime-power groups. They do not classify all cubic-phase windows, composite moduli with multiple distinct prime factors, or nonlinear recovery of arbitrary vectors. Known general formulas and ordinary quadratic Gauss sums make the proof elementary once this invariant is identified, and a broader existing table or implicit corollary might subsume the calculation. This manuscript reports a bounded originality comparison, **not independent certification or unconditional historical priority**. Numerical tests are corroboration only.

## References

1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (submitted 2015-03-19), especially Section 2, Theorem 2.3, and Example 2.3. https://arxiv.org/abs/1503.05800 ; open full text: https://arxiv.org/html/1503.05800v2
2. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614v1 (submitted 2026-09-09), especially Proposition 5.1. https://arxiv.org/abs/2609.09614
3. W. O. Alltop, *Complex sequences with low periodic correlations*, IEEE Transactions on Information Theory 26 (1980), 350–354 (as cited in Reference 1).
