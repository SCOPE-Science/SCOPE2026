# An exact three-day temporal EFX frontier for two recurring positive goods

## Finding

Two agents with the same additive valuation divide exactly two newly arriving goods each day: one good of value \(H\), one of value \(L\), where \(H\ge L>0\). Previously allocated goods cannot be moved, and every arriving good must be allocated on its arrival day. For \(\alpha\in[0,1]\), an allocation is *\(\alpha\)-TEFX* through day \(T\) if, for every day \(1\le t\le T\), distinct agents \(i,j\), and every good \(g\) in the cumulative bundle \(A_j^t\),
\[
v(A_i^t)\ge\alpha\,v(A_j^t\setminus\{g\}).
\]
Let \(\alpha_T^*(H,L)\) be the maximum such factor over all complete, irrevocable allocation schedules through day \(T\). Write \(h=H/L\).

**Exact existence boundary at all horizons.** For \(T=1,2\), \(\alpha_T^*(H,L)=1\) for every \(h\ge1\). For every integer \(T\ge3\), exact TEFX is feasible if and only if \(h\le2\).

**Exact three-day frontier.**
\[
\boxed{\alpha_3^*(H,L)=\begin{cases}
1,&1\le h\le2,\\
\displaystyle\max\left\{\frac{h+2}{2h},\frac{h}{h+1}\right\},&h>2.
\end{cases}}
\]
The two branches cross once at \(h_0=(3+\sqrt{17})/2\). Equivalently, beyond the exact-feasibility region the first branch is optimal for \(2<h\le h_0\) and the second for \(h\ge h_0\), with a tie at \(h_0\). In particular, the sharp uniform guarantee for the entire three-day recurring-two-good family is
\[
\boxed{\inf_{H\ge L>0}\alpha_3^*(H,L)=(\sqrt{17}-1)/4.}
\]

## Assumptions and scope

There are precisely two agents with an identical, nonnegative, additive valuation, and exactly two *distinct physical goods* arrive per day, one with value \(H\) and the other with value \(L\). The same two values recur every day, and \(H\) and \(L\) are finite positive real numbers. Both goods are completely and immediately allocated, possibly to the same agent. Future arrival values are known, but past allocations cannot be modified. Fairness is checked at **every prefix** and against deletion of **every** single good in the other agent's entire cumulative bundle. There is no requirement to split each day's goods between the agents. This last allowance is essential for the second three-day branch.

## Proof

**1. A useful two-bundle identity.** At any day, write \(V_X=v(X)\), \(V_Y=v(Y)\). As all individual values are positive, if \(Y\ne\varnothing\) its strongest condition against agent \(X\) is obtained by deleting the *least valued* good of \(Y\):
\[
V_X\ge \alpha\bigl(V_Y-\min_{g\in Y}v(g)\bigr).
\]
An empty rival bundle imposes no constraint. Consequently, for \(\alpha=1\), if \(V_Y\ge V_X\), the only potentially active condition is \(V_Y-V_X\le\min_{g\in Y}v(g)\). These are direct algebraic rewrites of the definition, including the singleton case, where the right side is zero.

**2. Exact TEFX for one or two days.** On day 1 assign \(H\) to agent \(X\) and \(L\) to agent \(Y\); both bundles are singletons and hence EFX. On day 2 assign \(H\) to \(Y\) and \(L\) to \(X\); both bundles now have total value \(H+L\), hence are EFX. For any horizon, continue alternating these two daily assignments. At even day \(t=2k\) the cumulative values are equal. At odd day \(t=2k+1\ge3\), the larger bundle has total \((k+1)H+kL\), the smaller has \(kH+(k+1)L\), and the difference is \(H-L\). The larger bundle contains a good valued \(L\), so the identity from Step 1 gives exact EFX precisely when \(H-L\le L\), equivalently \(H\le2L\). Day 1 has already been handled. Therefore \(H\le2L\) suffices for exact TEFX at every horizon.

**3. Sharp upper bound beyond \(H=2L\).** Assume \(H>2L\) and seek any positive three-day factor. If both first-day goods go to one agent, the empty-handed agent fails every positive-factor EFX inequality after deleting either single positive good, hence every feasible positive-factor schedule must split day 1. By symmetry take \(X\) to receive \(H\) and \(Y\) to receive \(L\). There are exactly four possible assignments of the second day's two goods:

* *Cross:* assign \(L\) to \(X\) and \(H\) to \(Y\). Both day-2 bundles have value \(H+L\). On day 3, if its goods are split between agents, the resulting higher-valued bundle consists of two \(H\)-goods and one \(L\)-good; its rival has one \(H\)-good and two \(L\)-goods. Deleting an \(L\)-good from the higher-valued bundle gives the bound \(\alpha\le(H+2L)/(2H)=:C\). If both day-3 goods instead go to the same agent, deleting its least valuable good gives \(\alpha\le(H+L)/(2H+L)<C\), since \(2H(H+L)<(H+2L)(2H+L)\) for positive \(H,L\). Thus every cross schedule has factor at most \(C\).
* *Repeat:* assign \(H\) to \(X\) and \(L\) to \(Y\). At day 2 the bundle values are \(2H\) and \(2L\), so deleting one of the two \(H\)-goods gives \(\alpha\le2L/H\le C\) because \(H\ge2L\).
* *Both to \(X\):* agent \(X\)'s day-2 bundle is \(\{H,H,L\}\); \(Y\)'s is \(\{L\}\). Deleting the \(L\)-good from \(X\)'s bundle yields \(\alpha\le L/(2H)\le C\).
* *Both to \(Y\):* agent \(X\)'s bundle is \(\{H\}\); \(Y\)'s is \(\{H,L,L\}\). Deleting an \(L\)-good from \(Y\)'s bundle gives \(\alpha\le H/(H+L)=:D\).

