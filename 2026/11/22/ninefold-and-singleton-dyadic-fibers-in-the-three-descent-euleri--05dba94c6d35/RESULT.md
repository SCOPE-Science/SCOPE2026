# Ninefold and singleton dyadic fibers in the three-descent Eulerian column

## Finding

Let \(E_n=\langle n,3\rangle\) denote the number of permutations of \(\{1,\ldots,n\}\) with exactly three descents, where \(n\ge4\). For any integers \(k\ge1\) and \(a\ge\max\{4,k\}\), put \(P_k=2^{k+1}\). The multiset of residues
\[
\{E_n\bmod2^k:a\le n<a+P_k\}
\]
contains each residue \(y\in\mathbb Z/2^k\mathbb Z\) with the following **exact** multiplicity:
\[
\boxed{
M_k(y)=
\begin{cases}
3,&k=1,2\ \text{and }y\equiv0\pmod2,\\
1,&k=1,2\ \text{and }y\equiv1\pmod2,\\
5,&k=3\ \text{and }y\equiv0,2\pmod8,\\
1,&k=3\ \text{and }y\not\equiv0,2\pmod8,\\
9,&k\ge4\ \text{and }y\equiv0,10\pmod{16},\\
1,&k\ge4\ \text{otherwise}.
\end{cases}}
\]
The **least eventual period** of \(E_n\bmod2^k\) is precisely \(P_k\). In particular every dyadic residue is attained infinitely often. Its limiting residue distribution is nonuniform: for every \(k\ge4\), the natural density of indices with residue \(y\) is \(9/2^{k+1}\) on the two classes \(0,10\pmod{16}\), and \(1/2^{k+1}\) elsewhere. Relative to normalized Haar measure on \(\mathbb Z_2\), this distribution has density
\[
\frac{1}{2}+4\mathbf1_{(16\mathbb Z_2)\cup(10+16\mathbb Z_2)}.
\]

## Assumptions and scope

The Eulerian number \(\langle n,j\rangle\) counts permutations with exactly \(j\) descents, indexed from \(j=0\). The classical inclusion–exclusion formula for three descents gives, for every \(n\ge4\),
\[
E_n=4^n-(n+1)3^n+\binom{n+1}{2}2^n-\binom{n+1}{3}.
\]
We distinguish the fixed **three-descent** column from the fixed two-descent column. A least eventual period means a smallest positive shift preserving all residues from some sufficiently late index onward. All assertions are at powers of two and concern actual integer counts, not probabilities on permutations of fixed size. The displayed threshold is sufficient and is not asserted to be best possible.

## Proof

**1. Reduction to a continuous dyadic expression.** Fix \(k\ge1\) and \(n\ge\max\{4,k\}\). The terms \(4^n\) and \(\binom{n+1}{2}2^n\) vanish modulo \(2^k\), so
\[
E_n\equiv G(n):=-(n+1)3^n-\binom{n+1}{3}\pmod{2^k}.
\]
The expression \(G(n)\) is integral for nonnegative \(n\) (the binomial coefficient is an integer). Separate parity, writing \(n=2t\) or \(n=2t+1\):
\[
U(t)=G(2t)=-(2t+1)9^t-\frac{4t^3-t}{3},
\qquad
V(t)=G(2t+1)=-6(t+1)9^t-\frac{2t(t+1)(2t+1)}{3}.
\]
The denominators are units in \(\mathbb Z_2\), and \(9^t=(1+8)^t\) extends continuously to every \(t\in\mathbb Z_2\) by its convergent binomial series.

