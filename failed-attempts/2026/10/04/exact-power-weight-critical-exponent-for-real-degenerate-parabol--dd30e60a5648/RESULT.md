# Exact power-weight critical exponent for real degenerate parabolic Riesz theory

## Finding

Let
\[
n\ge1,
\qquad
-n<\beta<n,
\]
and set
\[
\omega_\beta(x)=|x|^\beta.
\]
Consider any real-coefficient degenerate parabolic operator
\[
\mathcal H
=
\partial_t-
\omega_\beta^{-1}\operatorname{div}_x(A\nabla_x)
\]
in the class of Baadi's 2026 theorem.

The lower resolvent exponent from that theory is exactly
\[
p_-(\mathcal H)=p_\beta,
\]
where
\[
p_\beta=
\begin{cases}
\dfrac{2n}{2n+\beta},&-n<\beta<0,\\[4pt]
1,&0\le\beta<n.
\end{cases}
\]
This value depends only on the power degeneracy and not on the particular real measurable coefficient matrix satisfying the structural hypotheses.

For negative powers, the threshold has an especially concrete interpretation: the dual measure
\[
d\mu_{p'}(x,t)=|x|^{\beta p'/2}\,dx\,dt
\]
is locally finite if and only if
\[
p>p_\beta.
\]
Thus the exact lower exponent coincides with the local-integrability wall built into the definition of \(p_-(\mathcal H)\).

The source Riesz-transform theorem therefore gives
\[
\mathcal R_{\mathcal H}
=
(\nabla_x\mathcal H^{-1/2},D_t^{1/2}\mathcal H^{-1/2})
:
L^p_{\mu_p}\to L^p_{\mu_p}
\]
for every
\[
p_\beta<p\le2.
\]
The dual reverse estimate from the same paper becomes explicit as well:
\[
\|\mathcal H^{1/2}u\|_{L^p_{\mu_p}}
\lesssim
\|\mathbb Du\|_{L^p_{\mu_p}}
\]
for all finite
\[
p\in
\begin{cases}
[2,-2n/\beta),&-n<\beta<0,\\
[2,\infty),&0\le\beta<n.
\end{cases}
\]

Finally, if
\[
2_*=\frac{2(n+2)}{n+4},
\]
then
\[
p_\beta=2_*
\quad\Longleftrightarrow\quad
\beta=-\frac{n^2}{n+2}.
\]
At this exact power, the weight fails to belong to
\[
RH_{1+2/n},
\]
yet still satisfies
\[
p_-(\mathcal H)=2_*.
\]
So, within the real-coefficient power family, the endpoint reverse-Hölder assumption used by the source as a sufficient condition for \(p_-\le2_*\) is not necessary.

## Assumptions and scope

The weighted measures are those of the source:
\[
d\mu_p(x,t)=\omega_\beta(x)^{p/2}\,dx\,dt.
\]
The matrix \(A=A(x,t)\) is real measurable and satisfies the weighted boundedness and accretivity assumptions relative to \(\omega_\beta\).

The restriction
\[
-n<\beta<n
\]
is exactly the power-weight \(A_2(\mathbb R^n)\) range.

The quantity \(p_-(\mathcal H)\) is the infimum exponent from the source definition based on uniform \(L^p_{\mu_p}\) resolvent boundedness together with local finiteness of the dual measure. It is not being redefined here.

The result identifies that invariant and then substitutes it into the source's proved Riesz-transform and reverse-inequality theorems. It does not assert weak type at the lower endpoint.

## Proof

