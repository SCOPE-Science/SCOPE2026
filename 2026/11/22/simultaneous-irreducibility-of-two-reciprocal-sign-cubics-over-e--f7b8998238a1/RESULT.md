# Simultaneous irreducibility of two reciprocal-sign cubics over every prime field

## Finding
For every prime \(p\), let \(N_p\) be the number of \(c\in\mathbb F_p\) for which both
\[
P_c(X)=X^3+c(X^2+X+1),\qquad Q_c(X)=X^3+c(X^2-X+1)
\]
are irreducible over \(\mathbb F_p\). Then
\[
\boxed{N_p>0\quad\Longleftrightarrow\quad p\notin\{2,3,5,13\}.}
\]
For every prime \(p\ge11\), the following *explicit* inequality holds:
\[
\boxed{\bigl|9N_p-(p+1)\bigr|\le 26\sqrt p+93.}
\]
In particular \(N_p=p/9+O(\sqrt p)\), with a uniform, stated constant. There are at least two qualifying parameters for every prime \(p\ge7\) other than \(13\), since qualifying parameters occur in opposite pairs.

## Assumptions and scope
The base fields are exactly the prime fields \(\mathbb F_p\), not arbitrary extension fields. All irreducibility statements mean irreducibility of the indicated monic degree-three polynomial in \(\mathbb F_p[X]\). The parameter \(c=0\) does not qualify. The estimate is asserted only for \(p\ge11\); the exact exception classification includes smaller primes by direct finite calculation. The chosen family is the degree-three, sign-paired specialization of the geometric-series polynomial family studied by Jones (2026); no monogenicity conclusion is asserted here.

## Proof
**1. Reduce the pair to opposite parameters.** Let \(S(X)=X^2+X+1\), \(f_t(X)=X^3+tS(X)\). The identity
\[
Q_c(-X)=-f_{-c}(X)
\]
shows that both original cubics are irreducible exactly when \(f_c\) and \(f_{-c}\) are irreducible. In particular, \(N_p\) is even for odd \(p\).

**2. Rational parameter cover and branch data.** For \(f_t(X)\), a root \(X\) determines
\[
t=R(X)=-\frac{X^3}{X^2+X+1}.
\]
The map \(R:\mathbb P^1_X\to\mathbb P^1_t\) has degree three. Its derivative and the cubic discriminant are
\[
R'(X)=-\frac{X^2(X^2+2X+3)}{(X^2+X+1)^2},
\qquad \operatorname{disc}_X(f_t)=-t^2(3t^2-14t+27).
\]
For characteristic \(p\ge11\), there is one totally ramified point of index three above \(t=0\), and exactly two other simple branch points of index two at the distinct roots of \(B_-(t)=3t^2-14t+27\). No branching occurs over infinity. Indeed, the derivative shows the complete ramification, and \(\operatorname{disc}(B_-)=-128\ne0\) in these characteristics. For \(f_{-t}\), the two index-two branch values instead satisfy \(B_+(t)=3t^2+14t+27\). Their two root sets do not intersect, since
\[
\operatorname{Res}_t(B_-,B_+)=63504=2^4\,3^4\,7^2,
\]
and none of the four nonzero values is \(t=0\).

Each degree-three function-field extension is connected and has tame inertia of cycle types \((3)\) and \((2,1)\); hence its geometric Galois closure has full \(S_3\) monodromy. Its unique quadratic quotient is given by the square class of \(B_-\), respectively \(B_+\), up to a nonzero scalar. These classes are independent over \(\overline{\mathbb F}_p(t)\): each has two simple zeros absent from the other. A common quotient of two \(S_3\)-extensions, if nontrivial, has to include their unique quadratic quotients. Therefore the two splitting fields are linearly disjoint, and the composite geometric group is \(S_3\times S_3\). The arithmetic group embeds in that product and contains the geometric product, so the arithmetic group is also \(S_3\times S_3\), with full constant field \(\mathbb F_p\).

**3. Genus and a numerical Chebotarev estimate.** Denote by \(Y_p\to\mathbb P^1_t\) the smooth projective Galois cover of degree \(36\) for the composite splitting field. Above \(t=0\) its geometric inertia has order three: both local cubic covers use the same tame cube-root parameter. The four other geometric branch values have inertia order two. Riemann–Hurwitz gives
\[
2g(Y_p)-2=36(-2)+36(1-1/3)+4\cdot36(1-1/2)=24,
\]
so \(g(Y_p)=13\).

Fix a pair \(g=(\sigma,\sigma)\in S_3\times S_3\), where \(\sigma\) is a three-cycle, and form the Frobenius twist \(Y_p^{(g)}\) of this Galois cover. This twist is geometrically isomorphic to \(Y_p\), so it is a smooth projective genus-thirteen curve over \(\mathbb F_p\). Over an unramified rational parameter \(t\), its rational fiber has exactly \(\lvert C_{S_3\times S_3}(g)\rvert=9\) points when the two cubic Frobenius permutations are three-cycles, and otherwise zero. Thus every qualifying parameter contributes exactly nine rational points.

