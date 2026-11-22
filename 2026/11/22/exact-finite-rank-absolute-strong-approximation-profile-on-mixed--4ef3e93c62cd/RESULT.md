# Exact finite-rank absolute-strong approximation profile on mixed atomic and diffuse \(L^1\) spaces

## Finding

Let \((\Omega,\Sigma,\mu)\) be any probability measure space and let \(E=L^1(\mu;\mathbb R)\). For every \(f\in E^+\) and integer \(r\ge0\), define the *positive rank-budget absolute-strong error*
\[
\mathcal E_r(f)=\inf\bigl\{\|\,|I-T|f\,\|_1:\ T:E\to E\text{ positive},\ \|T\|\le1,\ \operatorname{rank}T\le r\bigr\}.
\]
The lattice modulus is the regular-operator modulus, not the ordinary pointwise absolute value of \((I-T)f\).

Let \(A_1,A_2,\ldots\) be the measure atoms (modulo null sets), and let \(D\) be their nonatomic complement. Reorder the masses \(a_j=\int_{A_j}f\,d\mu\) in nonincreasing order, padding by zeros if necessary. **For every** \(f\ge0\) and every integer \(r\ge0\),
\[
\boxed{\mathcal E_r(f)=\int_D f\,d\mu+\sum_{j>r}a_j.}
\]
An optimal operator is the coordinate/band projection retaining any \(r\) largest-mass atoms. No assumptions about distinct masses, finite atomic support, or separability are needed.

For example, if \(\mu=0.4\lambda_{[0,1]}+0.3\delta_2+0.2\delta_3+0.1\delta_4\) and \(f=1\), then the exact rank-budget errors for ranks \(r=0,1,2\) and \(r\ge3\) are respectively \(1,0.7,0.5,0.4\).

## Assumptions and scope

All spaces and operators are real. The measure is a probability measure, hence there are at most countably many distinct positive-measure atoms. Atoms may be abstract measurable sets; each function in \(L^1\) is constant almost everywhere on an atom. The nonatomic complement \(D\) may be empty. The infimum includes \(T=0\) at rank zero. The operator modulus exists because the range \(L^1(\mu)\) is Dedekind complete; for \(g\ge0\),
\[
|I-T|g=\sup_{|h|\le g}|(I-T)h|.
\]
It is important that the norm bound \(\|T\|\le1\) and positivity are part of the definition. We do not assert the same formula for unrestricted signs or noncontractive approximants.

## Proof

**Step 1: the nonatomic obstruction.** Write \(f_D=1_D f\) and let \(T\) be any admissible finite-rank operator. Represent it as \(Tg=\sum_{k=1}^{m}\varphi_k(g)v_k\), where each \(\varphi_k\) is a bounded linear functional on \(L^1(\mu)\). The finite-dimensional vector measure
\[
\nu(B)=(\varphi_1(f_D1_B),\ldots,\varphi_m(f_D1_B)),\qquad B\subseteq D,
\]
is countably additive and nonatomic: its components are integrals of bounded densities against the nonatomic finite measure \(f_D\,d\mu\). Lyapunov's convexity theorem gives a measurable \(B\subseteq D\) with \(\nu(B)=\nu(D)/2\). Set \(h=f_D(2\mathbf1_B-1_D)\). Then \(|h|=f_D\) and \(Th=0\). Consequently,
\[
|I-T|f_D\ \ge\ |(I-T)h|=f_D.
\]
This is an **order inequality**, stronger than a bound on norms. It holds even when \(T\) is not positive or contractive, provided it has finite rank and \(|I-T|\) exists.

**Step 2: the atomic diagonal budget.** For an atom \(A_i\), let \(e_i=\mathbf1_{A_i}/\mu(A_i)\), so \(\|e_i\|_1=1\). Define
\[
d_i=\int_{A_i}Te_i\,d\mu.
\]
Positivity and contractivity give \(0\le d_i\le1\). Let \(P_{\mathrm{at}}\) be the norm-one band projection onto all atoms and put \(C=P_{\mathrm{at}}T|_{E_{\mathrm{at}}}\). This is a positive contraction on the atomic \(\ell_1\) space with rank at most \(r\). Its diagonal is \((d_i)\). Since \(C\) is finite rank, its nuclear trace equals the absolutely convergent diagonal sum, and the finite-dimensional trace formula on its range yields
\[
0\le\sum_i d_i=\operatorname{tr}C\le\operatorname{rank}C\,\|C\|\le r.
\]
For every atom, the positive operator \(|I-T|\) satisfies
\[
\int_{A_i}|I-T|e_i\,d\mu\ge
\left|1-\int_{A_i}Te_i\,d\mu\right|=1-d_i.
\]
Because \(f\ge a_i e_i\), positivity yields the lower contribution \(a_i(1-d_i)\) on atom \(A_i\).

