# Sharp endpoint Fourier norms and a single negative shell for alternating rank-four balls

## Finding
Let \(q\ge2\) be a prime power and \(n\ge6\). The alternating-rank ball \(\mathcal B=\{X\in\operatorname{Alt}_n(\mathbb F_q):\operatorname{rank}(X)\le4\}\) has a Fourier transform with **exactly one negative rank orbit**, namely rank \(2\lfloor n/2\rfloor-2\). Every other Fourier coefficient is strictly positive; no coefficient vanishes. The sharp endpoint norm of the Fourier projection onto this ball has a closed rank-orbit formula.

For each dual alternating form \(B\) of rank \(2r\), put \(h=q^n\), \(z=q^{n-2r}\), \(S=1+q+q^2+q^3\) and \(D=q^4(q^2-1)^2(q^2+1)\). Then
\[
F_r:=\sum_{\operatorname{rank}X\le4}\psi(\langle B,X\rangle)
=\frac{h^2(z^2-Sz+qS)+hq^5((q^2+1)z-S)+q^{10}}{D}.
\]
The negative orbit has index \(r_*=\lfloor n/2\rfloor-1\). Its coefficient has magnitude
\[
-F_{r_*}=\begin{cases}
\dfrac{q(h-q^4)\big(h(q^4-q^3-1)+q^5\big)}{D},&n\text{ even},\\
\dfrac{q(h-q^5)\big(h(q^4-q-1)+q^4\big)}{D},&n\text{ odd}.
\end{cases}
\]
Writing
\[
T(n,r,q)={n\brack 2r}_q q^{r(r-1)}\prod_{j=1}^r(q^{2j-1}-1),
\]
for the number of alternating forms of rank \(2r\), the exact sharp norm is
\[
\boxed{\|P_{\mathcal B}\|_{\ell^1\to\ell^1}
=\|P_{\mathcal B}\|_{\ell^\infty\to\ell^\infty}
=1+\frac{2T(n,r_*,q)(-F_{r_*})}{q^{\binom n2}}.}
\]
In particular, the convolution operator with kernel \(\mathbf1_{\mathcal B}\) is invertible because every coefficient \(F_r\) is nonzero.

## Assumptions and scope
Identify the additive group \(G=\operatorname{Alt}_n(\mathbb F_q)\) with \(\Lambda^2V\) for \(V=\mathbb F_q^n\); in characteristic two, alternating always means skew-symmetric **with zero diagonal**. Its cardinality is \(|G|=q^{\binom n2}\). Fix any nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\), and pair an upper-triangular array \(X\) with a dual alternating array \(B\) by \(\langle B,X\rangle=\sum_{i<j}B_{ij}X_{ij}\). The dual rank is the ordinary matrix rank of \(B\) as an alternating form.

The Fourier projection acts on complex functions on the additive group and retains exactly frequencies in \(\mathcal B\). Norms use counting-measure \(\ell^1\) and \(\ell^\infty\) conventions; the convolution kernel is \(|G|^{-1}\widehat{\mathbf1_{\mathcal B}}\). The result covers **all** prime powers and dimensions in the stated range, not general nonsymmetric rank balls or rank thresholds above four.

## Proof
**1. Incidence decomposition.** For \(k\in\{2,4\}\), define \(H_k(X)\) as the number of \(k\)-dimensional subspaces \(U\le V\) with \(X\in\Lambda^2U\). An alternating bivector of rank \(2t\) has a canonical supporting subspace of dimension \(2t\), and therefore
\[
H_k(X)={n-2t\brack k-2t}_q
\]
when \(k\ge2t\), otherwise zero. Set \(a={n\brack2}_q\), \(b={n-2\brack2}_q\) and \(c={n\brack4}_q\). Evaluating at ranks zero, two, four and at all higher even ranks gives the pointwise identity
\[
\mathbf1_{\mathcal B}=H_4+(1-b)H_2+\big(1-c-(1-b)a\big)\mathbf1_{\{0\}}.
\]

