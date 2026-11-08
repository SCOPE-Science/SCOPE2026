# Planar graph Gabor measurements: exact operator spectrum and phase fibres

## Finding
Let \(q\ge3\) be an odd prime power, let \(K=\mathbb F_q\), and let \(f:K\to K\) be planar: for every \(a\ne0\), the map \(x\mapsto f(x+a)-f(x)\) permutes \(K\). On \(G=K\times K\), use the window \(g=\mathbf1_{\Gamma_f}\), where \(\Gamma_f=\{(x,f(x)):x\in K\}\). Form all \(|G|^2=q^4\) time-frequency shifts of this window and their complex-linear rank-one-projector analysis map \(\mathcal L_g\).

The full (including zero) singular-value multiset of \(\mathcal L_g\), with the counting of shifts and modulations and with unnormalized \(g\), is
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity}\\\hline
q^2&1\\
q^{3/2}&q(q-1)\\
q&q^3(q-1)\\
0&(q-1)(q^2+1).
\end{array}
\]
In particular, the exact complex rank is \(q^4-q^3+q^2-q+1\), and the positive-spectrum condition number is \(q\).

Write each signal as a collection of vertical-fibre vectors \(s_x=(s(x,y))_{y\in K}\). Let \(k(s)\) be the number of nonzero fibre vectors. The complete nonzero-signal phase-retrieval classification (comparison with **all** complex signals, not only a prescribed support class) is:

1. If \(k(s)\ge3\), the full intensity measurements determine \(s\) up to global phase.
2. If \(k(s)=2\), with nonzero fibres at \(i,j\), uniqueness fails exactly when both have constant nonzero coordinate moduli, \(|s(i,y)|^2=A\) and \(|s(j,y)|^2=B\) for every \(y\in K\), with \(A\ne B\). In that case there are exactly two phase orbits: the original, and the amplitude-exchanged partner whose fibre vectors are \(\sqrt{B/A}\,s_i\) and \(\sqrt{A/B}\,s_j\).
3. If \(k(s)=1\), uniqueness holds exactly when \(s\) has one nonzero coordinate. For a one-fibre signal, all independent coordinatewise phase changes preserve its measurements; a signal of constant nonzero coordinate modulus on a full fibre can additionally be moved to any other full fibre without changing its measurements.

The zero signal is uniquely determined. Consequently, all signals with at most one nonzero coordinate per vertical fibre are uniquely phase retrievable, without knowing their supports. In contrast, the complete linear operator lift has a kernel of dimension \((q-1)(q^2+1)\).

## Assumptions and scope
Choose any nontrivial additive character \(\psi:K\to\mathbb C\) of modulus one and identify the character group of \(G\) with \(G\) by \(\chi_{r,s}(x,y)=\psi(rx+sy)\). Define \((T_a h)(z)=h(z-a)\), \((M_\omega h)(z)=\chi_\omega(z)h(z)\), and \(g_{a,\omega}=M_\omega T_a g\), for every \(a,\omega\in G\). On the full complex matrix space \(\operatorname{End}(\mathbb C^G)\), endowed with the Hilbert--Schmidt norm, set
\[
\mathcal L_g(H)_{a,\omega}=\operatorname{tr}(H g_{a,\omega}g_{a,\omega}^{*}),
\qquad
\mathcal M_g(s)=\mathcal L_g(ss^*).
\]
All signals, frames, and matrices in the claim use these unnormalized conventions. A phase orbit consists of all multiples by scalars of modulus one. No group structure or quadratic-polynomial hypothesis on \(f\) beyond planarity is used.

## Proof
**1. Ambiguity magnitudes.** For translation \(a=(u,v)\) and modulation \(\omega=(r,s)\), put \(A_g(a,\omega)=\langle g,M_\omega T_a g\rangle\). Its summation support consists of graph points satisfying \(f(x)-f(x-u)=v\). When \(u\ne0\), planarity gives exactly one solution for each \(v\), so \(|A_g(a,\omega)|=1\), for **every** \(\omega\). When \(u=0\), \(v\ne0\), the two graph supports are disjoint, so \(A_g=0\) at every modulation.

For \(a=0\), the ambiguity is, up to complex conjugation,
\[
S(r,s)=\sum_{x\in K}\psi(rx+sf(x)).
\]
If \(s=0\), this equals \(q\) for \(r=0\) and zero otherwise. If \(s\ne0\), character orthogonality and the planarity permutations yield
\[
|S(r,s)|^2=\sum_{h\in K}\psi(rh)
 \sum_{x\in K}\psi\bigl(s(f(x+h)-f(x))\bigr)=q.
\]
The \(h=0\) inner sum equals \(q\); every \(h\ne0\) inner sum is zero. Hence the four ambiguity strata are exactly \(q\) once, \(\sqrt q\) on \(q(q-1)\) indices, \(1\) on \(q^3(q-1)\) indices, and \(0\) on \((q-1)(q^2+1)\) indices.

**2. Lifting spectrum and kernel.** The Weyl matrices \(M_\omega T_a\), normalized by \(|G|^{-1/2}\), form an orthonormal Hilbert--Schmidt basis of \(\operatorname{End}(\mathbb C^G)\). The Fourier transform in all translation/modulation measurement indices conjugates \(\mathcal L_g\) to diagonal multiplication by \(\sqrt{|G|}\,A_g(a,\omega)\), up to unimodular factors and permutations of the Weyl basis. Thus its singular values are \(q|A_g(a,\omega)|\). This gives the asserted full spectrum, rank, nullity, and positive-spectrum condition number.

