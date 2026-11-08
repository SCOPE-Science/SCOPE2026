# Exact Fourier spectrum and additive energy of the minimal parabolic Kakeya set

## Finding
Let \(q\) be any odd prime power, let \(F=\mathbb F_q\), and let \(S=\{t^2:t\in F\}\). Consider the parabolic Kakeya set
\[
K=\{(x,x^2-s):x\in F,\ s\in S\}\ \cup\ (\{0\}\times F).
\]
Then \(K\) contains an affine line of every direction and has the minimum possible cardinality \(|K|=(q^2+2q-1)/2\) for a planar Kakeya set over an odd field (the latter global minimum is an established theorem of Blokhuis--Mazzocca, not a new claim here).

Write \(\eta:F\to\{0,1,-1\}\) for the quadratic character, take any nontrivial additive character \(\psi:F\to\mathbb C\) and set
\[
G=\sum_{t\in F}\psi(t^2),\qquad \widehat{1_K}(u,v)=\sum_{(x,y)\in K}\psi(-ux-vy).
\]
The **complete Fourier transform** is
\[
\widehat{1_K}(u,v)=
\begin{cases}
|K|,&(u,v)=(0,0),\\
(q-1)/2,&v=0,\ u\ne0,\\
\dfrac{1+\eta(v)G}{2}\bigl(\eta(-v)G\psi(u^2/(4v))-1\bigr),&v\ne0.
\end{cases}
\]
In particular, the number \(E(K)\) of ordered quadruples \((a,b,c,d)\in K^4\) with \(a+b=c+d\) is exactly
\[
\boxed{16E(K)=
\begin{cases}
q^6+8q^5+21q^4+10q^3-35q^2-2q+13,&q\equiv3\pmod4,\\
q^6+8q^5+21q^4+14q^3+(8\eta(2)-39)q^2-14q+25-8\eta(2),&q\equiv1\pmod4.
\end{cases}}
\]
For the uniform probability measure \(\mu=1_K/|K|\), the same Fourier formula proves
\[
\max_{(u,v)\ne(0,0)}|\widehat\mu(u,v)|
\le \frac{(\sqrt q+1)^2}{q^2+2q-1}\le\frac2q.
\]
Thus this natural minimum-cardinality Kakeya set is *uniformly Salem* (or *strongly Salem* in the terminology distinguishing uniform measure from an arbitrary supporting measure). The novel finite invariant is the exact fourth Fourier moment, whose two branches distinguish both \(q\bmod4\) and, when \(q\equiv1\pmod4\), the character \(\eta(2)\).

## Assumptions and scope
The field cardinality is any odd prime power, including non-prime fields. The Fourier transform uses **unnormalized** sums and the character convention \(\psi(-ux-vy)\). In contrast, \(\widehat\mu\) is normalized by \(|K|\). The fourth moment is \(\sum_{u,v}|\widehat{1_K}(u,v)|^4=q^2E(K)\), with the factor \(q^2\) essential. These statements concern the specified parabolic set and its uniform measure, not every Kakeya set.

## Proof
**1. Geometry and size.** For each \(t\in F\), the full line \(\{(x,2tx-t^2):x\in F\}\) belongs to \(K\), because \(x^2-(2tx-t^2)=(x-t)^2\in S\). These lines have every nonvertical slope; the added line \(x=0\) has vertical direction. Since \(|S|=(q+1)/2\), every fiber at \(x\ne0\) contains exactly \((q+1)/2\) points and the fiber at zero contains \(q\), proving \(|K|=(q-1)(q+1)/2+q\). The known global lower bound for planar odd-order Kakeya sets is the same [2].

**2. Exact Fourier coefficients.** The elementary quadratic Gauss identities, for every \(v\ne0\), are
\[
\sum_{s\in S}\psi(vs)=\frac{1+\eta(v)G}{2}=:b_v,
\qquad
\sum_{x\in F}\psi(-vx^2-ux)=\eta(-v)G\psi(u^2/(4v)),
\]
where \(G^2=\eta(-1)q\) and \(|G|=\sqrt q\). The first identity follows because the squaring map has two preimages on nonzero squares, and the second by completing the square. For \(v\ne0\), the first (nonvertical) part of \(K\) has Fourier sum equal to the product of these two factors. Its contribution from \(x=0\) is \(b_v\), whereas the complete vertical fiber has Fourier sum \(\sum_{y\in F}\psi(-vy)=0\). Subtracting \(b_v\) proves the stated \(v\ne0\) formula. When \(v=0\) and \(u\ne0\), the nonzero fibers have equal size \((q+1)/2\), and therefore their character sum is \(-(q+1)/2\); adding the zero fiber of size \(q\) gives \((q-1)/2\).

