# Infinite two-sided commutator inertia of compact power-decaying Rhaly operators

## Finding

**Theorem.** Let \(s>1\) and let \((a_n)_{n\geq0}\) be a strictly positive real sequence such that
\[
\frac{a_{n+1}}{a_n}=1-\frac{s}{n+1}+O((n+1)^{-2})\quad(n\to\infty).
\]
Define the Rhaly (terraced) operator on complex \(\ell^2(\mathbb N_0)\) by
\[
(R_a x)_n=a_n\sum_{k=0}^{n}x_k.
\]
Then \(R_a\) is Hilbert–Schmidt, and its self-commutator
\[
K_a=R_a^*R_a-R_aR_a^*
\]
is self-adjoint and trace class with trace zero. **Its strictly positive and strictly negative spectral subspaces are both infinite dimensional.** Equivalently, \(K_a\) has infinitely many eigenvalues of each sign, counted with multiplicity. In particular, the conclusion holds for every \(a_n=(n+\beta)^{-s}\), \(s>1\), \(\beta>0\).

## Assumptions and scope

The asymptotic error has a constant that may depend on the fixed positive sequence and on \(s\), but is uniform in all sufficiently large integer indices. No monotonicity of the first finitely many weights is needed. The coordinate vectors \(e_j\) and all inner products are those of complex \(\ell^2(\mathbb N_0)\). Eigenvalues are counted with their geometric (equivalently, algebraic) multiplicity because the commutator is compact self-adjoint. The result classifies **inertia**, not the magnitude or exact asymptotic distribution of those eigenvalues.

## Proof

**1. Weight asymptotics and compactness.** Write \(h=n+1\). Since
\[
\frac{(n+2)^sa_{n+1}}{(n+1)^sa_n}=1+O(h^{-2}),
\]
the logarithms of these successive ratios form a convergent series. Thus there exists \(c>0\) such that
\[
a_n=c(n+1)^{-s}(1+O((n+1)^{-1})).
\]
The squares of the matrix entries of \(R_a\) sum to \(\sum_{n\geq0}(n+1)a_n^2<\infty\), because \(s>1\). Hence \(R_a\in\mathcal S_2\), \(K_a\in\mathcal S_1\), and cyclicity of the trace for Hilbert–Schmidt products gives \(\operatorname{Tr}K_a=0\).

**2. Infinitely many negative directions.** Direct multiplication of the infinite triangular matrix gives, for all integers \(i,j\geq0\),
\[
\langle K_a e_j,e_i\rangle
=\sum_{n\geq\max(i,j)}a_n^2-(\min(i,j)+1)a_i a_j.
\tag{1}
\]
The tail sum is absolutely convergent. Consequently,
\[
\langle K_ae_j,e_j\rangle
= -\frac{2(s-1)c^2}{2s-1}(j+1)^{1-2s}(1+o(1))<0
\tag{2}
\]
for all sufficiently large \(j\). For fixed \(i\) and \(j\to\infty\), (1) gives \(\langle K_ae_j,e_i\rangle=O_i((j+1)^{-s})\). Since (2) has magnitude comparable to \((j+1)^{1-2s}\), the normalized off-diagonal ratio is
\[
\frac{|\langle K_ae_j,e_i\rangle|}
{\sqrt{|\langle K_ae_i,e_i\rangle|\,|\langle K_ae_j,e_j\rangle|}}
=O_i((j+1)^{-1/2})\longrightarrow0.
\tag{3}
\]
For any prescribed positive integer \(m\), recursively choose sufficiently large indices \(j_1<\cdots<j_m\) with negative diagonal, so that all normalized off-diagonal entries in the selected \(m\)-by-\(m\) Gram matrix have modulus smaller than \(1/(2m)\). The normalized negative of that matrix has diagonal entries one and off-diagonal row sums less than one; strict diagonal dominance makes it positive definite. Thus \(K_a\) has an \(m\)-dimensional negative definite subspace for every \(m\), proving infinite negative inertia.

**3. Infinitely many positive directions.** Define finitely supported second-difference vectors
\[
v_j=e_j-2e_{j+1}+e_{j+2},\qquad
\delta_j=a_j-2a_{j+1}+a_{j+2}.
\]
Because their coordinate sums vanish,
\[
R_av_j=a_je_j-a_{j+1}e_{j+1}.
\]
The adjoint acts as
\[
R_a^*v_j=\delta_j\sum_{k=0}^{j}e_k+
(-2a_{j+1}+a_{j+2})e_{j+1}+a_{j+2}e_{j+2}.
\]
Thus their exact commutator quadratic forms are
\[
q_j:=\langle K_av_j,v_j\rangle
=a_j^2+a_{j+1}^2-(j+1)\delta_j^2
-(-2a_{j+1}+a_{j+2})^2-a_{j+2}^2.
\tag{4}
\]
The ratio hypothesis yields
\[
\begin{aligned}
 a_{j+1}/a_j&=1-s/(j+1)+O((j+1)^{-2}),\\
 a_{j+2}/a_j&=1-2s/(j+1)+O((j+1)^{-2}),\\
 \delta_j&=O(a_j(j+1)^{-2}),\\
 -2a_{j+1}+a_{j+2}&=-a_j+O(a_j(j+1)^{-2}).
\end{aligned}
\]
Substituting into (4) gives the strictly positive leading term
\[
q_j=\frac{2s\,a_j^2}{j+1}\bigl(1+O((j+1)^{-1})\bigr)>0
\tag{5}
\]
for all sufficiently large \(j\).

