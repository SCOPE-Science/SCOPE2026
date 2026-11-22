# Exact output and unique-decoding spectra of binary sliding-OR sensors

## Finding
For any integer window width \(h\ge2\), put \(n=m+h-1\), where \(m\ge1\). The binary sliding-OR observation of \(x\in\{0,1\}^n\) is the *ordered* \(m\)-bit vector \(T_h(x)=y\), with
\[
y_j=\bigvee_{t=j}^{j+h-1}x_t\qquad(1\le j\le m).
\]
Let \(R_h(m)=|T_h(\{0,1\}^n)|\) be the exact zero-error codebook size (one codeword per observation) and let \(U_h(m)\) count the observed vectors with exactly one preimage. Their complete all-width, all-length spectra are
\[
1+\sum_{m\ge1}R_h(m)z^m=\frac1{1-z}+\frac{z}{(1-z)((1-z)^2-z^{h+1})},
\]
\[
\sum_{m\ge1}U_h(m)z^m=\frac{z(1+z)^2}{1-z-z^{h+1}-z^{h+2}}.
\]
For each fixed \(h\ge2\), the proportion \(U_h(m)/R_h(m)\) decays exponentially with \(m\). More precisely, let \(\rho_R,\rho_U\in(0,1)\) be the unique positive solutions of
\[
(1-\rho_R)^2=\rho_R^{h+1},\qquad 1-\rho_U=(1+\rho_U)\rho_U^{h+1}.
\]
Then \(\rho_R<\rho_U\), and
\[
\frac{U_h(m)}{R_h(m)}=\Theta_h\!\left((\rho_R/\rho_U)^m\right).
\]
The image characterization and all preimage-list sizes appear in the proof; the displayed generating functions count *different outputs*, not source strings.

## Assumptions and scope
The source is a finite binary *linear* word with no padding, boundary wraparound, or input restrictions. Every consecutive window of width \(h\) contributes one Boolean hit/no-hit bit in its original position order. Output length \(m\ge1\), input length \(m+h-1\), and \(h\ge2\). An image word containing at least one zero is attainable exactly when every maximal one-run bounded on both sides by zero-runs has length at least \(h\). End one-runs are unrestricted. The all-one and all-zero outputs are always attainable. The formal constant coefficient \(1\) in the first generating function is a generating-series convention and is not a physical zero-window observation.

For a nonnegative integer \(d\), let \(c_h(d)\) be the number of compositions of \(d\) into parts from \(\{1,\ldots,h\}\), with \(c_h(0)=1\); for a negative argument set \(c_h(d)=0\). For \(a\ge1\), let \(g_h(a)\) be the number of binary words of length \(a-1\) with no run of \(h\) zeros, and put \(g_h(0)=1\). These are finite exact quantities.

## Proof
**1. Forced markers at a bounded one-run.** A one at input position \(t\) makes precisely output coordinates from \(\max(1,t-h+1)\) to \(\min(m,t)\) equal one. Consider an interior maximal one-run of output coordinates \(a,a+1,\ldots,b\) with zeros immediately outside it. Comparing the zero at \(a-1\) to the one at \(a\), the *only* newly entering input position is \(a+h-1\), which must contain one. Comparing the one at \(b\) with the zero at \(b+1\), the leaving input position \(b\) must contain one. No input ones may lie outside the interval \([a+h-1,b]\) while affecting this run. Therefore its length \(L=b-a+1\) must satisfy \(L\ge h\). Within the interval the two endpoints must be ones, and successive input ones must be at distance at most \(h\): precisely the compositions of \(L-h=b-(a+h-1)\) into parts between one and \(h\). The inverse-list factor is \(c_h(L-h)\).

**2. Boundary one-runs and independent factors.** Suppose an initial output one-run has length \(a>0\) and is followed by zero. Its rightmost required input marker is the one at input position \(a\); earlier input positions \(1,\ldots,a-1\) may be chosen freely subject only to containing no \(h\) consecutive zeros. Thus this boundary has \(g_h(a)\) admissible patterns. The trailing output one-run is symmetric. Every output zero forces its entire length-\(h\) input window to zero, so distinct one-runs have disjoint choices. Consequently, if \(y\) has at least one zero, leading/trailing one-run lengths \(a,d\ge0\), and interior one-run lengths \(L_1,\ldots,L_q\), then
\[
|T_h^{-1}(y)|=g_h(a)g_h(d)\prod_{i=1}^{q}c_h(L_i-h).
\]
An empty product is one. For the all-zero output the unique source is all zero; for the all-one output, the list comprises the binary input strings with no run of \(h\) zeros. These statements also establish the full image characterization.

