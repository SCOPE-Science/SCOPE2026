# Stage-parity classification of Gauss–Legendre positivity on complete multipartite heat graphs

## Finding

Consider the unweighted combinatorial heat equation on an arbitrary connected complete multipartite graph. For every integer stage number \(s\ge1\), all *off-diagonal* entries of the \(s\)-stage Gauss–Legendre collocation end-step are strictly positive for every positive step size. Its *entire* end-step matrix is entrywise nonnegative for every step size if and only if \(s\) is even or the graph consists of two vertices. For odd \(s\), every graph with at least three vertices has negative end-step diagonal entries at all sufficiently large steps. Thus the all-steps positivity classification depends only on stage parity and the two-vertex exception, not on the sizes of the multipartite classes.

This is a statement about the one-step endpoint matrix, not positivity of internal Runge–Kutta stages or a generic Markov generator.

## Assumptions and scope

Let \(p\ge2\), \(a_1,\ldots,a_p\) be positive integers, and \(N=\sum_{i=1}^{p}a_i\ge2\). Let \(G=K_{a_1,\ldots,a_p}\) be the simple unweighted complete multipartite graph, with graph Laplacian \(L=D-A\). Consider \(u'(t)=-Lu(t)\). The one-step matrix for \(s\)-stage Gauss–Legendre collocation at step \(h\ge0\) is \(T_s(h)=r_s(hL)\), where

\[
Q_s(z)=\sum_{j=0}^{s}\frac{s!(2s-j)!}{(2s)!(s-j)!j!}z^j,
\qquad r_s(z)=\frac{Q_s(-z)}{Q_s(z)}.
\]

The denominator is strictly positive for real \(z\ge0\), so this defines \(T_s(h)\) without ambiguity. Set \(f_s(z)=(1-r_s(z))/z\) for \(z>0\), with \(f_s(0)=1\). When the vertices \(x\) and \(y\) belong to different parts, and when they are different vertices of the same part \(i\), respectively, the entries satisfy

\[
(T_s(h))_{xy}=h f_s(Nh),
\]

\[
(T_s(h))_{xy}=\frac{(N-a_i)h}{a_i}\bigl[f_s((N-a_i)h)-f_s(Nh)\bigr].
\]

These entries are strictly positive whenever \(h>0\). The diagonal entry at a vertex of part \(i\), with \(b_i=N-a_i\), equals

\[
(T_s(h))_{xx}=\frac1N+\left(\frac1{a_i}-\frac1N\right)r_s(Nh)+\left(1-\frac1{a_i}\right)r_s(b_i h).
\]

For even \(s\), all diagonal entries are strictly positive for \(h\ge0\). For odd \(s\), \(T_s(h)\to 2\mathbf 1\mathbf 1^{\mathsf T}/N-I\) as \(h\to\infty\); hence each diagonal tends to \(2/N-1\), which is negative precisely when \(N\ge3\). For \(N=2\) the end-step is entrywise nonnegative for every integer \(s\ge1\) and every \(h\ge0\). In every case \(T_s(h)\mathbf 1=\mathbf 1\).

## Proof

**1. Scalar monotonicity.** Write \(u=z^2\) and split the positive-coefficient polynomial into its even and odd parts:

\[
Q_s(z)=E_s(u)+zO_s(u),\quad
E_s(u)=\sum_j q_{2j}u^j,\quad O_s(u)=\sum_j q_{2j+1}u^j,
\]

where \(q_j=s!(2s-j)!/((2s)!(s-j)!j!)\), and indices range over the available coefficients. Since \(O_s(u)>0\) for \(u\ge0\), direct subtraction yields

\[
f_s(z)=\frac{2}{z+E_s(z^2)/O_s(z^2)}.
\]

The quotient \(E_s/O_s\) is nondecreasing on \([0,\infty)\). To verify this without an unstated monotonicity assumption, let \(e_j=q_{2j}\), \(o_j=q_{2j+1}\), and observe, wherever both occur, that

\[
\frac{o_j}{e_j}=\frac{s-2j}{(2s-2j)(2j+1)}.
\]

For consecutive valid indices this ratio strictly decreases: the numerator factor \((s-2j)/(2s-2j)\) is nonincreasing (strict if \(s>0\)) and \(1/(2j+1)\) strictly decreases. The coefficient of \(u^{k}\) in \(E_s'O_s-E_sO_s'\) is the sum of \((i-j)e_i o_j\) over pairs with \(i+j=k+1\). Pairing \((i,j)\) with \((j,i)\), each term with \(i>j\) contributes \((i-j)(e_i o_j-e_j o_i)\ge0\). For even \(s\), the one extra highest even coefficient contributes only positive unpaired terms. Thus \(E_s'O_s-E_sO_s'\) has nonnegative coefficients, proving nondecreasing \(E_s/O_s\). Because \(z\) itself increases strictly, \(f_s\) strictly decreases on \([0,\infty)\) and is strictly positive. In particular \(r_s(z)<1\) for \(z>0\).

**2. Parity of the Padé numerator.** Let \(F(t)=t^s(1-t)^s\). Repeated integration by parts \(2s+1\) times, using that \(F\) and its first \(s-1\) derivatives vanish at both endpoints, and the explicit coefficients above, gives the exact real-axis identity

\[
e^{-z}Q_s(z)-Q_s(-z)=\frac{(-1)^{s+1}z^{2s+1}}{(2s)!}\int_0^1 e^{-zt}t^s(1-t)^s\,dt,
\qquad z\ge0.
\]

For completeness, in that integration-by-parts computation \(F^{(k)}(0)=k!(-1)^{k-s}\binom{s}{k-s}\) for \(s\le k\le2s\), and \(F^{(k)}(1)=(-1)^kF^{(k)}(0)\). These endpoint values reproduce exactly the coefficients of \(Q_s\) and establish the displayed identity. If \(s\) is even then \(Q_s(-z)=e^{-z}Q_s(z)+z^{2s+1}(2s)!^{-1}\int_0^1e^{-zt}F(t)\,dt>0\). Consequently \(0<r_s(z)<1\) for \(z>0\). For odd \(s\), the leading terms instead give \(r_s(z)\to-1\) as \(z\to\infty\). For all \(s\), the even/odd decomposition gives \(Q_s(z)>|Q_s(-z)|\) at \(z>0\), and hence \(-1<r_s(z)<1\).

**3. Spectral resolution.** Write \(J_m\) for the all-ones \(m\)-square matrix. The orthogonal spectral projectors of \(L\), with coincident eigenvalues combined where necessary, are built from

\[
P_0=\frac{J_N}{N},\quad
P_N=\operatorname{diag}(J_{a_i}/a_i)-\frac{J_N}{N},\quad
P_{b_i}=I_{a_i}-J_{a_i}/a_i,\qquad b_i=N-a_i.
\]

Here each \(P_{b_i}\) is supported on its part and may vanish when \(a_i=1\). Directly, \(LP_0=0\), \(LP_N=NP_N\), and \(LP_{b_i}=b_iP_{b_i}\); the projectors are mutually orthogonal and sum to the identity. Applying \(r_s(h\cdot)\) therefore gives

\[
T_s(h)=P_0+r_s(Nh)P_N+\sum_{i=1}^p r_s(b_ih)P_{b_i}.
\]

Taking matrix entries yields the three formulas in the scope section. For different parts, strict positivity follows from \(f_s>0\). For distinct vertices in one part, it follows from \(0<b_i<N\) and strict decrease of \(f_s\). For an even number of stages, the diagonal formula is a nonnegative weighted combination of the positive numbers \(1,r_s(Nh),r_s(b_ih)\), since \(1/a_i-1/N\ge0\). For an odd number of stages, all nonzero eigenvalue multipliers tend to \(-1\), yielding \(T_s(h)\to2P_0-I\). This forces negative diagonals for sufficiently large \(h\) when \(N\ge3\).

If \(N=2\), necessarily \(G=K_{1,1}\), and

\[
T_s(h)=\frac12\begin{pmatrix}1+r_s(2h)&1-r_s(2h)\\1-r_s(2h)&1+r_s(2h)\end{pmatrix},
\]

which is nonnegative because \(-1<r_s(2h)<1\) for \(h>0\), and equals the identity at \(h=0\). The constant vector lies in the zero eigenspace, so row sums are one. This proves all assertions.

## Verification

The included standalone \(\texttt{verify\_gauss\_multipartite.py}\) uses exact rational and symbolic arithmetic. It checks coefficientwise monotonicity certificates and the Padé Taylor matching for stages \(1\) through \(28\), exact functional-calculus identities for seven nonisomorphic multipartite part configurations and stages \(1\) through \(6\) at three rational steps, and the parity boundaries including the two-vertex exception. The recorded output reports 741 exact assertions passed. These finite checks support, but do not replace, the all-stage proof above. Run \(\texttt{python verify\_gauss\_multipartite.py}\) with SymPy installed.

## Relationship to prior work

The Gauss collocation stability functions as diagonal Padé approximants are standard; Banjai and Ferrari (2022, arXiv:2212.07170) give a modern primary treatment of Gauss stability functions, but their convolution-quadrature analysis does not assert endpoint stochastic positivity on multipartite heat graphs. Zappavigna and coauthors (2012) prove general positive-system limitations for Padé approximations and step-size restrictions under different assumptions, but do not provide this graph-family all-stage classification. Gottlieb and coauthors (2021) construct alternative high-order positivity-preserving time integrators.

Relevant earlier specialized results give the positivity horizon of explicit classical RK4 on every complete multipartite graph, and the two-stage Gauss–Legendre positivity behavior on selected cycle and strongly regular graphs. Those findings neither imply unconditional positivity for *all even stage numbers* on arbitrary unbalanced multipartite graphs, nor the all-stage odd/even classification. In particular this result does not claim priority for the two-stage balanced complete multipartite special cases.

## Limitations

The graph must be connected, simple, unweighted, undirected, and complete multipartite. The claim covers endpoint entrywise positivity and mass conservation, not positivity of internal Gauss stage values, unconditional positivity on arbitrary graphs or continuous-time-generator families, monotone energy decay, or time-step accuracy. Odd stages with at least three vertices may have nonnegative matrices on some bounded step ranges; the theorem asserts only eventual diagonal negativity, not an exact finite threshold. The cited comparison is a best-knowledge originality assessment; additional specialist treatments may exist.

## References

1. L. Banjai and M. Ferrari, *Runge–Kutta convolution quadrature based on Gauss methods*, first posted 2022-12-14, arXiv:2212.07170, https://arxiv.org/abs/2212.07170.
2. A. Zappavigna, P. Colaneri, S. Kirkland, and R. Shorten, *Essentially Negative News About Positive Systems*, Linear Algebra and its Applications (2012), https://doi.org/10.1016/j.laa.2011.12.021. Open manuscript: https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf.
3. A 2021 study of high-order positivity-preserving time discretizations, arXiv:2102.11939, https://arxiv.org/abs/2102.11939.
