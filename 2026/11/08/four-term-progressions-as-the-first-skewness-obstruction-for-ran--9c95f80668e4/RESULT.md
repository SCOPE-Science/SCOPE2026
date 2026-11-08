# Four-term progressions as the first skewness obstruction for random-phase Fourier fourth moments

## Finding
Let \(A\subset\mathbb Z\) be any nonempty finite set, let \((\xi_a)_{a\in A}\) be independent Haar-uniform unit complex numbers, and set
\[
P_A(t)=\sum_{a\in A}\xi_a e^{2\pi iat},\qquad X_A=\int_0^1|P_A(t)|^4\,dt.
\]
Write \(N_4(A)\) for the number of four-term arithmetic progressions with positive step contained in \(A\):
\[
N_4(A)=\#\{(x,d)\in\mathbb Z\times\mathbb Z_{>0}:\{x,x+d,x+2d,x+3d\}\subseteq A\}.
\]
Then the third centered moment obeys the universal **sharp progression inequality**
\[
\boxed{\mathbb E[(X_A-\mathbb EX_A)^3]\ge 192\,N_4(A)\ge 0.}
\]
The coefficient \(192\) cannot be increased: equality in the first inequality holds when \(A\) itself is a four-term progression.

For any four-element \(A\subset\mathbb Z\), the centered probability law of \(X_A\) is symmetric about zero **if and only if** \(A\) is not an affine four-term arithmetic progression. More precisely,
\[
\mathbb EX_A=28,\qquad
\mathbb E[(X_A-28)^3]=\begin{cases}192,&A\text{ is a four-term progression},\\0,&\text{otherwise}.\end{cases}
\]
When \(A\) is a four-term progression, its centered law is that of
\[
4\cos U+4\cos V+8\cos(U+V),
\]
for independent uniform \(U,V\in[0,2\pi)\). Its variance is \(48\) and standardized skewness is \(1/\sqrt3\).

## Assumptions and scope
All coefficient phases are mutually independent and continuously Haar-uniform, not uniform signs or a finite phase alphabet. Haar measure on the signal circle is normalized. Arithmetic progressions have strictly positive integer steps, so each distinct increasing progression is counted once. The fourth norm is raised to its fourth power before the random central moment is taken. The theorem holds for arbitrary finite integer supports, with no contiguous-support assumption. The symmetry classification applies only to sets of exactly four distinct integers.

## Proof
**1. Positive Haar-character expansion.** Put \(n=|A|\). For any unordered pair \(\{a,b\}\subseteq A\) with repetitions allowed, write \(m(a,b)=1\) if \(a=b\) and \(m(a,b)=2\) otherwise. Expanding the Fourier fourth norm and grouping by equal pair sums gives
\[
X_A=\sum_s\left|\sum_{\substack{a\le b\in A\\a+b=s}}m(a,b)\xi_a\xi_b\right|^2.
\]
The terms with equal unordered pairs contribute \(\mathbb EX_A=2n^2-n\), because distinct phase characters average to zero. After removing this constant, every remaining term is a nontrivial character of the independent phase torus, with a **positive integer coefficient**.

In fact a nontrivial equal-sum pair collision uses either three or four distinct integers. Write \(T(A)\) for all increasing three-term progressions, and \(Q(A)\) for all strictly increasing quadruples \(a<b<c<d\) in \(A\) satisfying \(a+d=b+c\). For each progression \(x,x+d,x+2d\), define
\[
\chi_{x,d}=\xi_x\xi_{x+2d}\overline{\xi_{x+d}}^{\,2};
\]
for each such quadruple define
\[
\psi_{a,b,c,d}=\xi_a\xi_d\overline{\xi_b\xi_c}.
\]
All these exponent vectors are distinct up to the explicitly displayed conjugate pair. Counting the two ordered cross terms for a repeated-index pair and four for a disjoint pair gives
\[
\boxed{X_A-(2n^2-n)=2\sum_{(x,d)\in T(A)}(\chi_{x,d}+\overline\chi_{x,d})
+4\sum_{(a,b,c,d)\in Q(A)}(\psi_{a,b,c,d}+\overline\psi_{a,b,c,d}).}
\]
Each coefficient is nonnegative. On cubing and integrating in the phase torus, character orthogonality retains exactly the ordered triples whose exponent vectors sum to zero. Every retained product has a **nonnegative integer** coefficient. This proves that the third centered moment is nonnegative.

**2. A mandatory contribution from every four-term progression.** Fix \(x,x+d,x+2d,x+3d\in A\). It contains two three-term progressions, with phase characters
\[
\chi_1=\xi_x\xi_{x+2d}\overline{\xi_{x+d}}^2,\qquad
\chi_2=\xi_{x+d}\xi_{x+3d}\overline{\xi_{x+2d}}^2,
\]
and one four-distinct collision with character
\[
\psi=\xi_x\xi_{x+3d}\overline{\xi_{x+d}\xi_{x+2d}}.
\]
Their identity \(\chi_1\chi_2=\psi\) yields exactly twelve ordered constant-character triples: the six permutations of \((\chi_1,\chi_2,\overline\psi)\) and their six conjugates. Each has coefficient \(2\cdot2\cdot4=16\), hence contributes a total \(12\cdot16=192\). Different increasing four-term progressions have distinct four-point supports and therefore yield disjoint indexed triples. All other surviving contributions are nonnegative, proving the stated inequality.

