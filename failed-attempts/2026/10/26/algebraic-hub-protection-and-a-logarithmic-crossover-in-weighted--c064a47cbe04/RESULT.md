# Algebraic hub protection and a logarithmic crossover in weighted windmill dimer adsorption

## Finding
For integers \(r\ge2\), \(k\ge1\), let \(G_{r,k}\) consist of \(r\) disjoint cliques \(K_{2k}\) (the blades) and one extra vertex \(h\) adjacent to every blade vertex. Irreversible dimer adsorption attempts occur at rate \(\alpha>0\) independently on each internal clique edge and at rate \(\beta>0\) on each hub edge. A dimer is accepted only if both endpoints are currently vacant. Write \(b=\beta/\alpha\). The exact probability that the hub remains vacant in the jammed state is
\[
P_{r,k}(b)=\left(\prod_{j=1}^{k}\frac{2j-1}{2j-1+2b}\right)^r
=\left(\frac{\Gamma(k+1/2)\Gamma(1/2+b)}{\sqrt\pi\,\Gamma(k+1/2+b)}\right)^r.
\]
If any blade has odd order, that probability is zero (the other blades may have arbitrary positive sizes). For fixed integers \(r\ge2\) and real \(b>0\),
\[
P_{r,k}(b)=\left(\frac{\Gamma(1/2+b)}{\sqrt\pi}\right)^r k^{-rb}(1+O_{r,b}(k^{-1})).
\]
There is also a joint-size/rate crossover. For sequences of integers \(k\to\infty\), \(r_k\ge2\), and positive \(b_k\),
\[
r_kb_k\log k\longrightarrow c\in[0,\infty)\quad\Longrightarrow\quad
P_{r_k,k}(b_k)\longrightarrow e^{-c},
\]
while \(r_kb_k\log k\to\infty\) implies \(P_{r_k,k}(b_k)\to0\).

## Assumptions and scope
The graph is finite; attempts on distinct edges are independent homogeneous Poisson processes; edge-dependent rates take exactly the two indicated positive values; occupied vertices stay occupied permanently. The jammed state is the almost-sure state after every still-available edge has eventually attempted. There are no additional edges between distinct blades. The vertex \(h\) is initially vacant. The symbol \(P_{r,k}(b)\) is a probability, not a coverage density or an equilibrium Gibbs weight. The formulas concern all integer \(r\ge2\), \(k\ge1\), every \(\alpha,\beta>0\), and the stated limits only.

## Proof
**Blade-level first-step law.** Keep the hub available until either a spoke adsorption occurs or a blade becomes fully covered internally. When a particular blade has \(2j\) vacant vertices, all of these vertices form a clique. Exactly \(j(2j-1)\) internal edges can accept adsorption, each at rate \(\alpha\), and \(2j\) spokes to the hub could accept adsorption, each at rate \(\beta\). By exponential-race/memorylessness, the probability that the next successful event incident to this blade is an internal deposition is
\[
\frac{\alpha j(2j-1)}{\alpha j(2j-1)+2j\beta}=\frac{2j-1}{2j-1+2b}.
\]
An internal deposition leaves a smaller clique with exactly \(2j-2\) available vertices. Thus the probability that a single blade becomes perfectly covered internally before any valid spoke deposition equals the product \(q_k(b)=\prod_{j=1}^k (2j-1)/(2j-1+2b)\).

**Independence, including the shared hub.** Construct separate independent Poisson-clock families for the edges internal to each blade and its spokes. For every blade, run a virtual competition in which \(h\) is kept vacant, declaring failure at its first successful spoke or success at its complete internal coverage. These events use disjoint clock families and are independent. In the actual coupled adsorption, the hub is never occupied if and only if *every* virtual blade competition succeeds: if one virtual blade fails first, its valid spoke is the first hub deposition (unless another already deposited a spoke, in which case hub protection already failed); if all succeed, every blade becomes internally covered and no spoke can ever deposit. Therefore \(P_{r,k}(b)=q_k(b)^r\). If a blade has odd order, internal dimers cannot cover it, and a vacant hub together with a vacant blade vertex cannot form a jammed state, proving the zero-probability assertion.

