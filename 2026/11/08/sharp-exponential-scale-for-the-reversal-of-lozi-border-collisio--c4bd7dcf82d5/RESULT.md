# Sharp exponential scale for the reversal of Lozi border-collision order

## Finding
For the orientation-preserving Lozi family and the two periodic-orbit creation curves \(l_{m,2}\) and \(l_{m,3}\) defined by Ou's itineraries, there is, for every sufficiently large integer \(m\), a unique intersection at \((a_m^*,b_m^*)\) in one common parameter neighborhood of \((2,0)\). The transverse crossing parameter has the **sharp constant**
\[
\boxed{\lim_{m\to\infty}2^{m+2}b_m^*=1.}
\]
In addition \(a_m^*\to2\). Thus a parameter perturbation of order \(2^{-m}\), with leading coefficient \(1/4\), is sufficient and necessary at the leading scale to reverse the creation order of these two length-\(m+2\) and length-\(m+3\) periodic itineraries. The crossing existence and transversality are established in the source; the sharp asymptotic constant is the present quantitative conclusion.

## Assumptions and scope
For \(a>1\), \(b\ge0\) sufficiently small, define
\[
\Lambda_{a,b}(x,y)=(a-b-1-a|x|-by,\,x).
\]
For integers \(m\ge5\), \(n\in\{2,3\}\), consider Ou's words
\[
\iota_{\sigma,m,n}=+\,(-)^{m-2}\,++\,(-)^{n-2}\,\sigma,\qquad\sigma\in\{-,+\}.
\]
In the parameter neighborhood provided by Ou's Theorem 6.6 and Corollary 6.7, \(a=l_{m,n}(b)\) is the unique border-collision creation threshold for the corresponding pair of formal periodic words. The curves are analytic and have \(l_{m,2}'(b)>l_{m,3}'(b)\) on a common interval \([0,\bar b]\), for all sufficiently large \(m\). The crossing is the unique solution \(l_{m,2}(b_m^*)=l_{m,3}(b_m^*)\) in that interval. At \(b=0\) the planar dynamics reduces to the tent-type map \(S_a(x)=a-1-a|x|\). This statement is for these precise itinerary pairs, not all Lozi orbit-creation curves.

