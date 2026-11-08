# A sharp mobility boundary for hotspot spacing in cyclic epidemic networks

## Finding

For every integer \(n\ge5\), consider a symmetric bidirectional movement network on the cycle \(C_n\): a resident stays at its own vertex with fraction \(1-2h\) and visits either neighbor with fraction \(h\), where \(0<h\le1/2\). All patches have equal population size and recovery rate \(\gamma>0\). The transmission rates are \(\beta+\delta\) at two distinct vertices at circular distance \(d\in\{1,\ldots,\lfloor n/2\rfloor\}\), and \(\beta\) elsewhere, with \(\beta,\delta>0\).

Let \(\mathcal R_d(h)\) be the basic reproduction number in the symmetric SIR-network model of Das and Stolerman [1]. Then:

1. **Sharp universal low-mobility ordering.** For every \(0<h<2/5\), every \(n\ge5\), and all \(\beta,\delta,\gamma>0\),
   \[
   \mathcal R_1(h)>\mathcal R_2(h)>\cdots>\mathcal R_{\lfloor n/2\rfloor}(h).
   \]
2. **Exact reversal on the five-cycle.** When \(n=5\),
   \[
   \begin{cases}
   \mathcal R_1(h)>\mathcal R_2(h),&0<h<2/5,\\
   \mathcal R_1(h)=\mathcal R_2(h),&h=2/5,\\
   \mathcal R_1(h)<\mathcal R_2(h),&2/5<h\le1/2.
   \end{cases}
   \]
   The reversal holds **for every** positive background transmission rate and positive common hotspot increment, not merely for weak hotspots.
3. **Complete spatial erasure at the boundary.** On \(C_5\), at \(h=2/5\), the reproduction number is unchanged by **any permutation** of an arbitrary positive vector of five transmission rates. Specifically, if \(\beta_0,\ldots,\beta_4>0\), the largest eigenvalue \(\lambda\) of the next-generation numerator is the unique solution above \(\max_i\beta_i/5\) of
   \[
   1=\frac4{25}\sum_{i=0}^{4}\frac{\beta_i}{\lambda-\beta_i/5},
   \qquad \mathcal R_0=\lambda/\gamma.
   \]

The constant \(2/5\) in the first assertion is sharp **uniformly across cycle sizes**, since \(C_5\) reverses the ordering for every larger admissible mobility fraction.

For a quantitative invasion reversal set \(\beta=4/5\), \(\gamma=1\), and \(\delta=9/20\) on \(C_5\). At \(h=1/4\), neighboring hotspots have \(\mathcal R_1>1\) while distance-two hotspots have \(\mathcal R_2<1\); at \(h=9/20\), the same rates yield \(\mathcal R_1<1<\mathcal R_2\). These are statements about local invasion of a disease-free equilibrium, **not** indefinite endemic persistence in a closed SIR model.

## Assumptions and scope

Index vertices modulo \(n\). Let \(P=P_{n,h}\) be the symmetric stochastic movement matrix defined by \(P_{ii}=1-2h\), \(P_{i,i\pm1}=h\), and all other entries zero. For \(n\ge5\), these positions are distinct. For a positive rate vector \(\boldsymbol\beta\), define
\[
K=P\operatorname{diag}(\boldsymbol\beta)P,\qquad \mathcal R_0=\rho(K)/\gamma.
\]
This is the next-generation matrix of [1, Eq. (4)] with equal patch populations, symmetric flux and common recovery. The two-hotspot case means \(\boldsymbol\beta_i=\beta+\delta\) at vertices \(0,d\) and \(\beta\) elsewhere. There are no assertions about unequal patch populations, asymmetric movement, negative rates, stochastic transmission, outbreak size, or nonlinear epidemic peak times.

## Proof

