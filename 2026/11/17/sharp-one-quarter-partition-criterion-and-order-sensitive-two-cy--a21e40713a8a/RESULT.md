# Sharp one-quarter partition criterion and order-sensitive two-cycles for geometric quadratic population operators

## Finding
Let \(k\ge2\) and let \(R\) be a nonempty proper subset of \(\{0,1,\ldots,k-1}\) containing \(0\). Form the infinite partition \(A_R=\{j\ge0:j\bmod k\in R}\) and its complement. For the geometric two-block quadratic stochastic operator with three independently selectable geometric offspring rates, set
\[
q_R(r)=\frac{\sum_{j\in R}r^j}{\sum_{j=0}^{k-1}r^j},\qquad m_R=\inf_{0<r<1}q_R(r).
\]
**Exact classification:** every choice of the three rates is regular (every orbit converges in total variation to a fixed probability measure) if and only if \(m_R\ge1/4\). If \(m_R<1/4\), a nonempty open set of rate triples instead produces a unique attracting primitive two-cycle of probability measures and hence is nonregular. The exact best possible upper envelope of the scalar fixed-point discriminant over all triples is \(5-4m_R\), a supremum rather than an attained maximum.

For consecutive initial residue blocks \(R=\{0,\ldots,m-1}\), \(1\le m<k\), the criterion simplifies to **a sharp arithmetical threshold**: a two-cycle is attainable if and only if \(k>4m\); when \(k\le4m\), all admissible operators converge.

**Residue order matters, even at identical density:** at modulus \(14\), the four-class set \(R_0=\{0,1,2,3}\) is universally regular, whereas \(R_1=\{0,11,12,13}\) supports attracting two-cycles. Both subsets have four of fourteen residues. An explicit witness for \(R_1\) is \(r_{11}=7/8\), \(r_{12}=1/1000\), \(r_{22}=1/2000\), with discriminant strictly between \(4\) and \(5\).

## Assumptions and scope
The state space is \(\mathbb N_0\) with its discrete sigma-algebra. A population is a countably additive probability measure \(\mu\). Fix a two-partition \(A_R\sqcup B_R\). Two parents from \(A_R,A_R\), mixed parents, and two parents from \(B_R,B_R\) independently generate offspring according to \(G_{r_{11}},G_{r_{12}},G_{r_{22}}\), respectively, with \(0<r_{ij}<1\) and \(G_r(\{j\})=(1-r)r^j\). Parameters may differ or coincide. The operator is
\[
V\mu=x^2G_{r_{11}}+2x(1-x)G_{r_{12}}+(1-x)^2G_{r_{22}},\quad x=\mu(A_R).
\]
Regular means convergence of \(V^n\mu\) for every initial probability measure in total variation. Nonregular means that at least one initial probability measure has no limit.

## Proof
**Reduction and discriminant.** For each \(r\), the geometric mass of \(A_R\) is
\[
G_r(A_R)=(1-r)\sum_{\ell\ge0}\sum_{j\in R}r^{k\ell+j}=q_R(r).
\]
Writing \(a=q_R(r_{11}),\ b=q_R(r_{12}),\ c=q_R(r_{22})\), the block mass follows
\[
x_{n+1}=f(x_n),\qquad f(x)=ax^2+2bx(1-x)+c(1-x)^2.
\]
The fixed-point equation has discriminant
\[
\Delta=1+4\bigl(b^2-b+c(1-a)\bigr).
\]
For every admissible triple, \(0<\Delta<5\). The classical quadratic-interval result, recalled in Karim--Hamzah--Ganikhodjaev (2022, Theorem 3.1), says \(\Delta<4\) yields convergence to the unique fixed point, whereas \(\Delta>4\) yields an attracting primitive two-cycle, all scalar orbits except the fixed one converging to it. The return multiplier of that cycle is \(5-\Delta\). These scalar-dynamical facts are **prior work**, not new claims here.

**Optimization over the geometric family.** Since \(b^2-b<0\), \(c<1\) and \(a\ge m_R\),
\[
\Delta<1+4(1-m_R)=5-4m_R.
\]
Conversely \(q_R(r)\to1\) as \(r\downarrow0\), because \(0\in R\); fix \(r_{11}\) with \(a\) arbitrarily close to \(m_R\) and let \(r_{12},r_{22}\downarrow0\). Then \(b,c\to1\), so \(\Delta\to5-4a\). This proves \(\sup\Delta=5-4m_R\). If \(m_R\ge1/4\), strict inequality gives \(\Delta<4\) for all triples. If \(m_R<1/4\), choose \(a<1/4\) and \(b,c\) sufficiently near one; then \(\Delta>4\). Continuity of all coefficients makes this a nonempty open parameter region.

