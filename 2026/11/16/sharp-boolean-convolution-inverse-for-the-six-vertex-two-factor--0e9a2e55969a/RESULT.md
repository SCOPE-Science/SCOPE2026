# Sharp Boolean convolution inverse for the six-vertex two-factor family

## Finding
Let \(G=(\mathbb F_2^{E(K_6)},+)\) with the counting measure and \(|E(K_6)|=15\). Let \(\mathcal F\) be the incidence vectors of the spanning simple two-regular graphs on the fixed labelled vertices \(\{0,1,2,3,4,5\}\), and let \(Tg=\mathbf1_{\mathcal F}*g\) be unnormalized group convolution. There are precisely \(70\) such two-factors: \(60\) Hamiltonian six-cycles and \(10\) unions of two disjoint triangles.

**Theorem.** The multiplier \(W(s)=\sum_{F\in\mathcal F}(-1)^{|F\cap s|}\), for every \(s\in G\), satisfies \(W(s)\equiv2\pmod4\). The complete signed multiplier histogram, in the form `(value: multiplicity)`, is

`-22:640, -14:3840, -2:11520, 2:11520, 6:960, 10:384, 14:3840, 70:64`.

Thus \(T\) is invertible, its \(\ell^2\) condition number is \(35\), and the *exact operator norms of its unique inverse* are
\[
\|T^{-1}\|_{\ell^2\to\ell^2}=\frac12,\qquad
\|T^{-1}\|_{\ell^1\to\ell^1}=\|T^{-1}\|_{\ell^\infty\to\ell^\infty}=\frac{3691}{770}.
\]
Furthermore, the inverse convolution kernel is supported exactly on the \(512\) even-cardinality Eulerian edge sets of \(K_6\) and assumes precisely six nonzero rational values. The complete inverse-kernel table is given in the proof.

## Assumptions and scope
All graphs are simple and labelled; a two-factor is a spanning subgraph in which every vertex has degree exactly two. In particular, a pair of disjoint triangles is counted as one two-factor. Each of the fifteen undirected edges is a separate Boolean coordinate. In \(G\), addition means symmetric difference of edge sets. No normalization factor is included in \(T\). Fourier inversion itself uses the standard factor \(1/|G|=1/32768\); all \(\ell^p\) norms are on the counting-measure sequence spaces of this finite group. The theorem concerns \(K_6\) only.

## Proof
**1. Two-factor census.** Every simple two-regular graph is a disjoint union of cycles of lengths at least three. Six vertices permit either a single six-cycle or two triangles. The first class has \((6-1)!/2=60\) labelled members, and the second has \(\binom63/2=10\), so \(|\mathcal F|=70\).

**2. Nonvanishing for all signs.** Fix an edge \(e\). By vertex-transitivity and double-counting of \((e,F)\) with \(e\in F\), it belongs to exactly \(70\cdot6/15=28\) two-factors. For any set \(s\) of negative edges, expand
\[
W(s)=\sum_{F\in\mathcal F}\prod_{e\in s}(1-2\mathbf1_{e\in F}).
\]
Modulo four only the empty and singleton terms survive, giving \(W(s)\equiv70-2\cdot28|s|\equiv2\pmod4\). This proves invertibility independently of spectral enumeration. It also shows \(|W(s)|\ge2\). To see sharpness, choose the three negative edges \(\{01,03,12\}\); its directly checked signed two-factor sum is \(-2\).

**3. Exact signed multiplier census.** Enumerate the \(\binom{15}{6}=5005\) six-edge masks and retain those whose six vertex degrees all equal two. The resulting \(70\) indicator entries yield, under the \(15\)-stage exact-integer Walsh–Hadamard transform, exactly the signed histogram in the theorem. An independent enumeration constructs the \(60\) six-cycles by anchored permutations, plus the \(10\) unordered complementary pairs of three-subsets; the sets agree. For every one of the \(32768\) frequencies, direct summation over the independently constructed factors equals the transformed integer. The histogram also passes \(\sum_s W(s)^2=32768\cdot70\). The smallest multiplier magnitude is \(2\) and the largest is \(70\); hence the spectral assertions follow by Plancherel.

