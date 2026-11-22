# Complete dyadic residue fibers of consecutive equal powers

## Finding
For every positive integer \(k\), define \(f_k(x)=x^k+(x+1)^k\). Put
\[
h(k)=\begin{cases}1,&k\text{ odd},\\2,&k=2,\\\nu_2(k)+2,&k\ge4\text{ even}.\end{cases}\]
For every integer \(n\ge1\) and residue \(a\bmod 2^n\), the exact number of solutions is
\[
\#\{x\bmod 2^n:f_k(x)\equiv a\pmod{2^n}\}
=\begin{cases}
2^{\min(n,h(k))},&a\equiv1\pmod{2^{\min(n,h(k))}},\\
0,&\text{otherwise}.
\end{cases}
\]
Consequently, the image over the ring of \(2\)-adic integers is exactly \(1+2^{h(k)}\mathbb Z_2\), of normalized Haar measure \(2^{-h(k)}\). If \(X\) is Haar-uniform on \(\mathbb Z_2\), then \(f_k(X)\) is uniform on that coset. For odd \(k\ge3\), each target in this coset has exactly two \(2\)-adic preimages; for \(k=2\), exactly two; for even \(k\ge4\), exactly four; and for \(k=1\), one. These are exact statements for all exponents and all dyadic moduli, not asymptotics.

## Assumptions and scope
The exponent \(k\) ranges through every positive integer, including odd and even exponents. The input \(x\) ranges over the entire residue ring \(\mathbb Z/2^n\mathbb Z\) or over \(\mathbb Z_2\); the adjacent summands must have precisely the same input \(x\), rather than varying independently. All solution counts modulo \(2^n\) count residues \(x\) once. By convention \(\nu_2(k)\) is the exponent of two in a positive integer \(k\). No integer representation claim over \(\mathbb Z\), nor an assertion for odd-prime-power moduli, is made.

## Proof
We use an elementary isometry observation. If \(G:\mathbb Z_2\to\mathbb Z_2\) satisfies \(\nu_2(G(u)-G(v))=\nu_2(u-v)\) for distinct \(u,v\), then for every \(m\ge1\) its induced map modulo \(2^m\) is injective, hence a permutation. Compactness (or compatible inverse limits) then makes \(G\) a bijective isometry of \(\mathbb Z_2\), preserving Haar probability. Here we prove the required identity on every indicated input branch.

**Odd exponents.** If \(k=1\), then \(f_1(x)=2x+1\), immediately giving the claim. Let \(k\ge3\) be odd. Since consecutive integers have opposite parity, \(f_k(x)\equiv1\pmod2\). For distinct \(x,y\) of the same parity write \(s=\nu_2(x-y)\ge1\). Of the two differences \(x^k-y^k\) and \((x+1)^k-(y+1)^k\), one has odd bases and one has even bases. The odd-base difference has valuation exactly \(s\): after division by the base difference, the sum of \(k\) odd monomials is odd. For the even bases, the same factorization bounds the valuation below by \(s+k-1\ge s+2\). Thus
\[
\nu_2(f_k(x)-f_k(y))=\nu_2(x-y)\qquad(x\equiv y\pmod2).
\]
For each \(r\in\{0,1\}\), the function \(G_r(z)=(f_k(r+2z)-1)/2\) is therefore a bijective isometry \(\mathbb Z_2\to\mathbb Z_2\). Both input parity branches map bijectively onto \(1+2\mathbb Z_2\); there are precisely two inverse branches.

**The quadratic exponent.** The identity \(f_2(x)=1+4T(x)\) holds for \(T(x)=x(x+1)/2\). If \(x\equiv y\pmod2\), then
\[
T(x)-T(y)=\frac{x-y}{2}(x+y+1),
\]
where \(x+y+1\) is odd. Consequently \(G_r(z)=T(r+2z)\), for \(r=0,1\), is a bijective isometry on \(\mathbb Z_2\). Hence each input parity branch maps bijectively onto \(1+4\mathbb Z_2\), giving two inverse branches.

**Even exponents at least four.** Write \(k=2^tu\) with \(t=\nu_2(k)\ge1\) and \(u\) odd, and put \(h=t+2\). The inequality \(k\ge h\) holds for every even \(k\ge4\). For any odd \(w\), the standard binary lifting identity gives \(w^k\equiv1\pmod{2^h}\): the group of odd units modulo \(2^h\) has exponent dividing \(2^t\). An even base has its \(k\)-th power divisible by \(2^k\). Since one of \(x,x+1\) is odd, it follows that \(f_k(x)\equiv1\pmod{2^h}\).

