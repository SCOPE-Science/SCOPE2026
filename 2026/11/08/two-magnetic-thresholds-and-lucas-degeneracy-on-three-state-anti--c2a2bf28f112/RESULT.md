# Two magnetic thresholds and Lucas degeneracy on three-state antiferromagnetic Potts wheels

## Finding

Let \(W_{n+1}=K_1\vee C_n\) be the wheel with one hub and \(n\ge5\) rim vertices, and let
\[
H_{J,h}(\sigma)=J\sum_{uv\in E(W_{n+1})}{\bf1}\{\sigma_u=\sigma_v\}-h\sum_{v\in V(W_{n+1})}{\bf1}\{\sigma_v=0\},\qquad \sigma_v\in\{0,1,2\},\quad J>0,\ h>0.
\]
Write \(x=h/J\) and \(L_n=F_{n-1}+F_{n+1}\), the number of independent sets of the labeled cycle \(C_n\) (the Lucas number). The complete exact ground-state energy \(E_n(x)\) and number \(g_n(x)\) of labeled spin configurations realizing it are
\[
\begin{array}{c|c|c}
\text{range}& E_n(x)/J&g_n(x)\\ \hline
0<x<2,\ n\text{ even}&-xn/2&4\\
0<x<2,\ n\text{ odd}&1-x(n+1)/2&2n\\
x=2&-n&2L_n\\
2<x<n&n(1-x)&2\\
x=n&n(1-n)&3\\
x>n&2n-(n+1)x&1
\end{array}
\]
The complete *configurations* are: for \(0<x<2\), the hub has one of the two nonfavored colors, the rim uses zero and the other nonfavored color, and zero occurs as frequently as possible subject to the parity-minimal monochromatic rim edge count; for \(x=2\), the hub has a nonfavored color and the set of rim sites in the *other* nonfavored color is an arbitrary independent set of \(C_n\), all remaining rim sites being zero; for \(2<x<n\), the rim is entirely zero and the hub is one of the two nonfavored colors; for \(x=n\) these two states coexist with the all-zero state; for \(x>n\), only the all-zero state remains. In the low-field even case, rim colors strictly alternate. In the low-field odd case, the zero sites have exactly one adjacent zero pair and otherwise alternate.

The critical field \(h=2J\) has exponentially many ground states: \(g_n(2)=2L_n\), hence \(\lim_{n\to\infty}\log g_n(2)/(n+1)=\log((1+\sqrt5)/2)\). Its favored-color occupation density changes from asymptotically \(1/2\) to asymptotically \(1\) across \(h=2J\). The second transition at \(h=nJ\) changes the hub itself and scales linearly with rim size.

## Assumptions and scope

Every edge is counted once. The wheel has \(n\ge5\) distinguishable rim vertices in cyclic order, each joined to the hub. The field is strictly positive; the symmetry-enlarged case \(h=0\) is excluded. Spins are classical named Potts colors, so exchanging the two nonfavored colors gives distinct configurations. No temperature-positive phase transition is asserted. The zero-temperature thermodynamic entropy is taken at the exactly critical field before any field or size limit.

## Proof

Normalize by \(J\), so minimizing the energy means minimizing \(U-xK\), where \(U\) is the number of monochromatic graph edges and \(K\) is the number of zero-colored vertices. First fix the hub to be color \(1\), with \(k\) of the \(n\) rim vertices colored zero. On the rim, a cyclic binary string with \(k\) zeros has at least \(\max(0,2k-n)\) adjacent zero pairs: if there are \(t\) adjacent pairs of nonzero sites, then the number of adjacent zero pairs is \(2k-n+t\). These edges necessarily contribute to \(U\). For odd \(n\), the wheel cannot be properly three-colored, because its odd rim requires three colors and its hub touches every rim site; consequently \(U\ge1\) for every spin configuration. It follows that for a nonzero hub,
\[
U-xK\ge \max\{\varepsilon_n,2k-n\}-xk,
\qquad \varepsilon_n=\begin{cases}0,&n\text{ even},\\1,&n\text{ odd}.\end{cases}
\]
For \(0<x<2\), minimizing this piecewise-linear lower bound over the integers \(0\le k\le n\) gives uniquely \(k=n/2\) for even \(n\) and \(k=(n+1)/2\) for odd \(n\). The bounds are attained by putting the other nonfavored color \(2\) on the nonzero rim sites. The even rim alternates; the odd rim has exactly one adjacent zero pair. The stated \(4\) and \(2n\) counts follow from the two hub choices and respectively two alternating arrangements or \(n\) possible positions of the unique zero-zero pair. The resulting energies are those in the first two table rows.

At \(x=2\), the same inequality gives \(U-2k\ge-n\). Equality forces \(k\ge\lceil n/2\rceil\), no adjacent nonzero rim sites, no nonzero rim site with the same color as the hub, and no additional monochromatic edges. Thus the nonzero rim sites form an arbitrary independent subset of the cycle, all in the remaining nonfavored color; conversely every such configuration has energy \(-nJ\). There are \(L_n\) independent subsets of \(C_n\), and two hub choices. For \(x>2\), the normalized nonzero-hub lower bound is uniquely minimized at \(k=n\), with all rim vertices zero and energy \(n(1-x)\); only the two hub color choices remain.