**2. An even-index isometry.** For distinct nonnegative \(s,t\), the difference of the polynomial parts of \(U(t)\) and \(U(s)\), divided by \(t-s\), equals
\[
-\frac{4(t^2+ts+s^2)-1}{3},
\]
which is odd in \(\mathbb Z_2\). The difference of the exponential parts, divided by \(t-s\), is even: for \(t>s\), it is the sum of the even term \(-2\cdot9^t\) and a multiple of \((9^{t-s}-1)/(t-s)\), which belongs to \(8\mathbb Z_2\). Reversing \(s,t\) handles the other order. Consequently
\[
\boxed{\nu_2(U(t)-U(s))=\nu_2(t-s).}
\]
Thus \(U\) induces a permutation of every \(\mathbb Z/2^k\mathbb Z\), and the even indices in a block of length \(P_k\) contribute **one** occurrence of each residue.

**3. Four odd-index isometries with two different image balls.** Write \(q=9^4=6561\). For any nonnegative \(t\) and positive integer \(h\), direct subtraction yields
\[
-\frac{V(t+4h)-V(t)}{8h}
=\frac34\,9^t(t+1)\frac{q^h-1}{h}
+3\,9^{t+4h}
+\frac{6t(t+1)+1+12h(2t+1)+32h^2}{3}.
\]
The first summand belongs to \(8\mathbb Z_2\), because \(\nu_2(q^h-1)=5+\nu_2(h)\). The second and third summands are each congruent to \(3\pmod4\) (since \(t(t+1)\) is even). Their sum is therefore \(2\pmod4\). The left side has valuation exactly one; equivalently
\[
\boxed{\nu_2(V(t+4h)-V(t))=4+\nu_2(h).}
\]
The same equality holds for differences in either order. For each \(r\in\{0,1,2,3\}\), the map
\[
W_r(u)=\frac{V(r+4u)-V(r)}{16},\qquad u\in\mathbb Z_2,
\]
is well defined, is an isometry, and permutes every \(\mathbb Z/2^m\mathbb Z\), because the valuation identity gives \(\nu_2(W_r(u)-W_r(v))=\nu_2(u-v)\). Direct exact evaluation gives
\[
(V(0),V(1),V(2),V(3))\equiv(10,0,10,0)\pmod{16}.
\]
Hence the four odd-index charts take values in two full residue balls, each reached by two isometric charts: \(10+16\mathbb Z_2\) and \(16\mathbb Z_2\).

**4. Count fibers and minimal periods.** For \(k\ge4\), in any \(P_k=2^{k+1}\) consecutive index positions, each parity contributes \(2^k\) positions. The even half gives one of each target by Step 2. Among the odd half, each class \(t\equiv r\pmod4\) consists of \(2^{k-2}\) consecutive \(u\)-residues. The isometry \(W_r\) makes each residue in its ball appear exactly \(2^{k-2}/2^{k-4}=4\) times. Two charts have center zero and two center ten modulo 16. Thus the odd half contributes eight more occurrences for exactly the targets \(0,10\pmod{16}\), proving the \(9\)-versus-\(1\) formula. Reducing the modulo-16 histogram to smaller moduli gives the three cases for \(k=1,2,3\).

The chart descriptions show that \(G(n+P_k)\equiv G(n)\pmod{2^k}\) for every nonnegative \(n\), and so \(P_k\) is an eventual period of \(E_n\). Every eventual period must be even: \(V(t)\) is always even while the even branch \(U(t)\) takes odd values arbitrarily late. Write any eventual period as \(2d\). On sufficiently late even indices, it forces \(U(t+d)\equiv U(t)\pmod{2^k}\). Step 2 then forces \(2^k\mid d\). Therefore every eventual period is divisible by \(2^{k+1}\), proving leastness. Finally, periodicity and positive counts imply infinitely many occurrences of every residue and the stated natural densities; compatibility across all dyadic levels gives the Haar-density formula. \(\square\)

## Verification