The real-coefficient theorem in the primary source states that, for every
\[
1<q\le2,
\]
\[
p_-(\mathcal H)<q
\quad\Longleftrightarrow\quad
\omega_\beta\in RH_{q'/2}.
\]

First suppose
\[
-n<\beta<0.
\]
For a finite exponent \(s>1\), the power weight satisfies
\[
|x|^\beta\in RH_s
\quad\Longleftrightarrow\quad
\beta s>-n.
\]
Necessity follows because \(|x|^{\beta s}\) must be locally integrable at the origin. For sufficiency, consider a Euclidean ball \(B=B(x_0,r)\). If \(|x_0|\ge2r\), then \(|x|\) is comparable to \(|x_0|\) on \(B\), so the reverse-Hölder ratio is uniformly bounded. If \(|x_0|<2r\), then \(B\subset B(0,3r)\); radial integration gives
\[
\left(\fint_B|x|^{\beta s}\,dx\right)^{1/s}
\lesssim r^\beta,
\]
while, since \(\beta<0\) and \(|x|\le3r\) on \(B\),
\[
\fint_B|x|^\beta\,dx
\ge (3r)^\beta.
\]
This proves the reverse-Hölder estimate.

Taking
\[
s=\frac{q'}2=\frac{q}{2(q-1)},
\]
the condition \(\beta s>-n\) is equivalent to
\[
q>\frac{2n}{2n+\beta}=p_\beta.
\]
Hence the source equivalence gives
\[
p_-(\mathcal H)<q
\quad\Longleftrightarrow\quad
q>p_\beta.
\]
It follows that
\[
p_-(\mathcal H)=p_\beta.
\]

The same threshold is visible directly in the local-finiteness clause of the definition. Indeed,
\[
\mu_{p'}\text{ is locally finite}
\quad\Longleftrightarrow\quad
\frac{\beta p'}2>-n
\quad\Longleftrightarrow\quad
p>p_\beta.
\]
Thus no exponent below or at \(p_\beta\) can enter the defining set, while every exponent above it is admitted by the real-coefficient equivalence.

Now suppose
\[
0\le\beta<n.
\]
The primary source records
\[
|x|^\beta\in RH_\infty.
\]
Its real-coefficient theorem then gives
\[
p_-(\mathcal H)=1.
\]

The Riesz-transform range follows by inserting the exact value into the source boundedness theorem
\[
p\in(p_-(\mathcal H),2].
\]

For the reverse inequality, the adjoint operator \(\mathcal H^*\) has the same real-coefficient structure and the same power weight. Therefore
\[
p_-(\mathcal H^*)=p_\beta.
\]
The source duality corollary applies for
\[
2\le p<p_\beta'.
\]
When \(\beta<0\), direct algebra gives
\[
p_\beta'=-\frac{2n}{\beta},
\]
while for \(\beta\ge0\),
\[
p_\beta'=\infty.
\]
This proves the displayed explicit ranges.

Finally,
\[
\frac{2n}{2n+\beta}
=
\frac{2(n+2)}{n+4}
\]
is equivalent to
\[
\beta=-\frac{n^2}{n+2}.
\]
At that power,
\[
\beta\left(1+\frac2n\right)=-n,
\]
so \(|x|^{\beta(1+2/n)}=|x|^{-n}\) is not locally integrable at the origin. Hence
\[
|x|^\beta\notin RH_{1+2/n},
\]
even though the already proved formula gives
\[
p_-(\mathcal H)=2_*.
\]

## Verification

The full primary text was checked at the definition of \(p_-(\mathcal H)\), Theorem 1.2, the power-weight examples, the real-coefficient proof, Corollary 1.3, and the final endpoint questions.

The primary theorem gives the exact real-coefficient equivalence
\[
p_-(\mathcal H)<q
\iff
\omega\in RH_{q'/2},
\]
and explicitly lists the power weights
\[
|x|^\beta,
\qquad
-n<\beta<n.
\]
It does not state the closed formula for \(p_-(\mathcal H)\) above.

The algebraic phase diagram is replayed by the packaged checker. The reverse-Hölder membership itself is proved in the preceding argument rather than inferred numerically.

The source explicitly leaves weak-type estimates at \(p_-(\mathcal H)\) open except for a special spatial-gradient endpoint. Accordingly, no endpoint weak-type conclusion is included here.

## Relationship to prior work

Baadi's 2026 paper establishes the degenerate parabolic theory and proves the real-coefficient equivalence between the resolvent lower exponent and reverse-Hölder membership. Its introduction lists power weights and gives sufficient inequalities in \(\beta\) for prescribed \(q\), but does not solve those inequalities into a single exact formula for \(p_-(\mathcal H)\), identify the local-finiteness barrier with that exponent, or isolate the critical power where \(p_-=2_*\) despite failure of the endpoint reverse-Hölder hypothesis.

The preceding unweighted non-autonomous parabolic theory corresponds to \(\beta=0\) and therefore sees only the special value
\[
p_-=1.
\]
It does not contain the negative-power phase line.

Weighted elliptic Riesz-transform theory contains extensive results for Muckenhoupt and reverse-Hölder weights, but it does not by itself determine the invariant defined by the non-autonomous parabolic resolvent family used here.

Targeted searches using the exact source identifier, power-weight terminology, the formula for the critical exponent, and the equivalent reverse-Hölder phase boundary did not locate a published statement of this explicit real-parabolic power law.

## Limitations

The exact formula for \(p_-\) uses the real-coefficient equivalence. For complex coefficients, the source proves only upper bounds and the same formula is not asserted.

The displayed \(L^p\) Riesz-transform interval is the strong range proved by the source theorem after substituting the exact \(p_-\). The result does not prove failure of the Riesz transform below that interval.

Weak type at
\[
p=p_\beta
\]
remains open in the cases identified as open by the primary source.

The reverse-inequality interval is the explicit range supplied by the source duality corollary; no claim is made that it is the maximal possible range.

## References

1. K. Baadi, *A boundedness result for degenerate parabolic Riesz transforms with rough coefficients*, arXiv:2609.21949v1, 2026.
2. K. Baadi, M. Egert, and B. W. Kosmala, *\(L^p\) bounds for parabolic Riesz transforms with rough coefficients: The case \(1<p\le2\)*, arXiv:2607.05181v1, 2026.
3. P. Auscher and J. M. Martell, weighted elliptic Riesz-transform theory cited in the primary source.
