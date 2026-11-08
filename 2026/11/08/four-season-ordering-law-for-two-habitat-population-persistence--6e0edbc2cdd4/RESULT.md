# Four-season ordering law for two-habitat population persistence

## Finding

**Theorem (complete ordering rule for four seasonal phases).** Consider one population dispersed between two habitats. In seasonal phase \(j\), of duration \(t_j>0\), its abundance vector \(x=(x_1,x_2)^\top\) obeys
\[
\dot x=G_jx,\qquad
G_j=\begin{pmatrix}r_{1j}-\mu_j&\mu_j\\\mu_j&r_{2j}-\mu_j\end{pmatrix},
\qquad\mu_j>0.
\]
The phases repeat periodically, and only their ordering may change. Define each phase's **contrast-to-dispersal ratio**
\[
q_j=\frac{r_{1j}-r_{2j}}{\mu_j}.
\]
Let \(\Lambda(\pi)\) be the exponential growth exponent for time ordering \(\pi\), defined precisely below.

For one, two or three phases, \(\Lambda(\pi)\) is independent of the phase permutation. For four phases, relabel the phases so that \(q_1\le q_2\le q_3\le q_4\). Then the following **complete ranking of all 24 orders** holds:
\[
\boxed{\Lambda(1,2,4,3)\ge\Lambda(1,2,3,4)
\ge\Lambda(1,3,2,4).}
\]
Every order is a cyclic rotation or reversal of exactly one of the three displayed words (as words of distinct phase labels). The inequalities are strict whenever all four ratios are distinct. Thus the maximum and minimum schedules are unique up to cyclic rotation and reversal when the ratios are distinct; their relative ranking is independent of the durations and of the mean local growth rates.

The distinction can change growth into decay while keeping **both habitats sinks in isolation**. Take four unit-duration phases, \(\mu_j=1\) and
\[
(d_1,d_2,d_3,d_4)=(-3,-1,1,3),\quad
r_{1j}=-\frac14+\frac{d_j}{2},\quad
r_{2j}=-\frac14-\frac{d_j}{2}.
\]
Each isolated habitat has time-averaged intrinsic growth \(-1/4\), for every permutation. Nonetheless the best ordering \((1,2,4,3)\) gives \(\Lambda>0\), whereas \((1,3,2,4)\) gives \(\Lambda<0\). This is an exact ordering-induced dispersal-growth transition, not a numerical conjecture.

## Assumptions and scope

All \(r_{ij}\) are real, every \(t_j\) and every symmetric exchange rate \(\mu_j\) is strictly positive, and all four phases repeat with fixed durations; ordering changes neither their rates nor durations. A single population moves between two habitats, with symmetric movement in each phase (the rate may vary *between* phases). Define \(E_j=e^{t_jG_j}\), \(T=\sum_jt_j\), and
\[
M_{\pi}=E_{\pi_s}\cdots E_{\pi_1},\qquad
\Lambda(\pi)=\frac{1}{T}\log\rho(M_{\pi}).
\]
Here \(\rho\) is spectral radius and \(s\in\{1,2,3,4\}\). All \(E_j\) and all products are strictly entrywise positive because \(\mu_j,t_j>0\). The exponent is therefore the common asymptotic exponential growth rate of both abundances for every nonzero nonnegative initial abundance. "Growth" means \(\Lambda>0\) in this linear model; "decay" means \(\Lambda<0\). No nonlinear carrying-capacity conclusion is asserted.

## Proof

**Phase exponential.** Write \(d_j=r_{1j}-r_{2j}\), \(\bar r_j=(r_{1j}+r_{2j})/2\), and
\[
H_j=\begin{pmatrix}d_j/2&\mu_j\\\mu_j&-d_j/2\end{pmatrix},
\qquad h_j=\sqrt{\mu_j^2+d_j^2/4}>0.
\]
Since \(H_j^2=h_j^2 I\),
\[
E_j=a_jI+b_jH_j,
\quad a_j=e^{t_j(\bar r_j-\mu_j)}\cosh(t_jh_j),
\quad b_j=e^{t_j(\bar r_j-\mu_j)}\frac{\sinh(t_jh_j)}{h_j}>0.
\]
In particular every \(E_j\) is symmetric and strictly positive. All permutations have the same positive determinant
\[
D=\prod_j\det E_j
=\exp\left(\sum_jt_j(r_{1j}+r_{2j}-2\mu_j)\right).
\]
For a positive \(2\times2\) matrix with positive determinant, the two eigenvalues are positive and distinct; its Perron eigenvalue is
\[
\rho=\frac{s+\sqrt{s^2-4D}}2,\qquad s=\operatorname{tr}M.
\]
At a fixed \(D>0\), this is strictly increasing in \(s\). It therefore suffices to compare traces.

**At most three phases.** Because the \(E_j\) are symmetric, the trace of their product is invariant under reversing the word (matrix transposition), as well as under cyclic rotation. For three distinct labels the rotation-and-reversal operations cover all six permutations, and similarly for one or two labels. All permutations consequently have identical trace and determinant, hence identical \(\Lambda\). The trace symmetry itself is elementary; it is not presented as a new matrix identity.

