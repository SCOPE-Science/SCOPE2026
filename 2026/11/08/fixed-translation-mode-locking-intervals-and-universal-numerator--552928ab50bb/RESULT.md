# Fixed-translation mode-locking intervals and universal numerator-free opening for contracted rotations

## Finding
Fix coprime integers \(1\le p<q\) and put \(r=p/q\). Consider the contracted circle rotation
\[
R_{\lambda,b}(x)=\{\lambda x+b\},\qquad 0<\lambda<1,\quad 0<b<1,\quad x\in[0,1).
\]
The braces indicate fractional part. Let \(\rho(\lambda,b)\) be its usual monotone-circle-lift rotation number. Set
\[
H_q(t)=\sum_{j=0}^{q-1}t^j,\quad
 a_j=\left\lceil\frac{(j+1)p}{q}\right\rceil-\left\lceil\frac{jp}{q}\right\rceil,\quad
 S_{p,q}(t)=\sum_{j=0}^{q-1}a_jt^j.
\]
For \(0<t<1\), define
\[
L_{p,q}(t)=\frac{S_{p,q}(t)}{H_q(t)},\qquad
U_{p,q}(t)=\frac{S_{p,q}(t)+t^{q-1}(1-t)}{H_q(t)}.
\]
**Theorem (fixed-translation rational tongue and universal opening).** Both \(L_{p,q}\) and \(U_{p,q}\) are strictly decreasing on \((0,1)\), with respective common limits \(1\) at \(t\downarrow0\) and \(r\) at \(t\uparrow1\). For every fixed \(0<b<1\),
\[
\{\lambda\in(0,1):\rho(\lambda,b)=r\}=\begin{cases}
\varnothing,&b\le r,\\[2mm]
[\alpha_{p,q}(b),\beta_{p,q}(b)],&r<b<1,
\end{cases}
\]
where \(\alpha_{p,q}(b)<\beta_{p,q}(b)\) are the unique solutions in \((0,1)\) of
\[
S_{p,q}(\alpha)=bH_q(\alpha),\qquad
S_{p,q}(\beta)+\beta^{q-1}(1-\beta)=bH_q(\beta).
\]
As \(b\downarrow r\), with \(p,q\) held fixed,
\[
\begin{aligned}
\alpha_{p,q}(b)&=1-\frac{2q}{q-1}(b-r)+O_{p,q}((b-r)^2),\\
\beta_{p,q}(b)&=1-\frac{2q}{q+1}(b-r)+O_{p,q}((b-r)^2),\\
\beta_{p,q}(b)-\alpha_{p,q}(b)&=\frac{4q}{q^2-1}(b-r)+O_{p,q}((b-r)^2).
\end{aligned}
\]
The first-order slope-window opening depends only on \(q\), not on \(p\).

## Assumptions and scope
The rotation number is defined using the nondecreasing lift
\[
F_{\lambda,b}(x)=\lambda x+(1-\lambda)\lfloor x\rfloor+b,\qquad
\rho(\lambda,b)=\lim_{n\to\infty}\frac{F_{\lambda,b}^n(x)-x}{n}.
\]
The limit is independent of \(x\). The assertion is for reduced positive rational rotation numbers strictly between zero and one. The translation parameter is fixed as the slope varies. No claim is made for irrational targets, zero rotation, arbitrary two-slope maps, or any other kind of circle map. Endpoint membership refers to rotation number; at a border endpoint an attracting period-\(q\) cycle need not exist.

## Proof
**1. The classical plateau input.** The known rational-tongue formula of Laurent and Nogueira (also restated as Proposition 7 by Gaivão and Nogueira) says that for \(0<\lambda<1\), \(\rho(\lambda,b)=p/q\) if and only if
\[
L_{p,q}(\lambda)\le b\le U_{p,q}(\lambda).
\]
Indeed, their numerator equals
\(1+\sum_{k=1}^{q-2}(\lfloor(k+1)p/q\rfloor-\lfloor kp/q\rfloor)t^k\).
This equals \(S_{p,q}(t)\): the zeroth upper-mechanical coefficient is one, the final coefficient is zero, and for \(1\le k\le q-2\), the integer \(kp/q\) is nonintegral, so replacing floors by ceilings does not change the increments. Multiplication of the published formula by \((1-t^q)/(1-t)=H_q(t)\) gives exactly the displayed \(L_{p,q}\) and \(U_{p,q}\). These direct plateau formulas are **prior literature**, not part of the novelty claim.

