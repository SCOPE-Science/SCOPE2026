# A ten-residue topology switch in three-opinion plurality equilibria on cyclic ladders

## Finding

For every integer \(n\ge3\), consider two labelled cubic graphs with \(2n\) vertices: the prism \(P_n=C_n\square K_2\) and the Möbius ladder \(M_n\), obtained by interchanging the two longitudinal edges at the closing seam. Give every vertex one of three named opinions. Under synchronous unique-plurality updating, a vertex changes to the uniquely most frequent opinion among its **three open neighbors**; if there is no unique plurality, it retains its existing opinion. Let \(E_P(n)\) and \(E_M(n)\) denote the numbers of fixed configurations, with no quotient by color or graph symmetries, and set \(D_n=E_P(n)-E_M(n)\).

**Exact all-length result.** Define integer sequences \(U_n,V_n\) by
\[
\begin{aligned}
&U_0=4,\quad U_1=0,\quad U_2=-2,\quad U_3=-3,\\
&U_{n+4}+U_{n+2}+U_{n+1}+U_n=0,\\[3pt]
&V_0=4,\quad V_1=3,\quad V_2=1,\quad V_3=-3,\\
&V_{n+4}-3V_{n+3}+4V_{n+2}-2V_{n+1}+V_n=0.
\end{aligned}
\]
Then for every \(n\ge3\),
\[
\boxed{D_n=6(-1)^n+2U_n+4V_n.}
\]
Put \(\varphi=(1+\sqrt5)/2\). The formula has the sharper exact spectral form
\[
D_n=6(-1)^n+2U_n+8\varphi^n\cos(n\pi/5)
       +8\varphi^{-n}\cos(2n\pi/5).
\]
In particular, its **strict sign for every allowable length** is determined by the residue of \(n\) modulo ten:
\[
\boxed{\begin{aligned}
E_P(n)&>E_M(n)&&\Longleftrightarrow n\bmod10\in\{0,1,2,8,9\},\\
E_P(n)&<E_M(n)&&\Longleftrightarrow n\bmod10\in\{3,4,5,6,7\}.
\end{aligned}}
\]
There is never equality. Moreover
\[
D_n=8\varphi^n\cos(n\pi/5)+O((3/2)^n).
\]
Thus a single closing twist changes the direction of the stationary-state advantage periodically in ten-rung blocks, with a golden-ratio-sized leading correction. Both complete counts are also exact finite traces of the explicit matrix in the proof, not just an asymptotic comparison.

## Assumptions and scope

For each \(i\in\{0,\ldots,n-1\}\) write the two vertices of rung \(i\) as \((i,0),(i,1)\). Both graphs have rung edges \((i,0)(i,1)\) and longitudinal edges \((i,r)(i+1,r)\) for \(0\le i<n-1\), \(r\in\{0,1\}\). In \(P_n\), the last longitudinal edges join \((n-1,r)\) to \((0,r)\); in \(M_n\), they join \((n-1,r)\) to \((0,1-r)\). These are simple cubic graphs exactly as required for \(n\ge3\). Configurations use the named colors \(\{0,1,2\}\), and each edge and neighbor has unit weight. A fixed configuration means it is unchanged after one synchronous update; no claim about first-entry times, basins, or possible longer cycles is made.

In a degree-three neighborhood, an opinion is fixed when either the three neighbor opinions are all distinct, or the opinion occurring twice or three times is the current one. The case with three distinct neighbor opinions is a tie and therefore does not change the vertex.

## Proof

