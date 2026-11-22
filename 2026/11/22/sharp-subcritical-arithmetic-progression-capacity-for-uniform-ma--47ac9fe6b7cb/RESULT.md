# Sharp subcritical arithmetic-progression capacity for uniform marginal couplings

## Finding
Fix an integer \(k\ge3\). Let \(U_1,\ldots,U_k\) each have the uniform distribution on \([0,1]\), with arbitrary joint dependence, and let \(E_{k,r}\) be the event that the increasing order statistics of these values have all \(k-1\) adjacent differences exactly \(r>0\). For every \(0<r<1/k\), write
\[
m=\lfloor1/r\rfloor,\qquad s=1-mr\in[0,r).
\]
Then the exact, attained extremal probability is
\[
\boxed{\sup_{\text{uniform marginals}}\Pr(E_{k,r})=
kr\lfloor m/k\rfloor+ks\,\mathbf1_{\{m\equiv k-1\pmod{k}\}}.}
\]
The value is one in the stated range exactly at gaps \(r=1/(k\ell)\) with integers \(\ell\ge2\). For \(k=3\), the values at gaps \(1/6,1/5,1/4\) are respectively \(1,3/5,3/4\), so the sharp capacity is not monotone in the prescribed gap.

## Assumptions and scope
The integer \(k\) is fixed but arbitrary, at least three, and the gap obeys \(0<r<1/k\). No exchangeability, absolute continuity, independence, or moment assumptions on the joint distribution are imposed. Each of the \(k\) single-coordinate marginals is exactly Lebesgue-uniform on the unit interval. Equality of all adjacent gaps is literal, not an approximation or an inequality. Under independent continuous coordinates the event has probability zero, whereas singular copulas can attain the displayed positive capacity.

## Proof
**Step 1 (residue-fiber geometry).** Discard the null set of multiples of \(r\). Every \(x\in[0,1]\) has a unique representation \(x=t+jr\), where \(0<t<r\) and \(j\in\{0,\ldots,N(t)-1\}\), with \(N(t)=\lfloor(1-t)/r\rfloor+1\). For almost every \(t\), the chain has \(m+1\) vertices for \(0<t<s\) and \(m\) vertices for \(s<t<r\). A successful unordered \(k\)-tuple corresponds to one of the consecutive length-\(k\) blocks \(\{j,j+1,\ldots,j+k-1\}\) of this chain.

**Step 2 (sharp fiber bound).** Symmetrize the coupling by an independent uniform permutation of its coordinate labels. This preserves all marginals and \(\Pr(E_{k,r})\). For every successful block \(j\), let \(w_j(t)\,dt\) denote its probability measure over residues \(t\). This measure is absolutely continuous: one of the coordinates lies at a vertex \(t+hr\), and its uniform marginal dominates the contribution of the event. Every coordinate, after symmetrization, occupies each vertex in that successful block with conditional weight \(w_j(t)/k\). Since each coordinate's full marginal has density one along every vertex strip, for almost every residue \(t\) and each vertex \(h\),
\[
\sum_{j:h\in\{j,\ldots,j+k-1\}}w_j(t)\le k.
\]
Choose the sentinel vertices \(h=k-1,2k-1,\ldots,k\lfloor N(t)/k\rfloor-1\). Every possible consecutive length-\(k\) block contains **exactly one** sentinel. Summing the preceding marginal bound over the sentinels therefore gives
\[
\sum_j w_j(t)\le k\lfloor N(t)/k\rfloor.
\]
Integrating and using the two possible chain sizes yields
\[
\Pr(E_{k,r})\le k\bigl[s\lfloor(m+1)/k\rfloor+(r-s)\lfloor m/k\rfloor\bigr]
=kr\lfloor m/k\rfloor+ks\mathbf1_{\{m\equiv k-1\pmod{k}\}}.
\]
The argument uses marginal capacities, not any unsupported assumption that successful blocks are independent.

**Step 3 (attainment).** Within each residue chain, partition consecutive vertices starting at index zero into full disjoint blocks of \(k\), leaving at most \(k-1\) terminal vertices. Sample \(X\) uniformly from \([0,1]\). If \(X=t+(jk+h)r\) belongs to a full block indexed by \(j\), set coordinate \(U_a=t+[jk+(h+a-1\bmod k)]r\), for \(a=1,\ldots,k\). If \(X\) is among the leftover terminal vertices, set \(U_a=X\) for every \(a\). For each fixed \(a\), this rule is a measurable, length-preserving permutation of the finite residue chain and hence preserves Lebesgue measure by integration in \(t\). Thus every \(U_a\) is uniform. Exactly the full-block portion succeeds, of Lebesgue measure \(k[s\lfloor(m+1)/k\rfloor+(r-s)\lfloor m/k\rfloor]\). It attains the upper bound.

**Step 4 (full-capacity resonance).** By the same formula, the deficiency from one is the integral \(\int_0^r(N(t)\bmod k)\,dt\). This vanishes precisely when the chain length is a multiple of \(k\) for almost every residue. If \(s>0\), both consecutive chain lengths \(m,m+1\) occur on sets of positive length and cannot both be multiples of \(k\). Hence \(s=0\) and \(m\equiv0\pmod{k}\), or equivalently \(r=1/(k\ell)\), with \(\ell\ge2\) in the stated domain.

## Verification
The standalone `checker_progressions.py` evaluates the exact formula and constructs coordinate permutations for every integer grid denominator \(4\le q\le42\), every step numerator \(1\le p<q\), and every \(3\le k<\min(q,7)\). It also independently solves symmetric finite marginal-capacity linear programs for denominators at most \(20\) using SciPy HiGHS. All 4,136 assertions passed. These finite tests are supporting consistency checks; the proof above establishes all real gaps in the stated range and all integers \(k\ge3\).

## Relationship to prior work
Chaudhary and Khandelwal (2026) characterize attainable *sums of two* dependent uniform variables, including symmetric two- and three-atom sum laws; those results settle a bivariate exact-displacement analogue, not the stated \(k\ge3\) joint arithmetic-progression event. Omladič, Vuk and Zalar (2026) give general finite copula interpolation feasibility criteria, not the capacity of this singular multi-coordinate event. General multi-marginal transport and matching principles explain the type of optimization but do not by themselves supply the explicit all-\(k\) residue resonance law. A known sharp hard-core separation capacity for uniform marginal couplings equals one throughout \(r\le1/k\), so it does not imply the strictly subunit equal-spacing probabilities proved here. This claim is restricted to the subcritical range to avoid the previously covered high-gap extremal regime.

## Limitations
The event requires exact, zero-tolerance gaps and therefore concerns singular copula optimization rather than independent sampling. This result does not characterize all optimizing copulas or give sharp toleranced near-progression probabilities. General multi-marginal transportation literature may contain equivalent formulations; independent assessment of priority is still warranted.

## References
1. P. Chaudhary and K. Khandelwal, *Sums of two dependent uniform random variables: a characterization by joint tail bounds*, arXiv:2610.24197, first public 16 October 2026. https://arxiv.org/abs/2610.24197
2. M. Omladič, M. Vuk and A. Zalar, *A linear programming approach to finite copula interpolation*, arXiv:2611.14008, first public 10 November 2026. https://arxiv.org/abs/2611.14008
3. D. Vögler, *Geometry of Kantorovich polytopes and support of optimizers for repulsive multi-marginal optimal transport on finite state spaces*, arXiv:1901.04568, 2019. https://arxiv.org/abs/1901.04568
