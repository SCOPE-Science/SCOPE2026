# Multiplicity-two fiber rigidity for numerical-semigroup symmetrization

## Finding

Let \(\Phi\) be the symmetrization introduced by Delgado, Süer, and Yeşil [1]. For a proper numerical semigroup \(S\), it deletes from its Young diagram precisely the rows indexed by the original pseudo-Frobenius numbers other than \(F(S)\). The pseudo-Frobenius numbers are determined **before** any deletion. The map \(\Phi\) is defined on almost symmetric numerical semigroups, and its output is a symmetric numerical set [1, Theorem 4.2]. A numerical set need not be closed under addition.

For every \(g\ge1\), define \(T_g=\langle2,2g+1\rangle=\{0,2,4,\ldots,2g-2\}\cup[2g,\infty)\). This symmetric numerical semigroup has genus \(g\), conductor \(2g\) and least positive element \(2\).

**Theorem (complete multiplicity-two image and fibers).** For every proper symmetric numerical set \(T\) with least positive member \(2\), the inverse fiber of \(\Phi\) is empty unless \(T=T_g\) for a unique integer \(g\ge1\). The nonempty fibers are

\[
\Phi^{-1}(T_g)=
\begin{cases}
\{\{0\}\cup[m,\infty):m\ge2\},&g=1,\\
\{\{0,m\}\cup[m+2,\infty):m\ge2\},&g=2,\\
\{T_g\},&g\ge3.
\end{cases}
\]

In particular, within the multiplicity-two target slice every image is an actual numerical semigroup, and only the first two genera exhibit any noninjectivity. **Exponential sparsity corollary.** For every \(g\ge3\) there are exactly \(2^{g-3}\) symmetric numerical sets of genus \(g\) and least positive member \(2\), because the pairs \(\{0,2g-1\}\), \(\{1,2g-2\}\), and \(\{2,2g-3\}\) are forced, while each of the remaining \(g-3\) complementary pairs is free. The fraction belonging to the image is therefore exactly \(2^{3-g}\).

## Assumptions and scope

A *numerical semigroup* is a cofinite subset \(S\subseteq\mathbb N_0\) containing zero and closed under addition. It is *proper* when \(S\ne\mathbb N_0\). Its *conductor* is \(C=F+1\), where \(F\) is its largest gap; its *multiplicity* \(m\) is its least positive member. Write \(G=\mathbb N_0\setminus S\), \(g=|G|\), and

\[
\operatorname{PF}(S)=\{x\in G: x+s\in S\text{ for all }s\in S\setminus\{0\}\}.
\]

The type is \(t=|\operatorname{PF}(S)|\). The semigroup is *almost symmetric* if \(2g=F+t\). A *symmetric numerical set* \(T\) is a cofinite subset of \(\mathbb N_0\) containing zero for which precisely one of \(a\) and \(F(T)-a\) lies in \(T\), for every integer \(0\le a\le F(T)\). This does not assume closure of \(T\).

The inverse fiber is taken over **all** proper almost symmetric source semigroups, with no bound on their multiplicity, Frobenius number, genus or type. The theorem concerns the entire slice of target symmetric numerical sets with least positive member \(2\), and does not classify images of higher multiplicity.

## Proof

**Step 1: the first positive output member.** Let \(S\) be any proper numerical semigroup, of multiplicity \(m\ge2\), and set \(P=\operatorname{PF}(S)\setminus\{F\}\). The boundary encoding of [1, Section 4] writes an element of \(S\) as a right step and a gap as an up step. Row deletion removes exactly the up steps indexed by \(P\), preserving the original order of the other steps. Thus the first positive output member is

\[
\min(\Phi(S)\setminus\{0\})=m-a,\qquad a=|P\cap\{1,\ldots,m-1\}|.\tag{1}
\]

(The formula is valid for the row-deletion operation on all proper semigroups, regardless of almost symmetry.) Suppose the output multiplicity is \(2\). Then \(a=m-2\), so exactly one of the original low gaps \(1,\ldots,m-1\) is not deleted.

**Step 2: ordinary sources.** If \(S\) has no positive member below its conductor, then \(S=O_m:=\{0\}\cup[m,\infty)\) and \(F=m-1\). Every gap \(1,\ldots,m-1\) is pseudo-Frobenius. Deleting all but \(F\) leaves the word consisting of membership at position zero, one remaining gap, then membership from position two onward. Thus \(\Phi(O_m)=T_1\). Conversely, any source with just one positive small element is ordinary, since that member is the conductor. Each \(O_m\) is almost symmetric: genus and type both equal \(m-1\), with \(F=m-1\).

**Step 3: the low-gap obstruction for a nonordinary source.** Now let \(S\) be nonordinary. Then \(F\ge m\), so all low gaps \(1,\ldots,m-1\) differ from \(F\). By (1), there is a unique \(u\in\{1,\ldots,m-1\}\) that is not pseudo-Frobenius, and every other low gap \(i\) is pseudo-Frobenius. In particular, \(m+i\in S\) for every \(i\) in this range except \(u\). If \(m+u\in S\), all of \(m,m+1,\ldots,2m-1\) belong to \(S\); additive closure then places every integer at least \(m\) in \(S\), contrary to nonordinariness. Hence \(m+u\notin S\). If \(u\ge2\), then \(1\in\operatorname{PF}(S)\) and \(m+u-1\in S\), but their sum \(m+u\) is a gap. This contradicts the defining property of pseudo-Frobenius numbers. Therefore \(u=1\):

