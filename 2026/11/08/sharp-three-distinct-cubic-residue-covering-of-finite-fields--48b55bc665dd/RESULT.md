# Sharp three-distinct-cubic-residue covering of finite fields

## Finding
For every prime power \(q\equiv1\pmod 3\), let \(H_q=\{x^3:x\in\mathbb F_q^\times\}\), the multiplicative subgroup of nonzero cubic residues, and define its **restricted threefold sumset**
\[
\Sigma_3(H_q)=\{a+b+c:a,b,c\in H_q\ \text{pairwise distinct}\}.
\]
Then
\[
\boxed{\Sigma_3(H_q)=\mathbb F_q\quad\Longleftrightarrow\quad(q=37)\ \text{or}\ (q\ge49).}
\]
Thus the least uniform lower bound for complete coverage is \(q=49\): the field of order \(43\) still misses zero. The isolated earlier full-covering field has order \(37\). The quantifier ranges over **all prime powers**, including fields of characteristic two, not only prime fields.

## Assumptions and scope
The sole assumption is that \(q=p^e\) is a prime power congruent to \(1\pmod3\). The subgroup \(H_q\) contains \(h=(q-1)/3\) elements. Three summands must be **distinct elements of the subgroup**; distinct cube roots are not sufficient. Every target \(b\in\mathbb F_q\), including zero, is included in the assertion. The formula gives existence and the exact cutoff, not a general closed form for target representation multiplicities.

## Proof
**1. Large fields.** Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\) and a multiplicative character \(\chi\) of order three. For \(u\in\mathbb F_q\), put \(S(u)=\sum_{x\in H_q}\psi(ux)\). Then \(S(0)=h\). For \(u\ne0\), expressing the indicator of \(H_q\) on nonzero elements by cubic characters gives
\[
S(u)=\frac{-1+\chi(u)^{-1}G(\chi)+\chi(u)^{-2}G(\chi^2)}{3},
\qquad |S(u)|\le B:=\frac{1+2\sqrt q}{3},
\]
where \(G(\eta)=\sum_{x\ne0}\eta(x)\psi(x)\), and the standard nontrivial Gauss-sum identity \(|G(\eta)|=\sqrt q\) holds over every finite field, including characteristic two.

Let \(T_b\) be the count of **ordered, unrestricted** triples in \(H_q^3\) summing to \(b\). Additive-character orthogonality yields
\[
T_b=\frac1q\left(h^3+\sum_{u\ne0}S(u)^3\psi(-ub)\right)
\ge\frac{h^3-(q-1)B^3}{q}.
\]
Let \(R_b\) count ordered triples with pairwise distinct entries. For each of the three coordinate-equality events \(x=y\), \(x=z\), or \(y=z\) in a triple \((x,y,z)\) summing to the target, choosing the common coordinate in \(H_q\) determines the third from the sum. Thus at most \(h\) solutions lie in each event, in every characteristic. The union bound gives \(R_b\ge T_b-3h\). Substitution and algebra provide the **uniform explicit lower bound**
\[
R_b\ge\frac{q-1}{27q}\left((q-1)^2-(1+2\sqrt q)^3-27q\right).
\]
Writing \(t=\sqrt q\), the parenthesis becomes \(t(t^3-8t^2-41t-6)\). At \(t=13\), the cubic equals \(306>0\), and its derivative \(3t^2-16t-41\) is positive and increasing for \(t\ge13\). Hence the lower bound is strictly positive whenever \(q\ge169\). This proves \(R_b>0\) for **every** target in every such field.

**2. The finite interval.** The only prime powers satisfying \(4\le q<169\) and \(q\equiv1\pmod3\) are
\[
4,7,13,16,19,25,31,37,43,49,61,64,67,73,79,97,103,109,121,127,139,151,157,163.
\]
The companion standalone verifier constructs every one of these \(24\) fields explicitly, takes all nonzero cubes, and enumerates every three-element subset of the resulting subgroup. The exact numbers of **missing** target residues at orders below \(49\) are

| \(q\) | \(4\) | \(7\) | \(13\) | \(16\) | \(19\) | \(25\) | \(31\) | \(37\) | \(43\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Missing | 4 | 7 | 9 | 6 | 6 | 1 | 1 | 0 | 1 |

At every eligible order from \(49\) through \(163\), every target has at least one three-element representation. These results follow from a **finite exhaustive calculation**, not from numerical sampling or interpolation. In the nonprime cases the verifier uses explicit binary- or quadratic-polynomial field representations, checks the finite-field property for every nonzero element, and evaluates the complete sum spectrum. There are \(131116\) distinct unordered triples across these fields; each is checked exactly once.

The finite exhaustive certificate and the analytic argument for \(q\ge169\) cover all allowed prime powers, proving the equivalence.

## Verification
Run `python3 verify_cubic_three_sums.py` with Python 3 and its standard library. It prints one line per allowed prime power below \(169\), with the subgroup size, number of missed targets, and minimum/maximum representation fibers. It terminates with `VERIFY_OK fields=24 distinct_triples=131116 threshold=49 exceptional_covering_field=37`. Its enumeration is complete for the specified finite range. The Gauss-sum bound and its strict positivity for \(q\ge169\) are proven symbolically above, not extrapolated from computation.

## Relationship to prior work
Zhu and Wan, *An Asymptotic Formula For Counting Subset Sums Over Subgroups Of Finite Fields* (first public preprint, December 31, 2010), treat general multiplicative subgroups and distinct-coordinate subset sums. Their Theorem 1.1 and Section 4 provide asymptotic representation estimates, while their positivity corollaries assume a subset size growing beyond logarithmic bounds; they do not state or imply the exact three-summand, index-three cutoff or the \(37\)/\(43\) contrast. The 2017 work of Wang, Wang, and Zhou gives an exact formula for the index-**two** subgroup of quadratic residues, not index three. Ge, Li, and Wang (2022), Theorem 1.4, explicitly determine numbers of zeros of some diagonal cubic equations over **prime** fields; their zero-target formulas may imply zero-target subcases of the present question after removing repeated values, which are **not** independently claimed as novel. They do not determine the simultaneous all-target, all-prime-power restricted-sumset cutoff. Classical cubic character and Gauss-sum facts are used as established ingredients.

## Limitations
The theorem does not cover \(q\not\equiv1\pmod3\), where the nonzero cubes are not an index-three subgroup; it also does not classify the exact number of representations for individual targets. The small-field part is an exhaustive, reproducible finite certificate; future independent reproduction of the code and a broader historical-priority search remain desirable. No independent scientific audit has been performed.

## References
1. G. Zhu and D. Wan, *An Asymptotic Formula For Counting Subset Sums Over Subgroups Of Finite Fields*, arXiv:1101.0289v1 (submitted 2010-12-31), https://arxiv.org/html/1101.0289v1 .
2. W. Wang, L. Wang, H. Zhou, *Subset Sums of Quadratic Residues over Finite Fields*, arXiv:1702.03028 (2017), https://arxiv.org/abs/1702.03028 .
3. W. Ge, W. Li, T. Wang, *A remark for Gauss sums of order 3 and some applications for cubic congruence equations*, AIMS Mathematics 7 (2022), 10671–10680, https://doi.org/10.3934/math.2022595 .
