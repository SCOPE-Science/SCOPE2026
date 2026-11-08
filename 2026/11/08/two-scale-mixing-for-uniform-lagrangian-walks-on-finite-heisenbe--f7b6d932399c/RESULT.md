# Two-scale mixing for uniform Lagrangian walks on finite Heisenberg groups

## Finding
Let \(q\) range over prime powers, \(m\ge1\), \(Q=q^m\), and let \(P_t\) be the \(t\)-step law of the probability measure \(\mu=(u_X+u_Y)/2\) on the finite Heisenberg group defined below. The right-convolution Markov operator has the following **complete eigenvalue multiset**, including algebraic multiplicities:

\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
1&1\\
1/2&2(Q-1)\\
(1+Q^{-1/2})/2&(q-1)Q\\
(1-Q^{-1/2})/2&(q-1)Q\\
0&(Q-1)^2+(q-1)Q(Q-2).
\end{array}
\]

For every integer \(t\ge1\), its exact chi-square divergence from uniformity is
\[
\chi^2(P_t\|U)=2(Q-1)4^{-t}+(q-1)Q\left[\left(\frac{1+Q^{-1/2}}2\right)^{2t}+\left(\frac{1-Q^{-1/2}}2\right)^{2t}\right]. \tag{1}
\]
Writing \(\alpha_t=t/2^{t-1}\), its total-variation distance satisfies the **uniform two-sided bounds**
\[
\alpha_t-\frac2q-\frac2{qQ}\ \le\ \lVert P_t-U\rVert_{\mathrm{TV}}\ \le\ \alpha_t+\frac{1-1/q}{Q}. \tag{2}
\]
In particular, for every fixed integer \(m\ge1\), as \(q\to\infty\) through prime powers, the limit of the total-variation distance at each fixed \(t\ge1\) is exactly \(t/2^{t-1}\); for any integer sequence \(t(q)\to\infty\), that distance tends to zero. In contrast, chi-square has a sharp order-\(\log q\) transition at \(t_*(q)=\log_4(q^{m+1})\): if \(t(q)-t_*(q)\to+\infty\), chi-square tends to zero, whereas if \(1\le t(q)\) and \(t(q)-t_*(q)\to-\infty\), it diverges. More precisely, whenever \(q^{m+1}4^{-t(q)}\to h\in(0,\infty)\), chi-square tends to \(2h\). Hence there are sequences with total-variation distance tending to zero while chi-square diverges, for example any \(t(q)\to\infty\) with \(t(q)=o(\log q)\).