\[
1\notin\operatorname{PF}(S),\quad m+1\notin S,\quad
\{2,\ldots,m-1\}\subseteq\operatorname{PF}(S),\quad
\{m+2,\ldots,2m-1\}\subseteq S.\tag{2}
\]

**Step 4: nonordinary sources of multiplicity at least three.** Suppose \(m\ge3\). Since \(m\) and \(m+2\) belong to \(S\), so does \(2m\), and because \(m-1\) is pseudo-Frobenius, \(2m+1=(m+2)+(m-1)\in S\). For every \(2\le i\le m-1\), \(2m+i=m+(m+i)\in S\). Thus every integer in \([2m,3m-1]\) belongs to \(S\). Repeated addition of \(m\) then fills all integers at least \(2m\). Together with (2), this proves

\[
S=B_m:=\{0,m\}\cup[m+2,\infty),\qquad m\ge3.\tag{3}
\]

For any \(m\ge2\), \(B_m\) is a numerical semigroup with \(F=m+1\), genus \(m\), and

\[
\operatorname{PF}(B_m)=\{2,3,\ldots,m-1\}\cup\{m+1\}.
\]

The first set is empty for \(m=2\). Its type is \(m-1\), so \(2g=2m=F+t\): it is almost symmetric. Deleting the \(m-2\) pseudo-Frobenius gaps \(2,\ldots,m-1\) turns its boundary word into \(T_2=\{0,2\}\cup[4,\infty)\). Hence all \(B_m\) give the stated genus-two fiber, and no nonordinary source with \(m\ge3\) produces any other multiplicity-two target.

**Step 5: sources of multiplicity two.** Every proper numerical semigroup of multiplicity \(2\) has the unique form \(T_g=\langle2,2g+1\rangle\), for some \(g\ge1\): all even numbers occur, and the least odd member is \(2g+1\). These semigroups are symmetric, and \(\operatorname{PF}(T_g)=\{2g-1\}\). Therefore \(\Phi(T_g)=T_g\), with no rows deleted. For \(g\ge3\), Steps 2 and 4 exclude all other source multiplicities, and the fiber is the singleton \(\{T_g\}\). At \(g=1\), Step 2 provides exactly the ordinary sources, and at \(g=2\), Step 4 together with \(B_2=T_2\) supplies precisely the listed \(B_m\). This exhausts every source and proves the theorem. \(\square\)

## Verification

The self-contained Python 3 program `verify.py` enumerates every proper numerical semigroup with Frobenius number at most \(20\), computes the entire pseudo-Frobenius set by its definition, tests almost symmetry, deletes the *original* pseudo-Frobenius rows (not recomputed ones), and checks both membership and gap-coordinate formulas for the resulting target. It verifies the theorem's cases and the symmetry condition for each produced target of least positive member two. On this finite range it checked \(601\) almost symmetric sources, including \(46\) such multiplicity-two outputs. Its transcript is `VERIFY_OUTPUT.txt`; run `python3 verify.py` to reproduce it. The infinite theorem follows from Steps 1–5, not from this enumeration.

## Relationship to prior work

Delgado, Süer, and Yeşil [1] define this precise symmetrization and prove its symmetric-output property, provide counts by source Frobenius number through \(78\), exhibit noninjectivity and nonsemigroup outputs, and explicitly ask for the image to be characterized. The exact all-source fiber classification on the multiplicity-two target slice is not in their reported theorem or tables. Yeşil [2] obtains earlier Young-diagram decompositions and symmetric-set constructions, including a consecutive-pseudo-Frobenius special construction, but does not establish these inverse fibers of the new map. An independent publicly available argument [3] proves only the necessary obstruction that no image contains \(1\); that does not imply the multiplicity-two fiber classification or genus transition here. The elementary classification of multiplicity-two numerical semigroups is standard; the new part is its compatibility and precise inverse-fiber rigidity under the row-deletion operation.

## Limitations

The result covers only outputs whose least positive element is \(2\); the much larger target range with higher multiplicities remains open. The proof uses no independent formal certification. The exact theorem was checked against accessible primary papers and relevant scientific literature but was not exhaustively compared with all historic literature. Computational enumeration is finite corroboration only. Independent review has not been performed.

## References

1. M. Delgado, M. Süer, M. Yeşil, *A Symmetrization for Almost Symmetric Numerical Semigroups*, arXiv:2611.14268v1, submitted 2026-11-10. https://arxiv.org/html/2611.14268v1
2. M. Yeşil, *Young Diagram Decompositions for Almost Symmetric Numerical Semigroups*, arXiv:2504.20688v1, first posted 2025-04-29; see Sections 3–5, especially Lemma 5.7. https://arxiv.org/abs/2504.20688
3. *Surjectivity of original-row symmetrization*, public mathematical note, 2026-11-13; uniform obstruction excluding images with member \(1\), not a multiplicity-two fiber theorem. https://the-omega-institute.github.io/trureturing-mdbook/Problems/delgado-suer-yesil-2026-symmetrization-surjectivity.html
4. H. Nari, *Symmetries on almost symmetric numerical semigroups*, arXiv:1111.6211, first posted 2011-11-27; pseudo-Frobenius symmetry background. https://arxiv.org/abs/1111.6211
