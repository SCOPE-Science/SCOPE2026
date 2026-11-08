# An exact analytic-core envelope for Mbekhta-type bilateral shifts

## Finding
For every \(0<q<1\), consider the bilateral weighted forward shift \(B_q\) on \(\ell^2(\mathbb Z)\) with weights \(w_j=1\) for \(j\le0\) and \(w_j=q^j\) for \(j\ge1\). Write \(\gamma_j=q^{j(j-1)/2}\) for integers \(j\ge1\). Its analytic core has the exact coordinate characterization
\[
\boxed{\mathcal K(B_q)=\left\{x\in\ell^2(\mathbb Z):\exists C>0,\ R\ge1\text{ such that }|x_j|\le CR^j\gamma_j\ (j\ge1)\right\}.}
\]
The negative coordinates obey no extra restriction beyond \(\ell^2\)-summability. In particular, defining \(x_j^{(c)}=q^{c j(j-1)/2}\) for \(j\ge1\), and \(x_j^{(c)}=0\) otherwise, gives, for every \(c>0\),
\[
x^{(c)}\in\bigcap_{n\ge1}\mathcal R(B_q^n),\qquad x^{(c)}\in\mathcal K(B_q)\iff c\ge1.
\]
Thus \(\mathcal K(B_q)\subsetneq\bigcap_{n\ge1}\mathcal R(B_q^n)\), even though the core is dense.

## Assumptions and scope
The Hilbert space is the complex space \(\ell^2(\mathbb Z)\) with its canonical basis \((e_j)_{j\in\mathbb Z}\). The bounded injective operator is \(B_qe_j=w_je_{j+1}\) for a fixed real \(q\in(0,1)\). The analytic core \(\mathcal K(T)\) consists of vectors \(x\) admitting a backward chain \((y^{(n)})_{n\ge0}\) with \(y^{(0)}=x\), \(Ty^{(n+1)}=y^{(n)}\), and \(\|y^{(n)}\|\le M A^n\) for some finite \(M\) and \(A\ge1\) independent of \(n\). For a fixed nonzero vector this is equivalent to the standard bound \(A_0^n\|x\|\), after increasing \(A_0\). The hyperrange is \(\mathcal R^\infty(T)=\bigcap_{n\ge1}\mathcal R(T^n)\); no boundedness condition is imposed on its separate backward preimages.

## Proof
All weights are nonzero, so \(B_q\) and each of its powers are injective. If \(B_q^n y=x\), the preimage coordinates are unique and necessarily satisfy
\[
y_{j-n}=\begin{cases}x_j,&j\le0,\\ x_j/\gamma_j,&1\le j\le n,\\x_j\gamma_{j-n}/\gamma_j,&j>n.\end{cases}
\]
Here and below \(\gamma_0=1\). For \(\alpha_j=x_j/\gamma_j\) for \(j\ge1\), orthogonality gives the **exact inverse-norm identity**
\[
\boxed{\|y\|^2=\sum_{j\le0}|x_j|^2+\sum_{j=1}^{n}|\alpha_j|^2+\sum_{k\ge1}|\alpha_{n+k}|^2q^{k(k-1)}.}\tag{1}
\]
The identity is valid whenever the right side is finite; then the displayed coordinate formula constructs the unique \(\ell^2\) preimage. It remains valid for \(n=0\), when \(y=x\).

If \(x\in\mathcal K(B_q)\), its bounded backward chain is unique. At step \(n=j\), coordinate zero of the preimage equals \(\alpha_j\). Thus \(|\alpha_j|\le MA^j\), which proves the necessity of the stated envelope.

