# A sharp repeat–alternate transition for two-step relaxed Kaczmarz coupling

## Finding

Consider a consistent real two-equation, two-unknown linear system whose two normalized row normals have absolute inner product \(c\in(0,1)\). Run two successive relaxed Kaczmarz updates with the same fixed relaxation \(h\in(0,2)\). Select row indices \((I,J)\) with both one-step marginals uniform on the two rows, allowing dependence. Such joint laws have a unique parameter \(q=\Pr(I\ne J)\in[0,1]\); the two equal ordered pairs each have probability \((1-q)/2\), and the two distinct ordered pairs each have probability \(q/2\).

Define the worst-case expected two-step squared-error factor over all unit initial errors by
\[
R_{c,h}(q)=\sup_{\|e\|_2=1}\mathbb E\,\|T_JT_Ie\|_2^2,
\quad T_i=I_2-hu_i u_i^{\mathsf T}.
\]
Set
\[
r=(1-h)^4,\qquad K=\tfrac12h^2(1-c^2)(2-h),\qquad
q_0=\frac{h^2-2h+2}{h^2(1-c^2)}.
\]
Then **for every** \(c\in(0,1)\), \(h\in(0,2)\), \(q\in[0,1]\),
\[
R_{c,h}(q)=\max\{\Lambda_+(q),\Lambda_-(q)\},
\]
where
\[
\begin{aligned}
\Lambda_+(q)&=1+\frac{1+c}{2}(r-1)+qK\bigl(h(1+c)-2\bigr),\\
\Lambda_-(q)&=1+\frac{1-c}{2}(r-1)-qK\bigl(2-h(1-c)\bigr).
\end{aligned}
\]
Consequently the **complete set of minimizers** of \(R_{c,h}\) on \([0,1]\) is
\[
\operatorname*{argmin}_{0\le q\le1}R_{c,h}(q)=
\begin{cases}
\{q_0\},&h(1+c)>2\ \text{and}\ q_0<1,\\
[q_0,1],&h(1+c)=2\ \text{and}\ q_0<1,\\
\{1\},&\text{otherwise}.
\end{cases}
\]
In the first regime the optimal policy assigns strictly positive probability to *repeating* a row, although forbidding repetition is normally the intuitive choice. Such an interior optimum exists if and only if \(0<c<1/\sqrt2\) and \(h\in(0,2)\) satisfies both \(h>2/(1+c)\) and \(h>2/(1+\sqrt{1-2c^2})\).

For the exact witness \(c=1/2\), \(h=3/2\), the **unique** minimizer is \(q_0=20/27\); its factor is \(3/8\), compared with \(103/256\) for always using two different rows, \(257/512\) for independent uniform rows, and \(49/64\) for always repeating a row. Thus deliberate but partial repetition reduces the sharp worst-case expected squared error relative to always switching rows.

## Assumptions and scope

The system has exactly two real linearly independent nonzero rows; after normalizing and possibly changing one row sign, its unit row normals satisfy \(u_1^{\mathsf T}u_2=c\in(0,1)\). The equations are consistent, so subtracting the unique solution eliminates the right-hand side. Each update uses the same \(h\in(0,2)\), with no data noise, and the joint row-index law is chosen before the initial error and independent of it. Each of the two time marginals is exactly uniform. The guarantee is an expected **squared Euclidean norm after two updates**, maximized over the initial error direction; it is not a multi-sweep mean-square exponent, a pointwise guarantee for every random path, or an optimality claim over all randomized solvers, step-dependent relaxations, or feedback policies.

## Proof

**Step 1: exhaust all admissible couplings.** If \(P_{ij}=\Pr(I=i,J=j)\), uniform row marginals impose \(P_{11}=P_{22}\), \(P_{12}=P_{21}\), and \(P_{11}+P_{12}=1/2\). Hence there is precisely one free parameter \(q=P_{12}+P_{21}\), as stated above.

