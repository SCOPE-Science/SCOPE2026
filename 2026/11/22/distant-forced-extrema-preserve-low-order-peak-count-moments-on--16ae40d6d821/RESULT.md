# Distant forced extrema preserve low-order peak-count moments on vertex-transitive graphs

## Finding

**Exact finite-graph moment shielding theorem.** Let \(G=(V,E)\) be a finite, simple, vertex-transitive graph, \(|V|\ge2\). Fix distinct vertices \(b,t\) at finite graph distance \(D=d_G(b,t)\). Assign independent identically distributed, atom-free real fitnesses \((X_v)_{v\in V}\), and put
\[
I_v=\mathbf 1\{X_v>X_w\text{ for every }w\sim v\},\qquad K=\sum_{v\in V}I_v.
\]
Let \(\mathbb P_{b,t}\) be the law of the rankings conditional on \(b\) carrying the unique global minimum and \(t\) the unique global maximum. For every positive integer \(r\) with \(2r<D\),
\[
\boxed{\mathbb E_{b,t}K^k=\mathbb EK^k\quad(1\le k\le r).}
\]
Thus the first \(r\) cumulants of the peak count coincide **exactly** under the two laws. This result concerns the whole random count, not just its expected value.

For the \(d\)-dimensional binary hypercube \(Q_d\), opposite vertices are distance \(d\) apart; moment matching therefore holds through order \(\lfloor(d-1)/2\rfloor\). In particular, for \(d\ge5\), both laws have
\[
\mathbb EK=\frac{2^d}{d+1},\qquad
\operatorname{Var}K=\frac{2^{d-1}(d-1)}{(d+1)^2}.
\]
The mean and unconstrained variance formulas are background finite-graph calculations, not claimed as independent novel results. The new statement is their exact persistence under *simultaneously fixed antipodal global extrema* and the arbitrary-order, vertex-transitive extension.

## Assumptions and scope

The graph must be finite, simple, vertex-transitive; no independence among peak indicators is presumed. Conditioning on two distinguished extremal **locations** is conditioning on an event of probability \(1/(|V|(|V|-1))\). It is equivalent, for ranking statistics, to assigning fixed lowest and highest scores at \(b,t\), with independent continuously distributed interior ranks at the remaining vertices. The theorem is distribution-free for atom-free iid scores.

Here \(d_G\) is the ordinary undirected shortest-path distance, and \(N[v]=\{v\}\cup\{w:w\sim v\}\) denotes the closed neighborhood. The constant \(2\) in the distance threshold arises from the radius of these neighborhoods. The theorem claims matching only for the first \(r\) moments and cumulants, not the entire distribution.

## Proof

**1. A single prescribed extremal location leaves the count law unchanged.** If \(a\in V\) is arbitrary, vertex transitivity implies that the conditional distribution of \(K\) given \(a=\arg\min X\) is independent of \(a\), because an automorphism carries one designated vertex to another and preserves \(K\). These equiprobable conditioning events partition the sample space, so each conditional law equals the unconditional law. The same argument applies to \(a=\arg\max X\).

**2. Disjoint local comparisons remain independent after extremum conditioning.** Under any of the four rank laws \(\mathbb P\), \(\mathbb P_b^-\), \(\mathbb P_t^+\), and \(\mathbb P_{b,t}\) (unconstrained, prescribed minimum, prescribed maximum, both prescribed), the relative orders of unconstrained score values on disjoint vertex subsets are independent uniform permutations. If one subset contains a forced minimum or maximum, its relative order has that corresponding fixed extreme; it is still independent of the other subsets. Consequently any families of peak indicators with pairwise disjoint unions of their closed neighborhoods are independent under all four laws.

**3. Vanishing disconnected mixed cumulants.** For an ordered \(k\)-tuple of vertices \((v_1,\ldots,v_k)\), connect indices \(i,j\) whenever \(d_G(v_i,v_j)\le2\), including repetitions. If this index graph is disconnected, the corresponding families \((I_{v_i})\) depend on disjoint collections of scores, so their joint cumulant vanishes under each of the four laws. If the index graph is connected, the union \(U=\bigcup_iN[v_i]\) cannot include both \(b\) and \(t\) unless \(D\le2k\): a spanning path through the index graph has at most \(k-1\) hops of length at most two, with one extra graph edge at either endpoint to reach an extremum. Thus for \(k\le r\) and \(D>2r\), at least one forced extremum lies outside \(U\).

