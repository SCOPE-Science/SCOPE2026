# The exact ternary fiber law for the cubic Dickson polynomial

## Finding
Let \(f(X)=D_3(X,1)=X^3-3X\). For every integer \(k\ge1\) and residue \(y\in\mathbb Z/3^k\mathbb Z\), define the **fiber size**
\[
N_k(y)=\#\{x\bmod 3^k:f(x)\equiv y\pmod{3^k}\}.
\]
The theorem below determines **every** \(N_k(y)\), not merely the set of attained values.

For \(r\ge0\), define \(Q_r(z)=\#\{w\bmod3^r:w^2\equiv z\pmod{3^r}\}\), with \(Q_0(z)=1\). For \(r\ge1\), its explicit formula is
\[
Q_r(z)=\begin{cases}
3^{\lfloor r/2\rfloor},&z\equiv0\pmod{3^r},\\
2\cdot3^j,&\nu_3(z)=2j<r\ \text{and}\ z/3^{2j}\equiv1\pmod3,\\
0,&\text{otherwise}.
\end{cases}
\]
Here a nonzero residue's valuation is the unique integer in \([0,r-1]\); no choice of a representative affects the formula.

For integers \(m\ge1\) and \(t\bmod3^m\), define
\[
C_m(t)=\begin{cases}
1,&m=1,\ t\equiv0\pmod3,\\
3,&m=2,\ t\equiv0\pmod9,\\
3Q_{m-2}(t/9),&m\ge3,\ t\equiv0\pmod9,\\
0,&\text{otherwise}.
\end{cases}
\]
For \(k\ge4\), put \(m=k-3\). The **complete fiber law** is
\[
N_k(y)=\begin{cases}
3,&y\equiv0\pmod9,\\
9\bigl(\mathbf1_{t\equiv0,2\ (\mathrm{mod}\ 3)}+C_m(t)\bigr),
&y\equiv-2\pmod{27},\quad t=(y+2)/27\bmod3^m,\\
9\bigl(\mathbf1_{t\equiv0,2\ (\mathrm{mod}\ 3)}+C_m(t)\bigr),
&y\equiv2\pmod{27},\quad t=(2-y)/27\bmod3^m,\\
0,&\text{otherwise}.
\end{cases}
\]
These four cases are disjoint. The displayed quotients are well-defined residues because the numerators are divisible by \(27\), and the characteristic function takes only the values zero and one.

For the small exponents, \(N_1(y)=1\) at all three residues; \(N_2(y)=3\) precisely for \(y\equiv0,2,-2\pmod9\) and is zero otherwise; and \(N_3(y)=3\) for \(y\equiv0\pmod9\), \(N_3(y)=9\) for \(y\equiv\pm2\pmod{27}\), and is zero otherwise.

Consequently the maximal fiber \(M_k=\max_y N_k(y)\) satisfies
\[
M_k=\begin{cases}
1,&k=1,\\3,&k=2,\\9,&k=3,\\18,&k=4,\\
9+3^{(k+1)/2},&k\ge5\text{ odd},\\
9+2\cdot3^{k/2},&k\ge6\text{ even}.
\end{cases}
\]
For every \(k\ge3\) **exactly two target residues** attain this maximum: \(y\equiv\pm2\pmod{3^k}\) for \(k=3,4\) and odd \(k\ge5\); for even \(k\ge6\), the targets are \(y\equiv\pm(2-3^{k-1})\pmod{3^k}\). As a consistency check, the image has \(3,3,5\) elements at precisions \(k=1,2,3\) and \(13\cdot3^{k-4}\) elements for \(k\ge4\), a previously established value-set formula.

## Assumptions and scope
The prime is exactly \(3\); the polynomial has parameter \(1\) and degree \(3\); the input and target are arbitrary residues of \(\mathbb Z/3^k\mathbb Z\). Fiber counts include all preimages modulo the **same** modulus \(3^k\), and zero fibers are included in the classification. The result makes no claim for other Dickson degrees, other primes, or general cubic polynomials.

## Proof
**1. A bijective linear branch.** For \(x=3u\),
\[
f(3u)=9G(u),\qquad G(u)=3u^3-u.
\]
For all \(u,v\in\mathbb Z_3\),
\(G(u)-G(v)=(u-v)(3(u^2+uv+v^2)-1)\); the second factor is a \(3\)-adic unit. Thus \(G\) is an isometry on \(\mathbb Z_3\) and induces a bijection modulo every power of three. At precision \(k\ge2\), the input ball \(3\mathbb Z_3\) maps onto \(9\mathbb Z_3\), with exactly three inputs modulo \(3^k\) per target. At \(k=1\), it gives the single target zero.

**2. Two reflected singular branches.** Write \(x=\sigma(1+3u)\) with \(\sigma\in\{1,-1\}\). Because \(f\) is odd,
\[
f(x)=\sigma\bigl(-2+27h(u)\bigr),\qquad h(u)=u^2(u+1).
\]
The outputs for the two signs reduce to distinct nonzero classes modulo three, and hence are disjoint from each other and from the linear branch. At \(k\le3\), each sign contributes one target. For \(k\ge4\), put \(m=k-3\). Each residue \(u\bmod3^m\) lifts to exactly nine choices of \(u\bmod3^{k-1}\), so the fiber count on one sign branch is nine times the root count of \(h(u)\equiv t\pmod{3^m}\).

**3. The two simple roots.** The reductions of \(h(u)\) at \(u\equiv0,1,-1\pmod3\) are \(0,2,0\), respectively, and \(h'(u)=u(3u+2)\). The derivative is a unit in the \(u\equiv1\) and \(u\equiv-1\) balls. Hensel lifting therefore makes the first ball a bijection onto \(2+3\mathbb Z_3\), and the second a bijection onto \(3\mathbb Z_3\). These contribute exactly one \(u\bmod3^m\) when \(t\equiv2\) or \(0\pmod3\), respectively; neither contributes when \(t\equiv1\pmod3\).

**4. The critical root and its exact multiplicity.** The remaining input ball has \(u=3v\), and
\[
h(3v)=9v^2(1+3v).
\]
The \(3\)-adic square root \(s(v)=\sqrt{1+3v}\) exists uniquely with \(s(v)\equiv1\pmod3\). Moreover, for \(v,w\in\mathbb Z_3\),
\[
s(v)-s(w)=\frac{3(v-w)}{s(v)+s(w)}\in3(v-w)\mathbb Z_3.
\]
For distinct \(v,w\), one has \(H(v)-H(w)=(v-w)(s(v)+w(s(v)-s(w))/(v-w))\), whose second factor is \(1\pmod3\). Thus \(H(v)=v\,s(v)\) is an isometry (and the equality case is immediate). This shows directly that \(H\) induces a bijection of \(\mathbb Z/3^r\mathbb Z\) for every \(r\ge1\), and \(h(3v)=9H(v)^2\).

For \(m=1,2\), all \(3^{m-1}\) choices of \(u\equiv0\pmod3\) produce \(t=0\). For \(m\ge3\), critical solutions exist only when \(t\equiv0\pmod9\). Then \(v\bmod3^{m-1}\) must satisfy \(H(v)^2\equiv t/9\pmod{3^{m-2}}\), so there are precisely \(3Q_{m-2}(t/9)\) such \(v\). This is exactly \(C_m(t)\). Adding the simple and critical contributions and multiplying by nine proves the fiber formula.

**5. Square-root counts and sharp maxima.** A nonzero square modulo \(3^r\) has even valuation \(2j<r\) and a unit part congruent to \(1\pmod3\). It has exactly \(2\cdot3^j\) roots; zero has exactly \(3^{\lfloor r/2\rfloor}\) roots. These are the displayed \(Q_r\) values. If \(r=2h\), the zero target uniquely maximizes \(Q_r\) with \(3^h\) roots, since \(2\cdot3^{h-1}<3^h\) when \(h\ge1\). If \(r=2h+1\), the unique maximizing residue is \(3^{2h}\pmod{3^{2h+1}}\), with \(2\cdot3^h\) roots. Apply this with \(r=m-2=k-5\), adding the nine simple-branch inputs and the factor \(27\) from the critical branch. The exceptional levels \(k=1,2,3,4\) follow directly. Each sign branch has exactly one maximizing target, producing the two explicitly stated residues. No other output class can tie because the linear branch has fibers of size three and the ordinary noncritical branch fibers have size nine.

## Verification
The standalone `verify.py` uses independent enumeration of all \(3^k\) inputs and all \(3^k\) targets for \(1\le k\le9\), comparing every observed fiber with the formula and checking the image cardinality, maximum, and **complete set** of maximizing targets. It then independently lifts roots of selected targets for \(10\le k\le14\). On the packaged code, 29,773 target comparisons passed. The enumeration is finite evidence only; Steps 1–5 prove the claim for every integer \(k\ge1\).

Run: `python3 verify.py` (Python 3 standard library; no external data or dependencies).

## Relationship to prior work
Shang (2023) gives universal maximal image-size bounds for nonpermutation polynomials over residue rings; its Theorem 1.1 and lifting lemmas do not classify the fibers of this particular polynomial. Brazelton–Harrington–Litman–Wong (2021) treats Dickson residue sums and image cardinalities over **finite fields**, not the successive ring levels. Bremser–Gomez-Calderon (1991) studies Dickson polynomials over Galois rings: its Theorem 5 gives fiber counts only under a **nonexceptional output discriminant** hypothesis \(y^2\not\equiv4a^d\pmod p\); for the present \(p=d=3\), \(a=1\), this covers the branch \(y\equiv0\pmod3\) but excludes both singular nonzero branches, where the new multiplicities occur. Its later result for degrees divisible by \(p\) gives estimates rather than the displayed exceptional fiber census.

Two previously available public notes, *Exact prime-power value sets of a Frobenius-minus-linear polynomial* (2026) and *Exact first-hit depth distribution for the cubic Dickson map modulo powers of three* (2026), cover, respectively, the present polynomial's thirteen-class image and its **iteration-depth** distribution. Neither states or implies the target-by-target one-step fiber counts or the parity-dependent sharp largest fiber proved here. The image formula is cited only as a check, not presented as new.

## Limitations
The result is specific to \(D_3(X,1)\) at powers of three. The older Galois-ring article was inspected through a publicly accessible text transcription whose mathematical typography is imperfect; its theorem hypotheses and exceptional/nonexceptional division were legible, but the possibility of an uncatalogued equivalent formula remains a priority risk. There is no claim of independent validation, publication priority beyond the compared material, or a general Dickson-degree classification.

## References
1. T. Brazelton, J. Harrington, M. Litman, T. W. H. Wong, *Residue sums of Dickson polynomials over finite fields*, arXiv:2103.09119v1, first posted 2021-03-16. https://arxiv.org/abs/2103.09119
2. S. Shang, *Value sets of non-permutation polynomials over the residue class rings of integers*, arXiv:2310.20226v1, first posted 2023-10-31. https://arxiv.org/html/2310.20226v1
3. P. S. Bremser and J. Gomez-Calderon, *Value sets of Dickson polynomials over Galois rings*, Journal of Number Theory 38 (1991), 240–250. DOI:10.1016/0022-314X(91)90087-R; public full-text transcription: https://www.academia.edu/48986625/Value_sets_of_Dickson_polynomials_over_Galois_rings
4. *Exact prime-power value sets of a Frobenius-minus-linear polynomial* (public mathematical note, 2026): https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-prime-power-value-sets-of-a-frobenius-minus-linear-polynom--8ac73addd4cb
5. *Exact first-hit depth distribution for the cubic Dickson map modulo powers of three* (public mathematical note, 2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-first-hit-depth-distribution-for-the-cubic-dickson-map-mod--24093f02440f