**Gamma evaluation and fixed-rate law.** Rewriting the product as \(\prod_{j=1}^k(j-1/2)/(j-1/2+b)\), the gamma recurrence gives
\[
q_k(b)=\frac{\Gamma(k+1/2)\Gamma(1/2+b)}{\Gamma(1/2)\Gamma(k+1/2+b)}.
\]
The standard ratio asymptotic for gamma functions is \(\Gamma(k+1/2)/\Gamma(k+1/2+b)=k^{-b}(1+O_b(k^{-1}))\), which yields the fixed-parameter statement.

**Sharp joint crossover.** Write \(H_k^*=\sum_{j=1}^k (j-1/2)^{-1}=\log k+O(1)\). Taking logarithms gives \(-\log q_k(b)=\sum_{j=1}^k\log(1+b/(j-1/2))\). For \(0<b\le1/4\), Taylor expansion and \(\sum_{j\ge1}(j-1/2)^{-2}<\infty\) imply the uniform estimate \(-\log q_k(b)=bH_k^*+O(b^2)\). If \(r_kb_k\log k\to c<\infty\), then \(r_kb_k\to0\) and \(b_k\to0\), and hence \(-\log P_{r_k,k}(b_k)=r_kb_k(\log k+O(1))+O(r_kb_k^2)\to c\). For all \(b>0\), the inequality \(\log(1+x)\ge x/(1+x)\) yields
\[
-\log P_{r,k}(b)\ge\frac{rb}{1+2b}\,H_k^*.
\]
If \(rb\log k\to\infty\), the right-hand side diverges: for \(b\le1\) it is at least \(rbH_k^*/3\), and for \(b>1\) at least \(rH_k^*/3\). This completes all limiting cases.

## Verification
A standalone, standard-library-only Python program `verify_windmill.py` evaluates an independent full occupied-vertex state recursion using exact rational arithmetic. It passes 36 exact hub-vacancy comparisons to the product formula (including multiple rates and blade sizes), 15 single-pair checks, and 15 odd-blade exact checks. The largest explored independent occupied-mask recursion contains 3,072 states. Run `python verify_windmill.py`. The infinite-family formula and scaling limits are proved above, not inferred from finite tests.

## Relationship to prior work
Irreversible RSA and edge-dimer matching dynamics are established models, notably discussed by Evans, De Smedt–Godrèche–Luck, and Pippenger. Haji-Akbari and collaborators investigate dimer covering and related percolation questions on lattices. These background results do not by themselves provide the evaluated weighted clique-windmill hub survival product or its simultaneous blade-count/rate crossover. This comparison does not assert universal bibliographic priority. Published work could contain a more general unlocated equivalent, particularly in older graph-adsorption literature. The odd-blade obstruction and the elementary one-blade boundary are not separately claimed as novel.

## Limitations
The theorem does not give all adsorbed-dimer counts, their correlations, a dynamic hub-survival curve at finite time, or an arbitrary-graph result. Its algebraic exponent is for large *clique blade size*, not for a large geometric lattice; its joint scaling assumes the stated rate variation. Earlier general results might imply some cases; a specialist's independent novelty assessment has not been performed.

## References
1. J. W. Evans, *Random and cooperative sequential adsorption*, Reviews of Modern Physics **65** (1993), 1281–1329. DOI: 10.1103/RevModPhys.65.1281.
2. S. De Smedt, C. Godrèche, J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems*, arXiv:cond-mat/0202465 (first public version 2002-02-26).
3. A. Haji-Akbari, N. Haji-Akbari, R. M. Ziff, *Dimer Covering and Percolation Frustration*, arXiv:1507.04411 (2015).
4. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics **2** (1989), 393–398, DOI: 10.1137/0402034.