**2. A weighted prefix-dominance lemma.** Let \(v_0,\ldots,v_{q-1}\) be real numbers such that for every \(1\le k\le q\) and every \(0\le h\le q-k\),
\[
\sum_{i=0}^{k-1}v_i\ge\sum_{i=h}^{h+k-1}v_i.
\]
Define \(P_v(t)=\sum_{i=0}^{q-1}v_it^i\). Then \(P_v(t)/H_q(t)\) is nonincreasing for \(0<t<1\). To prove this, differentiate and pair terms with indices separated by \(h\):
\[
P_vH_q'-P_v'H_q
=\sum_{h=1}^{q-1}h t^{h-1}
\sum_{i=0}^{q-1-h}(v_i-v_{i+h})t^{2i}.
\]
For fixed \(h\), every partial sum of \((v_i-v_{i+h})_{0\le i<q-h}\) is nonnegative by the hypothesis. Abel summation against the decreasing weights \(1,t^2,t^4,\ldots\) therefore makes each inner sum nonnegative. This proves the lemma. If at least one of the inner sums is positive for all \(t\in(0,1)\), the derivative is strictly negative.

**3. Two special mechanical words.** Put \(r=p/q\), and extend the coefficients by \(a_i=\lceil(i+1)r\rceil-\lceil ir\rceil\) for all nonnegative integer \(i\). Any factor of length \(k\) has sum
\[
\left\lceil(h+k)r\right\rceil-\lceil hr\rceil,
\]
which is either \(\lfloor kr\rfloor\) or \(\lceil kr\rceil\). Its initial length-\(k\) factor has sum \(\lceil kr\rceil\). Thus the word \((a_0,\ldots,a_{q-1})\) satisfies the prefix-dominance hypothesis. Moreover \(a_0=1\) and \(a_{q-1}=0\), so the \(h=q-1\) term in the derivative identity is strictly positive. Consequently
\[
L_{p,q}'(t)<0\quad(0<t<1).
\]
For \(U_{p,q}\), replace only the last coefficient by one: set \(v_i=a_i\) for \(0\le i\le q-2\) and \(v_{q-1}=1\). For factors not containing the last position, the preceding estimate still holds. For a factor of length \(k<q\) ending at position \(q-1\) and starting at \(h=q-k\ge1\), its modified sum is
\[
p-\lceil hr\rceil+1=p-\lfloor hr\rfloor=\lceil kr\rceil,
\]
since \(hr\notin\mathbb Z\). Hence this modified word also has maximal initial factors; the weighted prefix lemma gives \((P_v/H_q)'\le0\). But
\[
U_{p,q}(t)=\frac{P_v(t)}{H_q(t)}-\frac{t^q}{H_q(t)},\qquad
\left(\frac{t^q}{H_q(t)}\right)'=
\frac{t^{q-1}\sum_{i=0}^{q-1}(q-i)t^i}{H_q(t)^2}>0.
\]
It follows that \(U_{p,q}'(t)<0\) as well.

**4. Exact fixed-translation inversion.** Since \(\sum_{i=0}^{q-1}a_i=p\) and \(a_0=1\), both curves have limits \(1\) at zero and \(p/q\) at one. Further,
\[
U_{p,q}(t)-L_{p,q}(t)=\frac{t^{q-1}(1-t)}{H_q(t)}>0.
\]
For \(b\le p/q\), the strict decrease implies \(L_{p,q}(t)>p/q\ge b\), so the plateau condition is impossible. For \(p/q<b<1\), both endpoint equations have exactly one root. Since \(L_{p,q}<U_{p,q}\), the root \(\alpha\) of \(L=b\) comes strictly before the root \(\beta\) of \(U=b\). The two monotonic inequalities in step 1 hold simultaneously exactly on \([\alpha,\beta]\).

**5. Numerator-free boundary derivatives.** For coprime \(p,q\), the standard floor-sum pairing identity is
\[
\sum_{j=1}^{q-1}\left\lfloor\frac{jp}{q}\right\rfloor=
\frac{(p-1)(q-1)}2.
\]
Since none of \(jp/q\), \(1\le j\le q-1\), is integral, summation by parts gives
\[
\begin{aligned}
S_{p,q}(1)&=p,\\
S_{p,q}'(1)&=\sum_{i=0}^{q-1}ia_i
=(q-1)p-\sum_{j=1}^{q-1}\lceil jr\rceil
=\frac{(p-1)(q-1)}2.
\end{aligned}
\]
With \(H_q(1)=q\) and \(H_q'(1)=q(q-1)/2\), quotient differentiation yields
\[
L_{p,q}'(1)=-\frac{q-1}{2q},\qquad
U_{p,q}'(1)=L_{p,q}'(1)-\frac1q=-\frac{q+1}{2q}.
\]
Both derivatives are nonzero. The analytic inverse-function theorem at \(t=1\) gives the two displayed endpoint expansions, and subtraction gives the claimed opening coefficient \(4q/(q^2-1)\). This finishes the proof.

## Verification
A standalone Python 3 program, `verify.py`, checks the mechanical-word prefix dominance, first moments, exact-rational derivative signs, and strictly ordered sample endpoints using exact integer or rational arithmetic over coprime pairs with \(2\le q\le45\). The bounded test is a regression check only; the proof above establishes every denominator \(q\ge2\). For a simple exact example, \(p/q=1/2\) and \(b=3/4\) give
\[
\alpha_{1,2}(3/4)=\frac13,\qquad
\beta_{1,2}(3/4)=\frac{1+\sqrt{17}}8.
\]
The program checks the defining polynomial identity for this example and the universal derivative formulas for the tested denominators.

## Relationship to prior work
Laurent and Nogueira established the exact rational mode-locking interval in the translation parameter for **fixed slope**. Gaivão and Nogueira (2020 preprint, published 2022), after restating this classical formula, explicitly noted that a precise definition of the rational-tongue endpoints in the **slope parameter with translation fixed** was not available. Here those inverse sections are proved to be single intervals with unique polynomial endpoints, and their opening has a numerator-independent universal coefficient. Janson and Öberg (2019), Theorem 5.5 and Example 5.7, likewise characterize the translation parameter at fixed contraction; their two-dimensional formulation and explicit half-rotation example do not establish all-denominator strict inverse-slope monotonicity or the numerator-independent opening. A subsequent study by Gaivão, Laurent and Nogueira treats a wider two-interval family by varying a branch parameter with other parameters fixed; Guiraud and collaborators treat three-interval maps with the contraction rate fixed. Neither supplies the stated inverse-slope theorem or its boundary law in the inspected material. The direct rational plateau formula and its underlying symbolic coding remain fully credited as known.

## Limitations
The result does not determine irrational-rotation slope sections, nor does it characterize the dependence of the finite-distance interval width on the numerator beyond the leading-order result at \(b=p/q\). The asymptotic error depends on fixed \(p,q\), and no estimate uniform in denominator is proved. The original published rational plateau formula is necessary input. Claims of global publication priority would require further independent literature examination, including older mode-locking and contracted-rotation literature under alternate terminology. No independent mathematical audit has been performed.

## References
1. M. Laurent and A. Nogueira, *Rotation number of interval contracted rotations*, arXiv:1704.05130 (first posted 2017-04-17); published as *Rotation number of contracted rotations*, J. Modern Dynamics 12 (2018), 175–191. https://arxiv.org/abs/1704.05130
2. J. P. Gaivão and A. Nogueira, *Dynamics of piecewise increasing contractions*, arXiv:2007.08014 (first posted 2020-07-15), Proposition 7 and the paragraph immediately following; Bull. Lond. Math. Soc. 54 (2022), 482–500. https://arxiv.org/html/2007.08014v2
3. S. Janson and A. Öberg, *A piecewise contractive dynamical system and Phragmén’s election method*, Bull. Soc. Math. France 147 (2019), 395–441, Theorem 5.5 and Example 5.7. https://smf.emath.fr/system/files/filepdf/Janson%20Oberg.pdf
4. J. P. Gaivão, M. Laurent and A. Nogueira, *Rotation number of 2-interval piecewise affine maps*, Aequationes Mathematicae, first published 2024-04-22. https://doi.org/10.1007/s00010-024-01064-2
5. P. Guiraud, M. Hernández, A. Meyroneinc and A. Nogueira, *Rotation number and dynamics of 3-interval piecewise affine contractions*, arXiv:2501.16263 (first posted 2025-01-27). https://arxiv.org/abs/2501.16263
