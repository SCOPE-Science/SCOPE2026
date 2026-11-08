# Exact Fourier extension under arbitrary erasures of the cubic graph: an origin-triggered one-pair transition

## Finding

Let \(F\) be any finite field of cardinality \(q\) and characteristic greater than three, and let \(B\subseteq F\) be nonempty. The retained cubic-frequency graph is \(C_B=\{(t,t^3):t\in B\}\). Write \(b=\mathbf1_{\{0\in B\}}\), let \(k\) count intact nonzero antipodal pairs \(\{t,-t\}\subseteq B\), and let \(r=|B|-b-2k\) count unmatched nonzero sites. Let \(m=|B|\).

For any nontrivial additive character \(\psi:F\to\mathbb C\), set
\[
E_Bf(u,v)=q^{-1}\sum_{t\in B}f(t)\psi(ut+vt^3),\qquad
\mathcal R_B^4=\sup_{f\ne0}\frac{\sum_{(u,v)\in F^2}|E_Bf(u,v)|^4}{\left(q^{-1}\sum_{t\in B}|f(t)|^2\right)^2}.
\]
Then the exact sharp coefficient is
\[
\boxed{\mathcal R_B^4=\begin{cases}
2-\dfrac1m,&k=0\text{ or }(b=0,\ k=1),\\[4pt]
3-\dfrac6{3b+4k},& k\ge2\text{ or }(b=1,\ k\ge1).
\end{cases}}
\]
Both branches include *all* nonempty masks, including the single-site mask.

In the first branch, the nonzero extremizers have equal positive coefficient moduli on all sites of \(B\), with completely arbitrary phases. In the second branch, writing \(S=\sum_{t\in B}|f(t)|^2\), every nonzero extremizer is characterized precisely by:

1. \(f\) vanishes on each of the \(r\) unmatched nonzero sites;
2. \(|f(0)|^2=3S/(3b+4k)\) if \(b=1\), and \(|f(t)|^2=2S/(3b+4k)\) on all \(2k\) intact-pair sites;
3. the nonzero products \(f(t)f(-t)\) for the intact pairs have a common complex argument, also equal to the argument of \(f(0)^2\) when \(b=1\).

Every configuration satisfying these conditions is an extremizer. In particular, retaining the center and just *one* complete nonzero antipodal pair forces \(\mathcal R_B^4=15/7\), irrespective of how many unmatched sites remain, and all their coefficients must vanish at equality. Without the center, a single complete antipodal pair has the strictly smaller sharp coefficient \(2-1/m\), and all coefficients are then nonzero and equimodular.

## Assumptions and scope

The source set \(B\) is arbitrary, with no size or symmetry assumption. A nonzero complex input function is allowed to vanish at retained frequencies. All ambient norms use counting measure and each retained coefficient has the *fixed* mass \(q^{-1}\), not \(m^{-1}\). The characteristic exclusions are essential for the cubic pair-sum identity and the antipodal partition; no statement is made for characteristic two or three. Four-power rather than fourth-root constants are reported throughout.

## Proof

Put \(S=\sum_{t\in B}|f(t)|^2\), and extend \(f\) by zero to \(F\). Character orthogonality yields
\[
\sum_{(u,v)\in F^2}|E_Bf(u,v)|^4=q^{-2}Q(f),\qquad
Q(f)=\sum_{a+b=c+d\atop a^3+b^3=c^3+d^3}f(a)f(b)\overline{f(c)f(d)}.
\]
Thus the desired fourth-power quotient equals \(Q(f)/S^2\). For \(s=a+b\ne0\), the identity \(a^3+b^3=s^3-3abs\) implies \(ab=cd\), hence \(\{a,b\}=\{c,d\}\). For \(s=0\), every ordered pair \((t,-t)\), including the diagonal pair \((0,0)\), has cubic sum zero. Define
\[
P_4=\sum_t|f(t)|^4,\qquad
R=\sum_t|f(t)|^2|f(-t)|^2,\qquad
T=\sum_t f(t)f(-t).
\]
The ordinary unordered-pair contribution is \(2S^2-P_4\). Removing its zero-sum portion \(2R-|f(0)|^4\) and inserting the actual zero-sum contribution \(|T|^2\) proves the exact *fiber identity*
\[
\boxed{Q(f)=2S^2-P_4-2R+|f(0)|^4+|T|^2.}\tag{1}
\]

If \(k=0\), or \(b=0\) and \(k=1\), the zero-sum fiber has at most one unordered pair (the center diagonal or one nonzero antipodal pair). Consequently \(|T|^2=2R-|f(0)|^4\), so \(Q(f)=2S^2-P_4\). Cauchy--Schwarz gives \(P_4\ge S^2/m\), with equality exactly at positive constant squared modulus. This proves the first branch and all its equality cases, including arbitrary phases.

