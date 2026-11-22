# Exact Fourier singularity and optimal range projection for octagon quadrangulations

## Finding
Let \(D_N\) be the set of internal diagonals of a convex even-sided \(N\)-gon that connect vertices of opposite cyclic parity, and let \(Q_N\subseteq\mathbb F_2^{D_N}\) contain the incidence vector of every quadrangulation. Define unnormalized counting convolution \(T_N f(x)=\sum_{q\in Q_N}f(x+q)\) and its Walsh multiplier \(W_N(S)=\sum_{q\in Q_N}(-1)^{|S\cap q|}\), for every \(S\subseteq D_N\).

The **octagon** has eight eligible diagonals and twelve quadrangulations. Its complete signed Walsh spectrum is:

| \(W_8(S)\) | \(-8\) | \(-6\) | \(-4\) | \(-2\) | \(0\) | \(2\) | \(4\) | \(6\) | \(12\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 8 | 16 | 18 | 48 | 72 | 48 | 28 | 16 | 2 |

Consequently \(\operatorname{rank}(T_8)=184\), its nullity is \(72\), its least nonzero absolute multiplier is \(2\), and its positive-spectrum \(\ell^2\) condition number is \(6\). Among the vanishing frequencies, exactly \(16\), \(40\), and \(16\) have character supports of sizes \(2\), \(4\), and \(6\), respectively. In particular, the first cancellations occur at weight two, **precisely for pairs of crossing eligible diagonals**.

Writing \(\mathcal R=\operatorname{range}(T_8)\), the sharp norms among **all** real or complex linear projections \(P:\ell^1(\mathbb F_2^8)\to\mathcal R\) and among all such projections on \(\ell^\infty\) are both
\[
\min_P\|P\|=\frac{59}{16}.
\]

This is the first singular polygon-quadrangulation counting convolution: the square and hexagon instances are invertible. **Invertibility returns at the decagon**, whose \(55\) quadrangulations give odd-valued, everywhere nonzero Walsh multipliers. The sharp smallest decagon multiplier magnitude is \(1\), and its \(\ell^2\) condition number equals \(55\).

## Assumptions and scope
Vertices are indexed \(0,1,\ldots,N-1\) cyclically. Only internal diagonals with endpoints of different parity are coordinates: the polygon boundary is never a coordinate. A quadrangulation divides the full polygon into quadrilateral regions. Each such quadrangulation has exactly \((N-4)/2\) chosen diagonals. All groups use XOR addition and **counting**, not probability-normalized, convolution; all displayed Fourier transforms are unnormalized. The projection statements concern all bounded finite-dimensional real or complex linear projections, with no translation-invariance assumption.

## Proof
**1. Complete geometric reduction.** A diagonal in a quadrangulation joins opposite vertex colours, since each quadrilateral boundary alternates colours. Conversely, take \((N-4)/2\) noncrossing eligible diagonals. They partition the polygon into \((N-2)/2\) regions, each having even boundary length at least four. The sum of region side counts is \(N+2(N-4)/2=2N-4\), exactly four times the number of regions, so every region is a quadrilateral. Thus the noncrossing-subset model is exact in both directions.

**2. A Wagner-graph interpretation.** For \(N=8\), in lexicographic order the eight eligible diagonals are
\[
(0,3),(0,5),(1,4),(1,6),(2,5),(2,7),(3,6),(4,7).
\]
Call them \(d_0,\ldots,d_7\). The graph \(H\) with these diagonals as vertices and a pair joined if and only if they do not cross has the cycle of vertices
\[
(d_0,d_1,d_4,d_5,d_7,d_2,d_3,d_6)
\]
in that cyclic order, together with the four edges between opposite cycle vertices, and no other edges. This follows by the strict endpoint-interleaving crossing test. Hence \(H\) is the eight-vertex Möbius ladder, or Wagner graph. It is cubic, with twelve edges; those twelve edges are exactly the octagon quadrangulations.

**3. Character-to-cut identity and spectrum.** For any \(S\subseteq V(H)\), an edge has negative Walsh sign precisely when one of its endpoints belongs to \(S\). Therefore
\[
W_8(S)=12-2|\delta_H(S)|,
\]
where \(\delta_H(S)\) is the edge boundary of \(S\). An exact 256-subset enumeration (the complete integer certificate in `verify.py`) gives the following entire cut distribution:

| Cut size | 0 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Number of vertex subsets | 2 | 16 | 28 | 48 | 72 | 48 | 18 | 16 | 8 |

The formula above gives the claimed signed spectrum, rank and gap. For a singleton \(S\), cubic regularity gives \(W_8(S)=12-2\cdot3=6\). For \(S=\{u,v\}\), the cut has size \(6-2\mathbf1_{uv\in E(H)}\), so \(W_8(S)=4\mathbf1_{uv\in E(H)}\). Exactly \(\binom82-12=16\) pairs cancel, precisely the pairs of crossing diagonals. Exhaustive cut counting further gives the asserted higher-support zero counts.

**4. Unrestricted sharp projection norm.** Put \(G=\mathbb F_2^8\) and \(\Omega=\{S:W_8(S)\ne0\}\). The unique translation-invariant projection onto \(\mathcal R\) has convolution kernel
\[
K(g)=2^{-8}\sum_{S\in\Omega}(-1)^{\langle S,g\rangle}.
\]
Writing \(h(g)=256K(g)\), the exact integer multiplicity table is:

| \(h(g)\) | \(-72\) | \(-16\) | \(-8\) | \(-4\) | \(0\) | \(4\) | \(8\) | \(16\) | \(24\) | \(184\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 1 | 8 | 2 | 32 | 160 | 32 | 8 | 8 | 4 | 1 |

Thus \(\sum_g|h(g)|=944\) and \(\|K\|_{\ell^1}=944/256=59/16\). This is simultaneously the induced \(\ell^1\) and \(\ell^\infty\) operator norm of this convolution projection. To see optimality among arbitrary projections, average any projection \(P\) onto \(\mathcal R\) over all translation conjugates. Translations preserve \(\mathcal R\), the average remains a projection onto \(\mathcal R\), and its norm cannot exceed \(\|P\|\). The average commutes with every translation, so Fourier diagonalization forces it to be exactly the displayed unique projection. Therefore no unrestricted projection has smaller norm.

**5. First singular order and subsequent recovery.** The classical Fuss–Catalan count of quadrangulations of a convex \((2r+2)\)-gon is \(\frac1{2r+1}\binom{3r}{r}\). For \(r=1,2,3,4\), the counts are respectively \(1,3,12,55\), corresponding to four, six, eight, ten sides. Odd total cardinality forces every signed Walsh sum to be odd, hence nonzero, at the four-, six- and ten-gon orders; the octagon is singular by step 3. In the decagon, the selected three-coordinate frequency \(\{(0,3),(0,5),(1,8)\}\) has 27 negative and 28 positive quadrangulation contributions, so its multiplier is \(1\). This realizes the least positive absolute magnitude, and the zero-frequency multiplier \(55\) gives the stated condition number.

## Verification
The self-contained `verify.py` uses only Python integer arithmetic. It enumerates eligible diagonals by endpoint parity, independently checks every candidate noncrossing subset against the exact Fuss–Catalan count, and constructs the compatibility graph from geometry. It then checks that the graph equals the explicitly presented Möbius ladder, compares **every** one of 256 directly summed quadrangulation Walsh coefficients with an independently evaluated Wagner cut-size formula, and checks both complete spectra and every support-weight zero count. An integer Walsh transform of the zero/nonzero spectral mask checks the full projection-kernel multiplicity table and its exact \(59/16\) norm. The decagon computation enumerates all 55 configurations, checks oddness of all \(2^{15}\) coefficients, and independently evaluates the explicit magnitude-one witness. Running `python3 verify.py` terminates with three `PASS` lines. The finite exhaustive enumeration is a proof of these finite assertions, **not** of any infinite-order assertion.

## Relationship to prior work
Schuetz and Whieldon (2014, arXiv:1401.7194) develop exact Fuss–Catalan and polygonal-dissection enumeration, including a bijection with rooted trees. Chapoton (2015, arXiv:1505.05990) studies quadrangulation-compatible flip graphs, Stokes posets, and enumerative properties; those graphs are not the diagonal-pair compatibility graph used here. The Wagner-graph identification is explicitly demonstrated here, and its cut generating polynomial controls the signed quadrangulation Fourier transform. General Ising/cut and Tutte polynomial methods can in principle compute graph cut counts; the new finite claim is the particular geometric identification, complete signed spectral census, first cancellation geometry, immediate decagon recovery and exact unrestricted projection constant together.

## Limitations
The complete spectrum and projection constant are asserted only for the octagon. The decagon assertion is limited to zero-free invertibility, an attained smallest multiplier magnitude, and its resulting Hilbert-space condition number. No classification for larger quadrangulations, asymptotics, or independent verification is claimed. Numerical tables follow from complete finite integer enumeration, not closed formulas for all polygon sizes. The possibility of an unindexed equivalent prior computation remains.

## References
1. A. Schuetz and G. Whieldon, *Polygonal Dissections and Reversions of Series*, arXiv:1401.7194, first posted 2014-01-28. https://arxiv.org/abs/1401.7194
2. F. Chapoton, *Stokes posets and serpent nests*, arXiv:1505.05990, first posted 2015-05-22. https://arxiv.org/abs/1505.05990
3. House of Graphs, *Wagner graph M8*, graph 640, graph identity and structural reference. https://houseofgraphs.org/graphs/640
