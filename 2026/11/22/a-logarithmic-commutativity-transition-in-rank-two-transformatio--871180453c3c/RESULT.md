# A logarithmic commutativity transition in rank-two transformation variants

## Finding
Let \(n\geq2\) and let \(a:[n]\to[n]\) be a transformation of rank two, with the two nonempty kernel blocks having sizes \(k\) and \(\ell\), so \(k+\ell=n\). Endow the full transformation semigroup \(\mathcal T_n\) with the sandwich multiplication \(f\star_a g=f\circ a\circ g\). Let \(C_n(k,\ell)\) count **ordered** pairs \((f,g)\in\mathcal T_n^2\) satisfying \(f\star_a g=g\star_a f\). Then the complete count is
\[
\begin{aligned}
 C_n(k,\ell)={}&n(n^2)^{n-2}
 +n(n-1)(k^2+\ell^2)^{n-2}
 +2k\ell(2k\ell)^{n-2}\\
 &+2(n-1)\bigl[k(nk)^{n-2}+\ell(n\ell)^{n-2}\bigr]\\
 &+k(k-1)(k-2)(k^2)^{n-2}
 +\ell(\ell-1)(\ell-2)(\ell^2)^{n-2}.
\end{aligned}
\]
All terms are interpreted literally as integer products, including when a falling-factorial coefficient vanishes. The formula depends only on the unordered pair of kernel-block sizes, not on the individual representatives or their arrangement.

Write \(m_n=\min(k,\ell)\), let \(P_n=C_n(k,\ell)/n^{2n}\) be the commuting probability, and use natural logarithms. The exact formula gives a sharp **logarithmic crossover**:

1. If \(m_n=m\geq1\) is fixed, then \(nP_n\to e^{-2m}\).
2. If \(m_n-\log n\to t\in\mathbb R\), then \(n^3P_n\to(1+e^{-t})^2\).
3. If \(m_n-\log n\to+\infty\), then \(n^3P_n\to1\). In particular this holds whenever both kernel blocks occupy a fixed positive fraction of \([n]\).

Thus keeping a tiny kernel block produces order-\(n^{-1}\) commutativity, whereas balanced kernels produce order-\(n^{-3}\) commutativity. The crossover has a nonconstant limiting profile, not merely an order-of-magnitude estimate.

## Assumptions and scope
The maps are **total** functions on a labeled set of size \(n\); all \(n^n\) maps are included. Function composition is right-to-left: \((f\circ g)(x)=f(g(x))\). The operation \(\star_a\) is associative, and no identity for it is assumed. A rank-two sandwich means exactly two nonempty fibers of \(a\). There is no finite-field hypothesis. The three limits concern sequences of sizes tending to infinity, including subsequences of the integers in the critical window, where the smaller block size is integral.