Run `python3 verify.py` using only the Python standard library. It independently computes the Eulerian triangle using \(\langle n,j\rangle=(j+1)\langle n-1,j\rangle+(n-j)\langle n-1,j-1\rangle\), checks 101 three-descent terms against the exact exponential formula, compares 24,570 individual fiber counts in complete blocks for \(1\le k\le12\), checks 49,140 modular period shifts, and checks 3,810 exact two-adic isometry differences. The script returns `VERIFY_OK` and `all_levels_finite_checks=PASS` on success. These are finite corroborations only; the all-exponent proof is in Steps 1–4.

## Relationship to prior work

Krattenthaler's publicly posted November 2023 lecture on determining integer sequences modulo prime powers specifically lists Eulerian numbers among the motivating combinatorial examples. The classical finite-column Eulerian identity is not new: OEIS A000498 explicitly tabulates the three-descent column and gives exactly the same exponential formula, without the modular fiber claim in the inspected public excerpt. Cao and Pan (2006/2008) prove congruences for sums across Eulerian columns at a fixed size, not fixed-column value frequencies over varying sizes. Castro, González, and Medina (2015) investigate valuations of Eulerian numbers on index congruence classes, but the full primary text was not accessible; this is an explicit unresolved priority risk. Krattenthaler and Müller (2013) treat central Eulerian indices and mostly ternary prime-power congruences.

For a particularly close comparison, the published two-descent fixed-column result *Uniform dyadic residues in the two-descent Eulerian column with sharp onset* gives exactly **two** occurrences of every residue in an eventual period \(2^{k+1}\); its object is \(\langle n,2\rangle=3^n-(n+1)2^n+\binom{n+1}{2}\). It cannot imply the asymmetric nine-to-one law for the different object \(\langle n,3\rangle\). The published *Exact dyadic residue frequencies of the cubic binomial column* concerns \(\binom n3\) and has a different five-to-one law. This result neither claims those prior statements nor derives novelty from a partition of research topics; it computes and proves the new fixed three-descent image and multiplicities directly. A historical literature search cannot rule out every implicit earlier equivalent.

## Limitations

The result addresses exactly three descents and powers of two, with no assertion about higher descent columns or odd primes. The onset \(\max\{4,k\}\) is sufficient, not claimed optimal. The two-adic extension applies to the limiting formula \(G\), while the Eulerian sequence equals that formula only at the stated modular precisions and indices. The 2015 valuations paper was not inspected in full; prior coverage concealed in such material remains a priority risk. The result has not undergone independent mathematical audit.

## References

1. C. Krattenthaler, *A generating function method for the determination of differentially algebraic integer sequences modulo prime powers*, IHP lecture published **2023-11-27**, https://www.carmin.tv/en/video/a-generating-function-method-for-the-determination-of-differentially-algebraic-integer-sequences-mod, DOI:10.57987/IHP.2023.T3.WS3.SW.002.
2. H.-Q. Cao and H. Pan, *Congruences on Stirling numbers and Eulerian numbers*, first arXiv posting **2006-08-23**, https://arxiv.org/abs/math/0608564, *Acta Arith.* **132** (2008), 315–328.
3. F. N. Castro, O. E. González, and L. A. Medina, *The p-adic Valuation of Eulerian Numbers: Trees and Bernoulli Numbers*, *Experimental Mathematics* **24** (2015), 183–195, https://doi.org/10.1080/10586458.2014.981899.
4. C. Krattenthaler and T. W. Müller, *A method for determining the mod-3^k behaviour of recursively defined sequences*, first arXiv submission **2013-08-13**, https://arxiv.org/abs/1308.2856.
5. *Uniform dyadic residues in the two-descent Eulerian column with sharp onset*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-uniform-dyadic-residues-in-the-two-descent-eulerian-column-with--0b100cd06a37.
6. OEIS A000498, *Eulerian numbers (Euler’s triangle: column k=4)*, https://oeis.org/A000498; classic formula and first terms.
7. *Exact dyadic residue frequencies of the cubic binomial column*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-dyadic-residue-frequencies-of-the-cubic-binomial-column--2d5f4d6a8eb5.
