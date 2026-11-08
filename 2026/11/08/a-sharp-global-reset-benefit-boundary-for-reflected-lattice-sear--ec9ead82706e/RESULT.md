# A sharp global reset-benefit boundary for reflected lattice searches

## Finding

Let \(n\ge1\) and \(1\le k\le n\) be integers. Consider a discrete-time nearest-neighbor walk on \(\{0,1,\ldots,n\}\), started at \(k\), absorbed upon first reaching \(0\), moving to either neighbor with probability \(1/2\) at every interior vertex, and moving deterministically from \(n\) to \(n-1\) in one step. Independently at each step, with probability \(r\in[0,1)\) replace that move by a one-step reset to \(k\); a reset consumes one unit of time and never hits the target. Write \(H_{n,k}(r)\) for the mean time to absorption, and let \(a=n-k\).

**Theorem (complete global reset-benefit classification).** One has
\[
H_{n,k}(0)=n^2-a^2,
\qquad
H_{n,k}(r)=\frac{1}{r}\left[\frac{T_n(1/(1-r))}{T_a(1/(1-r))}-1\right]\quad(0<r<1),
\]
where \(T_j\) denotes the Chebyshev polynomial of the first kind. Moreover,
\[
\boxed{\ (\exists r\in(0,1):H_{n,k}(r)<H_{n,k}(0))
\quad\Longleftrightarrow\quad 5(n-k)^2>n^2+5.\ }
\]
When \(5(n-k)^2\le n^2+5\), *every* nonzero resetting probability strictly increases the mean time. When \(5(n-k)^2>n^2+5\), all sufficiently small positive resetting probabilities strictly decrease the mean time, and the mean attains a minimum at some interior \(r\in(0,1)\).

The boundary is an exact integer-lattice correction to the limiting critical relative starting position \(k/n=1-1/\sqrt5\). For example, at \((n,k)=(3,1)\), the no-reset mean is \(5\), whereas reset probability \(1/20\) gives the exact mean \(39980/8341<5\). In contrast, at \((n,k)=(5,3)\), every positive reset probability is detrimental.

## Assumptions and scope

The target is the left endpoint \(0\), and \(n\) is a *forced-inward* reflecting endpoint, not a self-looping or holding boundary. For each choice of \((n,k,r)\), resets occur independently, with fixed probability at every integer time, before an ordinary step; when a reset occurs the particle is placed at its initial non-target vertex \(k\). A reset is counted as one step. The absorbing target is reached only through an ordinary walk step. Both the time count and this endpoint convention are essential for the exact integer constant \(5\).

All assertions hold for every integer \(n\ge1\), every integer \(k\in\{1,\ldots,n\}\), and every indicated \(r\). No statement about optimizing other resetting laws, unknown boundaries, or simultaneous multiple walkers is intended.

## Proof

**1. Unreset first-passage transform.** Let \(\tau\) be the first hitting time of \(0\) of the *unreset* chain. For \(z\in(0,1]\), put \(f_j(z)=\mathbb E_j[z^\tau]\). The first-step equations are \(f_0(z)=1\), \(f_j(z)=z(f_{j-1}(z)+f_{j+1}(z))/2\) for \(1\le j<n\), and \(f_n(z)=zf_{n-1}(z)\). If \(\theta\ge0\) satisfies \(\cosh\theta=1/z\), their unique solution is
\[
f_j(z)=\frac{\cosh((n-j)\theta)}{\cosh(n\theta)}
=\frac{T_{n-j}(1/z)}{T_n(1/z)}.
\]
The reflecting equation holds because \(z\cosh\theta=1\). Uniqueness follows from the absorbing finite-chain linear system. Solving the corresponding first-step equations for \(\mathbb E_j\tau\) gives \(\mathbb E_k\tau=k(2n-k)=n^2-a^2\).

