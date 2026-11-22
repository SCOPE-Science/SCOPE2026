# First nonunimodality at 103 disjoint three-point fences in a generic-poset extension spectrum

## Finding

Let \(\mathbb P\) denote the countable homogeneous generic partial order. Let \(V\) be the three-point poset with distinct minimal elements \(a,b\) and a common maximum \(c\), so \(a<c\), \(b<c\), and \(a\parallel b\). For each integer \(k\ge1\), let \(P_k\) be the disjoint union of \(k\) copies of \(V\), whose \(3k\) points are named separately.

For a complete nonalgebraic singleton type \(p\) over these named parameters, write \(\gamma(p)\) for the number of parameters comparable with a realization of \(p\). Define \(c_{k,r}=|\{p:\gamma(p)=r\}|\) and \(C_k(z)=\sum_{r=0}^{3k}c_{k,r}z^r\). Then the exact identity is

\[
C_k(z)=(1+2z+z^2+z^3)^k+(1+z+2z^2+z^3)^k-1+k(2z^2+z^3).
\]

**Sharp first failure within this natural family.** For every \(1\le k\le102\) the coefficient sequence is log-concave, hence unimodal. At \(k=103\) it is neither, with the exact central certificate

\[
\begin{aligned}
c_{103,153}=c_{103,156}&=45962653957548884891645789675241995235438728517008986952427308649309576,\\
c_{103,154}=c_{103,155}&=45960158024999770109427615695570080662639005115061071799331564399274024.
\end{aligned}
\]

Their strictly positive difference is

\[
2495932549114782218173979671914572799723401947915153095744250035552.
\]

Additionally, nonunimodality holds for every \(k\ge10000\). The range \(104\le k<10000\) is not completely classified here.

**General eventual nonunimodality principle.** Let \(Q\) be any finite nonempty poset with \(m\) points. Choose an order ideal of \(Q\) uniformly among its order ideals, and write \(\mu\) for the expected cardinality. If \(\mu\ne m/2\), the comparable-parameter singleton-type polynomial over \(k\) disjoint named copies of \(Q\) is nonunimodal for all sufficiently large \(k\).

## Assumptions and scope

The language is a strict binary partial order, with all parameter vertices named. A singleton type is nonalgebraic, meaning the new element is different from each named parameter. The homogeneous generic poset realizes every consistent finite one-point extension. Coefficients count complete types over the *fixed named* parameter structure, not types modulo its automorphism group. A nonnegative sequence is unimodal if it weakly increases and then weakly decreases; it is log-concave if the square of every interior entry is at least the product of its immediate neighbors.

## Proof

**1. The exact extension correspondence.** For any finite named poset \(P\), a new point \(x\) determines disjoint subsets \(L=\{v\in P:v<x\}\) and \(U=\{v\in P:x<v\}\). Transitivity holds exactly when \(L\) is a lower order ideal, \(U\) is an upper order filter, and every \(l\in L\) lies strictly below every \(u\in U\). Conversely these conditions construct a valid induced one-point extension, realized in \(\mathbb P\). Its grade is \(|L|+|U|\).

**2. Single-sided and double-sided extensions.** For \(P=P_k\), the ideal rank enumerator is \(I(z)^k\), where \(I(z)=1+2z+z^2+z^3\) counts the five ideals of a single \(V\). The filter rank enumerator is \(J(z)^k\), with \(J(z)=1+z+2z^2+z^3=z^3I(z^{-1})\). These account for all types with \(U=\varnothing\) or \(L=\varnothing\), except their shared empty-empty type has been counted twice, so subtract \(1\).

If \(L,U\ne\varnothing\), then every element in each lies in the same one of the \(k\) components: points from different components are incomparable and cannot satisfy \(l<u\). Within \(V\), there are precisely three such pairs: \(L=\{a\},U=\{c\}\); \(L=\{b\},U=\{c\}\); and \(L=\{a,b\},U=\{c\}\), with grades \(2,2,3\). Consequently their enumerator is \(k(2z^2+z^3)\), proving the displayed formula for all positive \(k\).

**3. Exhaustive and independently checkable finite cutoff.** Using \(I(z)=(1+z)^2+z^3\), let \(A_{k,r}=[z^r]I(z)^k\), with \(A_{k,r}=0\) outside \(0\le r\le3k\). The coefficient identity

\[
A_{k,r}=\sum_{j=0}^{k}\binom{k}{j}\binom{2(k-j)}{r-3j}
\]

(with out-of-range binomial coefficients set to zero) yields an entirely finite exact certificate:

\[
c_{k,r}=A_{k,r}+A_{k,3k-r}-\mathbf1_{r=0}+2k\mathbf1_{r=2}+k\mathbf1_{r=3}.
\]

For each integer \(k=1,\ldots,102\), evaluate this explicitly for all \(r=0,\ldots,3k\) and check \(c_{k,r}^2\ge c_{k,r-1}c_{k,r+1}\) for each interior \(r\). The independent finite program `check_independent.py` evaluates exactly those integer expressions, while `check.py` uses polynomial-convolution recursion and checks each index, including grades \(153\) through \(156\) at \(k=103\). The two programs agree. Since all entries are positive, the finite log-concavity inequalities imply unimodality through \(102\); the strict central valley disproves unimodality at \(103\).

