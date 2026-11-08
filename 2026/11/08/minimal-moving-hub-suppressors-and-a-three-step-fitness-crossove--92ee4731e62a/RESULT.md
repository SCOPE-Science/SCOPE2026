# Minimal moving-hub suppressors and a three-step fitness crossover

## Finding

In the birth–death evolutionary graph process, consider three labeled sites \(\{0,1,2\}\). The network alternates between two unweighted paths, \(G_0\) having edges \(\{01,02\}\) and \(G_1\) having edges \(\{01,12\}\). Thus the center of the path moves from site \(0\) to site \(1\). Starting at the beginning of a \(G_0\) block, use \(G_0\) for \(\tau\) birth–death updates, then \(G_1\) for \(\tau\) updates, and repeat. A single mutant is initialized uniformly among the three vertices. Its relative reproductive fitness is \(r>0\), while residents have fitness one. Write \(\rho_\tau(r)\) for its probability of eventual fixation, and let

\[
\rho_{\mathrm M}(r)=\frac{r^2}{r^2+r+1}
\]

be the ordinary three-individual Moran probability.

**Theorem.** The following classification holds for every real \(r>0\), with strict inequalities whenever stated:

1. Each static constituent path is an amplifier: its fixation probability exceeds \(\rho_{\mathrm M}\) when \(r>1\), and is below it when \(0<r<1\).
2. For \(\tau=1\) and \(\tau=2\), the periodic network is a **strict suppressor**: \(\rho_\tau(r)<\rho_{\mathrm M}(r)\) for every \(r>1\), and the reverse inequality holds for \(0<r<1\).
3. For \(\tau=4\), the periodic network is a **strict amplifier**: \(\rho_4(r)>\rho_{\mathrm M}(r)\) for every \(r>1\), and the reverse inequality holds for \(0<r<1\).
4. For \(\tau=3\), there is precisely one threshold \(r_*>1\), approximately \(1.26531751981086\), with reciprocal threshold \(r_*^{-1}\approx0.790315461806\). The periodic network is suppressing for \(r_*^{-1}<r<1\) and \(1<r<r_*\), amplifying for \(0<r<r_*^{-1}\) and \(r>r_*\), and exactly Moran-equivalent at \(r=r_*^{-1},1,r_*\).

The threshold is the unique solution \(r>1\) of

\[
H(r+r^{-1}-2)=0,\quad
H(z)=34016z^5+686992z^4+5185052z^3+17279678z^2+21114193z-1229026.
\]

The three-site network is minimal among connected, simple, unweighted graph pairs with distinct graphs: with only two sites, the only connected graph is the single edge. Exchanging the order of the two phases at a block boundary leaves the uniform-initialization probability unchanged by relabeling vertices \(0\) and \(1\). No statement is made about initiation at arbitrary *within-block* times, or about block lengths above four.

## Assumptions and scope

At each discrete update, choose a parent with probability proportional to fitness (\(r\) for mutant, one for resident), then choose one of the parent's current neighbors uniformly. Replace that neighbor's type by the parent's type. Updates that do not change the configuration are retained as Markov self-loops. There is no mutation, all edges are undirected and unweighted within a phase, and the initial phase and starting time are fixed as described above. Both homogeneous states are absorbing. All parameters and inequalities refer to real \(r>0\), not merely the finite rational fitness values used in the coefficient certificate.

The phrase amplifier (respectively, suppressor) follows the standard full-fitness convention: higher (respectively, lower) fixation probability than Moran for all \(r>1\), and lower (respectively, higher) for all \(0<r<1\).

## Proof

**Step 1: Exact Markov reduction.** Encode a configuration by its three-bit mutant mask \(s\in\{0,\ldots,7\}\). For a graph \(G\), let \(T_G(r)\) be the stochastic matrix defined by summing, over each parent \(u\) and neighbor \(v\),

\[
\bigl(T_G(r)\bigr)_{s,s^{v\leftarrow u}}
\mathrel{+}=\frac{r^{\mathbf 1_{\{u\in s\}}}}{r|s|+3-|s|}\frac1{\deg_G(u)}.
\]

Here \(s^{v\leftarrow u}\) means that site \(v\) receives site \(u\)'s type. Let \(U=\{1,2,3,4,5,6\}\) be the six transient states and let

\[
Q_\tau(r)=T_{G_0}(r)^\tau T_{G_1}(r)^\tau,\qquad
x_\tau=(I-(Q_\tau)_{U,U})^{-1}(Q_\tau)_{U,7}.
\]

Both graphs are connected, so from every transient state there is positive probability of eventual absorption in boundedly many full blocks. Consequently the transient matrix has spectral radius below one and the inverse exists. The desired answer is exactly \(\rho_\tau=(x_{\tau,1}+x_{\tau,2}+x_{\tau,4})/3\). This is the backward equation at the start of a full period, not a stationary-phase approximation.

**Step 2: Rational-function certificates.** Exact elimination gives positive-coefficient polynomials \(A_\tau,B_\tau\) with

\[
\rho_\tau(r)=\frac{r^2 A_\tau(r)}{(r+2)B_\tau(r)},
\qquad \deg A_\tau=4\tau-1,\quad \deg B_\tau=4\tau,
\]

for each \(\tau=1,2,3,4\). Complete ascending coefficient arrays for all eight polynomials are recorded in `COEFFICIENTS.txt` and embedded in `verify.py`. Define \(S_\tau\) by the exact polynomial identity

\[
(r^2+r+1)A_\tau(r)-(r+2)B_\tau(r)=(r-1)S_\tau(r).
\]

