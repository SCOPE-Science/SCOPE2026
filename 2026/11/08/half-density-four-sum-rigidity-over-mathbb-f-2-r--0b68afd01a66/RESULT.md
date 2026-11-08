# Half-density four-sum rigidity over \(\mathbb F_2^r\)

## Finding

Let \(r\ge4\), let \(V=\mathbb F_2^r\), and let \(A\subseteq V\) have exactly \(2^{r-1}\) elements. Write
\[
\Sigma_4(A)=\{a_1+a_2+a_3+a_4:\ a_i\in A\text{ pairwise distinct}\}.
\]
For every \(r\ge5\), the restricted four-sumset is incomplete, \(\Sigma_4(A)\ne V\), **if and only if** \(A\) is an affine hyperplane. In that case \(\Sigma_4(A)\) is precisely the direction hyperplane, so exactly \(2^{r-1}\) target sums are absent. Consequently there are exactly \(2(2^r-1)\) non-covering half-sized subsets in dimension \(r\ge5\).

At \(r=4\), there are exactly \(870\) non-covering eight-element subsets, split into \(30\) affine hyperplanes (each with eight missing sums) and \(840\) non-hyperplanes (each with exactly one missing sum). The latter are characterized as follows: there is a unique nonzero \(g\in V\) for which \(A\) is the complete inverse image under \(V\to V/\langle g\rangle\cong\mathbb F_2^3\) of an affinely independent four-element set. This \(g\) is exactly the omitted four-sum target. The finite exceptional count is consistent with the previously published census of eight-point Walsh spectra; the independent claim of value here is the unrestricted higher-dimensional inverse theorem.

## Assumptions and scope

All vector spaces, sums, and affine subspaces are over \(\mathbb F_2\). The four elements in \(\Sigma_4(A)\) must be distinct. A hyperplane means a coset of a codimension-one linear subspace; its *direction* is that subspace. A four-element subset \(B\subseteq\mathbb F_2^3\) is affinely independent precisely when the sum of all its members is nonzero. The result assumes \(|A|=|V|/2\) and \(r\ge4\); no assertion about odd characteristic or other densities is intended.

## Proof

Put \(m=2^{r-1}\), so \(|V|=2m\) and \(|A|=m\ge8\). For any target \(g\in V\), call \(g\) *absent* if \(g\notin\Sigma_4(A)\).

**1. Zero is never absent.** There are \(\binom m2\) unordered pairs of distinct elements of \(A\), all with nonzero sums. There are at most \(2m-1\) possible such sums. Since \(\binom m2>2m-1\) for \(m\ge8\), two different pairs have the same sum. In characteristic two, pairs with the same sum cannot share exactly one endpoint, so the four endpoints are distinct and sum to zero. Hence \(0\in\Sigma_4(A)\).

**2. Quotient by a nonzero absent target.** Fix \(g\ne0\) assumed absent, and let \(Q=V/\langle g\rangle\), which has \(m\) elements. Every fiber of the quotient consists of a pair \(\{x,x+g\}\). Let \(f,s,z\) be the numbers of full, singly occupied, and empty fibers of \(A\). From \(2f+s=m\) and \(f+s+z=m\), obtain \(z=f\), \(s=m-2f\), and \(0\le f\le m/2\). Let \(B\subseteq Q\) consist of the occupied fibers, so \(|B|=m-f\).

Suppose that \(u_1,u_2,u_3,u_4\) are four **distinct** elements of \(B\) summing to zero and at least one of their fibers is full. Choosing one representative from each fiber gives a four-element subset of \(A\); replacing its representative in the full fiber by the other representative toggles the sum by \(g\). Since the image sum in \(Q\) vanishes, these two possible sums in \(V\) are exactly \(0\) and \(g\). Thus the absence of \(g\) forbids every such four-element zero-sum configuration in \(B\).