**Step 2: reduce the expectation to two symmetric matrices.** Since \(T_i\) is symmetric and \(T_i^2\) is well-defined, conditioning on equal and distinct index pairs gives
\[
H_q=\mathbb E\,(T_JT_I)^{\mathsf T}(T_JT_I)
=(1-q)S+qD,
\]
\[
S=\frac{T_1^4+T_2^4}{2},\qquad
D=\frac{T_1T_2^2T_1+T_2T_1^2T_2}{2}.
\]
The Rayleigh principle yields \(R_{c,h}(q)=\lambda_{\max}(H_q)\). There is no interchange of maxima and expectations: the supremum is taken **after** the expectation.

**Step 3: diagonalize by row symmetry.** Choose the orthonormal bisector basis in which
\[
u_1=\begin{pmatrix}\sqrt{(1+c)/2}\\ \sqrt{(1-c)/2}\end{pmatrix},\qquad
u_2=\begin{pmatrix}\sqrt{(1+c)/2}\\ -\sqrt{(1-c)/2}\end{pmatrix}.
\]
The reflection \(\operatorname{diag}(1,-1)\) swaps the rows. Both \(S\) and \(D\) commute with this reflection and are diagonal in this basis. Using \(T_i=I-hu_i u_i^{\mathsf T}\) and \(T_i^k=I+((1-h)^k-1)u_i u_i^{\mathsf T}\), direct multiplication gives
\[
S=\operatorname{diag}\left(1+\tfrac{1+c}{2}(r-1),\ 1+\tfrac{1-c}{2}(r-1)\right)
\]
and
\[
D-S=K\,\operatorname{diag}\bigl(h(1+c)-2,\ -[2-h(1-c)]\bigr).
\]
Thus the eigenvalues of \(H_q\) are exactly the two affine functions \(\Lambda_+(q)\) and \(\Lambda_-(q)\) stated in the finding. Their derivation involves only exact products of \(2\times2\) matrices, independently checked by symbolic expansion in the included verifier.

**Step 4: minimize the maximum of two lines without assuming uniqueness.** In the open parameter domain \(0<c<1\), \(0<h<2\), one has \(K>0\), \(r<1\), and \(2-h(1-c)>0\). Therefore \(\Lambda_-\) has **strictly negative** slope, whereas \(\Lambda_+\) has the sign of \(h(1+c)-2\). At \(q=0\),
\[
\Lambda_-(0)-\Lambda_+(0)=c(1-r)>0.
\]
The difference \(\Lambda_+-\Lambda_-\) is strictly increasing because its slope equals \(Kh(2c)>0\). Directly solving their equality gives
\[
q=q_0=\frac{c(1-r)}{2cKh}
=\frac{h^2-2h+2}{h^2(1-c^2)};
\]
the last equality uses \(1-(1-h)^4=h(2-h)(h^2-2h+2)\). For \(q<q_0\), the maximum is \(\Lambda_-\), and strictly decreases. For \(q>q_0\), it is \(\Lambda_+\), which strictly increases, is constant, or decreases according to whether \(h(1+c)\) is above, equal to, or below \(2\). If \(q_0\ge1\), the first branch remains active through \(q=1\), giving the unique minimizer \(1\). If \(q_0<1\), the three possible signs of the second slope give exactly the three cases in the displayed classification. In particular, an endpoint with coincident affine branches cannot create any further minimizers. The plateau case occurs exactly when \(h(1+c)=2\) and \(c<1/\sqrt3\), since substitution gives \(q_0=(1+c^2)/(2(1-c^2))\).

**Step 5: locate the existence of the repeat-beneficial regime.** The inequality \(q_0<1\) is equivalent to \(h^2c^2-2h+2<0\). Its discriminant is strictly positive precisely for \(c<1/\sqrt2\). For these \(c\), its lower root is \(2/(1+\sqrt{1-2c^2})\), and its upper root lies above \(2\). Combining this with the positive \(\Lambda_+\) slope proves the displayed necessary and sufficient conditions. At \(c=1/2,h=3/2\), exact substitution yields \(q_0=20/27\) and the four rational risks above, so both the phenomenon and strictness occur in the valid open domain.

## Verification

