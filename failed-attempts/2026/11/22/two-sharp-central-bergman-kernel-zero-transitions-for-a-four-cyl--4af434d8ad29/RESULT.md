# Two sharp central Bergman-kernel zero transitions for a four-cylinder intersection

## Finding
For every real \(p>0\), put
\[
D_p=\left\{(z,w_1,w_2,w_3,w_4)\in\mathbb C^5:
 |z|^{2p}+|w_j|^2<1\quad(1\le j\le4)\right\}.
\]
Let \(K_p\) be the unweighted Bergman kernel of \(D_p\), with ordinary Euclidean volume measure. On the axial slice \((z,0,0,0,0),(w,0,0,0,0)\), set \(t=z\overline w\), so \(|t|<1\). The number \(N(p)\) of zeros of this kernel on the scalar product disk, counted with multiplicities, is exactly
\[
\boxed{N(p)=\begin{cases}
2,&0<p<\tfrac14,\\
1,&\tfrac14\le p<\sqrt{2/3},\\
0,&p\ge\sqrt{2/3}.
\end{cases}}
\]
The only parameters at which a zero occurs on \(|t|=1\) are \(p=\tfrac14\) and \(p=\sqrt{2/3}\). At either parameter the unique boundary zero is \(t=-1\), and it is simple. Thus \(D_p\) is not a Lu Qi-Keng domain whenever \(0<p<\sqrt{2/3}\). The absence of axial zeros for larger \(p\) does **not** establish that \(D_p\) is globally zero-free.

## Assumptions and scope
The result concerns all real \(p>0\), exactly four independent transverse disks and one axial variable. All zeros are counted in the open scalar disk \(|z\overline w|<1\); products on its boundary are not attained by two points of \(D_p\). The term *axial kernel* means \(K_p((z,0,0,0,0),(w,0,0,0,0))\), not the kernel with arbitrary transverse coordinates. The normalization is the Lebesgue measure \(dV\) on \(\mathbb C^5\), with area \(\pi\) for the planar unit disk.

## Proof
**1. Exact axial kernel from monomial norms.** The domain is bounded, complete Reinhardt, and its square-integrable holomorphic monomials are orthogonal and complete. Integration of the four transverse variables gives the axial monomial norm
\[
\|z^n\|^2=\pi^4\int_{|z|<1}|z|^{2n}(1-|z|^{2p})^4\,dA(z)
=\frac{\pi^5}{p}B\left(\frac{n+1}{p},5\right)
=\frac{24\pi^5p^4}{\prod_{j=0}^4(n+1+jp)}.
\]
Therefore
\[
K_p((z,0),(w,0))=\frac{1}{24\pi^5p^4}
\sum_{n=0}^{\infty}\prod_{j=0}^4(n+1+jp)t^n
=\frac{Q_p(t)}{24\pi^5p^4(1-t)^6},
\]
where \(Q_p(t)=\sum_{j=0}^{4}q_j(p)t^j\), with
\[
\begin{aligned}
q_0&=(p+1)(2p+1)(3p+1)(4p+1),\\
q_1&=-2(p-1)(p+1)(2p+1)(24p+13),\\
q_2&=6(p-1)(p+1)(24p^2-11),\\
q_3&=-2(p-1)(p+1)(2p-1)(24p-13),\\
q_4&=(p-1)(2p-1)(3p-1)(4p-1).
\end{aligned}
\]
These identities follow directly by expressing the degree-five polynomial in \(n\) in falling-factorial powers and summing \(\sum_{n\ge0}(n)_kt^n=k!t^k/(1-t)^{k+1}\). The denominator of the kernel has no zeros for \(|t|<1\).

**2. A quartic half-plane problem.** The Cayley map \(t=(u-1)/(u+1)\) sends the open right half-plane \(\Re u>0\) bijectively to \(|t|<1\). Direct expansion gives
\[
H_p(u)=(u+1)^4Q_p\left(\frac{u-1}{u+1}\right)
=120u^4+480pu^3+120(7p^2-1)u^2
 +160p(5p^2-2)u+8(16p^2-1)(3p^2-2).
\]
Zeros of \(Q_p\) in the disk correspond exactly to zeros of \(H_p\) in the right half-plane, with their multiplicities.