**3. Unique fibers.** Every composition count \(c_h(d)\) equals one exactly for \(d=0\) or \(d=1\) when \(h\ge2\), and exceeds one for \(d\ge2\). Similarly, \(g_h(a)=1\) exactly for \(a=0\) or \(a=1\), and exceeds one for \(a\ge2\). The all-one output has at least two sources (all ones, or all ones except the last bit). Hence a *uniquely* decoded output is one containing zero, whose initial and final one-runs have length \(0\) or \(1\), with every interior one-run having length \(h\) or \(h+1\).

**4. Rational series.** Give a run of \(r\) bits the weight \(z^r\). Let \(Z=z/(1-z)\) represent a positive-length zero-run, \(E=1/(1-z)\) an arbitrary end one-run, and \(I=z^h/(1-z)\) an allowed positive interior one-run. Each realizable output containing at least one zero has the unique run grammar
\[
(\text{end-one})\,(\text{zero})\,[\,(\text{interior-one})(\text{zero})\,]^*\,(\text{end-one}).
\]
Its generating function is \(E^2Z/(1-IZ)=z/[(1-z)((1-z)^2-z^{h+1})]\). Adding all-one outputs at positive lengths gives \(z/(1-z)\), proving the first formula. For singleton lists, replace \(E\) by \(1+z\) and \(I\) by \(z^h+z^{h+1}\), obtaining \((1+z)^2Z/(1-(z^h+z^{h+1})Z)\), which simplifies to the second formula.

**5. Strict spectral gap.** Each denominator governing exponential growth has a unique simple positive root in \((0,1)\); the nonnegative run grammars have positive coefficients for all sufficiently large indices, so this is the unique dominant singularity, and their coefficient sequences have strictly positive leading exponential constants. Substituting \((1-\rho_R)^2=\rho_R^{h+1}\) into the singleton denominator gives
\[
1-\rho_R-(1+\rho_R)\rho_R^{h+1}=\rho_R^2(1-\rho_R)>0.
\]
The singleton denominator is strictly decreasing on \((0,1)\) and vanishes at \(\rho_U\), so \(\rho_U>\rho_R\). Since its leading constant is positive, the claimed exponential ratio follows. This is a strict discrepancy between the exponentially growing zero-error distinguishable-output population and the uniquely decodable-output population.

## Verification
The standalone standard-library-only script `verify.py` exhaustively enumerates all binary sources for \(h=2,3,4,5,6\), \(1\le m\le10\), with \(m+h-1\le16\): 50 width/length cases. For every output containing zero it compares the exact source fiber with the product formula. At each case it verifies the attainable-output count and singleton-fiber count against coefficients extracted independently from the rational generating functions. The checker prints `ALL PASS 50` upon successful completion. These finite checks stress-test boundary conventions; the proof above, not the computations, establishes the universal quantifiers.

## Relationship to prior work
Nguyen, Cai and Immink (2020) study sliding-window constrained binary codes, furnishing the motivating constrained coding perspective; their code constructions and lower-weight bounds do not enumerate the outputs of a Boolean OR measurement or all singleton inverse fibers. Sporring and Darkner (2022) investigate reconstruction from fully ordered binary window histograms, which retain exact ones counts, whereas the present Boolean OR measurement keeps only whether the count is positive. These observation maps are not equivalent, and a metameric-class formula for the finer histogram map does not provide the coarsened map's population counts directly.

Jen (1989) already established general transfer-recursion methods for preimage counting in elementary cellular automata, including a nearest-neighbor Boolean-OR rule (Rule 254). The case \(h=3\) is therefore related to classical CA preimages, and the present contribution is **not** a claim to have invented the local preimage concept or its general enumeration algorithm. The statements singled out here are the **all-window-width, all-output-length rational spectra** for attainable and singleton outputs, together with the strictly different exponential rates; the classical rule-specific formulas do not state these spectra or establish the uniform all-width comparison.

## Limitations
The result applies to noiseless, ordered, linear binary hit/no-hit observations with consecutive equal-width windows, not to unordered multisets, circular windows, arbitrary Boolean masks, threshold counts greater than one, noise, or higher-dimensional morphology. For each fixed width the coefficient asymptotics hold as output length tends to infinity; the estimates are not uniform in growing width. Historical priority is subject to equivalent unindexed or inaccessible literature; no independent mathematical audit has been performed.

## References
1. T. T. Nguyen, K. Cai, and K. A. S. Immink, *Efficient Design of Subblock Energy-Constrained Codes and Sliding Window-Constrained Codes*, arXiv:2009.09558, first posted 2020-09-21, https://arxiv.org/abs/2009.09558.
2. J. Sporring and S. Darkner, *Reconstructing Binary Signals from Local Histograms*, *Entropy* 24 (2022), 433, doi:10.3390/e24030433, https://www.mdpi.com/1099-4300/24/3/433.
3. E. Jen, *Enumeration of Preimages in Cellular Automata*, *Complex Systems* 3 (1989), 421–456, https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf.
