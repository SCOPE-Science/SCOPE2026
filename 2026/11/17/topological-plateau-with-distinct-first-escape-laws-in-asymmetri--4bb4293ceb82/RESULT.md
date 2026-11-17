# Topological plateau with distinct first-escape laws in asymmetric negative doubling

## Finding
Let \(T(x)=-2x\bmod 1\) be negative doubling of the unit circle, represented by \([0,1)\). For every integer \(k\ge1\), introduce the nested asymmetric open holes
\[
H_k^{\rm w}=\left(\frac14,\frac12+2^{-(2k+1)}\right),\qquad
H_k^{\rm n}=\left(\frac14,\frac12+2^{-(2k+2)}\right).
\]
Here \({\rm w}\) and \({\rm n}\) denote the wider and narrower hole. Starting from normalized Lebesgue measure, define the first-entry index \(\tau_k^j(x)=\inf\{n\ge0:T^n x\in H_k^j\}\). Put \(t=z/2\) and
\[
D_k(t)=1-t-t^2+t^{2k+1}=(1-t^2)\left(1-\sum_{i=0}^{k-1}t^{2i+1}\right).
\]
Then \(\tau_k^j\) is almost surely finite and has the **exact all-time probability-generating function**
\[
\boxed{\mathbb E[z^{\tau_k^{\rm w}}]=\frac{(1-t^{2k})/4+(1+t)/2^{2k+1}}{D_k(t)},\qquad
\mathbb E[z^{\tau_k^{\rm n}}]=\frac{(1+t^{2k+1})/4+(1+t)/2^{2k+2}}{D_k(t)}.}
\]
Both functions are initially defined for \(|z|\le1\); their denominators are nonzero in a neighborhood of that closed disk after removable cancellations. In particular,
\[
\boxed{\mathbb E\tau_k^{\rm w}=\frac{4^{k+1}-1-6k}{4^k+2},\qquad
\mathbb E\tau_k^{\rm n}=\frac{4^{k+1}-1-3k}{4^k+2},\qquad
\mathbb E\tau_k^{\rm n}-\mathbb E\tau_k^{\rm w}=\frac{3k}{4^k+2}>0.}
\]
Yet the two holes have **identical one-sided symbolic infinite survivor subshifts**. Their physical survivor sets differ at most on countably many boundary/precritical points; in particular their topological entropies, exponential Lebesgue escape rates and Hausdorff dimensions coincide. Writing \(\lambda_1=1\), and for \(k\ge2\) denoting by \(\lambda_k\in(1,2)\) the unique root of
\[
\lambda_k^{2k-1}=\sum_{j=0}^{k-1}\lambda_k^{2j},
\]
these common invariants are, respectively,
\[
h_k=\log\lambda_k,\qquad \gamma_k=\log(2/\lambda_k),\qquad \dim_H=\log\lambda_k/\log2.
\]
The novel point is the paired **uniform finite-time escape law and explicit positive mean gap**, not the general phenomenon of entropy plateaux or the general existence of forbidden-word algorithms.

## Assumptions and scope
All parameters \(k\) are positive integers. Times are nonnegative integers and initial points are uniform on the unit circle. The critical point, hole endpoints and their preimages are a countable Lebesgue-null set and may be assigned either endpoint convention for the probabilistic statements. For the symbolic survivor claim use the natural binary branch coding; topological conclusions use the standard completed compact survivor definition. We do not equate every boundary point of the two literal open-hole survivors.

## Proof
**1. Bernoulli coding of a geometrically natural hole.** The two branches of \(T\) are affine of slope \(-2\) and map bijectively onto the full interval up to endpoints. The branch itinerary \(s_0s_1\ldots\), with \(s_i=0\) on \([0,1/2)\) and \(s_i=1\) on \([1/2,1)\), consists under Lebesgue measure of independent fair bits. Each depth-\(m\) cylinder has length \(2^{-m}\). The interval \((1/4,1/2)\) corresponds to the two-bit forbidden word \(A=00\). The right one-sided interval \((1/2,1/2+2^{-\ell})\) corresponds to the length-\(\ell\) word \(B_\ell\), starting with \(11\), then alternating \(0,1,0,1,\ldots\). For the wide and narrow holes use \(\ell=2k+1\) and \(\ell=2k+2\), respectively. The right cylinders can be verified directly from monotonic branch preimages. The fact that the holes are *unions* of these two unequal-length cylinders is essential.