Every possible three-day schedule has therefore \(\alpha\le\max\{C,D\}\).

**4. Sharp constructions.** For \(C\), cross on day 2 and assign \(H\) to \(X\), \(L\) to \(Y\) on day 3. Days 1 and 2 are exactly EFX. Day 3 produces \(\{H,H,L\}\) versus \(\{H,L,L\}\), so deleting \(L\) from the first bundle is the only binding inequality, attaining \(C\). For \(D\), on day 2 assign *both* goods to \(Y\), and on day 3 assign \(H\) to \(X\) and \(L\) to \(Y\). At day 2 the binding ratio is \(H/(H+L)=D\). At day 3 the bundles are \(\{H,H\}\) and \(\{H,L,L,L\}\); for \(H\ge2L\), removing an \(L\)-good from the second bundle leaves \(H+2L\le2H\), so day 3 is exactly EFX. Hence \(D\) is attained. Combined with Step 3, this proves the exact three-day frontier for all \(H>2L\). In particular both \(C,D<1\), giving necessity of \(H\le2L\) for every horizon containing day 3.

**5. Crossover and uniform optimum.** On \(h>2\), the functions \(C(h)=(h+2)/(2h)\) and \(D(h)=h/(h+1)\) are respectively strictly decreasing and strictly increasing. Their equality is equivalent to \(h^2-3h-2=0\); its unique root above two is \(h_0=(3+\sqrt{17})/2\). Thus the maximum of the two branches decreases up to \(h_0\) and increases afterwards, and its minimum is \(D(h_0)=(\sqrt{17}-1)/4\). On \(1\le h\le2\) the optimum equals one, so this is also the unrestricted uniform infimum. All assertions follow. \(\square\)

## Verification

The standalone, standard-library Python program `check_temporal_efx.py` independently computes the minimum prefix-wise EFX factor of each of the \(4^3=64\) labeled three-day schedules at each of 21 rational values of \(H/L\). The check processes \(1344\) schedules and compares the exact rational maximum with the proposed formula. A separate finite-state recursion checks exact TEFX reachability over nine days for the same 21 ratios, and symbolic-rational checks test the crossover interval and sample values. Running `python3 check_temporal_efx.py` passes all assertions. These finite computations check the implementation and examples; the continuum formula, complete upper bound, and all-horizon existence theorem are proved analytically above, not inferred from enumeration.

## Relationship to prior work

Choi and Li, *Temporal Fair Division of Indivisible Goods with Scheduling* (arXiv:2601.12835, first posted 2026-01-19), prove that three identical rounds can obstruct exact TEFX, giving the concrete daily value multiset \(\{0,1,3\}\), and establish a \(1/2\)-TEFX construction for two agents on identical days. The zero item in the negative example is used to extend an argument based on the positive values \(1,3\). Therefore that paper already covers a particular nonexistence witness: the present claim is **not** a first negative instance. Its separate content is the continuum-wide exact \(H/L=2\) existence boundary, sharp three-day approximation frontier, algebraic optimizer transition, and uniform sharp factor.

Choi and Li, *Temporal Fair Division of Indivisible Goods with Structured Constraints* (arXiv:2607.17224, first posted 2026-07-19), repeat the identical-day negative example and prove a general \(1/2\)-TEFX guarantee on identical days. They also give value-dependent bounds for general identical valuations and arbitrary bi-valued sequences. Those broadly applicable guarantees are not exact for the two-agent, two-good-per-day, three-day domain and do not imply the claimed two-branch optimum. Elkind et al., *Temporal Fair Division of Indivisible Items* (arXiv:2410.14593), establish earlier temporal impossibility results without this sharp parameter classification. Cookson, Ebadian and Shah, *Temporal Fair Division* (arXiv:2410.23416), address EFX per day combined with cumulative EF1, not cumulative EFX at every prefix; Igarashi et al., *Repeated Fair Allocation of Indivisible Items* (arXiv:2304.01644), study related repeated-allocation fairness notions.

## Limitations

This result assumes exactly two agents, precisely one positive good of each of two fixed values *every day*, equal additive preferences, complete allocation, and irrevocability. The exact approximation frontier is proved only for three days; for longer horizons the theorem settles only exact TEFX existence and does not claim the same approximation factor. The result supplies a deterministic structural classification, not a distributional or strategic guarantee. No claim of exhaustive novelty across unpublished, inaccessible, or unindexed manuscripts is made; particularly, further specialized calculations in the temporal-fair-division literature could overlap. Independent external verification has not been performed.

## References

1. Kui Wang Choi and Minming Li. *Temporal Fair Division of Indivisible Goods with Scheduling*. arXiv:2601.12835 (first public 2026-01-19). https://arxiv.org/abs/2601.12835
2. Kui-Wang Choi and Minming Li. *Temporal Fair Division of Indivisible Goods with Structured Constraints*. arXiv:2607.17224 (first public 2026-07-19). https://arxiv.org/abs/2607.17224
3. Edith Elkind, Ayumi Lam, Mahsa Latifian, T. Y. Neoh, and Nicholas Teh. *Temporal Fair Division of Indivisible Items*. arXiv:2410.14593 (first public 2024-10-18). https://arxiv.org/abs/2410.14593
4. Benjamin Cookson, Soroush Ebadian, and Nisarg Shah. *Temporal Fair Division*. arXiv:2410.23416 (first public 2024-10-30). https://arxiv.org/abs/2410.23416
5. Ayumi Igarashi and collaborators. *Repeated Fair Allocation of Indivisible Items*. arXiv:2304.01644 (first public 2023-04-04). https://arxiv.org/abs/2304.01644
