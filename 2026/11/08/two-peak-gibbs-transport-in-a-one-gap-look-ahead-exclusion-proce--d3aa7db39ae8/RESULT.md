# Two-peak Gibbs transport in a one-gap look-ahead exclusion process

## Finding

**Theorem (a robust two-peak fundamental diagram).** Fix an integer jump length \(I\geq1\), a preferred empty headway \(k>I\), and a weight \(s>1\). For the conservative periodic exclusion process defined below, let \(J(\rho)\) denote the thermodynamic stationary signed current in its canonical Gibbs ensemble. There are choices of \(k,s\), for every \(I\geq1\), for which \(J(\rho)\) has at least two distinct strict local maxima separated by a local minimum, despite the Gibbs interaction favouring only one headway. More precisely, for every
\[
0<\theta<\log\!\left(1+\frac1I\right),
\]
all sufficiently large integers \(k>I\) with \(s=\exp(\theta k)\) yield at least two local maxima. This is a statement about the homogeneous Gibbs-ensemble fundamental diagram, not dynamical phase coexistence or open-boundary selection.

A fully exact finite-parameter witness is \(I=2\), \(k=7\), \(s=100\), with unit right-jump and zero left-jump rate. In this case the current has **exactly two** strict local maxima and exactly one intervening strict local minimum for \(0<\rho<1\). The fugacity locations are uniquely contained in, respectively,
\[
\left(\frac25,\frac12\right),\quad
\left(\frac12,\frac34\right),\quad
\left(\frac34,\frac{19}{20}\right).
\]
These are ordered in increasing fugacity; physical density decreases with fugacity. Numerical positions (not used in the proof) are approximately \(\rho=0.42988428\), \(0.20663085\), and \(0.11949132\), with corresponding currents \(0.14374495\), \(0.13252006\), and \(0.19404766\). The first and third points are maxima.

## Assumptions and scope

Consider a ring of \(L\) sites with \(N\) indistinguishable exclusion particles, with \(1\leq N<L\). In cyclic particle order define the *number of vacant sites* between consecutive particles as \(n_i\geq0\); hence \(\sum_i n_i=L-N\). For \(w(n)=s\) at \(n=k\) and \(w(n)=1\) otherwise, set
\[
u(n)=\begin{cases}w(n-I)/w(n),&n\geq I,\\0,&0\leq n<I.\end{cases}
\]
A particle jumps \(I\) sites to the right at rate \(r_+u(n_i)\) and to the left at rate \(r_-u(n_{i-1})\), where \(r_+>r_-\geq0\). All intermediate sites must be unoccupied. The unique preferred gap has energy gain \(\log s\); all permitted rates are finite and nonnegative. For \(I>1\) the finite Markov chain may be reducible, so *stationary* always means its explicitly specified Gibbs ensemble, not a unique stationary distribution from every initial state.

