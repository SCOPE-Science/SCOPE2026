# Uniform Cartier ranks for tame scalar quotients of additive Artin–Schreier curves

## Finding

**Theorem.** Fix an odd prime \(p\), an even integer \(h\ge 2\), and an algebraically closed field \(k\) of characteristic \(p\). Let
\[
R(x)=\sum_{j=0}^{h/2}b_{2j}x^{p^{2j}},\qquad b_0b_h\ne0,
\]
let \(W_R\) be the smooth projective model of \(y^p-y=xR(x)\), and let the group \(G=\mu_{2(p-1)}\) act by \((x,y)\mapsto(ax,a^2y)\). Write \(X_R=W_R/G\). Then
\[
g(X_R)=\frac{p^h-1}{4},\quad
\operatorname{rank}\bigl(\mathcal C\mid H^0(X_R,\Omega^1)\bigr)
=\frac{(p+1)(2p^{h-1}+p-3)}{24},
\]
\[
a(\operatorname{Jac}X_R)=\dim_k\ker\mathcal C
=\frac{(4p-2)p^{h-1}-p^2+2p-3}{24}.
\]
Equivalently, the exact discrepancy from the normalized first-Cartier ratio of the additive cover is
\[
a(\operatorname{Jac}X_R)
=\frac{2p-1}{3p}\,g(X_R)-\frac{(p-2)(p^2-1)}{24p}.
\]
The formulas are independent of every allowed coefficient \(b_{2j}\).

**New maximal-curve application.** For \(n\ge2\), Bartoli, Borges, Timpanella and Zini construct the prime-field curve
\[
X_{p,n}:\quad uv^p+v=-1-2\sum_{i=1}^{n}u^{(p^{2i}-1)/(2(p-1))}.
\]
Their Theorem 1.3(ii) proves that it is maximal over \(\mathbb F_{p^{4n+2}}\) and has trivial geometric automorphism group. Its construction uses the above scalar quotient with \(h=2n\), so its Cartier rank and \(a\)-number are precisely the displayed expressions with \(h=2n\). For \(p=3,n=2\), the genus is \(20\), Cartier rank \(9\), and \(a\)-number \(11\); for \(p=5,n=2\), the corresponding triple is \((156,63,93)\). Maximality and the automorphism statement are cited prior results, not contributions of this calculation.

## Assumptions and scope

All geometric invariants are computed over \(k\). The integer \(h\) is even, \(h\ge2\), and \(p\) is any odd prime; coefficients need not lie in the prime field. Smooth projective models and the usual \(p^{-1}\)-linear Cartier operator are understood. The group \(G\) has order \(D=2(p-1)\), which is prime to \(p\). Every exponent of \(R\) is an even power index; this ensures the scalar action preserves the defining equation, since \(a^{p^{2j}}=a\) for \(a^D=1\). The assumption \(b_0b_h\ne0\) is the natural scalar-quotient setup of Bartoli–Borges–Timpanella–Zini.

## Proof

**1. Geometry and tame descent.** Proposition 2.1 of [1] gives, when \(D=2(p-1)\), the quotient genus \(g(X_R)=(p^h-1)/4\). The pullback by the tame quotient map induces
\[
H^0(X_R,\Omega^1)\simeq H^0(W_R,\Omega^1)^G.
\]
This also follows locally: for a ramification parameter transformed by \(t\mapsto at\), invariant regular differentials are multiples of \(t^{e-1}dt\), the pullback of a differential in the quotient parameter \(t^e\). Cartier commutes with pullback and with the group action. Averaging with \(D^{-1}\) (which belongs to the prime field) shows
\[
\operatorname{Im}(\mathcal C_{X_R})
\simeq\bigl(\operatorname{Im}\mathcal C_{W_R}\bigr)^G.
\]
Indeed, for an invariant element in the image, the average of any preimage is an invariant preimage, using \(p^{-1}\)-linearity and \(D^{-1}\in\mathbb F_p\).

**2. The image basis and an invariant triangular minor.** The published Theorem 6.6 and its proof in [2], for \(h\ge2\), give a basis of \(\operatorname{Im}\mathcal C_{W_R}\) consisting of
\[
\omega_{s,t,z}=x^{p^{h-1}t+z}y^s\,dx,
\qquad s,t\ge0,\quad s+t\le p-2,\quad
0\le z<p^{h-2}(p-1-s-t).
\]
That theorem is uniform over all additive polynomials with \(b_h\ne0\), so it applies in our even-support subfamily. Under \(G\) the differential \(x^iy^s dx\) has weight \(i+2s+1\) modulo \(D\). Thus the invariant image basis is exactly the subset satisfying
\[
p^{h-1}t+z+2s+1\equiv0\pmod{2(p-1)}.\tag{1}
\]
For completeness, the triangular minor in [2, Lemmas 6.4–6.5] uses the source differential
\[
\eta_{s,t,z}=x^{pz+p-1-t}y^{s+t}dx.
\]
Its weight is \(pz+p+t+2s\), congruent to \(p\) times the weight of \(\omega_{s,t,z}\) modulo \(D\), because \(p^h\equiv1\) and \(2p\equiv2\) modulo \(D\). Since \(p\) is invertible modulo \(D\), an image row is invariant exactly when its paired input column is invariant. The selected minor remains block triangular after restriction to invariant rows and columns, and its diagonal entries \((-1)^t\binom{s+t}{s}b_h^t\) remain nonzero. Together with the universal image containment proved in [2, Lemma 6.2], this independently confirms that counting the invariant displayed rows gives the *exact* quotient Cartier rank for all coefficients, not just an upper bound.

