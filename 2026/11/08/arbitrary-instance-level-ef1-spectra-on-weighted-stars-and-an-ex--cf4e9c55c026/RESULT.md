# Arbitrary instance-level EF1 spectra on weighted stars and an exact \(n!\) allocation census

## Finding
Let \(G=K_{1,k}\) be a star with a hub and \(k\ge1\) leaves. All agents share the same nonnegative additive valuation of vertices, with hub value \(h\ge0\) and sorted leaf values \(0\le w_1\le\cdots\le w_k\). Every agent must receive a nonempty connected bundle, all vertices must be allocated, and fairness means **ordinary EF1**: for any two agents, the agent considering the other bundle may delete any one vertex from that bundle, even when deletion disconnects it.

For \(2\le n\le k+1\), put \(c=k-n+1\). A connected EF1 allocation to \(n\) labeled agents exists if and only if
\[
h+\sum_{i=1}^{c}w_i-\max\{h,w_c\}\le w_{c+1},\qquad 1\le c\le k-1.
\]
For \(c=0\), existence is automatic. For \(n=1\), existence is also automatic. When the criterion holds, an allocation is obtained by placing the hub and the \(c\) least-valued leaves in one bundle and allocating the remaining leaves as singletons.

Suppose additionally that \(0<w_1<\cdots<w_k\) and \(h>\sum_{i=1}^kw_i\). Then for every \(2\le n\le k+1\), the **number** of ordinary connected EF1 allocations to labeled agents is exactly
\[
n!\,\mathbf{1}\!\left\{\sum_{i=1}^{c}w_i\le w_{c+1}\right\},\qquad c=k-n+1,
\]
where the empty sum is zero. For \(n=1\) the count is one. Thus an attainable agent count has precisely \(n!\) labeled fair partitions, and an unattainable count has none.

For every \(k\ge3\) and every prescribed binary word \((\sigma_2,\ldots,\sigma_{k-1})\), there are *strictly increasing positive integer* leaf values and a larger positive integer hub value on this same star for which the EF1 feasibility at \(n=k-c+1\) is exactly \(\sigma_c\), simultaneously for every \(2\le c\le k-1\). Feasibility at \(n=1,k,k+1\) is always yes. In particular, arbitrary finite alternations of feasibility with the number of agents occur for one fixed graph and one fixed common strictly positive additive valuation.

The five-vertex star with hub value \(19\) and leaf values \((2,3,4,9)\) has numbers of fair allocations \((1,2,0,24,120)\) for \(n=1,2,3,4,5\), respectively. The star on five vertices is the smallest star allowing the **three-agent hole**: feasibility for two and four agents but not for three.

## Assumptions and scope
The items are the \(k+1\) **vertices**, not edges; the star's edges impose connectivity only. Valuation \(v(S)=\sum_{x\in S}v(\{x\})\) is defined for every subset, including a disconnected subset obtained after EF1 deletion. Every bundle is required to be nonempty and connected *before* deletion. Agents are labeled and items are individually identifiable. This is ordinary EF1, **not** EF1 up to an outer item, and it is not a statement of a universal guarantee over all valuations. The feasibility pattern is for a single fixed valuation repeated identically for the changing population of agents.

## Proof
**Connected-bundle form.** Exactly one bundle contains the hub. Every nonempty connected bundle not containing the hub is a single leaf. For \(n\ge2\), therefore, the hub bundle contains exactly \(c=k-n+1\) leaves, while \(n-1\) other bundles are singleton leaves.

**EF1 criterion for a fixed hub-leaf set.** If \(T\) is the set of leaves in the hub bundle, then a singleton leaf \(y\notin T\) values its own bundle at \(w_y\), and its envy of the hub bundle can be eliminated precisely when
\[
w_y\ge h+\sum_{i\in T}w_i-\max\bigl(\{h\}\cup\{w_i:i\in T\}\bigr).
\]
Every comparison involving a singleton as the envied bundle is automatically EF1 because that singleton can be deleted. Hence the allocation is EF1 exactly when the displayed inequality holds for the least-valued outside leaf. When \(T=\emptyset\), the right side is zero, so the allocation is EF1.

**Canonical least-leaf hub bundle.** For a fixed \(c\), replacing a selected leaf of value \(x\) by an outside leaf of value \(y\le x\) cannot increase the sum of all hub-bundle values except the largest: the function \(\sum z_i-\max z_i\) is coordinatewise nondecreasing. Simultaneously, the least value of the outside leaves cannot decrease, because the outside set replaces \(y\) by \(x\). Repeating exchanges produces \(T=\{1,\ldots,c\}\). Thus some hub bundle works if and only if this canonical one works, proving the general formula (including ties and zero values).

