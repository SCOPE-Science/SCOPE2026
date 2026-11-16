# A sharp curvature-controlled support gap for three-tap cyclic short-time Fourier transforms

## Finding
Let \(N\ge6\), and let \(g\) be a fixed complex window on \(\mathbb Z_N\) with precisely three consecutive nonzero taps \(g(0)=a\), \(g(1)=b\), \(g(2)=c\). Define its multiplicative discrete curvature and the sampled-frequency root group by
\[
R=\frac{ac}{b^2},\qquad \mu_N=\{z\in\mathbb C:z^N=1\}.
\]
For every nonzero signal \(f\), the cardinality of the support of its full cyclic short-time Fourier transform obeys the following exact **support gap**. A one-point-supported signal has \(3N\) nonzero transform entries; every signal supported on at least two points has at least \(4N-2\). More precisely, the sharp second support level is
\[
\min_{|\operatorname{supp} f|\ge2}|\operatorname{supp}V_g f|
=\begin{cases}4N-2,&R\in\mu_N,\\4N-1,&R\notin\mu_N.\end{cases}
\]
In the first case \(4N-1\) is **unattainable**, and in the second case \(4N-2\) is **unattainable**; these conclusions hold without prescribing the signal support. Every \(f\) with at least three nonzero entries has at least \(4N\) nonzero transform entries.

All minimizers above the one-site level have exactly two *cyclically adjacent* nonzero samples. After translating their support to \(\{u,u+1\}\) and setting \(r=f(u+1)/f(u)\), write
\[
C_1=-\frac{\overline a}{\overline b}\mu_N,\qquad C_2=-\frac{\overline b}{\overline c}\mu_N.
\]
The complete equality criterion is: when \(R\in\mu_N\), one has \(C_1=C_2\), and the minimizers are exactly \(r\in C_1\); otherwise the two cosets are disjoint, and minimizers are exactly \(r\in C_1\cup C_2\). All such ratios are realized and yield the claimed sharp values.

## Assumptions and scope
We use the full unnormalized transform
\[
V_gf(t,k)=\sum_{x\in\mathbb Z_N}f(x)\overline{g(x-t)}\exp(-2\pi i kx/N),\qquad (t,k)\in\mathbb Z_N^2.
\]
The result concerns support cardinality, so multiplying the transform by a fixed nonzero normalization has no effect. All three taps \(a,b,c\) are arbitrary nonzero complex numbers, with no equality-of-magnitude assumption; the signal \(f\) is otherwise arbitrary. A common cyclic translate of the window leads to the equivalent statement. The integer threshold \(N\ge6\) is essential to the classification by support size, not merely to a proof convenience.

## Proof
**(1) Translation rows and their zeros.** Write \(S=\operatorname{supp}f\), \(s=|S|\), and \(m=|S-\{0,1,2\}|\). For each translation \(t\) put \(r_t=|S\cap\{t,t+1,t+2\}|\). Then \(m\) is the number of nonzero translation rows and \(\sum_t r_t=3s\). Factoring out a monomial from each such row, its frequency polynomial has degree at most two. It has at most \(r_t-1\) sampled zeros when the support points in the row are consecutive or all three are occupied; when exactly its two endpoints are occupied, its polynomial has degree two and can have at most two sampled zeros. Let \(B\) be the number of windows containing just their two endpoints from \(S\). Each such window is indexed by a distinct occupied first endpoint, hence \(B\le s\). Consequently the total number \(Z\) of Fourier zeros in all active rows satisfies
\[
Z\le\sum_{t:r_t>0}(r_t-1)+B=3s-m+B,
\]
so
\[
|\operatorname{supp}V_gf|=Nm-Z\ge (N+1)m-3s-B.\tag{1}
\]
The cyclic interval expansion inequality gives \(m\ge\min(N,s+2)\): for a proper nonempty support, each occupied cyclic component is enlarged by two sites unless the entire circle becomes occupied, in which case the union size is \(N\). The same inequality follows by counting the at least two occupied-to-empty transitions at the boundary of a proper support interval.

**(2) Signals with at least three points.** Suppose \(N\ge7\). If \(3\le s\le N-2\), inequality (1) and \(B\le s\) imply
\[
|\operatorname{supp}V_gf|\ge(N-3)s+2(N+1)\ge 5N-7\ge4N.
\]
If \(s=N-1\), then \(m=N\) and (1) gives at least \(N^2-3N+4\ge4N\). If \(s=N\), (1) gives at least \(N(N-3)\ge4N\). For \(N=6\), consider \(s=3,4,5,6\). When \(s=3\) and \(m=5\), the support is a consecutive triple, and its five active rows have intersection sizes \(1,2,3,2,1\), contributing at most four zeros and at least \(5N-4=26\) nonzeros. For \(s=3,m=6\), (1) gives at least \(30\). For \(s=4\), one has \(m=6\) and (1) gives at least \(26\). For \(s=5\), one has \(m=6\) and exactly one endpoint-only window \(B=1\), giving at least \(26\). For \(s=6\), each of six rows is a full three-term polynomial with at most two zeros, so at least \(6(6-2)=24\) transform entries are nonzero. This proves the \(4N\) bound in every case.

