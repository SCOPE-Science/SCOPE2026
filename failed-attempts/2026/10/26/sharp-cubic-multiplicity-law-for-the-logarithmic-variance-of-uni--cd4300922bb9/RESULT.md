# Sharp cubic-multiplicity law for the logarithmic variance of unimodular-zero polynomials

## Finding
Let \(P(z)=c\prod_{j=1}^{r}(z-e^{i\phi_j})^{m_j}\), where \(c\ne0\), the angles \(\phi_j\) are distinct modulo \(2\pi\), each \(m_j\) is a positive integer, and \(n=\sum_jm_j\). Let \(dm\) denote normalized Haar measure on the unit circle and define
\[
V(P)=\int_{\mathbb T}\bigl(\log|P(z)|-\log|c|\bigr)^2\,dm(z).
\]
The following bound is sharp for **every prescribed multiplicity multiset**, and indeed for every prescribed cyclic order of those multiplicities:
\[
\boxed{V(P)\ge\frac{\pi^2}{12n}\sum_{j=1}^{r}m_j^3.}
\]
For an ordered lift \(\phi_1<\cdots<\phi_r<\phi_1+2\pi\), let \(B_j=\sum_{h<j}m_h\), \(\phi_j^*=\pi(2B_j+m_j-1)/n\), \(\delta_j=\phi_j-\phi_j^*\), and \(\overline\delta=\sum_jm_j\delta_j/n\). An exact global stability formula holds:
\[
\boxed{V(P)=\frac{\pi^2}{12n}\sum_{j=1}^{r}m_j^3+
\frac n4\sum_{j=1}^{r}m_j(\delta_j-\overline\delta)^2.}
\]
Equality occurs exactly when the distinct roots form, up to common rotation, the weighted-midpoint configuration \(\phi_j^*\). Equivalently, the consecutive cyclic gaps are
\[
\boxed{\phi_{j+1}-\phi_j=\frac\pi n(m_j+m_{j+1})}
\]
with cyclic indices and the final gap measured through \(2\pi\). When \(r=1\), the unique root angle is arbitrary, as is inherent in rotational symmetry.

If only the degree \(n\) and number \(r\) of **distinct** unimodular roots are prescribed, let \(n=qr+s\) with \(0\le s<r\). Then the exact minimum is
\[
\boxed{\frac{\pi^2}{12n}\bigl((r-s)q^3+s(q+1)^3\bigr).}
\]
Its complete equality family consists of cyclic weighted-midpoint configurations with precisely \(r-s\) multiplicities \(q\) and \(s\) multiplicities \(q+1\), in any cyclic order. All these minima are attained by polynomials having exactly \(r\) distinct roots.

## Assumptions and scope
Every integer \(n\ge1\), \(1\le r\le n\), and all positive integer multiplicity partitions of \(n\) are included. All roots lie exactly on \(\mathbb T\); roots may coincide according to their multiplicities, but the \(r\) listed roots are mutually distinct. The scalar \(c\) is arbitrary and cancels under centering by \(\log|c|\). The logarithmic singularities are square-integrable with respect to normalized Haar measure. The stability identity is global within any chosen cyclic-order chamber, not a perturbative approximation. The theorem does not concern off-circle zeros or the positive-exponent norm-ratio problem.

## Proof
**1. Exact circular quadratic energy.** List the \(n\) root angles with multiplicity as \(\theta_1\le\cdots\le\theta_n<\theta_1+2\pi\). The mean-zero Fourier expansion
\[
\log|e^{it}-e^{i\theta}|=-\sum_{k\ge1}\frac{\cos(k(t-\theta))}{k}
\quad\text{in }L^2(\mathbb T)
\]
and Parseval yield, with \(S_k=\sum_{h=1}^ne^{ik\theta_h}\),
\[
V(P)=\frac12\sum_{k\ge1}\frac{|S_k|^2}{k^2}
=\frac12\sum_{h,\ell=1}^nF(\theta_h-\theta_\ell),
\]
where the even, periodic Bernoulli kernel satisfies
\[
F(u)=\sum_{k\ge1}\frac{\cos(ku)}{k^2}
=\frac{\pi^2}{6}-\frac{\pi |u|}{2}+\frac{u^2}{4}
\quad (|u|\le2\pi).
\]
Thus, on a fixed ordered-angle chamber (including its coincidence faces), \(V\) is an exact quadratic polynomial. Put \(\alpha_h=2\pi(h-1)/n\), \(e_h=\theta_h-\alpha_h\), and \(\overline e=n^{-1}\sum_he_h\). Its Hessian is \((n/2)(I-\mathbf1\mathbf1^T/n)\). Its gradient vanishes at the regular configuration \(\boldsymbol\alpha\), and there \(V=\pi^2/12\) by the power-sum formula. Therefore, for **all** such ordered configurations,
\[
\boxed{V(P)=\frac{\pi^2}{12}+\frac n4\sum_{h=1}^n(e_h-\overline e)^2.}\tag{1}
\]
This is a polynomial identity extending to coinciding angles by continuity; no small-perturbation assumption occurs.

