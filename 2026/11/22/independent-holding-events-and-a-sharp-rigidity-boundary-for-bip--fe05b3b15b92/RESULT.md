# Independent holding events and a sharp rigidity boundary for bipartite tree exchange

## Finding

Fix integers \(a,b\ge 1\) and the labelled complete bipartite graph \(K_{a,b}\). Define the *cut-first uniform-reconnection chain* on its spanning trees as follows: at each discrete step select an edge of the current tree uniformly, delete it, and then choose uniformly among all host-graph edges joining the two resulting components, **including the deleted edge**. Add that edge to form the next tree. Set \(H_t=\mathbf{1}\{T_{t+1}=T_t\}\).

**Exact independence classification.** The holding indicators \((H_t)_{t\ge 0}\) are independent and identically distributed, for every deterministic or random starting spanning tree, whenever \(\min(a,b)\le 2\). Conversely, if \(a,b\ge3\), then under the uniform stationary tree law their consecutive covariance is strictly positive, so they are not independent. Thus \(\min(a,b)\le 2\) is the exact class of complete bipartite graphs with independent holding indicators under this update.

If \(\min(a,b)=1\), the host is a tree and every step holds. If \(a=2\), for every integer \(b\ge1\), the common holding parameter is
\[
q_b=\Pr(H_t=1)=\frac{b^2-b+4}{2b(b+1)}.
\]
In fact, the two-valued cut type and the holding indicator form an i.i.d. sequence of marked pairs: the *peripheral* class consists of the \(b-1\) edges incident to a degree-one vertex in the size-\(b\) part, and the *bridge* class consists of the other two edges. Their joint probabilities at every step are
\[
\begin{array}{c|cc}
 & H_t=1&H_t=0\\\hline
\mathrm{peripheral}&\dfrac{b-1}{2(b+1)}&\dfrac{b-1}{2(b+1)}\\
\mathrm{bridge}&\dfrac{2}{b(b+1)}&\dfrac{2(b-1)}{b(b+1)}
\end{array}.
\]
Consequently the number of unchanged updates in any \(r\) steps is exactly \(\operatorname{Bin}(r,q_b)\) for every initial state, while the number of attempted updates until the next genuine change has the geometric distribution with success probability \(1-q_b\), provided \(b\ge2\).

The holding probability is not monotone in the size-\(b\) part. Precisely,
\[
q_{b+1}-q_b=\frac{b-4}{b(b+1)(b+2)},
\]
so its unique integer minimizers are \(b=4\) and \(b=5\), both giving \(q_b=2/5\); after that it increases to \(1/2\).

For \(a,b\ge3\), write \(Q(T)=\Pr(T_{t+1}=T_t\mid T_t=T)\). The chain has the uniform spanning-tree law \(\pi\) as a reversible stationary measure and obeys
\[
\operatorname{Cov}_{\pi}(H_0,H_1)=\operatorname{Var}_{\pi}(Q(T))>0.
\]
For example, on \(K_{3,3}\) the exact covariance is \(2/10125\), giving an explicit contrast with independence at smaller bipartition width.

## Assumptions and scope

All graphs are simple complete bipartite graphs with fixed labelled vertices. The chain is *delete-first then uniformly reconnect across the induced cut*, with the removed edge included as an allowable replacement. It is not the more commonly studied procedure that first inserts a random host edge and then removes an edge of the resulting cycle. Updates use fresh independent randomness at every step. The theorem concerns the equality indicator of consecutive trees, not the independence of the tree states themselves or any mixing-time bound. The special case \(b=1\) gives a deterministic, one-state chain.

This is a finite-state theorem with no limit assumptions. Its primary probability classification is MSC2020 \(60J10\) (discrete-parameter Markov chains); the spanning-tree combinatorics supplies its proof.

## Proof

### General holding probability and stationarity

