# Sharp two-coordinate fastest mixing on nonbinary Hamming networks

## Finding
For integers \(d\ge2\) and \(q\ge3\), let \(X=\{1,\ldots,q\}^d\). Consider **all** symmetric, nonnegative, row-stochastic matrices \(P\) on \(X\) for which \(P_{xy}=0\) whenever the Hamming distance \(\delta(x,y)>2\). A loop is allowed. Write \(\Pi=\mathbf1\mathbf1^\top/q^d\) and \(\mu(P)=\|P-\Pi\|_2\). The exact unrestricted optimum is
\[
\min_P\mu(P)=\begin{cases}
0,&d=2,\\
1/7,&d=3,\ q\in\{3,4\},\\
1-2q/[d(q-1)],&\text{otherwise}.
\end{cases}
\]
Let \(A_j\) be the distance-\(j\) adjacency matrix, and \(E=\binom d2(q-1)^2\). An optimizer is, respectively,
\[
P_* =\begin{cases}
\Pi,&d=2,\\
I/21+2A_1/63+4A_2/63,&(d,q)=(3,3),\\
(I+A_2)/28,&(d,q)=(3,4),\\
A_2/E,&\text{otherwise}.
\end{cases}
\]
In the last regime, **every unrestricted optimizer**, even one lacking coordinate-permutation or alphabet symmetry, has no loops or distance-one transitions. For each starting word \(x\), each coordinate \(i\), and every alternative symbol \(t\ne x_i\), its one-step coordinate marginal satisfies
\[
\Pr\{X'_i=t\mid X=x\}=\frac{2}{d(q-1)},\qquad
\Pr\{X'_i=x_i\mid X=x\}=1-\frac2d.
\]
Thus every optimal move changes exactly two coordinates, and every alternative symbol occurs with a prescribed marginal probability. The statement does **not** assert uniqueness of unrestricted optimal matrices in this regime.

## Assumptions and scope
All matrices are real and symmetric; nonnegativity and row sums equal to one are entrywise, and only Hamming distances zero, one and two are permitted. The alphabet size \(q\) is an arbitrary integer, not necessarily a prime power. The norm is the centered spectral operator norm, equivalently the second-largest eigenvalue modulus (SLEM). Probabilities are per ordered transition, with no reversibility or stationary-distribution freedom beyond the imposed symmetric uniform-stationary setting.

## Proof
**1. Symmetry reduction and exact eigenvalues.** The full coordinate-and-symbol permutation group acts transitively on ordered pairs at each Hamming distance. Convexity and invariance of \(\|P-\Pi\|_2\) show that averaging any feasible \(P\) gives an optimal candidate of the form
\[
\bar P=(1-a-b)I+\frac{a}{D}A_1+\frac{b}{E}A_2,\quad
D=d(q-1),\quad E=\binom d2(q-1)^2,
\]
where \(a,b\ge0\), \(a+b\le1\). On the degree-\(k\) Hamming tensor harmonics (\(0\le k\le d\)), adjacency eigenvalues are the first two Krawtchouk values
\[
K_1(k)=D-qk,\qquad
K_2(k)=\frac{(D-qk)^2-(d-k)(q-1)^2-k}{2}.
\]
This follows by taking the first two coefficients in \((1+(q-1)z)^{d-k}(1-z)^k\). Hence
\[
\lambda_k=1-a-b+a\frac{K_1(k)}D+b\frac{K_2(k)}E.
\]
The constant mode has \(\lambda_0=1\); the SLEM is \(\max_{1\le k\le d}|\lambda_k|\). In particular
\[
\lambda_1=1-\frac{q}{d(q-1)}(a+2b).
\]

**2. The generic lower bound and its attainment.** For \(d\ge4,q\ge3\), or \(d=3,q\ge5\), the nonnegative number \(m=1-2q/[d(q-1)]\) satisfies \(\lambda_1\ge m\), because \(a+2b\le2\). Equality forces \(a=0,b=1\). For this candidate, \(\lambda_k=K_2(k)/E\). The polynomial \(K_2(k)\) is convex in the real variable \(k\), and its maximum on \([1,d]\) occurs at an endpoint. The endpoints obey
\[
\frac{K_2(1)}E=m,\qquad \frac{K_2(d)}E=\frac1{(q-1)^2}\le m,
\]
where the last inequality is exactly \(d(q-2)\ge2(q-1)\), valid in the stated generic regimes.

For the negative side, the real minimum occurs at
\[
k_0=\frac{2d(q-1)-(q-2)}{2q}.
\]
Direct completion of the square yields
\[
8\bigl(K_2(k_0)+K_2(1)\bigr)
=F(d,q):=4d^2(q-1)^2-12dq(q-1)+7q^2-4q-4.
\]
For \(d\ge4,q\ge3\), \(F(4,3)=15>0\), \(F(4,q)=23q^2-84q+60\) increases for \(q\ge3\), and \(F(d,q)\) increases with \(d\ge4\) since its derivative in \(d\) is \(4(q-1)[2d(q-1)-3q]>0\). For \(d=3,q\ge5\), \(F(3,q)=7q^2-40q+32\) is increasing and equals \(7>0\) at \(q=5\). Consequently \(-K_2(k)/E\le m\) for all integral \(1\le k\le d\). This proves \(\mu(A_2/E)=m\) and the unrestricted sharp lower bound by symmetry averaging.

**3. The two exceptional three-coordinate cases.** At \((d,q)=(3,3)\), the three nontrivial eigenvalues are
\[
\lambda_1=1-a/2-b,\quad
\lambda_2=1-a-5b/4,\quad
\lambda_3=1-3a/2-3b/4.
\]
The signed convex combination \((3\lambda_1-3\lambda_2+\lambda_3)/7=1/7\) proves the universal lower bound \(\mu\ge1/7\). It is attained by \(a=4/21,b=16/21\), for which the three eigenvalues are \((1,-1,1)/7\). Equality of all signed terms determines that unique orbit-constant minimizer.

At \((d,q)=(3,4)\),
\[
\lambda_1=1-4a/9-8b/9,\quad
\lambda_2=1-8a/9-32b/27,\quad
\lambda_3=1-4a/3-8b/9.
\]
The signed convex combination \((4\lambda_1-3\lambda_2)/7=1/7+8a/63\) forces \(\mu\ge1/7\). Equality requires \(a=0,b=27/28\), yielding nontrivial eigenvalues \((1,-1,1)/7\). When \(d=2\), all word pairs lie at distance at most two, so \(P=\Pi\) attains and uniquely characterizes zero SLEM.

**4. Rigidity of every generic optimizer.** Let \(P\) be *any* unrestricted optimizer in the generic regime and \(\bar P\) its automorphism average. Step 2 makes \(\bar P=A_2/E\) the unique optimal orbit-constant kernel. Let \(V_1\) denote the degree-one Hamming tensor-harmonic space, and \(Q_1\) its orthogonal projection. It is invariant under the averaging group. Therefore
\[
\operatorname{tr}(Q_1P)=\operatorname{tr}(Q_1\bar P)=m\dim V_1.
\]
On the centered space, symmetric \(P\) satisfies \(P\preceq mI\) because \(\mu(P)=m\). The positive semidefinite difference \(mI-P\) therefore has zero trace on \(V_1\), so \(Pf=mf\) for every \(f\in V_1\). Applying this to \(f(x)=\mathbf1_{\{x_i=t\}}-1/q\) proves the stated coordinate marginals. Their expected number of changed coordinates is exactly \(d(1-m)(q-1)/q=2\). Since every allowed transition changes at most two coordinates, every positive transition changes exactly two. This proves both support elimination and marginal rigidity.

## Verification
The included standalone standard-library program `verify.py` computes the degree-one and degree-two Hamming eigenvalues using exact rational arithmetic. It checks all \(2\le d\le60\), \(3\le q\le50\) (2,832 parameter pairs), and also constructs 306 full stochastic-matrix rows for selected small graphs, validating row sums, support and predicted one-coordinate marginals. The two exceptional signed dual identities are checked exactly. The program is supplementary: the universal proof is the preceding algebraic argument, not the finite test range.

## Relationship to prior work
Boyd, Diaconis, Parrilo and Xiao (first publicly posted 6 September 2007) establish automorphism averaging and solve fastest mixing for ordinary Hamming graphs **with distance-one edges only**. The present support includes all Hamming-distance-two edges; the problem, spectrum and optimal support differ. A prior binary-alphabet classification of radius-two Hamming mixing (including optimizer-face information) is acknowledged; the present result addresses the nonbinary alphabets and proves complete removal of distance-one transitions in the generic regime. Related positive-definite Turán extremal problems on Hamming radius-two balls optimize a different Fourier positivity/mass functional, not centered Markov-chain spectral norm.

## Limitations
No claim is made for nonsymmetric chains, nonuniform stationary measures, jumps of length three or more, or \(q=2\). The rigidity conditions for generic unrestricted optimizers are *necessary*, not claimed sufficient. The proof does not classify all unrestricted optimizer faces or prove global uniqueness except in the complete-graph case \(d=2\). Publication priority beyond the inspected sources cannot be guaranteed.

## References
1. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest mixing Markov chain on graphs with symmetries*, arXiv:0709.0955v1, initially public 2007-09-06; published in SIAM J. Optim. 20 (2009), 792–819. https://arxiv.org/abs/0709.0955 ; DOI: 10.1137/070689413.
2. S. Boyd, P. Diaconis, and L. Xiao, *Fastest mixing Markov chain on a graph*, SIAM Review 46 (2004), 667–689, DOI: 10.1137/S0036144503423264.
3. A. E. Brouwer, A. M. Cohen, and A. Neumaier, *Distance-Regular Graphs*, Springer (1989), background on Hamming schemes and Krawtchouk eigenvalues; the formula used here is independently derived in Step 1.
