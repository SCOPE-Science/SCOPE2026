# Independent mathematical audit

## correctness

PASS

The subset support dichotomy is exact: a nonempty set either lies in one part, in which case its closed neighborhood misses exactly the unselected vertices of that part, or it meets at least two parts, in which case it dominates the whole graph. This yields the displayed formulas. For ordinary domination, \(Q_G=(1+x)^N-D(G;x)=1+\sum_t m_t((1+x)^t-x^t-1)\); the largest positive degree of \(Q_G-1\) is one less than the largest nonsingleton part size and its leading coefficient is that size times its multiplicity, so recursive peeling is valid. For the bivariate polynomial, the coefficient of \(xy^{N-t}\) is \(t m_t\), recovering every part multiplicity.

## originality

FAIL

The ordinary domination polynomial is already explicitly published for complete multipartite graphs. Section 5.2 of Selvakumar--Manikandan--Murugan gives the same polynomial in product-sum form, algebraically identical to the submitted formula; Beaton--Brown had already characterized the same dominating sets. The submitted descending-degree reconstruction is an immediate triangular coefficient extraction from that prior exact formula. The bivariate rigidity adds no substantial independent novelty: singleton terms of \(J\) already encode the degree multiset, and in a complete multipartite graph degree \(N-t\) is equivalent to part size \(t\). The explicit bivariate expression is the routine two-support-case expansion of its definition. Under the audit rule that corollaries and mechanically implied specializations count as covered, no nonroutine original mathematical claim survives.

## value

FAIL

After removing the already published ordinary polynomial formula, the reconstruction consists of a descending leading-coefficient peel, and the bivariate reconstruction is simply degree-multiset recovery from singleton terms. These are routine consequences of known formulas/definitions rather than a motivated new structural lemma or unknown exact invariant under the stated value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
