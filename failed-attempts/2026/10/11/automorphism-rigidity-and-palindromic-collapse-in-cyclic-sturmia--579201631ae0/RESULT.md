# Automorphism rigidity and palindromic collapse in cyclic Sturmian lifts

## Finding
For every irrational \(\alpha\in(0,1)\) and integer \(k\ge3\), the cyclic first-difference lift of the Sturmian subshift of slope \(\alpha\) is strictly ergodic, and its full automorphism group is
\[
\operatorname{Aut}(X_{\alpha,k},\sigma)\cong \mathbb Z\times\mathbb Z/k\mathbb Z.
\]
It is measurably conjugate to rotation by \(\alpha\) on a circle of circumference \(k\); its eigenvalues are exactly \(\exp(2\pi i m\alpha/k)\), for integer \(m\). Its word complexity is \(p(n)=kn\), while its palindrome complexity has a sharp cutoff:
\[
 P(n)=\begin{cases}k,&1\le n\le\lceil1/\alpha\rceil,\\0,&n>\lceil1/\alpha\rceil.\end{cases}
\]
Thus no nonconstant palindrome occurs, and sufficiently long palindromes are absent altogether.

## Assumptions and scope
The phase space is the full two-sided shift on \(\mathbb Z/k\mathbb Z\), with left shift \((\sigma x)_j=x_{j+1}\). Let \(Y_\alpha\) denote the orbit closure of the mechanical Sturmian sequences \(y_j=\lfloor t+(j+1)\alpha\rfloor-\lfloor t+j\alpha\rfloor\), with \(t\in\mathbb R\). Define
\[
 X_{\alpha,k}=\{x:\ (x_{j+1}-x_j\bmod k)_{j\in\mathbb Z}\in Y_\alpha\}.
\]
A word of length \(n\) is any contiguous factor of a point of this shift. A palindrome equals its reversal. An automorphism is a homeomorphism commuting with \(\sigma\). The theorem concerns all irrational slopes, without bounded-continued-fraction or substitution assumptions, and every integer alphabet size \(k\ge3\).

## Proof
**1. A geometric coding and its fibers.** Write \(\mathbb T_k=\mathbb R/k\mathbb Z\), and for a phase outside the countable set \(S=\{a+j\alpha\bmod k:a,j\in\mathbb Z\}\), set
\[
 x(t)_j=\lfloor t+j\alpha\rfloor\bmod k.
\]
Its successive symbol differences equal the mechanical Sturmian coding with slope \(\alpha\). At each \(t\in S\), there are precisely two limiting codings, obtained by approaching the phase from opposite sides, differing at exactly one spatial coordinate. This follows since irrationality prevents two distinct indices from simultaneously hitting integer boundaries. Conversely each bi-infinite mechanical Sturmian code, including both boundary codings, integrates modulo \(k\) uniquely after fixing one symbol; every point of the preimage lift consequently arises from one of the geometric codings.

