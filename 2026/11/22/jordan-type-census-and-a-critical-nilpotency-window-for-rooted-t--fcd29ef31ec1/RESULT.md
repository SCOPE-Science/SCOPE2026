# Jordan-type census and a critical nilpotency window for rooted-tree incidence radicals

## Finding

Let \(b\ge2\), \(h\ge1\), and \(q\ge2\) be a prime power. Let \(T_{b,h}\) be the complete rooted \(b\)-ary tree with root at depth zero and leaves at depth \(h\), ordered by ancestry. Let \(A=I(T_{b,h},\mathbb F_q)\) be its incidence algebra, and \(J\) its Jacobson radical. Inside \(J\), let \(V\) be the canonical linear subspace of elements supported on **cover relations only**. Thus \(\dim V=E=\sum_{d=1}^{h}b^d\) and every \(X\in V\) is a nilpotent matrix on the canonical \(N=\sum_{d=0}^h b^d\)-dimensional incidence representation.

**The complete Jordan census.** Define polynomials \(H_{a}^{(j)}(x_0,\ldots,x_a)\), for \(0\le j\le a\le h\), by the following all-integer recursion. Start with \(H_0^{(0)}=x_0\). Given the polynomials at height \(a-1\), extend them to variables \(x_0,\ldots,x_a\), put

\[
A_{a-1}=\sum_{j=0}^{a-1}H_{a-1}^{(j)},\quad B_{a,j}=\sum_{i=0}^{j-1}H_{a-1}^{(i)},\quad W_{a,j}=(A_{a-1}+(q-1)B_{a,j})^b
\]

for \(0\le j\le a\), where \(B_{a,0}=0\) and \(W_{a,-1}=0\). Set

\[
H_a^{(j)}=x_j\big(W_{a,j}-W_{a,j-1}\big),\qquad P_{b,h,q}=\sum_{j=0}^{h}H_h^{(j)}.
\]

These polynomials have nonnegative integer coefficients. For every vector \(\mathbf c=(c_0,\ldots,c_h)\) of nonnegative integers, the coefficient \([x_0^{c_0}\cdots x_h^{c_h}]P_{b,h,q}\) is the **exact number** of matrices \(X\in V\) for which

\[
\operatorname{rank}(X^k)=\sum_{j=k}^{h}c_j\quad(1\le k\le h),\qquad \operatorname{rank}(X^0)=N=\sum_{j=0}^h c_j.
\]

Consequently this one finite recursion gives the number realizing **every nilpotent Jordan partition** of the canonical action, over **every** finite field. In particular, if \(r_k=\sum_{j=k}^h c_j\), \(r_0=N\), and \(r_{h+1}=r_{h+2}=0\), the number of Jordan blocks of size exactly \(k\) is \(r_{k-1}-2r_k+r_{k+1}\), for \(1\le k\le h+1\). Coefficients for different \(\mathbf c\) producing the same partition are summed. The coefficient sum of \(P_{b,h,q}\) equals \(q^E\).

**Nilpotency-index transition.** Let \(\nu_h(X)\) be the smallest positive integer \(m\) such that \(X^m=0\), for uniform \(X\in V\). Set \(\Delta_h=h+1-\nu_h(X)\). For \(p_0=1\), define

\[
p_{a+1}=1-\big(1-(1-q^{-1})p_a\big)^b.
\]

The exact probability of the maximal possible nilpotency index \(h+1\) is \(p_h\). When \((b,q)=(2,2)\), one has \(p_h\sim4/h\) and

\[
\Delta_h-\lfloor\log_2h\rfloor=O_{\mathbb P}(1).
\]

For every other \((b,q)\) with \(b\ge2\) and prime-power \(q\ge2\), the probability \(p_h\) decreases to the unique positive solution \(\rho_{b,q}\) of \(\rho=1-(1-(1-q^{-1})\rho)^b\), and \(\Delta_h=O_{\mathbb P}(1)\). For binary branching with \(q>2\), \(\rho_{2,q}=q(q-2)/(q-1)^2\).

The top-power assertion extends to **uniform elements of the whole radical** \(J\): since \(\dim J=R=\sum_{d=1}^h d b^d\), the number of \(X\in J\) with \(X^h\ne0\) is exactly \(q^R p_h\). The complete Jordan census and the claimed distribution of \(\Delta_h\) are **only** asserted for the cover-supported subspace \(V\), not for arbitrary elements of \(J\).

## Assumptions and scope

The tree has one root, exactly \(b\) children at each internal vertex, and height exactly \(h\). The canonical incidence algebra has basis the intervals \([u,v]\) with \(u\le v\) and convolution composition. Its Jacobson radical consists of strictly comparable intervals. The subspace \(V\subset J\) consists of functions supported solely on Hasse edges. The parameters \(b,h,q\) range over all stated values, with no characteristic exclusion. The Jordan partition refers to the canonical \(N\)-dimensional incidence-matrix representation, **not** the left regular action of \(X\) on \(A\).

