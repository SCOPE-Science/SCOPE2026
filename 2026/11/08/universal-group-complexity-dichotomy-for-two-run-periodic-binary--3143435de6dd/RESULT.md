# Universal group-complexity dichotomy for two-run periodic binary words

## Finding
For every pair of positive integers \(a,b\), consider the infinite periodic binary word
\[
x_{a,b}=(0^a1^b)^{\omega}.
\]
Its *universal group-complexity property* holds if and only if
\[
\boxed{\min(a,b)=1.}
\]
More precisely, for every \(n\ge1\), let \(p_x(n)\) denote the number of distinct length-\(n\) contiguous factors and \(p_x^{\mathrm{ab}}(n)\) the number of distinct Parikh vectors. For each \(G\le S_n\), let \(p_x^G(n)\) be the number of \(G\)-orbits (in the full binary cube \(\{0,1\}^n\)) meeting the factor set. Universality says that every integer between \(p_x^{\mathrm{ab}}(n)\) and \(p_x(n)\), inclusive, equals \(p_x^G(n)\) for some \(G\le S_n\), independently at each \(n\).

In the positive case, put \(r=a+b\). By complementing letters if necessary and rotating the period, one may work with \(z_r=(10^{r-1})^{\omega}\). Let \(H_m\le S_n\), \(0\le m\le n\), fix the first \(m\) coordinates pointwise and permute the remaining \(n-m\) coordinates arbitrarily. Their exact group-complexity values are:
\[
p_{z_r}^{H_m}(n)=
\begin{cases}
m+2,&1\le n<r,\quad 0\le m<n,\\
n+1,&1\le n<r,\quad m=n,\\
m+1+\mathbf1_{\{m<t\}},& n\ge r,\quad 0\le m<r,\\
r,&n\ge r,\quad r\le m\le n,
\end{cases}
\qquad t=n\bmod r.
\]
Thus the values from this single nested family of subgroups exhaust the interval between Abelian and ordinary factor complexity. Explicitly, the endpoints are \((p^{\mathrm{ab}},p)=(2,n+1)\) for \(n<r\), and \((1,r)\) if \(n\ge r\) and \(r\mid n\), or \((2,r)\) otherwise.

In the negative case \(a,b\ge2\), put \(\delta_a=\mathbf1_{\{a\ge3\}}\), \(\delta_b=\mathbf1_{\{b\ge3\}}\). At length three the set of attainable group complexities is exactly
\[
\boxed{\{p_{x_{a,b}}^G(3):G\le S_3\}=\{2+\delta_a+\delta_b,\ 4+\delta_a+\delta_b\}.}
\]
Consequently the intermediate integer \(3+\delta_a+\delta_b\) is not attained. Length three is the first failure, since all such two-run words satisfy universality at lengths one and two.

## Assumptions and scope
The alphabet consists of two distinct labeled symbols \(0\) and \(1\). The integers \(a,b,n\) are positive, and \(G\) ranges over every subgroup of the symmetric group on the \(n\) factor positions. Permutations act on position coordinates, **not** on alphabet symbols. Group equivalence is determined by the full permutation orbit, whether or not every intermediate orbit element is itself a factor. Complementation of every binary letter induces a bijection on factor sets commuting with every coordinate permutation. A cyclic rotation of the displayed period does not change the factor set of the infinite periodic word. These observations justify the one-marker normalization in the positive case.

## Proof
**Lemma 1 (one marker).** Let \(r\ge2\) and \(z_r=(10^{r-1})^{\omega}\). Then the displayed piecewise formula for \(p_{z_r}^{H_m}(n)\) holds for all \(n\ge1\), \(0\le m\le n\).

*Proof.* Every length-\(n\) factor comes from one of the \(r\) phases of the period. If \(n<r\), a factor contains at most one occurrence of \(1\). There is one all-zero factor and exactly one factor having its unique \(1\) at each of the \(n\) positions. The factors are therefore \(n+1\) distinct words. Two factors lie in the same \(H_m\)-orbit exactly when their first \(m\) symbols are identical and their last \(n-m\) symbols contain equally many ones. If \(m<n\), the \(m\) factors whose unique one occurs in the fixed prefix give \(m\) singleton classes. The remaining factors form exactly two classes (all zero; one in the permuted suffix), giving \(m+2\). If \(m=n\), every factor is its own class.

Now suppose \(n\ge r\) and write \(n=kr+t\), where \(k\ge1\) and \(0\le t<r\). Index the \(r\) phase factors by the position \(j\in\{0,\ldots,r-1\}\) of their **first** occurrence of \(1\). Because \(n\ge r\), each phase yields a distinct factor and each first position occurs once. The total number of ones is \(k+1\) for \(j<t\) and \(k\) for \(j\ge t\). If \(m<r\), the \(m\) factors with \(j<m\) have pairwise distinct fixed prefixes and each is alone in its \(H_m\)-class. All remaining factors have the all-zero fixed prefix; they give exactly one class if \(m\ge t\), and exactly two if \(m<t\), depending on their total ones count. This proves \(m+1+\mathbf1_{\{m<t\}}\). If \(m\ge r\), each factor has a different fixed prefix of length \(r\), hence the orbit count is \(r\). \(\square\)

