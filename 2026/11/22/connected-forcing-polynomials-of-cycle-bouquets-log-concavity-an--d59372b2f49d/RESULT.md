# Connected-forcing polynomials of cycle bouquets: log-concavity and a sharp real-zero boundary

## Finding

The connected-forcing polynomial of every bouquet of at least two simple cycles has a positive, log-concave coefficient sequence on its support. These coefficients can be log-concave even when the polynomial has nonreal zeros: in this family the latter occurs exactly when some petal has length at least five. The log-concavity theorem is the focus here. We obtain the size enumerator from prior cactus forcing structure and use the cycle-factor root test shared with the cycle-spider calculation to give the exact contrast.

## Assumptions and scope

Take labelled cycles of lengths \(\ell_1,\ldots,\ell_r\ge3\), with \(r\ge2\), identifying one vertex of each cycle at a common hub \(h\). There are \(N=1+\sum_i(\ell_i-1)\) vertices, and other petal vertices remain distinct. A connected-forcing set is a nonempty set inducing a connected subgraph which colors the entire graph by the ordinary rule that a blue vertex with precisely one white neighbor may color it. Write \(Z_c(B;z)\) for the polynomial summing \(z^{|S|}\) over these sets. Log-concavity excludes degrees below the support.

## Proof

The hub and at least one peripheral vertex from each cycle are initially blue in any connected forcing set, as also follows from Brimkov's cut and block constraints [1, Lemma 2 and Proposition 3]. To see it directly, an entirely white peripheral path cannot receive a first force: the only external neighbor is the hub, which has two white neighbors in that path. Omitting the hub confines a connected initial set to one petal, leaving another path entirely white. With the hub initially blue, connectivity implies a selected prefix and/or suffix on each peripheral path, with either end allowed to be empty as long as the peripheral selection is nonempty. Conversely, any such set contains the hub and at least one neighbor on each petal, so it contains one of the minimum seeds constructed in [1, Proposition 6] (choose a hub neighbor independently from each outer cycle block). Zero forcing is monotone under adding blue vertices; a force in an old sequence either remains valid or is skipped because its target is already blue. Thus every set of the described form works.

For a proper peripheral selection of size \(s\), where \(1\le s\le\ell-2\), the arbitrary nonnegative prefix and suffix lengths summing to \(s\) give \(s+1\) distinct sets. There is just one full selection. Consequently
\[
P_\ell(z)=\sum_{s=1}^{\ell-2}(s+1)z^s+z^{\ell-1},\qquad Z_c(B;z)=z\prod_{i=1}^rP_{\ell_i}(z).
\]
The minimum size is \(r+1\) with \(2^r\) choices, and evaluation at one gives \(\prod_i\binom{\ell_i}{2}\).

The nonzero petal coefficient sequence is \((2,1)\) for \(\ell=3\), and \((2,3,\ldots,\ell-1,1)\) otherwise. At internal entries of the linear run, the adjacent log-concavity difference is one; the final turn satisfies \((\ell-1)^2>(\ell-2)\cdot1\). The classical convolution theorem [2] preserves log-concavity for finite nonnegative sequences with no internal zero. Iterating shows log-concavity for the bouquet, and the sum of the contiguous petal supports is a contiguous interval, so every coefficient from \(r+1\) to \(N\) is positive.

For comparison, \(P_3=z(z+2)\) and \(P_4=z(z+1)(z+2)\). The cycle-spider calculation [3] uses the same factor and excludes real-rootedness of \(P_\ell\) for \(\ell\ge5\). One can see this directly: if \(P_\ell/z\) had only real roots they would all be negative, by its positive coefficients and constant term. Its constant-normalized polynomial would factor as \(\prod_i(1+x_i z)\) with \(x_i>0\). The first two nonconstant coefficients would be \(\sum_i x_i=3/2\) and \(\sum_{i<j}x_i x_j=2\), which would force \((3/2)^2=\sum_i x_i^2+4>4\), a contradiction. Since the roots of the product include those of every factor, any petal of length at least five yields nonreal zeros despite the log-concavity of the whole bouquet.

## Verification and relation to prior work

`python3 CODE/bouquet_verify.py` exhaustively checks the connected forcing counts on the finite listed bouquets and checks arithmetic examples; the proof gives the unrestricted conclusions. Brimkov's general cactus minimum theorem and its proof supply the structural seeds; neither the enumerator's derivation from those seeds nor the shared single-cycle root obstruction is claimed independently new here. The earlier exact bouquet fort enumerator (Resultary record `47aae2192937`) counts forcing obstructions rather than the connected forcing coefficients. The log-concavity conclusion contrasts with the nonunimodal connected-forcing examples of Newton and Brimkov [4].

1. B. Brimkov, *Complexity and Computation of Connected Zero Forcing*, arXiv:1607.00658v1, Lemma 2, Propositions 3 and 6. https://arxiv.org/abs/1607.00658v1
2. O. Johnson and C. Goldschmidt, *Preservation of log-concavity on summation*, ESAIM Probability and Statistics 10 (2006), 206–215, DOI:10.1051/ps:2006008.
3. *Connected zero-forcing polynomials of cycle spiders and a sharp real-root transition*, Resultary record `eb162260c6ac`, cycle-factor calculation.
4. T. Newton and B. Brimkov, *Zero forcing is not unimodal*, arXiv:2611.11352. https://arxiv.org/abs/2611.11352
