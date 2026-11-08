# Exact mixed additive energy of modular hyperbolas over odd residue rings

## Finding

For odd \(N\ge3\) and units \(\lambda,\mu\in(\mathbb Z/N\mathbb Z)^\times\), put
\[
H_\lambda(N)=\{(x,\lambda x^{-1}):x\in(\mathbb Z/N\mathbb Z)^\times\}\subseteq(\mathbb Z/N\mathbb Z)^2.
\]
The **mixed ordered additive energy** is
\[
E_N(\lambda,\mu)=\#\{(a,b,c,d):a,c\in H_\lambda(N),\ b,d\in H_\mu(N),\ a+b=c+d\}.
\]
This definition counts ordered quadruples with the first and third points on the first hyperbola and the second and fourth on the second.

It factors by the Chinese remainder theorem:
\[
E_N(\lambda,\mu)=\prod_{p^k\parallel N}E_{p^k}(\lambda,\mu).
\]
For any odd prime \(p\), integer \(k\ge1\), and units \(\lambda,\mu\) modulo \(p^k\), set \(v=\nu_p(\lambda-\mu)\) truncated to \(k\), so \(v=k\) if \(\lambda\equiv\mu\pmod{p^k}\). If \(v=0\), define \(\chi=\left(\frac{\lambda\mu}{p}\right)\in\{-1,1\}\). Then
\[
\boxed{E_{p^k}(\lambda,\mu)=
(p-1)p^{2k-2}\left[2p-5-\chi+(k-1)(p-1)(1+\chi)\right]\quad(v=0).}
\]
If \(1\le v\le k\), then
\[
\boxed{E_{p^k}(\lambda,\mu)=
(p-1)p^{2k-2}\left[3p-7+2(k-1)(p-1)+(v-1)(p-1)+\mathbf1_{v=k}\right].}
\]
These formulas hold without restrictions on the relationship of the two parameters. In particular, distinct reductions with \(\chi=-1\) give \(E_{p^k}=2(p-1)(p-2)p^{2k-2}\), independent of \(k\) after normalization by \(p^{2k-2}\). Equality of parameters recovers the established self-energy \(3(p-1)p^{2k-2}(k(p-1)-1)\). The exact answer changes at every positive valuation layer of \(\lambda-\mu\).

For example, modulo \(25\), fixing \(\lambda=1\) gives \(E_{25}(1,2)=600\), \(E_{25}(1,4)=1200\), \(E_{25}(1,6)=1600\), and \(E_{25}(1,1)=2100\), exhibiting all four local regimes.

Fourier orthogonality also yields the exact **two-parameter mixed fourth moment**
\[
\sum_{u,v\bmod N}|K(u,\lambda v;N)|^2\,|K(u,\mu v;N)|^2=N^2E_N(\lambda,\mu),
\]
where \(K(u,w;N)=\sum_{x\in(\mathbb Z/N\mathbb Z)^\times}e^{2\pi i(ux+wx^{-1})/N}\). (The summation indices \(u,v\) here are not the truncated valuation.)

## Assumptions and scope

All residue rings in this theorem have **odd** modulus. Every hyperbola parameter is a multiplicative unit. The energy counts **ordered** representations, including coincident points. The valuation \(v\) is computed on any representatives of \(\lambda-\mu\) and truncated at \(k\). The Legendre symbol is used only when \(v=0\). The theorem is exact for every \(k\ge1\), including \(p=3\), and for every odd composite modulus by CRT. No statement is made for even moduli or for nonunit parameters.

## Proof

**1. Difference fibers and valuation shells.** Work modulo \(q=p^k\) and write
\[
D_\lambda(s,t)=\#\{x,y\in(\mathbb Z/q\mathbb Z)^\times:x-y=s,\ \lambda x^{-1}-\lambda y^{-1}=t\}.
\]
Since exchanging the two inputs reverses each difference, \(D_\mu(-s,-t)=D_\mu(s,t)\). Therefore \(E_q(\lambda,\mu)=\sum_{s,t\bmod q}D_\lambda(s,t)D_\mu(s,t)\). The origin contributes \(\varphi(q)^2\). If exactly one of \(s,t\) is zero, or their truncated \(p\)-adic valuations differ, both fibers are zero: indeed \(t=-\lambda s/(xy)\) and \(xy\) is a unit.

