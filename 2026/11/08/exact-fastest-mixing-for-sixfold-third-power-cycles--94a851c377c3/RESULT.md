# Exact fastest mixing for sixfold third-power cycles

## Finding
For every integer \(m\ge2\), put \(n=6m\) and let \(C_n^3\) be the graph on \(\mathbb Z/n\mathbb Z\) joining vertices whose circular distance is one, two, or three. Among **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices supported on \(C_n^3\), including diagonal holding probabilities, the smallest second-largest eigenvalue modulus is exactly
\[
\boxed{\mu_n^*=\frac{2c-(1-c)(1+2c)}{2c+5(1-c)(1+2c)},\qquad c=\cos(2\pi/n).}
\]
An optimal matrix assigns the **same** probability
\[
a=\frac{(1-c)(1+2c)}{2c+5(1-c)(1+2c)}
\]
to holding and to each signed one-step and two-step move, and probability
\[
b=\frac{c}{2c+5(1-c)(1+2c)}
\]
to each signed three-step move. All seven probabilities are strictly positive. This matrix is the **unique cyclic-shift-invariant optimum**, although uniqueness among arbitrary non-invariant optima is not asserted.

The spectral gap obeys
\[
1-\mu_n^*=\frac{18\pi^2}{n^2}+O(n^{-4})\qquad(n\to\infty,\ 6\mid n),
\]
nine times the leading spectral gap of the optimally tuned nearest-neighbor symmetric walk on the same even cycle. The three-hop-only graph disconnects into three cyclic components when \(6\mid n\); optimal mixing instead retains positive, asymptotically small one- and two-hop probabilities.

## Assumptions and scope
The state space is \(\mathbb Z/n\mathbb Z\) with \(n=6m\), \(m\ge2\). Write \(S\) for the cyclic shift. Feasible matrices \(P\) are symmetric, entrywise nonnegative, satisfy \(P\mathbf1=\mathbf1\), and have no off-diagonal entries except between vertices at circular distance one, two or three. Holding is permitted. The objective is
\[
\mu(P)=\left\|P-\frac1n\mathbf1\mathbf1^\top\right\|_2
=\max_{v\perp\mathbf1,\,\|v\|_2=1}|v^\top Pv|,
\]
where both expressions include any repeated eigenvalue \(1\) occurring on the subspace orthogonal to the stationary vector.

Set \(\theta=2\pi/n\), \(c=\cos\theta\), \(A=(1-c)(1+2c)\), and \(H=2c+5A\). Since \(0<\theta\le\pi/6\), \(c\ge\sqrt3/2\); consequently \(A,H,a,b\) are positive, \(5a+2b=1\), and \(t=2b-a=(2c-A)/H\in(0,1)\).

## Proof
**1. Reduction to two translation classes and holding.** The centered spectral norm is convex and invariant under simultaneous permutation of rows and columns. Averaging an arbitrary feasible \(P\) under cyclic rotations preserves feasibility and cannot increase \(\mu\). The averaged symmetric circulant matrix has the form
\[
P=p_0I+\sum_{k=1}^3p_k(S^k+S^{-k}),\qquad p_k\ge0,\quad p_0+2(p_1+p_2+p_3)=1.
\]
It therefore suffices to optimize the three independent symmetric jump probabilities.

**2. Fourier spectrum.** The nonconstant Fourier modes have \(x_j=\cos(j\theta)\), \(1\le j\le n/2\). A symmetric circulant with range at most three has eigenvalue polynomial
\[
p(x)=p_0+2p_1T_1(x)+2p_2T_2(x)+2p_3T_3(x),\qquad p(1)=1,
\]
where \(T_k(\cos\phi)=\cos(k\phi)\). The proposed weights give
\[
p(x)=a(4x^2+2x-1)+2b(4x^3-3x),\qquad t=2b-a.
\]
Direct algebra with \(a/b=A/c\) gives the two exact factorizations
\[
\begin{aligned}
p(x)+t&=4b(x+1)(2x-1)\left(x-c+\frac1{2c}\right),\\
p(x)-t&=4b(2x+1)(x-c)\left(x+\frac1{2c}\right).
\end{aligned}
\]

**3. All Fourier values lie between the alternating extrema.** The allowed \(x_j\) decrease from \(c\) to \(-1\). For \(x_j\ge1/2\), the first factorization immediately gives \(p(x_j)\ge-t\). If \(x_j<1/2\), then \(j\ge n/6+1\) and
\[
x_j\le\cos(\pi/3+\theta)\le c-\frac1{2c}.
\]
The last inequality is equivalent to \(\tan\theta\le\sqrt3\), true for \(\theta\le\pi/6\). Thus the first factorization also gives \(p(x_j)\ge-t\) on this lower interval.