**3. Full four-point classification.** Suppose \(A=\{a<b<c<d\}\), with consecutive gaps \(r=b-a\), \(s=c-b\), \(t=d-c\). At most one four-distinct pair-sum collision is possible; it occurs exactly when \(r=t\). When \(r=t\), a three-term progression among these four points is possible precisely when \(r=s=t\); this follows by checking the four possible three-point subsets. Thus if \(A\) is not a four-term progression, it has either a single four-distinct collision and no three-term progressions, or one or two three-term progressions and no four-distinct collision, or neither.

The phase exponent vectors of any two distinct three-term progressions are linearly independent (their supports differ and no two nonzero integer multiples of a vector with exponent pattern \((1,-2,1)\) have different supports). Consequently the associated characters are jointly independent Haar phases: any full-rank integer homomorphism from a coefficient torus onto a two-torus is surjective and preserves Haar measure. The centered law in the nonprogression case is therefore a sum of at most two independent centered cosine variables (or one such variable), which is symmetric.

For the progression \(A=\{x,x+d,x+2d,x+3d\}\), its two distinct three-term phase characters are independent Haar variables \(e^{iU},e^{iV}\), while the four-distinct character equals their product. The expansion in step 1 becomes exactly \(4\cos U+4\cos V+8\cos(U+V)\). The only nonzero cubic phase expectation comes from the two signed triangle relations, giving \(192\). The square expectation is \((4^2+4^2+8^2)/2=48\), hence the standardized skewness is \(192/48^{3/2}=1/\sqrt3\). Positive third centered moment excludes symmetric law. This proves both directions and the sharpness assertion.

## Verification
The standalone exact-arithmetic script `artifacts/verify_skewness.py` reconstructs the nonconstant phase-character expansion directly from equal frequency pair sums, without using the progression inequality. It computes second and third centered moments by exact integer character orthogonality. It verifies all four-point supports having minimum zero and maximum at most twenty, and all five- and six-point supports with minimum zero and maximum at most ten: 1,602 supports total. It confirms the sharp moment \(192\) on four-point progressions, zero third moment on all other four-point supports in the tested domain, and the general lower bound on all tested supports. These finite checks corroborate, but do not replace, the proof above for every finite \(A\).

## Relationship to prior work
The classical autocorrelation framework of de Dios Pont and Madrid (arXiv:2106.13873v1, 25 June 2021; first listed classification 42A05) motivates studying structure of Fourier autocorrelations. Katz and Ramirez (arXiv:2307.14281v1, 26 July 2023) calculate central moments and positive skewness for uniformly random **binary** sequences of contiguous support; their coefficient probability law and support domain differ. Published work on continuous Haar-phase fourth moments gives an exact mean and variance in terms of three-point and four-distinct pair-sum collisions, but the variance formula cannot determine distributional symmetry or the third central moment. The present result isolates a four-term progression contribution to the third moment over **arbitrary supports**, and gives an exact four-point symmetry classification for **continuous phases**. An earlier result under higher-order spectral or random-polynomial terminology remains possible; no priority claim is based solely on unsuccessful searches.

## Limitations
The lower bound is generally not an equality for supports with more than four elements. The absence of four-term progressions does not imply vanishing skewness for all larger supports: other character triangles can contribute. Positive third moment is sufficient to show a law is asymmetric, but zero third moment alone does not generally prove symmetry; the four-point symmetry direction uses a separate explicit distribution argument. None of the results apply without additional analysis to binary coefficients, dependent phases, or finite cyclic supports with wraparound collisions. The theorem does not give the complete third-moment motif expansion for arbitrary \(A\) or a central limit theorem.

## References
1. J. de Dios Pont and J. Madrid, *On Classical Inequalities for Autocorrelations and Autoconvolutions*, arXiv:2106.13873v1 (25 June 2021), https://arxiv.org/abs/2106.13873.
2. D. J. Katz and M. E. Ramirez, *Moments of Autocorrelation Demerit Factors of Binary Sequences*, arXiv:2307.14281v1 (26 July 2023), https://arxiv.org/abs/2307.14281.
3. *Random-phase fourth-moment variance detects the non-Sidon relations of a finite integer support*, public mathematical statement (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-random-phase-fourth-moment-variance-detects-the-non-sidon-relati--dcec63467712.
4. *Exact finite variance of the fourth moment of a random unimodular polynomial*, public mathematical statement (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-finite-variance-of-the-fourth-moment-of-a-random-unimodula--2ac4e1c327c6.
