# Modulo-four Fourier rigidity for bipartite connectivity and its first nonunit recovery gap

## Finding
Let \(m,n\ge2\). In the Boolean edge group \(G_{m,n}=\mathbb F_2^{E(K_{m,n})}\), let \(f_{m,n}\) be the indicator of connected spanning edge subsets of the labelled complete bipartite graph. With the **unnormalized** character multiplier
\[
W_{m,n}(\xi)=\sum_{A\subseteq E(K_{m,n}):\ (V,A)\text{ connected}}(-1)^{|A\cap\xi|},
\]
all \(2^{mn}\) multipliers obey the single arithmetic law
\[
\boxed{W_{m,n}(\xi)\equiv(-1)^{m+n}\pmod4.}
\]
Consequently unnormalized XOR counting convolution \(T_{m,n}h=f_{m,n}*h\) is invertible for every \(m,n\ge2\). If \(\min(m,n)\le3\), the least multiplier magnitude is exactly \(1\). At the first case beyond this range, \(K_{4,4}\), it is exactly \(3\); the complete signed spectrum has 49 distinct levels, with precisely 11,664 characters attaining magnitude \(3\) and no zero character. More precisely,
\[
\operatorname{rank}(T_{4,4})=65536,\quad
\min_\xi|W_{4,4}(\xi)|=3,\quad
\max_\xi|W_{4,4}(\xi)|=36317,
\]
so \(\|T_{4,4}^{-1}\|_{2\to2}=1/3\) and its exact \(\ell^2\) condition number is \(36317/3\). These spectral assertions are joint parts of the stated finding; the first is an infinite-family theorem, while the last are complete finite statements.

## Assumptions and scope
All vertices and edges are labelled. Every potential bipartite edge is a separate Boolean coordinate. A connected spanning edge subset uses every vertex and joins it in one component; it need not be a tree or have fixed cyclomatic number. For \(\xi\subseteq E(K_{m,n})\), its edge-sign matrix is \(s_{ij}=(-1)^{1_{(i,j)\in\xi}}\). Convolution is the ordinary sum over the Boolean group, not probability-normalized. The norm is the counting-measure Hilbert norm; unitary Fourier diagonalization retains multipliers \(W_{m,n}(\xi)\).

## Proof
**Connected hypergraph reduction.** For each right-shore vertex \(j\), choose its nonempty neighbourhood \(B_j\subseteq[m]\). The original graph is connected precisely when the hypergraph on \([m]\) whose hyperedges are \(B_1,\ldots,B_n\) is connected. Let \(\Pi_m\) be the lattice of set partitions of \([m]\), and for \(\pi\in\Pi_m\) put \(b=|\pi|\) and
\[
q_\pi(j)=\sum_{C\in\pi}\left(\prod_{i\in C}(1+s_{ij})-1\right).
\]
This sums weights of all nonempty choices of \(B_j\) lying inside a block of \(\pi\). Möbius inversion on the partition lattice gives the exact signed formula
\[
\boxed{W_{m,n}(\xi)=\sum_{\pi\in\Pi_m}(-1)^{b-1}(b-1)!\prod_{j=1}^n q_\pi(j).}\tag{1}
\]
Here \((-1)^{b-1}(b-1)!\) is the Möbius coefficient from a partition with \(b\) blocks to the one-block partition, and connectivity means that the common coarsest partition of the hyperedges is one block.

**Uniform residue.** Each summand \(\prod_{i\in C}(1+s_{ij})-1\) is odd, hence \(q_\pi(j)\equiv b\pmod2\). If \(b\) is even then \(\prod_jq_\pi(j)\) is divisible by \(4\), since \(n\ge2\). For \(b\ge5\), \((b-1)!\) is also divisible by \(4\). Thus modulo \(4\) only \(b=1\) and \(b=3\) matter. The one-block contribution is \((-1)^n\), because \(q_{\hat1}(j)=\prod_i(1+s_{ij})-1\equiv-1\pmod4\) for \(m\ge2\). Every three-block contribution is \(2\pmod4\), independent of the signs. Writing \(S(m,3)\) for the Stirling number of the second kind, this proves
\[
W_{m,n}(\xi)\equiv(-1)^n+2S(m,3)\pmod4.
\]
The Stirling recurrence \(S(m,3)=3S(m-1,3)+S(m-1,2)\), together with \(S(k,2)=2^{k-1}-1\) and \(S(2,3)=0\), gives \(S(m,3)\equiv m\pmod2\). The displayed residue is therefore \((-1)^{m+n}\pmod4\). In particular it is odd and nonzero at every frequency, proving invertibility.