**3. Summation of the fourth moment.** For \(v\ne0\), put \(a_v=\eta(-v)G\) and \(z_{u,v}=\psi(u^2/(4v))\). Then \(|a_v|^2=q\), \(|z_{u,v}|=1\), and
\[
\sum_u z_{u,v}=\eta(v)G,\quad
\sum_u z_{u,v}^2=\eta(2v)G,\quad
 a_v\sum_u z_{u,v}=q,\quad a_v^2=\eta(-1)q.
\]
Using the identity \(4\operatorname{Re}(w)^2=w^2+\overline w^{\,2}+2|w|^2\) in the expansion of \(|a_vz_{u,v}-1|^4\) yields
\[
\sum_{u\in F}|a_vz_{u,v}-1|^4
=q(q^2-3)+2\eta(-1)q\eta(2v)\operatorname{Re}(G).
\tag{1}
\]
The \(v=0\) contribution to \(\sum_{u,v}|\widehat{1_K}(u,v)|^4\) is \(|K|^4+(q-1)^5/16\).

When \(q\equiv3\pmod4\), \(G^2=-q\), so \(\operatorname{Re}(G)=0\) and \(|b_v|^4=(q+1)^2/16\). Equation (1) gives the entire contribution from \(v\ne0\):
\[
\frac{(q-1)q(q^2-3)(q+1)^2}{16}.
\]
When \(q\equiv1\pmod4\), \(G^2=q\) and \(G\) is real. Writing \(\epsilon=\eta(2)\), we have \(|b_v|^4=(q+1+2\eta(v)G)^2/16\) and \(\eta(2v)=\epsilon\eta(v)\). Among nonzero \(v\), the signs \(\eta(v)=\pm1\) each occur \((q-1)/2\) times. Averaging these two signs gives the contribution
\[
\frac{(q-1)q}{16}
\bigl((q^2-3)(q^2+6q+1)+8\epsilon q(q+1)\bigr).
\]
Add the \(v=0\) contribution, divide by \(q^2\) using fourth-moment orthogonality, and expand. This produces the two displayed integer polynomial formulas for \(E(K)\).

**4. Uniform Fourier decay.** For \(v\ne0\), the coefficient formula gives
\[
|\widehat{1_K}(u,v)|\le\frac{1+\sqrt q}{2}(\sqrt q+1)=\frac{(\sqrt q+1)^2}{2}.
\]
For \(v=0, u\ne0\) the magnitude is \((q-1)/2\), no larger. Dividing by \(|K|\) proves the first estimate on \(\widehat\mu\). The inequality \((\sqrt q+1)^2\le2q+2\), together with \(q\ge3\), proves the stated \(2/q\) estimate. Since \(|K|\asymp q^2\), this is the uniform-measure Salem exponent in dimension two.

## Verification
Run `python3 CHECK.py` using only the Python standard library. It builds the set directly from its definition, counts ordered pair sums with integers and compares the resulting additive energy against the formula for ten prime fields \(q=3,5,7,11,13,17,19,23,29,31\) and two genuine quadratic extension fields \(q=9,25\). For five small fields it also computes every Fourier coefficient by direct character summation and independently compares it to the proposed closed formula. The observed output begins `CHECK_OK independent_integer_energy_cases=12 independent_fourier_cases=5`. These are finite consistency tests; the proof above handles all odd prime powers.

## Relationship to prior work
Fraser [1], first public preprint dated May 14, 2025, proves that **every** finite-field Kakeya set supports **some** probability measure with Fourier decay \(q^{-1}\), while distinguishing this property from Fourier decay of the **uniform** measure. The present result treats the uniform measure of one specific extremal planar Kakeya set and supplies its full pointwise Fourier coefficients and exact fourth moment; Fraser's general existence theorem does not imply those explicit identities. Blokhuis and Mazzocca [2] establish the minimum odd-planar Kakeya cardinality and classify equality configurations using dual-oval geometry, but do not provide this Fourier-moment formula. General quadratic Gauss sum identities are established input, not new results. Published finite-field parabola Fourier-extension estimates concern functions supported on the one-dimensional parabola, not the two-dimensional union of tangent lines; their sharp fourth-moment constants do not determine \(E(K)\).

## Limitations
No claim is made that the uniform measure of **every** finite-field Kakeya set has the same decay. The classification of smallest Kakeya sets and the quadratic Gauss identities are pre-existing. The arithmetic formula is specific to the displayed parabolic realization, although affine changes preserve additive energy. The bound on the largest nonzero Fourier coefficient need not be the exact best constant for every field. Absolute priority cannot be excluded in older quadratic-Gauss or additive-energy calculations not discoverable under this terminology. No independent audit or outside certification is claimed.

## References
1. J. M. Fraser, *Fourier analytic properties of Kakeya sets in finite fields*, arXiv:2505.09464v1 (first posted May 14, 2025), subsequently *Bulletin of the London Mathematical Society* 58 (2026), e70367. https://arxiv.org/abs/2505.09464 ; https://doi.org/10.1112/blms.70367 .
2. A. Blokhuis and F. Mazzocca, *The Finite Field Kakeya Problem*, arXiv:0911.4370v1 (November 23, 2009), especially Example 2 and Proposition 7. https://arxiv.org/abs/0911.4370 .
3. Classical quadratic Gauss-sum evaluation and character orthogonality over finite fields (identities derived or stated explicitly above).