For \(j>i+2\), the supports of \(R_av_i\) and \(R_av_j\) are disjoint; the first \(i+3\) coefficients of \(R_a^*v_j\) are all \(\delta_j\). Hence the *exact* cross-term is
\[
\langle K_av_j,v_i\rangle=-\delta_j B_i,
\quad B_i=(i+1)\delta_i+2(a_{i+2}-a_{i+1}).
\tag{6}
\]
For each fixed \(i\), using (5) and \(\delta_j=O(a_j(j+1)^{-2})\),
\[
\frac{|\langle K_av_j,v_i\rangle|}{\sqrt{q_iq_j}}
=O_i((j+1)^{-3/2})\longrightarrow0.
\tag{7}
\]
Choose any number \(m\) of widely spaced indices \(i_1<\cdots<i_m\), all with \(q_{i_k}>0\), separated by at least three, and recursively small enough normalized cross-terms (less than \(1/(2m)\)). The normalized Gram matrix \((\langle K_av_{i_l},v_{i_k}\rangle/\sqrt{q_{i_k}q_{i_l}})\) is strictly diagonally dominant with positive diagonal, hence positive definite. The \(v_{i_k}\) have disjoint supports, so their span is \(m\)-dimensional. Thus positive inertia is also infinite.

**4. Spectral conclusion.** As \(K_a\) is compact self-adjoint, its positive and negative definite subspaces cannot have dimensions exceeding the numbers of positive and negative eigenvalues respectively. Since both subspace dimensions are unbounded, the two eigenvalue counts are infinite. This finishes the proof.

## Verification

The standalone `checker.py` is executable with Python 3 and `mpmath`. It checks 182 finite or high-precision assertions, including the sign and coefficient of (2) and (5), exact rational checks of (4), and strict positive/negative definiteness of four-dimensional widely spaced Gram matrices for power-law weights. Run:

```bash
python checker.py
```

Expected output begins with `PASS 182 finite/high-precision diagnostics`. Equations (1), (4), and (6) follow from the displayed exact finite-support actions. The proof of the infinite-dimensional statement uses the uniform asymptotic estimates (3), (5), and (7), **not** extrapolation from the numerical examples.

## Relationship to prior work

Gallardo-Gutiérrez and Partington (arXiv:2408.03182, publicly submitted 6 August 2024) explicitly identify the positive-power Rhaly matrices with \(s>1\) as compact and nonhyponormal. Nonhyponormality detects **at least one negative direction**, but neither determines the infinite negative index nor establishes an infinite positive index. Their main theorems instead concern the spectrum of \(R_a\) itself and invariant subspaces. The subsequent Bellavita–Dellepiane–Stylogiannis work (arXiv:2503.21930) characterizes boundedness, compactness, and Schatten membership of \(R_a\), not the signed eigenvalue multiplicities of its self-commutator. These known results are not claimed as new here.

The classical Cesàro row sequence \(a_n=(n+1)^{-1}\) lies at the **excluded** endpoint \(s=1\); its operator is known to be subnormal and therefore hyponormal. Hence the two-sided commutator-sign phenomenon is a qualitative contrast with the canonical endpoint. No assertion about arbitrary sequences at \(s=1\) is made.

## Limitations

The theorem requires positive weights with a second-order remainder in the specified ratio. It does not cover arbitrary regularly varying sequences whose successive ratios have only an \(o(1/n)\) remainder, nor sequences with complex phases. It proves infinite eigenvalue multiplicity on both sides of zero but neither a quantitative Weyl law nor a sharp norm bound. As with any literature comparison, inaccessible or unindexed earlier proofs of an equivalent signed-inertia result remain a priority risk; independent validation of the proof has not been performed.

## References

1. E. A. Gallardo-Gutiérrez and J. R. Partington, *Rhaly operators: more on generalized Cesàro operators*, arXiv:2408.03182 (first public version 2024-08-06), https://arxiv.org/abs/2408.03182.
2. C. Bellavita, E. Dellepiane and G. Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930 (2025), https://arxiv.org/abs/2503.21930.
3. H. C. Rhaly, Jr., *Terraced matrices*, Houston J. Math. **15** (1989), 137–146, as discussed and cited in Reference 1.
4. A. Brown, P. R. Halmos and A. L. Shields, *Cesàro operators*, Acta Sci. Math. (Szeged) **26** (1965), 125–137, as cited in Reference 1.