**3. Exact congruence count.** Put \(T=p-1\), \(D=2T\) and \(Q=p^{h-2}\). Since \(h\) is even, \(Q\equiv1\pmod D\) and \(p^{h-1}\equiv p=T+1\pmod D\). For fixed \((s,t)\), let \(k=T-s-t\), so \(k\ge1\). The allowable interval \(0\le z<Qk\) contains \((Q-1)k/D\) complete blocks of \(D\) residues, followed by \(0\le z<k\). There are \(Kk\) solutions from the complete blocks, where \(K=(Q-1)/D\). Summing gives
\[
K\sum_{s+t\le T-1}(T-s-t)
=K\frac{T(T+1)(T+2)}6
=\frac{(Q-1)p(p+1)}{12}.
\]
For the final short interval \(0\le z<k\), set \(w=z+t+2s+1\). We have \(1\le w<2T\), so condition (1) becomes \(w+Tt\equiv0\pmod{2T}\). There is no solution for even \(t\). For odd \(t\) the condition is \(w=T\), equivalently
\[
z=T-t-2s-1,
\qquad 0\le s\le (T-t-1)/2.
\]
For \(t=1,3,\ldots,T-1\), the total number of short-interval solutions is
\[
\sum_{j=0}^{T/2-1}(T/2-j)=\frac{T(T+2)}8=\frac{p^2-1}{8}.
\]
Adding gives the first Cartier rank
\[
\frac{(Q-1)p(p+1)}{12}+\frac{p^2-1}{8}
=\frac{(p+1)(2p^{h-1}+p-3)}{24}.
\]
Subtracting from \(g(X_R)=(p^h-1)/4\) proves the \(a\)-number formula, and elementary simplification gives the discrepancy identity. No higher Cartier rank or full Ekedahl–Oort type is asserted.

## Verification

The included standard-library program `verify_cartier_quotient.py` makes two independent computations: a direct modulo-\(p\) Cartier–Manin matrix for \(R(x)=x+x^{p^2}+\cdots+x^{p^h}\), using the expansion \(y^j=\sum_s(-1)^{j-s}\binom js(y^s)^p(xR(x))^{j-s}\), and the congruence count (1). It compares both with the closed formula. The program returned `VERIFY_OK` for \((p,h)=(3,2),(3,4),(3,6),(5,2),(5,4),(7,2),(11,2),(13,2)\). The program is an exact finite consistency check; the arbitrary-parameter conclusion rests on the preceding proof and the cited universal image theorem.

To reproduce with Python 3, run `python verify_cartier_quotient.py` in a directory containing the extracted artifact. No nonstandard packages, external data, or network access are required.

## Relationship to prior work

Bartoli–Borges–Timpanella–Zini [1, Proposition 2.1 and Theorem 1.3(ii)] introduce the scalar quotient, establish its genus, maximality in the special family, and triviality of its full geometric automorphism group. Almeida Filho–Tafazolian–Vieira [2, Theorem 6.6] determine the *covering* additive curve's entire first Cartier image; they do not state a first Cartier rank or \(a\)-number for its order-\(2(p-1)\) scalar quotient. This result computes precisely the nontrivial invariant subrepresentation and evaluates its character count uniformly, with an exact constant discrepancy from the covering-curve normalized ratio. The quotient formula is an explicit consequence of the published cover-image theorem plus tame descent and the new residue calculation, not an independently discovered theorem about cover images. Bouw–Ho–Malmskog–Scheidler–Srinivasan–Vincent [3] discuss additive-curve quotient geometry and zeta functions, but the inspected account does not give this tame quotient \(a\)-number.

## Limitations

The formula concerns the first Cartier rank and \(a\)-number, not higher Cartier powers, Ekedahl–Oort classification, or all quotients of additive curves. It assumes odd characteristic, even-support \(R\), and even \(h\ge2\). The claimed arithmetic maximality and automorphism-freeness for the special prime-field family are supplied by [1]. The proof relies on the published full-image theorem [2] and does not independently reconstruct all of its universal containment argument. Searches and primary-source comparisons have not established absolute historical priority, particularly among older work on Jacobians of Artin–Schreier quotients; independent mathematical validation remains unperformed.

## References

[1] D. Bartoli, H. Borges, M. Timpanella, G. Zini, *Maximal curves with trivial automorphism group*, arXiv:2610.35788v1 (first submitted 26 October 2026), especially Proposition 2.1, Theorem 1.3(ii) and Section 6.1. https://arxiv.org/html/2610.35788v1

[2] G. B. Almeida Filho, S. Tafazolian, S. C. Vieira, *a-Numbers, higher Cartier ranks and maximality of van der Geer–van der Vlugt curves*, arXiv:2610.17476v1 (first submitted 12 October 2026), especially Lemmas 6.1–6.5 and Theorem 6.6. https://arxiv.org/abs/2610.17476

[3] I. Bouw, W. Ho, B. Malmskog, C. Scheidler, S. Srinivasan, C. Vincent, *Zeta functions of a class of Artin–Schreier curves with many automorphisms*, arXiv:1410.7031; published in 2016. https://arxiv.org/abs/1410.7031
