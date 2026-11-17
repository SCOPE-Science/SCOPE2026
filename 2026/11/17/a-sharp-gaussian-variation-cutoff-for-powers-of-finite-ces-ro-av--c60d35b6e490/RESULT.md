# A sharp Gaussian variation cutoff for powers of finite Cesàro averaging

## Finding
Let \(n\ge2\), let \(C_n\) be the \(n\)-coordinate prefix-averaging matrix, and let \(V(x)=\sum_{i=1}^{n-1}|x_i-x_{i+1}|\). For every integer \(m\ge0\), the sharp operator seminorm \(L_{n,m}\) of \(C_n^m\) in \(V\) is exactly
\[
L_{n,m}=\Pr\{T_n>m\},\qquad T_n=1+\sum_{j=2}^n G_j,
\]
where the random variables \(G_j\) are independent, nonnegative-integer-valued, and have \(\Pr\{G_j=r\}=(j-1)/j^{r+1}\) for every integer \(r\ge0\). This gives the exact generating function
\[
\sum_{m=0}^\infty L_{n,m}z^m=\frac{1-z\prod_{j=2}^n\frac{j-1}{j-z}}{1-z},\qquad |z|<1.
\]
For every \(m\ge1\), the only nonconstant norm-attaining real inputs, modulo addition of constants and multiplication by nonzero scalars, are the first-coordinate spike \((1,0,\ldots,0)\).

Set \(\mu_n=1+\sum_{r=1}^{n-1}1/r\) and \(s_n^2=\sum_{r=1}^{n-1}(1/r+1/r^2)\). If \(\Phi\) is the standard normal distribution function, then, with an absolute implicit constant,
\[
\sup_{m\in\mathbb Z_{\ge0}}\left|L_{n,m}-\left[1-\Phi\left(\frac{m-\mu_n}{s_n}\right)\right]\right|=O\!\left((\log n)^{-1/2}\right)\quad(n\to\infty).
\]
In particular, for every fixed real \(u\), with \(m_n(u)=\lfloor\mu_n+u s_n\rfloor\), one has \(L_{n,m_n(u)}\to1-\Phi(u)\). Thus the exact finite-section contraction exhibits a Gaussian cutoff centered at \(\log n\) iterations with window width \(\sqrt{\log n}\), rather than a dimension-independent geometric rate.

## Assumptions and scope
The dimension \(n\) is a finite integer at least two, \(m\) is a nonnegative integer, and all inputs are real. The matrix is defined by
\[
(C_nx)_i=\frac1i\sum_{j=1}^i x_j\quad(1\le i\le n).
\]
The seminorm \(V\) is the unweighted total variation on the ordered path \(1,\ldots,n\); its nullspace consists of constant vectors. Operator seminorms are taken on the quotient by constants:
\[
L_{n,m}=\sup_{V(x)>0}\frac{V(C_n^mx)}{V(x)}.
\]
The geometric variables are specified by their probability mass functions above; they do **not** denote geometric waiting times with the alternative support convention starting at one. The cutoff statement lets both dimension and iteration count tend to infinity together.

## Proof
**Step 1: sharp path-variation reduction.** For \(1\le t<n\), put \(u^{(t)}=(\underbrace{1,\ldots,1}_{t},0,\ldots,0)\). Every input admits the exact decomposition
\[
x=x_n\mathbf1+\sum_{t=1}^{n-1}(x_t-x_{t+1})u^{(t)},\qquad V(x)=\sum_{t=1}^{n-1}|x_t-x_{t+1}|.
\]
The matrix \(C_n\) is positive, fixes constants, and preserves nonincreasing vectors, because a prefix average never falls below the next term of a nonincreasing sequence. Therefore \(C_n^m u^{(t)}\) is nonincreasing, has first coordinate one, and
\[
V(C_n^m u^{(t)})=1-(C_n^m u^{(t)})_n=1-\sum_{j=1}^t(C_n^m)_{nj}.
\]
The entries are nonnegative, so the largest value over the path-step basis occurs at \(t=1\). Applying the triangle inequality to the displayed decomposition, and taking \(x=u^{(1)}\) for equality, yields
\[
L_{n,m}=1-(C_n^m)_{n1}.
\]
For \(m\ge1\), every entry \((C_n^m)_{nj}\) is strictly positive (already \(C_n\) has positive entries in its last row). Consequently all \(t>1\) have a strictly smaller step ratio, and equality in the upper bound forces \(x_t=x_{t+1}\) for all \(t>1\). This proves the stated rigidity, including \(n=2\). At \(m=0\), \(L_{n,0}=1\) but rigidity is not asserted.

