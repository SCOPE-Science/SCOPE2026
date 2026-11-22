# Maximal commutative subsemigroups of Brandt semigroups: exact size spectra and a Gaussian law

## Finding
For every finite nonempty group \(G\) and integer \(n\ge1\), the inclusion-maximal commutative subsemigroups of the Brandt inverse semigroup \(B_n(G)\) have exactly the two normal forms stated below. These yield a complete cardinality-generating polynomial, the total number of maximal commutative subsemigroups, the sharp maximum cardinality, and a limit law for the cardinality of a uniformly chosen such subsemigroup.

Let \(\mathcal A(G)\) be the set of *distinct inclusion-maximal abelian subgroups* of \(G\), and put \(M=|\mathcal A(G)|\), \(m=|G|\), and \(P_G(t)=\sum_{H\in\mathcal A(G)}t^{|H|}\). Then the exact cardinality polynomial, one term per subsemigroup, is
\[
F_{n,G}(t)=t\left[P_G(t)^n+\sum_{\substack{a,b\ge1\\a+b\le n}}\frac{n!}{a!b!(n-a-b)!}\,t^{mab}P_G(t)^{n-a-b}\right].
\]
In particular, the total number is
\[
F_{n,G}(1)=(M+2)^n-2(M+1)^n+2M^n.
\]
Writing \(h=\max\{|H|:H\in\mathcal A(G)\}\), the largest possible cardinality is \(1+h\) for \(n=1\), \(1+\max\{m,2h\}\) for \(n=2\), \(1+\max\{2m,3h\}\) for \(n=3\), and
\[
1+m\left\lfloor\frac{n^2}{4}\right\rfloor\qquad(n\ge4).
\]
For fixed \(G\), let \(X_n\) be the cardinality of a uniformly chosen inclusion-maximal commutative subsemigroup of \(B_n(G)\), and put \(p=1/(M+2)\). As \(n\to\infty\),
\[
\frac{X_n}{mn^2}\xrightarrow{\mathsf P}p^2,\qquad
\frac{X_n-mp^2n^2}{mn^{3/2}}\xrightarrow{\mathsf d}\mathcal N\bigl(0,2p^3(1-2p)\bigr).
\]
These assertions include nonabelian structure groups and the trivial group.

## Assumptions and scope
The Brandt semigroup is
\[
B_n(G)=\{0\}\sqcup\{(i,g,j):i,j\in[n],\ g\in G\},
\]
where \((i,g,j)(k,h,\ell)=(i,gh,\ell)\) when \(j=k\), and the product is zero otherwise; \(0\) is absorbing. All subsemigroups are nonempty, and "maximal commutative" means inclusion-maximal among all commutative subsemigroups of this fixed ambient semigroup, not maximal cardinality or a maximal subgroup. The set \(\mathcal A(G)\) counts actual subgroups, not conjugacy classes. The symbol \(\mathcal N(0,v)\) denotes the centered Gaussian law with variance \(v\). The limit theorem fixes \(G\) and lets the number of matrix indices \(n\) grow.

There are precisely two families of maximal commutative subsemigroups:

**Diagonal family.** For independent choices \(H_i\in\mathcal A(G)\) at all indices, take
\[
S=\{0\}\cup\bigcup_{i=1}^n\{(i,g,i):g\in H_i\}.
\]

**Rectangular family.** Take an ordered partition \([n]=A\sqcup B\sqcup D\), with \(A\ne\varnothing\) and \(B\ne\varnothing\). For every \(d\in D\), choose \(H_d\in\mathcal A(G)\). Then take
\[
S=\{0\}\cup\{(i,g,j):i\in A,\ j\in B,\ g\in G\}\cup\bigcup_{d\in D}\{(d,h,d):h\in H_d\}.
\]
The indicated normal forms are unique; there is no duplication within or between the two families.

## Proof
**Commutation restriction.** Every maximal commutative subsemigroup contains \(0\), since adjoining \(0\) preserves commutativity and closure. At a fixed diagonal position \(i\), its group-label set is a commutative subsemigroup of finite \(G\); a nonempty one is therefore an abelian subgroup. An off-diagonal element \((i,g,j)\), where \(i\ne j\), cannot commute with any nonzero diagonal element at either \(i\) or \(j\): the two products have respectively a nonzero and a zero value.

