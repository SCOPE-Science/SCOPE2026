# Exact endpoint norm of the full second symmetric-group Fourier level
## Finding
For every integer \(n\ge4\), let \(G=S_n\), and let \(P_n^{[2]}\) be the central orthogonal Fourier projection on \(\ell^2(G)\) onto **both** irreducible regular-representation isotypic blocks indexed by the partitions \((n-2,2)\) and \((n-2,1,1)\). These are exactly the two partitions whose first row has deficit two. Write
\[
N_n=n^2-3n+1,\qquad E_m=\sum_{j=0}^{m}\frac{(-1)^j}{j!} \quad (m\ge0).
\]
Then its sharp endpoint norms coincide and are given by the closed formula
\[
\boxed{\|P_n^{[2]}\|_{\ell^1\to\ell^1}=\|P_n^{[2]}\|_{\ell^\infty\to\ell^\infty}=\frac{3N_n}{2}E_{n-2}+\frac{(-1)^{n-2}(5-n^2)}{2(n-1)!}.}
\]
The degree-normalized norm has the exact asymptotic law
\[
\boxed{\lim_{n\to\infty}\frac{\|P_n^{[2]}\|}{N_n}=\frac{3}{2e}},
\]
with factorially decaying error \(O(1/(n-1)!)\) after normalization.

More precisely, if \(F(g)\) is the number of fixed points and \(C_2(g)\) the number of two-cycles of \(g\in S_n\), then the unnormalized central projection kernel has the strict sign law
\[
\operatorname{sgn} K_n(g)<0\quad\Longleftrightarrow\quad F(g)\in\{1,2\},
\]
**independently of the number of two-cycles**. On this negative region, the unnormalized kernel equals \(-n(n-3)/2-C_2(g)\). For the complementary Fourier projection one also has the sharp identity
\[
\|I-P_n^{[2]}\|_{\ell^1\to\ell^1}=\|I-P_n^{[2]}\|_{\ell^\infty\to\ell^\infty}=1+\|P_n^{[2]}\|-\frac{2(d_A^2+d_B^2)}{n!},
\]
where \(d_A=n(n-3)/2\) and \(d_B=(n-1)(n-2)/2\).

## Assumptions and scope
All Fourier projections use the complex group algebra of \(S_n\). Spaces \(\ell^p(S_n)\) use counting measure; replacing counting by normalized counting leaves the induced norms unchanged. Each isotypic block includes **all** matrix coefficients of the corresponding irreducible, not just a spherical vector on the space of two-element subsets. The central kernel, in convolution with counting measure, is
\[
k_n(g)=\frac1{n!}\bigl(d_A\chi_A(g^{-1})+d_B\chi_B(g^{-1})\bigr),
\]
where \(\chi_A\) and \(\chi_B\) are the characters indexed respectively by \((n-2,2)\) and \((n-2,1,1)\). The polynomial in the parentheses is denoted \(K_n(g)\). These are distinct irreducibles even at \(n=4\), and the formula holds at this boundary.

## Proof
First derive the two characters without a character table. The natural permutation representation \(\mathbb C^n\) decomposes as the trivial module plus the standard module \(V\) of degree \(n-1\), with character \(F-1\). The permutation module on unordered two-subsets decomposes multiplicity-freely as the trivial, standard, and \((n-2,2)\) modules. Its character counts fixed unordered pairs, namely \(\binom F2+C_2\). Subtracting \(F\) gives
\[
\chi_A(g)=\binom{F(g)}2+C_2(g)-F(g)=\frac{F(g)(F(g)-3)}2+C_2(g).
\]
On the other hand, \(\bigwedge^2 V\) is the irreducible module of shape \((n-2,1,1)\), whose character satisfies the standard exterior-square identity
\[
\chi_B(g)=\frac{(F(g)-1)^2-(F(g^2)-1)}2=\frac{(F(g)-1)(F(g)-2)}2-C_2(g),
\]
using \(F(g^2)=F(g)+2C_2(g)\). The respective degrees at the identity are \(d_A=n(n-3)/2\) and \(d_B=(n-1)(n-2)/2\). Their sum is \(N_n=n^2-3n+1\).

Therefore the degree-weighted central character simplifies to
\[
K_n(g)=d_A\frac{F(g)(F(g)-3)}2+d_B\frac{(F(g)-1)(F(g)-2)}2-C_2(g),
\]
since \(d_A-d_B=-1\). This cancellation of almost all dependence on two-cycles is the key point. If \(F=1\) or \(F=2\), the displayed value is \(-d_A-C_2<0\). If \(F=0\) or \(F=3\), the value is \(d_B-C_2>0\), because \(C_2\le n/2<d_B\) for \(n\ge4\). If \(F\ge4\), both quadratic coefficients are strictly positive and \(C_2\le n/2\), so \(K_n>0\). This proves the exact sign law.

