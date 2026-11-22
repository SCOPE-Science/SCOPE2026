# A degree-independent right-half-plane root staircase for connected zero forcing on one-long-arm spiders

## Finding

For integers \(r\ge3\) and \(h\ge1\), let \(S_{r,h}\) be the tree with one vertex (the hub) of degree \(r\), exactly \(r-1\) length-one arms, and one arm of length \(h\) edges. It has \(r+h\) vertices. Its connected zero-forcing polynomial, with the number of admissible initially blue connected sets of each size as coefficients, is

\[
Z_C(S_{r,h};z)=z^r Q_{r,h}(z),\qquad Q_{r,h}(z)=z^h+r\sum_{j=0}^{h-1}z^j.
\]

**Theorem (complex-root census).** The degree-\(h\) factor \(Q_{r,h}\) has no imaginary-axis roots, and exactly

\[
N_+(r,h)=2\left\lfloor\frac h4\right\rfloor
\]

roots in the open right half-plane, counted with multiplicity. Therefore the nonzero roots of \(Z_C\) all have negative real part exactly for \(h\le3\). For every \(h\ge4\), there is at least one conjugate pair in the open right half-plane, independently of the number of short arms.

**Theorem (negative-real census).** The polynomial \(Q_{r,h}\) has no positive real roots. For odd \(h\), it has exactly one simple negative real root. For even \(h\), the count of negative real roots with multiplicity is:

| Long-arm length | Number of negative real roots |
| --- | --- |
| \(h=2\), \(r=3\) | \(0\) |
| \(h=2\), \(r=4\) | \(2\), one double root at \(-2\) |
| \(h=2\), \(r\ge5\) | \(2\), both simple |
| \(h=4\), \(r=3\) | \(0\) |
| \(h=4\), \(r\ge4\) | \(2\), both simple |
| Even \(h\ge6\), \(r\ge3\) | \(2\), both simple |

Apart from the single double root above, all nonzero roots are simple. Together the two censuses also determine the number of nonreal roots in the open left half-plane.

## Assumptions and scope

All graphs are finite, undirected and simple. Initially blue vertices must induce a connected nonempty subgraph, and a blue vertex with exactly one white neighbor may force it blue. Every vertex must eventually become blue. Each root is counted with algebraic multiplicity. The \(r\) extractions of the root \(z=0\) from the generating polynomial are excluded from the complex-root census. No claim is made here for trees with two or more long arms or for arbitrary tree forcing polynomials.

## Proof

**1. Exact combinatorial reduction.** Every connected zero-forcing set contains the hub: if it did not, its blue vertices would lie in a single arm, and upon any later forcing of the hub at least two other arms would remain completely white, making further forcing impossible. Every initially blue arm portion is a connected prefix from the hub, and at most one arm may be initially unseeded. Conversely, any such choice is zero forcing: all seeded prefixes propagate to their leaves, after which the hub can force the one omitted arm. If the long arm is omitted, all \(r-1\) short leaves must be present (one set of size \(r\)). If the long arm has a blue prefix of length \(\ell\in\{1,\ldots,h\}\), there are \(r-1\) options omitting exactly one short leaf (size \(r-1+\ell\)) and one option taking all short leaves (size \(r+\ell\)). Therefore

\[
Z_C=z^r+(r-1)\sum_{\ell=1}^{h}z^{r-1+\ell}+\sum_{\ell=1}^{h}z^{r+\ell}
=z^r\left[z^h+r\sum_{j=0}^{h-1}z^j\right].
\]

This coefficient identity is a specialization of the independently published general tree formula; it is included to make the root proof self-contained and does not itself constitute the new claim.

**2. Imaginary-axis exclusion.** Set

\[
F_{r,h}(z)=(z-1)Q_{r,h}(z)=z^h(z+r-1)-r.
\]

We have \(Q_{r,h}(0)=r>0\) and \(Q_{r,h}(1)=1+rh>0\). For \(z=it\) with nonzero real \(t\), the imaginary part of \((it)^h(r-1+it)\) is \(\pm t^{h+1}\) when \(h\) is even, and \(\pm(r-1)t^h\) when \(h\) is odd. Since \(r>1\), it never vanishes. Thus \(Q_{r,h}\) has no root with zero real part for any real parameter \(r>1\).

**3. Exact right-half-plane count.** Regard \(r>1\) as a real parameter. Polynomial roots vary continuously as a multiset; Step 2 shows that their right-half-plane count cannot change. Divide by \(r\) and let \(r\to\infty\):

\[
r^{-1}Q_{r,h}(z)=\sum_{j=0}^{h-1}z^j+r^{-1}z^h.
\]

