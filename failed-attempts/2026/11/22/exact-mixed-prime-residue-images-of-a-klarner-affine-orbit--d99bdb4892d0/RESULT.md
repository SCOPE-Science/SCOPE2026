# Exact mixed-prime residue images of a Klarner affine orbit

## Finding

Let \(S\) be the least subset of \(\mathbb Z_{\geq0}\) containing \(0\) and closed under
\(A(x)=2x\), \(B(x)=3x+2\), and \(C(x)=6x+3\).
For every \(b\geq1\) and every odd positive integer \(u\) coprime to \(3\), put
\(m=2\cdot3^bu\). The exact image \(S_m=S\bmod m\) is the following disjoint union:

\[
S_m=\{x\bmod m:x\equiv0\pmod2\}
\;\sqcup\;\bigsqcup_{j=0}^{b-1}
\{x\bmod m:x\equiv4\cdot3^j-1\pmod{2\cdot3^{j+1}}\}
\;\sqcup\;
\{x\bmod m:x\equiv-1\pmod{2\cdot3^b}\}.
\]

Thus \(S_m\) contains precisely

\[
|S_m|=\frac{u(3^{b+1}+1)}2,
\qquad \frac{|S_m|}{m}=\frac34+\frac1{4\cdot3^b}.
\]

The projective residue closure \(\overline S\subset\mathbb Z/2\mathbb Z\times\mathbb Z_3\) has Haar measure exactly \(3/4\). Its even slice is complete; its odd slice consists of the point \(-1\) and all \(3\)-adic integers \(z\) for which \(z+1\neq0\) has its first nonzero ternary digit equal to \(1\). More explicitly,

\[
\overline S=(\{0\}\times\mathbb Z_3)\cup
\bigl(\{1\}\times\{-1\}\bigr)\cup
\bigcup_{j\geq0}\Bigl(\{1\}\times
\bigl(-1+3^j(1+3\mathbb Z_3)\bigr)\Bigr).
\]

Here \(\mathbb Z/2\mathbb Z\times\mathbb Z_3\) records parity and the compatible residue classes modulo powers of \(3\); it is not a claim about ordinary asymptotic density in \(\mathbb N\).

## Assumptions and scope

The source set is exactly \(S=\langle A,B,C:0\rangle\), using finite compositions of the three stated maps. Residues are taken in \(\mathbb Z/m\mathbb Z\), and congruence conditions in the displayed union are well-defined because their moduli divide \(m\). The theorem covers all \(m\) with \(v_2(m)=1\) and \(v_3(m)\geq1\); the coprimality \(\gcd(u,6)=1\) is mandatory. It does not prescribe the image for \(v_2(m)\geq2\).

## Proof

**1. Every odd modulus is covered.** First let \(u\geq1\) be coprime to \(6\). Modulo \(u\), both \(A\) and \(B\) are affine permutations, and positive powers of each realize its inverse. The two compositions are
\(A\circ B(x)=6x+4\) and \(B\circ A(x)=6x+2\). Their quotient \((A\circ B)\circ(B\circ A)^{-1}\) is translation by \(2\). Therefore the orbit of \(0\) under the finite permutation group contains all \(u\) residues (because \(2\) is invertible modulo odd \(u\)). In particular \(S\bmod u=\mathbb Z/u\mathbb Z\).

If \(N\) is any odd positive integer and \(S\bmod N\) is complete, then \(S\bmod3N\) is complete. Indeed, the maps \(C(x)=3(2x+1)\), \(A\circ B(x)=3(2x+1)+1\), and \(B(x)=3x+2\) attain, respectively, every class in the residue families \(0,1,2\pmod3\) modulo \(3N\), as \(x\) ranges through representatives of \(S\bmod N\). This works since \(2\) is invertible modulo \(N\). Induction proves
\(S\bmod N=\mathbb Z/N\mathbb Z\) for every odd \(N\).

**2. The even classes are complete.** Because \(A(s)=2s\in S\) and \(S\) is surjective modulo the odd number \(m/2=3^bu\), every even class modulo \(m\) occurs.

**3. Every odd orbit value has a rigid terminal form.** The map \(A\) always makes an even value; \(B\) preserves parity; \(C\) always makes an odd value. Hence an odd element must have a last application of \(C\), followed only by some \(j\geq0\) applications of \(B\). Its form is \(B^j(C(s))\), where \(s\in S\). Since \(B(x)+1=3(x+1)\),

\[
 B^j(C(s))+1=2\cdot3^j(3s+2).
\]

