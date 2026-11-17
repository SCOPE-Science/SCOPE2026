# Exact dyadic two-sum spectrum of the modular inverse hyperbola

## Finding

Let \(k\ge1\), \(q=2^k\), and \(U_k=(\mathbb Z/q\mathbb Z)^\times\). Set
\[
H_k=\{(x,x^{-1}):x\in U_k\}\subset(\mathbb Z/q\mathbb Z)^2,
\qquad
r_k(s,t)=\#\{(x,y)\in U_k^2:(x+y,x^{-1}+y^{-1})=(s,t)\}.
\]
Every representation is ordered. Define the square-root count
\[
R_m(d)=\#\{z\bmod 2^m:z^2\equiv d\pmod{2^m}\}.
\]
For \((s,t)=(0,0)\), one has \(r_k(s,t)=2^{k-1}\). For other targets, \(r_k(s,t)=0\) unless both coordinates are nonzero with the same exact \(2\)-adic valuation \(h\), where \(1\le h<k\). For such a target put
\[
m=k-h,\quad u=s/2^h,\quad v=t/2^h,\quad d=(s/2)^2-uv^{-1}\pmod{2^m},
\]
where \(u,v\) are units modulo \(2^m\), and \(s/2\) is well-defined modulo \(2^m\). Then
\[
\boxed{r_k(s,t)=2^hR_m(d).}
\]
The square-root function is explicit: \(R_m(0)=2^{\lfloor m/2\rfloor}\); a nonzero \(d\) with odd valuation has no roots; for \(d=2^{2j}w\), \(w\) odd and \(2j<m\),
\[
R_m(d)=2^j\rho_{m-2j}(w),\quad
\rho_1(w)=1,\quad
\rho_2(w)=2\mathbf1_{w\equiv1\ (4)},\quad
\rho_\ell(w)=4\mathbf1_{w\equiv1\ (8)}\ (\ell\ge3).
\]
Here the indicator is one for the stated congruence and zero otherwise. This determines **the full joint two-sum multiplicity spectrum**, not just an energy moment.

Write \(I_k=|H_k+H_k|\) and let \(Q(n)\) count square residues modulo \(2^n\) (with \(Q(0)=1\)). The exact cardinalities are
\[
I_1=1,\ I_2=2,\ I_3=4,\qquad
\boxed{I_k=2^{k-2}Q(k-3)+\frac{4^{k-3}+8}{3}\quad(k\ge4),}
\]
where
\[
Q(2r)=\frac{4^r+8}{6}\ (r\ge1),\qquad
Q(2r+1)=\frac{4^r+5}{3}\ (r\ge0).
\]
In particular \(I_4,\ldots,I_{10}=12,24,72,216,792,2904,11352\), and
\[
\boxed{\lim_{k\to\infty} I_k/4^k=1/96.}
\]
Equivalently, the compact twofold sum of the unit inverse graph \(H_\infty=\{(x,x^{-1}):x\in\mathbb Z_2^\times\}\) has normalized product Haar measure \(1/96\) inside \(\mathbb Z_2^2\).

## Assumptions and scope

The ring is precisely \(\mathbb Z/2^k\mathbb Z\), for every integer \(k\ge1\). Inverses are taken only of odd residues; sums are vector sums in the ambient **two-dimensional** additive group. The valuation of a nonzero residue modulo \(2^k\) is its uniquely determined integer \(h<k\). The zero residue has no finite valuation in this convention. The calculation concerns ordered pairs and does not claim analogous formulas at odd prime powers.

## Proof

**1. Valuations and the zero target.** Each \(x,y\in U_k\) is odd, so \(s=x+y\) is even and \(t=x^{-1}+y^{-1}=s(xy)^{-1}\). The factor \((xy)^{-1}\) is a unit, so either both \(s,t\) vanish, or they have the same exact valuation \(1\le h<k\). When \(s=t=0\), each \(x\in U_k\) gives exactly the partner \(y=-x\), hence \(r_k(0,0)=2^{k-1}\).

**2. Exact root reduction.** Suppose \(s=2^hu\), \(t=2^hv\) are both nonzero with equal valuation \(h\). The two vector equations are equivalent to \(y=s-x\) modulo \(2^k\), and
\[
u\equiv vxy=vx(s-x)\pmod{2^{k-h}}.
\]
Write \(m=k-h\) and \(a=s/2\), which is unambiguous modulo \(2^m\) since \(m\le k-1\). After dividing by the unit \(v\) and completing the square, this becomes
\[
(x-a)^2\equiv a^2-uv^{-1}=d\pmod{2^m}.
\]
Every root \(z\) gives \(x=a+z\) odd: indeed \(z^2\equiv a^2-1\pmod2\), so \(z\) and \(a\) have opposite parity. Conversely every odd \(x\) solution gives a root. There are exactly \(2^h\) lifts of each root modulo \(2^m\) to \(x\bmod2^k\); for each, \(y=s-x\) is automatically odd. Therefore \(r_k(s,t)=2^hR_m(d)\) with no missing or duplicated lifts.

