# Parity-sensitive compatibility of temporal EF1 and Pareto optimality for reciprocal two-phase goods

## Finding

For all integers \(p\ge2\), \(q\ge1\), and all real numbers \(\alpha>\beta>0\), a temporally EF1 and final-Pareto-optimal allocation exists **if and only if**
\[
q\beta\le\alpha\bigl(1+(p\bmod 2)\bigr).
\]
If the inequality holds, the exact number of valid assignments of the **distinct arriving goods** is
\[
N(p,q;\alpha,\beta)=2^{\lfloor p/2\rfloor};
\]
otherwise it is zero. In particular, the maximum allowable second-phase length is \(\lfloor\alpha/\beta\rfloor\) after an even first phase, but \(\lfloor 2\alpha/\beta\rfloor\) after an odd first phase. This parity jump is independent of the number of completed first-phase pairs.

## Assumptions and scope

There are precisely two agents, denoted 1 and 2, and every indivisible item is allocated immediately and irrevocably to one agent. The first \(p\ge2\) arriving items have type \(A\), followed by \(q\ge1\) items of type \(B\). Although items within a type have equal values, they are individually distinct and identified by their arrival rounds. Values are additive and reciprocal: agent 1 values one \(A\) at \(\beta\) and one \(B\) at \(\alpha\); agent 2 values one \(A\) at \(\alpha\) and one \(B\) at \(\beta\), where \(\alpha>\beta>0\). No later reallocation is allowed.

For a prefix, EF1 means that for each ordered pair of agents \((i,j)\), either the recipient \(j\) has an empty bundle or there is an item \(g\) in \(j\)'s bundle such that \(v_i(X_i)\ge v_i(X_j\setminus\{g\})\). TEF1 requires this at every nonempty arrival prefix. Final Pareto optimality (PO) means that there is no alternative complete assignment of the same goods that makes both agents weakly better off and at least one strictly better off. The final PO requirement, rather than just PO for each newly arriving item, matters here.

## Proof

**1. Pareto-optimality dichotomy.** A final assignment with an \(A\) item assigned to agent 1 and a \(B\) item assigned to agent 2 is not PO: exchanging these items raises each agent's utility by \(\alpha-\beta>0\). Conversely, if every \(B\) item is assigned to agent 1, the assignment maximizes the strictly positive weighted welfare \(\alpha v_1+\beta v_2\): each \(A\) contributes \(\alpha\beta\) regardless of recipient, while a \(B\) contributes \(\alpha^2\) when assigned to agent 1 instead of \(\beta^2\) when assigned to agent 2. Every maximizer of positive weighted welfare is PO. Similarly, if every \(A\) is assigned to agent 2, the assignment maximizes \(\beta v_1+\alpha v_2\) and is PO. Hence the absence of a crossed pair is both necessary and sufficient for PO.

**2. First-phase temporal fairness.** In any prefix containing only \(A\) items, both agents strictly value each \(A\) equally within their own valuation. Thus EF1 is equivalent to the two agents' counts of allocated \(A\) goods differing by at most one. In particular, after the first two items each agent has one \(A\), so agent 1 receives an \(A\). Step 1 therefore forces every subsequently arriving \(B\) to agent 1. Moreover, the counts differ by at most one after *every* first-phase prefix exactly when each consecutive pair of \(A\) items is split one-one, and any odd final \(A\) can initially be assigned either way.

**3. The odd endpoint is forced.** Write \(p=2k+1\) with \(k\ge1\). If the final first-phase \(A\) goes to agent 1, the type-\(A\) counts are \((k+1,k)\). After the first \(B\) is assigned to agent 1 as compelled by PO, agent 2 values her own bundle at \(k\alpha\) but values agent 1's bundle after discarding its most valuable single item at \(k\alpha+\beta\). (For agent 2, an \(A\) is more valuable than a \(B\).) Because \(\beta>0\), this violates EF1. Thus the last first-phase \(A\) must go to agent 2, yielding the endpoint counts \((k,k+1)\). For even \(p=2k\), the counts are necessarily \((k,k)\).

