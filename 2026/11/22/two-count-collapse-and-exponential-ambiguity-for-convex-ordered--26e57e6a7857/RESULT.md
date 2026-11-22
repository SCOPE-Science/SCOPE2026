# Two-count collapse and exponential ambiguity for convex ordered equivalence bases

## Finding
Let \(M=(\mathbb Q^2,<_{\mathrm{lex}},E)\), with lexicographic order and \(E((a,b),(c,d))\) precisely when \(a=c\). This is the countable homogeneous limit of finite linearly ordered equivalence relations with convex classes. Let \(A\subseteq M\) be a finite set of individually named parameters. Write \(n=|A|\) and let \(k\) be the number of equivalence classes meeting \(A\); for the empty base, put \(n=k=0\). Let \(t_r(A)\) be the number of complete types over \(A\) of ordered \(r\)-tuples of pairwise distinct elements outside \(A\), for every integer \(r\ge0\).

The entire numerical spectrum is

\[
\boxed{\sum_{r\ge0}\frac{t_r(A)}{r!}z^r=\frac{(1-z)^{1-n}}{(1-2z)^{k+1}}.}
\]

In particular,

\[
t_1(A)=n+2k+1,\qquad t_2(A)=t_1(A)^2+n+4k+3,
\]

and therefore the first two counts uniquely recover both parameters without advance knowledge of the base cardinality:

\[
\boxed{k=\frac{t_2(A)-t_1(A)^2-t_1(A)-2}{2},\qquad n=t_1(A)-2k-1.}
\]

Two bases have identical complete numerical spectra in every arity if and only if their pairs \((n,k)\) agree. For \(n\ge1\) and \(1\le k\le n\), the exact number of pairwise nonisomorphic finite ordered parameter structures in this spectrum fibre is \(\binom{n-1}{k-1}\). Its maximum for fixed \(n\) is \(\binom{n-1}{\lfloor(n-1)/2\rfloor}\), which grows as \(2^{n-1}\sqrt{2/(\pi(n-1))}\). The first distinct base structures with identical spectra occur at \(n=3,k=2\), with ordered class sizes \((1,2)\) and \((2,1)\). The first count alone cannot recover \((n,k)\): bases with \((n,k)=(2,2)\) and \((4,1)\) both have \(t_1=7\) but have \(t_2=62\) and \(t_2=60\), respectively.

There is a sharp contrast with a natural, relation-refined numerical spectrum. If the \(k\) represented classes contain \(m_1,\ldots,m_k\) named points in their order along the quotient, for \(r\ge1\) let \(C_r(A)\) count types in which all \(r\) new points lie in one common equivalence class represented in \(A\). Then

\[
\boxed{C_r(A)=r!\sum_{i=1}^{k}\binom{m_i+r}{r}.}
\]

Once \(k\) is known, the \(k\) values \(C_1(A),\ldots,C_k(A)\) determine the unordered multiset of class sizes. Thus the unrefined entire spectrum loses the class-size information, while finitely many relation-refined channels recover its unordered content. For example, the four-point bases with ordered class sizes \((1,3)\) and \((2,2)\) share all unrefined counts, including \(t_1=9\) and \(t_2=96\), but have \(C_2=26\) and \(C_2=24\).

## Assumptions and scope
The language has exactly the binary strict order and the binary equivalence relation. All classes of \(E\), and the quotient order of classes, are dense linear orders without endpoints. Old parameters are named individually, not merely setwise. New tuple entries are required to be mutually distinct and different from old parameters; the empty new tuple is allowed. Homogeneity and the finite relational language ensure that finite induced extension diagrams classify complete types over a fixed finite parameter set.

## Proof
Order the \(n\) old elements increasingly. Convexity partitions them into \(k\) successive nonempty represented classes with lengths \(m_1,\ldots,m_k\), with \(m_1+\cdots+m_k=n\). Every finite order-and-equivalence extension pattern satisfying convexity is realized inside \(M\), and two such patterns are automorphic over \(A\) exactly when their induced diagrams agree. It suffices to enumerate increasing arrangements of anonymous new points, then multiply the count at arity \(r\) by \(r!\) for their distinct coordinate labels.

Inside represented class \(i\), there are \(m_i+1\) order gaps between and outside the already named points. Placing arbitrary numbers of increasing new points in these gaps has ordinary generating function \((1-z)^{-(m_i+1)}\). Multiplying over represented classes gives \((1-z)^{-(n+k)}\).