**Exact four-phase interchange.** Let
\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
Direct multiplication of the displayed symmetric matrices gives
\[
[E_b,E_c]=b_b b_c(d_b\mu_c-\mu_b d_c)J,
\qquad\operatorname{tr}(E_aJE_d)=b_a b_d(d_a\mu_d-\mu_a d_d).
\]
Thus, for four distinct phase indices \(a,b,c,d\),
\[
\operatorname{tr}(E_aE_bE_cE_d)-\operatorname{tr}(E_aE_cE_bE_d)
=K(q_b-q_c)(q_a-q_d),
\qquad K=\prod_{j=1}^4(b_j\mu_j)>0.
\tag{1}
\]
The trace of the forward product equals the trace of the time-ordered reverse product, so the convention for temporal composition does not change this comparison.

Every permutation of four distinct labels lies in one of three rotation/reversal classes, represented by \(1243\), \(1234\), \(1324\). Applying (1) directly and after a cyclic rotation gives
\[
\operatorname{tr}M_{1243}-\operatorname{tr}M_{1234}
=K(q_4-q_3)(q_2-q_1)\ge0,
\]
\[
\operatorname{tr}M_{1234}-\operatorname{tr}M_{1324}
=K(q_3-q_2)(q_4-q_1)\ge0.
\]
Both are positive for four distinct ratios. Equality of determinants now transfers these inequalities, strictly when applicable, to the Floquet exponents. This establishes the complete ranking, not merely a comparison between selected orders.

**Exact growth/decay witness.** In the example, each phase matrix is
\[
G_j=\begin{pmatrix}-5/4+d_j/2&1\\1&-5/4-d_j/2\end{pmatrix}
\]
and has matrix infinity norm at most \(15/4\). Every product determinant is exactly \(D=e^{-10}<1/10\). Let \(S_{30}(G)=\sum_{k=0}^{30}G^k/k!\). The series tail has the rigorous norm bound
\[
\|e^G-S_{30}(G)\|_\infty\le\epsilon
=\frac{(15/4)^{31}}{31!\,[1-(15/4)/32]}.
\]
As \(e^{15/4}<e^4<55\), telescope the four product factors to obtain a trace error strictly below \(8\cdot56^3\epsilon<10^{-7}\). Exact rational evaluation of the four factors \(S_{30}(G_j)\) (reproduced in `verify.py`) proves
\[
\operatorname{tr}M_{1243}>11/10,
\qquad\operatorname{tr}M_{1324}<9/10.
\]
Since \(0<D<1/10\), the first inequality implies \(\rho(M_{1243})>1\), and the second \(\rho(M_{1324})<1\) (equivalently, \(\rho>1\) iff \(\operatorname{tr}M>1+D\) when \(0<D<1\)). The isolated growth averages are each \(-1/4\). Hence the same four environments produce dispersal-induced growth or exponential decay solely according to their order.

## Verification

Run `python3 verify.py` from the extracted package, using the standard library only. The program reconstructs all 24 finite four-phase products through rational matrix-exponential polynomials, checks the three eight-element rotation/reversal classes, checks the trace interchange factorization and three-phase trace invariance, and supplies rational error bounds proving the strict threshold signs without relying on floating-point classification. Its approximate printed traces are descriptive; the actual assertions operate on rational numbers. The general theorem is proved by the matrix identities above, not inferred from a finite experiment.

## Relationship to prior work

Benaïm, Lobry, Sari and Strickler's 2023 preprint (arXiv:2311.04706, first version November 8, 2023; 2024 journal publication) supplies the periodic cooperative two-patch population model and the Floquet/Perron growth criterion, with piecewise-constant seasons in Section 4.2 and further two- and three-patch examples. It does not give this all-permutation four-phase ratio ordering or the ordering-only growth/decay witness. The familiar cyclic and reversal invariance of traces is used and acknowledged, not claimed as a separate discovery. Matrix rearrangement studies such as Alaifari–Cheng–Pierce–Steinerberger (arXiv:1904.05239) compare words built from two symmetric matrices in operator norm, while Vladimirov (arXiv:2406.17524) studies binary-word joint spectral radii; neither result directly implies the ranking of four *distinct* symmetric migration-phase exponentials by their ecological contrast ratios.

## Limitations

The optimal-order classification concerns at most four phases, two habitats, and symmetric positive exchange rates within each phase. It is not a result for asymmetric exchange, three or more habitats, five or more distinct phases, arbitrary nonlinear density dependence, or a controlled total duration budget. The preservation of local growth averages assumes only a permutation of already fixed phases. The classification uses exact real arithmetic; the witness's strict inequalities are certified using rational Taylor truncations with an analytic remainder bound. An equivalent four-factor matrix ordering identity or ecological specialization in unindexed literature remains a publication-priority risk; independent external review is not yet performed.

## References

1. M. Benaïm, C. Lobry, T. Sari, E. Strickler, *When can a population spreading across sink habitats persist?*, arXiv:2311.04706v2 (2023), https://arxiv.org/html/2311.04706v2 .
2. R. Alaifari, X. Cheng, L. B. Pierce, S. Steinerberger, *On Matrix Rearrangement Inequalities*, arXiv:1904.05239v2 (2020), https://arxiv.org/html/1904.05239v2 .
3. A. Vladimirov, *Joint spectral radius and forbidden products*, arXiv:2406.17524v1 (2024), https://arxiv.org/html/2406.17524v1 .
4. J. D. Cook, *Cyclic permutations and trace* (2021), https://www.johndcook.com/blog/2021/05/10/cyclic-permutations-and-trace/ (background for the elementary symmetry used).