**3. If no fiber is full, \(A\) is an affine hyperplane.** When \(f=0\), \(B=Q\) and \(A\) is a transversal of all quotient fibers. Choose a linear section \(j:Q\to V\) and write the representative over \(u\) as \(j(u)+\phi(u)g\), where \(\phi:Q\to\mathbb F_2\). For any two independent \(a,b\in Q\) and any \(u\in Q\), the four quotient points \(u,u+a,u+b,u+a+b\) are distinct and sum to zero. Their unique selected lifts sum to \(\bigl(\phi(u)+\phi(u+a)+\phi(u+b)+\phi(u+a+b)\bigr)g\). As \(g\) is absent, every such second difference vanishes. For a fixed nonzero \(a\), this shows \(\phi(u)+\phi(u+a)\) is invariant under translation by every \(b\) independent of \(a\), and it is trivially invariant under translation by \(a\); therefore it is constant in \(u\). All first differences are constant, so \(\phi\) is affine. Its graph \(A\) is an affine hyperplane in \(V\).

**4. Full fibers force the small exceptional case.** Suppose \(f>0\) and pick a full fiber \(u\in B\). Put \(C=(B-u)\setminus\{0\}\subseteq Q\). A relation among three distinct \(x,y,z\in C\) of the form \(x+y=z\) would give four distinct quotient elements \(u,u+x,u+y,u+z\) summing to zero and including the full fiber \(u\), a contradiction to Step 2. Therefore \(C\) is sum-free. For any fixed \(c\in C\), the sets \(C\) and \(c+C\) are disjoint; hence \(2|C|\le m\), i.e. \(|B|-1\le m/2\). Since \(|B|=m-f\), we conclude \(f\ge m/2-1\). Thus only \(f=m/2-1\) and \(f=m/2\) remain.

If \(f=m/2-1\), then \(s=2\) and \(|B|=m/2+1\). In the \(m\)-element group \(Q\), the \(\binom{m/2+1}{2}>m-1\) unordered pairs from \(B\) therefore include two pairs with equal nonzero sum, and those pairs are disjoint. Their four endpoints form a zero-sum configuration. Since at most two occupied fibers are singleton, at least one of the four is full, contradicting Step 2.

Hence \(f=m/2\), so \(s=0\) and \(B\) has \(m/2\) members, **all** corresponding to full fibers. For \(m\ge16\), \(\binom{m/2}{2}>m-1\), and the same pair-collision argument produces a zero-sum quadruple of occupied fibers, contrary to Step 2. Thus \(m=8\), or equivalently \(r=4\), is the sole possibility. In this case \(B\) has four members and no zero-sum four-tuple: it is affinely independent in \(Q\cong\mathbb F_2^3\). Conversely, the complete lift of an affinely independent four-set contains no four distinct elements summing to \(g\): a four-sum of target \(g\) cannot use a full pair plus two other distinct points (nor two full pairs), so it would need four distinct quotient fibers whose sum is zero, contrary to affine independence.

**5. Hyperplane images and the number of exceptions.** If \(A=a+H\) is an affine hyperplane, every four-sum belongs to \(H\). Conversely, for \(h\ne0\) in \(H\), choose \(u,v\) so that \(h,u,v\) are linearly independent in \(H\); then \(0,u,v,h+u+v\) are four distinct members of \(H\) summing to \(h\). For \(h=0\), choose independent \(u,v\in H\) and the four distinct points \(0,u,v,u+v\). Translating all four summands by \(a\) preserves their sum, hence \(\Sigma_4(A)=H\). There are \(2(2^r-1)\) affine hyperplanes in \(V\).