The same Fourier diagonalization describes the kernel exactly. For \(H\in\ker\mathcal L_g\), all matrix entries \(H_{(x,y),(x',y')}\) with \(x\ne x'\) vanish: all corresponding displacements have nonzero first coordinate and every ambiguity multiplier is nonzero. At zero displacement, the only missing modulation frequencies are \((r,0)\) with \(r\ne0\). Hence the diagonal must have the form \(H_{(x,y),(x,y)}=c_x\), independent of \(y\), with \(\sum_{x\in K}c_x=0\). Conversely, within-fibre off-diagonal entries, where \(x=x'\) and \(y\ne y'\), are arbitrary, and these diagonal conditions are sufficient. The complex dimension is \(q\,q(q-1)+(q-1)=(q-1)(q^2+1)\).

**3. Exact phase fibres.** Suppose \(\mathcal M_g(s)=\mathcal M_g(t)\), so \(H=ss^*-tt^*\) belongs to the kernel just described. For every pair of different first coordinates, its off-fibre blocks vanish:
\[
s_xs_{x'}^*=t_xt_{x'}^*\quad(x\ne x').
\]
The diagonal conditions become
\[
|s(x,y)|^2-|t(x,y)|^2=c_x\quad\text{for every }y,
\qquad\sum_xc_x=0.
\]
If \(s\) occupies at least two fibres, the nonzero cross-blocks force \(t\) to occupy exactly the same fibres. Equality of each nonzero rank-one cross-block forces \(t_x=z_xs_x\), with nonzero complex \(z_x\) and \(z_x\overline{z_{x'}}=1\) for all distinct active fibres. With three or more active fibres, these relations force every \(z_x\) to be the same unimodular constant.

With exactly two active fibres, the relations give, after one common phase adjustment, \(z_i=r>0\) and \(z_j=r^{-1}\). If \(r\ne1\), the diagonal equations force \(|s(i,y)|^2=A\) and \(|s(j,y)|^2=B\) to be constant and positive for all \(y\), and their zero-sum condition is
\[
(1-r^2)A+(1-r^{-2})B=0.
\]
It reduces to \(r^2=B/A\). Thus a nontrivial second phase orbit exists exactly when \(A\ne B\); conversely the stated swap makes the off-fibre blocks and diagonal conditions identical and is therefore a genuine ambiguity. If \(A=B\), only \(r=1\) is possible.

With one active fibre, \(t\) can occupy at most one fibre, because every cross-block of \(ss^*\) vanishes. If it occupies the same fibre, the diagonal kernel condition forces coordinatewise equal moduli, and relative phases are unconstrained. If it occupies another fibre, both fibres must have a constant nonzero squared modulus, equal by \(\sum_xc_x=0\). This is possible precisely for a full, flat-modulus one-fibre signal. A one-coordinate signal is therefore unique up to phase; any one-fibre signal with at least two nonzero coordinates admits independent phase changes. Finally, summing the intensities over all time-frequency indices gives \(|G|\|g\|_2^2\|s\|_2^2\), so only the zero signal has all intensities zero.

## Verification
The standalone executable `verify_planar_gabor.py` uses the planar polynomial \(f(x)=x^2\) over prime fields. It explicitly computes all ambiguity coefficients for \(q=3,5,7\), checks every magnitude against the four strata, and checks the exact rank/nullity count. At \(q=3\) it separately constructs the full \(81\times81\) complex lifting matrix and checks every singular value against the theoretical multiset. Direct intensity calculations confirm both a two-fibre amplitude-exchange ambiguity and a one-fibre phase ambiguity. The script prints `PLANAR_GABOR_SPECTRUM_AND_PHASE_CHECKS_OK` on success. The universal claims are proved above; finite checks neither establish nor replace the universal result.

## Relationship to prior work
Planar functions and the forbidden-subgroup relative difference sets they define are classical; Zieve (2013) treats planar polynomial families, while Pott--Schmidt--Zhou (2014, Definition 4.3 and Proposition 4.4) establish the exact relative-difference-set correspondence. The Fourier consequence of planarity is standard in that setting.

Bojarovska--Flinth (2015, Section 2 and Theorems 2.1--2.4) establish the fundamental Gabor/Weyl lifting multiplier representation and general phase-retrieval criteria. Bojarovska--Paternostro (2015) study Gabor fusion frames for **ordinary difference sets** and their mutual coherence, not the forbidden-subgroup relative-difference-set phase-retrieval fibres here. The structural input from all these works is acknowledged, not claimed as new. The present claim is the all-planar-function **complete nonlinear phase-fibre classification**, together with the resulting explicit operator spectrum and kernel. Its phase-orbit bifurcation (one-, two-, and three-fibre cases, including the exact amplitude swap) is not stated in the inspected sources. More general unlocated classification results remain a possible priority risk.

## Limitations
The analysis uses every translation and modulation over the full group, and does not classify recovery from subsampled measurements or provide a global inverse stability constant. It does not claim informational completeness of the linear lift: its nonzero kernel is essential to the phenomenon. The full result is limited to odd finite fields and planar functions, not arbitrary nonlinear graphs or even-characteristic modified planar constructions. The scientific originality comparison is bounded, and no independent validation is claimed.

## References
1. M. E. Zieve, *Planar functions and perfect nonlinear monomials over finite fields*, arXiv:1301.5004v1 (January 21, 2013).
2. A. Pott, K.-U. Schmidt, Y. Zhou, *Semifields, relative difference sets, and bent functions*, arXiv:1401.3294v1 (January 14, 2014).
3. I. Bojarovska, A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (March 19, 2015).
4. I. Bojarovska, V. Paternostro, *Gabor fusion frames generated by difference sets*, arXiv:1507.01829v1 (July 7, 2015).
