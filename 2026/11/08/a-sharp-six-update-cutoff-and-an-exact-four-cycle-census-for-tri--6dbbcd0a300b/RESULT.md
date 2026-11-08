# A sharp six-update cutoff and an exact four-cycle census for tripartite excitation

## Finding

Consider synchronous four-state threshold-one Greenberg–Hastings excitation on a labelled complete tripartite graph \(K_{a,b,c}\), for arbitrary positive integers \(a,b,c\). The global map \(F\) obeys
\[
F^{10}=F^6.
\]
Every orbit therefore reaches periodic behavior by update six. There is exactly one fixed configuration (all resting), and every other periodic configuration has least period four. The maximal first-periodic-entry time is six if \(a+b+c\ge4\), and five on the triangle \(K_{1,1,1}\).

For \(j\in\{1,2,3,4\}\), define the onto-coloring polynomial evaluations
\[
S_j(n)=\sum_{h=0}^j(-1)^{j-h}\binom{j}{h}h^n.
\]
Define \(E_{ijk}(a,b,c)\) as the sum of \(S_u(a)S_v(b)S_w(c)\) over all **distinct** permutations \((u,v,w)\) of \((i,j,k)\). The exact number of initially primitive-four configurations is
\[
N_4(a,b,c)=\sum_{1\le i\le j\le k\le4}\alpha_{ijk}E_{ijk}(a,b,c).
\]
The 16 nonzero coefficients are:

| \((i,j,k)\) | \(\alpha_{ijk}\) | \((i,j,k)\) | \(\alpha_{ijk}\) |
|---|---:|---|---:|
| \((1,1,2)\) | 4 | \((2,2,2)\) | 42 |
| \((1,2,2)\) | 16 | \((2,2,3)\) | 32 |
| \((1,2,3)\) | 8 | \((2,2,4)\) | 6 |
| \((1,3,3)\) | 12 | \((2,3,3)\) | 36 |
| \((1,3,4)\) | 4 | \((2,3,4)\) | 12 |
| \((1,4,4)\) | 4 | \((2,4,4)\) | 6 |
| \((3,3,3)\) | 36 | \((3,3,4)\) | 12 |
| \((3,4,4)\) | 4 | \((4,4,4)\) | 1 |

All other coefficients vanish. There are exactly \(N_4(a,b,c)/4\) distinct primitive-four orbits. Primitive-four states exist if and only if \(a+b+c\ge4\), since \(S_2(n)>0\) exactly when \(n\ge2\) and every coefficient is nonnegative. In particular, \(K_{1,1,2}\) has eight primitive-four configurations (two orbits), and \(K_{2,2,2}\) has 552 primitive-four configurations (138 orbits).

## Assumptions and scope

Vertices have states \(0,1,2,3\), corresponding respectively to rest, excitation, and two recovery stages. At each synchronous step, states \(1,2,3\) become \(2,3,0\), respectively. A resting vertex becomes excited if and only if at least one vertex in a different shore has state \(1\); otherwise it remains resting. All shores are nonempty, vertices are labelled, and time is discrete. The assertions concern the first entry into an exact periodic state and the census of states already periodic at time zero, not the sizes of attraction basins.

## Proof

**(1) Exact reduction.** For a configuration, let \(M_i\subseteq\{0,1,2,3\}\) denote the nonempty set of colors occurring in shore \(i\). Let \(e_i=1\) exactly when \(1\in M_j\) for some \(j\ne i\), otherwise \(e_i=0\). Define \(g_e(0)=e\) and \(g_e(u)=u+1\) for \(u=1,2\), with \(g_e(3)=0\). Then the next support triple is exactly
\[
R(M_1,M_2,M_3)=\bigl(g_{e_1}(M_1),g_{e_2}(M_2),g_{e_3}(M_3)\bigr).
\]
The rule does not depend on within-shore multiplicities. There are only \(15^3=3375\) nonempty support triples.

