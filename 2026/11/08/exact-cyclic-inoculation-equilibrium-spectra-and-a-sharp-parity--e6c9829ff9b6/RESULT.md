# Exact cyclic inoculation equilibrium spectra and a sharp parity gap in the price of stability

## Finding

For every labelled cycle of length \(n\ge3\) and every positive cost ratio \(t=nC/L\), the finite generating function below counts **all pure Nash equilibria** by their number of inoculated vertices, including the equality boundaries in \(t\). In the open cost cell \(2<t<3\), the minimum equilibrium cost differs sharply with the parity of \(n\): the socially optimal configuration is a Nash equilibrium exactly for even \(n\), while an odd cycle has a strictly larger best-equilibrium cost by precisely \((L/n)(3-t)\). These are exact finite-population results, not mean-field approximations.

Let \(\mathrm{Opt}_n\) be the minimum social cost and \(\mathrm{BestNE}_n\) the smallest social cost among pure equilibria. For \(2<t<3\),
\[
\mathrm{Opt}_n=\frac Ln\left[n+(t-1)\left\lceil\frac n2\right\rceil\right],\qquad
\mathrm{BestNE}_n=\frac Ln\begin{cases}
n+(t-1)n/2,&n\text{ even},\\
n+(t-1)(n-1)/2+2,&n\text{ odd}.
\end{cases}
\]
Consequently
\[
\mathrm{PoS}(C_n)=\begin{cases}
1,&n\text{ even},\\
1+\dfrac{3-t}{n+(t-1)(n+1)/2},&n\text{ odd}.
\end{cases}
\]
The strict parity effect starts immediately above \(t=2\), disappears in the limit \(t\uparrow3\), and is witnessed by an explicit equilibrium for each odd \(n\).

The all-cost equilibrium spectrum is the following. For a strategy with \(k\ge2\) inoculated vertices, list, in cyclic order, the counts \(g_1,\ldots,g_k\ge0\) of consecutive uninoculated vertices separating them. Define
\[
 h=\min\{\lfloor t\rfloor,n-k\},\qquad
 T_{uv}(x)=x^v\mathbf1\{u+v+1\ge t\}\quad(0\le u,v\le h).
\]
Then the exact number with \(k\) inoculated vertices is
\[
 E_{n,k}(t)=\frac nk[x^{n-k}]\operatorname{tr}(T(x)^k)\qquad(2\le k\le n).
\]
The exceptional counts are \(E_{n,0}(t)=\mathbf1\{t\ge n\}\) and \(E_{n,1}(t)=n\mathbf1\{n-1\le t\le n\}\). Thus \(\sum_{k=0}^n E_{n,k}(t)z^k\) is an exact, constructive equilibrium enumerator for arbitrary \(t>0\).

In the natural first open cost cell \(1<t<2\), this specializes to
\[
 E_{n,k}(t)=\frac{n}{n-k}\binom{n-k}{2k-n}
\quad\left(\left\lceil n/2\right\rceil\le k\le\left\lfloor2n/3\right\rfloor\right),
\]
with zero elsewhere. Its total is the Perrin number \(P_n\), where \(P_0=3\), \(P_1=0\), \(P_2=2\) and \(P_n=P_{n-2}+P_{n-3}\); the associated welfare ratios are
\[
 \mathrm{PoS}(C_n)=1,\qquad
 \mathrm{PoA}(C_n)=\frac{n+(t-1)\lfloor2n/3\rfloor}{n+(t-1)\lceil n/2\rceil}.
\]

## Assumptions and scope

The graph is the undirected simple labelled cycle \(C_n\), \(n\ge3\). Every player selects either inoculation (cost \(C>0\)) or remaining susceptible. Following decisions, an infection starts at a uniformly selected vertex among **all \(n\) vertices**, and infects every susceptible vertex in the susceptible connected component of the seed; inoculated vertices cannot be infected or transmit infection. An infected player incurs loss \(L>0\). Each player minimizes their own expected loss plus inoculation cost; ties count as Nash-equilibrium best responses. Only pure strategies and total expected social cost are considered. The initial infection rule, homogeneous costs, and perfect inoculation are essential. We write \(t=nC/L\). A susceptible connected component of length \(\ell\) has individual infection probability \(\ell/n\), and contributes \((L/n)\ell^2\) to total social cost.