Suppose first \(s,t\) are units. Substituting \(y=x-s\) and multiplying by \(xy\) gives the quadratic
\[
x^2-sx+\lambda s/t=0.
\]
The change of variable \(z=(2x-s)/s\) is invertible modulo \(q\); the product condition makes both reconstructed \(x,y\) units. Thus
\[
D_\lambda(s,t)=R_k\left(1-4\lambda/(st)\right),\quad
R_k(w)=\#\{z\bmod p^k:z^2=w\}.
\]
For \(1\le h<k\), let \(s=p^hs_0,t=p^ht_0\), with \(s_0,t_0\) units modulo \(p^{k-h}\). The same quadratic is imposed modulo \(p^{k-h}\), has unit discriminant reducing to \(-4\lambda s_0/t_0\), and lifts \(p^h\)-fold to modulo \(p^k\). By the simple-root form of Hensel's lemma,
\[
D_\lambda(s,t)=p^h\left(1+\left(\frac{-\lambda s_0/t_0}{p}\right)\right).
\]
Since \(s_0/t_0\) ranges uniformly over the unit group, the contribution of shell \(h\) to the mixed energy is exactly
\[
p^{2h}\varphi(p^{k-h})^2\left(1+\left(\frac{\lambda\mu}{p}\right)\right)
=(p-1)^2p^{2k-2}(1+\chi),
\]
with \(\chi=\left(\frac{\lambda\mu}{p}\right)\) in both parameter regimes. Summing over \(h=1,\ldots,k-1\) multiplies this by \(k-1\).

**2. Unit-coordinate contribution.** The map \((s,t)\mapsto (st)^{-1}\) takes every unit value exactly \(\varphi(q)\) times. Hence the unit-coordinate contribution is \(\varphi(q)N_k\), where
\[
N_k=\sum_{w\in(\mathbb Z/q\mathbb Z)^\times}
R_k(1-4\lambda w)R_k(1-4\mu w).
\]
Equivalently, \(N_k\) counts triples of units \(w\) and residues \(x,y\) satisfying
\[
x^2=1-4\lambda w,\qquad y^2=1-4\mu w\pmod{p^k}.
\]
If \(\lambda\not\equiv\mu\pmod p\), the two equations define a smooth relative one-dimensional solution scheme modulo \(p\): the Jacobian in \((x,y,w)\) has rank two because its first two rows are \((2x,0,4\lambda)\) and \((0,2y,4\mu)\), which can fail to be independent only when \(x=y=0\), impossible for distinct reductions. Each solution modulo \(p\) therefore has exactly \(p^{k-1}\) lifts. Over the field, \(R_1(a)=1+\left(\frac ap\right)\), and a standard quadratic character-sum computation gives
\[
N_1=(p-1)-1-1-1-\left(\frac{\lambda\mu}{p}\right)=p-4-\chi.
\]
Indeed the two single-character sums over nonzero \(w\) equal \(-1\), and the product-character sum equals \(-1-\chi\) by the distinct-root quadratic-sum identity. Thus
\[
N_k=p^{k-1}(p-4-\chi)\qquad (v=0).
\]

**3. Singular intersection when parameters coincide modulo \(p\).** Now assume \(\lambda\equiv\mu\pmod p\), so \(\chi=1\). Modulo \(p\), there is exactly one singular triple: \(x=y=0\), \(w=(4\lambda)^{-1}\). The total mod-\(p\) count is \(2p-5\): among \(1-4\lambda w\in\mathbb F_p\setminus\{1\}\), zero contributes one pair and each of the \((p-3)/2\) nonzero squares contributes four. Consequently the \(2p-6\) smooth triples lift to \((2p-6)p^{k-1}\) triples modulo \(p^k\).