**1. An all-length transfer identity.** Let \(\mathcal R=\{0,1,2\}^2\) be the nine possible ordered rung-color pairs. Define
\[
s(c;a,b,d)=\begin{cases}
1,&\text{if }a,b,d\text{ are pairwise distinct, or if their unique plurality is }c,\\
0,&\text{otherwise}.
\end{cases}
\]
Use \(81\) transfer states \((u,v)\in\mathcal R^2\), where \(u\) is a previous rung and \(v\) a current rung. Define the integer transfer matrix \(T\) by
\[
T_{(u,v),(v',w)}=
\mathbf1_{\{v=v'\}}s(v_0;u_0,v_1,w_0)s(v_1;u_1,v_0,w_1).
\]
Each nonzero transition checks both stationary conditions at the current rung \(v\). A closed \(n\)-step walk is therefore exactly one labelled stationary coloring of \(P_n\), and
\[
E_P(n)=\operatorname{tr}(T^n).
\]
Let \(J\) be the involutive permutation of \(\mathcal R^2\) swapping the two rails of both rung entries: \(J(u,v)=((u_1,u_0),(v_1,v_0))\). The transfer commutes with \(J\). Twisted closure imposes \(v_{i+n}=Jv_i\), so it yields
\[
E_M(n)=\operatorname{tr}(JT^n).
\]
This equality is valid for all \(n\ge3\) and is independent of any finite-\(n\) enumeration.

**2. Exact antisymmetric determinant.** The 81 transfer states split under \(J\) into nine fixed states and 36 distinct two-element orbits. For each two-element orbit choose its lower-index representative \(i\), and define the \(36\times36\) integer matrix
\[
B_{ij}=T_{ij}-T_{i,Jj}.
\]
This is the action of \(T\) on the antisymmetric basis \(e_i-e_{Ji}\). By exact integer characteristic-polynomial expansion,
\[
\boxed{\det(zI-B)=z^{21}(z+1)^3
(z^4+z^2+z+1)
(z^4-3z^3+4z^2-2z+1)^2.}
\]
The expansion is an explicitly reproducible finite algebraic identity: `verify.py` builds every matrix entry from the local transition rule, constructs the antisymmetric quotient, and compares its exact symbolic characteristic polynomial with the right-hand side, with no numerical fitting. The same script independently checks the \(45\)-dimensional symmetric quotient, whose characteristic polynomial is
\[
z^{21}(z-1)^2(z+1)^3
(z^5-5z^4+7z^3-4z^2+6z-3)
(z^7-z^6+3z^5-2z^4-4z^2-3z-3)^2.
\]
Since \(\operatorname{tr}(T^n)-\operatorname{tr}(JT^n)\) is twice the trace of the antisymmetric quotient, we have \(D_n=2\operatorname{tr}(B^n)\). Newton identities applied to the two quartic factors give exactly the displayed integer recurrences and
\[
D_n=6(-1)^n+2U_n+4V_n.
\]
Thus the fixed finite matrix identity implies an infinite family of exact counting statements.

**3. Golden-ratio angular spectrum.** The roots of the second quartic are
\[
\varphi e^{\pm i\pi/5},\qquad \varphi^{-1}e^{\pm2i\pi/5}.
\]
Their sum-of-powers identity gives
\[
V_n=2\varphi^n\cos(n\pi/5)+2\varphi^{-n}\cos(2n\pi/5),
\]
which proves the exact trigonometric expression for \(D_n\).

**4. Rigorous all-length sign test.** Write \(P(z)=z^4+z^2+z+1\). On \(|z|=3/2\),
\[
|z^4|=81/16>19/4\ge|z^2+z+1|.
\]
Rouché's theorem puts all four roots of \(P\) strictly inside \(|z|=3/2\). Hence \(|U_n|<4(3/2)^n\). For integer \(n\), the smallest possible value of \(|\cos(n\pi/5)|\) is \((\sqrt5-1)/4\), never zero. The leading term in \(D_n\) therefore dominates the remainder whenever
\[
2(\sqrt5-1)\varphi^n>8(3/2)^n+6+8\varphi^{-n}.
\]
At \(n=16\), the left side minus the right side is exactly
\[
5168\sqrt5-93067073/8192>0.
\]
After division by \(\varphi^n\), every term on the right decreases with increasing \(n\), so the inequality holds for all \(n\ge16\). For \(3\le n\le15\), direct use of the two certified integer recurrences gives, in increasing order,
\[
(D_3,\ldots,D_{15})=(-24,-42,-84,-96,-78,102,462,996,1326,840,-1320,-5538,-10974).
\]
Their signs also agree with \(\cos(n\pi/5)\). This proves the ten-residue strict-sign classification and the stated asymptotic error bound.

## Verification

Run `python3 verify.py` in a Python 3 environment with SymPy installed. The program checks both exact characteristic polynomials; the transfer/rail-swap trace identities against Newton recurrences through length 18; the integer sign pattern through length 60; and the exact symbolic Rouché-domination margin. A separate code path builds each graph explicitly and exhaustively checks all \(3^{2n}\) named configurations on both graphs at \(n=3,4,5,6\), independently of the transfer matrix. `verification_output.txt` contains a successful run, including these complete stationary-state counts:

| \(n\) | \(E_P(n)\) | \(E_M(n)\) | \(D_n\) |
|---:|---:|---:|---:|
| 3 | 15 | 39 | -24 |
| 4 | 93 | 135 | -42 |
| 5 | 219 | 303 | -84 |
| 6 | 489 | 585 | -96 |
| 7 | 1227 | 1305 | -78 |
| 8 | 3645 | 3543 | 102 |
| 9 | 10293 | 9831 | 462 |
| 10 | 27069 | 26073 | 996 |

The finite enumerations corroborate but do not establish the all-length theorem; that conclusion rests on the transfer identity, exact determinant, quartic spectrum and analytic inequality.

## Relationship to prior work

The published model of Becchetti et al. (2013) uses randomized three-neighbor sampling on a clique and uniform random tie resolution. It does not specify the deterministic open-neighbor incumbent-retaining map on cubic ladders, nor exact stationary-state counts. The binary majority work of Benjamini et al. (2014) concerns a two-opinion update and eventual periods, not three-color fixed-state enumeration. Apt et al. (2015) study coordination-game Nash equilibria. **For this particular cubic graph and common three-color palette, the fixed states here are exactly the pure Nash equilibria of the unit-weight coordination game:** if all three neighbor colors differ, every available strategy has payoff one; otherwise the unique most frequent color is the unique best response. The existing general Nash-equilibrium analysis does not give the all-length enumerations on these two ladder families, their antisymmetric transfer spectrum, or the ten-residue sign law.

Sánchez Muñoz and Mc Gettrick (2021) enumerate equilibria on open and circular ladders, but for a **two-choice anti-coordination game** rather than this three-choice coordination game; their results neither include Möbius seam closure nor imply its present sign law. An exact published result on binary public-goods equilibria for prisms also uses a different best-response predicate (activate only at zero or three active neighbors), and supplies neither the three-opinion coordination count nor a Möbius seam comparison. An accessible published exact study of **binary** majority on prisms and Möbius ladders gives Lucas-number fixed-state and two-cycle counts and a mod-six oscillation response; those formulas do not imply the three-opinion stationary-state counts here. A separate earlier finite computation already gave the \(n=5\) prism value \(219\), so that isolated value is not presented as novel. The contribution here is the simultaneous all-size three-opinion fixed-state law, exact Möbius seam correction and proven ten-residue sign reversal.

## Limitations

This is a result about **fixed points only** under the specified three-color update rule, not about every recurrent orbit or convergence toward a fixed point. For other palette sizes, other tie rules, weighted edges, larger strip widths or arbitrary graph modifications, no classification is asserted. The published-literature comparison cannot exclude every unindexed equivalent derivation, and this work has not had independent external scientific validation. Finite computational agreement is not substituted for the infinite proof.

## References

1. L. Becchetti, A. Clementi, E. Natale, F. Pasquale, R. Silvestri and L. Trevisan, *Simple Dynamics for Plurality Consensus*, arXiv:1310.2858, initially submitted 2013-10-10. https://arxiv.org/abs/1310.2858
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, initially submitted 2014-05-11. https://arxiv.org/abs/1405.2486
3. K. R. Apt, B. de Keijzer, M. Rahn, G. Schäfer and S. Simon, *Coordination Games on Graphs*, arXiv:1501.07388, initially submitted 2015-01-29. https://arxiv.org/abs/1501.07388
4. *A Lucas-number seam response in majority oscillations on prism and Möbius ladders*, public mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-lucas-number-seam-response-in-majority-oscillations-on-prism-a--69a75f8bbc7c
5. V. Sánchez Muñoz and M. Mc Gettrick, *Nash Equilibria in Certain Two-Choice Multi-Player Games Played on the Ladder Graph*, arXiv:2101.09103, initially submitted 2021-01-22. https://arxiv.org/abs/2101.09103
6. *Parity-twisted equilibrium census for 0-or-3 public goods on prism networks*, publicly available mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parity-twisted-equilibrium-census-for-0-or-3-public-goods-on-pri--10332c192abb
