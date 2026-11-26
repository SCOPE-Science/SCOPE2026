# Critical dyadic holes for negative doubling: exact survival laws and an entropy onset

## Finding

For the negative-doubling circle map \(T(x)=-2x\pmod 1\), remove the centered open hole
\[
H_m=\left(\frac12-2^{-m},\frac12+2^{-m}\right),\qquad m\in\mathbb Z,\ m\ge2.
\]
Let \(S_m\) be the set of points whose forward orbit never enters \(H_m\), and let \(a_L(m)\) count length-\(L\) words in the full-branch symbolic language that avoid the two length-\(m\) forbidden cylinders defined below. The symbolic language includes standard one-sided endpoint completions. Then, with \(a_0(m)=1\),
\[
\sum_{L\ge0}a_L(m)z^L=\frac{1+z^{m-1}}{1-2z+z^{m-1}}. \tag{1}
\]
The entropy of the surviving dynamics and its Euclidean Hausdorff dimension are
\[
h_m=\log\lambda_m,\qquad \dim_{\mathrm H}S_m=\frac{\log\lambda_m}{\log2},\tag{2}
\]
where \(\lambda_2=\lambda_3=1\), and for \(m\ge4\), \(\lambda_m\in(1,2)\) is uniquely determined by
\[
\sum_{j=1}^{m-2}\lambda_m^{-j}=1
\quad\Longleftrightarrow\quad
\lambda_m^{m-2}(2-\lambda_m)=1.\tag{3}
\]
In particular, this natural dyadic sequence has zero survivor entropy at \(m=2,3\), and strictly positive entropy at every \(m\ge4\). At \(m=4\), \(\lambda_4=(1+\sqrt5)/2\).

For Lebesgue-distributed initial conditions and every integer \(n\ge1\), the exact probability of avoiding the hole on the first \(n\) iterates (times \(0,\ldots,n-1\)) is
\[
\mathbb P(\tau_{H_m}\ge n)=\frac{a_{n+m-1}(m)}{2^{n+m-1}}.\tag{4}
\]
Consequently, the escape rate exists and equals \(\gamma_m=\log(2/\lambda_m)\). Set \(q_m=|H_m|=2^{1-m}\). As \(m\to\infty\),
\[
\boxed{\gamma_m=q_m+\left(\log_2\frac1{q_m}-\frac12\right)q_m^2+O\!\left(q_m^3\log^2\frac1{q_m}\right).}\tag{5}
\]
The coefficient of the first logarithmically enhanced correction is exactly one on this shrinking-hole sequence. This numerical coefficient and the exact dyadic formulas are the conclusions here; the existence of logarithmically enhanced corrections for other expanding circle-map holes is prior knowledge.

## Assumptions and scope

We use the circle \(\mathbb R/\mathbb Z\), normalized Lebesgue probability, and the standard two equal-length monotonicity branches of \(T\), separated at \(1/2\). We code an orbit by \(s_i=0\) for \(T^i(x)\in(0,1/2)\) and \(s_i=1\) for \(T^i(x)\in(1/2,1)\). Points ever hitting a coding boundary are a countable exceptional set; for exact Lebesgue probabilities they have zero measure, and for Hausdorff dimension they have dimension zero. Both endpoints of the open hole are retained when their subsequent forward trajectories avoid the hole; these exceptional endpoint itineraries do not affect equations (2)–(5). Formula (1) refers to the completed full-branch symbolic language of the corresponding forbidden-word subshift; at the degenerate depth \(m=2\), its two infinite alternating codes describe the single surviving circle endpoint rather than two interior survivors. The coding conventions do not change entropy, dimension or Lebesgue survival. The open-hole endpoints are not claimed to be open cylinders.

The first-entrance time is \(\tau_{H_m}=\min\{j\ge0:T^j(x)\in H_m\}\), with infinity allowed. Formula (4) uses \(\tau_{H_m}\ge n\) and so tests exactly \(n\) positions. Its value at \(n=0\) is one separately.

## Proof

