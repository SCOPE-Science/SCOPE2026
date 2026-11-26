# All optimal overlap-distance identification probes on Kautz shift networks

## Finding

For each integer \(q\ge3\) and \(n\ge2\), let \(A\) be a fixed labeled alphabet of size \(q\). Let \(V\) be the set of all length-\(n\) words over \(A\) whose adjacent letters differ. A probe \(s\in V\) reports the directed shift-and-append distance \(d(s,v)\) to an unknown target \(v\in V\). A set \(S\subseteq V\) is identifying if every two target words have different vectors of probe responses.

**Theorem.** A probe set is identifying if and only if it contains all but at most one of the \(q-1\) vertices \(pa\) for each length-\(n-1\) proper prefix \(p\). Writing \(c=q(q-1)^{n-2}\) for the number of such prefix classes, the complete polynomial of identifying probe sets by their cardinality is

\[ R_{q,n}(z)=\bigl((q-1)z^{q-2}+z^{q-1}\bigr)^c. \]

In particular, the minimum probe count and the exact number of labeled optimal probe sets are

\[ \beta_{q,n}=c(q-2),\qquad N_{q,n}=(q-1)^c. \]

This theorem determines **all** feasible identifying probe sets, not merely one optimal construction. Their optimal choices are independent across prefix classes. Thus enumerating, ranking, unranking, and uniformly sampling optimum sets reduce to \(c\) choices among \(q-1\) letters, taking time linear in the printed probe-set size (apart from big-integer arithmetic for ranks).

## Assumptions and scope

The source and probe words are indexed, not quotiented by alphabet relabeling or cyclic rotation. Edges are directed: from \(x_1\cdots x_n\) to \(x_2\cdots x_na\) if \(a\ne x_n\). Probe responses are exact directed distances from probe to target, without noise or erasures. The number \(q\) of alphabet symbols is at least three; \(n\) is at least two. We count labeled subsets of vertices, not orderings of the probes.

## Proof

For distinct vertices \(s,v\), the shift graph admits a path of length \(t\lt n\) from \(s\) to \(v\) precisely if the last \(n-t\) letters of \(s\) equal the first \(n-t\) of \(v\); the appended letters must then be those in \(v\). A path of length \(n\) always exists if there is no positive overlap, because in that case the last symbol of \(s\) differs from the first of \(v\). Consequently, for distinct words,

\[ d(s,v)=n-\max\{\ell:0\le\ell\le n-1,\ \operatorname{suffix}_\ell(s)=\operatorname{prefix}_\ell(v)\},\qquad d(v,v)=0. \]

Fix a proper prefix \(p\) of length \(n-1\) and consider two distinct legal continuations \(pa,pb\). Every probe \(s\) outside this pair has equal distances to both targets: their prefixes of every length less than \(n\) coincide, so the displayed overlap formula gives the same distance. Hence omitting both \(pa,pb\) makes the targets indistinguishable. This proves the necessity of including at least \(q-2\) representatives from each prefix class.

For sufficiency, suppose each prefix class contains at most one omitted word. Given distinct targets \(u,v\) with the same length-\(n-1\) prefix, at least one of the two targets belongs to the probe set, because at most one vertex of that class is omitted; that target distinguishes itself by distance zero. Otherwise, let \(k\) be the length of their longest common prefix, so \(0\le k\le n-2\). For \(k\ge1\), choose a proper word \(p\) of length \(n-1\) ending in their common length-\(k\) prefix; for \(k=0\), choose one ending in a symbol unequal to both \(u_1\) and \(v_1\), possible since \(q\ge3\). The distinct words \(pu_{k+1}\) and \(pv_{k+1}\) are valid members of the same prefix class, so at least one belongs to \(S\). If such selected probe coincides with a target it distinguishes by distance zero. Otherwise, assuming it ends in \(u_{k+1}\), its overlap with \(u\) has length at least \(k+1\), whereas its overlap with \(v\) has exactly length \(k\): a longer overlap would force equality at the first differing target symbol. Their directed distances are therefore unequal. This proves sufficiency.

There are exactly \(c=q(q-1)^{n-2}\) valid prefixes. Each class allows either all \(q-1\) probes (one choice) or exactly \(q-2\) probes (\(q-1\) choices), and the classes partition \(V\). Multiplying their cardinality enumerators gives \(R_{q,n}\). The smallest power of \(z\) yields the asserted minimum size and its coefficient counts the optimal sets. A fixed ordering of the prefixes and of each legal final-letter list encodes any minimum set by a base-\(q-1\) digit vector, establishing the enumeration and sampling assertions.

## Verification

The standalone `verify.py` enumerates Kautz vertices and builds **graph distances by breadth-first search**, independently of the overlap formula. It checks the formula, equality of responses outside each prefix-twin pair, and unique fingerprints for all minimum prefix-transversals at \((q,n)=(3,2),(3,3),(3,4),(4,2),(5,2)\). It also tests the distance formula and twin relation at \((4,3)\). Run `python verify.py`; the final line is `VERIFY_OK`. Finite tests support but do not replace the all-parameter proof above.

## Relationship to prior work

Rajan, Rajasingh, Cynthia, and Manuel established the directed metric dimension of Kautz digraphs as \((d^{n-1}+d^{n-2})(d-1)\) for degree \(d=q-1\). Their Section 4.2 states the Kautz bounds without proof and does not give a characterization or enumerator for all minimum bases or all resolving sets. The minimum-size formula here agrees exactly with theirs and is **not** claimed as new. The new claim is the if-and-only-if structural characterization, its full resolving polynomial, and the exact labeled optimum count and enumeration procedure. Known Kautz identifying-code results based on radius-limited neighborhoods use a different measurement channel and do not imply this directed-distance classification.

## Limitations

The result concerns exact, oriented distance observations only. It makes no assertion about noisy, erased, undirected, bounded-radius or cyclic-quotiented measurements. The result has not undergone independent mathematical validation. Earlier unindexed papers or alternate terminology (“locating sets”, “metric bases”, “distance fingerprints”) could contain an equivalent complete classification; the originality assessment is qualified accordingly.

## References

1. B. Rajan, I. Rajasingh, J. A. Cynthia, P. Manuel, *Metric dimension of directed graphs*, International Journal of Computer Mathematics 91 (2014), 1397–1406, DOI: 10.1080/00207160.2013.844335. Accepted-author version publicly posted 2013-09-30. https://doi.org/10.1080/00207160.2013.844335.
2. Accessible full-text rendition of the above manuscript, https://www.academia.edu/15567718/Metric_dimension_of_directed_graphs (Sections 2 and 4 inspected).
3. E. B. Boutin, T. Horan and A. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, 2014, arXiv:1412.5842 (related bounded-radius identification problem; not the distance-observation model).
