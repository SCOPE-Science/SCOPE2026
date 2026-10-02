# An explicit six-logarithm lower bound for the Garsia rearrangement constant

## Result

For \(N\ge 2\), define the unimodular Garsia rearrangement constant
\[
\mathfrak G_N
:=
\sup_{\Phi}
\ \inf_{\tau\in S_N}
\ \sup_{\|a\|_{\ell^2}=1}
\left\|
\max_{1\le q\le N}
\left|
\sum_{j=1}^{q}a_{\tau(j)}\phi_{\tau(j)}
\right|
\right\|_{L^2},
\]
where the supremum is over all \(N\)-element orthonormal systems
\(\Phi=\{\phi_1,\ldots,\phi_N\}\) on probability spaces satisfying
\(|\phi_j|=1\) almost everywhere.

Let
\[
L_1(x)=\log_2 x,\qquad L_{r+1}(x)=\log_2 L_r(x)
\]
whenever the iterates are defined. There are absolute constants \(c,C>0\)
and \(N_0\) such that
\[
\boxed{\qquad
c\,L_6(N)\le \mathfrak G_N\le C\log\log(N+3),
\qquad N\ge N_0.
\qquad}
\]
The upper bound is Bourgain's 1989 theorem. The lower bound is the new
quantitative statement here. In particular, the qualitative divergence of
the optimal Garsia constant established by Lewko can be made explicit.

The same lower rate is realizable by real-valued orthonormal systems bounded
in absolute value by \(\sqrt2\).

## An explicit finite-scale form

For \(m\ge2\), put
\[
K=m^2,\qquad
B_m=\binom{m^2}{m},\qquad
Q_m=100m^2\log(2m)\,B_m,\qquad
D_m=2^{\,2^{m+9}},
\]
and
\[
X_m=2^{\,2^{\,Q_m^{D_m}}}.
\]
There is an integer \(N_m\le 2X_m\) and a unimodular \(N_m\)-element
orthonormal system such that every ordering \(\tau\) admits a real unit
coefficient vector \(a\) for which
\[
\left\|
\max_{q\le N_m}
\left|
\sum_{j\le q}a_{\tau(j)}\phi_{\tau(j)}
\right|
\right\|_2
\ge c_0\log m
\]
with an absolute \(c_0>0\). The example can be enlarged to every size
\(N\ge N_m\) without losing the lower bound.

The displayed value of \(X_m\) is intentionally explicit rather than
optimized. Its role is to turn the qualitative use of Szemerédi's theorem
in Lewko's permutation-pattern lemma into a quantitative one.

## Proof

### 1. A logarithmic finite Fourier obstruction

Karagulyan proved that for every \(m>1\) there is a permutation
\(\pi\in S_m\) for which the rearranged trigonometric maximal operator has
\[
\|T_{\pi,m}\|_{L^2(\mathbb T)\to L^2(\mathbb T)}
\ge c_1\log m.
\]
Since the operator depends only on the first \(m\) Fourier coefficients, this
gives a coefficient vector \(c\in\mathbb C^m\), \(\|c\|_2=1\), satisfying
\[
\left\|\max_{q\le m}
\left|\sum_{j\le q}c_{\pi(j)}e(\pi(j)x)\right|\right\|_2
\ge c_1\log m.
\]
Write \(c=u+iv\) with \(u,v\in\mathbb R^m\). Pointwise,
\[
M_c\le M_u+M_v.
\]
Hence one of \(u,v\), after normalization, is a real unit vector whose
maximal \(L^2\) norm is at least \((c_1/2)\log m\). Thus the Fourier
obstruction may be taken with real coefficients.

Translation and positive-integer dilation of the frequency set preserve the
distribution of the maximal absolute partial sum. Consequently the same
obstruction can be placed on any \(m\)-term arithmetic progression.

### 2. Quantifying the permutation-pattern lemma

Fix the bad permutation \(\pi\in S_m\) above and use Lewko's coloring
argument with \(K=m^2\) colors. Let \(\mathcal F_N\) be the colorings of
\([N]\) that fail to contain an \(m\)-term arithmetic progression whose
distinct colors realize the prescribed order \(\pi\).

