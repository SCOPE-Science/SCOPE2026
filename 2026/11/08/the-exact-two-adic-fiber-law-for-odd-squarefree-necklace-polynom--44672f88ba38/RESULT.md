# The exact two-adic fiber law for odd squarefree necklace polynomials

## Finding
For each positive integer \(n\), let the classical necklace polynomial be
\[
M_n(x)=\frac1n\sum_{d\mid n}\mu(n/d)x^d.
\]
For \(n\ge1\), its values at positive integer alphabet sizes count aperiodic necklaces; at prime-power alphabet sizes, they also count degree-\(n\) monic irreducible polynomials over the corresponding finite field. The result below concerns the *polynomial map on all two-adic input residues*, not just inputs that are prime powers.

**Theorem.** If \(n>1\) is odd and squarefree, put \(e=2+\nu_2(\varphi(n))\). For every integer \(k\ge1\), set \(h=\min(k,e)\). Every residue \(y\in\mathbb Z/2^k\mathbb Z\) has exactly
\[
F_{n,k}(y)=\#\{x\in\mathbb Z/2^k\mathbb Z:M_n(x)\equiv y\pmod{2^k}\}
=\mathbf 1_{2\mid y}+2^{h-1}\mathbf 1_{2^h\mid y}
\]
preimages. Hence the image contains precisely \(2^{k-1}\) residues, namely all the even residues. The closure of the values in \(\mathbb Z_2\) is \(2\mathbb Z_2\), and in fact the continuous map is surjective onto that set. Its normalized-Haar pushforward has density
\[
\frac{d(M_n)_*\lambda}{d\lambda}(y)
=\mathbf 1_{2\mathbb Z_2}(y)+2^{e-1}\mathbf 1_{2^e\mathbb Z_2}(y).
\]
Equivalently, one quarter of the input residues lie in each of the two odd classes modulo four, and each of those two odd branches maps, after division by \(2^e\), bijectively and isometrically onto the full two-adic integers. The even branch maps, after division by two, bijectively and isometrically onto the full two-adic integers.

The squarefree assumption is sharp for this full-even-image conclusion: if \(n>1\) is odd and not squarefree, then \(M_n(\mathbb Z_2)\subseteq8\mathbb Z_2\). This last inclusion does not assert the exact nonsquarefree image.

For example, at \(n=15\), one has \(\varphi(n)=8\), hence \(e=5\). Modulo \(64\), both residues \(0\) and \(32\) have \(17\) preimages, the other \(30\) even residues each have one, and every odd residue has none.

## Assumptions and scope
Throughout \(\mu\) is the Möbius function, \(\varphi\) Euler's totient, and \(\nu_2\) the valuation normalized by \(\nu_2(2)=1\). The polynomial \(M_n\) has coefficients in \(\mathbb Z_2\) whenever \(n\) is odd, so reduction modulo \(2^k\) depends only on the input residue. An *isometry* of \(\mathbb Z_2\) is a map preserving all two-adic distances, equivalently satisfying \(\nu_2(f(s)-f(t))=\nu_2(s-t)\) for distinct inputs; such a polynomial is bijective if all its finite reductions are permutations, which follows by induction from the isometry and the fact that it maps even/odd inputs to opposite parity classes. The theorem quantifies over every odd squarefree \(n>1\), all \(k\ge1\), and every output residue. The nonsquarefree statement quantifies over all odd nonsquarefree \(n>1\).

## Proof
**1. Even input branch.** For odd squarefree \(n>1\), the coefficient of \(x\) in \(M_n(x)\) is \(\mu(n)/n\), a two-adic unit. All remaining exponents \(d\mid n\) are odd and at least three, so there is a polynomial \(R(s)\in\mathbb Z_2[s]\) with
\[
\frac{M_n(2s)}2=\frac{\mu(n)}n s+4R(s).
\]
For any \(s,t\), the difference divided by \(s-t\) is odd, since every polynomial difference is divisible by \(s-t\). Thus this map is an isometry; its constant term is zero and its reduction modulo two is the identity, so it is a bijection on \(\mathbb Z_2\) and on all quotients. Consequently every even output modulo \(2^k\) has exactly one even preimage modulo \(2^k\), and odd outputs have none from even inputs.

