# Three-amplitude signed-permutation Parseval frames for spherical cubics

## Finding

Let \(n\geq3\), let \(B_n\) be the group of all signed coordinate permutations of \(\mathbb R^n\), and let \(\mathcal P_{\leq3}(S^{n-1})\) be the restrictions of real or complex polynomials of total degree at most three, equipped with normalized surface-measure \(L^2\) norm. For \(v\in S^{n-1}\), let \(X=B_n v\) be its orbit **as a set of distinct points**, with equal sampling weights. The following statements hold.

1. The identity
\[
\frac1{|X|}\sum_{x\in X}|f(x)|^2=\int_{S^{n-1}}|f(x)|^2\,d\sigma(x)\quad (f\in\mathcal P_{\leq3}(S^{n-1}))
\]
is equivalent to \(X\) being an equal-weight spherical \(7\)-design. Equivalently, its evaluation vectors, divided by \(\sqrt{|X|}\), form a Parseval frame for this finite-dimensional polynomial Hilbert space.
2. **No such single orbit exists in any dimension \(n\geq3\) if \(v\) has at most two distinct squared-coordinate values**, including zero as an allowed value.
3. **For every integer \(n\geq100\) divisible by \(20\), there is such a single orbit with exactly three distinct, strictly positive squared-coordinate values.** Explicitly, put \(M_2=3n/(n+2)\), \(M_3=15n^2/((n+2)(n+4))\). Select a root \(a\in(67/125,27/50)\) of the explicitly specified one-variable equation below; define \(b,c\) by that equation. Then \(0<a<b<c\) and \(v\) has exactly \(9n/10\) entries \(\sqrt{a/n}\), exactly \(n/20\) entries \(\sqrt{b/n}\), and exactly \(n/20\) entries \(\sqrt{c/n}\). Its orbit is a Parseval sampling frame for spherical cubics. In particular three squared-amplitude levels are a **sharp complexity minimum** whenever this construction applies.

The orbit size is \(2^n n!/((9n/10)!(n/20)!^2)\). No claim is made that this extremely large design has minimal cardinality among general spherical designs.

## Assumptions and scope

The inner product on \(\mathcal P_{\leq3}(S^{n-1})\) is \(\langle f,g\rangle=\int f\overline g\,d\sigma\), with probability-normalized spherical measure. Every group orbit is taken as a set of distinct points, not with multiplicities. All claims are exact, over the real numbers, and use a **single**, unweighted, signed-permutation orbit. The obstruction covers all dimensions \(n\geq3\); existence is asserted for the stated infinite arithmetic progression only.

## Proof

**Step 1: frame/design equivalence and invariant moment test.** By polarization, the Parseval identity for all degree-at-most-three polynomials is equivalent to exact integration of \(f\overline g\) for all such \(f,g\). Every monomial of degree at most six factors into two monomials each of degree at most three. Hence the Parseval identity is equivalent to exactness for all polynomials of degree at most six. An orbit of \(B_n\) is antipodal, so all odd polynomial moments vanish both for the orbit and the sphere, extending exactness through degree seven. This proves the first equivalence.

For \(j=2,3\) write \(p_{2j}(v)=\sum_{i=1}^{n}v_i^{2j}\). Averaging a polynomial over \(B_n\) kills odd coordinate exponents and symmetrizes even exponents. Modulo the sphere relation \(p_2=\sum_i x_i^2=1\), every invariant polynomial through degree six is a linear combination of \(1,p_4,p_6\) (equivalently of \(1,p_4,p_2p_4,p_6,p_2^2,p_2^3\)). The normalized sphere satisfies \(\mathbb E_\sigma p_4=3/(n+2)\) and \(\mathbb E_\sigma p_6=15/((n+2)(n+4))\). It follows that the equivalent frame/design condition is precisely
\[
p_4(v)=\frac3{n+2},\qquad p_6(v)=\frac{15}{(n+2)(n+4)}.\tag{1}
\]
This simple invariant test is the standard Sobolev/group-averaging mechanism; it is not claimed as a new general principle.

**Step 2: the two-level obstruction.** Put \(U_i=nv_i^2\). Equation (1) and \(\|v\|=1\) require the uniform empirical distribution of the \(U_i\) to have moments
\[
\mathbb E U=1,\quad B:=\mathbb E U^2=\frac{3n}{n+2},\quad C:=\mathbb E U^3=\frac{15n^2}{(n+2)(n+4)}.\tag{2}
\]
A single level has \(B=1\), contrary to (2) for \(n\ge3\). Suppose two distinct levels \(u>w\ge0\) occur with respective multiplicities \(m\) and \(n-m\), where \(1\le m\le n-1\). Since each of \(u,w\) satisfies \(t^2-(u+w)t+uw=0\), their first three moments give
\[
u+w=\frac{C-B}{B-1}=\frac{6n}{n+4},\quad uw=u+w-B=\frac{3n^2}{(n+2)(n+4)}.
\]
Combining the mean equation \((mu+(n-m)w)/n=1\) with the quadratic formula yields
\[
m=\frac n2-\frac{n-2}{6}\sqrt{\frac{6(n+2)}{n+1}}.
\]
The integrality of \(m\) therefore forces
\[
3(n-2m)^2(n+1)=2(n+2)(n-2)^2.
\]
Reducing modulo the integer \(n+1\) implies \(n+1\mid18\). The only possible \(n\ge3\) are \(5,8,17\); for these, the quantity \(6(n+2)/(n+1)\) is respectively \(7,20/3,19/3\), none a rational square. Thus no integer \(m\) exists. The zero-level case was included by allowing \(w=0\).

