# Exact two-point extension spectra over chains in the generic linearly ordered poset

## Finding
Let \(\mathcal L=(L,\triangleleft,\prec)\) be the countable Fraïssé limit of finite strict partial orders \(\triangleleft\) equipped with a distinguished linear extension \(\prec\). Individually name an induced chain \(a_1\triangleleft\cdots\triangleleft a_n\), with \(n\geq0\); its named order is also \(a_1\prec\cdots\prec a_n\). A *pair type* is a complete type over these individual parameters of an ordered pair \((x,y)\) of distinct elements outside the base.

Write \(C_n\) for the number of pair types with \(x\triangleleft y\), and \(I_n\) for the number with \(x\prec y\) but \(x\) and \(y\) incomparable under \(\triangleleft\). Then, for **every** integer \(n\geq0\),
\[
\boxed{C_n=\frac{(n+1)(n+2)^2(n+3)^2(n+4)}{144},\qquad
I_n=\frac{(n+1)(n+2)(n+3)(n+4)(3n^2+9n+10)}{240}.}
\]
The reverse linear-order orientation has the same two counts. Thus the number of all pair types is \(T_n=2(C_n+I_n)\), and their strictly partially ordered comparability fraction is
\[
\boxed{p_n=\frac{C_n}{C_n+I_n}=\frac{5(n+2)(n+3)}{14n^2+52n+60}.}
\]
The sequence \((p_n)_{n\geq0}\) is strictly decreasing, from \(p_0=1/2\) toward \(5/14\). More precisely,
\[
p_n-\frac5{14}=\frac{15(3n+4)}{14(7n^2+26n+30)}>0.
\]
The one-point count is \(N_n=\binom{n+3}{3}\), and \(T_n/N_n^2\to7/5\). These are uniform distributions on finite **sets of logical types**, not on vertices of the countable structure.

## Assumptions and scope
Both orders are strict; \(\triangleleft\subseteq\prec\); equality with a parameter or between the new coordinates is excluded. The chain elements are pointwise named, and the coordinates \((x,y)\) are ordered. The base may be empty. The class of all finite linearly extended partial orders has the hereditary, joint embedding and amalgamation properties, and its Fraïssé limit realizes all finite induced extensions. In its finite relational language, complete types of injective tuples over a named finite base are exactly the induced finite extension diagrams.

## Proof
**Cut encoding.** Fix \(x\prec y\). Suppose exactly \(i\) named elements precede \(x\) in the linear order and exactly \(j\) precede \(y\), so \(0\leq i\leq j\leq n\). The positions are uniquely determined even when \(i=j\), in which case both are in the same gap and the order is \(x\prec y\). Every possible relation between a new point and the old chain is specified by a lower cut \(\ell\) and an upper cut \(u\): the old points below the new point are \(a_1,\ldots,a_\ell\), and those above it are \(a_u,\ldots,a_n\), with \(u=n+1\) allowing an empty upper set. For \(x\), \(0\leq\ell_x\leq i\) and \(i+1\leq u_x\leq n+1\); for \(y\), \(0\leq\ell_y\leq j\) and \(j+1\leq u_y\leq n+1\). These inequalities are necessary and sufficient for the individual cut diagrams.

**Comparable channel.** Adding \(x\triangleleft y\) is transitive exactly when \(\ell_x\leq\ell_y\) and \(u_x\leq u_y\). Necessity follows because all old predecessors of \(x\) must precede \(y\), and all old successors of \(y\) must succeed \(x\). Conversely the two inequalities ensure these mixed transitivity conditions, while the chain and the new strict comparison are already transitive. The number of lower-cut pairs at fixed \((i,j)\) is
\[
L_{i,j}=\sum_{\ell_x=0}^{i}(j-\ell_x+1)=(i+1)(j+1)-\frac{i(i+1)}2,
\]
and the number of upper-cut pairs is
\[
U_{i,j}=\sum_{u_y=j+1}^{n+1}(u_y-i)=\frac{(n-j+1)(n+j+2-2i)}2.
\]
Consequently \(C_n=\sum_{i=0}^n\sum_{j=i}^n L_{i,j}U_{i,j}\).

**Incomparable channel.** Without \(x\triangleleft y\), the only possible missing transitive comparison forced through an old vertex is a path \(x\triangleleft a_t\triangleleft y\). Such a path exists precisely when \(u_x\leq\ell_y\). The reverse path is impossible because it would contradict the fixed linear order \(x\prec y\). Hence incomparability is realizable **exactly** when \(u_x>\ell_y\); no other relation is forced. The independent choices of \(\ell_x\) and \(u_y\) contribute \((i+1)(n-j+1)\). Among the \((n-i+1)(j+1)\) pairs \((u_x,\ell_y)\), exactly \(\binom{j-i+1}{2}\) violate the strict inequality. Therefore
\[
I_n=\sum_{i=0}^n\sum_{j=i}^n(i+1)(n-j+1)
\left((n-i+1)(j+1)-\frac{(j-i)(j-i+1)}2\right).
\]
These two cases exhaust all allowed extensions with \(x\prec y\). Symmetry of coordinate names gives identical counts for the reverse order \(y\prec x\), with comparable orientation reversed.

