# Sharp bounded-variation sensitivity of the two-choice centered box envelope

## Finding
For every integer \(r\ge1\), let \(Q_r\) be the uniform centered \((2r+1)\)-point averaging operator on bi-infinite real sequences and let \(T_r f\) be the pointwise maximum of \(f\) and \(Q_r f\). On bounded sequences of finite adjacent total variation, its **exact two-input bounded-variation Lipschitz coefficient** is
\[
\boxed{\sup_{V(f-g)>0}\frac{V(T_r f-T_r g)}{V(f-g)}
=1+\frac{4\lfloor r^2/4\rfloor}{2r+1}.}\tag{1}
\]
For every \(r\), this supremum is attained by a pair of bounded nonnegative finite-variation sequences whose difference is a single step. In particular, \(T_1\) is nonexpansive, \(T_2\) has sharp gain \(9/5\), and the sharp gain grows as \(r/2+O(1)\) as \(r\to\infty\). Thus radius two is the first expansive two-choice centered window, and the family is not uniformly Lipschitz in bounded variation as its radius increases. The claim concerns *differences of outputs for two inputs*, not the variation of an output relative to its own input.

## Assumptions and scope
Let \(\mathrm{BV}(\mathbb Z)\) be the space of all bounded real sequences \(f=(f_i)_{i\in\mathbb Z}\) with
\[
V(f)=\sum_{i\in\mathbb Z}|f_{i+1}-f_i|<\infty.
\]
Constants have zero seminorm; the operators in the theorem commute with adding a constant. Define
\[
(Q_rf)_i=\frac1{2r+1}\sum_{s=-r}^{r}f_{i+s},\qquad
(T_rf)_i=\max\{f_i,(Q_rf)_i\}.
\]
The denominator in (1) is restricted to strictly positive values. Boundedness follows automatically from finite total variation, but is stated explicitly. These operators preserve bounded variation: \(Q_r\) is a finite average of translations, and the scalar positive part is variation-nonincreasing on differences of scalar values. For nonnegative signals, \(T_r\) is the centered maximal average with the **two allowed radii \(\{0,r\}\)**. The theorem does not identify it with the full Hardy–Littlewood maximal operator over every intermediate radius.

## Proof
**1. Frozen branch representation for every input pair.** Write \(B_r=Q_r-I\). The identity
\[
T_rf=f+(B_rf)_+
\]
and monotonicity plus unit Lipschitz continuity of the positive-part function give, for each pair \(f,g\), coefficients \(\theta_i\in[0,1]\) with
\[
T_rf-T_rg=(I+\operatorname{diag}(\theta)B_r)(f-g)=:A_\theta(f-g).
\tag{2}
\]
For any real \(u,v\), the quotient \((u_+-v_+)/(u-v)\) belongs to \([0,1]\) if \(u\ne v\); otherwise choose an arbitrary element of \([0,1]\). This proves (2), including at ties. Every \(A_\theta\) fixes constant sequences.

**2. Reduction to one jump.** Put \(H_j(i)=\mathbf1_{\{i\ge j+1\}}\). Every \(h\in\mathrm{BV}(\mathbb Z)\) has an absolutely and uniformly convergent expansion
\[
h_i=c+\sum_{j\in\mathbb Z}d_jH_j(i),\qquad
 d_j=h_{j+1}-h_j,\quad \sum_j|d_j|=V(h),
\]
where \(c\) is the left limit of \(h\). Because \(A_\theta\) fixes constants and is bounded on the sequence sup norm, linearity and the variation triangle inequality imply
\[
V(A_\theta h)\le\sum_j|d_j|V(A_\theta H_j)
\le \left(\sup_j V(A_\theta H_j)\right)V(h).
\tag{3}
\]
The infinite summation is justified by absolute summability of the coefficient sequence and finite support of \(B_rH_j\). Thus it suffices to bound every single-jump column, uniformly over \(\theta\).

