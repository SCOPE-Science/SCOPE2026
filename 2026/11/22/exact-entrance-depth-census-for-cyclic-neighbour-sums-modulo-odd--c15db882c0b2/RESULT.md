# Exact entrance-depth census for cyclic neighbour sums modulo odd prime squares

## Finding

Let \(p\) be any odd prime and \(n\) any positive even integer divisible by \(p\). Put \(s=\nu_p(n)\ge1\), \(q=p^s\), and \(d=p^{s-1}\). On the finite module \(V=(\mathbb Z/p^2\mathbb Z)^n\), consider the cyclic neighbour-sum update
\[
T(a_0,\ldots,a_{n-1})=(a_0+a_1,a_1+a_2,\ldots,a_{n-1}+a_0),
\]
with entries reduced modulo \(p^2\). For \(a\in V\), let \(\ell(a)\) be the smallest nonnegative integer \(t\) such that \(T^t(a)\) belongs to a periodic orbit. For every integer \(t\ge0\), the exact cumulative entrance count is
\[
\boxed{\#\{a\in V:\ell(a)\le t\}
=p^{\,2(n-q)+\min\{2t,t+d,2q\}}.}
\]
The number entering for the first time at \(t=0\) equals \(p^{2(n-q)}\); at any integer \(t\ge1\) it is the above count minus the count at \(t-1\). The maximal first-entry time is \(2q-d=(2p-1)p^{s-1}\). The two phases of the cumulative count are
\[
\begin{aligned}
0\le t\le d &: \quad p^{2(n-q)+2t},\\
d\le t\le 2q-d &: \quad p^{2(n-q)+t+d},\\
t\ge 2q-d &: \quad p^{2n}.
\end{aligned}
\]
Thus the population grows by a factor \(p^2\) per step until time \(d\), then by a factor \(p\) per step until saturation. Exactly \((1-1/p)p^{2n}\) states have the maximal entrance time. In particular, periodic states comprise precisely \(p^{2(n-q)}\) of the \(p^{2n}\) states.

## Assumptions and scope

Throughout, \(p\ge3\) is prime, \(n\ge2\) is even with \(p\mid n\), and \(t\) ranges over all nonnegative integers. This is the *sum* map, not the nonlinear absolute-difference Ducci operation. The starting tuple is arbitrary, not necessarily the cyclic basis vector. Periodic includes any orbit length, not only fixed points. There are no probabilistic or asymptotic assumptions: all displayed counts are exact. The characteristic \(p^2\) (rather than \(p\)) and divisibility \(p\mid n\) are essential to the two growth phases. The exponent \(\nu_p(n)\) denotes the ordinary prime-adic valuation of the positive integer \(n\).

## Proof

**1. Splitting the cyclic module.** Reverse the coordinate orientation if needed so that the cyclic shift corresponds to multiplication by \(X\). Identify \(V\) with \(R=(\mathbb Z/p^2\mathbb Z)[X]/(X^n-1)\), with \(T\) acting as multiplication by \(1+X\). Write \(n=qm\), where \(m\) is even and \(p\nmid m\) (because \(q\) is odd and \(n\) even). In \((\mathbb Z/p^2\mathbb Z)[X]\), factor
\[
X^n-1=(X^q+1)\,B(X),\qquad
B(X)=\frac{X^{qm}-1}{X^q+1}.
\]
Modulo \(p\), \(X^q+1=(X+1)^q\), whereas \(B(-1)=-m\not\equiv0\pmod p\). Consequently the two factors are coprime modulo \(p\), and Bézout's identity lifts to the ring modulo \(p^2\). The Chinese remainder theorem gives the direct sum
\[
R\simeq A\oplus U,\quad
A=(\mathbb Z/p^2\mathbb Z)[X]/(X^q+1),\quad
U=(\mathbb Z/p^2\mathbb Z)[X]/(B(X)).
\]
Multiplication by \(1+X\) is invertible on \(U\), since its reduction modulo \(p\) is coprime to \(B\). It is nilpotent on \(A\), because its reduction modulo \(p\) has \((1+X)^q=0\). Hence a tuple reaches a cycle by time \(t\) exactly when its \(A\)-component is killed by multiplication by \((1+X)^t\). Since \(|U|=p^{2(n-q)}\), the desired count is \(p^{2(n-q)}\) times the kernel size on \(A\).

**2. Prime-square relation.** In \(A\), put \(Y=1+X\). The defining relation becomes \((Y-1)^q+1=0\), a monic polynomial relation of degree \(q\). Thus \(1,Y,\ldots,Y^{q-1}\) is a basis for \(A\) over \(\mathbb Z/p^2\mathbb Z\). The integer binomial-valuation identity
\[
\nu_p\!\binom{p^s}{j}=s-\nu_p(j),\qquad 0<j<p^s,
\]
shows that every coefficient of \(Y^j\) with \(0<j<d\) is divisible by \(p^2\), while the coefficient of \(Y^d\) is divisible by \(p\) but not \(p^2\). The constant coefficient is zero. Therefore, after using the defining relation, there is an explicit polynomial \(W(Y)\) such that
\[
Y^q=pY^dW(Y)\quad\text{in }A,\qquad W(0)\not\equiv0\pmod p.
\]
As \(Y\) is nilpotent modulo \(p\), a polynomial in \(Y\) with invertible constant coefficient is a unit of \(A\). In particular, \(W\) is a unit. Multiplying the preceding relation by \(p\) gives \(pY^q=0\), since \(p^2=0\) in \(A\).