Similarly, for \(x_j\ge-1/2\), the second factorization gives \(p(x_j)\le t\). If \(x_j<-1/2\), then \(j\ge n/3+1\) and
\[
x_j\le\cos(2\pi/3+\theta)\le-\frac1{2c}.
\]
Here the final inequality is equivalent to \(\cos(2\pi/3+2\theta)\le-1/2\), again true for \(0<\theta\le\pi/6\). Hence \(-t\le p(x_j)\le t\) for **every** nonconstant Fourier mode, proving feasibility and the upper bound \(\mu(P)\le t\). The modes \(j=1,n/6,n/3,n/2\) attain, in that order, \(t,-t,t,-t\), so in fact \(\mu(P)=t\).

**4. Matching lower bound for every feasible matrix.** At the four distinct decreasing nodes
\[
\xi_1=c,\quad\xi_2=1/2,\quad\xi_3=-1/2,\quad\xi_4=-1
\]
our cubic has values \(t,-t,t,-t\). For each node let \(L_i(x)\) be the Lagrange interpolation polynomial associated with these four nodes. Since \(1>\xi_1>\cdots>\xi_4\), the four numbers \(L_i(1)\) have signs \(+,-,+,-\), respectively, and none is zero. Interpolating the proposed cubic at \(1\) shows
\[
1=p(1)=t\sum_{i=1}^4|L_i(1)|.
\]
For any degree-at-most-three polynomial \(q\) with \(q(1)=1\), interpolation and the triangle inequality imply
\[
1\le\max_{1\le i\le4}|q(\xi_i)|\sum_{i=1}^4|L_i(1)|,
\]
so \(\max_i|q(\xi_i)|\ge t\). Equality forces \(q(\xi_i)=p(\xi_i)\) at every node, hence \(q=p\). This proves that the proposed polynomial uniquely minimizes the discrete Fourier maximum among all symmetric circulants; it is feasible by step 3. Rotational averaging in step 1 yields global optimality over every feasible symmetric stochastic matrix, without claiming arbitrary-matrix uniqueness.

**5. Gap comparison.** Since \(5a+2b=1\) and \(t=2b-a\), \(1-t=6a\). Taylor expansion of \(c=\cos(2\pi/n)\) yields \(a=3\pi^2/n^2+O(n^{-4})\), giving the stated gap. For an even nearest-neighbor cycle the optimal symmetric walk has each neighbor probability \(1/(3-c)\), with modulus \((1+c)/(3-c)\) and gap \(2\pi^2/n^2+O(n^{-4})\); the ratio of the two gaps tends to nine.

## Verification
The attached `verify_cubic_cycle.py` reconstructs the eigenvalue polynomial, both factor identities, the four alternating Fourier modes, every mode on 200 cycle sizes \(n=12,18,\ldots,1206\), and full cyclic transition matrices on seven representative sizes. On extraction it reported `VERIFY_OK spectral_checks=121600 factor_checks=243200 matrix_fourier_checks=9144`. Separate exact symbolic simplification established the factor identities, row normalization and the gap identity. These finite computations check formulas and implementations; the all-size theorem follows from the algebraic and trigonometric proof above, not from enumeration.

## Relationship to prior work
Boyd, Diaconis and Xiao established the convex and semidefinite fastest-mixing framework, and Boyd, Diaconis, Parrilo and Xiao developed automorphism reductions including a closed form for the ordinary cycle. Bénézit's 2009 dissertation, §4.2.3, formulates the degree-\(k\) discrete cosine minimax program for range-\(k\) circulant filters, but then relaxes it to a continuous minimax problem and supplies **near-optimal** Remez coefficients. That general optimization formulation does not itself specify the exact range-three optimizer on cycles of length divisible by six, the simultaneous equality of four distinct transition types, or the sharp gap constant obtained here. The degree-two cycle-power classification is a separate earlier calculation; its quadratic extremal polynomial and three alternating modes do not cover the present cubic support and four-mode certificate.

## Limitations
The exact classification here is only for \(n\ge12\) divisible by six, the natural congruence class in which the Fourier modes at angles \(\pi/3\), \(2\pi/3\), and \(\pi\) occur simultaneously. Other cycle lengths and other jump radii are not classified. The optimizer is proved unique only among cyclically invariant matrices. The spectral-gap expansion does not itself establish sharp total-variation mixing-time constants. Specialist results outside the inspected literature may bear on publication priority.

## References
1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: https://doi.org/10.1137/S0036144503423264 (published electronically 2004-10-29). Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (first version posted 2007-09-06), https://arxiv.org/pdf/0709.0955.
3. F. Bénézit, *Distributed Average Consensus for Wireless Sensor Networks*, EPFL doctoral thesis no. 4509 (2009), §4.2.3 and Eqs. (4.10)–(4.14), https://infoscience.epfl.ch/bitstreams/37436696-5172-4327-af58-7251826e769c/download.