**Step 1 (a two-dimensional secular equation).** Put \(Q=P^2\), \(u_j=Pe_j\), and \(T=\beta Q\). Then
\[
K_d=T+\delta u_0u_0^{\mathsf T}+\delta u_du_d^{\mathsf T}.
\]
The matrix \(K_d\) is nonnegative and symmetric; its Rayleigh quotient on the constant vector is \(\beta+2\delta/n\), so its top eigenvalue \(\lambda_d\) exceeds \(\beta=\rho(T)\). For \(\lambda>\beta\) define
\[
g_j(\lambda)=e_0^{\mathsf T}Q(\lambda I-\beta Q)^{-1}e_j.
\]
The rank-two determinant identity reduces the characteristic equation above \(\beta\) to the two eigenvalues \(g_0(\lambda)\pm g_d(\lambda)\) of the perturbation resolvent. Since \(Q\ge0\) entrywise, the Neumann expansion gives \(g_d(\lambda)>0\) for every \(d\) in the stated domain (the necessary positive paths exist); therefore \(g_0+g_d\) is the larger branch. It is positive, strictly decreasing in \(\lambda\) (it equals half a positive quadratic resolvent form), diverges as \(\lambda\downarrow\beta\), and tends to zero at infinity. Consequently \(\lambda_d\) is its **unique** root
\[
1=\delta\bigl(g_0(\lambda_d)+g_d(\lambda_d)\bigr).
\tag{1}
\]
Thus an ordering of \(g_d(\lambda)\) for every \(\lambda>\beta\) yields the identical ordering of \(\lambda_d\).

**Step 2 (cyclic unimodality).** Set \(a=1-2h\). The first row \(q\) of \(Q\) has
\[
q_0=a^2+2h^2,\quad q_{\pm1}=2ah,\quad q_{\pm2}=h^2,
\]
with all other entries zero (coincident labels already counted modulo \(n\)). For \(0<h<2/5\),
\[
q_0-q_1=1-6h+10h^2>0,\qquad q_1-q_2=h(2-5h)>0.
\]
In particular, \(q\) is symmetric and strictly radially decreasing on its support. The convolution of two nonnegative, symmetric, radially nonincreasing functions on the cyclic group is again symmetric and radially nonincreasing. For completeness, write either function as a nonnegative linear combination of centered cyclic balls \(B_r=\{j:\min(j,n-j)\le r\}\). For \(r<\lfloor n/2\rfloor\) and radially decreasing \(f\), direct cancellation yields
\[
(\mathbf1_{B_r}*f)(j)-(\mathbf1_{B_r}*f)(j+1)
=f(j-r)-f(j+r+1)\ge0
\]
for \(0\le j<\lfloor n/2\rfloor\), since the circular distance of \(j-r\) does not exceed that of \(j+r+1\). The largest ball is the whole group and gives a constant convolution. This proves closure under convolution.

Strictness for every consecutive radius follows from the positive coefficient \(q_1-q_2\) of \(\mathbf1_{B_1}\) in the ball decomposition of \(q\). For every \(1\le j<\lfloor n/2\rfloor\), the \(j\)-fold convolution \(\mathbf1_{B_1}^{*j}\) has a positive coefficient at displacement \(j\) and zero at displacement \(j+1\) (no walk of \(j\) steps of size at most one reaches \(j+1\) on the cycle). All other convolution terms have nonincreasing radial coefficients. Hence \(q^{*j}(j)>q^{*j}(j+1)\); the \(j=0\) comparison follows from \(q_0>q_1\).

The resolvent expansion
\[
g_j(\lambda)=\sum_{k=0}^{\infty}\frac{\beta^k}{\lambda^{k+1}}(Q^{k+1})_{0j}
\]
has strictly positive coefficients. The preceding comparisons therefore imply
\(g_0(\lambda)>g_1(\lambda)>\cdots>g_{\lfloor n/2\rfloor}(\lambda)\), for every \(\lambda>\beta\). Equation (1) proves assertion 1.

**Step 3 (exact five-cycle reversal).** For \(n=5\), the nontrivial Fourier multipliers of \(P\) are, each with multiplicity two,
\[
p_1=1-\frac{5-\sqrt5}{2}h,\qquad
p_2=1-\frac{5+\sqrt5}{2}h.
\]
Fourier inversion of the resolvent in Step 1 gives the **exact identity**
\[
g_1(\lambda)-g_2(\lambda)
=\frac{h(2-5h)\lambda}{(\lambda-\beta p_1^2)(\lambda-\beta p_2^2)}.
\tag{2}
\]
The denominator is strictly positive for \(\lambda>\beta\), since \(|p_1|,|p_2|\le1\). Hence the difference has the sign of \(2-5h\). Applying equation (1) proves assertion 2, including equality at the boundary.

