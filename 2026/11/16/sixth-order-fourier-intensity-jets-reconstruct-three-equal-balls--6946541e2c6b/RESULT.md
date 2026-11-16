# Sixth-order Fourier-intensity jets reconstruct three equal balls in every higher dimension

## Finding
Fix an integer \(d\ge2\). Let \(r>0\), let \(c_1,c_2,c_3\in\mathbb R^d\) be arbitrary, and define the **additive** three-ball signal
\[
 f(x)=\sum_{j=1}^{3}\mathbf1_{B(c_j,r)}(x),\qquad
 I(\xi)=\left|\int_{\mathbb R^d}f(x)e^{-i\xi\cdot x}\,dx\right|^2.
\]
The value \(I(0)\), the complete second differential \(D^2I(0)\), and the complete sixth differential \(D^6I(0)\) uniquely determine the common radius and the multiset of three centers up to common translation, inversion about a point, and permutation. This includes coincident centers, overlapping balls, collinear triples, and noncollinear triples. The complete fourth differential is a deterministic function of \(I(0)\) and \(D^2I(0)\). Moreover, even among noncollinear triples, no complete jet of order at most five is universally injective: **order six is sharp**.

For explicit reconstruction, let \(V=\sqrt{I(0)}/3\), recover \(r=(V/v_d)^{1/d}\), with \(v_d=\pi^{d/2}/\Gamma(d/2+1)\), and put \(B_r(\xi)=\widehat{\mathbf1_{B(0,r)}}(\xi)\). Near \(0\), form \(K(\xi)=I(\xi)/B_r(\xi)^2\). For every \(t\in\mathbb R^d\), write
\[
 K(st)=9+k_2(t)s^2+k_4(t)s^4+k_6(t)s^6+O_t(s^8).
\]
Then \(k_4(t)=k_2(t)^2/24\); the homogeneous polynomials
\[
 p_2(t)=-\frac{k_2(t)}3,\qquad
 p_3(t)^2=\frac{\tfrac{33}{2}p_2(t)^3+720k_6(t)}{18}
\]
are recovered from the stipulated intensity jet. There is a unique real homogeneous cubic \(p_3\), up to an overall sign, whose square equals the displayed sextic. Choosing either sign, factor
\[
 z^3-\frac{p_2(t)}2z-\frac{p_3(t)}3
 =\prod_{j=1}^3\bigl(z-t\cdot(c_j-\bar c)\bigr),\qquad
 \bar c=\frac{c_1+c_2+c_3}{3}.
\]
Its monic linear factors recover the centered vectors \(c_j-\bar c\), counting multiplicity. The other sign recovers their common negatives.

## Assumptions and scope
The balls are summed as indicator functions, not interpreted as the indicator of their union when they overlap. All amplitudes are exactly one and all radii are a common unknown positive number. Three centers count with multiplicity. The model class has exactly three such terms; neither unknown positive amplitudes nor differing radii are included. The complete tensors \(D^2I(0)\) and \(D^6I(0)\) mean all mixed partial derivatives in the angular Fourier convention \(e^{-i\xi\cdot x}\), not merely radial or coordinate-axis derivatives. Translation and simultaneous central inversion are physically unavoidable phase-retrieval symmetries. The statement concerns exact derivatives, not noisy sampled intensity values.

## Proof
**1. Recover the ball factor.** The unit-volume constant is \(v_d\), so \(I(0)=9v_d^2r^{2d}\) recovers \(r\). The real entire function \(B_r\) has \(B_r(0)=V>0\). Thus division by \(B_r^2\) is valid in a neighborhood of zero, and
\[
 K(\xi)=\sum_{j,\ell=1}^3e^{-i\xi\cdot(c_j-c_\ell)}.
\]
Writing \(z_j=c_j-\bar c\), we have \(\sum_jz_j=0\) and the differences are \(z_j-z_\ell\).

**2. Establish the moment identities.** Fix any real direction \(t\), write \(u_j=t\cdot z_j\), and define \(p_m=\sum_j u_j^m\) and \(M_m=\sum_{j,\ell}(u_j-u_\ell)^m\). Since \(\sum_j u_j=0\), Newton's identities give \(p_4=p_2^2/2\) and \(p_6=p_2^3/4+p_3^2/3\). Expanding \(M_m=\sum_{k=0}^{m}(-1)^k\binom mk p_{m-k}p_k\) with \(p_0=3\) and \(p_1=0\), one obtains
\[
 M_2=6p_2,\qquad M_4=9p_2^2,\qquad
 M_6=\frac{33}{2}p_2^3-18p_3^2.
\]
For example, \(M_6=6p_6+30p_2p_4-20p_3^2\), and substitution proves the last identity directly. Because \(K(st)=\sum_{j,\ell}\cos(s(u_j-u_\ell))\), its Taylor coefficients are \(k_2=-M_2/2\), \(k_4=M_4/24\), and \(k_6=-M_6/720\). The three displayed identities yield exactly the reconstruction formulas in the finding, including \(k_4=k_2^2/24\).