At \(r=4\), there are \(30\) affine hyperplanes. For each \(g\ne0\), the quotient \(Q\cong\mathbb F_2^3\) has \(\binom84=70\) four-sets, of which \(14\) are affine planes (seven direction planes with two cosets each), leaving \(56\) affinely independent four-sets. Each such lift is non-hyperplanar. Moreover, its translation stabilizer is exactly \(\{0,g\}\): an additional period would descend to a nonzero translation period of \(B\); any four-set invariant under a nonzero translation is a union of two pairs and therefore has sum zero, contradicting affine independence. By Steps 3–4, any other absent target \(h\ne g\) would itself be a translation period of this non-hyperplanar set, impossible. Thus the omitted target is unique, and the \(15\) possible \(g\)'s give disjoint families of size \(56\), or \(840\) exceptional nonhyperplanes. Together with the \(30\) hyperplanes, this yields \(870\) non-covering half-sized subsets in dimension four, completing the classification. \(\square\)

## Verification

The accompanying `verify.py` uses only exact integer and binary-vector operations. It enumerates all \(\binom{16}{8}=12{,}870\) eight-subsets of \(\mathbb F_2^4\), directly forms the four-sum support, and checks the three classes and their missing-target counts: \(12{,}000\) covering sets, \(840\) nonhyperplanes with one missing target, and \(30\) affine hyperplanes with eight missing targets. It independently checks the lift/period characterization. For \(\mathbb F_2^5\), it checks all \(62\) hyperplanes and a fixed-seed sample of \(2000\) half-sized subsets. Run `python verify.py` with Python 3.10 or newer. These finite checks do not replace the infinite proof.

## Relationship to prior work

Roth and Lempel (1992, Theorem 3.1) determined the critical threshold: in the relevant range, every subset with more than half the elements represents every target as a restricted four-sum. This threshold and the hyperplane counterexample are **not** new. The theorem proved here instead classifies **all** half-sized failures in every binary dimension \(r\ge4\) and shows that for \(r\ge5\) no non-hyperplanar boundary obstruction exists.

Bajnok (2014) develops a unified restricted-critical-number framework, with first public preprint on 12 December 2014 and number-theory primary classification. His results are about sizes forcing coverage and do not give the above equality-case classification.

The previously published exact Walsh-spectrum census of eight-subsets of \(\mathbb F_2^4\) gives \(840\) nonhyperplanes having two complementing translations, and \(30\) affine hyperplanes. These \(840\) sets coincide with the finite exceptional class characterized here, so their number and finite structural description are **not** asserted as independent historical novelty. That census explicitly restricts its theorem to dimension four and does not imply the infinite-dimensional four-sum inverse theorem without a new structural argument.

Chen and Huang (2026) establish critical-number results for restricted sums in finite abelian groups under size hypotheses; these do not cover the equality-case classification for elementary 2-groups (their even-order size hypothesis cannot hold for a nontrivial elementary 2-group). A historical equivalent under alternative additive-combinatorial terminology remains possible and merits specialist verification.

## Limitations

The result covers only half-sized subsets of binary vector spaces and sums of exactly four distinct members. It does not establish inverse classifications for other densities, other restricted-sum lengths, or nonbinary groups. The \(r=4\) exceptional census overlaps earlier finite Walsh-spectrum work and is included to mark the sharp rank boundary, not as a separate novel enumeration. The finite calculations are corroborating only and do not replace the unrestricted proof.

## References

1. R. M. Roth and A. Lempel, *t-Sum Generators of Finite Abelian Groups*, Discrete Mathematics **103** (1992), 279–292, doi:10.1016/0012-365X(92)90320-F. Author-hosted full text: https://ronny.cswp.cs.technion.ac.il/wp-content/uploads/sites/54/2016/05/ag.pdf
2. B. Bajnok, *The h-critical number of finite abelian groups*, arXiv:1412.4058v1 (12 December 2014), https://arxiv.org/html/1412.4058v1
3. B. Chen and J. Huang, *Critical Numbers for Restricted Sumsets: Rigidity and Collapse in Finite Abelian Groups*, arXiv:2602.10402v1 (11 February 2026), https://arxiv.org/html/2602.10402
4. *Exact Walsh-spectrum multiplicities for eight-point subsets of the Boolean four-cube*, published research record b981e436a3b1, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-walsh-spectrum-multiplicities-for-eight-point-subsets-of-t--b981e436a3b1
