# Exact spin-word classification at a range-three Ising coexistence field

## Finding

Let \(n\ge7\), and let \(\sigma_i\in\{0,1\}\) be a binary word on a labeled ring, with indices modulo \(n\). Consider the range-three Hamiltonian
\[
E_n(\sigma;h)=J\sum_{i=0}^{n-1}\sum_{d=1}^3\mathbf1\{\sigma_i=\sigma_{i+d}\}-h\sum_{i=0}^{n-1}\sigma_i,\qquad J>0.
\]
At \(h=10J/3\) one has \(E_n\ge -nJ\). **A word attains the bound if and only if every cyclic run of ones has length three, and every cyclic run of zeros has length one or two**, with both symbols present. Equivalently, the equality words are precisely arbitrary cyclic concatenations of \(1110\) and \(11100\), with a unique decomposition into those blocks when block starts are interpreted as the first ones in their runs. In particular, all those blocks can be mixed in any order, and no other local pattern can realize the coexistence energy.

## Scope

Each of the \(2^n\) labeled configurations is distinct; rotations are not quotiented out. The chosen field couples to the number of ones, and the interaction penalty is equal at distances one through three. The claim is about saturation of the coexistence energy, not a classification at other fields or the actual minimizers at sizes unable to saturate it.

## Proof

For a triple of consecutive bits \((b_0,b_1,b_2)\), oldest first, let \(a=b_0+2b_1+4b_2\). Appending \(b\in\{0,1\}\) sends \(a\) to \(j=\lfloor a/2\rfloor+4b\). In units of \(J/3\), that arc contributes \(3\sum_{s=0}^2\mathbf1\{b_s=b\}-10b\) to the energy. Put
\[
(p_0,p_1,p_2,p_3,p_4,p_5,p_6,p_7)=(0,-3,-4,-9,-7,-10,-11,-12),
\qquad
q(a,b)=3\sum_{s=0}^2\mathbf1\{b_s=b\}-10b+3+p_a-p_j.
\]
Substitution gives the entire local defect table:

| \(a\) | \(q(a,0)\) | \(q(a,1)\) |
|---:|---:|---:|
|0|12|0|
|1|6|0|
|2|8|2|
|3|0|0|
|4|6|0|
|5|0|0|
|6|4|0|
|7|0|2|

Triples from a periodic word form a closed walk. The potential cancels around it, so \(3(E_n+nJ)/J\) is exactly the sum of its nonnegative local defects. An equality word must use only zero-defect arcs. State 0 has no incoming zero-defect arc and state 2 has no outgoing one, so neither occurs on such a closed walk. After their removal, every closed walk visits state 3, and its first return from 3 is either
\(3\to5\to6\to7\to3\), appending \(1110\), or \(3\to1\to4\to6\to7\to3\), appending \(01110\). The concatenation of these return words is cyclic; each return contributes the run \(111\) followed by one zero, with an additional zero just before a run when its return is the five-step one. This proves the necessity of the stated run constraints. Conversely, any cyclic word with the stated runs has a unique occurrence of triple \(110\) at each one-run's end (including the first following zero). Between such triples the word traverses precisely one of the two listed walks according to the zero-run length. All defects vanish, so the bound is attained. The run starts are intrinsic to the word, which proves the decomposition assertion without choosing an origin.

## Counting and fluctuation consequences

These are included as consequences and alternative derivations of transfer-matrix quantities, not as independent priority claims. With \(a\) blocks of length 4 and \(b\) of length 5, the occupation is \(3(a+b)\). Marking a block start gives \(n\binom{a+b}{a}\) choices of marked labeled configuration and each labeled word is counted \(a+b\) times. Thus the occupation polynomial for equality words is
\[
 P_n(y)=\sum_{4a+5b=n\,,\ a,b\ge0}\frac{n}{a+b}\binom{a+b}{a}y^{3(a+b)}.
\]
The representable lengths for \(n\ge7\) are \(8,9,10\) and every \(n\ge12\) (the four consecutive lengths \(12,13,14,15\) are representable, and one can add 4). At 7 and 11 the displayed sum is empty, not the polynomial of actual ground states.

For completeness, path counting gives \(P_n(y)=\operatorname{tr} B(y)^n\), with the six-state adjacency matrix weighted by \(y\) for appending a one. The only simple cycles have lengths 4 and 5, each with weight \(y^3\), and share vertices, so \(\det(I-zB(y))=1-y^3(z^4+z^5)\). The adjacency is primitive (the graph is strongly connected and the two lengths are coprime). Its Perron root \(\rho(y)\) is simple and obeys \(\rho^5=y^3(\rho+1)\). Analytic separation near \(y=1\) gives
\[
\log\frac{P_n(e^s)}{P_n(1)}=n\bigl(\ell(s)-\ell(0)\bigr)+O(\theta^n),\qquad \ell(s)=\log\rho(e^s),\quad 0<\theta<1,
\]
uniformly in a small complex neighborhood of zero: the trace is the sum of powers of all eigenvalues, and the ratio of each other eigenvalue to the separated Perron branch has modulus uniformly bounded below 1. Write \(\lambda=\rho(1)\), \(p_i=\lambda^{-i}\) for \(i=4,5\), and \(L=4p_4+5p_5\). Differentiating \(e^{3s}(e^{-4\ell(s)}+e^{-5\ell(s)})=1\) gives \(\mu=\ell'(0)=3/L\) and \(v=\ell''(0)=9p_4p_5/L^3\). Analytic differentiation gives the limits of mean and variance divided by \(n\), and taking \(s=iu/\sqrt{n}\) and canceling the linear term gives \((K_n-\mu n)/\sqrt n\Rightarrow\mathcal N(0,v)\) for the uniform equality law as \(n\to\infty\).

## Relationship to prior work

Zarubin and Kassan-Ogly [1] study the same field-dependent range-three model, its finite-volume trace and characteristic polynomial (Sec. II, Eqs. (2)–(4)), phase orders (Sec. III, Eqs. (25), (27)), and the coexistence entropy and residual magnetization (Eq. (56)). In their normalization \(s_i=2\sigma_i-1\), equal interactions are \(J_i=-1\) and their field is \(10/3\). In particular, their Eq. (4) already implies the weighted equality-state determinant: at dimensionless coupling \(K_i=-q\) and dimensionless field \(B=10q/3+\tfrac12\log y\), rescale each eigenvalue by \(e^{5q/3}y^{-1/2}\). At \(q\to\infty\) the normalized coefficient of degree four tends to \(-y^3\) from \(-2\cosh(2B)\), that of degree three tends to \(-y^3\) from the term with \(\sinh(2(K_2+K_3))\sinh(2K_3)\cosh B\), and the others vanish except the leading degree eight. The normalized trace projects onto equality configurations by the energy bound, giving the same nonzero eigenvalue equation and occupation counts. The contribution here is instead a configuration-level classification: the exact iff run constraint for every labeled ring, including arbitrary changes between the two pure patterns. Neither a list of pure periodic orders nor a field-marked trace resolves that criterion on individual words. The limiting mean density is the prior residual magnetization converted to occupied fraction.

## Reproducibility and limitations

The 16-entry integer defect table is an exact local certificate. The accompanying `verify.py` checks the tight arcs and enumerates finite-ring counts, which are supplementary to the all-ring closed-walk proof. No finite-temperature claim or assertion about sizes failing the equality bound is made.

[1] A. V. Zarubin and F. A. Kassan-Ogly, *Frustration and ordering in Ising chain in an external magnetic field with third-neighbor interactions*, arXiv:2206.06753 (2022), https://arxiv.org/abs/2206.06753.
