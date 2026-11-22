# Sharp infinite-divisibility transition for geometric–negative-binomial-five mixtures and Poisson–XRani counts

## Finding
For every probability parameter \(0<q<1\) and mixture weight \(0<w<1\), consider the nonnegative-integer distribution with probability-generating function
\[
G(z)=w\frac{1-q}{1-qz}+(1-w)\left(\frac{1-q}{1-qz}\right)^5.
\]
Thus the distribution is a mixture of a zero-based geometric count and a negative-binomial count of shape five, using the same success probability \(1-q\). It is infinitely divisible under ordinary integer addition **if and only if**
\[
\boxed{\frac{1-w}{w}(1-q)^4\ge4.}
\]
At equality infinite divisibility holds. When the inequality is strict in the opposite direction, *infinitely many* Taylor coefficients of \(\log G(z)\) at \(z=0\) are negative. For either degenerate mixture weight \(w=0\) or \(w=1\), the pure negative-binomial or geometric law is infinitely divisible; these boundary cases are stated separately.

The Poisson–XRani count law of Borbye, Nasiru and Ajongba (2024) is the following explicit one-parameter subfamily. For rate \(\lambda>0\), mix a Poisson count with a positive intensity whose density is
\[
f_\lambda(t)=\frac{\lambda^5}{(\lambda^5+24)^2}\bigl(\lambda^6+48\lambda+24t^4\bigr)e^{-\lambda t},\qquad t>0.
\]
The count distribution is infinitely divisible **exactly** for
\[
\boxed{\lambda(1+\lambda)^4(\lambda^5+48)\le144.}
\]
The left-hand expression is strictly increasing, so the admissible interval is \(0<\lambda\le\lambda_*\), where \(\lambda_*=0.537024530655189\ldots\) is the unique positive root of the displayed equality. Thus mixed-Poisson overdispersion persists for every rate, while compound-Poisson infinite divisibility undergoes a sharp transition.

## Assumptions and scope
A zero-based \(\operatorname{NB}(r,q)\) distribution has probability-generating function \(((1-q)/(1-qz))^r\) for shape \(r>0\), with \(0<q<1\). The shape-one member is geometric. Ordinary infinite divisibility here means that for **every** integer \(m\ge1\) the same count law is an \(m\)-fold convolution of a nonnegative-integer probability law. For a law on \(\{0,1,2,\dots\}\) with positive mass at zero, this is equivalent to having a compound-Poisson representation with nonnegative summable jump intensities \((\nu_n)_{n\ge1}\):
\[
G(z)=\exp\!\left(\sum_{n\ge1}\nu_n(z^n-1)\right),\qquad \nu_n\ge0,\quad\sum_{n\ge1}\nu_n<\infty.
\]
There are no other restrictions on \(w,q\) in the general result. The Poisson–XRani specialization uses precisely the original positive continuous mixing density above and the convention \(Y\mid T=t\sim\operatorname{Poisson}(t)\).

## Proof
**Step 1: exact mixture reduction.** The gamma density of shape five and rate \(\lambda\) is \(\lambda^5t^4e^{-\lambda t}/24\), while the exponential density of rate \(\lambda\) is \(\lambda e^{-\lambda t}\). Direct coefficient comparison gives
\[
f_\lambda(t)=w_\lambda\,\lambda e^{-\lambda t}+(1-w_\lambda)\frac{\lambda^5t^4e^{-\lambda t}}{24},
\quad
w_\lambda=\frac{\lambda^5(\lambda^5+48)}{(\lambda^5+24)^2},
\quad
1-w_\lambda=\frac{576}{(\lambda^5+24)^2}.
\]
Both weights lie strictly between zero and one for every finite positive \(\lambda\), and sum to one. A Poisson mixture with the exponential parent is geometric with \(q=1/(1+\lambda)\); with the shape-five gamma parent it is \(\operatorname{NB}(5,q)\). This establishes the stated general generating function for the PXR model, including the correct normalization.

**Step 2: the complete logarithmic-coefficient formula.** For a general interior mixture put \(r=1-q\) and
\[
\delta=\left(\frac{1-w}{w}r^4\right)^{1/4}>0.
\]
Rearranging yields
\[
G(z)=wr\frac{(1-qz)^4+\delta^4}{(1-qz)^5}.
\]
Let \(\omega_j=\exp(i(2j+1)\pi/4)\), \(j=0,1,2,3\), be the fourth roots of \(-1\), and set \(\zeta_j=1-\delta\omega_j\). The numerator factors as \(\prod_{j=0}^3(\zeta_j-qz)\). Because \(\zeta_j\ne0\), expanding the analytic logarithm around \(z=0\), where \(G(0)>0\), gives the exact formula for every integer \(n\ge1\):
\[
\boxed{\nu_n=\frac{q^n}{n}\left(5-\sum_{j=0}^{3}\zeta_j^{-n}\right).}
\]
The expression is real because roots occur in conjugate pairs. Its sign is the only issue for integer infinite divisibility.

**Step 3: sufficient condition, including the boundary.** The two conjugate roots with positive real part \(\omega_j\) have squared modulus
\[
R_-^2=1+\delta^2-\sqrt2\delta,
\]
and the other conjugate pair has squared modulus \(R_+^2=1+\delta^2+\sqrt2\delta\). Thus when \(\delta\ge\sqrt2\), all four \(|\zeta_j|\ge1\) and so \(\sum_j\zeta_j^{-n}\le\sum_j|\zeta_j|^{-n}\le4\). Consequently \(\nu_n\ge q^n/n>0\), for every positive integer \(n\). Also \(\nu_n\le9q^n/n\), so the jump-intensity series is absolutely summable. The logarithmic expansion converges at \(z=1\) (because \(q<1\)) and \(G(1)=1\) sets the constant to \(-\sum_n\nu_n\). Hence the displayed generating function is compound Poisson. This proves infinite divisibility at and below the threshold in weight-space.

