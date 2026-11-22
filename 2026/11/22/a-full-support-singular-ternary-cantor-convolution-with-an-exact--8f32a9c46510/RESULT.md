# A full-support singular ternary Cantor convolution with an exact collision law

## Finding

Let \(C\subset\mathbb Z_3\) be the ternary digit Cantor set consisting of numbers with all digits in \(\{0,1\}\). Let \(\mu\) be the fair Bernoulli digit probability measure on \(C\), and let \(\nu\) be the distribution of \(X+2Y\) for independent \(X,Y\sim\mu\). The following hold simultaneously.

1. The measure \(\nu\) has **full topological support** on \(\mathbb Z_3\), although it is **continuous and singular** with respect to normalized Haar measure. More precisely, the indicators that successive ternary output digits equal \(2\) are independent and identically distributed Bernoulli random variables of parameter \(1/4\). Haar-typical ternary digit-\(2\) frequency is \(1/3\), whereas \(\nu\)-typical frequency is \(1/4\).
2. Write
   \[
   A_k=\left\{\sum_{i=0}^{k-1}\epsilon_i3^i:\epsilon_i\in\{0,1\}\right\},\qquad
   R_k(t)=\#\{(x,y)\in A_k^2:x+2y\equiv t\pmod{3^k}\}.
   \]
   For every integer \(k\ge0\), every residue \(t\pmod{3^k}\) has \(R_k(t)\ge1\), with the convention that \(\mathbb Z/3^0\mathbb Z\) is a singleton. If \(h_2(t;k)\) counts the digits equal to \(2\) in the \(k\)-digit ternary expansion of \(t\), then for \(0\le j\le k\),
   \[
   \boxed{\sum_{\substack{t\bmod3^k\\h_2(t;k)=j}}R_k(t)=\binom{k}{j}3^{k-j}.}
   \]
3. The *ordered modular collision energy* \(E_k=\sum_{t\bmod3^k}R_k(t)^2\) satisfies
   \[
   \boxed{E_0=1,\quad E_1=6,\quad E_{k+2}=6E_{k+1}-2E_k\quad(k\ge0).}
   \]
   Its exact value and generating function are
   \[
   \boxed{E_k=\frac{(3+\sqrt7)^{k+1}-(3-\sqrt7)^{k+1}}{2\sqrt7},\qquad
   \sum_{k\ge0}E_kz^k=\frac{1}{1-6z+2z^2}.}
   \]
   The grid correlation dimension of \(\nu\) is therefore
   \[
   \boxed{D_2(\nu)=\log_3\!\left(\frac{16}{3+\sqrt7}\right)
   =0.9481829495698588\ldots<1.}
   \]

## Assumptions and scope

All probability spaces use countably many independent fair bits, and all arithmetic for the limiting measure is in the complete compact additive group \(\mathbb Z_3\). The two input variables are independent. The finite sets \(A_k\) contain **distinct values** (not weighted digits), and \(R_k\) counts **ordered** pairs with repetition allowed. Collisions are congruences modulo \(3^k\), not equality of ordinary integers. The correlation dimension claimed here is specifically the limit based on residue-class cylinders (equivalently the \(3\)-adic ball correlation dimension); no claim is made about a Euclidean convolution density. The statement concerns the weighted mixed sum \(X+2Y\), not the self-sum \(X+Y\) or a threefold sum.

## Proof