**2. Reset renewal identity.** Put \(q=1-r\) and let \(R\) be an independent geometric first-reset time, \(\Pr(R=t)=rq^{t-1}\), for \(t\ge1\). A single unsuccessful trial restarts at \(k\), whereas a successful trial is precisely \(\tau<R\) (the reset decision at the successful step must be ordinary). Thus its success probability is \(\mathbb E[q^\tau]=f_k(q)\). Its expected duration is \(\mathbb E[\min(\tau,R)]=(1-f_k(q))/r\). Renewal gives
\[
H_{n,k}(r)=\frac{1-f_k(q)}{r f_k(q)},
\]
which proves the displayed Chebyshev formula. In particular \(H_{n,k}(r)\) is finite and continuous for \(0\le r<1\); since \(k\ge1\), it diverges as \(r\uparrow1\).

**3. Reduce *global* reset benefit to a polynomial sign.** Set \(M=n^2-a^2>0\), \(x=(1-r)^{-1}=1+y\) and \(y>0\). Chebyshev polynomials are positive for \(x\ge1\), so the exact renewal expression yields
\[
H_{n,k}(r)-M
=\frac{D_{n,a}(y)}{y T_a(1+y)},
\qquad
D_{n,a}(y)=(1+y)[T_n(1+y)-T_a(1+y)]-MyT_a(1+y).
\]
Therefore the *sign for every resetting probability* is the sign of one finite polynomial evaluated on \(y>0\).

**4. A sharp coefficient-positivity lemma.** Write \(T_b(1+y)=\sum_{j=0}^b c_j(b)y^j\), with \(c_0(b)=1\) and, for \(1\le j\le b\),
\[
c_j(b)=\frac{b^2\prod_{h=1}^{j-1}(b^2-h^2)}{j!(2j-1)!!}>0,
\]
setting \(c_j(b)=0\) beyond degree \(b\). This follows by successive differentiation of the Chebyshev differential equation or its standard recurrence. If \(A_j\) is the coefficient of \(y^j\) in \(D_{n,a}\), direct substitution gives \(A_0=A_1=0\) and
\[
A_2=\frac{M}{6}(n^2+5-5a^2).
\]
We prove that \(A_2\ge0\) forces **all** \(A_j\ge0\), so no negative interval can be hidden at a larger reset rate.

When \(a=0\), the polynomial is \((1+y)(T_n(1+y)-1)-n^2y\), whose coefficients of degree at least two are nonnegative. When \(a=1\), the same conclusion follows from the above formula for \(A_2\) and, above degree two, the vanishing of all coefficients of \(T_1\).

Now assume \(a\ge2\) and \(n^2+5\ge5a^2\). Since \(n\) and \(a\) are integers this implies \(n\ge2a\): for \(a\ge3\), use \(5a^2-5\ge4a^2\), and for \(a=2\), use \(n^2\ge15\). For \(2\le j\le a+1\), let \(R_{j-1}=c_{j-1}(n)/c_{j-1}(a)\) and \(d_j=j(2j-1)\). The Chebyshev coefficient ratio gives the exact equivalence
\[
A_j\ge0\quad\Longleftrightarrow\quad
R_{j-1}-1\ \ge\ U_j,
\qquad
U_j:=\frac{M(d_j-1)}{n^2+j^2+j-1}.
\]
For \(j=2\) this is exactly \(n^2+5\ge5a^2\). For \(2\le j\le a\),
\[
R_j=R_{j-1}\frac{n^2-(j-1)^2}{a^2-(j-1)^2}
\ge4R_{j-1},
\]
and consequently \(R_j-1\ge4(R_{j-1}-1)\). On the other hand,
\[
\frac{U_{j+1}}{U_j}\le
\frac{j(2j+3)}{(j-1)(2j+1)}\le\frac{14}{5}<4
\quad(j\ge2).
\]
Thus \(A_2\ge0\) inductively implies \(A_j\ge0\) through \(j=a+1\). For all higher indices, the coefficients involving \(T_a\) vanish and \(A_j=c_j(n)+c_{j-1}(n)\ge0\). Since \(A_{n+1}=c_n(n)>0\), \(D_{n,a}(y)>0\) for every \(y>0\). This proves global strict detriment when \(n^2+5\ge5a^2\), including equality.

