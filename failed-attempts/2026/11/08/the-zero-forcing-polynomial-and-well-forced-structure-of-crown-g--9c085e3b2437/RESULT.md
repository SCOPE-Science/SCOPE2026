# The zero-forcing polynomial and well-forced structure of crown graphs

## Finding

For every integer \(n\ge 3\), write \(\operatorname{Cr}_n=K_{n,n}\setminus M\), where the deleted perfect matching pairs \(a_i,b_i\) for \(i\in[n]\). Equivalently, its vertices are \(A=\{a_i:i\in[n]\}\) and \(B=\{b_i:i\in[n]\}\), with \(a_ib_j\) an edge exactly when \(i\ne j\). Standard zero forcing colors a white vertex blue when it is the unique white neighbor of a blue vertex.

**Theorem (complete forcing-set characterization).** A starting blue set \(S\subseteq V(\operatorname{Cr}_n)\) forces all vertices precisely when, with
\[
X=\{i:a_i\notin S\},\qquad Y=\{i:b_i\notin S\},
\]
one has \(|X|\le2\), \(|Y|\le2\), and it is **not** the case that \(|X|=|Y|=2\) and \(X=Y\).

Writing \(c=\binom n2\) and \(\mathcal Z(G;z)=\sum_{S\text{ zero forcing}}z^{|S|}\), the complete zero-forcing polynomial is
\[
\boxed{\mathcal Z(\operatorname{Cr}_n;z)=z^{2n-4}\big[(z^2+nz+c)^2-c\big].}
\]
The inclusion-minimal zero-forcing sets are exactly the complements of \(\{a_i:i\in X\}\cup\{b_j:j\in Y\}\) for *different* two-element subsets \(X,Y\subseteq[n]\). Consequently all minimal zero-forcing sets have size \(2n-4\) (the graph is well-forced), and there are precisely \(c(c-1)\) of them. The zero-forcing number and maximum failed zero-forcing number are
\[
\operatorname Z(\operatorname{Cr}_n)=2n-4,\qquad
\operatorname F(\operatorname{Cr}_n)=2n-3.
\]
The zero-forcing span, the number of cardinalities supporting both a successful and an unsuccessful starting set, equals \(2\).

**Root transition.** For \(n\ge5\), zero is the only real root of \(\mathcal Z(\operatorname{Cr}_n;z)\); the other four roots (counting multiplicity) are nonreal. For \(n=3,4\), two of these four are real and two are nonreal.

## Assumptions and scope

All graphs are finite, simple, undirected and labelled. The theorem covers integer \(n\ge3\), not \(n=2\), where the graph consists of two disjoint edges and the stated classification is inapplicable. In the standard zero-forcing rule, only *blue* vertices may force. For \(n=3\), the crown graph is the six-cycle; this special case is already covered by known cycle zero-forcing-polynomial results and is included for uniformity, not as separate novelty. The new family-wide assertion concerns in particular all \(n\ge4\).

## Proof

**1. A persistent-white obstruction.** Let \(X\) and \(Y\) denote the currently white indices on shores \(A\) and \(B\). When \(|X|\ge3\), every blue vertex \(b_j\) has at least \(|X|-1\ge2\) white neighbors among the \(a_i\). Thus no white \(a_i\) can be forced, and this obstruction persists forever, even if vertices on shore \(B\) become blue. Therefore \(|X|\ge3\) is incompatible with successful forcing. The same argument applies to \(|Y|\ge3\). Hence each of \(X,Y\) has size at most two for any successful starting set.

If \(X=Y\) is a two-element set, every initially blue \(a_i\) has two white neighbors on shore \(B\), and every initially blue \(b_i\) has two white neighbors on shore \(A\); no first force exists. This is a second obstruction.

**2. The two-by-two sufficient case.** Suppose \(|X|=|Y|=2\) and \(X\ne Y\). The intersection has size zero or one.

If \(X=\{i,j\}\) and \(Y=\{k,\ell\}\) are disjoint, the following legal forces, in order, turn every vertex blue:
\[
b_i\to a_j,\qquad b_j\to a_i,\qquad a_k\to b_\ell,\qquad a_\ell\to b_k.
\]
The first two are legal because each \(b_i\) is nonadjacent to \(a_i\), while the last two are legal because each \(a_k\) is nonadjacent to \(b_k\). All of these forcing vertices are blue at their indicated steps.

If the intersection has size one, relabel \(X=\{i,j\}\), \(Y=\{j,k\}\), where \(i,j,k\) are distinct. The following forces are legal in the indicated order:
\[
b_i\to a_j,\qquad a_j\to b_k,\qquad b_k\to a_i,\qquad a_i\to b_j.
\]
Thus every two-by-two white profile with different index sets is successful.

**3. All smaller white profiles.** Standard zero forcing is monotone in the initial blue set: a forcing sequence remains valid after adding initially blue vertices, ignoring any steps whose targets have already become blue. Let \(X,Y\) be arbitrary with \(|X|,|Y|\le2\), excluding the equal-two-by-two obstruction. The sets can be extended to two-element subsets \(X',Y'\subseteq[n]\) that remain different. Indeed, when one side has fewer than two elements, it has at least two distinct two-element extensions for \(n\ge3\), so equality with the other chosen extension can be avoided. The initial white set corresponding to \(X',Y'\) is forceable by Step 2, and the desired set has fewer white vertices; monotonicity proves sufficiency.

