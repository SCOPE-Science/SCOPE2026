# A mod-four reversal of minimum all-on Lights-Out presses under a Möbius ladder twist

## Finding
For each integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the ordinary two-rail cubic prism and let \(M_{2n}\) be the cubic Möbius ladder, with vertices \(\mathbb Z/(2n)\mathbb Z\) and edges between residues differing by \(1\) or \(n\). In the self-inclusive binary Lights-Out game, pressing a vertex flips that vertex and all its graph neighbors. Let \(L_G(z)\) count press subsets that extinguish the **all-on** initial position, by number of distinct pressed vertices; let \(Q_G(z)\) likewise count the *quiet* subsets whose net effect is zero. The complete polynomials are as follows:

| Circumference class | \(L_{P_n}(z)\) | \(L_{M_{2n}}(z)\) |
| --- | --- | --- |
| \(n\) odd | \(2z^n\) | \(2z^n\) |
| \(n\equiv0\pmod4\) | \(4z^{n/2}+8z^n+4z^{3n/2}\) | \(4z^n\) |
| \(n\equiv2\pmod4\) | \(4z^n\) | \(4z^{n/2}+4z^{3n/2}\) |

The companion quiet polynomials are
\[
(Q_{P_n},Q_{M_{2n}})=
\begin{cases}
(1+z^{2n},\,1+z^{2n}), & n\text{ odd},\\
(1+14z^n+z^{2n},\,1+2z^n+z^{2n}),&n\equiv0\pmod4,\\
(1+2z^n+z^{2n},\,1+6z^n+z^{2n}),&n\equiv2\pmod4.
\end{cases}
\]
All entries count **labelled press subsets**, not symmetry orbits. Consequently, the minimum numbers of presses needed to clear the all-on position are respectively
\[
\big(\ell(P_n),\ell(M_{2n})\big)=
\begin{cases}
(n,n),&n\text{ odd},\\
(n/2,n),&n\equiv0\pmod4,\\
(n,n/2),&n\equiv2\pmod4.
\end{cases}
\]
Thus a Möbius twist doubles the optimum when \(4\mid n\), but halves it when \(n\equiv2\pmod4\). In every even case the more efficient family has exactly four optimal press subsets. Both families admit solutions at every size stated, and no other all-on solutions exist.

## Assumptions and scope
The graphs are simple, undirected, labelled and cubic for \(n\ge3\). There is one binary light per vertex. Each vertex is pressed either once or not at all, because twice cancels. The closed-neighborhood matrix \(B_G=I+A(G)\) is interpreted over \(\mathbb F_2\). Thus an all-on solution is precisely a vector \(x\) satisfying \(B_Gx=\mathbf1\); a quiet press pattern satisfies \(B_Gx=0\). Cardinality means Hamming weight \(|x|\). A Möbius ladder is **not** the two-dimensional rectangular grid with Möbius boundary identification: it is the cubic graph explicitly specified above. The two families have the same number \(2n\) of vertices and degree three.

## Proof
**1. Prism reduction and completeness.** Label the two rails by bits \(a_i,b_i\) for \(i\in\mathbb Z/n\mathbb Z\), and let \(t\in\{0,1\}\) be the prescribed constant right-hand side. Put \((Ta)_i=a_{i-1}+a_i+a_{i+1}\). The complete closed-neighborhood equations are
\[
Ta+b=t\mathbf1,\qquad Tb+a=t\mathbf1.
\]
Because \(T\mathbf1=\mathbf1\) in characteristic two, the first equation determines \(b=t\mathbf1+Ta\); substitution in the second reduces the pair to \((T^2+I)a=0\). Directly expanding, \((T^2+I)a_i=a_{i-2}+a_{i+2}\), hence
\[
a_{i+4}=a_i\quad\text{for every }i\in\mathbb Z/n\mathbb Z.\tag{1}
\]
Conversely, every cyclic binary \(a\) obeying (1), together with \(b=t\mathbf1+Ta\), satisfies both original equations. Thus the complete solutions are obtained from an arbitrary \(\gcd(n,4)\)-periodic binary word \(a\), without missing other configurations.

If \(n\) is odd, \(a\) is constant and \(b=t+a\). The two choices have weights \(0,2n\) for \(t=0\) and both weight \(n\) for \(t=1\). If \(n\equiv2\pmod4\), \(a\) is an arbitrary alternating pair and \(Ta=a\). Therefore \(b=a\) for \(t=0\), giving weights \(0,n,n,2n\), while \(b=\mathbf1+a\) for \(t=1\), giving four solutions all of weight \(n\).

For \(4\mid n\), \(a\) consists of \(n/4\) repetitions of an arbitrary four-bit word \((a_0,a_1,a_2,a_3)\). Put \(s=a_0+a_1+a_2+a_3\pmod2\). For each index modulo four,
\[
b_i=t+s+a_{i+2}.
\]
If \(t=s\), the four-bit word \(b\) is just \(a\) rotated two positions and the eight-bit block has weight \(2\operatorname{wt}(a)\). Otherwise \(b\) is the complement of that rotation and the block has weight four. For \(t=0\), the sixteen possibilities have weights \(0,4,8\) with multiplicities \(1,14,1\). For \(t=1\), they have weights \(2,4,6\) with multiplicities \(4,8,4\). Repeating the block \(n/4\) times multiplies weights by \(n/4\), yielding the listed prism polynomials.