**(3) Two-site signals and the exact phase criterion.** For \(s=2\), the support \(S=\{u,v\}\) is either cyclically adjacent, cyclically separated by exactly two, or farther apart. In the second case there are five nonzero translation rows and at most two zeros, hence at least \(5N-2\) nonzero entries. In the last case there are six singleton translation rows and exactly \(6N\) nonzero entries. In particular, neither case can attain a support cardinality below \(4N\) for \(N\ge6\).

If instead \(v=u+1\), exactly four rows are nonzero, two of them singletons and two with two adjacent support points. The row containing the first two taps vanishes at one sampled frequency exactly when \(r\in C_1\), and the row containing the last two taps vanishes at one sampled frequency exactly when \(r\in C_2\). Each can vanish at most once. Therefore
\[
|\operatorname{supp}V_gf|=4N-\mathbf1_{r\in C_1}-\mathbf1_{r\in C_2}.\tag{2}
\]
Since the cosets \(C_1,C_2\) are either equal or disjoint, and
\[
C_1=C_2\quad\Longleftrightarrow\quad \overline{ac/b^2}\in\mu_N\quad\Longleftrightarrow\quad R\in\mu_N,
\]
formula (2) establishes both sharp possibilities, all equality cases, and the forbidden intermediate support level. A singleton signal intersects exactly three translates of \(g\); each resulting one-term Fourier row is nowhere zero, so its transform support is exactly \(3N\). This completes the proof.

**(4) Sharp dimension cutoff.** On \(\mathbb Z_5\), take the constant signal \(f\equiv1\) and \(g(0)=g(2)=1\), \(g(1)=-2\cos(2\pi/5)\). Each translation row is a phase multiple of the polynomial \(1-2\cos(2\pi/5)z+z^2\), which vanishes at the two sampled fifth roots \(z=e^{\pm2\pi i/5}\). Hence exactly three of five frequency coefficients survive in each of five rows, giving \(15=3N\) surviving coefficients although \(f\) has five nonzero samples. Thus the one-site rigidity conclusion fails for \(N=5\).

## Verification
The accompanying standalone `verify_three_tap.py` uses exact arithmetic in the cyclotomic number fields \(\mathbb Q(\zeta_N)\), reducing powers modulo cyclotomic polynomials rather than relying on floating-point tests. It independently constructs the transform for 5,088 nontrivial coefficient scenarios with \(6\le N\le13\), and exhaustively checks the combinatorial lower bound for all 15,892 support sets of size at least three in the same range. The checker prints `EXACT_CYCLOTOMIC_SUPPORT_CHECK_PASS 5088`, `EXHAUSTIVE_SUPPORT_BOUND_CHECK_PASS 15892`, and `THREE_TAP_STFT_VERIFIED`. These finite checks are consistency tests; the proof of the all-dimensional statement is the row-counting argument above. Required packages are Python 3 and SymPy; run `python verify_three_tap.py` from the containing directory.

## Relationship to prior work
Nicola (2022) characterizes equality in the universal lower bound \(|\operatorname{supp}V_g f|\ge N\); that classification does not give the second support level for a fixed three-tap window. Krahmer, Pfander and Rashkov (2006) prove a support-size lower bound that, for prime order with a two-site signal and a three-site window, already implies \(|\operatorname{supp}V_g f|\ge4N-2\). That earlier inequality is explicitly acknowledged and is not claimed as new. The present claim differs by determining the *complete sharp equality and forbidden-gap dichotomy* from the invariant \(R\), allowing arbitrary signal supports and composite orders \(N\ge6\).

Two-point-window support geometry and two-sparse-pair support classifications concern different window support sizes. A published phase-only three-by-three cross-ambiguity classification requires *both* signal and window to have three equally weighted entries; it does not determine the current two-by-three case or all-signal support cutoff. These nearby results were compared at the level of their complete statements, rather than by keyword only.

## Limitations
The result addresses exact zero/nonzero support counts, not numerical near-zero stability, approximate sparsity, noisy recovery, or general windows supported on nonconsecutive triples. It does not establish a quantitative stability theorem for signals whose transform is nearly support-extremal. The originality comparison cannot exclude earlier unindexed descriptions of equivalent three-tap identities. No independent mathematical audit has been performed.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176v1, first publicly posted 2022-04-29. https://arxiv.org/abs/2204.14176
2. F. Krahmer, G. E. Pfander and P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1, 2006-11-16. https://arxiv.org/abs/math/0611493
3. C. Fernández, A. Galbis and J. Martínez, *Localization Operators and an Uncertainty Principle for the Discrete Short Time Fourier Transform*, Abstract and Applied Analysis (2014), Article 131459, doi:10.1155/2014/131459.
4. *Exact support geometry for a two-point cyclic short-time Fourier window*, publicly accessible mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-support-geometry-for-a-two-point-cyclic-short-time-fourier--f7682ff5d741
5. *Exact support trichotomy for two-sparse prime cyclic STFTs*, publicly accessible mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-support-trichotomy-for-two-sparse-prime-cyclic-stfts--5b84852d543c
6. *Exact optimizer topology for phase-only three-tap cross-ambiguity on prime cycles*, publicly accessible mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-optimizer-topology-for-phase-only-three-tap-cross-ambiguit--114875b726db