## Proof

**1. Exact local equilibrium conditions.** A susceptible vertex in a component of size \(g\) prefers remaining susceptible precisely when \(Lg/n\le C\), or \(g\le t\). If an inoculated vertex changes action, its newly exposed component has size \(r\); staying inoculated is a best response precisely when \(C\le Lr/n\), or \(r\ge t\). On a cycle with \(k\ge2\) inoculated vertices the susceptible components are the nonzero gaps \(g_i\), and removing the \(i\)-th inoculation creates a component of length \(g_{i-1}+g_i+1\), even when one of the gaps is zero. Therefore the complete necessary and sufficient conditions are
\[
 0\le g_i\le t,\qquad g_{i-1}+g_i+1\ge t
 \quad\text{for all cyclic indices }i,
 \qquad\sum_i g_i=n-k.
\]
With no inoculation, an individual faces component size \(n\), so the all-susceptible configuration is equilibrium iff \(t\ge n\). With one inoculation, susceptible vertices see size \(n-1\), and its removal exposes all \(n\), so equilibrium holds iff \(n-1\le t\le n\). This proves all boundary cases.

**2. Counting every labelled equilibrium.** Nonnegative integer gaps are bounded above by \(h\). The transfer entry \(T_{uv}(x)\) records a permissible adjacent pair of gap sizes and weights the new gap by \(x^v\). Consequently \([x^{n-k}]\operatorname{tr}(T(x)^k)\) is precisely the number of ordered cyclic gap lists with a distinguished origin that sum to \(n-k\). Marking an inoculated vertex in a labelled configuration creates \(k\) possible such lists after fixing a vertex label as distinguished, while the distinguished label can be placed at any of the \(n\) cycle positions; double counting yields the factor \(n/k\). This is a finite polynomial identity for every positive real \(t\), including integer \(t\).

**3. Social optimum when \(1<t<3\).** If a susceptible component has \(\ell\ge2\) members, inoculating an end member replaces its square cost \(\ell^2\) by \((\ell-1)^2\) and costs an extra \(t\) in units of \(L/n\). The change is \(t-(2\ell-1)<0\) since \(t<3\). In the all-susceptible state, inoculating one member changes the squared loss from \(n^2\) to \((n-1)^2\), again improving the cost. Iterating yields only isolated susceptible vertices. Such configurations inoculate a vertex cover of \(C_n\); their cost in units \(L/n\) is \(n+(t-1)k\). Since \(t>1\), minimize \(k\) to get \(k=\lceil n/2\rceil\). This proves the exact social optimum above for the entire interval \(1<t<3\).

**4. The parity gap when \(2<t<3\).** Here the only allowed gaps are \(0,1,2\), and adjacent gaps must sum to at least \(2\). Let \(a,b,c\) be the numbers of gaps of sizes \(1,2,0\), respectively. Every zero gap has both adjacent gaps equal to two, so cyclic incidence counting gives \(b\ge c\). Since \(k=a+b+c\) and \(n=k+a+2b\),
\[
 n-2k=b-c\ge0,\qquad
 \frac nL\mathrm{Cost}=kt+a+4b=n+(t-1)k+2b.
\]
For even \(n=2m\), write \(k=m-d\) with \(d\ge0\). Then \(b-c=2d\) and \(b\ge2d\), giving
\[
 \frac nL\mathrm{Cost}\ge n+(t-1)m+(5-t)d.
\]
The alternating configuration with \(k=m\), all gaps one, attains equality. For odd \(n=2m+1\), write \(k=m-d\). Then \(b-c=1+2d\), so \(b\ge1+2d\) and
\[
 \frac nL\mathrm{Cost}\ge n+(t-1)m+2+(5-t)d.
\]
Equality occurs with \(k=m\), one gap of two and all other gaps one. The exceptional one-inoculation state for \(n=3\) satisfies the same bound and attains equality; for odd \(n\ge5\) a one-inoculation state cannot be equilibrium in this cost cell because its exposed component would have size \(n-1>t\). For even \(n\ge4\), a one-inoculation state likewise fails. As \(5-t>0\), these equality constructions minimize equilibrium cost. Subtracting the social optimum in Step 3 gives a gap of exactly \((L/n)(3-t)\) for odd \(n\) and zero for even \(n\). Division by the positive optimum proves the price-of-stability formulas.