**4. General eventual separation.** Let \(Q\) have \(m\) vertices, ideal enumerator \(I_Q(z)\), and filter enumerator \(J_Q(z)=z^m I_Q(z^{-1})\). Let \(B_Q(z)\) count the extensions with both \(L\) and \(U\) nonempty within one \(Q\). The same partition argument yields

\[
C_{Q,k}(z)=I_Q(z)^k+J_Q(z)^k-1+kB_Q(z).
\]

Every coefficient of \(B_Q\) has grade at most \(m\). Write \(M=I_Q(1)\). Then the coefficients of \(I_Q(z)^k\), divided by \(M^k\), give the law of a sum of \(k\) independent uniform-ideal cardinalities with mean \(k\mu\), and \(J_Q(z)^k\) is its reversal around \(mk\). If \(\mu\ne m/2\), Chebyshev's inequality puts a fixed positive fraction of each distribution into two disjoint linearly separated windows with only \(O(k)\) integer locations. Some coefficient in each window is therefore at least \(M^k/O(k)\). Hoeffding's inequality shows that at the midpoint degree \(\lfloor mk/2\rfloor\), both one-sided coefficient values are \(M^k\exp(-\Omega(k))\). The correction \(kB_Q(z)\) vanishes at this degree for large \(k\). Thus a coefficient on either side of the midpoint is strictly higher than the midpoint, forcing nonunimodality for all sufficiently large \(k\).

**5. Explicit all-large guarantee for \(V\).** Here \(M=5\), \(m=3\), and the uniform ideal size has mean \(7/5\) and variance \(26/25\). For \(k\ge10000\), Chebyshev's inequality ensures more than half the ideal-size mass lies within \(k/20\) of \(7k/5\). There are at most \(k/10+2\) integer grades in that window, so a coefficient there is at least \(5^k/(k/5+4)\). The reflected filter distribution gives such a coefficient on the opposite side of the midpoint. For \(h=\lfloor3k/2\rfloor\), Hoeffding's inequality for independent variables in \([0,3]\) gives

\[
c_{k,h}\le2\cdot5^k\exp(-k/500),
\]

because the one-sided distance from the mean is at least \(k/10-1\), and the correction has degree at most \(3\). Finally \(\exp(k/500)>2(k/5+4)\) for all \(k\ge10000\), so the central coefficient is lower than coefficients on both sides, proving the claim.

## Verification

Run the standalone scripts from a Python 3 installation using `python3 check.py` and `python3 check_independent.py`. Both use only the standard library, integer arithmetic and exact comparisons. The first script also enumerates every ternary relation-state assignment for \(k=1,2,3\) directly to verify the extension bijection. Outputs in `check_output.txt` and `binomial_output.txt` include `VERIFY_OK` and `BINOMIAL_VERIFY_OK`. The exact finite test includes all \(102\) values below the threshold and every coefficient index, not a sample. These are finite computations; the all-\(k\) enumerator and eventual nonunimodality follow separately from the arguments above.

## Relationship to prior work

The five order ideals of the three-point fence, and their general enumeration, belong to established fence-poset Whitney-number theory; see Conflitti (2005), especially definitions and Theorem 2.2, and its cited predecessors. Hubička (2010), Chapter 3.1, treats the countable generic partial order. Established generic-poset finite-parameter type-counting work gives the ideal/filter extension correspondence and computational complexity of the ungraded count. These prior results are credited; the new claim is specifically the degree-refined two-phase spectrum, sharp first nonunimodality index \(103\) within this disjoint-fence family, and an eventual separation principle for general disjoint copies with asymmetric ideal-size mean. Neither fence Whitney numbers alone nor an ungraded counting result entails the cutoff or bimodality without the additional analysis. Full historical priority across inaccessible publications is not certified.

## Limitations

The exact first threshold applies only to bases consisting of identical three-point \(V\) components, not to all finite posets or other homogeneous structures. The proof establishes nonunimodality for \(k=103\), supplies an analytic guarantee for \(k\ge10000\), but does not classify every intermediate \(104\le k<10000\). No claim is made for components whose ideal-size mean is exactly half their cardinality. No independent mathematical audit is represented by the reproducing programs.

## References

1. A. Conflitti, *On Whitney numbers of the Order Ideals of Generalized Fences and Crowns*, arXiv:math/0505636, original public version 30 May 2005, https://arxiv.org/html/math/0505636v2.
2. J. Hubička, *Combinatorial Properties of Finite Models*, arXiv:1009.0566, original public version 3 September 2010, Chapter 3.1, https://arxiv.org/html/1009.0566v1.
3. *Finite-parameter 1-type counting in the random poset is #P-complete*, publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-com--3b955f4020e1.
4. *Linear-arithmetic exact one-type counting on oriented tree-cover posets*, publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-linear-arithmetic-exact-one-type-counting-on-oriented-tree-cover--23742e530543.
