# All-or-nothing dispersal under alternating two-patch growth with migration mortality

## Finding

Consider a rare population with two habitat patches. During successive generations, the per-capita linear demographic factors alternate deterministically between the vectors \((a,b)\) and \((b,a)\), where \(a>b>0\). A proportion \(p\in[0,1]\) leaves each patch after reproduction, and a migrant reaches the other patch with probability \(h\in(0,1)\); non-migrants survive movement with probability one. The same \(p\) and \(h\) apply to both patches and seasons. Let \(G(p)\) be the asymptotic per-generation multiplicative growth factor from any strictly positive initial abundance vector.

**Theorem.** For every \(a>b>0\) and \(0<h<1\),
\[
 G(p)=\frac{hp(a+b)+\sqrt{h^2p^2(a-b)^2+4ab(1-p)^2}}{2}.
\]
This is strictly convex on \([0,1]\). Write
\[
 h_{\mathrm{global}}=\sqrt{b/a},\qquad
 h_{\mathrm{local}}=\frac{2\sqrt{ab}}{a+b}.
\]
Then \(0<h_{\mathrm{global}}<h_{\mathrm{local}}<1\), and the *unique* globally growth-maximizing dispersal policy is \(p=0\) when \(h<h_{\mathrm{global}}\), and \(p=1\) when \(h>h_{\mathrm{global}}\). At equality, **exactly** \(p=0\) and \(p=1\) are global maximizers; no interior policy is optimal. Moreover, for every \(h<h_{\mathrm{local}}\), the growth factor first decreases and then increases with \(p\), with exactly one interior minimum. In particular, the nonempty window \(h_{\mathrm{global}}<h<h_{\mathrm{local}}\) has a one-sided locally maximizing sedentary policy \(p=0\), even though complete migration \(p=1\) is strictly globally better.

This gives a strong extinction-rescue example: when \((a,b,h)=(4,1/8,3/10)\), both isolated patches decline geometrically with factor \(1/\sqrt 2\), and the derivative of \(G\) at \(p=0\) is negative, yet complete dispersal grows at factor \(6/5\). A population growth threshold \(G(p)=1\) is crossed at the unique point
\[
 p_{\mathrm{rescue}}=\frac{\sqrt{154625}-95}{364}=0.819296304452\ldots.
\]
The population declines at rates \(0\le p<p_{\mathrm{rescue}}\) and grows for \(p>p_{\mathrm{rescue}}\) in the linearized model.

## Assumptions and scope

The model has *fixed periodic environmental quality*, with complementary good and bad seasons, and **density-independent growth at low population size**. If \(x_t\in\mathbb R_{\ge0}^2\) is patch abundance before reproduction in season \(t\), then
\[
 x_{t+1}=M(p)D_t x_t,\quad
 M(p)=\begin{pmatrix}1-p&hp\\hp&1-p\end{pmatrix},\quad
 D_{2j}=\operatorname{diag}(a,b),\quad
 D_{2j+1}=\operatorname{diag}(b,a).
\]
All assertions quantify over **every** real \(a>b>0\), \(0<h<1\), and all admissible \(p\in[0,1]\). The intervention objective is the leading **per-generation Floquet/Perron multiplier** of the rare-population linearization, not carrying capacity, resident-mutant evolutionary stability, transient mean abundance, stochastic extinction probability, or a nonlinear equilibrium. At \(p=0\) the population decouples but both patches have the same two-season growth factor \(ab\), so the specified multiplier exists and is unambiguous.

## Proof