**2. Möbius recurrence and completeness.** Write \(x_i\in\mathbb F_2\) for the press at residue \(i\in\mathbb Z/(2n)\mathbb Z\). The equation at vertex \(i\) is
\[
x_{i-1}+x_i+x_{i+1}+x_{i+n}=t.\tag{2}
\]
Set \(u_i=x_i+x_{i+n}\). Adding (2) at \(i\) and \(i+n\) gives \(u_{i-1}+u_{i+1}=0\), so \(u_{i+2}=u_i\). Equation (2) also reads \(x_{i-1}+x_{i+1}=t+u_i\). Comparing its translates by two indices yields \(x_{i+3}=x_{i-1}\), so every solution is four-periodic:
\[
x_{i+4}=x_i\quad\text{for all }i.\tag{3}
\]
We now impose the original equations on **all** such words; the resulting conditions are sufficient as well as necessary.

If \(n\) is odd, the fact that \(2n\equiv2\pmod4\) forces the word to be two-periodic, \((a,b)\). The antipodal edge swaps the parity class and the other two neighbor terms cancel, so (2) becomes \(a+b=t\). There are two quiet patterns (empty and full) and two all-on strategies, both with \(n\) presses.

If \(4\mid n\), the antipodal shift preserves each position in the four-word \((a,b,c,d)\). The self and antipodal terms cancel, and (2) becomes the two independent conditions \(a+c=t\) and \(b+d=t\). For \(t=0\), there are four patterns with full-graph weights \(0,n,n,2n\); for \(t=1\), there are four patterns each of weight \(n\).

If \(n\equiv2\pmod4\), the antipodal shift advances by two within the four-word, and (2) is equivalent to the single parity condition \(a+b+c+d=t\). The eight even-parity four-words have weights \(0,2,2,2,2,2,2,4\), corresponding to graph weights \(0,n\) (six times), and \(2n\). The eight odd-parity words have weights one (four choices) or three (four choices), corresponding to graph weights \(n/2\) and \(3n/2\). This establishes every Möbius polynomial and excludes any extra solutions.

**3. Optimization.** The leading exponent of each all-on polynomial equals the minimum number of presses, and its coefficient counts minimizers. Reading the displayed polynomials proves the exact mod-four reversal and all multiplicities. No experimental extrapolation is used.

## Verification
The standalone `check_gauss.py` independently constructs the actual closed-neighborhood matrices for the two graph families, solves both target equations by full \(\mathbb F_2\) row reduction, and evaluates **every** affine solution for all \(3\le n\le80\) (312 target/graph/size cases). The standalone `check_exhaustive.cpp` independently builds the original graph-neighborhood masks and examines **all \(2^{2n}\) binary press subsets** for each \(3\le n\le11\), both graph types and both target states (36 complete censuses). The two checks use different algorithms and both passed. These finite tests corroborate the uniform algebraic proof rather than substitute for it.

For reproducibility, run `python3 check_gauss.py` and `g++ -std=c++17 -O2 check_exhaustive.cpp -o check_exhaustive && ./check_exhaustive`. Neither program requires third-party packages or datasets.

## Relationship to prior work
Minevich's 2012 theorem for symmetric binary matrices implies that the all-on Lights-Out state is reachable on **every** finite simple graph, but gives no minimum-weight or all-weight classification on either cubic ladder family [1]. Torrence and Torrence give general Lights-Out methods on generalized Petersen graphs and tabulate selected prism nullities, but do not state these mod-four affine enumerators or the Möbius twist comparison [2].

The published *Parity-kernel codes of cyclic prisms and their Reed–Muller support hierarchy* already determines the **entire prism quiet polynomial** \(Q_{P_n}\), the kernel dimensions and generalized support weights [3]. Those prism-quiet facts are **not new here**; they serve as an exact comparative baseline. The published *Möbius-ladder parity dynamics: exact transient shells and Jordan-chain fusion under a twist* studies **open-neighbor** synchronous XOR, and its fixed-point counts already imply the number of Möbius quiet patterns (two, four or eight, depending on the parity class) [4]. Those dimension/count facts are also **not new here**. The claimed contribution is the **complete affine all-on solution weight spectra for both graphs**, the Möbius quiet **weight refinement**, and the sharp, opposite minimum-press effect of twisting as \(n\) moves between the two even congruence classes. General Lights-Out solvability and complexity results do not supply this explicit all-family comparison [5].

## Limitations
Only simple cubic prisms and the specified cubic Möbius ladders, uniform binary self-inclusive switching, and initially all-on or all-off states are classified. The theorem does not determine shortest presses for arbitrary targets, other ladder widths, nonlinear update rules, or graphs outside these two families. The structural recurrence is elementary; the historical novelty assessment concerns the new *joint weight classification and twist-sensitive optimization*, not the existing nullity counts. Unindexed older recreational-mathematics, combinatorics and coding-theory sources may contain equivalent enumerations. Independent validation has not been performed.

## References
1. I. Minevich, *Symmetric Matrices over F_2 and the Lights Out Problem*, arXiv:1206.2973v1 (first public 14 June 2012), https://arxiv.org/abs/1206.2973.
2. B. Torrence and R. Torrence, *An iterative strategy for Lights Out on Petersen graphs*, Involve **9** (2016), 721–739, https://doi.org/10.2140/involve.2016.9.721.
3. *Parity-kernel codes of cyclic prisms and their Reed–Muller support hierarchy*, publicly available mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-parity-kernel-codes-of-cyclic-prisms-and-their-reed-muller-suppo--6f178222ad14/RESULT.md.
4. *Möbius-ladder parity dynamics: exact transient shells and Jordan-chain fusion under a twist*, publicly available mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-m-bius-ladder-parity-dynamics-exact-transient-shells-and-jordan--812449181a9b/RESULT.md.
5. J. Berman, C. Borer and N. Hungerbühler, *Lights Out on graphs*, Beiträge zur Algebra und Geometrie **62** (2021), https://doi.org/10.1007/s00591-021-00297-5.