**3. Exact jump-column combinatorics.** Translation symmetry permits \(j=0\). The nonzero values of \(B_rH_0\) consist of the left positive ramp \(k/(2r+1)\) at indices \(-r+k\), and the right negative ramp \(-k/(2r+1)\) at indices \(r+1-k\), for \(1\le k\le r\). Write the corresponding branch values on the two wings as \(a_1,\ldots,a_r\) and \(b_1,\ldots,b_r\), respectively, with all coefficients in \([0,1]\), and put \(a_0=b_0=0\). The central step is positive because its height is
\[
1-\frac{r(a_r+b_r)}{2r+1}\ge\frac1{2r+1}.
\]
Consequently an exact edge-by-edge calculation gives
\[
V(A_\theta H_0)
=1+\frac{E_r(a)+E_r(b)}{2r+1},\quad
E_r(a)=\sum_{k=1}^{r}|ka_k-(k-1)a_{k-1}|-ra_r.
\tag{4}
\]
The same formula applies to \(b\).

**4. Optimization and the sharp upper bound.** The expression \(E_r(a)\) is separately convex in each component of \(a\in[0,1]^r\); successively maximizing over the endpoints of each interval shows its maximum occurs at a binary vector. For \(a_k\in\{0,1\}\), the identity
\[
E_r(a)=2\sum_{k=1}^{r-1}k\,a_k(1-a_{k+1})
\tag{5}
\]
shows that only transitions from one to zero contribute. Their indices cannot be adjacent. For positive increasing weights \(1,2,\ldots,r-1\), the maximum sum over nonadjacent indices is
\[
(r-1)+(r-3)+\cdots=\left\lfloor\frac{r^2}{4}\right\rfloor.
\]
For completeness, define \(F(m)\) as the maximum nonadjacent-index sum on \(\{1,\ldots,m\}\). The recurrence \(F(m)=\max\{F(m-1),m+F(m-2)\}\), with \(F(0)=0\) and \(F(1)=1\), proves by induction \(F(m)=\lfloor(m+1)^2/4\rfloor\). Hence
\[
\max_{a\in[0,1]^r}E_r(a)=2\left\lfloor\frac{r^2}{4}\right\rfloor.
\tag{6}
\]
Combining (3), (4) and (6) proves the upper bound in (1) for every pair, without a finiteness or genericity hypothesis on the inputs.

**5. Every optimal branch pattern is actually attainable.** For the lower bound, choose binary values on each ramp that equal one at indices \(k=r-1,r-3,\ldots\) and zero at the intervening indices (including \(k=r\)). On both wings this attains equality in (6). Denote the corresponding prescribed activation mask by \(\alpha_i\) on the finite set \(J=\{-r+1,\ldots,r\}\), the support of \(B_rH_0\).

Consider real, finitely supported sequences vanishing off \(J\). The finite principal matrix \(B_r|_{J\times J}\) is invertible, since for every nonzero finitely supported real \(u\)
\[
\langle u,(I-Q_r)u\rangle
=\frac{1}{2(2r+1)}\sum_{i\in\mathbb Z}\sum_{s=-r}^{r}(u_{i+s}-u_i)^2>0.
\tag{7}
\]
Strict positivity follows already from the \(s=1\) terms. Solve the finite linear system
\[
(B_ru)_i=\begin{cases}1,&\alpha_i=1,\\-1,&\alpha_i=0,\end{cases}\qquad i\in J,
\]
with \(u\) zero off \(J\). Choose a constant \(C>\|u\|_\infty\), and set \(f=C+u\), \(g=f+H_0\). Both are bounded, nonnegative and of finite variation; \(V(g-f)=1\). On \(J\), \(|(B_rH_0)_i|\le r/(2r+1)<1/2\), so the strict sign of \(B_rf\) is unchanged when the unit step is added. Off \(J\), \(B_rH_0=0\). Therefore the positive-part difference is exactly the prescribed frozen branch, and
\[
T_rg-T_rf=A_\alpha H_0,
\qquad
V(T_rg-T_rf)=1+\frac{4\lfloor r^2/4\rfloor}{2r+1}.
\]
This realizes the coefficient exactly, rather than as a limit, and proves (1).