If \(j<b\), the right side has exact \(3\)-adic valuation \(j\); its normalized \(3\)-adic unit is \(1\pmod3\) after dividing by \(3^j\). This is equivalent to
\(B^j(C(s))\equiv4\cdot3^j-1\pmod{2\cdot3^{j+1}}\). If \(j\geq b\), the value is congruent to \(-1\pmod{2\cdot3^b}\). These are the only possibilities for odd members.

**4. Every permitted odd class occurs.** Fix \(0\leq j<b\), and consider a residue in the corresponding congruence class modulo \(m\). After adding \(1\) and dividing by \(2\cdot3^j\), the required normalized residue is \(2\pmod3\). Writing it as \(3s+2\) is therefore equivalent to specifying \(s\bmod 3^{b-j-1}u\). As this is an odd modulus and Step 1 gives complete surjectivity, some \(s\in S\) realizes the residue through \(B^j(C(s))\). For the terminal class \(-1\pmod{2\cdot3^b}\), choose \(j=b\); the same expression varies over all \(u\) choices because \(3\) is a unit modulo \(u\) and \(S\bmod u\) is complete. Thus every class in the claimed union occurs.

**5. Count and inverse limit.** The even branch has \(3^bu\) classes. For each \(j<b\), the corresponding odd branch has \(3^{b-j-1}u\) classes; the final odd branch has \(u\). Distinct \(j\) are disjoint by their different exact \(3\)-adic valuations of \(x+1\). Therefore

\[
|S_m|=3^bu+u\sum_{j=0}^{b-1}3^{b-j-1}+u
=\frac{u(3^{b+1}+1)}2.
\]

Taking the compatible images modulo \(2\cdot3^b\), the even slice is all of \(\mathbb Z_3\), and the odd slice is the disjoint union of the \(3\)-adic balls \(-1+3^j(1+3\mathbb Z_3)\) together with their limiting point \(-1\). The odd slice has normalized \(3\)-adic Haar mass
\(\sum_{j\geq0}3^{-(j+1)}=1/2\), whereas the even slice has mass \(1\) conditional on parity. Their mixture therefore has Haar mass \(1/2+(1/2)(1/2)=3/4\), proving the final assertion.

## Verification

The standalone standard-library program `verify.py` computes exact reachable residue sets by breadth-first closure in \(\mathbb Z/m\mathbb Z\) and constructs the theorem's disjoint union independently. Executing `python3 verify.py` confirms 70 exact modular-image comparisons across \(1\leq b\leq7\), eight coprime cofactors, and 14 additional odd-modulus cases; it checks the predicted cardinality at every tested mixed modulus. These finite checks are independent corroboration of the proof, not an argument for untested moduli or for inverse-limit measure.

## Relationship to prior work

Shamazov and Talambutsa, *On orbit sets generated by semigroups of one-dimensional affine functions* (arXiv:2507.06875v1, 9 July 2025), explicitly identify the Klarner triple \((0,2,3)\) at slopes \((2,3,6)\), but their results concern growth, freeness, and exact-covering systems, not the detailed mixed-prime reachable-residue image. Klarner and Rado (1974) establish general arithmetic properties of recursively defined sets; their reviewed results do not state the displayed all-depth image formula.

An earlier exact congruence-locality theorem for this very orbit proves \(S\bmod m\) is full precisely when \(6\nmid m\). It is stronger on the *surjectivity yes/no question across all moduli*, but does not imply the missing mixed-prime residue classes, their exact cardinality, or their compatible \(3\)-adic closure. In particular, the present classification describes the entire non-surjective regime with precisely one factor of two, including all odd cofactors, rather than restating the obstruction modulo six.

## Limitations

No description is claimed for moduli divisible by \(4\), or for the ordinary density of \(S\) among positive integers. The Haar measure describes a local projective closure and cannot be substituted for an ordinary density. Source comparison cannot exclude unindexed or implicit earlier derivations of the same mixed-prime classification.

## References

1. K. F. Shamazov and A. L. Talambutsa, *On orbit sets generated by semigroups of one-dimensional affine functions*, arXiv:2507.06875v1, public 9 July 2025, https://arxiv.org/html/2507.06875v1.
2. D. A. Klarner and R. Rado, *Arithmetic properties of certain recursively defined sets*, Pacific Journal of Mathematics 53 (1974), 445–463, https://msp.org/pjm/1974/53-2/pjm-v53-n2-p13-p.pdf.
