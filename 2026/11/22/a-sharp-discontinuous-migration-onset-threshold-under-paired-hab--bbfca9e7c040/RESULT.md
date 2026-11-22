# A sharp discontinuous migration-onset threshold under paired habitat seasons

## Finding

Consider two habitat patches, with the favorable reproductive patch remaining the same for two consecutive seasons before switching for another two seasons, repeatedly. Positive migrant mortality changes the global growth-optimal migration fraction through a **single first-order transition**. For every pair of reproductive multipliers \(a>b>0\), there is a unique migration-survival threshold \(s_*(a/b)\in(0,4ab/(a+b)^2)\) such that:

- If \(0<s<s_*\), no migration is the unique long-run growth maximizer.
- If \(s=s_*\), there are **exactly two** maximizers: no migration and one unique interior fraction \(m_*\in(0,1)\).
- If \(s_*<s\leq1\), every growth maximizer is strictly interior, hence beats both no migration and full migration.

The threshold and its positive co-optimizer are determined exactly as the unique solution in the specified ranges of the two polynomial equations
\[
H_{c,s}(m)=0,\qquad \partial_mH_{c,s}(m)=0,
\qquad c=\frac{(a+b)^2}{ab}>4,
\]
where
\[
H_{c,s}(m)=4-cs+(cs+2s^2-6)m+4(1-s^2)m^2-(1-s^2)^2m^3.
\]
Thus the optimal fraction jumps by a positive amount at the threshold; it does not emerge continuously from zero. There is also a nonempty interval \(s_*<s<4/c\) in which an infinitesimal migration increase **reduces** growth while a sufficiently large interior migration fraction **improves** growth over isolation. For \(a=3,b=1\), numerical root evaluation gives \(s_*\approx0.71697211496516\), \(m_*\approx0.31318440219702\).

## Assumptions and scope

The population consists of two nonnegative abundance coordinates, with deterministic, density-independent nonoverlapping generations. Local multipliers are \(a>b>0\) in the favorable and unfavorable positions, respectively. Write
\[
D_+=\begin{pmatrix}a&0\\0&b\end{pmatrix},\quad
D_-=\begin{pmatrix}b&0\\0&a\end{pmatrix},\quad
M_s(m)=\begin{pmatrix}1-m&sm\\sm&1-m\end{pmatrix}.
\]
Each season reproduction precedes movement; a common fraction \(m\in[0,1]\) attempts to change patch, survives with probability \(s\in(0,1]\), and otherwise dies. Residents incur no movement mortality. The environmental order is \(D_+,D_+,D_-,D_-\), repeated indefinitely. Its four-season monodromy is
\[
P_s(m)=(M_s(m)D_-)^2(M_s(m)D_+)^2,
\]
and the long-run per-season multiplier is \(G_s(m)=\rho(P_s(m))^{1/4}\). For boundary fractions, evaluate the spectral radius directly; a strictly positive initial abundance in both patches attains the displayed dominant growth exponent. Maximization always ranges over the entire closed interval \(m\in[0,1]\). There is no density dependence, environmental stochasticity, adaptive behavior, or an evolutionary stability claim.

## Proof

**1. Reduce the four-season eigenvalue to a single quadratic.** Let \(J=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). The identities \(JD_+J=D_-\) and \(JM_s(m)J=M_s(m)\) imply
\[
P_s(m)=\left[J(M_s(m)D_+)^2\right]^2=K_s(m)^2.
\]
The nonnegative matrix \(K_s(m)\) therefore has \(G_s(m)^2=\rho(K_s(m))\). Direct multiplication, with \(u=1-m\) and \(v=sm\), gives
\[
\operatorname{tr}K_s(m)=(a+b)^2uv,\qquad
\det K_s(m)=-(ab)^2(u^2-v^2)^2.
\]
The eigenvalues of \(K_s(m)\) have opposite signs or one is zero (including the endpoints by continuity). Its Perron eigenvalue is the unique positive root of the characteristic polynomial. With \(R_s(m)=G_s(m)/\sqrt{ab}\) and \(c=(a+b)^2/(ab)>4\), the exact normalized equation is
\[
R_s(m)^4-csm(1-m)R_s(m)^2-\bigl((1-m)^2-s^2m^2\bigr)^2=0.
\]
At the two endpoints, \(R_s(0)=1\) and \(R_s(1)=s\). For \(0<m<1\), the characteristic polynomial of \(K_s(m)/(ab)\) is negative at one exactly when its unique positive root exceeds one. Expanding and factoring yields the strict equivalence
\[
R_s(m)>1\quad\Longleftrightarrow\quad
1-csm(1-m)-\bigl((1-m)^2-s^2m^2\bigr)^2<0
\quad\Longleftrightarrow\quad H_{c,s}(m)<0.
\]
Similarly, equality of \(R_s(m)\) with one is equivalent to \(H_{c,s}(m)=0\) in the interior.

