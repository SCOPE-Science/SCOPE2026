# Exact minimal action budgets for partition-valued effectivity functions

## Finding

Let \(k\ge 2\). At a state \(w\) of a deterministic concurrent game, let \(R\) be the nonempty finite set of reachable outcomes. Suppose the prescribed individual-agent actual-effectivity family of each agent \(i\) is a partition \(\Pi_i\) of \(R\) into nonempty blocks. Assume **independence**: every choice \(B_i\in\Pi_i\) has nonempty intersection \(C(B_1,\ldots,B_k)=\bigcap_{i=1}^{k} B_i\).

Write \(t=\max_{B_i\in\Pi_i}|C(B_1,\ldots,B_k)|\). The smallest integer \(q\) for which the partition families can be realized by a deterministic concurrent game with **at most \(q\) distinct actions for each block of every agent** is exactly
\[
q=\left\lceil t^{1/(k-1)}\right\rceil.
\]
A realization exists with exactly \(q\) actions per block, simultaneously for every agent. In particular, **one action per block is possible exactly when all joint-block intersections are singletons**.

For \(k=2\), the stronger *coordinatewise exact minimum* holds. Enumerate \(\Pi_1=\{B_i:i\in I\}\) and \(\Pi_2=\{D_j:j\in J\}\), and put \(t_{ij}=|B_i\cap D_j|\). Among **all** deterministic realizations (including unequal multiplicities), the minimum possible number of actions realizing \(B_i\) is
\[
\alpha_i=\max_{j\in J} t_{ij},
\]
and the minimum possible number realizing \(D_j\) is
\[
\beta_j=\max_{i\in I} t_{ij}.
\]
Every one of these minima is attained **simultaneously** by one game. Thus the exact smallest total local action counts for the two agents are \(\sum_i\alpha_i\) and \(\sum_j\beta_j\), respectively.

## Assumptions and scope

The statement concerns a fixed local state of an ordinary *deterministic*, simultaneous-action game with \(k\) agents. Each agent has a nonempty finite action set, every complete action profile selects exactly one outcome in \(R\), and the actual-effectivity neighborhood of an action is its exact range of outcomes as the other agents vary their actions. Distinct actions may have the same neighborhood; their number is its **multiplicity**. The prescribed families \(\Pi_i\) consist of mutually disjoint nonempty subsets covering \(R\), and every tuple of blocks has nonempty intersection. No claim is made for arbitrary overlapping neighborhood families or for nondeterministic outcomes. At different states the construction is made independently, so the local theorems apply statewise to finite neighborhood frames with partition-valued neighborhoods.

## Proof

**Cell localization.** Every complete action profile has an outcome contained in each participating action's exact output set, hence in its joint block intersection. As \(\Pi_i\) is a partition, each \(x\in R\) belongs to a unique block of every agent; thus \(x\) is located in exactly one joint cell. All cells are nonempty by the hypothesis.

**Uniform lower bound.** Fix a cell \(C=\bigcap_i B_i\), an agent \(i\), and one action \(a_i\) whose range is \(B_i\). For each \(x\in C\), some completion of \(a_i\) produces \(x\), because \(a_i\) has the *whole* range \(B_i\). By uniqueness of the blocks containing \(x\), such a completion must select, for every other agent \(j\), an action whose range is \(B_j\). If every block has at most \(q\) actions, this gives at most \(q^{k-1}\) complete profiles that can produce the \(|C|\) distinct outcomes in \(C\). Therefore \(q^{k-1}\ge |C|\), and maximizing over cells gives \(q\ge\lceil t^{1/(k-1)}\rceil\).

**Uniform construction.** Let \(q=\lceil t^{1/(k-1)}\rceil\) and \(Q=\mathbb Z/q\mathbb Z\). Assign each agent \(i\) the actions \(\Pi_i\times Q\). For each cell \(C\), choose a surjection \(h_C:Q^{k-1}\twoheadrightarrow C\), possible because \(|C|\le q^{k-1}\). Given the profile \(((B_1,u_1),\ldots,(B_k,u_k))\), with \(C=\bigcap_i B_i\), define its outcome by
\[
 h_C(u_1-u_k,\ldots,u_{k-1}-u_k).
\]
For every fixed \(u_i\), the difference map from the other \(k-1\) coordinates is **bijective** onto \(Q^{k-1}\): when \(i=k\), choose all other coordinates directly; when \(i<k\), a prescribed difference at coordinate \(i\) determines \(u_k\), and the remaining differences determine the remaining coordinates. Thus each one-coordinate slice of the outcome array is surjective onto \(C\).

