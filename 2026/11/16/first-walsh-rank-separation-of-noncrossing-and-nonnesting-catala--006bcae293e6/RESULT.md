# First Walsh-rank separation of noncrossing and nonnesting Catalan partitions

## Finding

In the canonical pair-incidence representation of set partitions, the unnormalized Walsh transforms of the noncrossing and nonnesting Catalan families have identical signed spectra for \(n=2,3,4\) but different ranks already at \(n=5\). Both order-five supports have 42 elements. The noncrossing indicator has no vanishing Walsh multipliers, whereas the nonnesting indicator has exactly 119, so their counting-convolution ranks on \(\mathbb F_2^{10}\) are respectively \(1024\) and \(905\). In particular these two Catalan sets are not affinely equivalent in the canonical ten-dimensional binary edge space. The exact signed spectra are recorded in `spectrum.csv`.

## Assumptions and scope

Let \(n\) be an integer with \(2\le n\le5\). A set partition \(\pi\) of \([n]=\{1,\ldots,n\}\) is identified with the vector \(v(\pi)\in\mathbb F_2^{\binom n2}\) whose \(ij\) entry is one exactly when \(i,j\) share a block. A partition is noncrossing if no four positions \(a<b<c<d\) satisfy \(a,c\) in one block and \(b,d\) in another. Its arcs connect consecutive elements of each block; a partition is nonnesting if two arcs are never of the form \((a,d),(b,c)\) with \(a<b<c<d\). Denote these sets by \(\mathrm{NC}_n\) and \(\mathrm{NN}_n\).

For either family \(\mathcal F\), define the unnormalized Walsh coefficient at a frequency \(t\in\mathbb F_2^{\binom n2}\) by
\[
W_{\mathcal F}(t)=\sum_{\pi\in\mathcal F}(-1)^{\langle t,v(\pi)\rangle}.
\]
The convolution operator is \((T_{\mathcal F}f)(x)=\sum_{\pi\in\mathcal F} f(x+v(\pi))\) on complex (or real) functions on the Boolean group; its rank is the number of nonzero Walsh coefficients. Multiplicities in `spectrum.csv` count all frequency vectors, including zero frequency. The claims concern these precise embeddings; they do not assert equivalence or inequivalence for every other realization of the two Catalan families.

## Proof

Enumerate partitions by restricted growth strings: the first label is zero and each next label lies between zero and one plus the largest previous label. Each such string represents exactly one partition. Apply the four-point crossing criterion and the successive-element arc nesting criterion from the preceding definitions. This gives exactly \(2,5,14,42\) partitions in each family for \(n=2,3,4,5\).

For an independent construction of the nonnesting family, list all positive type-\(A\) roots as intervals \((i,j)\) with \(i<j\). An antichain is a set of intervals with no pair contained in the other. Join the endpoints of the chosen intervals, take connected components, and normalize the resulting block labels. Exhaustive traversal of all subsets of positive roots agrees, partition by partition, with the successive-arc criterion in each tested dimension. Thus the nonnesting support is not dependent on only one characterization.

For each family, set an indicator equal to one at every distinct pair-incidence vector and zero elsewhere. The Walsh–Hadamard butterfly recursion computes its complete \(2^{\binom n2}\) coefficients using only integer sums and differences. Independently, for every frequency, sum the character signs directly over the support vectors. The two lists agree term by term. For \(n=2,3,4\) the entire signed-multiplier multiplicity histograms agree, and the zero counts are \(1,0,16\). For \(n=5\), the certificate gives
\[
\#\{t:W_{\mathrm{NC}_5}(t)=0\}=0,\qquad
\#\{t:W_{\mathrm{NN}_5}(t)=0\}=119.
\]
Since there are \(2^{10}=1024\) frequencies, Fourier diagonalization yields ranks \(1024\) and \(905\). These are finite exhaustive identities, not extrapolations to larger \(n\).

To establish affine inequivalence, suppose an invertible affine map \(x\mapsto Ax+b\) mapped one support to the other. The Walsh transforms would then satisfy
\[
W_{A\mathcal F+b}(t)=(-1)^{\langle t,b\rangle} W_{\mathcal F}(A^{\mathsf T}t).
\]
The map \(t\mapsto A^{\mathsf T}t\) is a permutation of frequencies and phases cannot create or remove zeros. The observed distinct zero counts therefore rule out such an affine map.

## Verification

Run `python3 verify_catalan.py spectrum.csv` with Python 3.8 or newer. The checker reconstructs the complete combinatorial supports and all Walsh multipliers. Its positive marker is `CATALAN_NN_NC_FOURIER_SPLIT_PASS`. It verifies equality of every direct character sum and Hadamard coefficient, the support size, the independent root-antichain reconstruction of nonnesting partitions, signed multiplicities in `spectrum.csv`, and Parseval's exact identity \(\sum_t W(t)^2=2^{\binom n2}|\mathcal F|\). The checked dimensions are exactly \(2\le n\le5\).

## Relationship to prior work

Mamede (2008) and Armstrong–Stump–Thomas (2011) construct bijections and investigate the common Catalan enumeration of the noncrossing and nonnesting families. These results do not preserve the pair-incidence embedding or imply equality of all Fourier coefficients. Existing work on noncrossing incidence-character congruences concerns the noncrossing family alone, and work on noncrossing perfect matchings uses a distinct support. The contribution here is a concrete, exact obstruction to extending Catalan equinumerosity to affine Fourier equivalence in the most immediate pair-incidence realization.

## Limitations

The rank separation is an order-five result, with equality of histograms established only in orders two through four. No formula for all orders, canonical correspondence between individual frequencies, or minimality among other embeddings is claimed. The historical-literature search is bounded; uninspected related weighted-partition polynomial results could affect priority. No independent mathematical audit has been performed.

## References

1. Ricardo Mamede, *A bijection between noncrossing and nonnesting partitions of types A and B*, initial arXiv posting 2008-10-08, https://arxiv.org/abs/0810.1422.
2. Drew Armstrong, Christian Stump, Hugh Thomas, *A uniform bijection between nonnesting and noncrossing partitions*, initial arXiv posting 2011-01-06, https://arxiv.org/abs/1101.1277.