**2. Exact normalized expansion near the two odd roots.** Let
\[
H(z)=\frac1n\sum_{d\mid n}\mu(n/d)z^{(d-1)/2},
\qquad M_n(x)=xH(x^2).
\]
Because \(n>1\), the coefficient sum is zero, so \(H(1)=0\). Write \(v=\nu_2(\varphi(n))\), \(e=v+2\), and
\[
H(1+8t)=\sum_{j\ge1}a_jt^j.
\]
The linear coefficient is
\[
a_1=8H'(1)=\frac4n\sum_{d\mid n}\mu(n/d)(d-1)
=\frac{4\varphi(n)}n,
\]
so \(a_1/2^e\) is odd. For every \(j\ge2\), put \(P_j(D)=\prod_{i=0}^{j-1}(D-(2i+1))\in\mathbb Z[D]\). Then
\[
a_j=\frac{2^{2j}}{n\,j!}\sum_{d\mid n}\mu(n/d)P_j(d).
\]
The constant coefficient in \(P_j\) contributes zero because \(\sum_{d\mid n}\mu(n/d)=0\). Every positive-power term contributes a multiple of \(\varphi(n)\), since for each integer \(r\ge1\),
\[
\sum_{d\mid n}\mu(n/d)d^r
=\prod_{p\mid n}(p^r-1)
\quad\text{is divisible by}\quad
\prod_{p\mid n}(p-1)=\varphi(n).
\]
The coefficient sum is therefore divisible by \(\varphi(n)\), giving
\[
\nu_2(a_j)\ge v+2j-\nu_2(j!)\ge v+3=e+1\quad(j\ge2).
\]
The final inequality holds for every \(j\ge2\), because \(\nu_2(j!)\le j-1\) and \(2j-(j-1)=j+1\ge3\). We conclude that
\[
K(t):=2^{-e}H(1+8t)=u t+2t^2Q(t),
\]
where \(u\in\mathbb Z_2^\times\) and \(Q\in\mathbb Z_2[t]\). For any \(s\ne t\), the difference quotient \((K(s)-K(t))/(s-t)\) is odd. The map \(K\) is consequently a two-adic isometry and a bijection.

**3. Each odd class modulo four is an isometric full branch.** Fix \(\varepsilon\in\{-1,+1\}\) and write \(x=\varepsilon+4s\). Then
\[
T_\varepsilon(s)=\frac{x^2-1}{8}=\varepsilon s+2s^2
\]
is an isometry: its difference quotient is \(\varepsilon+2(s+t)\), always odd. Therefore
\[
G_\varepsilon(s)=2^{-e}M_n(\varepsilon+4s)
=(\varepsilon+4s)K(T_\varepsilon(s))
\]
is again an isometry. Indeed, for \(s\ne t\), subtract the two values and divide by \(s-t\): the first part is the product of an odd unit with the odd difference quotient of \(K\circ T_\varepsilon\), and the correction from the change of the prefactor has a factor four. Its reduction modulo two is an affine bijection; hence \(G_\varepsilon\) permutes each \(\mathbb Z/2^j\mathbb Z\) and is bijective on \(\mathbb Z_2\). Every odd input has \(M_n(x)\equiv0\pmod{2^e}\).

**4. Fiber count.** If \(k<e\), all \(2^{k-1}\) odd inputs map to zero modulo \(2^k\), while the even inputs give exactly one preimage per even output. This is the formula with \(h=k\). If \(k\ge e\), each of the two odd classes modulo four contains \(2^{k-2}\) inputs. The isometric map \(G_\varepsilon\) reduces modulo \(2^{k-e}\) to a bijection, so exactly \(2^{e-2}\) inputs in each odd class map to a given output divisible by \(2^e\), none to any other output. The total odd-branch contribution is \(2^{e-1}\); adding the unique even preimage gives the stated formula with \(h=e\). The formula also covers \(k=e\). Since polynomial maps are continuous and compatible with every finite quotient, the image in \(\mathbb Z_2\) is the inverse limit of the even residue images, and the Haar density follows by dividing each finite fiber count by the size of the input ring and comparing with normalized Haar masses of output residue balls.

