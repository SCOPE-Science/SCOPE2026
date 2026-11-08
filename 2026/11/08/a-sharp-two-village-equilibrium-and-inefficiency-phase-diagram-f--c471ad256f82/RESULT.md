# A sharp two-village equilibrium and inefficiency phase diagram for fair-cost-sharing facilities

## Finding

Consider a symmetric two-facility assignment game with \(m\ge1\) labeled clients at each of two locations separated by \(d>0\), and a facility at each location with equal building cost \(C>0\). Every client chooses one facility and pays travel distance plus an equal share of that facility's building cost among its users. A pure Nash equilibrium (PNE) is an assignment admitting no *strictly* cost-reducing unilateral switch.

Write \(r=d/C\), \(L_m=1/[m(m+1)]\), and \(U_m=1-1/(2m)\). **Every PNE is exactly one of** the two complete poolings (all \(2m\) clients choose one facility) or the home-segregated assignment (each group chooses its own facility). Each pooling is a PNE exactly when \(r\le U_m\); segregation is a PNE exactly when \(r\ge L_m\). Consequently the numbers of labeled PNEs are exactly \(2\) for \(0<r<L_m\), exactly \(3\) for \(L_m\le r\le U_m\), and exactly \(1\) for \(r>U_m\), including the simultaneous-threshold case \(m=1\).

The social optimum is \(\operatorname{OPT}=\min\{C+md,2C\}\). The sharp worst-PNE price of anarchy, maximized over all positive \(d,C\) for fixed \(m\), is
\[
\sup_{d,C>0}\operatorname{PoA}_m(d,C)=
\begin{cases}
4/3,&m=1,\\
3/2,&m=2,\\
(2m+1)/4,&m\ge3.
\end{cases}
\]
Each supremum is attained: at \(r=L_m\) for \(m=1,2\), and at \(r=U_m\) for \(m\ge3\). In particular, even equal-cost facilities and equally sized, separated populations allow worst-equilibrium inefficiency growing linearly with population size.

## Assumptions and scope

The positions are \(0,d\) with exactly \(m\) distinguishable clients at each point and fixed candidate facilities at the same two points. Both facilities have identical positive fixed opening cost \(C\); an unused facility costs nothing. A facility with \(k\ge1\) users charges each \(C/k\). Travel is unweighted absolute distance. Each client selects exactly one facility, can switch to either available site, and minimizes individual cost, including the post-deviation share. Ties count as stable. Social cost sums all private payments, so opening costs are paid once per used facility. There are no capacities or other strategic location choices.

## Proof

**1. No village can split at equilibrium.** Suppose two clients at the same home location \(x\in\{0,d\}\) use different facilities of loads \(k,l\ge1\). Nash stability of both clients implies
\[
|x-0|+C/k\le|x-d|+C/(l+1),\qquad
|x-d|+C/l\le|x-0|+C/(k+1).
\]
Adding eliminates the distance terms and forces \(C/k+C/l\le C/(k+1)+C/(l+1)\), impossible since \(C>0\). Hence each village has one common choice. This proves a structural statement about *all* labeled PNEs, including equality cases.

**2. Eliminate the crossed choice.** Village-homogeneity leaves four assignments: both pooled at facility \(0\), both pooled at facility \(d\), each village at its own facility, or each village at the opposite facility. In the crossed case, a client can switch home and pay \(C/(m+1)\), strictly below its current \(d+C/m\), so crossing is never stable.

**3. Exact stability boundaries.** Under pooling at facility \(0\), the home-side clients never profit by switching to the remote unused facility: their current cost is \(C/(2m)<d+C\). Each of the \(m\) remote clients has current cost \(d+C/(2m)\) and would pay \(C\) on opening the empty home facility. Therefore pooling is stable iff \(d+C/(2m)\le C\), or \(r\le U_m\). The same condition holds for pooling at \(d\) by symmetry. Under home segregation, every agent has cost \(C/m\) and would pay \(d+C/(m+1)\) after switching; thus the condition is \(r\ge L_m\). Direct calculation gives \(L_m\le U_m\) for every \(m\ge1\), equality only at \(m=1\). The exact three-regime enumeration follows.

**4. Welfare benchmark.** If a single facility is used, exactly \(m\) agents must travel distance \(d\), for total \(C+md\). If both are used, opening alone costs \(2C\) and all travel costs are nonnegative; home segregation attains \(2C\). Hence \(\operatorname{OPT}=\min(C+md,2C)\).