It remains to exclude a zero-colored hub below its actual transition and include it afterward. With a zero hub and \(k\) zero rim vertices, the spokes contribute exactly \(k\) monochromatic edges. For \(k\ge1\), the least possible number of zero-zero rim edges is \(\max(0,2k-n)\); all other rim edges can be made properly bichromatic by alternating colors \(1,2\) along the nonzero runs. For \(k=0\), the least rim-edge penalty is \(\varepsilon_n\). Therefore the exact minimum among configurations with a zero hub and a fixed \(k\) is
\[
B_n(k;x)=k+\max(0,2k-n)-x(k+1)\quad(1\le k\le n),\qquad B_n(0;x)=\varepsilon_n-x.
\]
For even \(n=2m\ge6\), minimizing these affine functions over \(k\) gives \(-x\) for \(0<x\le1\), \(m-(m+1)x\) for \(1\le x\le3\), and \(2n-(n+1)x\) for \(x\ge3\). For odd \(n=2m+1\ge5\), the minimum is \(1-2x\) for \(0<x\le1\), \(m-(m+1)x\) for \(1\le x\le2\), \((m+2)(1-x)\) for \(2\le x\le3\), and \(2n-(n+1)x\) for \(x\ge3\). The endpoint formulas agree where intervals meet. Direct comparison with the nonzero-hub minimum just derived shows that the zero-hub minimum is **strictly larger** for every \(0<x<n\) (the stipulated \(n\ge5\) is used here); for \(x=n\) the two hub sectors tie only at an all-zero rim; and for \(x>n\) the all-zero configuration uniquely wins. This proves all rows and configuration claims.

Finally, independent sets of \(C_n\) have count \(L_n=F_{n-1}+F_{n+1}\), by splitting on the status of one vertex and using Fibonacci path counts. Binet's formula implies \(L_n=((1+\sqrt5)/2)^n+((1-\sqrt5)/2)^n\). Hence the asserted entropy density and the occupation-density jump follow directly from the exact configuration classification. \(\square\)

## Verification

The included standalone file `verify.py` exhaustively enumerates every labeled configuration for each \(5\le n\le10\), groups by number of equal-color edges and zero sites, and checks nine rational positive field choices per size. It passes all 54 exact comparisons of ground energy and degeneracy over a total of 265356 configurations, and verifies critical occupation sets and a Lucas entropy consistency value. Run from the extracted artifact directory with `python verify.py`. The finite checks are supplementary and cannot establish statements for untested \(n\); the preceding combinatorial inequalities prove all \(n\ge5\).

## Relationship to prior work

The general finite-temperature magnetic-field Potts partition function and its spanning-subgraph representation are classical and appear in Chang–Shrock (2009, arXiv:0907.0777); this is not claimed to be a new model or partition identity. Chang–Shrock (2009, arXiv:0908.2375) and Shrock–Xu (2010, arXiv:1009.1182) give explicit **weighted proper-coloring** (zero-temperature infinite antiferromagnetic-coupling) formulas for wheel graphs. In contrast, the present finite-\(J\) magnetic competition admits and often requires monochromatic edges, including on odd wheels at arbitrarily weak positive field; the displayed full ground-state diagram and Lucas degeneracy do not follow from merely counting proper colorings. General magnetic-field strip transfer results (Chang–Shrock 2015, arXiv:1506.07392) do not explicitly evaluate this family. This is a comparison of actual mathematical content, not a claim of a globally exhaustive priority search.

## Limitations

Only three colors, one favored color, uniform positive exchange, a wheel with \(n\ge5\), and strictly positive fields are classified. It does not claim a new general Potts partition formula, positive-temperature singularity, or nontrivial infinite-volume Gibbs-phase coexistence. The first field transition occurs at fixed \(h/J=2\), while the second at \(h/J=n\) diverges with size. Earlier transfer-matrix literature may implicitly specialize to this result after additional finite-size optimization, and some older wheel-field discussions may not be indexed; such historical-priority uncertainty remains.

## References

- S.-C. Chang and R. Shrock, *Some Exact Results on the Potts Model Partition Function in a Magnetic Field*, arXiv:0907.0777 (2009), https://arxiv.org/abs/0907.0777.
- S.-C. Chang and R. Shrock, *Weighted Graph Colorings*, arXiv:0908.2375 (2009), https://arxiv.org/abs/0908.2375.
- R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182 (2010), https://arxiv.org/abs/1009.1182.
- S.-C. Chang and R. Shrock, *Exact Partition Functions for the q-State Potts Model with a Generalized Magnetic Field on Lattice Strip Graphs*, arXiv:1506.07392 (2015), https://arxiv.org/abs/1506.07392.