Since both characters are nontrivial, \(\sum_{g\in G}K_n(g)=0\). For convolution with a kernel on a finite group, both endpoint induced norms equal its \(\ell^1\) mass: a point mass is an \(\ell^1\) extremizer, and sign matching on a row is an \(\ell^\infty\) extremizer. Consequently
\[
\|P_n^{[2]}\|=\frac2{n!}\sum_{F(g)\in\{1,2\}}(d_A+C_2(g)).
\]
Let \(D_m\) count permutations of \(m\) letters with no fixed points, with \(D_0=1\), and write \(b_m=D_m/m!=\sum_{j=0}^{m}(-1)^j/j!\). The number of permutations with exactly \(r\) fixed points is \(\binom nrD_{n-r}\). The total number of two-cycles among permutations with exactly \(r\) fixed points is
\[
\binom nr\binom{n-r}{2}D_{n-r-2},
\]
because one marks a two-cycle and deranges the unmarked remaining letters. Thus the exact norm is
\[
\|P_n^{[2]}\|=2d_A\left(b_{n-1}+\frac12b_{n-2}\right)+b_{n-3}+\frac12b_{n-4}.
\]
Using \(b_m-b_{m-1}=(-1)^m/m!\) and \(2d_A+1=N_n\), this simplifies algebraically to
\[
\|P_n^{[2]}\|=\frac{3N_n}{2}b_{n-2}+\frac{(-1)^{n-2}(5-n^2)}{2(n-1)!},
\]
which is the first boxed identity. The alternating-series error bound \(|b_m-e^{-1}|\le1/(m+1)!\) proves the limit and its factorial rate.

Finally the identity operator has convolution kernel \(\delta_e\). The central projection kernel at the identity is \((d_A^2+d_B^2)/n!<1\), because the regular representation of \(S_n\) also contains other irreducibles, so its positive identity coefficient remains positive in \(\delta_e-k_n\). All other coefficients are simply negated. Therefore the complementary endpoint norm is \(1+\|P_n^{[2]}\|-2(d_A^2+d_B^2)/n!\), as claimed.

## Verification
The accompanying standalone `verify.py` uses only the Python 3 standard library. It enumerates every permutation for each \(4\le n\le9\), reconstructs the two characters independently from fixed-point and two-cycle counts, verifies the exact sign law, checks zero signed mass and direct absolute kernel sums against the theorem, and compares both finite derangement formulas. It also verifies the derangement inclusion-exclusion formula for sizes through 60 and checks the normalized asymptotics numerically. Its terminal marker is `VERIFY_OK exact_all_permutations_n4_to9 full_second_level_n4_to60`.

Exact initial norms are \(17/6\) at \(n=4\), \(71/12\) at \(n=5\), \(1267/120\) at \(n=6\), and \(5753/360\) at \(n=7\). These finite enumerations corroborate, but are not substitutes for, the all-\(n\) proof.

## Relationship to prior work
The stable character-polynomial framework of Church, Ellenberg and Farb and the symmetric-group character estimates of Müller and Schlage-Puchta supply the representation-theoretic setting. The two individual characters and the finite-group central-idempotent construction are classical. Existing exact endpoint results for the **single** \((n-2,2)\) block do not determine the norm of the **sum** of its kernel with the distinct \((n-2,1,1)\) kernel, because taking absolute values after adding central kernels is not additive. A published exact norm for a degree-two Johnson spherical projector instead acts on a homogeneous two-subset space, not on the entire regular group algebra. A published standard-block norm treats the distinct \((n-1,1)\) representation. Sanders's nonabelian idempotent theorem controls Fourier-algebra norms of indicator functions rather than endpoint norms of these isotypic operators. The additional exact cancellation \(d_A-d_B=-1\) and ensuing one-statistic strict sign law are the distinguishing content here.

## Limitations
This is the central Fourier projection onto exactly the **two** first-row-deficit-two irreducibles; it is not the projection onto every constituent of the tensor square of the standard module (which includes lower levels), and is not a claim about arbitrary irreducible layers, intermediate \(\ell^p\) norms or a continuous group. The sign-law reduction and exact norm are not claimed to establish exhaustive historical priority; an older general character-polynomial absolute-moment formula might imply the identity without naming this layer. The proof is an elementary exact argument, independently of finite experiments. Independent external mathematical auditing is not part of this package.

## References
1. T. W. Müller and J.-C. Schlage-Puchta, *Character Theory of Symmetric Groups, Subgroup Growth of Fuchsian Groups, and Random Walks*, arXiv:math/0305260 (first public 2003-05-18), Sections 2.2 and 5.2.
2. T. Church, J. Ellenberg and B. Farb, *FI-modules and stability for representations of symmetric groups*, arXiv:1204.4533 (first public 2012-04-20), Sections 1 and 2.9.
3. T. Sanders, *A quantitative version of the non-abelian idempotent theorem*, arXiv:0912.0308 (first public 2009-12-02), Introduction.
4. Published mathematical result, *Derangement density controls the standard Fourier block of every doubly transitive action*, publicly available in the 2026 mathematics archive.
5. Published mathematical result, *Exact endpoint norm of the second Johnson spherical projector*, publicly available in the 2026 mathematics archive.
