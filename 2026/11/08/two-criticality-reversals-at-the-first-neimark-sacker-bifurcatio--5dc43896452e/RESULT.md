# Two criticality reversals at the first Neimark–Sacker bifurcation of a five-site chiral logistic ring

## Finding

Consider the cyclic, antisymmetrically coupled five-site logistic system
\[
F_{r,a}(x)_j=H\!\left(r x_j[1-x_j+a(x_{j+1}-x_{j-1})]\right),\qquad j\pmod5,
\]
where \(H(y)=\min(1,\max(0,y))\), \(a>0\) and \(r>1\). Put
\[
k=\frac{\sqrt5-1}{2},\qquad u=\frac{5+\sqrt5}{2}a^2,\qquad r_c=1+\frac2{1+u}.
\]
The homogeneous fixed point \(x_j=1-1/r\) is linearly asymptotically stable for \(1<r<r_c\), and at \(r=r_c\) its first critical multipliers form one simple conjugate pair.

Its first Neimark–Sacker coefficient, normalized by the Fourier vector \(q_j=e^{2\pi i j/5}\), is
\[
\ell_1(u)=-\frac{(u+3)^2P(u)}{2(u+1)^2Q(u)},
\]
where
\[
P(u)=(10-9k)u^3+(18-30k)u^2+(11k-18)u+6,
\]
\[
Q(u)=5(1-k)u^2+(3k-2)u+1>0\quad(u\ge0).
\]
There are exactly two positive zeros of \(P\), and they satisfy
\[
u_-\in(1/2,3/4),\qquad u_+\in(5/4,3/2).
\]
For nonresonant \(u\) away from these two zeros, the first bifurcation is **subcritical** for \(u_-<u<u_+\), with a center-manifold-repelling small invariant Jordan curve on the stable-fixed-point side \(r<r_c\). It is **supercritical** for \(0<u<u_-\) or \(u>u_+\), with a locally attracting small invariant Jordan curve on the unstable-fixed-point side \(r>r_c\). Excluded strong resonances are \(u=1/3\) (1:3) and \(u=1\) (1:4). For example, \(a=1/2\) is nonresonant and strictly subcritical.

## Assumptions and scope

The assertions are local near the interior fixed point and concern precisely five sites on a directed cycle, with identical positive coupling \(a\). Indices are taken modulo five, and the state space is \([0,1]^5\). Because \(1-1/r\in(0,1)\), the clipping \(H\) is inactive in a sufficiently small neighborhood of the fixed point; all local derivatives below are those of the un-clipped polynomial map. The birth of invariant curves is asserted separately for each fixed nonresonant \(a\) with \(P(u)\ne0\); the size of the necessary parameter neighborhood need not be uniform as \(a\) approaches an excluded value. Repulsion in the subcritical case means the radial center-manifold direction; the other three directions are contracting.

## Proof

**Spectral threshold.** At the homogeneous fixed point, the Jacobian is \(J=(2-r)I+a(r-1)(S-S^{-1})\), where \(S\) is the forward cyclic shift. Its Fourier eigenpairs are
\[
q^{(m)}_j=e^{2\pi i m j/5},\qquad
\lambda_m(r)=2-r+2ia(r-1)\sin(2\pi m/5).
\]
For \(r>1\), the largest conjugate pair in modulus is \(m=\pm1\) because \(\sin^2(2\pi/5)>\sin^2(4\pi/5)\). Its modulus squared is
\[
(2-r)^2+u(r-1)^2.
\]
It crosses one at \(r_c=1+2/(1+u)\), with exact transverse derivative \(\left.\partial_r|\lambda_1|\right|_{r_c}=1\). The other three multipliers have strict modulus less than one there. Let \(\beta=\sqrt u\) and \(t=2/(1+u)\). At the threshold write
\[
\lambda=1-t+it\beta,\qquad
\lambda_2=1-t+itk\beta,\qquad k=2\cos(2\pi/5).
\]
The first multiplier has strong resonances \(\lambda^3=1\) exactly at \(u=1/3\) and \(\lambda^4=1\) exactly at \(u=1\); no others of orders one through four occur for finite \(u>0\).

