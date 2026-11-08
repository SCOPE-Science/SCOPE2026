# Weighted triangular-book anti-coordination: exact equilibrium census and a singular tie transition

## Finding

**Theorem (complete equilibrium classification, welfare, and singular collapse).** Let \(k\ge2\), let \(a_i,b_i>0\) for \(1\le i\le k\), and let \(\tau>0\). The graph has hubs \(u,v\), their edge of weight \(\tau\), and page vertices \(z_1,\ldots,z_k\) with edges \(uz_i\) of weight \(a_i\) and \(vz_i\) of weight \(b_i\); there are no other edges. Every vertex chooses action \(0\) or \(1\). A player's payoff is the sum of the weights of incident edges leading to opponents taking the other action; strict unilateral improvement is required to violate Nash stability.

Put
\[
A=\sum_{i=1}^k a_i,\quad B=\sum_{i=1}^k b_i,\quad M=\sum_{i=1}^k\max(a_i,b_i),\quad C=A+B-M.
\]
Define \(L=\{i:a_i>b_i\}\), \(E=\{i:a_i=b_i\}\), \(A_L=\sum_{i\in L}a_i\), \(B_L=\sum_{i\in L}b_i\), and \(w(S)=\sum_{i\in S}a_i\) for \(S\subseteq E\). Let
\[
H(\tau)=\#\left\{S\subseteq E:\frac{A-\tau}{2}-A_L\le w(S)\le\frac{B+\tau}{2}-B_L\right\}.
\]
Then the number of **labeled, two-action pure Nash equilibrium profiles**, including distinct global action complements, is exactly
\[
\boxed{N(\tau)=2\mathbf{1}_{\{\tau\le\min(A,B)\}}+2H(\tau).}
\]
Every equilibrium belongs to exactly one of two types:

* **Aligned hubs:** both hubs use one action and all pages use the other. These two profiles exist exactly when \(\tau\le\min(A,B)\), and their cut weight is \(X=A+B\).
* **Opposite hubs:** fix hub actions \(u=0,v=1\). Each page with \(a_i>b_i\) uses action \(1\), each with \(a_i<b_i\) uses \(0\), while the pages indexed by \(S\subseteq E\) use \(1\). This profile is an equilibrium exactly when \(S\) contributes to \(H(\tau)\); each admits a distinct global complement. Every such equilibrium has cut weight \(Y=\tau+M\).

Social welfare is twice cut weight, and the global optimum is \(2\max(X,Y)\). The price of stability equals \(1\); the exact price of anarchy equals
\[
\boxed{\operatorname{PoA}=\frac{\max(X,Y)}{\min\bigl(\{X:\tau\le\min(A,B)\}\cup\{Y:H(\tau)>0\}\bigr)}.}
\]
The denominator set is nonempty. In particular, when \(\tau<C\), any inefficiency must come from an opposite-hub equilibrium; when \(C<\tau\le\min(A,B)\), aligned hubs are inefficient; and when \(\tau>\min(A,B)\), all equilibria are optimal. For \(\tau=C\), all equilibria have the same welfare.

The exact threshold for an opposite-hub equilibrium is
\[
\boxed{\tau_{\mathrm{split}}=\min_{S\subseteq E}\max\{0,A-2(A_L+w(S)),\,2(B_L+w(S))-B\};}
\]
thus opposite-hub equilibria exist exactly when \(\tau\ge\tau_{\mathrm{split}}\).

**Singular tie effect.** For every even \(k\ge2\), take \(\tau=1/2\) and \(a_i=b_i=1\). Then
\[
N(1/2)=2+2\binom{k}{k/2},\qquad\operatorname{PoA}=\frac{2k}{k+1/2}.
\]
Now change each spoke pair to \(a_i=1+\varepsilon\), \(b_i=1-\varepsilon\), for any \(0<\varepsilon<1/2\), keeping \(\tau=1/2\). Exactly two equilibria remain, both socially optimal; hence \(N=2\) and \(\operatorname{PoA}=1\). The perturbation can be arbitrarily small. As even \(k\to\infty\), the number removed is asymptotic to \(2^{k+1}\sqrt{2/(\pi k)}\).

## Assumptions and scope

The result concerns finite triangular-book graphs \(K_{1,1,k}\), strictly positive undirected edge weights, two available actions for every vertex, pure Nash equilibrium with weak indifference allowed, and no isolated players. The leaf/page vertices are individually labeled. It does not concern mixed Nash equilibrium, more than two actions, strong/cooperative deviations, nonedge interaction payoffs, or general graphs. The result holds for arbitrary positive real weights; computation with exact rational weights supplies finite spot checks.

## Proof

**1. Best replies of pages.** Suppose hubs coincide. Each page's two incident edges point to the same hub action and have strictly positive weights, so its unique best response is the opposite action. If hubs disagree, orient the two actions so \(u=0,v=1\). A page using action \(1\) gets \(a_i\), whereas action \(0\) yields \(b_i\). Thus it chooses \(1\) for \(a_i>b_i\), chooses \(0\) for \(a_i<b_i\), and is indifferent if \(a_i=b_i\). Every page-best-reply profile is therefore classified by a subset \(S\subseteq E\).

