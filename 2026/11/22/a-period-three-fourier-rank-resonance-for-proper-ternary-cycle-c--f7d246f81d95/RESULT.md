# A period-three Fourier rank resonance for proper ternary cycle colourings

## Finding

Let \(n\geq3\), let \(G_n=(\mathbb Z/3\mathbb Z)^n\), and let \(f_n:G_n\to\{0,1\}\) indicate proper three-colourings of the labelled cycle \(C_n\): \(f_n(x)=1\) precisely when \(x_i\neq x_{i+1}\) for every cyclic edge. For the unnormalized Fourier transform \(W_n(\xi)=\sum_{x\in G_n}f_n(x)\exp(2\pi i\sum_i\xi_i x_i/3)\), define \(T_ng=f_n*g\), with unnormalized convolution on \(G_n\).

If \(\sum_i\xi_i\neq0\pmod3\), then \(W_n(\xi)=0\). For balanced \(\xi\) define \(\beta_i=\sum_{j=i}^{n-1}\xi_j\in\mathbb Z/3\mathbb Z\) for \(1\leq i\leq n-1\), and let \(a,b,c\) count the occurrences of \(0,1,2\) among these \(n-1\) values, respectively. Then the exact, signed Fourier multiplier is

\[
W_n(\xi)=(-1)^{n-1}\bigl(2(-2)^a-(-2)^b-(-2)^c\bigr).
\]

Each ordered triple \((a,b,c)\) with \(a+b+c=n-1\) contributes exactly \((n-1)!/(a!b!c!)\) balanced frequencies carrying that value, even when distinct triples yield the same value. This specifies the entire signed spectrum, including coincident levels.

**Sharp rank transition.** If \(n\not\equiv1\pmod3\), then \(\operatorname{rank}T_n=3^{n-1}\): the only Fourier zeros are the compulsory nonbalanced ones. If \(n=3k+1\), \(k\geq1\), define

\[
Z_k=\frac{(3k)!}{(k!)^3}\frac{3k+1}{k+1}.
\]

Then exactly \(Z_k\) further balanced frequencies vanish and

\[
\operatorname{rank}T_{3k+1}=3^{3k}-Z_k,
\qquad\operatorname{nullity}T_{3k+1}=3^{3k+1}-3^{3k}+Z_k.
\]

The extra vanishing frequencies are **exactly** the three count patterns \((a,b,c)=(k,k,k),(k-1,k,k+1),(k-1,k+1,k)\). In the resonant subsequence,

\[
\frac{Z_k}{3^{3k}}\sim\frac{3\sqrt3}{2\pi k},\qquad k\to\infty.
\]

Thus the additional information loss occurs at infinitely many lengths, but its fraction of the balanced Fourier space tends to zero.

## Assumptions and scope

All colours and Fourier frequencies lie in the additive group \(\mathbb Z/3\mathbb Z\). The cycle is simple with \(n\geq3\) labelled vertices \(0,1,\ldots,n-1\), connected cyclically. Fourier and convolution are **unnormalized**: \((f*g)(x)=\sum_{y\in G_n}f(y)g(x-y)\). Rank and nullity are dimensions over \(\mathbb C\), or equivalently over \(\mathbb R\) for this real symmetric convolution kernel. A balanced frequency means \(\sum_{i=0}^{n-1}\xi_i=0\pmod3\).

## Proof

**Step 1: translation symmetry and a bijective coordinate change.** Adding a common colour to all vertices preserves properness. Summing over this global colour therefore kills every nonbalanced Fourier frequency. For a balanced frequency set \(y_i=x_i-x_{i-1}\in\{1,2\}\) for \(1\leq i<n\). The last cycle edge is proper exactly when \(\sum_{i=1}^{n-1}y_i\neq0\) in \(\mathbb Z/3\mathbb Z\). The character exponent becomes \(\sum_{i=1}^{n-1}\beta_i y_i\) because its root-colour coefficient is zero. The linear map from balanced \(\xi\) to \(\beta\in(\mathbb Z/3\mathbb Z)^{n-1}\) is a bijection: \(\xi_0=-\beta_1\), \(\xi_i=\beta_i-\beta_{i+1}\) for \(1\leq i<n-1\), and \(\xi_{n-1}=\beta_{n-1}\).

**Step 2: exact Fourier evaluation.** Write \(m=n-1\), \(\omega=e^{2\pi i/3}\) and \(A(t)=\sum_{y\in\{1,2\}}\omega^{ty}\), so \(A(0)=2\), \(A(1)=A(2)=-1\). Summing over the root colour and subtracting closed chains via character orthogonality gives