Run `python verify.py` from the same directory with SymPy 1.14.0 (declared in `requirements.txt`). The checker independently constructs the two rank-one row projectors, multiplies the four ordered two-step update matrices, verifies that their averaged quadratic forms equal both displayed diagonal eigenvalues, checks the crossover and an exact-rational witness, and searches a rational grid of \(19\) overlaps, \(39\) relaxations and \(51\) coupling choices against the analytic optimum. The recorded execution reported `PASS: 39517 symbolic identities and exact-rational comparisons`. All identities and reported rational witness values are checked exactly. The finite grid is **not** evidence for the universal quantifiers; the proof above establishes those.

## Relationship to prior work

Yaniv, Moorman, Swartworth, Tu, Landis and Needell (2021) establish non-repetitive selectable-set Kaczmarz for exact orthogonal row projections, where a just-selected equation is already solved and immediately repeating it does no work; that premise does not hold for the overrelaxed maps used here. Marshall and Mickelin (2022) develop scheduled learning rates for randomized Kaczmarz and analyze without-replacement sampling with noise. Necoara (2019) studies randomized block Kaczmarz with extrapolation and convergence bounds. Agaskar, Wang and Lu (2014) derive exact mean-square formulas and optimize **independent** row-sampling probabilities, which does not cover dependent two-stage couplings with fixed uniform marginals. Ferreira, Acebrón and Monteiro (2024) survey and experimentally compare row-selection schemes, finding sampling without replacement effective in their experiments; their results do not assert that no repetition is optimal at a fixed overrelaxation for the present two-step minimax criterion. A separate published finding on finite-horizon cyclic two-row Kaczmarz overrelaxation concerns deterministic order and finite-sweep transient norms, not the worst-case expected two-step squared-error factor optimized over arbitrary uniform-marginal coupling. Likewise, a separate result on mixing the two sweep orders for unrelaxed Kaczmarz fixes distinct rows on every sweep, and does not imply this repeat/alternate transition.

The novelty claim is restricted to the **exact minimax classification of all admissible two-step joint row laws** at fixed \((c,h)\), including the strict interior region and plateau. It is not a claim of first use of relaxation, random row choices, symmetric two-row coordinates, or exact moment matrices. Analytically deriving one statement from earlier matrix identities is possible, but the cited earlier statements do not themselves assert or imply the optimizing dependence law without solving this separate problem.

## Limitations

This is a finite-horizon, two-equation, two-dimensional, consistent-system result with an initial-error-independent coupling and a common fixed relaxation parameter. It does not analyze repeated pairs over arbitrarily many updates, correlated errors, inconsistent right-hand sides, higher dimensions, nonuniform row marginals, different relaxations across the two stages, transient norms of individual sample paths, or joint optimization of relaxation and coupling. The exact boundary conditions \(c=0\), \(c=1\), \(h=0\), and \(h=2\) are excluded from the theorem because some inequalities used for uniqueness become equalities there. Literature precedence cannot be ruled out for all obscure sources; the source inspections below describe the closest comparisons and residual risk. An independent scientific audit has not been performed.

## References

- Y. Yaniv, J. D. Moorman, W. Swartworth, T. Tu, D. Landis and D. Needell, *Selectable Set Randomized Kaczmarz* (first preprint 2021-10-10), https://arxiv.org/abs/2110.04703 .
- A. Marshall and M. Mickelin, *An optimal scheduled learning rate for a randomized Kaczmarz algorithm* (first preprint 2022-02-24), https://arxiv.org/abs/2202.12224 .
- I. Necoara, *Faster randomized block Kaczmarz algorithms* (2019), https://arxiv.org/abs/1902.09946 .
- A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities* (GlobalSIP 2014), https://doi.org/10.1109/GlobalSIP.2014.7032145 ; freely available full text https://scholar.harvard.edu/files/yuelu/files/randkac_globalsip14.pdf .
- I. A. Ferreira, J. A. Acebrón and J. Monteiro, *Survey of a class of iterative row-action methods: The Kaczmarz method* (published online 2024-09-26), https://doi.org/10.1007/s11075-024-01945-2 .
- *Exact finite-horizon cost of asymptotically optimal two-row Kaczmarz overrelaxation* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-finite-horizon-cost-of-asymptotically-optimal-two-row-kacz--d549f7251aa1 .
