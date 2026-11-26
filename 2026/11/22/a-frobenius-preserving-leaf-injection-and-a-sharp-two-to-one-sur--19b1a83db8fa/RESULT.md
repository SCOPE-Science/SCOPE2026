# A Frobenius-preserving leaf injection and a sharp two-to-one surplus for multiplicity-four numerical semigroups

## Finding

Let \(L_4(F)\) and \(I_4(F)\) count, respectively, leaf and internal numerical semigroups of multiplicity \(4\) and Frobenius number \(F\), where children are taken in the **full** numerical-semigroup tree. For every integer \(F\ge3\) with \(4\nmid F\), there is an explicit injection from the leaves into the internal semigroups **preserving both multiplicity and Frobenius number**. In fact the sharp uniform bound is

\[
I_4(F)\ge 2L_4(F)+1.
\]

Equality holds **exactly** when \(F\in\{3,5,7,9,10,11\}\). The result gives a fixed-multiplicity-four, all-Frobenius-number case of the internal-versus-leaf conjecture, with a stronger strict surplus.

For complete reproducibility, write \(F=4(h-1)+r\) with \(r\in\{1,2,3\}\) and \(h\ge1\). Let \(N_4(F)=L_4(F)+I_4(F)\). The exact counts, with empty summands treated as zero, are

\[
\begin{array}{c|c|c}
r& L_4(4(h-1)+r)&N_4(4(h-1)+r)\\ \hline
1&\max\{0,\min(h-2,\lfloor(2h-1)/3\rfloor)\}&\displaystyle\sum_{c=1}^{h-1}\max\bigl\{0,\min(h-1,2c+1)-\max(1,h-1-c)+1\bigr\}\\
2&\lfloor(h-1)/2\rfloor& (\lfloor h/2\rfloor+1)\lceil h/2\rceil\\
3&h-\lceil h/3\rceil&\displaystyle\sum_{a=1}^{h}\max\bigl\{0,\min(h,2a)-\max(1,h-a)+1\bigr\}.
\end{array}
\]

The cases \(F=1,2\) (\(h=1\), \(r=1,2\)) are excluded: a multiplicity-four semigroup omits \(1,2,3\). For \(F\ge3\) with \(4\nmid F\), the table covers every admissible Frobenius number.

## Assumptions and scope

A numerical semigroup is a cofinite submonoid of \(\mathbb N_0\); its multiplicity is its least positive element and its Frobenius number is its largest omitted integer. A minimal generator greater than the Frobenius number is called *effective*. A semigroup is *internal* precisely when it has an effective generator, otherwise it is a *leaf*. These are full-tree notions; a child's multiplicity is not required to remain four.

The Apéry set of any multiplicity-four semigroup is uniquely

\[
\operatorname{Ap}(S,4)=\{0,4a+1,4b+2,4c+3\},
\]

where \(a,b,c\) are positive integers satisfying all four Kunz inequalities

\[
b\le2a,\quad c\le a+b,\quad a\le b+c+1,\quad b\le2c+1.
\]

Conversely every such triple gives a semigroup. Its Frobenius number is \(\max\{4a-3,4b-2,4c-1\}\).

## Proof

**1. Leaf partition (known structural criterion, reproduced for completeness).** Denote the three positive Apéry elements by \(w_1,w_2,w_3\). A positive Apéry element is nonminimal exactly when it is the sum of two positive Apéry elements: a summand reducible by 4 would make the sum reducible by 4. The possible equalities are \(a=b+c+1\) for \(w_1=w_2+w_3\), \(b=2a\) or \(b=2c+1\) for \(w_2=2w_1\) or \(2w_3\), and \(c=a+b\) for \(w_3=w_1+w_2\). A leaf's maximal Apéry element must be nonminimal: otherwise it is effective, since it equals \(F+4\). When \(w_1=w_2+w_3\) or \(w_3=w_1+w_2\), the two summands are below \(F\) because each positive Apéry element is at least 5. If \(b=2a\) and \(w_2\) is maximal, the inequalities give \(a\le c\le 2a-1\); at \(c=2a-1\), \(w_3>F\) is minimal because \(c<a+b\). Thus a leaf requires \(c\le 2a-2\), which puts \(w_3\le F\). If \(b=2c+1\) and \(w_2\) is maximal, the inequalities give \(c+1\le a\le 2c+1\); at \(a=2c+1\), \(w_1>F\) is minimal because \(a<b+c+1\). Thus a leaf requires \(a\le 2c\), which puts \(w_1\le F\). In the two \(w_2\) cases the doubled summand is already at most \(F\). This gives exactly the following pairwise disjoint families within the Kunz-admissible triples:

