# Exact additive energy of the quartic graph over prime-power rings

## Finding
For a prime \(p\ge5\) and integer \(k\ge1\), let \(R_k=\mathbb Z/p^k\mathbb Z\), and let \(C_k=\{(x,x^4):x\in R_k\}\). Its **additive energy** is the number of ordered quadruples \((a,b,c,d)\in R_k^4\) with
\[
a+b=c+d,\qquad a^4+b^4=c^4+d^4\pmod{p^k}.
\]
Set \(\epsilon_p=\left(\frac{-3}{p}\right)\in\{-1,1\}\), \(A_p=(p-1)(3+2\epsilon_p)\), and \(B_p=3(p^2-1)-2A_p\). Define \(E_p(0)=1\). Then, **for every \(k\ge1\)**, the exact energy \(E_p(k)=E(C_k)\) is
\[
\boxed{E_p(k)=p^{2k-2}\bigl(B_p+A_p[p+(k-2)(p-1)]\bigr)+\begin{cases}p^{3k-3},&1\le k\le4,\\p^9E_p(k-4),&k\ge5.\end{cases}}
\]
This is an explicit four-step recurrence with a specified initial value and no uncomputed local counts. For each positive integer \(q\) coprime to \(6\), the energy of \(C_q=\{(x,x^4):x\in\mathbb Z/q\mathbb Z\}\) satisfies
\[
E(C_q)=\prod_{p^k\parallel q}E_p(k).
\]
In particular, the previously known prime-field formula is recovered:
\[
E_p(1)=\begin{cases}3p^2-5p+3,&p\equiv1\pmod3,\\3p^2-p-1,&p\equiv2\pmod3.\end{cases}
\]

## Assumptions and scope
All four summation variables are unrestricted residues modulo \(p^k\), and the additive energy counts ordered quadruples. Prime characteristics \(2\) and \(3\) are excluded: division by two and nonsingularity of the quadratic form used below are essential. We use the usual quadratic character on \(\mathbb F_p\). The empty product at \(q=1\) is \(1\). There is no assertion about maximal Fourier-extension norms or individual two-sum fibers.

## Proof
**1. Quartic collisions become a three-variable product congruence.** For a collision set \(s=a+b=c+d\), \(d_1=a-b\), and \(d_2=c-d\). Since \(2\) is invertible,
\[
a^4+b^4=\frac{s^4+6s^2d_1^2+d_1^4}{8}.
\]
Hence equality of fourth-power sums is equivalent to
\[
(d_1-d_2)(d_1+d_2)(d_1^2+d_2^2+6s^2)\equiv0\pmod{p^k}.
\]
The change \(u=d_1-d_2\), \(v=d_1+d_2\) is invertible and gives \(d_1^2+d_2^2=(u^2+v^2)/2\). Thus
\[
E_p(k)=\#\{(s,u,v)\in R_k^3: F(s,u,v)\equiv0\pmod{p^k}\},\qquad F=uv(u^2+v^2+12s^2).
\]
Each change of variables is bijective; no factor of \(p^k\) or symmetry divisor is introduced.

**2. Classify primitive residue classes.** Write \(Q=u^2+v^2+12s^2\). Modulo \(p\ge5\), \(Q\) is a nonsingular ternary quadratic form. It has exactly \(p^2\) zero triples, including the origin. One elementary verification is to fix \(s\): the equation \(u^2+v^2=c\) has \(p-\chi(-1)\) solutions when \(c\ne0\) and \(p+(p-1)\chi(-1)\) when \(c=0\). Summing over the \(p-1\) nonzero values of \(s\) and \(s=0\) gives \(p^2\).

Outside the origin, each of the three components \(u=0\), \(v=0\), \(Q=0\) contains \(p^2-1\) points. There are no primitive triple intersections: \(u=v=0\) and \(Q=0\) force \(12s^2=0\) and hence \(s=0\). The pairwise intersections comprise \(p-1\) points for \(u=v=0\), plus \(2(p-1)\) on each of \(u=0,Q=0\) and \(v=0,Q=0\) when \(-3\) is a square, and zero on those latter pairs otherwise. Thus the number of primitive classes lying on exactly two components is
\[
A_p=(p-1)(3+2\epsilon_p).
\]
The number lying on exactly one component is
\[
B_p=3(p^2-1)-2A_p.
\]
All other primitive residue classes contribute no roots at higher precision.

**3. Lift primitive classes.** At any point on exactly one component, that factor has a unit partial derivative and all other factors are units. By a local invertible coordinate change over \(\mathbb Z_p\), the valuation of \(F\) is the valuation of one coordinate. For an arbitrary lift of a specified class modulo \(p\), the probability that \(p^k\mid F\) is \(p^{-(k-1)}\).