Now assume \(k\ge2\) or \(b=k=1\). Normalize \(S=1\). Write \(x=|f(0)|^2\) if the origin is retained, and \(x=0\) otherwise. For each intact pair \(\{t_j,-t_j\}\), put \(U_j=|f(t_j)|^2+|f(-t_j)|^2\), \(V_j=2f(t_j)f(-t_j)\). Let \(y_1,\ldots,y_r\) be the nonnegative squared moduli on unmatched sites and \(W=\sum_\ell y_\ell\). The fiber identity becomes
\[
Q=2-2x^2-\sum_{j=1}^k U_j^2-\tfrac12\sum_{j=1}^k|V_j|^2-\sum_{\ell=1}^r y_\ell^2
+\left|f(0)^2+\sum_{j=1}^k V_j\right|^2,
\qquad x+\sum_jU_j+W=1.
\]
Here \(f(0)=0\) when \(b=0\). The triangle inequality, followed by \(|V_j|\le U_j\), gives
\[
Q\le2-2x^2-\sum_jU_j^2-\sum_\ell y_\ell^2
-\tfrac12\sum_jv_j^2+\bigl(x+\sum_jv_j\bigr)^2
\le2+(x+\sum_jU_j)^2-2x^2-\tfrac32\sum_jU_j^2-\sum_\ell y_\ell^2,
\]
where \(v_j=|V_j|\). For the last step, increase each \(v_j\) up to \(U_j\): the derivative of the displayed quadratic in that variable equals \(2(x+\sum_iv_i)-v_j\ge0\). In the active regime equality in all these steps requires balance \(|f(t_j)|^2=|f(-t_j)|^2=U_j/2\) and alignment of all nonzero pair products, also with \(f(0)^2\) when present.

Weighted Cauchy--Schwarz gives
\[
2x^2+\tfrac32\sum_jU_j^2
\ge\frac{(x+\sum_jU_j)^2}{L},\qquad
L=\frac b2+\frac{2k}3=\frac{3b+4k}6.
\]
In the active regime \(L>1\). Hence
\[
Q\le 2+\left(1-\frac1L\right)(1-W)^2-\sum_\ell y_\ell^2
\le3-\frac1L=3-\frac6{3b+4k}.
\]
Equality in the last inequality forces \(W=0\), and equality in weighted Cauchy--Schwarz forces \(x=3/(3b+4k)\) when \(b=1\) and \(U_j=4/(3b+4k)\) for every pair. Together with pairwise balance and phase alignment this is exactly the stated extremizer family, whose members attain all inequalities. The case \(r=0\) is included with empty sums. The argument is independent of field cardinality except for the characteristic and existence of the specified mask. This proves the theorem.

## Verification

The standalone Python file `verify_cubic_erasures.py` independently implements the two-sum convolution, the fiber identity (1), and an explicit equality case for each mask. It exhausts all \(2^q-1\) nonempty masks for prime fields of orders five, seven and eleven, and samples 350 additional masks over the prime field of order thirteen. It tests 5,109 random complex integer coefficient vectors for the exact fiber identity and the predicted upper bound. Running `python3 verify_cubic_erasures.py` yields `CUBIC_ERASURES_VERIFY_PASS masks=2555 random_tests=5109 primes=5,7,11,13`. Finite checks corroborate rather than establish the all-prime-power theorem.

## Relationship to prior work

González-Riquelme and Oliveira e Silva (2024) develop sharp finite-field Fourier extension theory for parabolic and conic geometries, but their examined theorems do not give exact constants and all extremizers for arbitrary erasure masks of the odd cubic graph. The published full-cubic-graph theorem listed below computes \(\mathcal R_F^4=3-6/(2q+1)\) and its extremizers for the *unrestricted* frequency set \(B=F\); it does not determine what happens after arbitrary deletions. A published arbitrary-mask theorem for norm-one centered conics gives the analogous pair-count law **without an additive neutral site**, and therefore already covers the origin-free part of the present dichotomy at the abstract collision level. It does **not** give the origin-triggered one-pair branch: a norm-one conic contains no origin and no triple of collinear points, whereas the cubic graph contains the collinear triple \(\{(-t,-t^3),(0,0),(t,t^3)\}\). The genuinely new content relative to these results is the full classification for partial masks *containing the cubic origin*, its exact sharp interpolation between the full-graph and incomplete-pair cases, and the one-pair extinction threshold. The proof isolates these effects as the contribution of the central diagonal to the exceptional zero-sum convolution fiber.

## Limitations

Only the exponent-four norm in characteristic greater than three is treated. The theorem does not address higher extension moments, arbitrary general curves, best constants when the surviving frequencies are renormalized by their cardinality, or stability of near extremizers. The already known full-support cubic theorem and origin-free antipodal-mask algebra are not claimed as new. A potentially broader general theorem for additive sets with a unique exceptional sum fiber could subsume the new centered-mask branch; no such encompassing theorem was located in the checked primary literature and mathematical records. No independent mathematical audit has been performed.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1 (first public 2024-05-26), https://arxiv.org/abs/2405.16647 .
2. *Exact sharp finite-field cubic-graph \(L^2\) to \(L^4\) extension norm and extremizers*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-sharp-finite-field-cubic-graph-l-2-to-l-4-extension-norm-a--2db777d1e47b .
3. *Sharp Fourier extension and phase transitions under arbitrary erasures of finite-field conics*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourier-extension-and-phase-transitions-under-arbitrary-er--6b59f93aeabe .
4. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1 (first public 2002-04-18), https://arxiv.org/abs/math/0204234 .
