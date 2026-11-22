# A quadratic fixed-point staircase and universal boundary distribution in a three-dimensional modular logistic map

## Finding

The three-dimensional *simple intertwining logistic* map has an exactly solvable invariant boundary face. The number of fixed points on this face grows by an arithmetic staircase, with a continuum of equilibria at one resonance, and their spatial distribution has a universal nonuniform limit.

Write \(\{t\}=t-\lfloor t\rfloor\) and \(K=64\mu\). Zhao and Ma's map is
\[
\begin{aligned}
U&=\{K v(1-u)+w\},\\
V&=\{K v+w(1+U^2)\},\\
W&=\{(K/64)(64+U+V)(w-w^3/6)\},\\
T_K(u,v,w)&=(U,V,W).
\end{aligned}
\]
Its state space is the half-open cube \(Q=[0,1)^3\). The face \(\Sigma=\{(u,v,0):0\le u,v<1\}\) is invariant. **The complete fixed-point classification on \(\Sigma\)** is as follows.

- For \(0<K<1\), the only fixed point on the face is \((0,0,0)\).
- For \(K=1\), the face-fixed set is the continuous curve \(\{(v/(1+v),v,0):0\le v<1\}\).
- For \(K>1\), let \(J_K=\{j\in\mathbb Z:0\le j<K-1\}\). The distinct face-fixed points are exactly
  \[
  (u_{j,m},v_j,0),\quad v_j=\frac{j}{K-1},\quad
  u_{j,m}=\frac{K v_j-m}{1+K v_j},\quad
  j\in J_K,\quad m=0,\ldots,j.
  \]
  Their number is
  \[
  \boxed{N_\Sigma(K)=\frac{\lceil K\rceil(\lceil K\rceil-1)}2.}
  \]
  Immediately above each integer \(K=r\ge2\), exactly \(r\) new fixed points appear from the excluded boundary \(v=1\); at the integer itself they are not in the half-open state space.

Every nonzero face-fixed point for \(K>1\) has all three eigenvalues of the appropriate one-sided smooth local branch outside the closed unit disk. The origin's one-sided multipliers are \(0,K,K\). For example \(\mu=1\) yields \(2016\) face-fixed points, while the published parameter range \(0<\mu\le3.999\) allows \(32640\) when \(255<K\le255.936\).

There is also an exact spatial limit under the natural formal continuation of the same formula to arbitrarily large gains. For integer \(K=r\ge2\), put equal probability mass on the \(N_\Sigma(r)\) pairs \((u_{j,m},v_j)\). Call this measure \(\eta_r\). With the \(\ell^1\) distance on \([0,1]^2\),
\[
\boxed{W_1\bigl(\eta_r,\,2v\,du\,dv\bigr)\le \frac6{r-1}.}
\]
Thus the asymptotic face-fixed-point density is \(2v\), uniform in the \(u\) coordinate but increasing linearly in the \(v\) coordinate.

## Assumptions and scope

All arithmetic is exact real arithmetic, with reduction modulo one defined by the fractional-part convention above. Fixed points mean literal fixed states in \([0,1)^3\), not equivalence classes under a quotient-circle topology. At jumps, the half-open convention is essential. The map studied by Zhao and Ma uses \(0<\mu\le3.999\) (hence \(0<K\le255.936\)). The asymptotic statement for \(r\to\infty\) is an explicit mathematical continuation of the same algebraic family outside that experimental parameter limit, not a claim about the parameter bounds used in the paper. All fixed-point counts here are **on \(w=0\) only**; no full three-dimensional census is asserted. One-sided multipliers refer to approaching the invariant face from the positive \(w\) side, on branches without crossing a fractional-part discontinuity.

## Proof

**1. Invariance and scalar arithmetic.** When \(w=0\), the third coordinate is zero and the first two satisfy \(U=\{K v(1-u)\}\) and \(V=\{K v\}\). A fixed point therefore obeys \(v=\{K v\}\), or \((K-1)v=j\) for some integer \(j\). Because \(0\le v<1\) and \(K>0\), the right-hand-side integer is nonnegative. For \(K<1\), the left side is nonpositive and vanishes only when \(v=0\), whence \(u=0\). For \(K=1\), any \(v\in[0,1)\) satisfies the second fixed-point equation, while the first is \(u=v(1-u)\) without a wrap (its argument is less than one), giving \(u=v/(1+v)\). For \(K>1\), the integer condition is exactly \(0\le j<K-1\) with \(v=v_j=j/(K-1)\).

**2. Exact first-coordinate solutions and count.** For any such \(j\), put \(y=K v_j=j+v_j\). The first coordinate equation is \(u=\{y(1-u)\}\), equivalent to \(y(1-u)=m+u\) for a nonnegative integer \(m\). Thus \(u=(y-m)/(1+y)\). Since \(j\le y<j+1\), the condition \(0\le u<1\) holds exactly for \(m=0,\ldots,j\). These \(j+1\) points are distinct. There are \(\lceil K\rceil-1\) eligible rows \(j\), counting \(j=0\), and summation of \(j+1\) gives the claimed triangular number. When \(K\) crosses upward from an integer \(r\), row \(j=r-1\) enters from \(v=1\), bringing \(r\) points with limiting first coordinates \((r-m)/(r+1)\), \(m=0,\ldots,r-1\). The row does not exist at \(K=r\).