At each primitive double intersection the two vanishing components meet transversely. For \(u=v=0\), take \(u,v\) as local coordinates and note \(Q\) is a unit. At \(u=Q=0\), necessarily \(v\ne0\), so \(\partial Q/\partial v=2v\) is a unit, and \(u,Q\) are local coordinates. The case \(v=Q=0\) is symmetric. Therefore locally \(F\) is a unit times the product of two independent coordinates already divisible by \(p\). For independent Haar-uniform \(a,b\in\mathbb Z_p\), a direct geometric-series count gives
\[
\Pr\{v_p(ab)\ge j\}=p^{-j}\bigl(1+j(1-p^{-1})\bigr),\quad j\ge0.
\]
Indeed, splitting according to \(v_p(a)=0,1,\ldots,j-1\) and \(v_p(a)\ge j\) gives this expression. Thus the conditional probability of \(p^k\mid F\) in a fixed primitive double-intersection class equals \(1\) when \(k=1\), and when \(k\ge2\) equals \(p^{-(k-2)}[1+(k-2)(1-p^{-1})]\). The displayed formula also agrees at \(k=1\) upon simplifying its final integer-count expression.

Multiplying these probabilities by the \(A_p\) or \(B_p\) classes, then by the total of \(p^{3k-3}\) lifts per class, gives the **primitive contribution**
\[
B_p p^{2k-2}+A_p p^{2k-2}\bigl[p+(k-2)(p-1)\bigr],\quad k\ge1.
\]

**4. Lift the singular origin.** Every triple reducing to the origin is \((s,u,v)=p(s',u',v')\). By homogeneity, \(F(p s',p u',p v')=p^4F(s',u',v')\). If \(1\le k\le4\), all \(p^{3(k-1)}\) such triples satisfy the congruence. For \(k\ge5\), the condition is \(p^{k-4}\mid F(s',u',v')\). Each triple modulo \(p^{k-4}\) has exactly \(p^9\) lifts modulo \(p^{k-1}\), so the origin contribution is \(p^9 E_p(k-4)\). Adding primitive and origin counts proves the recurrence.

**5. Composite moduli.** The Chinese remainder theorem identifies the quartic graph and its additive collision constraints at coprime moduli with the respective direct products, so the exact number of ordered collision quadruples multiplies. This proves the stated product over prime powers.

## Verification
The accompanying standalone `verify.py` evaluates the formula using exact integer arithmetic and directly enumerates the polynomial congruence for ten prime-power cases, including \(5^3\), \(7^2\), and \(11^2\). It independently enumerates original graph-pair sums for selected moduli and four squarefree composite moduli. It also checks the primitive-stratum formulas by direct enumeration for six primes. Successful execution prints `VERIFY_OK prime_power_cases=10 squarefree_cases=4 primitive_strata=6 max_prime_power=125`. Finite tests are corroboration; the proof covers all admissible prime powers and products.

## Relationship to prior work
The finite-field exact formula is already established in *Exact additive energy of the finite-field quartic graph* (published-finding corpus, 2026). Its domain is a field and its proof uses quadratic characters; it does not count higher residue-ring collision lifts. The new theorem agrees at the field level but supplies a four-step local singular-lifting recurrence and values at every \(p^k\), \(k\ge2\). For example, the ring \(\mathbb Z/25\mathbb Z\) has energy \(2225\), whereas the field \(\mathbb F_{25}\) has energy \(1753\); equal cardinality does not make their additive energies interchangeable.

Cowan, Katz, and White (2015) give generating-function and exact local-zeta methods for **quadratic polynomials** over \(p\)-adic fields. Their Theorem 2.1 and Section 4 concern quadratic forms and quadratic-plus-linear expressions, not the product of two lines and a ternary quadratic form \(uvQ\). Their methods provide background but not the displayed quartic-collision count. Mockenhaupt and Tao (2002) establish the finite-field restriction and collision-counting framework, not a prime-power-ring quartic formula. The recurrence is an explicit special local congruence census; no claim is made that the general Igusa-zeta machinery is new.

## Limitations
Characteristics \(2\) and \(3\) and moduli divisible by them are excluded. No individual representation spectrum, extremizer theorem, or weighted fourth-moment claim is proved. The first-level finite-field formula is prior work. A differently indexed older local-zeta computation for the specific product \(uv(u^2+v^2+12s^2)\) could cover the prime-power formula and remains the principal historical-priority risk.

## References
1. R. A. Cowan, D. J. Katz, L. M. White, *A New Generating Function for Calculating the Igusa Local Zeta Function*, arXiv:1506.07869v1 (public 2015-06-25), especially Theorem 2.1 and Section 4.
2. G. Mockenhaupt, T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1 (public 2002-04-18), Duke Math. J. 121 (2004), 35–74.
3. *Exact additive energy of the finite-field quartic graph*, published-finding corpus, 2026, identifier `2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f`.
