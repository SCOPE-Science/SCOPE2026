# Exact heterogeneous action-copy budgets for finite actual effectivity

## Finding
Fix integers \(k\ge2\) and \(r\ge1\), and a positive integer vector \(\mathbf m=(m_1,\ldots,m_k)\). For every finite representable actual-effectivity frame with at most \(r\) possible local outcomes, a deterministic concurrent-game realization having **exactly \(m_i\) copies per distinct neighborhood of agent \(i\)** exists if and only if
\[
\prod_{j\ne i}m_j\ge r\quad\text{for every }i\in\{1,\ldots,k\}.
\]
Equivalently, writing the budgets in nondecreasing order as \(m_{(1)}\le\cdots\le m_{(k)}\), the criterion is
\[
\prod_{i=1}^{k-1}m_{(i)}\ge r.
\]
This characterizes the full feasible region of possibly unequal local action-copy budgets. For example, with three agents and five possible outcomes, \((2,3,3)\) works while \((2,2,4)\) does not. Uniform copies \((3,3,3)\) work but are unnecessary.

## Assumptions and scope
An actual-effectivity frame is \(F=(W,(\Sigma_i)_{i=1}^k)\), where \(W\) is a finite nonempty set and, for every \(w\in W\), \(\Sigma_i(w)\) is a nonempty finite family of nonempty subsets of \(W\). We assume three conditions at each \(w\): (a) all unions \(O(w)=\bigcup\Sigma_i(w)\) coincide and are nonempty, (b) every choice \(S_i\in\Sigma_i(w)\) satisfies \(\bigcap_iS_i\ne\varnothing\), and (c) \(1\le |O(w)|\le r\). An action of agent \(i\) is a pair \((S_i,x_i)\) with \(S_i\in\Sigma_i(w)\) and copy index \(0\le x_i<m_i\). An action's actual-effectivity set is the set of states attainable when that action is held fixed while all other agents' actions vary. Actions with different copy indices remain distinct even when their outcome sets agree. The transition is deterministic and all actions are simultaneous; all states and actual-effectivity families are retained.

## Proof
**Necessity.** Take \(|W|=r\) and \(\Sigma_i(w)=\{W\}\) for every world and agent. This satisfies all assumptions. With the prescribed copies, each agent has exactly \(m_i\) actions at each world. Fixing one action of agent \(i\) leaves exactly \(\prod_{j\ne i}m_j\) joint completions. Since its outcome set must equal \(W\), at least \(r\) different outputs are required, so \(\prod_{j\ne i}m_j\ge r\). This argument applies to every agent. The least such product is the one obtained by omitting a largest budget, proving the sorted equivalence.

**Mixed-modulus slice lemma.** Reorder the agents so that \(m_k\ge m_i\) for \(i<k\). Put \(X_i=\{0,\ldots,m_i-1\}\) and \(Y=X_1\times\cdots\times X_{k-1}\). Define
\[
H(x_1,\ldots,x_k)=\bigl((x_1+x_k)\bmod m_1,\ldots,(x_{k-1}+x_k)\bmod m_{k-1}\bigr).
\]
For every fixed \(x_k\), the other \(k-1\) coordinates vary independently and \(H\) runs through all of \(Y\). If a coordinate \(x_i\) with \(i<k\) is fixed and a target \(y\in Y\) is given, choose \(x_k\in X_k\) with \(x_k\equiv y_i-x_i\pmod {m_i}\), possible because \(m_k\ge m_i\), then choose each \(x_j\equiv y_j-x_k\pmod {m_j}\) for \(j\ne i,k\). Thus **every fixed-coordinate slice of \(H\) is onto \(Y\)**. The hypothesis says \(|Y|=\prod_{i<k}m_i\ge r\). At each world choose a surjection \(\pi_w:Y\twoheadrightarrow O(w)\) and put \(c_w=\pi_w\circ H\). Every fixed-coordinate slice of \(c_w\) is onto \(O(w)\).

**Realization.** For each tuple \((S_1,\ldots,S_k)\) of neighborhoods at \(w\), select a point \(d_w(S_1,\ldots,S_k)\in\bigcap_i S_i\). For an action profile \(((S_1,x_1),\ldots,(S_k,x_k))\), calculate \(z=c_w(x_1,\ldots,x_k)\); output \(z\) if it belongs to \(\bigcap_iS_i\), and otherwise output the selected fallback \(d_w(S_1,\ldots,S_k)\). This always returns an element of every selected neighborhood. Hence fixing agent \(i\)'s action \((S_i,x_i)\) can only produce states in \(S_i\). Conversely, given \(u\in S_i\), the common-union assumption permits each other agent \(j\) to select some \(S_j\in\Sigma_j(w)\) containing \(u\). Slice-surjectivity with \(x_i\) fixed gives copy labels for all other agents making \(z=u\). Then \(u\in\bigcap_jS_j\), so the transition outputs \(u\). Every element of \(S_i\) therefore occurs, and the actual-effectivity set is **exactly** \(S_i\), for each of its \(m_i\) action copies. This proves sufficiency at each world; assemble the local transitions into one concurrent game on \(W\).

## Verification
Run `python checks/verify_budget.py` using Python 3 without external libraries. The checker evaluates all fixed-coordinate slices for \(1,486\) small admissible parameter instances with two, three, or four agents; directly reconstructs exact action outcome sets on \(463\) finite frame instances, including all admissible two-agent neighborhood families with at most three neighborhoods per agent and at most three outcomes; and checks representative feasible and infeasible asymmetric profiles. It returns `VERIFY_OK slice_cases 1486 frame_cases 463`. These finite checks corroborate, but do not substitute for, the proof for unbounded \(k\) and \(r\).

## Relationship to prior work
Ciardelli's *Inquisitive Action Logic* (2026) proves the qualitative representability conditions and constructs actions with outcome-state labels; these premises are used here. The published *Sharp root-size action realization for finite actual-effectivity frames* (2026) improves to the worst-case **uniform** \(\lceil r^{1/(k-1)}\rceil\)-copy bound, using equal-modulus slice arrays. Its proof also states the necessary fixed-action product inequality, which is therefore **not** claimed as new. The present contribution is the exact sufficiency and hence the complete feasible region for **arbitrary unequal** action budgets, using the mixed-modulus slice construction; the uniform case is expressly a known corollary. General polychromatic coloring and cover-decomposition literature provides combinatorial context but does not supply this exact multi-agent realization criterion in the inspected material.

## Limitations
The theorem is a universal guarantee over all finite actual-effectivity frames with at most \(r\) outcomes at each world. A particular frame may admit fewer action copies than this worst-case region. A set-valued outcome model, stochastic transition, infinite world set, or additional constraints on the transition table is not included. The slice lemma is elementary and related to known quasigroup-type constructions; an equivalent heterogeneous budget theorem in earlier unindexed literature remains possible. No independent mathematical or priority audit is claimed.

## References
1. Ivano Ciardelli, *Inquisitive Action Logic*, arXiv:2606.31866, first public version June 30, 2026, https://arxiv.org/abs/2606.31866.
2. *Sharp root-size action realization for finite actual-effectivity frames* (published research record, October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-root-size-action-realization-for-finite-actual-effectivity--114a0e0912e6.
3. Béla Bollobás, David Pritchard, Thomas Rothvoß, and Alex Scott, *Cover-Decomposition and Polychromatic Numbers*, arXiv:1009.6144, https://arxiv.org/abs/1009.6144.