**1. Geometry of the hole and forbidden words.** Each inverse branch of \(T\) is affine with slope modulus \(1/2\); away from dyadic boundaries, the map from a length-\(m\) symbolic word to its cylinder is bijective onto one open dyadic cell of width \(2^{-m}\). Direct iteration on the two adjacent cells immediately to the left and right of \(1/2\) gives the branch itineraries
\[
w_m=00\,1010\cdots\quad\text{(first \(m\) symbols)},\qquad
\bar w_m=11\,0101\cdots\quad\text{(first \(m\) symbols)}.
\]
The hole is exactly the union of the interiors of these two adjacent cells, except for the finite collection of dyadic endpoints. Thus a generic orbit avoids the hole precisely when its infinite symbolic itinerary avoids both length-\(m\) factors \(w_m\) and \(\bar w_m\).

**2. Defect coding and a renewal recurrence.** Define the equality-defect indicator of a binary sequence by \(d_i=1\) if \(s_i=s_{i+1}\) and \(d_i=0\) otherwise. Given \(s_0\), this transformation is bijective, since each next symbol is determined from its predecessor and the defect. A length-\(m\) factor is either of the forbidden types exactly when its \(m-1\) consecutive defects equal \(10^{m-2}\). Therefore the allowed defect language consists of binary strings avoiding \(10^r\), where \(r=m-2\).

Let \(b_N(r)\) count binary strings of length \(N\) avoiding \(10^r\). For \(N\ge1\), either the entire string is zero, or its final \(1\) is followed by exactly \(j-1\) zeros for some \(1\le j\le r\). The prefix before that final \(1\) is an arbitrary allowed word of length \(N-j\). This gives
\[
b_0(r)=1,\qquad b_N(r)=1+\sum_{j=1}^{r} b_{N-j}(r),\tag{6}
\]
with \(b_k(r)=0\) for \(k<0\). In the degenerate case \(r=0\), the unique allowed defect word is all zeros. Summing (6) for \(r\ge1\) gives
\[
B_r(z)=\sum_{N\ge0}b_N(r)z^N=\frac1{1-2z+z^{r+1}}.
\]
For each defect word, there are two choices of initial symbol, hence \(a_0=1\) and \(a_L=2b_{L-1}\) for \(L\ge1\). This proves (1), including \(r=0\) by direct substitution. Every finite allowed word admits an infinite continuation: append defects all equal to one, with the obvious all-zero continuation in the case \(r=0\).

**3. Entropy and dimension.** For \(r=0\), all sequences have alternating symbols; for \(r=1\), the defect sequence avoids \(10\) and is therefore a block of zeros followed by a block of ones. In both cases \(a_L\) grows at most linearly and entropy vanishes. For \(r\ge2\), the recurrent component of the defect shift is the primitive finite-state renewal graph whose successive ones are separated by \(1,\ldots,r\) steps. Its Perron root is the unique \(\lambda\in(1,2)\) solving \(\sum_{j=1}^{r}\lambda^{-j}=1\). The all-zero defect orbit is an additional zero-entropy component and does not change the growth rate. The twofold binary extension has the same entropy, establishing (2) for entropy and (3).

For the dimension assertion, depth-\(L\) cylinders have diameter \(2^{-L}\) and disjoint interiors; their number grows with exponential rate \(\lambda_m\). This gives the dimension upper bound. For \(m\ge4\), a Perron eigenvector on the primitive renewal graph supplies a shift-invariant Markov probability whose cylinder masses are bounded by \(C\lambda_m^{-L}\). Transporting it through the two inverse branches and comparing a Euclidean interval of radius \(2^{-L}\) with at most a bounded number of length-\(L\) dyadic cylinders gives the Frostman lower bound \(\log\lambda_m/\log 2\). For \(m=2,3\), the polynomial word counts give dimension zero by covers. A countable collection of coding endpoints does not change Hausdorff dimension. This proves the remaining statement of (2).

**4. Exact finite-time survival.** Lebesgue measure assigns equal probability \(2^{-L}\) to each word of length \(L\), because \(T\) has two full affine branches of slope modulus two. Avoiding the length-\(m\) forbidden factors at times \(0,\ldots,n-1\) is equivalent to avoiding them within the first \(n+m-1\) symbols. Equation (4) follows. Its exponential decay rate is \(\log2-\log\lambda_m\), including the polynomial-growth cases \(m=2,3\).