**Step 3: combine disjoint bands.** Positivity of \(|I-T|\) and Step 1 imply that its output on \(D\) dominates \(f_D\); Step 2 bounds the output on every atom. Since these output bands are disjoint and the \(L^1\) norm is additive on positive functions,
\[
\|\,|I-T|f\,\|_1\ge\|f_D\|_1+\sum_i a_i(1-d_i).
\]
As \(0\le d_i\le1\) and \(\sum_i d_i\le r\), the fractional-knapsack/rearrangement inequality gives \(\sum_i a_i d_i\le\sum_{j\le r}a_j\). Therefore
\[
\|\,|I-T|f\,\|_1\ge\|f_D\|_1+\sum_{j>r}a_j.
\]
For infinitely many atoms the inequalities pass by monotone convergence and absolute summability. At \(r=0\), take \(T=0\); the same formula remains valid.

**Step 4: attain the bound.** Let \(F\) be the set of indices of any \(r\) largest-mass atoms (or all atoms if fewer than \(r\) exist). Define the band projection \(P_Fg=\sum_{i\in F}\mathbf1_{A_i}g\). It is positive, contractive and has rank at most \(r\). Since \(I-P_F\) is itself positive, \(|I-P_F|=I-P_F\). Thus
\[
\|\,|I-P_F|f\,\|_1=\|f_D\|_1+\sum_{j>r}a_j,
\]
proving equality and attainment. \(\square\)

## Verification

The proof establishes the statement for all probability measures and all nonnegative \(L^1\) inputs, not only finite discretizations. `CHECK.py` runs exact-rational finite-dimensional tests of the diagonal-rank inequality and matching coordinate projections, with 3,200 checked inequalities or equalities. This checks only the atomic finite-matrix part; the nonatomic Lyapunov argument and the infinite-dimensional trace passage are established analytically above.

## Relationship to prior work

Garcia, Luiz, and Miranda introduce the sequentially positive approximation property, formulated using \(\||T-I|f\|\) for positive finite-rank contractions, and their later 2026 version states the qualitative characterization by separable atomic order-continuous Banach lattices. This theorem does **not** claim that characterization as new. It instead fixes a nonnegative test function and an exact finite-rank budget, and obtains its whole optimal error curve on any mixed atomic/nonatomic \(L^1\) space. Earlier absolute-strong-operator topology theory sets the framework without solving this optimization. The exact s-number profiles known for finite-fiber multiplication operators concern uniform operator approximation norms, not this positive-contraction pointwise lattice-modulus optimization.

## Limitations

Only the positive contractive rank-budget problem on real \(L^1\) is solved. The formula does not address general Banach lattices, ordinary operator-norm approximation, nonpositive approximants, or simultaneous minimization at multiple prescribed test functions. Latest-version publication priority remains subject to comparison with the full later text of the principal source and with possibly unindexed earlier results; the accessible later-version material confirmed the qualitative characterization but did not permit complete quantitative comparison.

## References

1. L. A. Garcia, J. L. P. Luiz, and V. C. C. Miranda, *Norm attainment for multilinear operators and polynomials on Banach spaces and Banach lattices*, arXiv:2605.12117, first public 12 May 2026, later version dated 11 September 2026, https://arxiv.org/abs/2605.12117 .
2. A. E. de Jeu and M. E. Wortel, *Convergence structures and locally solid topologies on vector lattices of operators*, 2021, https://link.springer.com/article/10.1007/s43037-021-00124-y .
3. B. Jefferies, *Lattice Trace Operators*, https://www.academia.edu/67419170/Lattice_Trace_Operators .
4. Classical Lyapunov convexity theorem for finite-dimensional ranges of nonatomic vector measures; and the nuclear trace identity for finite-rank operators on \(\ell_1\).
