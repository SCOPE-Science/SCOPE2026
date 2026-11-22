# The sharp eight-vertex onset of interior geometric-reset splitting optima

## Finding

Consider a discrete nearest-neighbour birth–death chain on the vertices \(\{0,1,\ldots,a\}\), with absorbing endpoints \(0,a\) and strictly positive interior jump probabilities \(p_i\) to the right and \(q_i=1-p_i\) to the left. It starts at \(z\in\{1,\ldots,a-1\}\). Between independent attempts it is restarted at \(z\) according to the geometric survival weights \(w_n=s^{n-1}\), \(0<s\le1\). Let \(Q_{a,z}(s)\) be the eventual probability of absorption at \(0\).

**Sharp minimality.** For every such chain with \(a\le6\), and every initial vertex, \(Q_{a,z}(s)\) is monotone or constant on \((0,1]\). The smallest chain admitting a strict interior reset-rate optimum therefore has eight vertices (\(a=7\)), and this lower bound is attained.

**Complete first-case criterion.** For \(a=7,z=3\), put
\[
b=p_1q_2,\qquad A=p_4q_5+p_5q_6,\qquad C=\frac{q_1q_2q_3}{p_3p_4p_5p_6}.
\]
Then \(0<A,b<1\), \(C>0\), and
\[
\frac{Q_{7,3}(s)}{1-Q_{7,3}(s)}=\frac{C}{s}\,\frac{1-As^2}{1-bs^2}.
\]
A unique strict interior minimum occurs **if and only if**
\[
\boxed{\quad b>\frac{1+A}{3-A}.\quad}
\]
Otherwise \(Q_{7,3}\) is strictly decreasing in \(s\in(0,1)\). When the criterion holds, the optimizer is
\[
s_*=\sqrt{\frac{3b-A-\sqrt{(3b-A)^2-4Ab}}{2Ab}}\in(0,1).
\]
At the reflected site \(z=4\), the corresponding reflected environment has a unique strict *maximum* rather than a minimum.

One exact witness is \(p_1=4/5\), \(p_2=1/5\), and \(p_3=p_4=p_5=p_6=1/2\), giving
\[
Q_{7,3}(s)=\frac{16(2-s^2)}{32+25s-16s^2-16s^3},\qquad
s_*=\sqrt{\frac{71-\sqrt{1841}}{32}}\approx0.9369685843.
\]
Its optimal lower-exit probability is about \(0.6362752323\), smaller than the no-reset value \(Q_{7,3}(1)=16/25\).

## Assumptions and scope

The underlying chain makes a left or right step at each nonabsorbed time, with no holding and arbitrary site-dependent \(p_i\in(0,1)\). A reset clock is independent of the path; absorption after \(n\) steps survives a cycle with probability proportional to \(s^{n-1}\). Unsuccessful cycles regenerate independently at the same \(z\). The value \(s=1\) means no resetting, and smaller \(s\) means more frequent resetting. All assertions concern the two *splitting probabilities*, not mean absorption time, and arbitrary site inhomogeneity is allowed.

## Proof

**1. Discounted exit odds.** Write \(P\) for the substochastic transition matrix on the transient sites \(\{1,\ldots,a-1\}\). For \(1\le u\le v\le a-1\), let \(D_{u:v}(s)=\det(I-sP_{[u,v]})\), and set \(D_{u:v}=1\) for an empty interval. Let \(F_0(s)=\mathbb E_z[s^T\mathbf1_{\{J=0\}}]\), and similarly \(F_a(s)\) for exit at \(a\). Tridiagonal inversion, or solving the two discounted harmonic equations by continuants, gives exactly
\[
F_0(s)=\frac{s^z(\prod_{i=1}^{z}q_i)D_{z+1:a-1}(s)}{D_{1:a-1}(s)},\qquad
F_a(s)=\frac{s^{a-z}(\prod_{i=z}^{a-1}p_i)D_{1:z-1}(s)}{D_{1:a-1}(s)}.
\]
The renewal decomposition yields \(Q=F_0/(F_0+F_a)\), because a reset cycle exits on either side or restarts. Hence the exact odds identity
\[
\frac{Q_{a,z}(s)}{1-Q_{a,z}(s)}
=\frac{\prod_{i=1}^zq_i}{\prod_{i=z}^{a-1}p_i}\,
 s^{2z-a}\frac{D_{z+1:a-1}(s)}{D_{1:z-1}(s)}.\tag{1}
\]
Multiplying both discounted transforms by the common factor \(1/s\) recovers the stated reset-clock convention.

**2. Positivity and determinant monotonicity.** Each nonempty killed interval matrix \(P_{[u,v]}\) is similar, by strictly positive diagonal scaling, to a real symmetric tridiagonal matrix with zero diagonal. Its eigenvalues lie strictly inside \((-1,1)\): the substochastic chain on that interval has a positive probability of absorption within a bounded number of steps from every site. Bipartiteness pairs eigenvalues \(\pm\lambda_j\); zero eigenvalues are harmless. Consequently
\[
D_{u:v}(s)=\prod_{\lambda_j>0}(1-\lambda_j^2s^2)>0,
\]
and this determinant is nonincreasing for \(0\le s\le1\), strictly decreasing for intervals with two or more vertices. A one-vertex or empty determinant equals one.