**2. Character orthogonality and isotropic subspaces.** For a dual alternating form \(B\), write \(I_B(k)\) for the number of its totally isotropic \(k\)-subspaces. Orthogonality on each additive subspace \(\Lambda^2U\) gives
\[
\widehat H_k(B)=q^{\binom k2}I_B(k),
\quad
F_r=q^6 I_B(4)+(1-b)q I_B(2)+1-c-(1-b)a.
\]
If \(\operatorname{rank}B=2r\) and its radical has dimension \(d=n-2r\), then
\[
I_B(k)=\sum_{s=0}^{\min(k,d)}{d\brack s}_q q^{(d-s)(k-s)}J(r,k-s),
\]
where \(J(r,t)={r\brack t}_q\prod_{i=0}^{t-1}(q^{r-i}+1)\) for \(0\le t\le r\), and zero otherwise. Indeed, select the \(s\)-plane intersecting the radical, select an isotropic \((k-s)\)-plane in the nondegenerate symplectic quotient, and choose its lift by a linear map into the remaining \((d-s)\) radical coordinates. The formula for \(J\) follows by counting successive isotropic independent vectors \(q^{2r-i}-q^i\) and dividing by the number of ordered bases \(\prod_{i=0}^{t-1}(q^t-q^i)\).

Insert the Gaussian product formulas in the last two displays. After canceling common factors and collecting powers of \(z=q^d\), the polynomial numerator becomes
\[
D F_r=h^2\big(z^2-Sz+qS\big)+hq^5\big((q^2+1)z-S\big)+q^{10}.
\]
This reduction is an **exact polynomial identity**; the supplied checker independently evaluates the incidence sum and the polynomial at many prime powers and dimensions.

**3. One negative dual-rank shell.** Denote the last numerator by \(N(z)\). Direct substitution and factorization yield
\[
\begin{aligned}
N(1)&=q^4(h-q^2)(h-q^4),\\
N(q)&=q^2(h-q^3)(h-q^5),\\
N(q^2)&=q(q^4-h)\big[h(q^4-q^3-1)+q^5\big],\\
N(q^3)&=q(q^5-h)\big[h(q^4-q-1)+q^4\big].
\end{aligned}
\]
For even \(n\ge6\), the admissible radical sizes are \(1,q^2,q^4,\ldots\) in the variable \(z\); the first value is positive and the second negative. For odd \(n\ge7\), they are \(q,q^3,q^5,\ldots\); again the first is positive and the second negative. These signs are strict because \(h\ge q^6\) or \(h\ge q^7\), respectively, and \(q^4-q^3-1>0\), \(q^4-q-1>0\) for every \(q\ge2\).