Fix an action \((B_i,u_i)\). Its outcomes lie in \(B_i\). Conversely, for every \(x\in B_i\), select the unique blocks \(B_j\) of the other agents containing \(x\). Since \(x\in C\), the slice-surjectivity just proved supplies other action labels that produce \(x\). Therefore the exact action range equals \(B_i\), as required.

**Two-agent coordinatewise lower bounds.** Let \(a_i\) (respectively \(b_j\)) denote the number of actions realizing \(B_i\) (respectively \(D_j\)). Fix any one action realizing \(D_j\). Because its range is all of \(D_j\), it must produce every \(x\in B_i\cap D_j\) for some opponent action. Only the \(a_i\) actions realizing \(B_i\) could produce such an \(x\), by the partition property. Consequently \(a_i\ge t_{ij}\), for all \(j\), so \(a_i\ge\alpha_i\). By symmetry \(b_j\ge\beta_j\).

**Simultaneous attainment.** Give agent 1 precisely \(\alpha_i\) actions \((B_i,u)\), with \(0\le u<\alpha_i\), and agent 2 precisely \(\beta_j\) actions \((D_j,v)\), with \(0\le v<\beta_j\). Enumerate each cell \(B_i\cap D_j\) as \(x_{ij,0},\ldots,x_{ij,t_{ij}-1}\). Let the outcome of \(((B_i,u),(D_j,v))\) be
\[
 x_{ij,(u+v)\bmod t_{ij}}.
\]
Both \(\alpha_i\) and \(\beta_j\) are at least \(t_{ij}\). Holding either action fixed while varying the other therefore produces **every** member of that cell. Taking all opponent blocks gives exactly its prescribed block. All lower bounds hold with equality at once, proving both coordinatewise and total optimality.

## Verification

The standalone `checker.py` generates every labelled-set partition tuple with two agents and at most six outcomes, three agents and at most five outcomes, and four agents and at most four outcomes. It selects precisely the tuples whose every joint cell is inhabited, constructs the claimed outcome arrays, and checks each action's exact range. It additionally checks the two-agent coordinatewise-minimum construction and the stated power lower bounds. The script examines 1,655 valid partition tuples and prints `ALL_CHECKS_OK`. These finite tests are supporting checks; the argument above proves the results for all finite \(R\) and all \(k\ge2\).

## Relationship to prior work

Ciardelli's *Inquisitive Action Logic* (2026), Theorem 2.2, characterizes which families of individual actual-effectivity neighborhoods can arise from deterministic concurrent games. The present hypotheses satisfy those existence conditions (nonempty neighborhoods, common range, and independence) but add a partition condition to derive **exact per-neighborhood minimum action counts**, rather than mere representability.

Earlier published work titled *Sharp local-range compression for actual-effectivity representations* bounds the action-copy factor by \(|R|\). *Sharp root-size action realization for finite actual-effectivity frames* improves its general bound to \(\lceil |R|^{1/(k-1)}\rceil\) and explicitly does not claim the exact minimum for each frame. The present theorem replaces that ambient-range size by the **largest joint-cell size** for partition-valued families, proves necessity for each such frame, and gives the exact nonuniform action vector for two agents. For example, if \(R=[n]\times[n]\) and the two partitions are coordinate fibres, every cell is a singleton; one action per block suffices for both agents even though \(|R|=n^2\).

Chen, Ju, and Ågotnes (2026) give representation theorems for two-agent actual powers, including generalized game frames. Their inspected two-agent construction is qualitative and does not state the partition-cell action-minimum formula. The slice-surjective modular arrays used here are elementary combinatorial devices; novelty is not claimed for modular addition or Latin-array constructions in isolation.

## Limitations

The optimality statement is local and assumes every neighborhood family partitions the entire common outcome range; arbitrary overlapping neighborhoods can behave differently. For three or more agents the theorem gives an exact **uniform maximum copies per block**, not an exact vector of nonuniform block multiplicities. No complexity-theoretic improvement for the full logic is claimed. Existing representation theorems supply the qualitative game semantics, so the new contribution is the quantitative and structural exactness under the partition hypothesis. Priority from differently phrased finite game-form or quasigroup realization literature remains a possible risk; no independent audit has been performed.

## References

1. Ivano Ciardelli, *Inquisitive Action Logic*, arXiv:2606.31866, first public version 2026-06-30, Theorem 2.2, https://arxiv.org/abs/2606.31866.
2. Zixuan Chen, Fengkui Ju, and Thomas Ågotnes, *Representation theorems for actual and alpha powers over two-agent general concurrent game frames*, arXiv:2603.04160, first public version 2026-03-04, https://arxiv.org/html/2603.04160v2.
3. *Sharp local-range compression for actual-effectivity representations*, published mathematical research record, 2026-10-04.
4. *Sharp root-size action realization for finite actual-effectivity frames*, published mathematical research record, 2026-10-04.