For a spanning tree \(T\) of a connected host graph \(G\), write \(c_T(e)\) for the number of host edges with endpoints in different components of \(T\setminus\{e\}\). The old edge is exactly one of these, so
\[
Q(T)=\frac1{|V(G)|-1}\sum_{e\in E(T)}\frac1{c_T(e)}.\tag{1}
\]
If two different spanning trees \(T,T'\) are connected by one such edge exchange, then removing their respective differing edges gives the same two-component forest \(F\). The forward and reverse transition probabilities are both \(1/[(|V|-1)c(F)]\), where \(c(F)\) is the number of crossing host edges. Thus the transition kernel is symmetric and the uniform spanning-tree law \(\pi\) is stationary and reversible. The spanning-tree exchange graph of any connected host is connected, so this is its unique stationary law.

Let \(H_t\) denote a holding event. Conditional on the current state \(T\), a hold occurs with probability \(Q(T)\). If that hold happens, the next state remains \(T\); since the next update uses independent randomness,
\[
\Pr_{\pi}(H_0=H_1=1)=\mathbb E_{\pi}[Q(T)^2],\qquad
\Pr_{\pi}(H_0=1)=\Pr_{\pi}(H_1=1)=\mathbb E_{\pi}Q(T).\tag{2}
\]
Subtracting establishes the covariance identity. In particular stationary independence is impossible if \(Q(T)\) is nonconstant. Conversely, if \(Q(T)=q\) at every state, then conditional on the full past of the chain, every fresh holding event has constant probability \(q\), and induction proves that the holding sequence is i.i.d. Bernoulli \(q\) for any initial law.

### The two-vertex side

For \(K_{2,b}\), each of the \(b\) vertices on the size-\(b\) side has tree degree at least one, while their degree sum equals \(b+1\), the number of tree edges. Hence exactly one of these vertices has degree two, and the other \(b-1\) have degree one. The two edges incident to the degree-two vertex are the bridge edges connecting the two size-two-side hubs; all remaining tree edges are peripheral.

Removing any peripheral edge isolates one size-\(b\)-side vertex. Exactly two host edges cross that cut, so the probability of selecting the old edge again is \(1/2\). Removing either bridge edge separates the two size-two-side hubs. If the component containing one hub has \(j\) vertices from the opposite class, then the number of crossing host edges is \(j+(b-j)=b\), so the conditional holding probability is \(1/b\). There are \(b-1\) peripheral and two bridge edges in *every* spanning tree, yielding
\[
Q(T)=\frac1{b+1}\left(\frac{b-1}{2}+\frac2b\right)
=\frac{b^2-b+4}{2b(b+1)}
\]
independently of its shape. The same class counts and probabilities establish the displayed four-cell joint law of cut type and holding. Since the conditional joint law is identical in every state and updates use fresh randomness, the successive marked pairs are i.i.d. by conditioning on the complete past.

For \(K_{1,b}\), the unique spanning tree is the whole host and \(Q(T)=1\). Elementary common-denominator calculation gives the difference formula for \(q_{b+1}-q_b\), and the sign of \(b-4\) gives both integer minimizers. Its limit is \(1/2\).

### The sharp obstruction at width three

Now assume \(a,b\ge3\) and let the bipartition be \(A=\{A_0,\ldots,A_{a-1}\}\), \(B=\{B_0,\ldots,B_{b-1}\}\). Construct two spanning trees:

- The **double star** \(T_D\): join \(A_0\) to every vertex of \(B\), and join \(B_0\) to each \(A_i\) for \(i\ge1\).
- The **zigzag** \(T_Z\): include \(A_0B_0\), \(A_1B_0\), \(A_1B_1\); join every \(B_j\) for \(j\ge2\) to \(A_0\); and every \(A_i\) for \(i\ge2\) to \(B_1\).

In the double star there are \(a-1\) leaf edges with crossing count \(b\), \(b-1\) leaf edges with crossing count \(a\), and one central edge with crossing count \(1+(a-1)(b-1)\). Thus by (1),
\[
(a+b-1)Q(T_D)=\frac{a-1}{b}+\frac{b-1}{a}+\frac1{1+(a-1)(b-1)}.\tag{3}
\]
In the zigzag, the \(a-2\) size-\(a\)-side leaves have crossing count \(b\), and the \(b-2\) size-\(b\)-side leaves have crossing count \(a\). Its three path edges have crossing counts
\[
2+(a-1)(b-2),\qquad 1+(a-1)(b-1),\qquad2+(a-2)(b-1),
\]
respectively. Put \(d=(a-2)(b-2)>0\). Since the first and third displayed counts equal \(b+d\) and \(a+d\), subtracting yields
\[
Q(T_D)-Q(T_Z)=\frac{1}{a+b-1}
\left(\frac1a+\frac1b-\frac1{a+d}-\frac1{b+d}\right)>0.\tag{4}
\]
Both trees occur with positive probability under the uniform stationary law. Thus \(\operatorname{Var}_{\pi}(Q(T))>0\), and (2) proves the converse classification. This also shows why independence is not a generic property of delete-first exchange.

For the illustrative \(K_{3,3}\) constant, enumeration of its \(81\) spanning trees gives holding probabilities \(41/150\), \(3/10\), and \(23/75\) with multiplicities \(36\), \(36\), and \(9\), respectively. Consequently \(\mathbb E_{\pi}Q=13/45\) and \(\operatorname{Var}_{\pi}(Q)=2/10125\). This exact finite computation is not needed to establish the all-size theorem.

## Verification

Run \(python verify.py\) with Python 3 and no third-party libraries. The checker independently enumerates all spanning trees of \(K_{2,b}\) for \(1\le b\le6\), calculates every cut and its host crossing-edge count using exact rational arithmetic, verifies the all-state formula, checks the two contrasting spanning-tree configurations on \(K_{3,3}\), \(K_{3,4}\), and \(K_{4,4}\), enumerates all \(81\) trees of \(K_{3,3}\) for the exact variance, verifies the increment formula at \(79\) successive sizes, and checks detailed balance on \(K_{2,3}\) and \(K_{3,3}\). The recorded run passed \(2345\) exact assertions. These finite tests supplement rather than replace the proof for arbitrary positive \(a,b\) and arbitrary time horizons.

## Relationship to prior work

Uniform spanning-tree sampling, random tree fragmentation, and labelled forest enumeration are classical. Aldous's 1990 random-walk construction concerns generation of uniform spanning trees. Pitman's 1999 unrooted-forest deletion theorem gives exact probability weights for the components after deleting edges from a random tree. Bertoin and Miermont (2012, first arXiv posting 19 January 2012) analyze *successive cutting*, with continuum limits, rather than the cut-first reconnect-and-hold indicators. These sources motivate the stochastic tree-exchange question but do not themselves state its sharp all-biclique independence boundary.

Dias and collaborators' 2018 **Linking and Cutting Spanning Trees** studies a different *insert-first* update: choose a host edge and, unless it is already present, remove an edge on the resulting cycle. Its trivial holding mechanism and transition kernel therefore differ from the delete-first rule examined here. Dong and Ge's later forest-containing-tree enumeration supplies relevant structural context, but its accessible abstract gives no holding-indicator process or classification. Existing bipartite spanning-tree overlap results concern *independently sampled* trees, not adjacent states of this transition kernel. The all-initial-state marked-i.i.d. law, exact two-hub boundary, stationary positive serial covariance in the complementary family, and sharp integer minimizers form one combined finding.

## Limitations

The result concerns only complete bipartite host graphs and precisely the specified cut-first transition. It does not determine the mixing time of the tree-valued chain and does not claim that the holding indicators are independent of the entire tree trajectory. For larger bipartition width, the theorem proves positive lag-one covariance at stationarity but no full correlation-decay formula. While the named source comparisons were made against accessible primary material and published summaries, an unidentified broader exchange-chain theorem could subsume the classification; independent historical review has not been performed.

## References

1. J. Bertoin and G. Miermont, *The cut-tree of large Galton-Watson trees and the Brownian CRT*, arXiv:1201.4081, first public preprint 2012-01-19. https://arxiv.org/abs/1201.4081
2. J. Pitman, *Coalescent Random Forests*, Journal of Combinatorial Theory, Series A **85** (1999), 165–193. https://www.stat.berkeley.edu/~pitman/457.pdf
3. D. J. Aldous, *The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees*, SIAM Journal on Discrete Mathematics **3** (1990), 450–465. https://doi.org/10.1137/0403039
4. R. Dias et al., *Linking and Cutting Spanning Trees*, Algorithms **11** (2018), article 53. https://doi.org/10.3390/a11040053
5. F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, Journal of Graph Theory **101** (2022), 79–94. https://doi.org/10.1002/jgt.22812