**Exact count under a dominant hub.** If \(h>\sum_iw_i\), deleting the hub gives the greatest possible reduction of the hub bundle, leaving \(\sum_{i\in T}w_i\). Assume the leaf weights are positive and strictly increasing. If \(T\) is not the set of the \(c\) smallest leaves, there exist an outside leaf \(y\) and a selected leaf \(x\) with \(w_y<w_x\). Since \(\sum_{i\in T}w_i\ge w_x>w_y\), the singleton owner of \(y\) still envies the hub owner after any deletion. The canonical hub-leaf set is consequently **the only possible one**, if it works at all. The hub bundle can be assigned to any one of \(n\) labeled agents and the remaining \(n-1\) labeled singleton leaves can be bijectively assigned in \((n-1)!\) ways, giving either \(n!\) or zero allocations. For \(n=k+1\), each bundle is singleton, giving \((k+1)!\) allocations; for \(n=1\), there is exactly one.

**Realizing every binary word.** Fix \(k\ge3\), start with \(w_1=2,w_2=3\), and for each \(c=2,\ldots,k-1\), recursively define
\[
w_{c+1}=\begin{cases}\sum_{i=1}^{c}w_i,&\sigma_c=1,\\w_c+1,&\sigma_c=0.\end{cases}
\]
These weights are strictly increasing positive integers. In a yes step, the prefix sum equals the next leaf value. In a no step,
\[
\sum_{i=1}^cw_i-(w_c+1)=\sum_{i=1}^{c-1}w_i-1\ge1,
\]
so the necessary-and-sufficient inequality fails. Choose \(h=1+\sum_{i=1}^kw_i\), and apply the dominant-hub count formula. The indices \(c=0\) and \(c=1\) are always feasible, as is the one-agent case. This proves arbitrary realizability, including arbitrary alternations.

**Smallest three-agent hole.** For \(k\le3\), whenever three nonempty bundles are possible, \(c=k-2\le1\), and their EF1 existence follows from the criterion. The five-vertex instance above has \(c=2\) for three agents, for which \(2+3>4\), while for two agents \(c=3\) and \(2+3+4=9\). This proves both the claimed hole and the minimum star size.

## Verification
The accompanying `verify.py` independently enumerates all labeled vertex-to-agent assignments for 80 deterministic sampled nonnegative weighted stars of at most five leaves, applying both connectivity and EF1 directly. Its 320 agent-count comparisons agree with the general prefix criterion. It also constructs all 510 prescribed words on stars with three through ten leaves, and for their 3,586 intermediate agent-count cases directly checks every candidate hub-leaf subset for EF1, agreeing with the all-or-none count formula. Direct enumeration on the five-vertex witness yields \((1,2,0,24,120)\). Run `python3 verify.py` using Python 3 standard library. These finite checks support the proof and are **not** a substitute for its all-size argument.

## Relationship to prior work
Chen and Zwicker (2024), *Cutsets and EF1 Fair Division of Graphs*, study which **graphs guarantee** connected EF1 or the stronger outer-good variant for **every** profile in a valuation class. Their Section 5 conjectures a three-block structure for these *universal* spectra and supplies the corresponding star example; the result here addresses a distinct, fixed-profile spectrum and **does not refute that conjecture**. Bei, Igarashi, Lu and Suksompong (2019/2022), *The Price of Connectivity in Fair Division*, establish graph-wide guarantees and impossibilities, including for trees and three agents, rather than the claimed fixed-profile exact counts and arbitrary-pattern construction. Hosseini, Pathak and Zhou (2025), *Non-Monotonicity in Fair Division of Graphs*, concern nonadditive cut valuations together with transfer-stability constraints and therefore do not imply this positive-additive, connectivity-constrained EF1 classification. The published results establish context, not a novelty certificate.

## Limitations
The arbitrary-pattern and exact \(n!\) census statements require a star with a hub value strictly larger than the combined leaf value and strictly increasing positive leaves. The feasibility criterion without these restrictions remains valid for any nonnegative identical additive valuation, but the \(n!\) count need not. No claim is made for heterogeneous valuations, larger graph families, EF1 after *outer* deletion, or universal guarantees. Priority searches can miss unindexed equivalents; independent external audit has not been performed.

## References
1. Jiehua Chen and William S. Zwicker, *Cutsets and EF1 Fair Division of Graphs*, arXiv:2402.05884, initial public version 2024-02-08, https://arxiv.org/abs/2402.05884 .
2. Xiaohui Bei, Ayumi Igarashi, Xinhang Lu, and Warut Suksompong, *The Price of Connectivity in Fair Division*, arXiv:1908.05433 (2019); SIAM Journal on Discrete Mathematics 36 (2022), https://arxiv.org/abs/1908.05433 .
3. Hadi Hosseini, Shraddha Pathak, and Yu Zhou, *Non-Monotonicity in Fair Division of Graphs*, arXiv:2511.03629 (2025), https://arxiv.org/abs/2511.03629 .