For the *positive direction*, assume \(\min(a,b)=1\), so Lemma 1 applies up to complementing symbols and rotating a period. For \(n<r\), the obtained orbit counts as \(m\) varies run through \(2,3,\ldots,n+1\), precisely the interval between Abelian and ordinary complexity. For \(n\ge r\), if \(t=0\), the counts for \(m=0,\ldots,r-1\) run through \(1,2,\ldots,r\). If \(t>0\), the counts are \(2,3,\ldots,r\), with a repetition at the transition \(m=t-1\) to \(m=t\) but no gap. At \(n\ge r\), all phases have \(k\) or \(k+1\) ones, so the Abelian complexity is \(1\) for \(t=0\) and \(2\) otherwise. This proves universality and the stronger explicit witness formula.

**Lemma 2 (two non-singleton runs).** Let \(a,b\ge2\). The length-three factor set of \(x_{a,b}\) is
\[
F_{x_{a,b}}(3)=\{001,011,110,100\}
\cup(\{000\}\text{ if }a\ge3)
\cup(\{111\}\text{ if }b\ge3).
\]
Each subgroup \(G\le S_3\) produces either \(|F_{x_{a,b}}(3)|\) or \(|F_{x_{a,b}}(3)|-2\) factor orbits, and both possibilities occur.

*Proof.* The four transition-spanning factors occur because both runs have length at least two, while a length-three constant factor exists exactly when its run is at least three. There are \(2+\delta_a+\delta_b\) Abelian classes: one singleton for each existing constant factor and one each for weights one and two. Under a coordinate permutation, the two one-\(1\) factors \(001\) and \(100\) are equivalent exactly when the coordinates \(1\) and \(3\) belong to the same coordinate orbit of \(G\). The corresponding two one-\(0\) factors \(110\) and \(011\) are equivalent under precisely the same condition, by complementing all letters. Neither pair can merge with a different Parikh weight. Thus the two potential mergers happen simultaneously, reducing the number of classes by either zero or two. Both cases occur: the identity gives no mergers, and \(S_3\) gives both. \(\square\)

For the *negative direction*, Lemma 2 shows that the single integer strictly between the two attainable counts is never realized. These counts equal the Abelian and ordinary complexities respectively, so universality fails at length three. At length one the two complexities coincide; at length two the factor set is \(\{00,01,10,11\}\), so the identity and \(S_2\) attain both values \(4\) and \(3\), establishing the claimed first obstruction. Combining both directions proves the theorem.

## Verification
The accompanying Python standard-library script `checker.py` constructs periodic factor sets from their definition. It independently counts \(H_m\)-orbits via fixed prefixes and suffix Parikh counts, checks every formula across both symbol orientations, and enumerates all six subgroups of \(S_3\) from closure under composition in the negative case. Running `python3 checker.py` produced:

`PASS 156832 direct suffix-orbit comparisons; 324 full S3 subgroup spectra; 6 subgroups`

The positive tests cover period lengths \(2\) through \(30\) and factor lengths through four full periods; negative tests cover \(2\le a,b\le19\). These finite tests catch indexing and boundary errors but do not replace the two symbolic lemmas proving the infinite claims.

## Relationship to prior work
Launer, Puzynina and Voloshinova (2026) introduced and studied the universal group-complexity property and proved in Section 6 a finite algorithmic criterion for every specified eventually periodic word, using eventual stabilization. Their criterion applies to each word here, but their results do not state a *uniform necessary-and-sufficient condition* for all positive run lengths, identify the universal length-three obstruction for both runs nonsingleton, or supply the explicit nested-subgroup orbit counts above. The new classification gives those mathematical facts simultaneously without enumerating subgroups beyond \(S_3\). Charlier, Puzynina and Zamboni (2015/2017) developed the general group-complexity framework and a group-action Morse–Hedlund theorem, mainly addressing aperiodic factor complexity; they do not give the present run-length dichotomy. These statements concern compared material, not a claim that all possible earlier sources have been exhausted.

## Limitations
The classification is for purely periodic binary words whose period has exactly one zero run and one one run. It does not classify multi-run periods, eventually periodic words with nonempty preperiods, or general infinite words. The positive-branch formulas use an explicit convenient subgroup family, but do not classify every subgroup giving the same orbit count. The novelty assessment remains subject to unindexed or unavailable equivalent prior work. Independent mathematical validation has not been performed.

## References
1. M. Launer, S. Puzynina and E. Voloshinova, *On possible values of the group complexity function of infinite words*, arXiv:2607.07620, first posted 2026-07-08. https://arxiv.org/abs/2607.07620 (especially Sections 2 and 6).
2. É. Charlier, S. Puzynina and L. Q. Zamboni, *On a group theoretic generalization of the Morse–Hedlund theorem*, arXiv:1505.03848, first posted 2015-05-14, subsequently published in 2017. https://arxiv.org/abs/1505.03848.