**Step 3: a uniform three-level construction.** Assume \(n\ge100\) is divisible by \(20\). For \(a\in I:=[67/125,27/50]\), define
\[
\begin{aligned}
S(a)&=20-18a,\\
Q(a)&=20M_2-18a^2,\\
P(a)&=(S(a)^2-Q(a))/2,\\
\Delta(a)&=2Q(a)-S(a)^2,\\
F(a)&=S(a)^3-3S(a)P(a)-20M_3+18a^3.
\end{aligned}\tag{3}
\]
Direct exact rational arithmetic at the endpoints gives
\[
F(67/125)=-\frac{16(12913n^2+1624353n+123478304)}{390625(n+2)(n+4)}<0,
\]
\[
F(27/50)=\frac{24443n^2-168342n-31064456}{6250(n+2)(n+4)}>0
\quad (n\ge100).
\]
Moreover \(\Delta'(a)=720(1-a)>0\) and \(P'(a)=-360+342a<0\) on \(I\), with
\[
\Delta(67/125)=\frac{16(487n-45901)}{3125(n+2)}>0,
\]
\[
4-\Delta(27/50)=\frac{2(11n+15022)}{125(n+2)}>0,\qquad
P(27/50)=\frac{63659n+277318}{2500(n+2)}>0.
\]
Thus \(0<\Delta(a)<4\) and \(P(a)>0\) throughout \(I\), and \(S(a)\ge257/25>10\). By the intermediate value theorem, there exists \(a\in I^\circ\) with \(F(a)=0\). Set
\[
b=\frac{S(a)-\sqrt{\Delta(a)}}2,\qquad
c=\frac{S(a)+\sqrt{\Delta(a)}}2.
\]
Then \(0<a<0.54<4<b<c\). Since \(b+c=S\), \(b^2+c^2=Q\), and \(b^3+c^3=S^3-3SP\), the root equation \(F(a)=0\) yields
\[
\frac{18a+b+c}{20}=1,\quad
\frac{18a^2+b^2+c^2}{20}=M_2,\quad
\frac{18a^3+b^3+c^3}{20}=M_3.
\]
With the specified multiplicities \(9n/10,n/20,n/20\), these equations give \(\|v\|^2=1\), \(p_4(v)=3/(n+2)\), and \(p_6(v)=15/((n+2)(n+4))\). Step 1 proves the claimed single-orbit Parseval frame and spherical \(7\)-design in every asserted dimension.

## Verification

The standalone file `verify_design.py` uses only the Python standard library and reproduces the exact endpoint factorization inequalities, the arithmetic obstruction, and high-precision constructions at dimensions \(100,120,140,160,200,300,500,1000,2000\). It also evaluates the independent mixed sixth-moment identities \(\mathbb E x_1^6\), \(\mathbb E x_1^4x_2^2\), \(\mathbb E x_1^2x_2^2x_3^2\) against the normalized spherical values. Execute `python3 verify_design.py`; successful output ends in `ALL_CHECKS_PASS`. These finite computations support but do not replace the all-dimension proof.

## Relationship to prior work

Mohammadpour and Waldron (2019) established general reflection-group orbit-design methods and a two-orbit variational criterion; their generic single-orbit test does not supply the three-amplitude existence family or the all-dimension two-level obstruction. Bajnok studied orbit unions made from generalized hyperoctahedra (vectors with one nonzero magnitude and zeros), including seven-design criteria, rather than a single orbit with three positive magnitudes. Tanino, Tamaru, Hirao and Sawa analyzed a generalized corner-vector single-orbit family with at most two nonzero magnitudes, and identified existing degree-seven single-orbit examples in dimensions \(16\) and \(23\), each with a zero coordinate level. Those are acknowledged as earlier three-level examples; the present construction instead uses three **positive** levels in infinitely many dimensions. Misawa (2026) obtained symmetric-group-orbit simplex designs under the **uniform** simplex moment functional and then lifted them to higher-dimensional spherical seven-designs; that is a closely related interpolation method, but the present squared-sphere-coordinate functional is Dirichlet with parameter \(1/2\), not uniform Dirichlet parameter \(1\). The present contribution is the sharp coordinate-level obstruction paired with a three-positive-level infinite single-orbit Parseval frame construction. Its claim is not that seven-design existence, group averaging, or the general frame/design equivalence is new.

## Limitations

Existence is proved only for multiples of twenty at least one hundred; this does not classify all admissible dimensions. The coordinate-level minimum does not imply small cardinality, optimal point counts, improved noisy sampling stability, or a new general criterion for arbitrary groups. The finite calculations are supplementary. Historical priority is provisional: an earlier generalized symmetric cubature or invariant-design result might imply the construction under another description. Independent mathematical validation has not been performed.

## References

1. M. Mohammadpour and S. Waldron, *Constructing high order spherical designs as a union of two of lower order*, arXiv:1912.07151v1 (first posted 2019-12-16). https://arxiv.org/html/1912.07151v1
2. B. Bajnok, *Orbits of the hyperoctahedral group as Euclidean designs*, arXiv:2406.04023 (openly posted 2024; earlier work). https://arxiv.org/abs/2406.04023
3. K. Tanino, T. Tamaru, M. Hirao, and M. Sawa, *More on the corner-vector construction for spherical designs*, arXiv:2501.11437v1 (first posted 2025-01-20). https://arxiv.org/abs/2501.11437
4. R. Misawa, *Explicit construction of spherical 5- and 7-designs*, arXiv:2602.19757v1 (first posted 2026-02-23). https://arxiv.org/abs/2602.19757