\[
\begin{array}{c|l}
\mathcal A&a=b+c+1,\\
\mathcal B&c=a+b,\\
\mathcal C&b=2a,\quad a\le c\le 2a-2,\\
\mathcal D&b=2c+1,\quad c+1\le a\le2c.
\end{array}
\]

For the ordinary triple \((1,1,1)\), the generator \(4\) exceeds \(F=3\), and it is internal. No extra leaves arise from the multiplicity itself. This four-family structural classification was already available in the 2026 genus-preserving treatment listed below and is **not claimed as new here**.

**2. New fixed-F injection.** On leaves define the map on Kunz coordinates by

\[
\Psi(a,b,c)=\begin{cases}
(a,b,c+1)&\text{if }(a,b,c)\in\mathcal A\cup\mathcal D,\\
(a+1,b,c)&\text{if }(a,b,c)\in\mathcal B\cup\mathcal C.
\end{cases}
\]

For family \(\mathcal A\), the new coordinate \(c+1\) still satisfies every Kunz inequality. The Frobenius number remains \(4a-3\), since \(w_1=4a+1\) stays above the new \(w_3=4c+7\) by \(4b-2>0\). The equality \(a=b+c+1\) becomes \(a=b+(c+1)\), so \(w_1\) becomes minimal, and thus effective. For \(\mathcal B\), increasing \(a\) preserves validity and the maximal \(w_3\), because \(w_3-(4(a+1)+1)=4b-2>0\); \(c=a+b\) becomes \(c=(a+1)+b-1\), making \(w_3\) effective. For \(\mathcal C\), increasing \(a\) preserves Kunz validity and the maximal \(w_2\), because \(4b+2-(4(a+1)+1)=4a-3>0\) and \(c\le2a-2\); it breaks the sole equality \(b=2a\) that made \(w_2\) nonminimal. For \(\mathcal D\), increasing \(c\) similarly preserves validity and the maximal \(w_2\) (the difference above new \(w_3\) is \(4c-1>0\)), while it breaks \(b=2c+1\). Thus all images are internal, with the **same** Frobenius number as their sources.

Each branch is a translation and hence injective. Branches \(\mathcal A\) and \(\mathcal B\) have Frobenius numbers congruent to \(1\) and \(3\) modulo \(4\), respectively. Branches \(\mathcal C\) and \(\mathcal D\) both have Frobenius numbers congruent to \(2\), but their maximal \(w_2=4b+2\) has respectively even and odd Kunz coordinate \(b\), so their Frobenius numbers are distinct. Therefore images from different branches cannot collide. This proves the Frobenius-preserving injection.

**3. Exact counts.** Write \(F=4(h-1)+r\). If \(r=1\), then \(a=h\), \(1\le b,c\le h-1\), and the remaining nonautomatic Kunz inequalities are \(b+c\ge h-1\) and \(b\le2c+1\). For fixed \(c\), the possible values of \(b\) lie between \(\max(1,h-1-c)\) and \(\min(h-1,2c+1)\), giving the first total. The only leaves have \(a=b+c+1\), producing the first leaf count (with the small \(h=2\) boundary handled by the maximum with zero). If \(r=2\), then \(b=h\), \(\lceil h/2\rceil\le a\le h\), and \(\lceil(h-1)/2\rceil\le c\le h-1\); the number of pairs is the middle total. The leaves lie in \(\mathcal C\) when \(h\) is even and \(\mathcal D\) when it is odd, yielding \(\lfloor(h-1)/2\rfloor\). If \(r=3\), then \(c=h\), \(1\le a,b\le h\), \(a+b\ge h\), and \(b\le2a\), giving the last sum. The leaves satisfy \(a+b=h\), with \(\lceil h/3\rceil\le a\le h-1\), yielding \(h-\lceil h/3\rceil\).

**4. The sharp two-to-one surplus.** We prove the equivalent inequality \(N_4(F)\ge 3L_4(F)+1\). If \(r=2\), put \(h=2k\) or \(2k+1\). For even \(h\ge2\), \(N_4-3L_4=k(k+1)-3(k-1)=(k-1)^2+2\), which is at least two. For odd \(h\ge3\), \(N_4-3L_4=(k+1)^2-3k=k^2-k+1\), equal to one only at \(k=1\) and greater at every \(k\ge2\).