Form the closed graph \(\Gamma\subset\mathbb T_k\times X_{\alpha,k}\) of the phase-coding map. If \(t\ne t'\) modulo \(k\), then some integer translate of the dense irrational orbit places the two phases in distinct interiors of unit intervals modulo \(k\); thus their full symbolic codings differ. Therefore projection \(\Gamma\to X_{\alpha,k}\) is a continuous bijection from compact to Hausdorff, hence a homeomorphism. Its inverse followed by projection defines a continuous factor \(\pi:X_{\alpha,k}\to\mathbb T_k\) with \(\pi(\sigma x)=\pi(x)+\alpha\). The fiber above any phase outside \(S\) is a singleton; precisely the phases in \(S\) have two points, and those differ at one coordinate.

**2. Strict ergodicity and measurable spectrum.** Rotation by irrational \(\alpha\) on \(\mathbb T_k\) is minimal and uniquely ergodic. A cylinder of the symbolic extension containing a boundary coding also contains codings from a nonempty adjacent open interval of phases, so dense forward orbit visits show that every point of \(X_{\alpha,k}\) has dense orbit. Every invariant probability pushes forward under \(\pi\) to Lebesgue measure on \(\mathbb T_k\), and the fibers are singletons off the countable null set \(S\). Thus there is exactly one invariant probability, the pullback through the almost-everywhere inverse of \(\pi\). This gives a measure-theoretic isomorphism to the rotation and hence the stated pure point eigenvalue group.

**3. All automorphisms.** Let \(H\) be an automorphism. Points in the same two-element \(\pi\)-fiber differ at a single coordinate, so their iterates under the shift approach each other in both time directions. Uniform continuity and shift-commutation imply their images under \(H\) also approach each other, hence have equal \(\pi\)-coordinate because \(\pi\) is continuous and rotation preserves circle distance. Thus \(\pi H\) is constant on every fiber and descends to a continuous map \(g:\mathbb T_k\to\mathbb T_k\). Applying the same reasoning to \(H^{-1}\) shows that \(g\) is a homeomorphism. It commutes with irrational rotation, and the dense orbit forces \(g(t)=t+\beta\) for one \(\beta\in\mathbb T_k\).

Since \(H\) maps each \(\pi\)-fiber bijectively onto its image fiber, \(g\) preserves the set \(S\) of double-fiber phases. As \(0\in S\), we have \(\beta=j\alpha+a\bmod k\) for an integer \(j\) and an integer \(a\). This translation on the circle is precisely induced by \(\sigma^j\tau_a\), with \((\tau_a x)_n=x_n+a\bmod k\). The composition \((\sigma^j\tau_a)^{-1}H\) acts trivially on the base. It therefore fixes every singleton fiber and by density every point, proving \(H=\sigma^j\tau_a\). If \(\sigma^j\tau_a\) is the identity, then \(j\alpha+a\equiv0\pmod k\); irrationality forces \(j=0\), and then \(a=0\pmod k\). This establishes the direct-product group without hidden symmetries.

**4. Word and palindrome counts.** Within any half-open unit interval of phases (fixing the first symbol), the length-\(n\) itinerary changes at the \(n-1\) distinct fractional breakpoints \(-j\alpha\bmod1\), for integers \(1\le j<n\). These divide the unit interval into \(n\) positive-length atoms whose words differ: the difference sequence determines the slope itinerary, and the initial symbol is fixed. The \(k\) possible first symbols give \(p(n)=kn\).

Every adjacent increment of an admissible word lies in \(\{0,1\}\bmod k\). If a palindrome has an increment of \(1\), reversing the palindrome forces a corresponding increment of \(-1\), impossible for \(k\ge3\). Every palindromic word is therefore constant. A constant length-\(n\) word exists precisely when all \(n-1\) successive mechanical increments vanish; the interval of phases for this event has positive length exactly when \((n-1)\alpha<1\). For irrational \(\alpha\), this is equivalent to \(n\le\lceil1/\alpha\rceil\). Constant symbol translation produces each of the \(k\) different constant words, completing the palindrome formula.

## Verification
The accompanying `verify.py` runs exhaustive exact-fraction finite-period analog checks for two reduced rational slopes, \(89/144\) and \(71/171\), and alphabet sizes \(3,4,5,7\). It checks factor and palindrome counts, adjacency increments, and the sharp constant-palindrome cutoff for lengths \(1\) through \(15\). The program reports `FINITE_RATIONAL_CHECKS_PASS 4920`. These are exact finite consistency tests of the combinatorial formulas, **not** a computational proof of the irrational-rotation or automorphism assertions; those follow from the arguments above.

## Relationship to prior work
Kang and Jäger (2026) establish the general skew-product framework for permutative sliding-block lifts and strict ergodicity for several substitution families, including noble-means and Tribonacci shifts; the first-difference rule treated here is their two-block case. The present theorem treats **every irrational Sturmian slope** (including non-substitutive and non-linearly recurrent cases) and additionally identifies the *full* automorphism group, rotation spectrum, exact complexity, and the sharp disappearance of palindromes when the alphabet has at least three symbols. Rote (1993) studies binary sequences of complexity \(2n\), relevant to the excluded binary boundary; Blondin-Massé and coauthors study palindromes for binary rotation codings. Cyr and Kra's general low-complexity automorphism theorem constrains such groups abstractly but does not identify the exact direct product for this family.

## Limitations
The conclusion is specific to the first-difference lift with alphabet size at least three, not arbitrary permutative block maps. It does not give quantitative convergence rates of Birkhoff sums and does not extend the palindrome formula to the binary case, where reversal of a \(+1\) increment is allowed. Existing general work on rotation codings and automorphism groups could contain an equivalent specialization not found in the compared literature. 

## References
- Z. Kang and T. Jäger, *On lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1, first public September 1, 2026, https://arxiv.org/html/2609.01140v1 .
- G. Rote, *Sequences with subword complexity \(2n\)*, 1993, https://page.mi.fu-berlin.de/rote/Papers/abstract/Sequences%2Bwith%2Bsubword%2Bcomplexity%2B2n.html .
- V. Cyr and B. Kra, *The automorphism group of a shift of linear growth: Beyond transitivity*, 2015, https://doi.org/10.1017/fms.2015.3 .
- A. Blondin-Massé et al., *Palindromic complexity of codings of rotations*, 2011, https://archipel.uqam.ca/8430/ .
