# Cyclic mortality ordering shifts the weak-heterogeneity stability threshold at cubic order

## Finding

A well-mixed three-species competitive community has a subtle sensitivity to **which species receives each mortality rate**, even if the unordered mortality distribution and all its moments are unchanged. For the pairwise/three-way tournament model specified below, write \(q=2p-1>0\), let \(a_1+a_2+a_3=0\), and define
\[
S_2=a_1^2+a_2^2+a_3^2,\qquad
V=(a_1-a_2)(a_2-a_3)(a_3-a_1).
\]
For any fixed \(p\in(1/2,1)\) and nonzero zero-sum \((a_1,a_2,a_3)\), the unique local coexistence-equilibrium branch near equal abundances has a unique nearby linear-stability threshold, and
\[
\boxed{\alpha_c(\varepsilon)=\frac{S_2}{q^2}\varepsilon^2+\frac{V}{q^3}\varepsilon^3+O(\varepsilon^4).}
\]
The cubic correction is **orientation-sensitive**: a transposition of mortality rates reverses \(V\) while preserving all symmetric statistics of those rates. Therefore, no statistic of the *unordered* mortality-rate multiset can determine the exact local stability threshold, even arbitrarily close to the equal-rate regime.

For \(p=3/4\), the two assigned mortality perturbations \(a^+=(1,-1,0)\) and \(a^-=(1,0,-1)\), which share the multiset \(\{1,0,-1\}\), satisfy
\[
\alpha_c^+(\varepsilon)=8\varepsilon^2+16\varepsilon^3+O(\varepsilon^4),\qquad
\alpha_c^-(\varepsilon)=8\varepsilon^2-16\varepsilon^3+O(\varepsilon^4),
\]
so \(\alpha_c^+-\alpha_c^-=32\varepsilon^3+O(\varepsilon^4)>0\) for all sufficiently small positive \(\varepsilon\).

## Assumptions and scope

There are exactly three types, with frequencies \(x_i>0\), \(\sum_i x_i=1\), fecundities \(f_i=1\), and positive mortality rates \(d_i=1+\varepsilon a_i\). The vector \(a\) is fixed and nonzero with \(\sum_i a_i=0\). Fix \(1/2<p<1\) and set \(q=2p-1\). Pairwise dominance probabilities are
\[
H=\begin{pmatrix}\tfrac12&p&1-p\\1-p&\tfrac12&p\\p&1-p&\tfrac12\end{pmatrix}.
\]
For ordered pairwise opponents \(j,k\), define the triplewise tournament weights
\[
B_{ijk}=2H_{ij}H_{ik}+H_{ij}H_{jk}+H_{ik}H_{kj}.
\]
The fraction of contests taking three rather than two individuals is \(\alpha\in[0,1]\). Define \(D(x)=\sum_i d_ix_i\). The model, with time measured in the convention of the cited initiating article, is
\[
\frac{dx_i}{dt}=x_i\left(D(x)\left[2(1-\alpha)\sum_j H_{ij}x_j+\alpha\sum_{j,k}B_{ijk}x_jx_k\right]-d_i\right).
\]
This is Equation (3) of Duran-Sala, Meloni and Calleja-Solanas specialized to constant fecundity. The polynomial vector field leaves the simplex invariant. Every assertion here concerns the *analytic interior equilibrium branch near* \(x=(1/3,1/3,1/3)\), for \(|\varepsilon|\) and \(\alpha\) sufficiently small. No uniqueness of distant equilibria, global stability, or finite-population survival is claimed.

Precisely, for fixed \(p,a\), there are \(\varepsilon_0>0\), \(\eta>0\), and an analytic equilibrium \(x^*(\varepsilon,\alpha)\) with \(x^*(0,0)=(1/3,1/3,1/3)\), which is the sole equilibrium in a fixed neighborhood of that point for \(|\varepsilon|<\varepsilon_0\) and \(|\alpha|<\eta\). For each nonzero \(|\varepsilon|<\varepsilon_0\), there is exactly one \(\alpha_c(\varepsilon)\in(0,\eta)\) at which the trace of its two-dimensional simplex Jacobian vanishes. This branch is linearly unstable for \(0\le\alpha<\alpha_c\), locally asymptotically stable for \(\alpha_c<\alpha<\eta\), and has a nonzero purely imaginary conjugate linear pair at \(\alpha=\alpha_c\). The statements are local in \(\varepsilon,\alpha\) but hold for either sign of \(\varepsilon\).

## Proof