Of its \(h\) zeros, \(h-1\) tend to the distinct nontrivial \(h\)-th roots of unity \(\zeta\), and the last tends to \(-\infty\) along the real line (from the sum of roots \(-r\), with the bounded roots summing to \(-1+o(1)\)). Non-imaginary limit roots have the same limiting half-plane. If \(4\mid h\), the two roots tending to \(\zeta=\pm i\) require their first-order shifts. The implicit-function expansion at each such root is

\[
z_r=\zeta-\frac{\zeta(\zeta-1)}{hr}+O_h(r^{-2}),
\]

because the derivative of \(\sum_{j=0}^{h-1}z^j\) at \(\zeta\ne1\) equals \(h\zeta^{h-1}/(\zeta-1)\). For \(\zeta=\pm i\), the real part of the correction is \(+1/(hr)\), so **both** limiting imaginary roots approach from the right half-plane. Counting the nontrivial roots of unity with positive real part and adding these two boundary roots when present gives exactly \(2\lfloor h/4\rfloor\). By half-plane invariance the same count holds for every integer \(r\ge3\), and strict Hurwitz stability holds precisely when this count is zero, namely \(h=1,2,3\).

**4. Negative real roots and multiplicities.** All coefficients of \(Q_{r,h}\) are positive, so there are no nonnegative real roots. For \(z=-t\) with \(t>0\), the root equation becomes

\[
(-1)^h t^h(r-1-t)=r.
\]

For odd \(h\), it is \(t^h(t-r+1)=r\), which has exactly one solution on \(t>r-1\), by strict monotonicity. For even \(h\), negative roots correspond to intersections

\[
t^h(r-1-t)=r,\qquad 0<t<r-1.
\]

The left side has a unique maximum

\[
M_h(r)=\frac{h^h(r-1)^{h+1}}{(h+1)^{h+1}}
\]

at \(t=h(r-1)/(h+1)\). Its ratio \(M_h(r)/r\) is strictly increasing in \(r>1\), because its logarithmic derivative is \((h+1)/(r-1)-1/r>0\). For \(h=2\), the ratio is below one at \(r=3\), equals one at \(r=4\), and exceeds one thereafter. For \(h=4\), it is below one at \(r=3\) (\(M_4(3)=8192/3125<3\)), and already exceeds one at \(r=4\) (evaluate the left side at \(t=2\) to get \(16>4\)). For every even \(h\ge6\) and \(r\ge3\), evaluating at \(r=3\), \(t=3/2\), gives at least \((3/2)^6/2=729/128>3\); monotonicity in \(r\) completes the classification. The one tangency is \((h,r)=(2,4)\), where \(Q_{4,2}(z)=(z+2)^2\). Finally, \(F'_{r,h}(z)=z^{h-1}((h+1)z+h(r-1))\); a multiple nonzero root must be that tangency, so all other nonzero roots are simple.

## Verification

Run `python verify.py` with Python 3 and NumPy. The script directly enumerates the connected zero-forcing sets on 32 small labelled brooms, independently reconstructs their full polynomials, then computes the roots of 240 parameter instances covering \(1\le h\le24\) and \(3\le r\le12\). The output ends with `VERIFY_OK`. These checks are finite corroboration; the all-parameter result follows from the four proof steps above. The test is numerical for root locations and uses a small tolerance, so it is not an independent exact root certificate.

## Relationship to prior work

Mukherjee and Ray (arXiv:2611.10985, first posted November 7, 2026 UTC) prove a general connected zero-forcing polynomial for arbitrary finite trees, including a starlike specialization. Thus the coefficient identity for \(Q_{r,h}\) is already covered by their theorem and is **not** asserted to be new. The present proposed contribution is the analytic complex-root half-plane count, degree-independent sharp stability cutoff and complete real-root multiplicity phases; these require the separate zero-free imaginary-axis argument, homotopy to cyclotomic roots and signed-real analysis above. Newton and Brimkov (arXiv:2611.11352, posted November 8, 2026 UTC) show that general connected forcing polynomials can fail unimodality, but do not study this broom-root location claim. General polynomial root-location principles are classical and are not claimed as new.

## Limitations

The historical priority of the precise root census has not been independently certified. The polynomial family is elementary and may have been studied under a purely algebraic name; an equivalent classical root-location result would supersede the novelty claim. No claim is made about root geometry for all trees or for more than one long arm. Independent mathematical audit has not been performed.

## References

1. S. Mukherjee and P. Ray, *On the connected zero forcing polynomial of finite trees*, arXiv:2611.10985 (initial public posting 2026-11-07 UTC), https://arxiv.org/abs/2611.10985.
2. T. Newton and B. Brimkov, *Zero forcing is not unimodal*, arXiv:2611.11352 (initial public posting 2026-11-08 UTC), https://arxiv.org/abs/2611.11352.
3. NIST Digital Library of Mathematical Functions, §1.11, *Zeros of Polynomials*, https://dlmf.nist.gov/1.11 (classical root notation and background only).