**3. Show the requested intensity derivatives suffice.** The known radial factor has the convergent expansion
\[
 \frac{B_r(st)}V=\sum_{m=0}^\infty
 \frac{(-1)^m(r|t|)^{2m}}{4^m m!(d/2+1)_m}s^{2m}.
\]
Here \((a)_m\) is the usual rising factorial. Write its square as \(1+q_2s^2+q_4s^4+q_6s^6+O(s^8)\), with all \(q_j\) known from \(r\) and \(|t|\). If \(h_j\) is the coefficient of \(s^j\) in \(I(st)/V^2\), then
\[
 k_2=h_2-9q_2,\qquad
 k_6=h_6-9q_6-q_4k_2-q_2k_2^2/24.
\]
The stipulated 0th, 2nd and 6th tensors determine \(h_2\) and \(h_6\) for every \(t\); the structural identity supplies the otherwise missing fourth coefficient. The same multiplication yields \(h_4=9q_4+q_2k_2+k_2^2/24\), proving that the *entire* fourth tensor is determined by lower-order data (by polarization of its diagonal form).

**4. Recover centers from two invariant polynomials.** The formulas determine the quadratic \(p_2(t)=\sum_j(t\cdot z_j)^2\) and the square of the cubic \(p_3(t)=\sum_j(t\cdot z_j)^3\) as polynomials in \(t_1,\ldots,t_d\). In the integral domain \(\mathbb R[t_1,\ldots,t_d]\), \(p_3^2=\widetilde p_3^2\) entails \(\widetilde p_3=p_3\) or \(\widetilde p_3=-p_3\), including the identically zero case. Because \(u_1+u_2+u_3=0\), elementary symmetric-polynomial identities give the monic cubic displayed in the finding. Unique factorization in \(\mathbb R[t_1,\ldots,t_d,z]\) recovers exactly the multiset of monic factors \(z-t\cdot z_j\). Thus centers agree up to permutation and translation, or to their common negatives followed by translation.

**5. Exhibit a strict fifth-order collision with noncollinear centers.** Embed the following two centered triples in the first two coordinates of any \(\mathbb R^d\):
\[
 C=\begin{pmatrix}2&-1&-1\\1&2&-3\end{pmatrix},\qquad
 C'=\begin{pmatrix}2/7&-13/7&11/7\\3&-2&-1\end{pmatrix}.
\]
Their column sums vanish; each has rank two. They have identical second-moment matrices \(CC^T=C'C'^T\), but their column multisets are neither identical nor common negatives. Indeed \(C'=CR\), where
\[
 R=\frac17\begin{pmatrix}3&-2&6\\6&3&-2\\-2&6&3\end{pmatrix},
 \quad R^TR=I_3,\quad R(1,1,1)^T=(1,1,1)^T.
\]
Consequently all \(p_2(t)\) and \(k_2(t)\), and by the identity all \(k_4(t)\), coincide for the two triples. With the same \(r>0\), their complete intensity jets through order five coincide; all odd derivatives vanish because intensity is even. Yet \(p_3(1,0)=6\) for \(C\), whereas \(p_3(1,0)=-858/343\) for \(C'\). The sixth-order jets differ because their squared cubic invariants differ. This proves the sharpness of six even among strictly noncollinear triples. (Taking \(r\) sufficiently small also makes the three balls in each configuration pairwise disjoint.)

## Verification
A portable Python 3 script `CHECK.py` performs exact rational checks of all three difference-moment identities on 343 integer triples, verifies both centered noncollinear witness matrices and their equal quadratic/quartic moments along 49 integer directions, and distinguishes their cubic invariants. Its recorded run prints `THREE_BALL_EXACT_MOMENT_CHECK_OK assertions=1133`. It uses only Python's standard library. The proof above, rather than finite tests, establishes the claims for every \(d\ge2\) and every real parameter.

## Relationship to prior work
Xia and Xu (2026) investigate full Fourier-magnitude phase retrieval for one-dimensional finite unions of intervals, including general three-interval nonuniqueness. A separately published 2026 finite-jet classification shows that three **disjoint equal-width intervals in one dimension** have a sixth-order local reconstruction and fourth-order redundancy. The latter is a close conceptual precedent. It does **not** cover arbitrary noncollinear triples of Euclidean balls, the multivariate polarization and cubic-polynomial sign argument, or overlapping additive ball signals. In particular, projecting a Euclidean ball to a line gives a smooth radial marginal, not an indicator of an interval, so its hypotheses do not directly apply. The result here supplies a sharp multivariate all-configuration theorem and a noncollinear collision witness.

Huang and Dokmanić (2018) study reconstruction from complete unassigned pairwise distance distributions on the line or a loop, not from truncated multivariate Fourier-intensity derivatives. General discrete point-source autocorrelation methods suggest the full-data context; the sharp sixth-order tensor conclusion is substantially more specific. An exact older higher-dimensional three-point moment theorem could nevertheless dominate the present finding; this is an explicit originality risk.

## Limitations
The signal is an **additive** sum of three unit-density equal-radius balls; overlapping balls are not a set-theoretic union. The radius and number of balls are unknown only within this fixed model class. No claim is made for differing radii, weights, arbitrary shapes, noisy jets, or stable inversion near configurations with coincident centers. The proof concerns mathematical uniqueness, not a numerically robust factorization algorithm. Originality is assessed relative to the cited and inspected sources, not certified publication priority. Independent audit has not been performed.

## References
1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855, first publicly submitted 2026-06-18. https://arxiv.org/abs/2606.19855
2. Shuai Huang and Ivan Dokmanić, *Reconstructing Point Sets from Distance Distributions*, arXiv:1804.02465, first publicly submitted 2018-04-06. https://arxiv.org/abs/1804.02465
3. Published 2026 study, *Sixth-order Fourier-intensity recovery for three equal-width intervals*. A primary statement and its proof were inspected for comparison. Its one-dimensional equal-interval hypotheses are different from the higher-dimensional ball model here.