## Proof
**Reduction to a canonical sandwich.** If \(p,q\) are permutations and \(a'=p\circ a\circ q\), then the bijection \(\Phi(f)=q^{-1}\circ f\circ p^{-1}\) satisfies
\[\Phi(f\star_a g)=\Phi(f)\star_{a'}\Phi(g).\]
Every rank-two sandwich with block sizes \(k,\ell\) is left-right permutation-equivalent to an idempotent with image \(\{1,2\}\) and fibers \(K_1,K_2\) of sizes \(k,\ell\), with \(1\in K_1\), \(2\in K_2\). It suffices to count for this canonical form.

**Four boundary coordinates.** Denote \(u=f(1)\), \(v=f(2)\), \(s=g(1)\), \(t=g(2)\). Commutativity at a point \(x\) means
\[f\bigl(a(g(x))\bigr)=g\bigl(a(f(x))\bigr).\]
Once \((u,v,s,t)\) is fixed, the restrictions at \(x=1,2\) are exactly
\[ f(a(s))=g(a(u)),\qquad f(a(t))=g(a(v)).\]
At any other point, \(f(x)\) and \(g(x)\) can be chosen independently among \(n^2\) ordered values, except for the displayed equality. The number of allowed value pairs is
\[
 K(u,v,s,t)=k^2[u=s]+k\ell[v=s]+k\ell[u=t]+\ell^2[v=t],
\]
where \([\mathcal P]\) equals one if \(\mathcal P\) holds and zero otherwise. Therefore the boundary tuple contributes either \(0\) or \(K(u,v,s,t)^{n-2}\), according to its two boundary equations.

**Complete finite classification of the boundary tuples.** Encode equality among \((u,v,s,t)\) by a restricted-growth code \(p_1p_2p_3p_4\): the first distinct value is labeled \(0\), the next \(1\), and so on. Assign each distinct value a letter \(A\) or \(B\) according as it lies in \(K_1\) or \(K_2\). For a code with \(r_A\) distinct \(A\)-values and \(r_B\) distinct \(B\)-values, there are exactly \((k)_{r_A}(\ell)_{r_B}\) realizing tuples, where \((h)_r=h(h-1)\cdots(h-r+1)\). Check both boundary equations for every restricted-growth code and every block-letter assignment. There are precisely 18 admissible labeled types, grouped exhaustively as follows:

| \(K(u,v,s,t)\) | Admissible (code, block letters) | Number of boundary tuples |
|---|---|---|
| \(n^2\) | (0000,A), (0000,B) | \(n\) |
| \(nk\) | (0001,AA), (0001,AB), (0100,AA), (0100,AB) | \(2k(n-1)\) |
| \(n\ell\) | (0010,BA), (0010,BB), (0111,AB), (0111,BB) | \(2\ell(n-1)\) |
| \(k^2+\ell^2\) | (0101,AA), (0101,AB), (0101,BA), (0101,BB) | \(n(n-1)\) |
| \(2k\ell\) | (0110,AB), (0110,BA) | \(2k\ell\) |
| \(k^2\) | (0102,AAA) | \(k(k-1)(k-2)\) |
| \(\ell^2\) | (0121,BBB) | \(\ell(\ell-1)(\ell-2)\) |

All other assignments fail at least one boundary equation. The table is an exhaustive finite identity, not a statistical sampling assumption: restricted-growth codes uniquely enumerate the 15 partitions of four positions, and the letter assignments account for every value placement. Its entries can also be reconstructed exactly from `verify.py` without relying on a symbolic package. Multiplying each row's third column by its first column raised to \(n-2\) and adding proves the seven-base formula.

**Asymptotic analysis.** By symmetry put \(m=k\leq\ell=n-m\). The all-equal row contributes exactly \(n^{2n-3}\) commuting pairs, hence \(n^{-3}\) to the probability. If \(m\) is fixed, the \(\ell^2\)-base term satisfies
\[
\frac{\ell(\ell-1)(\ell-2)\ell^{2n-4}}{n^{2n}}\sim\frac{e^{-2m}}{n}.
\]
Every other term is of smaller order: the \(n\ell\) and \(k^2+\ell^2\) terms are \(O(n^{-2})\), and the terms with bases \(nk,k^2,2k\ell\) are exponentially smaller. This proves the fixed-\(m\) assertion.

If \(m-\log n\to t\), then \(m=O(\log n)\), and the ratios of the three potentially dominant terms to \(n^{2n-3}\) are
\[
1,\qquad 2(n-1)(1-m/n)^{n-1}\to2e^{-t},
\]
\[
\frac{\ell(\ell-1)(\ell-2)}{n}(1-m/n)^{2n-4}\to e^{-2t}.
\]
All four remaining row contributions, divided by \(n^{2n-3}\), tend to zero: the \(k^2+\ell^2\) term is \(O(ne^{-2m})=o(1)\), while the rows involving small-block powers are exponentially small. Their sum yields \((1+e^{-t})^2\).

Finally assume \(m-\log n\to+\infty\) with \(m\leq n/2\). Dividing each base by \(n^2\) and each prefactor by \(n\) gives the row's ratio to \(n^{2n-3}\). The normalized bases for the \(n\ell\) and \(k^2+\ell^2\) rows are at most \(1-m/n\); for the \(\ell^2\) row the base is \((1-m/n)^2\). Since \((1-m/n)^{n-2}\leq e^{-m+2m/n}\leq e^{1-m}\), the first two ratios are \(O(ne^{-m})\) and the third is \(O(n^2e^{-2m})\). All tend to zero under the stated assumption. The remaining normalized bases \(nk/n^2,k^2/n^2,2k\ell/n^2\) are at most \(1/2\), with polynomial prefactors. Thus the all-equal row dominates and \(n^3P_n\to1\).

## Verification
Run `python3 verify.py` using Python 3 standard-library modules. The script independently enumerates all \(n^{2n}\) ordered map pairs for a canonical rank-two sandwich of each ordered fiber-size profile with \(2\leq n\leq4\), checks the seven-row formula against the complete 18-type boundary classifier for all 66 pairs \((n,k)\) with \(2\leq n\leq12\), and checks invariance under a change of fiber placement at \(n=4,k=2\). It does not enumerate every sandwich map. Recorded counts include \(C_2(1,1)=10\), \(C_3(1,2)=133\), \(C_4(1,3)=5614\), and \(C_4(2,2)=3840\). Numerical comparisons in `verification_output.txt` illustrate the logarithmic transition. None of these finite tests substitutes for the proof for arbitrary \(n\).

## Relationship to prior work
Tsyaputa (2005 preprint) classifies variant isomorphism types by the **unordered kernel-fiber-size partition**, but does not state an ordered commuting-pair census. Dolinka and East (2014 preprint, 2015 revision) develop the Green-relational, regular and idempotent-generated structure of transformation variants, not their two-map commutativity probability. Cameron et al. (2021 preprint) study minimal faithful transformation degree of the same variants, again a different invariant. An earlier idempotent-commuting-graph result for rank-two variants describes the graph on **idempotent** elements; it cannot determine the commuting probability over all elements. The published rank-one multiplication-fingerprint work on published-finding corpus reconstructs the kernel partition from a **one-sided rank-one product count** rather than counting commuting pairs. The current finding's numerical seven-base formula and logarithmic crossover are not implications of those cited statements without the separate boundary-tuple analysis above.

## Limitations
This result is restricted to rank-two sandwiches on **full**, not partial, transformation semigroups. It does not classify centralizer sizes of individual maps, general rank sandwiches, or arbitrary transformations with different compositions. The logarithmic transition concerns a *sequence* of kernel partitions and has no claim of universality for unrelated semigroup families. Exhaustive testing was carried out only in the specified finite configurations; the unrestricted proof is the explicit finite boundary classification and asymptotic estimates. Priority could be affected by an unlocated prior specialized counting formula or a more general unpublished commuting-pair theorem; no independent review has been performed.

## References
1. G. Y. Tsyaputa, *Transformation Semigroups with the Deformed Multiplication*, arXiv:math/0508386v1, first submitted 20 August 2005, Theorem 2, https://arxiv.org/abs/math/0508386.
2. I. Dolinka and J. East, *Variants of finite full transformation semigroups*, arXiv:1410.5253v1, first submitted 20 October 2014, especially Sections 3–7, https://arxiv.org/abs/1410.5253.
3. P. J. Cameron, J. East, D. FitzGerald, J. D. Mitchell, L. Pebody and T. Quinn-Gregson, *Minimum degrees of finite rectangular bands, null semigroups, and variants of full transformation semigroups*, arXiv:2110.09701v1, first submitted 19 October 2021, https://arxiv.org/abs/2110.09701.
4. *A sharply separated rank-one multiplication fingerprint for finite transformation variants*, Resultary, 26 October 2026, https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-a-sharply-separated-rank-one-multiplication-fingerprint-for-fini--84067f9a2b4a/RESULT.md.
5. M. Soule, *A Single Family of Semigroups with Every Positive Rational Commuting Probability*, College Mathematics Journal 45 (2014), 136–139, https://doi.org/10.4169/college.math.j.45.2.136.