To rule out every other negative orbit, put \(P(z)=z^2-Sz+qS\), \(L(z)=(q^2+1)z-S\). Both are positive and increasing for \(z\ge q^4\):
\[
P(q^4)=q^5(q^3-q^2-q-1)+q^3+q^2+q>0,
\]
\[
L(q^4)=q^6+q^4-q^3-q^2-q-1>0.
\]
The derivative \(P'(z)=2z-S\) is positive there. Thus \(N(z)=h^2P(z)+hq^5L(z)+q^{10}>0\) for all larger admissible \(z\). This exhausts every rank orbit, proves the exact negative shell and proves nonvanishing.

**4. Sharp norm and orbit mass.** A matrix of rank \(2r\) is determined by its \(2r\)-dimensional supporting subspace and a nondegenerate alternating form on it. Orbit-stabilizer with the symplectic group gives exactly \(T(n,r,q)={n\brack 2r}_q q^{r(r-1)}\prod_{j=1}^{r}(q^{2j-1}-1)\). Since \(0\in\mathcal B\), Fourier inversion gives
\[
\sum_{B\in G^*}F(B)=|G|.
\]
As exactly one rank orbit has a negative coefficient,
\[
|G|^{-1}\sum_{B\in G^*}|F(B)|=1+\frac{2T(n,r_*,q)(-F_{r_*})}{|G|}.
\]
The normalized coefficients are a convolution kernel. The \(\ell^1\) and \(\ell^\infty\) operator norms equal its absolute row sum, with equality attained by a point mass and by a phase-aligned input, respectively. This completes the exact sharp-norm proof.

## Verification
The accompanying `alternating_rank4_check.py` uses exact integer Gaussian coefficients, isotropic-subspace counts, and rank-orbit multiplicities. It checks the polynomial against the independent incidence formula, the unique negative orbit, and the zero-free property for 42 parameter pairs: field sizes \(2,3,4,5,7,8\), dimensions \(6,\ldots,12\). It also verifies Fourier inversion and Parseval numerically **without approximation** in integer arithmetic at the orbit level. Independently, it reconstructs the entire Boolean Walsh transforms at dimensions six and seven and checks every rank shell. Recorded output is `ALL_ALTERNATING_RANK_FOUR_CHECKS_PASS`. The checker uses Python 3 and NumPy for these exhaustive Boolean transforms. Finite computations support, but are not a substitute for, the universal symbolic proof above.

As a reproducibility example, for \(q=2,n=6\), the four dual Fourier values at ranks \(0,2,4,6\) are \(18880,448,-64,64\), with multiplicities \(1,651,18228,13888\); the sharp norm is \(72.203125\).

## Relationship to prior work
The alternating-bilinear-forms association scheme and its character tables originate in work of Delsarte and Goethals (1975). Existing skew-rank MacWilliams and generalized Krawtchouk formulas (Friedlander, Bouganis, Gadouleau; first preprint in 2022) determine the constituent rank-sphere Fourier eigenvalues in principle. The novelty assessed here is **not** the general character table or a mere rewriting of it; it is the universal strict sign classification of the rank-at-most-four ball, its only negative corank-two/corank-three orbit, the all-field zero-free boundary, and the resulting explicitly evaluated sharp endpoint norm. Abiad–Alfarano–Ravagnani (2024) treat ratio-type eigenvalue bounds for codes, and Schmidt–Weiß (2025) treat packing linear programs; neither inspected argument evaluates this ball's absolute Fourier sum or the unique negative shell. Gow and Quinlan's day-verifiably posted work (31 January 2007) on alternating-form rank-two subspaces motivates the geometry; older 1975 bibliographic data provide month precision only.

## Limitations
The result is specific to rank at most four and \(n\ge6\); it is not a general sign theorem for arbitrary higher rank balls. The 1975 primary paper's complete original text was not accessible for direct comparison, despite bibliographic and lawful-access attempts, so an earlier implicit or explicit derivation cannot be excluded. Full originality against all historical tables and independent mathematical review are not established. The Fourier values themselves are specializations of established rank-scheme eigenvalue machinery; only the independently proved global sign/absolute-norm structure is claimed as the potential new contribution.

## References
1. P. Delsarte and J. M. Goethals, *Alternating bilinear forms over GF(q)*, Journal of Combinatorial Theory Series A 19 (1975), 26–50. DOI: https://doi.org/10.1016/0097-3165(75)90090-4. Bibliographic public date available only as July 1975.
2. R. Gow and R. Quinlan, *On the vanishing of subspaces of alternating bilinear forms*, Linear and Multilinear Algebra 54 (2006), 415–428; online 31 January 2007. https://doi.org/10.1080/03081080500361264.
3. I. Friedlander, T. Bouganis and M. Gadouleau, *The MacWilliams Identity for the Skew Rank Metric*, arXiv:2210.16153 (first preprint 2022), https://arxiv.org/abs/2210.16153. See especially Section 4, generalized Krawtchouk polynomials.
4. A. Abiad, G. N. Alfarano and A. Ravagnani, *Eigenvalue bounds and alternating rank-metric codes*, arXiv:2405.09254 (2024), https://arxiv.org/abs/2405.09254, Sections 2–3.
5. K.-U. Schmidt and C. Weiß, *The linear programming optimum for packings in classical association schemes*, arXiv:2508.12806 (initial preprint 2025), https://arxiv.org/abs/2508.12806, Sections 2–4.