**3. Global short-chain exclusion.** Reflection exchanges \(z\) with \(a-z\) and replaces \(Q\) by \(1-Q\), so assume \(z\le a/2\). If \(a\le6\) and \(z<a/2\), necessarily \(z\le2\), whence \(D_{1:z-1}=1\), and \(2z-a<0\). Both the power \(s^{2z-a}\) and \(D_{z+1:a-1}\) are positive nonincreasing, so (1), and therefore \(Q\), is strictly decreasing. If \(z=a/2\), \(a\) is even: for \(a=2,4\), numerator and denominator continuants are both one and the odds are constant. For \(a=6,z=3\), each is a two-vertex determinant, so the odds have the form \(C(1-\alpha s^2)/(1-\beta s^2)\) with \(\alpha,\beta\in(0,1)\), whose derivative has one fixed sign (possibly zero). This covers every \(a\le6\) and proves sharp minimality once the witness below is established.

**4. Classification of the first possible interior extremum.** At \(a=7,z=1,2\), the same power/determinant argument excludes interior extrema; \(z=5,6\) follow by reflection. At \(z=3\), the left and right continuants have lengths two and three, respectively, so
\[
D_{1:2}(s)=1-p_1q_2s^2=1-bs^2,
\qquad
D_{4:6}(s)=1-(p_4q_5+p_5q_6)s^2=1-As^2.
\]
This establishes the stated odds. Its derivative has the sign of
\[
N(s^2)=-1+(3b-A)s^2-Ab s^4.
\]
More usefully, for \(t=s^2\in[0,1]\),
\[
N(t)=-(1-bt)^2+(b-A)t(1+bt).\tag{2}
\]
If \(b\le A\), (2) is strictly negative. If \(b>A\), then \(N'(t)=3b-A-2Abt\ge b(3-2A)-A>0\) throughout \([0,1]\), while \(N(0)=-1\). Thus there is exactly one zero in \((0,1)\) if and only if \(N(1)>0\), equivalently \(b>(1+A)/(3-A)\). The sign changes from negative to positive, giving a strict minimum; if \(N(1)\le0\), the response is strictly decreasing on the open interval. The quadratic formula gives the stated \(s_*\); positivity of \(A,b\) rules out a degenerate denominator.

**5. Rational witness.** The displayed probabilities give \(b=16/25\) and \(A=1/2\), satisfying \(b>3/5\). Direct substitution into the odds formula gives the rational expression above. Its derivative numerator has the sign opposite to \(16s^4-71s^2+50\), whose unique zero in \((0,1)\) has the claimed radical form. Reflection yields a strict interior maximum for the opposite exit-side observable. This completes the proof.

## Verification

Run `python verify.py` with SymPy installed. The script independently inverts finite discounted transition matrices, verifies the rational witness and derivative, checks continuant odds over a rational sample of all smaller path sizes and starts, and exercises the sharp threshold on a rational parameter grid. At packaging it passed 801 exact symbolic/rational assertions. These checks are supplementary: the universal statement, strictness, and necessity/sufficiency are proved analytically above, not inferred from a grid.

## Relationship to prior work

Newton and Vega Coso's *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting* supplies the renewal identity, a broad stochastic-order comparison framework, spatial switching of exact-time exit ratios, and an explicit temporally multiply switching birth–death example. Its concluding open problem asks which birth–death chains develop interior reset-intensity extrema. It does not state the eight-vertex sharp minimality or this first-case parameter criterion. Vega Coso's earlier *Critical Spectral Invariants in Random Walks with Geometric Resetting* treats the spatially homogeneous biased walk, for which no such inhomogeneous eight-vertex threshold is developed. The new analysis isolates and solves the first nontrivial finite path size within the unresolved general classification, using classical continuant methods rather than claiming the renewal formula as new.

## Limitations

The classification of all environments is complete only for \(a\le6\) and the first critical case \(a=7\); for \(a\ge8\), multiple extrema or more complicated phase diagrams are not ruled out. It requires strictly positive nearest-neighbour rates, discrete geometric resetting to the original site, and absorption taking precedence over reset; state-dependent reset, holding transitions and non-geometric clocks are outside its scope. Historical priority beyond the inspected accessible sources is not certified, and independent mathematical assessment has not been performed.

## References

1. T. Newton and J. A. Vega Coso, *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting*, arXiv:2611.01756v1 (first public 2026-11-01), https://arxiv.org/html/2611.01756v1 . Relevant material: sections 2, 7, 10.3 and appendices.
2. J. A. Vega Coso, *Critical Spectral Invariants in Random Walks with Geometric Resetting*, arXiv:2603.24803v1 (2026), https://arxiv.org/html/2603.24803v1 . Relevant material: sections II–IV and conclusions.
3. M. Radice, *Non-homogeneous random walks with stochastic resetting: an application to the Gillis model*, arXiv:2208.10220 (2022), https://arxiv.org/abs/2208.10220 . Related one-target reset first-passage laws, not a two-boundary sharp-size criterion.