**Sharp unit gaps for thin shores.** By transposition assume \(m\le3\). For \(m=2\), use the signs \((+1,-1)\) in every column. Formula (1) reduces to \(W_{2,n}=(-1)^n\). For \(m=3\), its three two-block partition terms vanish if the columns include both patterns \((+1,+1,-1)\) and \((-1,-1,+1)\), or both \((+1,+1,-1)\) and \((+1,-1,+1)\). When \(n\) is even, take one column of the first pair's second pattern and all remaining columns of the first pattern; the one-block product is \(+1\), the three-singleton-block product equals \(-1\), and formula (1) gives \(W_{3,n}=-1\). When \(n\ge3\) is odd, take one column \((+1,-1,+1)\) and all remaining columns \((+1,+1,-1)\); then the one-block product is \(-1\), the three-singleton-block product is \(+1\), and \(W_{3,n}=+1\). Since every multiplier is a nonzero integer, these are sharp.

**The first nonunit gap.** At \(m=n=4\), the independent finite certificate `verify.py` enumerates all 65,536 edge subsets using connectivity union-find, then performs a full integer Walsh transform. It separately generates all 15 set partitions and evaluates formula (1) for each of the 65,536 frequency matrices, asserting pointwise equality. The resulting exact 49-level signed histogram is `spectrum.csv`, including the count of 11,664 multipliers equal to \(-3\) and no multipliers of magnitude \(1\) or \(2\). The frequency mask `123` in the row-major 16-bit convention has multiplier \(-3\). There are exactly 36,317 connected spanning edge subsets: in formula (1), setting every sign to \(+1\) gives
\[
15^4-4\cdot8^4-3\cdot6^4+12\cdot5^4-6\cdot4^4=36317.
\]
The triangle inequality bounds every multiplier magnitude by 36,317, attained at the trivial character. The claimed rank, inverse norm, and condition number now follow from Fourier diagonalization.

## Verification
Run `python3 verify.py` in the same directory as the supplied `spectrum.csv`; the program independently overwrites that CSV with its recomputed full histogram, so preserve a copy before rerunning if file-byte comparison is desired. For a non-mutating check run the script in a temporary copy of the directory. It checks all 65,536 frequencies by two independent expressions, the uniform modulo-four law for the finite instance, Parseval's sum of squares, exact rank, minimum, maximum and multiplicity, and all 49 histogram levels. In the packaged run the script reported 131,072 direct formula/congruence assertions and successful global checks. Exact arithmetic is used throughout; the infinite-family congruence and thin-shore unit constructions are proved above rather than inferred from these computations.

## Relationship to prior work
Standard Fourier inversion and convolution on Boolean groups are treated by Ronald de Wolf (2008). The chromatic-polynomial and acyclic-orientation enumeration of complete bipartite graphs is classical, and an explicit literature treatment appears in Bényi and Hajnal (2017), especially the portion on bipartite orientations and chromatic coefficients. These earlier expressions give ordinary unsigned enumerations and do not, in the inspected material, state the **frequency-uniform modulo-four signed reliability law** or the **complete first nonunit gap for \(K_{4,4}\)**. Earlier Fourier computations for fixed-excess connected spanning subgraphs of \(K_{2,n}\) and for spanning trees of \(K_{4,4}\) concern strict subfamilies of the unrestricted connected spanning edge sets here; their multipliers cannot be substituted for the present spectrum. The classical formulae make the parity of unsigned counts unsurprising, so the value of the finding rests on the uniform sign-sensitive congruence and the exact transition in recoverability conditioning, not on a claim that bipartite graph coloring is new.

## Limitations
No formula is claimed for the least positive multiplier in every thicker biclique, or for the complete spectra outside \(K_{4,4}\). The 49-level statement is exact but finite and relies on the supplied exhaustive integer certificate rather than an asymptotic proof. The findings do not infer an inverse norm for the normalized probability convolution (whose multipliers differ by division by the unsigned count). Search cannot establish historical uniqueness; an overlooked specialized signed all-terminal reliability polynomial or a previously tabulated \(K_{4,4}\) spectrum remains a priority risk. Independent validation has not been performed.

## References
1. Ronald de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Library, Graduate Surveys 1 (2008), published September 25, 2008, https://www.theoryofcomputing.org/articles/gs001/gs001.pdf .
2. Béata Bényi and Péter Hajnal, *Combinatorial Properties of Poly-Bernoulli Relatives*, Integers 17 (2017), #A31, especially the sections on bipartite orientations and chromatic polynomials, https://publicatio.bibl.u-szeged.hu/11970/1/Benyi_Hajnal_Integers_2017_u.pdf .
3. J. I. Brown and D. Cox, *Nonexistence of optimal graphs for all terminal reliability*, Networks 63 (2014), first published October 1, 2013, https://doi.org/10.1002/net.21530 (only the accessible abstract and bibliography were inspected).
4. Online Encyclopedia of Integer Sequences, A212084, chromatic-polynomial coefficients of \(K_{n,n}\), https://oeis.org/A212084 .