**3. One-sided local spectrum.** At a nonzero face-fixed state, both positive-output fractional-part operations select locally smooth branches. Differentiating the expressions before fractional-part reduction, at \(w=0\) and on the positive-\(w\) side, yields the upper-triangular Jacobian
\[
J=\begin{pmatrix}
-Kv_j&K(1-u_{j,m})&1\\
0&K&1+u_{j,m}^2\\
0&0&K\bigl(1+(u_{j,m}+v_j)/64\bigr)
\end{pmatrix}.
\]
For \(j\ge1\), \(Kv_j=j+v_j>1\), \(K>1\), and the last diagonal entry exceeds \(K\); therefore all three one-sided eigenvalues have modulus greater than one. At the origin, the positive-domain branch has diagonal entries \(0,K,K\); when \(K<1\) these have moduli below one, though the modulus statement alone is not used to claim global attraction. The ordinary smooth Jacobian across modular discontinuity surfaces is not asserted to exist.

**4. Spatial law.** Let \(K=r\ge2\) be an integer and write \(h=1/(r-1)\). The rows are \(j=0,\ldots,r-2\), at \(v_j=jh\), and contain \(j+1\) points. The row weights are \(a_j=(j+1)/N\) where \(N=r(r-1)/2\). Within row \(j\), relabel \(m+1=q\) to obtain
\[
u_{j,m}=1-\frac{q}{j+1+v_j},\qquad 1\le q\le j+1.
\]
Couple each point to \(1-q/(j+1)\). Their distance is at most \(1/(j+1)\). The latter equally spaced grid, with equal weights, can be coupled to the uniform law on \([0,1]\) at average cost at most \(1/[2(j+1)]\). Averaging rows, the cost of replacing their horizontal coordinates by independent uniform coordinates is at most
\[
\sum_{j=0}^{r-2}\frac{j+1}{N}\,\frac3{2(j+1)}=\frac3r.
\]
For the vertical marginal, the target density \(2v\,dv\) gives the bin \([jh,(j+1)h)\) mass \(b_j=(2j+1)h^2\), while the discrete row mass is \(a_j\). Direct arithmetic shows \(|a_j-b_j|\le h^2\), so the total variation distance between the discrete laws with weights \(a_j\) and \(b_j\) at \(v_j\) is at most \(h/2\). Quantizing the continuous target to those left endpoints costs at most \(h\). Therefore the vertical Wasserstein distance is at most \(3h/2\). By product coupling and the triangle inequality,
\[
W_1(\eta_r,2v\,du\,dv)\le 3/r+3/[2(r-1)]\le6/(r-1),
\]
as claimed. The proof does not use numerical extrapolation.

## Verification

The accompanying \(\texttt{verify.py}\) runs direct exact-rational substitution of every enumerated fixed state for 18 rational gain values, including \(K=64\), \(K=255\), and \(K=511/2\). It checks \(71115\) finite fixed states, \(71861\) exact assertions, five rational points on the \(K=1\) fixed curve, the nonzero one-sided multiplier inequalities, the triangular counts, and rational bin-mass inequalities for integer gains from \(2\) to \(39\). The source proof, not this finite test set, establishes the full parameter and asymptotic assertions. To reproduce: \(\texttt{python3 verify.py}\).

## Relationship to prior work

Zhao and Ma (2024, Equation (2), Sections 2.3–5) introduce the simple intertwining logistic map, explain its efficient implementation, and analyze its numerical bifurcation and random-sequence diagnostics. The exact invariant-face fixed-point staircase, resonance curve, one-sided multipliers, and limiting spatial law are not established there. Tian and Lu et al. (2017, Section 2.1) describe the earlier intertwining logistic map with a sine-based third-coordinate update. The earlier model shares the zero-third-coordinate boundary mechanism at equal gains, but its article gives a numerical S-box application rather than this exact classification. Consequently, the face subsystem is not novel by itself; the result is its quantitative classification for the published simplified family. In related modular-map literature, product-grid fixed-point counts for constant-gain triangular maps do not imply the variable-gain staircase or the triangular spatial density here.

## Limitations

The theorem covers only the invariant face \(w=0\), which is excluded by some published seed-generation rules using strictly positive coordinates. It makes no assertion about the number of interior fixed points, other invariant sets, typical interior orbits, cryptographic security, or floating-point implementations. Fractional-part discontinuities make the one-sided nature of local multipliers important. Only the finite-parameter count belongs to Zhao and Ma's stated range; the infinite-gain limit is for the natural mathematical extension. The literature comparison is a same-author mathematical review, not independent publication-priority certification; unindexed equivalent results are possible.

## References

1. W. Zhao and C. Ma, *Modification of Intertwining Logistic Map and a Novel Pseudo Random Number Generator*, Symmetry 16(2), 169 (2024), first published 2024-01-31. https://doi.org/10.3390/sym16020169 . Equation (2), Section 2.3; Sections 3–5.
2. Y. Tian, Z. Lu, et al., *Chaotic S-Box: Intertwining Logistic Map and Bacterial Foraging Optimization*, Mathematical Problems in Engineering 2017, 6969312 (first published 2017-11-15). https://doi.org/10.1155/2017/6969312 . Section 2.1.