**2. Renewal identities for competing forbidden words.** Let \(L\) be the first **completion time in bits**, with the initial bit read at time one, of either \(A\) or \(B_\ell\); let \(F_A(z)=\mathbb E[z^L;A\text{ completes first}]\) and \(F_B(z)=\mathbb E[z^L;B_\ell\text{ completes first}]\). The two patterns contain no occurrence of one another. The first completion is therefore also the first forbidden-word *start*, for which the start index is \(L-2\) on winner \(A\), or \(L-\ell\) on winner \(B_\ell\).

For patterns \(X,Y\), count the proper suffix/prefix matches of \(X\) and \(Y\). With \(t=z/2\) and \(q=1-z\), the renewal decomposition at the *first* completed pattern yields
\[
F_A K_{AA}+F_B K_{BA}=t^2/q,\qquad
F_A K_{AB}+F_B K_{BB}=t^\ell/q,
\]
where
\[
K_{AA}=1+t+t^2/q,\quad K_{AB}=t^\ell/q,
\]
\[
K_{BA}=\begin{cases}t+t^2/q,&\ell\text{ odd},\\t^2/q,&\ell\text{ even},\end{cases}\qquad
K_{BB}=\begin{cases}1+t^\ell/q,&\ell\text{ odd},\\1+t^{\ell-1}+t^\ell/q,&\ell\text{ even}.\end{cases}
\]
For completeness, these are the standard pattern-renewal equations: the unconditional probability of seeing \(Y\) ending at reading time \(m\) is \(2^{-|Y|}\); partition it by the earliest completed \(X\), then sum the possible compatible overlaps. Full non-overlapping continuations contribute the geometric term \(t^{|Y|}/q\). The only nontrivial proper overlaps are \(00\to00\) of length one, odd \(B\to00\) of length one, and even \(B\to B\) of length one. Multiplication by \(z^m\) and summation over \(m\) gives the displayed equations.

Solving their two-by-two system by elementary elimination gives, for \(\ell=2k+1\),
\[
F_A=\frac{t^2(1-t^{2k})}{D_k(t)},\qquad F_B=\frac{t^{2k+1}(1+t)}{D_k(t)},
\]
and for \(\ell=2k+2\),
\[
F_A=\frac{t^2(1+t^{2k+1})}{D_k(t)},\qquad F_B=\frac{t^{2k+2}(1+t)}{D_k(t)}.
\]
As \(\mathbb E[z^\tau]=z^{-2}F_A+z^{-\ell}F_B\), the two claimed rational generating functions follow. They are probability laws because every infinite Bernoulli sequence contains \(00\) almost surely. The denominator is nonzero for \(|z|\le1\): \(t\) then has modulus at most \(1/2\), while the finite sum of odd powers has modulus strictly less than one.

**3. Means and distinguishable right-side hits.** Differentiating the PGFs at \(z=1\) produces the exact mean formulas. Another direct calculation from \(F_B(1)\) shows
\[
\mathbb P(\text{first entry occurs through right side}\mid H_k^{\rm w})=\frac{3}{4^k+2},\quad
\mathbb P(\text{first entry occurs through right side}\mid H_k^{\rm n})=\frac{3}{2(4^k+2)}.
\]
Thus the positive mean difference is not a difference in eventual support: it measures unequal transient residence before a first visit to two nested holes.

**4. Exact symbolic plateau and spectral data.** The words obey \(B_{2k+2}=B_{2k+1}1\). If an infinite binary itinerary contains no \(00\), every occurrence of \(B_{2k+1}\) must be immediately followed by \(1\), since \(B_{2k+1}\) ends in \(0\). Therefore it contains \(B_{2k+2}\) at that position. The reverse implication is immediate. Hence avoiding \(\{00,B_{2k+1}\}\) and avoiding \(\{00,B_{2k+2}\}\) define exactly the same one-sided subshift. Passing to circle points may create only countable endpoint exceptions.