Conversely, suppose \(|\alpha_j|\le CR^j\) for all \(j\ge1\). For any \(R_1>\max\{R,1\}\), the finite sum in (1) satisfies \(\sum_{j=1}^n|\alpha_j|^2\le C_1R_1^{2n}\). Moreover,
\[
\sum_{k\ge1}|\alpha_{n+k}|^2q^{k(k-1)}\le C^2R^{2n}\sum_{k\ge1}R^{2k}q^{k(k-1)}<\infty,
\]
since Gaussian decay dominates the exponential factor. Equation (1) therefore produces a backward preimage for every \(n\) and gives \(\|y^{(n)}\|\le C_2R_1^n\). Injectivity makes these preimages compatible: \(B_qy^{(n+1)}=y^{(n)}\). Hence \(x\in\mathcal K(B_q)\), completing the exact classification.

For \(c>0\), the vector \(x^{(c)}\) is square summable. Its rescaled positive coordinates are \(\alpha_j=q^{(c-1)j(j-1)/2}\). They grow at most exponentially precisely for \(c\ge1\); for \(0<c<1\), their \(j\)-th roots tend to infinity. This proves the analytic-core threshold.

For any fixed integer \(n\ge1\), substitution in the tail of (1) gives
\[
\sum_{k\ge1}q^{(c-1)(n+k)(n+k-1)+k(k-1)}.
\]
Its exponent is \(ck^2+O_n(k)\), so the series converges whenever \(c>0\). The other two terms in (1) are finite. Thus all \(x^{(c)}\) belong to every range \(\mathcal R(B_q^n)\). Choosing \(0<c<1\) proves the strict inclusion. Finally every finite-support vector obeys the envelope and finite-support vectors are dense, so the core is dense.

## Verification
The identity (1) was independently checked with exact rational arithmetic for \(q\in\{1/2,2/3,3/4\}\), finite input supports ranging across negative and positive coordinates, and inverse orders \(0\) through \(12\). The standalone program `check_exact.py` reports `MBEKHTA_CORE_EXACT_FINITE_OK 429`. These finite checks corroborate (1) but do not replace the proof for arbitrary vectors, exponents and inverse orders.

## Relationship to prior work
Mbekhta's original 1990 construction (pp. 274–275) gives the shift at \(q=1/2\) and its non-pseudo-Fredholm property. Aznay and Chabbabi (2026, Section 2, Proposition 2.2) compute the quasinilpotent part using the *negative* coordinates, and prove density and nonclosedness of the analytic core; they do not give a positive-coordinate membership criterion or the hyperrange separation above. Aiena and Biondi (2002, Section 2) investigate analytic cores for an abstract shift condition and one-sided weighted right shifts with trivial hyperrange; that setting does not imply the present bilateral coordinate envelope. The present result determines the complementary analytic-core side of this natural non-pseudo-Fredholm example and its sharp decay transition.

## Limitations
This is an exact result for the specified geometrically damped bilateral shifts; it does not characterize arbitrary weighted bilateral shifts or settle new pseudo-Fredholm decomposition conjectures. It does not determine the topology of the analytic core under any additional norm. The general backward-chain criterion for analytic cores is classical; the claimed contribution is the complete coordinate envelope and its strict hyperrange boundary for this family. A more general published theorem in another formulation could affect publication priority; independent audit has not been performed.

## References
Aznay, Z. and Chabbabi, F., *On Mbekhta's conjecture and pseudo-Fredholm operators on Banach and Hilbert spaces*, arXiv:2610.23229v1 (publicly submitted 16 October 2026), Section 2, https://arxiv.org/abs/2610.23229.

Mbekhta, M., *Opérateurs pseudo-Fredholm. I: Résolvant généralisé*, Journal of Operator Theory **24** (1990), 255–276, especially pp. 255–257 and 274–275, https://jot.theta.ro/jot/archive/1990-024-002/1990-024-002-004.pdf.

Aiena, P. and Biondi, M. T., *Ascent, descent, quasi-nilpotent part and analytic core of operators*, Matematički Vesnik **54** (2002), 57–70, Section 2, https://euclid.matf.bg.ac.rs/index.php/vesnik/article/view/mv023401.
