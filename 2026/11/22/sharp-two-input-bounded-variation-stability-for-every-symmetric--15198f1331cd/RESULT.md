# Sharp two-input bounded-variation stability for every symmetric sliding trimmed mean

## Finding
For every integer \(r\ge1\), symmetric trimming level \(0\le q\le r\), and finite path length \(n\ge2r+2\), the centered sliding trimmed-mean filter \(T_{r,q}\), with repeated-endpoint extension, has the exact attained two-input total-variation Lipschitz coefficient
\[
\boxed{\displaystyle \sup_{V(x-y)>0}\frac{V(T_{r,q}x-T_{r,q}y)}{V(x-y)}=\frac{2r+1}{2r+1-2q}.}
\]
Here \(V(z)=\sum_{i=0}^{n-2}|z_{i+1}-z_i|\). The full coefficient cannot occur at any path length \(2\le n\le2r+1\). The result includes the moving mean at \(q=0\) and the running median at \(q=r\), but its intermediate-trim family and sharp mesh-size threshold are the substantive result.

## Assumptions and scope
Let \(x=(x_0,\ldots,x_{n-1})\in\mathbb R^n\), let \(w=2r+1\), and set \(k=w-2q\), a positive odd integer. Extend \(x\) by clamping: \(\widetilde x_j=x_0\) for \(j<0\), \(\widetilde x_j=x_{n-1}\) for \(j\ge n\), and \(\widetilde x_j=x_j\) otherwise. If the \(w\) samples \((\widetilde x_{i-r},\ldots,\widetilde x_{i+r})\) in nondecreasing order are \(a_{(1)},\ldots,a_{(w)}\), define
\[
(T_{r,q}x)_i=\frac1k\sum_{h=q+1}^{w-q}a_{(h)},\qquad 0\le i<n.
\]
Repeated sample occurrences count with multiplicity. The operator is continuous, piecewise linear, and translation equivariant. The seminorm quotient excludes \(V(x-y)=0\), which would give zero variation in the filtered difference as well.

## Proof
**Common-core lemma.** Consider two multisets of \(w\) labeled real observations which share \(w-1\) labeled occurrences, with just one occurrence replaced. Sort the \(w-1\) shared occurrences as \(b_1,\ldots,b_{w-1}\), breaking ties consistently. The middle \(k\) selected positions of either multiset necessarily include the same \(k-1\) shared occurrences
\[
b_{q+1},\ldots,b_{w-q-1}.
\]
Indeed, at most one extra entry may lie below or above any shared entry. Consequently, after trimming \(q\) observations at either end, the only possible additional selected occurrence is one of the two boundary shared observations or the newly supplied occurrence. Thus if each labeled occurrence carries a binary tag, the two sums of selected tags differ by at most one. This remains valid with duplicate values by fixed tie ordering, or by continuity from distinct values with identical tags on repeated endpoint copies.

**Universal upper bound.** Fix any generic vector \(z\), at which each window's ordering of distinct input values is locally constant. The directional derivative of \(T_{r,q}\) in a direction \(v\) is obtained by averaging the \(k\) selected coordinates of \(v\) in each window. Write
\[
v_i=v_0+\sum_{j=1}^{n-1}(v_j-v_{j-1})\,s^{(j)}_i,
\qquad s^{(j)}_i=\mathbf1_{\{i\ge j\}}.
\]
For a single step \(s^{(j)}\), the adjacent windows are related by removing one old labeled occurrence and inserting one new occurrence. The common-core lemma makes the difference of the two directional responses at most \(1/k\) on any edge. Further, the response equals zero if the whole window is left of the cut and equals one if the whole window lies right of the cut. Hence it can change on at most \(w\) edges. Its variation is therefore at most \(w/k\). Linearity of the directional derivative and the triangle inequality give
\[
V(DT_{r,q}(z)v)\le\frac wk V(v).
\]
On the segment \(z(t)=x+t(y-x)\), only finitely many ordering changes occur unless two coordinates tie identically. In the generic case integrate the piecewise-constant directional selection matrices and use convexity of \(V\):
\[
V(T_{r,q}y-T_{r,q}x)
\le\int_0^1 V(DT_{r,q}(z(t))(y-x))\,dt
\le\frac wk V(y-x).
\]
Continuity and approximation extend the inequality to all real inputs and ties. Translation equivariance resolves constant-difference directions.

**Sharpness simultaneously for all trimming levels.** First take \(n=w+1=2r+2\), with sites numbered \(0,\ldots,w\). Set
\[
x_i=2i\ (0\le i\le r),\qquad
x_{r+1+i}=2i+1\ (0\le i\le r),
\quad s_i=\mathbf1_{\{i\ge r+1\}}.
\]
For any \(0<\varepsilon<1\), the relative ordering of distinct values in every window stays unchanged upon replacing \(x\) by \(x+\varepsilon s\). Therefore the output difference is exactly \(\varepsilon c_i/k\), where \(c_i\) counts occurrences from the right half of the path among the middle \(k\) window ranks.

