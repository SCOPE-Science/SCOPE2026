# The \(2n\)-factor law for regular endomorphisms of even cycles

## Finding
For every even integer \(n\ge4\), let \(M_n=\operatorname{End}(C_n)\) be the monoid of strict graph endomorphisms of the loopless, undirected \(n\)-cycle (graph homomorphisms preserve edges and cannot collapse adjacent vertices). Let \(I_n\) be its number of idempotents and \(R_n\) its number of von Neumann regular elements, where regular means \(f=fgf\) for some \(g\in M_n\). Put
\[
a=\log 2,\qquad K=\frac32\pi^{2/3}a^{2/3},\qquad \Delta=(2^{2/3}-1)K.\]
Then, for every fixed \(\delta\) with \(0<\delta<\Delta\),
\[
0\le 1-\frac{R_n}{2n I_n}=O_\delta(e^{-\delta n^{1/3}}),\qquad n\longrightarrow\infty\text{ through even integers}.
\]
In particular \(R_n\sim 2n I_n\), and the proportion of regular elements satisfies
\[
\log\frac{R_n}{|M_n|}=-K n^{1/3}+O(\log n),
\qquad |M_n|=n\left(2+\binom n{n/2}\right).
\]
More precisely, with \(A_{h+1}\) the adjacency matrix of the path on vertices \(0,\ldots,h\) and \(W_{n,h}=(A_{h+1}^{\,n-h})_{0,h}\), the following finite, explicit bounds hold:
\[
I_n=1+n\sum_{h=1}^{n/2}W_{n,h},\quad
0\le 2n I_n-R_n\le 2n^3\sum_{h=1}^{n/2}\left[2\cos\left(\frac\pi{h+2}\right)\right]^{n-2h}.
\]
The quantitative error identifies a *unique full monotone span* as the typical witness of regularity under conditioning on regularity, rather than merely reproducing the idempotent count.

## Assumptions and scope
Write the vertex set of \(C_n\) as \(\mathbb Z/n\mathbb Z\), with edges between residues differing by \(\pm1\). Composition of maps may be read in either conventional order if the von Neumann regularity identity is adjusted consistently; here \(fgf=f\) means \(f\circ g\circ f=f\). The result is for even \(n\ge4\), since for odd cycles all strict endomorphisms are automorphisms. The notation \(\operatorname{rank}(f)\) refers to the cardinality of the image, not the minimum size of a generating set of a semigroup.

For \(n\) even, each strict endomorphism has a unique step word \(\epsilon_0,\ldots,\epsilon_{n-1}\in\{+1,-1\}\) specified by \(f(i+1)-f(i)\equiv\epsilon_i\pmod n\). Summing these integer steps gives either \(+n\), \(-n\), or \(0\). The first two are the \(2n\) automorphisms; the remaining maps correspond to length-\(n\) \(\pm1\)-bridges. Their lifted heights \(H_0=0, H_j=\sum_{i<j}\epsilon_i\) have span \(h=\max H_j-\min H_j\) between \(1\) and \(n/2\), and the image rank is \(h+1\).

## Proof
**1. Regularity and full spans.** A nonautomorphism \(f\) with bridge height span \(h\) is regular if and only if the cyclic step word contains a consecutive block of exactly \(h\) positive steps or exactly \(h\) negative steps. To see necessity without assuming a numerical enumeration theorem, take \(g\) with \(fgf=f\). The map \(gf\) is idempotent; its rank equals \(\operatorname{rank}(f)\), and \(f\) is injective on its image. The image of this idempotent is a proper connected arc of \(C_n\) of \(h\) edges. An injective graph homomorphism on that arc must be monotone along the target arc, so the step word has a full monotone run. Conversely a monotone run realizing both extrema gives a graph isomorphism from a source arc onto the image arc. Extend its inverse to a dihedral automorphism \(g\) of \(C_n\); then \(fgf=f\). This is also the criterion established by Dimitrova--Fernandes--Koppitz--Quinteiro, Proposition 2.1, for strict cycle endomorphisms.

**2. Mark the runs.** For fixed span \(h\), choose the starting input position of a full run in \(n\) ways, its orientation in \(2\) ways, and the image of its starting vertex in \(n\) ways. The other \(n-h\) steps form an endpoint-to-endpoint path within a strip of heights \(0,\ldots,h\); their number is \(W_{n,h}\). The total number \(T_n\) of *marked* full-run occurrences in nonautomorphism maps is consequently
\[
T_n=2n^2\sum_{h=1}^{n/2}W_{n,h}.
\]
On the other hand, a proper idempotent fixes its image arc pointwise. Choose that arc in \(n\) ways and fill the complementary input arc with such a strip walk. Including the identity gives \(I_n=1+n\sum_hW_{n,h}\), hence exactly \(T_n=2n(I_n-1)\).

**3. Multiple-run bound.** Two distinct full monotone runs of one bridge cannot share a step: overlapping runs of the same sign would force the bridge span to exceed \(h\), whereas opposite signs cannot overlap. Mark an ordered pair of such distinct runs. For span \(h\), there are at most \(n^2\) choices of their starting input positions, four orientation pairs, and \(n\) choices for one initial output label. The two intervening, unmarked walk pieces have lengths summing to \(n-2h\), each staying within the same \((h+1)\)-vertex path. Since the spectral radius of its adjacency matrix is \(\rho_h=2\cos(\pi/(h+2))\), the number of completions for fixed marks is at most \(\rho_h^{n-2h}\). Thus the number of unordered pairs of full runs is at most
\[
P_n\le2n^3\sum_{h=1}^{n/2}\rho_h^{n-2h}.
\]
If a map has \(m\ge1\) full runs, the excess \(m-1\) is at most \(\binom m2\). Hence the number \(B_n\) of regular nonautomorphisms satisfies \(T_n-P_n\le B_n\le T_n\). Adding the \(2n\) automorphisms yields \(0\le 2nI_n-R_n\le P_n\), the announced finite inequality.