**6. Threshold and growth.** The factor in (1) equals one at \(r=1\), exceeds one for every \(r\ge2\), and is \(r/2+O(1)\) as \(r\to\infty\), directly from the floor formula. These statements and the equality witnesses complete the claimed classification.

## Verification
The self-contained `VERIFY.py` uses exact rational arithmetic. It exhaustively checks all binary wing masks for radii one through seven; constructs exact nonnegative lower-bound witnesses by rational Gaussian elimination for radii one through eight; and tests 150 independently generated rational input pairs for each radius one through seven. Run `python VERIFY.py` in the extracted directory. The checker reports `ALL_TWO_CHOICE_BV_CHECKS_PASS`. These finite tests verify the formulas and constructive method at sample radii; the all-radius theorem is established by the recurrence and positive-definite finite-system argument above.

## Relationship to prior work
Bober, Carneiro, Hughes and Pierce (first public 2010-05-17) prove single-input variation contraction for the **uncentered full-radius** discrete maximal operator and an \(\ell^1\)-to-variation bound for the **centered full-radius** operator; the materially inspected primary paper does not prove a sharp **two-input BV Lipschitz constant for the two-radius pointwise envelope**. Carneiro and Hughes (first public 2013-09-06) prove endpoint \(\ell^1\)-to-gradient boundedness and continuity for full discrete maximal operators; their continuity theorem does not imply a global BV-seminorm Lipschitz bound. Madrid (first public 2015-12-13) proves sharp \(\ell^1\)-to-variation bounds, again distinct from the present two-input seminorm. These one-input or different-domain estimates neither imply nor contradict (1).

The closest accessible published two-choice maximum result gives an exact \(\ell^2\) norm for an **adjacent one-sided two-point kernel and rectangular products**; it does not give total-variation sensitivity for symmetric windows. A second published comparison determines weighted two-input path-variation constants for **running coordinatewise minima and maxima**, whose Jacobians are coordinate selectors, unlike the averaged active rows here. A third analyzes weighted **uncentered interval maximal** maps in the input Lipschitz seminorm, not the two-choice centered map in adjacent \(\ell^1\) variation. The explicit distinctions were checked against their complete public results. Available database search and primary-material comparison have not located a statement that implies (1); they do not prove historical uniqueness. Unindexed equivalent results remain a residual priority risk.

## Limitations
The theorem concerns bi-infinite one-dimensional, uniformly weighted, symmetric box averages with **only two selectable radii**, zero and \(r\). It is not a sharp bound for the full centered maximal operator with all radii \(0,1,\ldots,r\), nor for finite-endpoint conventions, variable radii, nonuniform kernels, higher-dimensional lattices, or individual-output variation. It establishes exact two-input sharpness and permits nonnegative attaining inputs, but does not classify every pair attaining equality. The analysis is over real sequences; complex-valued maxima are not defined here.

## References
1. J. Bober, E. Carneiro, K. Hughes and L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030v1, first posted 2010-05-17. https://arxiv.org/abs/1005.3030
2. E. Carneiro and K. Hughes, *On the endpoint regularity of discrete maximal operators*, arXiv:1309.1535v1, first posted 2013-09-06. https://arxiv.org/abs/1309.1535
3. J. Madrid, *Sharp inequalities for the variation of the discrete maximal function*, arXiv:1512.04112v1, first posted 2015-12-13. https://arxiv.org/abs/1512.04112
4. *Sharp two-choice rectangular maximal bounds and geometric rigidity*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-choice-rectangular-maximal-bounds-and-geometric-rigidi--2ae83343e2e7
5. *Finite-window morphology: sharp two-input variation and a boundary-weight transition*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-finite-window-morphology-sharp-two-input-variation-and-a-boundar--5f5f2cb7d7b2
6. *Endpoint-mass concentration and sharp Lipschitz amplification of discrete interval maximal averages*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-endpoint-mass-concentration-and-sharp-lipschitz-amplification-of--e07aeee621fe