For off-diagonal elements \(x=(i,g,j)\), \(y=(k,h,\ell)\), commutation is equivalent to both products being zero. Indeed, if \(j=k\) then \(xy\ne0\); if also \(\ell=i\), the reverse product \(yx\) is a distinct diagonal-coordinate element, not equal to \(xy\), while otherwise \(yx=0\). Thus \(xy=yx\) demands \(j\ne k\) and \(\ell\ne i\). Consequently, for any commuting off-diagonal collection, its set \(A\) of source indices and set \(B\) of target indices are disjoint. All its elements have coordinates in \(A\times B\), and every pair of such coordinates supports commuting elements, independently of labels.

**Maximality and uniqueness.** If there are no off-diagonal elements, all diagonal positions must be occupied: any absent position can receive its group identity without disturbing commutativity. Each occupied abelian subgroup must be inclusion-maximal in \(G\), yielding exactly the diagonal family. If off-diagonal elements exist, their nonempty source and target sets \(A,B\) are disjoint. No diagonal position in \(A\cup B\) can occur. Conversely, every vertex outside \(A\cup B\) must support a maximal abelian subgroup, since such a diagonal commutes with all existing off-diagonals. Every possible off-diagonal \((i,g,j)\) with \(i\in A,j\in B,g\in G\) must occur, because adjoining it cannot spoil commutativity or closure (its products with all present off-diagonals are zero, and no diagonals share its endpoints). This produces precisely the rectangular family. In either constructed family, any omitted nonzero element either has a prohibited diagonal index or has an off-diagonal endpoint conflicting with one of the present diagonal identities or off-diagonal edges; hence it cannot be adjoined while retaining commutativity. Finally the occupied off-diagonal source and target sets, and the diagonal label groups, recover all parameters uniquely. Each family is closed under products: cross-position diagonal products and all products with a rectangular off-diagonal element are zero, while diagonal groups are closed.

**Exact enumeration.** A diagonal-family member has size \(1+\sum_i|H_i|\), so the associated polynomial is \(tP_G(t)^n\). For a rectangular member with \(|A|=a\), \(|B|=b\), and \(|D|=n-a-b\), there are \(n!/(a!b!(n-a-b)!)\) ways to assign the labeled indices and its size is \(1+mab+\sum_{d\in D}|H_d|\). Summing these monomials proves the displayed polynomial. On setting \(t=1\), the rectangular-family total is the count of words of length \(n\) over \(M+2\) colors, with both distinguished colors present. Inclusion-exclusion gives \((M+2)^n-2(M+1)^n+M^n\); adding the \(M^n\) diagonal members gives the total formula.

**Sharp size bound.** Every chosen abelian subgroup has size at most \(h\le m\). A diagonal-family member has at most \(1+nh\) elements. A rectangular member with \(d=n-a-b\) has at most \(1+mab+dh\le1+m(\lfloor(n-d)^2/4\rfloor+d)\). For \(n\ge4\) and \(1\le d\le n-2\), \(\lfloor(n-d)^2/4\rfloor+d<\lfloor n^2/4\rfloor\); also \(n\le\lfloor n^2/4\rfloor\). For \(d=0\), choose a balanced split of \([n]\) into nonempty \(A,B\) to attain \(1+m\lfloor n^2/4\rfloor\). The exceptional values for \(n=1,2,3\) follow by listing the possible positive values of \(a,b\) and the diagonal case. For \(n\ge5\), only balanced, zero-\(D\) rectangular members attain the maximum. At \(n=4\), the diagonal family can tie when \(G\) is abelian.

**Asymptotics.** Form an i.i.d. length-\(n\) word in an alphabet consisting of distinct symbols \(\mathtt A\), \(\mathtt B\), and one symbol for each actual subgroup \(H\in\mathcal A(G)\). Condition on the word containing both \(\mathtt A\) and \(\mathtt B\). Every such word encodes exactly one rectangular-family member, and conditional on the event, all such members are equally likely. There are \(M^n\) additional diagonal members. Their share among all maximal commutative subsemigroups tends to zero exponentially, and the probability that an unconditioned word omits either distinguished color is at most \(2((M+1)/(M+2))^n\). Hence the law of a uniform maximal commutative member differs in total variation by an exponentially vanishing quantity from the law derived from an unconditioned word.

If \(A_n,B_n\) count occurrences of the two distinguished colors in that unconditioned word, then \((A_n,B_n)\) is multinomial with mean \((np,np)\), covariance matrix \(n\begin{psmallmatrix}p(1-p)&-p^2\\-p^2&p(1-p)\end{psmallmatrix}\), and obeys the multivariate central limit theorem. Its encoded size differs from \(1+mA_nB_n\) by at most \(nh\). The law of large numbers gives \(A_nB_n/n^2\to p^2\) in probability, and the delta method for multiplication, whose gradient at \((p,p)\) is \((p,p)\), gives asymptotic variance \(2p^3(1-2p)\) on the \(n^{3/2}\) scale. The bounded diagonal contribution vanishes on both normalized scales, proving the limit laws.