Lewko's deletion argument gives the following exact finite estimate. If
\(r_m(N)\) denotes the maximum size of an \(m\)-term-progression-free subset
of \([N]\), then with
\[
d_N\le B_m r_m(N)
\]
one has
\[
|\mathcal F_N|
\le
\sum_{j=0}^{d_N}
\binom Nj B_m^j(m-1)^{N-j}.
\]

Set
\[
\eta_m=\frac{1}{100m^2\log(2m)},\qquad
\delta_m=\frac{\eta_m}{B_m}=\frac1{Q_m}.
\]
Gowers's explicit quantitative Szemerédi theorem states that every subset of
\([N]\) of density at least \(\delta_m\) contains an \(m\)-term arithmetic
progression once
\[
N\ge
2^{\,2^{\,\delta_m^{-D_m}}}
=
X_m.
\]
Hence \(d_N\le \eta_m N\). For the binary entropy
\(H(t)=-t\log t-(1-t)\log(1-t)\),
\[
|\mathcal F_N|
\le
(m-1)^N
\exp\!\left(
N\left[
H(\eta_m)+
\eta_m\log\frac{B_m}{m-1}
\right]\right).
\]

Take \(N\) divisible by \(K\). The number \(T_N\) of balanced \(K\)-colorings
(each color used \(N/K\) times) satisfies
\[
T_N=\frac{N!}{((N/K)!)^K}
\ge \frac{K^N}{(N+1)^K},
\]
because the balanced multinomial coefficient is maximal and there are at
most \((N+1)^K\) possible count vectors.

For a uniformly random permutation \(\sigma\) of \([N]\), Lewko's averaging
argument shows that the expected number of balanced colorings \(c\) for
which both \(c\) and \(c\circ\sigma^{-1}\) are exceptional is at most
\[
\frac{|\mathcal F_N|^2}{T_N}.
\]
The logarithm of this quantity divided by \(N\) is at most
\[
2\log(m-1)-\log K
+2H(\eta_m)
+2\eta_m\log\frac{B_m}{m-1}
+\frac{K}{N}\log(N+1).
\]
Here
\[
2\log(m-1)-\log K
=
2\log\left(1-\frac1m\right)
\le-\frac2m.
\]
Also \(H(t)\le t\log(e/t)\),
\(\binom{m^2}{m}\le (em)^m\), and the definition of \(\eta_m\) give,
for \(m\ge2\),
\[
2H(\eta_m)
+
2\eta_m\log\frac{B_m}{m-1}
\le \frac1{2m}.
\]
For \(N\ge X_m\) the elementary term
\(K\log(N+1)/N\) is also at most \(1/(2m)\).
Thus the expectation is \(<1\). Some \(\sigma\) therefore has no balanced
coloring that is exceptional in both orders.

Exactly as in Lewko's argument, partitioning an arbitrary permutation
\(\tau\) into \(K\) consecutive equal blocks produces a balanced coloring.
For the chosen \(\sigma\), either that coloring or its \(\sigma\)-transport
contains the required progression. Hence every \(\tau\) contains the
prescribed \(m\)-point progression pattern in at least one of the two
frequency orders.

Taking the least multiple of \(K\) above \(X_m\) gives an admissible
\(N_m\le2X_m\).

### 3. The two-copy orthonormal system

For the resulting permutation \(\sigma\), define on
\(\mathbb T\times\{0,1\}\), with each copy of \(\mathbb T\) having mass
\(1/2\),
\[
\phi_n(x,0)=e(nx),\qquad
\phi_n(x,1)=e(\sigma(n)x).
\]
This is a unimodular orthonormal system.

Fix any ordering \(\tau\). The quantitative pattern lemma supplies an
\(m\)-term arithmetic progression whose \(\pi\)-order appears as a
subsequence in one of the two copies. Put the real unit coefficient vector
from Step 1 on those \(m\) functions and put zero on all others. Intermediate
terms in the subsequence therefore do not affect the partial sums.
Translation and dilation of the progression preserve the Fourier maximal
distribution, and restricting to one copy costs only a factor \(2^{-1/2}\)
in \(L^2\). Thus
\[
\inf_{\tau}
\sup_{\|a\|_2=1}
\left\|\max_q\left|\sum_{j\le q}
a_{\tau(j)}\phi_{\tau(j)}\right|\right\|_2
\ge c_0\log m.
\]