Put \(t=r-q+1\). For \(0\le i\le r\), the left endpoint value occurs \(r+1-i\) times and the right-half observations that appear are \(1,3,\ldots,2i-1\). The observation \(2j-1\) has sorted rank \(r+2j-i\) (one-based). Counting the ranks between \(q+1\) and \(w-q\) gives the exact integer formula
\[
c_i=\begin{cases}
i,&0\le i\le t,\\
t-((i-t)\bmod 2),&t<i\le r.
\end{cases}
\]
Thus \(|c_{i+1}-c_i|=1\) for \(0\le i<r\). Reflection of the data reverses values and exchanges the two half-path tags, giving \(c_{w-i}=k-c_i\). At \(i=r\), the window consists once each of the values \(0,1,\ldots,2r\). Its middle \(k\) consecutive values contain either \((k-1)/2\) or \((k+1)/2\) odd values, so \(|c_{r+1}-c_r|=|k-2c_r|=1\). Reflection gives unit changes on the remaining edges. Hence
\[
V(T_{r,q}(x+\varepsilon s)-T_{r,q}x)
=\frac{\varepsilon}{k}\sum_{i=0}^{w-1}|c_{i+1}-c_i|
=\frac{w\varepsilon}{k},\quad V(\varepsilon s)=\varepsilon.
\]
For any longer path, append copies of the last value \(x_w\) and the corresponding right-half tag. Repeated-endpoint extension means the first \(w+1\) filtered values are unchanged, and the universal upper bound forces the ratio to remain exactly \(w/k\).

**Earliest possible length.** Every output vector on a shorter path has only \(n-1\) edges. The common-core lemma bounds the difference of its adjacent directional step responses by \(1/k\) on each such edge, giving the stricter global upper bound \((n-1)/k<w/k\) whenever \(2\le n\le w\). Thus \(w+1\) is the minimum length at which the sharp all-length factor is attained.

## Verification
The standalone script `CHECKER.py` uses exact fractions to check the displayed extremizer and integer count formulas for every radius from \(1\) through \(30\) and all permitted trimming levels, including endpoint-extended paths. It also tests the common-core statement, exhaustive small-rank chambers, and random two-input inequalities. Execute with `python3 CHECKER.py` from the directory containing that file. The proof above, not finite enumeration, establishes all unbounded quantifiers.

## Relationship to prior work
Classical alpha-trimmed mean and order-statistic filtering is documented in Bednar–Watt (1984) and Pitas–Venetsanopoulos (1992). The latter's filtering formulas and discussion concern statistical robustness and edge preservation, not an exact two-input path-variation norm. Cai–Yang–Song (2018) use central trimmed filters in edge-preserving image restoration, without the claimed global seminorm classification. Earlier results on sliding medians and five-point cyclic trimmed means cover special cases or different boundary geometry, but do not imply the all-radius, all-trimming-level clamped-path formula or its minimal-length attainment. The novelty comparison is provisional because not all early original papers were accessible in full.

## Limitations
This is a two-input **difference** stability law for unweighted adjacent-edge total variation, not a one-input variation-diminishing statement. It applies to symmetric trimming of odd centered windows with endpoint clamping and finite real sequences. The exact coefficient for paths shorter than \(w+1\), nonuniform edge weights, cyclic extensions, asymmetric trimming, and adaptive trimming rules is not determined. Historical priority remains subject to inaccessible early full texts. The archival first-public date in the metadata pertains to a day-verified supporting publication, not to the original introduction of trimmed means.

## References
1. J. B. Bednar and T. L. Watt, "Alpha-trimmed means and their relationship to median filters," IEEE Transactions on Acoustics, Speech, and Signal Processing 32 (1984), 145–153. https://doi.org/10.1109/TASSP.1984.1164279
2. I. Pitas and A. N. Venetsanopoulos, "Order Statistics in Digital Image Processing," Proceedings of the IEEE 80 (1992), 1893–1921, especially Section III-C. https://web.eecs.utk.edu/~hqi/ece472-572/reference/order-statistics.pdf
3. M. Rashed, "Application of alternative seismic-stacking techniques to ringing noise removal from GPR data," Near Surface Geophysics 11 (first published 2013-02-01), 465–472. https://doi.org/10.3997/1873-0604.2013024
4. W. Cai, M. Yang, and F. Song, "Image filtering method using trimmed statistics and edge preserving," IET Image Processing 12 (2018), 1086–1094. https://doi.org/10.1049/iet-ipr.2017.0470
5. A. Restrepo and A. C. Bovik, "Adaptive trimmed mean filters for image restoration," IEEE Transactions on Acoustics, Speech, and Signal Processing 36 (1988), 1326–1337. https://doi.org/10.1109/29.1660
