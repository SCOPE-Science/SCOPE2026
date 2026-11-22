# Disconnected positivity times of quadratic Bernstein–Durrmeyer spectral powers

## Finding

Let \(M_2\) be the classical unweighted degree-two Bernstein–Durrmeyer Markov operator on \(L^2(0,1)\). For each real \(t>0\), let \(M_2^t\) be its positive *Hilbert-space spectral power* (zero eigenvalues remain zero). Positivity of an operator here means order positivity: every almost-everywhere nonnegative input is mapped to a nonnegative output. It is stronger than positive semidefiniteness, which holds for every \(M_2^t\).

There exist unique numbers \(0<\tau_-<1<\tau_+\), determined by
\[
1-\frac52 10^{-\tau_-}-\frac3{10}\left(\frac52\right)^{\tau_-}=0,
\qquad
1-3\,2^{-\tau_+}+5\,10^{-\tau_+}=0,
\]
with
\[
\tau_-=0.891289809950934\ldots,\qquad
\tau_+=1.130946264800074\ldots.
\]
Then the **entire order-positivity set** of the quadratic averaging operator's spectral-power family is disconnected:
\[
\boxed{\quad M_2^t\text{ is positivity preserving}\quad\Longleftrightarrow\quad
t\in[\tau_-,1]\ \cup\ [\tau_+,\infty),\quad t>0.\quad}
\]
In particular, this genuine Markov operator is positivity preserving at the integer time \(t=1\), loses positivity at every sufficiently small time just above one, and recovers it precisely at \(\tau_+\). This is already the smallest nontrivial degree: the degree-one operator has positivity-preserving spectral powers precisely when \(t\ge1\).

More strongly, the exact minimum of the continuous integral kernel of \(M_2^t\) on the unit square is
\[
\min_{x,y\in[0,1]}K_t(x,y)=
\begin{cases}
1-\frac52 10^{-t}-\frac3{10}(5/2)^t,&0<t\le1,\\
1-3\,2^{-t}+5\,10^{-t},&t\ge1.
\end{cases}
\]
The formulas agree at \(t=1\). When the minimum is negative, explicit negative-kernel witnesses are given below.

## Assumptions and scope

Use real or complex \(L^2(0,1)\), Lebesgue measure, and the usual almost-everywhere order on real functions. Define \(B_{n,k}(x)=\binom nk x^k(1-x)^{n-k}\). For \(n=1,2\), set
\[
(M_nf)(x)=(n+1)\sum_{k=0}^n B_{n,k}(x)
\int_0^1 B_{n,k}(y)f(y)\,dy.
\]
The kernel \(K_1\) or \(K_2\) in this formula is continuous, symmetric, and nonnegative, with row integral one. Each \(M_n\) is selfadjoint, a Markov contraction, and has polynomial range of dimension \(n+1\). Spectral powers \(M_n^t\), for \(t>0\), are defined on the whole Hilbert space with zero-eigenspace component set to zero. No assertion of strong continuity at \(t=0\) on the whole space is made.

The assertion concerns *order* positivity, equivalently pointwise nonnegativity of the continuous integral kernel; it does not concern the always-valid positive-semidefinite property of these spectral powers. The primary MSC2020 classification is \(47D07\), motivated by preservation (or failure) of Markov positivity under multiplicative time interpolation.

## Proof

**1. Exact spectral representation.** The three orthonormal shifted Legendre polynomials
\[
q_0(x)=1,\quad q_1(x)=\sqrt3(2x-1),\quad q_2(x)=\sqrt5(6x^2-6x+1)
\]
are eigenvectors of \(M_2\), with respective eigenvalues \(1,1/2,1/10\). This follows by directly integrating the three polynomials against the displayed Bernstein product kernel. Orthogonality and the three-dimensional range show there are no other nonzero eigenvalues. Hence
\[
K_t(x,y)=q_0(x)q_0(y)+2^{-t}q_1(x)q_1(y)+10^{-t}q_2(x)q_2(y).
\]
Set \(u=2x-1\), \(v=2y-1\), \(a=2^{-t}\), and \(b=10^{-t}\). Then
\[
K_t(x,y)=1+3auv+\frac{5b}{4}(3u^2-1)(3v^2-1).
\]
Its row integral is one, because \(q_1,q_2\) have zero integral. Order positivity is equivalent to \(K_t\ge0\) on the full square: one implication follows by integration, and the other by taking a positive input supported on a small neighbourhood of any strictly negative kernel value (including a negative boundary value by continuity).

**2. Exact global minimum, with no numerical optimization.** Put \(r=|u|\), \(s=|v|\), \(p=rs\). The linear product \(uv\) is smallest for opposite signs. Moreover,
\[
(1-r^2)(1-s^2)\ge0\quad\Longrightarrow\quad r^2+s^2\le1+p^2.
\]
As the coefficient of \(r^2+s^2\) in the remaining quadratic product is negative, these two inequalities give
\[
\begin{aligned}
K_t(x,y)&\ge1-3ap+\frac{5b}{4}\bigl(9p^2-3(r^2+s^2)+1\bigr)\\
&\ge 1-3ap+\frac{5b}{2}(3p^2-1)=:Q_t(p).
\end{aligned}
\]
For every \(p\in[0,1]\), equality is realized by \(u=1\), \(v=-p\), equivalently \(x=1\), \(y=(1-p)/2\). Therefore the global minimum of \(K_t\) is *exactly* the minimum of the convex quadratic \(Q_t\) on \([0,1]\), not merely a lower bound. Its unconstrained vertex is
\[
p_*(t)=\frac{a}{5b}=5^{t-1}.
\]
For \(0<t\le1\), the vertex is admissible and direct substitution gives
\[
\min K_t=F(t):=1-\frac52 10^{-t}-\frac3{10}(5/2)^t.
\]
For \(t\ge1\), the vertex lies at or beyond the right endpoint and the minimum is
\[
\min K_t=G(t):=1-3\,2^{-t}+5\,10^{-t}.
\]
In the first region, a negative witness is \(K_t(1,(1-5^{t-1})/2)<0\); in the second it is \(K_t(1,0)<0\).