**4. Cancellation of one-extremum effects.** Every subtuple of a fixed \(k\)-tuple has its peak events determined entirely by \(U\). If \(t\notin U\), the joint rank laws within \(U\) are identical under \(\mathbb P_{b,t}\) and \(\mathbb P_b^-\), and under \(\mathbb P_t^+\) and \(\mathbb P\). Hence their mixed cumulants satisfy
\[
\kappa_{b,t}(I_{v_1},\ldots,I_{v_k})
=\kappa_b^-(I_{v_1},\ldots,I_{v_k})
+\kappa_t^+(I_{v_1},\ldots,I_{v_k})
-\kappa(I_{v_1},\ldots,I_{v_k}).
\]
The same identity holds with \(b,t\) reversed if \(b\notin U\); and it is trivially true when the dependency graph is disconnected (all four terms vanish). Summing over all ordered \(k\)-tuples and using multilinearity of cumulants yields
\[
\kappa_k(K\mid b,t)=\kappa_k(K\mid b\text{ minimum})
+\kappa_k(K\mid t\text{ maximum})-\kappa_k(K)=\kappa_k(K).
\]
The final equality follows from Step 1. The standard universal moment–cumulant polynomial identities convert equality of the first \(r\) cumulants to equality of the first \(r\) ordinary moments. This proves the theorem.

**5. Unconstrained hypercube variance and boundary instances.** Write \(N=2^d\). Every peak indicator on \(Q_d\) has mean \(p=1/(d+1)\). Distinct indicators have zero joint probability at distance one, and at distance two their joint peak probability is \(1/[d(d+1)]\): two neighborhoods share two competitors, and integrating their two independent center scores gives this value. At distance more than two they are independent. There are \(Nd/2\) unordered distance-one pairs and \(N\binom d2/2\) unordered distance-two pairs. Therefore
\[
\operatorname{Var}K=Np(1-p)-Nd p^2
+N\binom d2\left(\frac1{d(d+1)}-p^2\right)
=\frac{N(d-1)}{2(d+1)^2}.
\]
The stated opposite-extrema variance follows from Step 4 with \(r=2\), \(d\ge5\). For the sharp boundary examples, direct ranking enumeration gives constrained and unconditional means \(1,4/3\) on \(Q_2\). On \(Q_4\), the exact conditional variance \(6/7\), compared with unconstrained \(24/25\), follows by summing conditional pair probabilities. In detail, for two distinct nonadjacent non-forced centers \(v,w\) that are not adjacent to the forced maximum, let \(N(v)\) denote the open neighbor set, \(A=N(v)\setminus\{b,t\}\), \(B=N(w)\setminus\{b,t\}\), and write \(a=|A|\), \(c=|B|\), \(h=|A\cap B|\). Given the forced endpoints, their joint peak probability is
\[
\mathbb P_{b,t}(I_v=I_w=1)=\frac{1/(a+1)+1/(c+1)}{a+c-h+2}.
\]
Indeed, integrate the independent uniform center scores over the regions \(X_v<X_w\) and \(X_v>X_w\), requiring all common neighbors to lie below the smaller center score and all other neighbors below their own center scores. If the centers are adjacent the joint probability is zero, if either is the forced minimum or adjacent to the forced maximum the event is impossible, and if one is the forced maximum its indicator is one. Summing this finite formula over all unordered pairs gives the exact variances, independently checked in `verification/check.py`.

## Verification

Run `python3 verification/check.py` using the Python standard library. It exhaustively enumerates all score rankings on the six- and seven-cycles and on \(Q_2,Q_3\), checks the single-extremum invariance and applicable two-extremum moment identities, and independently reconstructs exact rational mean/variance formulas for \(Q_d\) through \(d=9\). These finite checks confirm the stated small-dimensional boundaries and the formulas for sampled dimensions. The cumulant/locality argument above, not the finite checks, proves the unbounded statement for every allowed \(r\) and \(G\).

## Relationship to prior work

Hegarty and Martinsson (arXiv:1210.4798, first posted 17 October 2012) analyze the House-of-Cards and constrained House-of-Cards fitness models on the binary hypercube, with conclusions about increasing accessible paths and their concentration, not exact all-order peak-count moment invariance. Neidhart, Szendro and Krug (arXiv:1402.3065, first posted 13 February 2014; open journal full text PMCID:PMC4196622) derive local-peak expectations for House-of-Cards and rough-Mount-Fuji landscapes, but do not establish the two-fixed-extrema mixed-cumulant cancellation. The elementary unconditional peak expectation and variance are treated as known or directly derivable baselines, not novelty claims. The precise contribution is the *distance-dependent moment shielding* for simultaneous global extremum constraints on any vertex-transitive graph.

## Limitations

No assertion is made when \(D\le2r\), nor is the full peak-count distribution shown invariant. This is a conditional ranking model, not a model with added fitness correlations or a continuously varying additive fitness gradient. The claim is independently proved here, but mathematical priority against a general unpublished or differently named cumulant-locality theorem remains unverified, and no independent audit has occurred. The exact sharpness examples address the first and second moments; sharpness at every order is not claimed.

## References

1. P. Hegarty and A. Martinsson, *On the existence of accessible paths in various models of fitness landscapes*, arXiv:1210.4798 (2012), full text https://arxiv.org/html/1210.4798v4.
2. J. Neidhart, I. G. Szendro and J. Krug, *Adaptation in Tunably Rugged Fitness Landscapes: The Rough Mount Fuji Model*, arXiv:1402.3065 (2014), open full text https://pmc.ncbi.nlm.nih.gov/articles/PMC4196622/.