**2. Strict convexity selects one interior contact.** For \(0<s<1\), differentiation of the displayed cubic gives
\[
H''_{c,s}(m)=2(1-s^2)\bigl(4-3(1-s^2)m\bigr)>0
\qquad (0\leq m\leq1).
\]
Moreover, \(H_{c,s}(0)=4-cs\) and \(H_{c,s}(1)=1-s^4\). For \(s\to0\), the cubic converges uniformly on \([0,1]\) to \(4-6m+4m^2-m^3\), a strictly decreasing function with minimum one at \(m=1\). Consequently, at sufficiently small positive survival the cubic is everywhere strictly positive and no positive migration fraction beats isolation.

At \(s=4/c<1\), one instead has \(H_{c,s}(0)=0\) and
\[
H'_{c,4/c}(0)=-2+\frac{32}{c^2}<0.
\]
Thus the cubic is strictly negative at some sufficiently small positive fraction, and isolation is then strictly suboptimal. The normalized growth \(R_s(m)\) is continuous jointly in \((s,m)\). At every fixed \(0<m<1\), it is **strictly increasing** in \(s\): the interior positive matrix \(K_s(m)\) increases entrywise strictly in its underlying migration matrix, and Perron–Frobenius monotonicity applies to its positive four-season monodromy. More explicitly, \(M_{s'}(m)>M_s(m)\) in both off-diagonal entries for \(s'>s\); multiplying positive diagonal growth and four seasons yields a strict Perron increase.

Put \(F_c(s)=\max_{0\leq m\leq1}R_s(m)\). Since \(R_s(0)=1\), \(F_c(s)\geq1\), and continuity on a compact domain makes \(F_c\) continuous. Define \(s_*\) as the infimum of survivals for which \(F_c(s)>1\). The preceding arguments give \(0<s_*<4/c\). Once any interior fraction first beats one, it continues to beat one at every greater survival (strict pointwise monotonicity), so the threshold is unique and \(F_c(s)>1\) precisely for \(s>s_*\).

At \(s=s_*\), continuity forces \(F_c(s_*)=1\). A strictly positive interior tying fraction must exist: because \(s_*<4/c\), \(H_{c,s_*}(0)=4-cs_*>0\), and \(H_{c,s_*}(1)=1-s_*^4>0\); thus if every interior value of \(H\) were strictly positive, compactness would make that positivity persist for slightly larger \(s\), contradicting the definition of \(s_*\). The cubic is strictly convex, so its zero minimum occurs at **one and only one** interior point \(m_*\); there \(H=H'=0\). Every other positive fraction is strictly suboptimal. Conversely, any solution of the two algebraic equalities with \(s\in(0,4/c)\) and \(m\in(0,1)\) must be the unique zero minimum of the strictly convex cubic, hence realizes this same transition by monotonicity. This proves existence, uniqueness, and exact algebraic characterization of \((s_*,m_*)\).

**3. Classify both sides and the local–global paradox.** For \(s<s_*\), the value one is not attained at a positive fraction: otherwise a slightly larger survival, still below threshold, would strictly improve that same fraction above one. So only \(m=0\) maximizes. For \(s>s_*\), some interior fraction is strictly superior to isolation. Full migration is never superior to isolation because \(R_s(1)=s\leq1\); hence **every** global maximizer must be interior. At the threshold exactly the two fractions \(0,m_*\) tie.

Differentiating the implicit normalized eigenvalue equation at \(m=0\) gives
\[
R_s'(0)=\frac{cs-4}{4}.
\]
Since \(s_*<4/c\), throughout the nonempty interval \((s_*,4/c)\), the zero-migration endpoint is locally better than every sufficiently small positive migration fraction, while a larger interior fraction strictly improves growth. This proves the discontinuous, not infinitesimal, onset.

**4. Reproducible numerical and exact checks.** For \((a,b,s,m)=(3,1,3/4,1/3)\), exact fraction arithmetic gives \(H_{16/3,3/4}(1/3)=-721/6912<0\), providing a strict interior-benefit witness. A separate exact contact example has \(c=180\sqrt7/49>4\), \(s=1/\sqrt7\), \(m=1/3\), for which both \(H\) and \(H'\) vanish identically. Such \(c\) is attainable: choose \(b=1\) and \(a=(c-2+\sqrt{c(c-4)})/2>1\). Neither example replaces the preceding universal proof.

## Verification

The standalone `verify.py` uses only the Python standard library. Run `python verify.py`; it checks the exact matrix trace, determinant, characteristic polynomial and rational witness across an independently enumerated rational grid; checks an exact radical tangency using rationalized combinations; and independently computes roots and sign boundaries for three fitness contrasts. It reports `VERIFY_OK 1383 test cases` and \(s_*\approx0.716972114965161\), \(m_*\approx0.313184402197024\) for \(c=16/3\). Its finite grid is supplementary evidence, **not** the proof of uniqueness or optimality over continuous parameter ranges; those are established above.

## Relationship to prior work

Backus, Clements, and Baskett (2024) develop and simulate a multi-patch stochastic metapopulation under spatial and temporal environmental heterogeneity, including reproduction, dispersal, and density regulation. Their full open-access methods and discussion motivate attention to dispersal limitations, but do not specify or optimize this discrete four-season mortality-penalized matrix product. Benaïm, Lobry, Sari, and Strickler (arXiv:2407.07553) prove general continuous-time periodic dispersal growth/decay criteria and examine two-patch examples; their equations use conservative continuous migration generators and do not imply the present exact discrete-time mortality threshold.

Schreiber and Li (arXiv:1007.5267) analyze the evolution of unconditional dispersal in periodic environments under different objectives and without travel mortality in their main model. Published mathematical records describing a two-season endpoint theorem and an exactly alternating two-patch mortality threshold establish closely related **prior** results, and are expressly not claimed anew here. Those deal with alternating profiles \(D_+,D_-\), not repeated blocks \(D_+,D_+,D_-,D_-\). A distinct four-season result establishes existence of an interior optimum without movement mortality for generic sequences, and another classifies **reordering** four profiles at fixed dispersal. None of the inspected statements supplies the unique strictly interior tangency threshold, the exact cubic certificate, and the local-versus-global growth reversal for the present paired-block/mortality family. These are comparisons of mathematical implications, not an absolute historical priority certificate.

## Limitations

Only two patches; equal (but unequal across habitats) reproductive multipliers within each two-season block; exactly alternating paired blocks; deterministic linear dynamics; constant symmetric movement fraction and migrant survival; no competing evolutionary strategies or environmental randomization. The theorem does **not** prove uniqueness of the optimal positive fraction for survival *above* the threshold; only the critical fraction at the threshold is unique. A local Perron multiplier is not a statement about actual demographic extinction probability or a calibrated intervention. Uninspected older positive-matrix, migration-cost, and periodically varying environment literature can contain equivalent specialized formulas, so priority remains provisional. Independent external audit has not been performed.

## References

1. G. A. Backus, C. F. Clements, and M. L. Baskett, “Restoring spatiotemporal variability to enhance the capacity for dispersal-limited species to track climate change,” *Ecology* 105, e4257 (2024), first published 2024-03-01. https://doi.org/10.1002/ecy.4257 . Full HTML: https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/ecy.4257 .
2. M. Benaïm, C. Lobry, T. Sari, and E. Strickler, “Dispersal-induced growth or decay in a time-periodic environment,” arXiv:2407.07553, first submitted 2024-07-10. https://arxiv.org/abs/2407.07553 .
3. S. J. Schreiber and C.-K. Li, “Evolution of unconditional dispersal in periodic environments,” arXiv:1007.5267, first submitted 2010-07-29. https://arxiv.org/abs/1007.5267 .
4. “Four seasons are necessary and sufficient for interior-optimal dispersal in a two-patch periodic model,” published mathematical record (2026-10-12). https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-four-seasons-are-necessary-and-sufficient-for-interior-optimal-d--277a84601303 .
5. “Two-season endpoint optimality and the first interior dispersal optimum,” published mathematical record (2026-10-26). https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-season-endpoint-optimality-and-the-first-interior-dispersal--4bf78d70bf53 .
6. “An exact all-or-nothing dispersal transition under alternating habitat quality and migration mortality,” published mathematical record (2026-10-18). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-an-exact-all-or-nothing-dispersal-transition-under-alternating-h--087b8ca4b9b8 .
7. “Four-season ecological growth has an exact temporal-order reversal at half dispersal,” published mathematical record (2026-11-02). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-season-ecological-growth-has-an-exact-temporal-order-revers--3268e9366f52 .