**Lifting to actual countable-state populations.** Define \(\Phi(x)=x^2G_{r_{11}}+2x(1-x)G_{r_{12}}+(1-x)^2G_{r_{22}}\). Since each geometric law has total mass one, \(\|\Phi(x)-\Phi(y)\|_{\rm TV}\le4|x-y|\). The identity \(V\mu=\Phi(\mu(A_R))\) thus lifts scalar convergence to total variation. An alternating scalar cycle \(x_-\ne x_+\) lifts to the distinct measures \(\Phi(x_-),\Phi(x_+)\), because their masses of \(A_R\) are \(x_+,x_-\), respectively. They form a primitive two-cycle of \(V\).

**Initial residue blocks.** For \(R=\{0,\ldots,m-1}\), \(q_R(r)=(1-r^m)/(1-r^k)\). Put \(r=e^{-t}\). Then
\[
\frac{d}{dt}\log q_R(e^{-t})=\frac{m}{e^{mt}-1}-\frac{k}{e^{kt}-1}>0,
\]
because \(s\mapsto s/(e^{st}-1)\) decreases for \(s>0\). Thus \(q_R(r)\) decreases strictly from \(1\) to \(m/k\) as \(r\) increases from \(0\) to \(1\); hence \(m_R=m/k\), giving the threshold \(k>4m\).

**Equal-density order counterexample.** For \(R_0=\{0,1,2,3}\) modulo \(14\), the preceding result gives \(m_{R_0}=2/7>1/4\). For \(R_1=\{0,11,12,13}\), exact rational arithmetic shows
\[
q_{R_1}(7/8)<6/25<1/4,\quad q_{R_1}(1/1000)>999/1000,\quad q_{R_1}(1/2000)>1999/2000.
\]
For the stated triple these imply
\[
c(1-a)-b(1-b)>\frac{1999}{2000}\frac{19}{25}-\frac1{1000}>\frac34,
\]
so \(4<\Delta<5\). This exact witness proves opposite regularity possibilities at the same modular density.

## Verification
The standalone Python 3 script `verify_threshold.py` performs exact rational checks of the modulus-14 witness, discriminant, return multiplier, and several representative geometric-mass identities. Run `python3 verify_threshold.py` from the extracted file directory. Its output marker is `RESIDUE_QUARTER_THRESHOLD_EXACT_OK`. The universal criterion, the optimization, monotonicity and lifting are proved above; finite script checks are not used as a substitute for those arguments.

## Relationship to prior work
Karim, Hamzah and Ganikhodjaev (2022) define countable-state two-partition geometric quadratic stochastic operators with up to three rates and reproduce the scalar discriminant criterion and two-cycle formulas. The present result does **not** claim that discriminant criterion, the two-cycle multiplier or the dimensional reduction as new. Instead it computes the sharp supremum **subject to a specific geometric residue partition**, classifies all partitions containing zero through a one-variable infimum test, establishes the initial-residue arithmetic cutoff and gives an order-sensitive same-density contrast. Their 2020 work establishes regularity for a distinct restricted two-parameter family; it does not supply this classification of three-rate residue partitions.

## Limitations
The subset \(R\) must contain residue zero, and the three geometric rates must be freely selectable in \((0,1)\). The criterion concerns existence of parameter choices supporting a two-cycle, not a claim that all parameters are nonregular when \(m_R<1/4\). The scalar convergence theorem is imported from the cited published analysis; the exact residue optimization and contrast are self-contained. Equivalently phrased results in unindexed work are not ruled out.

## References
1. S. N. Karim, N. Z. A. Hamzah and N. Ganikhodjaev, *On the Dynamics of Geometric Quadratic Stochastic Operator Generated by 2-Partition on Countable State Space*, Malaysian Journal of Mathematical Sciences **16** (2022), 727–737, DOI: 10.47836/mjms.16.4.06. Full text: https://mjms.upm.edu.my/fullpaper/2022-December-16-4/Hamzah%2C%20N.%20Z.%20A.-727-737.pdf
2. S. N. Karim, N. Z. A. Hamzah and N. Ganikhodjaev, *Regularity of Geometric quadratic stochastic operator generated by 2-partition of infinite points*, Malaysian Journal of Fundamental and Applied Sciences **16** (2020), 281–285, DOI: 10.11113/mjfas.v16n3.1737. https://mjfas.utm.my/index.php/mjfas/article/view/1737