**(2) Finite universal identity.** The standalone program `verify_support.py` exhausts exactly these 3375 triples with the explicitly defined map \(R\). For every triple \(s\), it verifies \(R^{10}(s)=R^6(s)\); moreover, on each of the three shores, the composition of the four color maps along the support trajectory starting at \(R^6(s)\) is the identity on every occupied initial color. These checks are a finite exhaustive certificate, not a sampling argument. Because each individual vertex follows its shore's color map, they imply \(F^{10}=F^6\) for **every** graph size \(a,b,c\).

**(3) Primitive periods.** A full state is periodic at time zero if and only if the four-step color transports on its occupied supports return all occupied colors to themselves. The same exhaustive certificate finds exactly 620 such support triples. One triple, \((\{0\},\{0\},\{0\})\), has full period one. For all other 619 triples, no occupied full configuration returns after one or two steps, whereas every one returns after four. In particular, there are no other fixed states or primitive-two periodic states. Any eventual period must divide four by step (2), so this exhausts all possible periods.

**(4) Enumeration.** For a shore of \(n\) labelled vertices, a prescribed support of \(j\) colors has exactly \(S_j(n)\) realizations, by inclusion–exclusion. The 619 nontrivial periodic support triples group by their ordered support cardinalities. The complete finite certificate gives the 16 symmetric coefficients in the table. Multiplication of the three independent onto-coloring counts and summation proves the stated \(N_4\) formula, valid without any graph-size cutoff. Dividing by four counts distinct temporal orbits because every nontrivial periodic state has period four.

**(5) Sharp entry bound.** The certificate records first-periodic-entry counts \(620,248,658,739,641,391,78\) among support triples at times \(0,1,2,3,4,5,6\). A periodic support is reached precisely when the full configuration is periodic: necessity follows by taking supports, and sufficiency follows from the verified identity of four-step color transport. On \(K_{1,1,2}\), the labelled state \((0;3;1,2)\) visits \((0;0;0,3)\) at time five and becomes all-zero at time six, so the six-update bound is attained. This witness embeds into every larger triple of shore sizes by repeating one of the colors already present in each shore. When each shore has one vertex, direct examination of the eight support triples of cardinalities \((1,1,1)\) gives maximal entry time five.

## Verification

The exact finite quotient certificate `verify_support.py` enumerates every one of the 3375 support triples, confirms the required four-step transport identities and outputs the complete nonzero coefficient list (`support_output.txt`). An independently coded direct-configuration verifier `verify_direct.py` compares the symbolic formula to actual state dynamics for all 27 triples with \(1\le a,b,c\le3\), totaling 592704 labelled configurations (`direct_output.txt`). Both checks pass. The unrestricted theorem is proved by the exact finite reduction and exhaustive size-independent quotient certificate, not by extrapolating from the 27 small cases.

## Relationship to prior work

Greenberg and Hastings introduced the excitable-medium framework. Durrett and Griffeath investigated recurrent patterns and phase behavior in excitable cellular automata; Fisch and Gravner analyzed one-dimensional deterministic Greenberg–Hastings models and stable periodic objects. Gravner, Lyu and Sivakoff's 2016 work develops a general-graph theory for **three** colors. These sources do not state the present exact four-color three-shore orbit polynomial or six-update bound. Their qualitative periodicity framework is not presented as new here.

## Limitations

This classification is for threshold one, exactly four colors, and three nonempty independent shores joined completely across shores. It does not classify other thresholds, different numbers of colors, or arbitrary multipartite graphs. The formula counts initially periodic states and distinct temporal orbits, but does not give the full distribution of transient basin sizes. The finite exhaustive certificate is essential to the precise coefficients. A literature search cannot exclude an unindexed equivalent result.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata* (first public preprint 1993-03-22), arXiv:patt-sol/9303002. https://arxiv.org/abs/patt-sol/9303002
2. R. Fisch and J. Gravner, *One-dimensional Deterministic Greenberg–Hastings Models*, Complex Systems 9 (1995), 329–348. https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs* (first public preprint 2016-10-24), arXiv:1610.07320. https://arxiv.org/abs/1610.07320
4. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics 34 (1978), 515–523. DOI:10.1137/0134040.