Take distinct \(x,y\) with \(x\equiv y\pmod4\), and set \(s=\nu_2(x-y)\ge2\). Among the two power differences composing \(f_k(x)-f_k(y)\), one involves odd bases \(a,b\) with \(a\equiv b\pmod4\), so \(\nu_2(a+b)=1\). Binary lifting for an even exponent gives
\[
\nu_2(a^k-b^k)=\nu_2(a-b)+\nu_2(a+b)+\nu_2(k)-1=s+t.
\]
The other difference has even bases and hence valuation at least \(s+k-1\), strictly greater than \(s+t\) because \(k-1>t\). Therefore
\[
\nu_2(f_k(x)-f_k(y))=\nu_2(x-y)+t
\qquad(x\equiv y\pmod4).
\]
For each \(r\in\{0,1,2,3\}\), the normalized polynomial function
\[
G_r(z)=\frac{f_k(r+4z)-1}{2^{t+2}}
\]
is well-defined over \(\mathbb Z_2\) and is a bijective isometry, since the displayed equality becomes \(\nu_2(G_r(z)-G_r(w))=\nu_2(z-w)\). Thus all four residue branches map bijectively onto the same entire coset \(1+2^h\mathbb Z_2\).

**Finite fibers and the limiting law.** For each exponent, the maps on the relevant two-adic input branches are surjective isometries after the stated normalization. For \(n\ge h\), each branch has equal numbers of preimages for each target modulo \(2^n\): the target has \(2^{n-h}\) possibilities and each branch has \(2^{n-b}\) inputs modulo \(2^n\), where \(b=1\) for odd \(k\ge3\) and \(k=2\), and \(b=2\) for even \(k\ge4\). Hence each branch contributes \(2^{h-b}\) and all \(2^b\) branches contribute \(2^h\). For \(k=1\), the direct linear identity gives \(2\). For \(n<h\), every input maps to \(1\pmod{2^n}\), giving \(2^n\) solutions for that target and zero for all other targets. These counts yield the claimed formula. The branch isometries preserve normalized Haar probability, so the output is uniformly distributed on its complete coset image.

## Verification
The accompanying dependency-free Python program `verify.py` calculates every fiber by direct modular exponentiation for a broad set of exponents and dyadic moduli, and independently checks the defining valuation identities on all pairs within selected residue branches. The infinite proof is the branchwise valuation argument above; finite tests only catch implementation or algebraic mistakes.

## Relationship to prior work
Arias, Borja and Anaya (2023) treat modular images of sums of \(k\)-th powers with independently chosen variables, including \(x^k+y^k\). Their unrestricted two-variable image statistics do not identify the distribution of the constrained line \(y=x+1\). Related published modular results on full dyadic representation laws for two independently varying even powers, and on unrestricted subthreshold sums of even powers, likewise do not directly imply the correlated-input fiber law. Patel and Siksek (2017) study Diophantine perfect powers that equal sums of consecutive like powers; their existence and nonexistence results have a different target and quantification. The present finding supplies a complete image and exact uniform fiber classification for the constrained two-consecutive-term sum, across every positive exponent.

## Limitations
The local mapping criterion can be approached using standard lifting and isometry techniques; no fundamentally new local-field lemma is claimed. Published results may implicitly encode an equivalent special case without naming this constrained map, and bibliographic priority is not conclusively established by database searches. The full result is restricted to dyadic moduli, not general composite moduli. Numeric verification is finite and does not replace the proof. Independent mathematical validation has not been performed.

## References
1. F. Arias, J. Borja and S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences **26** (2023), Article 23.8.1, first published 2023-08-28. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.html
2. V. Patel and S. Siksek, *On powers that are sums of consecutive like powers*, Research in Number Theory **3** (2017), Article 2, published 2017-02-14. https://doi.org/10.1007/s40993-016-0068-0
3. *Full \(2\)-adic representation laws for sums of two even powers*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-full-2-adic-representation-laws-for-sums-of-two-even-powers--4a65caa0042e
4. *Exact subthreshold dyadic images of even-power sums*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-subthreshold-dyadic-images-of-even-power-sums--43f52adb715f
