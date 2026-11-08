# Sharp real-rootedness intervals for the first two wheel–whirl pencils

## Finding
Let \(W_r\) be the wheel graph with \(r\) rim vertices and one hub, \(M_r\) its cycle matroid and \(N_r\) the whirl obtained by relaxing the rim circuit-hyperplane. For a lattice polytope \(P\), write \(h_P^*(z)\) for the numerator of its Ehrhart series. Set
\[
H_{r,\lambda}(z)=(1-\lambda)h_{P(N_r)}^*(z)+\lambda h_{P(M_r)}^*(z),\qquad \lambda\in\mathbb{R}.
\]
For \(r=3\), this polynomial has four simple strictly negative roots **if and only if** \(\lambda<2\). For \(r=4\), it has six simple strictly negative roots **if and only if** \(\alpha<\lambda<\beta\), where \(\alpha,\beta\) are the two smallest real zeros of
\[
D(\lambda)=540\lambda^9+253179\lambda^8+20881044\lambda^7-2104879564\lambda^6+38517032576\lambda^5+505358362624\lambda^4-43739303378944\lambda^3+1148331013439488\lambda^2-15876704476069888\lambda+73794715169849344.
\]
There are exactly three distinct real zeros of \(D\), one in each of
\[
(-313/10,-312/10),\qquad(816/100,817/100),\qquad(3696/100,3697/100).
\]
Thus \(\alpha\approx-31.2694641272\), \(\beta\approx8.1613641429\), and the third zero \(\gamma\approx36.9649509915\). The rank-three left endpoint is unbounded, whereas the rank-four left endpoint is finite. The original geometric polytopes occur at \(\lambda=0,1\); other values define a formal real polynomial pencil and are **not** asserted to be Ehrhart numerators.

## Assumptions and scope
The assertions concern \(r\in\{3,4\}\), arbitrary **real** \(\lambda\), and simple negative zeros. At a discriminant-zero endpoint roots cease to be simple; the theorem is not an assertion about all ranks. The Ehrhart numerator is normalized by \(h_P^*(0)=1\). All interval endpoints are exact algebraic numbers isolated by rational bounds, not rounded decimals. The primary lattice-polytope content is the rank-\(r\) wheel/whirl base-polytope pair.

## Proof
**1. Derive the pencils.** For the crown order polytope with \(2r\) elements, the exact count for each nonnegative integer \(q\) is
\[
L_r(q)=\operatorname{tr}(K_{q+1}^r),\qquad K_m=(\min(i,j))_{1\le i,j\le m}.
\]
The crown–whirl Ehrhart identity, together with the circuit-hyperplane relaxation formula, gives
\[
H_{r,\lambda}(z)=F_r(z)-\lambda z\sum_{j=0}^{r-1}\binom{r-1}{j}^2z^j,
\]
where \(F_r\) is the crown Ehrhart numerator. From \(L_r(q)\), the coefficient of \(z^k\) in \(F_r\) is \(\sum_{j=0}^k(-1)^{k-j}\binom{2r+1}{k-j}L_r(j)\). In particular,
\[
F_3(z)=1+11z+24z^2+11z^3+z^4,
\]
\[
F_4(z)=1+38z+263z^2+484z^3+263z^4+38z^5+z^6.
\]
Consequently,
\[
H_{3,\lambda}=z^4+(11-\lambda)z^3+(24-4\lambda)z^2+(11-\lambda)z+1,
\]
\[
H_{4,\lambda}=z^6+38z^5+(263-\lambda)z^4+(484-9\lambda)z^3+(263-9\lambda)z^2+(38-\lambda)z+1.
\]
**2. Rank three.** Divide the reciprocal quartic by \(z^2\), and put \(y=z+z^{-1}\). Its equation becomes
\[
y^2+(11-\lambda)y+22-4\lambda=0.
\]
The discriminant is \(\lambda^2-6\lambda+33>0\). For \(\lambda<2\) the vertex of this parabola is to the left of \(-2\) and its value at \(-2\) is \(2(2-\lambda)>0\), hence both distinct solutions satisfy \(y<-2\); each produces two distinct negative reciprocal roots \(z\). At \(\lambda=2\), \(y=-2\) produces the repeated root \(z=-1\). For \(2<\lambda<8\), one \(y\)-root lies in \((-2,2)\), yielding two nonreal unit-modulus roots. For \(\lambda\ge8\), one \(y\)-root is at least \(2\), yielding positive roots. Thus the exact rank-three simple-negative locus is \((-\infty,2)\).