**5. Exact small-hole equation and sharp expansion.** For \(m\ge4\), let \(t_m=1-\lambda_m/2\) and \(q_m=2^{1-m}\). Equation (3) becomes the exact relation
\[
t_m(1-t_m)^{m-2}=q_m.\tag{7}
\]
Since \((m-2)q_m\to0\), monotonicity of \(t(1-t)^{m-2}\) on a neighborhood of zero bounds its small solution by \(q_m\le t_m\le2q_m\) for all sufficiently large \(m\). Taylor expansion of (7), with remainder uniform because \((m-2)t_m\to0\), yields
\[
t_m=q_m+(m-2)q_m^2+O(m^2q_m^3).
\]
Using \(\gamma_m=-\log(1-t_m)=t_m+t_m^2/2+O(t_m^3)\) and \(m-1=\log_2(1/q_m)\) proves (5). There are no unverified infinite extrapolations in these steps.

## Verification

The accompanying standalone Python 3 script `VERIFY.py` reconstructs all depth-\(m\) cells with exact rational arithmetic for \(2\le m\le9\), verifies that the hole consists of the two claimed cylinders, compares full binary-word enumeration with the renewal recurrence through length 13, and checks the second-order expansion against high-precision roots for \(8\le m\le25\). Running `python3 VERIFY.py` returned `PASS: 1150 finite and high-precision diagnostics; the proof supplies the infinite statement.` These finite checks test the definitions and formula implementation; they are not the proof of the all-\(m\) claim.

## Relationship to prior work

Ding, Steiner and Sun (2026) develop symbolic admissibility and entropy plateaux for decreasing Lorenz maps and negative doubling with holes around the discontinuity. Their theorems are structural and qualitative, while (1)–(5) give an explicit parameter-uniform family, a sharp zero-to-positive entropy onset, exact Lebesgue survival for every finite time, and a quantified shrinking-hole correction.

Cheriyath and Agarwal (2019/2022) give a general correlation-polynomial method for subshifts with finitely many forbidden cylinders; their result already implies rationality of the generating function and the general entropy-versus-escape-rate identity. The method is not claimed as new. The exact defect conjugacy and explicit all-level specialized law are the object of the present classification; priority over other specializations is not independently established.

Lu, Steiner and Zou (2025/2026) give a broad entropy-and-dimension framework for binary shifts with holes, not a stated all-depth survival law for this negative-doubling sequence.

Dettmann (2011/2013) obtains logarithmically enhanced second-order corrections for escape through small holes in the positively oriented doubling map, primarily with holes based at zero. Thus logarithmic enhancement is known; the result here gives the exact coefficient along a different, negative-doubling, symmetric central family and joins it to all-level language and dimension data. General overlap-polynomial machinery may independently recover this family; that is a residual priority risk.

## Limitations

The formulas concern exactly this centered dyadic sequence, rather than every symmetric hole. They do not assert a global critical hole parameter between the sampled radii or any new general escape-rate principle. For a circle model with a discontinuity at \(1/2\) the value assigned to the discontinuity itself is irrelevant to escape because it lies in every hole. Endpoint coding conventions affect only exceptional zero-dimensional sets, not the stated measures, entropy or Hausdorff dimensions. A published result specialized to precisely these complementary forbidden words might predate this treatment; no independent priority review has occurred.

## References

1. Y. Ding, W. Steiner, Y. Sun, *Open dynamical systems in topologically expansive decreasing Lorenz maps*, arXiv:2610.03327, first posted 2026-10-02. https://arxiv.org/abs/2610.03327
2. H. Cheriyath, N. Agarwal, *Subshifts of Finite Type with a Hole*, arXiv:1905.11767, first posted 2019-05-28; Journal of the Australian Mathematical Society (2022). https://arxiv.org/abs/1905.11767
3. C. P. Dettmann, *Open circle maps: Small hole asymptotics*, arXiv:1112.5390, first posted 2011-12-22; Nonlinearity 26 (2013), 307–317. https://arxiv.org/abs/1112.5390
4. J. Lu, W. Steiner, Y. Zou, *Hausdorff dimension of double base expansions and binary shifts with a hole*, arXiv:2509.04227, first posted 2025-09-04. https://arxiv.org/abs/2509.04227