**Exact evaluation for every size.** Each summand in the two displayed double sums is a polynomial of total degree at most four in \(i,j,n\). Consecutive summations over \(0\leq i\leq j\leq n\) therefore yield polynomials in \(n\) of degree at most six, by the elementary power-sum identities. To check the resulting rational factorisations *for all* \(n\), it suffices to check seven consecutive nonnegative integer inputs. Direct substitution into the two finite-sum formulas gives:

| \(n\) | \(C_n\) | \(I_n\) |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 10 | 11 |
| 2 | 50 | 60 |
| 3 | 175 | 224 |
| 4 | 490 | 658 |
| 5 | 1176 | 1638 |
| 6 | 2520 | 3612 |

Both claimed degree-six rational polynomials agree at these seven values, so the differences are zero polynomials. This is a valid all-size polynomial identity proof; it does **not** assume that finite checking alone proves an arbitrary sequence identity.

**Monotonicity and limits.** The displayed polynomial formulas give \(p_n=5(n+2)(n+3)/(14n^2+52n+60)\). Straight algebra yields
\[
p_n-p_{n+1}=\frac{15(n+3)(3n+2)}{2(7n^2+26n+30)(7n^2+40n+63)}>0.
\]
The leading coefficients of \(C_n,I_n,N_n\) are respectively \(1/144,1/80,1/6\). They imply \(p_n\to5/14\) and \(T_n/N_n^2\to7/5\), completing the proof.

## Verification
The standalone Python 3 program `verification/check_lo_poset.py` uses only standard-library modules. It recomputes both finite cut sums for \(0\leq n\leq16\), and independently enumerates every permitted partial-order relation matrix for every possible insertion of the two labelled new points into the fixed old linear chain for \(0\leq n\leq7\). It checks the full transitivity relation rather than assuming the cut characterisation. It also checks rational count identities. The recorded output in `verification/output.txt` ends in `ALL_LO_POSET_CHECKS_OK`. The universal conclusions follow from the cut lemmas and polynomial identity argument above, not from this finite test suite.

## Relationship to prior work
Dolinka and Mašulović (2012) identify the Fraïssé limit of all finite linearly ordered posets, its homogeneous linear-extension property and its relation to the random poset (Theorem 4.8 and Section 5); they do not give chain-base pair-type census formulas. Sokić (2011) treats Ramsey properties of linearly extended finite posets, a different invariant. Previously published enumeration of finite-base tuple types **in the reduct without a distinguished linear order** gives a quartic pair-type polynomial over a named chain, not this degree-six spectrum. A separate earlier analysis of this ordered-poset expansion over individually named **antichains** obtains an exponential rather than polynomial spectrum and a \(3/7\) limiting comparability fraction; that different base family does not determine the present chain-base spectrum. A publicly available antichain spectrum for the **unexpanded** random poset concerns a different language as well. The numeric sequence \((C_n)=(1,10,50,175,\ldots)\) is already recorded independently as OEIS A006542, with a Narayana-triangle interpretation: numerical sequence priority is not claimed. The contribution here is the simultaneous *logical-type interpretation and orientation-refined enumeration*, the incomparable channel, and the sharp \(5/14\) monotone law in the homogeneous linear-extension structure.

## Limitations
The result is for finite **chains** of named parameters and pairs of distinct new points. It does not give formulas for arbitrary parameter posets, all tuple arities, or probabilities under any ambient sampling measure. Prior related enumerations could have equivalent consequences under another encoding; the novelty comparison is best-of-knowledge, not a claim of exhaustive historical priority. Numerical agreement of the comparable channel with a known sequence is explicitly disclosed.

## References
1. I. Dolinka and D. Mašulović, *Countable homogeneous linearly ordered posets*, European Journal of Combinatorics **33** (2012), 1965–1973. Online 2012-07-15. DOI: 10.1016/j.ejc.2012.06.006. https://www.academia.edu/71212826/Countable_homogeneous_linearly_ordered_posets
2. M. Sokić, *Ramsey Properties of Finite Posets*, Order **29** (2012), 1–30, online 2011-01-13. DOI: 10.1007/s11083-011-9195-3. https://www.academia.edu/95297073/Ramsey_Properties_of_Finite_Posets
3. *Order-polynomial spectra of tuple types over chains in the generic partial order*, public research record, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-order-polynomial-spectra-of-tuple-types-over-chains-in-the-gener--67a71af3c8ab
4. *Exact two-point and fixed-arity type spectra over antichains in the random poset*, public research record concerning the unexpanded random poset, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-two-point-and-fixed-arity-type-spectra-over-antichains-in--3d742ffe8f7d
5. OEIS A006542, existing numerical comparable-channel sequence, https://oeis.org/A006542.