**3. Exact sign classification.** We have \(F(0)=-9/5\), \(F(1)=0\), and
\[
F''(t)=-\frac52(\log10)^2 10^{-t}
-\frac3{10}(\log(5/2))^2(5/2)^t<0,
\qquad F'(1)=\frac14\log(16/25)<0.
\]
Thus strict concavity, the negative left endpoint, and strict positivity immediately to the left of one imply that \(F\) has exactly one root \(\tau_-\) in \((0,1)\), is negative before it and positive between it and one. (One can equally use the strict decrease of the derivative to establish uniqueness.)

For the other region, \(G(1)=0\), \(G'(1)=\frac12\log(4/5)<0\), and \(G(t)\to1\). Furthermore,
\[
G'(t)=2^{-t}\bigl(3\log2-5\log10\,5^{-t}\bigr),
\]
whose parenthesis is strictly increasing and changes sign exactly once after \(t=1\). Thus \(G\) first decreases from zero, has a unique minimum, then increases to one and crosses zero exactly once at \(\tau_+>1\). Combining the two intervals yields precisely the stated positivity set. There are no other zeros or positivity components.

**4. Minimal degree.** For \(n=1\), the nonzero eigenvalues are \(1\) and \(1/3\), on \(q_0\) and \(q_1\). Its powered kernel is
\[
K_{1,t}(x,y)=1+3^{1-t}(2x-1)(2y-1),
\]
with exact minimum \(1-3^{1-t}\). Thus its positivity set is the single interval \([1,\infty)\); the disconnected behavior begins at quadratic degree.

## Verification

The included standalone `VERIFY.py` independently integrates the degree-one and degree-two Bernstein product kernels using exact rational polynomial arithmetic, reconstructs all nonzero eigenvalues, checks the spectral kernel identity at rational inputs, checks the exact global-minimum formula against a two-dimensional grid and stationary-point witnesses, and calculates the two transition times by bisection. All tests use only the Python standard library. These computations corroborate the formulas; the infinite quantifier over every real \(t>0\) and every \(x,y\in[0,1]\) is established by the inequalities and derivative-sign proofs above, not by the finite grid.

## Relationship to prior work

Altomare (online 4 January 2019, §6) treats Bernstein–Durrmeyer operators as positive Markov approximants to diffusion semigroups and studies integer iteration and large-degree limits. Its construction supplies a natural operator family but does not assert positivity of fixed-degree *noninteger spectral powers*. Earlier finite-dimensional results by Guillot, Khare, and Rajaratnam establish that conventional powers of every doubly nonnegative \(3\times3\) matrix are entrywise nonnegative for exponents at least one. That result does not imply this statement: evaluating a powered finite-rank *integral operator* at arbitrary continuum points is not the same as taking the corresponding power of a \(3\times3\) matrix sampled from its kernel. The present classification highlights this distinction.

A published result on Dirichlet Bernstein–Durrmeyer spectral-power *traces* on multivariate simplices covers eigenvalue sums, not entrywise kernel positivity or the univariate quadratic reentrant Markov-power phenomenon. The established quadratic Bernstein–Durrmeyer eigenvalues and positive Bernstein kernel are used as known structure; neither is presented as new. A complete historical search of approximation-theory and positive-kernel literature is not claimed.

## Limitations

This is an exact classification for the unweighted first two positive degrees, not a characterization for arbitrary degree or Jacobi weights. It concerns the canonical selfadjoint spectral-power family, not every imaginable semigroup embedding or the powers of arbitrary sampled matrices. The spectral powers have a nontrivial nullspace and do not form a strongly continuous semigroup with identity at \(t=0\) on the full \(L^2\) space. The positivity intervals do not establish independent bibliographic priority. The displayed decimal roots are numerical approximations to uniquely defined transcendental roots; their values are not proof of the sign classification.

## References

1. F. Altomare, *Iterates of Markov Operators and Constructive Approximation of Semigroups*, Constructive Mathematical Analysis 2 (2019), 22–39, DOI: 10.33205/cma.491601; published online 4 January 2019. Especially §6 and Theorems 6.9–6.10. https://dergipark.org.tr/en/download/article-file/618613
2. D. Guillot, A. Khare, and B. Rajaratnam, *The critical exponent conjecture for powers of doubly nonnegative matrices*, Linear Algebra and its Applications 439 (2013), 2422–2427, arXiv:1303.4701. Especially Theorem 1.6 and Corollary 2.3. https://arxiv.org/html/1303.4701v2
3. E. E. Berdysheva and K. Jetter, *Multivariate Bernstein–Durrmeyer operators with arbitrary weight functions*, Journal of Approximation Theory 162 (2010), 576–598, DOI: 10.1016/j.jat.2009.11.005. Background on the standard positive kernels and eigenpolynomial structure.