## Proof
**1. Uniform analytic-curve input and limiting slopes.** Ou's Theorem 6.6 and Corollary 6.7 establish the curves on a common fixed \([0,\bar b]\), their strict derivative ordering, and convergence with first derivatives to limiting thresholds determined by \(p_{\infty,n}(a,b)-r_\infty(a,b)=0\). Their uniform convergence follows from the first-derivative convergence in Corollaries 5.11 and 5.22 and the nonvanishing \(a\)-derivative of the root equation. At \(b=0\), the limiting thresholds both equal \(a=2\). In the source, Lemma 6.4 states
\[
\left.\partial_b p_{\infty,2}\right|_{b=0}=a^{-1}-2,\qquad
\left.\partial_b p_{\infty,3}\right|_{b=0}=-a^{-1},
\]
and \(p_{\infty,n}(a,0)=a-1\). The explicit stable-lamination endpoint from Proposition 5.28 is
\[
r_\infty(a,b)=1-\frac{(\lambda+2)b}{a\lambda+b},\qquad
\lambda=\frac{a+\sqrt{a^2-4b}}2.
\]
Thus \(\partial_a(p_{\infty,n}-r_\infty)(2,0)=1\), \(\partial_b r_\infty(2,0)=-1\), and implicit differentiation yields
\[
l_{\infty,2}'(0)=\frac12,\qquad l_{\infty,3}'(0)=-\frac12.
\]
Consequently, after choosing a possibly smaller fixed neighborhood, the difference \(d_m(b)=l_{m,2}(b)-l_{m,3}(b)\) satisfies \(d_m'\to d_\infty'\) locally uniformly and \(d_\infty'(0)=1\). For each fixed sufficiently small \(b_0>0\), \(d_\infty(b_0)>0\), and hence \(d_m(b_0)>0\) for large \(m\).

**2. Exact tent-family border equation.** At \(b=0\), rotate the source's border itinerary to start at its zero-coordinate switching point, assigning the first boundary symbol \(+\). The resulting formal word is \(++(-)^{m-2}++(-)^{n-2}\). Starting at \(x_0=0\) and applying \(S_a\) according to that word gives, by the affine recursion \(x\mapsto(a-1)\mp ax\),
\[
x_{m+n}=a^{m+n-1}(2-a)-2a^{n-1}(a-1)-1.
\]
A border-collision periodic point therefore satisfies exactly
\[
\boxed{a^{m+n-1}(2-a)=2a^{n-1}(a-1)+1.}\tag{1}
\]
(The second coordinate at \(b=0\) is chosen as the preceding first coordinate, ensuring the full planar return.) The source's existence, uniqueness and admissibility theorem identifies the root tending to \(2\) with \(a_{m,n}:=l_{m,n}(0)\). In particular \(a_{m,n}\to2\).

**3. Tent-family separation constant.** Rewriting (1), for \(n=2,3\),
\[
2-a_{m,n}=\frac{2a_{m,n}^{n-1}(a_{m,n}-1)+1}{a_{m,n}^{m+n-1}}.
\]
Since \(a_{m,n}\to2\), the right side is at most \(C(2-\varepsilon)^{-m}\) for any fixed small \(\varepsilon>0\) and all sufficiently large \(m\), implying \(m(2-a_{m,n})\to0\). Hence \((2/a_{m,n})^m\to1\), so
\[
\lim_{m\to\infty}2^m(2-a_{m,2})=\frac52,\qquad
\lim_{m\to\infty}2^m(2-a_{m,3})=\frac94.
\]
Subtracting yields the decisive difference
\[
\boxed{\lim_{m\to\infty}2^m\bigl(l_{m,3}(0)-l_{m,2}(0)\bigr)=\frac14.}\tag{2}
\]
In particular \(d_m(0)<0\) for all sufficiently large \(m\).

**4. Unique crossing and asymptotic.** By Step 1, \(d_m(b_0)>0\) for large \(m\), while Step 3 gives \(d_m(0)<0\). Strict positivity of \(d_m'\) on \([0,b_0]\) gives exactly one zero \(b_m^*\in(0,b_0)\). By (2) and the source's common positive derivative lower bound, \(b_m^*=O(2^{-m})\); thus \(b_m^*\to0\). The mean-value theorem gives \(0=d_m(0)+b_m^*d_m'(\xi_m)\) for some \(0<\xi_m<b_m^*\). First-derivative convergence and \(d_\infty'(0)=1\) show \(d_m'(\xi_m)\to1\). Equation (2) therefore yields \(2^m b_m^*\to1/4\), equivalent to the displayed theorem. Finally \(a_m^*=l_{m,2}(b_m^*)\to2\) by uniform convergence.

## Verification
The proof's nonstandard inputs are precisely identified in Ou: the threshold and admissibility theorem (Theorem 6.6), uniform derivative comparison (Corollary 6.7, using Corollaries 5.11 and 5.22), the limiting derivatives (Lemma 6.4), and the explicit expression for \(r_\infty\) (Proposition 5.28). Equation (1) follows from a direct two-branch affine recursion, not from numerical extrapolation. The accompanying pure-Python verifier checks that recurrence identity exactly as a polynomial identity for a finite range of integers and approximately locates crossing parameters as a consistency check. For example the computed values of \(2^{m+2}b_m^*\) for \(m=6,8,10,12\) are about \(1.1574317,1.0450201,1.0132971,1.0038965\). Finite tests are not used to prove the limit.

## Relationship to prior work
Ou's 2022 article proves the existence and uniqueness of transverse reversal crossings and the relevant analytic-curve and geometric convergence theory, including the essential derivative inputs. It does not state the sharp exponential crossing scale or its leading coefficient. Ishii (1997) develops a Lozi kneading/pruning framework, but the inspected available abstract does not give the two selected curve-crossing asymptotic. Sushko–Avrutin–Gardini (2023) analytically study rotation-number \(1/n\) periodicity-region boundaries for an embedding into the border-collision normal form; the accessible abstract concerns different periodicity regions, and its full text was unavailable for comparison. Exact equivalence in unindexed supplementary or inaccessible text is a residual priority risk, not a claimed proof of absolute novelty.

## Limitations
The conclusion is an asymptotic for the specific orbit-pair thresholds \(l_{m,2}\) and \(l_{m,3}\), not an upper bound for all border-collision parameters. It relies on the source's proved analytic-curve theorems and their derivative convergence, rather than independently reproving the whole Lozi admissibility classification. It does not assert a global bifurcation classification for arbitrary \(b\), nor a specified finite-\(m\) error term. Its originality is subject to further literature inspection; independent validation has not occurred.

## References
1. D.-S. Ou, *Critical points in higher dimensions, I: Reverse order of periodic orbit creations in the Lozi family*, arXiv:2203.02326, v1 4 March 2022, v2 3 October 2022. Theorems 6.6 and 7.1, Corollaries 5.11, 5.22 and 6.7, Lemma 6.4, Proposition 5.28. https://arxiv.org/html/2203.02326v2
2. Y. Ishii, *Towards a kneading theory for Lozi mappings I: A solution of the pruning front conjecture and the first tangency problem*, Nonlinearity 10 (1997), 731–747. https://doi.org/10.1088/0951-7715/10/3/008
3. I. Sushko, V. Avrutin and L. Gardini, *Lozi map embedded into the 2D border collision normal form*, J. Difference Equations Appl. (2023). https://doi.org/10.1080/10236198.2023.2205960
