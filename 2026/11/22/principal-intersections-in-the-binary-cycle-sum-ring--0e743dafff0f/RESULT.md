# Principal intersections in the binary cycle-sum ring

## Finding

Let \(S\) be the commutative, unital ring of finite formal sums \(\sum_{d\geq1}a_dC_d\), with \(a_d\in\mathbb F_2\), and multiplication specified on its formal cycle basis by
\[
C_mC_n=(\gcd(m,n)\bmod2)C_{\operatorname{lcm}(m,n)}.
\]
For **every** \(x,y\in S\) there is an explicitly constructible \(g\in S\) such that
\[
\boxed{xS\cap yS=gS.}
\]
Consequently every **nonempty finite intersection** of principal ideals of \(S\) is principal. If \(x\) and \(y\) have finite cycle supports, \(g\) can be constructed without introducing any new prime factor or larger power of two: write \(N=2^aK\) with \(K\) the least common multiple of their odd support factors (\(K=1\) for empty support) and \(a\) the greatest two-adic valuation of their cycle lengths (\(a=0\) for empty support). Then \(g\) can be chosen in the finite divisor-supported subring \(S_N=\operatorname{span}_{\mathbb F_2}\{C_d:d\mid N\}\).

This answers the general principal-intersection question posed in Section 3.7 of Gadouleau and Johnson (2026) for their binary cycle-sum ring. Importantly, \(S\) is **not** a principal ideal ring: the two-generated ideal \((C_2,C_4)\) is not principal.

## Assumptions and scope

All coefficients are in \(\mathbb F_2\); sums have **finite support**. The cycles are formal isomorphism classes of directed periodic transformations. The formula for their product is the direct-product cycle law reduced modulo two. The result concerns ring ideals \(xS\), not ideals of the underlying multiplication-only monoid nor formal sums over \(\mathbb N\). Zero and unit cases are included. The proof is valid for arbitrarily large support lengths and does not require a finite bound on the number of generators of \(S\).

For \(N=2^aK\) with \(K\) odd, the divisor-supported subring \(S_N\) is closed under multiplication because \(\operatorname{lcm}(d,e)\mid N\) whenever \(d,e\mid N\). When both inputs are zero, take \(N=1\).

## Proof

**1. Finite divisor model.** For \(t\mid K\) and \(0\leq j\leq a\), define the following binary coordinate of \(z=\sum_{d\mid N}z_dC_d\in S_N\):
\[
Z_{t,j}(z)=\sum_{d\mid t}z_{2^jd}\pmod2.
\]
For each fixed \(j\), this is the zeta transform of the coefficient function on the divisor poset of \(K\). It is bijective: process divisors of \(K\) in increasing order and recover
\[
z_{2^jt}=Z_{t,j}(z)+\sum_{\substack{d\mid t\\d<t}}z_{2^jd}\pmod2.
\]
(Equivalently use Möbius inversion, whose integer signs disappear in characteristic two.)

When both factors are odd, the binary cycle product is indexed by their least common multiple. For an odd cycle and a cycle with positive two-adic valuation \(j\), the same rule holds in that fixed \(j\)-layer. Two even cycles multiply to zero. Hence the zeta coordinates obey
\[
\begin{aligned}
Z_{t,0}(zw)&=Z_{t,0}(z)Z_{t,0}(w),\\
Z_{t,j}(zw)&=Z_{t,0}(z)Z_{t,j}(w)+Z_{t,j}(z)Z_{t,0}(w)\quad(1\leq j\leq a).
\end{aligned}
\]
Thus, as a unital commutative ring,
\[
S_N\cong\prod_{t\mid K}R_a,\qquad
R_a=\mathbb F_2\oplus\mathbb F_2^a,
\]
where \((b,u)(c,v)=(bc,bv+cu)\). The second summand of each factor is square-zero, and the identity is \((1,0)\). This also treats \(a=0\), when \(R_0=\mathbb F_2\).

**2. Local principal intersections.** In \(R_a\), every element \((1,u)\) is a unit, since its square is \((1,0)\). If \(u\neq0\), then
\[
(0,u)R_a=\{(0,0),(0,u)\};
\]
for \(u=0\) the ideal is zero. Two nonzero radical-generated principal ideals are therefore either equal (when their defining binary vectors agree) or have zero intersection. Consequently, for any pair \((b,u),(c,v)\), their principal ideals intersect in a principal ideal, with this canonical generator:

- If \(b=c=1\), use \((1,0)\).
- If \(b=1,c=0\), use \((0,v)\); if \(b=0,c=1\), use \((0,u)\).
- If \(b=c=0\) and \(u=v\), use \((0,u)\) (including \(u=v=0\)).
- Otherwise use zero.

**3. Explicit global generator.** Apply the rule in step 2 independently to the factors indexed by \(t\mid K\) in the decomposition of step 1. Invert the divisor zeta transforms to obtain \(g\in S_N\). The finite product decomposition proves
\[
xS_N\cap yS_N=gS_N.
\]
Every required operation uses finite binary sums, Boolean comparisons and divisor enumeration.