**5. Nonsquarefree boundary.** Suppose \(n>1\) is odd and nonsquarefree. The term of exponent one vanishes because \(\mu(n)=0\). Every exponent appearing with nonzero coefficient is a multiple of \(n/\operatorname{rad}(n)\ge3\). Hence, for even \(x\), each term is divisible by eight, so \(M_n(x)\equiv0\pmod8\). For odd \(x\), all divisors \(d\mid n\) are odd and \(x^d\equiv x\pmod8\). The Möbius coefficient sum equals zero, so again \(M_n(x)\equiv0\pmod8\). Division by the odd integer \(n\) preserves this congruence. Continuity extends it to all two-adic inputs. This proves the strict failure of full-even-image surjectivity without asserting an exact nonsquarefree image. \(\square\)

## Verification
The standalone `verify.py` uses integer Möbius and totient functions together with modular polynomial evaluation, without importing a symbolic formula for the predicted fibers. For each of the eleven squarefree lengths \(3,5,7,11,13,15,21,33,35,105,1155\) and each \(1\le k\le11\), it enumerates every input modulo \(2^k\) and compares the entire output histogram with the theorem. It separately tests the normalized even and two odd isometric branches through seven precision levels, and checks the mod-eight nonsquarefree boundary for nine test lengths. Run `python3 verify.py`; the output is `VERIFY_OK squarefree_lengths=11 residue_entries=45034 local_branch_bijections=231 nonsquarefree_lengths=9 finite_level_fibers=PASS`. These finite checks are supplementary to the unrestricted argument.

## Relationship to prior work
The necklace polynomial and its identity with irreducible polynomial counts are classical. Moree's paper *The formal series Witt transform* expressly records the established evenness of \(M_n(q)\) when \(n\ge3\) and \(n\not\equiv2\pmod4\); neither evenness nor the formula for \(M_n\) is claimed as new. The examined sections of von zur Gathen–Viola–Ziegler provide the classical univariate irreducible count and higher-dimensional count formulas, but no full two-adic fiber law as the input alphabet size varies. Hyde studies cyclotomic factors and roots-of-unity values of necklace polynomials, including certain local polynomial congruences; those statements do not determine the input-to-output fiber counts for every \(2^k\). Metropolis–Rota's older necklace-ring work establishes algebraic product identities; its complete original text was not materially inspected and is a historical-priority risk. The distinction here is the exact parameterized residue distribution, its isometric branch mechanism, and the squarefree obstruction; it is not merely the known parity statement.

## Limitations
The uniform formula is proved for odd squarefree lengths greater than one, not even lengths. For odd nonsquarefree lengths only an inclusion in \(8\mathbb Z_2\) is claimed. The theorem distributes \(M_n(x)\) as \(x\) varies through all input residues or all two-adic integers; it does not claim that actual finite-field sizes, which must be prime powers, are equidistributed among these input residues. A search and implication comparison of accessible literature did not locate an equivalent theorem, but absence of a match is not an independent proof of historical novelty. No independent mathematical audit has been performed.

## References
1. J. von zur Gathen, A. Viola, K. Ziegler, *Counting reducible, powerful, and relatively irreducible multivariate polynomials over finite fields*, arXiv:0912.3312v1 (first publicly submitted 2009-12-17), especially the univariate irreducible count formula in §3. Primary MSC 11T06.
2. P. Moree, *The formal series Witt transform*, arXiv:math/0311194v1 (first publicly submitted 2003-11-12), published in *Discrete Mathematics* 295 (2005), 143–160. Introduction gives the known parity statement.
3. T. Hyde, *Cyclotomic factors of necklace polynomials*, arXiv:1811.08601v1 (first publicly submitted 2018-11-21), especially Theorems 1.3 and 2.24 on cyclotomic and local factors.
4. N. Metropolis, G.-C. Rota, *Witt vectors and the algebra of necklaces*, *Advances in Mathematics* 50 (1983), 95–125, doi:10.1016/0001-8708(83)90035-X. Background product identities; full primary text not inspected.