**5. The complementary regime.** If \(5a^2>n^2+5\), the coefficient \(A_2\) is strictly negative. Since \(A_0=A_1=0\), we have \(D_{n,a}(y)=A_2y^2+O(y^3)<0\) for all sufficiently small \(y>0\). This gives genuinely beneficial positive reset rates, and divergence as \(r\uparrow1\) guarantees that a global minimum occurs at an interior rate. Combining both regimes proves the theorem. \(\square\)

## Verification

A standalone exact-rational checker (`verify.py`, standard-library Python only) constructs the reset chain's full transient transition matrix, solves its mean hitting-time equations independently using rational Gaussian elimination, and compares those means with the closed Chebyshev formula. It tests every \(1\le k\le n\le18\) at reset probabilities \(0,1/11,1/4,3/5\), and checks the Chebyshev coefficient identities and global non-beneficial coefficient signs for those sizes. Its completed run prints `VERIFY_OK 1881 exact assertions`. These finite checks do not prove the all-size coefficient lemma, which is proved above.

## Relationship to prior work

Riascos, Boyer and Mateos (2021, arXiv:2110.15437) derive general discrete-time Markov-chain reset criteria and examine rings and Cayley trees. Their local derivative criterion is background for the first-order boundary, but does not imply the present **necessary and sufficient global** path threshold without the coefficient-positivity theorem. Chen, Li and Huang (2021, arXiv:2111.01330) likewise derive general restarting conditions and analyze two absorbing endpoints; their discussion explicitly notes that a positive infinitesimal-reset derivative alone need not preclude medium-rate acceleration, so the present coefficient-sign argument is essential. Bonomo and Pal (2021, arXiv:2102.00895) analyze discrete-time restarting in intervals with *two absorbing* boundaries; this differs from the present one-absorbing/forced-inward endpoint geometry. Das and Giuggioli (2022, arXiv:2209.08330) analyze resetting with *holding* reflecting boundaries and plot first-passage means against reset rate. Their endpoint transition rule (Section 3.2) does not match deterministic reflection, and their plotted examples do not give the sharp all-integer boundary proved here. Earlier work supplies renewal identities and spectral solutions; these formulas are not claimed to be new. This result isolates a rigorous global classification under one precisely stated discrete-time reflection convention.

## Limitations

The all-parameter theorem covers only a finite nearest-neighbor interval with deterministic one-step reflection, geometric resetting to the initial state, and one absorbing endpoint. It is a statement about *mean* first-passage time, not finite-sample estimation, tail dominance, or all restart mechanisms. It proves existence but not uniqueness or an explicit formula for the optimal positive resetting rate. The general restart renewal formulas and the small-rate variance test are prior work; the contribution is the sharp global if-and-only-if and its coefficient proof. Historical priority remains subject to literature coverage outside the inspected works.

## References

1. A. P. Riascos, D. Boyer and J. L. Mateos, *Discrete-time random walks and Lévy flights on arbitrary networks: when resetting becomes advantageous?*, arXiv:2110.15437, initially posted 28 October 2021. https://arxiv.org/abs/2110.15437
2. O. L. Bonomo and A. Pal, *First passage under restart for discrete space and time: application to one dimensional confined lattice random walks*, arXiv:2102.00895, initially posted 1 February 2021. https://arxiv.org/abs/2102.00895
3. D. Das and L. Giuggioli, *Discrete space-time resetting model: Application to first-passage and transmission statistics*, arXiv:2209.08330, initially posted 17 September 2022. https://arxiv.org/abs/2209.08330
4. Chen, Li and Huang, *First passage in discrete-time absorbing Markov chains under stochastic resetting*, arXiv:2111.01330, initially posted 2 November 2021. https://arxiv.org/abs/2111.01330