**4. Exact last-phase bound.** Let \(t\), with \(1\le t\le q\), denote the number of \(B\) goods already assigned to agent 1. At this prefix, write the first-phase \(A\) counts as \((a_1,a_2)=(k,k+\varepsilon)\), with \(\varepsilon=p\bmod2\in\{0,1\}\) and \(k\ge1\). Agent 1 is EF1 toward agent 2 automatically: her own value is \(\beta k+\alpha t\), at least the value \(\beta(k+\varepsilon-1)\) of agent 2's bundle after one \(A\) is discarded. For agent 2, the largest single item in agent 1's bundle is an \(A\), worth \(\alpha\), since \(\alpha>\beta\) and \(k\ge1\). Hence her EF1 condition is equivalent to
\[
\alpha(k+\varepsilon)\ge\alpha k+\beta t-\alpha
\quad\Longleftrightarrow\quad
\beta t\le\alpha(1+\varepsilon).
\]
These inequalities hold for every second-phase prefix exactly when they hold at \(t=q\). This proves necessity and sufficiency.

**5. Exact number of allocations.** For each of the \(k=\lfloor p/2\rfloor\) successive \(A\)-pairs, choose which agent receives the first item (two independent choices). The odd final \(A\), if any, must go to agent 2, and all \(B\) goods must go to agent 1. These \(2^k\) choices are distinct labeled-item assignments and exhaust the possibilities by Steps 1–4. The criterion includes equality and does not require integral values or integral utility ratios.

## Verification

The accompanying `verify.py` uses Python standard-library exhaustive enumeration. It independently computes Pareto optimality by testing every complete competing assignment and computes EF1 for every ordered agent pair at every prefix. These results agree with the theorem for 192 parameter cases, encompassing 45,120 direct candidate assignments and 105 feasible parameter cases. A second set of 189 larger parameter cases checks the theorem against exact exhaustive enumeration based on the crossed-pair PO characterization. Run `python3 verify.py`; the expected four printed PASS lines identify the exact case counts. The finite experiments corroborate the proof and are not used as evidence for untested infinite sizes.

## Relationship to prior work

Elkind, Lam, Latifian, Neoh and Teh (2024), *Temporal Fair Division of Indivisible Items*, introduce temporal EF1 and give a two-agent incompatibility example for simultaneous TEF1 and Pareto optimality (Proposition 4.2), as well as existence results for TEF1 without PO and broader complexity results. Their specific two-plus-two goods counterexample at value levels \((\alpha,\beta)=(2,1.1)\) lies above the even-phase threshold here. The present result characterizes an infinite reciprocal-valuation, two-block family, including its sharp phase-length boundary and exact allocation count; it does not challenge the earlier impossibility claim.

Cookson, Ebadian and Shah (2024), *Temporal Fair Division*, study per-day fairness and cumulative fairness; a per-day PO condition for a one-item day does not impose PO on the eventual combined assignment. Choi, Li and Teh (2026), *Temporal Fair Division of Indivisible Mixed Manna: Tractable Settings*, investigate other structured temporal domains, including positive-value normalization agreement and blocks of chores followed by goods. The reciprocal positive-goods valuations considered here do not satisfy the former agreement condition when \(\alpha>\beta\). These comparisons concern mathematical hypotheses and implications, not merely terminology.

## Limitations

The theorem is restricted to exactly two agents, two consecutive homogeneous phases, strictly positive reciprocal valuations and \(p\ge2\). It says nothing about arbitrary arrival sequences, nonreciprocal valuations, mixed goods and chores, or online algorithms without advance knowledge. Pareto optimality is required only for the final allocation; all intermediate allocations must be EF1. Priority relative to unindexed equivalent research remains uncertain, and no independent external audit is claimed.

## References

- Edith Elkind, Alexander Lam, Mohamad Latifian, Tzeh Yuan Neoh, Nicholas Teh, *Temporal Fair Division of Indivisible Items* (first public version 2024-10-18), https://arxiv.org/abs/2410.14593 . Relevant material: Section 3, Proposition 4.2 and adjacent discussion.
- Benjamin Cookson, Soroush Ebadian, Nisarg Shah, *Temporal Fair Division* (first public version 2024-10-30), https://arxiv.org/abs/2410.23416 . Relevant material: fairness notions, two-agent results and appendix.
- Kui-Wang Choi, Minming Li, Nicholas Teh, *Temporal Fair Division of Indivisible Mixed Manna: Tractable Settings* (2026), https://arxiv.org/abs/2608.20033 . Relevant material: structured valuations and two-part sequences.