\[
W_n(\xi)=3\prod_{i=1}^{m}A(\beta_i)
-\sum_{t=0}^{2}\prod_{i=1}^{m}A(\beta_i+t).
\]

For occupancy counts \((a,b,c)\), the first product is \((-1)^m(-2)^a\); the other two products are \((-1)^m(-2)^b\) and \((-1)^m(-2)^c\). This proves the displayed signed formula. The occupancy multiplicity follows from the bijection in Step 1.

**Step 3: complete zero classification.** The zero equation is \(2(-2)^a=(-2)^b+(-2)^c\). If \(b=c\), equality forces \(a=b=c\). Otherwise exchange \(b,c\) so that \(b<c\). Factoring the right side as \((-2)^b(1+(-2)^{c-b})\), the factor in parentheses is odd. Comparison of exact powers of two therefore gives \(b=a+1\). Dividing by \((-2)^b\) leaves \(-1=1+(-2)^{c-b}\), hence \(c=b+1\). Thus the only remaining patterns are \((a,b,c)=(r,r+1,r+2)\) and \((r,r+2,r+1)\), with \(r\geq0\). All zero patterns have \(a+b+c\) divisible by three. For \(n=3k+1\) this yields precisely the three stated count patterns.

**Step 4: rank and asymptotics.** Balanced frequencies number \(3^{n-1}\). The three vanishing patterns contribute

\[
\frac{(3k)!}{(k!)^3}+2\frac{(3k)!}{(k-1)!k!(k+1)!}
=\frac{(3k)!}{(k!)^3}\frac{3k+1}{k+1}.
\]

Fourier characters diagonalize convolution, so subtracting these additional zeros proves the rank and nullity. Stirling's formula gives \((3k)!/(k!)^3\sim3^{3k}\sqrt3/(2\pi k)\), and the final ratio follows.

## Verification

Two dependency-free exact-arithmetic Python programs accompany the proof. Execute `python3 check_increments.py` and `python3 check_vertices.py` from the directory containing these files. The first sums over all nonzero edge increments, tests **every** balanced frequency for \(3\le n\le9\), and checks the complete signed formula and predicted nullities. The second independently enumerates proper vertex colourings and evaluates exact character sums by three residue buckets for **every** balanced frequency for \(3\le n\le8\); it uses no edge-difference enumeration to evaluate those sums. Both print `PASS` on completion. Their finite tests corroborate but do not replace Steps 1–4.

Selected exact outputs (\(n\), additional balanced nullity, convolution rank): \((3,0,9)\), \((4,12,15)\), \((7,210,519)\), \((10,4200,15483)\); the last values follow from the all-length formula and can be calculated with integer factorials.

## Relationship to prior work

Finite-abelian Fourier analysis of graph-colouring models and their tension/flow descriptions is classical; Goodall [1] develops that framework. The Fourier expansion of group-valued hard-constraint graph colouring is treated by Babson and Beck [2], whose main object is the aggregate number of colourings, rather than the individual vertex-frequency convolution multipliers and their exact zero multiplicities. The Potts transfer-matrix methods of Bedini and Jacobsen [3] compute counting partition functions and chromatic polynomials, not this ternary Fourier rank transition. These methodological antecedents are credited rather than asserted as novel. The present claim is the period-three classification of **all** vertex-frequency zeros and their exact multiplicities in the ternary cycle family.

## Limitations

The proof applies to the three-element additive palette and simple cycles of length at least three. It does not classify convolution rank for larger palettes, general graphs, or weighted colouring models. The full formula is unnormalized and must not be confused with a degree-one sampling Gram spectrum. The result is mathematically proved here but has not received independent external review; an unindexed earlier equivalent calculation remains a priority risk.

## References

[1] A. Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, arXiv:0806.4848 (first public 2008-06-30), https://arxiv.org/abs/0806.4848 .

[2] E. Babson and M. Beck, *Counting Group Valued Graph Colorings*, arXiv:1204.1283 (2012-04-05), https://arxiv.org/abs/1204.1283 .

[3] A. Bedini and J. L. Jacobsen, *A tree-decomposed transfer matrix for computing exact Potts model partition functions for arbitrary graphs, with applications to planar graph colourings*, arXiv:1003.4847 (2010-03-25), https://arxiv.org/abs/1003.4847 .