**4. Passing to the infinite ring.** Let \(M=2^bL\) be any multiple of \(N\). For a divisor \(s\mid L\), an element of \(S_N\) has at the \(s\)-factor of \(S_M\) precisely its old coordinates at \(t=\gcd(s,K)\), with \(b-a\) trailing zeros in the radical vector. Indeed, for every \(d\mid K\), the conditions \(d\mid s\) and \(d\mid\gcd(s,K)\) are equivalent. This preserves whether the scalar component is a unit and whether the two binary radical vectors coincide. Hence the generator rule from step 2 is compatible with enlarging \(N\), and
\[
xS_M\cap yS_M=gS_M
\]
for **every multiple** \(M\) of \(N\). Given \(w\in xS\cap yS\), choose witnesses \(r,s\in S\) with \(w=xr=ys\). All four elements lie in some \(S_M\) with \(N\mid M\); therefore \(w\in gS_M\subseteq gS\). The reverse inclusion \(gS\subseteq xS\cap yS\) follows already from \(g\in xS_N\cap yS_N\). This proves the asserted equality in \(S\). Repeated application proves the finite-intersection conclusion.

**5. Boundary: not all ideals are principal.** There is a ring homomorphism from \(S\) to the square-zero local ring \(R_2\), obtained by retaining only the binary zeta coordinates at the odd divisor \(t=1\) and the layers \(j=0,1,2\). It sends \(C_2\) and \(C_4\) to \((0,(1,0))\) and \((0,(0,1))\), respectively. Their generated ideal is the entire two-dimensional square-zero radical of \(R_2\), which no single element generates. Its inverse image cannot be principal, so the source ideal \((C_2,C_4)\) is not principal either. This distinguishes principal-intersection closure from the much stronger principal-ideal-ring property.

## Verification

The companion \(VERIFY.py\) uses the basis cycle-product rule independently of the divisor-coordinate generator algorithm. It builds each finite ring \(S_N\), enumerates all its elements, calculates every principal ideal as an actual set of multiples, and verifies the equality of that intersection with the ideal generated by the reconstructed candidate. It also checks the coordinate product law and inverts every coordinate vector. A separate exhaustive embedding test confirms that the canonical generator is unchanged under the cutoff extensions \(2\mid24\), \(6\mid12\), \(6\mid30\), and \(12\mid24\).

The completed exhaustive finite test covers \(N\in\{2,6,12,18,24,30\}\), corresponding to \(139{,}536\) ordered pairs of ring elements, and terminates with `VERIFY_OK 139536`. The unbounded claim is proved in steps 1–4; the finite test is only a cross-check.

As a nontrivial instance outside the previously proven regular-factor and zero-product cases, choose \(x=C_2+C_3\) and \(y=C_4+C_5\). Neither is regular and \(xy=C_{10}+C_{12}+C_{15}\neq0\). The algorithm gives
\[
xS\cap yS=(C_{10}+C_{12}+C_{15}+C_{30}+C_{60})S.
\]

## Relationship to prior work

Gadouleau and Johnson, *Semirings of formal sums and injective partial transformations* (first publicly submitted March 27, 2026), define precisely this binary ring in their Section 3 and establish the multiplication-coordinate rule (Lemma 3.1), the Boolean algebra of odd-cycle idempotents (Lemma 3.2), and division results. Their Section 3.7 explicitly leaves the general question of principal-ideal intersections unresolved, proving it when one input is regular (Proposition 3.23) or when the product is zero (Proposition 3.24). The argument here applies with no regularity or zero-product restriction and supplies an explicit finite divisor-supported generator. Its underlying square-zero decomposition and Boolean zeta coordinates are elementary structural ingredients; the all-pairs intersection theorem is the additional conclusion. The result does not claim originality for the cycle multiplication law, finite Boolean-ring decomposition, or standard properties of square-zero local rings.

For comparison, Guerrieri and Loper (2020) discuss Bézout-type intersection properties for **integral domains**. Those domain results do not settle the cycle-sum ring, which has nonzero square-zero elements. General ring-theoretic results for idealizations may imply the abstract intermediate lemma; whether the same special-ring conclusion appeared in literature beyond the checked sources is a residual priority risk.

## Limitations

Only \(\mathbb F_2\)-formal sums of cycles are considered. The result does **not** assert that the ring of formal sums of *chains and cycles*, or the original \(\mathbb N\)-coefficient transformation semiring, shares the intersection property. It establishes existence and an explicit algorithm for one generator, not uniqueness of generators. It does not imply that arbitrary (infinite) intersections of principal ideals are principal or that finitely generated ideals are principal. Earlier general theorems on square-zero idealizations have not been exhaustively ruled out as prior abstract coverage; the claimed advance is the specific resolution of the publicly stated cycle-sum question, pending independent priority review.

## References

1. M. Gadouleau and M. Johnson, *Semirings of formal sums and injective partial transformations*, arXiv:2603.26508v1, first publicly submitted 2026-03-27, https://arxiv.org/abs/2603.26508 (especially Sections 3.1–3.2 and 3.7, Lemma 3.1 and Propositions 3.23–3.24).
2. L. Guerrieri and K. A. Loper, *On the integral domains characterized by a Bezout Property on intersections of principal ideals*, arXiv:2002.00950, https://arxiv.org/abs/2002.00950 (background on a different, domain-only setting).