**3. Rank four, complete discriminant isolation.** Direct expansion of \(\operatorname{disc}_z H_{4,\lambda}\) gives \(16D(\lambda)\). Apply the exact Sturm-sequence algorithm to \(D\): the sequence of sign-variation counts at \(-\infty,-313/10,-312/10,816/100,817/100,3696/100,3697/100,+\infty\) is, in that order,
\[
6,6,5,5,4,4,3,3.
\]
The differences certify precisely three real discriminant zeros, one in each stated rational interval and no others. These exact integer/rational computations are reproduced by the embedded checker.

**4. Classify the connected intervals.** Applying Sturm's theorem in the variable \(z\) to \(H_{4,\lambda}\), the variation counts at \((-\infty,0)\) are \((5,1)\) at \(\lambda=-32\), \((6,0)\) at \(\lambda=0\), and \((5,1)\) at \(\lambda=9\). Thus these samples have respectively four, six, and four strictly negative real zeros. The discriminant is nonzero between successive real zeros of \(D\); on each resulting open interval the number of negative real roots cannot change, because the leading coefficient is constantly \(1\) and the constant coefficient is constantly \(1\), so no root can cross infinity or zero. Hence exactly the interval \((\alpha,\beta)\) has six simple strictly negative roots among all parameters less than \(\gamma\). At each endpoint \(\alpha,\beta,\gamma\), the discriminant vanishes and six *simple* roots are impossible. Finally, for \(\lambda\ge\gamma>263/9\), the coefficient of \(z^2\), namely \(263-9\lambda\), is negative. A monic polynomial with all roots strictly negative has strictly positive coefficients. Thus no \(\lambda\ge\gamma\) is admissible. This proves the exact rank-four interval and completes the classification.

## Verification
Run `python wheel_whirl_sturm_check.py` with Python 3 and SymPy. The program independently counts small crown lattice-point sets directly and by the transfer matrix; reconstructs the rank-four numerator from nine exact counts; verifies the degree-nine discriminant identity; isolates *all* its real zeros using exact Sturm sequences; counts negative roots at three rational witnesses; and checks the rank-three quartic discriminant. All critical computations use integers or rational arithmetic. The mathematical proof is the derivation, the Sturm sign-variation certificates, and constancy of root counts—not numerical root plotting.

## Relationship to prior work
Cao and Fu (2026), Theorem 1.2, prove simple negative roots for every rank \(r\ge3\) and all \(0\le\lambda\le1\), and supply the polynomial pencil and crown–whirl correspondence. Their Section 4.1 computes the rank-three crown numerator, and Sections 4.1–4.4 prove the restricted interval. The present theorem determines the **maximal real parameter domain** in ranks three and four, including all negative parameters and the first positive collision. Neither their theorem nor its proof implies the sharp outside-segment thresholds. Ferroni's circuit-hyperplane relaxation formula gives the correction term but no global root-locus. Lundström and Saud Maia Leite derive crown Ehrhart data and study gamma-nonnegativity, not the relaxed wheel–whirl polynomial pencil on all real parameters. The exact stability domain is an algebraic property of the pencil, not a claim of new lattice polytopes for nonendpoint parameters.

## Limitations
Only ranks three and four are classified; nothing is asserted about higher ranks, polytope realization for noninteger \(\lambda\), or a general uniform over-relaxation theorem. The endpoints are discriminant-zero values and fail *simplicity*. The result is an exact mathematical computation with a self-contained Sturm argument and a SymPy-based replay script, not an independently audited theorem. Historical priority remains subject to independent literature assessment.

## References
- Y. Cao and H. Fu, *Real-rooted Ehrhart \(h^*\)-polynomials of crown posets and wheel and whirl matroids*, arXiv:2610.40496v1 (first public 2026-10-29), Theorems 1.1–1.2, Sections 2–4. https://arxiv.org/abs/2610.40496
- T. Lundström and L. Saud Maia Leite, *On order polytopes of crown posets*, arXiv:2504.05123 (2025), Sections 4–6. https://arxiv.org/abs/2504.05123
- L. Ferroni, *On the Ehrhart Polynomial of Minimal Matroids*, arXiv:2003.02679 (2020), especially Section 5 on circuit-hyperplane relaxation. https://arxiv.org/abs/2003.02679
- C. Sturm, classical theorem on real-root counting by polynomial remainder sequences, as implemented in exact rational arithmetic by SymPy.