**5. The first open cost cell.** If \(1<t<2\), all susceptible gaps are at most one, and the second equilibrium inequality excludes three consecutive inoculated vertices. Equivalently, the cyclic binary word has no consecutive susceptible pair and no triple of consecutive inoculated vertices. The \(u=n-k\) susceptible vertices are separated by runs of one or two inoculated vertices, with exactly \(2k-n\) two-vertex runs. Choose those runs and mark an origin to obtain \(n/u\binom{u}{2k-n}\) profiles, with the stated support. The total is the classical Perrin number (cyclic words avoiding \(00\) and \(111\)), also verified by a three-state transfer recurrence. Every equilibrium has only singleton susceptible components, hence cost \((L/n)[n+(t-1)k]\). The smallest allowed count \(\lceil n/2\rceil\) equals the optimum; the largest is \(\lfloor2n/3\rfloor\). Both endpoints are attainable. The stated prices of stability and anarchy follow.

## Verification

The accompanying standard-library-only `verify.py` computes the equilibrium spectrum using the transfer formula and, separately, enumerates all labelled binary decisions and directly recomputes each player's component size after unilateral deviation. It checks 86 cycle/parameter pairs for \(3\le n\le11\), including integer equality boundaries, and verifies the Perrin enumerator in the open \(1<t<2\) cell. It additionally checks the exact social optimum, extremal equilibrium costs and \(\mathrm{PoA}\) for 27 cases in that cell and the odd/even \(\mathrm{PoS}\) formula for 27 cases with \(2<t<3\). Verification is finite and supplements—not replaces—the general proofs above. Run `python verify.py` (Python 3, no additional dependencies).

## Relationship to prior work

Aspnes, Chang, and Yampolskiy established the inoculation model and the general component-threshold characterization of pure Nash equilibria in 2006; that characterization is **prior work**, not claimed as new. DiCicco, Poskanzer, and Reichman (arXiv:2304.12303, publicly posted April 24, 2023) studied bounded-degree and cost-sensitive inefficiency, including cyclic graphs as an example in their bound construction. Chen, David, and Kempe (2010) studied different social-optimum/voluntary-inoculation trade-offs. The present claim is restricted to the exact labelled-cycle equilibrium enumerator across all cost ratios and its explicit sharp parity-sensitive price-of-stability and first-cell price-of-anarchy consequences. Perrin numbers and maximal independent-set counting are classical; the specialization in the first open cost cell is not claimed to discover Perrin numbers.

## Limitations

Only pure equilibria, perfect inoculation, uniform attack seed selection, symmetric homogeneous costs, and simple cycles are addressed. Price-of-stability formulas are asserted only for the specified open cost cells; the all-cost transfer formula separately covers exact integer boundaries but does not by itself supply a closed welfare formula for every cost cell. Large-scale empirical epidemiological predictions, mixed-strategy equilibria, dynamics of equilibrium selection, and non-cycle graphs are not established. The original general Nash-characterization makes the cycle-gap inequalities a direct specialization; the distinct contribution is an exact parameterized enumeration and parity-sensitive welfare evaluation. A differently indexed equivalent cycle enumeration or parity result remains a publication-priority risk.

## References

1. M. DiCicco, H. Poskanzer, D. Reichman, *Inoculation Strategies for Bounded Degree Graphs*, arXiv:2304.12303, first version April 24, 2023. https://arxiv.org/abs/2304.12303
2. J. Aspnes, K. Chang, A. Yampolskiy, *Inoculation Strategies for Victims of Viruses and the Sum-of-Squares Partition Problem*, Journal of Computer and System Sciences 72 (2006), 1077–1093. https://www.cs.yale.edu/homes/aspnes/papers/jcss-inoculation-final.pdf
3. P.-A. Chen, M. David, D. Kempe, *Better Vaccination Strategies for Better People*, ACM EC 2010. https://david-kempe.com/publications/vaccinations.pdf