For an edge assignment, declare an edge **open** exactly when its coefficient is nonzero. For every vertex \(v\) define \(L(v)\) to be the maximum number of open edges along a directed downward path starting at \(v\) (zero if no open child edge). Thus \(0\le L(v)\le h\). The variables \(x_j\) mark vertices having \(L(v)=j\), not matrix entries or field coordinates. The polynomial and the nilpotency law are independent of which nonzero coefficients are selected, depending only on their supports. Counts are for *labeled* tree vertices and *individual* algebra elements; no quotient by tree automorphisms is taken.

## Proof

**1. Unique-path product and rank lemma.** For every \(X\in V\), the entry \((X^k)_{u,v}\) is zero unless \(v\) is a descendant of \(u\) at graph distance precisely \(k\). In that case there is exactly one directed path from \(u\) to \(v\), so the entry equals the product of the \(k\) edge coefficients along this path. In particular it is nonzero exactly when every edge of that path is open; there are no cancellations in any characteristic. Within a fixed starting level, the nonzero rows of \(X^k\) have disjoint supports because distinct starting vertices have disjoint descendant sets. Rows at different starting levels are supported on different ending levels. Therefore all nonzero rows are linearly independent, and

\[
\operatorname{rank}(X^k)=\#\{v:L(v)\ge k\}=\sum_{j=k}^{h}c_j.
\]

This rank lemma holds over an arbitrary field and is the key link between incidence multiplication and the whole Jordan partition, as opposed to only the existence of a root-to-leaf path. The standard second-difference formula for Jordan blocks follows by applying it to the ranks of powers of a nilpotent matrix.

**2. Full multivariate recursion.** Write \(L_{\mathrm{root}}\) for the root's maximum open-path length in a subtree of height \(a\). Interpret \(H_a^{(j)}\) as the sum, over all edge assignments whose root has length \(j\), of the monomial \(\prod_{v}x_{L(v)}\). At height zero, the only vertex has length zero, giving \(x_0\). For each of the \(b\) child subtrees choose an assignment counted by \(A_{a-1}\). To ensure \(L_{\mathrm{root}}\le j\), either the edge to that child is zero (one choice, child unrestricted), or it is nonzero (\(q-1\) choices, child-root length at most \(j-1\)). Hence the total child contribution is \(A_{a-1}+(q-1)B_{a,j}\), independently raised to the power \(b\). Taking the difference between the conditions root length at most \(j\) and at most \(j-1\), then marking the root by \(x_j\), proves the recurrence for \(H_a^{(j)}\), including \(j=0\) with \(W_{a,-1}=0\). Induction proves the coefficient interpretation and nonnegativity. Evaluating all variables at one counts all edge assignments, so \(P_{b,h,q}(1,\ldots,1)=q^{E}\). The rank lemma then gives every Jordan multiplicity without needing the entries of the Jordan normal form.

**3. Exact top index and the field-order transition.** The condition \(X^h\ne0\) means that at least one root-to-leaf path is entirely open. The probability a given edge is open is \(t=1-q^{-1}\), independently for distinct edges. Thus the root survival probabilities satisfy \(p_0=1\) and \(p_{a+1}=1-(1-tp_a)^b\). This is a classical Galton–Watson/percolation recurrence; no originality is claimed for it or for the general branching threshold. Because \(bt>1\) except at \((b,q)=(2,2)\), the increasing, strictly concave function \(g(u)=1-(1-tu)^b\) has a unique nonzero fixed point \(\rho\in(0,1)\), and iteration from one decreases to \(\rho\). The binary fixed-point expression follows by solving the quadratic. At \((b,q)=(2,2)\), the recurrence becomes \(p_{a+1}=p_a-p_a^2/4\), and

\[
\frac1{p_{a+1}}-\frac1{p_a}=\frac1{4(1-p_a/4)}.
\]

Since \(p_a\downarrow0\), Cesàro averaging yields \(a p_a\to4\). More explicitly, \(3/(a+3)\le p_a\le4/(a+4)\) for every \(a\ge0\), by bounding each reciprocal increment between \(1/4\) and \(1/3\).

**4. Tightness of the nilpotency deficit.** Let \(M_h=\max_vL(v)\). By the rank lemma, \(\nu_h(X)=1+M_h\) and \(\Delta_h=h-M_h\). Fix an integer \(k\) with \(0\le k<h\). A downward open path of length at least \(h-k\) must start in one of the first \(k+1\) levels, containing \(S_k=1+b+\cdots+b^k\) vertices. Every such vertex has at most probability \(p_{h-k}\) of supporting a downward open path of length \(h-k\), so the union bound gives

\[
\Pr(\Delta_h\le k)\le S_kp_{h-k}.
\]

Conversely, each of the \(b^k\) disjoint subtrees rooted at depth \(k\) has an independent root-to-leaf open path with probability \(p_{h-k}\); their existence ensures \(M_h\ge h-k\). Hence

\[
\Pr(\Delta_h>k)\le(1-p_{h-k})^{b^k}\le\exp(-b^kp_{h-k}).
\]