It follows that

\[
\rho_\tau(r)-\rho_{\mathrm M}(r)=
\frac{r^2(r-1)S_\tau(r)}{(r+2)(r^2+r+1)B_\tau(r)}.
\]

Every denominator displayed here is positive for \(r>0\). The explicit coefficients show \(S_1(r)=-25(r+1)^2\); \(S_2\) has strictly negative coefficients; and \(S_4\) has strictly positive coefficients. This proves the universal signs for blocks one, two, and four. For three-step blocks, the palindromic polynomial \(S_3\) satisfies the *exact* identity

\[
S_3(r)=r^5 H(r+r^{-1}-2).
\]

Since \(H(0)=-1229026<0\) and every other coefficient of \(H\) is positive, \(H\) is strictly increasing on \([0,\infty)\) and tends to positive infinity. Hence it has a unique positive root \(z_*\). The map \(r\mapsto r+r^{-1}-2\) is strictly increasing on \((1,\infty)\), decreasing on \((0,1)\), and invariant under \(r\leftrightarrow r^{-1}\). This proves the full three-step classification and both threshold values.

**Step 3: Certificate validity for all real fitness values.** The standalone `verify.py` does not infer an infinite theorem from a finite sample. Each entry of either one-step transition matrix has, after multiplication by the common denominator \(d(r)=(r+2)(2r+1)\), a polynomial numerator of degree at most two. Therefore every entry of \(Q_\tau\), after multiplication by \(d(r)^{2\tau}\), has polynomial degree at most \(4\tau\). Cramer's rule on the six transient equations makes the exact uniform fixation probability a rational function with numerator and denominator degrees at most \(24\tau\). Cross-multiplication against the proposed formula, whose numerator and denominator each have degree \(4\tau+1\), gives a polynomial identity of degree at most \(28\tau+1\). The verifier evaluates the original finite Markov chain in exact rational arithmetic at \(28\tau+2\) distinct positive integer fitness values and checks the proposed rational formula identically at every point. A nonzero polynomial of the stated degree cannot have that many roots; thus the verified formula holds identically as a rational function for **all real** \(r>0\). The verifier separately checks the exact difference identities and the transformed polynomial \(H\).

Finally, exact elimination in the static path gives

\[
\rho_{\mathrm{path}}(r)=\frac{r^2(2r+3)}{(r+2)(2r^2+r+2)},\qquad
\rho_{\mathrm{path}}(r)-\rho_{\mathrm M}(r)=
\frac{r^2(r-1)}{(r+2)(r^2+r+1)(2r^2+r+2)}.
\]

The same bounded-degree method verifies this identity independently, and its sign proves strict amplification of both constituent paths. For two vertices there is no distinct connected simple unweighted pair, proving the stated minimality within this graph class.

## Verification

Run `python3 verify.py` with Python 3.10 or later from the extracted package. It uses the standard library only and checks the 30, 58, 86, and 114 exact-rational interpolation nodes for block lengths one through four, respectively, the static-path identity at 18 additional nodes, every polynomial difference certificate, and the all-positive or all-negative sign coefficients. `COEFFICIENTS.txt` is an independent readable record of the full arrays. All files are included in this package; no external data, floating-point computation or unavailable historical artifact is needed. Numerical approximations to the threshold are illustrative; the polynomial-root characterization is exact.

## Relationship to prior work

Bhaumik and Masuda (arXiv:2304.00170, original preprint March 31, 2023) introduce deterministic switching birth–death dynamics and derive the general matrix backward equation. Their three-site example alternates a star/path and a triangle; other examples alternate a star and a complete bipartite graph. This theorem treats **two path/star graphs with different hub vertices**, so *both* static constituents are individually strict amplifiers. The earlier Markov-equation framework is used here but its general form alone does not give the all-fitness signs, minimal three-site two-amplifier example, or the exact unique three-step fitness crossover. Su, McAvoy and Plotkin (arXiv:2301.11982) analyze broader evolutionary strategy dynamics on changing networks, but the accessible material inspected does not identify the stated small-graph exact fixation phase diagram. Mathematical record searches found no exact equivalent; absence from those searches is not a proof of novelty.

## Limitations

The classification is restricted to the given labeled three-site changing-hub path pair, boundary-aligned equal integer block lengths \(\tau\in\{1,2,3,4\}\), birth–death (not death–birth) updating, and one uniformly placed mutant of constant fitness. No complete theorem for all \(\tau\ge5\), arbitrary dynamic graphs, within-block initialization, nonlinear fitness or mutation is asserted. The uniqueness of a priority claim is not certified; unindexed analogous temporal-graph formulas and general domination theorems remain possible. No independent external audit has been carried out.

## References

1. J. Bhaumik and N. Masuda, *Fixation probability in evolutionary dynamics on switching temporal networks*, arXiv:2304.00170 (initial public release March 31, 2023), https://arxiv.org/abs/2304.00170 ; *Journal of Mathematical Biology* **87**, article 64 (2023), DOI:10.1007/s00285-023-01987-5.
2. Q. Su, A. McAvoy and J. B. Plotkin, *Strategy evolution on dynamic networks*, arXiv:2301.11982 (initial public release January 27, 2023), https://arxiv.org/abs/2301.11982 ; *Nature Computational Science* **3**, 763–776 (2023).
3. E. Lieberman, C. Hauert and M. Nowak, *Evolutionary dynamics on graphs*, *Nature* **433**, 312–316 (2005), DOI:10.1038/nature03204.