**4. Sharp logarithmic exponent and excess suppression.** For every \(h\ge1\), \(\rho_h=2\cos(\pi/(h+2))\) and \(\log\cos t\le-t^2/2\) for \(0\le t<\pi/2\). Minimizing \(ax+\pi^2n/(2x^2)\), with \(x>0\), gives \(K n^{1/3}\); minimizing \(2ax+\pi^2n/(2x^2)\) gives \(2^{2/3}K n^{1/3}\). Writing \(x=h+2\) shows uniformly for \(1\le h\le n/2\) that
\[
\rho_h^{n-h}\le C2^n e^{-K n^{1/3}},\qquad
\rho_h^{n-2h}\le C2^n e^{-2^{2/3}K n^{1/3}}
\]
with an absolute constant \(C\). Therefore
\[
\sum_hW_{n,h}\le Cn2^n e^{-K n^{1/3}},\qquad
P_n\le Cn^4 2^n e^{-2^{2/3}K n^{1/3}}.
\]
For the needed lower bound, take \(h=\lfloor(\pi^2n/a)^{1/3}\rfloor-2\) and \(L=n-h\). The two extremal path eigenvalues are \(\rho_h\) and \(-\rho_h\), and their endpoint spectral coefficients add (because \(n\) is even). Their combined coefficient is \(4(h+2)^{-1}\sin^2(\pi/(h+2))\asymp h^{-3}\). The total absolute contribution of all other eigenvalues is at most \(\rho_{2,h}^{L}\), where \(\rho_{2,h}=2\cos(2\pi/(h+2))\). Since \(L/h^2\asymp n^{1/3}\), this is negligible relative to \(h^{-3}\rho_h^L\). Consequently \(W_{n,h}\ge c n^{-1}2^n e^{-K n^{1/3}}\) for all sufficiently large even \(n\). Combined with the upper bound, this proves
\[
\log\sum_hW_{n,h}=n\log2-K n^{1/3}+O(\log n).
\]
Finally, divide the bound on \(P_n\) by \(T_n=2n^2\sum_hW_{n,h}\):
\[
\frac{P_n}{T_n}\le\exp\left(-\Delta n^{1/3}+O(\log n)\right).
\]
This gives the asserted relative estimate for every \(\delta<\Delta\). The exact total size \(|M_n|=n(2+\binom n{n/2})\) follows by counting the two constant-sign step words and the \(\binom n{n/2}\) balanced ones for each initial image label. Stirling's formula completes the proportion asymptotic.

## Verification
A standalone Python 3 standard-library program, `verify.py`, enumerates every balanced step word for even \(n=4,6,\ldots,18\), calculates each word's span and the number of cyclic full monotone runs, and independently computes the path-adjacency transfer counts \(W_{n,h}\). It checks the exact marked-run identity, the finite bound, the idempotent formula and the direct counting of regular words. It separately constructs all graph endomorphisms for even \(n\le8\) and directly checks \(fgf=f\) and \(f^2=f\), independent of the run criterion. The verifier does **not** claim that finite checks prove the uniform asymptotic estimates; those follow from the spectral proof above.

## Relationship to prior work
Dimitrova, Fernandes, Koppitz and Quinteiro (2023 preprint, later 2024 publication) prove the full-consecutive-images criterion, classify regularity/Green relations, and compute the total cycle-endomorphism count. Those inputs are credited; their stated results do not give the present marked-run second-moment bound or asymptotic \(R_n\sim2nI_n\). Earlier exact enumeration of cycle idempotents yields the formula for \(I_n\) and its cubic-root exponent; it does not by itself count or bound regular nonidempotents. An analogous cubic-root rarity result for *path* endomorphisms involves a different monoid and has no two-cycle-to-one-retraction factor. Bouchot's 2022 work concerns random walks penalized by their range, providing broader spectral context but not the semigroup regularity comparison. No uniqueness is inferred merely from unsuccessful literature searches.

## Limitations
The graph maps are strict; weak maps that contract edges are not covered. The asymptotics are only along even \(n\), and the sharp relation has a stretched-exponential *relative error* rather than an independently derived full leading constant for \(I_n\). Published general semigroup or lattice-walk formulas not identified in the available searches might imply the result. The finite computation corroborates only the finite counting identities, not the uniform spectral estimates.

## References
1. I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149v1 (6 October 2023), Proposition 2.1; later *Mathematica Slovaca* 74 (2024), 1071–1088, DOI:10.1515/ms-2024-0078.
2. I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *Ranks of monoids of endomorphisms of a finite undirected path*, arXiv:1810.09307v1 (22 October 2018).
3. N. Bouchot, *Scaling limits for the random walk penalized by its range in dimension one*, arXiv:2202.11953v1 (24 February 2022).
4. M. A. Michels and U. Knauer, *The congruence classes of paths and cycles*, Discrete Mathematics 309 (2009), 5352–5359.