At the critical binary field, use \(p_a\asymp1/a\) and choose \(k=\lfloor\log_2 h\rfloor-L\) in the first bound or \(k=\lfloor\log_2h\rfloor+L\) in the second. As \(L\to\infty\), both tails vanish uniformly for sufficiently large \(h\), proving \(\Delta_h-\lfloor\log_2h\rfloor=O_{\mathbb P}(1)\). In the supercritical cases, \(p_a\ge\rho>0\) for all \(a\), so the second bound with fixed \(k\to\infty\) establishes \(\Delta_h=O_{\mathbb P}(1)\).

**5. Whole-radical top power.** In the incidence representation of an arbitrary \(X\in J\), a factor in \(X^h\) must follow an increasing chain of \(h\) strict comparable steps. The only possible such chain runs along consecutive Hasse edges from root to a depth-\(h\) leaf, and it is unique for each leaf. Every noncover coefficient is irrelevant to \(X^h\); there are exactly \(R-E\) such freely selected coefficients. Consequently every cover-edge assignment has \(q^{R-E}\) lifts to \(J\) with the same top power, giving the stated \(q^R p_h\) maximal-index count. No assertion about smaller powers or Jordan profiles of arbitrary \(J\) follows from this argument.

## Verification

The standalone standard-library programs `verify.py` and `verify_jordan.py` and their captured text outputs provide independent finite tests of the formulae. `verify.py` uses literal incidence-matrix multiplication and actual powers in prime fields, checking root-to-leaf nonzero counts, nilpotency indices, the separate exact length-cutoff recurrence, and the entire radical at \((b,h,q)=(2,2,2)\). `verify_jordan.py` generates the multivariate recursion with integer polynomial arithmetic, independently enumerates every cover-edge assignment, determines each vertex's maximal open path directly, and converts the resulting profile to Jordan block multiplicities. The checked configurations include \((b,h,q)=(2,1,2),(2,2,2),(2,2,3),(2,3,2),(3,2,2)\). For the binary height-three tree over \(\mathbb F_2\), all \(2^{14}=16384\) cover-supported operators were enumerated and assigned to exactly 21 Jordan types. These checks establish finite cases only; the proof above establishes the all-parameter claim.

The ordinary Python command `python verify.py` and `python verify_jordan.py`, run from a directory containing these files, reproduces the attached outputs. No external packages or network access are required.

## Relationship to prior work

Khripchenko and Novikov (first public 2008) provide foundational definitions and structural descriptions of finitary incidence algebras, including the radical, but not a finite-field Jordan census of cover-supported elements. Quinn (first public 2015) connects incidence algebras to path-algebra presentations and lex-shellability, but not random Jordan types. Mohammadi, Sáenz-de-Cabezón and Wynn (first public 2015) explicitly study complete rooted-tree bond percolation, including exact reliability recursions and the classical critical threshold. The root-to-leaf survival probability, its basic recurrence and its phase transition are therefore **prior work**, not original claims. The asserted new contribution is the simultaneous **all-powers rank/Jordan distribution** in a canonical incidence-algebra subspace, with its positive finite-field counting recursion, together with the derived typical maximal-Jordan-block deficit. The latter uses known percolation estimates, but concerns the *maximum path starting anywhere*, not only root survival.

The closest identified published result on random finite incidence radical powers, *Exact maximal nilpotency-index census in layered incidence-algebra radicals* (2026), counts top-power ranks for ordinal sums of antichains by products of dense matrices. Its posets do not include the branching ancestry tree of height at least two, and it does not enumerate complete Jordan types in the cover-supported layer. Likewise the earlier height-two incidence-algebra rank studies have nilpotency class only two. The match of some intermediate percolation probabilities to previous literature is explicitly not claimed as novel.

## Limitations

The formula is a recursive complete census, not a closed product for each partition. It counts Jordan types only in the canonical incidence action of the cover-supported subspace \(V\); the full radical statement concerns **only** the maximal nilpotency index. The critical asymptotic asserts tight centered deviations, not a fully identified limiting lattice distribution. The connection to classical percolation is essential, and a more general unpublished or unidentified theorem for weighted tree shifts could imply the Jordan recurrence; independent mathematical audit and publication-priority certification have not been performed.

## References

1. N. S. Khripchenko and B. V. Novikov, *Finitary incidence algebras*, arXiv:0803.0069, first public 2008-03-01. https://arxiv.org/abs/0803.0069.
2. D. Quinn, *The incidence algebras of posets and acyclic categories*, arXiv:1501.02481, first public 2015-01-11. https://arxiv.org/abs/1501.02481.
3. F. Mohammadi, E. Sáenz-de-Cabezón and H. P. Wynn, *The algebraic method in tree percolation*, arXiv:1510.04036, first public 2015-10-14. https://arxiv.org/abs/1510.04036.
4. *Exact maximal nilpotency-index census in layered incidence-algebra radicals*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-maximal-nilpotency-index-census-in-layered-incidence-algeb--89b75cde9cfe.