The remaining rational points lie above the at most six exceptional geometric parameters: \(t=0\) (at most \(36/3=12\) points), the four roots of \(B_-B_+\) (each at most \(36/2=18\) points), and \(t=\infty\) (at most nine rational points, by the centralizer calculation for an unramified fiber). Consequently
\[
\#Y_p^{(g)}(\mathbb F_p)=9N_p+E_p,\qquad 0\le E_p\le12+4(18)+9=93.
\]
The Weil bound for the smooth curve gives
\[
\left|\#Y_p^{(g)}(\mathbb F_p)-(p+1)\right|\le 26\sqrt p,
\]
which proves the stated explicit inequality.

**4. A finite cutoff and complete exact sieve.** For every integer \(p\ge851\), one has \(p+1-26\sqrt p-93>0\). This follows by checking the inequality at \(851\) and that its left side is increasing for \(p\ge851\). Hence every prime \(p\ge851\) has \(N_p>0\). It remains to test the \(146\) primes \(p\le850\). A cubic over a field is reducible if and only if it has a root; for any such prime, the exact set of parameters for which \(f_c\) has a root is
\[
T_p=\left\{-x^3\bigl(x^2+x+1\bigr)^{-1}:x\in\mathbb F_p,\ x^2+x+1\ne0\right\}.
\]
Therefore
\[
N_p=p-\lvert T_p\cup(-T_p)\rvert.
\]
The standalone standard-library checker `verify.py` enumerates the complete set \(T_p\) over every prime through \(850\), independently checks the cubic-root definition for each prime through \(101\), and finds \(N_p=0\) precisely for \(p\in\{2,3,5,13\}\). This is a finite exhaustive proof for the remaining range, not a sampling extrapolation. Together with step 3 this proves the equivalence for all primes.

## Verification
Run `python3 verify.py` in the extracted directory. It uses the exact prime sieve up to \(850\), exact modular inverses and exact finite sets; no external packages, randomization or numerical approximations enter the finite certificate. The checker verifies \(146\) prime characteristics, finds the four exceptions, and cross-checks the direct cubic-root condition at every prime through \(101\). Independent symbolic algebra checks confirm the derivative, discriminant and resultant identities written above. The infinite assertion depends on the proved Galois-cover geometry and Weil's bound; the enumerator alone establishes only the finite cutoff.

## Relationship to prior work
Lenny Jones's 2026 study introduces and investigates monogenicity for the geometric-series polynomial family of which the two cubics are a natural sign-paired specialization. It does not classify their simultaneous irreducibility over all prime fields. Pan (2025) studies simultaneous irreducibility for a distinct quadratic-and-cubic pair, and is a close finite-field analogue rather than an instance of this claim. General simultaneous-specialization Chebotarev results, including Andrade–Bary-Soroker–Rudnick's effective function-field formulation and Bary-Soroker's exposition, imply an asymptotic \(p/9+O(\sqrt p)\) after the monodromy is established. The potentially new contribution here is the **specific genus-thirteen cover, fully explicit numerical error, finite cutoff, and exact all-prime exception classification**. None of the foregoing general results, by itself, gives the displayed exceptional-prime list.

## Limitations
The proof uses standard non-elementary results (the Weil bound and the existence of a Frobenius twist of a finite Galois cover); these are invoked, not reproved. The explicit error constant is not claimed to be optimal. The result concerns prime fields, not general \(\mathbb F_{p^m}\). General literature could contain a logically stronger specialization theorem with an explicitly evaluated threshold for this exact pair; that residual priority risk is not mathematically eliminated by search. No independent mathematical audit has been performed.

## References
- L. Jones, *The monogenicity of \(x^n+c\sum_{j=0}^{n-1}a^{n-j-1}x^j\)*, arXiv:2611.20332v1, first public 15 November 2026. https://arxiv.org/html/2611.20332v1
- E. X. Pan, *A note on some quadratics and cubics over finite fields*, *Bulletin of the Australian Mathematical Society* 113 (2026), 447–454, first online 28 November 2025. https://doi.org/10.1017/S0004972725100671
- J. C. Andrade, L. Bary-Soroker and Z. Rudnick, *Shifted convolution and the Titchmarsh divisor problem over \(\mathbb F_q[t]\)*, *Philosophical Transactions of the Royal Society A* 373 (2015), 20140308, Appendix A: explicit Chebotarev theorem. https://doi.org/10.1098/rsta.2014.0308
- L. Bary-Soroker, *Field arithmetician's blog*, section “Irreducible Specializations,” explaining general simultaneous irreducibility asymptotics. https://liorbarysoroker.wordpress.com/