Outside those classes, there are exactly \(k+1\) open gaps in the quotient order of classes. Every new, unrepresented equivalence class in a quotient gap must contain a nonempty consecutive run of the new points; a single such run has generating function \(z/(1-z)\). An ordered finite sequence of such classes consequently contributes \(1/(1-z/(1-z))=(1-z)/(1-2z)\). The \(k+1\) quotient gaps contribute \(((1-z)/(1-2z))^{k+1}\), independently of the sizes of the represented classes. Multiplication proves the displayed generating function, including the empty parameter case.

Logarithmic differentiation at zero gives \(t_1=n+2k+1\) and \(t_2-t_1^2=n+4k+3\). Solving these two equations yields the inverse formulas. Therefore two spectra are equal precisely when their pairs \((n,k)\) are equal. Ordered finite convex equivalence structures with these parameters correspond bijectively to positive ordered compositions of \(n\) into \(k\) parts, whose count is \(\binom{n-1}{k-1}\). Maximizing the binomial coefficient and applying the central-binomial asymptotic proves the stated exponential fibre size. The indicated small bases prove the first collision and the necessity of the second count when \(n\) is not known.

If all \(r\ge1\) new points occupy the same already represented class \(i\), the number of increasing placements among its \(m_i+1\) gaps is \(\binom{m_i+r}{r}\). These conditions for distinct represented classes are disjoint; summing and multiplying by \(r!\) proves the channel formula. Each polynomial \(\binom{X+r}{r}\) has degree \(r\) and nonzero leading coefficient \(1/r!\). Consequently the first \(k\) normalized channel counts, together with the known number \(k\) of terms, successively determine the first \(k\) power sums of \(m_1,\ldots,m_k\). Newton's identities recover the monic polynomial with these integers as its roots, hence their unordered multiset. This proves all assertions.

## Verification
The standalone standard-library program `verify_counts.py` directly enumerates finite order/equivalence extension diagrams using old-point interleavings and every subset of potential equivalence cuts, independently of the generating-function counting argument. The recorded output is in `verification_output.txt`. It checks all ordered class-size compositions for \(0\le n\le6\), arities \(0\le r\le3\), and also arity four for \(0\le n\le4\), for 272 direct comparisons. It further checks 5,051 algebraic inverse reconstructions for \(0\le n\le100\). It compares the two four-point refined channels. These finite checks support but do not replace the preceding proof for arbitrary parameters and arities.

## Relationship to prior work
Kechris, Pestov and Todorcevic established the convex-equivalence Fraïssé class and its lexicographic \(\mathbb Q^2\) limit (their Section 6 and Theorem 6.6). Dorais, Gubkin, McDonald and Rivera developed the broader Ramsey and ordered-convex-equivalence framework. Cameron established general permutation-group orbit-series operations and a point-stabilizer construction. Coulson, Dobrinen and Patel explicitly analyzed one-point coding trees for this convex-equivalence limit in their Section 4.1, Example 4.6. These works supply the model and general counting background; the specific unrefined all-arity pointed spectrum, two-count inversion, exact nonisomorphic fibre classification, and refined recovery contrast were not identified in the inspected relevant material. General group-theoretic machinery can support deriving these results, but the stated parameter-specific reconstruction and collision classification require the explicit calculation above. Earlier equivalent formulations remain possible.

## Limitations
This concerns the complete type-counting sequence for pairwise-distinct nonparameter tuples in the explicitly named relational language, not geometric random sampling, arbitrary weak orders, or expansions with different relations. The unrefined series does not recover the order or sizes of represented equivalence classes. The refined channel recovers only the unordered multiset, not its placement order. Small finite computations do not prove the infinite theorem. Publication priority remains provisional, and there has been no independent mathematical audit.

## References
- A. S. Kechris, V. G. Pestov and S. Todorcevic, *Fraïssé Limits, Ramsey Theory, and Topological Dynamics of Automorphism Groups*, arXiv:math/0305241, first submitted 16 May 2003, especially Section 6, Theorem 6.6. https://arxiv.org/abs/math/0305241
- F. G. Dorais, S. Gubkin, D. McDonald and M. Rivera, *Automorphism Groups of Countably Categorical Linear Orders are Extremely Amenable*, arXiv:1202.4092, 18 February 2012. https://arxiv.org/abs/1202.4092
- P. J. Cameron, *Sequences Realized by Oligomorphic Permutation Groups*, Journal of Integer Sequences 3 (2000), Article 00.1.5, Sections 4–5. https://cs.uwaterloo.ca/journals/JIS/VOL3/groups.html
- R. Coulson, N. Dobrinen and R. Patel, *Fraïssé Classes with Simply Characterized Big Ramsey Degrees*, arXiv:2010.02034, Section 4.1, Example 4.6. https://arxiv.org/abs/2010.02034
