# A period-two Ehrhart law for three-world Łukasiewicz fuzzy frames

## Finding
Fix an integer \(m\geq1\). On the labelled set \(W=\{1,2,3\}\), consider all matrices \(R:W^2\to L_m\), with \(L_m=\{0,1/m,\ldots,1\}\), satisfying reflexivity \(R(i,i)=1\) and Łukasiewicz transitivity
\[
\max\bigl(0,R(i,j)+R(j,k)-1\bigr)\leq R(i,k)
\quad(i,j,k\in W).
\]
The exact number of such matrices is
\[
\boxed{F(m)=\frac{54m^6+324m^5+875m^4+1340m^3+1236m^2+656m+160}{160}
-\frac{1-(-1)^m}{64}.}
\]
In particular, \(F(1)=29\), \(F(2)=281\), \(F(3)=1490\), and \(F(4)=5533\). This is an Ehrhart quasipolynomial of **minimal period two**. The associated six-dimensional directed-distance polytope has exactly \(31\) vertices, of which \(29\) are integral and exactly two have half-integral coordinates. Those two vertices encode the two cyclic orientations of a three-world directed distance pattern.

## Assumptions and scope
Worlds are **labelled**, all six off-diagonal relation values are independent choices before transitivity is imposed, and there are no symmetry, antisymmetry, totality, or other restrictions. The Łukasiewicz strong conjunction is \(u\odot v=\max(0,u+v-1)\). The relation is reflexive and satisfies \(R(i,j)\odot R(j,k)\leq R(i,k)\), exactly as in the motivating fuzzy Kripke-frame definition. The count is not the number of unlabelled isomorphism classes or of distinct induced fuzzy topologies. The claim concerns every integer granularity \(m\geq1\), without taking a limit in the number of worlds.

## Proof
**1. Directed-distance equivalence.** Define \(d_{ii}=0\) and \(d_{ij}=m(1-R(i,j))\) for \(i\ne j\). Then \(d_{ij}\in\{0,\ldots,m\}\). Because \(d_{ik}\leq m\), Łukasiewicz transitivity is equivalent, with no excluded boundary case, to
\[
d_{ik}\leq d_{ij}+d_{jk}\quad(i,j,k\in W).
\]
If \(d_{ij}+d_{jk}\geq m\), transitivity holds automatically; otherwise substitution and rearrangement yield precisely the same triangle inequality. Thus the required frames are the bounded integral directed pseudometrics on three labelled points, allowing zero off-diagonal distances and asymmetry.

**2. Exact fourfold count.** Write the six off-diagonal distances, in order, as
\[
(a,b,c,d,e,f)=(d_{12},d_{21},d_{23},d_{32},d_{13},d_{31}).
\]
The six nontrivial triangle inequalities are
\[
\begin{gathered}
e\leq a+c,\quad f\leq d+b,\quad
 a\leq e+d,\quad b\leq c+f,\\
 c\leq b+e,\quad d\leq f+a.
\end{gathered}
\]
Given any \(a,b,c,d\in\{0,\ldots,m\}\), the admissible values of \(e\) and \(f\) are **independent** and satisfy
\[
\begin{aligned}
\max(0,a-d,c-b)&\leq e\leq\min(m,a+c),\\
\max(0,b-c,d-a)&\leq f\leq\min(m,b+d).
\end{aligned}
\]
Both intervals are nonempty: e.g., \(a-d\leq a+c\), \(c-b\leq a+c\), and \(a-d,c-b\leq m\). Consequently
\[
\boxed{F(m)=\sum_{a,b,c,d=0}^{m}
\bigl(1+\min(m,a+c)-\max(0,a-d,c-b)\bigr)
\bigl(1+\min(m,b+d)-\max(0,b-c,d-a)\bigr).}
\tag{1}
\]
This finite expression provides exact integer values without numerical approximation.

