# Induced stars are uniformly close to maximum independent sets in random interval graphs

## Finding

Let \(G_n\) be the intersection graph of \(n\ge2\) independent random intervals, each obtained by taking the smaller and larger of two independent samples from the same atomless continuous real probability distribution. Let \(\alpha_n\) be the maximum number of mutually disjoint sampled intervals. Let
\[\beta_n=\max_{v\in V(G_n)}\alpha(G_n[N(v)]),\qquad D_n=\alpha_n-\beta_n,\]
where \(N(v)\) is the open neighborhood and \(\alpha(\varnothing)=0\). Thus \(\beta_n\) is the maximum number of pairwise nonoverlapping sampled intervals that all overlap one common *sampled* interval (the number of leaves in a largest induced star).

For every integer \(n\ge2\) and \(k\ge1\),
\[\boxed{\Pr(D_n>k+1)\le \exp(-k/4)+(e/4)^k.}\]
In particular, the difference is uniformly exponentially tight: for every \(0<\lambda<1/4\),
\[\sup_{n\ge2}\mathbb E\exp(\lambda D_n)<\infty.\]
Moreover \(\alpha_n\to\infty\) in probability and
\[\boxed{\beta_n/\alpha_n\longrightarrow1\quad\text{in probability}.}\]

## Assumptions and scope

The endpoint distribution is the same for all \(2n\) observations, has no atoms, and the endpoints of different intervals are independent. Continuity of its cumulative distribution function reduces the entire order pattern to independent uniforms on \([0,1]\), with probability-one distinct endpoints. Intersections are nonempty intersections of closed intervals; ties have probability zero. The graph is labelled and simple, and the local invariant uses *open*, not closed, neighborhoods. The result concerns random intervals with independently sampled endpoints, not random unit intervals, graphons with arbitrary interval measures, or worst-case interval graphs.

## Proof

**Uniformization and an intersecting hub.** Apply the common distribution function to all endpoints. This preserves endpoint ordering and therefore preserves all interval intersections almost surely. Work with independent uniform endpoints. Fix \(n\ge2\) and an integer \(1\le k\le n\); set
\[t=\sqrt{\frac{k}{8n}},\qquad 0<t\le\frac12.\]
Call a sampled interval a **hub** if it contains the central segment \([t,1-t]\). Each interval has hub probability \(2t^2=k/(4n)\), since one endpoint must lie in \([0,t]\) and the other in \([1-t,1]\). Therefore the event \(H\) that at least one hub exists satisfies
\[\Pr(H^c)=\left(1-\frac{k}{4n}\right)^n\le e^{-k/4}.\]
Let \(Y\) be the number of sampled intervals whose two endpoints both lie in \([0,t]\), or both lie in \([1-t,1]\). These events are disjoint for an individual sampled interval, so
\[Y\sim\operatorname{Bin}\left(n,2t^2\right)=\operatorname{Bin}\left(n,\frac{k}{4n}\right).\]
On \(H\), choose any hub \(v\). An interval disjoint from \(v\) must lie wholly to the left of its left endpoint (at most \(t\)) or wholly to the right of its right endpoint (at least \(1-t\)), hence is among the \(Y\) tail intervals. In any maximum independent family, delete those at most \(Y\) intervals and also delete \(v\) if it belongs to that family (at most one more). The remaining family is independent and entirely contained in \(N(v)\). Thus
\[0\le D_n\le Y+1\quad\text{on }H.\]
Using the union bound over the \(k\)-subsets of intervals (no independence between \(H\) and \(Y\) is required),
\[\Pr(Y\ge k)\le\binom nk\left(\frac{k}{4n}\right)^k\le\left(\frac e4\right)^k,\]
where \(\binom nk\le(en/k)^k\). Combining the bounds proves the displayed tail inequality for \(k\le n\). For \(k>n\), the left-hand probability is zero since \(D_n\le n\).