**Exact digit-and-carry matrices.** At each ternary position, let the input digits be \(\epsilon,\eta\in\{0,1\}\), and let the incoming carry be \(c\in\{0,1\}\). The outgoing digit and carry are the remainder and quotient on dividing \(\epsilon+2\eta+c\) by three. From carry zero, the four digit pairs yield \((d,c')=(0,0),(1,0),(2,0),(0,1)\). From carry one, they yield \((1,0),(2,0),(0,1),(1,1)\). Consequently the carry-count matrices, indexed by incoming and outgoing carries, are
\[
M_0=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
M_1=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad
M_2=\begin{pmatrix}1&0\\1&0\end{pmatrix}.
\]
For any residue with least-to-most-significant digits \(t=\sum_{i=0}^{k-1}d_i3^i\), its exact representation multiplicity is
\[
\boxed{R_k(t)=(1,0)M_{d_0}\cdots M_{d_{k-1}}\binom11.}
\]
This identity follows by induction on the digit positions; summing over both possible final carries is correct because the representation is only required modulo \(3^k\). In terms of a row carry-count state \((a,b)\), the three updates are
\[
0:(a,b)\mapsto(a,a+b),\qquad
1:(a,b)\mapsto(a+b,b),\qquad
2:(a,b)\mapsto(a+b,0).
\]
Every update maps a nonzero nonnegative row to another nonzero row. Starting with \((1,0)\) proves \(R_k(t)\ge1\) for all residues, including \(k=0\). The mass of each residue cylinder is exactly \(R_k(t)/4^k>0\), giving full support. In particular, the finite-level surjectivity and compactness of \(C\times C\) imply \(C+2C=\mathbb Z_3\).

**Independent exceptional-digit indicators and singularity.** Conditional on any previously chosen lower input digit pairs, the incoming carry is known and the next input digit pair is uniform on four possibilities. In **both** carry states, precisely one pair yields output digit \(2\). Thus the conditional probability that the next output digit is \(2\), given all prior input digits, is exactly \(1/4\), independently of the carry. Iterated conditioning proves that the successive indicators are independent Bernoulli\((1/4)\). Counting the \(4^k\) equally weighted input-pair words by the number of digit-\(2\) outputs gives the finite formula \(\binom{k}{j}3^{k-j}\). The strong law yields digit-\(2\) frequency \(1/4\) almost surely under \(\nu\). Haar measure gives independent uniform ternary output digits, whose digit-\(2\) frequency is almost surely \(1/3\). The two probability-one sets are disjoint, proving \(\nu\perp\mathrm{Haar}\). Since \(\mu\) assigns each length-\(k\) cylinder mass at most \(2^{-k}\), it is atomless; consequently \(\nu(\{t\})=\int\mu(\{t-2y\})\,d\mu(y)=0\) for every \(t\). Thus \(\nu\) is singular continuous despite full support.

**Exact collisions.** For each output word \(w\) of length \(k\), write \((a_w,b_w)=(1,0)M_w\), set
\[
E_k=\sum_w(a_w+b_w)^2,\qquad H_k=\sum_w a_wb_w.
\]
For any one row \((a,b)\), the three successor row-sums are \(2a+b\), \(a+2b\) and \(a+b\), while their pairwise coordinate products sum to \((a+b)^2\). Therefore
\[
(2a+b)^2+(a+2b)^2+(a+b)^2=6(a+b)^2-2ab,
\]
\[
E_{k+1}=6E_k-2H_k,\qquad H_{k+1}=E_k.
\]
The empty word gives \(E_0=1\) and \(H_0=0\). Therefore \(E_1=6\) and \(E_{k+2}=6E_{k+1}-2E_k\) for all \(k\ge0\). The characteristic roots are \(3\pm\sqrt7\), proving both exact closed form and generating function.

**Dimension.** Since every length-\(k\) residue cylinder has \(\nu\)-mass \(R_k(t)/4^k\), its collision probability is exactly
\[
\sum_{t\bmod3^k}\nu(t+3^k\mathbb Z_3)^2=E_k/16^k.
\]
The explicit positive-root formula above shows \(E_k\sim\frac{3+\sqrt7}{2\sqrt7}(3+\sqrt7)^k\). Taking minus logarithms and dividing by \(k\log3\) gives the claimed dimension, strictly below one because \(3+\sqrt7>16/3\).

## Verification

The independent finite enumerator in `check.py` constructs \(A_k\) directly for every \(1\le k\le8\), computes the full modular fiber histogram by iterating all \(4^k\) ordered pairs, and compares every residue fiber against the two-state matrix formula. It checks complete support, energy recurrence, and all binomial exceptional-digit counts, as well as a separate quadratic-moment recurrence. On the packaged source it returns `CHECK_OK 9935 finite exact assertions plus floating-point sanity check`. The real-valued closed-form and dimension comparisons are approximate sanity checks only; the all-depth identities follow from the exact matrix proof, not finite experiments.

## Relationship to prior work

Abram and Lagarias established general closure of \(p\)-adic path sets under Minkowski sums and multiplication by suitable rationals [1], and studied multiplicative intersections of the \(3\)-adic Cantor set [2]. Those structural theorems furnish a natural setting but do not state the specific *weighted probability convolution* and its independent indicator digits, singularity, complete modular fibers, or energy exponent. The integer sequence \(1,6,34,192,1084,\ldots\) and its order-two recurrence appear previously in OEIS A154244 [3], in a different numerical context. **No originality is claimed for this abstract recurrence or its bare numerical values.** The claim here combines its exact identification as the modular energy of \(C+2C\) with the weighted digit law and the full-support singular continuous measure; the numerical match is explicitly acknowledged. Earlier studies of different Cantor-digit convolutions may employ related finite-state methods, without implying the particular measure-theoretic conclusions in this setting.

## Limitations

The finite-level collision energy is **modular**, not ordinary integer additive energy. Full support does not mean absolute continuity; the measure is in fact singular. The digit-\(2\) indicators are independent, but the full ternary output digits are **not** asserted to be independent. The displayed dimension is the \(3\)-adic grid correlation dimension, not a formula for the full multifractal spectrum or an optimal density integrability exponent. Scholarly priority beyond the inspected sources remains subject to historical checking; a numerical recurrence alone is not a novel result. No external independent mathematical audit has been performed.

## References

1. W. Abram and J. C. Lagarias, *p-adic path set fractals and arithmetic*, arXiv:1210.2478, first publicly posted October 9, 2012; *Journal of Fractal Geometry* **1** (2014), 45–81. https://arxiv.org/abs/1210.2478 and https://doi.org/10.4171/JFG/2.
2. W. Abram and J. C. Lagarias, *Intersections of multiplicative translates of \(3\)-adic Cantor sets*, arXiv:1308.3133, first publicly posted August 14, 2013. https://arxiv.org/abs/1308.3133.
3. *OEIS A154244*, integer sequence with first terms \(1,6,34,192,1084,6120,\ldots\) and rational generating function; sequence entry dated January 5, 2009. https://oeis.org/A154244.