Steps 1–3 give the necessary-and-sufficient classification for every \(n\ge3\).

**4. Counting and minimality.** The possible white indices on each shore have generating polynomial \(1+ny+cy^2\). Independent choices on both shores give its square; the \(c\) disallowed profiles \(X=Y\) with \(|X|=2\) have weight \(y^4\). Therefore the white-count polynomial is \((1+ny+cy^2)^2-cy^4\). Replacing the weight of \(q\) whites by \(z^{2n-q}\) yields the displayed zero-forcing polynomial exactly.

If at least one of \(|X|,|Y|\) is smaller than two, Step 3 gives a strictly larger forceable white set, so the corresponding blue set is not inclusion-minimal. Conversely, for \(|X|=|Y|=2\) and \(X\ne Y\), removing any blue vertex causes one of the white-shore counts to become three and Step 1 prevents forcing. Such sets are precisely the minimal forcing sets. There are \(c^2-c\), all of cardinality \(2n-4\). Every proper starting set with \(2n-2\) or more blue vertices forces all vertices, while some sets with \(2n-3\) blue vertices fail (choose three whites on one shore). Hence the extremal and span formulas follow. Both cardinalities \(2n-4\) and \(2n-3\) have successful and failed sets: at the former size use an allowed two-by-two profile and a forbidden equal two-by-two profile.

**5. Roots.** The nonzero-root factor splits over the reals as
\[
(z^2+nz+c-\sqrt c)(z^2+nz+c+\sqrt c).
\]
Its quadratic discriminants are \(-n(n-2)+4\sqrt c\) and \(-n(n-2)-4\sqrt c\). The second is always negative. For \(n\ge5\), \(n(n-2)>4\sqrt{n(n-1)/2}\), since squaring reduces this to \(n(n-2)^2>8(n-1)\), immediate from \((n-2)^2\ge9\) and \(n>n-1\). Hence the first is also negative. Direct substitution for \(n=3,4\) gives a positive first discriminant. This proves the root assertion without numerical approximation.

## Verification

Run `python verify_crown.py` using a standard Python installation; no third-party packages are needed. The verifier constructs the adjacency matrix indirectly through independent bitset neighborhoods, applies one legal force at a time, and compares outcomes with the white-profile criterion for every labelled vertex subset when \(3\le n\le9\). It also independently enumerates inclusion-minimal sets by deletion tests and verifies every cardinality coefficient, plus symbolic coefficient identities through \(n=100\). The recorded output is:

```
VERIFY_OK orders=3..9 subsets=349504 minimal_sets=2772 direct_sequential_forces=PASS white_profile=PASS zero_forcing_polynomials=PASS inclusion_minimality=PASS symbolic_counts=3..100 PASS
```

The finite experiments are corroboration, not a proof for arbitrary \(n\). The unrestricted argument is Steps 1–5 above.

## Relationship to prior work

Boyer et al. (2018) introduced the zero-forcing polynomial and gave exact forms for complete multipartite graphs, paths, cycles, wheels, and threshold graphs. Their cycle formula covers the \(n=3\) crown. The complete-multipartite formula cannot be directly applied to the nonmultipartite crown family for \(n\ge3\). Jacob (2023) defined and studied zero-forcing span, giving the general relation between span and the extremal forcing numbers; it does not compute the full crown polynomial. Brimkov and Carlson (2022) study inclusion-minimal forcing sets generally, and Grood et al. (2023) study well-forced trees, rather than this family of regular bipartite graphs. Pelayo and Abara (2022) treat maximal failed forcing sets for Cartesian, strong, lexicographic, and corona products, but not the categorical product \(K_n\times K_2\) that represents a crown graph. None of these inspected results contains the displayed family-wide polynomial or its white-profile classification.

## Limitations

The scope is ordinary (not skew or positive-semidefinite) zero forcing on labelled crowns. The result does not address arbitrary submatchings deleted from unbalanced bicliques. The root theorem concerns real roots, not their precise complex locations. Non-discovery in the searched literature cannot rule out an unindexed or differently formulated equivalent theorem; independent publication-priority review remains appropriate. No independent mathematical audit is asserted.

## References

1. B. Jacob, *The zero forcing span of a graph*, first submitted September 12, 2023, arXiv:2309.06234v1. https://arxiv.org/html/2309.06234v1
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, first submitted January 26, 2018, arXiv:1801.08910v1. https://arxiv.org/abs/1801.08910
3. B. Brimkov and J. Carlson, *Minimal Zero Forcing Sets*, first submitted April 4, 2022, arXiv:2204.01810v1. https://arxiv.org/abs/2204.01810
4. C. Grood, R. Haas, B. Jacob, E. King, S. Nasserasr, *Well-forced graphs*, first submitted December 21, 2023, arXiv:2312.14298v1. https://arxiv.org/abs/2312.14298
5. P. A. B. Pelayo and M. N. M. Abara, *Maximal failed zero forcing sets for products of two graphs*, first submitted February 10, 2022, arXiv:2202.04997v1. https://arxiv.org/html/2202.04997v1