**3. Square-root and square-residue counts.** If \(z^2\equiv0\pmod{2^m}\), exactly \(2^{\lfloor m/2\rfloor}\) classes of \(z\) work. If \(d\ne0\) is a square modulo \(2^m\), its valuation must be even, say \(2j\), and the change \(z=2^jw\) reduces the congruence to an odd-unit square equation modulo \(2^{m-2j}\), with \(2^j\) lifts. Odd-unit squares have one root modulo \(2\), two roots modulo \(4\) when the target is \(1\), and four roots modulo \(2^\ell\) for \(\ell\ge3\) precisely when the target is \(1\bmod8\). This proves the stated formula for \(R_m\).

There is one zero square residue. Each nonzero square has even valuation \(2j<n\), followed by an odd square modulo \(2^{n-2j}\). The number \(A(\ell)\) of odd square residues is \(A(1)=A(2)=1\), \(A(\ell)=2^{\ell-3}\) for \(\ell\ge3\). Consequently
\[
Q(n)=1+\sum_{0\le j<n/2}A(n-2j).
\]
Summing the geometric progression separately for even and odd \(n\) gives the displayed formulas for \(Q\).

**4. Counting represented two-coordinate targets.** Fix \(h\) and put \(m=k-h\). There are exactly \(2^{m-1}\) nonzero first coordinates \(s\) of valuation \(h\). For each such \(s\), the map \(v\mapsto uv^{-1}\) permutes the odd residues modulo \(2^m\); therefore the quantity \(d=(s/2)^2-uv^{-1}\) runs bijectively through residues whose parity is opposite to the parity of \((s/2)^2\).

If \(h=1\), then \(s/2\) is odd and \(d\) runs through all even residues modulo \(2^m\). For \(m\ge3\), an even residue is square exactly when it is four times a square modulo \(2^{m-2}\); there are \(Q(m-2)\) choices. Hence for \(k\ge4\) this shell contributes exactly \(2^{k-2}Q(k-3)\) represented pairs \((s,t)\).

If \(h\ge2\), then \(s/2\) is even and \(d\) runs over all odd residues. With \(m=k-h\), the number of represented pairs in this shell is \(B_m=2^{m-1}A(m)\), namely
\[
B_1=1,\qquad B_2=2,\qquad B_m=4^{m-2}\quad(m\ge3).
\]
Therefore for \(k\ge4\), the total contribution from these shells is
\[
\sum_{m=1}^{k-2} B_m=\frac{4^{k-3}+5}{3}.
\]
Adding the single zero target yields the formula for \(I_k\). The small cases \(k=1,2,3\) follow from the same root formula, or direct enumeration.

**5. The Haar limit.** The elementary square-residue formulas give \(Q(n)=2^n/6+O(1)\). Inserting this into the exact \(I_k\) expression shows that each of its two principal contributions is \(4^k/192+o(4^k)\), so \(I_k/4^k\to1/96\). Finally, reduction of the compact set \(H_\infty+H_\infty\) modulo \(2^k\) is exactly \(H_k+H_k\). The preimages of those images form decreasing clopen neighborhoods whose intersection is \(H_\infty+H_\infty\). Continuity from above of normalized Haar measure identifies its measure with this limit.

## Verification

The included `verify.py` independently enumerates all ordered pairs and all coordinate targets for \(1\le k\le9\), comparing the observed multiplicities with the independent square-root formula and comparing the observed image sizes to the closed formula. It also cross-checks the known dyadic fourth-moment/energy expression \(3(k-3)2^{2k-1}\) for \(k\ge4\). The finite tests are corroboration, not the unrestricted proof.

Run `python verify.py` using Python 3.9+; the script needs only the standard library.

## Relationship to prior work

Bower, Evans, Luo and Miller (arXiv:1212.2930, public 2012-12-12, Theorem 3.3) give exact **coordinate** sum and difference set sizes \(\{x+x^{-1}\}\) over modular hyperbolas. Their scalar coordinate projection does not determine the simultaneous vector sum \(H_k+H_k\) or its ordered representation multiplicities.

Gong, Veys and Wan (arXiv:1306.4104, public 2013-06-18, Section 7, the \(n=4\) case) compute the dyadic fourth Kloosterman moment, equivalently the **total additive energy** of the inverse graph. In particular, that work already implies the energy expression mentioned under Verification. The present finding does **not** claim this moment as novel: an energy sum of squared fiber counts does not determine the exact fibers or the number of nonzero fibers. The present theorem determines both. Classical odd-prime or finite-field inverse-graph results concern different coefficient rings and do not yield this dyadic spectrum.

## Limitations

This is an all-exponent theorem only for powers of two and the unweighted, ordered, twofold vector sum of the unit inverse graph. Its proof uses elementary root counting and does not assert novelty for the fourth moment already known. Historical priority is qualified: the searches and inspected primary works identified no equal or stronger full two-coordinate dyadic spectrum, but no search can certify absence of uncatalogued equivalent statements. There is no independent mathematical audit.

## References

1. A. Bower, R. Evans, V. Luo, S. J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930v1, public 2012-12-12, Sections 1 and 3, Theorem 3.3. https://arxiv.org/abs/1212.2930
2. K. Gong, W. Veys, D. Wan, *Power moments of Kloosterman sums*, arXiv:1306.4104v1, public 2013-06-18, Section 7, the \(n=4\) case. https://arxiv.org/abs/1306.4104
3. T. Tao, *What's new*, August 2015, Kloosterman fourth-moment combinatorial argument (moment bound rather than individual dyadic fiber classification). https://terrytao.wordpress.com/2015/08/