## Verification
`CHECK.py` implements Brandt multiplication directly, enumerates every maximal commuting clique via an independent Bron--Kerbosch search, checks that each such clique is a product-closed subsemigroup, and compares its exact set of elements and cardinalities with the two classification formulas. Its recorded replay in `CHECK_OUTPUT.txt` passes ten instances: trivial, cyclic order-two and order-three groups for indices up to four, and the nonabelian symmetric group on three letters for two and three indices. For the latter, the four actual maximal abelian subgroups are all enumerated and used, rather than assuming \(G\) abelian. The final line is `VERIFY_OK`. These are finite corroborations; all general quantifiers and the limit law rest on the mathematical proof, not the sample enumeration.

## Relationship to prior work
Kumar and Krishna [1, Sections 1--3] analyze largest *proper* subsemigroups and the large rank of Brandt semigroups. Their extremum is over arbitrary subsemigroups and does not determine the present commutative family or its size distribution. Margolis, Rhodes and Silva [2, Section 5] describe subsemigroups of aperiodic Brandt semigroups by transitive relations, and their maximal nilpotent subsemigroups are parametrized by strict orders; that result covers broader subsemigroup structural context, but does not itself give this commutative maximal-family polynomial with arbitrary structure group. Ballester-Bolinches and Pérez-Calabuig [3] study the abelian kernel of an inverse semigroup via relational morphisms, not the family of maximal commuting subsemigroups.

Published results on finite commutative divisors of Brandt semigroups [4], and more generally completely \(0\)-simple Rees semigroups [5], already show that an **abstract** commutative quotient has a zero-disjoint-union-of-groups-and-annihilators structure. These antecedents encompass a structural shadow of the present classification. The added statement concerns *all maximal embedded commutative subsemigroups within one fixed* \(B_n(G)\), how they depend on the **actual maximal abelian subgroups of that fixed group**, their exact cardinality spectrum, and the Gaussian size limit. No claim is made to have originated the abstract decomposition. A study of commuting graphs of completely simple (rather than completely \(0\)-simple) Rees semigroups [6] identifies their largest commuting subsemigroups as group pieces; the absence of the Brandt zero changes the relevant multiplication and permits no rectangular zero-product family. Its available published text was inspected at Corollary 3.5, but a full publisher copy was inaccessible.

## Limitations
The classification is for Brandt semigroups with identity sandwich matrix, not arbitrary completely \(0\)-simple sandwich matrices, and for *commutative* rather than merely nilpotent or solvable subsemigroups. The Gaussian limit fixes \(G\); no claim is made for simultaneously growing structure groups. The polynomial depends on the list of maximal abelian subgroups of \(G\), so it does not eliminate the independent group-theoretic problem of determining those subgroups. Small direct computations do not verify the unrestricted theorem or limiting normality. Historical priority remains a residual risk: a stronger older classification of maximal commuting cliques in Brandt semigroups might imply these expressions without using their exact wording.

## References
[1] J. Kumar and K. V. Krishna, *The Large Rank of a Finite Semigroup using Prime Subsets*, arXiv:1308.5382, first version public 2013-08-25, https://arxiv.org/abs/1308.5382.

[2] S. Margolis, J. Rhodes and P. V. Silva, *On the subsemigroup complex of an aperiodic Brandt semigroup*, arXiv:1705.04956 (2017), https://arxiv.org/abs/1705.04956.

[3] A. Ballester-Bolinches and V. Pérez-Calabuig, *The Abelian Kernel of an Inverse Semigroup*, Mathematics 8 (2020), article 1219, https://doi.org/10.3390/math8081219.

[4] *Commutative Brandt divisors coincide with embeddings, with the sharp matrix index*, published 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-commutative-brandt-divisors-coincide-with-embeddings-with-the-sh--375b1d05a823.

[5] *Commutative divisors of finite completely zero-simple semigroups collapse to Brandt embeddings*, published 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-commutative-divisors-of-finite-completely-zero-simple-semigroups--64205f67af4f.

[6] *Commuting graphs of completely simple semigroups*, Communications in Algebra (2025), https://doi.org/10.1080/00927872.2025.2481079.
