# Parity-rigid ternary Fourier recovery on all complete bipartite graphs

## Finding

Let \(K_{m,n}\) be the labelled complete bipartite graph with two nonempty shores of cardinalities \(m,n\ge1\), and write \(P_{m,n}\) for its proper three-colourings in the additive alphabet \(\mathbb Z/3\mathbb Z\). Set \(\omega=\exp(2\pi i/3)\), and define the unnormalized Fourier multiplier
\[
W_{m,n}(\alpha,\beta)=\sum_{(x,y)\in P_{m,n}}\omega^{\sum_{i=1}^{m}\alpha_i x_i+\sum_{j=1}^{n}\beta_j y_j}.
\]
For any frequency, put \(A=\sum_i\alpha_i\), \(B=\sum_j\beta_j\) modulo three, and let \(a=|\{i:\alpha_i=0\}|\), \(b=|\{j:\beta_j=0\}|\). Then
\[
\boxed{W_{m,n}(\alpha,\beta)=
\begin{cases}
0,&A+B\ne0,\\
3\left((-1)^{m-a}2^a+(-1)^{n-b}2^b+1-3\mathbf1_{A=0}\right),&A+B=0.
\end{cases}}
\]
An **additional zero** means a vanishing multiplier satisfying the unavoidable balance condition \(A+B=0\). Additional zeros exist **if and only if both shores have even size**. For even \(m,n\), their complete classification is the following five disjoint frequency types:

| Number of zero frequencies \((a,b)\) | Shore sum \(A\) modulo three |
|---|---|
| \((0,0)\) | \(0\) |
| \((0,1)\) | \(1\) or \(2\) |
| \((1,0)\) | \(1\) or \(2\) |
| \((1,2)\) | \(0\) |
| \((2,1)\) | \(0\) |

Write \(U_r=(2^r+2(-1)^r)/3\) and \(V_r=(2^r-(-1)^r)/3\) for nonnegative integers \(r\). The exact count of additional zeros is \(E_{m,n}=0\) unless both \(m,n\) are even. In the even-even case,
\[
\boxed{E_{m,n}=U_mU_n+m\binom n2U_{m-1}U_{n-2}
+\binom m2nU_{m-2}U_{n-1}
+2nV_mV_{n-1}+2mV_{m-1}V_n.}
\]
Hence counting convolution by the proper-colouring indicator on \(\ell^2((\mathbb Z/3\mathbb Z)^{m+n})\) has rank
\[
\boxed{\operatorname{rank}(\mathbf1_{P_{m,n}}*)=3^{m+n-1}-E_{m,n}.}
\]
For even-even shore sizes other than \((2,2)\), the first extra Fourier zero has character support degree exactly \(m+n-3\); when \((m,n)=(2,2)\), that first degree is three. In particular, **every** balanced Fourier frequency is nonvanishing whenever at least one shore has odd size, and the high-degree blind modes in the even-even case are completely classified.

## Assumptions and scope

The graph is simple, labelled, with nonempty shores; three colours are represented by residues modulo three. Properness requires different colours across every edge, while repetitions within either shore are allowed. Character exponents and shore sums are interpreted modulo three. Fourier transforms and convolution use counting, not probability normalization. The elementary count of proper colourings is \(|P_{m,n}|=3(2^m+2^n-2)\). The rank is over \(\mathbb C\); this is also the rank of the convolution matrix over \(\mathbb R\) after complexification. A frequency's support degree is the number of nonzero coordinate frequencies.

## Proof

**1. Colouring decomposition and Fourier multiplier.** Every proper three-colouring of \(K_{m,n}\) has at least one monochromatic shore, since the palettes on the two shores are nonempty and disjoint subsets of a three-element alphabet. Split the colouring set into those with the left shore monochromatic and those with the right shore monochromatic; subtract the colourings with both shores monochromatic to correct their overlap. For a fixed colour \(c\),
\[
\sum_{u\in\mathbb Z/3\mathbb Z\setminus\{c\}}\omega^{tu}
=\begin{cases}2,&t=0,\\-\omega^{tc},&t\ne0.\end{cases}
\]
Therefore the left-monochromatic contribution is \(3(-1)^{n-b}2^b\) when \(A+B=0\), and zero otherwise; the right-monochromatic contribution is \(3(-1)^{m-a}2^a\) when balanced. The both-monochromatic contribution, which was counted twice and must be subtracted once, is
\[
\sum_{c\ne d}\omega^{Ac+Bd}
=9\mathbf1_{A=0}\mathbf1_{B=0}-3\mathbf1_{A+B=0}.
\]
Combining these identities proves the boxed multiplier formula. The same expression at frequency zero equals \(3(2^m+2^n-2)\), independently checking the total colouring count.