## Assumptions and scope
The group is \(H_m(\mathbb F_q)=\mathbb F_q^m\times\mathbb F_q^m\times\mathbb F_q\), with multiplication
\[
(x,y,z)(x',y',z')=(x+x',y+y',z+z'+x\cdot y').
\]
Here \(x\cdot y\) is the standard nondegenerate bilinear dot product. Define the two order-\(Q\) subgroups \(X=\{(x,0,0)\}\) and \(Y=\{(0,y,0)\}\), and let \(u_X,u_Y\) be their uniform probability measures. Independent steps are drawn from \(\mu=(u_X+u_Y)/2\), and multiplication begins at the identity. The uniform measure on the group of order \(qQ^2\) is \(U\). The chi-square convention is \(\chi^2(P\|U)=\sum_{g}(P(g)-U(g))^2/U(g)\), and total variation is half the \(\ell^1\)-distance. All results hold for even and odd characteristic and for prime-power, not just prime, field orders; the asymptotic statements keep \(m\) fixed. The formula (1) is asserted only for \(t\ge1\), because the zero eigenvalue directions do contribute at time zero.

## Proof
**Representation decomposition.** The group has exactly \(Q^2\) one-dimensional irreducible characters, parametrized by \((a,b)\) in the dual of \(\mathbb F_q^m\times\mathbb F_q^m\). Its other irreducibles are the \(q-1\) Stone--von Neumann representations of dimension \(Q\), one for each nontrivial additive character \(\psi\) of the center; the sum of squared dimensions is \(Q^2+(q-1)Q^2=qQ^2\), proving completeness. In a Schrödinger model on functions \(f:\mathbb F_q^m\to\mathbb C\), the first subgroup translates arguments and the second multiplies by phases \(\psi(y\cdot x)\). Averaging over \(X\) is the orthogonal projection \(P_c\) onto the constant vector, and averaging over \(Y\) is the orthogonal projection \(P_0\) onto the delta vector at zero. Their unit spanning vectors have overlap modulus \(Q^{-1/2}\).

**All eigenvalues.** On one-dimensional characters, the two subgroup averages are indicators of \(a=0\) and \(b=0\). This gives one eigenvalue \(1\), exactly \(2(Q-1)\) eigenvalues \(1/2\), and \((Q-1)^2\) eigenvalues zero. On each nontrivial central representation, the Fourier multiplier is \((P_c+P_0)/2\). The sum of two unit rank-one projections with overlap \(c\) has nonzero eigenvalues \(1\pm c\), so its spectrum consists of \((1\pm Q^{-1/2})/2\) and \(Q-2\) zeros (none of the two positive levels is zero when \(Q\ge2\)). The right-regular representation contains each irreducible with multiplicity its dimension; hence multiply each central-representation eigenvalue multiplicity by \(Q\). This produces the displayed complete multiset. All Fourier multipliers are Hermitian because \(\mu\) is inversion invariant.

**Exact divergence.** Finite-group Plancherel for a symmetric measure gives \(\chi^2(P_t\|U)=\sum_{\rho\ne\mathbf1}d_\rho\operatorname{tr}(\widehat\mu(\rho)^{2t})\). Substituting all nonprincipal eigenvalues yields (1), with no approximation or missing zero directions when \(t\ge1\).

**Total-variation run decomposition.** Condition on the independent fair labels \(X,Y\) assigned to the \(t\) steps. Uniform subgroup measures are convolution-idempotent, so a block of identical labels collapses to one uniform subgroup factor. Of the \(2^t\) label strings, exactly \(2t\) have at most two runs. Their total probability is \(\alpha_t\); their products are supported on the event \(E=X\cup Y\cup XY\cup YX\), with \(U(E)\le(2Q^2+2Q)/(qQ^2)=2/q+2/(qQ)\). Thus \(\lVert P_t-U\rVert_{\rm TV}\ge P_t(E)-U(E)\ge\alpha_t-2/q-2/(qQ)\).

Every label string with at least three runs contains a consecutive reduced factor \(XYX\) or \(YXY\), with other subgroup-convolution factors on either side. For the \(XYX\) product, the two abelianized coordinates are jointly uniform; conditional on the middle \(Y\)-coordinate being nonzero, the central coordinate is exactly uniform, whereas at middle coordinate zero the central coordinate is identically zero. Consequently \(\lVert u_X*u_Y*u_X-U\rVert_{\rm TV}=(1-1/q)/Q\). The same holds for \(YXY\). Additional convolutions cannot increase distance to the bi-invariant measure \(U\). Convexity after splitting the low- and high-run strings gives the upper bound in (2).

**Different mixing scales.** For fixed \(m\), \(Q=q^m\to\infty\). Bound (2) yields the fixed-step total-variation profile and convergence for all \(t(q)\to\infty\). For \(t=O(\log q)\), the binomial expansions or \((1\pm Q^{-1/2})^{2t}=1+o(1)\) show, uniformly in this range, \(\chi^2(P_t\|U)=2(qQ-1)4^{-t}(1+o(1))\). At the critical scale this proves the asserted \(2h\) profile. Above the scale by an unbounded number of steps, use monotonicity of chi-square under convolution and compare with an intermediate time \(t_*+r(q)\), where \(r(q)\to\infty\) and \(r(q)=O(\log q)\); below the scale, the \((q-1)Q\) central-representation terms and \((1+Q^{-1/2})^{2t}\ge1\) give a divergent lower bound. Both conclusions are valid for any admissible integer sequences.

## Verification
The independent-from-the-formulas computational route in `check_heisenberg.py` constructs each group law and computes the full probability distribution by explicit integer convolution. It then compares the **exact rational** chi-square distance with (1) and checks both inequalities (2), for every step in the following ranges: \((q,m,t)\) with \((q,m)\in\{(2,1),(3,1),(4,1),(5,1)\}\) and \(1\le t\le6\), also \((7,1)\) and \(1\le t\le5\), \((2,2)\) and \(1\le t\le5\), \((3,2)\) and \(1\le t\le3\), and \((2,3)\) and \(1\le t\le4\). Field order \(4\) uses genuine \(\mathbb F_4\) arithmetic, not integers modulo \(4\). The run ends with `HEISENBERG_LAGRANGIAN_WALK_EXACT_CHECKS_PASS`. These finite experiments check normalizations and identities; the general theorems follow from the preceding algebraic and probabilistic proofs.

## Relationship to prior work
Bump--Diaconis--Hicks--Miclo--Widom (2015 preprint, 2017 publication) analyze a **four-generator nearest-neighbor** walk on the finite Heisenberg group and its Harper-operator matrices; their sharp scale is quadratic in the modulus, not the present full-subgroup walk. Diaconis--Hough (2015 preprint, 2021 publication) study local limits for unipotent groups and mixing of certain coordinates under bounded-support generating measures. The present subgroup-averaging walk instead has two rank-one Fourier projections and admits an exact all-eigenvalue formula, an exact all-time chi-square formula, and a short-run total-variation profile. These works supply established general Fourier and probability context, not those explicit conclusions for the specified measure. General two-projection spectral identities cover the linear-algebra step, but do not themselves give the group-specific eigenvalue multiplicities or the high-contrast total-variation/chi-square mixing laws.

## Limitations
No exact finite-parameter total-variation formula is claimed: (2) is an explicit two-sided bound and gives a sharp limiting profile with \(m\) fixed and \(q\to\infty\). The result concerns uniform full coordinate subgroups, not sparse nearest-neighbor Heisenberg generators. Historical-priority comparison was bounded; an unlocated general theorem on walks driven by subgroup averages might imply part of the spectral calculation. Independent mathematical validation has not been performed.

## References
1. D. Bump, P. Diaconis, A. Hicks, L. Miclo, H. Widom, *An Exercise (?) in Fourier Analysis on the Heisenberg Group*, arXiv:1502.04160 (first posted 2015-02-14); Ann. Fac. Sci. Toulouse 26 (2017), 263–288, doi:10.5802/afst.1533. https://arxiv.org/abs/1502.04160
2. P. Diaconis, R. Hough, *Random Walk on Unipotent Matrix Groups*, arXiv:1512.06304 (first posted 2015-12-20); Ann. Sci. Éc. Norm. Supér. 54 (2021), 587–625, doi:10.24033/asens.2466. https://arxiv.org/abs/1512.06304
3. P. Diaconis, *Group Representations in Probability and Statistics*, IMS Lecture Notes–Monograph Series 11, 1988 (Fourier Plancherel for finite-group random walks).
