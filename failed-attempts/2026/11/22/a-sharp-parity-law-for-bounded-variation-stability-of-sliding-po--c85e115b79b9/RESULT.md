# A sharp parity law for bounded-variation stability of sliding population variance

## Finding
Let \(m\ge2\), \(n\ge2m\), and let \(a<b\). For an input sequence \(x\in[a,b]^n\), define the full-window population-variance operator \(W_{m,n}\) by
\[
 (W_{m,n}x)_i=\frac1m\sum_{r=0}^{m-1}\left(x_{i+r}-\frac1m\sum_{s=0}^{m-1}x_{i+s}\right)^2,
 \qquad 1\le i\le n-m+1.
\]
For any finite vector \(u\), set \(\operatorname{Var}(u)=\sum_{i}|u_{i+1}-u_i|\). The exact two-input variation Lipschitz *supremum* is
\[
\boxed{\sup_{\substack{x,y\in[a,b]^n\\\operatorname{Var}(x-y)>0}}
 \frac{\operatorname{Var}(W_{m,n}x-W_{m,n}y)}{\operatorname{Var}(x-y)}
 =(b-a)\frac{4\lfloor m^2/4\rfloor}{m^2}.}
\]
Consequently the sharp coefficient is \(b-a\) for even windows and \((b-a)(1-1/m^2)\) for odd windows. Thus on unit-range data every sliding population-variance map is nonexpansive for the variation *between two inputs*, with strict sharp contraction for each odd window width. The bound remains valid (not asserted sharp) for every \(m\le n<2m\). Sharpness means arbitrarily closely approached by finite pairs; no assertion of finite-pair attainment is made.

## Assumptions and scope
The signals are finite real paths, the windows have exactly \(m\) consecutive observations, no endpoint padding or periodic wrapping is applied, the variance divisor is \(m\) (not \(m-1\)), and all input coordinates lie in the *same* fixed interval \([a,b]\). Both input and output seminorms are the unweighted adjacent-difference total variation. The range restriction is essential: multiplying signal amplitudes by a factor \(c\) multiplies the operator's variation Lipschitz coefficient by \(|c|\).

## Proof
**1. Normalization and reduction to a single input jump.** Translation does not affect the output, while scaling by \(b-a\) multiplies its variance values by \((b-a)^2\); it therefore suffices to take \([a,b]=[0,1]\). The operator is quadratic and smooth. Its derivative kills constant vectors. For each \(1\le j<n\), let \(H^{(j)}\) be zero on positions at most \(j\) and one on the remaining positions. Every \(h\in\mathbb R^n\) decomposes as
\[
 h=h_1\mathbf1+\sum_{j=1}^{n-1}(h_{j+1}-h_j)H^{(j)}.
\]
Subadditivity of variation gives
\[
\operatorname{Var}(DW(z)h)\le\operatorname{Var}(h)
\max_{1\le j<n}\operatorname{Var}(DW(z)H^{(j)})
\]
for each \(z\in[0,1]^n\). Integrate the derivative along the segment from \(y\) to \(x\) to reduce the global two-input upper bound to those step directions.

**2. Exact local derivative packet.** Fix a jump between positions \(j\) and \(j+1\). A full window wholly on one side has derivative zero. For a window containing \(m-k\) samples on the left and \(k\) on the right, list the adjacent samples outward from the jump as \(L_1,L_2,\ldots\) on the left and \(R_1,R_2,\ldots\) on the right. Direct differentiation of the second central moment gives
\[
 g_k=(DW(z)H^{(j)})_{\mathrm{window}}=\frac{2}{m^2}h_k,\qquad
 h_k=(m-k)\sum_{r=1}^kR_r-k\sum_{s=1}^{m-k}L_s
\]
for \(1\le k\le m-1\), with \(h_0=h_m=0\). For a jump near a boundary, missing samples can be supplied by an arbitrary extension in \([0,1]\), and the actual derivative output is a consecutive subsequence of this full packet \((g_0,\ldots,g_m)\). Its variation cannot exceed the full-packet variation.