**Step 4: necessary condition and infinitely many obstructions.** Suppose \(0<\delta<\sqrt2\), so \(0<R_-<1<R_+\). Write the pair of near roots as \(R_-e^{\pm i\phi}\) with \(\phi\not\equiv0\pmod{2\pi}\) and the far roots as \(R_+e^{\pm i\psi}\). The same coefficient formula reads
\[
\frac{n\nu_n}{q^n}=5-2R_-^{-n}\cos(n\phi)-2R_+^{-n}\cos(n\psi).
\]
There are infinitely many positive integers \(n\) with \(\cos(n\phi)>1/2\): if \(\phi/(2\pi)\) is rational, take multiples of its denominator; otherwise use the density of irrational circle rotations (or the elementary pigeonhole/Dirichlet approximation argument). Along those integers, \(R_-^{-n}\to\infty\) whereas \(R_+^{-n}\to0\). Therefore \(\nu_n<0\) for infinitely many positive integers, contradicting the necessary compound-Poisson coefficient condition. This proves the converse. Since \(\delta^4=((1-w)/w)(1-q)^4\), the threshold is precisely \(\delta^4\ge4\).

**Step 5: the PXR cutoff.** Substitute the explicit weights and \(r=\lambda/(1+\lambda)\) to obtain
\[
\delta_\lambda^4
=\frac{576}{\lambda(1+\lambda)^4(\lambda^5+48)}.
\]
Thus \(\delta_\lambda^4\ge4\) is exactly \(\lambda(1+\lambda)^4(\lambda^5+48)\le144\). Each positive factor in the denominator is strictly increasing in \(\lambda>0\), with product ranging from zero to infinity, so there is exactly one positive threshold and no other transitions. Finally, the intensity has positive variance for all \(\lambda>0\), hence \(\operatorname{Var}(Y)=\mathbb EY+\operatorname{Var}(T)>\mathbb EY\), independently of infinite divisibility. This completes the sharp classification.

## Verification
Run `python checker.py` with SymPy. All symbolic equalities are checked by exact algebra/rational arithmetic: XRani density normalization and the exponential/gamma mixture weights; the independently integrated Poisson-mixture generating function; quartic parameter reduction and the tenth-degree critical polynomial. For rate \(\lambda=1\), the first negative logarithmic coefficient occurs at \(n=5\), with exact value \(n\nu_n=-3836474651/141985700000\). The checker also verifies the first 24 positive coefficients at rates \(1/10\) and \(1/2\) and numerically refines the unique threshold. These finite computations are only cross-checks: the infinite, all-parameter theorem follows from the exact algebraic root-modulus argument in the proof, not from sampled coefficients.

## Relationship to prior work
Borbye, Nasiru and Ajongba (2024), DOI 10.1155/2024/5554949, introduced the Poisson–XRani law, its mass and generating functions, and overdispersion; no infinite-divisibility phase classification is stated in its accessible full article narrative. Etaga, Onyekwere, Oramulu and Obulezi (2023), DOI 10.36347/sjpms.2023.v10i07.003, introduced the XRani continuous intensity density used in this proof. The broad structural literature on mixed Poisson laws, including *Mutant Number Laws and Infinite Divisibility* (2022), gives the classical discrete compound-Poisson criterion and distinguishes negative-binomial convolutions from arbitrary mixtures; it does not provide this geometric/shape-five mixture's necessary-and-sufficient threshold. Results on zero-inflated negative-binomial laws treat a point-mass-plus-negative-binomial model, whose generating polynomial differs from the current geometric-plus-shape-five mixture. The present claim is the exact root-geometric sign classification and its induced PXR cutoff, not the original density or generic infinite-divisibility criterion.

## Limitations
The result concerns ordinary convolution infinite divisibility of discrete counts, not thinning self-decomposability, geometric infinite divisibility, or the infinite divisibility of the *continuous mixing intensity*. It does not classify arbitrary mixtures with negative-binomial shape other than five, unequal success probabilities, or arbitrary Poisson-mixture mixing densities. The exact curve extends the published distribution within the general two-component model; this mathematical analysis makes no exhaustive historical-priority claim. The original 2024 article's scientific sections were accessible in publisher HTML, but several rendered equations were missing from the text extraction; the density was verified independently from its original 2023 source and exact integrations.

## References
1. S. Borbye, S. Nasiru and K. K. Ajongba, “Poisson XRani Distribution: An Alternative Discrete Distribution for Overdispersed Count Data,” *International Journal of Mathematics and Mathematical Sciences*, 2024, article 5554949, first published 9 July 2024. https://doi.org/10.1155/2024/5554949.
2. H. O. Etaga, C. K. Onyekwere, D. O. Oramulu and O. J. Obulezi, “A New Modification of Rani Distribution with More Flexibility in Application,” *Scholars Journal of Physics, Mathematics and Statistics* 10 (2023), 160–176, published 30 September 2023. https://doi.org/10.36347/sjpms.2023.v10i07.003. Open scientific text: https://www.saspublishers.com/media/articles/SJPMS_107_160-176.pdf.
3. “Mutant Number Laws and Infinite Divisibility,” *Axioms* 11 (2022), article 584, particularly the discrete infinite-divisibility canonical representation and Definition 9 / Fact 8 for Poisson-gamma mixtures. https://www.mdpi.com/2075-1680/11/11/584.