**3. Polytope denominator.** Let \(P\subset\mathbb R^6\) be defined by the twelve coordinate inequalities \(0\leq x_i\leq1\) together with the six displayed triangle inequalities. It is bounded and full-dimensional: all six coordinates equal to \(1/2\) makes every defining inequality strict. In particular, \(F(m)=\#(mP\cap\mathbb Z^6)\).

The accompanying standard-library-only exact-arithmetic certificate (`checker.py`) constructs all eighteen inequalities as rational rows, enumerates **every** choice of six active hyperplanes (\(\binom{18}{6}=18564\)), solves each system with exact rational Gaussian elimination, discards singular or infeasible systems, and deduplicates the feasible intersections. Every vertex of a full-dimensional six-polytope must be determined by six linearly independent active facets, so this enumeration is complete. It finds \(4704\) nonsingular candidate bases and exactly \(31\) feasible distinct vertices. There are \(29\) vertices in \(\{0,1\}^6\) and exactly the following two nonintegral vertices, in the displayed coordinate order:
\[
\left(\tfrac12,1,\tfrac12,1,1,\tfrac12\right),
\qquad\left(1,\tfrac12,1,\tfrac12,\tfrac12,1\right).
\]
The exhaustive certificate tests inequalities using `fractions.Fraction`, so no floating-point tolerance or vertex-library assumption enters. Therefore the least common multiple of vertex denominators is \(2\).

**4. Ehrhart interpolation, valid for all granularities.** The rational-polytope Ehrhart theorem states that a full-dimensional rational \(d\)-polytope with vertex-coordinate denominators dividing \(q\) has a lattice-point quasipolynomial of degree at most \(d\) and period dividing \(q\). Therefore, **separately on each parity class**, \(F(m)\) agrees with an ordinary polynomial of degree at most six. Evaluating (1) exactly for \(m=0,1,\ldots,13\) produces
\[
(1,29,281,1490,5533,16281,40693,90152,182045,341585,
603877,1016226,1640689,2556869).
\]
The entry \(m=0\) is the formal Ehrhart count of \(0P\), not an additional finite-truth-value semantics. Exact substitution verifies that all seven even-index samples agree with
\[
E(m)=\frac{54m^6+324m^5+875m^4+1340m^3+1236m^2+656m+160}{160},
\]
and that all seven odd-index samples agree with \(E(m)-1/32\). Two polynomials of degree at most six agreeing at seven distinct arguments coincide identically. This proves the boxed count for **all** nonnegative integer dilations and hence all \(m\geq1\). Since the odd and even polynomial branches differ by the nonzero constant \(1/32\), the quasipolynomial has minimal period exactly two.

## Verification
Run `python3 checker.py` with standard Python 3. It performs the complete rational active-hyperplane enumeration, checks the \(31\)-vertex classification and both fractional coordinates, evaluates the exact fourfold sum for all fourteen interpolation arguments, checks the asserted polynomial and its integer numerators, and independently enumerates all six coordinates for \(m=0,1,2,3\). Expected final message:

`LUKASIEWICZ_THREE_WORLD_EXACT_CHECKS_OK vertices= 31 independent_bases= 4704 samples= 14`

The checker verifies the finite certificate and interpolation data. The universal quantifier over \(m\) is supplied by the mathematical Ehrhart theorem and the polynomial identity argument, not by extrapolation from finite samples. The vertex certificate requires only exact integer and rational operations and exhaustively enumerates every six-facet basis.

## Relationship to prior work
Khan, Martins, Madeira and Zaman (2026), Definition 15 and Propositions 1–3, motivate the reflexive and Łukasiewicz-transitive fuzzy accessibility relation and establish its fuzzy-topological semantics, but do not give a counting theorem for the three-world finite truth-value grid. Boixader and Recasens (2015) study representation and generation of general fuzzy \(T\)-preorders, not this grid-dependent labelled three-world Ehrhart enumeration. Pfeiffer (2004) treats **crisp** reflexive transitive relations; the value \(F(1)=29\) recovers the classical labelled three-element preorder count and is not claimed new. The general rational-polytope Ehrhart theorem is classical; the specific polytope, complete vertex certificate, and explicit period-two census are the result here. Gödel-type frame counting results are not interchangeable with this enumeration: Łukasiewicz transitivity involves additive truncation and is not invariant under arbitrary order-preserving regrading of relation weights.

## Limitations
This is a labelled **three-world** classification only, not a general formula for arbitrary world number or arbitrary finite truth algebras. The interval restriction \(d_{ij}\leq m\) is essential. The proof uses an exact finite combinatorial certificate plus a classical infinite theorem; it does not give a closed symbolic determinant-free account of all vertex cases. The prior-literature comparison is limited to accessible primary material and searches; broader directed-metric polytope literature or earlier fuzzy-relation enumeration may affect historical priority. The statement does not assert independent validation or historical uniqueness.

## References
1. M. A. Khan, M. A. Martins, A. Madeira, and B. Zaman, *On Łukasiewicz Topological Semantics*, arXiv:2610.40809, first posted 29 October 2026, https://arxiv.org/abs/2610.40809 .
2. D. Boixader and J. Recasens, *Generation and Characterization of Fuzzy T-preorders*, Applied Artificial Intelligence 29 (2015), 514–530, https://doi.org/10.1080/08839514.2015.1026663 .
3. D. Boixader and J. Recasens, *Transitivity of fuzzy relations under discretization*, Information Sciences 237 (2013), 261–270, https://doi.org/10.1016/j.ins.2013.03.017 .
4. G. Pfeiffer, *Counting Transitive Relations*, Journal of Integer Sequences 7 (2004), Article 04.3.2, https://cs.uwaterloo.ca/journals/JIS/VOL7/Pfeiffer/pfeiffer6.html .
5. M. Beck and S. Robins, *Computing the Continuous Discretely: Integer-Point Enumeration in Polyhedra*, chapter on rational Ehrhart quasipolynomials, https://matthbeck.github.io/papers/ccd.pdf .