**3. A sharp sign-pair lemma.** For any \(L_s,R_r\in[0,1]\), the packet above satisfies
\[
\sum_{k=1}^m|h_k-h_{k-1}|\le2\left\lfloor\frac{m^2}{4}\right\rfloor.
\]
Indeed, by sign duality the left side is the maximum, over \(\sigma_1,\ldots,\sigma_m\in\{-1,1\}\), of \(\sum_{k=1}^m\sigma_k(h_k-h_{k-1})\). For fixed signs, the coefficients of \(R_b\) and \(L_a\) in this linear expression are respectively
\[
 \alpha_b=(m-b)\sigma_b-\sum_{k=b+1}^m\sigma_k,\qquad
 \beta_a=(m-a)\sigma_{m-a+1}-\sum_{k=1}^{m-a}\sigma_k.
\]
When \(\sigma_b=1\), \(\alpha_b\) is twice the number of later negative signs; otherwise it is minus twice the number of later positive signs. Similarly, \(\beta_a\) is twice the number of earlier negative signs if \(\sigma_{m-a+1}=1\), and nonpositive otherwise. Maximizing the linear expression over all \(L_a,R_b\in[0,1]\) is therefore exactly twice the number of *opposite-sign unordered index pairs*. If \(r\) of the \(m\) signs are positive, that number is \(r(m-r)\), at most \(\lfloor m^2/4\rfloor\). This proves the lemma and the global upper bound \(4\lfloor m^2/4\rfloor/m^2\).

**4. Matching finite-signal witnesses in the limiting sense.** Take \(n=2m\), jump \(j=m\), and binary baseline \(z\) with zero entries everywhere except the first \(q=\lfloor m/2\rfloor\) sites immediately to the right of the jump, where the entries are one. Every crossing window exists, with zero derivative at the two ends. Its integer packet becomes
\[
 h_k=(m-k)\min\{k,q\},\qquad 0\le k\le m.
\]
This is nonnegative and first increases, then decreases, with maximum \(q(m-q)=\lfloor m^2/4\rfloor\); hence its total variation is exactly \(2\lfloor m^2/4\rfloor\). The derivative-output variation is the claimed sharp constant. To realize this by permissible *pairs*, replace each zero coordinate of \(z\) by \(\varepsilon\), each one by \(1-\varepsilon\), obtaining \(z_\varepsilon\), and put
\[
 x=z_\varepsilon+\frac{\varepsilon}{2}H^{(m)},\qquad
 y=z_\varepsilon-\frac{\varepsilon}{2}H^{(m)},\qquad 0<\varepsilon<1/4.
\]
Both are in \([0,1]^{2m}\). Since \(W\) is quadratic, its symmetric secant identity is exact:
\[
 W(x)-W(y)=\varepsilon\,DW(z_\varepsilon)H^{(m)},\qquad
 \operatorname{Var}(x-y)=\varepsilon.
\]
Letting \(\varepsilon\downarrow0\) proves sharpness. For \(n>2m\), append zeros to the baseline far enough from the chosen jump; the same complete derivative packet occurs, so the lower bound persists. This completes the proof.

## Verification
The standalone file `verify_variance.py` independently recomputes full derivative packets for every binary chamber through window width eight, checks the sign-pair dual formula for all sign vectors through width eighteen, checks the extremizing packets through width eighty, tests 3,300 randomly generated input pairs, and verifies finite-pair approach to the bound through width forty-one. Run `python3 verify_variance.py`. Exhaustive finite checks are supplemental; the proof above establishes the statement for all widths and lengths in scope.

## Relationship to prior work
Local-variance computation is well established in signal and image processing. Wu and Chang (2015, §3.2, Eq. 9) compute local second central moments for image noise estimation. Tamburo's (2011) *Variance Image Filter* describes neighborhood-variance output and software, though its full manuscript was not available to inspect. These works provide the practical context, not a known bound on the two-input adjacent variation seminorm. The precise operator, its amplitude-normalized setting, the sign-pair extremality argument, and the even/odd sharp law are the subject here. Results for sliding standard deviations, medians, and moving averages do not imply the identity above: standard deviation is the square root of variance and has a different derivative and amplitude behavior. No claim of exhaustive historical priority is made.

## Limitations
The statement is an exact supremum, not a proof of attainment by distinct finite pairs. It does not establish the sharp constant for shorter signals \(m\le n<2m\), even though the same upper bound holds. It does not cover unbiased sample variance, variable or weighted windows, cyclic/extended boundaries, unbounded amplitudes, or higher-dimensional windows. The nearest historical neighborhood-variance implementation's manuscript remained inaccessible, leaving a residual literature-priority risk.

## References
1. Cheng-Ho Wu and Herng-Hua Chang, *Superpixel-based image noise variance estimation with local statistical assessment*, EURASIP Journal on Image and Video Processing 2015:38, published 28 November 2015, https://doi.org/10.1186/s13640-015-0093-2 (accessible article, especially §3.2).
2. Robert Tamburo, *Variance Image Filter*, Insight Journal, submission dated 5 January 2011, https://doi.org/10.54294/z4rl5e (landing-page abstract consulted; manuscript not inspected).
3. Peder Klith Bøcher and Keith R. McCloy, *The fundamentals of average local variance—Part I: Detecting regular patterns*, IEEE Transactions on Image Processing 15 (2006), 300–310, https://pubmed.ncbi.nlm.nih.gov/16479800/ (abstract consulted).