**2. Complete zero classification.** Restrict to balanced frequencies. The zero equation becomes
\[
(-1)^{m-a}2^a+(-1)^{n-b}2^b=
\begin{cases}-1,&A\ne0,\\2,&A=0.\end{cases}
\]
For \(A\ne0\), parity shows exactly one of \(a,b\) is zero, and a two-adic comparison forces \((a,b)=(0,1)\) with signs \((+,-)\), or \((a,b)=(1,0)\) with signs \((-,+)\). These sign conditions say exactly that \(m,n\) are even. For \(A=0\), the only signed-power-of-two solutions are \((a,b)=(0,0)\), with both signs positive, and \((a,b)=(1,2)\) or \((2,1)\), with the exponent-one term negative and the exponent-two term positive. Again all require both shores to have even size. Conversely the five listed classes give exact cancellation when the shore sizes are even. Extra zeros genuinely exist in every even-even case because choosing an equal number of the two nonzero frequency symbols on each shore produces \((a,b,A)=(0,0,0)\).

**3. Exact class counts.** For \(r\ge0\), the number of length-\(r\) words in the nonzero alphabet \(\{1,2\}\) with coordinate sum zero is \(U_r\), and the number with sum any specified nonzero residue is \(V_r\). Indeed, the roots-of-unity filter on \((\omega+\omega^2)^r=(-1)^r\) yields these formulas. For fixed zero counts \((a,b)\), the zero positions may be chosen in \(\binom ma\binom nb\) ways. In a zero-sum class the two shores contribute \(U_{m-a}U_{n-b}\) assignments. In a nonzero-sum class they contribute \(2V_{m-a}V_{n-b}\) assignments, the factor two accounting for the two possible nonzero residues of \(A\). Adding the five disjoint class contributions gives exactly \(E_{m,n}\). There are \(3^{m+n-1}\) balanced frequencies. Fourier diagonalization of finite group convolution now proves the rank formula.

**4. First vanishing support degree.** The five classes have support degrees \(m+n\), \(m+n-1\), \(m+n-1\), \(m+n-3\), \(m+n-3\), respectively. For \(m=n=2\), the last two classes cannot occur because \(U_1=0\), whereas the middle classes occur. If at least one even shore has size at least four, one of the last two classes occurs: for example, when \(n\ge4\), choose \(a=2,b=1\) and use \(U_{m-2}\ge1\) and \(U_{n-1}>0\). This gives precisely the asserted first support degrees, including all boundary cases.

## Verification

The included `check_bipartite.py` directly enumerates proper colourings and their cyclotomic character sums as integer pairs in \(\mathbb Z[\omega]\), checking small shore pairs including \((2,2)\), \((3,4)\), and \((4,4)\). Independently, `check_group_transform.py` constructs the full colouring indicator, performs an exact three-point discrete Fourier transform along every coordinate, and checks the complete multiplier and rank predictions for six small cases. Both scripts require only Python's standard library and run as `python3 check_bipartite.py` and `python3 check_group_transform.py` in the same directory. Examples: the ranks are \(15\) for \((2,2)\), \(179\) for \((2,4)\), \(243\) for \((3,3)\), and \(1719\) for \((4,4)\). The proof is all-order; computations are independent finite stress tests, not substitutes for the power-of-two classification and the character-sum argument.

## Relationship to prior work

Gebhard and Sagan's noncommutative chromatic symmetric function records the labelled proper-colouring structure and gives a deletion-contraction calculus, but does not state the present additive character multipliers or their complete nullity classification. Sokal's Potts/chromatic-polynomial formulation supplies the classical counting context but does not address the Fourier transform in arbitrary vertex-frequency directions. The published first-coordinate Fourier sampling result for complete bipartite proper colourings computes a positive first-degree Gram spectrum; it does not classify the full convolution zero locus or identify the even-even high-degree blind modes. The previously treated thin-shore special case \(K_{2,n}\) is subsumed, not claimed as an independent contribution. The all-shore-size parity criterion, five zero classes, exact rank and first cancellation degree are the present mathematical result. Searches did not identify an equivalent table or stronger all-frequency theorem, but lack of a result in searches is not proof of historical priority.

## Limitations

The theorem is specific to the three-state additive alphabet and complete bipartite graphs with nonempty shores. It does not give a sharp nonzero Fourier multiplier gap, all nonzero spectral multiplicities, or analogous claims for four or more colours, incomplete bipartite graphs or general Potts interactions. Some broader colour-pattern enumerators can recover weighted sums after specialization; no claim is made that such general encodings are new. Historical work under weighted chromatic/Potts terminology could contain an equivalent cancellation theorem; literature comparison is bounded and independent mathematical audit has not been performed.

## References

1. D. D. Gebhard and B. E. Sagan, *A Noncommutative Chromatic Symmetric Function*, arXiv:math/9907076v1, first publicly submitted 1999-07-12, https://arxiv.org/html/math/9907076v1 (especially Sections 1 and 3).
2. A. D. Sokal, *Chromatic Polynomials, Potts Models and All That*, arXiv:cond-mat/9910503v1, first publicly submitted 1999-10-30, https://arxiv.org/html/cond-mat/9910503v1 (Sections 1–3).
3. *Exact Fourier sampling spectra and a thin-side conditioning transition for bipartite colourings*, published research record `2b34d08d2568`, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-fourier-sampling-spectra-and-a-thin-side-conditioning-tran--2b34d08d2568 (first-coordinate Gram result, not complete convolution support).