Extending \(\sigma\) by fixed additional frequencies enlarges the example to
every greater \(N\); zero coefficients on the added functions preserve the
same lower bound.

For a real-valued version, adjoin \(t\in\mathbb T\) and replace
\(\phi_n(x,\varepsilon)\) by
\[
\sqrt2\,\operatorname{Re}\!\left(e(t)\phi_n(x,\varepsilon)\right).
\]
These functions are real orthonormal and bounded by \(\sqrt2\). For real
coefficients, averaging in \(t\) shows that their maximal \(L^2\) norm is at
least the complex-system maximal \(L^2\) norm, so the same lower rate holds.

### 4. Inverting the explicit scale

The crude bound
\[
B_m\le(em)^m
\]
shows
\[
\log_2 Q_m=O(m\log m).
\]
From the definition of \(X_m\),
\[
L_3(X_m)=D_m\log_2Q_m,
\]
and therefore
\[
L_4(X_m)
=
2^{m+9}+O(\log m),
\qquad
L_5(X_m)=m+O(1).
\]
The harmless passage from \(X_m\) to \(N_m\le2X_m\) changes this only by
\(O(1)\). Hence there is an absolute \(C_0\) such that
\[
L_5(N_m)\le m+C_0.
\]
Given sufficiently large \(N\), choose
\[
m=\left\lfloor L_5(N)-C_0-1\right\rfloor.
\]
Then \(N\ge N_m\), so
\[
\mathfrak G_N\ge c_0\log m
\ge c\,L_6(N).
\]
This proves the lower bound.

## Relation to prior work

Lewko (2026) disproved Garsia's conjecture and Kolmogorov's rearrangement
problem. For the finite problem, his paper explicitly notes that its proof
does not provide a useful dependence of the system size \(N\) on the target
maximal constant \(H\), because the argument uses qualitative Fourier
divergence and qualitative Szemerédi; it also states that the true growth
rate of the optimal finite constant is unknown.

Two quantitative results already in the literature fit precisely into those
two slots. Karagulyan (2020) proved the sharp logarithmic \(L^2\) lower bound
for a suitably rearranged finite trigonometric system, while Gowers (2001)
gave an explicit quantitative form of Szemerédi's theorem. Combining those
inputs with the finite counting inequality in Lewko's proof yields the
six-fold iterated-log lower rate above.

Bourgain's 1989 theorem remains the upper bound
\[
\mathfrak G_N\lesssim \log\log(N+3).
\]
Thus the present estimate is far from resolving the true order of
\(\mathfrak G_N\).

## Limitations

- The lower bound \(L_6(N)\) is extremely slow and is not claimed to be close
  to the true growth rate.
- The explicit \(N_m\) is deliberately crude. Better quantitative
  progression bounds with controlled dependence on the progression length,
  or a more efficient permutation-pattern argument, can improve it.
- The result quantifies the finite \(L^2\) Garsia constant. It does not give a
  quantitative almost-everywhere divergence rate for the infinite
  Kolmogorov construction.
- The unimodular formulation is complex-valued. The real-valued corollary has
  uniform bound \(\sqrt2\), not \(1\).
- No leading constant is claimed.

## References

1. M. Lewko, *On Kolmogorov's rearrangement problem and Garsia's conjecture*,
   arXiv:2609.18491 (2026). https://arxiv.org/abs/2609.18491
2. G. A. Karagulyan, *On Weyl multipliers of the rearranged trigonometric
   system*, Sbornik: Mathematics 211 (2020), 1704--1736.
   https://arxiv.org/abs/2004.01003
3. W. T. Gowers, *A new proof of Szemerédi's theorem*, Geometric and
   Functional Analysis 11 (2001), 465--588.
   https://doi.org/10.1007/s00039-001-0332-9
4. J. Bourgain, *On Kolmogorov's rearrangement problem for orthogonal systems
   and Garsia's conjecture*, Lecture Notes in Mathematics 1376 (1989),
   209--250. https://doi.org/10.1007/BFb0090057