**Consequences.** The right-hand side is the sum of two geometric tails, the slower decaying as \(e^{-k/4}\). Summing the tail probabilities by parts yields \(\sup_n\mathbb E e^{\lambda D_n}<\infty\) for every \(0<\lambda<1/4\). To show \(\alpha_n\to\infty\), fix any positive integer \(r\). Divide \([0,1]\) into \(r\) disjoint adjacent bins of length \(1/r\). Each bin contains both endpoints of at least one sampled interval with probability at least \(1-(1-r^{-2})^n\). Hence
\[\Pr(\alpha_n<r)\le r(1-r^{-2})^n\to0.\]
An interval wholly inside each bin forms a pairwise disjoint family. Combining this divergence with the uniform tightness of \(D_n\) gives \(D_n/\alpha_n\to0\) in probability and therefore \(\beta_n/\alpha_n\to1\).

## Verification

The standalone Python-standard-library file `verify.py` independently computes \(\alpha_n\) and every \(\alpha(G_n[N(v)])\) by exhaustive subset enumeration and by earliest-finish interval scheduling. It enumerates each possible perfect matching of the \(2n\) ordered endpoints for \(2\le n\le7\), a total of \(146598\) equally likely configurations. All optimization methods agree, and the histogram for \(n=7\) has counts \(100346,29068,4942,676,90,12,1\) at \(D_n=0,1,2,3,4,5,7\), respectively, summing to \(135135\). This exact finite verification checks definitions and the claimed local/global relation; it does *not* establish the infinite family of inequalities, which follows from the preceding analytic proof.

Run: `python3 verify.py`.

## Relationship to prior work

Justicz, Scheinerman and Winkler's *Random Intervals* (1990) studies the same iid-endpoint model, its maximum disjoint packing and universal intervals. The established exact probability \(2/3\) of a universal vertex implies only that \(\beta_n=\alpha_n\) on that event; it does not by itself control the other outcomes. Boucheron and Fernandez de la Vega (2001) study the fluctuations of the global independence number in the same model. Diaconis, Holmes and Janson's *Interval graph limits* (first publicly posted 2011-02-14) provides a detailed model comparison, including its Section 2.3 and Example 7.4, but does not derive the uniform additive local/global gap. De, Khurana and Singh (2023) explicitly discuss the independent kissing number for general geometric intersection graphs; their algorithmic and deterministic graph-parameter results are distinct from an iid random-interval concentration theorem. A complete historical equivalence search is not guaranteed, especially for older inaccessible full texts.

## Limitations

The tail bound is sufficient and not claimed to be sharp. It does not establish a limiting distribution for \(D_n\), the optimal tail exponent, or an exact finite-dimensional joint law of \(\alpha_n\) and \(\beta_n\). The independence claim for distinct tail samples comes from independently sampled endpoint pairs; it need not persist under alternative random interval models. This is an analytic mathematical finding with computational checks; it has not undergone independent mathematical audit. The full texts of two close historical papers were not available for detailed theorem-by-theorem comparison, leaving a specific historical-priority risk.

## References

1. Joyce Justicz, Edward R. Scheinerman and Peter M. Winkler, “Random Intervals,” *American Mathematical Monthly* 97 (1990), 881–889. https://doi.org/10.1080/00029890.1990.11995679
2. Stéphane Boucheron and Wenceslas Fernandez de la Vega, “On the Independence Number of Random Interval Graphs,” *Combinatorics, Probability and Computing* 10 (2001), 385–396. https://doi.org/10.1017/S0963548301004813
3. Persi Diaconis, Susan Holmes and Svante Janson, “Interval graph limits,” arXiv:1102.2841, first version publicly posted 2011-02-14. https://arxiv.org/abs/1102.2841
4. Minati De, Sambhav Khurana and Satyam Singh, “Online Dominating Set and Coloring for Geometric Intersection Graphs,” arXiv:2312.01467, first posted 2023-12-03. https://arxiv.org/abs/2312.01467