**2. Hub best replies.** In an aligned-hub page-best-reply profile, the payoffs of \(u\) and \(v\) are \(A\) and \(B\). A hub that flips gains only the spine edge, receiving \(\tau\), so the two aligned profiles are stable precisely for \(\tau\le\min(A,B)\). In a profile with \(u=0,v=1\) and subset \(S\), set \(P=L\cup S\). Hub \(u\) receives \(\tau+\sum_{i\in P}a_i\), but would receive \(A-\sum_{i\in P}a_i\) by flipping. Hub \(v\) receives \(\tau+B-\sum_{i\in P}b_i\), but by flipping would receive \(\sum_{i\in P}b_i\). Their respective stability inequalities are
\[
2\sum_{i\in P}a_i\ge A-\tau,\qquad2\sum_{i\in P}b_i\le B+\tau.
\]
Since \(a_i=b_i\) on \(E\), these are precisely the defining interval bounds for \(H(\tau)\). There are two action-complemented profiles for each admissible \(S\), proving the exhaustive count and the threshold formula by solving both inequalities for \(\tau\) and minimizing over subsets.

**3. Welfare and efficiency.** The sum of all player payoffs equals twice the total weight of cut edges. With hubs coincident, the largest possible cut weight is \(A+B\), achieved by opposing all pages. With hubs opposite, the spine is cut and each page contributes at most \(\max(a_i,b_i)\); independent optimal choices achieve \(\tau+M\). Thus the maximum is \(\max(X,Y)\). Flipping a single player's action changes that player's payoff by the same amount as it changes the cut weight, so any maximum cut is Nash stable. This proves price of stability \(1\) and ensures a nonempty denominator in the displayed price-of-anarchy formula. The two equilibrium cut weights and their existence indicators give the exact worst-equilibrium efficiency. Since \(Y-X=\tau-C\), the stated regimes follow. In the final regime, aligned equilibria do not exist, and all opposite-hub equilibria have cut weight \(Y\), which must equal the optimum.

**4. Singular family.** For equal unit spokes, both aligned profiles are stable at \(\tau=1/2\). In a split-hub profile, stability is equivalent to \(|2|S|-k|\le1/2\), forcing \(|S|=k/2\) when \(k\) is even. Thus there are \(2+2\binom{k}{k/2}\) equilibria. Their two cut weights are \(2k\) and \(k+1/2\), so the price of anarchy is \(2k/(k+1/2)\). After the positive asymmetric perturbation, each page has the unique action opposite \(u\), so the proposed split would give \(v\) a payoff of only \(1/2\); its unilateral flip instead yields \(k(1-\varepsilon)>1/2\). Hence no split-hub profile remains. Both aligned profiles are Nash stable since \(1/2<k(1-\varepsilon)\), and they attain the global maximum cut \(2k\) because \(1/2+k(1+\varepsilon)<2k\). Stirling's formula gives \(\binom{k}{k/2}\sim2^k\sqrt{2/(\pi k)}\) along even \(k\), establishing the loss asymptotic.

## Verification

The standalone reproducibility artifact `verify.py` reconstructs all graph edges, calculates each player's unilateral payoff change exactly with rational arithmetic, enumerates every binary action profile, and compares the resulting equilibrium census and welfare to the theorem's independent formula. It tests 2,605 parameter settings and 318,360 labeled profiles across exhaustive small choices, random rational heterogeneous weights, equality-boundary cases, and the singular perturbation family. Run with `python3 verify.py`. This finite experiment checks examples only; all-integer and real-weight cases are covered by the symbolic argument, not by enumeration.

## Relationship to prior work

The model is the binary weighted max-cut/anti-coordination game studied by Deligkas, Eiben, Gutin, Neary and Yeo [1] and by Carosi, Fioravanti, Gualà and Monaco [3]. Earlier work of Kun, Powers and Reyzin [4] studies existence, stability, and general price-of-anarchy bounds for the unweighted version; its general \(2\)-strategy upper bound of \(2\) also applies by the same payoff argument to positive weighted edges. The equivalence of its pure Nash equilibria with locally stable cuts, including minimum-stable-cut complexity, is established in particular by Lampis [2]. Crucially, [2, Theorem 3.5] already uses weighted complete bipartite graphs with two distinguished vertices and a PARTITION-type reduction. Therefore the partition-like special case with symmetric spokes and zero spine is **not** claimed as novel. The new assessed statement is the exact asymmetric positive-spine equilibrium count, the two-level welfare classification, the sharp split threshold, and the explicit disappearance of an exponential number of equilibria and all inefficiency under arbitrarily small asymmetric perturbations. The inspected primary texts do not state this joint characterization; a mathematically equivalent treatment elsewhere is not ruled out.

## Limitations

The analysis assumes strictly positive undirected weights and only two actions. It counts all labeled equilibria rather than symmetry classes, including tie equilibria. The subset-count formula can still require exponentially many subsets for unrestricted weights; it is an exact structural description, not a claim of polynomial-time computation in binary encoding. Literature searches do not prove worldwide novelty; the closest previously identified symmetric two-center partition reduction creates nontrivial priority risk. No independent external audit has been performed.

## References

[1] A. Deligkas, E. Eiben, G. Gutin, P. R. Neary and A. Yeo, *Some coordination problems are harder than others*, arXiv:2311.03195, first publicly posted 2023-11-06. https://arxiv.org/abs/2311.03195.

[2] M. Lampis, *Minimum Stable Cut and Treewidth*, arXiv:2104.13097, first publicly posted 2021-04-27, particularly Theorem 3.5. https://arxiv.org/abs/2104.13097.

[3] R. Carosi, S. Fioravanti, L. Gualà and G. Monaco, *Coalition Resilient Outcomes in Max k-Cut Games*, arXiv:1810.09278, first publicly posted 2018-10-22. https://arxiv.org/abs/1810.09278.

[4] J. Kun, B. Powers and L. Reyzin, *Anti-Coordination Games and Stable Graph Colorings*, arXiv:1308.3258, first publicly posted 2013-08-14. https://arxiv.org/abs/1308.3258.