**5. Sharp price of anarchy.** Put \(r=d/C\). For any admissible pooling PNE its welfare ratio is \((1+mr)/\min(1+mr,2)\). For an admissible segregated PNE its ratio is \(2/\min(1+mr,2)\). In the interval \(L_m\le r<1/m\) the inefficient candidate is segregation and its ratio \(2/(1+mr)\) decreases in \(r\); the maximum at \(r=L_m\) is \(2(m+1)/(m+2)\). For \(1/m<r\le U_m\), if this interval is nonempty, the inefficient candidate is pooling and its ratio \((1+mr)/2\) increases in \(r\); its maximum at \(r=U_m\) is \((2m+1)/4\). Outside these overlap intervals every available equilibrium is socially optimal or has a smaller ratio. If \(m=1\), \(U_m=L_m=1/2<1/m\) and the first maximum is \(4/3\). If \(m=2\), the first maximum \(3/2\) exceeds the second \(5/4\). If \(m\ge3\), the second maximum is at least the first, as \((2m+1)(m+2)-8(m+1)=2m^2-3m-6>0\) for all integer \(m\ge3\). The stated sharp, attained constants follow. \(\square\)

## Verification

The standalone, standard-library-only `verify.py` uses exact rational arithmetic to enumerate all binary assignments for each \(m\in\{1,2,3,4,5\}\) at two opening costs and nine boundary-sensitive distance values. It tests the Nash condition using actual post-deviation loads, compares the full set of equilibria with the structural classification, independently minimizes social cost over every assignment, and checks the price-of-anarchy formula. It evaluated \(24{,}536\) labeled assignments without a discrepancy. Separate exact calculations confirm the sharp constants for \(1\le m\le7\). The proof, rather than this finite enumeration, establishes the claims for unbounded \(m\) and all real \(C,d>0\).

Reproduce using `python3 verify.py` from a directory containing this result and its companion script; no external dependencies are required.

## Relationship to prior work

Ma, Xiao, Bai, and Cheng [1] define this fixed-facility equal-share assignment model. Their Theorem 3.1 computes a PNE by potential minimization and their Lemma 1 establishes a noncrossing property for agents at distinct positions. Proposition 1 bounds the social cost of the *computed* PNE relative to an optimum, not that of every PNE. Their inspected text, including the proofs and appendices, does not give the exact two-village three-profile classification, the two rational coexistence boundaries, or the sharp worst-PNE constant for the symmetric fixed-cost restriction. This result proves an additional same-location no-splitting property not supplied by the distinct-location noncrossing lemma, then closes the special-case classification. The general existence theorem does not imply the worst-equilibrium bound.

Hansen and Telelis [2] address different installation-choice facility-location games, discussing price of stability and strong-equilibrium inefficiency. Their accessible abstract does not cover this exact fixed-site two-village PNE census. General facility cost-sharing games can exhibit poor weak equilibria; the qualitative possibility of inefficient outcomes is not asserted to be new. The contribution is the *sharp subclass-specific thresholds and price-of-anarchy envelope*.

## Limitations

The result concerns pure unilateral Nash equilibrium under equal opening charges and exactly two fixed facilities with two equally sized colocated groups. It does not describe heterogeneous, capacitated, continuously selectable, strategic-opening, strong-equilibrium, or many-facility instances. Price of anarchy is a worst-PNE concept and differs from the cost guarantee of potential-minimizing algorithms. While searches and the accessible primary literature did not identify an equivalent complete result, unindexed results or inaccessible details of earlier broader facility-location work could affect publication priority. No independent external audit has been performed.

## References

[1] Mengfan Ma, Mingyu Xiao, Tian Bai, and Xin Cheng, *Facility Assignment with Fair Cost Sharing: Equilibrium and Mechanism Design*, arXiv:2404.08963 (first public version 13 April 2024), https://arxiv.org/abs/2404.08963; open full text https://arxiv.org/html/2404.08963v1.

[2] Thomas Dueholm Hansen and Orestis A. Telelis, *On Pure and (approximate) Strong Equilibria of Facility Location Games*, arXiv:0809.4792 (first public version 28 September 2008), https://arxiv.org/abs/0809.4792.