**4. The exact inverse kernel.** Let \(L=2310\), the least common multiple of all nonzero absolute multipliers. Put \(r(s)=L/W(s)\), which is always an integer. Fourier inversion gives
\[
h(x)=\frac{1}{32768L}\sum_{s\in G}r(s)(-1)^{|s\cap x|},\qquad T^{-1}g=h*g.
\]
The *complete* histogram for the integer numerator \(32768Lh(x)\) is:

| Integer numerator | Number of edge sets |
| ---: | ---: |
| \(-4718592\) | 10 |
| \(-655360\) | 180 |
| \(-65536\) | 240 |
| \(0\) | 32256 |
| \(393216\) | 16 |
| \(2048000\) | 60 |
| \(8798208\) | 6 |

These values come from a second exact Walsh transform and are independently checked by a \(512\)-character quotient computation. The absolute numerator sum is \(362840064\). Thus
\[
\sum_{x\in G}|h(x)|=\frac{362840064}{32768\cdot2310}=\frac{3691}{770}.
\]
For convolution on a finite group the \(\ell^1\) and \(\ell^\infty\) operator norms equal the absolute kernel sum: the triangle inequality gives the upper bound and a matched-sign test vector gives equality. The exact identity \(\mathbf1_{\mathcal F}*h=\delta_0\) is checked at all \(32768\) group elements using integer numerators.

**5. Structural support check.** Every \(F\in\mathcal F\) has even degree at each vertex and exactly six edges. Therefore \(W\) is invariant under addition of a cut vector, and also under addition of the all-ones edge vector. These generate a six-dimensional character-period subspace. Consequently, the inverse kernel is supported on its annihilator: the subgroup of even-degree, even-cardinality edge sets, of order \(2^9=512\). The exact histogram above has \(512\) nonzero entries and confirms there are no further zeros of the inverse kernel.

## Verification
Execute `python3 check_2factor6.py` with the supplied standalone source. It uses standard-library exact integers and fractions only. Its independent construction check, \(32768\) direct character sums, exact transform, Parseval check, quotient inverse transform, exhaustive convolution identity and inverse-kernel absolute sum must all pass. The output marker is `TWO_FACTOR_K6_EXACT_PASS`. The associated `CERTIFICATE.json` records the expected integer histograms and rational norm. A failed or incomplete run is not evidence for the theorem.

## Relationship to prior work
Classical two-factor theory studies the existence, decomposition, and prescribed-edge structure of spanning two-regular graphs. Aldred–Holton–Sheehan (2005) give prescribed/proscribed edge existence criteria; Alspach–Bryant–Horsley–Maenhaut–Scharaschkin (2014) and Pasotti–Pellegrini (2016) study two-factorizations of complete and multipartite graphs. These do not, in their inspected portions and relevant main statements, evaluate the signed edge-incidence Fourier transform or the endpoint norm of its inverse for all two-factors of \(K_6\). Baldridge–Lowrance–McCarty (2018) develop a different two-factor polynomial for planar trivalent graphs with a prescribed perfect matching, not the signed \(K_6\) transform here. A prior Hamiltonian-cycle-only Fourier nonvanishing theorem concerns a strict subfamily of the present \(70\) two-factors, excluding the ten disjoint-triangle members. Its congruence statement does not imply the claimed complete inverse-kernel histogram or norm.

## Limitations
The complete multiplier and inverse-kernel histograms are finite exact calculations for \(K_6\); they do not establish a family-wide norm formula for larger complete graphs. The congruence proof gives nonvanishing but does not alone yield the endpoint inverse norm: the histogram and integer certificate are needed. Literature comparisons were bounded and are not an exhaustive historical-priority certification. No independent external mathematical validation is claimed.

## References
1. R. E. L. Aldred, D. A. Holton, and J. Sheehan, *2-factors with prescribed and proscribed edges*, Journal of Graph Theory 49 (2005), 48–58. First online 25 February 2005. https://doi.org/10.1002/jgt.20065
2. B. Alspach, D. Bryant, D. Horsley, B. Maenhaut, and V. Scharaschkin, *On factorisations of complete graphs into circulant graphs and the Oberwolfach Problem* (2014). https://arxiv.org/abs/1411.6047
3. A. Pasotti and M. A. Pellegrini, *Cyclic uniform 2-factorizations of the complete multipartite graph* (2016). https://arxiv.org/abs/1603.06469
4. S. Baldridge, A. M. Lowrance, and B. McCarty, *The 2-Factor Polynomial Detects Even Perfect Matchings* (2018). https://arxiv.org/abs/1812.10346