Write \(z\in(0,1)\), \(Z(z)=\sum_{n\geq0}w(n)z^n=(1-z)^{-1}+(s-1)z^k\), and
\[
m(z)=\frac{zZ'(z)}{Z(z)},\qquad \rho(z)=\frac1{1+m(z)}.\]
For any \(\rho\in(0,1)\), \(\rho(z)\) determines a unique \(z\). The thermodynamic stationary current is
\[
J(\rho(z))=I(r_+-r_-)\,\frac{z^I}{1+m(z)}.
\]

## Proof

**Stationarity and current.** In gap coordinates, a right jump transfers \(I\) vacant sites from the outgoing gap \(n_i\) to the preceding gap \(n_{i-1}\); the reverse direction transfers from \(n_{i-1}\) to \(n_i\). For fixed \(L,N\), the canonical weight of a cyclic gap tuple is proportional to \(\prod_i w(n_i)\), conditioned on its specified total. Since \(u(n)w(n)=w(n-I)\) for \(n\geq I\), each incoming weighted flux after a right jump cancels an outgoing weighted flux from the neighbouring gap when the fluxes are summed cyclically. The same holds for left jumps. Thus this canonical Gibbs weight is invariant separately under each direction.

At fixed density \(\rho\), the canonical one-gap marginal converges to \(\nu_z(n)=w(n)z^n/Z(z)\), with \(m(z)=(1-\rho)/\rho\). Indeed, this is conditioning an iid exponentially-tailed span-one law on its typical total; the local central-limit ratio tends to one. Summing the rates gives
\[
\mathbb E_{\nu_z}[u(n)]
=\frac1{Z(z)}\sum_{n\geq I}w(n-I)z^n=z^I.
\]
Each jump crosses \(I\) bonds, so translation invariance yields the asserted \(J=I(r_+-r_-)\rho z^I\). Moreover \(zm'(z)=\operatorname{Var}_{\nu_z}(n)>0\), and \(\rho\) decreases continuously from \(1\) to \(0\) as \(z\) increases from \(0\) to \(1\). Therefore the fugacity and density parametrizations have identical types and counts of local extrema.

**Two-peak family.** Write \(z_0=I/(I+1)\) and \(q=e^{-\theta}\), so \(z_0<q<1\). With \(s_k=e^{\theta k}\), the product \((s_k-1)z^k\) and all its first two derivatives tend to zero on compact subintervals of \((0,q)\). Therefore \(J_k(z)\to I(r_+-r_-)z^I(1-z)\) in \(C^1\) there. On any compact interval of \((q,1)\), the preferred gap term dominates both \(Z\) and \(Z+zZ'\), and
\[
(k+1)J_k(z)\longrightarrow I(r_+-r_-)z^I
\]
in \(C^1\). Choose \(0<a<z_0<b<q<c<1\). For all sufficiently large \(k\), the respective derivative signs at \(a,b,c\) are positive, negative, positive. Finally \(J_k(c)>0=J_k(1)\), so by the mean-value theorem \(J_k'\) is negative at some point in \((c,1)\). Continuity and real analyticity force three alternating interior critical regions and hence two strict local maxima with a local minimum between them.

**Exact three-critical-point certificate.** For \(I=2,k=7,s=100,r_+=1,r_-=0\), direct substitution gives
\[
J(z)=\frac{2z^2(1-z)[1+99z^7(1-z)]}{1+792z^7(1-z)^2},
\quad
J'(z)=\frac{2zP(z)}{[1+792z^7(1-z)^2]^2},
\]
where
\[
\begin{aligned}
P(z)={}&2-3z-3069z^7+10692z^8-12375z^9+4752z^{10}\\
&+156816z^{14}-627264z^{15}+940896z^{16}\\
&-627264z^{17}+156816z^{18}.
\end{aligned}
\]
The denominator is strictly positive on \((0,1)\). The integer polynomial \(Q(x)=(1+x)^{18}P(x/(1+x))\), which bijectively transforms \(0<z<1\) to \(x>0\), has coefficient signs in increasing powers of \(x\) of
\[
\underbrace{+\cdots+}_{9},\quad
\underbrace{-\cdots-}_{5},\quad
\underbrace{++}_{2},\quad
\underbrace{---}_{3}.
\]
Thus Descartes' rule permits at most three positive roots counted with multiplicity. Exact rational evaluation yields \(P(2/5)>0\), \(P(1/2)<0\), \(P(3/4)>0\), \(P(19/20)<0\). The intermediate-value theorem produces one root in each of the three disjoint stated intervals. Therefore there are exactly three simple critical points and their derivative signs are \(+,-,+,-\), proving the exact max–min–max classification. Since the signs are strict, the phenomenon persists for \(s\) in an open interval around \(100\).

## Verification

`verify_gap_flux.py` independently forms the integer numerator of the derivative using polynomial arithmetic, recomputes the transformed Descartes coefficients and their three sign changes, and checks all four critical sign evaluations using exact rational arithmetic. It additionally enumerates labelled canonical gap states for \(N=3,4\) and total hole counts \(7\) through \(12\), checking exact weighted inflow–outflow balance separately for each direction. Run `python3 verify_gap_flux.py`; the expected final line is `ALL_CHECKS_PASSED`. Finite tests support the transfer-rate identity but do not replace the proof for arbitrary \(N,L,I,k\).

## Relationship to prior work

Nhung, Ngoc and Thi's 2026 look-ahead exclusion work supplies a general Gibbs stationary-measure construction and a fugacity-parametrized current. It examines the location of the leading peak and inflection conditions, but does not establish two maxima for a single preferred-gap Gibbs interaction or the all-jump-length scaling family here. The present result builds on that current representation while proving a separate qualitative classification and furnishing an exact root-count certificate for a finite-range instance.

Multiple current–density maxima are *not* new in all lattice-gas or traffic models: Midha, Gomes, Kolomeisky and Gupta (2018) demonstrate two maxima under strong repulsive interactions for extended interacting particles, within a cluster mean-field framework, and earlier traffic literature shows double-peak fundamental diagrams. Those results use different rates and stationary structures and do not imply the displayed exact one-gap Gibbs law, nor the all-\(I\) construction. General zero-range partition-function methods provide the functional setting, not this multi-peak classification. This is not a claim that the general phenomenon was first discovered here.

## Limitations

The current is that of the canonical Gibbs measure, which may be a mixture of noncommunicating classes when \(I>1\); no universal long-time current from arbitrary initial conditions is asserted. The two maxima are local, not equal-height global optimizers. No hydrodynamic phase coexistence, metastability, open-reservoir selection, or fluctuations are proved. The scaling-family theorem gives existence for all sufficiently large \(k\), without a uniform explicit cutoff. The exact witness supplies a root count only for its stated parameters. A broader unindexed result may already cover the same preferred-gap family; publication-priority assessment remains open.

## References

1. L. T. Nhung, N. P. N. Ngoc, H. A. Thi, *Invariant measures of exclusion processes with a look-ahead rule*, arXiv:2604.01796v1 (first submitted 2026-04-02), https://arxiv.org/abs/2604.01796 .
2. T. Midha, L. V. F. Gomes, A. B. Kolomeisky, A. K. Gupta, *Theoretical investigations of asymmetric simple exclusion processes for interacting oligomers*, Journal of Statistical Mechanics (2018) 053209, https://doi.org/10.1088/1742-5468/aac139 .
3. M. Kanai, *Exact solution of the zero-range process: fundamental diagram of the corresponding exclusion process*, arXiv:cond-mat/0701190, https://arxiv.org/abs/cond-mat/0701190 .
4. J. S. Hager, *Extremal principle for the steady-state selection in driven lattice gases with open boundaries* (2001), https://www.researchgate.net/publication/11925471 .