**1. Analytic equilibrium and linear spectrum at the reference point.** Eliminate \(x_3=1-x_1-x_2\). The restricted vector field is polynomial in \(x_1,x_2,\varepsilon,\alpha\), so real analytic. At \(\varepsilon=\alpha=0\), the equal-abundance state \(u=(1/3,1/3,1/3)\) is an equilibrium. Direct differentiation of the pairwise vector field gives a reduced Jacobian with determinant \(q^2/3>0\) and trace zero. Thus the Jacobian is invertible with eigenvalues \(\pm iq/\sqrt3\). The real-analytic implicit function theorem gives a locally unique analytic branch \(x^*(\varepsilon,\alpha)\); its determinant remains strictly positive, and the branch remains interior after reducing the neighborhood.

**2. An exact pairwise equilibrium and trace.** For \(a=(a,b,-a-b)\), at \(\alpha=0\) define
\[
\bar x(\varepsilon)=\frac13(1,1,1)+\frac{\varepsilon}{3q}(-a-2b,\,2a+b,\,-a+b).
\]
A direct multiplication verifies \(\sum_i\bar x_i=1\), \(D(\bar x)=1\), and \(2H\bar x=(d_1,d_2,d_3)^T\). These are exactly the interior fixed-point conditions, so \(\bar x=x^*(\varepsilon,0)\) for sufficiently small \(\varepsilon\). The pairwise trace identity, Eq. (21) of Duran-Sala et al., with \(f_i=1\) and \(F=D=1\), reads
\[
\tau(\varepsilon,0)=\sum_i\bar x_i(d_i-1)^2=\varepsilon^2\sum_i\bar x_i a_i^2.
\]
The right side is a cubic polynomial in \(\varepsilon\). Direct substitution, using \(a_1+a_2+a_3=0\), gives the **exact identity**
\[
\tau(\varepsilon,0)=\frac{S_2}{3}\varepsilon^2+\frac{V}{3q}\varepsilon^3.
\]
The coefficient \(V\) follows by expanding \(\sum_i a_i^2(-a-2b,2a+b,-a+b)_i\); it equals \((a-b)(a+2b)(-2a-b)\). No asymptotic numerical fitting is involved.

**3. Exact homogeneous trace and absence of a mixed linear perturbation.** At \(\varepsilon=0\), the equilibrium stays at \(u\) for all \(\alpha\) near zero. The homogeneous tournament Jacobian identity, Eq. (23) of the initiating source, is
\[
J(0,\alpha)=\left(1+\frac\alpha2\right)J(0,0)+\frac\alpha2J(0,0)^2.
\]
Since \(\operatorname{tr}J(0,0)=0\) and \(\det J(0,0)=q^2/3\), Cayley–Hamilton gives
\[
\tau(0,\alpha)=-\frac{q^2}{3}\alpha.
\]
Furthermore, cyclic permutation of the three species leaves \(H\) and \(B\) invariant. For each fixed sufficiently small \(\alpha\), the linear coefficient in \(\varepsilon\) of \(\tau(\varepsilon,\alpha)\), evaluated at the analytic equilibrium branch, is a cyclic-invariant linear functional of \((a_1,a_2,a_3)\). Such a functional must be a scalar multiple of \(a_1+a_2+a_3=0\). Consequently \(\partial_\varepsilon\tau(0,\alpha)=0\) identically, including the potentially troublesome \(\alpha\varepsilon\) term.

Analyticity, the exact \(\alpha=0\) trace, and these identities imply, for \(\alpha=O(\varepsilon^2)\),
\[
\tau(\varepsilon,\alpha)=\frac{S_2}{3}\varepsilon^2+\frac{V}{3q}\varepsilon^3-\frac{q^2}{3}\alpha+O(\varepsilon^4+|\alpha|\varepsilon^2).
\]
The remainder statement follows by Taylor expansion: every term not displayed either vanishes on \(\alpha=0\), vanishes on \(\varepsilon=0\), or contains at least \(\varepsilon^2\alpha\). In fact the \(\alpha=0\) trace has no fourth-order term.

**4. The unique crossing.** Since \(\partial_\alpha\tau(0,0)=-q^2/3<0\), the implicit function theorem gives a unique real-analytic trace-zero curve \(\alpha_c(\varepsilon)\) near the origin, with \(\alpha_c(0)=0\). Its coefficient of \(\varepsilon\) vanishes. Substituting \(\alpha_c=c_2\varepsilon^2+c_3\varepsilon^3+O(\varepsilon^4)\) in the trace expansion gives \(c_2=S_2/q^2\), \(c_3=V/q^3\). Because \(S_2>0\), the critical fraction is positive for sufficiently small nonzero \(\varepsilon\). Shrinking the neighborhood ensures \(\partial_\alpha\tau<0\) and \(\det J>0\) throughout. Thus the trace is strictly positive below its sole zero and strictly negative above; the standard two-dimensional trace/determinant criterion proves the claimed linear instability and local asymptotic stability. At the crossing, \(\tau=0\) and \(\det J>0\), giving two nonzero purely imaginary linear eigenvalues, without any assertion about nonlinear Hopf criticality.