For the singular branch put \(\rho=\mu/\lambda\equiv1\pmod p\) and \(\varepsilon=\rho-1\). Since \(p\) is odd, Hensel's lemma gives a unit \(r\) with \(r^2=\rho\) modulo \(p^k\). Eliminating \(w\) by \(w=(1-x^2)/(4\lambda)\), the condition reduces to
\[
y^2-\rho x^2=-\varepsilon,\quad x,y\in p\mathbb Z/p^k\mathbb Z.
\]
The invertible linear change \(A=y-rx\), \(B=y+rx\) maps the two restricted variables bijectively to \(A,B\in p\mathbb Z/p^k\mathbb Z\) and gives
\[
AB=-\varepsilon\pmod{p^k}.
\]
Let \(v=\min(k,\nu_p(\varepsilon))=\min(k,\nu_p(\lambda-\mu))\). If \(v<k\), the number of such pairs is \(0\) for \(v=1\) and \((v-1)(p-1)p^{k-1}\) for \(v\ge2\): classify \(\nu_p(A)=i\) for \(1\le i<v\), and observe that each \(i\) contributes \((p-1)p^{k-1}\) pairs. If \(v=k\), the count is \([1+(k-1)(p-1)]p^{k-1}\): the \(k-1\) nonzero valuation classes each contribute \((p-1)p^{k-1}\), and \(A=0\) contributes \(p^{k-1}\). Therefore
\[
N_k=p^{k-1}\left[2p-6+(v-1)(p-1)+\mathbf1_{v=k}\right]\qquad (v\ge1).
\]

**4. Assemble and apply CRT.** In either regime,
\[
E_{p^k}(\lambda,\mu)=\varphi(p^k)^2+\varphi(p^k)N_k
 +(k-1)(p-1)^2p^{2k-2}(1+\chi).
\]
Substituting the two evaluations of \(N_k\), with \(\chi=1\) whenever \(v\ge1\), gives the displayed local factors. Chinese-remainder decomposition identifies each hyperbola, each difference fiber, and each quadruple independently across distinct prime powers, hence multiplies the local energies. Finally, \(K(u,\lambda v;N)\) is the unnormalized two-dimensional Fourier transform of \(1_{H_\lambda(N)}\). Parseval/orthogonality of characters for the convolution of the two hyperbola indicators yields the mixed fourth-moment identity. \(\square\)

## Verification

A standalone Python program `verify_mixed_energy.py` directly constructs the two hyperbolas modulo small odd prime powers, tabulates **ordered** difference fibers by subtraction in both coordinates, takes their inner product, and checks it against the local formula for unit parameters in all valuation regimes. It additionally checks CRT products for selected composite moduli, including squareful ones, without using the proof's quadratic-root calculation. Run `python3 verify_mixed_energy.py` with Python 3.8 or newer; no nonstandard modules are required. See `VERIFICATION.md` for its precise finite coverage and limitations.

## Relationship to prior work

Cilleruelo and Garaev, *Concentration points on two and three dimensional modular hyperbolas and applications* (arXiv:1007.1526, first public July 9, 2010), study incidence/concentration and related product-set estimates for modular hyperbolas, not mixed whole-graph additive energy. This is the archival motivation and the source of the subject classification. Gong, Veys and Wan, *Power moments of Kloosterman sums* (arXiv:1306.4104), compute and study **single-family** power moments for Kloosterman sums; their ordinary fourth moment does not determine the cross-parameter product of squared Fourier magnitudes. Ricotta and Royer, *Kloosterman paths of prime powers moduli* (arXiv:1609.03694), Proposition 5.4, give a uniform bound for quadruple solutions on a **single** modular inverse graph restricted to an interval, not an exact mixed-parameter census. The established same-parameter self-energy is recovered here but is not claimed as new. The separate-parameter valuation transition and exact local factors are the claimed addition. Potential unlocated equivalent work on correlated Kloosterman moments remains a historical-priority risk.

## Limitations

The statement excludes the prime \(2\), nonunit hyperbola parameters, and incomplete-interval energies. The mixed fourth moment includes **all** additive frequencies \((u,v)\), not only primitive frequencies. Finite exhaustive tests are supporting evidence, not an infinite proof. Any claim of historical priority is limited by the possibility of unlocated equivalent work.

## References

- J. Cilleruelo and M. Z. Garaev, *Concentration points on two and three dimensional modular hyperbolas and applications*, arXiv:1007.1526 (first public 2010-07-09), https://arxiv.org/abs/1007.1526.
- K. Gong, W. Veys and D. Wan, *Power moments of Kloosterman sums*, arXiv:1306.4104 (2013), https://arxiv.org/abs/1306.4104.
- G. Ricotta and E. Royer, *Kloosterman paths of prime powers moduli*, arXiv:1609.03694 (2016), https://arxiv.org/abs/1609.03694.