**Nonlinear coefficient.** With \(B=D^2F\) at the fixed point, let \(q_j=e^{2\pi i j/5}\) and \(\langle p,q\rangle=1\) for \(p=q/5\) in the standard complex scalar product. The quadratic tensor is
\[
B(v,w)_j=r_c[-2v_jw_j+a\{v_j(w_{j+1}-w_{j-1})+w_j(v_{j+1}-v_{j-1})\}].
\]
A Fourier multiplication gives
\[
B(q,\bar q)=-2r_c\mathbf1,\qquad B(q,q)=2r_c(-1+i\beta)q^2.
\]
The second-order homological solutions (the inverses exist because the noncritical eigenvalues lie strictly inside the unit disk) are
\[
h_{11}=(I-J)^{-1}B(q,\bar q)=-\frac{2r_c}{t}\mathbf1,
\quad h_{20}=(\lambda^2I-J)^{-1}B(q,q)
=\frac{2r_c(-1+i\beta)}{\lambda^2-\lambda_2}q^2.
\]
Furthermore
\[
B(q,\mathbf1)=r_c(-2+i\beta)q,
\quad B(\bar q,q^2)=r_c[-2+i(k-1)\beta]q.
\]
The usual nonresonant discrete-time first Lyapunov coefficient is
\[
\ell_1=\frac12\operatorname{Re}\left\{\bar\lambda\langle p,B(\bar q,h_{20})+2B(q,h_{11})\rangle\right\}.
\]
There is no cubic derivative because the map is quadratic. Substituting these four tensor identities, rationalizing with \(\beta^2=u\) and \(k^2+k=1\), gives exactly the displayed \(\ell_1(u)\). The accompanying \(\texttt{VERIFY\_NS5.py}\) checks this reduction symbolically.

**Exactly two reversals.** The quadratic denominator \(Q\) has positive leading coefficient, positive value at zero and discriminant
\[
(3k-2)^2-20(1-k)=-\frac{13+\sqrt5}{2}<0;
\]
therefore it is strictly positive. The four exact sign tests are
\[
P(1/2)=\frac{69-25\sqrt5}{16}>0,\quad
P(3/4)=\frac{1671-795\sqrt5}{128}<0,
\]
\[
P(5/4)=\frac{7233-3245\sqrt5}{128}<0,\quad
P(3/2)=\frac{1503-651\sqrt5}{16}>0.
\]
The descending coefficient signs of \(P\) are \(+,-,-,+\), hence Descartes' rule bounds the number of positive zeros by two, counted with multiplicity. The sign tests produce two distinct roots in the stated rational intervals; thus there are exactly two, both simple, and \(P\) changes sign precisely at these roots. Since all other factors in \(\ell_1\) are positive, \(\ell_1>0\) exactly between the roots and \(\ell_1<0\) outside.

**Bifurcating invariant curves.** The nonresonant Neimark–Sacker theorem applies because the critical pair is simple, nonresonant through order four, crosses transversely and has nonzero cubic coefficient. A positive cubic coefficient gives an unstable radial invariant curve for \(r<r_c\) (subcritical); a negative coefficient gives an attracting invariant curve for \(r>r_c\) (supercritical). The other modes contract, and the curves lie in the clipping-inactive interior when \(r\) is sufficiently close to \(r_c\). For the explicit coupling \(a=1/2\), one has \(u=(5+\sqrt5)/8\) and
\[
P(u)=\frac{83-111\sqrt5}{128}<0,
\]
which rigorously gives the subcritical example.

## Verification

Run \(\texttt{python VERIFY\_NS5.py}\) with Python 3 and SymPy. The standalone script checks the golden-ratio reduction, the polynomial denominator and root-bracketing certificates, the equality of the exact Fourier normal-form formula with the rational expression, and independent substitutions at three rational coupling strengths. Numerical roots are corroborative; exact sign tests and Descartes' rule prove their completeness.

## Relationship to prior work

Baron and Galla, *The disordered logistic map* (arXiv:2609.24402v1, first public on 2026-09-21), develops interacting logistic systems and oscillatory instabilities, with emphasis on disordered couplings and statistical behavior. The present calculation applies its local dynamics to one explicit deterministic oriented five-cycle and determines nonlinear criticality, not merely spectral onset. Existing three-site calculations of the same cyclic rule prove uniformly supercritical behavior away from resonances; they do not imply the two five-site criticality reversals. Standard Neimark–Sacker theory supplies the bifurcation implication once the new coefficient is obtained and is not itself new. No claim of exhaustive historical priority is made.

## Limitations

There is no assertion at \(u=1/3\), \(u=1\), or the two roots of \(P\). In particular, a vanishing cubic coefficient does not prove a generalized Neimark–Sacker (Bautin) bifurcation without higher-order work. No global attraction, circle uniqueness away from the local center manifold, quasiperiodicity for every parameter, higher-period orbit classification, or extension to random coupling matrices is claimed. Related literature and the complete appendix of the motivating paper should be examined in independent priority review; some source access was restricted.

## References

1. J. W. Baron and T. Galla, *The disordered logistic map*, arXiv:2609.24402v1 (2026-09-21), https://arxiv.org/abs/2609.24402.
2. S. Mareno and L. English, *The effect of coupling on the dynamics of two coupled logistic maps*, International Journal of Differential Equations (2020), DOI:10.1155/2020/4103606.
3. Standard nonresonant Neimark–Sacker normal-form theorem (used solely as an established local bifurcation result).