**Step 4 (all-rate permutation invariance).** Direct multiplication at \(h=2/5\), \(n=5\) gives
\[
P^2=\frac15 I+\frac4{25}\mathbf1\mathbf1^{\mathsf T}.
\tag{3}
\]
For \(D=\operatorname{diag}(\boldsymbol\beta)\), the matrices \(PDP=(PD^{1/2})(PD^{1/2})^{\mathsf T}\) and \(D^{1/2}P^2D^{1/2}=(PD^{1/2})^{\mathsf T}(PD^{1/2})\) have identical eigenvalues. Equation (3) turns the latter into
\(D/5+(4/25)\boldsymbol\beta^{1/2}(\boldsymbol\beta^{1/2})^{\mathsf T}\), which is conjugated by a permutation matrix whenever the rates are permuted. Its rank-one secular equation is the stated all-rate formula. This proves assertion 3. Conversely, if \(h\ne2/5\) in the positive admissible interval, equation (2) shows that some two-hotspot placement changes the top eigenvalue under a permutation, so this all-rate spatial invariance is unique.

**Step 5 (exact local-invasion witness).** If \(0<\beta<\gamma\), the eigenvalue crosses \(\gamma\) as \(\delta\) grows at the unique value
\[
\delta_d^{\mathrm{crit}}=\frac{1}{g_0(\gamma)+g_d(\gamma)}.
\]
For \(n=5\), \(\beta=4/5\), \(\gamma=1\), the pair of critical values at distances \(1,2\) is, respectively,
\[
\begin{array}{c|cc}
h&\delta_1^{\mathrm{crit}}&\delta_2^{\mathrm{crit}}\\\hline
1/4&348/815&348/715\\
2/5&7/15&7/15\\
9/20&24244/51605&24244/56105
\end{array}
\]
Every entry is obtained by rational inversion of \(I-(4/5)P^2\). The rational increment \(9/20\) lies between the two thresholds in opposite orders at the first and last mobility values, completing the witness.

## Verification

The enclosed `verify.py` uses only Python's standard library. It performs exact-rational tests of cyclic ball convolution closure, the movement-square entries, radial resolvent inequalities for multiple cycle sizes and mobility fractions, identity (2), the exact flattening (3), and all rational threshold values and strict comparisons in the witness. Run `python3 verify.py`; no external data or dependencies are required. The finite checks corroborate but do not replace the proof for arbitrary \(n\) and continuous parameters.

## Relationship to prior work

Das and Stolerman [1] derive the SIR-network next-generation formula for symmetric movement and analyze several network topologies with exactly one heterogeneous transmission vertex. The result here holds for two equal hotspots on every cycle, establishes a sharp distance-order transition, and identifies full arbitrary-rate permutation invariance at a particular five-cycle mobility. Altenberg [2] develops general spectral-radius comparisons for commuting mobility matrices under changes to a mixing parameter; the results inspected there do not fix two hotspot sites and compare their spatial separation, or state the five-cycle reversal. Discrete rearrangement methods [3] motivate the low-mobility monotonic side but do not give the high-mobility sign change for this squared movement kernel. The ordinary finite-group convolution lemma is not claimed as new.

## Limitations

All patch populations are equal, movement is symmetric, and recovery is homogeneous. The hotspot comparison assumes two equal **positive** increments above a positive common background; it does not compare arbitrary unequal hotspots for all cycle sizes. The universal monotonicity is asserted only for \(h<2/5\); the exact reverse ordering is proved on the five-cycle, not on all larger cycles. The equality at the boundary concerns \(C_5\); larger cycles need not have full permutation invariance. The epidemic threshold is a linear invasion criterion, not a statement that a closed SIR model sustains an endemic state. Claims of publication priority are subject to possible unindexed or not-fully-accessible equivalents.

## References

[1] H. K. Das and L. M. Stolerman, *Epidemic thresholds and disease dynamics in metapopulations: the role of network geometry and human mobility*, arXiv:2308.01998, first posted 2023-08-03. Journal version: *Epidemic Thresholds and Disease Dynamics in Metapopulations: The Role of Network Structure and Human Mobility*, SIAM Journal on Applied Dynamical Systems, DOI 10.1137/23M1579522. https://arxiv.org/abs/2308.01998

[2] L. Altenberg, *On the Ordering of Spectral Radius Product r(A) r(AD) Versus r(A^2 D) and Related Applications*, arXiv:1301.4969 (2013). https://arxiv.org/abs/1301.4969

[3] H. Hajaiej, F. Han and B. Hua, *Discrete Schwarz rearrangement in lattice graphs*, arXiv:2209.01003 (2022). https://arxiv.org/abs/2209.01003