For \(r=1\), direct substitution for \(h=2,3,4,5,6,7\) gives \((N_4,L_4)=(1,0),(4,1),(8,2),(12,3),(17,3),(23,4)\), and equality occurs only at \(h=2,3\). For every \(h\ge8\), every pair \(b,c\in[\lceil h/2\rceil,h-1]\) is allowed, and the additional pair \((b,c)=(1,h-2)\) is allowed but lies outside this square. Therefore \(N_4\ge\lfloor h/2\rfloor^2+1\). Since \(L_4\le\lfloor(2h-1)/3\rfloor\), this lower bound exceeds \(3L_4+1\) for all \(h\ge8\): for even \(h=2k\ge8\), the difference \(\lfloor h/2\rfloor^2+1-(2h-1)=k^2-4k+2\ge2\); for odd \(h=2k+1\ge11\) it is \(k^2-4k\ge5\), while at \(h=9\) the exact \(L_4=5\) gives \(17>3\cdot5+1\).

For \(r=3\), direct substitution for \(h=1,2,3,4,5\) yields \((N_4,L_4)=(1,0),(4,1),(7,2),(11,2),(16,3)\), with equality only for \(h=1,2,3\). For \(h\ge6\), all pairs \(a,b\in[\lceil h/2\rceil,h]\) are allowed, and \((a,b)=(h,1)\) is a further allowed pair outside this square. Thus \(N_4\ge(\lfloor h/2\rfloor+1)^2+1\). As \(3L_4\le2h\), this bound exceeds \(3L_4+1\) for even \(h\ge6\) and odd \(h\ge7\) by the elementary quadratic inequalities \((k+1)^2>4k\) for \(k\ge3\) and \((k+1)^2>4k+2\) for \(k\ge3\). Combining all cases, equality corresponds precisely to \(F=3,5,7,9,10,11\). \(\square\)

## Verification

`VERIFY.py` uses only the Python 3 standard library. It enumerates all Kunz-admissible triples with coordinates at most \(75\), computes real semigroup membership and minimal generators from the Apéry set independently of the four leaf formulas, and checks the counts, Frobenius preservation, target internality, and injection for **every admissible \(F\) from \(3\) through \(299\)**. It prints `VERIFY_OK F_range=3..299 leaf_checks=5093`. These finite calculations are supporting tests, **not** a proof of the unbounded statement; the preceding argument covers all \(F\).

## Relationship to prior work

Casas, Madrid and Rosales (2026), Section 6 and Conjecture 41, pose the fixed-multiplicity/fixed-Frobenius internal-versus-leaf inequality. Their Proposition 42 proves a complementary large-multiplicity range (\(m>F/2\)), not this unbounded fixed-multiplicity-four case; their Algorithm 38 and tables give finite data, including examples. The new finding is the **Frobenius-preserving injection and sharp \(I_4(F)\ge2L_4(F)+1\) theorem for all permissible \(F\)**, not the original conjecture or prior finite tables.

A 2026 genus-preserving result already gives the four-family **leaf partition** and an injection at fixed genus. That map changes Frobenius number and does not prove the present fixed-Frobenius preservation or two-to-one surplus. The four-family partition itself is explicitly prior work. An independent 2026 study enumerates two- and three-child multiplicity-four semigroups **by genus**, not by fixed Frobenius number. García-Sánchez, Marín-Aragón and Robles-Pérez (2018) give the Kunz framework and enumerate total semigroups by fixed genus, whereas Bras-Amorós and Torra (2026) provide counts under the distinct large-multiplicity condition \(m\ge(F+1)/3\), as well as finite multi-parameter computations.

## Limitations

Only multiplicity exactly four is covered. No inequality for all multiplicities, and no injection simultaneously preserving both genus and Frobenius number, is claimed. The exact fixed-F counts can be extracted from the previously known Kunz and leaf descriptions by elementary arithmetic; their standalone enumeration is not claimed as conceptually new. The all-F two-to-one internal surplus and the explicit F-preserving injection are the actual contributions. Unindexed prior computations or equivalent formulations could affect historical priority.

## References

1. M. Casas, J. A. Madrid and J. C. Rosales, *Internal numerical semigroups*, arXiv:2608.19984v1, first public August 20, 2026. https://arxiv.org/abs/2608.19984
2. P. A. García-Sánchez, D. Marín-Aragón and A. M. Robles-Pérez, *The tree of numerical semigroups with low multiplicity*, arXiv:1803.06879v1 (2018). https://arxiv.org/html/1803.06879v1
3. *A genus-preserving leaf-to-internal injection for multiplicity-four numerical semigroups* (2026-10-26), Resultary, record 786d5662b2ca.
4. *Exact two-child and three-child profiles of multiplicity-four numerical semigroups* (2026-10-25), Resultary, record 0a6ecda60e6d.
5. M. Bras-Amorós and V. Torra, *Algorithms and results on multiparameter counting of numerical semigroups*, arXiv:2607.23111 (2026). https://arxiv.org/abs/2607.23111
