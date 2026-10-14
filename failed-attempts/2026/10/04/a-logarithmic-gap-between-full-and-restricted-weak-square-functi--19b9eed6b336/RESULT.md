# A logarithmic gap between full and restricted weak square-function bounds

## Finding

Let \(S\) denote the dyadic square function on \([0,1)\). For a dyadic \(A_2\) weight \(w\), set
\[
S_{w^{-1}}g=S(w^{-1}g)
\]
and define
\[
C_{\mathrm{full}}(w)
=
\|S_{w^{-1}}\|_{L^2(w^{-1})\to L^{2,\infty}(w)}.
\]
Define the characteristic-input restricted weak constant by
\[
C_{\mathrm{res}}(w)
=
\sup_{\substack{E\subset[0,1)\\0<w^{-1}(E)<\infty}}
\frac{\|S_{w^{-1}}\mathbf 1_E\|_{L^{2,\infty}(w)}}
{\|\mathbf 1_E\|_{L^2(w^{-1})}}.
\]

There is an absolute constant \(c>0\) and a sequence of dyadic \(A_2\) weights \(w_j\) satisfying
\[
[w_j]_{A_2^d}\to\infty
\]
for which
\[
\frac{C_{\mathrm{full}}(w_j)}
{C_{\mathrm{res}}(w_j)}
\ge
c\sqrt{\log\!\bigl(1+[w_j]_{A_2^d}\bigr)}.
\]

In particular, characteristic-input restricted weak testing does not control the full weighted weak-\(L^2\) norm by any universal multiplicative constant. Along some weights, the transfer from restricted weak control to full weak control necessarily loses at least a square-root logarithm of the dyadic \(A_2\) characteristic.

## Assumptions and scope

The dyadic \(A_2\) characteristic is
\[
[w]_{A_2^d}
=
\sup_{I\in\mathcal D}
\langle w\rangle_I
\langle w^{-1}\rangle_I.
\]
The weak norm is
\[
\|h\|_{L^{2,\infty}(w)}
=
\sup_{\lambda>0}
\lambda\,w(\{|h|\ge\lambda\})^{1/2}.
\]

The multiplication map
\[
g\longmapsto w^{-1}g
\]
is an isometry from \(L^2(w^{-1})\) onto \(L^2(w)\), because
\[
\|w^{-1}g\|_{L^2(w)}^2
=
\int |g|^2w^{-1}.
\]
Therefore
\[
C_{\mathrm{full}}(w)
=
\|S\|_{L^2(w)\to L^{2,\infty}(w)}.
\]

The restricted constant is exactly the characteristic-input quantity studied in the earlier weighted square-function theorem. The result concerns this weighted restricted weak notion; it does not assert an analogous statement for every possible alternative definition of restricted type.

## Proof

A 2018 theorem of Ivanisvili, Mozolyako, and Volberg gives an absolute constant \(C_0\) such that every dyadic \(A_2\) weight satisfies
\[
C_{\mathrm{res}}(w)
\le
C_0\sqrt{[w]_{A_2^d}}.
\]

Osękowski's 2026 theorem states that for every prescribed \(c_0\ge1\), there is a dyadic \(A_2\) weight \(w\) with
\[
[w]_{A_2^d}\ge c_0
\]
and an \(f\in L^2(w)\) such that
\[
\|S(f)\|_{L^{2,\infty}(w)}
>
\frac{e^{-2}}{48}
\sqrt{
[w]_{A_2^d}
\log(1+[w]_{A_2^d})
}
\,\|f\|_{L^2(w)}.
\]
By the isometric reformulation above,
\[
C_{\mathrm{full}}(w)
>
\frac{e^{-2}}{48}
\sqrt{
[w]_{A_2^d}
\log(1+[w]_{A_2^d})
}.
\]

Dividing by the universal restricted weak estimate yields
\[
\frac{C_{\mathrm{full}}(w)}
{C_{\mathrm{res}}(w)}
>
\frac{e^{-2}}{48C_0}
\sqrt{\log(1+[w]_{A_2^d})}.
\]

Choose the prescribed lower thresholds \(c_0\) tending to infinity, and for each threshold choose a weight supplied by Osękowski's theorem. The resulting characteristics tend to infinity, and the displayed lower bound gives the claimed sequence.

If there were a universal \(K<\infty\) with
\[
C_{\mathrm{full}}(w)\le K C_{\mathrm{res}}(w)
\]
for every dyadic \(A_2\) weight, the ratio above would stay bounded, contradicting its divergence. Hence no universal restricted-to-full weak transfer constant exists.

## Verification

The argument uses two published inequalities with compatible normalization.

For the full weak norm, Osękowski defines the dyadic square function on \([0,1)\), uses the dyadic \(A_2\) characteristic, and proves the explicit lower constant
\[
e^{-2}/48
\]
multiplying
\[
\sqrt{[w]_{A_2^d}\log(1+[w]_{A_2^d})}.
\]

For the restricted weak norm, Ivanisvili, Mozolyako, and Volberg define
\[
S_{w^{-1}}=SM_{w^{-1}}
\]
and prove
\[
\|S_{w^{-1}}\mathbf 1_E\|_{L^{2,\infty}(w)}
\le
C_0\sqrt{[w]_{A_2^d}}
\|\mathbf 1_E\|_{L^2(w^{-1})}
\]
for every measurable \(E\).

The only new deduction is division of these two compatible estimates and selection of Osękowski weights with arbitrarily large characteristic. No interpolation, limiting argument, numerical experiment, or unproved lower estimate for the restricted constant is used.

## Relationship to prior work

The 2018 restricted-weak paper proved that characteristic inputs require no logarithmic correction and explicitly contrasted this with the then-best full weak upper estimate, which did contain a logarithm. At that time the logarithm in the full weak estimate was not known to be necessary, so an unbounded full-versus-restricted separation did not follow.

Osękowski's 2026 paper resolves that missing full weak sharpness question by constructing weights for which the logarithmic factor is necessary. Its paper studies the full weak norm and does not formulate the consequence for the restricted weak testing constant.

Combining the two statements shows that the critical logarithm is not merely a common feature of two estimates: it measures a genuine failure of characteristic-input restricted weak testing to capture the full weak norm.

A separate 2026 calibration of Osękowski's construction refines the numerical full-weak lower constant and the exact characteristic of that example. That refinement does not compare the full norm with restricted weak testing and is not needed for the present separation theorem.

## Limitations

The theorem proves a lower separation of order
\[
\sqrt{\log(1+[w]_{A_2^d})}
\]
along some weights. It does not prove a matching upper bound for the ratio on those same weights, because the universal restricted estimate is an upper bound rather than a same-weight lower asymptotic.

The result is specific to the critical weighted weak-\(L^2\) dyadic square-function setting and to the characteristic-input restricted notion used above.

No claim is made about continuous square functions, non-dyadic weights, or strong \(L^2\) norms.

## References

1. A. Osękowski, *On the weighted weak-type constant for the dyadic square function*, arXiv:2609.14430v1, 2026.
2. P. Ivanisvili, P. Mozolyako, and A. Volberg, *Strong weighted and restricted weak weighted estimates of the square function*, arXiv:1804.06869v3, 2018.