For \(k\ge2\), count avoidance words by the prefix automaton of the two forbidden patterns. Its nontrivial Perron factor is equivalently obtained from the renewal denominator
\[
1-\sum_{j=0}^{k-1}t^{2j+1};
\]
when the branch count grows as \(\lambda_k^n\), put \(t=1/\lambda_k\) to obtain \(1=\sum_{j=0}^{k-1}\lambda_k^{-(2j+1)}\). The corresponding primitive recurrent component has Perron root \(\lambda_k\in(1,2)\); for \(k=1\) the recurrent component has root one and only polynomial word growth. The repeated factor \((1-t^2)\) in \(D_k\) contributes possible boundary or periodic components but no larger exponential growth. The uniform branch cylinder lengths \(2^{-n}\) give entropy \(\log\lambda_k\), Hausdorff dimension \(\log\lambda_k/\log2\), and Lebesgue escape rate \(\log(2/\lambda_k)\). These standard graph-directed deductions are included to identify the precise topological plateau, not claimed as a new theorem independent of known open-map theory.

## Verification
The standalone standard-library Python checker `verify.py` constructs the finite forbidden-prefix automaton for \(00\) and \(B_\ell\). For every \(1\le k\le5\), both parity choices are tested by exact rational linear algebra for the winner probability and hitting-time mean. It separately iterates exact rational midpoints of all sufficiently fine binary cylinders through four time steps and compares the probabilities to the first five PGF coefficients. It checks \(B_{2k+2}=B_{2k+1}1\). Running `python verify.py` completed with `VERIFY_OK exact_rational_patterns=10 means=10 winning_probabilities=10 direct_time_probabilities=50`. These finite tests are diagnostics, not proofs for all \(k\); the renewal identities and symbolic argument above handle the full quantifiers.

## Relationship to prior work
Ding, Steiner and Sun [1] prove parity-sensitive admissibility and a general entropy/dimension devil's-staircase theory for negative doubling with holes \((a,b)\). This provides the natural motivation for studying *physical first-entry statistics inside* a common symbolic plateau; the plateau itself is not asserted novel. The available public abstract and initial HTML section, not the complete 47-page source, were accessible; full-text priority against that paper remains a material residual risk. A published exact symmetric-dyadic escape family [2] establishes multinacci finite-time survival and its mean for holes \((1/2-2^{-m},1/2+2^{-m})\), and explicitly excludes asymmetric holes from its scope. The present two asymmetric holes have fixed left endpoint \(1/4\), unequal forbidden lengths and equal infinite survivor languages, so neither symmetry nor a parameter substitution turns [2] into the present formula. Earlier symmetric-hole phase results [3] concern different parameter families. General pattern-overlap methods [4,5] underlie the renewal calculation and would allow a separate finite algorithm at each fixed \(k\); no novelty is claimed for those methods. The potentially new addition is the compact closed all-parameter pair of exact PGFs and their strictly positive mean gap on a natural topological plateau.

## Limitations
The result concerns one asymmetric dyadic hole family and normalized Lebesgue initial data. It does not classify arbitrary asymmetric holes, conditional late-survival distributions, or perturbations of the piecewise-linear map. Boundary survivor sets need an endpoint convention; exact countable equality is asserted for symbolic sequences, not every literal circle point. The classical renewal and Perron methods are not new. The primary 2026 47-page article could not be completely inspected in this review, so a previously published equivalent special-case hitting-time formula is a residual originality risk; the published abstract concerns survivor spaces and entropy rather than finite-time expectations. Independent verification has not been carried out.

## References
[1] Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327v1, first posted 2026-10-02, https://arxiv.org/abs/2610.03327 .
[2] *Exact multinacci escape statistics for symmetric dyadic holes of the negative-doubling map*, published mathematical finding (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-multinacci-escape-statistics-for-symmetric-dyadic-holes-of--c3e891785474 .
[3] *Exact escape-time phase transition for symmetric negative-doubling holes*, published mathematical finding (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-escape-time-phase-transition-for-symmetric-negative-doubli--ca3ad35b54de .
[4] L. J. Guibas, A. M. Odlyzko, *String overlaps, pattern matching, and nontransitive games*, Journal of Combinatorial Theory, Series A 30 (1981), 183–208.
[5] K. Jin, *Computing the Pattern Waiting Time: A Revisit of the Intuitive Approach*, ISAAC 2016, https://doi.org/10.4230/LIPIcs.ISAAC.2016.39 .