**2. Orthogonal projection to the multiplicity constraints.** Form contiguous blocks of lengths \(m_1,\ldots,m_r\) in the ordered angle list, with the angle of every member of block \(j\) equal to \(\phi_j\). The arithmetic mean of the regular positions \(\alpha_h\) in block \(j\) is exactly \(\phi_j^*=\pi(2B_j+m_j-1)/n\). Within a block,
\[
\sum_{h=B_j+1}^{B_j+m_j}(\alpha_h-\phi_j^*)=0,
\quad
\sum_{h=B_j+1}^{B_j+m_j}(\alpha_h-\phi_j^*)^2
=\frac{\pi^2}{3n^2}m_j(m_j^2-1).
\]
Because the within-block centered residuals sum to zero, expansion of the squares in (1) has no cross term between the residuals and the block shifts \(\delta_j=\phi_j-\phi_j^*\). Moreover \(\overline e=\overline\delta\). Substitution into (1) gives
\[
V(P)=\frac{\pi^2}{12}+\frac{\pi^2}{12n}\sum_j(m_j^3-m_j)
+\frac n4\sum_jm_j(\delta_j-\overline\delta)^2,
\]
which simplifies to the stated cubic law and exact defect.

**3. Attainment, order, and rigidity.** The target angles have successive gaps \(\phi_{j+1}^*-\phi_j^*=\pi(m_j+m_{j+1})/n>0\), and the last-to-first cyclic gap has the same formula. These gaps sum to \(2\pi\), so the target lies in the required distinct-root chamber. The nonnegative defect vanishes if and only if all \(\delta_j\) are equal, i.e. the target configuration is rotated rigidly. This also proves uniqueness within every prescribed cyclic order. The endpoint \(r=1\) has identically zero defect and the correct minimum \(n^2\pi^2/12\).

**4. Exact classification with only \(n\) and \(r\) prescribed.** By the integer exchange inequality
\[
(a^3+b^3)-((a-1)^3+(b+1)^3)
=3(a-b-1)(a+b)>0\quad(a\ge b+2\ge3),
\]
any nonbalanced pair of positive multiplicities can be balanced to lower the sum of cubes. Repetition forces and characterizes the unique multiset consisting of \(r-s\) entries \(q\) and \(s\) entries \(q+1\). Every cyclic ordering is geometrically attained as in Step 3. This proves the final formula and complete equality classification.

## Verification
The accompanying `verify.py` evaluates the Bernoulli-energy formula and the exact quadratic remainder using rational arithmetic with angles measured in turns. It verifies **all 1023 ordered integer compositions in degrees 1 through 10** at both the claimed minimizer and a strictly ordered rational perturbation, and checks the balancing exchange argument across \(1\le r\le n\le20\). Its successful output is:

`CHECK_OK: 1023 exact rational composition/stability tests across degrees 1..10; balanced-profile checks 1..20`

These finite checks do not establish the infinite theorem. The proof is the general Fourier/Bernoulli identity, finite-dimensional orthogonal projection, and integer convexity argument above. No computer algebra or external certificate is needed to justify the universal quantifiers.

## Relationship to prior work
T. Zhang (2026), arXiv:2610.02009v1, §7.4, proves the unconditioned lower bound \(V(P)\ge\pi^2/12\), identifies regular polygons as equality examples, and records the equivalent power-sum energy. That prior theorem is recovered here when all multiplicities are one; it does **not** itself state the sharp minimum with fixed collisions or the cubic cost of multiplicity, nor the exact global weighted angular defect. The contribution here is the complete multiplicity-constrained optimization and rigidity across every cyclic ordering.

N. Nagel (2025), Proposition 2.1, develops generalized weighted periodic \(L^2\)-discrepancy energies. Its one-dimensional Bernoulli kernel is equivalent, up to normalization, to the present quadratic energy representation. The kernel identity and Fourier method are classical and are not claimed new. The precise minimizer with *prescribed integer multiplicities*, the cubic partition minimum, and the exact root-angle stability are the claimed contributions. Existing local Hessian calculations around simple regular root polygons do not, by themselves, imply the repeated-root and global chamber statements.

## Limitations
The scientific priority of the sharp fixed-multiplicity optimization is assessed against accessible primary literature and mathematical records, not independently certified; an older result in one-dimensional weighted quadrature or discrepancy may implicitly contain the same theorem. The claim is intentionally limited to unit-circle zeros and the centered logarithmic second moment. The simple-root specialization of the local Hessian and the unconstrained universal bound are not priority claims. The global stability identity compares configurations with a fixed cyclic assignment of multiplicities, and different cyclic orders require their corresponding reference configurations. No claim is made about strong extremality, positive-exponent Baernstein deficits, or independent validation.

## References
1. T. Zhang, *Baernstein's quasi-norm monotonicity conjecture for polynomials with unimodular zero*, arXiv:2610.02009v1, first posted 2026-10-01, especially §7.4, Corollary 7.4. https://arxiv.org/abs/2610.02009
2. N. Nagel, *On the \(L_2\)-discrepancy of Latin hypercubes*, Monatshefte für Mathematik **207** (2025), 309–336, Proposition 2.1. https://doi.org/10.1007/s00605-025-02065-2
3. The classical Fourier series for the second Bernoulli polynomial, \(\sum_{k\ge1}\cos(ku)/k^2=\pi^2/6-\pi|u|/2+u^2/4\) on \(|u|\le2\pi\), used as an explicit identity rather than an asserted new result.