**3. Exact exclusion of any other boundary passage.** For \(u=i\omega\), \(\omega\in\mathbb R\), the imaginary part is
\[
\Im H_p(i\omega)=160p\omega(5p^2-3\omega^2-2).
\]
If \(\omega\ne0\), it is necessary that \(\omega^2=(5p^2-2)/3>0\). Under this condition the real part becomes
\[
\Re H_p(i\omega)=-\frac{32}{3}(4p^2-1)(16p^2-1),
\]
which cannot vanish because \(p^2>2/5\). At \(\omega=0\), the identity
\[
H_p(0)=Q_p(-1)=8(16p^2-1)(3p^2-2)
\]
shows the only positive boundary-crossing parameters are \(1/4\) and \(\sqrt{2/3}\). At these parameters, the derivatives of \(Q_p\) at \(-1\) are respectively \(-135/4\) and \(320\sqrt6/9\), so the boundary zeros are simple.

**4. Counting roots in the open half-plane.** Away from the exceptional Routh pivots, the first column of the standard quartic Routh array for \(H_p\) is exactly
\[
120,\quad480p,\quad40(16p^2-1),\quad128p(4p^2-1),
\quad8(16p^2-1)(3p^2-2).
\]
For a real polynomial having no imaginary-axis root, the number of right-half-plane roots counted with multiplicity is the number of sign changes in this column. The signs give two roots for \(0<p<1/4\), one for \(1/4<p<1/2\), one for \(1/2<p<\sqrt{2/3}\), and none for \(p>\sqrt{2/3}\). At \(p=1/2\) the Routh pivot degenerates, but the polynomial has no imaginary-axis zeros by Step 3; continuity of roots gives one right-half-plane root there. At the two boundary parameters, a single simple root lies on the boundary, so the open-half-plane counts are respectively one and zero. The announced formula follows.

**5. Domain implication.** Each \(|t|<1\) can be written as \(z\overline w=t\) with \(|z|,|w|<1\), by choosing both moduli \(\sqrt{|t|}\) and appropriate phases. Hence each axial scalar zero produces a genuine off-diagonal Bergman-kernel zero for two points of \(D_p\). This proves the non-Lu-Qi-Keng consequence, without making the unwarranted converse assertion.

## Verification
The companion `VERIFY.py` recomputes the numerator from the monomial generating function (not from a hardcoded list), checks every coefficient, reconstructs the Cayley quartic, verifies the two Routh pivots, the imaginary-axis exclusion and boundary derivatives symbolically, and computes exact sign-change counts at rational representatives \(p=1/10\), \(p=2/5\), and \(p=1\). Running `python VERIFY.py` with SymPy must return a `PASS` message. These computations verify identities; the all-parameter zero classification is furnished by Steps 3-4, not by sampling.

## Relationship to prior work
Perälä's *Vanishing Bergman kernels on the disk* (first posted 17 March 2017) proves existence results and general finiteness facts for zeros of radial weighted disk kernels; it does not calculate the exact \((1-r^{2p})^4\) family or these parameter thresholds. Park's study of intersections of cylindrical domains supplies general high-dimensional monomial norms and a Lauricella representation, as well as the zero-free \(p=1\) subfamily; it does not enumerate the axial zeros for four cylinders and variable \(p\). Beberok's earlier two-cylinder formulas and the zero-free \(p=1\) multi-cylinder family provide relevant boundary cases, but neither implies the two distinct interior zero-loss thresholds for variable \(p\). The weighted Jacobi and Euclidean-distance Bergman-kernel transitions studied elsewhere involve different radial moment families; a holomorphic equivalence reducing those families to \((1-r^{2p})^4\) is not established. The new contribution here is the exact all-parameter zero census and boundary simplicity, not the existence of a monomial expansion.

## Limitations
This is a statement only on the axial two-point kernel, not a complete Lu Qi-Keng classification of \(D_p\) for \(p\ge\sqrt{2/3}\). It does not classify zero locations individually within the disk, beyond their number and the boundary crossing. Algebraic root counting and the stated Routh array are over exact real parameters; `VERIFY.py` does not certify an infinite parameter range by numerical sampling. Priority against unindexed equivalent results is not independently established.

## References
1. A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976v1, 17 March 2017, https://arxiv.org/abs/1703.05976.
2. J.-D. Park, *The Bergman kernel function for intersections of some cylindrical domains and Lauricella's hypergeometric function*, Journal of Mathematical Analysis and Applications 504 (2021), 125398, https://doi.org/10.1016/j.jmaa.2021.125398, especially Sections 2 and 6.
3. T. Beberok, *The Bergman kernel: explicit formulas, deflation, Lu Qi-Keng problem and Jacobi polynomials*, arXiv:1601.02989v1, 12 January 2016, https://arxiv.org/abs/1601.02989, especially Section 5.