**5. Assigning the same rates to different positions.** The choices \((1,-1,0)\) and \((1,0,-1)\) have the same unordered values, mean and variance; their \(S_2=2\), while \(V=2\) and \(V=-2\). At \(q=1/2\), the displayed two expansions and their strict difference follow. The oriented cubic term changes sign under odd permutations and is unchanged by cyclic relabeling, exactly as required by the directional cycle structure.

## Verification

The standalone `CHECK.py` uses exact symbolic arithmetic (SymPy) to verify the normalization of both contest tensors, exact pairwise equilibrium, exact cubic pairwise trace, base determinant, homogeneous trace, and vanishing linear mixed derivative. It additionally computes independently the equilibrium and Jacobian by numerical root-finding and finite differences for two permuted assignments and three perturbation sizes; those numerical computations are *consistency checks*, not the proof of the asymptotic theorem. Run `python3 CHECK.py` with `sympy`, `numpy`, and `scipy` installed. The script prints `All checks passed` on success. Its exact checks complement, but do not substitute for, the analytic implicit-function and symmetry argument given above.

For \(p=3/4\) and \(\varepsilon=0.02\), numerical trace-zero crossings are approximately \(0.00333310532008\) for \(a^+\) and \(0.00307710740516\) for \(a^-\), versus cubic predictions \(0.003328\) and \(0.003072\).

## Relationship to prior work

Duran-Sala, Meloni and Calleja-Solanas introduce the mixed pairwise/three-way contest dynamics and establish the zero-higher-order instability trace and equal-rate stabilization. Their Appendix C states that for heterogeneous physiological rates the equilibrium and local-stability threshold generally require numerical analysis; figures describe a leading dependence on physiological-rate variability. The displayed exact weak-heterogeneity expansion resolves a narrower analytic question and, specifically, distinguishes two **assignments of the same mortality-rate multiset** by a signed third-order term. The known first-order effect of mortality variance and the source's pairwise trace and homogeneous Jacobian formulas are acknowledged as ingredients, not new discoveries.

Grilli et al. establish the tournament-based stabilizing mechanism, especially under equal physiological rates. Gibbs et al. analyze constrained higher-order terms in a generalized Lotka–Volterra model rather than the exact normalized three-contest mixture here. The specific cubic, permutation-sensitive threshold comparison was not found in the accessible material inspected, but bibliographic search cannot prove universal historical priority. The initiating article mentions supplementary material on *small-difference threshold scaling* without an accessible complete text in this inspection; a prior derivation of a matching cubic term in that supplement would cover this claim. This risk remains explicit.

## Limitations

The proof concerns one local analytic equilibrium branch and sufficiently weak heterogeneity; it makes no claim for arbitrary demographic differences, all higher-order proportions, uniqueness of distant equilibria, global persistence or the existence of bifurcating cycles. It assumes constant fecundity, cyclic symmetric pairwise win strengths, and a very specific tournament rule for triplewise interactions. The theorem is a mathematical, not empirically calibrated, species-competition statement. Its historical priority is contingent on material accessible in the described comparison, particularly the not-fully-accessible supplement.

## References

1. M. Duran-Sala, S. Meloni, V. Calleja-Solanas, *Species differences dilute the stabilizing effect of higher-order interactions in competitive communities*, arXiv:2501.09172, initial submission 15 January 2025, revised v4 12 November 2026. https://arxiv.org/abs/2501.09172 ; https://arxiv.org/html/2501.09172v4 . Equations (3), (21), (23); Section III.2 and Appendix C.
2. J. Grilli, G. Barabás, M. J. Michalska-Smith, S. Allesina, *Higher-order interactions stabilize dynamics in competitive network models*, Nature **548** (2017), 210–213. https://doi.org/10.1038/nature23273 ; open author manuscript: https://michalska-smith.com/pdfs/higherorder.pdf .
3. T. L. Gibbs et al., *When can higher-order interactions produce stable coexistence?*, Ecology Letters **27** (2024), e14458. https://doi.org/10.1111/ele.14458 .