**3. Counting kernels up to \(q\).** Put \(S=\mathbb Z/p^2\mathbb Z\). For \(1\le t\le q\), the cokernel of multiplication by \(Y^t\) is
\[
A/Y^tA\simeq S[Y]/(Y^t,Y^q-pY^dW(Y))=S[Y]/(Y^t,pY^d).
\]
Here \(Y^q\) is zero modulo \(Y^t\), and \(W\) is a unit modulo \(Y^t\) since \(W(0)\) is a unit in \(S\) and \(Y\) is nilpotent in that quotient. The polynomial \(Y^q-pY^dW\) is the original monic relation, with \(W\) chosen as in part 2. In the last quotient the coefficients of \(Y^j\), \(0\le j<\min(t,d)\), range freely in \(S\); those with \(d\le j<t\) range freely modulo \(p\). Thus the cokernel has order \(p^{2\min(t,d)+\max(t-d,0)}=p^{\min(2t,t+d)}\). An endomorphism of a finite abelian group has equal kernel and cokernel cardinalities, giving the claimed kernel order. At \(t=0\) the map is the identity and its kernel has cardinality one, agreeing with the same formula.

**4. Counting kernels after \(q\).** Write \(t=q+r\), \(r\ge0\). The same relation gives
\[
Y^{q+r}A=pY^{d+r}A,
\]
using that \(W\) is a unit. For \(0\le r\le q-d\), this image has order \(p^{q-d-r}\), because \(pA\simeq\mathbb F_p[Y]/(Y^q)\). Therefore its kernel has order \(p^{q+d+r}=p^{t+d}\). For \(r\ge q-d\), the image is zero and its kernel has order \(p^{2q}\). Combining with part 3 gives, for every \(t\ge0\),
\[
|\ker(Y^t)|=p^{\min(2t,t+d,2q)}.
\]
Multiply by \(|U|\) from part 1. The last unsaturated exponent is \(2q-1\) at \(t=2q-d-1\), so exactly \((1-1/p)p^{2n}\) tuples enter at the maximal depth. All claims follow. \(\square\)

## Verification

The enclosed dependency-free program `verify.py` performs modular local-ring row and column reduction (independent of the polynomial-ideal proof) to calculate kernel exponents of powers of \(1+X\) modulo \(p^2\). It checks all steps for \((p,q)=(3,3),(3,9),(5,5),(7,7)\), and whole cyclic matrices for \((p,n)=(3,6),(3,12),(3,18),(5,10),(7,14)\). Separately, it exhaustively simulates the \(9^6=531441\) starting tuples for \((p,n)=(3,6)\), assigning their exact first-entry times by the periodicity criterion and comparing all populations. The observed entrance-time histogram at times \(0\) through \(5\) is
\[
(729,5832,13122,39366,118098,354294),
\]
which sums to \(531441\). The program prints `VERIFY_OK local_pairs=4 whole_matrix_pairs=5 full_states=531441 n6_depth_buckets=[729, 5832, 13122, 39366, 118098, 354294]` on success. These finite checks supplement but do not establish the universal statement; the proof is in the preceding sections.

## Relationship to prior work

Dular's *Cycles of Sums of Integers* characterizes periodic states over prime fields. Lewis and Tefft give a prime-power upper bound on maximum transient length. The later exact-maximal-length theorem [4] is stronger in its range of moduli; it also supplies the same primary group-ring reduction and its proof establishes the order-\(d\) factor in the mod-\(p^2\) relation \(Y^q=pY^dW\) (with \(Y=1-g\) in its notation). Neither that relation nor the maximum is claimed as new. The additional computation counts each intermediate cokernel, rather than finding only the first zero image, and gives the two-phase distribution and fraction at every entrance depth when \(p\mid n\).

Breuer's *Ducci Sequences and Cyclotomic Fields* (2010) addresses cyclotomic periods and periodic tuples, with an abstract specifying the separable case \(p\nmid n\); the potentially relevant full text was not obtainable in this check. Work on modulo-four transient distributions concerns another prime and does not determine the odd-prime-square formula. The originality conclusion is relative to the inspected primary statements and searched mathematical records, not a guarantee against unindexed equivalences.

## Limitations

The result addresses odd-prime-square moduli and even lengths divisible by that prime. It does not classify primitive cycle lengths, periods within the eventual core, prime-power moduli beyond the square, or the nonlinear absolute-difference map. The multiplicity counts use all labelled tuples, not rotation equivalence classes. The independent verification samples finite parameter families and one complete state space; no numerical experiment substitutes for proof. Inaccessible closely related material and unindexed mathematical equivalents are residual bibliographic risks. Independent scientific audit has not been performed.

## References

1. B. Dular, *Cycles of Sums of Integers*, arXiv:1905.01765 (first submitted 2019-05-05), *Fibonacci Quarterly* **58** (2020), 126–139; https://arxiv.org/abs/1905.01765.
2. M. L. Lewis and S. M. Tefft, *The Maximum Length for Ducci Sequences on* \(\mathbb Z_m^n\) *when* \(n\) *is Even*, arXiv:2410.18204 (first submitted 2024-10-23); https://arxiv.org/html/2410.18204v1.
3. F. Breuer, *Ducci Sequences and Cyclotomic Fields*, *Journal of Difference Equations and Applications* **16** (2010), 847–862; doi:10.1080/10236190802566509.
4. *Exact maximal transient lengths for cyclic neighbour-sum dynamics*, Finding and Proof §§1–2, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-maximal-transient-lengths-for-cyclic-neighbour-sum-dynamic--8221ed9a0ac0/RESULT.md