Set \(D=\operatorname{diag}(a,b)\), \(J=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), and \(D'=JDJ=\operatorname{diag}(b,a)\). Because \(J\) commutes with \(M(p)\), the two-season matrix satisfies the exact identity
\[
 P(p)=M(p)D'M(p)D=(JM(p)D)^2.
\]
Indeed, writing \(N=JM(p)D\), we obtain
\[
 N=\begin{pmatrix}hpa&(1-p)b\\(1-p)a&hpb\end{pmatrix},\quad
 \operatorname{tr}N=hp(a+b),\quad
 \det N=ab\bigl(h^2p^2-(1-p)^2\bigr).
\]
The two characteristic roots are real, and the larger one is nonnegative and at least the absolute value of the smaller root because \(N\) is nonnegative. Its formula is precisely \(G(p)\) in the theorem, because \(\rho(P)=\rho(N^2)=\rho(N)^2\); for strictly positive initial conditions this equals the asymptotic per-generation growth factor. This also holds at both endpoints by direct evaluation.

For strict convexity, put \(A=h^2(a-b)^2>0\), \(B=4ab>0\), and \(Q(p)=Ap^2+B(1-p)^2\). The exact derivative identity
\[
 G''(p)=\frac{AB}{2[Q(p)]^{3/2}}>0
\]
holds throughout \([0,1]\), since \(Q(p)>0\). Therefore, for each \(0<p<1\),
\[
 G(p)<(1-p)G(0)+pG(1)\le\max\{G(0),G(1)\}.
\]
The endpoint values are \(G(0)=\sqrt{ab}\) and \(G(1)=ha\). Comparing them proves the entire global optimizer classification including the exact tie and strict interior exclusion.

The endpoint derivatives are
\[
 G'(0)=\frac{h(a+b)}2-\sqrt{ab},\qquad
 G'(1)=ha>0.
\]
Strictly increasing \(G'\) implies a unique interior stationary point, necessarily a strict minimum, if and only if \(h<h_{\mathrm{local}}\). If \(h\ge h_{\mathrm{local}}\), the function is strictly increasing on \((0,1)\). The inequality \(h_{\mathrm{global}}<h_{\mathrm{local}}\) follows from \(a+b<2a\), and \(h_{\mathrm{local}}<1\) from strict arithmetic–geometric mean, so the stated hysteresis-like local-versus-global optimization window is nonempty.

For the example, \(G(0)=1/\sqrt2<1\), \(G(1)=6/5>1\), and \(G'(0)=99/160-1/\sqrt2<0\). The function is strictly convex with exactly one minimum; hence there is exactly one crossing of \(G(p)=1\) in \((0,1)\). Squaring the characteristic equation at multiplier one yields
\[
 ab(1-h^2)p^2+[h(a+b)-2ab]p+ab-1=0,
\]
which for these parameters reduces to \(182p^2+95p-200=0\). Its unique positive root is the displayed \(p_{\mathrm{rescue}}\). At that root the positive Perron eigenvalue is one (rather than the other eigenvalue), because \(G\) crosses one continuously and uniquely and the formula gives \(2-hp(a+b)>0\); direct substitution also verifies this condition.

## Verification

The accompanying `verify.py` is standalone Python 3 (standard library only). Run `python3 verify.py` from the extracted package directory. It computes direct two-season matrices and the independently factored square using exact rational arithmetic across 504 parameter combinations, checks characteristic invariants, and compares the computed spectral root to the closed formula and the two-season Perron root. It also checks strict-chord diagnostics and the rational example. The tested cases are finite diagnostics only; the all-real-parameter result is proved by the analytical identities and convexity argument above.

## Relationship to prior work

The 2010 preprint of Schreiber and Li analyzes the evolution of dispersal in periodically varying patches, using season-dependent demographic factors and migration matrices, but explicitly assumes **no loss of migrants** in its main theorem (column-stochastic redistribution). Its main comparisons concern evolutionary invasion of dispersal phenotypes and do not yield the mortality-dependent global optimizer, two separate critical survival thresholds, or the strict nonconvex strategic consequence reported here. Their discussion specifically identifies intermediate costs of dispersal as needing additional methods.

Kirkland, Li, and Schreiber (2006) permit column-substochastic migration matrices, but analyze **temporally constant** patch qualities; their spectral-radius monotonicity results for a *single* growth matrix do not compare the product of two periodically reversed growth-and-dispersal matrices. McPeek and Holt (1992) analyze density-regulated, phenotype-competition simulations with changing carrying capacities, not the rare-population linear multiplier under a fixed mortality cost. These are materially related, but their inspected statements do not imply the theorem by a parameter substitution. A separate finite-state two-patch source–sink result concerns continuous-time biomass optimization and not Floquet growth of an alternating season.

## Limitations

The result is deliberately restricted to two patches, exactly complementary growth factors in the two seasons, symmetric dispersal and mortality, and one common time-independent dispersal probability. Changing season length, asymmetric patch exchange, adding density regulation, demographic stochasticity, or optimizing total population rather than rare-population growth may create interior optima; none is excluded by this theorem. In particular, “locally optimal” refers to the one-sided derivative of the specified growth objective, **not** evolutionary or dynamical stability. Existing literature may contain an equivalent spectral optimization in a different terminology; historical priority remains provisional pending an independent specialized literature audit. The source papers themselves make no claim of independent verification of this result.

## References

1. S. J. Schreiber and C.-K. Li, *Evolution of unconditional dispersal in periodic environments* (preprint public 2010-07-29), arXiv:1007.5267, https://arxiv.org/abs/1007.5267, journal DOI:10.1080/17513758.2010.525667.
2. S. Kirkland, C.-K. Li, and S. J. Schreiber, *On the Evolution of Dispersal in Patchy Landscapes*, SIAM Journal on Applied Mathematics 66 (2006), 1366–1382, DOI:10.1137/050628933. Lawfully accessible full text: https://schreiber.faculty.ucdavis.edu/wp-content/uploads/sites/568/2022/09/050628933.pdf.
3. M. A. McPeek and R. D. Holt, *The Evolution of Dispersal in Spatially and Temporally Varying Environments*, American Naturalist 140 (1992), 1010–1027, DOI:10.1086/285453. Publicly accessible full text: https://www.zoology.ubc.ca/let/pdfs/McPeek_Holt_1992.pdf.
4. D. P. Hardin, P. Takáč, and G. F. Webb, *A Comparison of Dispersal Strategies for Survival of Spatially Heterogeneous Populations*, SIAM Journal on Applied Mathematics 48 (1988), DOI:10.1137/0148086 (abstract inspected).