**Step 2: an absorbing chain and exact factorization.** Treat \(C_n\) as the transition matrix of the downward Markov chain that moves from state \(i\) uniformly to a state in \(\{1,\ldots,i\}\); state one is absorbing. Let \(T_i\) be the first hitting time of state one when started at \(i\), with \(T_1=0\), and let \(f_i(z)=\mathbb E z^{T_i}\). For \(i\ge2\), first-step conditioning gives
\[
f_i(z)=\frac z i\sum_{j=1}^i f_j(z).
\]
The base is \(f_2(z)=z/(2-z)\). Subtracting the equations for successive \(i\ge3\) gives \((i-z)f_i(z)=(i-1)f_{i-1}(z)\), hence
\[
f_n(z)=z\prod_{j=2}^n\frac{j-1}{j-z}.
\]
Since \((j-1)/(j-z)\) is the probability-generating function of \(G_j\), equality of generating functions proves \(T_n\stackrel{d}{=}1+\sum_{j=2}^nG_j\). Because state one is absorbing, \((C_n^m)_{n1}=\Pr\{T_n\le m\}\). Combining with Step 1 proves the finite norm and geometric-tail formulas. Summing \(\sum_{m=0}^{T_n-1}z^m\) proves the displayed norm generating function.

**Step 3: the Gaussian cutoff.** The geometric moments are
\[
\mathbb EG_j=\frac1{j-1},\qquad\operatorname{Var}(G_j)=\frac{j}{(j-1)^2}.
\]
Thus \(\mathbb ET_n=\mu_n\) and \(\operatorname{Var}(T_n)=s_n^2=\sum_{r=1}^{n-1}(1/r+1/r^2)\). In particular \(s_n^2=\log n+O(1)\). Direct geometric-moment formulas give \(\mathbb E|G_j-\mathbb EG_j|^3=O(1/j)\), with an absolute constant, uniformly for \(j\ge2\). The sum of these third absolute moments is \(O(\log n)\). The Berry–Esseen inequality for independent, not necessarily identically distributed summands therefore yields
\[
\sup_{v\in\mathbb R}\left|\Pr\{(T_n-\mu_n)/s_n\le v\}-\Phi(v)\right|
\le C\frac{\sum_{j=2}^n\mathbb E|G_j-\mathbb EG_j|^3}{s_n^3}
=O\!\left((\log n)^{-1/2}\right).
\]
Substitution \(v=(m-\mu_n)/s_n\) proves the uniform norm approximation. The floor in \(m_n(u)\) changes its standardized argument by at most \(1/s_n\), establishing the asserted Gaussian cutoff profile.

## Verification
The supplied `verify_cesaro.py` uses exact fractions to compare the matrix-entry formula, geometric-tail convolution, and every step norm for dimensions two through ten and iteration counts zero through nine. It separately checks general signed-grid inputs on dimensions two through seven and moments/generating functions. All these diagnostics passed. The infinite-dimensional-index limit and the universal bounds rely on the analytic argument above, not on finite computation.

## Relationship to prior work
Akhmedov and Başar (2008, Theorem 3.1) computed the norm and spectrum of the infinite Cesàro operator on bounded-variation sequence spaces. That result is in a different normed setting: constants are controlled by an initial-coordinate term, and it does not give the exact finite path-seminorm powers or their growing-dimension mixing window. Adell and Lekuona (electronically published October 22, 2009) obtained integral/binomial-mixture representations for powers of the discrete Cesàro operator and sharp fixed-space sup-norm iteration estimates. In particular their Proposition 2.3 supplies a representation of matrix entries related to the present \(\Pr\{T_n\le m\}\); that background is acknowledged as prior. It does not state the exact finite path-variation norm, unique extremizer directions, independent-geometric hitting-time factorization, or sharp joint \(n,m\) Gaussian variation cutoff. Earlier summability/spectral results may implicitly encode portions of the transition law; the present originality assertion is restricted to the combined path-variation theorem and joint Gaussian cutoff, not to the definition or classical analysis of the Cesàro operator itself.

## Limitations
The result concerns uniform prefix averaging on finite linearly ordered coordinates and unweighted adjacent-edge variation. It does not assert the same cutoff for weighted Cesàro matrices, other graph variations, finite sections with different boundary conventions, or arbitrary Banach norms. The exact hitting law follows from a known triangular averaging kernel; an unindexed earlier equivalent cutoff under Markov-chain or combinatorial terminology remains a publication-priority risk. The finite tests cannot prove the all-dimension result; that result follows from the written proof.

## References
1. J. A. Adell and A. Lekuona, “Rates of convergence for the iterates of Cesàro operators,” *Proceedings of the American Mathematical Society* **138** (2010), 1011–1021, electronically published 2009-10-22, DOI: 10.1090/S0002-9939-09-10127-2. Author-uploaded full-text transcription: https://www.researchgate.net/publication/243067145_Rates_of_convergence_for_the_iterates_of_Cesaro_operators .
2. A. M. Akhmedov and F. Başar, “The Fine Spectra of the Cesàro Operator \(C_1\) over the Sequence Space \(bv_p\),” *Mathematical Journal of Okayama University* **50** (2008), 135–147, DOI: 10.18926/mjou/33130. Publisher full text: https://ousar.lib.okayama-u.ac.jp/files/public/3/33130/20160528030811158559/fulltext.pdf .
